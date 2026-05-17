# Bootstrap Prompt — Start a New Project

> Use this when initializing a brand-new project from scratch with the template.

---

## How to use

1. Copy this entire file content.
2. Open Claude Code in the empty project folder.
3. Paste, replacing `{{IDEA}}` with one sentence describing your app.
4. Answer the 5 questions Claude asks.
5. Claude scaffolds backend, frontend, and i18n.

---

## The Prompt

```
I want to build {{IDEA}}.

This project follows the rules in CLAUDE.md, ARCHITECTURE.md, BACKEND.md,
SHARED-CORE.md, FRONTEND-WEB.md, FRONTEND-MOBILE.md, DESIGN.md, BUSINESS-MODEL.md,
and PARITY-AUDIT.md (already in /docs).

Please ask me 5 short questions to clarify the domain before scaffolding.
After my answers:

1. Fill the placeholders in CLAUDE.md ({{PROJECT_NAME}}, {{ENTITIES}},
   {{USER_ROLES}}, {{INTEGRATIONS}}, {{PRIMARY_COLOR}}).
2. Scaffold backend/:
   - Django project with config/settings split (base/dev/prod)
   - apps/core/ with SoftDeleteModel
   - apps/users/ with custom User (email login) + JWT
   - One app per entity, with model + serializer + viewset + urls + admin
   - requirements.txt
   - .env.example
3. Scaffold web/:
   - Next.js 16.1 App Router project (React 19, TypeScript 5, Turbopack dev,
     FontAwesome 7, NO Tailwind / NO CSS-in-JS)
   - src/ folder structure (components, screens, hooks, services, types,
     constants, lib, theme)
   - theme/globals.css with CSS Variables from DESIGN.md
   - constants/strings/{pt-BR,en,de-DE,types,index}.ts with actions namespace
   - docs/BUSINESS-MODEL.md with assumptions, scenarios, KPIs, and validation backlog
   - docs/PARITY-AUDIT.md for web/mobile tree, render-only, STRINGS, and token audits
   - constants/routes.ts and constants/icons.ts
   - lib/storage.ts and lib/iconMapper.ts
   - services/api.ts (axios with JWT interceptors)
   - One feature folder per entity (with .module.css)
   - One screen per entity following the 3-layer pattern
4. Do NOT run npm install or python migrate — just scaffold the code.
5. End with a summary: list every file created and the next 3 commands
   I should run to get the system live (db setup, deps install, dev server).

Follow every rule strictly. No Tailwind. No hardcoded text. No raw fetch.
Mobile-first CSS. BFF philosophy.
```

---

## The 5 questions Claude will ask

These are the questions Claude should ask before scaffolding. They map directly to placeholders.

1. **Project name** — short slug (kebab-case) for folder names, and a display name.
2. **Domain in one paragraph** — what does the app do, who is the user, what is the core action?
3. **Entities** — list 2-5 main domain entities with their key fields and relationships.
   Example: "Order has many OrderItems; Order belongs to User; OrderItem references Product."
4. **User roles** — who can do what?
   Example: "customer (browses, orders), vendor (lists products), admin (everything)".
5. **Brand color** — primary accent (hex). If unsure, default to `#0066ff`.

---

## What Claude produces

After answers, expect:

```
backend/
├── apps/
│   ├── core/         (models.py with SoftDeleteModel)
│   ├── users/        (models.py + JWT views + serializers)
│   ├── {{entity1}}/
│   └── {{entity2}}/
├── config/settings/  (base, development, production)
├── manage.py
├── requirements.txt
└── .env.example

web/
├── app/
│   ├── (auth)/{login,register}/page.tsx
│   ├── (main)/dashboard/page.tsx
│   ├── (main)/{{entity}}/[id]/page.tsx
│   ├── layout.tsx
│   └── globals.css
├── src/
│   ├── components/
│   │   ├── ui/{Button,Input,Modal,Icon,Skeleton}/
│   │   ├── shared/{Header,BottomNav}/
│   │   └── features/{{Entity}}Detail/
│   ├── screens/{{Entity}}Screen/
│   ├── hooks/
│   │   ├── auth/useAuthForm.ts
│   │   └── {{entity}}/{useScreen,useForm}.ts
│   ├── services/{api,authService,{{entity}}Service}.ts
│   ├── types/{user,{{entity}}}/index.ts
│   ├── constants/
│   │   ├── strings/{pt-BR,en,de-DE,types,index}.ts
│   │   ├── icons.ts
│   │   └── routes.ts
│   ├── lib/{storage,iconMapper,errors,auth}.ts
│   └── theme/globals.css
├── package.json
├── tsconfig.json
└── next.config.ts

CLAUDE.md (filled with project specifics)
docs/{ARCHITECTURE,BACKEND,FRONTEND-WEB,FRONTEND-MOBILE,SHARED-CORE,DESIGN,BUSINESS-MODEL,PARITY-AUDIT}.md (copied from template)
```

And the 3 next commands:
```
1. cd backend && cp .env.example .env && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt
2. createdb {{project_db}} && python manage.py migrate && python manage.py createsuperuser
3. cd ../web && npm install && npm run dev
```
