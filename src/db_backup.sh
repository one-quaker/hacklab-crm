#!/bin/sh
pg_dump --host=$POSTGRES_URL --dbname=$POSTGRES_DB --port=$POSTGRES_PORT --username=$POSTGRES_USER | gzip -c > "dump-db.gz"
