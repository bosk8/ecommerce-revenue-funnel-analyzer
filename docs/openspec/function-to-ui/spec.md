# Function-to-UI Mapping

## Overview

Protocol mapping backend Python functions to UI triggers, data contracts, input validation, error handling, and feedback patterns.

## Function 1: ETL Pipeline Execution

### Backend Function
**File:** `src/etl_funnel.py`  
**Function:** `main()`

### UI Trigger
- **Component:** Button Primary (`.btn.btn-primary`) on Pipeline page
- **Action:** Click event
- **Initial State:** Button enabled, status message shows default info text

### Data Contract

**Inputs:**
- None (reads from `data/raw/events.csv`)

**Outputs:**
- **Success:**
  - Files created:
    - `artifacts/funnel_session.csv`
    - `artifacts/funnel_steps.csv`
  - Metrics available (parsed from pipeline stdout or CSV):
    - `events_count` (integer)
    - `steps_count` (integer)
    - `session_count` (integer)
    - `view_to_cart_rate` (float, percentage)
    - `cart_to_purchase_rate` (float, percentage)

**Error Cases:**
- `FileNotFoundError`: `data/raw/events.csv` missing
- `duckdb.Error`: SQL execution failure
- `Exception`: Unexpected errors

### Validation

**Pre-execution:**
- Check if `data/raw/events.csv` exists (optional, can fail fast on execution)
- Verify write permissions for `artifacts/` directory

**Post-execution:**
- Verify `funnel_session.csv` and `funnel_steps.csv` created
- Parse row counts from files
- Validate metrics are numeric and within expected ranges (e.g., rates 0-100%)

### Error States

**File Not Found:**
- **Error Code:** `FileNotFoundError`
- **UI Display:**
  - Status: `.status.error`
  - Message: "❌ Error: events.csv not found in data/raw/. Please download the RetailRocket dataset and place events.csv in data/raw/"
  - Button: Re-enabled (allow retry)

**DuckDB Error:**
- **Error Code:** `duckdb.Error`
- **UI Display:**
  - Status: `.status.error`
  - Message: "❌ DuckDB Error: [error message]"
  - Button: Re-enabled

**Unexpected Error:**
- **Error Code:** `Exception`
- **UI Display:**
  - Status: `.status.error`
  - Message: "❌ Unexpected error: [error message]"
  - Button: Re-enabled

### Feedback Patterns

**Loading State:**
- Button: `disabled` attribute
- Status: "RUNNING..." or spinner (if implemented)
- Prevent multiple concurrent executions

**Success State:**
- Button: Re-enabled
- Status: `.status.success`
- Message: "✅ Pipeline complete! Events: X, Sessions: Y, View→Cart: Z%, Cart→Purchase: W%"
- Summary section: Update with actual metrics
- Auto-navigate hint: "CONTINUE TO ANALYTICS" link visible

**Progress Indication:**
- Optional: Poll `artifacts/` directory for file creation
- Optional: Read stdout/stderr from subprocess if available

### Implementation Notes

**Backend Integration (To Be Implemented):**
- Option A: Execute `python src/etl_funnel.py` via subprocess
- Option B: REST API endpoint that calls `main()` function
- Option C: WebSocket for real-time progress (future enhancement)

**Data Parsing:**
- Parse stdout for metrics (e.g., regex for "Events loaded: X")
- Or read CSV files and calculate metrics client-side
- Or backend returns JSON response with metrics

---

## Function 2: Analytics Query Execution

### Backend Function
**File:** `src/run_analytics.py`  
**Function:** `main()` → calls `run_sql_query()` for each query

### UI Trigger
- **Component:** Button Primary on Analytics page
- **Action:** Click event
- **Initial State:** Button enabled, status message shows default info text

### Data Contract

**Inputs:**
- Prerequisite: `artifacts/funnel_steps.csv` must exist

**Outputs:**
- **Success:**
  - Files created:
    - `artifacts/sku_dropoff.csv`
    - `artifacts/cohort_retention.csv`
  - Row counts available:
    - `sku_dropoff_rows` (integer)
    - `cohort_retention_rows` (integer)

**Error Cases:**
- `FileNotFoundError`: `artifacts/funnel_steps.csv` missing or SQL file missing
- `duckdb.Error`: SQL execution failure
- `Exception`: Unexpected errors

### Validation

**Pre-execution:**
- Check if `artifacts/funnel_steps.csv` exists
- If missing, disable button or show warning

**Post-execution:**
- Verify both CSV files created
- Parse row counts (read first line or count programmatically)

### Error States

**Prerequisite Missing:**
- **Error Code:** `FileNotFoundError` (funnel_steps.csv)
- **UI Display:**
  - Status: `.status.error`
  - Message: "❌ Error: funnel_steps.csv not found. Please run the pipeline first."
  - Button: Re-enabled (allow retry after fixing)

**SQL File Missing:**
- **Error Code:** `FileNotFoundError` (SQL file)
- **UI Display:**
  - Status: `.status.error`
  - Message: "❌ Error: SQL file not found: [path]"
  - Button: Re-enabled

**DuckDB Error:**
- **Error Code:** `duckdb.Error`
- **UI Display:**
  - Status: `.status.error`
  - Message: "❌ DuckDB Error: [error message]"
  - Button: Re-enabled

**Unexpected Error:**
- **Error Code:** `Exception`
- **UI Display:**
  - Status: `.status.error`
  - Message: "❌ Unexpected error: [error message]"
  - Button: Re-enabled

### Feedback Patterns

**Loading State:**
- Button: `disabled`
- Status: "RUNNING..."
- Show progress: "Executing sku_dropoff.sql..." → "Executing cohort_retention.sql..."

**Success State:**
- Button: Re-enabled
- Status: `.status.success`
- Message: "✅ All analytics queries complete! Exported X rows to sku_dropoff.csv, Y rows to cohort_retention.csv"
- Export section: Update row counts

### Implementation Notes

**Backend Integration:**
- Execute `python src/run_analytics.py` via subprocess
- Or REST API endpoint
- Parse stdout for row counts or read CSV files

**Progress Indication:**
- Optional: Stream progress for each SQL file execution
- Display: "Executing sku_dropoff.sql..." → "✅ Exported 150 rows"

---

## Function 3: Artifact File Reading

### Backend Function
**N/A** (File system read)

### UI Trigger
- **Component:** Artifacts page load
- **Action:** Page initialization

### Data Contract

**Inputs:**
- File system: `artifacts/` directory

**Outputs:**
- **Success:**
  - List of files:
    - `funnel_session.csv` (exists: boolean, row_count: integer, optional)
    - `funnel_steps.csv` (exists: boolean, row_count: integer, optional)
    - `mall_dropoff.csv` (exists: boolean, row_count: integer, optional)
    - `cohort_retention.csv` (exists: boolean, row_count: integer, optional)

**Error Cases:**
- Directory not found
- File read permission denied

### Validation

**File Existence:**
- Check each expected file exists
- If missing, show placeholder or "—" in UI

**Row Count Calculation:**
- Read CSV file and count rows (excluding header)
- Cache result (refresh on page reload or manual refresh)

### Error States

**Directory Not Found:**
- **UI Display:**
  - Empty state: 영"No artifacts found. Run pipeline and analytics first."
  - Links to PIPELINE and ANALYTICS pages

**Permission Denied:**
- **UI Display:**
  - Error message: "❌ Error: Permission denied reading artifacts/ directory"

### Feedback Patterns

**Loading State:**
- Optional: Show skeleton/placeholder while reading files

**Success State:**
- Display file list with row counts
- Copy buttons functional

**Empty State:**
- Message: "No artifacts found. Run pipeline and analytics first."
- Action links: PIPELINE, ANALYTICS

### Implementation Notes

**Client-Side Reading:**
- Option A: Backend API endpoint returns file list and row counts
- Option B: JavaScript reads files via File System Access API (limited browser support)
- Option C: Fetch CSV files and count rows (requires CORS/server configuration)

**Recommended:**
- Backend API endpoint: `GET /api/artifacts` returns JSON:
  ```json
  {
    "files": [
      {"name": "funnel_session.csv", "exists": true, "rows": 5000},
      {"name": "funnel_steps.csv", "exists": true, "rows": 15000}
    ]
  }
  ```

---

## Function 4: Copy to Clipboard

### Backend Function
**N/A** (Browser API)

### UI Trigger
- **Component:** Copy Button (`.copy-btn`)
- **Action:** Click event

### Data Contract

**Inputs:**
- `data-copy` attribute: String to copy

**Outputs:**
- **Success:**
  - Clipboard updated
  - Visual feedback: Check icon displayed

**Error Cases:**
- Clipboard API unavailable
- Permission denied

### Validation

**Pre-copy:**
- Verify `data-copy` attribute exists
- Check `navigator.clipboard` availability

### Error States

**Clipboard API Unavailable:**
- **Fallback:** Show text in alert dialog or use `document.execCommand('copy')` (deprecated)

**Permission Denied:**
- **UI Display:**
  - Alert: "Failed to copy to clipboard. Please copy manually: [text]"

### Feedback Patterns

**Success State:**
- Copy icon: Hidden
- Check icon: Visible, `--accent-success` color
- Screen reader: "Copied to clipboard" announcement
- Revert after 2s: Copy icon visible, check icon hidden

### Implementation Notes

**JavaScript Implementation:**
- Use `navigator.clipboard.writeText()`
- Fallback to `document.execCommand('copy')` for older browsers
- Screen reader announcement via `aria-live` region

---

## API Endpoints (Proposed for Backend Integration)

### POST /api/pipeline/run
**Purpose:** Execute ETL pipeline

**Request:**
```json
{}
```

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
**Purpose:** Execute analytics queries

**Request:**
```json
{}
```

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

**Response (Error):**
```json
{
  "status": "error",
  "error_code": "FileNotFoundError",
  "message": "funnel_steps.csv not found. Please run the pipeline first."
}
```

### GET /api/artifacts
**Purpose:** List artifacts and row counts

**Request:**
```
GET /api/artifacts
```

**Response (Success):**
```json
{
  "files": [
    {"name": "funnel_session.csv", "exists": true Monaco, "rows": 5000},
    {"name": "funnel_steps.csv", "exists": true, "rows": 15000},
    {"name": "sku_dropoff.csv", "exists": true, "rows": 150},
    {"name": "cohort_retention.csv", "exists": true, "rows": 45}
  ]
}
```

