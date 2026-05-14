"""
Seed das 6 seÃ§Ãµes da Fase 3 Espanhol A1 â€” "El Camino de Tierra".

Primeiro dia fora dos muros do pueblo. Don Miguel leva o protagonista pelo
caminho de terra que cruza os campos e chega atÃ© o rio. LÃ¡ encontram El Viejo
LeÃ±ador â€” um velho lenhador que reage ao protagonista de forma estranha.

Novos vocab (3): Ã¡rbol Â· piedra Â· rÃ­o
RevisÃ£o F1+F2: hola, buenos dÃ­as, buenas tardes, gracias, bien/mal,
               forastero, me llamo, tengo hambre, tengo sed, pan, agua
NPC principal:   Don Miguel (fio condutor)
NPC cameo:       El Viejo LeÃ±ador (reaÃ§Ã£o estranha â€” primeiro sinal do dom)
Itens:           piedra_del_rÃ­o (word_id: es_piedra) Â· flor_silvestre (word_id: es_flor)
Arco emocional:  confinado â†’ expansivo; curiosidade + primeiro pressentimento
TransiÃ§Ã£o:       voltam ao pueblo ao entardecer; Miguel quieto; pedra no bolso
                 do protagonista como lembranÃ§a do dia.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f3_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # ManhÃ£ â€” Don Miguel propÃµe sair dos muros. PortÃ£o do pueblo, campos abertos,
    # caminho de terra. Novo NPC (LeÃ±ador) ouvido ao longe. Vocab aparece sem
    # traduÃ§Ã£o â€” imersÃ£o. ExercÃ­cios: reconhecimento contextual.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ„ ManhÃ£ clara. Don Miguel estÃ¡ na porta da posada com um "
                        "saco velho Ã s costas. Aponta pro portÃ£o de madeira pesada "
                        "na borda do pueblo â€” a saÃ­da pros campos."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Hoy salimos. Quiero que veas el campo. Hay cosas que el pueblo no te enseÃ±a.",
                },
                {
                    "kind": "player",
                    "text": "VocÃª seguiu sem perguntar. Faz dias que vocÃª sÃ³ viu adobe e pedra. A ideia de campo aberto parecia boa.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸŒ¾ O portÃ£o abre pesado. Do outro lado: campos de milho, um caminho de terra batida, e longe â€” o verde-escuro de Ã¡rvores.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Mira â€” los Ã¡rboles allÃ¡. El rÃ­o estÃ¡ detrÃ¡s de ellos.",
                },
                {
                    "kind": "player",
                    "text": "Ãrboles. Rio. A palavra era nova, mas o gesto era claro â€” ele apontou pro verde e depois fez um gesto de Ã¡gua correndo.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Y en el camino â€” piedras. Cuidado con los pies.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸª¨ Caminho cheio de pedras brancas. VocÃª olhou pra baixo â€” algumas lisas, algumas pontiagudas.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¡Ey! Â¿EstÃ¡s bien? Camina â€” no mires tanto el suelo.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "VocÃª ergueu a cabeÃ§a. O campo se abria de todos os lados. Depois de dias no pueblo fechado, aquilo parecia enorme.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel apontou pro verde-escuro no horizonte e disse uma palavra. O que vocÃª vÃª ao longe?",
                    "options": [
                        {"id": "a", "text": "Ãrboles"},
                        {"id": "b", "text": "Piedras"},
                        {"id": "c", "text": "El rÃ­o"},
                        {"id": "d", "text": "La posada"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "Ã¡rbol", "native": "Ã¡rvore",
                    "npc_reaction": "Ãrboles. Onde tem Ã¡rbol, tem sombra. E onde tem sombra...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O caminho estava cheio delas â€” brancas, lisas, pontiagudas. Don Miguel avisou pra vocÃª cuidar dos pÃ©s. O que estava no caminho?",
                    "options": [
                        {"id": "a", "text": "Piedras"},
                        {"id": "b", "text": "Ãrboles"},
                        {"id": "c", "text": "Agua"},
                        {"id": "d", "text": "Flores"},
                    ],
                    "correct": "a",
                    "word_id": "es_piedra", "target": "piedra", "native": "pedra",
                    "npc_reaction": "Piedras. O chÃ£o do campo sempre tem piedras. Os pÃ©s aprendem.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel fez um gesto â€” as duas mÃ£os correndo pra frente â€” e apontou atrÃ¡s dos Ã¡rboles. O que estÃ¡ alÃ©m das Ã¡rvores?",
                    "options": [
                        {"id": "a", "text": "El rÃ­o"},
                        {"id": "b", "text": "El pueblo"},
                        {"id": "c", "text": "La posada"},
                        {"id": "d", "text": "El mercado"},
                    ],
                    "correct": "a",
                    "word_id": "es_rio", "target": "rÃ­o", "native": "rio",
                    "npc_reaction": "El rÃ­o. Ãgua fria, agua limpia. Melhor que a fonte da plaza.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃªs caminharam bastante. O sol esquentou. O que vocÃª provavelmente vai querer ao chegar no rÃ­o?",
                    "options": [
                        {"id": "a", "text": "Agua â€” tengo sed"},
                        {"id": "b", "text": "Pan â€” tengo hambre"},
                        {"id": "c", "text": "La posada"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. E o rÃ­o vai resolver isso.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # No campo, Don Miguel aproveita o caminho pra revisar F1+F2 vocab.
    # SituaÃ§Ãµes reais: um pÃ¡ssaro, uma flor, parar pra beber Ã¡gua.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "VocÃªs passaram pelo portÃ£o e o campo se abriu. Don Miguel "
                    "apontou 'Ã¡rboles', 'piedras', 'el rÃ­o'. O campo Ã© diferente "
                    "do pueblo â€” mais silÃªncio, mais espaÃ§o, o cheiro de terra.\n\n"
                    "Enquanto caminham, Don Miguel continua te testando. 'O campo "
                    "tambÃ©m ensina. VocÃª olha, eu pergunto.'"
                ),
                "now": "RevisÃ£o das palavras de F1 e F2 â€” cada uma num contexto de campo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel para, pega uma pedra lisa do chÃ£o e te joga. VocÃª pega no ar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿CÃ³mo estÃ¡s hoy? Con el campo y el sol?",
                    "translation": "Como vocÃª estÃ¡ hoje? Com o campo e o sol?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O ar estÃ¡ limpo, o campo aberto, vocÃª comeu o pÃ£o de Rosa antes de sair. Don Miguel quer saber como vocÃª estÃ¡:",
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
                    "line": "Oye â€” Â¿y en la maÃ±ana, cuando llegas a un sitio nuevo y ves a alguien?",
                    "translation": "Ei â€” e de manhÃ£, quando vocÃª chega num lugar novo e vÃª alguÃ©m?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um trabalhador do campo passa com uma enxada. Ã‰ cedo ainda. VocÃª cumprimenta:",
                    "options": [
                        {"id": "a", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "b", "text": "Â¡Buenas noches!"},
                        {"id": "c", "text": "Â¡Hola noche!"},
                        {"id": "d", "text": "Â¡AdiÃ³s!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. O trabalhador levantou dois dedos â€” reconheceu.",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel aponta pra uma flor vermelha no borde do caminho. 'Flor silvestre â€” flor do campo.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um menino do pueblo passa correndo e para quando vÃª a flor â€” 'La flor, quÃ© bonita!' O que ele viu?",
                    "options": [
                        {"id": "a", "text": "Flor"},
                        {"id": "b", "text": "Piedra"},
                        {"id": "c", "text": "Ãrbol"},
                        {"id": "d", "text": "RÃ­o"},
                    ],
                    "correct": "a",
                    "word_id": "es_flor", "target": "flor", "native": "flor",
                    "npc_reaction": "Flor silvestre. Essa Ã© do campo â€” nÃ£o cresce na plaza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "El forastero â€” asÃ­ te llaman. Â¿Pero te acuerdas quÃ© significa?",
                    "translation": "O forasteiro â€” assim te chamam. Mas vocÃª lembra o que significa?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra vocÃª: 'Los del pueblo te llaman forastero porque...'",
                    "options": [
                        {"id": "a", "text": "VocÃª veio de fora â€” nÃ£o Ã© do pueblo"},
                        {"id": "b", "text": "VocÃª nÃ£o tem nome"},
                        {"id": "c", "text": "VocÃª trabalha no campo"},
                        {"id": "d", "text": "VocÃª Ã© muito jovem"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Eso. Forastero = de fora. Mas o pueblo jÃ¡ tÃ¡ acostumando contigo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y yo â€” Â¿quÃ© soy? Â¿Recuerdas la palabra?",
                    "translation": "E eu â€” o que sou? VocÃª lembra a palavra?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel arranca um pedaÃ§o de erva do chÃ£o, cheira. Trabalha com a terra toda a vida. Ele Ã©:",
                    "options": [
                        {"id": "a", "text": "Campesino"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Doctor"},
                        {"id": "d", "text": "Maestro"},
                    ],
                    "correct": "a",
                    "word_id": "es_campesino", "target": "campesino", "native": "camponÃªs",
                    "npc_reaction": "Campesino. E orgulhoso disso.",
                },
                {
                    "kind": "narrative",
                    "text": "As Ã¡rvores estÃ£o mais perto. Um som novo â€” Ã¡gua correndo, fresco, abaixo do ruÃ­do do vento.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª ouviu o som, ficou com a boca seca de querer beber. Don Miguel olhou pra vocÃª. VocÃª fala:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. El rÃ­o tÃ¡ ali. JÃ¡ estamos chegando.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Chegaram ao rÃ­o. Don Miguel ensina "hay" + lugar:
    # "Hay Ã¡rboles. Hay piedras. Hay agua en el rÃ­o."
    # TambÃ©m: "no hay" â€” "no hay pan aquÃ­".
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "VocÃªs chegaram ao rÃ­o. Ãgua fria, pedras brancas no fundo, "
                    "sombra das Ã¡rvores. Don Miguel jogou o saco no chÃ£o e sentou "
                    "numa pedra grande.\n\n"
                    "'Olha o que tem aqui. Aprenda a dizer.'"
                ),
                "now": "Don Miguel ensina 'hay' â€” a forma de dizer que algo existe num lugar.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel aponta em volta â€” Ã¡rvores, pedras, o rÃ­o, o cÃ©u. Faz um gesto amplo com o braÃ§o.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "'Hay' â€” eso es lo que usas cuando algo estÃ¡ aquÃ­. 'Hay Ã¡rboles.'",
                    "translation": "'Hay' â€” isso vocÃª usa quando algo estÃ¡ aqui. 'HÃ¡ Ã¡rvores.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Hay Ã¡rboles",
                    "meaning": "HÃ¡ Ã¡rvores / Tem Ã¡rvores",
                    "note": "hay = hÃ¡ / tem | serve pra qualquer coisa: hay agua, hay pan, hay piedras",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y si algo no estÃ¡ â€” 'no hay'. Simple. 'No hay pan aquÃ­ en el campo.'",
                    "translation": "E se algo nÃ£o estÃ¡ â€” 'nÃ£o tem'. Simples. 'NÃ£o tem pÃ£o aqui no campo.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "No hay pan",
                    "meaning": "NÃ£o tem pÃ£o / NÃ£o hÃ¡ pÃ£o",
                    "note": "no hay = nÃ£o tem | o oposto de hay",
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
                    "example": "Hay piedras en el rÃ­o. / No hay pan aquÃ­.",
                    "translation": "Tem pedras no rio. / NÃ£o tem pÃ£o aqui.",
                    "note": "Hay = existe. No hay = nÃ£o existe. Um padrÃ£o, infinitas coisas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pro rÃ­o com pedras brancas no fundo. Como vocÃª descreve?",
                    "options": [
                        {"id": "a", "text": "Hay piedras en el rÃ­o"},
                        {"id": "b", "text": "No hay piedras"},
                        {"id": "c", "text": "Hay pan en el rÃ­o"},
                        {"id": "d", "text": "Tengo piedras"},
                    ],
                    "correct": "a",
                    "word_id": "es_piedra", "target": "piedra", "native": "pedra",
                    "npc_reaction": "Hay piedras. Exato. O rÃ­o fala por si mesmo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª olha pra volta â€” sÃ³ campo, Ã¡rvores e rio. NÃ£o hÃ¡ nenhuma padaria. Don Miguel: 'Â¿Hay pan aquÃ­?'",
                    "options": [
                        {"id": "a", "text": "No hay pan"},
                        {"id": "b", "text": "Hay pan"},
                        {"id": "c", "text": "Tengo pan"},
                        {"id": "d", "text": "Hay agua"},
                    ],
                    "correct": "a",
                    "npc_reaction": "No hay pan. No hay Rosa tampoco. SÃ³ campo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Pero â€” Â¿hay agua?",
                    "translation": "Mas â€” tem Ã¡gua?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O rÃ­o estÃ¡ na sua frente, correndo sobre pedras brancas. Don Miguel espera:",
                    "options": [
                        {"id": "a", "text": "SÃ­, hay agua"},
                        {"id": "b", "text": "No hay agua"},
                        {"id": "c", "text": "Tengo agua"},
                        {"id": "d", "text": "Hay pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "Ã¡gua",
                    "npc_reaction": "SÃ­, hay agua. Mucha agua. Beba.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra cima, pras copas das Ã¡rvores. 'Â¿Y aquÃ­ â€” hay Ã¡rboles?'",
                    "options": [
                        {"id": "a", "text": "SÃ­, hay Ã¡rboles"},
                        {"id": "b", "text": "No hay Ã¡rboles"},
                        {"id": "c", "text": "Hay piedras"},
                        {"id": "d", "text": "Hay pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "Ã¡rbol", "native": "Ã¡rvore",
                    "npc_reaction": "Hay Ã¡rboles. E eles ficam aqui hÃ¡ cem anos â€” antes do pueblo.",
                },
                {
                    "kind": "narrative",
                    "text": "Ao longe, um som de machado batendo em madeira. Ritmado, constante. Don Miguel levanta a cabeÃ§a.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ese es el viejo Ernesto. El leÃ±ador. Viene aquÃ­ hace treinta aÃ±os.",
                    "translation": "Esse Ã© o velho Ernesto. O lenhador. Vem aqui hÃ¡ trinta anos.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Encontro com El Viejo LeÃ±ador (Ernesto). Pratica hay/no hay em situaÃ§Ãµes
    # reais do campo enquanto o lenhador se aproxima. NPC presente em cada exercÃ­cio.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel te ensinou 'hay' e 'no hay'. Ãrboles, piedras, "
                    "agua â€” tudo que estÃ¡ ao redor pode ser descrito assim.\n\n"
                    "O som do machado ficou mais prÃ³ximo. O velho Ernesto estÃ¡ "
                    "vindo pela margem do rÃ­o."
                ),
                "now": "PrÃ¡tica rÃ¡pida antes do encontro com o leÃ±ador.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Antes de ele chegar â€” vamos praticar rÃ¡pido. Olha ao redor e responde.",
                    "translation": "Antes dele chegar â€” vamos praticar rÃ¡pido. Olha ao redor e responde.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pro outro lado do rÃ­o â€” sÃ³ pedras, grama, sem Ã¡rvores. 'Â¿Hay Ã¡rboles allÃ¡?'",
                    "options": [
                        {"id": "a", "text": "No, no hay Ã¡rboles"},
                        {"id": "b", "text": "SÃ­, hay Ã¡rboles"},
                        {"id": "c", "text": "Hay pan allÃ¡"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "Ã¡rbol", "native": "Ã¡rvore",
                    "npc_reaction": "No hay Ã¡rboles allÃ¡. Correto.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel abre o saco â€” tem um pedaÃ§o de pÃ£o seco lÃ¡ dentro. 'Â¿Hay pan?'",
                    "options": [
                        {"id": "a", "text": "SÃ­, hay pan"},
                        {"id": "b", "text": "No hay pan"},
                        {"id": "c", "text": "Hay agua"},
                        {"id": "d", "text": "No hay agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pÃ£o",
                    "npc_reaction": "Hay pan. Seco, mas hay.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª estÃ¡ com fome depois de caminhar bastante. Como vocÃª fala pro Don Miguel?",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "No hay pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. Pega o pÃ£o do saco â€” hÃ¡ um lÃ¡.",
                },
                {
                    "kind": "narrative",
                    "text": "Ernesto chega pela margem do rÃ­o. Alto, pele curtida, machado no ombro. Olhos pequenos que enxergam longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ernesto â€” buenos dÃ­as. Vine a mostrar el rÃ­o al forastero.",
                    "translation": "Ernesto â€” bom dia. Vim mostrar o rÃ­o pro forasteiro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Ernesto para na frente de vocÃªs, olha pra vocÃª, depois pro rÃ­o. Don Miguel disse 'buenos dÃ­as' â€” Ã© de manhÃ£. Qual hora do dia Ã© essa?",
                    "options": [
                        {"id": "a", "text": "De manhÃ£ â€” hora do buenos dÃ­as"},
                        {"id": "b", "text": "De tarde â€” hora do buenas tardes"},
                        {"id": "c", "text": "De noite â€” hora do buenas noches"},
                        {"id": "d", "text": "Meio-dia â€” sem saudaÃ§Ã£o especÃ­fica"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. O sol ainda estÃ¡ subindo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Ernesto",
                    "line": "...",
                    "translation": "(O velho nÃ£o responde imediatamente. Te olha.)",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Ernesto te examina por tempo demais. Os olhos vÃ£o do rosto "
                        "pra mÃ£o, de volta pro rosto. Don Miguel ri nervoso."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Ernesto finalmente fala â€” em espanhol lento, sem tirar os olhos de vocÃª: 'Â¿CÃ³mo te llamas?' Como vocÃª responde?",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Hay Ã¡rboles"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Ernesto ouviu, assentiu devagar. NÃ£o disse nada mais por um longo segundo.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Ernesto faz algo estranho. Ele pega uma pedra lisa do rÃ­o, examina, e a
    # entrega ao protagonista dizendo algo que nÃ£o faz sentido.
    # A narrativa aqui Ã© densa â€” menos exercÃ­cios, mais beats. O vocab Ã© usado
    # dentro da conversa.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Ernesto el LeÃ±ador"],
                "story": (
                    "Ernesto te olhou por tempo demais antes de perguntar seu nome. "
                    "Quando vocÃª respondeu, ele ficou quieto uns instantes. Don Miguel "
                    "ficou desconfortÃ¡vel â€” vocÃª percebeu.\n\n"
                    "Ernesto ainda estÃ¡ parado na margem do rÃ­o, machado no ombro, "
                    "te observando."
                ),
                "now": "Ernesto vai fazer algo que ninguÃ©m esperava.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Ernesto abaixa o machado devagar. Entra no rÃ­o com as botas â€” a Ã¡gua na canela â€” e pega uma pedra do fundo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Ernesto",
                    "line": "Esta piedra del rÃ­o. TÃ³mala.",
                    "translation": "Essa pedra do rio. Pega.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª pegou a pedra. Lisa, pesada, fria. Branca com uma veia cinza no meio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Ernesto",
                    "line": "El rÃ­o la hizo asÃ­. AÃ±os y aÃ±os de agua.",
                    "translation": "O rÃ­o fez ela assim. Anos e anos de Ã¡gua.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Ernesto",
                    "question": "Ernesto disse 'Esta piedra del rÃ­o'. Que objeto ele te entregou?",
                    "options": [
                        {"id": "a", "text": "Piedra"},
                        {"id": "b", "text": "Flor"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "Agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_piedra", "target": "piedra", "native": "pedra",
                    "npc_reaction": "Piedra. Do rÃ­o. Guarda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Ernesto",
                    "line": "Forastero â€” tienes algo. En los ojos. Como los que escuchan la tierra.",
                    "translation": "Forasteiro â€” vocÃª tem algo. Nos olhos. Como os que escutam a terra.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o entendeu completamente. Mas 'tienes algo' ficou claro o suficiente â€” ele estava dizendo que vocÃª tem algo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ernesto â€” Â¿quÃ© dices?",
                    "translation": "Ernesto â€” o que vocÃª estÃ¡ dizendo?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Ernesto",
                    "line": "Nada. Buenos dÃ­as, Miguel. Forastero.",
                    "translation": "Nada. Bom dia, Miguel. Forasteiro.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Ernesto pegou o machado e foi embora pela margem. NÃ£o olhou pra trÃ¡s.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel ficou quieto olhando Ernesto ir embora. Depois te olhou. 'Â¿EstÃ¡s bien?' â€” como vocÃª estÃ¡?",
                    "options": [
                        {"id": "a", "text": "Bien... pero raro"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "No hay agua"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bien. Ernesto Ã© assim â€” fala coisas, vai embora. NÃ£o se preocupa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª estÃ¡ segurando a pedra do rÃ­o. Don Miguel aponta pra ela: 'Â¿QuÃ© tienes ahÃ­?' VocÃª olha e responde:",
                    "options": [
                        {"id": "a", "text": "Una piedra del rÃ­o"},
                        {"id": "b", "text": "Una flor del campo"},
                        {"id": "c", "text": "Pan de Rosa"},
                        {"id": "d", "text": "Agua del rÃ­o"},
                    ],
                    "correct": "a",
                    "word_id": "es_piedra", "target": "piedra", "native": "pedra",
                    "npc_reaction": "Piedra del rÃ­o. Guarda. Ernesto nÃ£o dÃ¡ coisas pra qualquer um.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel joga o saco nas costas. O sol jÃ¡ estÃ¡ mais alto â€” "
                        "hora de voltar. VocÃª pÃ´s a pedra no bolso. Ela estava fria "
                        "ainda. VocÃª se perguntou o que Ernesto quis dizer."
                    ),
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Voltando ao pueblo pelo campo. Don Miguel vai na frente, vocÃª fica pra trÃ¡s
    # cansado. Dois trabalhadores do campo te abordam â€” curiosos com o forasteiro.
    # VocÃª tem que usar tudo que aprendeu pra se apresentar e explicar o que hÃ¡
    # no campo. SeÃ§Ã£o gated â€” errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Ernesto foi embora. VocÃªs comeram o pÃ£o seco do saco de Miguel "
                    "Ã  beira do rÃ­o. Depois Don Miguel se levantou. 'Vamos voltando.'\n\n"
                    "O caminho de volta Ã© longo e o sol esquentou. Don Miguel caminhou "
                    "mais rÃ¡pido â€” conversando com ele mesmo, em espanhol, sobre as "
                    "plantas do campo. VocÃª ficou pra trÃ¡s."
                ),
                "now": "VocÃª estÃ¡ sozinho no caminho. Dois trabalhadores do campo se aproximam.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ¾ Caminho de terra. Don Miguel Ã© um ponto distante lÃ¡ na frente. Dois homens com enxadas param na sua frente â€” curiosos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 1",
                    "line": "Â¡Hola! Â¿Eres el forastero nuevo?",
                    "translation": "OlÃ¡! VocÃª Ã© o forasteiro novo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 1",
                    "question": "O homem perguntou 'Â¡Hola!' e quer saber quem vocÃª Ã©. O que vocÃª responde primeiro?",
                    "options": [
                        {"id": "a", "text": "Â¡Hola! SÃ­, soy el forastero"},
                        {"id": "b", "text": "No hay pan"},
                        {"id": "c", "text": "Tengo sed"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "O homem ri. 'SabÃ­amos que ia aparecer um forasteiro. Miguel falou.' ",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 2",
                    "line": "Â¿Y cÃ³mo te llamas?",
                    "translation": "E como vocÃª se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 2",
                    "question": "O segundo homem quer saber seu nome. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Hay Ã¡rboles"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "'Ah! Mucho gusto.' Os dois inclinam a cabeÃ§a.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 1",
                    "line": "Â¿Y por acÃ¡ â€” hay algo especial? Â¿Viste el rÃ­o?",
                    "translation": "E por aqui â€” tem algo especial? VocÃª viu o rÃ­o?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 1",
                    "question": "VocÃª acabou de passar o dia no rÃ­o. VocÃª viu muita coisa. O que hÃ¡ por lÃ¡?",
                    "options": [
                        {"id": "a", "text": "Hay Ã¡rboles, piedras y agua"},
                        {"id": "b", "text": "No hay nada"},
                        {"id": "c", "text": "Hay pan y posada"},
                        {"id": "d", "text": "No hay Ã¡rboles"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "Ã¡rbol", "native": "Ã¡rvore",
                    "npc_reaction": "Os dois assentem. 'Siempre hay Ã¡rboles y piedras en el rÃ­o. Claro.'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 2",
                    "line": "Â¿CÃ³mo estÃ¡s, forastero? El sol estÃ¡ fuerte hoy.",
                    "translation": "Como vocÃª estÃ¡, forasteiro? O sol estÃ¡ forte hoje.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 2",
                    "question": "VocÃª caminhou bastante, bebeu do rÃ­o, ainda tem a pedra no bolso. Como vocÃª estÃ¡?",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo sed"},
                        {"id": "d", "text": "No hay agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "'Â¡Bien! Eso es.' Os dois riem. 'Bem-vindo ao campo, forastero.'",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Os dois levantam as enxadas e seguem caminho. Don Miguel jÃ¡ parou pra te esperar lÃ¡ na frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¡Forastero! Â¿QuÃ© pasÃ³? Â¿EstÃ¡s bien?",
                    "translation": "Forasteiro! O que aconteceu? EstÃ¡ bem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel voltou pra te esperar, preocupado. Mas vocÃª se virou bem. Como vocÃª responde?",
                    "options": [
                        {"id": "a", "text": "SÃ­ â€” me presentÃ© solo"},
                        {"id": "b", "text": "Mal â€” tengo miedo"},
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
                        "VocÃªs voltaram ao pueblo com o sol se pondo. VocÃª com a "
                        "pedra do rÃ­o no bolso â€” fria ainda, lisa, pesada.\n\n"
                        "VocÃª se perguntou o que Ernesto quis dizer com 'tienes algo "
                        "en los ojos'. E o que eram 'los que escuchan la tierra'."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
