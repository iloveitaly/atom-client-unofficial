##########################
# Tooling for Atom Tickets
# https://apidocs.atomtickets.com
##########################

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

github_repo_set_metadata:
  gh repo edit \
    --description "$(jq -r '.description' metadata.json)" \
    --homepage "$(jq -r '.homepage' metadata.json)" \
    --add-topic "$(jq -r '.keywords | join(",")' metadata.json)"
