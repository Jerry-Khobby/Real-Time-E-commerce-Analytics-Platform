SELECT
    customer_id,
    name,
    email,
    country,
    signup_date
FROM {{ source('raw', 'customers') }}