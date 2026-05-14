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
        PhaseSection.objects.create(
            phase=phase,
            section_number=section["section_number"],
            section_type=section["section_type"],
            content=hydrate_section_content(section["content"]),
        )
        created_count += 1

    stdout.write(f"  - Fase {phase_number}: {created_count} secoes criadas")
    return created_count


def seed_language_sections(stdout, style, *, lang_code, chapter_slug, phases, reset=False):
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
        )
    return total
