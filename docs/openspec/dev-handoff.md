# Developer Handoff Guide

## Overview

This document provides implementation-ready artifacts for developers to build the UI system according to the specifications. All references use exact `style.md` tokens.

## Design Tokens / CSS Token Map

### CSS Variables (Complete Set)

```css
:root {
  /* Typography */
  --font-ui: JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
  --fs-base: clamp(16px, calc(15.2px + 0.25vw), 20px);

  /* Colors - Backgrounds */
  --bg-black: #000;
  --bg-elev1: #0A0A0A;
  --surface-card: #09090B;

  /* Colors - Text */
  --text-primary: #fff;
  --text-muted: #e8e8e8;
  --text-subtle: #a1a1aa;
  --text-dim: #71717a;
  --text-highlight: #f4f4f5;

  /* Colors - Accents */
  --accent-success: #22c55e;

  /* Colors - Borders & Shadows */
  --border-color: rgb(39 39 42);
  --shadow-tint: #0000000d;

  /* Borders */
  --border-w: 1px;           /* Elevated to 1.5px ≥1024px */
  --border-outer-w: 1px;     /* Elevated to 2px ≥1024px */

  /* Radii */
  --r-sm: 4px;
  --r-md: 6px;

  /* Spacing */
  --space-0_5: 0.5rem;
  --space-0_75: 0.75rem;
  --space-1: 1rem;
  --space-1_5: 1.5rem;
  --space-2: 2rem;
  --space-4: 4rem;
}

@media (min-width: 1024px) {
  :root { 
    --border-w: 1.5px; 
    --border-outer-w: 2px; 
  }
}
```

### Derived Tokens (Documented)

```css
/* Error color (derived - see Style Decisions Log) */
--error-color: #ef4444;

/* Copy button hover (derived) */
--copy-hover: #d4d4d8;
```

## Spacing Redlines

### Component Spacing

| Component | Padding | Gap | Notes |
|-----------|---------|-----|-------|
| Navigation Header | `--space-1` (1rem) | `--space-1` (1rem) between links | |
| Card (default) | `--space-1` (1rem) | N/A | Inline style override allowed |
| Button | `--space-0_75` (12px) vertical, `--space-1` (16px) horizontal | `--space-0_75` (12px) for icon gap | Verify 44px touch target |
| Feature Tile | `--space-lg` (24px) vertical, `--space-1` (16px) horizontal | N/A | |
| Artifact Row | `--space-0_75` (12px) all sides | `--space-0_75` (12px) between rows | |
| Hero Section | `4rem` (64px) vertical, `2rem` (32px) horizontal | N/A | From `style.md` example |

### Layout Spacing

| Element | Spacing | Notes |
|---------|---------|-------|
| Main container padding-top | `10rem` (160px) | Hero spacing |
| Main container padding sides | `--space-1` (1rem) | |
| Section margin-bottom | `--space-1` (1rem) | Between cards |
| Grid gap | `--space-0_75` (12px) | For artifact rows |

## Sample HTML/CSS Snippets

### Navigation Header

```html
<nav class="card nav-header" style="padding: var(--space-1);">
  <div class="nav-links">
    <a href="./index.html" class="nav-link">HOME</a>
    <a href="./pipeline.html" class="nav-link">PIPELINE</a>
    <a href="./analytics.html" class="nav-link">ANALYTICS</a>
-seek    <a href="./artifacts.html" class="nav-link">ARTIFACTS</a>
    <a href="./style.html" class="nav-link">STYLE</a>
  </div>
</nav>
```

```css
.nav-header { 
  margin-bottom: var(--space-1); 
  display: flex; 
  justify-content: space-between; 
  align-items: center;
  gap: var(--space-1);
}
.nav-links { 
  display: flex; 
  gap: var(--space-1); 
  flex-wrap: wrap;
}
 ху nav-link { 
  color: var(--text-muted); 
  text-decoration: none; 
  transition: color .15s;
  font-family: var(--font-ui);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 0.75rem;
}
.nav-link:hover { color: var(--text-primary); }
.nav-link.active { color: var(--text-primary); font-weight: 500; }
```

### Button Primary

```html
<button class="btn btn-primary" disabled aria-live="polite" title="Run ETL Pipeline">
  <span>RUN</span>
</button>
```

```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-0_75);
  padding: var(--space-0_75) var(--space-1);
  background: transparent;
  border: var(--border-w) solid var(--border-color);
  border-radius: var(--r-sm);
  color: var(--text-muted);
  font-family: var(--font-ui);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all .15s;
}
.btn:hover:not(:disabled) {
  color: var(--text-primary);
  border-color: var(--text-primary);
}
.btn:focus-visible {
  outline: 2px solid var(--border-color);
  outline-offset: 2px;
}
.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.btn-primary {
  background: var(--surface-card);
  border-color: var(--border-color);
}
```

### Status Message

```html
<div class="status info" id="etl-status">
  Click RUN to execute the ETL pipeline.
</div>
```

```css
.status {
  font-size: 0.75rem;
  color: var(--text-subtle);
  margin-top: var(--space-0_75);
}
.status.success { color: var(--accent-success); }
.status.error { color: #ef4444; } /* Derived token */
.status.info { color: var(--text-subtle); }
```

### Copy Button

```html
<button class="copy-btn" data-copy="artifacts/funnel_session.csv" aria-label="Copy path">
  <span class="copy-icon">⧉</span>
  <span class="check-icon" style="display: none;">✓</span>
</button>
```

```css
.copy-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-0_75);
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
}
.copy-icon {
  color: var(--text-dim);
  transition: color .15s;
}
.copy-btn:hover .copy-icon {
  color: #d4d4d8; /* Derived token */
}
.check-icon {
  color: var(--accent-success);
}
```

### Card

```html
<section class="card" style="padding: var(--space-1);">
  <div class="meta-md">SECTION TITLE</div>
  <div class="meta-sm" style="color: var(--text-subtle);">Content...</div>
</section>
```

```css
.card {
  background-color: var(--surface-card);
  box-shadow: 0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint);
  border-radius: var(--r-sm);
}
.border-b { border-bottom: var(--border-w) solid var(--border-color); }
.border-r { border-right: var(--border-w) solid var(--border-color); }
```

### Feature Tiles Grid

```html
<section class="card grid-tiles border-b">
  <div class="tile border-r">UNIVERSAL</div>
  <div class="tile">OPEN SOURCE</div>
  <div class="tile border-r">NO API KEYS</div>
  <div class="tile">NO MCP</div>
</section>
```

```css
.grid-tiles {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}
@media (min-width: 768px) {
  .grid-tiles {
    grid-template-columns: repeat(4, 1fr);
  }
}
.tile {
  padding: 1.5rem 1rem;
  text-align: center;
}
```

## JavaScript Implementation Snippets

### Navigation Active State

```javascript
(function() {
  const pathname = window.location.pathname;
  const currentPage = pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    const normalizedHref = href.replace(/^\.\//, '');
    if (normalizedHref === currentPage || 
        (currentPage === '' && normalizedHref === 'index.html') ||
        (pathname.endsWith('/') && normalizedHref === 'index.html')) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
})();
```

### Copy to Clipboard

```javascript
(function() {
  const copyButtons = document.querySelectorAll('.copy-btn[data-copy]');
  
  copyButtons.forEach(btn => {
    btn.addEventListener('click', async function() {
      const textToCopy = this.getAttribute('data-copy');
      const icon = this.querySelector('.copy-icon');
      const checkIcon = this.querySelector('.check-icon');
      
      try {
        await navigator.clipboard.writeText(textToCopy);
        
        // Visual feedback
        if (icon) icon.style.display = 'none';
        if (!checkIcon) {
          const check = document.createElement('span');
          check.className = 'check-icon';
          check.textContent = '✓';
          check.style.display = 'inline';
          this.appendChild(check);
        } else {
          checkIcon.style.display = 'inline';
       可以对}
        
        // Reset after 2 seconds
        setTimeout(() => {
          if (icon) icon.style.display = 'inline';
          if (checkIcon) checkIcon.style.display = 'none';
        }, 2000);
        
        // Announce to screen readers
        const announcement = document.createElement('div');
        announcement.className = 'sr-only';
        announcement.setAttribute('role', 'status');
        announcement.setAttribute('aria-live', 'polite');
        announcement.textContent = 'Copied to clipboard';
        document.body.appendChild(announcement);
        setTimeout(() => announcement.remove(), 2000);
        
      } catch (err) {
        console.error('Failed to copy:', err);
        alert('Failed to copy to clipboard. Please copy manually: ' + textToCopy);
      }
    });
  });
})();
```

### Backend Integration (Proposed)

```javascript
// Pipeline execution (example - to be implemented)
async function runPipeline() {
  const button = document.querySelector('#run-etl-btn');
  const status = document.querySelector('#etl-status');
  
  button.disabled = true;
  status.className = 'status info';
  status.textContent = 'RUNNING...';
  
  try {
    // Option A: Subprocess (if server-side)
    const response = await fetch('/api/pipeline/run', { method: 'POST' });
    const data = await response.json();
    
    if (data.status === 'success') {
      status.className = 'status success';
      status.textContent = `✅ Pipeline complete! Events: ${data.metrics.events_count}, Sessions: ${data.metrics.session_count}`;
      updateSummary(data.metrics);
    } else {
      status.className = 'status error';
      status.textContent = `❌ Error: ${data.message}`;
    }
  } catch (error) {
    status.className = 'status error';
    status.textContent = `❌ Error: ${error.message}`;
  } finally {
    button.disabled = false;
  }
}
```

## Acceptance Checklist

### Visual Design
- [ ] All colors match `style.md` tokens
- [ ] All spacing uses `style.md` tokens
- [ ] Typography uses JetBrains Mono, uppercase labels
- [ ] Cards have correct shadow and border styling
- [ ] Responsive breakpoints work (768px, 1024px)
- [ ] Border widths change at 1024px breakpoint

### Components
- [ ] Navigation header renders correctly on all pages
- [ ] Active page highlighted in navigation
- [ ] Buttons have correct hover/focus/disabled states
- [ ] Status messages display correctly (info/success/error)
- [ ] Copy buttons work and show feedback
- [ ] Cards have correct padding and styling
- [ ] Links have hover underline effect

### Functionality
- [ ] Navigation links work correctly
- [ ] Copy to clipboard functionality works
- [ ] Button disabled states work
- [ ] Status messages update correctly (if backend integrated)
- [ ] Empty states display correctly

### Accessibility
- [ ] Keyboard navigation works (Tab, Enter, Space)
- [ ] Focus indicators visible on all interactive elements
- [ ] Screen reader announces status updates
- [ ] Color contrast meets WCAG AA (verify status messages)
- [ ] Touch targets meet 44x44px minimum (verify buttons)
- [ ] All images have alt text (if any)

### Responsive
- [ ] Mobile layout (<768px) works correctly
- [ ] Tablet layout (768px-1023px) works correctly
- [ ] Desktop layout (≥1024px) works correctly
- [ ] Grid tiles change from 2 to 4 columns at 768px
- [ ] Navigation wraps on mobile if needed

### Browser Compatibility
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

### Performance
- [ ] Page load time < 2s
- [ ] CSS/JS files minified for production
- [ ] No layout shift on load

## File Structure

```
ui/
├── index.html          # HOME page
├── pipeline.html       # PIPELINE page
├── analytics.html      # ANALYTICS page
├── artifacts.html      # ARTIFACTS page
├── style.html          # STYLE reference page
├── bosk8.css          # Main stylesheet (token definitions + components)
└── app.js             # JavaScript (navigation, copy, etc лечит.)
```

## Next Steps

1. **Implement Backend Integration:**
   - Set up subprocess execution or REST API
   - Implement pipeline/analytics execution endpoints
   - Add artifact listing endpoint

2. **Enhance Status Updates:**
   - Real-time progress indication (if needed)
   - Stream stdout/stderr from subprocess
   - Poll artifact directory for updates

3. **Accessibility Enhancements:**
   - Verify button touch target sizes
   - Test with screen readers
   - Add skip links (optional)

4. **Testing:**
   - Manual testing on all browsers
   - Accessibility audit (WAVE, axe)
   - Performance testing

5. **Documentation:**
   - Update README with UI setup instructions
   - Document backend integration approach
   - Add troubleshooting guide

