-- Cohort Retention Analysis
-- Calculates monthly cohort retention rates for users who made purchases
-- Uses DATE_TRUNC and COUNT DISTINCT window functions

-- Load funnel_steps if not already loaded (path resolved relative to project root)
CREATE TABLE IF NOT EXISTS funnel_steps AS
SELECT * FROM read_csv_auto('artifacts/funnel_steps.csv', header=true);

WITH first_purchase AS (
  SELECT user_id, MIN(ts)::DATE AS first_purchase_date
  FROM funnel_steps
  WHERE event_type='transaction'
  GROUP BY 1
),
cohorts AS (
  SELECT user_id, DATE_TRUNC('month', first_purchase_date) AS cohort_month
  FROM first_purchase
),
repeats AS (
  SELECT f.user_id, DATE_TRUNC('month', fs.ts) AS month_active
  FROM cohorts f JOIN funnel_steps fs USING(user_id)
  WHERE fs.event_type='transaction'
)
SELECT cohort_month, month_active,
       COUNT(DISTINCT CASE WHEN month_active=cohort_month THEN user_id END) AS cohort_size,
       COUNT(DISTINCT user_id) AS active_users,
       1.0*COUNT(DISTINCT user_id)/NULLIF(COUNT(DISTINCT CASE WHEN month_active=cohort_month THEN user_id END),0) AS retention
FROM repeats
GROUP BY 1,2
ORDER BY 1,2;

