# Build Instructions — Cross-Platform (mobile + web + shared-core)

> **Claude reads this file first** when the user says:
> *"Read setup/INSTRUCTIONS.md and execute"* or *"Lê o setup e constrói o projeto cross-platform"*.
>
> This template scaffolds the HobbyMap-style root: `docs/`, `bats/`, `backend/`, `packages/shared-core/` (the brain), `mobile/` (RN + Expo), `web/` (Next.js), and optional `frontend/` admin.

---

## What you must do

### Step 1 — Read all specs

Read these files in this exact order before doing anything:

1. `setup/CLAUDE.md` — the inviolable rules (11 of them, including shared-core as #1)
2. `setup/ARCHITECTURE.md` — layers, hooks, BFF, shared-core philosophy
3. `setup/SHARED-CORE.md` — **the brain** (read this carefully — it's the heart of the project)
4. `setup/BACKEND.md` — Django patterns
5. `setup/FRONTEND-WEB.md` — Next.js patterns (render-only consumer)
6. `setup/FRONTEND-MOBILE.md` — RN + Expo patterns (render-only consumer)
7. `setup/DESIGN.md` — tokens, palette, components
8. `setup/BUSINESS-MODEL.md` — business assumptions, scenarios, KPIs, validation backlog
9. `setup/PARITY-AUDIT.md` — web/mobile tree parity, render-only audit, STRINGS/tokens review
10. `setup/IDEA.md` — **the user's project brief**

### Step 2 — Parse the IDEA

From `setup/IDEA.md` extract:
- Project name (kebab-case for folders, display name for UI)
- Domain description
- Entities (with fields + relationships)
- User roles
- External integrations
- Brand color (default `#0066ff`)
- Business model notes (or "not validated yet") to seed `docs/BUSINESS-MODEL.md`
- **Mobile-specific notes** (push? deep links? offline? feature-parity?)
- **Platforms to scaffold** (default: all — backend + shared-core + mobile + web)

If any required field is missing or ambiguous, ask the user up to 3 short questions.

### Step 3 — Fill placeholders in CLAUDE.md

Replace `{{PROJECT_NAME}}`, `{{DOMAIN_DESCRIPTION}}`, `{{ENTITIES}}`, `{{USER_ROLES}}`, `{{INTEGRATIONS}}`, `{{PRIMARY_COLOR}}`, `{{MOBILE_NOTES}}`, and entity placeholders. Replace `{{project}}` with the kebab-case project name (used in `@{{project}}/shared-core` package name).

### Step 4 — Move docs into final position

```
setup/CLAUDE.md          → ./CLAUDE.md
setup/ARCHITECTURE.md    → ./docs/ARCHITECTURE.md
setup/BACKEND.md         → ./docs/BACKEND.md
setup/SHARED-CORE.md     → ./docs/SHARED-CORE.md
setup/FRONTEND-WEB.md    → ./docs/FRONTEND-WEB.md
setup/FRONTEND-MOBILE.md → ./docs/FRONTEND-MOBILE.md
setup/DESIGN.md          → ./docs/DESIGN.md
setup/BUSINESS-MODEL.md  → ./docs/BUSINESS-MODEL.md
setup/PARITY-AUDIT.md    → ./docs/PARITY-AUDIT.md
setup/PROMPTS/           → ./docs/PROMPTS/
```

Canonical root layout:

```text
{{PROJECT_NAME}}/
├── CLAUDE.md
├── docs/
├── bats/
├── backend/
├── packages/
│   └── shared-core/
├── mobile/
├── web/
└── frontend/        # only if Admin panel: yes
```

Do not put generated docs inside app folders. Do not place automation scripts at random root paths. Windows scripts must live in `bats/`, matching the HobbyMap organization.

Leave `INSTRUCTIONS.md` and `IDEA.md` in `setup/` as audit trail.

### Step 5 — Scaffold backend/

Follow `docs/BACKEND.md` (Django) exactly. Same as `_TEMPLATENEXTDJANGO`:
- `manage.py`, `requirements.txt`, `.env.example`, `.gitignore`
- `config/` with settings split
- `apps/core/`, `apps/users/`, one app per entity
- Wire URLs into `config/urls.py`

Do NOT run `pip install`, `migrate`, `createsuperuser`.

### Step 6 — Scaffold packages/shared-core/

This is the **most important package**. Follow `docs/SHARED-CORE.md` exactly.

Create:
- `packages/shared-core/package.json` with:
  - `"name": "@{{project}}/shared-core"`
  - Build via `tsup`: `"build": "tsup src/index.ts --format esm,cjs --dts --clean"`
  - Watch via `"dev": "tsup src/index.ts --format esm,cjs --dts --watch"`
  - Peer deps: `react`, `react-dom` (let consumers provide)
- `packages/shared-core/tsconfig.json` (strict mode, target ES2020, declaration: true)
- `packages/shared-core/src/`:
  - `types/{shared, user, {{entity1}}, {{entity2}}}/index.ts`
  - `services/{api.ts, authService.ts, {{entity}}Service.ts}` — services use injected `api()` client, never raw fetch
  - `hooks/{auth, shared, {{entity}}}/use*.ts` — full screen/form/data hooks
  - `constants/{strings/{pt-BR.ts, en.ts, de-DE.ts, types.ts, index.ts}, icons.ts, routes.ts}`
  - `theme/{spacing.ts, colors.ts, radius.ts, fontSize.ts, fontFamily.ts, shadows.ts, index.ts}`
  - `utils/{format.ts, errors.ts, mappers/{{entity}}/, validation/{{entity}}/}`
  - `lib/{storage.ts (adapter interface), apiClient.ts (interface)}`
  - `index.ts` — public exports
- `packages/shared-core/.gitignore` (`dist/`, `node_modules/`)

Do NOT run `yarn build` or `npm install`.

### Step 7 — Scaffold mobile/ (skip if "skip mobile" in IDEA)

Follow `docs/FRONTEND-MOBILE.md` exactly.

Create:
- `mobile/package.json` with:
  - `"expo": "~52.0.0"`, `"react-native": "0.76.x"`, `"react": "19.x"`, `"typescript": "^5"`
  - `"expo-router": "^4"`, `"@react-native-async-storage/async-storage"`, `"react-native-reanimated": "^3"`
  - `"@fortawesome/react-native-fontawesome"`, `"@fortawesome/fontawesome-svg-core": "^7"`, `"@fortawesome/free-solid-svg-icons": "^7"`
  - `"axios": "^1.7"`, `"@gorhom/bottom-sheet": "^5"`
  - `"@{{project}}/shared-core": "file:../packages/shared-core"`
  - Scripts: `"start": "expo start"`, `"ios": "expo start --ios"`, `"android": "expo start --android"`
- `mobile/app.json` (Expo config: name, slug, scheme, splash, icon)
- `mobile/babel.config.js` (with `react-native-reanimated/plugin`)
- `mobile/tsconfig.json` (extending `expo/tsconfig.base`)
- `mobile/app/`:
  - `_layout.tsx` — root, sets shared-core adapters (storage + API client) at boot via `useEffect`
  - `(auth)/_layout.tsx`, `(auth)/login.tsx`, `(auth)/register.tsx`
  - `(tabs)/_layout.tsx` — tab bar
  - `(tabs)/home.tsx`, `(tabs)/profile.tsx`
  - `{{entity}}/[id].tsx` per entity
- `mobile/src/`:
  - `components/{ui, shared, features, cards}/` — all RN, with `*.styles.ts` separate
  - `screens/` — fetch + skeleton + delegate to feature
  - `hooks/{domain}/use*.ts` — **5-line wrappers** that import shared-core hooks and inject router/Alert
  - `lib/{apiClient.ts, storageAdapter.ts, iconMapper.ts}`

Do NOT run `npm install` or `expo start`.

### Step 8 — Scaffold web/ (skip if "skip web" in IDEA)

Follow `docs/FRONTEND-WEB.md` exactly. Same as `_TEMPLATENEXTDJANGO`'s frontend section, but:
- Replace `web/src/types/`, `web/src/hooks/`, `web/src/services/`, `web/src/constants/`, `web/src/lib/{storage,errors}.ts` with **wrappers** that import from `@{{project}}/shared-core`
- `web/src/theme/globals.css` mirrors the values in `packages/shared-core/src/theme/*` as CSS Variables (manual sync — both must match)
- `web/src/hooks/{domain}/use*.ts` — **5-line wrappers** that import shared-core hooks and inject `useRouter()` from `next/navigation`

Do NOT run `npm install` or `npm run dev`.

### Step 8.4 — Scaffold frontend/ (admin) — ONLY if `Admin panel: yes` in IDEA.md

Skip entirely if `no`. Follow `docs/ADMIN.md` exactly.

Create `frontend/` as a **fourth package** (alongside `backend/`, `packages/shared-core/`, `mobile/`, `web/`):

- `frontend/package.json` (Vite 6, React 19, react-router-dom 7, axios, FontAwesome 7)
- `frontend/vite.config.js`, `.env.example` (`VITE_API_URL`)
- `frontend/src/{main, App, ErrorBoundary}.jsx`
- `frontend/src/services/api.js` — axios + JWT (same JWT as web/mobile)
- `frontend/src/admin/AdminApp.jsx` — routes + role guard (role=admin)
- `frontend/src/admin/styles/{variables, globals, reset}.css` — `--admin-*` tokens (see ADMIN.md)
- `frontend/src/admin/ini/config/endpoints.js`
- `frontend/src/admin/shared/{layout, components, hooks, contexts}/`
- `frontend/src/admin/apps/{auth, dashboard, business-plan, {{entity_per_idea}}, trash, history, profile}/`

**Important — admin uses shared-core for STRINGS/i18n.** The admin is a separate audience (internal team) and can keep admin-specific logic local when it is only operator tooling, but visible UI text still comes from `@{{project}}/shared-core` as `STRINGS.admin.*` in `pt-BR`, `en`, and `de-DE` together. Do not hardcode labels in admin JSX, config, constants, table columns, filters, placeholders, toasts, modals, aria labels, empty states, or errors.

Backend additions when admin=yes:
- `backend/apps/admin_api/` with ViewSets gated by `permissions.IsAdminUser`
- `/api/admin/trash/`, `/api/admin/audit/`, `/api/admin/stats/`

Do NOT run `npm install` in `frontend/`.

### Step 8.5 — Scaffold Windows automation scripts

Create `bats/` at the project root and copy `setup/SCRIPTS/setup.bat`, `setup/SCRIPTS/dev.bat`, and `setup/SCRIPTS/README.md` into `bats/`. Replace placeholders:

- `{{DISPLAY_NAME}}` → IDEA.md "Display name"
- `{{CONDA_ENV}}` → IDEA.md "Conda env name" (default: kebab-case project name)
- `{{DB_NAME}}` → IDEA.md "Database name"

Final filenames:
- `bats/setup.bat` — one-time install (Conda env + deps + DB + shared-core build + web/mobile/admin deps + opens WT)
- `bats/dev.bat` — daily startup (opens WT with Claude, backend, shared-core watch, web, mobile, and optional admin)
- `bats/README.md` — documents the local automation flow

These scripts orchestrate **5 things**:
- Conda env + Django backend (install + migrate + createsuperuser)
- shared-core (yarn install + yarn build)
- web (npm install)
- mobile (npm install)
- Opens 3 WT tabs: Claude · backend+shared-core(watch) · web+mobile

If IDEA.md says "skip mobile" or "skip web", remove the corresponding split-pane line from both setup.bat and dev.bat, AND the corresponding `npm install` block in setup.bat.

If `Admin panel: yes` in IDEA.md, also add a 4th tab to both scripts:
```
; new-tab --title "admin" -d "%PROJECT_PATH%\frontend" cmd /k "npm run dev"
```
And in setup.bat, append a `cd /d "%PROJECT_PATH%\frontend" && npm install` block.

Tell the user in the final report: "Run `bats\setup.bat` once; run `bats\dev.bat` every day."

### Step 9 — Verify rule compliance

Before finishing, mentally scan the generated code:
- No business logic outside `packages/shared-core/src/hooks/`?
- Mobile and web hook wrappers are ~5 lines each?
- No types duplicated between mobile/, web/, shared-core/?
- Web uses CSS Modules + CSS Variables (no Tailwind, no styled-components)?
- Mobile uses StyleSheet + shared-core tokens (no styled-components, no NativeWind)?
- All visual values come from shared-core tokens (or CSS Variables that mirror them on web)?
- All text via `STRINGS` from shared-core?
- New strings exist in `pt-BR.ts`, `en.ts`, and `de-DE.ts` together?
- Shared features keep the same conceptual tree in `web/` and `mobile/`, or document differences in `docs/PARITY-AUDIT-EXECUTION.md`?
- Web's `globals.css` values **exactly match** `packages/shared-core/src/theme/*`?
- `packages/shared-core/src/index.ts` exports everything mobile and web need?
- Both platforms register adapters (storage, API client) at boot?
- `docs/BUSINESS-MODEL.md` exists and has pessimistic, realistic, and optimistic scenarios?

If any violation: fix it before reporting done.

### Step 10 — Final report

End with:
- **Total files created** (number)
- **Folder tree** (`docs/`, `bats/`, `backend/`, `packages/shared-core/`, `mobile/`, `web/`, and `frontend/` if admin exists — first 3 levels)
- **Critical reminder**: `yarn build` in `packages/shared-core/` is required after every change to shared-core (or run `yarn dev` for watch mode during development)
- **Next 5 commands to run** to bring everything up:

  ```
  1. cd backend && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && cp .env.example .env
  2. createdb {{project_db}} && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver
  3. cd ../packages/shared-core && yarn install && yarn build
  4. cd ../../web && npm install && cp .env.example .env.local && npm run dev
  5. cd ../mobile && npm install && cp .env.example .env && npx expo start
  ```

  (skip 4 if web is skipped, skip 5 if mobile is skipped)

- **Optional sanity check** — anything in IDEA.md you had to assume

---

## What you must NOT do

- Add features, fields, endpoints, or screens not requested in `IDEA.md`
- Run any state-changing command (`pip install`, `npm install`, `yarn install`, `migrate`, `createsuperuser`, `expo start`, `npm run dev`, `git init`, `git commit`)
- Use Tailwind on web · use styled-components or NativeWind on mobile
- Hardcode any text in JSX (must come from `STRINGS` in shared-core)
- Hardcode any visual value in components (must come from shared-core tokens or CSS Variables that mirror them)
- Skip the `index.ts` barrel export in any component folder
- Put fetch logic inside a component, screen, or platform-specific hook (only shared-core services + hooks fetch)
- Duplicate a type, service, or hook between mobile/, web/, and shared-core/ — it must live in shared-core only
- Trust the client — every business rule must be enforced in Django
- Forget to mirror `globals.css` on web with shared-core token values

---

## When the user asks "Read setup and build"

Your first message must be a short plan, not silent execution:

```
Plan:
1. Read 10 spec files in setup/
2. Extract project + mobile config from IDEA.md
3. [Ask N clarifying questions if needed]
4. Scaffold backend/, packages/shared-core/, web/, mobile/ (in this order)
5. Report files + 5 startup commands

Starting now.
```

Then execute. Brief checkpoints between major scaffolds.
