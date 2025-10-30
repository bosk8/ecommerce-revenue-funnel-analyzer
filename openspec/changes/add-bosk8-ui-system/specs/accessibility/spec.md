## ADDED Requirements

### Requirement: WCAG 2.2 AA Contrast and Motion
The UI MUST meet WCAG 2.2 AA contrast and limit transitions under 200ms, per `style.md`.

#### Scenario: Reduced motion
- **WHEN** animating hover/focus changes
- **THEN** transitions ≤ 200ms and no parallax/auto animations

### Requirement: Keyboard Navigation
All interactive elements MUST be reachable by Tab/Shift+Tab, activatable by Enter/Space, and show `:focus-visible` outline 2px `--border-color`.

#### Scenario: Focus outline
- **WHEN** focusing a button or link
- **THEN** outline appears with offset 2px per `style.md`

### Requirement: ARIA semantics
Accordions MUST use `aria-expanded` on trigger and `role="region"` with `aria-labelledby` for content. Tooltips MUST not trap focus and should announce via `aria-describedby` if used for essential info.

#### Scenario: Accordion state
- **WHEN** toggled
- **THEN** `aria-expanded` reflects state and content id matches `aria-controls`


