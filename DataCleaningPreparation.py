-- Prepare clean data for Tableau visualization
CREATE VIEW clean_product_data AS
SELECT 
    product_id,
    product_name,
    COALESCE(category, 'Uncategorized') AS product_category,
    ROUND(price, 2) AS standardized_price,
    CASE 
        WHEN inventory_count = 0 THEN 'Out of Stock'
        WHEN inventory_count < 10 THEN 'Low Stock'
        ELSE 'In Stock'
    END AS stock_status
FROM products
WHERE is_active = true
