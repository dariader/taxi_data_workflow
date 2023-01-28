# Taxi data workflow

Here lies the code, that enables analysis, storage and possible maintenance of NYC taxi data. 

## Current state: 
Postgres db (in Docker) that is being updated by intestion script (`ingest_data.py`)

## How to run: 
0) Install Docker and Docker Compose
1) Create image using `Docker Compose` -- This will create db and launch ingestion script. Ingestion script uses `ingest_config.yaml` configuration as input. 
2) login to pgadmin `localhost:8080` 
