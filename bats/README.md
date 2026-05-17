# Local Automation

Use these scripts from the repository root.

```bat
bats\setup.bat
bats\dev.bat
```

`setup.bat` is the one-time dependency/setup flow.

`dev.bat` opens local development panes for backend, shared-core, web and mobile.

The legacy `frontend-web/` app remains available during migration, but the target template app is `web/`.
