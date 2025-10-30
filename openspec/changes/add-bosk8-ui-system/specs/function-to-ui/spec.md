## ADDED Requirements

### Requirement: Map ETL Run to UI Action
The UI SHALL provide an action to run `src/etl_funnel.py` and display validation outputs.

#### Scenario: Run ETL success
- **WHEN** user triggers Run ETL
- **THEN** show loading, then print summary lines (events, steps, sessions; conversion rates) in a `.card` using `.meta-md`

#### Scenario: Missing events.csv
- **WHEN** `FileNotFoundError` raised
- **THEN** show error state card with guidance to place `data/raw/events.csv`

### Requirement: Map Analytics Run to UI Action
The UI SHALL provide an action to run `src/run_analytics.py` and show exported row counts for `sku_dropoff.csv` and `cohort_retention.csv`.

#### Scenario: Missing funnel_steps.csv
- **WHEN** precondition fails
- **THEN** show error instructing to run ETL first

### Requirement: Data Contracts (Inputs/Outputs)
The UI SHALL document and validate inputs/outputs:
- Input: `data/raw/events.csv`
- Outputs: `artifacts/funnel_session.csv`, `artifacts/funnel_steps.csv`, `artifacts/sku_dropoff.csv`, `artifacts/cohort_retention.csv`

#### Scenario: Copy/export actions
- **WHEN** outputs exist
- **THEN** show `.copy-btn` to copy absolute path


