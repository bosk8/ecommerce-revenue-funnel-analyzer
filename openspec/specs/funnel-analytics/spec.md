# funnel-analytics Specification

## Purpose
TBD - created by archiving change implement-funnel-analyzer. Update Purpose after archive.
## Requirements
### Requirement: SKU Drop-off Analysis
The system SHALL identify SKUs with low cart-to-purchase conversion rates using SQL window functions and ranking.

#### Scenario: Calculate conversion rates per SKU
- **WHEN** SKUs have been added to cart and potentially purchased
- **THEN** the system SHALL calculate cart_to_purchase_rate as purchases/carts using NULLIF to handle division by zero, with LEFT JOIN between carted and purchased CTEs

#### Scenario: Rank low converting SKUs
- **WHEN** cart-to-purchase rates are calculated
- **THEN** the system SHALL rank SKUs by conversion rate (lowest first) using RANK() OVER window function

#### Scenario: Filter high-volume SKUs
- **WHEN** ranking SKUs by conversion rate
- **THEN** the system SHALL only include SKUs with >=50 carts using QUALIFY clause

#### Scenario: Handle zero purchases
- **WHEN** a SKU has carts but zero purchases
- **THEN** the system SHALL return 0.0 for cart_to_purchase_rate (not NULL) using COALESCE

### Requirement: Cohort Retention Analysis
The system SHALL calculate monthly cohort retention rates for users who made purchases.

#### Scenario: Identify first purchase cohort
- **WHEN** transaction events exist in funnel_steps
- **THEN** the system SHALL create first_purchase CTE identifying each user's first purchase date using MIN(ts) with GROUP BY user_id

#### Scenario: Assign cohort months
- **WHEN** first purchase dates are identified
- **THEN** the system SHALL assign cohort_month using DATE_TRUNC('month', first_purchase_date) to group users into monthly cohorts

#### Scenario: Calculate monthly activity
- **WHEN** cohorts are assigned
- **THEN** the system SHALL identify month_active for each purchase transaction using DATE_TRUNC('month', ts) joined with cohorts

#### Scenario: Compute retention rates
- **WHEN** cohort and activity data are available
- **THEN** the system SHALL calculate retention as active_users/cohort_size using COUNT DISTINCT with window functions, handling division by zero with NULLIF

### Requirement: Conversion Rate Metrics
The system SHALL compute view-to-cart and cart-to-purchase conversion rates at session level.

#### Scenario: View-to-cart rate
- **WHEN** session-level flags are available
- **THEN** the system SHALL compute view_to_cart_rate as SUM(has_cart)/SUM(has_view) across all sessions

#### Scenario: Cart-to-purchase rate
- **WHEN** session-level flags are available
- **THEN** the system SHALL compute cart_to_purchase_rate as SUM(has_purchase)/SUM(has_cart) across all sessions

#### Scenario: Handle zero division
- **WHEN** calculating rates with zero denominators (e.g., no views or no carts)
- **THEN** the system SHALL return NULL or 0.0 appropriately to avoid division by zero errors

### Requirement: Uplift Model
The system SHALL calculate revenue uplift opportunity based on target conversion rate improvements.

#### Scenario: Calculate revenue uplift
- **WHEN** current rates, target rates, cart volumes, and AOV are available
- **THEN** the system SHALL calculate uplift as (target_rate - current_rate) x carts x AOV

#### Scenario: Monthly uplift projection
- **WHEN** uplift is calculated per conversion point
- **THEN** the system SHALL provide monthly projections for quantified opportunity statements (e.g., "+$50k/mo if cart->purchase +15%")

