"""
Seed das 6 seÃ§Ãµes da Fase 3 Italiano A1 â€” "La Strada di Terra".

Primeiro dia fora dos muros do borgo. Antonio leva o protagonista pelo
caminho de terra que cruza os campos e chega atÃ© o rio. LÃ encontram El Viejo
LeÃ±ador â€” um velho lenhador que reage ao protagonista de forma estranha.

Novos vocab (3): Ãrbol · pietra · rÃ­o
RevisÃ£o F1+F2: ciao, buongiorno, buonasera, grazie, bene/male,
               straniero, mi chiamo, ho fame, ho sete, pane, acqua
NPC principal:   Antonio (fio condutor)
NPC cameo:       El Viejo LeÃ±ador (reaÃ§Ã£o estranha â€” primeiro sinal do dom)
Itens:           pietra_del_rÃ­o (word_id: it_pietra) · fiore_silvestre (word_id: it_fiore)
Arco emocional:  confinado â†’ expanesivo; curiosidade + primeiro pressentimento
TransiÃ§Ã£o:       voltam ao borgo ao entardecer; Nico quieto; pedra no bolso
                 do protagonista como lembranÃ§a do dia.

PrÃ©-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # ManhÃ£ â€” Antonio propÃµe sair dos muros. PortÃ£o do borgo, campos abertos,
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
                        "ðŸŒ„ ManhÃ£ clara. Antonio estÃ na porta da locanda com um "
                        "saco velho Ã s costas. Aponta pro portÃ£o de madeira pesada "
                        "na borda do borgo â€” a saÃ­da pros campos."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Oggi usciamo. Voglio che tu veda il campo. Ci sono cose che il borgo non insegna.",
                },
                {
                    "kind": "player",
                    "text": "VocÃª seguiu sem perguntar. Faz dias que vocÃª sÃ³ viu pedra clara e pedra. A ideia de campo aberto parecia boa.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸŒ¾ O portÃ£o abre pesado. Do outro lado: campos de milho, um caminho de terra batida, e longe â€” o verde-escuro de Ãrvores.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Guarda â€” los Ãrboles allÃ. El rÃ­o estÃ detrÃs de ellos.",
                },
                {
                    "kind": "player",
                    "text": "Ãrboles. Rio. A palavra era nova, mas o gesto era claro â€” ele apontou pro verde e depois fez um gesto de Ãgua corrindo.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Y en el camino â€” pietre. Attenzione con los pies.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸª¨ Caminho cheio de pedras brancas. VocÃª olhou pra baixo â€” algumas lisas, algumas pontiagudas.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Ey! Stai bene? Cammina â€” no mires tanto el suelo.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "VocÃª ergueu a cabeÃ§a. O campo se abria de todos os lados. Depois de dias no borgo fechado, aquilo parecia enorme.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio apontou pro verde-escuro no horizonte e disse uma palavra. O que vocÃª vÃª ao longe?",
                    "options": [
                        {"id": "a", "text": "Ãrboles"},
                        {"id": "b", "text": "Pietre"},
                        {"id": "c", "text": "El rÃ­o"},
                        {"id": "d", "text": "La locanda"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "Ãrbol", "native": "Ãrvore",
                    "npc_reaction": "Ãrboles. Onde tem Ãrbol, tem sombra. E onde tem sombra...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O caminho estava cheio delas â€” brancas, lisas, pontiagudas. Antonio avisou pra vocÃª cuidar dos pÃ©s. O que estava no caminho?",
                    "options": [
                        {"id": "a", "text": "Pietre"},
                        {"id": "b", "text": "Ãrboles"},
                        {"id": "c", "text": "Acqua"},
                        {"id": "d", "text": "Fiorees"},
                    ],
                    "correct": "a",
                    "word_id": "it_pietra", "target": "pietra", "native": "pedra",
                    "npc_reaction": "Pietre. O chÃ£o do campo sempre tem pietre. Os pÃ©s aprendem.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio fez um gesto â€” as duas mÃ£os corrindo pra frente â€” e apontou atrÃs das Ãrvores. O que estÃ alÃ©m das Ãrvores?",
                    "options": [
                        {"id": "a", "text": "El rÃ­o"},
                        {"id": "b", "text": "El borgo"},
                        {"id": "c", "text": "La locanda"},
                        {"id": "d", "text": "El mercado"},
                    ],
                    "correct": "a",
                    "word_id": "it_rio", "target": "rÃ­o", "native": "rio",
                    "npc_reaction": "El rÃ­o. Ãgua fria, acqua limpia. Melhor que a fonte da piazza.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃªs caminharam bastante. O sol esquentou. O que vocÃª provavelmente vai querer ao chegar no rÃ­o?",
                    "options": [
                        {"id": "a", "text": "Acqua â€” ho sete"},
                        {"id": "b", "text": "Pane â€” ho fame"},
                        {"id": "c", "text": "La locanda"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. E o rÃ­o vai resolver isso.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # No campo, Antonio aproveita o caminho pra revisar F1+F2 vocab.
    # SituaÃ§Ãµes reais: um pÃssaro, uma fiore, parar pra beber Ãgua.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "VocÃªs passaram pelo portÃ£o e o campo se abriu. Antonio "
                    "apontou 'Ãrboles', 'pietre', 'el rÃ­o'. O campo Ã© diferente "
                    "do borgo â€” mais silÃªncio, mais espaÃ§o, o cheiro de terra.\n\n"
                    "Enquanto caminham, Antonio continua te testando. 'O campo "
                    "tambÃ©m ensina. VocÃª olha, eu pergunto.'"
                ),
                "now": "RevisÃ£o das palavras de F1 e F2 â€” cada uma num contexto de campo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio para, pega uma pedra lisa do chÃ£o e te joga. VocÃª pega no ar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Come stai hoy? Con il campo y el sol?",
                    "translation": "Como vocÃª estÃ hoje? Com o campo e o sol?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O ar estÃ limpo, o campo aberto, vocÃª comeu o pÃ£o de Giulia antes de sair. Antonio quer saber como vocÃª estÃ:",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Ho sete"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. O campo faz isso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E la mattina, quando arrivi in un posto nuovo e vedi qualcuno?",
                    "translation": "Ei â€” e de manhÃ£, quando vocÃª chega num lugar novo e vÃª alguÃ©m?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um trabalhador do campo passa com uma enxada. Ã‰ cedo ainda. VocÃª cumprimenta:",
                    "options": [
                        {"id": "a", "text": "Buongiorno!"},
                        {"id": "b", "text": "Buonanotte!"},
                        {"id": "c", "text": "Ciao noche!"},
                        {"id": "d", "text": "AdiÃ³s!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Buongiorno. O trabalhador levantou dois dedos â€” reconheceu.",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio aponta pra uma fiore vermelha no borde do caminho. 'Fiore silvestre â€” fiore do campo.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um menino do borgo passa corrindo e para quando vÃª a fiore â€” 'La fiore, quÃ© bonita!' O que ele viu?",
                    "options": [
                        {"id": "a", "text": "Fiore"},
                        {"id": "b", "text": "Pietra"},
                        {"id": "c", "text": "Ãrbol"},
                        {"id": "d", "text": "RÃ­o"},
                    ],
                    "correct": "a",
                    "word_id": "it_fiore", "target": "fiore", "native": "fiore",
                    "npc_reaction": "Fiore silvestre. Essa Ã© do campo â€” nÃ£o cresce na piazza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "El straniero â€” asÃ­ te llaman. Pero te acuerdas quÃ© significa?",
                    "translation": "O straniero â€” assim te chamam. Mas vocÃª lembra o que significa?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra vocÃª: 'Quelli del borgo ti chiamano straniero perche...'",
                    "options": [
                        {"id": "a", "text": "VocÃª veio de fora â€” nÃ£o Ã© do borgo"},
                        {"id": "b", "text": "VocÃª nÃ£o tem nome"},
                        {"id": "c", "text": "VocÃª trabalha no campo"},
                        {"id": "d", "text": "VocÃª Ã© muito jovem"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "Eso. Straniero = de fora. Mas o borgo jÃ tÃ acostumando contigo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E io, che cosa sono? Recuerdas la palabra?",
                    "translation": "E eu â€” o que sou? VocÃª lembra a palavra?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio arranca um pedaÃ§o de erva do chÃ£o, cheira. Trabalha com a terra toda a vida. Ele Ã©:",
                    "options": [
                        {"id": "a", "text": "Contadino"},
                        {"id": "b", "text": "Straniero"},
                        {"id": "c", "text": "Doctor"},
                        {"id": "d", "text": "Maestro"},
                    ],
                    "correct": "a",
                    "word_id": "it_contadino", "target": "contadino", "native": "camponÃªs",
                    "npc_reaction": "Contadino. E orgulhoso disso.",
                },
                {
                    "kind": "narrative",
                    "text": "As Ãrvores estÃ£o mais perto. Um som novo â€” Ãgua corrindo, fresco, abaixo do ruÃ­do do vento.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª ouviu o som, ficou com a boca seca de querer beber. Antonio olhou pra vocÃª. VocÃª fala:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Estoy male"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. El rÃ­o tÃ ali. JÃ estamos chegando.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: GramÃtica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Chegaram ao rÃ­o. Antonio ensina "c'e" + lugar:
    # "C'e Ãrboles. C'e pietre. C'e acqua en el rÃ­o."
    # TambÃ©m: "non c'e" â€” "non c'e pane aquÃ­".
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "VocÃªs chegaram ao rÃ­o. Ãgua fria, pedras brancas no fundo, "
                    "sombra das Ãrvores. Antonio jogou o saco no chÃ£o e sentou "
                    "numa pedra grande.\n\n"
                    "'Olha o que tem aqui. Aprenda a dizer.'"
                ),
                "now": "Antonio ensina 'c'e' â€” a forma de dizer que algo existe num lugar.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio aponta em volta â€” Ãrvores, pedras, o rÃ­o, o cÃ©u. Faz um gesto amplo com o braÃ§o.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "'C'e' â€” questo si usa quando qualcosa e qui. 'C'e Ãrboles.'",
                    "translation": "'C'e' â€” isso vocÃª usa quando algo estÃ aqui. 'HÃ Ãrvores.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "C'e Ãrboles",
                    "meaning": "HÃ Ãrvores / Tem Ãrvores",
                    "note": "c'e = hÃ / tem | serve pra qualquer coisa: c'e acqua, c'e pane, c'e pietre",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y si algo no estÃ â€” 'non c'e'. Simple. 'Non c'e pane aquÃ­ en il campo.'",
                    "translation": "E se algo nÃ£o estÃ â€” 'nÃ£o tem'. Simples. 'NÃ£o tem pÃ£o aqui no campo.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Non c'e pane",
                    "meaning": "NÃ£o tem pÃ£o / NÃ£o hÃ pÃ£o",
                    "note": "non c'e = nÃ£o tem | o oposto de c'e",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "C'e",    "isKey": True},
                        {"text": " + ",    "isKey": False},
                        {"text": "coisa",  "isKey": True},
                        {"text": " | ",    "isKey": False},
                        {"text": "Non c'e", "isKey": True},
                        {"text": " + ",    "isKey": False},
                        {"text": "coisa",  "isKey": True},
                    ],
                    "example": "C'e pietre en el rÃ­o. / Non c'e pane aquÃ­.",
                    "translation": "Tem pedras no rio. / NÃ£o tem pÃ£o aqui.",
                    "note": "C'e = existe. Non c'e = nÃ£o existe. Um padrÃ£o, infinitas coisas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pro rÃ­o com pedras brancas no fundo. Como vocÃª descreve?",
                    "options": [
                        {"id": "a", "text": "C'e pietre en el rÃ­o"},
                        {"id": "b", "text": "Non c'e pietre"},
                        {"id": "c", "text": "C'e pane en el rÃ­o"},
                        {"id": "d", "text": "Ho pietre"},
                    ],
                    "correct": "a",
                    "word_id": "it_pietra", "target": "pietra", "native": "pedra",
                    "npc_reaction": "C'e pietre. Exato. O rÃ­o fala por si mesmo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª olha pra volta â€” sÃ³ campo, Ãrvores e rio. NÃ£o hÃ nenhuma padaria. Antonio: 'C'e pane aquÃ­?'",
                    "options": [
                        {"id": "a", "text": "Non c'e pane"},
                        {"id": "b", "text": "C'e pane"},
                        {"id": "c", "text": "Ho pane"},
                        {"id": "d", "text": "C'e acqua"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Non c'e pane. Non c'e Giulia tampoco. SÃ³ campo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Pero â€” c'e acqua?",
                    "translation": "Mas â€” tem Ãgua?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O rÃ­o estÃ na sua frente, corrindo sobre pedras brancas. Antonio espera:",
                    "options": [
                        {"id": "a", "text": "SÃ­, c'e acqua"},
                        {"id": "b", "text": "Non c'e acqua"},
                        {"id": "c", "text": "Ho acqua"},
                        {"id": "d", "text": "C'e pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "Ãgua",
                    "npc_reaction": "SÃ­, c'e acqua. Mucha acqua. Beba.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra cima, pras copas das Ãrvores. 'Y aquÃ­ â€” c'e Ãrboles?'",
                    "options": [
                        {"id": "a", "text": "SÃ­, c'e Ãrboles"},
                        {"id": "b", "text": "Non c'e Ãrboles"},
                        {"id": "c", "text": "C'e pietre"},
                        {"id": "d", "text": "C'e pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "Ãrbol", "native": "Ãrvore",
                    "npc_reaction": "C'e Ãrboles. E eles ficam aqui hÃ cem anos â€” antes do borgo.",
                },
                {
                    "kind": "narrative",
                    "text": "Ao longe, um som de machado batendo em madeira. Ritmado, constante. Antonio levanta a cabeÃ§a.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ese es el viejo Pietro. El leÃ±ador. Viene aquÃ­ hace treinta aÃ±os.",
                    "translation": "Esse Ã© o velho Pietro. O lenhador. Vem aqui hÃ trinta anos.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: PrÃtica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Encontro com El Viejo LeÃ±ador (Pietro). Pratica c'e/non c'e em situaÃ§Ãµes
    # reais do campo enquanto o lenhador se aproxima. NPC presente em cada exercÃ­cio.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Antonio te ensinou 'c'e' e 'non c'e'. Ãrboles, pietre, "
                    "acqua â€” tudo que estÃ ao redor pode ser descrito assim.\n\n"
                    "O som do machado ficou mais prÃ³ximo. O velho Pietro estÃ "
                    "vindo pela margem do rÃ­o."
                ),
                "now": "PrÃtica rÃpida antes do encontro com o leÃ±ador.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Antes de ele chegar â€” vamos praticar rÃpido. Olha ao redor e responde.",
                    "translation": "Antes dele chegar â€” vamos praticar rÃpido. Olha ao redor e responde.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pro outro lado do rÃ­o â€” sÃ³ pedras, grama, sem Ãrvores. 'C'e Ãrboles allÃ?'",
                    "options": [
                        {"id": "a", "text": "No, non c'e Ãrboles"},
                        {"id": "b", "text": "SÃ­, c'e Ãrboles"},
                        {"id": "c", "text": "C'e pane allÃ"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "Ãrbol", "native": "Ãrvore",
                    "npc_reaction": "Non c'e Ãrboles allÃ. Corrito.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio abre o saco â€” tem um pedaÃ§o de pÃ£o seco lÃ dentro. 'C'e pane?'",
                    "options": [
                        {"id": "a", "text": "SÃ­, c'e pane"},
                        {"id": "b", "text": "Non c'e pane"},
                        {"id": "c", "text": "C'e acqua"},
                        {"id": "d", "text": "Non c'e acqua"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pÃ£o",
                    "npc_reaction": "C'e pane. Seco, mas c'e.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª estÃ com fome depois de caminhar bastante. Como vocÃª fala pro Antonio?",
                    "options": [
                        {"id": "a", "text": "Ho fame"},
                        {"id": "b", "text": "Ho sete"},
                        {"id": "c", "text": "Estoy bene"},
                        {"id": "d", "text": "Non c'e pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_hambre", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Hambre. Pega o pÃ£o do saco â€” hÃ um lÃ.",
                },
                {
                    "kind": "narrative",
                    "text": "Pietro chega pela margem do rÃ­o. Alto, pele curtida, machado no ombro. Olhos pequenos que enxergam longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Pietro â€” buongiorno. Vine a mostrar el rÃ­o al straniero.",
                    "translation": "Pietro â€” bom dia. Vim mostrar o rÃ­o pro straniero.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Pietro para na frente de vocÃªs, olha pra vocÃª, depois pro rÃ­o. Antonio disse 'buongiorno' â€” Ã© de manhÃ£. Qual hora do dia Ã© essa?",
                    "options": [
                        {"id": "a", "text": "De manhÃ£ â€” hora do buongiorno"},
                        {"id": "b", "text": "De tarde â€” hora do buonasera"},
                        {"id": "c", "text": "De noite â€” hora do buonanotte"},
                        {"id": "d", "text": "Meio-dia â€” sem saudaÃ§Ã£o especÃ­fica"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Buongiorno. O sol ainda estÃ subindo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "...",
                    "translation": "(O velho nÃ£o responde imediatamente. Te olha.)",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Pietro te examina por tempo demais. Os olhos vÃ£o do rosto "
                        "pra mÃ£o, de volta pro rosto. Antonio ri nervoso."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Pietro finalmente fala â€” em italiano lento, sem tirar os olhos de vocÃª: 'Come ti chiami?' Como vocÃª responde?",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "C'e Ãrboles"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "Pietro ouviu, assentiu devagar. NÃ£o disse nada mais por um longo segundo.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Pietro faz algo estranho. Ele pega uma pedra lisa do rÃ­o, examina, e a
    # entrega ao protagonista dizendo algo que nÃ£o faz sentido.
    # A narrativa aqui Ã© densa â€” menos exercÃ­cios, mais beats. O vocab Ã© usado
    # dentro da conversa.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio", "Pietro el LeÃ±ador"],
                "story": (
                    "Pietro te olhou por tempo demais antes de perguntar seu nome. "
                    "Quando vocÃª respondeu, ele ficou quieto uns instantes. Antonio "
                    "ficou desconfortÃvel â€” vocÃª percebeu.\n\n"
                    "Pietro ainda estÃ parado na margem do rÃ­o, machado no ombro, "
                    "te observando."
                ),
                "now": "Pietro vai fazer algo que ninguÃ©m esperava.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Pietro abaixa o machado devagar. Entra no rÃ­o com as botas â€” a Ãgua na canela â€” e pega uma pedra do fundo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Esta pietra del rÃ­o. TÃ³malea.",
                    "translation": "Essa pedra do rio. Pega.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª pegou a pedra. Lisa, pesada, fria. Branca com uma veia cinza no meio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "El rÃ­o la hizo asÃ­. AÃ±os y aÃ±os de acqua.",
                    "translation": "O rÃ­o fez ela assim. Anos e anos de Ãgua.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro disse 'Esta pietra del rÃ­o'. Que objeto ele te entregou?",
                    "options": [
                        {"id": "a", "text": "Pietra"},
                        {"id": "b", "text": "Fiore"},
                        {"id": "c", "text": "Pane"},
                        {"id": "d", "text": "Acqua"},
                    ],
                    "correct": "a",
                    "word_id": "it_pietra", "target": "pietra", "native": "pedra",
                    "npc_reaction": "Pietra. Do rÃ­o. Guarda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Straniero, hai qualcosa. Negli occhi. Come quelli che ascoltano la terra.",
                    "translation": "Forasteiro â€” vocÃª tem algo. Nos olhos. Como os que escutam a terra.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o entendeu completamente. Mas 'tienes algo' ficou claro o suficiente â€” ele estava dizendo que vocÃª tem algo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Pietro â€” che dici?",
                    "translation": "Pietro â€” o que vocÃª estÃ dizendo?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Nada. Buongiorno, Nico. Straniero.",
                    "translation": "Nada. Bom dia, Nico. Forasteiro.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Pietro pegou o machado e foi embora pela margem. NÃ£o olhou pra trÃs.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio ficou quieto olhando Pietro ir embora. Depois te olhou. 'Stai bene?' â€” como vocÃª estÃ?",
                    "options": [
                        {"id": "a", "text": "Bene... ma raro"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Non c'e acqua"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bene. Pietro Ã© assim â€” fala coisas, vai embora. NÃ£o se preocupa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª estÃ segurando a pedra do rÃ­o. Antonio aponta pra ela: 'QuÃ© tienes ahÃ­?' VocÃª olha e responde:",
                    "options": [
                        {"id": "a", "text": "Una pietra del rÃ­o"},
                        {"id": "b", "text": "Una fiore dil campo"},
                        {"id": "c", "text": "Pane de Giulia"},
                        {"id": "d", "text": "Acqua del rÃ­o"},
                    ],
                    "correct": "a",
                    "word_id": "it_pietra", "target": "pietra", "native": "pedra",
                    "npc_reaction": "Pietra del rÃ­o. Guarda. Pietro nÃ£o dÃ coisas pra qualquer um.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio joga o saco nas costas. O sol jÃ estÃ mais alto â€” "
                        "hora de voltar. VocÃª pÃ´s a pedra no bolso. Ela estava fria "
                        "ainda. VocÃª se perguntou o que Pietro quis dizer."
                    ),
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃculo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Voltando ao borgo pelo campo. Antonio vai na frente, vocÃª fica pra trÃs
    # cansado. Dois trabalhadores do campo te abordam â€” curiosos com o straniero.
    # VocÃª tem que usar tudo que aprendeu pra se apresentar e explicar o que hÃ
    # no campo. SeÃ§Ã£o gated â€” errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Pietro foi embora. VocÃªs comeram o pÃ£o seco do saco de Nico "
                    "Ã  beira do rÃ­o. Depois Antonio se levantou. 'Vamos voltando.'\n\n"
                    "O caminho de volta Ã© longo e o sol esquentou. Antonio caminhou "
                    "mais rÃpido â€” conversando com ele mesmo, em italiano, sobre as "
                    "plantas do campo. VocÃª ficou pra trÃs."
                ),
                "now": "VocÃª estÃ sozinho no caminho. Dois trabalhadores do campo se aproximam.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ¾ Caminho de terra. Antonio Ã© um ponto distante lÃ na frente. Dois homens com enxadas param na sua frente â€” curiosos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 1",
                    "line": "Ciao! Eres el straniero nuevo?",
                    "translation": "OlÃ! VocÃª Ã© o straniero novo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 1",
                    "question": "O homem perguntou 'Ciao!' e quer saber quem vocÃª Ã©. O que vocÃª responde primeiro?",
                    "options": [
                        {"id": "a", "text": "Ciao! Si, sono lo straniero"},
                        {"id": "b", "text": "Non c'e pane"},
                        {"id": "c", "text": "Ho sete"},
                        {"id": "d", "text": "Buonanotte"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "O homem ri. 'SabÃ­amos que ia aparecer um straniero. Nico falou.' ",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 2",
                    "line": "Y come ti chiami?",
                    "translation": "E como vocÃª se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 2",
                    "question": "O segundo homem quer saber seu nome. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "C'e Ãrboles"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "'Ah! Piacere.' Os dois inclinam a cabeÃ§a.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 1",
                    "line": "Y por acÃ â€” c'e algo especial? Viste el rÃ­o?",
                    "translation": "E por aqui â€” tem algo especial? VocÃª viu o rÃ­o?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 1",
                    "question": "VocÃª acabou de passar o dia no rÃ­o. VocÃª viu muita coisa. O que hÃ por lÃ?",
                    "options": [
                        {"id": "a", "text": "C'e Ãrboles, pietre y acqua"},
                        {"id": "b", "text": "Non c'e nada"},
                        {"id": "c", "text": "C'e pane y locanda"},
                        {"id": "d", "text": "Non c'e Ãrboles"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "Ãrbol", "native": "Ãrvore",
                    "npc_reaction": "Os dois assentem. 'Siempre c'e Ãrboles y pietre en el rÃ­o. Claro.'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 2",
                    "line": "Come stai, straniero? El sol estÃ fuerte hoy.",
                    "translation": "Como vocÃª estÃ, straniero? O sol estÃ forte hoje.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 2",
                    "question": "VocÃª caminhou bastante, bebeu do rÃ­o, ainda tem a pedra no bolso. Como vocÃª estÃ?",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho sete"},
                        {"id": "d", "text": "Non c'e acqua"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "'Bene! Questo e.' Os dois riem. 'Bem-vindo ao campo, straniero.'",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Os dois levantam as enxadas e seguem caminho. Antonio jÃ parou pra te esperar lÃ na frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Straniero! QuÃ© pasÃ³? Stai bene?",
                    "translation": "Forasteiro! O que aconteceu? EstÃ bem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio voltou pra te esperar, preocupado. Mas vocÃª se virou bem. Como vocÃª responde?",
                    "options": [
                        {"id": "a", "text": "SÃ­ â€” me presentÃ© solo"},
                        {"id": "b", "text": "Male â€” ho paura"},
                        {"id": "c", "text": "Non c'e nada"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Antonio sorriu. 'Solo. Bene hecho, straniero.'",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs voltaram ao borgo com o sol se pondo. VocÃª com a "
                        "pedra do rÃ­o no bolso â€” fria ainda, lisa, pesada.\n\n"
                        "VocÃª se perguntou o que Pietro quis dizer com 'tienes algo "
                        "en los ojos'. E o que eram 'los que escuchan la tierra'."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
