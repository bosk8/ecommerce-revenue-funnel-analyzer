# Dev Handoff

## Tokens and CSS Variable Map
- Source: `style.md` JSON tokens and CSS variables. Implement `:root` variables exactly as listed in `style.md`.

## Spacing / Redlines
- Container: width `min(1100px, 90vw)`
- `main.bosk8` padding: top `spacing.2xl` (10rem per `style.md` recipe), sides `spacing.md`, bottom `spacing.md`
- Grid: 2 columns mobile, 4 columns ≥768px
- Tile padding: `spacing.lg` vertical, `spacing.md` horizontal

## Sample HTML/CSS Snippets

```html
<main class="bosk8">
  <div class="container">
    <section class="card border-b" style="padding:4rem 2rem; display:flex; flex-direction:column; align-items:center;">
      <h1 class="tagline">A LIGHTWEIGHT SPEC-DRIVEN FRAMEWORK</h1>
    </section>
  </div>
</main>
```

```css
.card { background: var(--surface-card); box-shadow: 0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint); }
.link { color: var(--text-muted); }
.link:hover { color: var(--text-primary); text-decoration: underline; text-underline-offset: 4px; }
```

## Accessibility Acceptance
- WCAG 2.2 AA contrast verified for white-on-black and muted text as meta
- Keyboard: All interactive controls reachable; focus-visible outlines `--border-color`
- Motion: transitions ≤200ms; no auto animations

## Acceptance Checklist
- [ ] Tokens implemented exactly as `style.md`
- [ ] Components match required states (default/hover/focus/active/disabled/error/loading)
- [ ] Screens route correctly and responsive rules match
- [ ] A11y checklist passes (keyboard, ARIA semantics, contrast)
