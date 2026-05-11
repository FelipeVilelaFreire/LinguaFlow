"""
Seed ES A1 T1 · "El Pueblo" — Fase 1 apenas.

Uso: python manage.py seed_es_full
"""
from django.core.management.base import BaseCommand

from apps.adventure.models import (
    AdventureCharacter,
    AdventureChapter,
    AdventureItem,
    AdventurePhase,
)
from apps.learning.models import Language, Phrase, Scenario


# ═══════════════════════════════════════════════════════════════════════════════
# CENÁRIOS
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIOS = [
    ("es-social",   "Social",     "Saudações, apresentações e convívio."),
    ("es-lugares",  "Lugares",    "Orientação, direções e pontos do pueblo."),
    ("es-comida",   "Comida",     "Alimentação, pedidos e sabores."),
    ("es-mercado",  "Mercado",    "Compras, preços e negociação."),
    ("es-salud",    "Salud",      "Saúde, corpo e cuidado pessoal."),
    ("es-trabalho", "Trabajo",    "Trabalho, ofícios e rotina."),
    ("es-historia", "Historia",   "Memória, passado e mistério."),
    ("es-desafio",  "Desafío",    "Provas, conflito e decisões."),
]


# ═══════════════════════════════════════════════════════════════════════════════
# FRASES PT → ES
# ═══════════════════════════════════════════════════════════════════════════════

PHRASES: list[tuple[str, str, str]] = [

    # ── es-social ──────────────────────────────────────────────────────────────
    ("Olá",                        "Hola",                   "es-social"),
    ("Bom dia",                    "Buenos días",            "es-social"),
    ("Boa tarde",                  "Buenas tardes",          "es-social"),
    ("Boa noite",                  "Buenas noches",          "es-social"),
    ("Tchau",                      "Adiós",                  "es-social"),
    ("Até logo",                   "Hasta luego",            "es-social"),
    ("Meu nome é",                 "Me llamo",               "es-social"),
    ("Como você se chama?",        "¿Cómo te llamas?",       "es-social"),
    ("Prazer",                     "Mucho gusto",            "es-social"),
    ("Forasteiro",                 "Forastero",              "es-social"),
    ("Fazendeiro",                 "Campesino",              "es-social"),
    ("Bem",                        "Bien",                   "es-social"),
    ("Por favor",                  "Por favor",              "es-social"),
    ("Obrigado",                   "Gracias",                "es-social"),
    ("De nada",                    "De nada",                "es-social"),
    ("Amigo",                      "Amigo",                  "es-social"),
    ("Passo a passo",              "Paso a paso",            "es-social"),
    ("Sente-se",                   "Siéntate",               "es-social"),
    ("Sim",                        "Sí",                     "es-social"),
    ("Não",                        "No",                     "es-social"),

    # ── es-lugares ─────────────────────────────────────────────────────────────
    ("Onde fica?",                 "¿Dónde está?",           "es-lugares"),
    ("À esquerda",                 "A la izquierda",         "es-lugares"),
    ("À direita",                  "A la derecha",           "es-lugares"),
    ("Em frente",                  "Enfrente",               "es-lugares"),
    ("Aqui",                       "Aquí",                   "es-lugares"),
    ("Ali",                        "Allá",                   "es-lugares"),
    ("O mercado",                  "El mercado",             "es-lugares"),
    ("A praça",                    "La plaza",               "es-lugares"),
    ("A pousada",                  "La posada",              "es-lugares"),
    ("A Igreja",                   "La iglesia",             "es-lugares"),
    ("O portão",                   "La puerta",              "es-lugares"),
    ("O poço",                     "El pozo",                "es-lugares"),
    ("A cidade",                   "La ciudad",              "es-lugares"),
    ("O caminho",                  "El camino",              "es-lugares"),
    ("Próximo",                    "Cerca",                  "es-lugares"),

    # ── es-comida ──────────────────────────────────────────────────────────────
    ("Estou com fome",             "Tengo hambre",           "es-comida"),
    ("Estou com sede",             "Tengo sed",              "es-comida"),
    ("Água",                       "Agua",                   "es-comida"),
    ("Pão",                        "Pan",                    "es-comida"),
    ("Tortilha",                   "Tortilla",               "es-comida"),
    ("Feijão",                     "Frijoles",               "es-comida"),
    ("Queijo",                     "Queso",                  "es-comida"),
    ("Fruta",                      "Fruta",                  "es-comida"),
    ("Carne",                      "Carne",                  "es-comida"),
    ("Quero comer",                "Quiero comer",           "es-comida"),
    ("Está bom",                   "Está bueno",             "es-comida"),
    ("Muito gostoso",              "Muy rico",               "es-comida"),
    ("A mesa",                     "La mesa",                "es-comida"),
    ("A taverna",                  "La taberna",             "es-comida"),
    ("Um prato",                   "Un plato",               "es-comida"),

    # ── es-mercado ─────────────────────────────────────────────────────────────
    ("Quanto custa?",              "¿Cuánto cuesta?",        "es-mercado"),
    ("Muito caro",                 "Muy caro",               "es-mercado"),
    ("Barato",                     "Barato",                 "es-mercado"),
    ("Quero comprar",              "Quiero comprar",         "es-mercado"),
    ("Dinheiro",                   "Dinero",                 "es-mercado"),
    ("Moeda",                      "Moneda",                 "es-mercado"),
    ("Tem desconto?",              "¿Hay descuento?",        "es-mercado"),
    ("Vou levar",                  "Me lo llevo",            "es-mercado"),
    ("Vendedor",                   "Vendedor",               "es-mercado"),
    ("Permissão",                  "Permiso",                "es-mercado"),
    ("Documento",                  "Documento",              "es-mercado"),
    ("Passe",                      "Pase",                   "es-mercado"),

    # ── es-salud ───────────────────────────────────────────────────────────────
    ("Estou doente",               "Estoy enfermo",          "es-salud"),
    ("Dói aqui",                   "Me duele aquí",          "es-salud"),
    ("Curandeira",                 "Curandera",              "es-salud"),
    ("Remédio",                    "Medicina",               "es-salud"),
    ("Melhor",                     "Mejor",                  "es-salud"),
    ("Descanse",                   "Descanse",               "es-salud"),
    ("Erva",                       "Hierba",                 "es-salud"),
    ("Mão",                        "Mano",                   "es-salud"),
    ("Cabeça",                     "Cabeza",                 "es-salud"),
    ("Cansado",                    "Cansado",                "es-salud"),

    # ── es-trabalho ────────────────────────────────────────────────────────────
    ("Ferreiro",                   "Herrero",                "es-trabalho"),
    ("Padeira",                    "Panadera",               "es-trabalho"),
    ("Cozinheiro",                 "Cocinero",               "es-trabalho"),
    ("Sentinela",                  "Vigilante",              "es-trabalho"),
    ("Trabalho",                   "Trabajo",                "es-trabalho"),
    ("Trabalho muito",             "Trabajo mucho",          "es-trabalho"),
    ("De onde você vem?",          "¿De dónde vienes?",      "es-trabalho"),
    ("Venho de longe",             "Vengo de lejos",         "es-trabalho"),
    ("Forte",                      "Fuerte",                 "es-trabalho"),
    ("Ferro",                      "Hierro",                 "es-trabalho"),

    # ── es-historia ────────────────────────────────────────────────────────────
    ("Não me lembro",              "No recuerdo",            "es-historia"),
    ("Meu passado",                "Mi pasado",              "es-historia"),
    ("Esqueci",                    "Olvidé",                 "es-historia"),
    ("É verdade",                  "Es verdad",              "es-historia"),
    ("É mentira",                  "Es mentira",             "es-historia"),
    ("Segredo",                    "Secreto",                "es-historia"),
    ("Perigo",                     "Peligro",                "es-historia"),
    ("Cuidado",                    "Cuidado",                "es-historia"),
    ("Conheço",                    "Conozco",                "es-historia"),
    ("Preciso ir",                 "Necesito irme",          "es-historia"),
    ("Ficar",                      "Quedarme",               "es-historia"),
    ("Futuro",                     "Futuro",                 "es-historia"),

    # ── es-desafio ─────────────────────────────────────────────────────────────
    ("Prova",                      "Prueba",                 "es-desafio"),
    ("Mostrar",                    "Demostrar",              "es-desafio"),
    ("Respeito",                   "Respeto",                "es-desafio"),
    ("Honra",                      "Honor",                  "es-desafio"),
    ("Julgamento",                 "Juicio",                 "es-desafio"),
    ("Estrangeiro",                "Extranjero",             "es-desafio"),
    ("Provar que",                 "Demostrar que",          "es-desafio"),
    ("Deixar passar",              "Dejar pasar",            "es-desafio"),
    ("Autoridade",                 "Autoridad",              "es-desafio"),
    ("Bem-vindo",                  "Bienvenido",             "es-desafio"),
]


# ═══════════════════════════════════════════════════════════════════════════════
# FASES
# ═══════════════════════════════════════════════════════════════════════════════

PHASES = [
    {
        "number": 1, "phase_type": "story",
        "title": "O Despertar no Campo",
        "narrative_intro": (
            "Você acorda sozinho num campo de milho dourado. Não sabe seu nome — "
            "não sabe de onde veio. Um homem de sombrero caminha na sua direção.\n\n"
            "'¡Oye, forastero! ¿Estás bien?'"
        ),
        "narrative_outro": (
            "Você aprendeu as primeiras palavras e Don Miguel te acompanhou até a posada do pueblo. "
            "Antes de entrar, ele te dá um tapinha no ombro:\n\n"
            "'Descansa, forastero. Mañana es otro día.'"
        ),
        "key_words": ["hola", "me llamo", "forastero", "campesino", "bien"],
        "scenario_slug": "es-social", "phrase_count": 8,
    },
]


# ═══════════════════════════════════════════════════════════════════════════════
# PERSONAGENS
# ═══════════════════════════════════════════════════════════════════════════════

CHARACTERS = [
    (
        "don_miguel",
        "Don Miguel el Campesino",
        "Campesino",
        "👨‍🌾",
        "ally",
        True,
        1,
        1,
        "Poco a poco, amigo. La lengua se aprende viviendo.",
    ),
    (
        "vigilante",
        "El Vigilante del Mercado",
        "Vigilante",
        "💂",
        "npc",
        False,
        1,
        2,
        "El pase o la puerta. No hay otra opción.",
    ),
    (
        "senora_carmen",
        "Señora Carmen",
        "Vecina",
        "👩",
        "npc",
        False,
        1,
        3,
        "La palabra más bonita del español es 'gracias'.",
    ),
    (
        "rosa_panadera",
        "Rosa la Panadera",
        "Panadera",
        "👩‍🍳",
        "npc",
        False,
        1,
        4,
        "¡Hola, hola! Bienvenido.",
    ),
]


# ═══════════════════════════════════════════════════════════════════════════════
# ITENS  (nenhum ainda — sem boss na fase 1)
# ═══════════════════════════════════════════════════════════════════════════════

ITEMS: list = []


# ═══════════════════════════════════════════════════════════════════════════════
# COMMAND
# ═══════════════════════════════════════════════════════════════════════════════

class Command(BaseCommand):
    help = "Seed ES A1 T1 — El Pueblo, Fase 1"

    def handle(self, *args, **options):
        self.stdout.write("\n📦 Iniciando seed ES A1 T1 — El Pueblo (Fase 1)\n")

        # ── 1. Idiomas ────────────────────────────────────────────────────────
        pt, _ = Language.objects.get_or_create(code="PT", defaults={"name": "Português", "is_ready": False})
        es, created = Language.objects.get_or_create(code="ES", defaults={"name": "Español", "is_ready": True})
        if not created:
            Language.objects.filter(code="ES").update(is_ready=True)
        self.stdout.write("  ✓ Idiomas: PT, ES")

        # ── 2. Cenários ───────────────────────────────────────────────────────
        scenario_objs: dict[str, Scenario] = {}
        for slug, title, description in SCENARIOS:
            obj, _ = Scenario.objects.get_or_create(
                slug=slug, defaults={"title": title, "description": description}
            )
            scenario_objs[slug] = obj
        self.stdout.write(f"  ✓ Cenários: {len(scenario_objs)} criados/existentes")

        # ── 3. Frases PT→ES ───────────────────────────────────────────────────
        phrase_count = 0
        for source_text, target_text, scenario_slug in PHRASES:
            _, created = Phrase.objects.get_or_create(
                source_language=pt,
                target_language=es,
                source_text=source_text,
                target_text=target_text,
                defaults={"scenario": scenario_objs[scenario_slug], "difficulty": "A1"},
            )
            if created:
                phrase_count += 1
        self.stdout.write(f"  ✓ Frases PT→ES: {phrase_count} novas ({len(PHRASES)} total)")

        # ── 4. Chapter ────────────────────────────────────────────────────────
        chapter, _ = AdventureChapter.objects.update_or_create(
            slug="es-a1-t1",
            defaults={
                "language":           es,
                "level":              "A1",
                "order":              1,
                "title":              "El Pueblo",
                "subtitle":           "T1 · A chegada",
                "background":         "es_pueblo",
                "boss_name":          "El Jefe del Pueblo",
                "boss_intro": (
                    "O senhor do pueblo. Ninguém passa pela Ciudad de la Plata "
                    "sem o seu sello — e ele não dá sellos de graça."
                ),
                "reward_name":        "Sello del Pueblo",
                "reward_description": (
                    "Impresso em cera vermelha. Prova que você sobreviveu ao Pueblo "
                    "e conhece as suas regras."
                ),
            },
        )
        self.stdout.write(f"  ✓ Chapter: {chapter.slug}")

        # ── 5. Fases ──────────────────────────────────────────────────────────
        phase_map: dict[int, AdventurePhase] = {}
        for p in PHASES:
            phase_obj, _ = AdventurePhase.objects.update_or_create(
                chapter=chapter,
                number=p["number"],
                defaults={
                    "title":           p["title"],
                    "narrative_intro": p["narrative_intro"],
                    "narrative_outro": p["narrative_outro"],
                    "key_words":       p["key_words"],
                    "scenario_slug":   p["scenario_slug"],
                    "phrase_count":    p["phrase_count"],
                    "phase_type":      p["phase_type"],
                },
            )
            phase_map[p["number"]] = phase_obj
        self.stdout.write(f"  ✓ Fases: {len(PHASES)}")

        # ── 6. Personagens ────────────────────────────────────────────────────
        char_map: dict[str, AdventureCharacter] = {}
        for slug, name, role, emoji, ctype, lang_bridge, first_phase_num, order, quote in CHARACTERS:
            char_obj, _ = AdventureCharacter.objects.update_or_create(
                chapter=chapter,
                slug=slug,
                defaults={
                    "name":           name,
                    "role":           role,
                    "emoji":          emoji,
                    "character_type": ctype,
                    "quote":          quote,
                    "lang_bridge":    lang_bridge,
                    "first_phase":    phase_map[first_phase_num],
                    "order":          order,
                },
            )
            char_map[slug] = char_obj
        self.stdout.write(f"  ✓ Personagens: {len(CHARACTERS)}")

        # ── 7. Itens ──────────────────────────────────────────────────────────
        # Mochila Fase 1 = bolsa de viajante de verdade. Itens cotidianos que
        # mapeiam aos momentos da fase. Cada item reforça vocab (pan, manzana,
        # agua) e ancora um beat narrativo. Sem item lendário/épico aqui — esses
        # ficam pra fases avançadas (boss, marcos emocionais).

        # Remove sombrero antigo se existir (foi substituído pelos itens diários)
        AdventureItem.objects.filter(chapter=chapter, slug="sombrero_viejo").delete()

        PHASE1_ITEMS = [
            {
                "slug": "pan_fresco",
                "emoji": "🍞",
                "name": "Pan Fresco",
                "lore": (
                    "Quente, ainda saindo do forno de barro. Uma senhora de avental "
                    "empoeirado te entregou um pedaço quando você passava pela porta "
                    "de adobe dela. 'Para el camino, forastero.' Ela não pediu nada "
                    "em troca — só sorriu e voltou pra dentro."
                ),
                "source_character_slug": None,
                "order": 1,
            },
            {
                "slug": "manzana_del_campo",
                "emoji": "🍎",
                "name": "Manzana del Campo",
                "lore": (
                    "Don Miguel arrancou esta manzana da árvore atrás da casa dele e "
                    "te passou sem cerimônia. Pequena, vermelha, com gosto de fruta "
                    "de verdade. 'El campesino siempre tiene algo en el bolsillo, ¿eh?'"
                ),
                "source_character_slug": "don_miguel",
                "order": 2,
            },
            {
                "slug": "agua_del_pozo",
                "emoji": "💧",
                "name": "Agua del Pozo",
                "lore": (
                    "Você bebeu da água do poço da plaza central. Fria, com gosto leve "
                    "de pedra molhada. Don Miguel acenou enquanto você bebia: 'El agua "
                    "de este pozo es buena. Aquí no te enfermarás, forastero.'"
                ),
                "source_character_slug": None,
                "order": 3,
            },
            {
                "slug": "moneda_de_cobre",
                "emoji": "🪙",
                "name": "Moneda de Cobre",
                "lore": (
                    "Don Miguel te entregou esta moeda velha antes de você seguir caminho. "
                    "'Quédatela. Te trae suerte en este pueblo.' Pequena, manchada de "
                    "verde nas bordas, parece ter passado por muitas mãos antes da sua."
                ),
                "source_character_slug": "don_miguel",
                "order": 4,
            },
        ]

        created_count = 0
        for item_data in PHASE1_ITEMS:
            source_char_slug = item_data.get("source_character_slug")
            source_char = char_map.get(source_char_slug) if source_char_slug else None
            _, created = AdventureItem.objects.update_or_create(
                chapter=chapter,
                slug=item_data["slug"],
                defaults={
                    "emoji":            item_data["emoji"],
                    "name":             item_data["name"],
                    "lore":             item_data["lore"],
                    "rarity":           AdventureItem.RARITY_COMUM,
                    "action":           AdventureItem.ACTION_EXAMINAR,
                    "source_phase":     phase_map[1],
                    "source_character": source_char,
                    "order":            item_data["order"],
                },
            )
            if created:
                created_count += 1
        self.stdout.write(f"  ✓ Itens: {len(PHASE1_ITEMS)} (cotidiano) — {created_count} novos")

        # ─────────────────────────────────────────────────────────────────────
        self.stdout.write(self.style.SUCCESS(
            "\n✅ Seed ES A1 T1 completo!\n"
            f"   1 fase · {len(CHARACTERS)} personagens · 0 itens · {len(PHRASES)} frases\n"
        ))
