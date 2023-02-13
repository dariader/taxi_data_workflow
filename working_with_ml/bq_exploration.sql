CREATE OR REPLACE EXTERNAL TABLE `trips_data_all.vfh_data_ext`
OPTIONS (
  format = 'CSV',
  uris = ['gs://dtc_data_lake_taxiworkflow/*.csv.gz']
);

CREATE OR REPLACE TABLE `trips_data_all.vfh_data_simp` AS
SELECT * FROM  `trips_data_all.vfh_data_ext`;


CREATE OR REPLACE EXTERNAL TABLE `trips_data_all.vfh_data_pq`
OPTIONS (
  format = 'parquet',
  uris = ['gs://dtc_data_lake_taxiworkflow/*.parquet']
);


CREATE OR REPLACE TABLE `trips_data_all.vfh_data_pq_simp` AS
SELECT * FROM  `trips_data_all.vfh_data_pq`;



-- What is the count for fhv vehicle records for year 2019?
SELECT COUNT(1) from `trips_data_all.vfh_data_simp`;

-- Write a query to count the distinct number of affiliated_base_number for the entire dataset on both the tables.
-- What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?
SELECT COUNT(DISTINCT(affiliated_base_number)) from `trips_data_all.vfh_data_simp`;
SELECT COUNT(DISTINCT(affiliated_base_number)) from `trips_data_all.vfh_data_ext`;


-- How many records have both a blank (null) PUlocationID and DOlocationID in the entire dataset?
SELECT COUNT(1) from `trips_data_all.vfh_data_simp` where PUlocationID is null and DOlocationID is null;

-- What is the best strategy to optimize the table if query always filter by pickup_datetime and order by affiliated_base_number?
CREATE OR REPLACE TABLE `trips_data_all.vfh_data_part`
PARTITION BY DATE(pickup_datetime)
CLUSTER BY affiliated_base_number AS
SELECT * FROM `trips_data_all.vfh_data_simp`;

-- Write a query to retrieve the distinct affiliated_base_number between pickup_datetime 2019/03/01 and 2019/03/31 (inclusive).
-- Use the BQ table you created earlier in your from clause and note the estimated bytes.
SELECT COUNT(DISTINCT(affiliated_base_number)) from `trips_data_all.vfh_data_part`
WHERE DATE(pickup_datetime) BETWEEN '2019-03-01' AND '2019-03-31';

SELECT COUNT(DISTINCT(affiliated_base_number)) from `trips_data_all.vfh_data_simp`
WHERE DATE(pickup_datetime) BETWEEN '2019-03-01' AND '2019-03-31';


