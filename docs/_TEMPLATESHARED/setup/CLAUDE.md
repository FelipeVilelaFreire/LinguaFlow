# {{PROJECT_NAME}} — Claude Code Rules

> {{DOMAIN_DESCRIPTION}}
>
> Stack: Django 5 + DRF + PostgreSQL 17 · Next.js 16.1 (App Router, Turbopack) + React 19 (web) · React Native 0.76 + Expo SDK 52 (mobile) · TypeScript 5 · `@{{project}}/shared-core` (single brain) · CSS Modules (web) · StyleSheet (mobile) · FontAwesome 7 · i18n PT/EN/DE.
>
> This is a **cross-platform** project. Mobile and web both consume `packages/shared-core/` for all logic.

---

## ⚡ THE FIVE PRINCIPLES

```
backend     = SOURCE OF TRUTH   →  business rules, integrity, authorization in Django
shared-core = SINGLE BRAIN      →  types · hooks · services · constants · theme · validation · strings
mobile      = RENDER ONLY       →  React Native JSX. Zero logic.
web         = RENDER ONLY       →  Next.js JSX. Zero logic.
backend ↔ shared-core           →  any rule on the client must also exist server-side.
```

> **Logic in mobile/ or web/ that is not pure render → move to `packages/shared-core/`.**
> **Type/service/hook duplicated between mobile and web → STOP. Consolidate in shared-core.**

---

## 🔴 11 INVIOLABLE RULES

### 1 · SHARED-CORE IS THE SINGLE BRAIN

`packages/shared-core/` owns: types · hooks (with all business logic) · services (HTTP) · constants (STRINGS, ICONS, ROUTES) · theme tokens (SPACING, COLORS, etc.) · validation · mappers.

Mobile and web are **render-only** consumers. If you write the same hook in both `mobile/src/hooks/` and `web/src/hooks/`, that's a bug — extract it to shared-core.

Allowed in `mobile/src/hooks/` or `web/src/hooks/`: **only thin wrappers** that inject platform-specific dependencies (router, Alert.alert vs window.alert, animations) into a shared-core hook via `onSuccess` / `onError` callbacks.

For shared features, web and mobile should keep the same conceptual tree. If `web/src/components/features/{{Entity}}Detail/` exists, the mobile equivalent should exist with the same feature responsibility, unless `docs/PARITY-AUDIT-EXECUTION.md` records a platform-specific reason.

### 2 · BACKEND IS THE SOURCE OF TRUTH (BFF philosophy)

The frontend can compute, validate, and transform — but only for UX. Every business rule is **also enforced in Django**. The client cannot be trusted, regardless of platform.

| Allowed in shared-core | Required in Django |
|------------------------|--------------------|
| Form validation (instant feedback) | Same validation, stricter, in serializer |
| Permission-based UI hiding | Permission check on the ViewSet |
| Optimistic updates | Real authorization on every endpoint |
| Display transformation (format dates, sums) | Source data, untouched |

### 3 · LOGIC = HOOK IN SHARED-CORE. ALWAYS.

All business logic lives in `packages/shared-core/src/hooks/{domain}/`. Mobile and web call those hooks via thin wrappers. Zero `useState` for data, zero `useEffect` for fetching, zero validation in either platform's components.

### 4 · COMPONENTS = RENDER ONLY (mobile + web)

Zero `useState` for forms in components. Zero `handleSave`. Zero `toCreateData`. Zero validation. Components receive data and callbacks as props from the screen, which calls the hook wrapper.

Allowed locally: `useState` for pure UI (modal open, active tab) · animations · router calls · error feedback.

### 5 · TYPES = CENTRALIZED IN SHARED-CORE

Entity, payload, business enum → `packages/shared-core/src/types/{domain}/index.ts`. Never recreate in `mobile/` or `web/`.

**Allowed locally per platform:** `XxxProps` · UI state · `UseXxxReturn` / `UseXxxOptions` · display DTOs (e.g. `MobileXxxCardProps`).

### 6 · SERVICES = NO RAW FETCH. EVER.

```typescript
// shared-core
await {{entity}}Service.list()      // ✅
fetch('/api/{{entity}}/')           // ❌ NEVER
```

The service uses `api()` from shared-core, which receives a platform-injected client at boot (axios for both, but with platform-specific token reading).

### 7 · NEVER TAILWIND ON WEB. NEVER STYLED-COMPONENTS ON MOBILE.

- Web: CSS Modules + CSS Variables. **No Tailwind, no styled-components, no CSS-in-JS.**
- Mobile: `StyleSheet.create` + tokens from shared-core. **No styled-components, no NativeWind.**

### 8 · NEVER HARDCODE VALUES. USE SHARED-CORE TOKENS.

Mobile reads `SPACING`, `COLORS`, `RADIUS`, `FONT_SIZE`, `FONT_FAMILY` directly from shared-core.
Web mirrors the same values as CSS Variables in `web/src/theme/globals.css` (kept in sync manually — DO NOT diverge).

```typescript
// Mobile ✅
import { SPACING, COLORS } from '@{{project}}/shared-core';
const styles = StyleSheet.create({ card: { padding: SPACING.lg, backgroundColor: COLORS.white } });

// Mobile ❌
const styles = StyleSheet.create({ card: { padding: 16, backgroundColor: '#fff' } });
```

```css
/* Web ✅ */ padding: var(--spacing-lg); color: var(--color-white);
/* Web ❌ */ padding: 16px; color: #fff;
```

AI enforcement:
- raw hex/rgb/hsl/px values are allowed only in token declaration files;
- web CSS must use `var(--color-*)`, `var(--spacing-*)`, `var(--radius-*)`, `var(--font-*)`, and `var(--shadow-*)`;
- mobile styles must use shared-core tokens (`COLORS`, `SPACING`, `RADIUS`, `FONT_*`);
- admin CSS must use `var(--admin-*)`;
- never use token fallbacks like `var(--color-surface, #fff)` in component CSS;
- if a token is missing, add it to `packages/shared-core/src/theme/*`, mirror it in `web/src/theme/globals.css`, rebuild `dist/`, then use it;
- before finishing visual work, search changed files for `#`, `rgb`, `rgba`, `hsl`, `px`, `white`, and `black`.

### 9 · ONE FOLDER PER COMPONENT (both platforms)

```
ComponentName/
├── ComponentName.tsx                # component
├── ComponentName.module.css         # web only
├── ComponentName.styles.ts          # mobile only (StyleSheet.create separated)
├── ComponentName.types.ts           # if > 5 interfaces
└── index.ts                         # mandatory barrel export
```

Inline `style={{...}}` (web) or `style={{...}}` (RN) is allowed only for **runtime-computed** values.

### 10 · NEVER HARDCODE USER-FACING TEXT

All UI text comes from `STRINGS` in `packages/shared-core/src/constants/strings/`. Never literal strings in JSX (mobile or web).

```typescript
import { STRINGS } from '@{{project}}/shared-core';
<Text>{STRINGS.{{entity}}.title}</Text>          // mobile
<h1>{STRINGS.{{entity}}.title}</h1>              // web
```

**Protocol when adding a new string:**
1. Add to `pt-BR.ts`, `en.ts`, and `de-DE.ts` in shared-core (same change)
2. Run `yarn build` in `packages/shared-core/`
3. Both platforms pick up the new strings automatically

### 11 · MOBILE-FIRST ON WEB. NATIVE-FIRST ON MOBILE.

Web defaults target mobile (≤768px). Desktop styles use `@media (min-width: 769px)`.

```css
/* Web ✅ Mobile-first */
.card { padding: var(--spacing-lg); flex-direction: column; }
@media (min-width: 769px) { .card { padding: var(--spacing-2xl); flex-direction: row; } }
```

Mobile uses `Dimensions` or `useWindowDimensions` only when truly needed — most layouts are already vertical-first.

| Aspect | Web Mobile (≤768px) | Web Desktop (≥769px) | Native Mobile |
|--------|---------------------|----------------------|---------------|
| Modals | `<BottomModal>` | `<Modal>` centered | `<BottomSheetModal>` (Gorhom) |
| Layout | Single column | Multi-column grid | Single column |
| Buttons | Full-width | Auto-width | Full-width default |
| Tabs/filters | Horizontal scroll | Inline row | Horizontal scroll |

---

## 🚨 AUTOMATIC DIAGNOSTIC

**If a `.tsx` (web or mobile) has any of these → move to a hook in shared-core:**
```
useState for data or form  |  useEffect for fetching  |  handleSave / handleDelete
isValid / errors / validation  |  toCreateData         |  raw fetch() or axios
```

**If the same hook exists in both `mobile/src/hooks/` and `web/src/hooks/`:**
```
That's duplication. Extract to packages/shared-core/src/hooks/{domain}/.
Keep only the thin wrapper (5 lines) in each platform.
```

---

## 🧭 BEFORE CREATING

### TYPE
```
Domain type (entity, payload, business enum)?
  ├── YES → Already in packages/shared-core/src/types/?
  │          ├── YES → Import from '@{{project}}/shared-core'. Never recreate.
  │          └── NO  → Add to shared-core/types/{domain}/index.ts
  │                    Run yarn build in packages/shared-core/
  └── NO  → Props, UI state, hook contract? → Stays local to platform.
```

### HOOK
```
Already in shared-core/hooks/?
  ├── YES → Import + (if needed) wrap in mobile/ or web/ for router/Alert.
  └── NO  → Is it business logic / data / form?
             ├── YES → Create in shared-core/hooks/{domain}/use{{Entity}}Xxx.ts
             │         Then create thin wrappers in mobile/ and web/ if router needed.
             └── NO  → Pure platform concern (router, animation, Alert)?
                       → Stays in the platform layer.
```

### COMPONENT
```
Has business logic? → STOP. Extract to a shared-core hook first.
Used in 1 route → self-contained inside the route file.
Used in 2+ routes → src/components/features/FeatureName/.

Is the component identical in mobile and web?
  → No, never. RN primitives differ from HTML. Each platform owns its own components.
  → They share data, types, hooks, strings, tokens — NOT JSX.
```

### USER-FACING TEXT
```
Already in STRINGS?
  ├── YES → Use STRINGS.{domain}.{key}
  └── NO  → Add to shared-core/constants/strings/pt-BR.ts, en.ts, and de-DE.ts
            Run yarn build in packages/shared-core/
```

---

## 🏗️ CODE TEMPLATES

### Page → Screen → Feature (per platform)

| Layer | Web (`web/`) | Mobile (`mobile/`) |
|-------|-------------|--------------------|
| Route | `app/route/page.tsx` | `app/route.tsx` |
| Screen | `src/screens/XxxScreen/` | `src/screens/XxxScreen/` |
| Feature | `src/components/features/XxxDetail/` | `src/components/features/XxxDetail/` |
| Hook | thin wrapper → `@{{project}}/shared-core` | thin wrapper → `@{{project}}/shared-core` |

### Hook in shared-core

```typescript
// packages/shared-core/src/hooks/{domain}/use{{Entity}}Screen.ts
export interface Use{{Entity}}ScreenOptions {
  id: number;
  onSuccess?: () => void;       // platform injects router.back() etc.
  onError?: (msg: string) => void;
}
export interface Use{{Entity}}ScreenReturn {
  data: {{Entity}} | null;
  loading: boolean;
  error: string | null;
  isSaving: boolean;
  handleSave: (data: {{Entity}}UpdateData) => Promise<void>;
  handleDelete: () => Promise<void>;
  refresh: () => Promise<void>;
}
```

### Wrapper per platform (mobile)

```typescript
// mobile/src/hooks/{{entity}}/use{{Entity}}Screen.ts
import { use{{Entity}}Screen as useCore } from '@{{project}}/shared-core';
import { router } from 'expo-router';
import { Alert } from 'react-native';

export function use{{Entity}}Screen(id: number) {
  return useCore({
    id,
    onSuccess: () => router.back(),
    onError: (msg) => Alert.alert('Erro', msg),
  });
}
```

### Wrapper per platform (web)

```typescript
// web/src/hooks/{{entity}}/use{{Entity}}Screen.ts
import { use{{Entity}}Screen as useCore } from '@{{project}}/shared-core';
import { useRouter } from 'next/navigation';

export function use{{Entity}}Screen(id: number) {
  const router = useRouter();
  return useCore({
    id,
    onSuccess: () => router.back(),
    onError: (msg) => window.alert(msg),
  });
}
```

---

## 📦 FOLDER STRUCTURE

Root-level contract:
- Keep the same organization as HobbyMap: `docs/`, `bats/`, `backend/`, `packages/shared-core/`, `mobile/`, `web/`, and `frontend/` when admin exists.
- Windows automation scripts live in `bats/` only. Do not leave `setup.bat` or `dev.bat` loose at the project root.
- `docs/` is the only home for architecture, design, business model, prompts, and audit files.
- `packages/shared-core/` is the brain. `web/`, `mobile/`, and `frontend/` consume it according to their audience.
- `frontend/` means the admin panel. Do not mix admin code into `web/`.

```
{{PROJECT_NAME}}/
├── bats/                                 # Windows automation scripts
├── backend/                              # Django API
│   ├── apps/{core,users,{{entity1}},{{entity2}}}/
│   ├── config/
│   └── manage.py
│
├── packages/
│   └── shared-core/                      # SINGLE BRAIN
│       ├── src/
│       │   ├── types/{domain}/index.ts
│       │   ├── hooks/{domain}/use*.ts
│       │   ├── services/*Service.ts
│       │   ├── constants/{strings/, icons.ts, routes.ts}
│       │   ├── theme/{spacing.ts, colors.ts, ...}
│       │   ├── lib/{storage.ts, apiClient.ts}
│       │   └── index.ts
│       ├── package.json
│       └── tsconfig.json
│
├── mobile/                               # React Native + Expo (RENDER ONLY)
│   ├── app/                              # Expo Router
│   ├── src/
│   │   ├── components/{ui, shared, features, cards}/
│   │   ├── screens/
│   │   ├── hooks/{domain}/use*.ts        # thin wrappers
│   │   └── lib/{apiClient.ts, storageAdapter.ts, iconMapper.ts}
│   └── package.json
│
├── web/                                  # Next.js (RENDER ONLY)
│   ├── app/                              # App Router
│   ├── src/
│   │   ├── components/{ui, shared, features, cards}/
│   │   ├── screens/
│   │   ├── hooks/{domain}/use*.ts        # thin wrappers
│   │   ├── lib/{apiClient.ts, storageAdapter.ts, iconMapper.ts}
│   │   └── theme/globals.css             # CSS Variables mirroring shared-core tokens
│   └── package.json
│
├── frontend/                             # Admin panel only if scaffolded
│   ├── src/admin/
│   └── package.json
│
└── docs/
    ├── ARCHITECTURE.md
    ├── BACKEND.md
    ├── SHARED-CORE.md          # the brain
    ├── FRONTEND-WEB.md
    ├── FRONTEND-MOBILE.md
    └── DESIGN.md
```

---

## 🌐 i18n PROTOCOL

All UI text goes through `STRINGS` from `@{{project}}/shared-core`.

```
packages/shared-core/src/constants/strings/
├── pt-BR.ts          # default
├── en.ts             # same shape
├── de-DE.ts          # same shape
├── types.ts          # type extracted from pt-BR
└── index.ts          # exports STRINGS based on locale
```

**Adding a string:**
1. Edit `pt-BR.ts`, `en.ts`, and `de-DE.ts` in shared-core (same change)
2. `yarn build` inside `packages/shared-core/`
3. Mobile and web pick up the new keys automatically (file: link)

Admin copy uses the same protocol under `STRINGS.admin.*`. Do not put visible labels in admin `config.jsx`, `constants.js`, table columns, filters, tabs, modals, toasts, placeholders, aria labels, empty states, or errors.

---

## WEB/MOBILE PARITY AUDIT

When reviewing a shared feature, use [`docs/PARITY-AUDIT.md`](./docs/PARITY-AUDIT.md):

- compare equivalent folders with `rg --files`;
- record file counts and missing/excess files;
- check render-only components on both platforms;
- confirm hooks/services/types/strings/tokens come from shared-core;
- update `docs/PARITY-AUDIT-EXECUTION.md` with `[x]` progress and percentages.

Do not approve a cross-platform feature only because both apps compile. Approve it when the tree, responsibilities, shared-core ownership, strings, tokens, and platform differences are explicit.

---

## 🔁 SHARED-CORE BUILD PROTOCOL

After any change in `packages/shared-core/src/`:

```bash
cd packages/shared-core && yarn build
```

The `dist/` folder is what mobile and web import. CI runs this before platform builds.

For dev convenience, run `yarn dev` in shared-core (watch mode) — both platforms pick up changes in real time.

---

## 🔍 PRE-MERGE CHECKLIST

**Logic & shared-core**
- [ ] All business logic lives in `packages/shared-core/src/hooks/`?
- [ ] Mobile and web only have thin (~5 line) hook wrappers?
- [ ] No type duplicated between mobile/, web/, and shared-core?
- [ ] Every service uses the injected `api()` client (no raw fetch/axios in shared-core)?
- [ ] Backend enforces every rule the shared-core hook enforces?

**Strings**
- [ ] Zero hardcoded text in JSX (mobile + web)?
- [ ] New strings added to `pt-BR.ts`, `en.ts`, and `de-DE.ts` in shared-core?
- [ ] Admin text uses `STRINGS.admin.*` instead of literals in JSX/config/constants?
- [ ] `yarn build` ran in `packages/shared-core/`?

**Styling**
- [ ] Web: no Tailwind, only `.module.css` + CSS Variables?
- [ ] Web: CSS Variables mirror `packages/shared-core/src/theme/*` values exactly?
- [ ] Mobile: no styled-components, only `StyleSheet.create`?
- [ ] Mobile: no `fontWeight`, only `fontFamily` (FONT_FAMILY.bold etc.)?
- [ ] Both: zero hardcoded px/colors/font-sizes/radii outside token declaration files?
- [ ] Changed files searched for `#`, `rgb`, `rgba`, `hsl`, `px`, `white`, and `black`?
- [ ] Admin styles, if touched, use only `--admin-*` tokens?

**Structure**
- [ ] Component folder has `Component.tsx` + (`.module.css` web | `.styles.ts` mobile) + `index.ts`?
- [ ] Same component name in mobile and web (e.g. `OrderDetail/` exists in both)?
- [ ] Parity differences are recorded in `docs/PARITY-AUDIT-EXECUTION.md`?
- [ ] 3-layer pattern (route → screen → feature) on both platforms?

**Business model**
- [ ] `docs/BUSINESS-MODEL.md` exists and has capital, monthly investment, CAC, conversion, costs, cashflow, and pessimistic/realistic/optimistic scenarios?

---

## 🌿 GIT WORKFLOW

| Environment | Branch | URL / Build target |
|-------------|--------|---------------------|
| Web Production | `main` | `{{prod-url}}` (Vercel) |
| Web Staging | `staging` | `{{staging-url}}` (Vercel) |
| Mobile Production | `main` (release branch) | EAS Build → App Store / Play Store |
| Mobile Staging | `staging` | EAS Build → TestFlight / Internal Track |

**Flow:** branch from `main` → push → preview → merge to `staging` → approved → merge to `main`.

**Rules:** never push directly to `main` or `staging` · always test mobile + web both work · run `yarn build` in shared-core before opening PR.

---

## 📚 References

| Area | Doc |
|------|-----|
| Architecture deep-dive (BFF, layers, hooks, shared-core) | [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) |
| Django patterns | [`docs/BACKEND.md`](./docs/BACKEND.md) |
| **Shared-core (the brain) — read first** | [`docs/SHARED-CORE.md`](./docs/SHARED-CORE.md) |
| Web rendering (Next.js) | [`docs/FRONTEND-WEB.md`](./docs/FRONTEND-WEB.md) |
| Mobile rendering (RN + Expo) | [`docs/FRONTEND-MOBILE.md`](./docs/FRONTEND-MOBILE.md) |
| Design system | [`docs/DESIGN.md`](./docs/DESIGN.md) |
| Business model and financial assumptions | [`docs/BUSINESS-MODEL.md`](./docs/BUSINESS-MODEL.md) |
| Web/mobile parity audit | [`docs/PARITY-AUDIT.md`](./docs/PARITY-AUDIT.md) |
| Admin panel (Vite + React, config-driven) — only if scaffolded | [`docs/ADMIN.md`](./docs/ADMIN.md) |

---

## 🛠️ THIS PROJECT'S DOMAIN

> Fill in when starting the project.

### Entities
{{ENTITIES}}
### User roles
{{USER_ROLES}}
### External integrations
{{INTEGRATIONS}}
### Brand color
- `--color-primary` (web) / `COLORS.primary` (mobile, shared-core): `{{PRIMARY_COLOR}}`
### Mobile-specific notes
{{MOBILE_NOTES}}
<!-- e.g. iOS-only initially, push notifications via Expo, deep links via expo-linking -->
