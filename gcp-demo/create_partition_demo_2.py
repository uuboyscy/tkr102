from csv import DictReader, DictWriter
from pathlib import Path


SOURCE_FILE = Path("partition-demo/sell.csv")
OUTPUT_ROOT = Path("partition-demo-2/daily")

PARTITIONS = {
    "2026-09-01": {"P001": 120, "P002": 890, "P003": 80, "P004": 4990, "P005": 4990},
    "2026-09-02": {"P001": 130, "P002": 920, "P003": 85, "P004": 4890, "P005": 4890},
    "2026-09-03": {"P001": 115, "P002": 875, "P003": 78, "P004": 5050, "P005": 5050},
}


def create_partitions() -> None:
    with SOURCE_FILE.open(newline="", encoding="utf-8") as source:
        rows = list(DictReader(source))

    if not rows:
        raise ValueError(f"No rows found in {SOURCE_FILE}")

    fieldnames = list(rows[0])
    for partition_date, prices in PARTITIONS.items():
        partition_dir = OUTPUT_ROOT / f"dt={partition_date}"
        partition_dir.mkdir(parents=True, exist_ok=True)

        partition_rows = []
        for row in rows:
            product_id = row["product_id"]
            if product_id not in prices:
                raise KeyError(f"Missing price for {product_id} on {partition_date}")

            partition_row = row.copy()
            partition_row["price"] = str(prices[product_id])
            partition_rows.append(partition_row)

        output_file = partition_dir / "sell.csv"
        with output_file.open("w", newline="", encoding="utf-8") as output:
            writer = DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(partition_rows)

        print(f"Created {output_file}")


if __name__ == "__main__":
    create_partitions()