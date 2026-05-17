# Architecture

> The deep-dive behind the rules in `CLAUDE.md`.
> Read this when designing a feature. Read `CLAUDE.md` before writing code.

Shared-template override: this architecture is the web pattern plus a cross-platform layer. In this template, `packages/shared-core/` owns hooks, services, types, strings, tokens, validation, and mappers. `web/` and `mobile/` are render-only wrappers. For shared features, keep equivalent web/mobile trees or record intentional differences in `docs/PARITY-AUDIT-EXECUTION.md`.

---

## ⚡ The Four Principles

```
backend     = SOURCE OF TRUTH   →  business rules, integrity, authorization in Django
shared-core = BRAIN             →  hooks, services, types, strings, tokens, validation
web/mobile  = RENDER ONLY       →  platform JSX/TSX. Zero domain logic. Zero hardcoded values.
admin       = CONFIG DRIVEN     →  config/tabs/cards render from STRINGS.admin.*
```

These rules compose: a platform component renders what a shared-core hook gives it, the hook calls a shared-core service, the service hits Django, and Django decides what is true.

---

## 🛡️ BFF (Backend-for-Frontend) Philosophy

The frontend is a **dumb pipe with smart UX**. It can transform, validate, and decorate — but it cannot decide. Every business rule that protects data integrity, authorization, or money lives in Django.

### Trust boundaries

```
┌───────────────────────────────────────────┐
│  Browser (untrusted)                      │
│  — UX validation only                     │
│  — Anything visible is replayable by user │
└───────────────────────────────────────────┘
              ↓ HTTPS
┌───────────────────────────────────────────┐
│  Next.js server (semi-trusted)            │
│  — Server actions / API routes (BFF)      │
│  — Adds session, composes Django calls    │
│  — Still cannot bypass Django authz       │
└───────────────────────────────────────────┘
              ↓
┌───────────────────────────────────────────┐
│  Django (trusted, sole authority)         │
│  — Authorization, validation, persistence │
│  — All rules enforced here, no exceptions │
└───────────────────────────────────────────┘
```

### The duplication rule

If a rule appears in the UI, it must also exist in Django. The reverse is not required — Django can have rules the UI never shows.

| Example rule | Frontend (UX) | Django (truth) |
|--------------|---------------|----------------|
| Order amount must be > 0 | Form validation, button disabled | `serializer.validate_amount()` raises `ValidationError` |
| Only owner can edit | Hide edit button | `permission_classes = [IsOwner]` |
| Cart total = sum(items) | Computed in `useCart()` for optimistic UI | Recomputed on backend during checkout, frontend value ignored |
| Coupon discount applied | Show discounted price immediately | Recalculated on `POST /orders/`, persisted from server result |

### Anti-pattern: trusting the client

```typescript
// ❌ NEVER — frontend decides authorization
if (user.role === 'admin') {
  await api.delete(`/users/${id}`);
}

// ✅ — frontend hides UI, backend enforces
{user.role === 'admin' && <DeleteButton onClick={() => deleteUser(id)} />}
// And on the backend: permission_classes = [IsAdmin]
```

### When Next.js acts as a BFF

Use Next.js server actions / API routes as a **thin orchestration layer**:
- Aggregate multiple Django calls into one
- Add HTTP-only session cookies
- Hide internal API shapes from the browser
- Cache server-side

The BFF layer **does not own business logic** — it composes Django. If you find yourself writing rules in `app/api/...` instead of Django, stop.

---

## 🏛️ The 3 Layers

Every screen follows the same pattern: a thin route wrapper, a screen that fetches, and a feature that renders.

```
┌─────────────────────────────────────────┐
│  app/(group)/route/page.tsx             │  Thin wrapper (~5 lines)
│  - Reads route params                   │
│  - Renders <XxxScreen id={id} />        │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  src/screens/XxxScreen/                 │  Fetch layer
│  - Calls useXxxScreen(id)               │
│  - Renders skeleton / error / data      │
│  - Delegates UI to feature              │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  src/components/features/XxxDetail/     │  Pure UI
│  - Receives data via props              │
│  - Zero fetch, zero router              │
│  - Reusable across contexts             │
└─────────────────────────────────────────┘
```

### Layer 1: `app/route/page.tsx`

```typescript
// app/(main)/orders/[id]/page.tsx
import { OrderScreen } from '@/src/screens/OrderScreen';

export default async function Page({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  return <OrderScreen id={Number(id)} />;
}
```

Rules: ~5 lines. Zero logic. Zero styles. Only routing concerns.

### Layer 2: `src/screens/XxxScreen/`

```typescript
// src/screens/OrderScreen/OrderScreen.tsx
'use client';
import { useOrderScreen } from '@/src/hooks/order/useOrderScreen';
import { OrderDetail } from '@/src/components/features/OrderDetail';
import { Skeleton } from '@/src/components/ui/Skeleton';
import { ErrorState } from '@/src/components/ui/ErrorState';

export function OrderScreen({ id }: { id: number }) {
  const { data, loading, error, handleSave, handleDelete } = useOrderScreen({ id });

  if (loading) return <Skeleton />;
  if (error || !data) return <ErrorState message={error} />;

  return <OrderDetail order={data} onSave={handleSave} onDelete={handleDelete} />;
}
```

Rules: handles loading/error states. Delegates UI. No JSX beyond shell.

### Layer 3: `src/components/features/XxxDetail/`

```typescript
// src/components/features/OrderDetail/OrderDetail.tsx
import styles from './OrderDetail.module.css';
import { STRINGS } from '@/src/constants/strings';
import type { Order, OrderUpdateData } from '@/src/types/order';

interface OrderDetailProps {
  order: Order;
  onSave: (data: OrderUpdateData) => Promise<void>;
  onDelete: () => Promise<void>;
}

export function OrderDetail({ order, onSave, onDelete }: OrderDetailProps) {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>{STRINGS.order.detail.title}</h1>
      {/* render fields, buttons, etc. */}
    </div>
  );
}
```

Rules: pure UI. Zero fetch, zero router, zero authentication. Reusable in any context.

---

## 🪝 Hook Taxonomy

There are five canonical hook levels. If your hook doesn't fit one, you are probably mixing concerns.

| Level | Suffix | Responsibility | Returns |
|-------|--------|----------------|---------|
| Screen | `useXxxScreen` | Full screen lifecycle: fetch + save + delete | `{ data, loading, error, handleSave, handleDelete, isSaving }` |
| Form | `useXxxForm` | Form state, validation, transformation | `{ form, errors, isValid, setField, toCreateData }` |
| Tab | `useXxxTab` | Filterable list inside a parent screen | `{ items, filter, setFilter, loading }` |
| Data | `useXxxData` | Just loads data, no actions | `{ data, loading, error, refresh }` |
| Card | `useXxxCardData` | Computes display DTOs from raw entities | `{ title, subtitle, badge, accentColor }` |

### Standard interfaces

```typescript
// Screen-level — full lifecycle
export interface UseXxxScreenOptions {
  id?: number;
  onSuccess?: () => void;
  onError?: (msg: string) => void;
}
export interface UseXxxScreenReturn {
  data: XxxDetail | null;
  loading: boolean;
  error: string | null;
  isSaving: boolean;
  handleSave: (data: XxxCreateData) => Promise<void>;
  handleDelete: () => Promise<void>;
  refresh: () => Promise<void>;
}

// Form-level — pure state
export interface UseXxxFormOptions {
  initial?: Partial<XxxCreateData>;
}
export interface UseXxxFormReturn {
  form: XxxFormState;
  errors: Partial<Record<keyof XxxCreateData, string>>;
  isValid: boolean;
  setField: <K extends keyof XxxFormState>(key: K, value: XxxFormState[K]) => void;
  toCreateData: () => XxxCreateData;
  reset: () => void;
}
```

### Composition rule

A screen hook **composes** smaller hooks; it does not duplicate them.

```typescript
// ✅ Composition
export function useOrderScreen({ id }: UseOrderScreenOptions) {
  const { data, loading, error, refresh } = useOrderData(id);
  const form = useOrderForm({ initial: data });
  // ...combines them
}

// ❌ Duplication
export function useOrderScreen({ id }) {
  const [order, setOrder] = useState(null);
  const [formState, setFormState] = useState({});
  // ...reimplements what useOrderData and useOrderForm already do
}
```

---

## 📁 Folder Structure

```
{{PROJECT_NAME}}/
│
├── backend/                       # Django API
│   ├── apps/
│   │   ├── core/                  # Base classes, soft delete
│   │   ├── users/                 # User + JWT
│   │   ├── {{entity1}}/
│   │   └── {{entity2}}/
│   ├── config/                    # settings/, urls.py, wsgi.py
│   └── manage.py
│
├── web/                           # Next.js
│   ├── app/                       # File-based routing
│   │   ├── (auth)/
│   │   │   ├── login/page.tsx
│   │   │   └── register/page.tsx
│   │   ├── (main)/
│   │   │   ├── dashboard/page.tsx
│   │   │   └── {{entity}}/[id]/page.tsx
│   │   ├── layout.tsx
│   │   └── globals.css
│   │
│   └── src/
│       ├── components/
│       │   ├── features/          # Cross-route reusable UIs
│       │   │   └── OrderDetail/
│       │   │       ├── OrderDetail.tsx
│       │   │       ├── OrderDetail.module.css
│       │   │       ├── OrderDetail.types.ts
│       │   │       └── index.ts
│       │   ├── modals/            # Reusable modals
│       │   ├── shared/            # Layout, header, nav
│       │   ├── cards/             # List item cards
│       │   └── ui/                # Button, Input, Modal, Icon, Skeleton
│       │
│       ├── screens/               # Fetch layer (between app/ and features/)
│       │   └── OrderScreen/
│       │       ├── OrderScreen.tsx
│       │       └── index.ts
│       │
│       ├── hooks/                 # BRAIN — all logic
│       │   ├── order/
│       │   │   ├── useOrderScreen.ts
│       │   │   ├── useOrderForm.ts
│       │   │   └── useOrdersTab.ts
│       │   └── auth/
│       │       └── useAuthForm.ts
│       │
│       ├── services/              # HTTP layer
│       │   ├── api.ts             # axios instance + interceptors
│       │   ├── orderService.ts
│       │   └── authService.ts
│       │
│       ├── types/                 # Domain contracts
│       │   ├── order/index.ts
│       │   └── user/index.ts
│       │
│       ├── constants/             # STRINGS, ICONS, ROUTES
│       │   ├── strings/
│       │   │   ├── pt-BR.ts
│       │   │   ├── en.ts
│       │   │   ├── de-DE.ts
│       │   │   ├── types.ts
│       │   │   └── index.ts
│       │   ├── icons.ts
│       │   └── routes.ts
│       │
│       ├── lib/                   # iconMapper, utils
│       └── theme/                 # globals.css with CSS Variables
│
└── docs/
    ├── ARCHITECTURE.md            # this file
    ├── BACKEND.md
    ├── FRONTEND-WEB.md
    ├── FRONTEND-MOBILE.md
    ├── SHARED-CORE.md
    ├── PARITY-AUDIT.md
    └── DESIGN.md
```

---

## 🎯 Decision Trees

### Where does this code go?

```
Is it a database query, business rule, or authorization?
  └─ Django.

Is it state, form, or domain behavior used across components/platforms?
  └─ Hook in packages/shared-core/src/hooks/{domain}/

Is it a network call?
  └─ Service in packages/shared-core/src/services/

Is it a TypeScript type for an entity?
  └─ packages/shared-core/src/types/{domain}/

Is it user-facing text?
  └─ packages/shared-core/src/constants/strings/{pt-BR,en,de-DE}.ts

Is it a static visual value (color, spacing, font)?
  └─ web/src/theme/globals.css as a CSS Variable

Is it pure UI (JSX + render-only logic)?
  └─ Component in web/src/components/ and/or mobile/src/components/
```

### Should this be a feature or live inline in the route?

```
How many routes use this UI?
  ├─ 1 → inline in app/{route}/page.tsx (or screen)
  └─ 2+ → src/components/features/{Name}/
```

---

## 🧱 Naming Conventions

| Concept | Pattern | Example |
|---------|---------|---------|
| Component folder | `PascalCase` | `OrderDetail/` |
| Component file | `PascalCase.tsx` | `OrderDetail.tsx` |
| Hook file | `camelCase.ts` | `useOrderScreen.ts` |
| Type file | `index.ts` inside `types/{domain}/` | `types/order/index.ts` |
| Service file | `camelCase.ts` | `orderService.ts` |
| Handler | `handleXxx` | `handleSave`, `handleDelete` |
| Boolean | `isXxx`, `hasXxx`, `canXxx` | `isSaving`, `hasError` |
| Interface — props | `XxxProps` | `OrderDetailProps` |
| Interface — payload | `XxxCreateData`, `XxxUpdateData` | `OrderCreateData` |
| Interface — hook return | `UseXxxReturn` | `UseOrderScreenReturn` |
| Interface — hook options | `UseXxxOptions` | `UseOrderScreenOptions` |

---

## 🚦 Refactoring Decision

Before writing new code in an existing component, run the diagnostic from `CLAUDE.md`:

```
Component .tsx contains:
  useState for data?    →  Extract to a hook.
  useEffect for fetch?  →  Extract to a hook.
  handleSave/Delete?    →  Extract to a hook.
  Validation logic?     →  Extract to a hook.
  Raw fetch/axios?      →  Move to a service.
  Hardcoded text?       →  Move to STRINGS.
  Hardcoded color/px?   →  Replace with var(--token).
  Tailwind class?       →  Replace with .module.css.
```

Refactor first, then add your new code on top of clean structure.
