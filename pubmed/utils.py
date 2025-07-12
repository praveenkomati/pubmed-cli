import csv
from typing import List, Dict

def save_to_csv(data: List[Dict[str, str]], filename: str) -> None:
    if not data:
        print("⚠️ No data to write.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"💾 Saved {len(data)} detailed records to {filename}")
