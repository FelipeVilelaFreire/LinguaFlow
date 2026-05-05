from __future__ import annotations

from content.models import Language, Lesson, Phrase, Scenario, StudyDay


COURSES = [
    ("PT", "DE"),
    ("EN", "DE"),
    ("PT", "ES"),
]

LEVELS = ["A1", "A2", "B1"]

LANGUAGE_NAMES = {
    "PT": "Portugues",
    "EN": "Ingles",
    "DE": "Alemao",
    "ES": "Espanhol",
}

SCENARIOS = [
    ("restaurant", "Restaurante", "Pedir comida, pagar e resolver situacoes simples."),
    ("market", "Mercado", "Comprar itens, perguntar precos e quantidades."),
    ("transport", "Transporte", "Usar trem, onibus, taxi e pedir direcoes."),
    ("university", "Universidade", "Conversas sobre aula, estudo, tarefas e rotina academica."),
    ("housing", "Moradia", "Aluguel, manutencao, vizinhos e vida em casa."),
    ("work", "Trabalho", "Reunioes, prazos, tarefas, feedback e comunicacao profissional."),
    ("health", "Saude", "Consultas, sintomas, farmacia, emergencia e cuidados pessoais."),
    ("travel", "Viagem", "Hotel, aeroporto, turismo, reservas e problemas de viagem."),
    ("social", "Vida social", "Conhecer pessoas, convites, opinioes e pequenos conflitos."),
    ("services", "Servicos", "Banco, correio, documentos, atendimento e suporte."),
    ("daily-routine", "Rotina diaria", "Casa, horarios, habitos, planos e organizacao pessoal."),
    ("technology", "Tecnologia", "Celular, internet, apps, suporte tecnico e seguranca digital."),
]

LESSON_FOCUS = {
    "A1": [
        "basic needs",
        "simple questions",
        "polite requests",
        "prices and time",
        "directions and location",
        "common verbs",
        "short answers",
        "real-life mini dialogue",
        "memory checkpoint",
        "quick review",
    ],
    "A2": [
        "past experiences",
        "specific problems",
        "preferences and reasons",
        "planning and scheduling",
        "comparisons and options",
        "follow-up questions",
        "explaining choices",
        "short story practice",
        "memory checkpoint",
        "situational review",
    ],
    "B1": [
        "explaining context",
        "negotiating solutions",
        "giving opinions",
        "handling complications",
        "summarizing outcomes",
        "cause and consequence",
        "polite disagreement",
        "extended response",
        "memory checkpoint",
        "fluency review",
    ],
}

VOCAB = {
    "restaurant": {
        "items": {
            "PT": ["agua", "cardapio", "mesa", "conta", "prato", "sobremesa"],
            "EN": ["water", "menu", "table", "bill", "dish", "dessert"],
            "DE": ["Wasser", "Speisekarte", "Tisch", "Rechnung", "Gericht", "Nachtisch"],
            "ES": ["agua", "menu", "mesa", "cuenta", "plato", "postre"],
        },
        "places": {
            "PT": ["restaurante", "mesa", "cozinha", "caixa", "entrada", "banheiro"],
            "EN": ["restaurant", "table", "kitchen", "cash register", "entrance", "bathroom"],
            "DE": ["Restaurant", "Tisch", "Kuche", "Kasse", "Eingang", "Toilette"],
            "ES": ["restaurante", "mesa", "cocina", "caja", "entrada", "bano"],
        },
        "problems": {
            "PT": ["a comida esta fria", "a conta esta errada", "o pedido atrasou", "nao tenho reserva", "sou alergico", "o prato esta picante"],
            "EN": ["the food is cold", "the bill is wrong", "the order is late", "I do not have a reservation", "I am allergic", "the dish is spicy"],
            "DE": ["das Essen ist kalt", "die Rechnung ist falsch", "die Bestellung ist spat", "ich habe keine Reservierung", "ich habe eine Allergie", "das Gericht ist scharf"],
            "ES": ["la comida esta fria", "la cuenta esta mal", "el pedido tarda", "no tengo reserva", "soy alergico", "el plato esta picante"],
        },
    },
    "market": {
        "items": {
            "PT": ["pao", "leite", "tomates", "queijo", "arroz", "frutas"],
            "EN": ["bread", "milk", "tomatoes", "cheese", "rice", "fruit"],
            "DE": ["Brot", "Milch", "Tomaten", "Kase", "Reis", "Obst"],
            "ES": ["pan", "leche", "tomates", "queso", "arroz", "fruta"],
        },
        "places": {
            "PT": ["mercado", "padaria", "caixa", "corredor", "feira", "prateleira"],
            "EN": ["market", "bakery", "checkout", "aisle", "street market", "shelf"],
            "DE": ["Markt", "Backerei", "Kasse", "Gang", "Wochenmarkt", "Regal"],
            "ES": ["mercado", "panaderia", "caja", "pasillo", "feria", "estante"],
        },
        "problems": {
            "PT": ["o preco esta alto", "nao encontro o produto", "o caixa esta fechado", "esqueci a sacola", "o cartao nao passa", "o produto venceu"],
            "EN": ["the price is high", "I cannot find the product", "the checkout is closed", "I forgot the bag", "the card does not work", "the product expired"],
            "DE": ["der Preis ist hoch", "ich finde das Produkt nicht", "die Kasse ist geschlossen", "ich habe die Tute vergessen", "die Karte funktioniert nicht", "das Produkt ist abgelaufen"],
            "ES": ["el precio es alto", "no encuentro el producto", "la caja esta cerrada", "olvide la bolsa", "la tarjeta no funciona", "el producto vencio"],
        },
    },
    "transport": {
        "items": {
            "PT": ["bilhete", "trem", "onibus", "taxi", "mapa", "passe mensal"],
            "EN": ["ticket", "train", "bus", "taxi", "map", "monthly pass"],
            "DE": ["Fahrkarte", "Zug", "Bus", "Taxi", "Karte", "Monatskarte"],
            "ES": ["billete", "tren", "autobus", "taxi", "mapa", "abono mensual"],
        },
        "places": {
            "PT": ["estacao", "plataforma", "aeroporto", "centro", "parada", "saida"],
            "EN": ["station", "platform", "airport", "downtown", "stop", "exit"],
            "DE": ["Bahnhof", "Bahnsteig", "Flughafen", "Zentrum", "Haltestelle", "Ausgang"],
            "ES": ["estacion", "anden", "aeropuerto", "centro", "parada", "salida"],
        },
        "problems": {
            "PT": ["o trem atrasou", "perdi o onibus", "estou perdido", "a linha mudou", "o bilhete nao funciona", "a plataforma mudou"],
            "EN": ["the train is late", "I missed the bus", "I am lost", "the line changed", "the ticket does not work", "the platform changed"],
            "DE": ["der Zug hat Verspatung", "ich habe den Bus verpasst", "ich habe mich verlaufen", "die Linie hat sich geandert", "die Fahrkarte funktioniert nicht", "der Bahnsteig hat sich geandert"],
            "ES": ["el tren esta retrasado", "perdi el autobus", "estoy perdido", "la linea cambio", "el billete no funciona", "el anden cambio"],
        },
    },
    "university": {
        "items": {
            "PT": ["aula", "tarefa", "prova", "biblioteca", "professor", "horario"],
            "EN": ["class", "assignment", "exam", "library", "professor", "schedule"],
            "DE": ["Unterricht", "Aufgabe", "Prufung", "Bibliothek", "Professor", "Stundenplan"],
            "ES": ["clase", "tarea", "examen", "biblioteca", "profesor", "horario"],
        },
        "places": {
            "PT": ["sala", "campus", "biblioteca", "secretaria", "laboratorio", "auditorio"],
            "EN": ["classroom", "campus", "library", "office", "laboratory", "auditorium"],
            "DE": ["Raum", "Campus", "Bibliothek", "Sekretariat", "Labor", "Horsaal"],
            "ES": ["aula", "campus", "biblioteca", "secretaria", "laboratorio", "auditorio"],
        },
        "problems": {
            "PT": ["nao entendo a tarefa", "perdi o prazo", "a sala mudou", "o link nao abre", "preciso imprimir", "a prova foi dificil"],
            "EN": ["I do not understand the assignment", "I missed the deadline", "the room changed", "the link does not open", "I need to print", "the exam was hard"],
            "DE": ["ich verstehe die Aufgabe nicht", "ich habe die Frist verpasst", "der Raum hat sich geandert", "der Link offnet sich nicht", "ich muss drucken", "die Prufung war schwer"],
            "ES": ["no entiendo la tarea", "perdi la fecha limite", "el aula cambio", "el enlace no abre", "necesito imprimir", "el examen fue dificil"],
        },
    },
    "housing": {
        "items": {
            "PT": ["apartamento", "quarto", "aluguel", "chave", "contrato", "internet"],
            "EN": ["apartment", "room", "rent", "key", "contract", "internet"],
            "DE": ["Wohnung", "Zimmer", "Miete", "Schlussel", "Vertrag", "Internet"],
            "ES": ["apartamento", "habitacion", "alquiler", "llave", "contrato", "internet"],
        },
        "places": {
            "PT": ["apartamento", "predio", "cozinha", "banheiro", "bairro", "entrada"],
            "EN": ["apartment", "building", "kitchen", "bathroom", "neighborhood", "entrance"],
            "DE": ["Wohnung", "Gebaude", "Kuche", "Bad", "Gegend", "Eingang"],
            "ES": ["apartamento", "edificio", "cocina", "bano", "barrio", "entrada"],
        },
        "problems": {
            "PT": ["a internet nao funciona", "a luz apagou", "o aluguel subiu", "a chave sumiu", "o aquecimento falhou", "o vizinho faz barulho"],
            "EN": ["the internet does not work", "the light went out", "the rent increased", "the key disappeared", "the heating failed", "the neighbor is noisy"],
            "DE": ["das Internet funktioniert nicht", "das Licht ist ausgegangen", "die Miete ist gestiegen", "der Schlussel ist weg", "die Heizung funktioniert nicht", "der Nachbar ist laut"],
            "ES": ["internet no funciona", "la luz se apago", "el alquiler subio", "la llave desaparecio", "la calefaccion fallo", "el vecino hace ruido"],
        },
    },
}

GENERIC_SCENARIOS = ["work", "health", "travel", "social", "services", "daily-routine", "technology"]

GENERIC_ITEMS = {
    "work": ("reuniao", "meeting", "Besprechung", "reunion"),
    "health": ("consulta", "appointment", "Termin", "consulta"),
    "travel": ("reserva", "reservation", "Reservierung", "reserva"),
    "social": ("convite", "invitation", "Einladung", "invitacion"),
    "services": ("documento", "document", "Dokument", "documento"),
    "daily-routine": ("horario", "schedule", "Zeitplan", "horario"),
    "technology": ("aplicativo", "app", "App", "aplicacion"),
}

GENERIC_PLACES = {
    "work": ("escritorio", "office", "Buro", "oficina"),
    "health": ("clinica", "clinic", "Klinik", "clinica"),
    "travel": ("hotel", "hotel", "Hotel", "hotel"),
    "social": ("festa", "party", "Party", "fiesta"),
    "services": ("banco", "bank", "Bank", "banco"),
    "daily-routine": ("casa", "home", "Zuhause", "casa"),
    "technology": ("site", "website", "Webseite", "sitio web"),
}

GENERIC_PROBLEMS = {
    "work": ("o prazo esta curto", "the deadline is tight", "die Frist ist knapp", "el plazo es corto"),
    "health": ("nao me sinto bem", "I do not feel well", "ich fuhle mich nicht gut", "no me siento bien"),
    "travel": ("minha reserva nao aparece", "my reservation does not appear", "meine Reservierung erscheint nicht", "mi reserva no aparece"),
    "social": ("nao posso chegar cedo", "I cannot arrive early", "ich kann nicht fruh kommen", "no puedo llegar temprano"),
    "services": ("preciso atualizar meus dados", "I need to update my details", "ich muss meine Daten aktualisieren", "necesito actualizar mis datos"),
    "daily-routine": ("estou sem tempo", "I am short on time", "ich habe wenig Zeit", "tengo poco tiempo"),
    "technology": ("a senha nao funciona", "the password does not work", "das Passwort funktioniert nicht", "la contrasena no funciona"),
}


def expand_vocab() -> None:
    for slug in GENERIC_SCENARIOS:
        pt_item, en_item, de_item, es_item = GENERIC_ITEMS[slug]
        pt_place, en_place, de_place, es_place = GENERIC_PLACES[slug]
        pt_problem, en_problem, de_problem, es_problem = GENERIC_PROBLEMS[slug]
        VOCAB[slug] = {
            "items": {"PT": [pt_item] * 6, "EN": [en_item] * 6, "DE": [de_item] * 6, "ES": [es_item] * 6},
            "places": {"PT": [pt_place] * 6, "EN": [en_place] * 6, "DE": [de_place] * 6, "ES": [es_place] * 6},
            "problems": {"PT": [pt_problem] * 6, "EN": [en_problem] * 6, "DE": [de_problem] * 6, "ES": [es_problem] * 6},
        }


PATTERNS = {
    "A1": [
        ("I want {item}.", "Ich mochte {item}.", "Quiero {item}."),
        ("Where is the {place}?", "Wo ist {place}?", "Donde esta {place}?"),
        ("I need help with the {item}.", "Ich brauche Hilfe mit {item}.", "Necesito ayuda con {item}."),
        ("How much does the {item} cost?", "Wie viel kostet {item}?", "Cuanto cuesta {item}?"),
        ("I have a question about the {item}.", "Ich habe eine Frage zu {item}.", "Tengo una pregunta sobre {item}."),
        ("Can you repeat that, please?", "Konnen Sie das bitte wiederholen?", "Puede repetir eso, por favor?"),
        ("I do not understand.", "Ich verstehe nicht.", "No entiendo."),
        ("I am looking for the {place}.", "Ich suche {place}.", "Busco {place}."),
        ("I would like to pay now.", "Ich mochte jetzt bezahlen.", "Me gustaria pagar ahora."),
        ("This is important for me.", "Das ist wichtig fur mich.", "Esto es importante para mi."),
        ("Can you help me today?", "Konnen Sie mir heute helfen?", "Puede ayudarme hoy?"),
        ("Thank you for your help.", "Danke fur Ihre Hilfe.", "Gracias por su ayuda."),
    ],
    "A2": [
        ("Yesterday I had a problem: {problem}.", "Gestern hatte ich ein Problem: {problem}.", "Ayer tuve un problema: {problem}."),
        ("I would like to know if the {item} is available.", "Ich mochte wissen, ob {item} verfugbar ist.", "Me gustaria saber si {item} esta disponible."),
        ("I prefer the option near the {place}.", "Ich bevorzuge die Option in der Nahe von {place}.", "Prefiero la opcion cerca de {place}."),
        ("Could we solve this before tomorrow?", "Konnten wir das vor morgen losen?", "Podriamos resolver esto antes de manana?"),
        ("I need a simple explanation.", "Ich brauche eine einfache Erklarung.", "Necesito una explicacion sencilla."),
        ("The first option is better, but it is more expensive.", "Die erste Option ist besser, aber sie ist teurer.", "La primera opcion es mejor, pero es mas cara."),
        ("I already tried to fix the problem.", "Ich habe schon versucht, das Problem zu losen.", "Ya intente resolver el problema."),
        ("Can you show me another possibility?", "Konnen Sie mir eine andere Moglichkeit zeigen?", "Puede mostrarme otra posibilidad?"),
        ("I have time this afternoon.", "Ich habe heute Nachmittag Zeit.", "Tengo tiempo esta tarde."),
        ("Please send me the information by email.", "Bitte senden Sie mir die Informationen per E-Mail.", "Por favor envieme la informacion por correo."),
        ("I need to change the appointment.", "Ich muss den Termin andern.", "Necesito cambiar la cita."),
        ("That works for me.", "Das passt fur mich.", "Eso me sirve."),
    ],
    "B1": [
        ("The main issue is that {problem}, so I need a practical solution.", "Das Hauptproblem ist, dass {problem}, deshalb brauche ich eine praktische Losung.", "El problema principal es que {problem}, por eso necesito una solucion practica."),
        ("In my opinion, the best option is connected to the {place}.", "Meiner Meinung nach hangt die beste Option mit {place} zusammen.", "En mi opinion, la mejor opcion esta relacionada con {place}."),
        ("I understand the situation, but I would like to discuss the details.", "Ich verstehe die Situation, aber ich mochte die Details besprechen.", "Entiendo la situacion, pero me gustaria hablar de los detalles."),
        ("If we cannot solve it today, we should make a clear plan.", "Wenn wir es heute nicht losen konnen, sollten wir einen klaren Plan machen.", "Si no podemos resolverlo hoy, deberiamos hacer un plan claro."),
        ("I have already compared the options and this one seems more reliable.", "Ich habe die Optionen schon verglichen und diese scheint zuverlassiger zu sein.", "Ya compare las opciones y esta parece mas confiable."),
        ("Could you explain what changed and what I should do next?", "Konnten Sie erklaren, was sich geandert hat und was ich als Nachstes tun soll?", "Podria explicar que cambio y que debo hacer ahora?"),
        ("I am trying to avoid the same problem in the future.", "Ich versuche, dasselbe Problem in Zukunft zu vermeiden.", "Estoy intentando evitar el mismo problema en el futuro."),
        ("From my perspective, the deadline is realistic if we start now.", "Aus meiner Sicht ist die Frist realistisch, wenn wir jetzt anfangen.", "Desde mi perspectiva, el plazo es realista si empezamos ahora."),
        ("I would appreciate a written confirmation.", "Ich wurde eine schriftliche Bestatigung schatzen.", "Agradeceria una confirmacion por escrito."),
        ("Let me summarize what we agreed on.", "Lassen Sie mich zusammenfassen, was wir vereinbart haben.", "Permitime resumir lo que acordamos."),
        ("This solution is not perfect, but it is acceptable for now.", "Diese Losung ist nicht perfekt, aber sie ist vorerst akzeptabel.", "Esta solucion no es perfecta, pero es aceptable por ahora."),
        ("The next step should be simple and measurable.", "Der nachste Schritt sollte einfach und messbar sein.", "El siguiente paso debe ser simple y medible."),
    ],
}


PT_SOURCES = {
    "A1": [
        "Eu quero {item}.",
        "Onde fica {place}?",
        "Eu preciso de ajuda com {item}.",
        "Quanto custa {item}?",
        "Tenho uma pergunta sobre {item}.",
        "Pode repetir, por favor?",
        "Eu nao entendo.",
        "Estou procurando {place}.",
        "Eu gostaria de pagar agora.",
        "Isso e importante para mim.",
        "Pode me ajudar hoje?",
        "Obrigado pela ajuda.",
    ],
    "A2": [
        "Ontem tive um problema: {problem}.",
        "Eu gostaria de saber se {item} esta disponivel.",
        "Eu prefiro a opcao perto de {place}.",
        "Podemos resolver isso antes de amanha?",
        "Eu preciso de uma explicacao simples.",
        "A primeira opcao e melhor, mas e mais cara.",
        "Eu ja tentei resolver o problema.",
        "Pode me mostrar outra possibilidade?",
        "Tenho tempo hoje a tarde.",
        "Por favor, envie as informacoes por email.",
        "Eu preciso mudar o horario.",
        "Isso funciona para mim.",
    ],
    "B1": [
        "O problema principal e que {problem}, entao preciso de uma solucao pratica.",
        "Na minha opiniao, a melhor opcao esta ligada a {place}.",
        "Eu entendo a situacao, mas gostaria de discutir os detalhes.",
        "Se nao conseguirmos resolver hoje, devemos fazer um plano claro.",
        "Eu ja comparei as opcoes e esta parece mais confiavel.",
        "Pode explicar o que mudou e o que devo fazer agora?",
        "Estou tentando evitar o mesmo problema no futuro.",
        "Do meu ponto de vista, o prazo e realista se comecarmos agora.",
        "Eu agradeceria uma confirmacao por escrito.",
        "Deixe-me resumir o que combinamos.",
        "Essa solucao nao e perfeita, mas e aceitavel por enquanto.",
        "O proximo passo deve ser simples e mensuravel.",
    ],
}


def source_patterns(source_code: str, level: str) -> list[str]:
    if source_code == "PT":
        return PT_SOURCES[level]
    return [item[0] for item in PATTERNS[level]]


def target_patterns(target_code: str, level: str) -> list[str]:
    index = 1 if target_code == "DE" else 2
    return [item[index] for item in PATTERNS[level]]


def format_phrase(template: str, vocab: dict[str, list[str]], language: str, offset: int) -> str:
    item = vocab["items"][language][offset % len(vocab["items"][language])]
    place = vocab["places"][language][offset % len(vocab["places"][language])]
    problem = vocab["problems"][language][offset % len(vocab["problems"][language])]
    return template.format(item=item, place=place, problem=problem)


def ensure_languages() -> dict[str, Language]:
    return {
        code: Language.objects.update_or_create(code=code, defaults={"name": name})[0]
        for code, name in LANGUAGE_NAMES.items()
    }


def ensure_scenarios() -> None:
    for slug, title, description in SCENARIOS:
        Scenario.objects.update_or_create(slug=slug, defaults={"title": title, "description": description})


def cleanup_generated_courses(languages: dict[str, Language]) -> None:
    for source_code, target_code in COURSES:
        for level in LEVELS:
            Lesson.objects.filter(title__startswith=f"{source_code}-{target_code} {level}").delete()
            Phrase.objects.filter(
                source_language=languages[source_code],
                target_language=languages[target_code],
                difficulty=level,
            ).delete()


def seed_complete_courses() -> dict[str, int]:
    expand_vocab()
    ensure_scenarios()
    languages = ensure_languages()
    cleanup_generated_courses(languages)
    totals = {"phrases": 0, "lessons": 0, "study_days": 0}

    for source_code, target_code in COURSES:
        for level in LEVELS:
            day_number = 1
            for scenario_slug, _, _ in SCENARIOS:
                scenario = Scenario.objects.get(slug=scenario_slug)
                vocab = VOCAB[scenario_slug]
                src_templates = source_patterns(source_code, level)
                tgt_templates = target_patterns(target_code, level)
                focus_items = LESSON_FOCUS[level]

                for lesson_index, focus in enumerate(focus_items, start=1):
                    phrase_objects = []
                    for phrase_index in range(12):
                        template_index = (phrase_index + lesson_index - 1) % len(src_templates)
                        offset = phrase_index + (lesson_index * 2)
                        source_text = format_phrase(src_templates[template_index], vocab, source_code, offset)
                        target_text = format_phrase(tgt_templates[template_index], vocab, target_code, offset)
                        phrase, created = Phrase.objects.update_or_create(
                            source_language=languages[source_code],
                            target_language=languages[target_code],
                            source_text=source_text,
                            target_text=target_text,
                            defaults={"category": scenario.title, "scenario": scenario, "difficulty": level},
                        )
                        phrase_objects.append(phrase)
                        totals["phrases"] += int(created)

                    lesson, created_lesson = Lesson.objects.update_or_create(
                        title=f"{source_code}-{target_code} {level} Day {day_number:03d}: {scenario.title} - {focus}",
                        defaults={
                            "day_number": day_number,
                            "scenario": scenario,
                            "video_title": f"{target_code} {level}: {scenario.title} - {focus}",
                            "video_url": f"https://www.youtube.com/results?search_query={target_code.lower()}+{level.lower()}+{scenario.slug}+phrases",
                            "video_duration": "~12 min",
                        },
                    )
                    lesson.phrases.set(phrase_objects)
                    totals["lessons"] += int(created_lesson)

                    _, created_day = StudyDay.objects.update_or_create(
                        lesson=lesson,
                        defaults={"day_number": day_number, "is_active": day_number == 1},
                    )
                    totals["study_days"] += int(created_day)
                    day_number += 1

    return totals
