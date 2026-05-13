"""
Seed das 6 seções da Fase 3 Espanhol A1 — "El Camino de Tierra".

Primeiro dia fora dos muros do pueblo. Don Miguel leva o protagonista pelo
caminho de terra que cruza os campos e chega até o rio. Lá encontram El Viejo
Leñador — um velho lenhador que reage ao protagonista de forma estranha.

Novos vocab (3): árbol · piedra · río
Revisão F1+F2: hola, buenos días, buenas tardes, gracias, bien/mal,
               forastero, me llamo, tengo hambre, tengo sed, pan, agua
NPC principal:   Don Miguel (fio condutor)
NPC cameo:       El Viejo Leñador (reação estranha — primeiro sinal do dom)
Itens:           piedra_del_río (word_id: es_piedra) · flor_silvestre (word_id: es_flor)
Arco emocional:  confinado → expansivo; curiosidade + primeiro pressentimento
Transição:       voltam ao pueblo ao entardecer; Miguel quieto; pedra no bolso
                 do protagonista como lembrança do dia.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f3_sections [--reset]
"""
from django.core.management.base import BaseCommand, CommandError

from apps.adventure.models import AdventureChapter, AdventurePhase, PhaseSection


SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Manhã — Don Miguel propõe sair dos muros. Portão do pueblo, campos abertos,
    # caminho de terra. Novo NPC (Leñador) ouvido ao longe. Vocab aparece sem
    # tradução — imersão. Exercícios: reconhecimento contextual.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌄 Manhã clara. Don Miguel está na porta da posada com um "
                        "saco velho às costas. Aponta pro portão de madeira pesada "
                        "na borda do pueblo — a saída pros campos."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Hoy salimos. Quiero que veas el campo. Hay cosas que el pueblo no te enseña.",
                },
                {
                    "kind": "player",
                    "text": "Você seguiu sem perguntar. Faz dias que você só viu adobe e pedra. A ideia de campo aberto parecia boa.",
                },
                {
                    "kind": "scene",
                    "text": "🌾 O portão abre pesado. Do outro lado: campos de milho, um caminho de terra batida, e longe — o verde-escuro de árvores.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Mira — los árboles allá. El río está detrás de ellos.",
                },
                {
                    "kind": "player",
                    "text": "Árboles. Rio. A palavra era nova, mas o gesto era claro — ele apontou pro verde e depois fez um gesto de água correndo.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Y en el camino — piedras. Cuidado con los pies.",
                },
                {
                    "kind": "scene",
                    "text": "🪨 Caminho cheio de pedras brancas. Você olhou pra baixo — algumas lisas, algumas pontiagudas.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¡Ey! ¿Estás bien? Camina — no mires tanto el suelo.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Você ergueu a cabeça. O campo se abria de todos os lados. Depois de dias no pueblo fechado, aquilo parecia enorme.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel apontou pro verde-escuro no horizonte e disse uma palavra. O que você vê ao longe?",
                    "options": [
                        {"id": "a", "text": "Árboles"},
                        {"id": "b", "text": "Piedras"},
                        {"id": "c", "text": "El río"},
                        {"id": "d", "text": "La posada"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "árbol", "native": "árvore",
                    "npc_reaction": "Árboles. Onde tem árbol, tem sombra. E onde tem sombra...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O caminho estava cheio delas — brancas, lisas, pontiagudas. Don Miguel avisou pra você cuidar dos pés. O que estava no caminho?",
                    "options": [
                        {"id": "a", "text": "Piedras"},
                        {"id": "b", "text": "Árboles"},
                        {"id": "c", "text": "Agua"},
                        {"id": "d", "text": "Flores"},
                    ],
                    "correct": "a",
                    "word_id": "es_piedra", "target": "piedra", "native": "pedra",
                    "npc_reaction": "Piedras. O chão do campo sempre tem piedras. Os pés aprendem.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel fez um gesto — as duas mãos correndo pra frente — e apontou atrás dos árboles. O que está além das árvores?",
                    "options": [
                        {"id": "a", "text": "El río"},
                        {"id": "b", "text": "El pueblo"},
                        {"id": "c", "text": "La posada"},
                        {"id": "d", "text": "El mercado"},
                    ],
                    "correct": "a",
                    "word_id": "es_rio", "target": "río", "native": "rio",
                    "npc_reaction": "El río. Água fria, agua limpia. Melhor que a fonte da plaza.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Vocês caminharam bastante. O sol esquentou. O que você provavelmente vai querer ao chegar no río?",
                    "options": [
                        {"id": "a", "text": "Agua — tengo sed"},
                        {"id": "b", "text": "Pan — tengo hambre"},
                        {"id": "c", "text": "La posada"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. E o río vai resolver isso.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # No campo, Don Miguel aproveita o caminho pra revisar F1+F2 vocab.
    # Situações reais: um pássaro, uma flor, parar pra beber água.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Vocês passaram pelo portão e o campo se abriu. Don Miguel "
                    "apontou 'árboles', 'piedras', 'el río'. O campo é diferente "
                    "do pueblo — mais silêncio, mais espaço, o cheiro de terra.\n\n"
                    "Enquanto caminham, Don Miguel continua te testando. 'O campo "
                    "também ensina. Você olha, eu pergunto.'"
                ),
                "now": "Revisão das palavras de F1 e F2 — cada uma num contexto de campo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel para, pega uma pedra lisa do chão e te joga. Você pega no ar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Cómo estás hoy? Con el campo y el sol?",
                    "translation": "Como você está hoje? Com o campo e o sol?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O ar está limpo, o campo aberto, você comeu o pão de Rosa antes de sair. Don Miguel quer saber como você está:",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Tengo sed"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. O campo faz isso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Oye — ¿y en la mañana, cuando llegas a un sitio nuevo y ves a alguien?",
                    "translation": "Ei — e de manhã, quando você chega num lugar novo e vê alguém?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um trabalhador do campo passa com uma enxada. É cedo ainda. Você cumprimenta:",
                    "options": [
                        {"id": "a", "text": "¡Buenos días!"},
                        {"id": "b", "text": "¡Buenas noches!"},
                        {"id": "c", "text": "¡Hola noche!"},
                        {"id": "d", "text": "¡Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. O trabalhador levantou dois dedos — reconheceu.",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel aponta pra uma flor vermelha no borde do caminho. 'Flor silvestre — flor do campo.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um menino do pueblo passa correndo e para quando vê a flor — 'La flor, qué bonita!' O que ele viu?",
                    "options": [
                        {"id": "a", "text": "Flor"},
                        {"id": "b", "text": "Piedra"},
                        {"id": "c", "text": "Árbol"},
                        {"id": "d", "text": "Río"},
                    ],
                    "correct": "a",
                    "word_id": "es_flor", "target": "flor", "native": "flor",
                    "npc_reaction": "Flor silvestre. Essa é do campo — não cresce na plaza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "El forastero — así te llaman. ¿Pero te acuerdas qué significa?",
                    "translation": "O forasteiro — assim te chamam. Mas você lembra o que significa?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra você: 'Los del pueblo te llaman forastero porque...'",
                    "options": [
                        {"id": "a", "text": "Você veio de fora — não é do pueblo"},
                        {"id": "b", "text": "Você não tem nome"},
                        {"id": "c", "text": "Você trabalha no campo"},
                        {"id": "d", "text": "Você é muito jovem"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Eso. Forastero = de fora. Mas o pueblo já tá acostumando contigo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y yo — ¿qué soy? ¿Recuerdas la palabra?",
                    "translation": "E eu — o que sou? Você lembra a palavra?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel arranca um pedaço de erva do chão, cheira. Trabalha com a terra toda a vida. Ele é:",
                    "options": [
                        {"id": "a", "text": "Campesino"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Doctor"},
                        {"id": "d", "text": "Maestro"},
                    ],
                    "correct": "a",
                    "word_id": "es_campesino", "target": "campesino", "native": "camponês",
                    "npc_reaction": "Campesino. E orgulhoso disso.",
                },
                {
                    "kind": "narrative",
                    "text": "As árvores estão mais perto. Um som novo — água correndo, fresco, abaixo do ruído do vento.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você ouviu o som, ficou com a boca seca de querer beber. Don Miguel olhou pra você. Você fala:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. El río tá ali. Já estamos chegando.",
                },
            ],
        },
    },

    # ── Seção 3: Gramática Narrativa ───────────────────────────────────────────
    # Chegaram ao río. Don Miguel ensina "hay" + lugar:
    # "Hay árboles. Hay piedras. Hay agua en el río."
    # Também: "no hay" — "no hay pan aquí".
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Vocês chegaram ao río. Água fria, pedras brancas no fundo, "
                    "sombra das árvores. Don Miguel jogou o saco no chão e sentou "
                    "numa pedra grande.\n\n"
                    "'Olha o que tem aqui. Aprenda a dizer.'"
                ),
                "now": "Don Miguel ensina 'hay' — a forma de dizer que algo existe num lugar.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel aponta em volta — árvores, pedras, o río, o céu. Faz um gesto amplo com o braço.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "'Hay' — eso es lo que usas cuando algo está aquí. 'Hay árboles.'",
                    "translation": "'Hay' — isso você usa quando algo está aqui. 'Há árvores.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Hay árboles",
                    "meaning": "Há árvores / Tem árvores",
                    "note": "hay = há / tem | serve pra qualquer coisa: hay agua, hay pan, hay piedras",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y si algo no está — 'no hay'. Simple. 'No hay pan aquí en el campo.'",
                    "translation": "E se algo não está — 'não tem'. Simples. 'Não tem pão aqui no campo.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "No hay pan",
                    "meaning": "Não tem pão / Não há pão",
                    "note": "no hay = não tem | o oposto de hay",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Hay",    "isKey": True},
                        {"text": " + ",    "isKey": False},
                        {"text": "coisa",  "isKey": True},
                        {"text": " | ",    "isKey": False},
                        {"text": "No hay", "isKey": True},
                        {"text": " + ",    "isKey": False},
                        {"text": "coisa",  "isKey": True},
                    ],
                    "example": "Hay piedras en el río. / No hay pan aquí.",
                    "translation": "Tem pedras no rio. / Não tem pão aqui.",
                    "note": "Hay = existe. No hay = não existe. Um padrão, infinitas coisas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pro río com pedras brancas no fundo. Como você descreve?",
                    "options": [
                        {"id": "a", "text": "Hay piedras en el río"},
                        {"id": "b", "text": "No hay piedras"},
                        {"id": "c", "text": "Hay pan en el río"},
                        {"id": "d", "text": "Tengo piedras"},
                    ],
                    "correct": "a",
                    "word_id": "es_piedra", "target": "piedra", "native": "pedra",
                    "npc_reaction": "Hay piedras. Exato. O río fala por si mesmo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você olha pra volta — só campo, árvores e rio. Não há nenhuma padaria. Don Miguel: '¿Hay pan aquí?'",
                    "options": [
                        {"id": "a", "text": "No hay pan"},
                        {"id": "b", "text": "Hay pan"},
                        {"id": "c", "text": "Tengo pan"},
                        {"id": "d", "text": "Hay agua"},
                    ],
                    "correct": "a",
                    "npc_reaction": "No hay pan. No hay Rosa tampoco. Só campo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Pero — ¿hay agua?",
                    "translation": "Mas — tem água?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O río está na sua frente, correndo sobre pedras brancas. Don Miguel espera:",
                    "options": [
                        {"id": "a", "text": "Sí, hay agua"},
                        {"id": "b", "text": "No hay agua"},
                        {"id": "c", "text": "Tengo agua"},
                        {"id": "d", "text": "Hay pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "água",
                    "npc_reaction": "Sí, hay agua. Mucha agua. Beba.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra cima, pras copas das árvores. '¿Y aquí — hay árboles?'",
                    "options": [
                        {"id": "a", "text": "Sí, hay árboles"},
                        {"id": "b", "text": "No hay árboles"},
                        {"id": "c", "text": "Hay piedras"},
                        {"id": "d", "text": "Hay pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "árbol", "native": "árvore",
                    "npc_reaction": "Hay árboles. E eles ficam aqui há cem anos — antes do pueblo.",
                },
                {
                    "kind": "narrative",
                    "text": "Ao longe, um som de machado batendo em madeira. Ritmado, constante. Don Miguel levanta a cabeça.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ese es el viejo Ernesto. El leñador. Viene aquí hace treinta años.",
                    "translation": "Esse é o velho Ernesto. O lenhador. Vem aqui há trinta anos.",
                },
            ],
        },
    },

    # ── Seção 4: Prática Aplicada ─────────────────────────────────────────────
    # Encontro com El Viejo Leñador (Ernesto). Pratica hay/no hay em situações
    # reais do campo enquanto o lenhador se aproxima. NPC presente em cada exercício.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel te ensinou 'hay' e 'no hay'. Árboles, piedras, "
                    "agua — tudo que está ao redor pode ser descrito assim.\n\n"
                    "O som do machado ficou mais próximo. O velho Ernesto está "
                    "vindo pela margem do río."
                ),
                "now": "Prática rápida antes do encontro com o leñador.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Antes de ele chegar — vamos praticar rápido. Olha ao redor e responde.",
                    "translation": "Antes dele chegar — vamos praticar rápido. Olha ao redor e responde.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pro outro lado do río — só pedras, grama, sem árvores. '¿Hay árboles allá?'",
                    "options": [
                        {"id": "a", "text": "No, no hay árboles"},
                        {"id": "b", "text": "Sí, hay árboles"},
                        {"id": "c", "text": "Hay pan allá"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "árbol", "native": "árvore",
                    "npc_reaction": "No hay árboles allá. Correto.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel abre o saco — tem um pedaço de pão seco lá dentro. '¿Hay pan?'",
                    "options": [
                        {"id": "a", "text": "Sí, hay pan"},
                        {"id": "b", "text": "No hay pan"},
                        {"id": "c", "text": "Hay agua"},
                        {"id": "d", "text": "No hay agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pão",
                    "npc_reaction": "Hay pan. Seco, mas hay.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você está com fome depois de caminhar bastante. Como você fala pro Don Miguel?",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "No hay pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. Pega o pão do saco — há um lá.",
                },
                {
                    "kind": "narrative",
                    "text": "Ernesto chega pela margem do río. Alto, pele curtida, machado no ombro. Olhos pequenos que enxergam longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ernesto — buenos días. Vine a mostrar el río al forastero.",
                    "translation": "Ernesto — bom dia. Vim mostrar o río pro forasteiro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Ernesto para na frente de vocês, olha pra você, depois pro río. Don Miguel disse 'buenos días' — é de manhã. Qual hora do dia é essa?",
                    "options": [
                        {"id": "a", "text": "De manhã — hora do buenos días"},
                        {"id": "b", "text": "De tarde — hora do buenas tardes"},
                        {"id": "c", "text": "De noite — hora do buenas noches"},
                        {"id": "d", "text": "Meio-dia — sem saudação específica"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. O sol ainda está subindo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Ernesto",
                    "line": "...",
                    "translation": "(O velho não responde imediatamente. Te olha.)",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Ernesto te examina por tempo demais. Os olhos vão do rosto "
                        "pra mão, de volta pro rosto. Don Miguel ri nervoso."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Ernesto finalmente fala — em espanhol lento, sem tirar os olhos de você: '¿Cómo te llamas?' Como você responde?",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Hay árboles"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Ernesto ouviu, assentiu devagar. Não disse nada mais por um longo segundo.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ───────────────────────────────────────────────────────
    # Ernesto faz algo estranho. Ele pega uma pedra lisa do río, examina, e a
    # entrega ao protagonista dizendo algo que não faz sentido.
    # A narrativa aqui é densa — menos exercícios, mais beats. O vocab é usado
    # dentro da conversa.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Ernesto el Leñador"],
                "story": (
                    "Ernesto te olhou por tempo demais antes de perguntar seu nome. "
                    "Quando você respondeu, ele ficou quieto uns instantes. Don Miguel "
                    "ficou desconfortável — você percebeu.\n\n"
                    "Ernesto ainda está parado na margem do río, machado no ombro, "
                    "te observando."
                ),
                "now": "Ernesto vai fazer algo que ninguém esperava.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Ernesto abaixa o machado devagar. Entra no río com as botas — a água na canela — e pega uma pedra do fundo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Ernesto",
                    "line": "Esta piedra del río. Tómala.",
                    "translation": "Essa pedra do rio. Pega.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você pegou a pedra. Lisa, pesada, fria. Branca com uma veia cinza no meio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Ernesto",
                    "line": "El río la hizo así. Años y años de agua.",
                    "translation": "O río fez ela assim. Anos e anos de água.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Ernesto",
                    "question": "Ernesto disse 'Esta piedra del río'. Que objeto ele te entregou?",
                    "options": [
                        {"id": "a", "text": "Piedra"},
                        {"id": "b", "text": "Flor"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "Agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_piedra", "target": "piedra", "native": "pedra",
                    "npc_reaction": "Piedra. Do río. Guarda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Ernesto",
                    "line": "Forastero — tienes algo. En los ojos. Como los que escuchan la tierra.",
                    "translation": "Forasteiro — você tem algo. Nos olhos. Como os que escutam a terra.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você não entendeu completamente. Mas 'tienes algo' ficou claro o suficiente — ele estava dizendo que você tem algo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ernesto — ¿qué dices?",
                    "translation": "Ernesto — o que você está dizendo?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Ernesto",
                    "line": "Nada. Buenos días, Miguel. Forastero.",
                    "translation": "Nada. Bom dia, Miguel. Forasteiro.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Ernesto pegou o machado e foi embora pela margem. Não olhou pra trás.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel ficou quieto olhando Ernesto ir embora. Depois te olhou. '¿Estás bien?' — como você está?",
                    "options": [
                        {"id": "a", "text": "Bien... pero raro"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "No hay agua"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bien. Ernesto é assim — fala coisas, vai embora. Não se preocupa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você está segurando a pedra do río. Don Miguel aponta pra ela: '¿Qué tienes ahí?' Você olha e responde:",
                    "options": [
                        {"id": "a", "text": "Una piedra del río"},
                        {"id": "b", "text": "Una flor del campo"},
                        {"id": "c", "text": "Pan de Rosa"},
                        {"id": "d", "text": "Agua del río"},
                    ],
                    "correct": "a",
                    "word_id": "es_piedra", "target": "piedra", "native": "pedra",
                    "npc_reaction": "Piedra del río. Guarda. Ernesto não dá coisas pra qualquer um.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel joga o saco nas costas. O sol já está mais alto — "
                        "hora de voltar. Você pôs a pedra no bolso. Ela estava fria "
                        "ainda. Você se perguntou o que Ernesto quis dizer."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Voltando ao pueblo pelo campo. Don Miguel vai na frente, você fica pra trás
    # cansado. Dois trabalhadores do campo te abordam — curiosos com o forasteiro.
    # Você tem que usar tudo que aprendeu pra se apresentar e explicar o que há
    # no campo. Seção gated — errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Ernesto foi embora. Vocês comeram o pão seco do saco de Miguel "
                    "à beira do río. Depois Don Miguel se levantou. 'Vamos voltando.'\n\n"
                    "O caminho de volta é longo e o sol esquentou. Don Miguel caminhou "
                    "mais rápido — conversando com ele mesmo, em espanhol, sobre as "
                    "plantas do campo. Você ficou pra trás."
                ),
                "now": "Você está sozinho no caminho. Dois trabalhadores do campo se aproximam.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌾 Caminho de terra. Don Miguel é um ponto distante lá na frente. Dois homens com enxadas param na sua frente — curiosos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 1",
                    "line": "¡Hola! ¿Eres el forastero nuevo?",
                    "translation": "Olá! Você é o forasteiro novo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 1",
                    "question": "O homem perguntou '¡Hola!' e quer saber quem você é. O que você responde primeiro?",
                    "options": [
                        {"id": "a", "text": "¡Hola! Sí, soy el forastero"},
                        {"id": "b", "text": "No hay pan"},
                        {"id": "c", "text": "Tengo sed"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "O homem ri. 'Sabíamos que ia aparecer um forasteiro. Miguel falou.' ",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 2",
                    "line": "¿Y cómo te llamas?",
                    "translation": "E como você se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 2",
                    "question": "O segundo homem quer saber seu nome. Você responde:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Hay árboles"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "'Ah! Mucho gusto.' Os dois inclinam a cabeça.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 1",
                    "line": "¿Y por acá — hay algo especial? ¿Viste el río?",
                    "translation": "E por aqui — tem algo especial? Você viu o río?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 1",
                    "question": "Você acabou de passar o dia no río. Você viu muita coisa. O que há por lá?",
                    "options": [
                        {"id": "a", "text": "Hay árboles, piedras y agua"},
                        {"id": "b", "text": "No hay nada"},
                        {"id": "c", "text": "Hay pan y posada"},
                        {"id": "d", "text": "No hay árboles"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "árbol", "native": "árvore",
                    "npc_reaction": "Os dois assentem. 'Siempre hay árboles y piedras en el río. Claro.'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 2",
                    "line": "¿Cómo estás, forastero? El sol está fuerte hoy.",
                    "translation": "Como você está, forasteiro? O sol está forte hoje.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 2",
                    "question": "Você caminhou bastante, bebeu do río, ainda tem a pedra no bolso. Como você está?",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo sed"},
                        {"id": "d", "text": "No hay agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "'¡Bien! Eso es.' Os dois riem. 'Bem-vindo ao campo, forastero.'",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Os dois levantam as enxadas e seguem caminho. Don Miguel já parou pra te esperar lá na frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¡Forastero! ¿Qué pasó? ¿Estás bien?",
                    "translation": "Forasteiro! O que aconteceu? Está bem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel voltou pra te esperar, preocupado. Mas você se virou bem. Como você responde?",
                    "options": [
                        {"id": "a", "text": "Sí — me presenté solo"},
                        {"id": "b", "text": "Mal — tengo miedo"},
                        {"id": "c", "text": "No hay nada"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Don Miguel sorriu. 'Solo. Bien hecho, forastero.'",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês voltaram ao pueblo com o sol se pondo. Você com a "
                        "pedra do río no bolso — fria ainda, lisa, pesada.\n\n"
                        "Você se perguntou o que Ernesto quis dizer com 'tienes algo "
                        "en los ojos'. E o que eram 'los que escuchan la tierra'."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────

class Command(BaseCommand):
    help = "Seed das 6 seções da Fase 3 Espanhol A1 (requer seed_es_full antes)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Apaga e recria as seções (default: pula se já existem)",
        )

    def handle(self, *args, **options):
        self.stdout.write("\n📦 Seeding seções — ES A1 T1 Fase 3\n")

        try:
            chapter = AdventureChapter.objects.get(slug="es-a1-t1")
        except AdventureChapter.DoesNotExist:
            raise CommandError(
                "Chapter 'es-a1-t1' não encontrado. Rode 'seed_es_full' primeiro."
            )

        try:
            phase = AdventurePhase.objects.get(chapter=chapter, number=3)
        except AdventurePhase.DoesNotExist:
            raise CommandError(
                "Fase 3 do chapter 'es-a1-t1' não encontrada. Rode 'seed_es_full' primeiro."
            )

        existing = PhaseSection.objects.filter(phase=phase).count()
        if existing and not options["reset"]:
            self.stdout.write(
                self.style.WARNING(
                    f"  Fase 3 já tem {existing} seções. Use --reset para recriar."
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
            f"\n✅ {created_count} seções criadas para Fase 3 · ES A1 T1\n"
            "   Endpoint: GET /api/adventure/phases/{phase_id}/sections/\n"
        ))
