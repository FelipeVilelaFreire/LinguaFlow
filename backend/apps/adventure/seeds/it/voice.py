from copy import deepcopy


VOICE_PROFILES = {
    "Antonio il Contadino": {"lang": "it-IT", "gender": "male", "pitch": 0.86, "rate": 0.88},
    "Antonio": {"lang": "it-IT", "gender": "male", "pitch": 0.86, "rate": 0.88},
    "Nico": {"lang": "it-IT", "gender": "male", "pitch": 0.96, "rate": 0.96},
    "Giulia": {"lang": "it-IT", "gender": "female", "pitch": 1.1, "rate": 0.96},
    "Pietro": {"lang": "it-IT", "gender": "male", "pitch": 0.84, "rate": 0.88},
    "Il Mercante": {"lang": "it-IT", "gender": "male", "pitch": 0.94, "rate": 1.0},
    "La Guardia": {"lang": "it-IT", "gender": "male", "pitch": 0.78, "rate": 0.86},
    "Bianca": {"lang": "it-IT", "gender": "female", "pitch": 0.98, "rate": 0.9},
    "Chiara": {"lang": "it-IT", "gender": "female", "pitch": 1.15, "rate": 1.04},
    "Lucia": {"lang": "it-IT", "gender": "female", "pitch": 0.98, "rate": 0.9},
    "Donna Elena": {"lang": "it-IT", "gender": "female", "pitch": 0.92, "rate": 0.88},
    "Elena": {"lang": "it-IT", "gender": "female", "pitch": 0.92, "rate": 0.88},
    "Il Podesta": {"lang": "it-IT", "gender": "male", "pitch": 0.76, "rate": 0.82},
    "L'Ispettore": {"lang": "it-IT", "gender": "male", "pitch": 0.8, "rate": 0.94},
    "Mateusz l'Altro": {"lang": "pl-PL", "gender": "male", "pitch": 0.9, "rate": 0.92},
}

PACE_SPEECH_RATE = {"slow": 0.9, "normal": 1.0, "urgent": 1.3}


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

