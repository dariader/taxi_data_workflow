FROM python:3.10-alpine

RUN apt install wget
RUN pip install pandas sqlalchemy psycopg2 pyyaml

WORKDIR /app
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]