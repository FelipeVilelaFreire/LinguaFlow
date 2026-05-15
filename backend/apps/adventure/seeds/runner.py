from importlib import import_module

from django.core.management.base import CommandError

from apps.adventure.models import AdventureChapter, AdventurePhase, PhaseSection


def seed_phase_sections(
    stdout,
    style,
    *,
    chapter_slug,
    phase_number,
    sections,
    hydrate_section_content,
    reset=False,
    step_targets=None,
):
    try:
        chapter = AdventureChapter.objects.get(slug=chapter_slug)
    except AdventureChapter.DoesNotExist as exc:
        raise CommandError(
            f"Chapter '{chapter_slug}' nao encontrado. Rode o seed do chapter primeiro."
        ) from exc

    try:
        phase = AdventurePhase.objects.get(chapter=chapter, number=phase_number)
    except AdventurePhase.DoesNotExist as exc:
        raise CommandError(
            f"Fase {phase_number} do chapter '{chapter_slug}' nao encontrada. "
            "Rode o seed do chapter primeiro."
        ) from exc

    existing = PhaseSection.objects.filter(phase=phase).count()
    if existing and not reset:
        stdout.write(
            style.WARNING(
                f"  Fase {phase_number} ja tem {existing} secoes. Use --reset para recriar."
            )
        )
        return 0

    if reset:
        deleted, _ = PhaseSection.objects.filter(phase=phase).delete()
        stdout.write(f"  - Fase {phase_number}: {deleted} secoes apagadas")

    created_count = 0
    for section in sections:
        content = hydrate_section_content(section["content"])
        if step_targets:
            content = _limit_section_content(
                content,
                max_steps=step_targets.get(section["section_type"]),
            )
        PhaseSection.objects.create(
            phase=phase,
            section_number=section["section_number"],
            section_type=section["section_type"],
            content=content,
        )
        created_count += 1

    stdout.write(f"  - Fase {phase_number}: {created_count} secoes criadas")
    return created_count


def _limit_section_content(content, *, max_steps):
    if not max_steps:
        return content
    limited = dict(content)
    for key in ("steps", "beats"):
        entries = limited.get(key)
        if not isinstance(entries, list) or len(entries) <= max_steps:
            continue
        if max_steps <= 1:
            limited[key] = entries[:max_steps]
        else:
            limited[key] = entries[: max_steps - 1] + [entries[-1]]
    return limited


def seed_language_sections(stdout, style, *, lang_code, chapter_slug, phases, reset=False, step_targets=None):
    voice_module = import_module(f"apps.adventure.seeds.{lang_code}.voice")
    total = 0
    for phase_number in phases:
        module = import_module(f"apps.adventure.seeds.{lang_code}.phases.f{phase_number:02d}")
        total += seed_phase_sections(
            stdout,
            style,
            chapter_slug=chapter_slug,
            phase_number=phase_number,
            sections=module.SECTIONS,
            hydrate_section_content=voice_module.hydrate_section_content,
            reset=reset,
            step_targets=step_targets,
        )
    return total
