# Cross-Platform Starter Template (Mobile + Web + Shared-Core + Django)

> Drop a `setup/` folder into an empty project, write your idea in `IDEA.md`, and tell Claude:
> *"Read setup/INSTRUCTIONS.md and execute."*
>
> Out comes a working cross-platform app: React Native (Expo) + Next.js + Django, all sharing a single TypeScript brain (`packages/shared-core/`).

---

## When to use this template

Use `_TEMPLATESHARED` when:
- The product needs **both mobile and web**, and you want feature parity without duplicating code
- You want a single source of truth for types, hooks, services, strings, and design tokens
- You're willing to pay the complexity tax of monorepo + shared package builds

For **web-only** projects, use `_TEMPLATENEXTDJANGO` (5× simpler).
For **flexible backend** (FastAPI / NestJS), use `_TEMPLATEALL`.

---

## The architecture

```
┌──────────────────────────────────────────┐
│         backend/ (Django + DRF)          │
│         Source of truth                  │
└──────────────────────────────────────────┘
                  ↑↓
         ┌────────────────────┐
         │ shared-core/       │  ← types, hooks, services,
         │ THE BRAIN          │     constants, theme, validation
         └────────────────────┘
                  ↑↓
       ┌──────────────────────┐
       ↓                      ↓
┌──────────────┐    ┌──────────────────┐
│   mobile/    │    │      web/        │
│  RN + Expo   │    │  Next.js + CSS   │
│  RENDER ONLY │    │  RENDER ONLY     │
└──────────────┘    └──────────────────┘
```

Mobile and web are **dumb renderers**. All logic lives in `shared-core/`. A `useOrderScreen` hook is written once; both platforms wrap it in 5 lines to inject `router.back()` / `Alert.alert` etc.

This is the architecture HobbyMap uses today.

---

## What this template contains

```
setup/
├── INSTRUCTIONS.md          ← Claude reads first (scaffolds 4 packages)
├── IDEA.md                  ← YOU fill, includes mobile-specific fields
├── CLAUDE.md                ← 11 inviolable rules (shared-core is #1)
├── ARCHITECTURE.md          ← BFF + 3 layers + shared-core principle
├── BACKEND.md               ← Django 5 + DRF + PostgreSQL
├── SHARED-CORE.md           ← THE BRAIN spec (most important file)
├── FRONTEND-WEB.md          ← Next.js render-only consumer
├── FRONTEND-MOBILE.md       ← React Native + Expo render-only consumer
├── DESIGN.md                ← Cross-platform tokens, Calm/Notion-flat
├── BUSINESS-MODEL.md        ← Assumptions, scenarios, KPIs, validation backlog
├── PARITY-AUDIT.md          ← Web/mobile tree, render-only, STRINGS, token audit
├── ADMIN.md                 ← Config-driven admin, tabs, cards, business-plan app
└── PROMPTS/
    ├── bootstrap.md
    ├── new-feature.md
    └── new-screen.md
```

After Claude finishes:
- `CLAUDE.md` moves to project root
- All spec MDs move to `docs/`
- Windows automation scripts move to `bats/`
- `INSTRUCTIONS.md` + `IDEA.md` stay in `setup/` as audit trail
- Project tree created: `docs/` · `bats/` · `backend/` · `packages/shared-core/` · `mobile/` · `web/` · optional `frontend/`
- `STRINGS` are created in `pt-BR`, `en`, and `de-DE`
- shared features can be audited with `docs/PARITY-AUDIT.md`
- business assumptions live in `docs/BUSINESS-MODEL.md`

---

## How to use

### Step 1 — Create the new project folder

```powershell
cd C:\Users\felip_x6n9d9e\OneDrive\Documentos\FELIPE\PROGRAMAÇÃO
mkdir NovoProjeto
cd NovoProjeto
```

### Step 2 — Copy the `setup/` folder

```powershell
cp -r ..\HobbyMap\docs\_TEMPLATESHARED\setup .
```

### Step 3 — Fill `setup/IDEA.md`

Open `setup/IDEA.md` and write:
- Project name + display name
- One paragraph: what the app does
- Entities (fields, relationships)
- User roles
- External integrations
- Brand color (hex)
- **Mobile-specific notes** (push? deep links? feature parity with web?)
- **Platforms to scaffold** (default: all four)

### Step 4 — Trigger the build

```powershell
claude
```

Then type:

```
Read setup/INSTRUCTIONS.md and execute.
```

Claude:
1. Reads all 8 spec files
2. Parses IDEA.md, asks 1-3 clarifying questions if needed
3. Scaffolds the canonical root tree in this order: `docs/` + `bats/` + `backend/` → `packages/shared-core/` → `web/` → `mobile/` → optional `frontend/`
4. Reports 5 startup commands

### Step 5 — Run the startup commands

```powershell
# 1. Backend
cd backend && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && cp .env.example .env
createdb novo_projeto && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver

# 2. Shared-core (in another shell, BEFORE mobile/web)
cd ..\packages\shared-core
yarn install && yarn build           # or `yarn dev` for watch mode

# 3. Web (in another shell)
cd ..\..\web && npm install && cp .env.example .env.local && npm run dev

# 4. Mobile (in another shell)
cd ..\mobile && npm install && cp .env.example .env && npx expo start
```

**Critical:** `yarn build` (or `yarn dev`) in `packages/shared-core/` must run **before** mobile or web can resolve `@{{project}}/shared-core`.

### Or use the bat scripts (Windows + Conda workflow)

Claude scaffolds two `.bat` files inside `bats/`:

```powershell
.\bats\setup.bat   # one-time: Conda + deps + DB + shared-core build + superuser + opens 3 WT tabs
.\bats\dev.bat     # daily: opens 3 WT tabs (Claude · backend+shared-core watch · web+mobile)
```

`bats/dev.bat` orchestrates everything cross-platform:
- **Tab 1**: Claude
- **Tab 2**: Django runserver (top) + `yarn dev` shared-core watch (bottom)
- **Tab 3**: Next.js dev (top) + Expo dev (bottom)

The shared-core watch mode rebuilds `dist/` on every change, so mobile and web pick up the new logic without you re-running anything.

---

## After the build — iterating

Same prompts as the other templates:

| Goal | File |
|------|------|
| Add a feature reused across 2+ routes | `docs/PROMPTS/new-feature.md` |
| Add a screen with fetch + skeleton + UI | `docs/PROMPTS/new-screen.md` |

But the workflow is different: **always edit shared-core first** (types, services, hooks), then update each platform's wrapper. Run `yarn build` in shared-core after every change.

---

## The 11 inviolable rules (from CLAUDE.md)

1. **Shared-core is the single brain** — all logic, types, services, tokens, strings
2. **Backend is source of truth** — every UI rule re-validated in Django
3. **Logic = hook in shared-core**
4. **Components = render-only** (mobile and web)
5. **Types centralized in shared-core**
6. **Services use injected API client** — no raw fetch
7. **Web: no Tailwind. Mobile: no styled-components.**
8. **Never hardcode values** — use shared-core tokens
9. **One folder per component** (both platforms)
10. **Never hardcode text** — `STRINGS` from shared-core, type-checked
11. **Mobile-first responsive on web · native-first on mobile**

---

## Trade-offs you're accepting

| Pain point | Why it's worth it |
|------------|-------------------|
| Monorepo setup + shared-core builds | Single source of truth = no drift between platforms |
| `yarn build` after every shared-core change | Catches breaking changes immediately; production-ready dist |
| Web token sync (CSS Variables ↔ shared-core/theme) | Web needs CSS strings, mobile needs JS values — manual sync once is cheaper than runtime translation |
| Mobile setup (Expo, EAS, native deps) | You get a real native app, not a wrapped WebView |
| 5-line wrappers everywhere | Tiny boilerplate that pays for itself the first time you change a hook signature once and have both platforms update |

If any of those costs feel too high for the project, use `_TEMPLATENEXTDJANGO` instead.

---

## Fixed stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 5 + DRF + PostgreSQL + SimpleJWT |
| Shared-core | TypeScript 5 + tsup (build) |
| Web | Next.js 16 (App Router, Turbopack) + React 19 + CSS Modules |
| Mobile | React Native 0.76 + Expo SDK 52 + Expo Router |
| Auth | JWT (axios + refresh interceptor on both platforms) |
| Storage | localStorage (web) ↔ AsyncStorage (mobile), abstracted in shared-core |
| Icons | FontAwesome 7 (`@fortawesome/free-solid-svg-icons` v7.1) |
| i18n | TS files (`pt-BR.ts` + `en.ts`) in shared-core, type-checked |

Need a different stack? Fork the template — don't generalize it.
