# tableau-artifacts Specification

## Purpose
TBD - created by archiving change implement-funnel-analyzer. Update Purpose after archive.
## Requirements
### Requirement: CSV Artifact Generation
The system SHALL export analytical outputs as CSV files optimized for Tableau Public consumption.

#### Scenario: Export funnel_session data
- **WHEN** funnel_session table is created
- **THEN** the system SHALL export to artifacts/funnel_session.csv with HEADER row and comma delimiter using DuckDB COPY command

#### Scenario: Export SKU drop-off results
- **WHEN** SKU drop-off SQL query completes
- **THEN** the system SHALL export results to artifacts/sku_dropoff.csv with proper schema (sku, carts, purchases, cart_to_purchase_rate, low_conv_rank)

#### Scenario: Export cohort retention results
- **WHEN** cohort retention SQL query completes
- **THEN** the system SHALL export results to artifacts/cohort_retention.csv with schema (cohort_month, month_active, cohort_size, active_users, retention)

#### Scenario: Artifact directory creation
- **WHEN** artifacts directory does not exist
- **THEN** the system SHALL create the directory automatically with mkdir(parents=True, exist_ok=True)

### Requirement: Tableau-Compatible Schema
All CSV artifacts SHALL conform to Tableau Public import requirements.

#### Scenario: Valid CSV format
- **WHEN** artifacts are generated
- **THEN** CSV files SHALL use comma delimiters, proper header rows, and UTF-8 encoding

#### Scenario: Date/timestamp formatting
- **WHEN** date or timestamp columns are exported
- **THEN** values SHALL be formatted in a way that Tableau can automatically parse (ISO 8601 or standard date formats)

#### Scenario: Numeric data types
- **WHEN** numeric columns (rates, counts, ranks) are exported
- **THEN** values SHALL be properly formatted as numbers (no string prefixes, proper decimal notation)

### Requirement: Artifact Metadata for Dashboard
The system SHALL provide sufficient data columns for Tableau dashboard visualizations.

#### Scenario: Funnel visualization data
- **WHEN** funnel_session.csv is exported
- **THEN** the file SHALL contain session_id, has_view, has_cart, has_purchase flags needed for funnel step calculations

#### Scenario: SKU analysis data
- **WHEN** sku_dropoff.csv is exported
- **THEN** the file SHALL contain sku, carts, purchases, cart_to_purchase_rate, low_conv_rank for sorting and filtering in Tableau

#### Scenario: Cohort heatmap data
- **WHEN** cohort_retention.csv is exported
- **THEN** the file SHALL contain cohort_month, month_active, retention for heatmap visualization

