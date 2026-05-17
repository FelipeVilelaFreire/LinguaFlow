# Parity Audit - Web/Mobile/Shared-Core

> Use this playbook whenever a project has both `web/` and `mobile/`.
> The goal is to keep both platforms structurally comparable while keeping all domain logic in `packages/shared-core`.

---

## Golden Rule

Web and mobile may render differently, but they must share the same domain brain:

```text
packages/shared-core = hooks, services, types, strings, tokens, validation, mappers
web/                 = render-only Next.js wrapper
mobile/              = render-only Expo/React Native wrapper
```

If a feature exists on both platforms, the tree should be intentionally symmetric.

---

## What to Audit

For each equivalent folder pair, for example:

```text
web/src/components/cards/entity
mobile/src/components/cards/entity
```

verify:

1. Folders and component names match, or differences are documented.
2. Components are render-only.
3. Domain hooks/services/types come from `@{{project}}/shared-core`.
4. Visible text uses `STRINGS.xxx`.
5. New strings exist in `pt-BR.ts`, `en.ts`, and `de-DE.ts`.
6. Web uses CSS Modules and `var(--...)` tokens.
7. Mobile uses `.styles.ts` and shared-core tokens.
8. Web dark/light theme is not broken by fixed white/black/hex surfaces.
9. No platform has duplicated validation, payload mapping, or fetch logic.
10. Platform-specific differences are justified.

---

## Render-Only Criteria

A component is render-only when it:

- receives data through props or a shared-core hook wrapper;
- renders JSX/TSX only;
- does not call `fetch`, axios, or API services directly;
- does not own domain validation;
- does not build API payloads;
- does not duplicate domain types;
- uses local state only for local UI state, such as modal open/closed or selected tab.

Move anything else to `packages/shared-core/src/hooks`, `services`, `utils`, or `validation`.

---

## Audit Flow

Follow this sequence one folder at a time:

1. Pick one web/mobile folder pair.
2. Run `rg --files` for both sides.
3. Record file counts and missing/excess files.
4. Build a pair matrix.
5. Read web TSX, web CSS module, mobile TSX, mobile styles, then shared-core imports.
6. Record findings with file paths and line numbers.
7. Fix only small obvious issues during the audit.
8. Update the execution report.
9. Move to the next folder only after the current pair is classified.

Recommended first folders:

| Order | Web | Mobile |
|---:|---|---|
| 1 | `web/src/components/cards/entity` | `mobile/src/components/cards/entity` |
| 2 | `web/src/components/cards` | `mobile/src/components/cards` |
| 3 | `web/src/components/features` | `mobile/src/components/features` |
| 4 | `web/src/components/modals` | `mobile/src/components/modals` |
| 5 | `web/src/components/shared` | `mobile/src/components/shared` |
| 6 | `web/src/components/ui` | `mobile/src/components/ui` |

---

## Execution Report

Create or update:

```text
docs/PARITY-AUDIT-EXECUTION.md
```

Use this structure:

```markdown
# Parity Audit Execution

Progress: 0/0 pairs (0%)

## Folder Matrix

| Status | Area | Web | Mobile | Pairs | Done | Result |
|---|---|---|---|---:|---:|---|
| [ ] | cards/entity | web/src/components/cards/entity | mobile/src/components/cards/entity | 0 | 0 | Pending |

## Pair Matrix

| Status | Pair | Web | Mobile | Result | Issues |
|---|---|---|---|---|---|
| [ ] | ExampleCard | web/... | mobile/... | Pending | - |

## Findings

| Severity | File | Line | Problem | Recommendation |
|---|---|---:|---|---|
| Medium | web/... | 0 | Visible text hardcoded | Move to STRINGS |

## Decisions

- 
```

After each pair, update `[ ]` to `[x]` and update the percentage.

---

## Severity

Use these classifications:

- `OK`
- `OK with justified platform difference`
- `Minor issue`
- `Medium issue`
- `Major issue`
- `Blocked`

Major issues include direct HTTP in components, duplicated domain logic, hardcoded visible text across many files, local domain types, or one platform missing a feature without a recorded decision.

---

## Stop Conditions

Pause and ask for direction when:

- the tree mismatch is structural;
- fixing the issue requires broad shared-core + web + mobile changes;
- the worktree has many unrelated edits;
- the audit is turning into a large refactor.

Audit first. Refactor in small blocks after the problem is clearly mapped.
