# Retail Sales Analytics – Indian Multi-City Chain (2023)

This portfolio project analyzes one year of retail transaction data from a fictional Indian multi-city retail chain. The goal is to demonstrate end-to-end data analytics skills: data cleaning, exploratory data analysis (EDA), SQL-based analysis, and creation of business-ready insights.

## Business Context

A mid-sized retail chain operates stores in major Indian cities (Bangalore, Delhi, Mumbai, Chennai, Hyderabad) and sells multiple product categories such as Electronics, Clothing, Groceries, and Home Decor. Management wants to understand:

- How overall revenue and transaction volumes are trending.
- Which stores and categories are driving sales.
- How seasonality and weekdays/weekends affect performance.
- Where to focus promotional or optimization efforts.

## Dataset

File: `data/retail_sales_2023_india.csv`

Each row represents a single transaction with:

- `date` – transaction date (2023)
- `store` – city/store (e.g., Bangalore, Delhi, Mumbai)
- `category` – product category (Electronics, Clothing, Groceries, Home Decor)
- `product` – product code (e.g., A1, B1, C1, D1)
- `quantity` – quantity sold
- `unit_price` – unit price in INR
- `revenue` – transaction revenue in INR

The dataset is synthetic but structured to closely resemble real-world point-of-sale data [attached_file:3].

## Project Structure

retail-sales-analytics/
├─ data/
│ ├─ retail_sales_2023_india.csv
│ └─ retail_sales_2023_india_clean.csv # generated after cleaning
├─ notebooks/
│ └─ 01_retail_sales_eda.ipynb
├─ sql/
│ └─ retail_sales_analysis.sql
├─ src/
│ ├─ data_preparation.py
│ └─ kpi_calculations.py
├─ reports/
│ └─ figures/ # exported charts (optional)
├─ requirements.txt
└─ README.md


## Analytical Steps

1. **Data Preparation (`src/data_preparation.py`)**
   - Standardize column names.
   - Parse dates and engineer features: year, month, month name, day of week.
   - Recalculate revenue (`quantity * unit_price`) and flag mismatches.

2. **Exploratory Data Analysis (`notebooks/01_retail_sales_eda.ipynb`)**
   - Basic checks: missing values, data types, descriptive statistics.
   - Key KPIs: total revenue, total transactions, average order value.
   - Revenue by store, category, and product.
   - Monthly revenue trend across 2023.
   - Store vs. category revenue heatmap.
   - Weekday vs. weekend performance.

3. **SQL Analysis (`sql/retail_sales_analysis.sql`)**
   - Dataset overview (transactions, stores, categories, total revenue).
   - Revenue by store and category.
   - Monthly revenue trend.
   - Top products by revenue per store.
   - Store revenue contribution percentages.

## How to Run Locally
1. Clone the repository:
git clone https://github.com/IshanMangla/retail-sales-analytics.git
cd retail-sales-analytics

2. (Optional) Create and activate a virtual environment.

3. Install dependencies:
pip install -r requirements.txt

4. Run the data cleaning script:
python src/data_preparation.py

5. Launch Jupyter Notebook:
jupyter notebook notebooks/01_retail_sales_eda.ipynb

## Potential Extensions
- Build an interactive dashboard in Power BI, Tableau, or Streamlit using the cleaned dataset.
- Add simple time-series forecasting for monthly revenue.
- Introduce customer dimensions (if available) and perform cohort or RFM analysis.
- Deploy a lightweight dashboard app that reads the cleaned CSV.
## About This Project
This project was created to showcase practical data analytics skills for retail use cases, including Python, SQL, and clear communication of insights to business stakeholders.








