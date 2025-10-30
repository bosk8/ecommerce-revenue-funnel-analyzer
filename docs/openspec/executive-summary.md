# Executive Summary

## Project Goals

The E-Commerce Revenue Funnel Analyzer provides a web-based interface for data analysts and business stakeholders to:

1. **Execute ETL pipelines** to process raw e-commerce event data into sessionized funnel metrics
2. **Run analytics queries** to identify revenue leakage opportunities (SKU drop-off, cohort retention)
3. **View and export artifacts** (CSV files) for Tableau dashboard integration
4. **Monitor pipeline status** and validate data quality through real-time feedback

**Success Metrics:**
- Reproducible execution from clean clone in ≤10 minutes
- Clear visibility into conversion rates (View→Cart, Cart→Purchase)
- Actionable insights via SKU-level drop-off analysis
- Accessible data exports for downstream analytics tools

## Primary Personas

### 1. Data Analyst (Primary)
- **Goal:** Run pipeline, analyze results, export for Tableau
- **Technical Level:** Intermediate (comfortable with SQL, command-line tools)
- **Context:** May run pipelines multiple times as data updates; needs quick access to artifacts
- **Pain Points:** Manual CLI execution, lack of visual feedback during processing

### 2. Business Analyst (Secondary)
- **Goal:** Understand funnel metrics, identify revenue opportunities
- **Technical Level:** Beginner (limited command-line experience)
- **Context:** Needs visual summaries and easy artifact access
- **Pain Points:** Cannot interpret raw CSV files without context

## Major User Flows

### Flow 1: Initial Setup & First Run
1. User lands on **HOME** page
2. Clicks **RUN PIPELINE** → navigates to Pipeline page
3. Clicks **RUN** button → ETL executes
4. Sees progress/status updates
5. Views summary metrics (events, sessions, conversion rates)
6. Clicks BENEFIT: **CONTINUE TO ANALYTICS**
7. Runs analytics queries → views export summary
8. Navigates to **ARTIFACTS** → copies file paths for Tableau

### Flow 2: Re-analysis (Data Updates)
1. User returns to **PIPELINE** page
2. Reviews "Last Run Summary" to verify previous state
3. Clicks **RUN** to re-execute with new data
4. Confirms metrics changed as expected
5. Runs analytics if needed
6. Downloads/exports updated artifacts

### Flow 3: Quick Artifact Access
1. User goes directly to **ARTIFACTS** page
2. Copies file paths to clipboard
3. Opens Tableau and imports CSVs
4. Returns to verify artifact row counts if needed

### Flow 4: Error Recovery
1. User runs pipeline but sees error status
2. Reads error message (e.g., "events.csv not found")
3. Corrects data file location/format
4. Retries pipeline execution
5. Confirms success via status message

## Constraints

### Technical Constraints
- **Backend:** Python scripts executed via command-line (no REST API)
- **Architecture:** Static HTML + JavaScript (no server-side rendering)
- **Data:** Large CSV files (performance considerations for parsing)
- **Browser:** Modern browsers with ES6+ support

### Design Constraints
- **Style System:** Strict adherence to `style.md` (Bosk8 design tokens)
- **Responsive:** Mobile-first, breakpoints at 768px (tablet) and 1024px (desktop)
- **Accessibility:** WCAG 2.2 AA minimum
- **Performance:** UI interactions <200ms, data processing feedback within 2s

### Business Constraints
- **No Authentication:** Single-user tool (local execution)
- **No Persistence:** State not saved between page reloads (stateless UI)
- **File-based:** All communication via file system (artifacts directory)

## Key Assumptions

1. **Backend Integration:** UI will execute Python scripts via Web API or similar (to be implemented)
2. **Data Format:** Raw events follow RetailRocket schema (user_id, timestamp, event, itemid)
3. **File Permissions:** UI has read/write access to `artifacts/` directory
4. **User Context:** Single-user environment, no concurrent pipeline executions
5. **Browser Support:** Chrome, Firefox, Safari, Edge (latest 2 versions)

## Open Questions

1. **Backend Integration Method:**
   - Q: Should UI call Python scripts via subprocess (local) or REST API (server)?
   - Assumption: Local subprocess execution for MVP; can be upgraded to API later
   - Logged in Style Decisions Log

2. **Real-time Progress:**
   - Q: How to stream pipeline progress updates to UI?
   - Assumption: Polling artifact directory or reading stdout/stderr files
   - Logged in Style Decisions Log

3. **Error Handling Granularity:**
   - Q: Should errors be displayed inline per-step or as summary?
   - Assumption: Summary-level errors with expandable details
   - Logged in Style Decisions Log

4. **Table Visualization:**
   - Q: Should SKU drop-off data be displayed as interactive table in UI?
   - Assumption: Yes, with sortable columns and copy-to-clipboard for paths
   - Logged in Style Decisions Log

