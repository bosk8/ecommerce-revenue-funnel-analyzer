## ADDED Requirements

### Requirement: Global Navigation
Global navigation SHALL include routes: `/`, `/pipeline`, `/analytics`, `/artifacts`, `/style` with uppercase labels and `.nav` styling.

#### Scenario: Active route indication
- **WHEN** a route is active
- **THEN** label uses `--text-primary`; inactive uses `--text-muted`

### Requirement: Breadcrumbs (Derived)
Where nested pages exist in future, breadcrumbs SHALL use meta styling `.meta-sm` and `--text-subtle` for non-active segments.

#### Scenario: Keyboard navigation
- **WHEN** tabbing through nav
- **THEN** focus-visible outline uses `--border-color` and items are reachable in logical order


