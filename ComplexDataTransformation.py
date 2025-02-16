-- Create a materialized view for Tableau dashboard
CREATE MATERIALIZED VIEW customer_performance_metrics AS
WITH customer_metrics AS (
    SELECT 
        customer_id,
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(order_total) AS lifetime_value,
        AVG(order_total) AS average_order_value,
        MAX(order_date) AS last_purchase_date
    FROM orders
    GROUP BY customer_id
)
SELECT 
    cm.*,
    CASE 
        WHEN lifetime_value > 10000 THEN 'Premium'
        WHEN lifetime_value > 5000 THEN 'Gold'
        WHEN lifetime_value > 1000 THEN 'Silver'
        ELSE 'Bronze'
    END AS customer_tier
FROM customer_metrics cm
