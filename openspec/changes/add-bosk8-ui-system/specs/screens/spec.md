## ADDED Requirements

### Requirement: Screen List and Purpose
The system SHALL provide the following screens:
- Home: overview and quick actions
- Pipeline: run ETL, show progress and validation summary
- Analytics: run SQL exports and show row counts
- Artifacts: list CSVs with copy-path actions
- Style: token reference and examples (read-only)

#### Scenario: Navigation presence
- **WHEN** visiting any route
- **THEN** global nav/top meta is present with uppercase labels

### Requirement: Layout Grid and Container
Screens SHALL use `.container` width `min(1100px, 90vw)`, grid `grid-tiles` where applicable, and `main.bosk8` with `padding-top: 10rem`.

#### Scenario: Responsive tiles
- **WHEN** on Home or Style
- **THEN** use two-column grid on mobile and four-column grid ≥768px

### Requirement: States and Feedback
Each interactive action SHALL define states: default, hover, focus-visible, active, disabled, error, loading (<200ms transitions).

#### Scenario: Loading feedback
- **WHEN** running ETL/Analytics
- **THEN** show loading state on the action and disable repeated triggers until completion or failure

### Requirement: Artifacts Listing
Artifacts screen SHALL read from `artifacts/` and render entries with `.card` rows and `.copy-btn` to copy absolute paths.

#### Scenario: Copy path success
- **WHEN** user clicks copy
- **THEN** swap icon to `.check-icon` momentarily and announce via ARIA live region


