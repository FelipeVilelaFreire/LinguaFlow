# Parity Audit Execution

Progress: 1/12 pairs (8%)

Checkpoint: 2026-05-17

## Current Decision

The active target is the `_TEMPLATESHARED` architecture:

- `backend/` is the source of truth.
- `packages/shared-core/` owns domain logic, types, services, strings, tokens and cross-platform hooks.
- `web/` and `mobile/` are render-only consumers.
- `frontend-web/` is the legacy working app during migration and must be retired after parity is reached.

## Folder Matrix

| Status | Area | Web | Mobile | Result |
|---|---|---|---|---|
| [x] | initial shell | `web/app`, `web/src/screens` | `mobile/app`, `mobile/src/screens` | OK with limited scope |
| [ ] | adventure map | `web/src/screens/AdventureMapScreen` | `mobile/src/screens/AdventureMapScreen` | Partial |
| [ ] | adventure phase runner | pending | pending | Legacy only |
| [ ] | adventure inventory | pending | pending | Legacy only |
| [ ] | adventure characters | pending | pending | Legacy only |
| [ ] | adventure words | pending | pending | Legacy only |
| [ ] | study home | pending | pending | Legacy only |
| [ ] | study session | pending | pending | Legacy only |
| [ ] | auth | pending | pending | Legacy only |
| [ ] | profile/account | pending | pending | Legacy only |
| [ ] | history | pending | pending | Legacy only |
| [ ] | admin strings | pending | not applicable | Legacy only |

## Shared-Core Ownership

Already moved:

- `packages/shared-core/src/types/adventure`
- `packages/shared-core/src/types/content`
- `packages/shared-core/src/types/sections`
- `packages/shared-core/src/services/adventureService`
- `packages/shared-core/src/services/authService`
- `packages/shared-core/src/services/contentService`
- `packages/shared-core/src/hooks/adventure/useAdventureChapters`
- `packages/shared-core/src/constants/strings`
- `packages/shared-core/src/constants/routes`
- `packages/shared-core/src/theme`
- `packages/shared-core/src/lib/apiClient`
- `packages/shared-core/src/lib/storage`

Still outside shared-core:

- Auth/account screen hooks and renderers.
- Study screen hooks and renderers.
- Phase runner state machine.
- Section chat state machine.
- Audio/browser TTS behavior.
- Full app router/session boot logic.
- Full string tree from legacy `frontend-web/src/constants/strings.ts`.
- Character image/profile constants.

## Pair Matrix

| Status | Pair | Web | Mobile | Shared Hook | Result | Issues |
|---|---|---|---|---|---|---|
| [x] | Adventure map loader | `web/src/screens/AdventureMapScreen` | `mobile/src/screens/AdventureMapScreen` | `useAdventureChapters` | Partial OK | UI is simple scaffold, not feature parity with legacy map |

## Findings

| Severity | File | Problem | Recommendation |
|---|---|---|---|
| Major | `frontend-web/src/features/adventure/**` | Legacy web still owns full adventure UX and much local state | Migrate feature-by-feature into `web/` + `mobile/`, extracting hooks first |
| Major | `frontend-web/src/features/adventure/.../AdventureChapterSections.tsx` | Large section state machine still inside a render component | Extract section runner hook/model into shared-core |
| Major | `frontend-web/src/constants/strings.ts` | Full i18n still lives in legacy web | Move strings by namespace into shared-core |
| Medium | `web/` | New web is a scaffold, not full product parity | Continue migrating Aventura before retiring legacy |
| Medium | `mobile/` | New mobile is a scaffold, not full product parity | Build native renderers against shared hooks |
| Medium | `web/package.json` | Uses `next --webpack` because Turbopack cannot resolve Windows absolute alias in this repo path | Revisit after moving repo path or when Turbopack Windows support improves |

## Decisions

- Do not delete `frontend-web/` until `web/` reaches feature parity.
- Keep migrating logic into shared-core before recreating rich UI on web/mobile.
- Web uses CSS Modules and tokens from now on.
- Mobile uses StyleSheet and shared-core tokens from now on.
- Tailwind remains only in legacy `frontend-web/` during migration.
