#!/bin/bash
psql -U admin -h postgres-service -d delta_metadata -c "CREATE TABLE IF NOT EXISTS delta_logs (id SERIAL PRIMARY KEY, log TEXT);"
