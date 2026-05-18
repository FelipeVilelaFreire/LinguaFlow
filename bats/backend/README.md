# Backend Automation

Run these scripts from the repository root or by double-clicking them on Windows.

```bat
bats\backend\setup.bat
bats\backend\migrations.bat
bats\backend\tts.bat
```

- `setup.bat`: interactive backend setup for ES, IT, DE, or all seeds.
- `migrations.bat`: runs Django migrations without seeds.
- `tts.bat`: optional dev/lab setup for Adventure Piper TTS.

Do not recreate `backend\bats`; `bats\` is the single automation root.
