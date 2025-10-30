# Bosk8 Design System — Dark Minimal Mono

Reference this document verbatim to reproduce the Bosk8 brand style across apps, sites, and tools. It provides natural-language guidance plus implementation-ready tokens and CSS. Inspired by OpenSpec’s landing aesthetic, adapted to Bosk8.

Links: [bosk8.com](https://bosk8.com) · Reference inspo: [openspec.dev](https://openspec.dev)

## Brand Essence
- High-contrast, dark, minimal, utilitarian.
- Monospace type, all-caps UI labels, subtle borders, soft depth.
- Dense but breathable spacing; everything feels precise and engineered.

## Core Design Tokens
Use these as the single source of truth.

```json
{
  "fontFamily": {
    "ui": "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace"
  },
  "fontSize": {
    "base": "clamp(16px, calc(15.2px + 0.25vw), 20px)",
    "xs": "0.625rem",
    "sm": "0.75rem",
    "md": "0.875rem",
    "lg": "1rem"
  },
  "colors": {
    "bg.black": "#000000",
    "bg.elev1": "#0A0A0A",
    "surface.card": "#09090B",
    "text.primary": "#FFFFFF",
    "text.muted": "#E8E8E8",
    "text.subtle": "#A1A1AA",
    "text.dim": "#71717A",
    "text.linkHover": "#FFFFFF",
    "text.highlight": "#F4F4F5",
    "accent.success": "#22C55E",
    "border.neutral": "rgb(39 39 42)",
    "shadow.tint": "#0000000d"
  },
  "radii": { "sm": "4px", "md": "6px" },
  "borders": { "thin": "1px", "md": "1.5px", "outer": "2px" },
  "spacing": {
    "xs": "0.5rem",
    "sm": "0.75rem",
    "md": "1rem",
    "lg": "1.5rem",
    "xl": "2rem",
    "2xl": "4rem",
    "containerPadTop": "10rem"
  },
  "layout": {
    "containerMax": "min(1100px, 90vw)",
    "gridColsMobile": 2,
    "gridColsDesktop": 4
  }
}
```

## CSS Variables (drop-in)
Add these to the root or a page wrapper and use throughout components.

```css
:root {
  --font-ui: JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
  --fs-base: clamp(16px, calc(15.2px + 0.25vw), 20px);

  --bg-black: #000;
  --bg-elev1: #0A0A0A;
  --surface-card: #09090B;

  --text-primary: #fff;
  --text-muted: #e8e8e8;
  --text-subtle: #a1a1aa;
  --text-dim: #71717a;
  --text-highlight: #f4f4f5;

  --accent-success: #22c55e;

  --border-color: rgb(39 39 42);
  --border-w: 1px;           /* elevated to 1.5px ≥1024px */
  --border-outer-w: 1px;     /* elevated to 2px ≥1024px */

  --shadow-tint: #0000000d;

  --r-sm: 4px;
  --r-md: 6px;

  --space-0_5: 0.5rem;
  --space-0_75: 0.75rem;
  --space-1: 1rem;
  --space-1_5: 1.5rem;
  --space-2: 2rem;
  --space-4: 4rem;
}

@media (min-width: 1024px) {
  :root { --border-w: 1.5px; --border-outer-w: 2px; }
}
```

## Global Resets & Base

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--fs-base); }
html, body {
  margin: 0; width: 100%; height: 100%;
  background-color: var(--bg-black);
  font-family: var(--font-ui);
  color: var(--text-primary);
}
main.bosk8 {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  min-height: 100vh;
  padding: var(--space-4) var(--space-1) var(--space-1);
  padding-top: 10rem; /* hero spacing */
  background-color: var(--bg-elev1);
}
.container { width: 100%; max-width: min(1100px, 90vw); position: relative; }
```

## Cards & Surfaces

```css
.card {
  background-color: var(--surface-card);
  box-shadow: 0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint);
}
.border-b { border-bottom: var(--border-w) solid var(--border-color); }
.border-r { border-right: var(--border-w) solid var(--border-color); }
```

## Typography
- UI copy uses JetBrains Mono.
- All navigation, labels, and meta copy use uppercase with slight letter-spacing.

```css
.tagline, .meta, .label, .nav {
  font-family: var(--font-ui);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
}
.tagline { font-size: 1rem; text-align: center; }
.meta-sm { font-size: 0.75rem; }
.meta-md { font-size: 0.875rem; }
```

## Links & Actions

```css
.link { color: var(--text-muted); text-decoration: none; transition: all .15s; }
.link:hover { color: var(--text-primary); text-decoration: underline; text-underline-offset: 4px; }
.copy-btn {
  display: inline-flex; align-items: center; gap: 0.75rem; background: transparent; border: none; cursor: pointer; padding: 0;
}
.copy-icon { color: var(--text-dim); transition: color .15s; }
.copy-btn:hover .copy-icon { color: #d4d4d8; }
.check-icon { color: var(--accent-success); }
```

## Grid & Layout

```css
.grid-tiles {
  display: grid; grid-template-columns: repeat(2, 1fr);
}
@media (min-width: 768px) { .grid-tiles { grid-template-columns: repeat(4, 1fr); } }
.tile { padding: 1.5rem 1rem; text-align: center; }
```

## Tooltip Pattern

```css
.tooltip-trigger { position: relative; background: transparent; border: none; padding: 0; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; }
.tooltip {
  position: absolute; left: 50%; bottom: calc(100% + .5rem); transform: translate(-50%);
  background-color: var(--surface-card); border: var(--border-w) solid var(--border-color);
  padding: .5rem; font-size: .625rem; font-family: var(--font-ui); color: var(--text-subtle);
  max-width: 280px; width: max-content; line-height: 1.5; opacity: 0; visibility: hidden; transition: opacity .15s, visibility .15s; pointer-events: none; z-index: 10;
}
.tooltip:before { content: ""; position: absolute; top: 100%; left: 50%; transform: translate(-50%); border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 4px solid var(--border-color); }
.tooltip:after  { content: ""; position: absolute; top: calc(100% - 1px); left: 50%; transform: translate(-50%); border-left: 3px solid transparent; border-right: 3px solid transparent; border-top: 3px solid rgb(9 9 11); }
@media (min-width: 768px) { .tooltip-trigger:hover .tooltip { opacity: 1; visibility: visible; } }
@media (max-width: 767px) { .tooltip-trigger.active .tooltip { opacity: 1; visibility: visible; } }
```

## FAQ / Accordion Pattern

```css
.faq-item { border-bottom: var(--border-w) solid var(--border-color); transition: background-color .15s; }
.faq-item:hover { background: #18181b; }
.faq-q { width: 100%; background: transparent; border: none; padding: 1.25rem 1.75rem; cursor: pointer; display: flex; align-items: center; justify-content: space-between; gap: 1rem; font-size: .75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: .05em; transition: color .15s; }
.faq-q:hover { color: #fff; }
.faq-a { display: none; font-size: .8rem; color: var(--text-subtle); line-height: 1.5; padding: 0 1.75rem 1.25rem; }
.faq-a.active { display: block; }
```

## Logo & Mark
- Primary mark: `B8` monoline logo in white on pure black.
- Minimum clear-space: height of the inner diamond on all sides.
- Display sizes: 8rem width in hero contexts; scale proportionally elsewhere.
- Never place on colored backgrounds; use black or near-black only.

## Accessibility & Motion
- Color contrast: maintain WCAG AA minimum; prefer high-contrast white-on-black.
- Motion: keep transitions under 200ms; no large parallax or auto animations.
- Focus styles: visible, 2px outline using `--border-color` over `--surface-card`.

```css
:focus-visible { outline: 2px solid var(--border-color); outline-offset: 2px; }
```

## Layout Recipe (Hero Page)

```html
<main class="bosk8">
  <div class="container">
    <header class="logo-container"><img class="logo" src="/B8.svg" alt="Bosk8" width="128" /></header>
    <section class="card border-b" style="padding:4rem 2rem; display:flex; flex-direction:column; align-items:center;">
      <h1 class="tagline">A LIGHTWEIGHT SPEC-DRIVEN FRAMEWORK</h1>
    </section>
    <section class="card grid-tiles border-b">
      <div class="tile border-r">UNIVERSAL</div>
      <div class="tile">OPEN SOURCE</div>
      <div class="tile border-r">NO API KEYS</div>
      <div class="tile">NO MCP</div>
    </section>
  </div>
</main>
```

## Tailwind (optional mapping)
If using Tailwind, extend your config with these keys.

```js
// tailwind.config.js
export default {
  theme: {
    extend: {
      colors: {
        black: '#000000',
        elev1: '#0A0A0A',
        card: '#09090B',
        muted: '#E8E8E8',
        subtle: '#A1A1AA',
        dim: '#71717A',
        success: '#22C55E',
        border: 'rgb(39 39 42)'
      },
      fontFamily: { mono: ["JetBrains Mono", "ui-monospace", "SFMono-Regular", "Menlo", "Monaco", "Consolas", "Liberation Mono", "DejaVu Sans Mono", "Courier New", "monospace"] },
      boxShadow: { card: '0 0 0 var(--border-outer-w) var(--tw-border-color), 0 1px 2px #0000000d' },
      letterSpacing: { mono: '.05em' }
    }
  }
}
```

## Content Voice
- Confident, terse, technical; use sentence case in paragraphs, ALL CAPS for UI labels.
- Prefer single-line CTAs; avoid exclamation marks. Engineering-first tone.

## Do / Don’t
- Do: use subtle borders and soft outer rings for depth.
- Do: uppercase labels with JetBrains Mono and 0.05em tracking.
- Don’t: introduce saturated brand colors; keep palette grayscale with functional green.
- Don’t: round corners aggressively; keep radii small.

---
This file is the canonical Bosk8 style reference. Tools and LLMs should read tokens first, then apply the component patterns and behavior notes above to ensure faithful reproduction across projects.
