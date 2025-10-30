## Context
Spec-only change to introduce a UI/UX system grounded in `style.md` for the funnel analyzer. No backend changes required.

## Goals / Non-Goals
- Goals: Define foundations, components, screens, mapping, a11y, and handoff artifacts strictly bound to `style.md`.
- Non-Goals: Implementing runtime UI stack, adding new visual tokens, changing ETL/SQL behavior.

## Decisions
- Use CSS variables from `style.md` verbatim; responsive rules per media queries in `style.md`.
- Derive only where missing (buttons/inputs) and record derivations in Style Decisions Log.

## Risks / Trade-offs
- Stack-agnostic specs may need adaptation per framework; mitigated by vanilla HTML/CSS examples.

## Open Questions
- Will the UI be embedded locally (electron/static) or web-deployed? Logged; proceed stack-agnostic.


