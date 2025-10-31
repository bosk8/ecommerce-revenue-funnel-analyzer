# Quick Start Guide - All 4 Projects

This guide provides step-by-step instructions to start and test each project.

---

## PROJECT 1: E-Commerce Revenue Funnel Analyzer

### Setup

```bash
cd 01-ecommerce-revenue-funnel-analyzer

# Install dependencies
pip install -r env/requirements.txt

# Prepare data (download RetailRocket dataset)
# Place events.csv in data/raw/
```

### Start Server

```bash
# From project root
python app/server.py
```

**Server will start at**: `http://127.0.0.1:5501/`

### Test UI

1. **Open Browser**: Navigate to `http://127.0.0.1:5501/`
2. **HOME Page**: Verify navigation links work
3. **PIPELINE Page**: 
   - Click "RUN" button
   - Verify status updates
   - Check summary metrics appear
4. **ANALYTICS Page**:
   - Click "RUN" button
   - Verify export row counts update
5. **ARTIFACTS Page**:
   - Verify artifact list displays
   - Click copy buttons
   - Verify clipboard functionality

### Verify Features

- ✅ Navigation between all pages
- ✅ Pipeline execution button
- ✅ Analytics execution button
- ✅ Status messages (info/success/error)
- ✅ Copy to clipboard buttons
- ✅ Row counts display

---

## PROJECT 2: Customer Churn Prediction Dashboard

### Setup

```bash
cd 02-customer-churn-prediction-dashboard

# Install dependencies
pip install -r env/requirements.txt

# Train model (if not already trained)
python src/train.py

# Generate scores (if not already generated)
python src/score.py
```

### Start Streamlit App

```bash
# From project root
streamlit run app/streamlit_app.py
```

**App will start at**: `http://localhost:8501`

### Test UI

1. **Open Browser**: Navigate to `http://localhost:8501`
2. **Dashboard View**:
   - Verify ROC AUC displays (if metrics.json exists)
   - Verify top 500 at-risk customers table displays
3. **Single Customer Scoring (Sidebar)**:
   - Fill out form fields
   - Click "SCORE CUSTOMER"
   - Verify churn probability displays

### Verify Features

- ✅ Dashboard header displays
- ✅ ROC AUC metric displays
- ✅ Top risk customers table
- ✅ Single customer scoring form
- ✅ Prediction output

---

## PROJECT 3: Marketing AB Test Analyzer

### Setup

```bash
cd 03-marketing-ab-test-analyzer

# Install dependencies (use project/config/requirements.txt)
pip install -r project/config/requirements.txt

# Or use root env/requirements.txt
pip install -r env/requirements.txt
```

### Start Streamlit App

```bash
# From project root (or project/ directory)
streamlit run app/ab_app.py

# Or from project/ directory:
cd project
streamlit run app/ab_app.py
```

**App will start at**: `http://localhost:8501`

### Test UI

1. **Open Browser**: Navigate to `http://localhost:8501`
2. **Aggregated Data Method**:
   - Enter conversion counts for A and B
   - Enter sample sizes for A and B
   - Click "Run Analysis"
   - Verify results display (p-value, confidence interval)
3. **CSV Upload Method**:
   - Select CSV file
   - Upload file
   - Verify analysis runs automatically
   - Verify results display

### Verify Features

- ✅ Aggregated data input
- ✅ CSV file upload
- ✅ Statistical analysis execution
- ✅ Results display
- ✅ Visualization charts

---

## PROJECT 4: Realtime Supply Chain KPIs

### Setup

```bash
cd 04-realtime-supply-chain-kpi-dbt-snowflake

# Note: This project uses mock API data
# Backend API implementation required for production use
```

### Test UI (Mock Data)

**Option 1: Open HTML files directly**

```bash
# Open in browser
open ui/index.html  # macOS
xdg-open ui/index.html  # Linux
start ui/index.html  # Windows
```

**Option 2: Use local file server**

```bash
# Python 3
python -m http.server 8000

# Navigate to: http://localhost:8000/ui/
```

### Test UI

1. **Dashboard Page** (`index.html`):
   - Verify KPI cards display (mock data loads after 500ms)
   - Verify warehouse table populates
   - Click "Filters" button
   - Verify filter panel opens
   - Select date range and warehouses
   - Click "Apply"
   - Verify data refreshes

2. **Warehouse Detail Page** (`warehouse.html`):
   - Verify warehouse header displays
   - Verify KPI cards display
   - Verify orders table displays

3. **Data Quality Page** (`data-quality.html`):
   - Verify freshness table displays
   - Verify test results table displays

### Verify Features

- ✅ Dashboard KPI cards
- ✅ Warehouse table
- ✅ Filter panel functionality
- ✅ Date range selection
- ✅ Warehouse checkbox selection
- ✅ Navigation links

### ⚠️ Important Note

**This project uses mock API data**. For production use:
1. Implement backend API server (Flask/FastAPI)
2. Connect to dbt/Snowflake data sources
3. Update API calls in `ui/app.js`, `ui/warehouse.js`, `ui/data-quality.js`

---

## Testing Checklist

### Project 1 ✅

- [ ] Server starts without errors
- [ ] All pages load correctly
- [ ] Navigation links work
- [ ] Pipeline button executes
- [ ] Analytics button executes
- [ ] Status messages display
- [ ] Copy buttons work
- [ ] Error handling works (missing data file)

### Project 2 ✅

- [ ] Streamlit app starts
- [ ] Dashboard displays correctly
- [ ] Model loads (if available)
- [ ] Metrics display (if available)
- [ ] Top risk table displays (if available)
- [ ] Scoring form functional
- [ ] Prediction displays

### Project 3 ✅

- [ ] Streamlit app starts
- [ ] Aggregated data input works
- [ ] CSV upload works
- [ ] Analysis executes
- [ ] Results display correctly
- [ ] Charts render

### Project 4 ⚠️

- [ ] HTML pages load correctly
- [ ] Mock data displays
- [ ] Filter panel works
- [ ] Navigation works
- [ ] All buttons functional
- [ ] **Backend API required for production**

---

## Common Issues & Solutions

### Issue: ModuleNotFoundError

**Solution**:
```bash
# Install dependencies
pip install -r env/requirements.txt
# or
pip install -r project/config/requirements.txt
```

### Issue: Port Already in Use

**Solution**:
- Change port in server configuration
- Or stop existing process using the port

### Issue: File Not Found Errors

**Solution**:
- Verify data files exist in expected locations
- Check file paths in code match actual structure
- Ensure you're running from correct directory

### Issue: API Errors (Project 4)

**Solution**:
- This is expected - Project 4 uses mock API
- Implement backend API for production use
- See project specifications for API endpoint requirements

---

## Next Steps

1. **Install Dependencies**: Use `requirements.txt` for each project
2. **Prepare Data**: Download/place required data files
3. **Start Applications**: Follow instructions above
4. **Test Features**: Use checklists above
5. **Report Issues**: Document any problems found

---

## Support

For detailed information about each project:
- See `README.md` in each project directory
- See `COMPREHENSIVE_UI_UX_TEST_REPORT.md` for complete test results
- Check project-specific documentation in `docs/` or `specs/` directories

