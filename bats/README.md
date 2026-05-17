# Local Automation

Use these scripts from the repository root.

```bat
bats\setup.bat
bats\dev.bat
```

`setup.bat` is the one-time setup-from-zero flow based on `docs\_TEMPLATESHARED`:

- creates/uses the `linguaflow` Conda env
- installs backend requirements and runs Django migrations
- installs and builds `packages\shared-core`
- installs the new `web` Next app
- installs the new `mobile` Expo app
- installs `frontend-web` only as the temporary legacy app during migration

`dev.bat` opens local development panes for backend, shared-core, web and mobile.

The legacy `frontend-web/` app remains available during migration, but the target template app is `web/`.
