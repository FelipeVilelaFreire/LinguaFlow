from copy import deepcopy


VOICE_PROFILES = {
    "Don Miguel": {
        "lang": "es-ES",
        "gender": "male",
        "pitch": 0.85,
        "rate": 0.88,
    },
    "Miguel": {
        "lang": "es-ES",
        "gender": "male",
        "pitch": 0.95,
        "rate": 0.95,
    },
    "Rosa": {
        "lang": "es-ES",
        "gender": "female",
        "pitch": 1.12,
        "rate": 0.95,
    },
    "Rosa la Panadera": {
        "lang": "es-ES",
        "gender": "female",
        "pitch": 1.1,
        "rate": 0.95,
    },
    "Carmen": {
        "lang": "es-ES",
        "gender": "female",
        "pitch": 0.95,
        "rate": 0.88,
    },
    "SeÃƒÂ±ora Carmen": {
        "lang": "es-ES",
        "gender": "female",
        "pitch": 0.95,
        "rate": 0.88,
    },
    "El Vigilante": {
        "lang": "es-ES",
        "gender": "male",
        "pitch": 0.8,
        "rate": 0.85,
    },
    "El Vigilante del Mercado": {
        "lang": "es-ES",
        "gender": "male",
        "pitch": 0.8,
        "rate": 0.85,
    },
    "Sofía": {
        "lang": "es-ES",
        "gender": "female",
        "pitch": 1.18,
        "rate": 1.05,
    },
    "Sofia": {
        "lang": "es-ES",
        "gender": "female",
        "pitch": 1.18,
        "rate": 1.05,
    },
    "María": {
        "lang": "es-ES",
        "gender": "female",
        "pitch": 1.0,
        "rate": 0.92,
    },
    "Maria": {
        "lang": "es-ES",
        "gender": "female",
        "pitch": 1.0,
        "rate": 0.92,
    },
    "El Alcalde": {
        "lang": "es-ES",
        "gender": "male",
        "pitch": 0.78,
        "rate": 0.82,
    },
    "Alcalde": {
        "lang": "es-ES",
        "gender": "male",
        "pitch": 0.78,
        "rate": 0.82,
    },
    "Doña Lucía": {
        "lang": "es-ES",
        "gender": "female",
        "pitch": 0.92,
        "rate": 0.85,
    },
    "Eduardo": {
        "lang": "es-ES",
        "gender": "male",
        "pitch": 0.88,
        "rate": 0.9,
    },
    "El Inspector": {
        "lang": "es-ES",
        "gender": "male",
        "pitch": 0.82,
        "rate": 0.95,
    },
    "Inspector": {
        "lang": "es-ES",
        "gender": "male",
        "pitch": 0.82,
        "rate": 0.95,
    },
}

PACE_SPEECH_RATE = {
    "slow": 0.9,
    "normal": 1.0,
    "urgent": 1.3,
}


def hydrate_section_content(content):
    hydrated = deepcopy(content)

    def hydrate_step(step):
        npc = step.get("npc")
        if not npc:
            return

        voice = VOICE_PROFILES.get(npc)
        if voice:
            step.setdefault("voice", voice)

        if "speech_rate" not in step and step.get("pace") in PACE_SPEECH_RATE:
            step["speech_rate"] = PACE_SPEECH_RATE[step["pace"]]

    for beat in hydrated.get("beats", []):
        if beat.get("kind") == "npc":
            hydrate_step(beat)

    for step in hydrated.get("steps", []):
        if step.get("kind") == "npc_speak":
            hydrate_step(step)

    for step in hydrated.get("exercises", []):
        if step.get("kind") == "npc_speak":
            hydrate_step(step)

    return hydrated
