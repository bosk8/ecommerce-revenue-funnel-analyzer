## 1. Project Foundation

- [x] 1.1 Create repository directory structure (data/raw, data/interim, artifacts, notebooks, sql, src, env)
- [x] 1.2 Create `env/requirements.txt` with duckdb>=1.0, pandas>=2.2, pyarrow>=16, jupyterlab
- [x] 1.3 Create initial README.md with project description, setup instructions, and structure overview
- [x] 1.4 Add `.gitignore` to exclude raw data, virtual environment, and artifacts

## 2. ETL Pipeline Core

- [x] 2.1 Create `src/utils.py` with path constants and helper functions
- [x] 2.2 Implement `src/etl_funnel.py` with DuckDB connection setup
- [x] 2.3 Add CSV loading logic with proper type casting (user_id, timestamp, event, itemid)
- [x] 2.4 Implement 30-minute sessionization using LAG() window function
- [x] 2.5 Implement session sequence assignment using SUM() window function
- [x] 2.6 Create funnel_steps table with session_id and step_order using ROW_NUMBER()
- [x] 2.7 Generate funnel_session table with has_view, has_cart, has_purchase flags
- [x] 2.8 Add export to `artifacts/funnel_session.csv` with HEADER and comma delimiter

## 3. Analytics SQL Queries

- [x] 3.1 Create `sql/sku_dropoff.sql` with carted and purchased CTEs
- [x] 3.2 Implement cart_to_purchase_rate calculation with NULLIF handling
- [x] 3.3 Add RANK() window function for low conversion ranking
- [x] 3.4 Add QUALIFY clause to filter SKUs with ≥50 carts
- [x] 3.5 Create `sql/cohort_retention.sql` with first_purchase CTE
- [x] 3.6 Implement cohort_month assignment using DATE_TRUNC
- [x] 3.7 Calculate retention rates using COUNT DISTINCT window functions
- [x] 3.8 Add export commands for both SQL outputs to artifacts/

## 4. Pipeline Execution

- [x] 4.1 Create bash script or update etl_funnel.py to execute SQL files
- [x] 4.2 Test pipeline end-to-end with sample data
- [x] 4.3 Verify all artifacts are generated correctly
- [x] 4.4 Add data validation checks (row counts, null handling, timestamp parsing)

## 5. Documentation and QA

- [x] 5.1 Update README.md with complete setup instructions
- [x] 5.2 Document data acquisition steps (RetailRocket or UCI)
- [x] 5.3 Add troubleshooting section (event label mismatches, empty conversions, large CSV handling)
- [x] 5.4 Quantify revenue opportunity in README (e.g., "+$50k/mo if cart→purchase +15%")
- [x] 5.5 Verify reproducible execution ≤10 minutes from clean clone
- [x] 5.6 Document Tableau dashboard publishing process

## 6. Notebook and Exploratory Analysis

- [x] 6.1 Create `notebooks/01_eda.ipynb` with initial data exploration
- [x] 6.2 Add cells for data profiling, event distribution, basic statistics
- [x] 6.3 Include visualization examples for funnel metrics

