# Cross-Platform Roadmap Checkpoint

Checkpoint date: 2026-05-17

This document records the current checkpoint for the local shared web/mobile/admin architecture.

## Current State

The project currently has:

- `backend/`: Django + DRF, already split by domain apps.
- `frontend-web/`: Vite + React 18 + Tailwind CSS.
- `admin/`: separate admin frontend.
- `docs/`: product, content, design, architecture and feature docs.
- `docs/architecture/`: target architecture docs for this project.

The backend is close to the target architecture. The frontend is not: it still keeps types, services, hooks, strings and render logic inside `frontend-web`.

## Target Architecture

The target is to move toward this repository shape:

```txt
backend/                source of truth
packages/shared-core/   shared brain: types, services, hooks, strings, tokens
frontend-web/           current web app, later render-only consumer
mobile/                 Expo app, render-only consumer
admin/                  admin app
docs/                   canonical decisions and audits
```

Important adaptation: this project will not immediately replace `frontend-web` with Next.js. The safer first step is to keep the current Vite app and extract shared logic into `packages/shared-core`.

## Future Folder Consolidation

After parity is complete and `frontend-web/` has been removed, consider one
structural cleanup: consolidate the client-side projects under a single
`frontend/` folder.

Potential future shape:

```txt
backend/
frontend/
  shared-core/
  web/
  mobile/
  admin/
docs/
bats/
```

This is cleaner for new templates and future projects because it separates the
Django source of truth from all client consumers. It also makes it clear that
`frontend/shared-core` is the shared client brain while `backend/` remains the
authoritative source of business rules, persistence, permissions, rewards and
content integrity.

Do not do this during the active parity migration. The current repo has many
path-sensitive references in package file links, TypeScript aliases, Next config,
BAT automation, package locks and architecture docs. Moving folders now would
add migration risk without improving product parity. Revisit only after:

- `frontend-web/` is deleted;
- `web/`, `mobile/` and `admin/` builds are stable;
- package locks can be regenerated intentionally;
- docs and BATs can be updated in one focused structural pass.

## Checkpoint Decision

We are preserving the current working product before starting the broad refactor.

From this point forward:

- New cross-platform domain contracts should start in `packages/shared-core`.
- Existing web code should be migrated gradually, not rewritten all at once.
- Mobile should be created only after the first Adventure contracts/services are in shared-core.
- Generated TTS audio, Piper models and local tool binaries must not be committed. They are local/dev artifacts and should be recreated by setup scripts when needed.

## Tailwind Status

The current `frontend-web` does use Tailwind:

- `frontend-web/tailwind.config.js` exists.
- `frontend-web/package.json` includes `tailwindcss`, `postcss` and `autoprefixer`.
- Many components use utility classes through `className`.

The target architecture says web should use CSS Modules + design tokens, not Tailwind. That is a large UI migration and should happen after shared-core extraction, otherwise we would be changing architecture and visual implementation at the same time.

## Migration Phases

### Phase 1 - Checkpoint and Guardrails

- Add this checkpoint document.
- Add generated TTS/media/tool folders to `.gitignore`.
- Scaffold `packages/shared-core` with the first domain contracts.
- Stage the current work in Git after excluding local generated artifacts.

### Phase 2 - Shared-Core Foundation

- Move stable API types into `packages/shared-core/src/types`.
- Move API client abstraction into `packages/shared-core/src/lib`.
- Move adventure service contracts into `packages/shared-core/src/services`.
- Add shared strings/tokens only after the service/type layer is stable.

### Phase 3 - Web Consumes Shared-Core

- Replace duplicated `frontend-web/src/types/*` imports with shared-core imports.
- Replace direct adventure service implementation with a web adapter around shared-core.
- Keep Tailwind during this phase to avoid mixing logic migration and visual migration.

### Phase 4 - Mobile MVP

- Create `mobile/` with Expo.
- Register storage and API adapters at boot.
- Build the first Adventure MVP: map, phase runner, section completion and inventory basics.

### Phase 5 - Render-Only + Design Alignment

- Audit web/mobile feature parity.
- Move domain hooks into shared-core.
- Gradually replace Tailwind-heavy web screens with CSS Modules and tokens.
- Record intentional web/mobile differences in a parity audit execution doc.

## First Shared-Core Scope

The first shared-core slice should include:

- Adventure types.
- Section types.
- Minimal study content types used by adventure.
- API client interface.
- Adventure service factory.

This is enough to start mobile without duplicating API contracts.
