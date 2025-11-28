WITH customers AS (
    SELECT * FROM {{ ref('stg_customers') }}
),

orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
),

products AS (
    SELECT * FROM {{ ref('stg_products') }}
),

customer_metrics AS (
    SELECT
        c.customer_id,
        c.name,
        c.email,
        c.country,
        c.signup_date,
        COUNT(o.order_id) AS total_orders,
        SUM(CASE WHEN o.is_completed THEN 1 ELSE 0 END) AS completed_orders,
        SUM(o.quantity * p.price) AS lifetime_value,
        MIN(o.order_date) AS first_order_date,
        MAX(o.order_date) AS last_order_date
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    LEFT JOIN products p ON o.product_id = p.product_id
    GROUP BY c.customer_id, c.name, c.email, c.country, c.signup_date
)

SELECT * FROM customer_metrics