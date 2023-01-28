#!/usr/bin/env python
# coding: utf-8
"""
This tool will download taxi data from the URL, define data type and save to pg database. Will use all entries from yaml.
Usage:
./ingest_data.py ingest_config
"""
import os
import sys
import yaml

from time import time

import pandas as pd
from sqlalchemy import create_engine
# todo:  add logger


def convert_to_timestamp(df):
    datetime_columns = df.filter(like="datetime").columns
    if len(datetime_columns) > 0:
        print(f'detected datetime columns {datetime_columns}')
        for col in datetime_columns:
            df[col] = pd.to_datetime(df[col])
    return df

def main(params):
    # todo: use and abstract class to parse args automatically
    user = params.get('user')
    password = params.get('password')
    host = params.get('host')
    port = params.get('port')
    db = params.get('db')
    table_name = params.get('table_name')
    url = params.get('url')

    # the backup files are gzipped, and it's important to keep the correct extension
    # for pandas to be able to open the file
    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df = convert_to_timestamp(df)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df.to_sql(name=table_name, con=engine, if_exists='append')

    while True:
        try:
            t_start = time()

            df = next(df_iter)
            df = convert_to_timestamp(df)

            df.to_sql(name=table_name, con=engine, if_exists='append')

            t_end = time()

            print('inserted another chunk, took %.3f second' % (t_end - t_start))

        except StopIteration:
            print("Finished ingesting data into the postgres database")
            break


if __name__ == '__main__':
    ingestion_list = yaml.safe_load(open(sys.argv[1]))
    for ingestion_item in ingestion_list.keys():
        params = ingestion_list.get(ingestion_item)
        print(f'Ingesting {ingestion_item}...')
        main(params)
    print('Ingestion finished')
