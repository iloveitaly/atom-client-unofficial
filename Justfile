##########################
# Tooling for Atom Tickets
# https://apidocs.atomtickets.com
##########################

atom_generate_client:
  uvx openapi-python-client@latest generate \
  --path ./atom.yaml \
  --meta poetry \
  --output-path atom-client \
  --overwrite

  # https://github.com/openapi-generators/openapi-python-client/pull/1213
  # only *some* of the API endpoints require a Z at the end of the ISO date
  cd atom-client && \
    fastmod --accept-all 'isoformat\(\)' 'isoformat(timespec="seconds")'
  # && fastmod --accept-all 'isoformat\(timespec="seconds"\)' 'isoformat(timespec="seconds") + "Z"' -- atom_client/api/default/get_partner_v_1_showtime_details_by_venue_venue_id.py
