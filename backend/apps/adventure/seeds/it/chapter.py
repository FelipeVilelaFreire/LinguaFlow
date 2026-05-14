from django.core.management.base import BaseCommand

from apps.adventure.models import AdventureCharacter, AdventureChapter, AdventureItem, AdventurePhase
from apps.learning.models import Language, Phrase, Scenario

from .content import (
    BOSS_REWARDS,
    CHARACTERS,
    CHEST_PHASES,
    CHEST_POOL,
    CHAPTER,
    DEGRADED,
    PHASE1_ITEMS,
    PHASES,
    PHRASES,
    SCENARIOS,
    SOURCE_LANGUAGE,
    TARGET_LANGUAGE,
)


class Command(BaseCommand):
    help = "Seed PT -> IT A1 T1 - Il Borgo"

    def handle(self, *args, **options):
        self.stdout.write("\nSeed PT -> IT A1 T1 - Il Borgo\n")

        source, _ = Language.objects.get_or_create(
            code=SOURCE_LANGUAGE["code"],
            defaults={"name": SOURCE_LANGUAGE["name"], "is_ready": SOURCE_LANGUAGE["is_ready"]},
        )
        target, created = Language.objects.get_or_create(
            code=TARGET_LANGUAGE["code"],
            defaults={"name": TARGET_LANGUAGE["name"], "is_ready": TARGET_LANGUAGE["is_ready"]},
        )
        if not created:
            Language.objects.filter(code=TARGET_LANGUAGE["code"]).update(is_ready=True)

        scenario_objs = {}
        for slug, title, description in SCENARIOS:
            scenario, _ = Scenario.objects.get_or_create(slug=slug, defaults={"title": title, "description": description})
            scenario_objs[slug] = scenario

        for source_text, target_text, scenario_slug in PHRASES:
            Phrase.objects.get_or_create(
                source_language=source,
                target_language=target,
                source_text=source_text,
                target_text=target_text,
                defaults={"scenario": scenario_objs[scenario_slug], "difficulty": CHAPTER["level"]},
            )

        chapter, _ = AdventureChapter.objects.update_or_create(
            slug=CHAPTER["slug"],
            defaults={
                "language": target,
                "level": CHAPTER["level"],
                "order": CHAPTER["order"],
                "title": CHAPTER["title"],
                "subtitle": CHAPTER["subtitle"],
                "background": CHAPTER["background"],
                "boss_name": CHAPTER["boss_name"],
                "boss_intro": CHAPTER["boss_intro"],
                "reward_name": CHAPTER["reward_name"],
                "reward_description": CHAPTER["reward_description"],
            },
        )

        phase_map = {}
        for phase in PHASES:
            phase_obj, _ = AdventurePhase.objects.update_or_create(
                chapter=chapter,
                number=phase["number"],
                defaults={
                    "title": phase["title"],
                    "narrative_intro": f"{phase['title']} - Il Borgo continua a mesma narrativa em italiano.",
                    "narrative_outro": f"Voce sai com: {', '.join(word for _, word in phase['new'])}.",
                    "key_words": phase["key_words"],
                    "scenario_slug": phase["scenario_slug"],
                    "phrase_count": phase["phrase_count"],
                    "phase_type": phase["phase_type"],
                },
            )
            phase_map[phase["number"]] = phase_obj

        char_map = {}
        for slug, name, role, emoji, ctype, lang_bridge, first_phase_num, order, description, quote in CHARACTERS:
            char, _ = AdventureCharacter.objects.update_or_create(
                chapter=chapter,
                slug=slug,
                defaults={
                    "name": name,
                    "role": role,
                    "emoji": emoji,
                    "character_type": ctype,
                    "description": description,
                    "quote": quote,
                    "lang_bridge": lang_bridge,
                    "first_phase": phase_map[first_phase_num],
                    "order": order,
                },
            )
            char_map[slug] = char

        for item in PHASE1_ITEMS:
            AdventureItem.objects.update_or_create(
                chapter=chapter,
                slug=item["slug"],
                defaults={
                    "emoji": item["emoji"],
                    "name": item["name"],
                    "lore": item["lore"],
                    "rarity": AdventureItem.RARITY_COMUM,
                    "action": item["action"],
                    "word_id": item["word_id"],
                    "item_tag": item["item_tag"],
                    "source_phase": phase_map[1],
                    "source_character": char_map.get(item["source_character_slug"]) if item["source_character_slug"] else None,
                    "order": item["order"],
                },
            )

        for item in CHEST_POOL:
            AdventureItem.objects.update_or_create(
                chapter=chapter,
                slug=item["slug"],
                defaults={
                    "emoji": item["emoji"],
                    "name": item["name"],
                    "lore": item["lore"],
                    "rarity": item["rarity"],
                    "action": AdventureItem.ACTION_EXAMINAR,
                    "word_id": "",
                    "item_tag": item["tag"],
                },
            )

        for item in DEGRADED:
            full_item = AdventureItem.objects.filter(chapter=chapter, slug=item["of"]).first()
            if not full_item:
                continue
            AdventureItem.objects.update_or_create(
                chapter=chapter,
                slug=item["slug"],
                defaults={
                    "emoji": item["emoji"],
                    "name": item["name"],
                    "lore": item["lore"],
                    "rarity": AdventureItem.RARITY_COMUM,
                    "action": AdventureItem.ACTION_USAR,
                    "word_id": full_item.word_id,
                    "item_tag": full_item.item_tag,
                    "is_degraded": True,
                    "degrades_to": full_item,
                },
            )

        for phase_number, tier in CHEST_PHASES.items():
            phase = phase_map.get(phase_number)
            if phase:
                phase.has_chest = True
                phase.chest_tier = tier
                phase.save(update_fields=["has_chest", "chest_tier"])

        for item in BOSS_REWARDS:
            AdventureItem.objects.update_or_create(
                chapter=chapter,
                slug=item["slug"],
                defaults={
                    "emoji": item["emoji"],
                    "name": item["name"],
                    "lore": item["lore"],
                    "rarity": item["rarity"],
                    "action": item["action"],
                    "item_tag": item["item_tag"],
                    "word_id": item["word_id"],
                    "source_phase": phase_map[25],
                    "order": item["order"],
                },
            )

        self.stdout.write(self.style.SUCCESS(f"\nSeed IT completo: {len(PHASES)} fases\n"))
