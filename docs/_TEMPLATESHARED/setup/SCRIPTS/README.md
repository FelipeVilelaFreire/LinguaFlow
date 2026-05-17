# Automation Scripts

This folder mirrors HobbyMap's `bats/` convention.

- `setup.bat`: one-time setup for Conda, backend, shared-core, web, mobile, optional admin, and Windows Terminal startup.
- `dev.bat`: daily startup for Claude, backend, shared-core watch, web, mobile, and optional admin.

Keep these scripts inside `bats/`. Do not leave `setup.bat` or `dev.bat` at the project root.
