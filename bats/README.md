# Local Automation

Use these scripts from the repository root.

```bat
bats\setup.bat
bats\dev.bat
```

`setup.bat` is the one-time setup-from-zero flow based on this repository's current architecture:

- creates/uses the `linguaflow` Conda env
- installs backend requirements and runs Django migrations
- installs and builds `packages\shared-core`
- installs the new `web` Next app
- installs the new `mobile` Expo app
- installs and builds the new `admin` app
- runs `python manage.py check`, `makemigrations`, and `migrate`
- optionally opens `bats\backend\setup.bat` to seed ES/IT/DE
- installs `frontend-web` only as the temporary legacy app for QA comparison

Backend-specific helpers live under `bats\backend\`:

```bat
bats\backend\setup.bat
bats\backend\migrations.bat
bats\backend\tts.bat
```

Do not add new automation under `backend\bats`; `bats\` is the single automation root.

`dev.bat` opens a menu so you can choose exactly what to run. It launches the selected services in Windows Terminal using one tab per service:

- `1`: Web - backend + web
- `2`: Mobile - backend + mobile
- `3`: Admin - backend + admin
- `4`: Web + Mobile - backend + web + mobile
- `5`: Web + Admin - backend + web + admin
- `6`: Mobile + Admin - backend + mobile + admin
- `7`: Web + Mobile + Admin - backend + web + mobile + admin
- `8`: Everything with legacy - backend + web + mobile + admin + frontend-web
- `9`: Backend only

The legacy `frontend-web/` app remains available during migration QA, but the target apps are `web/`, `mobile/`, and `admin/`.
