# Project Structure

## Complete Single-Folder Organization

All application files are now consolidated in a single `app/` folder:

```
01-ecommerce-revenue-funnel-analyzer/
├── app/                      # ALL APPLICATION FILES (single folder)
│   ├── index.html            # HOME page
│   ├── pipeline.html         # PIPELINE page
│   ├── analytics.html        # ANALYTICS page
│   ├── artifacts.html        # ARTIFACTS page
│   ├── style.html            # STYLE reference page
│   ├── _shared.html          # Shared template
│   ├── bosk8.css             # Main stylesheet
│   ├── app.js                # Navigation and copy functionality
│   ├── api.js                # Backend API integration
│   ├── server.py             # Flask API server
│   ├── etl_funnel.py         # ETL pipeline script
│   ├── run_analytics.py      # Analytics query script
│   └── utils.py              # Utility functions
│
├── artifacts/                # Output CSV files for Tableau
│
├── data/                     # Data files
│   ├── raw/                  # Raw input data (not committed)
│   └── interim/              # Intermediate processed data
│
├── sql/                      # SQL queries
│   ├── sku_dropoff.sql       # SKU drop-off analysis
│   └── cohort_retention.sql  # Cohort retention analysis
│
├── docs/                     # Documentation
│   ├── openspec/             # UI/UX specifications
│   ├── SANITY_CHECK.md       # Sanity check report
│   └── STRUCTURE.md          # This file
│
├── env/                      # Environment configuration
│   └── requirements.txt      # Python dependencies
│
├── notebooks/                # Jupyter notebooks
│   └── 01_eda.ipynb          # Exploratory data analysis
│
├── project-scope.md          # Project requirements
└── README.md                 # Project overview
```

## File References

### HTML Files → CSS/JS
All HTML files in `app/` reference:
- CSS: `./bosk8.css`
- JS: `./app.js` and `./api.js`
- Navigation links: `./*.html` (same folder)

### Backend Server
- Location: `app/server.py`
- Serves all files from: `app/` folder
- Static folder: `app/` (single folder)
- Executes scripts from: `app/` folder

### Python Scripts
- All scripts are in `app/` folder
- `etl_funnel.py`, `run_analytics.py`, `utils.py`, `server.py`
- All reference project root correctly via `Path(__file__).parent.parent`

## Running the Project

### Start Backend Server
```bash
python app/server.py
```

### Access UI
- Open browser to: `http://localhost:5000`

## API Endpoints

All endpoints serve files from `app/` folder:
- `/` → Serves `app/index.html`
- `/api/pipeline/run` → Executes `app/etl_funnel.py`
- `/api/analytics/run` → Executes `app/run_analytics.py`
- `/api/artifacts` → Lists artifacts from `artifacts/`
- `/api/pipeline/summary` → Returns metrics from artifacts

## Benefits of Single Folder Structure

1. **Simplicity**: All application files in one place
2. **Easy Navigation**: No nested folder structure to navigate
3. **Simple Deployment**: Single folder to deploy
4. **Clear Organization**: One folder = all app code
5. **Straightforward Paths**: All references are `./filename` (same folder)
