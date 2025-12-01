-- Retail Sales Analytics - SQL Portfolio Script
-- Table: retail_sales_2023

-- 1. Basic dataset overview
SELECT
    COUNT(*) AS total_transactions,
    COUNT(DISTINCT store) AS store_count,
    COUNT(DISTINCT category) AS category_count,
    COUNT(DISTINCT product) AS product_count,
    SUM(revenue) AS total_revenue
FROM retail_sales_2023;

-- 2. Revenue by store (descending)
SELECT
    store,
    SUM(revenue) AS store_revenue
FROM retail_sales_2023
GROUP BY store
ORDER BY store_revenue DESC;

-- 3. Revenue by product category
SELECT
    category,
    SUM(revenue) AS category_revenue
FROM retail_sales_2023
GROUP BY category
ORDER BY category_revenue DESC;

-- 4. Monthly revenue trend
-- Adjust date functions to your SQL dialect if needed
SELECT
    CAST(DATEFROMPARTS(YEAR(date), MONTH(date), 1) AS date) AS month_start,
    SUM(revenue) AS monthly_revenue
FROM retail_sales_2023
GROUP BY DATEFROMPARTS(YEAR(date), MONTH(date), 1)
ORDER BY month_start;

-- 5. Top 3 products by revenue per store
SELECT
    store,
    product,
    SUM(revenue) AS product_revenue,
    RANK() OVER (PARTITION BY store ORDER BY SUM(revenue) DESC) AS revenue_rank
FROM retail_sales_2023
GROUP BY store, product
HAVING RANK() OVER (PARTITION BY store ORDER BY SUM(revenue) DESC) <= 3;

-- 6. Weekday vs weekend performance
SELECT
    CASE
        WHEN DATENAME(WEEKDAY, date) IN ('Saturday', 'Sunday') THEN 'Weekend'
        ELSE 'Weekday'
    END AS day_type,
    COUNT(*) AS transactions,
    SUM(revenue) AS total_revenue
FROM retail_sales_2023
GROUP BY
    CASE
        WHEN DATENAME(WEEKDAY, date) IN ('Saturday', 'Sunday') THEN 'Weekend'
        ELSE 'Weekday'
    END;

-- 7. Store contribution to total revenue (percentage)
WITH store_rev AS (
    SELECT store, SUM(revenue) AS store_revenue
    FROM retail_sales_2023
    GROUP BY store
),
total AS (
    SELECT SUM(store_revenue) AS total_revenue
    FROM store_rev
)
SELECT
    s.store,
    s.store_revenue,
    ROUND(100.0 * s.store_revenue / t.total_revenue, 2) AS revenue_contribution_pct
FROM store_rev s
CROSS JOIN total t
ORDER BY store_revenue DESC;
