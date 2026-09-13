import os
import time


print("starting batch job")
print(f"batch_id={os.environ.get('BATCH_ID', 'local')}")

# Do your ETL, backup, or data processing work here
for item in range(3):
    print(f"processing item {item}")
    time.sleep(1)

print("batch job completed")