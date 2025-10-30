# Style Decisions Log

Timestamp: 2025-10-30

1) Derivation: Buttons
- Need: Buttons are referenced but not fully specified in `style.md`.
- Rule: Derive only from existing tokens.
- Decision: Text `--text-muted` → hover `--text-primary`; border `--border-color` using `--border-w`; radius `--r-sm`; padding `--space-0_75` x `--space-1`; focus `:focus-visible` 2px outline `--border-color`.

2) Derivation: Inputs
- Need: Inputs not explicitly specified.
- Decision: Background `--surface-card`, text `--text-primary`, placeholder `--text-dim`, border `--border-w`/`--border-color`, radius `--r-sm`; focus outline 2px `--border-color`.

3) Conflict Check: Motion
- Need: Loading indicators should be visible but minimal.
- Resolution: Use opacity/label changes within ≤200ms; no spinners with large motion.

4) Breadcrumbs (future)
- Need: Not in `style.md`; minimal meta styling needed.
- Decision: Use `.meta-sm` with `--text-subtle` for non-active; active inherits `--text-primary`.


