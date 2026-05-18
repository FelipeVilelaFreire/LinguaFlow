# Agent Operating Guide

This file mirrors `CLAUDE.md` for any coding agent working in this repo. If there is a conflict, follow the stricter rule.

## Prime Directive

Follow this repository's canonical architecture docs. Do not invent a new architecture or reintroduce external template folders.

The target is:

- `backend/` is the source of truth.
- `packages/shared-core/` is the single brain.
- `web/` is render-only Next.js.
- `mobile/` is render-only Expo.
- `admin/` is the separate config-driven admin app.
- `frontend-web/` is legacy reference only.

## Architecture Contract

These are the primary rules. String/i18n rules support this contract, but they do not replace it.

```txt
backend     = SOURCE OF TRUTH
  Owns business rules, authorization, validation, persistence, seeds and content truth.

shared-core = BRAIN
  Owns hooks, services, types, strings, tokens, validation, mappers and flow state.

web/mobile  = RENDER ONLY
  Own platform JSX/TSX, styling and platform UX only. No domain rules. No direct fetch.

admin       = CONFIG DRIVEN
  Owns admin render/config under admin/src/admin/**. Labels come from STRINGS.admin.*.
```

BFF rule:

- Next.js/API routes may be used only as thin orchestration if needed.
- BFF code may compose backend calls, add session/cookies or adapt response shape.
- BFF code must not own business rules. If a rule protects data, progress, payment, auth, content integrity or rewards, it belongs in Django.

Render-only rule:

- Platform components may branch for layout, animation, native alerts, routing and local UI-only state.
- Platform components must not decide progression, rewards, correctness, permissions, pricing, item logic, SRS logic or content rules.
- If web and mobile need the same behavior, put it in `packages/shared-core/src/hooks/**` or `packages/shared-core/src/services/**`.

## Before Editing

1. Read `CLAUDE.md`.
2. Check `docs/PARITY-AUDIT-EXECUTION.md`.
3. Check the matching doc under `docs/architecture/**` when changing backend, web, mobile, admin or shared-core boundaries.
4. Identify whether the change is domain logic, platform render, backend rule or documentation.
5. If the behavior already exists in `frontend-web/`, inspect it first.
6. If adding visible text, add it to all string locale files first.

## Where Code Goes

| Kind of change | Location |
|---|---|
| Business rules, authz, persistence, seeds | `backend/apps/**` |
| Domain types | `packages/shared-core/src/types/**` |
| API services | `packages/shared-core/src/services/**` |
| Cross-platform state/flow/form logic | `packages/shared-core/src/hooks/**` |
| Validation/mappers/formatters shared by platforms | `packages/shared-core/src/**` |
| Strings | `packages/shared-core/src/constants/strings/**` |
| Tokens | `packages/shared-core/src/theme/**` and mirrored in `web/src/theme/globals.css` |
| Web render | `web/app/**`, `web/src/screens/**`, `web/src/components/**` |
| Mobile render | `mobile/app/**`, `mobile/src/screens/**`, `mobile/src/components/**` |
| Admin render/config | `admin/src/admin/**` |
| Legacy reference | `frontend-web/**` |

## Do Not

- Do not add new architecture to `frontend-web/`.
- Do not duplicate services, hooks or types between `web/` and `mobile/`.
- Do not fetch directly from components.
- Do not put domain state machines, reward logic, gates, validation, permissions, pricing or SRS logic inside render components.
- Do not use Next.js BFF/API routes to bypass or replace Django rules.
- Do not hardcode visible UI text.
- Do not create local label maps for visible copy.
- Do not put visible text inside configs, constants, JSX, CSS pseudo-content, alerts, placeholders, aria labels, table columns, buttons, empty states or errors unless it comes from `STRINGS.*`.
- Do not use Tailwind in `web/`.
- Do not use NativeWind/styled-components in `mobile/`.
- Do not put admin routes inside `web/`; admin belongs in `admin/`.
- Do not use Tailwind in `admin/`; use `--admin-*` variables.
- Do not delete `frontend-web/` until the audit says manual QA passed.

## String Contract

All visible UI text must live in `packages/shared-core/src/constants/strings/{pt-BR,en,de-DE}.ts`.

Use these namespaces:

| Surface | Namespace |
|---|---|
| User app shared text | `STRINGS.app`, `STRINGS.actions`, `STRINGS.nav`, etc. |
| Adventure | `STRINGS.adventure.*` |
| Auth/onboarding/profile/study/vocabulary | matching feature namespace |
| Admin | `STRINGS.admin.*` |

Rules:

- Add the same key to `pt-BR`, `en`, and `de-DE` before using it.
- Import `STRINGS` from `@linguaflow/shared-core`.
- Admin configs must store `STRINGS.admin.*` references, not literal labels.
- Do not add new visible text to only one locale.
- After editing strings, run shared-core typecheck and build.

## Required Validation

After shared-core changes:

```bat
cd packages\shared-core
npm run typecheck
npm run build
```

After web changes:

```bat
cd web
npm run typecheck
npm run build
```

After mobile changes:

```bat
cd mobile
npm run typecheck
```

After admin changes:

```bat
cd admin
npm run build
```

## Task Tracking

Every parity slice must update `docs/PARITY-AUDIT-EXECUTION.md` with:

- what changed
- web path
- mobile path
- shared-core hook/service used
- remaining gaps

## Current Migration Priority

1. Finish rich adventure runner parity.
2. Finish map, inventory, chest, hero and character interactions.
3. Finish guided study runner and scenario polish.
4. Finish profile edit and locale switching.
5. Run manual QA against seeded backend.
6. Only then remove `frontend-web/`.
