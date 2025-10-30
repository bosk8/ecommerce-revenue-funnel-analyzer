## ADDED Requirements

### Requirement: Single Source of Truth Tokens
All visual and interaction decisions SHALL use tokens from `style.md` without invention of new tokens.

#### Scenario: Token usage
- **WHEN** implementing any component or screen
- **THEN** use exact tokens: `fontFamily.ui`, `fontSize.base|xs|sm|md|lg`, `colors.bg.black|bg.elev1|surface.card|text.primary|text.muted|text.subtle|text.dim|text.linkHover|text.highlight|accent.success|border.neutral|shadow.tint`, `radii.sm|md`, `borders.thin|md|outer`, `spacing.xs|sm|md|lg|xl|2xl|containerPadTop`, `layout.containerMax|gridColsMobile|gridColsDesktop`

### Requirement: CSS Variable Mapping
The system SHALL expose CSS variables exactly as in `style.md` CSS section and media queries.

#### Scenario: Root variables
- **WHEN** initializing the UI foundation
- **THEN** define variables `--font-ui`, `--fs-base`, `--bg-black`, `--bg-elev1`, `--surface-card`, `--text-primary`, `--text-muted`, `--text-subtle`, `--text-dim`, `--text-highlight`, `--accent-success`, `--border-color`, `--border-w`, `--border-outer-w`, `--shadow-tint`, `--r-sm`, `--r-md`, `--space-0_5`, `--space-0_75`, `--space-1`, `--space-1_5`, `--space-2`, `--space-4`

#### Scenario: Responsive border widths
- **WHEN** viewport width ≥ 1024px
- **THEN** elevate `--border-w` to 1.5px and `--border-outer-w` to 2px

### Requirement: Base Resets and Container
Global resets and base styles SHALL match `style.md` Base block.

#### Scenario: Base
- **WHEN** rendering `html`, `body`, `main.bosk8`, `.container`
- **THEN** apply rules matching `style.md` Base (font-size, background colors, font-family, min-height, padding, container max width)


