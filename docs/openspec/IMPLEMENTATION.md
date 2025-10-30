# Implementation Guide

## Overview

The UI system has been fully implemented according to the specifications. This document provides setup and usage instructions.

## File Structure

```
project-root/
├── ui/
│   ├── index.html          # HOME page
│   ├── pipeline.html       # PIPELINE page (with ETL execution)
│   ├── analytics.html      # ANALYTICS page (with query execution)
│   ├── artifacts.html       # ARTIFACTS page (with row counts)
│   ├── style.html          # STYLE reference page
│   ├── bosk8.css          # Main stylesheet (complete with all components)
│   ├── app.js              # Navigation and copy functionality
│   └── api.js              # Backend API integration
├── src/
│   ├── server.py           # Flask backend API server
│   ├── etl_funnel.py      # ETL pipeline script
│   ├── run_analytics.py    # Analytics query script
│   └── utils.py            # Utility functions
└── openspec/               # Complete specification documents
```

## Setup Instructions

### 1. Install Dependencies

```bash
# Activate virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install Python dependencies
pip install -r env/requirements.txt
```

### 2. Start Backend Server

```bash
# From project root
python src/server.py
```

The server will:
- Start on `http://localhost:5000`
- Serve UI files from `ui/` directory
- Provide API endpoints at `/api/*`

### 3. Access UI

Open your browser and navigate to:
- `http://localhost:5000/` (HOME page)
- `http://localhost:5000/pipeline.html` (PIPELINE)
- `http://localhost:5000/analytics.html` (ANALYTICS)
- `http://localhost:5000/artifacts.html` (ARTIFACTS)
- `http://localhost:5000/style.html` (STYLE reference)

## API Endpoints

### POST /api/pipeline/run
Execute ETL pipeline.

**Response (Success):**
```json
{
  "status": "success",
  "metrics": {
    "events_count": 10000,
    "steps_count": 15000,
    "session_count": 5000,
    "view_to_cart_rate": 15.5,
    "cart_to_purchase_rate": 8.2
  }
}
```

**Response (Error):**
```json
{
  "status": "error",
  "error_code": "FileNotFoundError",
  "message": "events.csv not found in data/raw/"
}
```

### POST /api/analytics/run
Execute analytics queries.

**Response (Success):**
```json
{
  "status": "success",
  "exports": [
    {"file": "sku_dropoff.csv", "rows": 150},
    {"file": "cohort_retention.csv", "rows": 45}
  ]
}
```

### GET /api/artifacts
Get list of artifacts with row counts.

**Response:**
```json
{
  "files": [
    {"name": "funnel_session.csv", "exists": true, "rows": 5000},
    {"name": "funnel_steps.csv", "exists": true, "rows": 15000},
    {"name": "sku_dropoff.csv", "exists": true, "rows": 150},
    {"name": "cohort_retention.csv", "exists": true, "rows": 45}
  ]
}
```

### GET /api/pipeline/summary
Get pipeline summary metrics from artifacts.

**Response:**
```json
{
  "status": "success",
  "metrics": {
    "events_count": 10000,
    "steps_count": 15000,
    "session_count": 5000,
    "view_to_cart_rate": 15.5,
    "cart_to_purchase_rate": 8.2
  }
}
```

## Features Implemented

### ✅ Complete Implementation

1. **Navigation System**
   - Active page highlighting
   - Keyboard accessible
   - Screen reader support

2. **Pipeline Execution**
   - Button with loading states
   - Status updates (info/success/error)
   - Summary metrics display
   - Error handling

3. **Analytics Execution**
   - Button with loading states
   - Status updates
   - Export row counts display
   - Error handling

4. **Artifacts Management**
   - Dynamic row counting
   - Copy to clipboard functionality
   - Empty state handling
   - Auto-refresh (every 30s)

5. **Accessibility**
   - WCAG 2.2 AA compliance
   - Keyboard navigation
   - Screen reader support
   - Touch target sizes (mobile)

6. **Responsive Design**
   - Mobile-first layout
   - Breakpoints at 768px and 1024px
   - Touch-optimized buttons

7. **Error Handling**
   - Clear error messages
   - Retry functionality
   - Helpful error hints

8. **Empty States**
   - Empty artifacts list
   - Guidance messages
   - Action links

## Usage Flow

### First-Time Setup

1. **Prepare Data**
   - Download RetailRocket dataset
   - Place `events.csv` in `data/raw/`

2. **Start Server**
   ```bash
   python src/server.py
   ```

3. **Run Pipeline**
   - Navigate to `http://localhost:5000/pipeline.html`
   - Click "RUN" button
   - Wait for completion
   - View summary metrics

4. **Run Analytics**
   - Navigate to `http://localhost:5000/analytics.html`
   - Click "RUN" button
   - Wait for completion
   - View export row counts

5. **View Artifacts**
   - Navigate to `http://localhost:5000/artifacts.html`
   - Copy file paths for Tableau
   - View row counts

### Subsequent Runs

1. Update `data/raw/events.csv` (if needed)
2. Run pipeline (overwrites previous artifacts)
3. Run analytics (overwrites previous exports)
4. View updated artifacts

## Troubleshooting

### Backend Server Not Running

**Symptom:** Buttons show errors about backend server

**Solution:** 
```bash
python src/server.py
```

### Data File Not Found

**Symptom:** Pipeline execution fails with "events.csv not found"

**Solution:** 
- Verify `data/raw/events.csv` exists
- Check file permissions
- Ensure file is correctly named

### Port Already in Use

**Symptom:** Server fails to start with "Address already in use"

**Solution:**
- Change port in `src/server.py`: `app.run(..., port=5001)`
- Update `API_BASE_URL` in `ui/api.js`: `const API_BASE_URL = '/api';`

### CORS Errors

**Symptom:** Browser console shows CORS errors

**Solution:**
- Ensure `flask-cors` is installed: `pip install flask-cors`
- Verify CORS is enabled in `src/server.py`: `CORS(app)`

## Development Notes

### Frontend Files
- `ui/app.js`: Navigation and copy functionality
- `ui/api.js`: Backend API integration
- `ui/bosk8.css`: Complete stylesheet with all components

### Backend Files
- `src/server.py`: Flask API server
- Executes Python scripts via subprocess
- Provides REST API endpoints
- Serves static UI files

### Integration Points
- UI calls `/api/pipeline/run` for ETL execution
- UI calls `/api/analytics/run` for analytics execution
- UI calls `/api/artifacts` for artifact listing
- UI calls `/api/pipeline/summary` for metrics

## Testing Checklist

- [ ] Server starts without errors
- [ ] Home page loads correctly
- [ ] Navigation works on all pages
- [ ] Pipeline execution works (with valid data)
- [ ] Analytics execution works (after pipeline)
- [ ] Artifacts page shows row counts
- [ ] Copy to clipboard works
- [ ] Empty states display correctly
- [ ] Error messages are clear
- [ ] Mobile layout works (resize browser)
- [ ] Keyboard navigation works
- [ ] Screen reader announces status updates

## Next Steps

1. **Enhance Error Handling**
   - Add more specific error messages
   - Implement error recovery flows

2. **Progress Indication**
   - Add real-time progress updates
   - Implement progress bars (optional)

3. **Data Visualization**
   - Add charts/graphs for metrics
   - Display funnel visualization

4. **Performance Optimization**
   - Minify CSS/JS for production
   - Add caching for static files

5. **Testing**
   - Add automated tests
   - Integration tests for API
   - E2E tests for UI flows

