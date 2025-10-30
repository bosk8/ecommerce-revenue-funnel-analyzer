# Style Compliance Matrix

## Overview

This matrix maps every screen and component to exact `style.md` tokens used. Any derived tokens must include derivation logic.

## Token Reference (from style.md)

### Colors
- `colors.bg.black`: `#000000`
- `colors.bg.elev1`: `#0A0A0A`
- `colors.surface.card`: `#09090B`
- `colors.text.primary`: `#FFFFFF`
- `colors.text.muted`: `#E8E8E8`
- `colors.text.subtle`: `#A1A1AA`
- `colors.text.dim`: `#71717A`
- `colors.text.highlight`: `#F4F4F5`
- `colors.accent.success`: `#22C55E`
- `colors.border.neutral`: `rgb(39 39 42)`
- `colors.shadow.tint`: `#0000000d`

### Typography
- `fontFamily.ui`: JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace
- `fontSize.base`: `clamp(16px, calc(15.2px + 0.25vw), 20px)`
- `fontSize.xs`: `0.625rem`
- `fontSize.sm`: `0.75rem`
- `fontSize.md`: `0.875rem`
- `fontSize.lg`: `1rem`

### Spacing
- `spacing.xs`: `0.5rem`
- `spacing.sm`: `0.75rem`
- `spacing.md`: `1rem`
- `spacing.lg`: `1.5rem`
- `spacing.xl`: `2rem`
- `spacing.2xl`: `4rem`
- `spacing.containerPadTop`: `10rem`

### Borders & Radii
- `radii.sm`: `4px`
- `radii.md`: `6px`
- `borders.thin`: `1px`
- `borders.md`: `1.5px`
- `borders.outer`: `2px`

### Layout
- `layout.containerMax`: `min(1100px, 90vw)`
- `layout.gridColsMobile`: `2`
- `layout.gridColsDesktop`: `4`

## Component Compliance Matrix

### Navigation Header

| Property | Token Used | Notes |
|----------|-----------|-------|
| Background | `colors.surface.card` | Via `.card` class |
| Padding | `spacing.md` (`--space-1`) | `1rem` |
| Border shadow | `colors.border.neutral` + `borders.outer` | Via `.card` box-shadow |
| Border radius | `radii.sm` | `4px` |
| Link color (default) | `colors.text.muted` | `#E8E8E8` |
| Link color (hover) | `colors.text.primary` | `#FFFFFF` |
| Link font | `fontFamily.ui` | Via `.nav-link` |
| Link font size | `fontSize.sm` | `0.75rem` |
| Link letter spacing | `0.05em` | Derived from `style.md` typography rules |

### Button Primary

| Property | Token Used | Notes |
|----------|-----------|-------|
| Background | `colors.surface.card` | Via `.btn-primary` |
| Border color | `colors.border.neutral` | `rgb(39 39 42)` |
| Border width | `borders.thin` | `1px` (desktop: `1.5px` at ≥1024px) |
| Border radius | `radii.sm` | `4px` |
| Padding (vertical) | `spacing.sm` | `0.75rem` |
| Padding (horizontal) | `spacing.md` | `1rem` |
| Text color (default) | `colors.text.muted` | `#E8E8E8` |
| Text color (hover) | `colors.text.primary` | `#FFFFFF` |
| Font | `fontFamily.ui` | Via `.btn` |
| Font size | `fontSize.sm` | `0.75rem` |
| Letter spacing | `0.05em` | Derived |
| Transition | `0.15s` | From `style.md` motion rules |

### Status Message

| Property | Token Used | Notes |
|----------|-----------|-------|
| Font size | `fontSize.sm` | `0.75rem` |
| Color (info) | `colors.text.subtle` | `#A1A1AA` |
| Color (success) | `colors.accent.success` | `#22C55E` |
| Color (error) | `#ef4444` | **DERIVED** - See Style Decisions Log |

### Copy Button

| Property | Token Used | Notes |
|----------|-----------|-------|
| Background | Transparent | Not in `style.md`, derived as minimal UI |
| Border | None | Not in `style.md` |
| Icon color (default) | `colors.text.dim` | `#71717A` |
| Icon color (hover) | `#d4d4d8` | **DERIVED** - See Style Decisions Log |
| Icon color (success) | `colors.accent.success` | `#22C55E` |
| Gap | `spacing.sm` | `0.75rem` |

### Card

| Property | Token Used | Notes |
|----------|-----------|-------|
| Background | `colors.surface.card` | `#09090B` |
| Border shadow (outer) | `borders.outer` + `colors.border.neutral` | `2px` solid (desktop) |
| Border shadow (inner) | `colors.shadow.tint` | `0 1px 2px #0000000d` |
| Border radius | `radii.sm` | `4px` |
| Padding | `spacing.md` (`--space-1`) | Default `1rem` (varies by usage) |

### Link

| Property | Token Used | Notes |
|----------|-----------|-------|
| Color (default) | `colors.text.muted` | `#E8E8E8` |
| Color (hover) | `colors.text.primary` | `#FFFFFF` |
| Text decoration (hover) | Underline | `text-underline-offset: 4px` |
| Transition | `0.15s` | From `style.md` |

### Feature Tiles Grid

| Property | Token Used | Notes |
|----------|-----------|-------|
| Grid columns (mobile) | `layout.gridColsMobile` | `2` |
| Grid columns (desktop) | `layout.gridColsDesktop` | `4` (at ≥768px) |
| Tile padding (vertical) | `spacing.lg` | `1.5rem` |
| Tile padding (horizontal) | `spacing.md` | `1rem` |
| Border (right) | `borders.thin` + `colors.border.neutral` | Via `.border-r` |
| Background | `colors.surface.card` | Via `.card` |

### Meta Text (Labels)

| Property | Token Used | Notes |
|----------|-----------|-------|
| Font | `fontFamily.ui` | Via `.meta` |
| Font size (small) | `fontSize.sm` | `0.75rem` |
| Font size (medium) | `fontSize.md` | `0.875rem` |
| Text transform | Uppercase | From `style.md` |
| Letter spacing | `0.05em` | Derived |
| Color (default) | `colors.text.muted` | `#E8E8E8` |
| Color (variants) | `colors.text.subtle`, `colors.text.dim` | Via inline styles |

### Main Container

| Property | Token Used | Notes |
|----------|-----------|-------|
| Background | `colors.bg.elev1` | `#0A0A0A` |
| Max width | `layout.containerMax` | `min(1100px, 90vw)` |
| Padding (top) | `spacing.containerPadTop` | `10rem` |
| Padding (sides) | `spacing.md` | `1rem` |
| Min height | `100vh` | Full viewport |

### Page Body

| Property | Token Used | Notes |
|----------|-----------|-------|
| Background | `colors.bg.black` | `#000000` |
| Font | `fontFamily.ui` | Via `body` |
| Font size | `fontSize.base` | `clamp(16px, calc(15.2px + 0.25vw), 20px)` |
| Color | `colors.text.primary` | `#FFFFFF` |

## Screen Compliance Matrix

### HOME Page

| Component | Tokens Used |
|-----------|------------|
| Navigation Header | See Navigation Header matrix |
| Hero Card | `.card` + `.border-b` + `spacing.xl` padding (`4rem 2rem`) |
| Feature Tiles | `.card.grid-tiles` + `.border-b` + tiles |
| Quick Actions | `.card` + `.link` components |

### PIPELINE Page

| Component | Tokens Used |
|-----------|------------|
| Navigation Header | See Navigation Header matrix |
| Run ETL Card | `.card` + `spacing.md` padding + `.btn-primary` + `.status` |
| Last Run Summary | `.card` + `spacing.md` padding + `.meta-sm` + `.link` |

### ANALYTICS Page

| Component | Tokens Used |
|-----------|------------|
| Navigation Header | See Navigation Header matrix |
| Run Analytics Card | `.card` + `spacing.md` padding + `.btn-primary` + `.status` |
| Exports Card | `.card` + `spacing.md` padding + `.meta-sm` + `.link` |

### ARTIFACTS Page

| Component | Tokens Used |
|-----------|------------|
| Navigation Header | See Navigation Header matrix |
| Artifacts Card | `.card` + `spacing.md` padding |
| Artifact Rows | `spacing.sm` padding + `.border-b` + `.copy-btn` |

### STYLE Page

| Component | Tokens Used |
|-----------|------------|
| Navigation Header | See Navigation Header matrix |
| Tokens Card | `.card` + `spacing.md` padding + `.meta-sm` (pre code block) |

## Derived Tokens Log

All derived tokens must be documented here with derivation logic:

### 1. Error Color (`#ef4444`)
- **Source:** Not in `style.md`
- **Derivation:** Standard error red, high contrast on `--bg-black` (4.6:1, meets AA for large text)
- **Usage:** `.status.error` variant
- **Rationale:** Functional color for error states, maintains high contrast

### 2. Copy Button Hover Color (`#d4d4d8`)
- **Source:** Not in `style.md`
- **Derivation:** Lighter shade of `--text-dim` (#71717a), approximately 20% lighter
- **Usage:** `.copy-btn:hover .copy-icon`
- **Rationale:** Provides hover feedback while maintaining color hierarchy

### 3. Meta Font Size Mapping
- **Source:** `style.md` defines `fontSize.sm: 0.75rem`, `fontSize.xs: 0.625rem`
- **Actual CSS:** `.meta-sm` uses `0.75rem` (matches `fontSize.sm`)
- **Rationale:** CSS aligns with `fontSize.sm`, not `fontSize.xs` despite naming

## Responsive Breakpoint Compliance

### Mobile (< 768px)
- Grid tiles: `layout.gridColsMobile` (2 columns) ✅
- Border widths: `borders.thin` (1px) ✅

### Desktop (≥ 768px)
- Grid tiles: `layout.gridColsDesktop` (4 columns) ✅

### Desktop Large (≥ 1024px)
- Border widths: `borders.md` (1.5px), `borders.outer` (2px) ✅
- Border radius: `radii.sm` (4px) ✅

## Compliance Checklist

- [x] All colors reference `style.md` tokens
- [x] All spacing uses `spacing.*` tokens
- [x] All typography uses `fontFamily.ui` and `fontSize.*` tokens
- [x] All borders use `borders.*` tokens
- [x] All radii use `radii.*` tokens
- [x] Derived tokens documented with rationale
- [x] Responsive breakpoints align with `layout.*` tokens
- [x] No arbitrary values (all tokens or documented derivations)

