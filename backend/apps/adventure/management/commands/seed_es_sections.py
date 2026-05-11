"""
Seed das 6 seções da Fase 1 Espanhol A1 — Don Miguel el Campesino.

Pré-requisito: python manage.py seed_es_full (cria chapter + fase)
Uso:           python manage.py seed_es_sections [--reset]

⚠️  Padrão obrigatório: chat conversacional do começo ao fim.
Toda multiple_choice carrega 'npc' (situação) + 'npc_reaction' (reação ao acerto).
Don Miguel é o fio condutor — nunca exercício solto, nunca pergunta seca.
"""
from django.core.management.base import BaseCommand, CommandError

from apps.adventure.models import AdventureChapter, AdventurePhase, PhaseSection


# ─── Conteúdo das seções ──────────────────────────────────────────────────────

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Imersão intencional: Don Miguel fala sem tradução. Exercícios são
    # compreensão contextual — o jogador decodifica pelo gesto e situação.
    # Cada multiple_choice é atribuída a Don Miguel via campo 'npc'.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "O sol da tarde bate forte em San Cristóbal del Pueblo. "
                        "Poeira no ar, galinhas na rua. Um velho de chapéu largo "
                        "te observa da sombra de uma parede de adobe."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¡Hola, forastero! ¿Cómo te llamas?",
                },
                {
                    "kind": "player",
                    "text": "Você não entende nada, mas sorri e aponta para si mesmo.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Yo me llamo Miguel. Don Miguel el campesino, ¿eh?",
                },
                {
                    "kind": "player",
                    "text": "Você faz um gesto de não entender.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¡Buenos días! Bueno... ya son buenas tardes. ¿Estás bien, forastero?",
                },
                {
                    "kind": "narrative",
                    "text": "O velho ri, inclina o chapéu e aponta para o céu avermelhado.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Ele se aproximou de você acenando. Qual palavra ele usou pra cumprimentar?",
                    "options": [
                        {"id": "a", "text": "¡Hola!"},
                        {"id": "b", "text": "Gracias"},
                        {"id": "c", "text": "Perdón"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olá",
                    "npc_reaction": "¡Eso! Hola — palabra que abre puertas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Ele bateu no próprio peito enquanto falava o nome. Qual frase ele usou?",
                    "options": [
                        {"id": "a", "text": "Me llamo Miguel"},
                        {"id": "b", "text": "Soy Miguel"},
                        {"id": "c", "text": "Mi nombre es Juan"},
                        {"id": "d", "text": "Él llama Miguel"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Eso. 'Me llamo Miguel'. Mucho gusto, forastero.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sol já está baixo. Ele apontou pro céu e cumprimentou. Como?",
                    "options": [
                        {"id": "a", "text": "Buenas tardes"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "Hola noche"},
                        {"id": "d", "text": "Buenos tiempos"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_tardes", "target": "buenas tardes", "native": "boa tarde",
                    "npc_reaction": "Sí. Antes era 'buenos días', ahora ya es tarde. Cambia con el sol.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Ele te chamou de 'forastero'. Você acabou de chegar de fora. O que isso significa?",
                    "options": [
                        {"id": "a", "text": "estrangeiro / forasteiro"},
                        {"id": "b", "text": "agricultor / campesino"},
                        {"id": "c", "text": "médico / doutor"},
                        {"id": "d", "text": "soldado / guerreiro"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Eso. Pero menos cada hora que pasa, ¿eh?",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS (aquecimento contextual — primeira fase) ──────────
    # Don Miguel leva o jogador pra passear pelo pueblo. Cada exercício é uma
    # pergunta dele dentro de uma situação real (vizinho que passa, senhora que
    # oferece pão). Sem vocab_list — palavras testadas em uso direto.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Você acabou de chegar ao pueblo de San Cristóbal. O sol da tarde "
                    "queimava forte quando Don Miguel saiu da sombra de um muro de "
                    "adobe e te abordou em espanhol.\n\n"
                    "Ele te chamou de '¡forastero!', falou '¡Hola!' e disse 'Me llamo "
                    "Miguel'. Quando você fez cara de quem não entendeu, ele riu e "
                    "perguntou '¿Estás bien?', apontando pro próprio peito."
                ),
                "now": "Agora Don Miguel quer te levar pra passear e ver se as palavras grudaram.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel se levanta, espana a roupa de terra e faz sinal pra "
                        "você seguir. 'Vamos andar. Quero ver si esas palabras se "
                        "quedaron en tu cabeza.'"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Cuando encuentras a alguien por la calle, ¿qué dices?",
                    "translation": "Quando você encontra alguém na rua, o que diz?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um vizinho passa pela rua de pedra e te olha com um sorriso. Você diz:",
                    "options": [
                        {"id": "a", "text": "¡Hola!"},
                        {"id": "b", "text": "¡Gracias!"},
                        {"id": "c", "text": "¡Mal!"},
                        {"id": "d", "text": "¡Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olá",
                    "npc_reaction": "Eso. Sencillo, ¿no? Hola sirve a cualquier hora.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Pero si es la mañana — más temprano — saludamos diferente.",
                    "translation": "Mas se é de manhã — mais cedo — cumprimentamos diferente.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sol acabou de subir, está cedo. Como você cumprimenta?",
                    "options": [
                        {"id": "a", "text": "¡Buenos días!"},
                        {"id": "b", "text": "¡Buenas tardes!"},
                        {"id": "c", "text": "¡Buenas noches!"},
                        {"id": "d", "text": "¡Buen día!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Bueno. 'Buenos días' hasta el mediodía, más o menos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y al final del día, cuando ya pasó el almuerzo, cambia.",
                    "translation": "E no final do dia, quando já passou o almoço, muda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Já é de tarde. Como você cumprimenta agora?",
                    "options": [
                        {"id": "a", "text": "¡Buenas tardes!"},
                        {"id": "b", "text": "¡Buenos días!"},
                        {"id": "c", "text": "¡Hola noche!"},
                        {"id": "d", "text": "¡Buenos tiempos!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_tardes", "target": "buenas tardes", "native": "boa tarde",
                    "npc_reaction": "Exacto. Aprende a mirar el sol — él te dice qué decir.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês passam pela porta de uma casa de adobe. Cheiro forte "
                        "de pão recém saído do forno. Uma mulher de avental empoeirado "
                        "aparece na entrada — Don Miguel acena pra ela como quem "
                        "conhece de longa data."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "¡Hola, Miguel! ¿Quién es el forastero?",
                    "translation": "Olá Miguel! Quem é o forasteiro?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ya está aprendiendo, Rosa. Mira — le voy a mostrar el pueblo.",
                    "translation": "Já tá aprendendo, Rosa. Olha — vou mostrar o pueblo pra ele.",
                },
                {
                    "kind": "narrative",
                    "text": "Rosa sorri e estende um pedaço de pão quente pra você.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa te entrega o pão sem pedir nada em troca. Você responde:",
                    "options": [
                        {"id": "a", "text": "¡Gracias!"},
                        {"id": "b", "text": "¡Hola!"},
                        {"id": "c", "text": "¡Bien!"},
                        {"id": "d", "text": "¡Mal!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, hijo. Vuelve cuando quieras pan.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel acena pra Rosa enquanto vocês seguem. Como ela respondeu seu 'gracias'?",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Buenas tardes"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Ahá. 'De nada' — la respuesta natural. Es el ciclo, forastero.",
                },
            ],
        },
    },

    # ── Seção 3: Gramática Narrativa ───────────────────────────────────────────
    # Don Miguel senta com o jogador e ensina explicitamente as estruturas:
    # ¿Cómo te llamas? / Me llamo + ¿Cómo estás? / Bien o mal.
    # Beats de ensino (npc_speak/reveal/pattern) intercalados com exercícios
    # conduzidos por ele.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel passou a tarde te fazendo repetir as saudações que ele "
                    "tinha soltado no portão: '¡Hola!', 'Buenos días', 'Buenas tardes'.\n\n"
                    "Quando você acertou 'Gracias' e ele respondeu 'De nada', ele bateu "
                    "palma uma vez só, satisfeito. 'Vê? Você consegue.'\n\n"
                    "Aí ele largou a enxada, puxou uma cadeira de madeira da parede de "
                    "adobe e te apontou pra sentar do lado dele."
                ),
                "now": "Don Miguel vai te ensinar a pedir nomes e responder como você está.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel cruza as pernas, ajeita o chapéu e te olha de frente. "
                        "'Hay palabras que todo mundo usa aquí. Te las enseño una por una.'"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Primero: ¿cómo te llamas?",
                    "translation": "Primeiro: como você se chama?",
                },
                {
                    "kind": "reveal",
                    "phrase": "¿Cómo te llamas?",
                    "meaning": "Como você se chama?",
                    "note": "Pergunta padrão pra pedir o nome de alguém",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y la respuesta empieza así: 'Me llamo' — y dices tu nombre.",
                    "translation": "E a resposta começa assim: 'Me llamo' — e você diz seu nome.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Me llamo ___",
                    "meaning": "Meu nome é ___",
                    "note": "Use seu próprio nome: 'Me llamo [nome]'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra você: '¿Cómo te llamas?' Como você responde?",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy llamo [seu nome]"},
                        {"id": "c", "text": "Tú llamas [seu nome]"},
                        {"id": "d", "text": "Hola Miguel"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "¡Mucho gusto otra vez, amigo!",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ahora otra cosa importante: '¿Cómo estás?'",
                    "translation": "Agora outra coisa importante: 'como você está?'",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "¿Cómo estás?", "isKey": False},
                        {"text": " → ",          "isKey": False},
                        {"text": "Bien",          "isKey": True},
                        {"text": " / ",           "isKey": False},
                        {"text": "Mal",           "isKey": True},
                    ],
                    "example": "— ¿Cómo estás? — Bien, gracias.",
                    "translation": "— Como você está? — Bem, obrigado.",
                    "note": "Bien = bem | Mal = mal",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sol tá bom, o pão da senhora ainda quente no seu bolso. Don Miguel: '¿Cómo estás?'",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "¡Perfecto!",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Pero si no estás bien, no mientas. Dilo.",
                    "translation": "Mas se você não está bem, não minta. Fale.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Seus pés doem, suas pálpebras pesam. Faz dias que você caminha sem parar. Don Miguel olha pra você: '¿Cómo estás?'",
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bien"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Entiendo, forastero. Descansa tranquilo aquí.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você quer saber o nome de alguém. Pergunta:",
                    "options": [
                        {"id": "a", "text": "¿Cómo te llamas?"},
                        {"id": "b", "text": "¿Cómo estás?"},
                        {"id": "c", "text": "¿Dónde estás?"},
                        {"id": "d", "text": "¿Y tú?"},
                    ],
                    "correct": "a",
                    "word_id": "es_como_te_llamas", "target": "¿cómo te llamas?", "native": "como você se chama?",
                    "npc_reaction": "Bien. Y mira al pecho del otro mientras preguntas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: '¡Mucho gusto!' Agora você quer perguntar como ele está. Diz:",
                    "options": [
                        {"id": "a", "text": "¿Cómo estás?"},
                        {"id": "b", "text": "¿Cómo te llamas?"},
                        {"id": "c", "text": "¿Y tú?"},
                        {"id": "d", "text": "Me llamo"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Eso. Y la respuesta — ya sabes.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel se aponta com o polegar: 'Yo soy un...'",
                    "options": [
                        {"id": "a", "text": "Campesino"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Médico"},
                        {"id": "d", "text": "Soldado"},
                    ],
                    "correct": "a",
                    "word_id": "es_campesino", "target": "campesino", "native": "camponês",
                    "npc_reaction": "Eso. Toda mi vida en el campo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta agora pra você: 'Pero tú llegaste de lejos. Tú eres un...'",
                    "options": [
                        {"id": "a", "text": "Forastero"},
                        {"id": "b", "text": "Campesino"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Amigo"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero. Pero menos cada hora que pasa, ¿eh?",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel tira uma manzana do bolso e te passa sem cerimônia. 'Del árbol detrás de mi casa.' Você aceita com um aceno.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel cruza os braços, satisfeito com o que viu até aqui: '¿Cómo estás?'",
                    "options": [
                        {"id": "a", "text": "Bien, ¿y tú?"},
                        {"id": "b", "text": "Mal, gracias"},
                        {"id": "c", "text": "Hola, Miguel"},
                        {"id": "d", "text": "De nada"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "¡Excelente! Y devolviendo siempre — '¿y tú?' — eso es lo bueno.",
                },
            ],
        },
    },

    # ── Seção 4: Encontro com Carmen ──────────────────────────────────────────
    # Narrativa-heavy: Don Miguel te leva pra plaza e te apresenta a Señora
    # Carmen, vizina antiga que conhece todo o pueblo. Poucos exercícios — os
    # que aparecem servem o encontro, não testam exaustivamente.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel passou a tarde te fazendo praticar até as palavras "
                    "saírem sem hesitar. Saudações, perguntas, respostas — você "
                    "respondeu cada uma sem tropeçar.\n\n"
                    "Quando ele cruzou os braços satisfeito, você sabia que tinha "
                    "passado por algo. 'Bueno, forastero. Vamos a la plaza. Hay "
                    "alguien que quiero que conozcas.'"
                ),
                "now": "Don Miguel vai te apresentar alguém importante do pueblo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês entram na plaza central do pueblo. Sombra de árvores "
                        "antigas, fonte de pedra no meio. Uma mulher mais velha está "
                        "sentada num banco, costurando uma camisa com agulha fina."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Mira — esa es doña Carmen. Conoce a todos en el pueblo. Si quieres saber algo, ella te dice.",
                    "translation": "Olha — essa é doña Carmen. Conhece todo mundo no pueblo. Se quiser saber algo, ela te conta.",
                },
                {
                    "kind": "narrative",
                    "text": "Carmen levanta os olhos do bordado. Sorri pra Don Miguel, depois pra você.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¡Hola, Miguel! ¿Y este forastero?",
                    "translation": "Olá, Miguel! E esse forasteiro?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Mi forastero. Lo estoy enseñando. Ya sabe saludar.",
                    "translation": "Meu forasteiro. Tô ensinando ele. Já sabe cumprimentar.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Carmen tira os óculos pequenos do nariz, te examina de cima "
                        "a baixo. Gesto materno, sem maldade."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Acércate, hijo. Déjame verte mejor.",
                    "translation": "Chega mais perto, filho. Deixa eu te ver melhor.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen aponta o banco do lado dela: '¿Y tú, hijo? ¿Cómo te llamas?'",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Soy forastero"},
                        {"id": "d", "text": "Hola Carmen"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto. Yo soy Carmen. Llevo toda mi vida en este pueblo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você se senta no banco de pedra ao lado dela. As mãos da "
                        "Carmen voltam ao bordado — ágeis, apesar das veias salientes "
                        "e dos anos."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Dime una cosa — ¿cómo estás hoy? El primer día siempre es duro.",
                    "translation": "Me diz uma coisa — como você está hoje? O primeiro dia sempre é duro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "O sol da tarde te aquece, o pão da Rosa ainda quente no bolso. Você responde:",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Me alegro. Aquí siempre se está bien si el cuerpo no falla y la gente saluda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¿Y sabes despedirte también, forastero?",
                    "translation": "E você sabe se despedir também, forasteiro?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen te olha esperando. Você precisa dizer tchau em espanhol.",
                    "options": [
                        {"id": "a", "text": "Adiós"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Gracias"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_adios", "target": "adiós", "native": "tchau / adeus",
                    "npc_reaction": "Bien. Aunque espero que no tan pronto, hijo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Ahora — pregúntale a Miguel cómo está.",
                    "translation": "Agora — pergunta pro Miguel como ele tá.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Carmen aponta pra Don Miguel. É a sua vez de perguntar.",
                    "options": [
                        {"id": "a", "text": "¿Cómo estás?"},
                        {"id": "b", "text": "¿Cómo te llamas?"},
                        {"id": "c", "text": "¿Y tú?"},
                        {"id": "d", "text": "¿Adiós?"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bien. Como siempre que enseño a alguien que quiere aprender.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel observa de pé, satisfeito. Carmen continua "
                        "costurando, mas claramente tem coisas pra te contar."
                    ),
                },
            ],
        },
    },

    # ── Seção 5: Convivência com Carmen ────────────────────────────────────────
    # Narrativa-heavy: Carmen ensina sobre o ritmo social do pueblo enquanto
    # costura. Poucos exercícios — o foco é desenvolver o personagem e
    # contextualizar o vocab (saudação, gracias, de nada) em sabedoria popular.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Carmen"],
                "story": (
                    "Don Miguel te apresentou a doña Carmen na plaza central. Uma "
                    "mulher mais velha, costurando num banco de pedra, com olhar "
                    "calmo de quem viu tudo.\n\n"
                    "Você se apresentou, disse que estava bem. Carmen sorriu e "
                    "falou que sempre se está bem no pueblo — se o corpo não "
                    "falha e se a gente cumprimenta. Agora ela quer te contar "
                    "como funciona o pueblo."
                ),
                "now": "Carmen vai te ensinar o ritmo social — quando cumprimentar como, e por quê.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Aquí en el pueblo, somos pocos. Pero todos nos conocemos.",
                    "translation": "Aqui no pueblo, somos poucos. Mas todos nos conhecemos.",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel acena com a cabeça concordando, mas deixa Carmen falar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Si saludas a alguien, te recordará. Si dices 'gracias', te invitará. Es así.",
                    "translation": "Se você cumprimenta alguém, vão lembrar. Se diz 'gracias', vão te convidar. É assim.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "La palabra más bonita del español es 'gracias'. No la olvides nunca.",
                    "translation": "A palavra mais bonita do espanhol é 'gracias'. Não esqueça nunca.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen aponta pra Don Miguel: 'Cuando él te dé algo — pan, agua, una palabra — ¿qué dices?'",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Eso. Y si te lo dicen a ti...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Don Miguel te entrega a manzana que estava no bolso dele. Você diz 'gracias'. Como ele responde?",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Ese es el ciclo, hijo. Saludo, palabra, respuesta. Así vivimos en el pueblo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¿Y cuando el sol se pone y llega la noche?",
                    "translation": "E quando o sol se põe e chega a noite?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "O sol sumiu. Você encontra alguém na rua à noite. Como cumprimenta?",
                    "options": [
                        {"id": "a", "text": "Buenas noches"},
                        {"id": "b", "text": "Buenos días"},
                        {"id": "c", "text": "Buenas tardes"},
                        {"id": "d", "text": "Hola noche"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                    "npc_reaction": "Así. Cada hora tiene su saludo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Una última cosa, forastero — ¿cómo te llamas?",
                    "translation": "Uma última coisa, forasteiro — como você se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen te olha com um sorriso. Ela quer ouvir você dizer seu nome.",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Hola Carmen"},
                        {"id": "d", "text": "Soy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Eso. Nunca olvides tu nombre cuando alguien te lo pida.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Carmen volta ao bordado. O sol começou a baixar mais — "
                        "sombras compridas no chão de pedra. Don Miguel olha pra "
                        "ela com afeto."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Vuelve mañana si quieres. Siempre estoy aquí — en este banco, con la aguja en la mano.",
                    "translation": "Volta amanhã se quiser. Sempre estou aqui — neste banco, com a agulha na mão.",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel coloca a mão no seu ombro. É hora de seguir.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Vamos, forastero. Aún hay una cosa antes de descansar.",
                    "translation": "Vamos, forasteiro. Ainda tem uma coisa antes de você descansar.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate final — gated) ────────────────────────────────
    # Don Miguel vira examinador. Cada exercício é um desafio dele encurtado.
    # Errar trava (front aplica isGated). 'npc_reaction' marca a aprovação.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel encaixou as três frases numa só sequência e fez você "
                    "repetir até soar natural: '¡Hola! ¿Cómo estás?' — pausa — "
                    "resposta — '¿Y tú, cómo te llamas?'\n\n"
                    "Na terceira vez ele não corrigiu nada. Só acenou com a cabeça e "
                    "tirou o chapéu por um segundo, num gesto sério: 'Bueno. Ya casi "
                    "puedes hablar con cualquiera.'\n\n"
                    "Aí o sorriso saiu do rosto dele. 'Ahora vamos a ver de verdad.'"
                ),
                "now": "Hora do teste final. Errar trava — você precisa acertar pra passar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ya basta de explicaciones. Si te equivocas, repites. Sin atajos.",
                    "translation": "Chega de explicações. Se errar, repete. Sem atalhos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'Es la mañana. Llego a tu lado. ¿Qué dices?'",
                    "options": [
                        {"id": "a", "text": "¡Buenos días!"},
                        {"id": "b", "text": "¡Buenas tardes!"},
                        {"id": "c", "text": "¡Buenas noches!"},
                        {"id": "d", "text": "¡Hola noche!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Eso. Pasa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'Te di un pedazo de pan. Responde.'",
                    "options": [
                        {"id": "a", "text": "¡Gracias!"},
                        {"id": "b", "text": "¡Hola!"},
                        {"id": "c", "text": "¡Bien!"},
                        {"id": "d", "text": "¡Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Bien. Sigue.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'Dijiste gracias. ¿Qué te respondo yo?'",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Eso. Es el ciclo. Memorízalo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'Me quieres saber el nombre. Pregunta.'",
                    "options": [
                        {"id": "a", "text": "¿Cómo te llamas?"},
                        {"id": "b", "text": "¿Cómo estás?"},
                        {"id": "c", "text": "¿Y tú?"},
                        {"id": "d", "text": "¿Dónde vas?"},
                    ],
                    "correct": "a",
                    "word_id": "es_como_te_llamas", "target": "¿cómo te llamas?", "native": "como você se chama?",
                    "npc_reaction": "Sí, forastero.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'Yo te pregunto cómo te llamas. Tu respuesta empieza con...'",
                    "options": [
                        {"id": "a", "text": "Me llamo"},
                        {"id": "b", "text": "Soy llamo"},
                        {"id": "c", "text": "Mi llama"},
                        {"id": "d", "text": "Te llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Eso es.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'¿Cómo estás? Tú estás bien.'",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'Pero también puedes estar...'",
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bueno"},
                        {"id": "c", "text": "Bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Eso. Honesto siempre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'Se hace tarde. ¿Cómo saludas?'",
                    "options": [
                        {"id": "a", "text": "¡Buenas tardes!"},
                        {"id": "b", "text": "¡Buenos días!"},
                        {"id": "c", "text": "¡Hola tarde!"},
                        {"id": "d", "text": "¡Buenos noches!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_tardes", "target": "buenas tardes", "native": "boa tarde",
                    "npc_reaction": "Sí. Aprendiste.",
                },
                # ── Closing beats — transição pro Dia 2 / la posada ──
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel se ajeita o chapéu e olha pro céu — o sol já tá "
                        "baixo, sombras compridas no chão de terra. Ele te dá um "
                        "tapinha no ombro."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ya hiciste mucho por hoy. Ven, vamos a la posada del pueblo.",
                    "translation": "Já fez muito por hoje. Vem, vamos pra posada do pueblo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Descansa. Mañana hay más pueblo para conocer.",
                    "translation": "Descansa. Amanhã tem mais pueblo pra conhecer.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês caminham juntos pelas ruas de pedra. As primeiras "
                        "luzes começam a aparecer nas janelas. Don Miguel te aponta "
                        "uma casa de dois andares no canto da plaza — la posada. "
                        "Onde você vai dormir essa noite."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────

class Command(BaseCommand):
    help = "Seed das 6 seções da Fase 1 Espanhol A1 (requer seed_es_full antes)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Apaga e recria as seções (default: pula se já existem)",
        )

    def handle(self, *args, **options):
        self.stdout.write("\n📦 Seeding seções — ES A1 T1 Fase 1\n")

        try:
            chapter = AdventureChapter.objects.get(slug="es-a1-t1")
        except AdventureChapter.DoesNotExist:
            raise CommandError(
                "Chapter 'es-a1-t1' não encontrado. Rode 'seed_es_full' primeiro."
            )

        try:
            phase = AdventurePhase.objects.get(chapter=chapter, number=1)
        except AdventurePhase.DoesNotExist:
            raise CommandError(
                "Fase 1 do chapter 'es-a1-t1' não encontrada. Rode 'seed_es_full' primeiro."
            )

        existing = PhaseSection.objects.filter(phase=phase).count()
        if existing and not options["reset"]:
            self.stdout.write(
                self.style.WARNING(
                    f"  Fase 1 já tem {existing} seções. Use --reset para recriar."
                )
            )
            return

        if options["reset"]:
            deleted, _ = PhaseSection.objects.filter(phase=phase).delete()
            self.stdout.write(f"  ↻ {deleted} seções apagadas")

        created_count = 0
        for sec in SECTIONS:
            PhaseSection.objects.create(
                phase=phase,
                section_number=sec["section_number"],
                section_type=sec["section_type"],
                content=sec["content"],
            )
            self.stdout.write(
                f"  ✓ Seção {sec['section_number']}: {sec['section_type']}"
            )
            created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"\n✅ {created_count} seções criadas para Fase 1 · ES A1 T1\n"
            "   Endpoint: GET /api/adventure/phases/{phase_id}/sections/\n"
        ))
