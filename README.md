# E-Commerce Revenue Funnel Analyzer

**Stack:** SQL • Python • Pandas • Tableau

## Purpose

Find and quantify revenue leakage from **view → add-to-cart → purchase** conversion. This project provides a reproducible ETL pipeline, clean data artifacts, and a Tableau dashboard to identify revenue improvement opportunities.

## Quick Start

### Prerequisites

- **OS**: macOS/Windows/Linux
- **Python**: 3.10 or higher
- **Account**: [Tableau Public](https://public.tableau.com/) (free)
- **Install**: Git

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd 01-ecommerce-revenue-funnel-analyzer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r env/requirements.txt
   ```

4. **Acquire data** (see Data Acquisition section below)

5. **Run pipeline**
   ```bash
   python src/etl_funnel.py
   ```

6. **Execute analytics queries**
   
   Option 1: Using Python script (recommended)
   ```bash
   python src/run_analytics.py
   ```
   
   Option 2: Using DuckDB CLI directly
   ```bash
   duckdb -c ".read sql/sku_dropoff.sql" > artifacts/sku_dropoff.csv
   duckdb -c ".read sql/cohort_retention.sql" > artifacts/cohort_retention.csv
   ```

## Repository Structure

```
ecom-funnel/
├─ data/
│  ├─ raw/                    # source CSVs (not committed)
│  └─ interim/                # cleaned parquet (optional)
├─ artifacts/                 # CSVs for Tableau
├─ notebooks/01_eda.ipynb     # Exploratory data analysis
├─ sql/
│  ├─ sku_dropoff.sql         # SKU conversion analysis
│  └─ cohort_retention.sql    # Cohort retention analysis
├─ src/
│  ├─ etl_funnel.py           # Main ETL pipeline
│  └─ utils.py                # Helper functions
├─ env/requirements.txt       # Python dependencies
└─ README.md                  # This file
```

## Data Acquisition

### Option 1: RetailRocket E-Commerce Dataset (Recommended)

The RetailRocket dataset contains all required events (view, addtocart, transaction).

1. Visit [Kaggle: RetailRocket E-Commerce Dataset](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset)
2. Download `events.csv` and `item_properties_part*.csv` files
3. Place files in `data/raw/` directory

> **Note**: If Kaggle API is unavailable, download manually via browser. Raw data files are not committed to the repository.

### Option 2: UCI Online Retail II (Alternative)

Alternative dataset with transactions only (useful for AOV and cohorts, but less funnel detail).

1. Visit [UCI Online Retail II](https://archive.ics.uci.edu/ml/datasets/online%2Bretail%2BII)
2. Download the dataset
3. Place files in `data/raw/` directory

## Metrics and Definitions

- **Session**: Sequence of events for a user with ≤30 minute inactivity gap
- **Funnel**: `view → addtocart → transaction` within a session
- **Conversion Rates**:
  - `view_to_cart = carts / views`
  - `cart_to_purchase = transactions / carts`
- **Uplift Model**: `uplift = (target_rate − current_rate) × carts × AOV`

## Revenue Opportunity

After running the pipeline with your data, calculate the uplift using the funnel metrics:

**Uplift Formula**: `uplift = (target_rate - current_rate) × carts × AOV`

**Example Calculation**:
- Current cart-to-purchase rate: 15%
- Target rate: 30% (15% improvement)
- Monthly carts: 10,000
- Average Order Value (AOV): $50

**Revenue Opportunity**: `(0.30 - 0.15) × 10,000 × $50 = $75,000/month`

*Note: Update this with actual numbers from your data after running the pipeline.*

## Troubleshooting

### Empty Conversions

**Symptom**: All conversion rates are zero or NULL

**Solution**: Verify event labels match expected values:
- `view` (not "View" or "views")
- `addtocart` (not "add to cart" or "AddToCart")
- `transaction` (not "Transaction" or "purchase")

Check your source data and adjust the ETL script if needed.

### Large CSV Files

**Symptom**: Processing is slow with very large datasets

**Solution**: 
1. Convert to Parquet format in `data/interim/`
2. Update `etl_funnel.py` to read from Parquet instead of CSV
3. DuckDB handles Parquet efficiently with `read_parquet()`

### Tableau Publishing Issues

**Symptom**: Cannot publish dashboard to Tableau Public

**Solution**: 
- Ensure at least one worksheet exists before publishing
- Check data size limits (free tier has restrictions)
- Verify CSV files are properly formatted (headers, UTF-8 encoding)

### Missing Raw Data

**Symptom**: ETL script fails with "file not found" error

**Solution**: 
- Verify `data/raw/` directory exists
- Ensure CSV files are placed in `data/raw/` (not subdirectories)
- Check file names match expected patterns (e.g., `events.csv`)

## Tableau Dashboard Publishing

### Creating the Dashboard

1. **Open Tableau Public** and sign in to your free account

2. **Connect to Data**:
   - Click "Connect to Data" → "Text File"
   - Select `artifacts/funnel_session.csv`
   - Add additional data sources: `sku_dropoff.csv` and `cohort_retention.csv` (use Data → Edit Data Source)

3. **Create Calculated Fields**:
   - `View_to_Cart %`: `SUM([has_cart]) / SUM([has_view])`
   - `Cart_to_Purchase %`: `SUM([has_purchase]) / SUM([has_cart])`
   - `Total Revenue Opportunity`: Create based on your AOV data

4. **Create Worksheets**:
   - **KPIs Dashboard**: Cards showing conversion rates and totals
   - **Funnel Visualization**: Bar or step chart showing view → cart → purchase flow
   - **SKU Drop-off Table**: Table sorted by `cart_to_purchase_rate` (lowest first)
   - **Cohort Heatmap**: Heatmap showing retention by cohort month (optional)

5. **Build Dashboard**:
   - Create a new dashboard
   - Add KPI cards at top
   - Add funnel visualization
   - Add SKU drop-off table with filters
   - Add date/device/category filters as needed

6. **Publish**:
   - Click "Server" → "Tableau Public" → "Save to Tableau Public"
   - Choose a workbook name and description
   - Set privacy settings (Public dashboards are viewable by anyone)
   - Click "Save"

7. **Share the Link**:
   - After publishing, copy the public URL
   - Add it to this README under "Dashboard Link" section below

### Dashboard Link

*Add your Tableau Public dashboard URL here after publishing*

## Success Criteria

- ✅ Reproducible execution from clean clone in ≤10 minutes
- ✅ Tableau Public dashboard link accessible to anyone
- ✅ View→Cart, Cart→Purchase, AOV, Revenue visible by date, device, category
- ✅ ≥3 SQL window functions used; uplift model included
- ✅ README includes quantified opportunity statement

## License

[Add your license here]

