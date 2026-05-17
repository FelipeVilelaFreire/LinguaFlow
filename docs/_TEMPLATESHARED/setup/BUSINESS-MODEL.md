# Business Model - Decision Tool

> Every new project must have a business model document before serious launch or heavy feature expansion.
> The goal is not to predict the future perfectly. The goal is to expose assumptions, cost pressure, pricing logic, and validation priorities.

---

## Principle

Treat the model as a decision tool, not as a promise.

The first version can be simple, but it must separate:

- registered users vs active users;
- active users vs paying customers;
- core recurring revenue vs optional upside revenue;
- infra cost vs marketing cost vs team/operation cost;
- cash in the bank vs profit;
- product usage validation vs business model validation.

---

## Required Inputs

At minimum, define these assumptions:

| Area | Inputs |
|---|---|
| Capital | initial cash, already spent amount, monthly investment/aportes, planned runway |
| Users | registered users, monthly active users, paid users, activation rate, churn |
| Acquisition | organic growth, paid growth, CAC by channel/persona, referral rate |
| Pricing | plan names, monthly prices, conversion by plan, discounts, free trial |
| Revenue | subscriptions, marketplace take rate, sponsorship/ads, one-time services |
| Costs | hosting, database, storage, bandwidth, email/SMS/AI/API, payment gateway, taxes |
| Team | founders, contractors, support, sales, operations, accounting/legal |
| Risk | dependency on one revenue stream, regulation, payment failure, high churn |

Do not hide assumptions inside formulas. Put them in a visible `Assumptions` tab or config file.

---

## Scenario Presets

Create at least three scenarios:

| Scenario | Purpose |
|---|---|
| Pessimistic | Slow acquisition, higher CAC, lower conversion, higher churn |
| Realistic | Conservative growth based on what can be validated soon |
| Optimistic | Better conversion/growth, but still with defensible assumptions |

Optional fourth scenario:

| Scenario | Purpose |
|---|---|
| Breakout | What happens if a strong channel or marketplace loop works unusually well |

The realistic scenario is the default. Never present the optimistic scenario as the base case.

---

## Spreadsheet or Admin Structure

If the project uses a spreadsheet, create these tabs:

1. `Assumptions`
2. `Scenarios`
3. `Acquisition`
4. `Usage`
5. `Revenue`
6. `Costs`
7. `Cashflow`
8. `KPIs`
9. `Sensitivity`
10. `Validation Backlog`

If the project has an admin panel, also scaffold a business-plan app:

```text
frontend/src/admin/apps/business-plan/
├── BusinessPlan.jsx
├── BusinessPlan.config.js
├── components/
├── hooks/
└── index.js
```

All visible admin labels must come from `STRINGS.admin.businessPlan.*`.

---

## KPIs to Show

The model should show:

- MRR and ARR;
- active users and payer conversion;
- CAC and CAC payback;
- LTV/CAC when churn is known;
- churn and retention;
- gross margin and EBITDA;
- burn rate and runway;
- break-even month;
- cash balance by month;
- dependency on sponsorship/ads/marketplace upside;
- valuation as optional context, never as the main proof.

For marketplace products, also show:

- GMV;
- take rate;
- number of transactions;
- average ticket;
- supply-side active sellers/providers;
- demand-side active buyers/users.

---

## Validation Backlog

Every financial assumption must map to a validation action.

Examples:

| Assumption | Validation action | Evidence |
|---|---|---|
| Users will pay R$ X/month | Ask 10 target users to choose between real plans | calls, forms, pre-sales |
| CAC can stay below R$ X | Run a small paid campaign or manual outreach batch | cost per lead/customer |
| Providers will use management tools weekly | Pilot with 3-5 providers | weekly usage, feedback |
| Marketplace can create transactions | Manual concierge transaction before automation | completed orders |

If an assumption cannot be validated soon, mark it as speculative.

---

## Admin Business-Plan Rules

If implemented inside admin:

- keep formulas/config in `BusinessPlan.config.js`;
- keep UI render-only in `BusinessPlan.jsx` and components;
- keep labels in `STRINGS.admin.businessPlan.*`;
- expose scenario toggles instead of editing formulas inline;
- make assumptions visible and editable;
- show monthly and yearly views;
- show "realism/risk" indicators based on CAC, payback, churn, and revenue dependency.

---

## Pre-Launch Checklist

- [ ] Base model exists in `docs/BUSINESS-MODEL.md` or admin business-plan app?
- [ ] Assumptions are visible and named?
- [ ] Pessimistic, realistic, and optimistic scenarios exist?
- [ ] Capital, monthly investment, costs, taxes, gateway, CAC, churn, and conversion are modeled?
- [ ] Active users are separated from registered users?
- [ ] Paying customers are separated from active users?
- [ ] Revenue streams are separated instead of grouped into one number?
- [ ] Every visible string uses `STRINGS` (`STRINGS.admin.*` in admin)?
- [ ] Validation backlog says what must be tested next?
