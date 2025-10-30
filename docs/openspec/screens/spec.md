# Screen-by-Screen Specifications

## Screen 1: HOME (index.html)

### Purpose
Landing page providing project overview, feature highlights, and quick navigation to main actions.

### Layout Grid
- **Container:** `min(1100px, 90vw)` (from `--layout.containerMax`)
- **Structure:**
  - Navigation header (full width, card)
  - Hero section (centered, card with border-bottom)
  - Feature tiles (4-column grid on desktop, 2-column on mobile)
  - Quick Actions section (card)

### Components Used
1. **Navigation Header** (`.nav-header`)
2. **Hero Card** (`.card.border-b`)
3. **Feature Tiles** (`.grid-tiles` with `.tile`)
4. **Quick Actions Links** (`.link`)

### Exact Layout Structure

```html
<main class="bosk8">
  <div class="container">
    <!-- Navigation Header -->
    <nav class="card nav-header" style="padding: var(--space-1);">
      <div class="nav-links">
        <a href="./index.html" class="nav-link active">HOME</a>
        <!-- ... other nav links ... -->
      </div>
    </nav>

    <!-- Hero Section -->
    <header class="card border-b" style="padding: 4rem 2rem; display: flex; flex-direction: column; align-items: center; margin-bottom: var(--space-1);">
      <h1 class="tagline">E-COMMERCE REVENUE FUNNEL ANALYZER</h1>
    </header>

    <!-- Feature Tiles -->
    <section class="card grid-tiles border-b" style="margin-bottom: var(--space-1);">
      <div class="tile border-r">UNIVERSAL</div>
      <div class="tile">OPEN SOURCE</div>
      <div class="tile border-r">NO API KEYS</div>
      <div class="tile">NO MCP</div>
    </section>

    <!-- Quick Actions -->
    <section class="card" style="padding: var(--space-1);">
      <div class="meta-md" style="margin-bottom: var(--space-1);">QUICK ACTIONS</div>
      <div style="display: flex; gap: var(--space-1); flex-wrap: wrap;">
        <a class="link" href="./pipeline.html">RUN PIPELINE</a>
        <a class="link" href="./analytics.html">RUN ANALYTICS</a>
        <a class="link" href="./artifacts.html">VIEW ARTIFACTS</a>
        <a class="link" href="./style.html">VIEW STYLE</a>
      </div>
    </section>
  </div>
</main>
```

### Responsive Rules

**Mobile (< 768px):**
- Grid tiles: 2 columns
- Hero padding: `2rem 1rem` (reduced from `4rem 2rem`)
- Navigation: Links wrap to multiple lines

**Tablet (768px - 1023px):**
- Grid tiles: 2 columns (same as mobile)
- Hero padding: `3rem 1.5rem`
- Navigation: Horizontal, no wrapping

**Desktop (≥ 1024px):**
- Grid tiles: 4 columns
- Hero padding: `4rem  مدیریت2rem`
- Border widths: `--border-w: 1.5px`, `--border-outer-w: 2px`

### States

**Default State:**
- All links normal color (`--text-muted`)
- Active nav link highlighted (`--text-primary`)

**Hover State:**
- Links: `--text-primary`, underline with `4px` offset
- Feature tiles: Background change (if implemented: `rgba(255,255,255,0.02)`)

**Focus State:**
- Links: `2px` outline using `--border-color`
- Outline offset: `2px`

---

## Screen 2: PIPELINE (pipeline.html)

### Purpose
Execute ETL pipeline, monitor execution status, view last run summary metrics.

### Layout Grid
- **Container:** `min(1100px, 90vw)`
- **Structure:**
  - Navigation header
  - Run ETL section (card)
  - Last Run Summary section (card)

### Components Used
1. **Navigation Header**
2. **Run ETL Card** (`.card` with button and status)
3. **Button Primary** (`.btn.btn-primary`)
4. **Status Message** (`.status`)
5. **Last Run Summary Card** (`.card` with metrics display)

### Exact Layout Structure

```html
<main class="bosk8">
  <div class="container">
    <!-- Navigation Header -->
    <nav class="card nav-header" style="padding: var(--space-1);">
      <!-- ... nav links ... -->
    </nav>

    <!-- Run ETL Section -->
    <section class="card" style="padding: var(--space-1); margin-bottom: var(--space-1);">
      <div class="meta-md" style="margin-bottom: var(--space-1);">RUN ETL</div>
      <div class="meta-sm" style="color: var(--text-subtle); margin-bottom: var(--space-1);">
        Ensure data/raw/events.csv exists before running.
      </div>
      <div style="display: flex; gap: var(--space-1); flex-wrap: wrap; align-items: center;">
        <button class="btn btn-primary" aria-live="polite" title="Run ETL Pipeline">
          <span>RUN</span>
        </button>
        <div class="status info" id="etl-status">
          Click RUN to execute the ETL pipeline.
        </div>
      </div>
    </section>

    <!-- Last Run Summary -->
    <section class="card" style="padding: var(--space-1);">
      <div class="meta-md" style="margin-bottom: var(--space-1);">LAST RUN SUMMARY</div>
      <div class="meta-sm" style="color: var(--text-subtle); margin-bottom: var(--space-0_5);">
        Events: — · Steps: — · Sessions: —
      </div>
      <div class="meta-sm" style="color: var(--text-subtle);">
        View→Cart: — · Cart→Purchase: —
      </div>
      <div style="margin-top: var(--space-1);">
        <a href="./analytics.html" class="link">→ CONTINUE TO ANALYTICS</a>
      </div>
    </section>
  </div>
</main>
```

### Responsive Rules

**Mobile:**
- Button and status stack vertically if needed (flex-wrap)
- Metrics display: Single line per metric (wrap if needed)

**Desktop:**
- Button and status remain horizontal
- Metrics: Multiple per line

### States

**Default State:**
- Button: Enabled, normal border color
- Status: `--text-subtle` color, info message
- Summary: Placeholder values ("—") if no previous run

**Loading State:**
- Button: `disabled` attribute, `opacity: 0.5`, `cursor: not-allowed`
- Status: "RUNNING..." message (or spinner if implemented)
- Button text: May change to "RUNNING..." (optional)

**Success State:**
- Status: `.status.success`, `--accent-success` color
- Message: "✅ Pipeline complete! Events: X, Sessions: Y..."
- Summary: Updated with actual metrics
- Button: Re-enabled

**Error State:**
- Status: `.status.error`, error color (see Style Decisions Log for derivation)
- Message: "❌ Error: [error message]"
- Button: Re-enabled (allow retry)
- Summary: May show previous values or remain as "—"

**Empty State (No Previous Run):**
- Summary shows placeholder values ("—")
- Status: Default info message
- Button: Enabled (ready for first run)

---

## Screen 3: ANALYTICS (analytics.html)

### Purpose
Execute analytics queries (SKU drop-off, cohort retention), view export summaries.

### Layout Grid
- **Container:** `min(1100px, 90vw)`
- **Structure:**
  - Navigation header
  - Run Analytics section (card)
  - Exports section (card)

### Components Used
1. **Navigation Header**
2. **Run Analytics Card** (`.card` with button and status)
3. **Button Primary**
4. **Status Message**
5. **Exports Card** (`.card` with export list)

### Exact Layout Structure

```html
<main class="bosk8">
  <div class="container">
    <!-- Navigation Header -->
    <nav class="card nav-header" style="padding: var(--space-1);">
      <!-- ... nav links ... -->
    </nav>

    <!-- Run Analytics Section -->
    <section class="card" style="padding: var(--space-1); margin-bottom: var(--space-1);">
      <div class="meta-md" style="margin-bottom: var(--space-1);">RUN ANALYTICS</div>
      <div class="meta-sm" style="color: var(--text-subtle); margin-bottom: var(--space-1);">
        Requires artifacts/funnel_steps.csv (run pipeline first).
      </div>
      <div style="display: flex; gap: var(--space-1); flex-wrap: wrap; align-items: center;">
        <button class="btn btn-primary" aria-live="polite" title="Run Analytics Queries">
          <span>RUN</span>
        </button>
        <div class="status info" id="analytics-status">
          Click RUN to execute analytics queries.
        </div>
      </div>
    </section>

    <!-- Exports Section -->
    <section class="card" style="padding: var(--space-1);">
      <div class="meta-md" style="margin-bottom: var(--space-1);">EXPORTS</div>
      <div class="meta-sm" style="color: var(--text-subtle); margin-bottom: var(--space-0_5);">
        sku_dropoff.csv — rows: —
      </div>
      <div class="meta-sm" style="color: var(--text-subtle);">
        cohort_retention.csv — rows: —
      </div>
      <div style="margin-top: var(--space-1);">
        <a href="./artifacts.html" class="link">→ VIEW ALL ARTIFACTS</a>
      </div>
    </section>
  </div>
</main>
```

### Responsive Rules

Same as Pipeline page.

### States

**Default State:**
- Button: Enabled
- Status: Info message
- Exports: Placeholder row counts ("—")

**Loading State:**
- Button: Disabled
- Status: "RUNNING..." or progress indicator

**Success State:**
- Status: Success message with export details
- Exports: Updated row counts (e.g., "sku_dropoff.csv — rows: 150")

**Error State:**
- Status: Error message (e.g., "funnel_steps.csv not found")
- Button: Re-enabled (allow retry)

**Prerequisite Missing State:**
- If `funnel_steps.csv` doesn't exist:
  - Status: Warning message
  - Button: May be disabled or show error on click

---

## Screen 4: ARTIFACTS (artifacts.html)

### Purpose
List all artifacts, provide copy-to-clipboard functionality for file paths.

### Layout Grid
- **Container:** `min(1100px, 90vw)`
- **Structure:**
  - Navigation header
  - Artifacts list (card with rows)

### Components Used
1. **Navigation Header**
2. **Artifacts Card** (`.card`)
3. **Artifact Row** (flex container with border-bottom)
4. **Copy Button** (`.copy-btn` with icons)
5. **Link** (for navigation hints)

### Exact Layout Structure

```html
<main class="bosk8">
  <div class="container">
    <!-- Navigation Header -->
    <nav class您在="card nav-header" style="padding: var(--space-1);">
      <!-- ... nav links ... -->
    </nav>

    <!-- Artifacts Section -->
    <section class="card" style="padding: var(--space-1);">
      <div class="meta-md" style="margin-bottom: var(--space-1);">ARTIFACTS</div>
      <div class="meta-sm" style="color: var(--text-subtle); margin-bottom: var(--space-1);">
        Click copy icon to copy file path to clipboard.
      </div>
      <div style="display: grid; gap: var(--space-0_75);">
        <!-- Artifact Row -->
        <div style="display: flex; justify-content: space-between; align-items: center; padding: var(--space-0_75);" class="border-b">
          <span class="meta-sm" style="color: var(--text-muted);">
            artifacts/funnel_session.csv
          </span>
          <button class="copy-btn" data-copy="artifacts/funnel_session.csv" aria-label="Copy path">
            <span class="copy-icon">⧉</span>
            <span class="check-icon" style="display: none;">✓</span>
          </button>
        </div>
        <!-- ... more artifact rows ... -->
      </div>
    </section>
  </div>
</main>
```

### Responsive Rules

**Mobile:**
- Artifact rows: Full width, text may wrap
- Copy button: Fixed size, stays right-aligned

**Desktop:**
- Same layout (optimized for readability)

### States

**Default State:**
- Copy icon: `--text-dim` color, visible
- Check icon: Hidden

**Hover State (Copy Button):**
- Copy icon: `#d4d4d8` color (derived from `--text-dim`, see Style Decisions Log)

**Active State (After Click):**
- Copy icon: Hidden
- Check icon: Visible, `--accent-success` color
- After 2s: Reverts to default

**Empty State:**
- Message: "No artifacts found. Run pipeline and analytics first."
- Links to PIPELINE and ANALYTICS pages

---

## Screen 5: STYLE (style.html)

### Purpose
Developer reference for design tokens and style system.

### Layout Grid
- **Container:** `min(1100px, 90vw)`
- **Structure:**
  - Navigation header
  - Tokens reference (card)

### Components Used
1. **Navigation Header**
2. **Style Reference Card** (`.card` with code block)

### Exact Layout Structure

```html
<main class="bosk8">
  <div class="container">
    <!-- Navigation Header -->
    <nav class="card nav-header" style="padding: var(--space-1);">
      <!-- ... nav links ... -->
    </nav>

    <!-- Tokens Section -->
    <section class="card" style="padding: var(--space-1);">
      <div class="meta-md" style="margin-bottom: var(--space-1);">TOKENS</div>
      <div class="meta-sm" style="color: var(--text-subtle); margin-bottom: var(--space-1);">
        Reference copied from style.md
      </div>
      <pre class="meta-sm" style="color: var(--text-subtle); white-space: pre-wrap; overflow-x: auto;">
        fontFamily.ui → JetBrains Mono...
        fontSize.base|xs|sm|md|lg
        colors.bg.black|bg.elev1|surface.card|text.primary|text.muted|text.subtle|text.dim|text.highlight|accent.success|border.neutral|shadow.tint
        radii.sm|md
        borders.thin|md|outer
        spacing.xs|sm|md|lg|xl|2xl|containerPadTop
        layout.containerMax|gridColsMobile|gridColsDesktop
      </pre>
    </section>
  </div>
</main>
```

### Responsive Rules

**Mobile:**
- Code block: Horizontal scroll if needed (`overflow-x: auto`)

**Desktop:**
- Code block: Full width, no scroll needed

### States

**Default State:**
- All tokens displayed as reference text
- No interactive elements (read-only reference)

