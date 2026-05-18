# Parity Audit Execution

Progress: functional coverage exists for the main learner surfaces, but visual/product parity is not complete.

Visual parity reset: 2026-05-18

The previous `13/13 pairs` number meant that the main routes existed and loaded data in both `web` and `mobile`. It did not mean that the migrated product matched `frontend-web`.

From this point forward, a screen can be marked complete only when it passes both gates:

- Functional parity: route exists, data loads from `shared-core` services/hooks, no direct fetch from render components, no domain rules in web/mobile.
- Visual/product parity: layout order, information hierarchy, labels, icons/assets, colors/tokens, spacing, states, interactions and transitions match the legacy `frontend-web` reference as closely as the target platform allows.

Do not mark a pair as `[x]` for visual parity just because it is usable. Use `[~]` for a functional migration that still needs visual/product parity.

Current visual parity status:

| Area | Functional | Visual/Product | Notes |
|---|---:|---:|---|
| App shell/navigation | [~] | [ ] | Sidebar and tabs exist, but add-area/switch-area modal, locale chips and transitions are incomplete. |
| Home `/` | [~] | [ ] | Must match legacy order: course badge, percent, flag/language, language path, series/season/phase, phrase progress, CTA, stats, next session/routine. Current web still has different hierarchy/copy. |
| Guided study `/estudo-guiado` | [~] | [~] | New web design is closer and uses shared strings/tokens, but runner/scenario parity is still pending. |
| Adventure map | [~] | [ ] | Data loads; winding map, node states, transitions and rich map UX still need legacy parity. |
| Adventure runner | [~] | [ ] | Shared runner exists; rich section renderer, audio, rewards and character UX still pending. |
| Inventory/chests/words/hero/characters | [~] | [ ] | Data parity exists; per-tab rich renderers and interactions still pending. |
| Vocabulary | [~] | [ ] | Functional screen exists; filters/rich states need comparison against legacy. |
| Profile/account | [~] | [ ] | Functional screen exists; edit profile, locale switch and routine flows need parity QA. |
| History | [~] | [ ] | Functional screen exists; calendar/rich history UI still simpler than legacy. |

Checkpoint: 2026-05-17

Visual identity checkpoint: 2026-05-18

Current update:

- Legacy language/study colors were moved into `packages/shared-core/src/theme/studyAreaTheme.ts`.
- Legacy adventure color palettes were moved into `packages/shared-core/src/theme/adventureTheme.ts`.
- Flag CDN metadata and character image candidate helpers now live in `packages/shared-core/src/theme/languageAssets.ts`.
- Character avatar slug lookup now lives in `packages/shared-core/src/theme/characterAssets.ts`.
- Legacy public assets (`lang-plus.svg` and `de/es/it/characters`) were copied into `web/public/` and `mobile/assets/`.
- `web` adventure map, collection screens and phase runner now consume shared adventure theme variables.
- `mobile` adventure map, collection styles and runner styles now consume shared adventure theme tokens.

Interpretation:

- This is not full visual parity yet. It is the shared visual foundation needed before migrating the richer legacy renderers.
- Next parity slices should replace the generic collection screen with per-tab renderers and migrate the legacy map/runner interactions.

## Visual Parity Contract

Every parity slice must start by inspecting the matching legacy files under `frontend-web/**`.

For each screen, record the legacy source and target files before editing:

| Requirement | Expected proof |
|---|---|
| Legacy reference inspected | Exact `frontend-web/**` file path listed in this doc or the PR notes. |
| Web target | Exact `web/**` route/screen/components listed. |
| Mobile target | Exact `mobile/**` route/screen/components listed, or a documented platform exception. |
| Shared owner | Hook/service/type/string/token path listed under `packages/shared-core/**`. |
| Text contract | New visible labels added to `pt-BR`, `en`, and `de-DE`; no new hardcoded visible copy in JSX/config/CSS. |
| Token contract | Colors/assets come from shared tokens/theme helpers or copied legacy assets; no new arbitrary palette. |
| Render-only contract | Web/mobile render only; business rules stay in backend/shared-core. |
| Visual order | The order of visible blocks matches the legacy screen unless a platform exception is documented. |
| States | Loading, empty, error, disabled, active/current/completed/locked states match legacy intent. |
| Validation | Required typecheck/build commands listed with pass/fail result. |

Completion labels:

- `[ ]`: not migrated or not checked.
- `[~]`: functional migration exists, visual/product parity still incomplete.
- `[x]`: functional and visual/product parity accepted after manual comparison.

Do not use `[x]` until the screen has been manually compared against `frontend-web` with seeded backend data.

## Immediate Slice: Home

Legacy reference:

- `frontend-web/src/pages/HomePage.tsx` or the matching legacy home feature/component files if the route delegates.
- `frontend-web/src/components/layout/AppLayout.tsx` for the sidebar/mobile shell around the home route.
- Legacy strings/constants used by the home card and area selector.

Targets:

- Web: `web/app/page.tsx`, `web/src/screens/HomeScreen/**`, `web/src/components/AppShell/**`.
- Mobile: matching `mobile/app/(tabs)` home route and `mobile/src/screens/HomeScreen/**` if present.
- Shared: `packages/shared-core/src/constants/strings/**`, `packages/shared-core/src/theme/**`, `packages/shared-core/src/services/**` or hooks if reusable state is needed.

Acceptance criteria for the main home block:

- Visible order matches legacy: area/course badge, progress percent, flag, target language name, language path, series/season/phase, phrase progress, continue adventure CTA, stats, next session/routine.
- Text comes from `STRINGS.*` or backend/seed content; no hardcoded visible labels in web/mobile renderers.
- Course/area colors come from shared study-area theme tokens.
- Flag and logo assets use the shared language asset helpers or copied legacy assets.
- Web desktop keeps the sidebar text on the left and uses the same primary layout width/density as legacy.
- Mobile keeps the current bottom-tab/header direction unless the legacy mobile reference proves otherwise.
- Any data mismatch, such as `30 min` vs `60 min`, must be traced to backend/seed/current goal data rather than patched in render code.

Home parity example accepted on 2026-05-18:

The correct migration pattern is the one used for the main home block after comparison with `http://localhost:5173/`.

Expected legacy order:

1. Course badge: `ES · NONE → A1`.
2. Progress percent: `0%`.
3. Flag plus target language name.
4. Language path: `Portugues para Espanhol - A1`.
5. Adventure position: `Serie NONE · NONE · T2 · F3`.
6. Phrase progress: `0 / 104 frases`.
7. Primary CTA: `Continuar Aventura`.
8. Stats block: `Sequencia`, `Palavras`, `Nivel`.
9. Next session card: title, computed next session date, routine days and minutes.

Implementation rules from this example:

- Do not add a new top banner or dashboard block if the legacy screen does not have it in that position.
- Do not replace the legacy hierarchy with a new "today dashboard" hierarchy unless the user explicitly approves that product change.
- Keep backend/seed values as the source of truth. For example, `30 min` vs `60 min` must come from `goal.session_minutes`, not from hardcoded render fixes.
- Move visible formatting such as `home.levelBadge`, `home.nextSession`, and `home.adventurePosition` into `STRINGS.*`.
- Use shared theme helpers such as `getStudyAreaThemeVars` and language asset helpers instead of arbitrary local colors/assets.
- Web and mobile should consume the same data and copy, but platform layout may adapt only for ergonomics, not to change the product order.
- When a slice looks good, document the accepted visible order here so the next slice can follow the same standard.

Home/layout checkpoint: 2026-05-18

- `web/src/components/AppShell/**` now restores the logged-in app frame: desktop sidebar, mobile header and bottom navigation.
- `web/src/components/AppBoot/AppBoot.tsx` wraps authenticated routes with `AppShell` while leaving auth/onboarding and chapter runner immersive.
- `web/src/screens/HomeScreen/**` now loads the active goal and renders the language area, flag, progress, routine and action cards instead of a landing-style placeholder.
- `web/src/screens/HomeScreen/HomeScreen.tsx` now mirrors the legacy home block order from `frontend-web/src/features/home/screens/HomeScreen.tsx`: course badge, percent, flag/language, language path, series/season/phase, phrase progress, CTA, stats, next session/routine.
- `mobile/src/screens/HomeScreen/**` now uses the same data and visible order for the mobile home surface.
- Shared-core strings added for `home.nextSession` and `home.allDays`; `home.adventurePosition` was restored to the legacy middle-dot format.
- Validation: `packages/shared-core npm run typecheck`, `packages/shared-core npm run build`, `web npm run typecheck`, `web npm run build`, and `mobile npm run typecheck` passed.
- Remaining gap: the shell is a first CSS Modules migration of the legacy layout. It still needs the full add-area/switch-area modal, locale chips and exact transition overlay parity from `frontend-web/src/components/layout/AppLayout.tsx`.

Guided study checkpoint: 2026-05-18

- `packages/shared-core/src/constants/strings/**` now owns the guided study, tab, state and SRS review labels used by web and mobile.
- `web/src/screens/StudyScreen/**` now follows the legacy `frontend-web/src/features/study/screens/StudyScreen.tsx` structure more closely: guided/modules tabs, next adventure phase card, current lesson card, phrase preview, SRS review card and seed module trail.
- `web/src/screens/StudyScreen/**` now applies shared study-area theme variables instead of the generic scaffold palette.
- `mobile/src/screens/StudyScreen/StudyScreen.tsx` now consumes the same shared strings for the existing mobile study surface.
- Shared-core hook/service used: `adventureService.getStudySession`, `adventureService.listChapters`, `contentService.listStudyModules`, `contentService.listPhrases`, `contentService.getCurrentGoal`, and `useStudySessionRunner`.
- Remaining gaps: the full legacy `GuidedLessonRunner` step flow, audio speak button, answer feedback animations and scenario tab renderer still need their own parity slice before this area is complete.

## Current Decision

The active target is the local shared architecture:

- `backend/` is the source of truth.
- `packages/shared-core/` owns domain logic, types, services, strings, tokens and cross-platform hooks.
- `web/` and `mobile/` are render-only consumers.
- `frontend-web/` is now a frozen legacy reference. It must not receive new product work and must only be deleted after QA confirms parity.

## Primary Architecture Rules

The main contract is architectural. Strings are important, but they are only one part of the larger rule set.

```txt
backend     = SOURCE OF TRUTH
shared-core = BRAIN
web/mobile  = RENDER ONLY
admin       = CONFIG DRIVEN
```

Required ownership:

- `backend/` owns business rules, authorization, validation, persistence, seeds, content truth, rewards and progress integrity.
- `packages/shared-core/` owns hooks, services, domain types, strings, tokens, validation helpers, mappers and cross-platform state machines.
- `web/` owns Next.js routes, CSS Modules, browser UX, route guards and render-only screens/components.
- `mobile/` owns Expo routes, StyleSheet, native UX, mobile guards and render-only screens/components.
- `admin/` owns config-driven admin apps, operational views and business-plan dashboards.

BFF rule:

- Next.js server actions or API routes may exist only as a thin orchestration layer.
- BFF may compose Django calls, attach session/cookies, adapt response shape or cache server-side.
- BFF must not own rules for authorization, payment, progress, rewards, SRS, item use, phase completion, content integrity or admin permissions.
- If a rule appears in web/mobile/admin, Django must enforce it too.

Render-only rule:

- Platform components may render, style, animate, route, show toasts/alerts, and hold local UI-only state.
- Platform components must not decide progression, correctness, rewards, pricing, permissions, item behavior, SRS scheduling or content rules.
- Shared behavior goes to `packages/shared-core/src/hooks/**`.
- HTTP goes to `packages/shared-core/src/services/**`.
- Durable truth goes to Django.

## Non-Negotiable String Rule

All visible UI text must come from `packages/shared-core/src/constants/strings/{pt-BR,en,de-DE}.ts`.

This includes:

- button labels;
- page titles and subtitles;
- placeholders;
- aria labels;
- table columns;
- admin config labels;
- modal text;
- empty states;
- errors;
- badges/status labels;
- toast/alert text.

Required pattern:

- user app text uses `STRINGS.app`, `STRINGS.actions`, `STRINGS.nav`, `STRINGS.adventure`, or the matching feature namespace;
- admin text uses `STRINGS.admin.*`;
- every new key is added to `pt-BR`, `en`, and `de-DE`;
- after string changes, run `npm run typecheck` and `npm run build` in `packages/shared-core`.

Hardcoded visible strings are allowed only in seed/story/content data owned by backend or docs. Renderer UI must not hardcode copy.

## Current Platform Status

The new `web/` and `mobile/` apps now have the main functional coverage that existed as the central product surface in `frontend-web/`.

Covered in both new platforms:

- Login.
- Onboarding.
- App shell and navigation.
- Adventure map.
- Adventure chapter/phase runner.
- Adventure inventory.
- Adventure chests.
- Adventure learned words.
- Adventure hero.
- Adventure characters.
- Guided study / study session.
- Vocabulary.
- Profile.
- History.
- Session/route guards.
- Shared adventure and study hooks in `packages/shared-core`.

Not covered yet by the new shared architecture migration:

- Full admin CRUD/form builder per entity.
- Admin trash/history apps.
- Backend soft-delete/audit endpoints for universal admin apps.

Current interpretation:

- `frontend-web/` is legacy and should be treated as read-only reference.
- `web/` is the official new web frontend.
- `mobile/` is the official new mobile app.
- `packages/shared-core/` is the shared brain for types, services, strings, tokens and cross-platform hooks.
- `backend/` remains the source of truth for business rules and content.
- `admin/` exists as the dedicated admin app. It replaces the old `frontend-admin/` folder name and must follow the local config-driven admin architecture.

Deletion rule:

`frontend-web/` can be removed only after manual QA proves that `web/` and `mobile/` cover the required flows with real backend and seeded data. Until then, keep it for comparison against legacy behavior and visual parity.

## Admin And Business Model Status

The repository currently has two admin surfaces:

- Django Admin at `/admin/`.
- React admin in `admin/`.

Current React admin coverage:

- Dashboard.
- Users.
- Goals/areas.
- Content catalog.
- Study/learning overview.
- Adventure overview.
- Progress overview.
- System/Django app map.
- Business model / business-plan scenario table.
- Backend endpoints under `/api/admin-dashboard/*`.
- Config-driven app registry under `admin/src/admin/apps/*`.
- Admin copy under `STRINGS.admin.*`.
- Admin CSS variables under `--admin-*`.

Important gap:

`admin/` now follows the local folder/name direction and is separated from `web/`, but it is not a full CRUD admin yet.

Required target for admin parity:

- Keep admin separate from `web/`; do not put admin routes inside the learner-facing Next app.
- Keep upgrading `admin/` as a config-driven admin architecture.
- Maintain `admin/src/admin/apps/business-plan/`.
- Move all visible admin labels to `STRINGS.admin.*` in `packages/shared-core/src/constants/strings/{pt-BR,en,de-DE}.ts`.
- Use admin-specific CSS variables with `--admin-*`.
- Add shared admin primitives: layout, sidebar, topbar, list page, detail page, tabs, form builder, cards, badges, modal, toast.
- Add universal admin apps for trash and history if backend support exists.
- Keep backend admin endpoints protected by `IsAdminUser`.

Business model status:

- `docs/BUSINESS-MODEL.md` must exist before serious launch or heavy feature expansion.
- The admin should eventually expose the same model as a `business-plan` app with pessimistic, realistic and optimistic scenarios.
- The business model must separate registered users, active users and paying customers.
- The business model must separate revenue, infra cost, AI/API cost, storage, payment fees, taxes, marketing, support and runway.
- Every major financial assumption must map to a validation action.

## Folder Matrix

| Status | Area | Web | Mobile | Result |
|---|---|---|---|---|
| [~] | initial shell | `web/app`, `web/src/screens` | `mobile/app`, `mobile/src/screens` | Functional with limited scope; visual parity still pending |
| [ ] | adventure map | `web/src/screens/AdventureMapScreen` | `mobile/src/screens/AdventureMapScreen` | Partial |
| [~] | adventure phase runner | `web/app/aventura/capitulo/[phaseId]` | `mobile/app/adventure/chapter/[phaseId]` | Shared runner, first functional version; rich visual parity pending |
| [~] | adventure inventory | `web/app/aventura/mochila` | `mobile/app/adventure/inventory` | Data parity, UI still simpler than legacy |
| [~] | adventure characters | `web/app/aventura/personagens` | `mobile/app/adventure/characters` | Data parity with character profile modal; images still pending |
| [~] | adventure words | `web/app/aventura/palavras` | `mobile/app/adventure/words` | Data parity, UI still simpler than legacy |
| [~] | adventure chests | `web/app/aventura/baus` | `mobile/app/adventure/chests` | Data parity, UI still simpler than legacy |
| [~] | adventure hero | `web/app/aventura/heroi` | `mobile/app/adventure/hero` | Data parity, UI still simpler than legacy |
| [~] | study home | `web/app/estudo-guiado` | `mobile/app/(tabs)/study` | Better visual pass started; runner still pending |
| [~] | study session | `web/src/screens/StudyScreen` | `mobile/src/screens/StudyScreen` | Shared SRS runner, first functional version |
| [~] | vocabulary | `web/app/vocabulario` | `mobile/app/(tabs)/vocabulary` | Data parity, rich interactions simpler |
| [~] | auth | `web/app/login` | `mobile/app/login` | Basic functional parity; visual QA pending |
| [~] | onboarding | `web/app/onboarding` | `mobile/app/onboarding` | Basic functional parity; visual QA pending |
| [~] | profile/account | `web/app/perfil` | `mobile/app/(tabs)/profile` | Data parity, edit routine/add area pending |
| [~] | history | `web/app/historico` | `mobile/app/history` | Data parity, calendar UI simpler |
| [x] | admin strings | `packages/shared-core/src/constants/strings/*` | not applicable | `STRINGS.admin.*` namespace exists; keep expanding as admin grows |

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
- `packages/shared-core/src/theme/adventureTheme`
- `packages/shared-core/src/theme/studyAreaTheme`
- `packages/shared-core/src/theme/languageAssets`
- `packages/shared-core/src/theme/characterAssets`
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

## Pair Matrix

| Status | Pair | Web | Mobile | Shared Hook | Result | Issues |
|---|---|---|---|---|---|---|
| [~] | Adventure map loader | `web/src/screens/AdventureMapScreen` | `mobile/src/screens/AdventureMapScreen` | `useAdventureChapters` | Functional only | UI is simple scaffold, not feature parity with legacy map |
| [~] | Adventure inventory | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services | Functional only | Data parity only; item actions/modals are not fully migrated |
| [~] | Adventure chests | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services | Functional only | Start/claim chest interactions still need parity |
| [~] | Adventure words | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services | Functional only | Search/filter/rich mastery visuals still need parity |
| [~] | Adventure hero | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services | Functional only | Achievements/powers rich layout still need parity |
| [~] | Adventure characters | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services | Functional only | Basic profile modal exists; character images still need parity |
| [~] | Auth/login | `web/src/screens/AuthScreen` | `mobile/src/screens/AuthScreen` | shared services | Functional only | Global route guard and visual QA pending |
| [~] | Onboarding | `web/src/screens/OnboardingScreen` | `mobile/src/screens/OnboardingScreen` | shared services | Functional only | Full app boot flow and visual QA pending |
| [~] | Study home | `web/src/screens/StudyScreen` | `mobile/src/screens/StudyScreen` | shared services | Functional plus first visual pass | Guided runner and SRS exercise renderer pending |
| [~] | Vocabulary | `web/src/screens/VocabularyScreen` | `mobile/src/screens/VocabularyScreen` | shared services | Functional only | Polished filters and empty states can be improved |
| [~] | Profile | `web/src/screens/ProfileScreen` | `mobile/src/screens/ProfileScreen` | shared services | Functional only | Add area, edit routine, edit profile pending |
| [~] | History | `web/src/screens/HistoryScreen` | `mobile/src/screens/HistoryScreen` | shared services | Functional only | Legacy calendar richness pending |
| [~] | Adventure phase runner | `web/src/screens/AdventureChapterRunnerScreen` | `mobile/src/screens/AdventureChapterRunnerScreen` | `useAdventurePhaseRunner`, `useAdventureSectionRunner` | First functional parity | Rich legacy animations/audio/character modals pending |
| [~] | Study SRS runner | `web/src/screens/StudyScreen` | `mobile/src/screens/StudyScreen` | `useStudySessionRunner` | First functional parity | Guided lesson runner polish pending |

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
