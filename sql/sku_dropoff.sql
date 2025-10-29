-- SKU Drop-off Analysis
-- Identifies SKUs with low cart-to-purchase conversion rates
-- Uses RANK() window function and QUALIFY clause

-- Load funnel_steps if not already loaded (path resolved relative to project root)
CREATE TABLE IF NOT EXISTS funnel_steps AS
SELECT * FROM read_csv_auto('artifacts/funnel_steps.csv', header=true);

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
SELECT c.sku, c.carts, COALESCE(p.purchases,0) AS purchases,
       1.0*COALESCE(p.purchases,0)/NULLIF(c.carts,0) AS cart_to_purchase_rate,
       RANK() OVER (ORDER BY 1.0*COALESCE(p.purchases,0)/NULLIF(c.carts,0)) AS low_conv_rank
FROM carted c
LEFT JOIN purchased p USING(sku)
QUALIFY c.carts >= 50
ORDER BY cart_to_purchase_rate;

