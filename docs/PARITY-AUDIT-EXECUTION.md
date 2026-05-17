# Parity Audit Execution

Progress: 13/13 pairs (100% functional coverage, polish pending)

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
| [x] | adventure phase runner | `web/app/aventura/capitulo/[phaseId]` | `mobile/app/adventure/chapter/[phaseId]` | Shared runner, first parity version |
| [x] | adventure inventory | `web/app/aventura/mochila` | `mobile/app/adventure/inventory` | Data parity, UI still simpler than legacy |
| [x] | adventure characters | `web/app/aventura/personagens` | `mobile/app/adventure/characters` | Data parity with character profile modal; images still pending |
| [x] | adventure words | `web/app/aventura/palavras` | `mobile/app/adventure/words` | Data parity, UI still simpler than legacy |
| [x] | adventure chests | `web/app/aventura/baus` | `mobile/app/adventure/chests` | Data parity, UI still simpler than legacy |
| [x] | adventure hero | `web/app/aventura/heroi` | `mobile/app/adventure/hero` | Data parity, UI still simpler than legacy |
| [x] | study home | `web/app/estudo-guiado` | `mobile/app/(tabs)/study` | Data parity, runner still pending |
| [x] | study session | `web/src/screens/StudyScreen` | `mobile/src/screens/StudyScreen` | Shared SRS runner, first parity version |
| [x] | vocabulary | `web/app/vocabulario` | `mobile/app/(tabs)/vocabulary` | Data parity, rich interactions simpler |
| [x] | auth | `web/app/login` | `mobile/app/login` | Basic parity |
| [x] | onboarding | `web/app/onboarding` | `mobile/app/onboarding` | Basic parity |
| [x] | profile/account | `web/app/perfil` | `mobile/app/(tabs)/profile` | Data parity, edit routine/add area pending |
| [x] | history | `web/app/historico` | `mobile/app/history` | Data parity, calendar UI simpler |
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
- Character image constants.

## Pair Matrix

| Status | Pair | Web | Mobile | Shared Hook | Result | Issues |
|---|---|---|---|---|---|---|
| [x] | Adventure map loader | `web/src/screens/AdventureMapScreen` | `mobile/src/screens/AdventureMapScreen` | `useAdventureChapters` | Partial OK | UI is simple scaffold, not feature parity with legacy map |
| [x] | Adventure inventory | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services | Partial OK | Data parity only; item actions/modals are not fully migrated |
| [x] | Adventure chests | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services | Partial OK | Start/claim chest interactions still need parity |
| [x] | Adventure words | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services | Partial OK | Search/filter/rich mastery visuals still need parity |
| [x] | Adventure hero | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services | Partial OK | Achievements/powers rich layout still need parity |
| [x] | Adventure characters | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services | Partial OK | Basic profile modal exists; character images still need parity |
| [x] | Auth/login | `web/src/screens/AuthScreen` | `mobile/src/screens/AuthScreen` | shared services | Partial OK | Global route guard pending |
| [x] | Onboarding | `web/src/screens/OnboardingScreen` | `mobile/src/screens/OnboardingScreen` | shared services | Partial OK | Full app boot flow pending |
| [x] | Study home | `web/src/screens/StudyScreen` | `mobile/src/screens/StudyScreen` | shared services | Partial OK | Guided runner and SRS exercise renderer pending |
| [x] | Vocabulary | `web/src/screens/VocabularyScreen` | `mobile/src/screens/VocabularyScreen` | shared services | Partial OK | Polished filters and empty states can be improved |
| [x] | Profile | `web/src/screens/ProfileScreen` | `mobile/src/screens/ProfileScreen` | shared services | Partial OK | Add area, edit routine, edit profile pending |
| [x] | History | `web/src/screens/HistoryScreen` | `mobile/src/screens/HistoryScreen` | shared services | Partial OK | Legacy calendar richness pending |
| [x] | Adventure phase runner | `web/src/screens/AdventureChapterRunnerScreen` | `mobile/src/screens/AdventureChapterRunnerScreen` | `useAdventurePhaseRunner`, `useAdventureSectionRunner` | First functional parity | Rich legacy animations/audio/character modals pending |
| [x] | Study SRS runner | `web/src/screens/StudyScreen` | `mobile/src/screens/StudyScreen` | `useStudySessionRunner` | First functional parity | Guided lesson runner polish pending |

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

## Remaining Polish Before Retiring Legacy

- Match the rich legacy animations, audio controls, character images and reward visuals in the new renderers.
- Add/profile routine flows now exist in web and mobile; profile edit remains pending.
- Route guards/boot session logic now exists in web and mobile; manual QA is still needed on device/browser.
- Run manual QA against real seeded backend data before deleting `frontend-web/`.
