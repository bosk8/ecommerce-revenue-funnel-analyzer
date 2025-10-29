## Context

This is a greenfield data analytics project for analyzing e-commerce revenue funnel conversion. The system must identify revenue leakage points and quantify improvement opportunities. The project targets reproducible execution (≤10 minutes from clean clone), production of clean data artifacts for visualization, and publication of a Tableau Public dashboard accessible to anyone.

## Goals / Non-Goals

### Goals
- Reproducible ETL pipeline using DuckDB and Python
- Sessionization with 30-minute inactivity gap logic
- Funnel conversion analysis (view → cart → purchase)
- SKU-level drop-off identification
- Cohort retention analysis
- Uplift modeling for revenue opportunity quantification
- Tableau-optimized CSV artifacts
- Complete project documentation with quantified insights

### Non-Goals
- Identity stitching across devices/sessions
- Attribution modeling for marketing channels
- Paid media data joins
- Real-time processing or streaming
- Multi-tenant or enterprise deployment
- User authentication or authorization
- API endpoints or web services

## Decisions

### Decision: DuckDB for SQL Processing
- **Rationale**: In-memory analytical database with excellent CSV/Parquet support, no server setup required, perfect for ETL workflows
- **Alternatives considered**: PostgreSQL (requires server), SQLite (less analytical features), Pandas-only (more verbose for complex window functions)

### Decision: SQL Window Functions for Sessionization
- **Rationale**: Efficient sessionization using LAG() and SUM() window functions; leverages SQL strengths for time-series event processing
- **Alternatives considered**: Pandas groupby (slower for large datasets), custom Python loops (complex, error-prone)

### Decision: CSV Artifacts for Tableau
- **Rationale**: Tableau Public best supports CSV; Parquet would require additional conversion steps
- **Alternatives considered**: Parquet (better compression but requires conversion), Database connection (not supported by Tableau Public free tier)

### Decision: Python 3.10+ Virtual Environment
- **Rationale**: Standard isolation, compatible with modern pandas/duckdb versions
- **Alternatives considered**: Poetry/Pipenv (more complexity for simple project), Conda (heavier weight)

### Decision: RetailRocket Dataset (Recommended)
- **Rationale**: Contains all required events (view, addtocart, transaction) in single dataset
- **Alternatives considered**: UCI Online Retail II (transactions only, less funnel detail)

## Risks / Trade-offs

### Data Acquisition Risk
- **Risk**: Kaggle API may require authentication or rate limiting
- **Mitigation**: Document manual download fallback; provide clear instructions

### Tableau Public Limitations
- **Risk**: Free tier has data size limits and requires public publishing
- **Mitigation**: Ensure artifacts are optimized (filter low-volume SKUs in queries); document publishing process

### Performance with Large Datasets
- **Risk**: Very large CSV files may slow processing
- **Mitigation**: Document Parquet intermediate storage option; use DuckDB's efficient CSV reader

### Event Label Inconsistency
- **Risk**: Source data may use different event names (e.g., "add to cart" vs "addtocart")
- **Mitigation**: Document data validation steps; include troubleshooting section for event name mismatches

## Migration Plan

Not applicable - greenfield project with no existing system to migrate from.

## Open Questions

- Should we support both RetailRocket and UCI datasets with conditional logic, or choose one primary dataset?
- What's the expected dataset size? (affects whether intermediate Parquet storage is needed)
- Are there specific timezone requirements for timestamp parsing?
