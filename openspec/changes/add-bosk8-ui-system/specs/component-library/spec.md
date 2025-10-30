## ADDED Requirements

### Requirement: Cards and Surfaces
Cards SHALL use `--surface-card`, outer ring with `--border-outer-w` and `--border-color`, and soft shadow `--shadow-tint`.

#### Scenario: Default card
- **WHEN** rendering `.card`
- **THEN** background uses `--surface-card` and box-shadow `0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint)`

### Requirement: Grid Tiles
Grid tiles SHALL use `grid-tiles` with mobile 2 columns, ≥768px 4 columns; `.tile` padding and center alignment.

#### Scenario: Responsive grid
- **WHEN** width ≥ 768px
- **THEN** `grid-template-columns: repeat(4, 1fr)`; otherwise 2 columns

### Requirement: Typography Labels
Meta/labels SHALL be uppercase monospace with `letter-spacing: 0.05em` and use `--text-muted`.

#### Scenario: Tagline
- **WHEN** `.tagline`
- **THEN** font-size 1rem, centered, uppercase, JetBrains Mono

### Requirement: Links and Copy Button
Links SHALL default to `--text-muted`, hover to `--text-primary`; copy button/icon states as defined.

#### Scenario: Link hover
- **WHEN** hovering `.link`
- **THEN** color changes to `--text-primary` and underline with 4px offset

### Requirement: Tooltip
Tooltip SHALL use absolute positioning, border `--border-w`/`--border-color`, background `--surface-card`, font `.625rem`, with hover trigger ≥768px and tap/active on mobile.

#### Scenario: Hover desktop
- **WHEN** hovering `.tooltip-trigger` on ≥768px
- **THEN** child `.tooltip` becomes visible with opacity 1

### Requirement: FAQ / Accordion
Accordion items SHALL have bottom border and hover background `#18181b`; question `.faq-q` uppercase `.75rem`; answer toggled via `.active`.

#### Scenario: Expand answer
- **WHEN** toggling to active
- **THEN** `.faq-a.active` displays block

### Requirement: Buttons (Derived)
Buttons SHALL derive from tokens without inventing new colors: text `--text-muted` default, hover `--text-primary`, border `--border-color`, radius `--r-sm`, padding from `--space-0_75`/`--space-1`.

#### Scenario: Button states
- **WHEN** hover
- **THEN** text color becomes `--text-primary`; focus-visible uses 2px outline `--border-color` over `--surface-card`

### Requirement: Inputs (Derived)
Inputs SHALL use background `--surface-card`, text `--text-primary`, placeholder `--text-dim`, border `--border-w`/`--border-color`, radius `--r-sm`.

#### Scenario: Input focus
- **WHEN** input receives focus
- **THEN** outline 2px `--border-color` and maintain minimal motion (<200ms)

### Accessibility (Components)
All interactive components MUST be keyboard operable (Tab, Shift+Tab, Enter/Space) and meet WCAG 2.2 AA. Tooltips not focus traps; accordions expose `aria-expanded` on trigger and `aria-controls`.

#### Scenario: Keyboard activation
- **WHEN** focusing a button or accordion trigger and pressing Enter/Space
- **THEN** it activates and toggles state with ARIA updated


