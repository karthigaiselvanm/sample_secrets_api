#!/bin/bash
# File: backup.sh
DB_USER="admin"
DB_PASSWORD="SuperSecretPassword123"
DB_NAME="mydatabase"

pg_dump -U $DB_USER -W $DB_PASSWORD $DB_NAME > backup.sql
