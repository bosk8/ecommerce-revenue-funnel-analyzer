# Navigation & Routing Model

## Global Navigation

### Structure
- **Location:** Top of every page (`.nav-header` card)
- **Type:** Horizontal link list
- **Items:** HOME | PIPELINE | ANALYTICS | ARTIFACTS | STYLE
- **Behavior:** Client-side navigation (page reloads)

### Active State Detection
- **Method:** JavaScript reads `window.location.pathname`
- **Logic:** Match current page filename to `href` attribute
- **Visual:** Active link uses `.nav-link.active` class
- **Accessibility:** Active link has `aria-current="page"` attribute

### Implementation (JavaScript)
```javascript
(function() {
  const pathname = window.location.pathname;
  const currentPage = pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    const normalizedHref = href.replace(/^\.\//, '');
    if (normalizedHref === currentPage || 
        (topPage === '' && normalizedHref === 'index.html')) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
})();
```

## Secondary Navigation

### Context Links
- **Pipeline → Analytics:** "→ CONTINUE TO ANALYTICS" link
- **Analytics → Artifacts:** "→ VIEW ALL ARTIFACTS" link
- **Home → All Pages:** Quick Actions links

### Behavior
- Standard `<a>` links with `class="link"`
- Hover state: Underline with 4px offset
- No breadcrumbs (flat hierarchy)

## Routing Rules

### Route Structure
```
/ → index.html (HOME)
/pipeline.html → Pipeline page
/analytics.html → Analytics page
/artifacts.html → Artifacts page
/style.html → Style reference page
```

### Default Route
- **Path:** `/` or `/index.html`
- **Behavior:** Loads `index.html`

### Deep Links
- **All pages accessible via direct URL**
- **No redirects needed** (static HTML)

### 404 Handling
- **Current:** Browser default 404 page
- **Future Enhancement:** Custom 404 page with navigation links

## Breadcrumbs

### Design Decision
- **Not implemented** (flat navigation model)
- **Rationale:** Simple 5-page structure, global nav always visible
- **Alternative:** Could add breadcrumbs for future nested pages if needed

## Empty States

### Pipeline Page (No Previous Run)
- **Condition:** `artifacts/funnel_session.csv` does not exist
- **Display:**
  - "Last Run Summary" shows placeholders: "Events: — · Steps: — · Sessions: —"
  - Status message: Default info text
  - No error state (expected first-run)

### Analytics Page (Prerequisite Missing)
- **Condition:** `artifacts/funnel_steps.csv` does not exist
- **Display:**
  - Status: Warning message "⚠️ Requires artifacts/funnel_steps.csv (run pipeline first)."
  - Button: May be disabled or show error on click
  - Export summaries: "—" for row counts

### Artifacts Page (No Files)
- **Condition:** `artifacts/` directory empty
- **Display:**
  - Empty state message: "No artifacts found. Run pipeline and analytics first."
  - Action links: "→ RUN PIPELINE" and "→ RUN ANALYTICS"

### Implementation Example
```html
<!-- Empty State Component -->
<div class="empty-state">
  <div class="meta-md" style="margin-bottom: var(--space-1);">NO ARTIFACTS</div>
  <div class="meta-sm" style="color: var(--text-subtle); margin-bottom: var(--space-1);">
    No artifacts found. Run pipeline and analytics first.
  </div>
  <div style="display: flex; gap: var(--space-1); flex-wrap: wrap;">
    <a href="./pipeline.html" class="link">→ RUN PIPELINE</a>
    <a href="./analytics.html" class="link">→ RUN ANALYTICS</a>
  </div>
</div>
```

## First-Run Experience

### Flow
1. User lands on HOME page
2. Sees Quick Actions: "RUN PIPELINE", "RUN ANALYTICS", etc.
3. Clicks "RUN PIPELINE"
4. Pipeline page loads → Shows instruction: "Ensure data/raw/events.csv exists"
5. User may:
   - Download data first, then return
   - Attempt run → See error → Download data → Retry
6. After successful run, sees "CONTINUE TO ANALYTICS" link
7. Completes full flow

### Guidance
- Clear instructions on each page
- Error messages include actionable hints
- Progressive disclosure (don't overwhelm first-time users)

## State Persistence

### Client-Side State
- **Navigation active state:** Derived on page load (no storage)
- **Copy button feedback:** In-memory only (2s timeout)
- **No form data:** All actions via buttons/links

### Server-Side State (Artifacts)
- **Pipeline status:** Determined by file existence
- **Last run metrics:** Parsed from CSV files on page load
- **Row counts:** Read from CSV files on page load

### Refresh Behavior
- **Page reload:** Resets all UI state (buttons, status messages)
- **Navigation:** Full page load (no SPA routing)
- **Status messages:** Reset to default on page load

## URL Structure

### Current
- **Static HTML files:** `/index.html`, `/pipeline.html`, etc.
- **Relative paths:** `./index.html`, `./pipeline.html`
- **Assets:** `./bosk8.css`, `./app.js`

### Future Considerations
- **SPA routing:** Could implement client-side router if needed
- **Query parameters:** Could add `?status=success` for post-action feedback
- **Hash routing:** Alternative for client-side navigation without server config

