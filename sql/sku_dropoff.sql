-- SKU Drop-off Analysis
-- Identifies SKUs with low cart-to-purchase conversion rates
-- Uses RANK() window function

WITH carted AS (
  SELECT sku, COUNT(*) AS carts
  FROM funnel_steps
  WHERE event_type='addtocart'
  GROUP BY 1
),
purchased AS (
  SELECT sku, COUNT(*) AS purchases
  FROM funnel_steps
  WHERE event_type='transaction'
  GROUP BY 1
)
SELECT * FROM (
    SELECT c.sku, c.carts, COALESCE(p.purchases,0) AS purchases,
           1.0*COALESCE(p.purchases,0)/NULLIF(c.carts,0) AS cart_to_purchase_rate,
           RANK() OVER (ORDER BY 1.0*COALESCE(p.purchases,0)/NULLIF(c.carts,0)) AS low_conv_rank
    FROM carted c
    LEFT JOIN purchased p USING(sku)
)
WHERE carts >= 50
ORDER BY cart_to_purchase_rate;
