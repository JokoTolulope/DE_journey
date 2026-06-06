# A list of raw table names arriving from a source database
tables = ["customers", "orders", "payments", "products", "returns"]

#Add a new table name
tables.append("shipments")

#only process the first 3 tables in this batch
batch = tables[:3]

#List comprehension, generate the S3 path where each table will be stored
s3_paths = [f"s3://my-data-lake/raw/{table}/" for table in tables]

print(f"Tables in this batch: {batch}")
print(f"S3 paths generated:")
for path in s3_paths:
    print(f"  {path}")
    
#metadata about a table arriving in the pipeline
table_info = {"table_name": "orders",
              "source": "sql server",
              "row_count": 95000,
              "last_updated": "2026-06-04",
              "status": "pending"}

# update the pipeline status
table_info["status"] = "loaded"

#add a new piece of metadata
table_info["destination"] = "s3://my-data-lake/raw/orders/"

#print a load summary
print("=== Table Load Summary ===")
for key, value in table_info.items():
    print(f"  {key}: {value}")
    
#sets -- removes duplicates, useful when you want to know which unique tables actually ran today
# The pipeline runs every hour and logs which tables were processed
#sometimes the same tables get logged more than once due to retries
processed_log = ["orders", "customers", "payments", "orders", "products", "customers", "shipments"]
unique_tables = set(processed_log)

print(f"Total log entries: {len(processed_log)}")
print(f"Unique tables processed: {len(unique_tables)}")
print(f"Tables: {unique_tables}")

#comprehension
# The pipeline tracked these tables and their row count
tables = {"orders": 95000,
          "customers": 42000,
          "payments": 18000,
          "products": 3200,
          "returns": 870}

#List comprehension to find tables with more than 10,000 rows
#These are the heavy tables that need partitioning
heavy_tables = [table for table, count in tables.items() if count > 10000]

#Dict comprehension, calculate what % of total rows each table holds
total_rows = sum(tables.values())
row_share = {table: round((count/total_rows) * 100, 2) for table, count in tables.items()}


print(f"Heavy tables (>10k rows): {heavy_tables}")
print(f"\nRow share per table:")
for table, pct in row_share.items():
    print(f"  {table}: {pct}%")




