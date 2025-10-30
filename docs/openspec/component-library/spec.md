# Interactive Component Library

## Component 1: Navigation Header

### Purpose
Global navigation bar present on all pages, providing access to main sections.

### Props/Variants
- None (stateless component)

### Structure
```html
<nav class="card nav-header" style="padding: var(--space-1);">
  <div class="nav-links">
    <a href="./index.html" class="nav-link">HOME</a>
    <!-- ... other links ... -->
  </div>
</nav>
```

### Style Token References
- Container: `.card` → `--surface-card`, `--border-outer-w`, `--border-color`, `--shadow-tint`, `--r-sm`
- Padding: `--space-1`
- Links: `.nav-link` → `--text-muted`, surface card background
- Font: `--font-ui`, uppercase, `0.05em` letter-spacing, `0.75rem` size

### States

**Default:**
- Link color: `--text-muted`
- No background change

**Hover:**
- Link color: `--text-primary`
- Transition: `color .15s`

**Active (Current Page):**
- Link color: `--text-primary`
- Font weight: `500`
- `aria-current="page"` attribute

**Focus:**
- Outline: `2px solid --border-color`, `2px` offset

### Accessibility
- Semantic `<nav>` element
- Active link: `aria-current="page"`
- All links keyboard accessible
- Focus indicators visible

### Example Usage
```html
<nav class="card nav-header" style="padding: var(--space-1);">
  <div class="nav-links">
    <a href="./index.html" class="nav-link">HOME</a>
    <a href="./pipeline.html" class="nav-link">PIPELINE</a>
    <a href="./analytics.html" class="nav-link">ANALYTICS</a>
    <a href="./artifacts.html" class="nav-link">ARTIFACTS</a>
    <a href="./style.html" class="nav-link">STYLE</a>
  </div>
</nav>
```

---

## Component 2: Button Primary

### Purpose
Primary action button for executing pipelines, analytics, and other main operations.

### Props/Variants
- `disabled` (boolean): Disables button interaction
- `aria-live` (string): Screen reader announcement (optional, e.g., "polite")
- `title` (string): Tooltip text

### Structure
```html
<button class="btn btn-primary" disabled aria-live="polite" title="Run ETL Pipeline">
  <span>RUN</span>
</button>
```

### Style Token References
- Base: `.btn` → `--border-w`, `--border-color`, `--r-sm`, `--text-muted`, `--font-ui`
- Padding: `--space-0_75` vertical, `--space-1` horizontal
- Font: Uppercase, `0.05em` letter-spacing, `0.75rem` size
- Primary variant: `.btn-primary` → `--surface-card` background

### States

**Default:**
- Border: `--border-w solid --border-color`
- Background: `--surface-card` (from `.btn-primary`)
- Color: `--text-muted`
- Cursor: `pointer`

**Hover (not disabled):**
- Color: `--text-primary`
- Border color: `--text-primary`
- Transition: `all .15s`

**Focus:**
- Outline: `2px solid --border-color`, `2px` offset

**Disabled:**
- Opacity: `0.5`
- Cursor: `not-allowed`
- No hover effects

**Active (while pressing):**
- Optional: Slight scale down (not specified in style.md, omit for now)

### RFC/Accessibility
- Semantic `<button>` element
- Keyboard accessible (Enter/Space)
- Disabled state announced to screen readers
- `aria-live` for status updates (optional)

### Example Usage
```html
<!-- Enabled state -->
<button class="btn btn-primary" aria-live="polite" title="Run ETL Pipeline">
  <span>RUN</span>
</button>

<!-- Disabled state -->
<button class="btn btn-primary" disabled title="Processing...">
  <span>RUNNING...</span>
</button>
```

---

## Component 3: Status Message

### Purpose
Display status feedback for pipeline/analytics execution (info, success, error).

### Props/Variants
- `variant` (string): `info` | `success` | `error`
- `id` (string): For JavaScript targeting (optional)

### Structure
```html
<div class="status info" id="etl-status">
  Click RUN to execute the ETL pipeline.
</div>
```

### Style Token References
- Base: `.status` → `0.75rem` font size, `--text-subtle` color
- Variants:
  - `.status.info` → `--text-subtle`
  - `.status.success` → `--accent-success`
  - `.status.error` → `#ef4444` (derived, see Style Decisions Log)

### States

**Info (Default):**
- Color: `--text-subtle`
- Message: Neutral/informational text

**Success:**
- Color: `--accent-success`
- Message: "✅ [success message]"

**Error:**
- Color: `#ef4444` (error red, not in style.md, see Style Decisions Log)
- Message: "❌ Error: [error message]"

### Accessibility
- `aria-live="polite"` on parent container (button) for status updates
- Screen readers announce status changes

### Example Usage
```html
<!-- Info state -->
<div class="status info" id="etl-status">
  Click RUN to execute the ETL pipeline.
</div>

<!-- Success state -->
<div class="status success">
  ✅ Pipeline complete! Events: 10,000, Sessions: 5,000
</div>

<!-- Error state -->
<div class="status error">
  ❌ Error: events.csv not found in data/raw/
</div>
```

---

## Component 4: Copy Button

### Purpose
Copy file paths to clipboard with visual feedback.

### Props/Variants
- `data-copy` (string): Text to copy to clipboard
- `aria-label` (string): Accessible label (required)

### Structure
```html
<button class="copy-btn" data-copy="artifacts/funnel_session.csv" aria-label="Copy path">
  <span class="copy-icon">⧉</span>
  <span class="check-icon" style="display: none;">✓</span>
</button>
```

### Style Token References
- Base: `.copy-btn` → Transparent background, no border
- Icon: `.copy-icon` → `--text-dim` color
- Success icon: `.check-icon` → `--accent-success` color

### States

**Default:**
- Copy icon: Visible, `--text-dim` color
- Check icon: Hidden (`display: none`)

**Hover:**
- Copy icon: `#d4d4d8` color (derived from `--text-dim`, see Style Decisions Log)

**Active (After Click):**
- Copy icon: Hidden
- Check icon: Visible, `--accent-success` color
- After 2s: Reverts to default (JavaScript-managed)

### Accessibility
- `aria-label` provides context
- Screen reader announcement: "Copied to clipboard" (via `aria-live` region)

### Example Usage
```html
<button class="copy-btn" data-copy="artifacts/funnel_session.csv" aria-label="Copy path">
  <span class="copy-icon">⧉</span>
  <span class="check-icon" style="display: none;">✓</span>
</button>
```

---

## Component 5: Card

### Purpose
Container for page sections, providing visual separation and depth.

### Props/Variants
- None (base component)

### Structure
```html
<section class="card" style="padding: var(--space-1);">
  <!-- content -->
</section>
```

### Style Token References
- Background: `--surface-card`
- Shadow: `0 0 0 --border-outer-w --border-color, 0 1px 2px --shadow-tint`
- Border radius: `--r-sm`
- Padding: Custom (via inline style, typically `--space-1`)

### States

**Default:**
- Background: `--surface-card`
- Shadow applied (subtle depth)

**Hover:**
- No state changes (card is container, not interactive)

### Accessibility
- Semantic container (use `<section>`, `<article>`, or `<div>` as appropriate)
- No interactive behavior

### Example Usage
```html
<section class="card" style="padding: var(--space-1);">
  <div class="meta-md">SECTION TITLE</div>
  <div class="meta-sm" style="color: var(--text-subtle);">
    Section content...
  </div>
</section>
```

---

## Component 6: Link

### Purpose
Text links for navigation and actions.

### Props/Variants
- `href` (string): Destination URL
- Content: Link text

### Structure
```html
<a href="./此类pipeline.html" class="link">RUN PIPELINE</a>
```

### Style Token References
- Color: `--text-muted`
- Font: Inherits from body (`.bosk8`)
- Transition: `all .15s`

### States

**Default:**
- Color: `--text-muted`
- Text decoration: None

**Hover:**
- Color: `--text-primary`
- Text decoration: Underline
- Text underline offset: `4px`

的责任:**
- Outline: `2px solid --border-color`, `2px` offset

### Accessibility
- Semantic `<a>` element
- Keyboard accessible
- Clear visual focus indicators

### Example Usage
```html
<a href="./pipeline.html" class="link">RUN PIPELINE</a>
<a href="./artifacts.html" class="link">→ VIEW ALL ARTIFACTS</a>
```

---

## Component 7: Feature Tiles Grid

### Purpose
Display feature highlights in a grid layout (used on HOME page).

### Props/Variants
- None (layout component)

### Structure
```html
<section class="card grid-tiles border-b">
  <div class="tile border-r">UNIVERSAL</div>
  <div class="tile">OPEN SOURCE</div>
  <div class="tile border-r">NO API KEYS</div>
  <div class="tile">NO MCP</div>
</section>
```

### Style Token References
- Container: `.card.grid-tiles` → Grid layout, `border-b` variant
- Grid columns:
  - Mobile: `repeat(2, 1fr)` (from `--layout.gridColsMobile`)
  - Desktop (≥768px): `repeat(4, 1fr)` (from `--layout.gridColsDesktop`)
- Tile: `.tile` → `1.5rem` vertical padding, `1rem` horizontal padding, center text
- Border variants: `.border-r` → `--border-w solid --border-color` (right border)

### States

**Default:**
- Grid items displayed in columns
- Center-aligned text

**Hover:**
- Optional: Subtle background change (not specified in style.md, omit for now)

### Responsive Behavior
- Mobile (<768px): 2 columns
- Desktop (≥768px): 4 columns

### Accessibility
- Semantic container
- Text readable with sufficient contrast

### Example Usage
See HOME page specification.

---

## Component 8: Meta Text (Labels/Headings)

### Purpose
Uppercase labels and section headings following Bosk8 typography rules.

### Props/Variants
- Size: `.meta-sm` (0.75rem) | `.meta-md` (0.875rem)

### Structure
```html
<div class="meta-md">SECTION TITLE</div>
<div class="meta-sm" style="color: var(--text-subtle);">Subtitle text</div>
```

### Style Token References
- Base: `.meta`, `.meta-sm`, `.meta-md` → `--font-ui cotton`, uppercase, `0.05em` letter-spacing
- Sizes:
  - `.meta-sm`: `0.75rem` (from `--fontSize.sm` mapped to `xs` in style.md: `0.625rem`, but actual CSS uses `0.75rem` — see Style Decisions Log)
  - `.meta-md`: `0.875rem` (from `--fontSize.md`)
- Color: Default `--text-muted`, can override with `--text-subtle` or `--text-dim`

### States

**Default:**
- Uppercase text
- Specified color

**No interactive states** (text-only component)

### Accessibility
- Semantic HTML (use `<h1>`, `<h2>`, `<div>`, etc. as appropriate)
味 - Ensure heading hierarchy

### Example Usage
```html
<div class="meta-md" style="margin-bottom: var(--space-1);">RUN ETL</div>
<div class="meta-sm" style="color: var(--text-subtle);">Description text</div>
```

