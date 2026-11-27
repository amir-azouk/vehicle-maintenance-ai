
from pathlib import Path
import pandas as pd

# Locate the project and raw data folders
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA = PROJECT_ROOT / "data" / "raw"

# Dataset folders
RESULTS_FOLDER = RAW_DATA / "MOT testing data results (2024)"
FAILURES_FOLDER = RAW_DATA / "MOT Testing data failure item (2024)"


def inspect_dataset(folder, dataset_name):
    print("\n" + "=" * 70)
    print(f"INSPECTING: {dataset_name}")
    print("=" * 70)

    # Find the first monthly CSV file
    csv_files = sorted(folder.glob("*.csv"))

    if not csv_files:
        print("No CSV files found!")
        return

    file_path = csv_files[0]

    print(f"\nFile: {file_path.name}")
    print(f"File size: {file_path.stat().st_size / (1024**3):.2f} GB")

    # Read a small sample to inspect the structure
    df = pd.read_csv(file_path, nrows=5, sep=None, engine="python")

    print("\nColumn names:")
    for column in df.columns:
        print(f"- {column}")

    print("\nFirst 5 records:")
    print(df.to_string(index=False))

    print("\nMissing values in sample:")
    print(df.isnull().sum())


# Inspect one month from each dataset
inspect_dataset(RESULTS_FOLDER, "MOT Test Results")
inspect_dataset(FAILURES_FOLDER, "MOT Failure Items")
