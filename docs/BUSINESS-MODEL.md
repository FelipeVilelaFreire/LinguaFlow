# Business Model

Status: draft

This document is a decision tool for LinguaFlow/Talkly. It does not try to prove that the business will work; it exposes assumptions that must be validated before heavy launch, paid acquisition or major infra spend.

## Product

LinguaFlow/Talkly is a language-learning product built around:

- story-driven adventure learning;
- guided study and SRS review;
- vocabulary mastery;
- user progress, streaks and learning goals;
- cross-platform web and mobile apps.

## Current Business Assumption

The product is still in validation. The current priority is not maximizing revenue immediately; it is proving that users complete sessions, return, and feel that the adventure format improves learning.

Default stance:

- keep costs low;
- avoid expensive AI/audio generation by default;
- validate retention before paid acquisition;
- validate willingness to pay before building complex billing;
- keep professional voice acting as a future quality upgrade, not an MVP dependency.

## Revenue Options

Possible revenue streams:

- Free plan with limited daily progress.
- Monthly subscription for unlimited study/adventure access.
- Annual subscription with discount.
- School/family/group plan later.
- Premium content seasons later.
- Professional voice packs later, if quality becomes a strong differentiator.

Do not treat ads or sponsorship as base revenue until there is real usage volume.

## Required Metrics

Track separately:

- registered users;
- monthly active users;
- weekly active users;
- daily active users;
- activated users, meaning users who complete onboarding and first meaningful session;
- paying customers;
- churned customers;
- retained learners after 1, 7, 14 and 30 days.

Core product KPIs:

- phase completion rate;
- section completion rate;
- study session completion rate;
- D1, D7 and D30 retention;
- average sessions per active user;
- words mastered per active user;
- adventure-to-study crossover rate;
- profile/goal completion rate.

Business KPIs:

- MRR;
- ARR;
- payer conversion;
- ARPU;
- ARPPU;
- churn;
- gross margin;
- burn rate;
- runway;
- CAC;
- CAC payback;
- LTV/CAC once churn is known.

## Scenario Model

The admin `business-plan` app should expose at least these scenarios:

| Scenario | Purpose |
|---|---|
| Pessimistic | Slow acquisition, low conversion, high churn, higher infra cost |
| Realistic | Conservative default based on evidence that can be validated soon |
| Optimistic | Better retention/conversion, but still defensible |

The realistic scenario is always the default. The optimistic scenario is never the base case.

## Assumptions To Model

| Area | Required Inputs |
|---|---|
| Capital | starting cash, monthly investment, already spent amount, runway target |
| Users | registered users, active users, activated users, paid users, churn |
| Acquisition | organic growth, paid growth, CAC, referral rate |
| Pricing | plan names, monthly price, annual price, trial, discount |
| Revenue | subscription revenue, content upgrades, future group plans |
| Costs | hosting, database, storage, bandwidth, email, AI/API, TTS/audio, payment fees |
| Team | founders, contractors, support, content, design, legal/accounting |
| Risk | one revenue stream, high churn, high API cost, content production bottleneck |

## Validation Backlog

| Assumption | Validation Action | Evidence |
|---|---|---|
| Users understand the adventure format | Watch 5 users complete phase 1 section 1 | session recordings, notes |
| Adventure improves motivation | Compare return rate of adventure users vs study-only users | D1/D7 retention |
| Users will pay for the product | Ask 10 target users to choose between real plan options | interviews, pre-sale intent |
| Default audio is good enough for MVP | Test current browser/Piper/default voice with real users | qualitative feedback |
| Premium voices matter | A/B test default vs generated/pro voice samples later | conversion/retention delta |
| CAC can stay sustainable | Run a tiny manual outreach or paid test only after retention signal | cost per activated user |
| Mobile is necessary | Compare usage and retention between web and Expo builds | platform analytics |

## Admin Business-Plan Target

When the admin is upgraded to the full local admin architecture, add:

```txt
admin/src/admin/apps/business-plan/
├── BusinessPlan.jsx
├── BusinessPlan.config.js
├── components/
├── hooks/
└── index.js
```

The admin app should show:

- scenario selector;
- assumptions table;
- pricing table;
- user funnel;
- revenue forecast;
- cost forecast;
- cashflow;
- runway;
- break-even month;
- KPI summary;
- sensitivity/risk indicators;
- validation backlog.

All labels must come from:

```txt
STRINGS.admin.businessPlan.*
```

## Launch Gate

Before serious launch, confirm:

- [ ] `docs/BUSINESS-MODEL.md` is current.
- [ ] At least pessimistic, realistic and optimistic scenarios exist.
- [ ] Active users are separate from registered users.
- [ ] Paying users are separate from active users.
- [ ] AI/audio/storage costs are modeled.
- [ ] Payment fees and taxes are modeled.
- [ ] Retention is measured with real users.
- [ ] Every major assumption has a validation action.
- [ ] Admin business-plan app exists or the document is enough for the current stage.
