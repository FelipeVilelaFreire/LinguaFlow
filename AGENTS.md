# Agent Operating Guide

This file mirrors `CLAUDE.md` for any coding agent working in this repo. If there is a conflict, follow the stricter rule.

## Prime Directive

Follow `docs/_TEMPLATESHARED`. Do not invent a new architecture.

The target is:

- `backend/` is the source of truth.
- `packages/shared-core/` is the single brain.
- `web/` is render-only Next.js.
- `mobile/` is render-only Expo.
- `frontend-web/` is legacy reference only.

## Before Editing

1. Read `CLAUDE.md`.
2. Check `docs/PARITY-AUDIT-EXECUTION.md`.
3. Identify whether the change is domain logic, platform render, backend rule or documentation.
4. If the behavior already exists in `frontend-web/`, inspect it first.

## Where Code Goes

| Kind of change | Location |
|---|---|
| Domain types | `packages/shared-core/src/types/**` |
| API services | `packages/shared-core/src/services/**` |
| Cross-platform state/flow/form logic | `packages/shared-core/src/hooks/**` |
| Strings | `packages/shared-core/src/constants/strings/**` |
| Tokens | `packages/shared-core/src/theme/**` and mirrored in `web/src/theme/globals.css` |
| Web render | `web/app/**`, `web/src/screens/**`, `web/src/components/**` |
| Mobile render | `mobile/app/**`, `mobile/src/screens/**`, `mobile/src/components/**` |
| Legacy reference | `frontend-web/**` |

## Do Not

- Do not add new architecture to `frontend-web/`.
- Do not duplicate services, hooks or types between `web/` and `mobile/`.
- Do not fetch directly from components.
- Do not hardcode visible UI text.
- Do not use Tailwind in `web/`.
- Do not use NativeWind/styled-components in `mobile/`.
- Do not delete `frontend-web/` until the audit says manual QA passed.

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
