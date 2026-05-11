"""
Seed PT → ES aventura — Phase 1 apenas (para testes).
Cria: idiomas, cenário, frases, chapter es-a1-t1, fase 1, personagens, item.

Uso: python manage.py seed_es
"""
from django.core.management.base import BaseCommand

from apps.adventure.models import (
    AdventureCharacter,
    AdventureChapter,
    AdventureItem,
    AdventurePhase,
)
from apps.learning.models import Language, Phrase, Scenario


# ─── Vocabulário da Fase 1 ────────────────────────────────────────────────────
# (source PT, target ES)

PHRASES_FASE1 = [
    ("Olá",               "Hola"),
    ("Meu nome é",        "Me llamo"),
    ("Forasteiro",        "Forastero"),
    ("Fazendeiro",        "Campesino"),
    ("Bem",               "Bien"),
    ("Amigo",             "Amigo"),
    ("Sente-se",          "Siéntate"),
    ("Passo a passo",     "Paso a paso"),
]


class Command(BaseCommand):
    help = "Seed PT→ES adventure — Phase 1 only (testing)"

    def handle(self, *args, **options):

        # ── 1. Idiomas ────────────────────────────────────────────────────────
        pt, _ = Language.objects.get_or_create(code="PT", defaults={"name": "Português"})
        es, _ = Language.objects.get_or_create(code="ES", defaults={"name": "Español"})
        self.stdout.write("  Idiomas: PT, ES")

        # ── 2. Cenário ────────────────────────────────────────────────────────
        scenario, _ = Scenario.objects.get_or_create(
            slug="pueblo",
            defaults={
                "title": "El Pueblo",
                "description": "Sobreviver num pueblo colonial espanhol.",
            },
        )
        self.stdout.write("  Cenário: pueblo")

        # ── 3. Frases PT→ES ───────────────────────────────────────────────────
        phrase_count = 0
        for source_text, target_text in PHRASES_FASE1:
            _, created = Phrase.objects.get_or_create(
                source_language=pt,
                target_language=es,
                source_text=source_text,
                target_text=target_text,
                defaults={"scenario": scenario, "difficulty": "A1"},
            )
            if created:
                phrase_count += 1
        self.stdout.write(f"  Frases: {phrase_count} criadas ({len(PHRASES_FASE1)} total)")

        # ── 4. Chapter ────────────────────────────────────────────────────────
        chapter, _ = AdventureChapter.objects.get_or_create(
            slug="es-a1-t1",
            defaults={
                "language":            es,
                "level":               "A1",
                "order":               1,
                "title":               "El Pueblo",
                "subtitle":            "T1 · A chegada",
                "background":          "es_pueblo",
                "boss_name":           "El Jefe del Pueblo",
                "boss_intro":          (
                    "O senhor do pueblo. Ninguém passa pela Ciudad de la Plata "
                    "sem o seu selo — e ele não dá selos de graça."
                ),
                "reward_name":         "Sello del Pueblo",
                "reward_description":  (
                    "Impresso em cera vermelha. Prova que você sobreviveu ao Pueblo "
                    "e conhece as suas regras."
                ),
            },
        )
        self.stdout.write(f"  Chapter: {chapter.slug}")

        # ── 5. Fase 1 ─────────────────────────────────────────────────────────
        phase1, _ = AdventurePhase.objects.get_or_create(
            chapter=chapter,
            number=1,
            defaults={
                "title":           "O Despertar no Campo",
                "narrative_intro": (
                    "Você acorda sozinho num campo de milho dourado. Não sabe seu nome, "
                    "não sabe de onde veio. Um homem de sombrero caminha na sua direção.\n\n"
                    "'¡Oye, forastero! ¿Estás bien?'\n\nVocê precisa responder."
                ),
                "narrative_outro": (
                    "Você aprendeu as primeiras palavras. "
                    "Don Miguel sorri e aponta para o pueblo ao longe.\n\n"
                    "'Poco a poco, amigo. Paso a paso.'"
                ),
                "key_words":    ["hola", "me llamo", "forastero", "campesino", "bien"],
                "scenario_slug": "pueblo",
                "phrase_count":  8,
                "phase_type":   AdventurePhase.PHASE_TYPE_STORY,
            },
        )
        self.stdout.write(f"  Fase 1: {phase1.title}")

        # ── 6. Personagens ────────────────────────────────────────────────────
        miguel, _ = AdventureCharacter.objects.get_or_create(
            chapter=chapter,
            slug="don_miguel",
            defaults={
                "name":           "Don Miguel el Campesino",
                "role":           "Campesino",
                "emoji":          "👨‍🌾",
                "character_type": AdventureCharacter.TYPE_ALLY,
                "quote":          "Poco a poco, amigo. La lengua se aprende viviendo.",
                "lang_bridge":    True,   # fala português quebrado — é a ponte do player
                "first_phase":    phase1,
                "order":          1,
            },
        )
        self.stdout.write(f"  Personagem: {miguel.name} ({miguel.get_character_type_display()})")

        # ── 7. Item da Fase 1 ─────────────────────────────────────────────────
        item, _ = AdventureItem.objects.get_or_create(
            chapter=chapter,
            slug="pase_mercado",
            defaults={
                "emoji":            "🎫",
                "name":             "Pase del Mercado",
                "lore":             (
                    "El Vigilante dobrou o papel sem dizer nada. "
                    "Só empurrou pelo portão. Você provou que sabia quem era — "
                    "e ele deixou passar."
                ),
                "rarity":           AdventureItem.RARITY_COMUM,
                "action":           AdventureItem.ACTION_EXAMINAR,
                "source_phase":     phase1,
                "source_character": miguel,
                "order":            1,
            },
        )
        self.stdout.write(f"  Item: {item.emoji} {item.name}")

        # ─────────────────────────────────────────────────────────────────────
        self.stdout.write(self.style.SUCCESS(
            "\n✅ Seed ES completo — 1 chapter · 1 fase · 1 personagem · 1 item"
        ))
