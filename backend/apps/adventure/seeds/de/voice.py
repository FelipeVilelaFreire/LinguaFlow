from copy import deepcopy


VOICE_PROFILES = {
    "Elias der Bauer": {"lang": "de-DE", "gender": "male", "pitch": 0.86, "rate": 0.88},
    "Elias": {"lang": "de-DE", "gender": "male", "pitch": 0.86, "rate": 0.88},
    "Otto": {"lang": "de-DE", "gender": "male", "pitch": 0.96, "rate": 0.96},
    "Hanna die Baeckerin": {"lang": "de-DE", "gender": "female", "pitch": 1.1, "rate": 0.96},
    "Hanna": {"lang": "de-DE", "gender": "female", "pitch": 1.1, "rate": 0.96},
    "Friedrich": {"lang": "de-DE", "gender": "male", "pitch": 0.82, "rate": 0.86},
    "Der Markthaendler": {"lang": "de-DE", "gender": "male", "pitch": 0.94, "rate": 1.0},
    "Der Waechter": {"lang": "de-DE", "gender": "male", "pitch": 0.78, "rate": 0.86},
    "Greta": {"lang": "de-DE", "gender": "female", "pitch": 0.98, "rate": 0.9},
    "Lina": {"lang": "de-DE", "gender": "female", "pitch": 1.16, "rate": 1.04},
    "Marta die Heilerin": {"lang": "de-DE", "gender": "female", "pitch": 0.98, "rate": 0.9},
    "Marta": {"lang": "de-DE", "gender": "female", "pitch": 0.98, "rate": 0.9},
    "Klara": {"lang": "de-DE", "gender": "female", "pitch": 0.92, "rate": 0.88},
    "Der Vogt": {"lang": "de-DE", "gender": "male", "pitch": 0.76, "rate": 0.82},
    "Der Inspektor": {"lang": "de-DE", "gender": "male", "pitch": 0.8, "rate": 0.94},
    "Joao der Andere": {"lang": "pt-PT", "gender": "male", "pitch": 0.9, "rate": 0.92},
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
