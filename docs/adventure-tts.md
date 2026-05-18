# Adventure TTS Cache

The adventure can use generated audio files when they exist, while keeping the
browser Web Speech voice as fallback.

## Runtime

For normal product validation, keep cached/generated audio disabled and use the
browser voice:

```env
ADVENTURE_TTS_ENABLED=false
```

The Piper setup is kept as a dev/lab path for testing future character voices.

When enabled, the API adds `audio_url` fields for cached files under:

```txt
backend/media/adventure/voice/<lang>/<character>/<hash>.wav
```

If a file is missing, the frontend uses the existing browser TTS.

## Piper Setup

On Windows, the easiest local setup is:

```bat
bats\backend\tts.bat
```

The main interactive setup also offers this when you choose ES:

```bat
bats\backend\setup.bat
```

That script downloads Piper and voices to the local user cache under
`%USERPROFILE%\.codex\memories\linguaflow-tts`, writes `backend\.env`, and can
generate the WAV cache at the end. Old local copies under `backend\tools`,
`backend\tts_models`, and `backend\media` are generated artifacts, not source
code.

Configure Piper and at least one voice model:

```env
ADVENTURE_TTS_ENABLED=1
ADVENTURE_TTS_PROVIDER=piper
ADVENTURE_TTS_PIPER_EXE=piper
ADVENTURE_TTS_PIPER_DEFAULT_MODEL=C:\tts\voices\es_default.onnx
```

Optional per-character models:

```env
ADVENTURE_TTS_PIPER_MODEL_DON_MIGUEL=C:\tts\voices\es_old_male.onnx
ADVENTURE_TTS_PIPER_MODEL_MIGUEL=C:\tts\voices\es_young_male.onnx
ADVENTURE_TTS_PIPER_MODEL_ROSA=C:\tts\voices\es_female_1.onnx
ADVENTURE_TTS_PIPER_MODEL_CARMEN=C:\tts\voices\es_female_old.onnx
ADVENTURE_TTS_PIPER_MODEL_SOFIA=C:\tts\voices\es_female_young.onnx
ADVENTURE_TTS_PIPER_MODEL_MARIA=C:\tts\voices\es_female_calm.onnx
ADVENTURE_TTS_PIPER_MODEL_ALCALDE=C:\tts\voices\es_authority_male.onnx
ADVENTURE_TTS_PIPER_MODEL_VIGILANTE=C:\tts\voices\es_guard_male.onnx
ADVENTURE_TTS_PIPER_MODEL_INSPECTOR=C:\tts\voices\es_official_male.onnx
```

List the configured voice slots:

```bash
py manage.py generate_adventure_audio --lang ES --voices
```

Preview cache paths without generating audio:

```bash
py manage.py generate_adventure_audio --lang ES --phase 1 --provider manifest --dry-run
```

Generate audio:

```bash
py manage.py generate_adventure_audio --lang ES --provider piper
```

Regenerate after changing a model or seed text:

```bash
py manage.py generate_adventure_audio --lang ES --provider piper --overwrite
```

## Deployment

Generated audio files are static media. In production, keep `backend/media` on a
persistent disk or upload the generated `adventure/voice` folder to object
storage/CDN. Users do not call the TTS engine; they only download audio files.
