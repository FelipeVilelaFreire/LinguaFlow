from content.models import Language, Lesson, Phrase, Scenario, StudyDay


SPANISH_PHRASES = {
    "restaurant": [
        ("Eu gostaria de uma agua.", "Me gustaria un agua."),
        ("A conta, por favor.", "La cuenta, por favor."),
        ("Tem uma mesa livre?", "Tiene una mesa libre?"),
        ("Eu quero pedir agora.", "Quiero pedir ahora."),
        ("Sem cebola, por favor.", "Sin cebolla, por favor."),
        ("Isso estava muito bom.", "Estuvo muy bueno."),
        ("Eu tenho uma reserva.", "Tengo una reserva."),
        ("Para duas pessoas, por favor.", "Para dos personas, por favor."),
        ("Eu gostaria do cardapio.", "Me gustaria el menu."),
        ("O que voce recomenda?", "Que recomienda?"),
        ("Eu sou vegetariano.", "Soy vegetariano."),
        ("Eu gostaria de pagar.", "Me gustaria pagar."),
        ("Pode trazer mais agua?", "Puede traer mas agua?"),
        ("A comida esta fria.", "La comida esta fria."),
        ("Esta muito picante?", "Es muy picante?"),
        ("Eu levo para viagem.", "Lo llevo para llevar."),
        ("Onde fica o banheiro?", "Donde esta el bano?"),
        ("Aceita cartao?", "Acepta tarjeta?"),
    ],
    "market": [
        ("Quanto custa isso?", "Cuanto cuesta esto?"),
        ("Eu preciso de pao.", "Necesito pan."),
        ("Onde fica o leite?", "Donde esta la leche?"),
        ("Eu pago com cartao.", "Pago con tarjeta."),
        ("Voce tem uma sacola?", "Tiene una bolsa?"),
        ("Isso e tudo.", "Eso es todo."),
        ("Eu estou procurando tomates.", "Estoy buscando tomates."),
        ("Onde ficam as frutas?", "Donde estan las frutas?"),
        ("Isso esta em promocao?", "Esto esta en oferta?"),
        ("Eu quero meio quilo.", "Quiero medio kilo."),
        ("Pode pesar isso?", "Puede pesar esto?"),
        ("Eu preciso de ovos.", "Necesito huevos."),
        ("O caixa esta aberto?", "La caja esta abierta?"),
        ("Eu esqueci minha sacola.", "Olvide mi bolsa."),
        ("Tem leite sem lactose?", "Hay leche sin lactosa?"),
        ("Isso e fresco?", "Esto es fresco?"),
        ("Eu quero queijo.", "Quiero queso."),
        ("Onde fica a padaria?", "Donde esta la panaderia?"),
    ],
    "transport": [
        ("Onde fica a estacao?", "Donde esta la estacion?"),
        ("Eu preciso de um bilhete.", "Necesito un billete."),
        ("Esse onibus vai ao centro?", "Este autobus va al centro?"),
        ("Eu desco aqui.", "Me bajo aqui."),
        ("Quando sai o trem?", "Cuando sale el tren?"),
        ("Esta longe daqui?", "Esta lejos de aqui?"),
        ("Onde compro o bilhete?", "Donde compro el billete?"),
        ("Este trem esta atrasado.", "Este tren esta retrasado."),
        ("Qual plataforma?", "Que anden?"),
        ("Eu preciso ir ao aeroporto.", "Necesito ir al aeropuerto."),
        ("O metro esta lotado.", "El metro esta lleno."),
        ("Eu perdi o onibus.", "Perdi el autobus."),
        ("Quando chega o proximo?", "Cuando llega el proximo?"),
        ("Eu tenho um passe mensal.", "Tengo un abono mensual."),
        ("Este lugar esta livre?", "Este asiento esta libre?"),
        ("Preciso trocar de linha.", "Necesito cambiar de linea."),
        ("A parada e aqui?", "La parada es aqui?"),
        ("Quanto tempo demora?", "Cuanto tarda?"),
    ],
    "university": [
        ("Onde e a sala?", "Donde esta el aula?"),
        ("Eu tenho aula hoje.", "Tengo clase hoy."),
        ("Voce pode me ajudar?", "Puedes ayudarme?"),
        ("Eu nao entendo a tarefa.", "No entiendo la tarea."),
        ("A prova e amanha.", "El examen es manana."),
        ("Eu estudo espanhol.", "Estudio espanol."),
        ("Eu sou estudante novo.", "Soy estudiante nuevo."),
        ("Onde fica a biblioteca?", "Donde esta la biblioteca?"),
        ("Tenho uma pergunta.", "Tengo una pregunta."),
        ("A aula comeca as nove.", "La clase empieza a las nueve."),
        ("Eu preciso entregar o trabalho.", "Necesito entregar el trabajo."),
        ("Pode falar mais devagar?", "Puede hablar mas despacio?"),
        ("Eu estudo engenharia.", "Estudio ingenieria."),
        ("Onde esta o professor?", "Donde esta el profesor?"),
        ("A sala esta cheia.", "El aula esta llena."),
        ("Eu preciso imprimir.", "Necesito imprimir."),
        ("O prazo e hoje.", "La fecha limite es hoy."),
        ("Eu tenho uma reuniao.", "Tengo una reunion."),
    ],
    "housing": [
        ("Eu procuro um apartamento.", "Busco un apartamento."),
        ("O aluguel e caro.", "El alquiler es caro."),
        ("A internet nao funciona.", "Internet no funciona."),
        ("Onde esta a chave?", "Donde esta la llave?"),
        ("O quarto e pequeno.", "La habitacion es pequena."),
        ("Eu moro com amigos.", "Vivo con amigos."),
        ("Eu quero visitar o apartamento.", "Quiero visitar el apartamento."),
        ("Quantos quartos tem?", "Cuantas habitaciones tiene?"),
        ("O aquecimento funciona?", "Funciona la calefaccion?"),
        ("A cozinha e compartilhada.", "La cocina es compartida."),
        ("Quando posso entrar?", "Cuando puedo mudarme?"),
        ("O contrato e de um ano.", "El contrato es por un ano."),
        ("O deposito e alto.", "El deposito es alto."),
        ("Tem maquina de lavar?", "Hay lavadora?"),
        ("O bairro e tranquilo.", "El barrio es tranquilo."),
        ("O quarto tem moveis.", "La habitacion esta amueblada."),
        ("Eu moro perto do centro.", "Vivo cerca del centro."),
        ("A luz nao funciona.", "La luz no funciona."),
    ],
}


def seed_spanish_a1() -> dict[str, int]:
    pt, _ = Language.objects.update_or_create(code="PT", defaults={"name": "Portugues"})
    es, _ = Language.objects.update_or_create(code="ES", defaults={"name": "Espanhol"})
    day_number = 1
    phrases_count = 0
    lessons_count = 0
    study_days_count = 0

    for scenario_slug, scenario_phrases in SPANISH_PHRASES.items():
        scenario = Scenario.objects.get(slug=scenario_slug)
        for lesson_index in range(0, len(scenario_phrases), 6):
            lesson_phrases = scenario_phrases[lesson_index : lesson_index + 6]
            phrase_objects = []

            for source_text, target_text in lesson_phrases:
                phrase, created = Phrase.objects.update_or_create(
                    source_language=pt,
                    target_language=es,
                    source_text=source_text,
                    target_text=target_text,
                    defaults={"category": scenario.title, "scenario": scenario, "difficulty": "A1"},
                )
                phrase_objects.append(phrase)
                phrases_count += int(created)

            lesson, created_lesson = Lesson.objects.update_or_create(
                title=f"PT-ES A1 Day {day_number}: {scenario.title} Sprint {lesson_index // 6 + 1}",
                defaults={
                    "day_number": day_number,
                    "scenario": scenario,
                    "video_title": f"A1 Spanish: {scenario.title} in real life",
                    "video_url": "https://www.youtube.com/results?search_query=spanish+a1+phrases",
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
