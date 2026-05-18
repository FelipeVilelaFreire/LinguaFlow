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
| Home `/` | [~] | [~] | Main block now follows the accepted legacy order; shell/add-area/switch-area QA is still pending before `[x]`. |
| Auth/onboarding | [~] | [~] | Onboarding now uses the legacy `lang-plus.svg`, two-step card flow, flag cards, level/routine controls, progress bar and shared strings; manual browser/device QA still pending. |
| Guided study `/estudo-guiado` | [~] | [~] | Web/mobile now include tabs, current lesson, phrase runner, SRS review and study trail; full legacy guided exercise/scenario parity still pending. |
| Adventure entry/map | [~] | [~] | `/aventura` and mobile adventure tab render a hub; map now has legacy-style winding path, phase states, season headers and adventure menu. Rich map interactions still need QA. |
| Adventure runner | [~] | [~] | Shared runner now uses shared strings, web TTS/audio cues, NPC replay, answer/section animations and richer trophy/reward stages; full legacy dev voice lab and deeper character UX still pending. |
| Inventory/chests/words/hero/characters | [~] | [~] | Collection tabs share the adventure shell; inventory, chests, words and characters open details, with item use, chest open/claim, slots/timers and reward states wired. Hero polish still pending. |
| Vocabulary | [~] | [~] | Web/mobile now follow the legacy saved-phrases structure with shared strings, filters, summary cards, empty states and rich phrase cards; manual QA still pending. |
| Profile/account | [~] | [~] | Account surface now follows the legacy profile hierarchy; edit-profile/locale switch and manual QA still pending. |
| History | [~] | [~] | Web/mobile now follow the legacy month calendar, stats, all/by-area toggle, legends and shared strings; manual QA still pending. |

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
- `web/src` and `mobile/src` now follow the same top-level organization contract: `components`, `config`, `contexts`, `hooks`, `lib`, `screens`, `setup`, `styles`, and `utils`.
- `web/src/components` and `mobile/src/components` now follow the same component organization contract: `cards`, `features`, `layout`, `modals`, `shared`, and `ui`.
- New platform files must respect this structure by default. Do not add new top-level `src` folders or loose component folders unless the architecture section below is updated first.

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

- Web: `web/app/page.tsx`, `web/src/screens/HomeScreen/**`, `web/src/components/layout/AppShell/**`.
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

- `web/src/components/layout/AppShell/**` now restores the logged-in app frame: desktop sidebar, mobile header and bottom navigation.
- `web/src/components/layout/AppBoot/AppBoot.tsx` wraps authenticated routes with `AppShell` while leaving auth/onboarding and chapter runner immersive.
- `web/src/screens/HomeScreen/**` now loads the active goal and renders the language area, flag, progress, routine and action cards instead of a landing-style placeholder.
- `web/src/screens/HomeScreen/HomeScreen.tsx` now mirrors the legacy home block order from `frontend-web/src/features/home/screens/HomeScreen.tsx`: course badge, percent, flag/language, language path, series/season/phase, phrase progress, CTA, stats, next session/routine.
- `mobile/src/screens/HomeScreen/**` now uses the same data and visible order for the mobile home surface.
- Shared-core strings added for `home.nextSession` and `home.allDays`; `home.adventurePosition` was restored to the legacy middle-dot format.
- Validation: `packages/shared-core npm run typecheck`, `packages/shared-core npm run build`, `web npm run typecheck`, `web npm run build`, and `mobile npm run typecheck` passed.
- Remaining gap: the shell is a first CSS Modules migration of the legacy layout. It still needs the full add-area/switch-area modal, locale chips and exact transition overlay parity from `frontend-web/src/components/layout/AppLayout.tsx`.

Guided study checkpoint: 2026-05-18

- Legacy references inspected: `frontend-web/src/features/study/screens/StudyScreen.tsx`, `StudySessionScreen.tsx`, `GuidedLessonRunner.tsx`, `ScenariosScreen.tsx`, and `TodayScreen.tsx`.
- Web target updated: `web/src/screens/StudyScreen/StudyScreen.tsx` and `web/src/screens/StudyScreen/StudyScreen.module.css`.
- Mobile target updated: `mobile/src/screens/StudyScreen/StudyScreen.tsx` and `mobile/src/screens/StudyScreen/StudyScreen.styles.ts`.
- Shared owner: `packages/shared-core/src/constants/strings/**`, `adventureService.getStudySession`, `adventureService.listChapters`, `contentService.listStudyModules`, `contentService.listPhrases`, `contentService.getCurrentGoal`, and `useStudySessionRunner`.
- Shared strings added in `pt-BR`, `en`, and `de-DE` for the phrase runner title, progress, source/target labels, translation reveal, next phrase and finish action.
- Web now opens a phrase lesson runner from the hero/current lesson CTA, keeps the guided/modules tabs, and preserves the current lesson, SRS review and module trail structure.
- Mobile now follows the same study hierarchy: session/modules tabs, adventure context hero, current lesson phrase previews, SRS review card, module/lesson trail, SRS review runner and phrase runner.
- Validation: `packages/shared-core npm.cmd run typecheck`, `packages/shared-core npm.cmd run build`, `web npm.cmd run typecheck`, `web npm.cmd run build`, and `mobile npm.cmd run typecheck` passed.
- Remaining gaps: this is not full legacy `GuidedLessonRunner` parity yet. Audio speak controls, full exercise renderer, answer feedback animations, richer scenario tab content and the old `TodayScreen` lesson-card flow still need dedicated parity slices.

Onboarding checkpoint: 2026-05-18

- Legacy reference inspected: `frontend-web/src/features/auth/screens/OnboardingScreen.tsx` and `frontend-web/src/styles/globals.css` `onb-*` / `auth-*` rules.
- Web target inspected/updated: `web/src/screens/OnboardingScreen/OnboardingScreen.tsx` and `web/src/screens/OnboardingScreen/OnboardingScreen.module.css`.
- Mobile target updated: `mobile/src/screens/OnboardingScreen/OnboardingScreen.tsx` and `mobile/src/screens/OnboardingScreen/OnboardingScreen.styles.ts`.
- Shared owner: `packages/shared-core/src/constants/strings/**`, `packages/shared-core/src/theme/languageAssets.ts`, `adventureService.listAvailableLanguages`, and `contentService.createGoal`.
- `lang-plus.svg` is present with the same hash in `frontend-web/public/`, `web/public/`, and `mobile/assets/`; onboarding web/mobile now render that asset.
- Mobile onboarding now mirrors the legacy/web structure: centered shell, logo plus step counter, 4px progress bar, card panel, language flag cards with check state, A1 level pill, weekday pills, session duration pills, estimate card, back button and primary CTA.
- Web onboarding visual tokens were realigned with the legacy reference: teal glow, 4px progress bar, 2px select-card/pill borders, rounded day pills and shared-string logo alt.
- Text contract: visible labels and alt text come from `STRINGS.*` or backend language metadata; removed mobile hardcoded `Portugues`, `Voltar`, and `Carregando...`.
- Validation: `mobile npm.cmd run typecheck` passed; `web npm.cmd run typecheck` passed.
- Remaining gaps: manual browser/device QA with seeded backend data is still required before marking onboarding `[x]`; auth/login visual parity is a separate slice.

Profile/account checkpoint: 2026-05-18

- Legacy reference inspected: `frontend-web/src/features/account/screens/AccountScreen.tsx`, `frontend-web/src/features/account/screens/EditProfileScreen.tsx`, and legacy profile/add-area/routine styles.
- Web target updated: `web/src/screens/ProfileScreen/ProfileScreen.tsx` and `web/src/screens/ProfileScreen/ProfileScreen.module.css`.
- Mobile target updated: `mobile/src/screens/ProfileScreen/ProfileScreen.tsx` and `mobile/src/screens/ProfileScreen/ProfileScreen.styles.ts`.
- Shared owner: `packages/shared-core/src/constants/strings/**`, `contentService.listGoals`, `contentService.activateGoal`, `contentService.updateGoal`, `contentService.deleteGoal`, `contentService.getHistory`, `authService.me`, and `authService.logout`.
- Shared strings added for `STRINGS.profile.*` and `STRINGS.actions.delete` in `pt-BR`, `en`, and `de-DE`; Profile renderers no longer hardcode the main labels, modal labels, loading state, delete copy or routine actions.
- Web/mobile Profile now follow the legacy account hierarchy: user card, active course card with flag and routine, week activity preview, other areas list with use/delete actions, add-area card, plan card and sign-out action.
- Add-area and edit-routine modals now use shared copy, shared language metadata, weekday/session controls and backend services on both web and mobile.
- Mobile profile add/edit/delete modals now live in `mobile/src/components/modals/ProfileModals.tsx`; `ProfileScreen` keeps only modal state and goal callbacks.
- Validation: `packages/shared-core npm.cmd run typecheck` passed; `packages/shared-core npm.cmd run build` passed; `web npm.cmd run typecheck` passed; `web npm.cmd run build` passed; `mobile npm.cmd run typecheck` passed.
- Remaining gaps: the separate legacy `EditProfileScreen` account settings/locale switch surface is not fully recreated yet; manual browser/device QA with seeded backend data is still required before marking Profile `[x]`.

Vocabulary checkpoint: 2026-05-18

- Legacy reference inspected: `frontend-web/src/features/study/screens/VocabularyScreen.tsx`.
- Web target updated: `web/src/screens/VocabularyScreen/VocabularyScreen.tsx` and `web/src/screens/VocabularyScreen/VocabularyScreen.module.css`.
- Mobile target updated: `mobile/src/screens/VocabularyScreen/VocabularyScreen.tsx` and `mobile/src/screens/VocabularyScreen/VocabularyScreen.styles.ts`.
- Shared owner: `packages/shared-core/src/constants/strings/**`, `contentService.listFavorites`, and `contentService.removeFavorite`.
- Shared strings added for `STRINGS.vocabulary.*` in `pt-BR`, `en`, and `de-DE`; loading, error, header, filters, empty states, remove label and metadata fallback copy now come from shared-core.
- Web/mobile now render the same vocabulary hierarchy: header, saved/scenario/category counters, horizontal scenario filters, empty/filter-empty states, phrase cards, source/target text, scenario/category/difficulty metadata and remove action.
- Validation: `packages/shared-core npm.cmd run typecheck` passed; `packages/shared-core npm.cmd run build` passed; `web npm.cmd run typecheck` passed; `web npm.cmd run build` passed; `mobile npm.cmd run typecheck` passed.
- Remaining gaps: manual browser/device QA with seeded favorites is still required before marking Vocabulary `[x]`; any future richer search/sort mastery controls should remain shared-string driven.

History checkpoint: 2026-05-18

- Legacy reference inspected: `frontend-web/src/features/history/screens/HistoryScreen.tsx`.
- Web target updated: `web/src/screens/HistoryScreen/HistoryScreen.tsx` and `web/src/screens/HistoryScreen/HistoryScreen.module.css`.
- Mobile target updated: `mobile/src/screens/HistoryScreen/HistoryScreen.tsx` and `mobile/src/screens/HistoryScreen/HistoryScreen.styles.ts`.
- Shared owner: `packages/shared-core/src/constants/strings/**`, `contentService.getHistory`, `HistoryMonth`, `GoalHistory`, `HistoryDay`, and `getStudyAreaTheme`.
- Shared strings added for `STRINGS.history.*` in `pt-BR`, `en`, and `de-DE`; loading, error, month nav, stats, segmented view, legends, active badge and empty states now come from shared-core.
- Web/mobile now render the same legacy-aligned structure: month navigation, best streak/completed days/session stats, all/by-area toggle, merged monthly calendar, per-area calendars, completed/planned/open legend, active-area badge and empty/error states.
- Validation: `packages/shared-core npm.cmd run typecheck` passed; `packages/shared-core npm.cmd run build` passed; `web npm.cmd run typecheck` passed; `web npm.cmd run build` passed; `mobile npm.cmd run typecheck` passed.
- Remaining gaps: manual browser/device QA with seeded history data is still required before marking History `[x]`; if lesson-level drilldown returns, it should be added as a dedicated parity slice.

Adventure entry checkpoint: 2026-05-18

- User decision: Aventura must have its own entry screen first; navigation must not jump directly to the map.
- Web updated: `web/src/components/layout/AppShell/AppShell.tsx`, `web/src/screens/HomeScreen/HomeScreen.tsx`, `web/src/screens/StudyScreen/StudyScreen.tsx`, and `web/src/screens/AdventureScreen/**`.
- Mobile updated: `mobile/app/(tabs)/adventure.tsx`, `mobile/app/adventure/map.tsx`, `mobile/src/screens/AdventureScreen/**`, `mobile/src/screens/AdventureCollectionScreen/AdventureCollectionScreen.tsx`, and `mobile/src/screens/AdventureChapterRunnerScreen/AdventureChapterRunnerScreen.tsx`.
- Shared strings added for the adventure hub and collection shortcut labels in `pt-BR`, `en`, and `de-DE`.
- Web now routes shell/Home/Study adventure entry actions to `ROUTES.adventure`; `/aventura` renders the hub and only then links to `ROUTES.adventureMap`.
- Mobile tab `/(tabs)/adventure` now renders the hub; the map moved to `/adventure/map`, and collection/runner return links target that map route.
- Validation: `packages/shared-core npm.cmd run typecheck` passed; `packages/shared-core npm.cmd run build` passed; `web npm.cmd run typecheck` passed; `web npm.cmd run build` passed; `mobile npm.cmd run typecheck` passed.
- Remaining gaps: this only fixes the entry point. Map parity, collection tabs and runner richness still need separate Aventura slices.

Adventure transition checkpoint: 2026-05-18

- Legacy reference inspected: `frontend-web/src/components/navigation/ImmersiveTransitionOverlay.tsx` and `frontend-web/src/hooks/useImmersiveNav.tsx`.
- Web added `web/src/components/features/adventure/AdventureTransitionLink/**`; Home, Study and the Adventure hub primary CTA now show an immersive overlay before navigating to `ROUTES.adventureMap`.
- Mobile added `mobile/src/components/features/adventure/AdventureTransitionButton.tsx`; Home, Study and the Adventure hub primary CTA now show the native transition modal before navigating to `/adventure/map`.
- Product rule clarified: navigation/tab entry can land on the `/aventura` hub, but explicit “continue/open adventure” CTAs transition directly into the map.
- Validation: `web npm.cmd run typecheck` passed; `web npm.cmd run build` passed; `mobile npm.cmd run typecheck` passed.

Adventure map checkpoint: 2026-05-18

- Legacy reference inspected: `frontend-web/src/features/adventure/screens/adventure/abas/mapa/AdventureMapScreen.tsx`.
- Web target updated: `web/src/screens/AdventureMapScreen/AdventureMapScreen.tsx` and `web/src/screens/AdventureMapScreen/AdventureMapScreen.module.css`.
- Mobile target updated: `mobile/src/screens/AdventureMapScreen/AdventureMapScreen.tsx` and `mobile/src/screens/AdventureMapScreen/AdventureMapScreen.styles.ts`.
- Shared strings expanded for map labels, phase states, section labels, phase detail labels and season progress in `pt-BR`, `en`, and `de-DE`.
- Web map now renders the legacy-style adventure shell: horizontal adventure menu, season header, winding SVG path, phase nodes, completed/current/locked states, boss/review styling, section progress ring and a phase detail modal before entering the runner.
- Mobile map now mirrors the same product structure with a native horizontal menu, season cards, absolute winding path segments, positioned phase nodes and a native bottom-sheet phase detail modal before entering the runner.
- Validation: `packages/shared-core npm.cmd run typecheck` passed; `packages/shared-core npm.cmd run build` passed; `web npm.cmd run typecheck` passed; `web npm.cmd run build` passed; `mobile npm.cmd run typecheck` passed.
- Remaining gaps: manual browser/device QA is needed for exact path spacing and touch behavior; decorative seasonal dividers and finer modal animation polish can be a follow-up map polish slice.

Adventure collection checkpoint: 2026-05-18

- Web target updated: `web/src/screens/AdventureCollectionScreen/AdventureCollectionScreen.tsx`.
- Mobile target updated: `mobile/src/screens/AdventureCollectionScreen/AdventureCollectionScreen.tsx`.
- Web modal structure updated: Aventura detail/character modals now live in `web/src/components/modals/**` and use the shared `BaseModal` wrapper instead of being embedded in the screen file.
- Mobile modal structure updated: Aventura detail/character sheets now live in `mobile/src/components/modals/**`, with `AdventureCollectionScreen` keeping only selected state and refresh callbacks.
- Shared strings expanded for collection tab titles, subtitles, empty states, load error, item status, chest labels and hero metrics in `pt-BR`, `en`, and `de-DE`.
- Collection tabs now include the same top-level adventure menu structure as the map: hub, map, mochila, baus, palavras, heroi and personagens.
- Web/mobile collection renderers now use `STRINGS.adventure.*` for visible UI copy while keeping backend-owned content such as item names, lore, character descriptions and word data unchanged.
- Validation: `packages/shared-core npm.cmd run typecheck` passed; `packages/shared-core npm.cmd run build` passed; `web npm.cmd run typecheck` passed; `web npm.cmd run build` passed; `mobile npm.cmd run typecheck` passed.
- Web/mobile collection renderers now open detail modals/sheets for inventory items, chests, learned words and characters. Inventory uses `adventureService.useInventoryItem`, while chests use `startChest`/`claimChest` and refresh the tab after the action.
- Remaining gaps: hero progression remains metric-first and still needs legacy animation/achievement polish; character art/details are functional but can be enriched with the full legacy presentation.

Adventure runner checkpoint: 2026-05-18

- Web target updated: `web/src/screens/AdventureChapterRunnerScreen/AdventureChapterRunnerScreen.tsx`.
- Mobile target updated: `mobile/src/screens/AdventureChapterRunnerScreen/AdventureChapterRunnerScreen.tsx`.
- Web phase modal structure updated: the map phase modal now lives in `web/src/components/modals/AdventurePhaseModal.tsx` and uses the same `BaseModal` wrapper as collection modals.
- Mobile phase modal structure updated: the native map phase sheet now lives in `mobile/src/components/modals/AdventurePhaseModal.tsx`, and `AdventureMapScreen` keeps only the selected phase state.
- Web audio adapter added: `web/src/lib/audioService.ts`, porting the legacy browser TTS/audio-url fallback, NPC voice profile matching, muted state, speed storage and correct/wrong/complete tones.
- Shared hook updated: `packages/shared-core/src/hooks/adventure/useAdventureSectionRunner.ts` now preserves NPC `pace`, `speech_rate`, `voice`, `audio_url` and NPC reactions so clients can render/play richer section beats.
- Shared strings expanded for runner loading, empty section, recap, answer feedback, section completion, counters and completion stages in `pt-BR`, `en`, and `de-DE`.
- Runner visible copy now uses `STRINGS.adventure.*` / `STRINGS.actions.*` on both web and mobile instead of hardcoded Portuguese labels.
- Web runner now auto-plays/replays NPC lines with audio-url fallback/TTS, plays answer/complete cues, and has animated answer cards, section summary, trophy stars and chest/item reveal.
- Mobile runner now has richer trophy/reward completion presentation matching the same product moments without adding native audio dependencies.
- Validation after this slice: `packages/shared-core npm.cmd run typecheck`, `packages/shared-core npm.cmd run build`, `web npm.cmd run typecheck`, `web npm.cmd run build`, and `mobile npm.cmd run typecheck` passed.

- Remaining gaps: the standalone legacy `AdventureVoiceDevScreen` voice lab is not yet routed in the new apps; full parity still needs that dev surface, richer recap/character profile overlays and native mobile voice playback if we choose to add an Expo audio/speech dependency.

Adventure chests rich checkpoint: 2026-05-18

- Web/mobile collection chests now render opening slots, stored chests, claimed history, ready/opening/stored labels, countdown text and progress bars instead of one flat list.
- Shared strings expanded for chest slot labels, summary metrics, ready-to-claim and stored-for-later states in `pt-BR`, `en`, and `de-DE`.
- Chest cards now keep the detail modal/action path from the previous slice, so clicking a slot or stored chest still opens the same start/claim flow.

- Remaining gaps: timer values update when the screen rerenders; the exact legacy 1-second interval refresh and claimed reward confetti can be a focused follow-up if we want complete chest parity.

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
- Web and mobile modal/sheet components must be centralized under `*/src/components/modals/**`. Screen files hold selection state and pass data/actions into modal components; shared modal shell behavior goes through the platform modal base such as `BaseModal`.

Folder structure rule:

- `web/src` and `mobile/src` must keep the same top-level folders listed below.
- `web/src/components` and `mobile/src/components` must keep the same component category folders listed below.
- New platform code should go into an existing category. If a new category is genuinely needed, update this audit first with the ownership rule and reason.
- Avoid recreating loose root component folders such as `web/src/components/AppShell` or `mobile/src/components/AdventureTransitionButton.tsx`; use `layout`, `features`, `shared`, `modals`, `cards`, or `ui`.
- Avoid adding platform-only services under `*/src/services`; platform adapters belong in `*/src/lib`, while HTTP/domain services belong in `packages/shared-core/src/services`.

Component organization target for both `web/src/components` and `mobile/src/components`:

- `cards/`: reusable card primitives and future card families.
- `features/`: domain-specific components, grouped by feature such as `features/adventure`.
- `layout/`: app shells, boot wrappers, navigation frames and layout-only components.
- `modals/`: modal/sheet components and shared modal wrappers.
- `shared/`: small cross-screen components such as flags and avatars.
- `ui/`: low-level UI primitives.

Top-level `src/` organization target for both `web` and `mobile`:

- `components/`: organized as above.
- `config/`: platform config values and constants.
- `contexts/`: React providers/contexts owned by the platform.
- `hooks/`: platform-only hooks.
- `lib/`: platform adapters and client-side utilities such as storage/audio adapters.
- `screens/`: render-only route screens for this app.
- `setup/`: platform bootstrap/setup helpers.
- `styles/`: global styles or style entry points.
- `utils/`: platform-only helpers.

Current structure examples:

- `web/src/components/layout/AppShell/**`
- `web/src/components/layout/AppBoot/**`
- `web/src/components/shared/CharacterAvatar/**`
- `web/src/components/shared/LangFlag/**`
- `web/src/components/features/adventure/AdventureTransitionLink/**`
- `web/src/components/modals/BaseModal.tsx`
- `web/src/components/modals/AdventurePhaseModal.tsx`
- `mobile/src/components/modals/BaseModal.tsx`
- `mobile/src/components/modals/AdventurePhaseModal.tsx`
- `mobile/src/components/modals/AdventureCollectionModals.tsx`
- `mobile/src/components/modals/ProfileModals.tsx`
- `web/src/lib/audioService.ts`
- `web/src/styles/globals.css`
- `mobile/src/components/features/adventure/AdventureTransitionButton.tsx`

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
| [~] | adventure entry/map | `web/app/aventura`, `web/src/screens/AdventureMapScreen` | `mobile/app/(tabs)/adventure`, `mobile/app/adventure/map` | Entry hub plus winding map visual pass; manual QA/popup polish pending |
| [~] | adventure phase runner | `web/app/aventura/capitulo/[phaseId]` | `mobile/app/adventure/chapter/[phaseId]` | Shared runner with shared strings, web TTS/audio cues and richer completion/reward animations; voice dev lab pending |
| [~] | adventure inventory | `web/app/aventura/mochila` | `mobile/app/adventure/inventory` | Shared adventure menu/strings, dark surface, detail modal and use-item action |
| [~] | adventure characters | `web/app/aventura/personagens` | `mobile/app/adventure/characters` | Shared adventure menu/strings and modal; richer art/details pending |
| [~] | adventure words | `web/app/aventura/palavras` | `mobile/app/adventure/words` | Shared adventure menu/strings, list surface and word detail modal; filters/mastery pending |
| [~] | adventure chests | `web/app/aventura/baus` | `mobile/app/adventure/chests` | Shared adventure menu/strings, slots/timers, detail modal and start/claim actions |
| [~] | adventure hero | `web/app/aventura/heroi` | `mobile/app/adventure/hero` | Shared adventure menu/strings and metric surface; progression polish pending |
| [~] | study home | `web/app/estudo-guiado` | `mobile/app/(tabs)/study` | Better visual pass with phrase runner; full legacy guided runner/scenarios pending |
| [~] | study session | `web/src/screens/StudyScreen` | `mobile/src/screens/StudyScreen` | Shared SRS runner plus phrase runner; rich feedback/audio pending |
| [~] | vocabulary | `web/app/vocabulario` | `mobile/app/(tabs)/vocabulary` | Legacy-aligned saved phrases surface; manual QA pending |
| [~] | auth | `web/app/login` | `mobile/app/login` | Basic functional parity; visual QA pending |
| [~] | onboarding | `web/app/onboarding` | `mobile/app/onboarding` | Legacy-aligned visual pass applied; manual browser/device QA pending |
| [~] | profile/account | `web/app/perfil` | `mobile/app/(tabs)/profile` | Legacy-aligned account surface with add-area/edit-routine; edit profile/locale QA pending |
| [~] | history | `web/app/historico` | `mobile/app/history` | Legacy-aligned monthly calendar and per-area views; manual QA pending |
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
| [~] | Adventure map loader | `web/src/screens/AdventureMapScreen` | `mobile/src/screens/AdventureMapScreen` | `useAdventureChapters`, shared strings/theme | Functional plus visual pass | Manual path/touch QA and decorative divider/modal animation polish pending |
| [~] | Adventure inventory | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services, shared strings/theme | Functional plus visual pass | Detail modal and use action wired; manual QA with real items pending |
| [~] | Adventure chests | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services, shared strings/theme | Functional plus rich visual pass | Slots/timers and actions wired; 1-second live timer refresh/confetti pending |
| [~] | Adventure words | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services, shared strings/theme | Functional plus visual pass | Word detail modal wired; search/filter/rich mastery visuals still need parity |
| [~] | Adventure hero | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services, shared strings/theme | Functional plus visual pass | Achievements/powers rich layout still need parity |
| [~] | Adventure characters | `web/src/screens/AdventureCollectionScreen` | `mobile/src/screens/AdventureCollectionScreen` | shared services, shared strings/theme | Functional plus visual pass | Character images/richer details still need parity |
| [~] | Auth/login | `web/src/screens/AuthScreen` | `mobile/src/screens/AuthScreen` | shared services | Functional only | Global route guard and visual QA pending |
| [~] | Onboarding | `web/src/screens/OnboardingScreen` | `mobile/src/screens/OnboardingScreen` | shared services, shared strings/assets | Functional plus visual pass | Manual browser/device QA pending before `[x]`; full app boot flow still needs QA |
| [~] | Study home | `web/src/screens/StudyScreen` | `mobile/src/screens/StudyScreen` | shared services, shared strings | Functional plus visual pass | Full legacy scenario richness and TodayScreen flow pending |
| [~] | Vocabulary | `web/src/screens/VocabularyScreen` | `mobile/src/screens/VocabularyScreen` | shared services, shared strings | Functional plus visual pass | Manual browser/device QA with seeded favorites pending |
| [~] | Profile | `web/src/screens/ProfileScreen` | `mobile/src/screens/ProfileScreen` | shared services, shared strings/assets | Functional plus visual pass | Edit profile/locale switch surface and manual QA pending before `[x]` |
| [~] | History | `web/src/screens/HistoryScreen` | `mobile/src/screens/HistoryScreen` | shared services, shared strings/theme | Functional plus visual pass | Manual browser/device QA with seeded history pending |
| [~] | Adventure phase runner | `web/src/screens/AdventureChapterRunnerScreen` | `mobile/src/screens/AdventureChapterRunnerScreen` | `useAdventurePhaseRunner`, `useAdventureSectionRunner`, shared strings, web audio service | Functional shared runner plus rich completion/audio pass | Voice dev lab, richer recap and character modals pending |
| [~] | Study SRS/phrase runners | `web/src/screens/StudyScreen` | `mobile/src/screens/StudyScreen` | `useStudySessionRunner`, shared services | SRS runner plus phrase runner | Audio, rich feedback animations and full GuidedLessonRunner parity pending |

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
- Keep `web/src` and `mobile/src` aligned with the shared top-level folder contract.
- Keep `web/src/components` and `mobile/src/components` aligned with the shared component category contract.
- Put platform adapters in `*/src/lib`; put domain HTTP services in `packages/shared-core/src/services`.
- Put modal/sheet components in `*/src/components/modals`; screens should not keep large inline modal implementations.

## Remaining Polish Before Retiring Legacy

- Match the rich legacy animations, audio controls, character images and reward visuals in the new renderers.
- Add/profile routine flows now exist in web and mobile; profile edit remains pending.
- Route guards/boot session logic now exists in web and mobile; manual QA is still needed on device/browser.
- Run manual QA against real seeded backend data before deleting `frontend-web/`.
