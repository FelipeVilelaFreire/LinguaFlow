# Study Seed ES A1 — O que precisa ser feito

## Contexto

O Talkly tem dois caminhos de aprendizado paralelos e independentes:

```
AVENTURA ──→ fases narrativas + vocab em contexto RPG
                    ↕  (WordMastery compartilhado — mesmo tier)
ESTUDO   ──→ sessão do dia + cenários + prática estruturada
```

- O usuário pode seguir só a aventura, só o estudo, ou os dois.
- O estudo **mostra onde o usuário está na aventura** como referência visual — mas não depende dela para funcionar.
- O `WordMastery` (tier: bronze → esmeralda) é **compartilhado**: acertar uma palavra na aventura avança o tier dela no estudo também, e vice-versa.

---

## O problema atual

O app `learning/` (cenários, frases, lições) **não tem conteúdo para ES A1**. O seed existente cobre IT ou DE. Sem esse seed, o modo Estudo mostra tela vazia para quem escolheu Espanhol.

---

## O que precisa ser criado

### 1. Cenários ES A1 (`Scenario`)

8–10 cenários temáticos, alinhados com os temas das fases da aventura:

| Cenário | Slug | Fases da aventura que se relacionam |
|---------|------|-------------------------------------|
| Saudações e apresentações | `es-saudacoes` | F1 (hola, buenos días, me llamo) |
| Comida e bebida | `es-comida` | F2 (pan, agua, tengo hambre) |
| Natureza e ambiente | `es-natureza` | F3 (árbol, piedra, río, flor) |
| Mercado e números | `es-mercado` | F4 (naranja, uno/dos/tres, mucho/poco) |
| Emoções e sensações | `es-emocoes` | F5 (miedo, bien/mal, cansado) |
| Lugares e direções | `es-lugares` | F6+ (aquí, allá, cerca, lejos) |
| Família e pessoas | `es-pessoas` | F7+ (amigo, señor, señora) |
| Tempo e clima | `es-tempo` | F8+ (hoy, mañana, hace calor) |

### 2. Frases por cenário (`Phrase`)

~15 frases por cenário. Campos obrigatórios:
- `source_language`: PT
- `target_language`: ES
- `source_text`: frase em português
- `target_text`: frase em espanhol
- `category`: ex. `"saudacao"`, `"comida"`, `"numero"`
- `difficulty`: `"A1"`
- `scenario`: FK para o cenário acima

Exemplo para `es-saudacoes`:
```python
{ "source": "Olá",                    "target": "Hola" },
{ "source": "Bom dia",                "target": "Buenos días" },
{ "source": "Boa tarde",              "target": "Buenas tardes" },
{ "source": "Boa noite",              "target": "Buenas noches" },
{ "source": "Como vai você?",         "target": "¿Cómo estás?" },
{ "source": "Eu estou bem",           "target": "Estoy bien" },
{ "source": "Qual é o seu nome?",     "target": "¿Cómo te llamas?" },
{ "source": "Meu nome é...",          "target": "Me llamo..." },
{ "source": "Com licença",            "target": "Con permiso" },
{ "source": "Desculpe",               "target": "Perdón" },
{ "source": "Por favor",              "target": "Por favor" },
{ "source": "Obrigado",               "target": "Gracias" },
{ "source": "De nada",                "target": "De nada" },
{ "source": "Até logo",               "target": "Hasta luego" },
{ "source": "Tchau",                  "target": "Adiós" },
```

### 3. Lições (`Lesson`) — opcional para MVP

Uma lição agrupa um cenário com suas frases + metadados de sessão. Para MVP, cada cenário pode virar automaticamente uma lição com `day_number` sequencial.

### 4. O arquivo seed

Criar: `backend/apps/adventure/management/commands/seed_es_study.py`

```python
from django.core.management.base import BaseCommand
from apps.learning.models import Language, Scenario, Phrase

class Command(BaseCommand):
    help = "Seed study content for ES A1 (scenarios + phrases)"

    def handle(self, *args, **options):
        pt = Language.objects.get(code="PT")
        es = Language.objects.get(code="ES")

        SCENARIOS = [
            {
                "slug": "es-saudacoes",
                "title": "Saudações",
                "description": "Como cumprimentar e se apresentar",
                "phrases": [
                    ("Olá", "Hola"),
                    ("Bom dia", "Buenos días"),
                    # ... etc
                ],
            },
            # ... outros cenários
        ]

        for s_data in SCENARIOS:
            scenario, _ = Scenario.objects.update_or_create(
                slug=s_data["slug"],
                defaults={"title": s_data["title"], "description": s_data["description"]},
            )
            for source_text, target_text in s_data["phrases"]:
                Phrase.objects.update_or_create(
                    source_language=pt,
                    target_language=es,
                    source_text=source_text,
                    defaults={
                        "target_text": target_text,
                        "difficulty": "A1",
                        "scenario": scenario,
                    },
                )
```

---

## Alinhamento temático aventura ↔ estudo

O vocabulário do estudo **deve ser um superconjunto** do vocabulário da aventura no mesmo tema — nunca exatamente igual. O estudo vai mais fundo em cada tema enquanto a aventura dá o contexto narrativo.

| Aventura F1 introduz | Estudo `es-saudacoes` cobre |
|---------------------|----------------------------|
| hola, buenos días, buenas tardes, gracias, de nada, me llamo, ¿cómo estás?, bien | + boa noite, perdón, por favor, hasta luego, adiós, con permiso, estoy mal |

---

## Ordem de execução dos seeds

```bash
# 1. Linguagens (já existem)
python manage.py seed_languages

# 2. Aventura ES A1
python manage.py seed_es_full
python manage.py seed_es_f1_sections
python manage.py seed_es_f2_sections
python manage.py seed_es_f3_sections
python manage.py seed_es_f4_sections
python manage.py seed_es_f5_sections

# 3. Estudo ES A1 (a criar)
python manage.py seed_es_study
```

---

## Estimativa de esforço

| Item | Complexidade | Notas |
|------|-------------|-------|
| Escrever as frases dos 8 cenários (~120 frases) | Média | Conteúdo A1, simples |
| Criar `seed_es_study.py` | Baixa | Segue padrão dos outros seeds |
| Conectar `StudyDayViewSet` com ES | Baixa | Verificar se `GET /study-days/today/` filtra por idioma do goal |
| Testar fluxo completo | Baixa | Rodar seed + testar `GET /scenarios/` + `GET /phrases/?scenario=es-saudacoes` |

---

## Status

- [x] Modo Aventura ES A1 — seed F1–F5 criado
- [x] Modo Estudo — SRS session conectado ao WordMastery da aventura
- [x] StudyScreen conectado à API (due_count real, progresso real por capítulo)
- [ ] **Seed de cenários + frases ES A1 para o modo Estudo** ← próximo passo
- [ ] Conectar `Sessão do Dia` ao conteúdo ES A1 (hoje usa IT/DE)
