"""
Seed das 6 seções da Fase 3 Italiano A1 — "La Strada di Terra".

Primeiro dia fora dos muros do borgo. Antonio leva o protagonista pelo
caminho de terra que cruza os campos e chega até o rio. L? encontram El Viejo
Leñador — um velho lenhador que reage ao protagonista de forma estranha.

Novos vocab (3): ?rbol · pietra · río
Revisão F1+F2: ciao, buongiorno, buonasera, grazie, bene/male,
               straniero, mi chiamo, ho fame, ho sete, pane, acqua
NPC principal:   Antonio (fio condutor)
NPC cameo:       El Viejo Leñador (reação estranha — primeiro sinal do dom)
Itens:           pietra_del_río (word_id: it_pietra) · fiore_silvestre (word_id: it_fiore)
Arco emocional:  confinado → expanesivo; curiosidade + primeiro pressentimento
Transição:       voltam ao borgo ao entardecer; Nico quieto; pedra no bolso
                 do protagonista como lembrança do dia.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Manhã — Antonio propõe sair dos muros. Portão do borgo, campos abertos,
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
                        "🌄 Manhã clara. Antonio est? na porta da locanda com um "
                        "saco velho às costas. Aponta pro portão de madeira pesada "
                        "na borda do borgo — a saída pros campos."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Oggi usciamo. Voglio che tu veda il campo. Ci sono cose che il borgo non insegna.",
                },
                {
                    "kind": "player",
                    "text": "Você seguiu sem perguntar. Faz dias que você só viu pedra clara e pedra. A ideia de campo aberto parecia boa.",
                },
                {
                    "kind": "scene",
                    "text": "🌾 O portão abre pesado. Do outro lado: campos de milho, um caminho de terra batida, e longe — o verde-escuro de ?rvores.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Guarda — los ?rboles all?. El río est? detr?s de ellos.",
                },
                {
                    "kind": "player",
                    "text": "Árboles. Rio. A palavra era nova, mas o gesto era claro — ele apontou pro verde e depois fez um gesto de ?gua corrindo.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Y en el camino — pietre. Attenzione con los pies.",
                },
                {
                    "kind": "scene",
                    "text": "🪨 Caminho cheio de pedras brancas. Você olhou pra baixo — algumas lisas, algumas pontiagudas.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Ey! Stai bene?Cammina — no mires tanto el suelo.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Você ergueu a cabeça. O campo se abria de todos os lados. Depois de dias no borgo fechado, aquilo parecia enorme.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio apontou pro verde-escuro no horizonte e disse uma palavra. O que você vê ao longe?",
                    "options": [
                        {"id": "a", "text": "Árboles"},
                        {"id": "b", "text": "Pietre"},
                        {"id": "c", "text": "El río"},
                        {"id": "d", "text": "La locanda"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "?rbol", "native": "?rvore",
                    "npc_reaction": "Árboles. Onde tem ?rbol, tem sombra. E onde tem sombra...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O caminho estava cheio delas — brancas, lisas, pontiagudas. Antonio avisou pra você cuidar dos pés. O que estava no caminho?",
                    "options": [
                        {"id": "a", "text": "Pietre"},
                        {"id": "b", "text": "Árboles"},
                        {"id": "c", "text": "Acqua"},
                        {"id": "d", "text": "Fiorees"},
                    ],
                    "correct": "a",
                    "word_id": "it_pietra", "target": "pietra", "native": "pedra",
                    "npc_reaction": "Pietre. O chão do campo sempre tem pietre. Os pés aprendem.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio fez um gesto — as duas mãos corrindo pra frente — e apontou atr?s das ?rvores. O que est? além das ?rvores?",
                    "options": [
                        {"id": "a", "text": "El río"},
                        {"id": "b", "text": "El borgo"},
                        {"id": "c", "text": "La locanda"},
                        {"id": "d", "text": "El mercado"},
                    ],
                    "correct": "a",
                    "word_id": "it_rio", "target": "río", "native": "rio",
                    "npc_reaction": "El río. Água fria, acqua limpia. Melhor que a fonte da piazza.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Vocês caminharam bastante. O sol esquentou. O que você provavelmente vai querer ao chegar no río?",
                    "options": [
                        {"id": "a", "text": "Acqua — ho sete"},
                        {"id": "b", "text": "Pane — ho fame"},
                        {"id": "c", "text": "La locanda"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. E o río vai resolver isso.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # No campo, Antonio aproveita o caminho pra revisar F1+F2 vocab.
    # Situações reais: um p?ssaro, uma fiore, parar pra beber ?gua.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Vocês passaram pelo portão e o campo se abriu. Antonio "
                    "apontou '?rboles', 'pietre', 'el río'. O campo é diferente "
                    "do borgo — mais silêncio, mais espaço, o cheiro de terra.\n\n"
                    "Enquanto caminham, Antonio continua te testando. 'O campo "
                    "também ensina. Você olha, eu pergunto.'"
                ),
                "now": "Revisão das palavras de F1 e F2 — cada uma num contexto de campo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio para, pega uma pedra lisa do chão e te joga. Você pega no ar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Come stai hoy?Con il campo y el sol?",
                    "translation": "Como você est? hoje?Com o campo e o sol?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O ar est? limpo, o campo aberto, você comeu o pão de Giulia antes de sair. Antonio quer saber como você est?:",
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
                    "translation": "Ei — e de manhã, quando você chega num lugar novo e vê alguém?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um trabalhador do campo passa com uma enxada. É cedo ainda. Você cumprimenta:",
                    "options": [
                        {"id": "a", "text": "Buongiorno!"},
                        {"id": "b", "text": "Buonanotte!"},
                        {"id": "c", "text": "Ciao noche!"},
                        {"id": "d", "text": "Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Buongiorno. O trabalhador levantou dois dedos — reconheceu.",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio aponta pra uma fiore vermelha no borde do caminho. 'Fiore silvestre — fiore do campo.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um menino do borgo passa corrindo e para quando vê a fiore — 'La fiore, qué bonita!' O que ele viu?",
                    "options": [
                        {"id": "a", "text": "Fiore"},
                        {"id": "b", "text": "Pietra"},
                        {"id": "c", "text": "Árbol"},
                        {"id": "d", "text": "Río"},
                    ],
                    "correct": "a",
                    "word_id": "it_fiore", "target": "fiore", "native": "fiore",
                    "npc_reaction": "Fiore silvestre. Essa é do campo — não cresce na piazza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "El straniero — así te llaman. Pero te acuerdas qué significa?",
                    "translation": "O straniero — assim te chamam. Mas você lembra o que significa?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra você: 'Quelli del borgo ti chiamano straniero perche...'",
                    "options": [
                        {"id": "a", "text": "Você veio de fora — não é do borgo"},
                        {"id": "b", "text": "Você não tem nome"},
                        {"id": "c", "text": "Você trabalha no campo"},
                        {"id": "d", "text": "Você é muito jovem"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "Eso. Straniero = de fora. Mas o borgo j? t? acostumando contigo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E io, che cosa sono?Recuerdas la palabra?",
                    "translation": "E eu — o que sou?Você lembra a palavra?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio arranca um pedaço de erva do chão, cheira. Trabalha com a terra toda a vida. Ele é:",
                    "options": [
                        {"id": "a", "text": "Contadino"},
                        {"id": "b", "text": "Straniero"},
                        {"id": "c", "text": "Doctor"},
                        {"id": "d", "text": "Maestro"},
                    ],
                    "correct": "a",
                    "word_id": "it_contadino", "target": "contadino", "native": "camponês",
                    "npc_reaction": "Contadino. E orgulhoso disso.",
                },
                {
                    "kind": "narrative",
                    "text": "As ?rvores estão mais perto. Um som novo — ?gua corrindo, fresco, abaixo do ruído do vento.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você ouviu o som, ficou com a boca seca de querer beber. Antonio olhou pra você. Você fala:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Estoy male"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. El río t? ali. J? estamos chegando.",
                },
            ],
        },
    },

    # ── Seção 3: Gram?tica Narrativa ───────────────────────────────────────────
    # Chegaram ao río. Antonio ensina "c'e" + lugar:
    # "C'e ?rboles. C'e pietre. C'e acqua en el río."
    # Também: "non c'e" — "non c'e pane aquí".
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Vocês chegaram ao río. Água fria, pedras brancas no fundo, "
                    "sombra das ?rvores. Antonio jogou o saco no chão e sentou "
                    "numa pedra grande.\n\n"
                    "'Olha o que tem aqui. Aprenda a dizer.'"
                ),
                "now": "Antonio ensina 'c'e' — a forma de dizer que algo existe num lugar.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio aponta em volta — ?rvores, pedras, o río, o céu. Faz um gesto amplo com o braço.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "'C'e' — questo si usa quando qualcosa e qui. 'C'e ?rboles.'",
                    "translation": "'C'e' — isso você usa quando algo est? aqui. 'H? ?rvores.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "C'e ?rboles",
                    "meaning": "H? ?rvores / Tem ?rvores",
                    "note": "c'e = h? / tem | serve pra qualquer coisa: c'e acqua, c'e pane, c'e pietre",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y si algo no est? — 'non c'e'. Simple. 'Non c'e pane aquí en il campo.'",
                    "translation": "E se algo não est? — 'não tem'. Simples. 'Não tem pão aqui no campo.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Non c'e pane",
                    "meaning": "Não tem pão / Não h? pão",
                    "note": "non c'e = não tem | o oposto de c'e",
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
                    "example": "C'e pietre en el río. / Non c'e pane aquí.",
                    "translation": "Tem pedras no rio. / Não tem pão aqui.",
                    "note": "C'e = existe. Non c'e = não existe. Um padrão, infinitas coisas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pro río com pedras brancas no fundo. Como você descreve?",
                    "options": [
                        {"id": "a", "text": "C'e pietre en el río"},
                        {"id": "b", "text": "Non c'e pietre"},
                        {"id": "c", "text": "C'e pane en el río"},
                        {"id": "d", "text": "Ho pietre"},
                    ],
                    "correct": "a",
                    "word_id": "it_pietra", "target": "pietra", "native": "pedra",
                    "npc_reaction": "C'e pietre. Exato. O río fala por si mesmo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você olha pra volta — só campo, ?rvores e rio. Não h? nenhuma padaria. Antonio: 'C'e pane aquí?'",
                    "options": [
                        {"id": "a", "text": "Non c'e pane"},
                        {"id": "b", "text": "C'e pane"},
                        {"id": "c", "text": "Ho pane"},
                        {"id": "d", "text": "C'e acqua"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Non c'e pane. Non c'e Giulia tampoco. Só campo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Pero — c'e acqua?",
                    "translation": "Mas — tem ?gua?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O río est? na sua frente, corrindo sobre pedras brancas. Antonio espera:",
                    "options": [
                        {"id": "a", "text": "Sí, c'e acqua"},
                        {"id": "b", "text": "Non c'e acqua"},
                        {"id": "c", "text": "Ho acqua"},
                        {"id": "d", "text": "C'e pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "?gua",
                    "npc_reaction": "Sí, c'e acqua. Mucha acqua. Beba.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra cima, pras copas das ?rvores. 'Y aquí — c'e ?rboles?'",
                    "options": [
                        {"id": "a", "text": "Sí, c'e ?rboles"},
                        {"id": "b", "text": "Non c'e ?rboles"},
                        {"id": "c", "text": "C'e pietre"},
                        {"id": "d", "text": "C'e pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "?rbol", "native": "?rvore",
                    "npc_reaction": "C'e ?rboles. E eles ficam aqui h? cem anos — antes do borgo.",
                },
                {
                    "kind": "narrative",
                    "text": "Ao longe, um som de machado batendo em madeira. Ritmado, constante. Antonio levanta a cabeça.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ese es el viejo Pietro. El leñador. Viene aquí hace treinta años.",
                    "translation": "Esse é o velho Pietro. O lenhador. Vem aqui h? trinta anos.",
                },
            ],
        },
    },

    # ── Seção 4: Pr?tica Aplicada ─────────────────────────────────────────────
    # Encontro com El Viejo Leñador (Pietro). Pratica c'e/non c'e em situações
    # reais do campo enquanto o lenhador se aproxima. NPC presente em cada exercício.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Antonio te ensinou 'c'e' e 'non c'e'. Árboles, pietre, "
                    "acqua — tudo que est? ao redor pode ser descrito assim.\n\n"
                    "O som do machado ficou mais próximo. O velho Pietro est? "
                    "vindo pela margem do río."
                ),
                "now": "Pr?tica r?pida antes do encontro com o leñador.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Antes de ele chegar — vamos praticar r?pido. Olha ao redor e responde.",
                    "translation": "Antes dele chegar — vamos praticar r?pido. Olha ao redor e responde.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pro outro lado do río — só pedras, grama, sem ?rvores. 'C'e ?rboles all??'",
                    "options": [
                        {"id": "a", "text": "No, non c'e ?rboles"},
                        {"id": "b", "text": "Sí, c'e ?rboles"},
                        {"id": "c", "text": "C'e pane all?"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "?rbol", "native": "?rvore",
                    "npc_reaction": "Non c'e ?rboles all?. Corrito.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio abre o saco — tem um pedaço de pão seco l? dentro. 'C'e pane?'",
                    "options": [
                        {"id": "a", "text": "Sí, c'e pane"},
                        {"id": "b", "text": "Non c'e pane"},
                        {"id": "c", "text": "C'e acqua"},
                        {"id": "d", "text": "Non c'e acqua"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pão",
                    "npc_reaction": "C'e pane. Seco, mas c'e.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você est? com fome depois de caminhar bastante. Como você fala pro Antonio?",
                    "options": [
                        {"id": "a", "text": "Ho fame"},
                        {"id": "b", "text": "Ho sete"},
                        {"id": "c", "text": "Estoy bene"},
                        {"id": "d", "text": "Non c'e pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_hambre", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Hambre. Pega o pão do saco — h? um l?.",
                },
                {
                    "kind": "narrative",
                    "text": "Pietro chega pela margem do río. Alto, pele curtida, machado no ombro. Olhos pequenos que enxergam longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Pietro — buongiorno. Vine a mostrar el río al straniero.",
                    "translation": "Pietro — bom dia. Vim mostrar o río pro straniero.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Pietro para na frente de vocês, olha pra você, depois pro río. Antonio disse 'buongiorno' — é de manhã. Qual hora do dia é essa?",
                    "options": [
                        {"id": "a", "text": "De manhã — hora do buongiorno"},
                        {"id": "b", "text": "De tarde — hora do buonasera"},
                        {"id": "c", "text": "De noite — hora do buonanotte"},
                        {"id": "d", "text": "Meio-dia — sem saudação específica"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Buongiorno. O sol ainda est? subindo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "...",
                    "translation": "(O velho não responde imediatamente. Te olha.)",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Pietro te examina por tempo demais. Os olhos vão do rosto "
                        "pra mão, de volta pro rosto. Antonio ri nervoso."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Pietro finalmente fala — em italiano lento, sem tirar os olhos de você: 'Come ti chiami?' Como você responde?",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "C'e ?rboles"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Pietro ouviu, assentiu devagar. Não disse nada mais por um longo segundo.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ───────────────────────────────────────────────────────
    # Pietro faz algo estranho. Ele pega uma pedra lisa do río, examina, e a
    # entrega ao protagonista dizendo algo que não faz sentido.
    # A narrativa aqui é densa — menos exercícios, mais beats. O vocab é usado
    # dentro da conversa.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio", "Pietro el Leñador"],
                "story": (
                    "Pietro te olhou por tempo demais antes de perguntar seu nome. "
                    "Quando você respondeu, ele ficou quieto uns instantes. Antonio "
                    "ficou desconfort?vel — você percebeu.\n\n"
                    "Pietro ainda est? parado na margem do río, machado no ombro, "
                    "te observando."
                ),
                "now": "Pietro vai fazer algo que ninguém esperava.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Pietro abaixa o machado devagar. Entra no río com as botas — a ?gua na canela — e pega uma pedra do fundo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Esta pietra del río. Tómalea.",
                    "translation": "Essa pedra do rio. Pega.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você pegou a pedra. Lisa, pesada, fria. Branca com uma veia cinza no meio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "El río la hizo así. Años y años de acqua.",
                    "translation": "O río fez ela assim. Anos e anos de ?gua.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro disse 'Esta pietra del río'. Que objeto ele te entregou?",
                    "options": [
                        {"id": "a", "text": "Pietra"},
                        {"id": "b", "text": "Fiore"},
                        {"id": "c", "text": "Pane"},
                        {"id": "d", "text": "Acqua"},
                    ],
                    "correct": "a",
                    "word_id": "it_pietra", "target": "pietra", "native": "pedra",
                    "npc_reaction": "Pietra. Do río. Guarda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Straniero, hai qualcosa. Negli occhi. Come quelli che ascoltano la terra.",
                    "translation": "Forasteiro — você tem algo. Nos olhos. Como os que escutam a terra.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você não entendeu completamente. Mas 'tienes algo' ficou claro o suficiente — ele estava dizendo que você tem algo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Pietro — che dici?",
                    "translation": "Pietro — o que você est? dizendo?",
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
                    "text": "Pietro pegou o machado e foi embora pela margem. Não olhou pra tr?s.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio ficou quieto olhando Pietro ir embora. Depois te olhou. 'Stai bene?' — como você est??",
                    "options": [
                        {"id": "a", "text": "Bene... ma raro"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Non c'e acqua"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bene. Pietro é assim — fala coisas, vai embora. Não se preocupa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você est? segurando a pedra do río. Antonio aponta pra ela: 'Qué tienes ahí?' Você olha e responde:",
                    "options": [
                        {"id": "a", "text": "Una pietra del río"},
                        {"id": "b", "text": "Una fiore dil campo"},
                        {"id": "c", "text": "Pane de Giulia"},
                        {"id": "d", "text": "Acqua del río"},
                    ],
                    "correct": "a",
                    "word_id": "it_pietra", "target": "pietra", "native": "pedra",
                    "npc_reaction": "Pietra del río. Guarda. Pietro não d? coisas pra qualquer um.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio joga o saco nas costas. O sol j? est? mais alto — "
                        "hora de voltar. Você pôs a pedra no bolso. Ela estava fria "
                        "ainda. Você se perguntou o que Pietro quis dizer."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obst?culo ────────────────────────────────────────────────────
    # Voltando ao borgo pelo campo. Antonio vai na frente, você fica pra tr?s
    # cansado. Dois trabalhadores do campo te abordam — curiosos com o straniero.
    # Você tem que usar tudo que aprendeu pra se apresentar e explicar o que h?
    # no campo. Seção gated — errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Pietro foi embora. Vocês comeram o pão seco do saco de Nico "
                    "à beira do río. Depois Antonio se levantou. 'Vamos voltando.'\n\n"
                    "O caminho de volta é longo e o sol esquentou. Antonio caminhou "
                    "mais r?pido — conversando com ele mesmo, em italiano, sobre as "
                    "plantas do campo. Você ficou pra tr?s."
                ),
                "now": "Você est? sozinho no caminho. Dois trabalhadores do campo se aproximam.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌾 Caminho de terra. Antonio é um ponto distante l? na frente. Dois homens com enxadas param na sua frente — curiosos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 1",
                    "line": "Ciao! Eres el straniero nuevo?",
                    "translation": "Ol?! Você é o straniero novo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 1",
                    "question": "O homem perguntou 'Ciao!' e quer saber quem você é. O que você responde primeiro?",
                    "options": [
                        {"id": "a", "text": "Ciao! Si, sono lo straniero"},
                        {"id": "b", "text": "Non c'e pane"},
                        {"id": "c", "text": "Ho sete"},
                        {"id": "d", "text": "Buonanotte"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "O homem ri. 'Sabíamos que ia aparecer um straniero. Nico falou.' ",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 2",
                    "line": "Y come ti chiami?",
                    "translation": "E como você se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 2",
                    "question": "O segundo homem quer saber seu nome. Você responde:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "C'e ?rboles"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "'Ah! Piacere.' Os dois inclinam a cabeça.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 1",
                    "line": "Y por ac? — c'e algo especial?Viste el río?",
                    "translation": "E por aqui — tem algo especial?Você viu o río?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 1",
                    "question": "Você acabou de passar o dia no río. Você viu muita coisa. O que h? por l??",
                    "options": [
                        {"id": "a", "text": "C'e ?rboles, pietre y acqua"},
                        {"id": "b", "text": "Non c'e nada"},
                        {"id": "c", "text": "C'e pane y locanda"},
                        {"id": "d", "text": "Non c'e ?rboles"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "?rbol", "native": "?rvore",
                    "npc_reaction": "Os dois assentem. 'Siempre c'e ?rboles y pietre en el río. Claro.'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Trabajador 2",
                    "line": "Come stai, straniero?El sol est? fuerte hoy.",
                    "translation": "Como você est?, straniero?O sol est? forte hoje.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Trabajador 2",
                    "question": "Você caminhou bastante, bebeu do río, ainda tem a pedra no bolso. Como você est??",
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
                    "text": "Os dois levantam as enxadas e seguem caminho. Antonio j? parou pra te esperar l? na frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Straniero! Qué pasó?Stai bene?",
                    "translation": "Forasteiro! O que aconteceu?Est? bem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio voltou pra te esperar, preocupado. Mas você se virou bem. Como você responde?",
                    "options": [
                        {"id": "a", "text": "Sí — me presenté solo"},
                        {"id": "b", "text": "Male — ho paura"},
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
                        "Vocês voltaram ao borgo com o sol se pondo. Você com a "
                        "pedra do río no bolso — fria ainda, lisa, pesada.\n\n"
                        "Você se perguntou o que Pietro quis dizer com 'tienes algo "
                        "en los ojos'. E o que eram 'los que escuchan la tierra'."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
