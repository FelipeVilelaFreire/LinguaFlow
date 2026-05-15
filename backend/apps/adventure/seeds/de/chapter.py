from django.core.management.base import BaseCommand

from apps.adventure.models import AdventureCharacter, AdventureChapter, AdventureItem, AdventurePhase, AdventureSkill
from apps.learning.models import Language, Phrase, Scenario

from apps.adventure.seeds.skills import seed_chapter_skills, sync_chapter_item_skills

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
    help = "Seed EN -> DE A1 T1 - Das Dorf, phases 1-25"

    def handle(self, *args, **options):
        self.stdout.write("\nSeed EN -> DE A1 T1 - Das Dorf\n")

        source, _ = Language.objects.get_or_create(
            code=SOURCE_LANGUAGE["code"],
            defaults={
                "name": SOURCE_LANGUAGE["name"],
                "is_ready": SOURCE_LANGUAGE["is_ready"],
            },
        )
        target, created = Language.objects.get_or_create(
            code=TARGET_LANGUAGE["code"],
            defaults={
                "name": TARGET_LANGUAGE["name"],
                "is_ready": TARGET_LANGUAGE["is_ready"],
            },
        )
        if not created:
            Language.objects.filter(code=TARGET_LANGUAGE["code"]).update(is_ready=True)
        self.stdout.write("  - Languages: EN, DE")

        scenario_objs = {}
        for slug, title, description in SCENARIOS:
            scenario, _ = Scenario.objects.get_or_create(
                slug=slug,
                defaults={"title": title, "description": description},
            )
            scenario_objs[slug] = scenario
        self.stdout.write(f"  - Scenarios: {len(scenario_objs)}")

        phrase_count = 0
        for source_text, target_text, scenario_slug in PHRASES:
            _, created = Phrase.objects.get_or_create(
                source_language=source,
                target_language=target,
                source_text=source_text,
                target_text=target_text,
                defaults={"scenario": scenario_objs[scenario_slug], "difficulty": CHAPTER["level"]},
            )
            if created:
                phrase_count += 1
        self.stdout.write(f"  - Phrases EN -> DE: {phrase_count} new ({len(PHRASES)} total)")

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
        self.stdout.write(f"  - Chapter: {chapter.slug}")

        skill_defs = [
            {"slug": "waffen", "name": "Waffen", "description": "Combat through tools and weapons.", "category": AdventureSkill.CATEGORY_COMBATE, "emoji": "W", "base_power": 12},
            {"slug": "versorgung", "name": "Versorgung", "description": "Food and survival resources.", "category": AdventureSkill.CATEGORY_SOBREVIVENCIA, "emoji": "F", "base_power": 10},
            {"slug": "wasser", "name": "Wasser", "description": "Water, thirst, and endurance.", "category": AdventureSkill.CATEGORY_SOBREVIVENCIA, "emoji": "A", "base_power": 10},
            {"slug": "heilung", "name": "Heilung", "description": "Remedies, herbs, and body protection.", "category": AdventureSkill.CATEGORY_SUPORTE, "emoji": "H", "base_power": 14},
            {"slug": "ueberzeugung", "name": "Ueberzeugung", "description": "Coins, documents, and social authority.", "category": AdventureSkill.CATEGORY_SOCIAL, "emoji": "P", "base_power": 12},
            {"slug": "ermittlung", "name": "Ermittlung", "description": "Clues, maps, letters, and memory.", "category": AdventureSkill.CATEGORY_INVESTIGACAO, "emoji": "I", "base_power": 12},
        ]
        skills = seed_chapter_skills(chapter, skill_defs)

        def sync_item_skills():
            sync_chapter_item_skills(chapter, skills, skill_defs)

        phase_map = {}
        for phase in PHASES:
            phase_obj, _ = AdventurePhase.objects.update_or_create(
                chapter=chapter,
                number=phase["number"],
                defaults={
                    "title": phase["title"],
                    "narrative_intro": (
                        f"{phase['title']}. The village pulls you through the same old mystery, "
                        f"but now every clue is carried in German. Focus: {phase['focus']}."
                    ),
                    "narrative_outro": (
                        f"You leave this moment with {', '.join(word for _, word in phase['new'])}. "
                        "The northern road is still waiting."
                    ),
                    "key_words": phase["key_words"],
                    "scenario_slug": phase["scenario_slug"],
                    "phrase_count": phase["phrase_count"],
                    "phase_type": phase["phase_type"],
                },
            )
            phase_map[phase["number"]] = phase_obj
        self.stdout.write(f"  - Phases: {len(PHASES)}")

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
        self.stdout.write(f"  - Characters: {len(CHARACTERS)}")

        created_items = 0
        for item in PHASE1_ITEMS:
            source_character = char_map.get(item["source_character_slug"]) if item["source_character_slug"] else None
            _, created = AdventureItem.objects.update_or_create(
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
                    "source_character": source_character,
                    "order": item["order"],
                },
            )
            if created:
                created_items += 1
        self.stdout.write(f"  - Phase 1 items: {len(PHASE1_ITEMS)} ({created_items} new)")

        chest_created = 0
        for item in CHEST_POOL:
            _, created = AdventureItem.objects.update_or_create(
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
            if created:
                chest_created += 1
        self.stdout.write(f"  - Chest pool: {len(CHEST_POOL)} ({chest_created} new)")

        degraded_created = 0
        for item in DEGRADED:
            full_item = AdventureItem.objects.filter(chapter=chapter, slug=item["of"]).first()
            if not full_item:
                continue
            _, created = AdventureItem.objects.update_or_create(
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
            if created:
                degraded_created += 1
        self.stdout.write(f"  - Degraded items: {len(DEGRADED)} ({degraded_created} new)")

        chest_phases_marked = 0
        for phase_number, tier in CHEST_PHASES.items():
            phase = phase_map.get(phase_number)
            if not phase:
                continue
            phase.has_chest = True
            phase.chest_tier = tier
            phase.save(update_fields=["has_chest", "chest_tier"])
            chest_phases_marked += 1
        self.stdout.write(f"  - Chest phases: {chest_phases_marked}")

        boss_phase = phase_map.get(25)
        if boss_phase:
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
                        "source_phase": boss_phase,
                        "order": item["order"],
                    },
                )
            self.stdout.write(f"  - Boss rewards: {len(BOSS_REWARDS)}")

        sync_item_skills()

        self.stdout.write(self.style.SUCCESS(
            f"\nSeed DE complete: {len(PHASES)} phases, {len(CHARACTERS)} characters, {len(PHRASES)} phrases\n"
        ))
