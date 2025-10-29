# E-Commerce Revenue Funnel Analyzer — Project Scope  
**Stack:** SQL • Python • Pandas • Tableau

## 0) Purpose
Find and quantify revenue leakage from **view → add-to-cart → purchase**. Produce a reproducible ETL, export clean artifacts, and publish a Tableau dashboard. The doc is zero-context build instructions.

## 1) Success Criteria
- Repro runs from clean clone in ≤10 min.
- Tableau Public dashboard link loads for anyone.
- View→Cart, Cart→Purchase, AOV, Revenue visible by date, device, category.
- ≥3 SQL window functions used; uplift model included.
- README states quantified opportunity (e.g., “+\$50k/mo if cart→purchase +15%”).

## 2) Scope and Non-Goals
- Scope: sessionization, funnel steps, conversions, cohorts, SKU drop-off, Tableau dashboard.
- Non-Goals: identity stitching across devices, attribution modeling, paid media joins.

## 3) Prereqs
- OS: macOS/Windows/Linux.
- Accounts: **Tableau Public**.
- Install: Python 3.10+, Git.

## 4) Repository Layout
```

ecom-funnel/
├─ data/
│  ├─ raw/                    # source CSVs
│  └─ interim/                # cleaned parquet
├─ artifacts/                 # CSVs for Tableau
├─ notebooks/01_eda.ipynb
├─ sql/
│  ├─ sku_dropoff.sql
│  └─ cohort_retention.sql
├─ src/
│  ├─ etl_funnel.py
│  └─ utils.py
├─ env/requirements.txt
└─ README.md

```

### env/requirements.txt
```

duckdb>=1.0
pandas>=2.2
pyarrow>=16
jupyterlab

````

## 5) Data Acquisition
Pick one and place files under `data/raw/`:
- **RetailRocket e-commerce events** (recommended; has `view`, `addtocart`, `transaction`). Files: `events.csv`, `item_properties_part*.csv`.  
  Link: https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset
- **UCI Online Retail II** (transactions only; still useful for AOV and cohorts).  
  Link: https://archive.ics.uci.edu/ml/datasets/online%2Bretail%2BII

> If Kaggle blocks API, download via browser once. Do not commit raw data.

## 6) Metrics and Definitions
- **Session:** sequence of events for a user with ≤30 min inactivity gap.
- **Funnel:** `view → addtocart → transaction` within a session.
- **Rates:**  
  `view_to_cart = carts / views`  
  `cart_to_purchase = transactions / carts`
- **Uplift model:** `uplift = (target_rate − current_rate) × carts × AOV`.

## 7) Build Steps

### 7.1 Create environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r env/requirements.txt
````

### 7.2 Implement ETL (`src/etl_funnel.py`)

```python
import duckdb, pandas as pd, pathlib as p
RAW = p.Path("data/raw"); ART = p.Path("artifacts"); ART.mkdir(parents=True, exist_ok=True)
con = duckdb.connect(database=":memory:")

# Load events
con.execute("""
CREATE OR REPLACE TABLE events AS
SELECT CAST(user_id AS VARCHAR) AS user_id,
       CAST(timestamp AS TIMESTAMP) AS ts,
       event AS event_type,
       CAST(itemid AS VARCHAR) AS sku
FROM read_csv_auto('data/raw/events.csv');
""")

# Sessionize: 30-min gap => new session
con.execute("""
CREATE OR REPLACE TABLE events_s AS
WITH e AS (
  SELECT user_id, ts, event_type, sku,
         CASE WHEN ts - LAG(ts) OVER (PARTITION BY user_id ORDER BY ts) > INTERVAL 30 MINUTE
              OR LAG(ts) OVER (PARTITION BY user_id ORDER BY ts) IS NULL
              THEN 1 ELSE 0 END AS new_session
  FROM events
)
SELECT *, SUM(new_session) OVER (PARTITION BY user_id ORDER BY ts ROWS UNBOUNDED PRECEDING) AS session_seq
FROM e;
""")

# Ordered steps per session
con.execute("""
CREATE OR REPLACE TABLE funnel_steps AS
SELECT user_id,
       CONCAT(user_id,'-',session_seq) AS session_id,
       ts, event_type, sku,
       ROW_NUMBER() OVER (PARTITION BY user_id, session_seq ORDER BY ts) AS step_order
FROM events_s;
""")

# Session-level flags
con.execute("""
CREATE OR REPLACE TABLE funnel_session AS
SELECT session_id,
       MAX(CASE WHEN event_type='view' THEN 1 ELSE 0 END) AS has_view,
       MAX(CASE WHEN event_type='addtocart' THEN 1 ELSE 0 END) AS has_cart,
       MAX(CASE WHEN event_type='transaction' THEN 1 ELSE 0 END) AS has_purchase
FROM funnel_steps
GROUP BY 1;
""")

# Export artifacts
con.execute("COPY (SELECT * FROM funnel_session) TO 'artifacts/funnel_session.csv' (HEADER, DELIMITER ',');")
```

### 7.3 Analytics SQL (`sql/sku_dropoff.sql`)

```sql
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
```

### 7.4 Optional cohort SQL (`sql/cohort_retention.sql`)

```sql
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
```

### 7.5 Run pipeline

```bash
python src/etl_funnel.py
duckdb -c ".read sql/sku_dropoff.sql" > artifacts/sku_dropoff.csv
duckdb -c ".read sql/cohort_retention.sql" > artifacts/cohort_retention.csv
```

## 8) Tableau Build

1. Install **Tableau Public**; sign in.
2. **Data → New Data Source → Text File** → select `artifacts/*.csv`.
3. Worksheets:

   * **KPIs**: create calculated fields for rates and AOV.
   * **Funnel**: step conversion.
   * **SKU Drop-off**: table sorted by `cart_to_purchase_rate`.
   * **Cohort Heatmap**: from `cohort_retention.csv` (optional).
4. Dashboard:

   * Place KPI cards, funnel viz, SKU table, filters (Date, Category, Device).
5. Publish:

   * **Server → Tableau Public → Save to Tableau Public**. Copy URL into README.

### Calculations to add in Tableau

* `View_to_Cart % = SUM(has_cart)/SUM(has_view)`
* `Cart_to_Purchase % = SUM(has_purchase)/SUM(has_cart)`
* `Revenue = SUM(AOV proxy * has_purchase)` if price data exists, else omit.

## 9) QA

* Row counts between artifacts and Tableau match.
* Timestamps parse to correct timezone.
* Filters do not change totals unexpectedly.
* Performance: dashboard interactions <2s.

## 10) Deliverables Checklist

* Code, SQL, artifacts, dashboard URL, README with quantified uplift.
* Commit history ≥6 meaningful commits.

## 11) Troubleshooting

* Empty conversions: verify event labels match (`addtocart`, `transaction`).
* Very large CSVs: convert to Parquet in `data/interim/` and query directly with DuckDB.
* Tableau publishing blocked: ensure at least one worksheet exists before publish.

````
