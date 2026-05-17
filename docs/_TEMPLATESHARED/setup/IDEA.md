# Project Idea

> Fill this file with your project specifics. Claude reads it to build the app.
>
> You can write in Portuguese — Claude understands. The generated **code and docs** will be in English, but visible UI strings must use `STRINGS` in `pt-BR`, `en`, and `de-DE`.
>
> Delete the example comments (`<!-- ... -->`) once you've filled your own values.

---

## Project name

`{{kebab-case-name}}`

<!-- Example: `finance-track` -->

## Display name

`{{Display Name}}`

<!-- Example: `FinanceTrack` -->

## What does the app do?

<!-- One paragraph: what is the product, who is the user, what is the core action?
     Example:
     A personal finance tracker. Users register income and expenses, categorize
     transactions, set monthly budgets per category, and see dashboards showing
     where their money goes. Single-user app for now (no shared accounts).
-->

{{One paragraph describing the product}}

---

## Entities

<!-- List 2-6 main entities with their key fields and relationships.
     For each entity, list: fields (with type), relationships, special rules.

     Example:
     - **Transaction**
       Fields: amount (decimal), type (income|expense), date, description, category (FK Category)
       Belongs to: User (FK), Category (FK)
       Rules: amount must be > 0; date cannot be in the future

     - **Category**
       Fields: name, icon (string), color (hex), monthly_budget (decimal, optional)
       Belongs to: User (FK)
       Rules: unique name per user

     - **MonthlySummary** (computed, not persisted)
       Fields: month, total_income, total_expense, balance, by_category[]
-->

{{Bulleted list of entities}}

---

## User roles

<!-- Who can do what?
     Example:
     - **user** — full access to own data only (single role, no admin separation for now)

     Or:
     - **customer** — browses products, places orders
     - **vendor** — creates products, manages own catalog
     - **admin** — full access to everything
-->

{{Roles list}}

---

## External integrations

<!-- Anything that requires API keys / OAuth / webhooks?
     "none yet" is a valid answer.

     Example:
     - **Plaid** (later) — sync bank transactions automatically
     - **SendGrid** — transactional emails (welcome, password reset)
     - **AWS S3** — receipt image uploads
-->

{{Integrations or "none yet"}}

---

## Brand color

<!-- Primary accent color in hex. Default: #0066ff.
     Examples:
     - #10b981 — green (finance, health)
     - #5e6ad2 — purple (productivity, Linear-like)
     - #0070f3 — blue (Vercel-like)
     - #18181b — black (Notion-like, neutral premium)
     - #ef4444 — red (alert, food delivery)
-->

`{{#hex}}`

---

## Admin panel

<!-- Cross-platform projects often also need a custom admin frontend.

- yes  → scaffolds `frontend/` as a Vite + React project (separate from mobile/ and web/).
         Config-driven modular admin, gated by `role=admin`. See docs/ADMIN.md.
         Admin uses shared-core for `STRINGS.admin.*` and locale; visible UI text must be added in pt-BR, en, and de-DE together.

- no   → Django Admin at /admin/ is enough.
-->

`{{yes | no}}`

---

## Business model notes

<!-- Used to seed docs/BUSINESS-MODEL.md and the optional admin business-plan app.
     Keep it rough if the business model is not validated yet.

     Include:
     - expected users and active users;
     - who pays and why;
     - initial capital and monthly investment/aportes;
     - likely prices/plans;
     - possible revenue streams (subscription, marketplace, sponsorship, services);
     - expected infra/operation/marketing costs;
     - pessimistic, realistic, and optimistic scenario notes;
     - assumptions that need validation.
-->

{{Business model assumptions or "not validated yet"}}

---

## Conda env name

<!-- Name for the Conda environment that setup.bat will create (for the Django backend).
     Default: same as project name (kebab-case). Used by setup.bat and dev.bat.
-->

`{{conda-env-name}}`

## Database name

<!-- PostgreSQL database name. Default: project_name with underscores.
     Used by setup.bat to create the DB via psql.
-->

`{{db_name}}`

---

## Optional — additional notes

<!-- Anything Claude should know but doesn't fit above.
     Examples:
     - "Mobile-first heavily — 80% of users will be on phone"
     - "Use the Bento Grid pattern on the dashboard"
     - "Make the dashboard the default landing page after login"
     - "All money values should display with R$ prefix"
     - "Dates always in DD/MM/YYYY format"
-->

{{Notes or "none"}}

---

## Optional — decorative effects (ReactBits)

<!-- ReactBits (https://www.reactbits.dev) is allowed ONLY on public-facing pages.
     If you want any, list which page → which component. Stub will be created with
     a // TODO link so you paste the real component later. See docs/FRONTEND-WEB.md.
     Leave as "none" if the project is purely operational.

     Examples:
     - /login → Aurora background (gold tint matching brand color)
     - /onboarding → ShinyText for "Welcome to {{display name}}" headline
     - /register → Beams background (subtle)
     - 404 page → DecryptionEffect on the headline
     - none — internal tool, no marketing surface
-->

{{Per-page list or "none"}}

---

## Mobile-specific notes

<!-- This is a CROSS-PLATFORM project (mobile + web + shared-core). Provide details
     that affect mobile but not web (or vice versa).

     Examples:
     - "iOS first, Android in iteration 2"
     - "Push notifications via Expo (configure expo-notifications)"
     - "Deep linking: scheme=myapp, universal links to {{prod-url}}/*"
     - "Camera access for receipt scanning (expo-camera)"
     - "Offline support via local SQLite (expo-sqlite)"
     - "Web is admin/dashboard only; mobile is the main user surface"
     - "none — mobile and web are feature-parity"
-->

{{Mobile notes or "none"}}

---

## Platforms to scaffold

<!-- All three (backend + shared-core + mobile + web) are scaffolded by default.
     Override if you want to skip one for now.

     Examples:
     - all (default — backend + shared-core + mobile + web)
     - skip mobile (web + backend + shared-core only — saves the mobile/ folder for later)
     - skip web (mobile + backend + shared-core only)
-->

{{all | skip mobile | skip web}}

---

## Optional — first screens to prioritize

<!-- If you want Claude to start with specific screens before scaffolding the rest.
     Example:
     1. Login + Register
     2. Dashboard with monthly summary
     3. Add Transaction modal
     4. Transaction list
     5. Categories management
-->

{{Ordered list or "scaffold all from the entities above"}}
