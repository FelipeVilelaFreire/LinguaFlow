from __future__ import annotations

from typing import Any

from apps.learning.models import Language, Lesson, Phrase, Scenario, StudyDay, StudyModule


SCENARIO_GROUPS = [
    ("social", "food"),
    ("place", "market"),
    ("health", "work"),
    ("memory",),
    ("trial",),
]

SCENARIO_HINTS = {
    "social": ("social", "sociale"),
    "food": ("cibo", "essen", "food"),
    "place": ("luoghi", "orte", "places"),
    "market": ("mercato", "markt", "market"),
    "health": ("salute", "gesundheit", "health"),
    "work": ("lavoro", "arbeit", "work"),
    "memory": ("memoria", "geschichte", "memory"),
    "trial": ("prova", "pruefung", "trial"),
}

MODULE_TITLES = {
    "IT": [
        "Primi Passi",
        "Orientamento e Mercato",
        "Cura e Mestieri",
        "Memoria e Segreti",
        "Giudizio e Sfida",
    ],
    "DE": [
        "First Steps",
        "Orientation and Market",
        "Care and Work",
        "Memory and Secrets",
        "Judgment and Challenge",
    ],
}


def seed_study_from_adventure(
    *,
    stdout,
    source_language: dict[str, Any],
    target_language: dict[str, Any],
    chapter: dict[str, Any],
    scenarios: list[tuple[str, str, str]],
    phrases: list[tuple[str, str, str]],
    phases: list[dict[str, Any]],
) -> dict[str, int]:
    source = _get_or_create_language(source_language)
    target = _get_or_create_language(target_language)
    lang_code = target.code
    scenario_meta = _build_scenario_meta(scenarios, phases)
    modules = _seed_modules(lang_code, scenario_meta)

    scenario_objs = {}
    for order, (slug, title, description) in enumerate(scenarios, start=1):
        meta = scenario_meta[slug]
        module = modules[meta["group_index"]]
        scenario, _ = Scenario.objects.update_or_create(
            slug=slug,
            defaults={
                "title": title,
                "description": description,
                "module": module,
                "adventure_phase": meta["first_phase"],
                "order": order,
            },
        )
        scenario_objs[slug] = scenario

    phrase_total = _seed_phrases(source, target, chapter, phrases, scenario_objs)
    created_days = _seed_study_days(source, target, chapter, phases, scenario_objs)

    stdout.write(
        f"  Study {lang_code}: {len(modules)} modules, {len(scenario_objs)} scenarios, "
        f"{phrase_total} phrases, {len(phases)} canonical days ({created_days} new)."
    )
    return {
        "modules": len(modules),
        "scenarios": len(scenario_objs),
        "phrases": phrase_total,
        "days": len(phases),
        "created_days": created_days,
    }


def _get_or_create_language(data: dict[str, Any]) -> Language:
    language, created = Language.objects.get_or_create(
        code=data["code"],
        defaults={"name": data["name"], "is_ready": data.get("is_ready", False)},
    )
    if not created and data.get("is_ready"):
        Language.objects.filter(pk=language.pk).update(is_ready=True)
        language.is_ready = True
    return language


def _build_scenario_meta(
    scenarios: list[tuple[str, str, str]],
    phases: list[dict[str, Any]],
) -> dict[str, dict[str, int]]:
    first_phase_by_slug = {}
    for phase in sorted(phases, key=lambda item: item["number"]):
        first_phase_by_slug.setdefault(phase["scenario_slug"], phase["number"])

    meta = {}
    for order, (slug, _title, _description) in enumerate(scenarios, start=1):
        group_index = _group_index_for_slug(slug)
        meta[slug] = {
            "first_phase": first_phase_by_slug.get(slug, order),
            "group_index": group_index,
        }
    return meta


def _group_index_for_slug(slug: str) -> int:
    lowered = slug.lower()
    for group_index, group in enumerate(SCENARIO_GROUPS):
        for key in group:
            if any(hint in lowered for hint in SCENARIO_HINTS[key]):
                return group_index
    return len(SCENARIO_GROUPS) - 1


def _seed_modules(lang_code: str, scenario_meta: dict[str, dict[str, int]]) -> dict[int, StudyModule]:
    titles = MODULE_TITLES.get(lang_code, [f"{lang_code} Module {index}" for index in range(1, 6)])
    used_groups = sorted({meta["group_index"] for meta in scenario_meta.values()})
    modules = {}
    for index in used_groups:
        title = titles[index]
        module, _ = StudyModule.objects.update_or_create(
            lang_code=lang_code,
            title=title,
            defaults={"order": index + 1},
        )
        modules[index] = module
    return modules


def _seed_phrases(
    source: Language,
    target: Language,
    chapter: dict[str, Any],
    phrases: list[tuple[str, str, str]],
    scenario_objs: dict[str, Scenario],
) -> int:
    for source_text, target_text, scenario_slug in phrases:
        scenario = scenario_objs[scenario_slug]
        dupes = Phrase.objects.filter(
            source_language=source,
            target_language=target,
            source_text=source_text,
        )
        if dupes.count() > 1:
            dupes.exclude(pk=dupes.first().pk).delete()
        Phrase.objects.update_or_create(
            source_language=source,
            target_language=target,
            source_text=source_text,
            defaults={
                "target_text": target_text,
                "difficulty": chapter["level"],
                "scenario": scenario,
                "category": scenario.title,
            },
        )
    return len(phrases)


def _seed_study_days(
    source: Language,
    target: Language,
    chapter: dict[str, Any],
    phases: list[dict[str, Any]],
    scenario_objs: dict[str, Scenario],
) -> int:
    fallback_phrases = list(
        Phrase.objects.filter(
            source_language=source,
            target_language=target,
            difficulty=chapter["level"],
        )
        .select_related("scenario")
        .order_by("id")[:12]
    )
    StudyDay.objects.filter(
        is_active=True,
        lesson__phrases__source_language=source,
        lesson__phrases__target_language=target,
        lesson__phrases__difficulty=chapter["level"],
    ).update(is_active=False)

    created_days = 0
    for phase in phases:
        day_number = phase["number"]
        scenario = scenario_objs[phase["scenario_slug"]]
        lesson, _ = Lesson.objects.update_or_create(
            title=f"{_lesson_prefix(target.code, chapter)} Dia {day_number:02d}: {phase['title']}",
            defaults={
                "day_number": day_number,
                "scenario": scenario,
                "objective": _objective_for_phase(phase, target.name),
                "explanation": _explanation_for_phase(phase, scenario, target.name),
                "exercise_notes": _exercise_notes_for_phase(phase),
                "video_title": f"{_lesson_prefix(target.code, chapter)} - {phase['title']}",
                "video_url": "",
                "video_duration": "10 min",
            },
        )
        lesson.phrases.set(_phrases_for_phase(source, target, chapter, phase, scenario, fallback_phrases))

        day_dupes = StudyDay.objects.filter(day_number=day_number, lesson=lesson).order_by("id")
        if day_dupes.count() > 1:
            day_dupes.exclude(pk=day_dupes.first().pk).delete()
        _day, created = StudyDay.objects.update_or_create(
            day_number=day_number,
            lesson=lesson,
            defaults={"is_active": True},
        )
        created_days += 1 if created else 0

    return created_days


def _lesson_prefix(lang_code: str, chapter: dict[str, Any]) -> str:
    return f"{lang_code} {chapter['level']} T1"


def _phrases_for_phase(
    source: Language,
    target: Language,
    chapter: dict[str, Any],
    phase: dict[str, Any],
    scenario: Scenario,
    fallback_phrases: list[Phrase],
) -> list[Phrase]:
    phase_phrases = list(
        Phrase.objects.filter(
            source_language=source,
            target_language=target,
            difficulty=chapter["level"],
            scenario=scenario,
        ).order_by("id")[:12]
    )
    if len(phase_phrases) < 12:
        seen = {phrase.id for phrase in phase_phrases}
        phase_phrases.extend([phrase for phrase in fallback_phrases if phrase.id not in seen])
    return phase_phrases[:12]


def _objective_for_phase(phase: dict[str, Any], language_name: str) -> str:
    words = ", ".join(word for _native, word in phase.get("new", [])[:3])
    if words:
        return (
            f"Understand the same language core from adventure phase {phase['number']} "
            f"and practice it directly in {language_name}: {words}."
        )
    return f"Understand and practice the same language core from adventure phase {phase['number']} in {language_name}."


def _explanation_for_phase(phase: dict[str, Any], scenario: Scenario, language_name: str) -> str:
    focus = phase.get("focus") or scenario.description
    grammar = phase.get("grammar")
    key_words = ", ".join(phase.get("key_words") or [])
    new_words = ", ".join(f"{native} -> {target}" for native, target in phase.get("new", [])[:4])
    grammar_note = f" The grammar focus is {grammar}, kept practical and tied to the scene." if grammar else ""
    key_word_note = f" Key words to recognize: {key_words}." if key_words else ""
    new_word_note = f" New phrase anchors: {new_words}." if new_words else ""
    return (
        f"This study day mirrors adventure phase {phase['number']} without repeating the whole story. "
        f"The scenario is {scenario.title}, and the learning focus is {focus}. "
        f"Use this lesson to slow down what the adventure uses under pressure: first recognize the words, "
        f"then connect them to meaning, then answer with full reusable {language_name} phrases."
        f"{grammar_note}{key_word_note}{new_word_note}"
    )


def _exercise_notes_for_phase(phase: dict[str, Any]) -> list[str]:
    new_pairs = phase.get("new", [])[:3]
    anchor_note = "Copy the phrase anchors into memory before starting the faster exercises."
    if new_pairs:
        anchor_note = "Phrase anchors: " + "; ".join(f"{native} = {target}" for native, target in new_pairs) + "."

    notes = [
        anchor_note,
        "Read the target phrase, say what you think it means, then reveal the translation.",
        "Answer with the whole phrase when the exercise expects a sentence, not only the main word.",
        "Use mistakes as review: repeat the corrected answer once before moving on.",
    ]
    key_words = phase.get("key_words") or []
    if key_words:
        notes.append(f"End by repeating these key words aloud: {', '.join(key_words[:5])}.")
    return notes
