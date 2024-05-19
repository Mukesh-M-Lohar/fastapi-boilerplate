#!/bin/bash

# PostgreSQL connection details
DB_USER=$POSTGRES_USER
DB_NAME=$PROJECT_DATABASE

# Prompt for password if not set in .env
if [ -z "$POSTGRES_PASSWORD" ]; then
  read -s -p "Enter PostgreSQL password for user $DB_USER: " DB_PASSWORD
  echo
fi

# Export password for use by psql
export PGPASSWORD=$POSTGRES_PASSWORD

# Create database
echo "Creating database $DB_NAME..."
psql -U "$DB_USER" --command="CREATE DATABASE $DB_NAME;" -d "postgres" --host "localhost"
psql -U "$DB_USER" --command="CREATE DATABASE "fastapi_test";" -d "postgres" --host "localhost"


# Unset the password variable
unset PGPASSWORD

echo "Database $DB_NAME created successfully!"
