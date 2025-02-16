-- Prepare sales summary for Tableau
CREATE VIEW tableau_sales_summary AS
SELECT 
    YEAR(sale_date) AS sales_year,
    MONTH(sale_date) AS sales_month,
    product_category,
    SUM(total_sales) AS monthly_category_sales,
    AVG(total_sales) AS avg_monthly_sales
FROM sales_table
GROUP BY 
    YEAR(sale_date),
    MONTH(sale_date),
    product_category
