"""
Data Preparation Script for Retail Sales Analytics Project
----------------------------------------------------------

This script loads raw retail sales data, performs cleaning, validation,
and feature engineering, and saves a cleaned dataset for further analysis.

Author: Ishan Mangla
"""

import pandas as pd

def kpi_overall_revenue(df: pd.DataFrame) -> float:
    """Total revenue across all transactions."""
    return float(df["revenue"].sum())

def kpi_total_transactions(df: pd.DataFrame) -> int:
    """Total number of transactions."""
    return int(df.shape[0])

def kpi_avg_order_value(df: pd.DataFrame) -> float:
    """Average revenue per transaction."""
    if df.shape[0] == 0:
        return 0.0
    return float(df["revenue"].sum() / df.shape[0])

def revenue_by_store(df: pd.DataFrame) -> pd.DataFrame:
    """Revenue aggregated by store."""
    return (
        df.groupby("store", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )

def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Revenue aggregated by product category."""
    return (
        df.groupby("category", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
    )

def monthly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Monthly revenue trend."""
    return (
        df.groupby(["year", "month", "month_name"], as_index=False)["revenue"]
        .sum()
        .sort_values(["year", "month"])
    )

def store_category_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Store x Category revenue matrix for heatmaps."""
    pivot = (
        df.pivot_table(
            index="store",
            columns="category",
            values="revenue",
            aggfunc="sum"
        )
        .fillna(0)
    )
    return pivot
