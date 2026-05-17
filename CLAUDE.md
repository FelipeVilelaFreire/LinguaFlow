# LinguaFlow / Talkly - Agent Rules

This repository is being migrated to the `docs/_TEMPLATESHARED` architecture. These rules are mandatory for Claude, Codex and any automated agent.

## Current Goal

Make `web/` and `mobile/` reach full product parity with the old `frontend-web/`, then retire `frontend-web/` only after manual QA confirms parity.

`frontend-web/` is a legacy reference. Do not add new product work there unless the user explicitly asks for an emergency legacy fix.

## Canonical Docs

Read these before architecture or parity work:

- `docs/_TEMPLATESHARED/setup/CLAUDE.md`
- `docs/_TEMPLATESHARED/setup/ARCHITECTURE.md`
- `docs/_TEMPLATESHARED/setup/SHARED-CORE.md`
- `docs/_TEMPLATESHARED/setup/FRONTEND-WEB.md`
- `docs/_TEMPLATESHARED/setup/FRONTEND-MOBILE.md`
- `docs/_TEMPLATESHARED/setup/DESIGN.md`
- `docs/PARITY-AUDIT-EXECUTION.md`
- `docs/architecture/cross-platform-roadmap.md`

For story, seeds and adventure content, also read:

- `docs/content/es-a1/story.md`
- `docs/content/es-a1/characters.md`
- `docs/content/es-a1/inventory-system.md`

## Architecture Contract

```txt
backend/                source of truth, Django/DRF business rules
packages/shared-core/   single brain: types, services, hooks, strings, tokens
web/                    Next.js render-only app, CSS Modules only
mobile/                 Expo render-only app, StyleSheet only
frontend-web/           legacy reference, frozen for migration
docs/                   canonical decisions, audits and task tracking
bats/                   Windows automation only
```

## Inviolable Rules

1. Business logic goes in `packages/shared-core/src/hooks/**`.
2. API calls go through `packages/shared-core/src/services/**` and the injected `api()` client.
3. Domain types live in `packages/shared-core/src/types/**`.
4. User-facing strings live in `packages/shared-core/src/constants/strings/{pt-BR,en,de-DE}.ts`.
5. Web uses CSS Modules and CSS variables. No Tailwind in `web/`.
6. Mobile uses `StyleSheet.create` and shared-core tokens. No NativeWind or styled-components.
7. `web/` and `mobile/` components render only. Local state is allowed only for UI-only concerns such as open modal, selected tab, input draft and animation state.
8. Every shared feature must have equivalent web and mobile routes/screens, or the difference must be documented in `docs/PARITY-AUDIT-EXECUTION.md`.
9. After editing `packages/shared-core/src/**`, run `npm run build` in `packages/shared-core`.
10. Do not delete `frontend-web/` until QA proves parity across auth, onboarding, adventure, study, vocabulary, profile and history.

## Required Work Pattern

For every migration task:

1. Find the legacy behavior in `frontend-web/`.
2. Extract reusable data/state/validation to `packages/shared-core`.
3. Render it separately in `web/` and `mobile/`.
4. Add missing strings to all three locales.
5. Use shared-core tokens for visual values.
6. Update `docs/PARITY-AUDIT-EXECUTION.md`.
7. Validate:

```bat
cd packages\shared-core && npm run typecheck && npm run build
cd ..\..\web && npm run typecheck && npm run build
cd ..\mobile && npm run typecheck
```

## Current Parity Tasks

Keep this task list current as work progresses.

### Must Finish Before Retiring `frontend-web/`

- [ ] Rich adventure runner parity:
  - [ ] audio controls and global mute UI
  - [ ] NPC/character avatar and profile modal
  - [ ] scene/recap overlays
  - [ ] reward animations for words, XP, chests and items
  - [ ] gated obstacle retry behavior and 50 percent section gate
  - [ ] item moment UX matching legacy
- [ ] Adventure map polish:
  - [ ] winding/path visual parity
  - [ ] phase completion fill animation
  - [ ] day/night mode parity
  - [ ] dev jump/voice tools if still needed
- [ ] Inventory/chests/hero/characters:
  - [ ] chest start/claim interactions
  - [ ] item use interactions
  - [ ] hero powers, achievements and mastery details
  - [ ] character images and profile modal
- [ ] Study:
  - [ ] guided lesson runner parity
  - [ ] full exercise renderer parity
  - [ ] scenarios/modules rich UI parity
- [ ] Account:
  - [ ] edit profile screen
  - [ ] locale switch parity
  - [ ] add-area/edit-routine/delete-area QA on web and mobile
- [ ] Auth/onboarding:
  - [ ] full visual parity
  - [ ] route guards tested on browser and Expo
- [ ] QA:
  - [ ] seed data loads
  - [ ] all web routes open
  - [ ] all mobile routes open
  - [ ] phase 1 section 1 through completion works
  - [ ] study review works
  - [ ] profile modals work

## Content Rules

- Aventura and Estudo are separate modules but must stay pedagogically aligned.
- Every adventure item must be tied to a `word_id`; items are never generic rewards.
- Items are bonuses, never blockers.
- `item_moment` is the only step type where items are used inside phases.
- The backend/seed owns story, NPC dialogue, vocabulary and exercises. Renderers must stay generic.
- For Spanish A1 content, respect the story bible and character docs listed above.

## Automation

- One-time setup: `bats\setup.bat`
- Daily dev: `bats\dev.bat`
- Backend TTS setup remains under `backend\bats\setup_adventure_tts.bat`.

Do not create root-level random `.bat` files. Use `bats/` or `backend/bats/` only.
