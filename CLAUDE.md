# LinguaFlow / Talkly - Agent Rules

This repository follows the local architecture documented in `AGENTS.md`, this file and `docs/architecture/**`. These rules are mandatory for Claude, Codex and any automated agent.

## Current Goal

Make `web/` and `mobile/` reach full product parity with the old `frontend-web/`, then retire `frontend-web/` only after manual QA confirms parity.

`frontend-web/` is a legacy reference. Do not add new product work there unless the user explicitly asks for an emergency legacy fix.

## Canonical Docs

Read these before architecture or parity work:

- `AGENTS.md`
- `docs/architecture/backend.md`
- `docs/architecture/frontend-web.md`
- `docs/architecture/frontend-admin.md`
- `docs/architecture/admin.md`
- `docs/architecture/cross-platform-roadmap.md`
- `docs/design/design-system.md`
- `docs/PARITY-AUDIT-EXECUTION.md`
- `docs/BUSINESS-MODEL.md`

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
admin/                  separate Vite React admin, config-driven, CSS variables only
frontend-web/           legacy reference, frozen for migration
docs/                   canonical decisions, audits and task tracking
bats/                   Windows automation only
```

## Four Principles

These are the highest-priority rules in the repo:

```txt
backend     = SOURCE OF TRUTH
shared-core = BRAIN
web/mobile  = RENDER ONLY
admin       = CONFIG DRIVEN
```

Meaning:

- `backend/` owns business rules, authorization, validation, persistence, seeds, content truth, rewards and progress integrity.
- `packages/shared-core/` owns hooks, services, domain types, strings, tokens, validation helpers, mappers and cross-platform state machines.
- `web/` and `mobile/` own platform rendering, styles, routing adapters, native/browser UX and local UI-only state.
- `admin/` owns admin render/config and operational dashboards, separated from the learner-facing app.

## BFF / Trust Boundary

The frontend is a dumb pipe with smart UX. It may improve ergonomics, but it cannot decide what is true.

- Django is trusted and authoritative.
- Browser/mobile clients are untrusted.
- Next.js server actions or API routes may act as a thin BFF only when they compose Django calls, attach session/cookies, adapt response shape or cache server-side.
- BFF code must never own rules for authorization, payment, progress, rewards, content integrity, SRS, item use, phase completion or admin permissions.
- If a rule appears in the UI, Django must also enforce it.

## Render-Only Contract

Routes and screens render what shared-core/backend provide.

- `web/app/**` route files should be thin wrappers.
- `web/src/screens/**` and `mobile/src/screens/**` may handle loading/error shell and platform UI, but not domain decisions.
- `web/src/components/**` and `mobile/src/components/**` receive props/view models and render.
- Cross-platform behavior goes in `packages/shared-core/src/hooks/**`.
- Network calls go through `packages/shared-core/src/services/**` and the injected API client.
- Platform wrappers may inject router, toast, Alert, animation triggers or local modal state.

## Inviolable Rules

1. Business logic goes in `packages/shared-core/src/hooks/**`.
2. API calls go through `packages/shared-core/src/services/**` and the injected `api()` client.
3. Domain types live in `packages/shared-core/src/types/**`.
4. Backend owns rules that protect data integrity, authorization, money, progress, rewards, content or admin access.
5. BFF/API-route logic must stay thin and cannot replace Django rules.
6. User-facing strings live in `packages/shared-core/src/constants/strings/{pt-BR,en,de-DE}.ts`.
7. No visible text may be hardcoded in JSX, configs, constants, placeholders, aria labels, errors, empty states, buttons, tables, modals or CSS pseudo-content.
8. Every new string key must be added to `pt-BR`, `en`, and `de-DE` before use.
9. Web uses CSS Modules and CSS variables. No Tailwind in `web/`.
10. Mobile uses `StyleSheet.create` and shared-core tokens. No NativeWind or styled-components.
11. Admin belongs in `admin/`, never inside learner-facing `web/`.
12. Admin uses config-driven apps under `admin/src/admin/apps/**`, labels from `STRINGS.admin.*`, and `--admin-*` CSS variables. No Tailwind in `admin/`.
13. `web/` and `mobile/` components render only. Local state is allowed only for UI-only concerns such as open modal, selected tab, input draft and animation state.
14. Every shared feature must have equivalent web and mobile routes/screens, or the difference must be documented in `docs/PARITY-AUDIT-EXECUTION.md`.
15. After editing `packages/shared-core/src/**`, run `npm run build` in `packages/shared-core`.
16. Do not delete `frontend-web/` until QA proves parity across auth, onboarding, adventure, study, vocabulary, profile and history.

## String Contract

Visible copy is product surface and must be centralized.

Namespaces:

| Surface | Namespace |
|---|---|
| App shell/common actions | `STRINGS.app`, `STRINGS.actions`, `STRINGS.nav` |
| Auth/onboarding/profile/study/vocabulary | matching feature namespace |
| Adventure | `STRINGS.adventure.*` |
| Admin | `STRINGS.admin.*` |

Rules:

- Import strings from `@linguaflow/shared-core`.
- Admin config files must store `STRINGS.admin.*` references, not literal labels.
- Do not create local translation maps inside components.
- Do not add strings to only one locale.
- When a missing label is discovered, add the key to all locale files first, rebuild shared-core, then use it.

## Required Work Pattern

For every migration task:

1. Find the legacy behavior in `frontend-web/`.
2. Decide the owner: backend rule, shared-core brain, platform render, admin config or docs.
3. Put reusable data/state/validation/flow logic in `packages/shared-core`.
4. Render it separately in `web/` and `mobile`.
5. Add missing strings to all three locales.
6. Use shared-core tokens for visual values.
7. Update `docs/PARITY-AUDIT-EXECUTION.md`.
8. Validate:

```bat
cd packages\shared-core && npm run typecheck && npm run build
cd ..\..\web && npm run typecheck && npm run build
cd ..\mobile && npm run typecheck
cd ..\admin && npm run build
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
- [ ] Admin:
  - [x] rename `frontend-admin/` to `admin/`
  - [x] remove Tailwind from admin
  - [x] add config-driven admin apps
  - [x] add `business-plan` app scaffold
  - [ ] add full CRUD/form builder per entity
  - [ ] add trash/history apps once backend endpoints exist

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
- Backend setup/seeds: `bats\backend\setup.bat`
- Backend migrations: `bats\backend\migrations.bat`
- Backend TTS setup: `bats\backend\tts.bat`.

Do not create root-level random `.bat` files. Use `bats/` only; backend-specific automation belongs in `bats/backend/`.
