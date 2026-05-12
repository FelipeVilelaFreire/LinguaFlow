from django.core.management.base import BaseCommand

from apps.learning.models import Language, Phrase, Scenario, StudyModule

MODULES = [
    {
        "lang_code": "ES",
        "title": "Primeiros Passos",
        "order": 1,
        "scenarios": [
            {
                "slug": "es-saudacoes",
                "title": "Saudações e apresentações",
                "description": "Como cumprimentar e se apresentar no pueblo.",
                "adventure_phase": 1,
                "order": 1,
                "phrases": [
                    ("Olá", "Hola"),
                    ("Bom dia", "Buenos días"),
                    ("Boa tarde", "Buenas tardes"),
                    ("Boa noite", "Buenas noches"),
                    ("Como você está?", "¿Cómo estás?"),
                    ("Estou bem", "Estoy bien"),
                    ("Qual é o seu nome?", "¿Cómo te llamas?"),
                    ("Meu nome é...", "Me llamo..."),
                    ("Com licença", "Con permiso"),
                    ("Desculpe", "Perdón"),
                    ("Por favor", "Por favor"),
                    ("Obrigado", "Gracias"),
                    ("De nada", "De nada"),
                    ("Até logo", "Hasta luego"),
                    ("Tchau", "Adiós"),
                ],
            },
            {
                "slug": "es-comida",
                "title": "Comida e bebida",
                "description": "Alimentos, bebidas e situações à mesa.",
                "adventure_phase": 2,
                "order": 2,
                "phrases": [
                    ("O pão", "El pan"),
                    ("A água", "El agua"),
                    ("A maçã", "La manzana"),
                    ("O vinho", "El vino"),
                    ("O leite", "La leche"),
                    ("Estou com fome", "Tengo hambre"),
                    ("Estou com sede", "Tengo sed"),
                    ("Tem algo para comer?", "¿Tiene algo de comer?"),
                    ("Quero comer", "Quiero comer"),
                    ("A comida está boa", "La comida está buena"),
                    ("Um pouco mais", "Un poco más"),
                    ("Mais nada, obrigado", "Nada más, gracias"),
                    ("Quanto custa?", "¿Cuánto cuesta?"),
                    ("É muito caro", "Es muy caro"),
                    ("A conta, por favor", "La cuenta, por favor"),
                ],
            },
        ],
    },
    {
        "lang_code": "ES",
        "title": "O Mundo Natural",
        "order": 2,
        "scenarios": [
            {
                "slug": "es-natureza",
                "title": "Natureza e ambiente",
                "description": "O campo, o céu e os elementos ao redor do pueblo.",
                "adventure_phase": 3,
                "order": 3,
                "phrases": [
                    ("A árvore", "El árbol"),
                    ("A pedra", "La piedra"),
                    ("O rio", "El río"),
                    ("A flor", "La flor"),
                    ("O campo", "El campo"),
                    ("O sol", "El sol"),
                    ("A lua", "La luna"),
                    ("O céu", "El cielo"),
                    ("O vento", "El viento"),
                    ("A chuva", "La lluvia"),
                    ("A floresta", "El bosque"),
                    ("A montanha", "La montaña"),
                    ("O caminho", "El camino"),
                    ("A terra", "La tierra"),
                    ("O fogo", "El fuego"),
                ],
            },
            {
                "slug": "es-mercado",
                "title": "Mercado e números",
                "description": "Comprar, vender e os primeiros números.",
                "adventure_phase": 4,
                "order": 4,
                "phrases": [
                    ("Um", "Uno"),
                    ("Dois", "Dos"),
                    ("Três", "Tres"),
                    ("Quatro", "Cuatro"),
                    ("Cinco", "Cinco"),
                    ("Muito", "Mucho"),
                    ("Pouco", "Poco"),
                    ("O preço", "El precio"),
                    ("A moeda", "La moneda"),
                    ("O mercado", "El mercado"),
                    ("Comprar", "Comprar"),
                    ("Vender", "Vender"),
                    ("Caro", "Caro"),
                    ("Barato", "Barato"),
                    ("O troco", "El cambio"),
                ],
            },
        ],
    },
    {
        "lang_code": "ES",
        "title": "Dentro de Você",
        "order": 3,
        "scenarios": [
            {
                "slug": "es-emocoes",
                "title": "Emoções e sensações",
                "description": "Como você se sente — por dentro e no corpo.",
                "adventure_phase": 5,
                "order": 5,
                "phrases": [
                    ("O medo", "El miedo"),
                    ("Bem", "Bien"),
                    ("Mal", "Mal"),
                    ("Cansado", "Cansado"),
                    ("Feliz", "Feliz"),
                    ("Triste", "Triste"),
                    ("Assustado", "Asustado"),
                    ("Seguro", "Seguro"),
                    ("Perdido", "Perdido"),
                    ("Sozinho", "Solo"),
                    ("Confuso", "Confundido"),
                    ("Tranquilo", "Tranquilo"),
                    ("Com raiva", "Enojado"),
                    ("Surpreso", "Sorprendido"),
                    ("Aliviado", "Aliviado"),
                ],
            },
            {
                "slug": "es-lugares",
                "title": "Lugares e direções",
                "description": "Navegar pelo pueblo e pedir direções.",
                "adventure_phase": 5,
                "order": 6,
                "phrases": [
                    ("Aqui", "Aquí"),
                    ("Lá", "Allá"),
                    ("Perto", "Cerca"),
                    ("Longe", "Lejos"),
                    ("À esquerda", "A la izquierda"),
                    ("À direita", "A la derecha"),
                    ("Em frente", "Recto"),
                    ("A praça", "La plaza"),
                    ("A pousada", "La posada"),
                    ("A porta", "La puerta"),
                    ("Onde fica?", "¿Dónde está?"),
                    ("Por aqui", "Por aquí"),
                    ("Ao fundo", "Al fondo"),
                    ("A entrada", "La entrada"),
                    ("O caminho", "El camino"),
                ],
            },
        ],
    },
    {
        "lang_code": "ES",
        "title": "Pessoas e Tempo",
        "order": 4,
        "scenarios": [
            {
                "slug": "es-pessoas",
                "title": "Família e pessoas",
                "description": "Os habitantes do pueblo e os vínculos entre eles.",
                "adventure_phase": 6,
                "order": 7,
                "phrases": [
                    ("O amigo", "El amigo"),
                    ("O senhor", "El señor"),
                    ("A senhora", "La señora"),
                    ("O forasteiro", "El forastero"),
                    ("O camponês", "El campesino"),
                    ("A criança", "El niño"),
                    ("A família", "La familia"),
                    ("O pai", "El padre"),
                    ("A mãe", "La madre"),
                    ("O irmão", "El hermano"),
                    ("A irmã", "La hermana"),
                    ("O vizinho", "El vecino"),
                    ("Juntos", "Juntos"),
                    ("As pessoas", "La gente"),
                    ("O povo", "El pueblo"),
                ],
            },
            {
                "slug": "es-tempo",
                "title": "Tempo e clima",
                "description": "Dias, horários e como o tempo muda no campo.",
                "adventure_phase": 7,
                "order": 8,
                "phrases": [
                    ("Hoje", "Hoy"),
                    ("Amanhã", "Mañana"),
                    ("Ontem", "Ayer"),
                    ("A manhã", "La mañana"),
                    ("A tarde", "La tarde"),
                    ("A noite", "La noche"),
                    ("Está quente", "Hace calor"),
                    ("Está frio", "Hace frío"),
                    ("Em breve", "Pronto"),
                    ("Tarde", "Tarde"),
                    ("Cedo", "Temprano"),
                    ("Agora", "Ahora"),
                    ("Depois", "Después"),
                    ("Antes", "Antes"),
                    ("O tempo", "El tiempo"),
                ],
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Seed study modules, scenarios and phrases for ES A1"

    def handle(self, *args, **options):
        try:
            pt = Language.objects.get(code="PT")
            es = Language.objects.get(code="ES")
        except Language.DoesNotExist as exc:
            self.stderr.write(f"Language not found: {exc}. Run seed_languages first.")
            return

        total_phrases = 0

        for mod_data in MODULES:
            module, created = StudyModule.objects.update_or_create(
                lang_code=mod_data["lang_code"],
                title=mod_data["title"],
                defaults={"order": mod_data["order"]},
            )
            action = "created" if created else "updated"
            self.stdout.write(f"  Module {action}: {module}")

            for sc_data in mod_data["scenarios"]:
                scenario, _ = Scenario.objects.update_or_create(
                    slug=sc_data["slug"],
                    defaults={
                        "title":           sc_data["title"],
                        "description":     sc_data["description"],
                        "module":          module,
                        "adventure_phase": sc_data["adventure_phase"],
                        "order":           sc_data["order"],
                    },
                )
                self.stdout.write(f"    Scenario: {scenario.title}")

                for source_text, target_text in sc_data["phrases"]:
                    Phrase.objects.update_or_create(
                        source_language=pt,
                        target_language=es,
                        source_text=source_text,
                        defaults={
                            "target_text": target_text,
                            "difficulty":  "A1",
                            "scenario":    scenario,
                            "category":    sc_data["title"],
                        },
                    )
                    total_phrases += 1

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {len(MODULES)} modules, 8 scenarios, {total_phrases} phrases seeded for ES A1."
        ))
