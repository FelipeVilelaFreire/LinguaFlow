from content.models import Scenario

SCENARIOS = [
    ("restaurant", "Restaurante", "Pedir comida, pagar e resolver situações simples."),
    ("market", "Mercado", "Comprar itens, perguntar preços e quantidades."),
    ("transport", "Transporte", "Usar trem, ônibus, táxi e pedir direções."),
    ("university", "Universidade", "Conversas rápidas sobre aula, estudo e rotina."),
    ("housing", "Moradia", "Aluguel, manutenção e vida em casa."),
]


def seed_scenarios() -> None:
    for slug, title, description in SCENARIOS:
        Scenario.objects.update_or_create(slug=slug, defaults={"title": title, "description": description})
