#!/bin/sh

set -e

while read -r p; do
  if [ -n "$p" ]; then
    export "${p?}"
  fi
done < "$ENV_FILE"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" --username="$POSTGRES_USER" dbname="$POSTGRES_DB" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

while read -r p; do
  if [ -n "$p" ]; then
    unset "$p"
  fi
done < "$ENV_FILE"

exec "$@"
