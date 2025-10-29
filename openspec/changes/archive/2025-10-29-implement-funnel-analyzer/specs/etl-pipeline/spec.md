## ADDED Requirements

### Requirement: Event Data Loading
The system SHALL load raw e-commerce event data from CSV files into DuckDB with proper type casting.

#### Scenario: Load RetailRocket events CSV
- **WHEN** events.csv is located in data/raw/
- **THEN** events are loaded into DuckDB table with columns: user_id (VARCHAR), ts (TIMESTAMP), event_type (VARCHAR from 'event' column), sku (VARCHAR from 'itemid' column)

#### Scenario: Handle missing raw data directory
- **WHEN** data/raw/ directory does not exist or contains no CSV files
- **THEN** the system SHALL raise a clear error message indicating missing data source

### Requirement: Sessionization with Inactivity Gap
The system SHALL create sessions by grouping user events with ≤30 minute inactivity gaps using SQL window functions.

#### Scenario: Identify session boundaries
- **WHEN** events for a user have timestamps with gaps >30 minutes
- **THEN** the system SHALL assign a new session_id to events after each 30+ minute gap using LAG() window function

#### Scenario: First event for user
- **WHEN** processing the first event for a user (no previous timestamp)
- **THEN** the system SHALL create a new session using NULL check in LAG() window function

#### Scenario: Session sequence assignment
- **WHEN** session boundaries are identified
- **THEN** the system SHALL assign sequential session numbers per user using SUM() window function with ROWS UNBOUNDED PRECEDING

### Requirement: Funnel Step Identification
The system SHALL identify funnel steps (view, addtocart, transaction) within each session and order them chronologically.

#### Scenario: Create funnel_steps table
- **WHEN** sessionized events are available
- **THEN** the system SHALL create funnel_steps table with: user_id, session_id (user_id + session_seq), ts, event_type, sku, step_order (using ROW_NUMBER() window function)

#### Scenario: Step ordering
- **WHEN** multiple events occur in a session
- **THEN** steps SHALL be ordered chronologically per session using ROW_NUMBER() OVER (PARTITION BY user_id, session_seq ORDER BY ts)

### Requirement: Session-Level Funnel Flags
The system SHALL generate session-level flags indicating presence of view, cart, and purchase events.

#### Scenario: Generate funnel flags
- **WHEN** funnel_steps table contains events
- **THEN** the system SHALL create funnel_session table with: session_id, has_view (1 if view event exists, else 0), has_cart (1 if addtocart exists, else 0), has_purchase (1 if transaction exists, else 0) using MAX(CASE WHEN...) aggregations

#### Scenario: Multiple events of same type
- **WHEN** a session contains multiple view, cart, or purchase events
- **THEN** flags SHALL be set to 1 if any event of that type exists (MAX() ensures single 1 value)

