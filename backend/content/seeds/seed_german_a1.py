from content.models import Goal, Language, Lesson, Phrase, Scenario, StudyDay

PHRASES = {
    "restaurant": [
        ("Eu gostaria de uma água.", "Ich hätte gern ein Wasser."),
        ("A conta, por favor.", "Die Rechnung, bitte."),
        ("Tem uma mesa livre?", "Haben Sie einen freien Tisch?"),
        ("Eu quero pedir agora.", "Ich möchte jetzt bestellen."),
        ("Sem cebola, por favor.", "Ohne Zwiebeln, bitte."),
        ("Isso estava muito bom.", "Das war sehr gut."),
    ],
    "market": [
        ("Quanto custa isso?", "Wie viel kostet das?"),
        ("Eu preciso de pão.", "Ich brauche Brot."),
        ("Onde fica o leite?", "Wo ist die Milch?"),
        ("Eu pago com cartão.", "Ich zahle mit Karte."),
        ("Você tem uma sacola?", "Haben Sie eine Tüte?"),
        ("Isso é tudo.", "Das ist alles."),
    ],
    "transport": [
        ("Onde fica a estação?", "Wo ist der Bahnhof?"),
        ("Eu preciso de um bilhete.", "Ich brauche eine Fahrkarte."),
        ("Esse ônibus vai ao centro?", "Fährt dieser Bus ins Zentrum?"),
        ("Eu desço aqui.", "Ich steige hier aus."),
        ("Quando sai o trem?", "Wann fährt der Zug?"),
        ("Está longe daqui?", "Ist es weit von hier?"),
    ],
    "university": [
        ("Onde é a sala?", "Wo ist der Raum?"),
        ("Eu tenho aula hoje.", "Ich habe heute Unterricht."),
        ("Você pode me ajudar?", "Kannst du mir helfen?"),
        ("Eu não entendo a tarefa.", "Ich verstehe die Aufgabe nicht."),
        ("A prova é amanhã.", "Die Prüfung ist morgen."),
        ("Eu estudo alemão.", "Ich lerne Deutsch."),
    ],
    "housing": [
        ("Eu procuro um apartamento.", "Ich suche eine Wohnung."),
        ("O aluguel é caro.", "Die Miete ist teuer."),
        ("A internet não funciona.", "Das Internet funktioniert nicht."),
        ("Onde está a chave?", "Wo ist der Schlüssel?"),
        ("O quarto é pequeno.", "Das Zimmer ist klein."),
        ("Eu moro com amigos.", "Ich wohne mit Freunden."),
    ],
}

EXTRA_PHRASES = {
    "restaurant": [
        ("Eu tenho uma reserva.", "Ich habe eine Reservierung."),
        ("Para duas pessoas, por favor.", "Fur zwei Personen, bitte."),
        ("Eu gostaria do cardapio.", "Ich hatte gern die Speisekarte."),
        ("O que voce recomenda?", "Was empfehlen Sie?"),
        ("Eu sou vegetariano.", "Ich bin Vegetarier."),
        ("Eu gostaria de pagar.", "Ich mochte bezahlen."),
        ("Pode trazer mais agua?", "Konnen Sie mehr Wasser bringen?"),
        ("A comida esta fria.", "Das Essen ist kalt."),
        ("Esta muito picante?", "Ist es sehr scharf?"),
        ("Eu levo para viagem.", "Ich nehme es zum Mitnehmen."),
        ("O cafe esta incluso?", "Ist der Kaffee inklusive?"),
        ("Foi excelente, obrigado.", "Es war ausgezeichnet, danke."),
        ("Eu quero uma sopa.", "Ich mochte eine Suppe."),
        ("Tem sobremesa?", "Gibt es Nachtisch?"),
        ("Mais uma cerveja, por favor.", "Noch ein Bier, bitte."),
        ("Onde fica o banheiro?", "Wo ist die Toilette?"),
        ("Eu tenho alergia.", "Ich habe eine Allergie."),
        ("Sem carne, por favor.", "Ohne Fleisch, bitte."),
        ("A mesa perto da janela.", "Der Tisch am Fenster."),
        ("Podemos sentar aqui?", "Konnen wir hier sitzen?"),
        ("Eu gostaria de uma salada.", "Ich hatte gern einen Salat."),
        ("A conta separada, por favor.", "Getrennt bezahlen, bitte."),
        ("Aceita cartao?", "Akzeptieren Sie Karte?"),
        ("Eu preciso de um guardanapo.", "Ich brauche eine Serviette."),
        ("O prato do dia, por favor.", "Das Tagesgericht, bitte."),
        ("Esta delicioso.", "Es ist lecker."),
        ("Eu ainda estou escolhendo.", "Ich wahle noch."),
        ("Pode repetir, por favor?", "Konnen Sie das bitte wiederholen?"),
        ("Eu quero algo pequeno.", "Ich mochte etwas Kleines."),
        ("Estamos prontos para pedir.", "Wir sind bereit zu bestellen."),
    ],
    "market": [
        ("Eu estou procurando tomates.", "Ich suche Tomaten."),
        ("Onde ficam as frutas?", "Wo ist das Obst?"),
        ("Isso esta em promocao?", "Ist das im Angebot?"),
        ("Eu quero meio quilo.", "Ich mochte ein halbes Kilo."),
        ("Pode pesar isso?", "Konnen Sie das wiegen?"),
        ("Eu preciso de ovos.", "Ich brauche Eier."),
        ("O caixa esta aberto?", "Ist die Kasse offen?"),
        ("Eu esqueci minha sacola.", "Ich habe meine Tute vergessen."),
        ("Tem leite sem lactose?", "Gibt es laktosefreie Milch?"),
        ("Isso e fresco?", "Ist das frisch?"),
        ("Eu quero queijo.", "Ich mochte Kase."),
        ("Onde fica a padaria?", "Wo ist die Backerei?"),
        ("Eu pago em dinheiro.", "Ich zahle bar."),
        ("A fila esta longa.", "Die Schlange ist lang."),
        ("Eu preciso de arroz.", "Ich brauche Reis."),
        ("Tem desconto?", "Gibt es Rabatt?"),
        ("Eu so estou olhando.", "Ich schaue nur."),
        ("Isso e caro demais.", "Das ist zu teuer."),
        ("Pode me ajudar?", "Konnen Sie mir helfen?"),
        ("Eu quero uma garrafa de agua.", "Ich mochte eine Flasche Wasser."),
        ("Onde estao os legumes?", "Wo ist das Gemuse?"),
        ("Preciso de uma nota fiscal.", "Ich brauche einen Beleg."),
        ("Isso vence quando?", "Wann lauft das ab?"),
        ("Eu levo este.", "Ich nehme das."),
        ("Tem pao integral?", "Gibt es Vollkornbrot?"),
        ("A maquina nao funciona.", "Das Gerat funktioniert nicht."),
        ("Quanto devo?", "Wie viel schulde ich?"),
        ("Pode trocar isso?", "Konnen Sie das umtauschen?"),
        ("Eu quero uma pequena quantidade.", "Ich mochte eine kleine Menge."),
        ("Obrigado pela ajuda.", "Danke fur die Hilfe."),
    ],
    "transport": [
        ("Onde compro o bilhete?", "Wo kaufe ich die Fahrkarte?"),
        ("Este trem esta atrasado.", "Dieser Zug hat Verspatung."),
        ("Qual plataforma?", "Welcher Bahnsteig?"),
        ("Eu preciso ir ao aeroporto.", "Ich muss zum Flughafen."),
        ("O metro esta lotado.", "Die U-Bahn ist voll."),
        ("Eu perdi o onibus.", "Ich habe den Bus verpasst."),
        ("Quando chega o proximo?", "Wann kommt der nachste?"),
        ("Eu tenho um passe mensal.", "Ich habe eine Monatskarte."),
        ("Este lugar esta livre?", "Ist dieser Platz frei?"),
        ("Preciso trocar de linha.", "Ich muss umsteigen."),
        ("A parada e aqui?", "Ist die Haltestelle hier?"),
        ("Quanto tempo demora?", "Wie lange dauert es?"),
        ("Eu vou de bicicleta.", "Ich fahre mit dem Fahrrad."),
        ("Onde fica a saida?", "Wo ist der Ausgang?"),
        ("Eu preciso de informacao.", "Ich brauche Information."),
        ("Esse trem vai para Berlim?", "Fahrt dieser Zug nach Berlin?"),
        ("Eu quero uma passagem ida e volta.", "Ich mochte eine Hin- und Ruckfahrt."),
        ("O taxi e caro.", "Das Taxi ist teuer."),
        ("Pode parar aqui?", "Konnen Sie hier halten?"),
        ("Eu estou perdido.", "Ich habe mich verlaufen."),
        ("A conexao e rapida.", "Die Verbindung ist schnell."),
        ("Preciso validar o bilhete.", "Ich muss die Fahrkarte entwerten."),
        ("Onde fica o ponto de taxi?", "Wo ist der Taxistand?"),
        ("Vou descer na proxima.", "Ich steige an der nachsten aus."),
        ("O trem foi cancelado.", "Der Zug wurde abgesagt."),
        ("Tem elevador?", "Gibt es einen Aufzug?"),
        ("Eu vou a pe.", "Ich gehe zu Fuss."),
        ("Qual e o melhor caminho?", "Was ist der beste Weg?"),
        ("A estacao fica perto.", "Der Bahnhof ist in der Nahe."),
        ("Eu preciso de um mapa.", "Ich brauche eine Karte."),
    ],
    "university": [
        ("Eu sou estudante novo.", "Ich bin neuer Student."),
        ("Onde fica a biblioteca?", "Wo ist die Bibliothek?"),
        ("Tenho uma pergunta.", "Ich habe eine Frage."),
        ("A aula comeca as nove.", "Der Unterricht beginnt um neun."),
        ("Eu preciso entregar o trabalho.", "Ich muss die Arbeit abgeben."),
        ("Pode falar mais devagar?", "Konnen Sie langsamer sprechen?"),
        ("Eu estudo engenharia.", "Ich studiere Ingenieurwesen."),
        ("Onde esta o professor?", "Wo ist der Professor?"),
        ("A sala esta cheia.", "Der Raum ist voll."),
        ("Eu preciso imprimir.", "Ich muss drucken."),
        ("O prazo e hoje.", "Die Frist ist heute."),
        ("Eu tenho uma reuniao.", "Ich habe ein Treffen."),
        ("Voce tem as anotacoes?", "Hast du die Notizen?"),
        ("Eu esqueci meu caderno.", "Ich habe mein Heft vergessen."),
        ("A prova foi dificil.", "Die Prufung war schwer."),
        ("Eu preciso estudar mais.", "Ich muss mehr lernen."),
        ("Onde fica a secretaria?", "Wo ist das Sekretariat?"),
        ("Tenho aula online.", "Ich habe Online-Unterricht."),
        ("O link nao abre.", "Der Link offnet sich nicht."),
        ("Podemos estudar juntos?", "Konnen wir zusammen lernen?"),
        ("Eu nao conheco ninguem.", "Ich kenne niemanden."),
        ("O campus e grande.", "Der Campus ist gross."),
        ("Preciso do horario.", "Ich brauche den Stundenplan."),
        ("A tarefa e para amanha.", "Die Aufgabe ist fur morgen."),
        ("Eu entendi a explicacao.", "Ich habe die Erklarung verstanden."),
        ("Pode corrigir minha frase?", "Konnen Sie meinen Satz korrigieren?"),
        ("Eu tenho intervalo agora.", "Ich habe jetzt Pause."),
        ("O seminario e interessante.", "Das Seminar ist interessant."),
        ("Preciso de ajuda com alemao.", "Ich brauche Hilfe mit Deutsch."),
        ("Vejo voce depois da aula.", "Ich sehe dich nach dem Unterricht."),
    ],
    "housing": [
        ("Eu quero visitar o apartamento.", "Ich mochte die Wohnung besichtigen."),
        ("Quantos quartos tem?", "Wie viele Zimmer gibt es?"),
        ("O aquecimento funciona?", "Funktioniert die Heizung?"),
        ("A cozinha e compartilhada.", "Die Kuche ist geteilt."),
        ("Quando posso entrar?", "Wann kann ich einziehen?"),
        ("O contrato e de um ano.", "Der Vertrag ist fur ein Jahr."),
        ("O deposito e alto.", "Die Kaution ist hoch."),
        ("Tem maquina de lavar?", "Gibt es eine Waschmaschine?"),
        ("O bairro e tranquilo.", "Die Gegend ist ruhig."),
        ("O quarto tem moveis.", "Das Zimmer ist mobliert."),
        ("Eu moro perto do centro.", "Ich wohne in der Nahe vom Zentrum."),
        ("A luz nao funciona.", "Das Licht funktioniert nicht."),
        ("Preciso chamar o proprietario.", "Ich muss den Vermieter anrufen."),
        ("A janela esta quebrada.", "Das Fenster ist kaputt."),
        ("O aluguel inclui agua?", "Ist Wasser in der Miete enthalten?"),
        ("Eu divido apartamento.", "Ich wohne in einer WG."),
        ("O quarto esta disponivel?", "Ist das Zimmer frei?"),
        ("Posso trazer um amigo?", "Kann ich einen Freund mitbringen?"),
        ("A internet esta lenta.", "Das Internet ist langsam."),
        ("Tem mercado perto?", "Gibt es einen Markt in der Nahe?"),
        ("O predio e antigo.", "Das Gebaude ist alt."),
        ("Preciso de uma copia da chave.", "Ich brauche eine Kopie des Schlussels."),
        ("A mudanca e no sabado.", "Der Umzug ist am Samstag."),
        ("Meu endereco mudou.", "Meine Adresse hat sich geandert."),
        ("O quarto e claro.", "Das Zimmer ist hell."),
        ("Tem vaga para bicicleta?", "Gibt es Platz fur ein Fahrrad?"),
        ("O banheiro e pequeno.", "Das Bad ist klein."),
        ("Eu gosto da localizacao.", "Ich mag die Lage."),
        ("Quando vence o aluguel?", "Wann ist die Miete fallig?"),
        ("Preciso assinar aqui?", "Muss ich hier unterschreiben?"),
    ],
}


def all_phrases_for(scenario_slug: str) -> list[tuple[str, str]]:
    combined = [*PHRASES[scenario_slug], *EXTRA_PHRASES[scenario_slug]]
    return combined[:36]


ENGLISH_PHRASES = {
    "restaurant": [
        ("I would like a water.", "Ich hÃ¤tte gern ein Wasser."),
        ("The bill, please.", "Die Rechnung, bitte."),
        ("Do you have a free table?", "Haben Sie einen freien Tisch?"),
        ("I want to order now.", "Ich mÃ¶chte jetzt bestellen."),
        ("Without onions, please.", "Ohne Zwiebeln, bitte."),
        ("That was very good.", "Das war sehr gut."),
        ("I have a reservation.", "Ich habe eine Reservierung."),
        ("For two people, please.", "Fur zwei Personen, bitte."),
        ("I would like the menu.", "Ich hatte gern die Speisekarte."),
        ("What do you recommend?", "Was empfehlen Sie?"),
        ("I am vegetarian.", "Ich bin Vegetarier."),
        ("I would like to pay.", "Ich mochte bezahlen."),
        ("Can you bring more water?", "Konnen Sie mehr Wasser bringen?"),
        ("The food is cold.", "Das Essen ist kalt."),
        ("Is it very spicy?", "Ist es sehr scharf?"),
        ("I will take it to go.", "Ich nehme es zum Mitnehmen."),
        ("Is the coffee included?", "Ist der Kaffee inklusive?"),
        ("It was excellent, thank you.", "Es war ausgezeichnet, danke."),
    ],
    "market": [
        ("How much does this cost?", "Wie viel kostet das?"),
        ("I need bread.", "Ich brauche Brot."),
        ("Where is the milk?", "Wo ist die Milch?"),
        ("I pay by card.", "Ich zahle mit Karte."),
        ("Do you have a bag?", "Haben Sie eine TÃ¼te?"),
        ("That is everything.", "Das ist alles."),
        ("I am looking for tomatoes.", "Ich suche Tomaten."),
        ("Where is the fruit?", "Wo ist das Obst?"),
        ("Is this on sale?", "Ist das im Angebot?"),
        ("I would like half a kilo.", "Ich mochte ein halbes Kilo."),
        ("Can you weigh this?", "Konnen Sie das wiegen?"),
        ("I need eggs.", "Ich brauche Eier."),
        ("Is the checkout open?", "Ist die Kasse offen?"),
        ("I forgot my bag.", "Ich habe meine Tute vergessen."),
        ("Is there lactose-free milk?", "Gibt es laktosefreie Milch?"),
        ("Is this fresh?", "Ist das frisch?"),
        ("I would like cheese.", "Ich mochte Kase."),
        ("Where is the bakery?", "Wo ist die Backerei?"),
    ],
    "transport": [
        ("Where is the station?", "Wo ist der Bahnhof?"),
        ("I need a ticket.", "Ich brauche eine Fahrkarte."),
        ("Does this bus go downtown?", "FÃ¤hrt dieser Bus ins Zentrum?"),
        ("I get off here.", "Ich steige hier aus."),
        ("When does the train leave?", "Wann fÃ¤hrt der Zug?"),
        ("Is it far from here?", "Ist es weit von hier?"),
        ("Where do I buy the ticket?", "Wo kaufe ich die Fahrkarte?"),
        ("This train is late.", "Dieser Zug hat Verspatung."),
        ("Which platform?", "Welcher Bahnsteig?"),
        ("I need to go to the airport.", "Ich muss zum Flughafen."),
        ("The subway is full.", "Die U-Bahn ist voll."),
        ("I missed the bus.", "Ich habe den Bus verpasst."),
        ("When does the next one arrive?", "Wann kommt der nachste?"),
        ("I have a monthly pass.", "Ich habe eine Monatskarte."),
        ("Is this seat free?", "Ist dieser Platz frei?"),
        ("I need to change lines.", "Ich muss umsteigen."),
        ("Is the stop here?", "Ist die Haltestelle hier?"),
        ("How long does it take?", "Wie lange dauert es?"),
    ],
    "university": [
        ("Where is the room?", "Wo ist der Raum?"),
        ("I have class today.", "Ich habe heute Unterricht."),
        ("Can you help me?", "Kannst du mir helfen?"),
        ("I do not understand the task.", "Ich verstehe die Aufgabe nicht."),
        ("The exam is tomorrow.", "Die PrÃ¼fung ist morgen."),
        ("I study German.", "Ich lerne Deutsch."),
        ("I am a new student.", "Ich bin neuer Student."),
        ("Where is the library?", "Wo ist die Bibliothek?"),
        ("I have a question.", "Ich habe eine Frage."),
        ("Class starts at nine.", "Der Unterricht beginnt um neun."),
        ("I need to submit the assignment.", "Ich muss die Arbeit abgeben."),
        ("Can you speak more slowly?", "Konnen Sie langsamer sprechen?"),
        ("I study engineering.", "Ich studiere Ingenieurwesen."),
        ("Where is the professor?", "Wo ist der Professor?"),
        ("The room is full.", "Der Raum ist voll."),
        ("I need to print.", "Ich muss drucken."),
        ("The deadline is today.", "Die Frist ist heute."),
        ("I have a meeting.", "Ich habe ein Treffen."),
    ],
    "housing": [
        ("I am looking for an apartment.", "Ich suche eine Wohnung."),
        ("The rent is expensive.", "Die Miete ist teuer."),
        ("The internet does not work.", "Das Internet funktioniert nicht."),
        ("Where is the key?", "Wo ist der SchlÃ¼ssel?"),
        ("The room is small.", "Das Zimmer ist klein."),
        ("I live with friends.", "Ich wohne mit Freunden."),
        ("I want to visit the apartment.", "Ich mochte die Wohnung besichtigen."),
        ("How many rooms are there?", "Wie viele Zimmer gibt es?"),
        ("Does the heating work?", "Funktioniert die Heizung?"),
        ("The kitchen is shared.", "Die Kuche ist geteilt."),
        ("When can I move in?", "Wann kann ich einziehen?"),
        ("The contract is for one year.", "Der Vertrag ist fur ein Jahr."),
        ("The deposit is high.", "Die Kaution ist hoch."),
        ("Is there a washing machine?", "Gibt es eine Waschmaschine?"),
        ("The neighborhood is quiet.", "Die Gegend ist ruhig."),
        ("The room is furnished.", "Das Zimmer ist mobliert."),
        ("I live near the center.", "Ich wohne in der Nahe vom Zentrum."),
        ("The light does not work.", "Das Licht funktioniert nicht."),
    ],
}


def seed_course(source_language: Language, target_language: Language, course_phrases: dict[str, list[tuple[str, str]]], title_prefix: str) -> dict[str, int]:
    phrases_count = 0
    lessons_count = 0
    study_days_count = 0
    day_number = 1

    for scenario_slug, scenario_phrases in course_phrases.items():
        scenario = Scenario.objects.get(slug=scenario_slug)

        for lesson_index in range(0, len(scenario_phrases), 6):
            phrase_objects = []
            lesson_phrases = scenario_phrases[lesson_index : lesson_index + 6]

            for source_text, target_text in lesson_phrases:
                phrase, created = Phrase.objects.update_or_create(
                    source_language=source_language,
                    target_language=target_language,
                    source_text=source_text,
                    target_text=target_text,
                    defaults={"category": scenario.title, "scenario": scenario, "difficulty": "A1"},
                )
                phrase_objects.append(phrase)
                phrases_count += int(created)

            lesson, created_lesson = Lesson.objects.update_or_create(
                title=f"{title_prefix} Day {day_number}: {scenario.title} Sprint {lesson_index // 6 + 1}",
                defaults={
                    "day_number": day_number,
                    "scenario": scenario,
                    "video_title": f"A1 German: {scenario.title} in real life",
                    "video_url": "https://www.youtube.com/results?search_query=german+a1+phrases",
                    "video_duration": "~10 min",
                },
            )
            lesson.phrases.set(phrase_objects)
            lessons_count += int(created_lesson)

            _, created_day = StudyDay.objects.update_or_create(
                lesson=lesson,
                defaults={"day_number": day_number, "is_active": day_number == 1},
            )
            study_days_count += int(created_day)
            day_number += 1

    return {"phrases": phrases_count, "lessons": lessons_count, "study_days": study_days_count}


def seed_german_a1() -> dict[str, int]:
    pt, _ = Language.objects.update_or_create(code="PT", defaults={"name": "Português"})
    en, _ = Language.objects.update_or_create(code="EN", defaults={"name": "Inglês"})
    es, _ = Language.objects.update_or_create(code="ES", defaults={"name": "Espanhol"})
    de, _ = Language.objects.update_or_create(code="DE", defaults={"name": "Alemão"})

    Goal.objects.update_or_create(
        id=1,
        defaults={
            "source_language": pt,
            "target_language": de,
            "target_level": "A1",
            "duration_days": 90,
            "total_phrases": 300,
            "learned_phrases": 0,
            "completed_lessons": 0,
            "streak_days": 0,
        },
    )

    pt_course = {scenario_slug: all_phrases_for(scenario_slug) for scenario_slug in PHRASES}
    pt_result = seed_course(pt, de, pt_course, "PT-DE A1")
    en_result = seed_course(en, de, ENGLISH_PHRASES, "EN-DE A1")

    # Keep references to supported languages alive for linters and future expansion.
    _ = es
    return {
        "phrases": pt_result["phrases"] + en_result["phrases"],
        "lessons": pt_result["lessons"] + en_result["lessons"],
        "study_days": pt_result["study_days"] + en_result["study_days"],
    }
