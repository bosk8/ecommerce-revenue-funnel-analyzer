# UI/UX System Specification

## Overview

This directory contains the complete UI/UX specification for the E-Commerce Revenue Funnel Analyzer, following the Bosk8 design system (`style.md`) as the single source of truth.

## Document Structure

### 1. [Executive Summary](./executive-summary.md)
- Project goals, primary personas, major user flows
- Constraints and assumptions
- Open questions and resolutions

### 2. [Information Architecture & User Flows](./information-architecture.md)
- Sitemap and navigation model
- Detailed user flows (happy paths and error cases)
- Empty states and route rules
- State management approach

### 3. [Screen-by-Screen Specifications](./screens/spec.md)
- Complete specifications for all 5 pages (HOME, PIPELINE, ANALYTICS, ARTIFACTS, STYLE)
- Layout grids, component usage, responsive rules
- All states (default, hover, focus, loading, success, error, empty)

### 4. [Interactive Component Library](./component-library/spec.md)
- 8 core components with props, variants, states
- Exact `style.md` token references
- Accessibility notes and example usage
- Component structure and behavior

### 5. [Function-to-UI Mapping](./function-to-ui/spec.md)
- Backend functions mapped to UI triggers
- Data contracts (inputs/outputs)
- Validation rules and error states
- Feedback patterns (loading, success, error)
- Proposed API endpoints

### 6. [Navigation & Routing Model](./navigation-routing.md)
- Global and secondary navigation
- Route structure and rules
- Empty states and first-run experience
- State persistence approach

### 7. [Accessibility Checklist](./accessibility.md)
- WCAG 2.2 AA compliance checklist
- Color contrast verification
- Keyboard navigation and focus management
- Screen reader support
- Known issues and future improvements

### 8. [Style Compliance Matrix](./style-compliance-matrix.md)
- Complete mapping of screens/components to `style.md` tokens
- Derived tokens with derivation logic
- Responsive breakpoint compliance
- Compliance checklist

### 9. [Style Decisions Log](./style-decisions-log.md)
- Timestamped log of all assumptions, derivations, conflicts
- Rationale and impact for each decision
- Open questions and resolutions
- Compliance status

### 10. [Developer Handoff Guide](./dev-handoff.md)
- Complete CSS token map
- Spacing redlines
- Sample HTML/CSS/JavaScript snippets
- Acceptance checklist
- File structure and next steps

## Key Principles

### Style.md as Single Source of Truth
- All visual decisions must reference `style.md` tokens
- No new tokens created without derivation documentation
- Conflicts resolved in favorifically of `style.md`
- All derivations logged in Style Decisions Log

### Component-First Approach
- Reusable components before screen-specific implementations
- Consistent patterns across all screens
- Clear component boundaries and responsibilities

### Accessibility First
- WCAG 2.2 AA minimum standards
- Keyboard navigation for all interactive elements
- Screen reader support
- Sufficient color contrast

## Quick Reference

### Core Components
1. Navigation Header
2. Button Primary
3.穩 Status Message
4. Copy Button
5. Card
6. Link
7. Feature Tiles Grid
8. Meta Text (Labels)

### Pages
1. HOME (`index.html`)
2. PIPELINE (`pipeline.html`)
3. ANALYTICS (`analytics.html`)
4. ARTIFACTS (`artifacts.html`)
5. STYLE (`style.html`)

### Backend Functions
1. ETL Pipeline Execution (`src/etl_funnel.py`)
2. Analytics Query Execution (`src/run_analytics.py`)
3. Artifact File Reading (file system)
4. Copy to Clipboard (browser API)

## Implementation Status

- ✅ Specifications complete
- ⏳ Backend integration (to be implemented)
- ⏳ Real-time progress updates (to be implemented)
- ⏳ Button touch target verification (known issue)

## Related Documents

- [`../style.md`](../style.md) - Bosk8 design system reference
- [`../project-scope.md`](../project-scope.md) -來 Project requirements
- [`../README.md`](../README.md) - Project overview

## Questions or Issues

For questions about the specification or to log new decisions:
1. Check [Style Decisions Log](./style-decisions-log.md) for existing decisions
2. Document new assumptions/derivations in the log
3. Update relevant specification documents
4. Ensure all changes reference `style.md` tokens

