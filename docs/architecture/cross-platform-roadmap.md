# Cross-Platform Roadmap Checkpoint

Checkpoint date: 2026-05-17

This document records the current checkpoint before the larger architecture shift toward the `_TEMPLATESHARED` model.

## Current State

The project currently has:

- `backend/`: Django + DRF, already split by domain apps.
- `frontend-web/`: Vite + React 18 + Tailwind CSS.
- `frontend-admin/`: separate admin frontend.
- `docs/`: product, content, design, architecture and feature docs.
- `docs/_TEMPLATESHARED/`: target architecture template for shared web/mobile projects.

The backend is close to the target architecture. The frontend is not: it still keeps types, services, hooks, strings and render logic inside `frontend-web`.

## Target Architecture

The target is to move toward the `_TEMPLATESHARED` shape:

```txt
backend/                source of truth
packages/shared-core/   shared brain: types, services, hooks, strings, tokens
frontend-web/           current web app, later render-only consumer
mobile/                 Expo app, render-only consumer
frontend-admin/         admin app
docs/                   canonical decisions and audits
```

Important adaptation: this project will not immediately replace `frontend-web` with Next.js. The safer first step is to keep the current Vite app and extract shared logic into `packages/shared-core`.

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

The template target says web should use CSS Modules + design tokens, not Tailwind. That is a large UI migration and should happen after shared-core extraction, otherwise we would be changing architecture and visual implementation at the same time.

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
