# Style Compliance Matrix

Per screen/component, list exact `style.md` tokens used.

Home
- Container: `layout.containerMax`, `colors.bg.elev1`, spacing `spacing.2xl`, `spacing.md`
- Cards: `colors.surface.card`, `borders.outer`, `colors.border.neutral`, `colors.shadow.tint`, radii `radii.sm`
- Grid: `layout.gridColsMobile|gridColsDesktop`
- Labels: `fontFamily.ui`, `fontSize.md`, `colors.text.muted`, uppercase, letter-spacing `.05em`

Pipeline
- Buttons (derived): text `colors.text.muted` → hover `colors.text.primary`; border `colors.border.neutral`; `borders.thin`; `radii.sm`; spacing `spacing.sm|spacing.md`
- Status text: `colors.text.subtle` / `colors.text.primary`

Analytics
- Same as Pipeline; table rows rendered as cards

Artifacts
- Copy button: `.copy-btn`, `.copy-icon` uses `colors.text.dim` → `#d4d4d8` hover; `.check-icon` uses `colors.accent.success`

Style
- Token listing reflects `style.md` CSS variables and JSON tokens


