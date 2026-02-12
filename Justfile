##########################
# Tooling for Atom Tickets
# https://apidocs.atomtickets.com
##########################

# Set up the Python environment
setup:
    uv venv && uv sync
    @echo "activate: source ./.venv/bin/activate"

# Run tests
test:
    uv run pytest -v

# python linting checks
[script]
lint FILES=".":
    set +e
    exit_code=0

    if [ -n "${CI:-}" ]; then
        # CI mode: GitHub-friendly output
        uv run ruff check --output-format=github {{FILES}} || exit_code=$?
        uv run ruff format --check {{FILES}} || exit_code=$?

        uv run pyright {{FILES}} --outputjson > pyright_report.json || exit_code=$?
        jq -r \
            --arg root "$GITHUB_WORKSPACE/" \
            '
                .generalDiagnostics[] |
                .file as $file |
                ($file | sub("^\\Q\($root)\\E"; "")) as $rel_file |
                "::\(.severity) file=\($rel_file),line=\(.range.start.line),endLine=\(.range.end.line),col=\(.range.start.character),endColumn=\(.range.end.character)::\($rel_file):\(.range.start.line): \(.message)"
            ' < pyright_report.json
        rm pyright_report.json
    else
        # Local mode: regular output
        uv run ruff check {{FILES}} || exit_code=$?
        uv run ruff format --check {{FILES}} || exit_code=$?
        uv run pyright {{FILES}} || exit_code=$?
    fi

    if [ $exit_code -ne 0 ]; then
        echo "One or more linting checks failed"
        exit 1
    fi

atom_generate_client:
  # Generate into a temporary directory
  uvx openapi-python-client@latest generate \
    --path ./atom.yaml \
    --meta uv \
    --output-path generated-client \
    --overwrite

  # Replace the local package with the generated one
  rm -rf atom_client
  mv generated-client/atom_client .
  rm -rf generated-client

  # https://github.com/openapi-generators/openapi-python-client/pull/1213
  # only *some* of the API endpoints require a Z at the end of the ISO date
  fastmod --accept-all 'isoformat\(\)' 'isoformat(timespec="seconds")' -- atom_client

  # Fix regression in production_detail.py where date object doesn't support timespec
  fastmod --accept-all 'isoformat\(timespec="seconds"\)' 'isoformat()' -- atom_client/models/production_detail.py

# set publish permissions, update metadata, and protect master; all in one command
github_setup: github_enable_actions github_repo_permissions_create github_repo_set_metadata github_ruleset_protect_master_create

github_repo_set_metadata:
  gh repo edit \
    --description "$(jq -r '.description' metadata.json)" \
    --homepage "$(jq -r '.homepage' metadata.json)" \
    --add-topic "$(jq -r '.keywords | join(",")' metadata.json)"

github_enable_actions:
  gh api --method PUT repos/:owner/:repo/actions/permissions --field enabled=true

GITHUB_PROTECT_MASTER_RULESET := """
{
  "name": "Protect master from force pushes",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/master"],
      "exclude": []
    }
  },
  "rules": [
    {
      "type": "non_fast_forward"
    }
  ]
}
"""

_github_repo:
  gh repo view --json nameWithOwner -q .nameWithOwner

# TODO this only supports deleting the single ruleset specified above
github_ruleset_protect_master_delete:
  repo=$(just _github_repo) && \
    ruleset_name=$(echo '{{GITHUB_PROTECT_MASTER_RULESET}}' | jq -r .name) && \
    ruleset_id=$(gh api repos/$repo/rulesets --jq ".[] | select(.name == \"$ruleset_name\") | .id") && \
    (([ -n "${ruleset_id}" ] || (echo "No ruleset found" && exit 0)) || gh api --method DELETE repos/$repo/rulesets/$ruleset_id)

# adds github ruleset to prevent --force and other destructive actions on the github main branch
github_ruleset_protect_master_create: github_ruleset_protect_master_delete
  gh api --method POST repos/$(just _github_repo)/rulesets --input - <<< '{{GITHUB_PROTECT_MASTER_RULESET}}'

# Set GitHub Actions permissions for the repository to allow workflows to write and approve PR reviews
# This enables release-please to run without a personal access token
github_repo_permissions_create:
  repo_path=$(gh repo view --json nameWithOwner --jq '.nameWithOwner') && \
    gh api --method PUT "/repos/${repo_path}/actions/permissions/workflow" \
      -f default_workflow_permissions=write \
      -F can_approve_pull_request_reviews=true && \
    gh api "/repos/${repo_path}/actions/permissions/workflow"
