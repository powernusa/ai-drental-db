#!/bin/bash
set -e

echo "==> Starting automatic database restore..."

# give Postgres a moment
sleep 2

pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" /docker-entrypoint-initdb.d/dvdrental_3_db.tar

echo "==> Database restore completed."
