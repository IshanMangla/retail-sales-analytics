"""
Data Preparation Script for Retail Sales Analytics Project
----------------------------------------------------------

This script loads raw retail sales data, performs cleaning, validation,
and feature engineering, and saves a cleaned dataset for further analysis.

Author: Ishan Mangla
"""

import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "retail_sales_2023_india.csv"

def load_raw_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load raw retail sales data from CSV."""
    df = pd.read_csv(path)
    return df

def clean_and_enrich(df: pd.DataFrame) -> pd.DataFrame:
    """Clean dataset and create additional time and quality-check features."""
    # Standardize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Parse dates
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Basic data quality checks
    df = df.dropna(subset=["date", "store", "category", "product", "quantity", "unit_price", "revenue"])

    # Create additional time features
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.strftime("%b")
    df["day_of_week"] = df["date"].dt.day_name()

    # Recalculate revenue as a quality check
    df["calculated_revenue"] = df["quantity"] * df["unit_price"]

    # Flag revenue mismatch
    df["revenue_mismatch_flag"] = (df["revenue"].round(2) != df["calculated_revenue"].round(2))

    return df

def main():
    df_raw = load_raw_data()
    df_clean = clean_and_enrich(df_raw)

    output_path = DATA_PATH.parent / "data" / "processed" / "retail_sales_2023_india_clean.csv"
    df_clean.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path}")

if __name__ == "__main__":
    main()

