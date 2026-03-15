import os
import sys

# ensure project root is on path for local imports
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data


def run_pipeline():
    df = extract_data(os.path.join("data", "raw", "retail_sales.csv"))
    df = transform_data(df)

    # write cleaned output
    df.to_csv(os.path.join("data", "processed", "cleaned_sales.csv"), index=False)

    load_data(df)


if __name__ == "__main__":
    run_pipeline()