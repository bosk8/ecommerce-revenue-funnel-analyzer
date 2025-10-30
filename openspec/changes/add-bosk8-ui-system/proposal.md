## Why
E-commerce Revenue Funnel Analyzer lacks a production-ready, consistent UI/UX system. We need a reusable design system and screen specifications to operationalize the pipeline, visualize analytics exports status, and provide a cohesive developer handoff. `style.md` is the single source of truth for all visual and interaction decisions, and this proposal formalizes its application.

## What Changes
- Introduce Bosk8 Dark Minimal Mono UI foundations mapped 1:1 to tokens in `style.md`
- Define an interactive component library (buttons, inputs, cards, grid, tooltip, FAQ/accordion) strictly using existing tokens
- Specify screens, layouts, routing, and responsive rules for pipeline execution and analytics export management
- Provide accessibility checklist (WCAG 2.2 AA), keyboard flows, and ARIA notes
- Create a Style Compliance Matrix and Style Decisions Log (with derivations only when necessary)
- Deliver dev handoff artifacts (token CSS map, redlines, snippets)

## Impact
- Affected specs: `ui-foundations`, `component-library`, `screens`, `navigation`, `accessibility`, `style-compliance`
- Affected code: none immediately (specs first). Future UI implementations will reference: `style.md`, `src/etl_funnel.py`, `src/run_analytics.py`, `sql/*.sql`, and `README.md` for Function-to-UI mapping.

## Assumptions
- UI will be implemented as a lightweight web app or static site embedding controls for running local scripts, or as a design-handoff reference used by a chosen frontend stack later.
- No new visual tokens will be invented. Missing specifics will be derived from `style.md` and recorded.
- Data operations remain as-is; this proposal does not change ETL/SQL logic.

## Risks
- Over-specification without an immediate frontend stack; mitigated by stack-agnostic CSS/token mapping and HTML examples.


