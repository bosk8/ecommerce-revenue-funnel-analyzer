## Why

The project needs a complete e-commerce revenue funnel analyzer system to identify and quantify revenue leakage from view → add-to-cart → purchase conversion. This system will provide actionable insights through reproducible ETL pipelines, clean data artifacts, and a published Tableau dashboard.

## What Changes

- **ADDED** `etl-pipeline` capability: Load raw e-commerce event data, implement 30-minute sessionization logic using SQL window functions, and identify funnel steps (view → addtocart → transaction) within sessions
- **ADDED** `funnel-analytics` capability: Compute conversion rates, SKU drop-off analysis, cohort retention, and uplift models using SQL window functions and analytical queries
- **ADDED** `tableau-artifacts` capability: Generate CSV artifacts optimized for Tableau Public dashboard consumption with proper schema and metadata
- **ADDED** `project-foundation` capability: Establish repository structure, Python virtual environment, dependency management, and comprehensive README with quantified opportunity statements

## Impact

- Affected specs: All new capabilities (etl-pipeline, funnel-analytics, tableau-artifacts, project-foundation)
- Affected code: Entire codebase (greenfield project)
- External dependencies: DuckDB, Pandas, PyArrow, JupyterLab, Tableau Public account
- Data requirements: E-commerce event dataset (RetailRocket recommended or UCI Online Retail II)
