# Information Architecture & User Flows

## Sitemap

```
/
├── index.html (HOME)
│   └── Purpose: Landing page, overview, quick actions
│
├── pipeline.html (PIPELINE)
│   └── Purpose: ETL execution, status monitoring, summary metrics
│
├── analytics.html (ANALYTICS)
│   └── Purpose: Analytics query execution, export summaries
│
├── artifacts.html (ARTIFACTS)
│   └── Purpose: Artifact listing, file path copying, row counts
│
└── style.html (STYLE)
    └── Purpose: Design token reference (developer documentation)
```

## Navigation Model

### Primary Navigation
- **Location:** Top of every page (`.nav-header` card)
- **Structure:** Horizontal list of links
- **Items:** HOME | PIPELINE | ANALYTICS | ARTIFACTS | STYLE
- **Behavior:**
  - Active page highlighted (`.nav-link.active`)
  - Hover state: `--text-primary` color
  - No breadcrumbs (flat navigation model)
  - Always visible (sticky or fixed)

### Secondary Navigation
- **Location:** Context-specific (within page content)
- **Examples:**
  - Quick Actions section on HOME page
  - "CONTINUE TO ANALYTICS" link on Pipeline page
  - "VIEW ALL ARTIFACTS" link on Analytics page

## User Flows

### Flow 1: Complete Pipeline Execution (Happy Path)

```
START: HOME page
  ↓
Click "RUN PIPELINE" link
  ↓
PIPELINE page loads
  ↓
Click "RUN" button
  ↓
[Backend executes etl_funnel.py]
  ↓
Status updates:
  - "RUNNING..." (loading state)
  - Progress indicators (if available)
  ↓
Completion:
  - Status: "✅ Pipeline complete!"
  - Summary metrics displayed:
    * Events loaded: X
    * Sessions created: Y
    * View→Cart: Z%
    * Cart→Purchase: W%
  ↓
Click "CONTINUE TO ANALYTICS" link
  ↓
ANALYTICS page loads
  ↓
Click "RUN" button
  ↓
[Backend executes run_analytics.py]
  ↓
Status updates:
  - "RUNNING..."
  ↓
Completion:
  - Status: "✅ Analytics queries complete!"
  - Export summaries:
    * sku_dropoff.csv — rows: X
    * cohort_retention.csv — rows: Y
  ↓
Click "VIEW ALL ARTIFACTS" link
  ↓
ARTIFACTS page loads
  ↓
Copy file paths as needed
  ↓
END: Ready for Tableau import
```

### Flow 2: Error Handling (Missing Data)

```
START: PIPELINE page
  ↓
Click "RUN" button
  ↓
[Backend attempts to execute etl_funnel.py]
  ↓
Error detected: "events.csv not found"
  ↓
Status displays:
  - Status: "❌ Error: events.csv not found in data/raw/"
  - Visual: Error state (red text)
  - Action hint: "Please download the RetailRocket dataset..."
  ↓
User fixes data file location
  ↓
Click "RUN" button again
  ↓
Success path continues...
```

### Flow  יכול להיות Flow 3: Quick Artifact Access (Direct Navigation)

```
START: User knows artifacts exist
  ↓
Direct navigation to ARTIFACTS page
  ↓
ARTIFACTS page loads
  ↓
Artifact list displays:
  - funnel_session.csv
  - funnel_steps.csv
  - sku_dropoff.csv
  - cohort_retention.csv
  ↓
Click copy icon for desired file
  ↓
Path copied to clipboard
  ↓
Visual feedback: Checkmark icon (2s)
  ↓
User pastes path into Tableau
  ↓
END
```

### Flow 4: Re-run After Data Update

```
START: PIPELINE page
  ↓
Review "Last Run Summary" section:
  - Events: 10,000 · Sessions: 5,000
  - View→Cart: 15% · Cart→Purchase: 8%
  ↓
User updates data/raw/events.csv
  ↓
Click "RUN" button
  ↓
Pipeline executes with new data
  ↓
Summary updates:
  - Events: 12,000 · Sessions: 6,000
  - View→Cart: 16% · Cart→Purchase: 9%
  ↓
User confirms metrics changed as expected
  ↓
Optionally run analytics queries if needed
  ↓
END
```

### Flow 5: First-Time User Onboarding

```
START: HOME page (first visit)
  ↓
User reads:
  - Tagline: "E-COMMERCE REVENUE FUNNEL ANALYZER"
  - Feature tiles: UNIVERSAL | OPEN SOURCE | NO API KEYS | NO MCP
  ↓
Clicks "RUN PIPELINE" (Quick Actions)
  ↓
PIPELINE page loads
  ↓
Sees instruction: "Ensure data/raw/events.csv exists before running."
  ↓
User may:
  A) Op 1: Go back, download data, then return
  B) Op 2: Attempt run → see error → download data → retry
  ↓
After successful run, user continues to ANALYTICS
  ↓
First-time user may explore STYLE page for design reference
  ↓
END
```

## Empty States

### Pipeline Page (No Previous Run)
- **Condition:** No `artifacts/funnel_session.csv` exists
- **Display:**
  - "Last Run Summary" section shows placeholder: "Events: — · Steps: — · Sessions: —"
  - Status message: "Click RUN to execute the ETL pipeline."
  - No error state (expected first-run behavior)

### Analytics Page (No Artifacts)
- **Condition:** No `artifacts/funnel_steps.csv` exists
- **Display:**
  - Status message: "⚠️ Requires artifacts/funnel_steps.csv (run pipeline first)."
  - "RUN" button disabled (or shows error on click)
  - Export summaries show "—" for row counts

### Artifacts Page (No Files)
- **Condition:** `artifacts/` directory empty or missing files
- **Display:**
  - Empty state message: "No artifacts found. Run pipeline and analytics first."
  - Links back to PIPELINE and ANALYTICS pages

## Route Rules

- **Default route:** `/` → `index.html`
- **Deep links:** All pages accessible via direct URL
- **No redirects:** Pages load directly (client-side routing not needed)
- **404 handling:** If file not found, browser default (consider custom 404 page later)

## State Management

### Client-Side State
- **Navigation active state:** Derived from `window.location.pathname`
- **Copy button feedback:** Managed via JavaScript (2s timeout)
- **Form inputs:** None (all actions via buttons/links)

### Server-Side State (Artifacts)
- **Pipeline status:** Determined by file existence in `artifacts/` directory
- **Last run metrics:** Parsed from `funnel_session.csv` (if exists)
- **Row counts:** Read from CSV files on page load or after execution

### Loading States
- **Button disabled:** While pipeline/analytics executing
- **Status message:** Shows "RUNNING..." with spinner (if implemented)
- **Progress indication:** Optional (poll artifact directory or read stdout)

