WITH source as (

  select * from {{source('raw','orders')}}
)

cleaned AS (
    SELECT
        order_id,
        customer_id,
        product_id,
        quantity,
        order_date,
        status,
        CASE 
            WHEN status = 'completed' THEN true
            ELSE false
        END AS is_completed
    FROM source
)

SELECT * FROM cleaned