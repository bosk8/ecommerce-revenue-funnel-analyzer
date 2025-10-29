# project-foundation Specification

## Purpose
TBD - created by archiving change implement-funnel-analyzer. Update Purpose after archive.
## Requirements
### Requirement: Repository Structure
The project SHALL follow a standard directory structure for data, code, SQL, and artifacts.

#### Scenario: Directory creation
- **WHEN** repository is initialized
- **THEN** the following directories SHALL exist: data/raw (source CSVs), data/interim (cleaned parquet), artifacts (CSVs for Tableau), notebooks, sql, src, env

#### Scenario: File organization
- **WHEN** files are created
- **THEN** ETL scripts SHALL be in src/, SQL queries in sql/, Jupyter notebooks in notebooks/, and requirements in env/

### Requirement: Python Environment Setup
The project SHALL provide reproducible Python environment configuration.

#### Scenario: Requirements file
- **WHEN** setting up the project
- **THEN** env/requirements.txt SHALL contain: duckdb>=1.0, pandas>=2.2, pyarrow>=16, jupyterlab

#### Scenario: Virtual environment creation
- **WHEN** user runs setup
- **THEN** instructions SHALL be provided for creating venv with `python -m venv .venv` and activating it

#### Scenario: Dependency installation
- **WHEN** virtual environment is activated
- **THEN** dependencies SHALL be installable via `pip install -r env/requirements.txt`

### Requirement: Data Acquisition Documentation
The project SHALL provide clear instructions for obtaining required datasets.

#### Scenario: RetailRocket dataset instructions
- **WHEN** user needs to acquire data
- **THEN** documentation SHALL specify downloading events.csv and item_properties_part*.csv from Kaggle (RetailRocket e-commerce dataset)

#### Scenario: Alternative dataset support
- **WHEN** RetailRocket is unavailable
- **THEN** documentation SHALL provide instructions for UCI Online Retail II dataset as alternative

#### Scenario: Data placement
- **WHEN** datasets are downloaded
- **THEN** files SHALL be placed in data/raw/ directory (not committed to repository)

### Requirement: README Documentation
The project SHALL include comprehensive README with setup, usage, and quantified insights.

#### Scenario: Setup instructions
- **WHEN** user clones the repository
- **THEN** README.md SHALL provide step-by-step setup instructions including: Python version (3.10+), virtual environment creation, dependency installation, data acquisition steps

#### Scenario: Execution instructions
- **WHEN** user wants to run the pipeline
- **THEN** README.md SHALL document commands: `python src/etl_funnel.py`, SQL execution commands, expected output artifacts

#### Scenario: Quantified opportunity statement
- **WHEN** README is complete
- **THEN** README.md SHALL include a quantified revenue opportunity statement (e.g., "+$50k/mo if cart→purchase +15%") based on uplift model results

#### Scenario: Troubleshooting section
- **WHEN** users encounter common issues
- **THEN** README.md SHALL include troubleshooting guidance for: empty conversions (event label mismatches), large CSV handling (Parquet conversion), Tableau publishing issues

### Requirement: Reproducibility
The entire pipeline SHALL be reproducible from a clean clone in ≤10 minutes.

#### Scenario: Fresh clone execution
- **WHEN** repository is cloned fresh
- **THEN** complete setup and execution SHALL complete in ≤10 minutes (excluding data download time)

#### Scenario: Clean execution
- **WHEN** pipeline runs from scratch
- **THEN** no manual intervention SHALL be required beyond following README instructions

### Requirement: Git Configuration
The project SHALL exclude generated files and sensitive data from version control.

#### Scenario: .gitignore file
- **WHEN** repository is initialized
- **THEN** .gitignore SHALL exclude: raw data files (data/raw/*), virtual environment (.venv/), generated artifacts (artifacts/*), Python cache files (__pycache__/, *.pyc)

#### Scenario: Commit history
- **WHEN** project is complete
- **THEN** git history SHALL contain ≥6 meaningful commits demonstrating incremental development

