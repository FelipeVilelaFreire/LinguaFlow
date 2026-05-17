# New Screen Prompt — Add a screen following the 3-layer pattern

> Use this when adding a route that needs to fetch data and render a feature.

---

## When to use

- New route in `app/`
- The route needs to load data from the API
- Has loading / error / data states

If the route is purely static (no fetch, no logic), skip this — just write the page directly.

---

## The Prompt

```
Add a new screen: {{SCREEN_NAME}} at route {{ROUTE_PATH}}.

What it shows: {{ONE_PARAGRAPH_DESCRIPTION}}

Data source: {{API_ENDPOINT_OR_HOOK_NAME}}

Mobile layout: {{MOBILE_DESCRIPTION}}
Desktop layout: {{DESKTOP_DESCRIPTION}}

Follow CLAUDE.md, ARCHITECTURE.md, SHARED-CORE.md, FRONTEND-WEB.md, FRONTEND-MOBILE.md, PARITY-AUDIT.md, and DESIGN.md.

Steps to perform IN THIS ORDER:

1. CHECK FOR EXISTING PIECES:
   - Does the type exist in packages/shared-core/src/types/{{domain}}/? If yes, import.
     If no, add it.
   - Does the service method exist in packages/shared-core/src/services/{{domain}}Service.ts?
     If no, add it.
   - Does the hook exist in packages/shared-core/src/hooks/{{domain}}/? If no, create it.
   - Ensure web/src/hooks/{{domain}}/ and mobile/src/hooks/{{domain}}/ are thin wrappers only.

2. LAYER 1 — ROUTE FILE (~5 lines):
   - app/{{ROUTE_PATH}}/page.tsx
   - Reads params, renders <{{ScreenName}} />
   - Zero logic, zero styles

3. LAYER 2 — SCREEN (fetch + skeleton + error):
   - web/src/screens/{{ScreenName}}/{{ScreenName}}.tsx
   - Calls use{{ScreenName}}() hook
   - Renders <Skeleton /> while loading
   - Renders <ErrorState /> on error
   - Renders <{{Feature}} /> with data when loaded
   - Plus barrel index.ts

4. LAYER 3 — FEATURE (pure UI):
   - If a matching feature exists in src/components/features/, reuse it
   - Otherwise create web/src/components/features/{{FeatureName}}/
     - {{FeatureName}}.tsx — pure render, props in
     - {{FeatureName}}.module.css — mobile-first
     - index.ts — barrel

5. STRINGS:
   - Every visible text from STRINGS.{{domain}}.{{key}}
   - If new keys needed: add to pt-BR.ts, en.ts, and de-DE.ts in shared-core
   - If the screen is shared, create/confirm the equivalent web and mobile feature tree or record the intentional difference in docs/PARITY-AUDIT-EXECUTION.md

6. STYLES:
   - .module.css starts with mobile defaults
   - @media (min-width: 769px) adds desktop layout
   - Every value uses CSS Variables (zero hardcoded px/colors)
   - One of {box-shadow, border} on cards, never both

7. ROUTES CONSTANT:
   - Add to web/src/constants/routes.ts:
     {{SCREEN_NAME_UPPER}}: '{{ROUTE_PATH}}' (or function if it has params)

When done, report:
- All files created
- Whether existing hooks/services were reused or new ones added
- Mobile vs desktop differences
- Visual decisions (which design tokens used)
```

---

## Example invocation

```
Add a new screen: OrderListScreen at route /orders.

What it shows: A paginated list of the current user's orders. Top bar with
filter pills (All, Pending, Paid, Delivered, Cancelled). Each row is a
clickable card showing date, status (colored text), total. Empty state
when no orders.

Data source: GET /api/orders/ with optional ?status=...

Mobile layout: Single column, full-width cards, filter pills horizontal
scroll at top.
Desktop layout: Same single column (max-width 800px centered), filter
pills inline.

[paste the rest of the prompt above]
```

---

## What Claude should NOT do

- Put fetch in the page or the feature (only the hook fetches)
- Add styles inline with `style={{...}}` for static values
- Use Tailwind classes
- Skip the barrel `index.ts`
- Use desktop-first CSS (`@media (max-width: ...)`)
- Use literal strings in JSX
- Forget to update the `ROUTES` constant
