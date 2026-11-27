
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

LOOKUP_FOLDER = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "MOT lookup tables"
)

lookup_files = [
    "item_detail.csv",
    "item_group.csv",
    "mdr_fuel_types.csv",
    "mdr_rfr_location.csv",
    "mdr_test_outcome.csv",
    "mdr_test_type.csv",
]

for filename in lookup_files:
    file_path = LOOKUP_FOLDER / filename

    print("\n" + "=" * 70)
    print(f"FILE: {filename}")
    print("=" * 70)

    if not file_path.exists():
        print("File not found!")
        continue

    df = pd.read_csv(file_path, sep="|", nrows=5)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 records:")
    print(df.to_string(index=False))
