# New Feature Prompt — Add a shared feature

> Use this when adding a feature reused across **2 or more routes**.
> If only 1 route uses it, keep it inline (don't create a feature folder).

---

## When to use

- A card / view / form / panel will appear in multiple screens
- The feature has its own data lifecycle (fetch, save, delete)
- The feature has business logic that warrants its own hook

If only 1 route uses it, skip this prompt and write the code inline.

---

## The Prompt

```
Add a feature: {{FEATURE_NAME}}.

What it does: {{ONE_PARAGRAPH_DESCRIPTION}}

Where it appears (routes): {{LIST_OF_ROUTES}}

Backend endpoints needed: {{ENDPOINTS_OR_"reuse existing"}}

Follow the rules in CLAUDE.md, ARCHITECTURE.md, SHARED-CORE.md, FRONTEND-WEB.md, FRONTEND-MOBILE.md, PARITY-AUDIT.md, and BACKEND.md.

Steps to perform IN THIS ORDER:

1. BACKEND (if endpoints don't exist yet):
   - Create or update model in apps/{{domain}}/models.py
   - Add migration
   - Read serializer + Write serializer in serializers.py
   - ViewSet with permissions in views.py
   - Register URL in apps/{{domain}}/urls.py
   - Register in admin.py
   - Add validation rules: {{LIST_OF_RULES}}

2. SHARED TYPES:
   - Add or update packages/shared-core/src/types/{{domain}}/index.ts with:
     - {{Entity}} (read shape, matches read serializer)
     - {{Entity}}CreateData / {{Entity}}UpdateData (write shapes)

3. SHARED SERVICE:
   - Add methods to packages/shared-core/src/services/{{domain}}Service.ts
   - Match endpoints exactly: list, retrieve, create, update, delete, [custom actions]

4. SHARED HOOK + PLATFORM WRAPPERS:
   - Create packages/shared-core/src/hooks/{{domain}}/use{{Entity}}Screen.ts
   - Create thin wrappers in web/src/hooks/{{domain}}/ and mobile/src/hooks/{{domain}}/
   - Standard interface: { data, loading, error, isSaving, handleSave, handleDelete, refresh }
   - If form involved: also create use{{Entity}}Form.ts with { form, errors, isValid, setField, toCreateData }

5. FRONTEND STRINGS:
   - Add new copy to packages/shared-core/src/constants/strings/pt-BR.ts, en.ts, and de-DE.ts
   - All three files updated in this same change

6. FRONTEND COMPONENT:
   - Create web/src/components/features/{{Entity}}{{Variant}}/
     - {{Entity}}{{Variant}}.tsx (render only, consumes hook via props)
     - {{Entity}}{{Variant}}.module.css (mobile-first, CSS Variables only)
     - index.ts (barrel export)
   - Create the matching mobile feature folder when this is a shared feature
   - Record any intentional web/mobile tree difference in docs/PARITY-AUDIT-EXECUTION.md
   - Component receives data and callbacks via props — never fetches itself

7. WIRE INTO ROUTES:
   - For each route in {{LIST_OF_ROUTES}}:
     - app/{route}/page.tsx remains thin (~5 lines)
     - src/screens/{Route}Screen/ uses the hook and renders the feature

DO NOT:
- Use Tailwind
- Hardcode any text (use STRINGS)
- Hardcode any color/spacing (use CSS Variables)
- Use raw fetch (use the service)
- Put logic in the component (it goes in the hook)

When done, report:
- All files created/modified
- Backend rules added (and where they're enforced — ViewSet permission? serializer.validate?)
- Whether mobile and desktop layouts diverge (and how)
```

---

## Example invocation

```
Add a feature: OrderSummaryCard.

What it does: Shows an order's status, total, and last 3 items in a compact
card. Tapping the card navigates to the order detail. Has a "Cancel order"
button visible only when status is 'pending' and the user is the owner.

Where it appears (routes): /dashboard, /orders, /profile

Backend endpoints needed: reuse existing GET /api/orders/, POST /api/orders/{id}/cancel/

[paste the rest of the prompt above]
```

---

## What Claude should NOT do

- Skip the read-vs-write serializer split
- Recreate types that already exist in `src/types/`
- Put fetch logic inside the component
- Mix mobile and desktop styles without `@media (min-width: 769px)`
- Forget to add strings to `pt-BR.ts`, `en.ts`, and `de-DE.ts`
- Add icons without registering them in `iconMapper.ts`
