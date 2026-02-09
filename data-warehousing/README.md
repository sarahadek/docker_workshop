Question 1
Query used to find the total count of records:
SELECT COUNT(*) FROM `emerald-stage-486216-g1.ny_taxi.yellow_tripdata_2024_regular`;

Answer: 20,332,093

Question 2
Queries to compare estimated bytes:
1. SELECT COUNT(DISTINCT PULocationID) FROM `emerald-stage-486216-g1.ny_taxi.external_yellow_tripdata`;
2. SELECT COUNT(DISTINCT PULocationID) FROM `emerald-stage-486216-g1.ny_taxi.yellow_tripdata_2024_regular`;
before running the query i highlighted the code and it showed the query will process o bytes for external table and 155.22mb for regular table
Answer: 0 MB for the External Table and 155.12 MB for the Materialized Table.

Question 3
the Reason for different byte estimations: BigQuery is a columnar database. It only scans the specific columns requested. 

Adding `DOLocationID` to a query that already has `PULocationID` increases the 
data read because BigQuery must now access the storage blocks for both columns 
instead of just one.

Question 4
Query to find records with a fare_amount of 0:
SELECT count(*) 
FROM `emerald-stage-486216-g1.ny_taxi.yellow_tripdata_2024_regular` 
WHERE fare_amount = 0;

Answer: 8,333

Question 5
Strategy: Partition by `tpep_dropoff_datetime` and Cluster on `VendorID`.

TABLE SQL
EPLACE TABLE `emerald-stage-486216-g1.ny_taxi.yellow_tripdata_2024_partitioned`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `emerald-stage-486216-g1.ny_taxi.external_yellow_tripdata`;


Question 6
Query to compare performance:
SELECT DISTINCT(VendorID)
FROM `emerald-stage-486216-g1.ny_taxi.yellow_tripdata_2024_partitioned`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

Answer: 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

Question 7
GCP Bucket
Explanation: External tables in BigQuery do not store the data internally. Instead, they point to data stored in external sources like Google Cloud Storage (GCP Buckets).

Question 8
False
Explanation: While clustering improves performance for large datasets.For small datasets (typically < 1 GB), the benefits are negligible, and the metadata overhead may not justify the implementation.