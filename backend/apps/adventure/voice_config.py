from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from django.conf import settings
from django.utils.text import slugify


@dataclass(frozen=True)
class CharacterVoice:
    key: str
    display_name: str
    description: str
    env_name: str
    fallback_key: str | None = None


ES_CHARACTER_VOICES: dict[str, CharacterVoice] = {
    "don-miguel": CharacterVoice(
        key="don-miguel",
        display_name="Don Miguel",
        description="Older calm male voice; slow, grounded guide.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_DON_MIGUEL",
    ),
    "miguel": CharacterVoice(
        key="miguel",
        display_name="Miguel",
        description="Young warm male voice; friendly bridge character.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_MIGUEL",
    ),
    "rosa": CharacterVoice(
        key="rosa",
        display_name="Rosa",
        description="Adult female voice; expressive market/panadera energy.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_ROSA",
    ),
    "carmen": CharacterVoice(
        key="carmen",
        display_name="Carmen",
        description="Calm older female voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_CARMEN",
    ),
    "sofia": CharacterVoice(
        key="sofia",
        display_name="Sofia",
        description="Young female voice; alert and emotional.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_SOFIA",
    ),
    "maria": CharacterVoice(
        key="maria",
        display_name="Maria",
        description="Adult female voice; controlled, healer-like tone.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_MARIA",
    ),
    "el-alcalde": CharacterVoice(
        key="el-alcalde",
        display_name="El Alcalde",
        description="Older authoritative male voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_ALCALDE",
    ),
    "el-vigilante": CharacterVoice(
        key="el-vigilante",
        display_name="El Vigilante",
        description="Male guard voice; tense and direct.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_VIGILANTE",
    ),
    "el-inspector": CharacterVoice(
        key="el-inspector",
        display_name="El Inspector",
        description="Male official voice; controlled pressure.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_INSPECTOR",
    ),
    "dona-esperanza": CharacterVoice(
        key="dona-esperanza",
        display_name="Doña Esperanza",
        description="Older female village voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_ESPERANZA",
    ),
    "pablo": CharacterVoice(
        key="pablo",
        display_name="Pablo",
        description="Male cook voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_PABLO",
    ),
    "ernesto": CharacterVoice(
        key="ernesto",
        display_name="Ernesto",
        description="Older male field voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_ERNESTO",
    ),
    "el-mercader": CharacterVoice(
        key="el-mercader",
        display_name="El Mercader",
        description="Male market voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_MERCADER",
    ),
    "elena": CharacterVoice(
        key="elena",
        display_name="Elena",
        description="Female healer voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_ELENA",
    ),
    "pedro": CharacterVoice(
        key="pedro",
        display_name="Pedro",
        description="Male blacksmith voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_PEDRO",
    ),
    "carlos": CharacterVoice(
        key="carlos",
        display_name="Carlos",
        description="Young male voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_CARLOS",
    ),
    "jefe-pueblo": CharacterVoice(
        key="jefe-pueblo",
        display_name="El Jefe del Pueblo",
        description="Older authority voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_JEFE_PUEBLO",
    ),
    "dona-lucia": CharacterVoice(
        key="dona-lucia",
        display_name="Doña Lucía",
        description="Older female family voice.",
        env_name="ADVENTURE_TTS_PIPER_MODEL_LUCIA",
    ),
}

NPC_ALIASES = {
    "don-miguel-el-campesino": "don-miguel",
    "miguel-el-campesino": "miguel",
    "dona-esperanza": "dona-esperanza",
    "pablo-el-cocinero": "pablo",
    "el-mercader": "el-mercader",
    "elena-la-curandera": "elena",
    "pedro-el-herrero": "pedro",
    "el-nino-carlos": "carlos",
    "el-niño-carlos": "carlos",
    "el-jefe-del-pueblo": "jefe-pueblo",
    "dona-lucia": "dona-lucia",
    "rosa-la-vendedora": "rosa",
    "senora-carmen": "carmen",
    "vigilante": "el-vigilante",
    "rosa-la-panadera": "rosa",
    "sofia": "sofia",
    "sofía": "sofia",
    "maria": "maria",
    "maría": "maria",
    "alcalde": "el-alcalde",
    "inspector": "el-inspector",
    "el-vigilante-del-mercado": "el-vigilante",
}


def character_voice_key(npc: str | None) -> str:
    if not npc:
        return "default"
    key = slugify(npc) or "default"
    return NPC_ALIASES.get(key, key)


def character_voice_for(npc: str | None, language_code: str = "ES") -> CharacterVoice | None:
    if language_code.upper() != "ES":
        return None
    return ES_CHARACTER_VOICES.get(character_voice_key(npc))


def resolve_model_path(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""
    path = Path(value)
    if path.is_absolute():
        return str(path)
    return str(Path(settings.BASE_DIR) / path)


def piper_model_for(npc: str | None, language_code: str = "ES", override: str | None = None) -> tuple[str, str]:
    if override:
        return resolve_model_path(override), "command override"

    character_voice = character_voice_for(npc, language_code)
    if character_voice:
        value = os.environ.get(character_voice.env_name, "").strip()
        if value:
            return resolve_model_path(value), character_voice.env_name

    default_model = getattr(settings, "ADVENTURE_TTS_PIPER_DEFAULT_MODEL", "")
    if default_model:
        return resolve_model_path(default_model), "ADVENTURE_TTS_PIPER_DEFAULT_MODEL"

    return "", character_voice.env_name if character_voice else "ADVENTURE_TTS_PIPER_DEFAULT_MODEL"


def configured_voice_rows(language_code: str = "ES") -> list[dict[str, str]]:
    if language_code.upper() != "ES":
        return []
    rows = []
    for voice in ES_CHARACTER_VOICES.values():
        model = resolve_model_path(os.environ.get(voice.env_name, "").strip())
        rows.append({
            "key": voice.key,
            "name": voice.display_name,
            "env": voice.env_name,
            "model": model,
            "description": voice.description,
        })
    return rows
