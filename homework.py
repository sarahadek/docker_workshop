import pandas as pd
from sqlalchemy import create_engine

# UPDATED connection string to match the assignment's credentials
# User: postgres, Pass: postgres, Port: 5433 (external mapping)
engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

# Load Green Taxi
print("Loading Green Taxi...")
df_green = pd.read_parquet('green_tripdata_2025-11.parquet')
df_green.to_sql(name='green_tripdata_2025_11', con=engine, if_exists='replace')

# Load Zones
print("Loading Zones...")
df_zones = pd.read_csv('taxi_zone_lookup.csv')
df_zones.to_sql(name='zones', con=engine, if_exists='replace')

print("Done! Data is ready for SQL queries.")

