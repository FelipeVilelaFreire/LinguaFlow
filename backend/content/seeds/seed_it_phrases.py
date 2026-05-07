"""
Seed PT → IT phrases, lessons and study days.
Run via: python manage.py seed_content_it
"""
from __future__ import annotations

from content.models import Language, Lesson, Phrase, Scenario, StudyDay


LANGUAGE_NAMES = {
    "PT": "Portugues",
    "IT": "Italiano",
}

# ─── Phrases: (source_pt, target_it, scenario_slug, difficulty) ──────────────

PHRASES: list[tuple[str, str, str, str]] = [

    # ── social ──────────────────────────────────────────────────────────────
    ("Ola",                          "Ciao",                           "social", "A1"),
    ("Bom dia",                      "Buongiorno",                     "social", "A1"),
    ("Boa tarde",                    "Buon pomeriggio",                "social", "A1"),
    ("Boa noite",                    "Buonasera",                      "social", "A1"),
    ("Ate logo",                     "Arrivederci",                    "social", "A1"),
    ("Tchau",                        "Ciao ciao",                      "social", "A1"),
    ("Como voce esta",               "Come stai?",                     "social", "A1"),
    ("Estou bem, obrigado",          "Sto bene, grazie",               "social", "A1"),
    ("Meu nome e",                   "Mi chiamo",                      "social", "A1"),
    ("Qual e o seu nome",            "Come ti chiami?",                "social", "A1"),
    ("Prazer em conhecer voce",      "Piacere di conoscerti",          "social", "A1"),
    ("De onde voce e",               "Di dove sei?",                   "social", "A1"),
    ("Sou do Brasil",                "Sono del Brasile",               "social", "A1"),
    ("Voce fala italiano",           "Parli italiano?",                "social", "A1"),
    ("Nao entendo",                  "Non capisco",                    "social", "A1"),
    ("Pode repetir por favor",       "Puoi ripetere per favore?",      "social", "A1"),
    ("Fala mais devagar por favor",  "Parla più lentamente per favore","social", "A1"),
    ("Com licenca",                  "Scusa",                          "social", "A1"),
    ("Desculpe",                     "Mi dispiace",                    "social", "A1"),
    ("Nao tem problema",             "Non c'è problema",               "social", "A1"),
    ("Sim",                          "Sì",                             "social", "A1"),
    ("Nao",                          "No",                             "social", "A1"),
    ("Por favor",                    "Per favore",                     "social", "A1"),
    ("Obrigado",                     "Grazie",                         "social", "A1"),
    ("Muito obrigado",               "Grazie mille",                   "social", "A1"),
    ("De nada",                      "Prego",                          "social", "A1"),

    # ── social A2 ───────────────────────────────────────────────────────────
    ("Quanto tempo voce esta aqui",  "Da quanto tempo sei qui?",       "social", "A2"),
    ("Morei em Roma por dois anos",  "Ho vissuto a Roma per due anni", "social", "A2"),
    ("O que voce faz",               "Cosa fai nella vita?",           "social", "A2"),
    ("Sou estudante",                "Sono studente",                  "social", "A2"),
    ("Trabalho como professor",      "Lavoro come insegnante",         "social", "A2"),
    ("Tenho trinta anos",            "Ho trent'anni",                  "social", "A2"),
    ("Voce e casado",                "Sei sposato?",                   "social", "A2"),
    ("Tenho dois filhos",            "Ho due figli",                   "social", "A2"),
    ("Gosto muito de Italia",        "Mi piace molto l'Italia",        "social", "A2"),
    ("Que horas sao",                "Che ore sono?",                  "social", "A2"),
    ("Sao tres horas",               "Sono le tre",                    "social", "A2"),

    # ── restaurant ──────────────────────────────────────────────────────────
    ("O cardapio por favor",         "Il menu, per favore",            "restaurant", "A1"),
    ("Uma mesa para dois",           "Un tavolo per due",              "restaurant", "A1"),
    ("Eu quero um cafe",             "Vorrei un caffè",                "restaurant", "A1"),
    ("Eu quero agua",                "Vorrei dell'acqua",              "restaurant", "A1"),
    ("Tenho fome",                   "Ho fame",                        "restaurant", "A1"),
    ("Tenho sede",                   "Ho sete",                        "restaurant", "A1"),
    ("A conta por favor",            "Il conto, per favore",           "restaurant", "A1"),
    ("Quanto custa",                 "Quanto costa?",                  "restaurant", "A1"),
    ("Esta delicioso",               "È delizioso",                    "restaurant", "A1"),
    ("Eu sou vegetariano",           "Sono vegetariano",               "restaurant", "A1"),
    ("Sem gluten por favor",         "Senza glutine, per favore",      "restaurant", "A1"),
    ("O que voce recomenda",         "Cosa consiglia?",                "restaurant", "A1"),
    ("Posso pagar com cartao",       "Posso pagare con carta?",        "restaurant", "A1"),
    ("O servico esta incluido",      "Il servizio è incluso?",         "restaurant", "A1"),
    ("Esta um pouco salgado",        "È un po' salato",                "restaurant", "A2"),
    ("Posso ver o cardapio de vinhos","Posso vedere la carta dei vini?","restaurant", "A2"),
    ("Quero reservar uma mesa",      "Vorrei prenotare un tavolo",     "restaurant", "A2"),
    ("Para quantas pessoas",         "Per quante persone?",            "restaurant", "A2"),
    ("Traga mais pao por favor",     "Ci porti altro pane per favore", "restaurant", "A2"),

    # ── market ──────────────────────────────────────────────────────────────
    ("Quanto custa isso",            "Quanto costa questo?",           "market", "A1"),
    ("E muito caro",                 "È troppo caro",                  "market", "A1"),
    ("Eu preciso de pao",            "Ho bisogno di pane",             "market", "A1"),
    ("Quero comprar",                "Voglio comprare",                "market", "A1"),
    ("Voce tem",                     "Hai...?",                        "market", "A1"),
    ("Onde posso encontrar",         "Dove posso trovare...?",         "market", "A1"),
    ("Isso e para mim",              "Questo è per me",                "market", "A1"),
    ("Tem desconto",                 "C'è uno sconto?",                "market", "A1"),
    ("Pode embrulhar por favor",     "Può incartarlo per favore?",     "market", "A2"),
    ("Quero trocar este produto",    "Vorrei cambiare questo prodotto","market", "A2"),
    ("Qual e o tamanho",             "Qual è la taglia?",              "market", "A2"),
    ("Tem em outro tamanho",         "Ce l'ha in un'altra misura?",    "market", "A2"),
    ("Onde fica o mercado",          "Dov'è il mercato?",              "market", "A1"),
    ("Vou levar dois",               "Ne prendo due",                  "market", "A1"),

    # ── transport ───────────────────────────────────────────────────────────
    ("Onde fica a estacao",          "Dov'è la stazione?",             "transport", "A1"),
    ("Um bilhete para Roma",         "Un biglietto per Roma",          "transport", "A1"),
    ("A que horas parte o trem",     "A che ora parte il treno?",      "transport", "A1"),
    ("Quanto tempo leva",            "Quanto tempo ci vuole?",         "transport", "A1"),
    ("E longe",                      "È lontano?",                     "transport", "A1"),
    ("Vire a esquerda",              "Giri a sinistra",                "transport", "A1"),
    ("Vire a direita",               "Giri a destra",                  "transport", "A1"),
    ("Va em frente",                 "Vada dritto",                    "transport", "A1"),
    ("Onde estamos",                 "Dove siamo?",                    "transport", "A1"),
    ("Estou perdido",                "Mi sono perso",                  "transport", "A1"),
    ("Voce pode me ajudar",          "Può aiutarmi?",                  "transport", "A1"),
    ("O trem esta atrasado",         "Il treno è in ritardo",          "transport", "A2"),
    ("Preciso ir ao aeroporto",      "Devo andare all'aeroporto",      "transport", "A2"),
    ("Ha um onibus para o centro",   "C'è un autobus per il centro?",  "transport", "A2"),
    ("Onde fica a parada de metro",  "Dov'è la fermata della metro?",  "transport", "A2"),
    ("E necessario prenotar",        "Bisogna prenotare?",             "transport", "A2"),

    # ── health ──────────────────────────────────────────────────────────────
    ("Esta doendo",                  "Mi fa male",                     "health", "A1"),
    ("Estou com febre",              "Ho la febbre",                   "health", "A1"),
    ("Nao me sinto bem",             "Non mi sento bene",              "health", "A1"),
    ("Socorro",                      "Aiuto!",                         "health", "A1"),
    ("E uma emergencia",             "È un'emergenza",                 "health", "A1"),
    ("Onde fica o hospital",         "Dov'è l'ospedale?",              "health", "A1"),
    ("Preciso de um medico",         "Ho bisogno di un medico",        "health", "A1"),
    ("Tenho alergia a",              "Sono allergico a",               "health", "A1"),
    ("Pode me dar um remedio",       "Può darmi una medicina?",        "health", "A2"),
    ("Estou melhorando",             "Sto migliorando",                "health", "A2"),
    ("Ha quanto tempo esta doendo",  "Da quanto tempo le fa male?",    "health", "A2"),
    ("Preciso de receita medica",    "Ho bisogno di una ricetta",      "health", "A2"),

    # ── travel ──────────────────────────────────────────────────────────────
    ("Onde fica o hotel",            "Dov'è l'hotel?",                 "travel", "A1"),
    ("Tenho uma reserva",            "Ho una prenotazione",            "travel", "A1"),
    ("Quero um quarto para uma pessoa","Vorrei una camera singola",    "travel", "A1"),
    ("Com cafe da manha incluido",   "Con colazione inclusa",          "travel", "A1"),
    ("A que horas e o check-out",    "A che ora è il check-out?",      "travel", "A2"),
    ("Pode guardar minha mala",      "Può custodire il mio bagaglio?", "travel", "A2"),
    ("Quero visitar o Colosseo",     "Voglio visitare il Colosseo",    "travel", "A1"),
    ("Onde compro os ingressos",     "Dove si comprano i biglietti?",  "travel", "A2"),
    ("Ha uma vista bonita",          "C'è una bella vista",            "travel", "A1"),
    ("Minha mala nao chegou",        "Il mio bagaglio non è arrivato", "travel", "A2"),

    # ── daily-routine ───────────────────────────────────────────────────────
    ("Acordo as sete",               "Mi sveglio alle sette",          "daily-routine", "A1"),
    ("Tomo cafe da manha",           "Faccio colazione",               "daily-routine", "A1"),
    ("Vou trabalhar",                "Vado al lavoro",                 "daily-routine", "A1"),
    ("Estudo italiano todo dia",     "Studio italiano ogni giorno",    "daily-routine", "A1"),
    ("Vou dormir",                   "Vado a dormire",                 "daily-routine", "A1"),
    ("De manha",                     "Di mattina",                     "daily-routine", "A1"),
    ("A noite",                      "Di sera",                        "daily-routine", "A1"),
    ("Todo dia",                     "Ogni giorno",                    "daily-routine", "A1"),
    ("Nos fins de semana",           "Nel weekend",                    "daily-routine", "A2"),
    ("Normalmente",                  "Di solito",                      "daily-routine", "A1"),
    ("Gosto de cozinhar",            "Mi piace cucinare",              "daily-routine", "A2"),
    ("Pratico esporte",              "Faccio sport",                   "daily-routine", "A2"),

    # ── housing ─────────────────────────────────────────────────────────────
    ("Onde voce mora",               "Dove abiti?",                    "housing", "A1"),
    ("Moro em Roma",                 "Abito a Roma",                   "housing", "A1"),
    ("Tenho um apartamento",         "Ho un appartamento",             "housing", "A1"),
    ("Quanto custa o aluguel",       "Quanto costa l'affitto?",        "housing", "A1"),
    ("Duas quartos e uma cozinha",   "Due camere e una cucina",        "housing", "A2"),
    ("O apartamento e pequeno mas aconchegante","L'appartamento è piccolo ma accogliente","housing", "A2"),
    ("Procuro um apartamento",       "Sto cercando un appartamento",   "housing", "A2"),
    ("Perto do centro",              "Vicino al centro",               "housing", "A1"),

    # ── work ────────────────────────────────────────────────────────────────
    ("Tenho uma reuniao agora",      "Ho una riunione adesso",         "work", "A2"),
    ("Posso ajudar",                 "Posso aiutare?",                 "work", "A1"),
    ("Entendi",                      "Ho capito",                      "work", "A1"),
    ("Vou terminar hoje",            "Finisco oggi",                   "work", "A2"),
    ("Preciso de mais tempo",        "Ho bisogno di più tempo",        "work", "A2"),
    ("Esta e minha apresentacao",    "Questa è la mia presentazione",  "work", "A2"),
    ("Qual e o prazo",               "Qual è la scadenza?",            "work", "A2"),
    ("Trabalho em equipe",           "Lavoro in team",                 "work", "A2"),
]


# ─── Lessons config ──────────────────────────────────────────────────────────

LESSONS_CONFIG = [
    # (day_number, title, scenario_slug, difficulty)
    (1,  "Primeiras palavras",          "social",        "A1"),
    (2,  "Apresentacoes",               "social",        "A1"),
    (3,  "No restaurante",              "restaurant",    "A1"),
    (4,  "Comida e bebida",             "restaurant",    "A1"),
    (5,  "No mercado",                  "market",        "A1"),
    (6,  "Compras e precos",            "market",        "A1"),
    (7,  "Transporte e direcoes",       "transport",     "A1"),
    (8,  "Como chegar",                 "transport",     "A1"),
    (9,  "Saude basica",                "health",        "A1"),
    (10, "Emergencias",                 "health",        "A1"),
    (11, "Vida cotidiana",              "daily-routine", "A1"),
    (12, "Habitos e rotina",            "daily-routine", "A1"),
    (13, "Onde voce mora",              "housing",       "A1"),
    (14, "Viagem e hotel",              "travel",        "A1"),
    (15, "Revisao A1",                  "social",        "A1"),
    (16, "Conversas do dia a dia",      "social",        "A2"),
    (17, "Restaurante avancado",        "restaurant",    "A2"),
    (18, "Compras e trocas",            "market",        "A2"),
    (19, "Transporte urbano",           "transport",     "A2"),
    (20, "Saude e consultas",           "health",        "A2"),
    (21, "Casa e aluguel",              "housing",       "A2"),
    (22, "Turismo e visitas",           "travel",        "A2"),
    (23, "Trabalho e reunioes",         "work",          "A2"),
    (24, "Fins de semana",              "daily-routine", "A2"),
    (25, "Revisao A2",                  "social",        "A2"),
]


def seed_it_phrases() -> dict:
    pt, _ = Language.objects.get_or_create(code="PT", defaults={"name": LANGUAGE_NAMES["PT"]})
    it, _ = Language.objects.get_or_create(code="IT", defaults={"name": LANGUAGE_NAMES["IT"]})

    scenarios: dict[str, object] = {}
    from content.seeds.seed_complete_courses import SCENARIOS as SCENARIO_DEFS
    for slug, title, desc in SCENARIO_DEFS:
        obj, _ = Scenario.objects.get_or_create(slug=slug, defaults={"title": title, "description": desc})
        scenarios[slug] = obj

    phrases_created = 0
    phrase_map: dict[tuple, object] = {}

    for source_text, target_text, scenario_slug, difficulty in PHRASES:
        scenario = scenarios.get(scenario_slug)
        phrase, created = Phrase.objects.get_or_create(
            source_language=pt,
            target_language=it,
            source_text=source_text,
            target_text=target_text,
            defaults={
                "scenario": scenario,
                "difficulty": difficulty,
                "category": scenario_slug,
            },
        )
        if created:
            phrases_created += 1
        phrase_map[(scenario_slug, difficulty, source_text)] = phrase

    lessons_created = 0
    study_days_created = 0

    for day_number, title, scenario_slug, difficulty in LESSONS_CONFIG:
        scenario = scenarios[scenario_slug]

        lesson, lesson_created = Lesson.objects.get_or_create(
            title=title,
            day_number=day_number,
            scenario=scenario,
        )
        if lesson_created:
            lessons_created += 1

        lesson_phrases = [
            p for (s, d, _), p in phrase_map.items()
            if s == scenario_slug and d == difficulty
        ][:8]
        lesson.phrases.set(lesson_phrases)

        _, sd_created = StudyDay.objects.get_or_create(
            day_number=day_number,
            lesson=lesson,
            defaults={"is_active": True},
        )
        if sd_created:
            study_days_created += 1

    return {
        "phrases": phrases_created,
        "lessons": lessons_created,
        "study_days": study_days_created,
    }
