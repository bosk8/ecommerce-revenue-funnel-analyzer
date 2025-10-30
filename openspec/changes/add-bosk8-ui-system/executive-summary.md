## Executive Summary
Goals: Provide a production-ready UI/UX system for running the ETL pipeline, monitoring analytics exports, and handing off dashboard artifacts, strictly adhering to `style.md` (Bosk8 Dark Minimal Mono). Personas: Data Analyst (runs pipeline, checks outputs), Data Engineer (maintains ETL/SQL), Stakeholder (reviews dashboard link/status).

Primary flows:
- Run ETL: Trigger `src/etl_funnel.py`, view progress, validate outputs (artifacts paths)
- Run Analytics: Execute `src/run_analytics.py`, confirm CSV outputs for Tableau
- Handoff: Show artifact files, instructions, and dashboard publishing link entry

Constraints: No new visual tokens; only derive from `style.md`. Keep UI lean, high-contrast, monospace, uppercase labels, subtle borders.

Open questions captured in Style Decisions Log; proceed with defaults documented there.

## Information Architecture (Sitemap)
- Home (/): Overview cards and quick actions
- Pipeline (/pipeline): Run ETL; show validation and rates
- Analytics (/analytics): Run SQL exports; show row counts
- Artifacts (/artifacts): List CSVs and copy paths
- Style (/style): Token reference mapped from `style.md`

## User Flows
### Happy path: Run ETL and analytics
1) Home → Start ETL → Success states → View summary → Go to Analytics → Run → View row counts → Artifacts visible → Copy paths

### Edge cases
- Missing data: Surface error with guidance (events.csv not found)
- DuckDB error: Show error block with retry guidance
- Long run: Show loading state with minimal motion (<200ms transitions)


