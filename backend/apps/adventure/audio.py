from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from copy import deepcopy
from pathlib import Path
from shutil import move
from typing import Any, Iterable

from django.conf import settings
from django.utils.text import slugify

from apps.adventure.voice_config import character_voice_key


AUDIO_VERSION = "v1"
AUDIO_EXT = "wav"


def adventure_tts_enabled() -> bool:
    return bool(getattr(settings, "ADVENTURE_TTS_ENABLED", False))


def audio_root() -> Path:
    return Path(settings.MEDIA_ROOT) / "adventure" / "voice"


def voice_profile_for(language_code: str, npc: str | None) -> dict[str, Any]:
    if not npc:
        return {}

    if language_code.upper() == "ES":
        try:
            from apps.adventure.seeds.es.voice import VOICE_PROFILES

            return dict(VOICE_PROFILES.get(npc) or {})
        except Exception:
            return {}

    return {}


def audio_identity(
    *,
    language_code: str,
    npc: str | None,
    text: str,
    pace: str | None = None,
    speech_rate: float | None = None,
    voice: dict[str, Any] | None = None,
) -> dict[str, Any]:
    profile = {**voice_profile_for(language_code, npc), **(voice or {})}
    return {
        "version": AUDIO_VERSION,
        "language": language_code.upper(),
        "npc": npc or "narrator",
        "voice_key": character_voice_key(npc),
        "text": text,
        "pace": pace or "",
        "speech_rate": speech_rate,
        "voice": profile,
    }


def audio_digest(identity: dict[str, Any]) -> str:
    raw = json.dumps(identity, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:20]


def audio_relative_path(identity: dict[str, Any]) -> str:
    language = slugify(identity["language"].lower()) or "xx"
    npc = slugify(identity["npc"]) or "npc"
    return f"adventure/voice/{language}/{npc}/{audio_digest(identity)}.{AUDIO_EXT}"


def audio_file_path(identity: dict[str, Any]) -> Path:
    return Path(settings.MEDIA_ROOT) / audio_relative_path(identity)


def audio_url_for(identity: dict[str, Any], request=None) -> str | None:
    rel = audio_relative_path(identity).replace("\\", "/")
    path = Path(settings.MEDIA_ROOT) / rel
    if not path.exists():
        return None

    url = f"{settings.MEDIA_URL.rstrip('/')}/{rel}"
    if request is not None:
        return request.build_absolute_uri(url)
    return url


def iter_voice_targets(content: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for bucket in ("beats", "steps", "exercises"):
        for step in content.get(bucket, []):
            if not isinstance(step, dict):
                continue

            kind = step.get("kind")
            if kind in {"npc", "npc_speak"} and step.get("line"):
                yield {
                    "container": step,
                    "field": "line",
                    "audio_field": "audio_url",
                    "npc": step.get("npc"),
                    "text": step.get("line"),
                    "pace": step.get("pace"),
                    "speech_rate": step.get("speech_rate"),
                    "voice": step.get("voice"),
                }

            if kind == "multiple_choice" and step.get("npc_reaction"):
                yield {
                    "container": step,
                    "field": "npc_reaction",
                    "audio_field": "npc_reaction_audio_url",
                    "npc": step.get("npc"),
                    "text": step.get("npc_reaction"),
                    "pace": step.get("pace"),
                    "speech_rate": step.get("speech_rate"),
                    "voice": step.get("voice"),
                }

            if kind == "item_moment":
                if step.get("npc_line"):
                    yield {
                        "container": step,
                        "field": "npc_line",
                        "audio_field": "npc_line_audio_url",
                        "npc": step.get("npc"),
                        "text": step.get("npc_line"),
                        "pace": step.get("pace"),
                        "speech_rate": step.get("speech_rate"),
                        "voice": step.get("voice"),
                    }
                for reaction_key, audio_key in (
                    ("on_use", "npc_reaction_audio_url"),
                    ("on_skip", "npc_reaction_audio_url"),
                ):
                    payload = step.get(reaction_key)
                    if isinstance(payload, dict) and payload.get("npc_reaction"):
                        yield {
                            "container": payload,
                            "field": "npc_reaction",
                            "audio_field": audio_key,
                            "npc": step.get("npc"),
                            "text": payload.get("npc_reaction"),
                            "pace": step.get("pace"),
                            "speech_rate": step.get("speech_rate"),
                            "voice": step.get("voice"),
                        }


def content_with_audio_urls(content: dict[str, Any], *, language_code: str, request=None) -> dict[str, Any]:
    hydrated = deepcopy(content)
    if not adventure_tts_enabled():
        return hydrated

    for target in iter_voice_targets(hydrated):
        identity = audio_identity(
            language_code=language_code,
            npc=target["npc"],
            text=target["text"],
            pace=target["pace"],
            speech_rate=target["speech_rate"],
            voice=target["voice"],
        )
        url = audio_url_for(identity, request=request)
        if url:
            target["container"][target["audio_field"]] = url

    return hydrated


def synthesize_with_piper(
    *,
    text: str,
    output_path: Path,
    model_path: str,
    piper_exe: str,
    length_scale: float | None = None,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        temp_output = Path(tmp.name)

    command = [piper_exe, "--model", model_path, "--output_file", str(temp_output)]
    if length_scale:
        command.extend(["--length_scale", str(length_scale)])
    try:
        subprocess.run(command, input=text, text=True, check=True, encoding="utf-8")
        move(str(temp_output), str(output_path))
    finally:
        if temp_output.exists():
            temp_output.unlink()
