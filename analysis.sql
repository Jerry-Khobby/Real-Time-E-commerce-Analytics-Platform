-- Connect to your database using any SQL client or:
-- docker exec -it ecommerce_db psql -U dataeng -d ecommerce

-- Query 1: Daily sales summary
SELECT 
    order_date,
    COUNT(*) as total_orders,
    SUM(o.quantity * p.price) as total_revenue
FROM raw.orders o
JOIN raw.products p ON o.product_id = p.product_id
WHERE status = 'completed'
GROUP BY order_date
ORDER BY order_date DESC
LIMIT 10;

-- Query 2: Top 10 customers by revenue
SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) as total_orders,
    SUM(o.quantity * p.price) as total_spent
FROM raw.customers c
JOIN raw.orders o ON c.customer_id = o.customer_id
JOIN raw.products p ON o.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC
LIMIT 10;

-- Query 3: Product performance by category
SELECT 
    p.category,
    COUNT(DISTINCT o.order_id) as orders,
    SUM(o.quantity) as units_sold,
    SUM(o.quantity * p.price) as revenue
FROM raw.products p
JOIN raw.orders o ON p.product_id = o.product_id
WHERE o.status = 'completed'
GROUP BY p.category
ORDER BY revenue DESC;