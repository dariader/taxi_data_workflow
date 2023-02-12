FROM python:3.10-alpine

WORKDIR /app
COPY requirements.txt requirements.txt

RUN apt install wget
RUN pip install -r requirements.txt
COPY ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]