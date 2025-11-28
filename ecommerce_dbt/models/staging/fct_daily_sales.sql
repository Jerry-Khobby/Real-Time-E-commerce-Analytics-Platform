WITH orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
),

products AS (
    SELECT * FROM {{ ref('stg_products') }}
),

daily_sales AS (
    SELECT
        o.order_date,
        COUNT(o.order_id) AS total_orders,
        SUM(o.quantity) AS total_units,
        SUM(o.quantity * p.price) AS total_revenue,
        AVG(o.quantity * p.price) AS avg_order_value
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    WHERE o.is_completed = true
    GROUP BY o.order_date
)

SELECT * FROM daily_sales
ORDER BY order_date DESC