"""
Seed das 6 seÃ§Ãµes da Fase 4 Espanhol A1 â€” "El Mercado".

Dia de mercado no pueblo. Don Miguel leva o protagonista para a plaza central
onde os comerciantes montam as bancas. Barulho, cor, gente. O protagonista
comeÃ§a a chamar atenÃ§Ã£o â€” Carmen faz um aviso a Miguel.

Novos vocab (3): naranja Â· uno/dos/tres Â· mucho / poco
RevisÃ£o F1â€“F3: hola, buenos dÃ­as, gracias, de nada, bien/mal, me llamo,
               forastero, hay/no hay, pan, agua, Ã¡rbol, piedra, rÃ­o
NPC principal:   Don Miguel (fio condutor)
NPC cameo:       El Mercader (vendedor de frutas) Â· SeÃ±ora Carmen (aviso)
Itens:           naranja_del_mercado (word_id: es_naranja)
Arco emocional:  anÃ´nimo â†’ percebido; tensÃ£o comeÃ§a a surgir
TransiÃ§Ã£o:       voltam da plaza; Miguel mais quieto que o normal.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f4_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Dia de mercado. Barulho, cores, cheiro de fruta. Don Miguel apresenta o
    # mercado. Vocab novo aparece sem traduÃ§Ã£o â€” imersÃ£o. ExercÃ­cios: reconhecimento.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸ§º Plaza central do pueblo. ManhÃ£ de mercado â€” bancas de "
                        "madeira com frutas e legumes, tecidos coloridos pendurados, "
                        "crianÃ§as correndo entre as pernas dos adultos. O barulho Ã© o "
                        "dobro do normal."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¡Bienvenido al mercado, forastero! Una vez a la semana, toda la plaza se llena.",
                },
                {
                    "kind": "player",
                    "text": "VocÃª ficou parado na entrada olhando. Nunca tinha visto tanta coisa num sÃ³ lugar.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Mira â€” naranjas. Frutas del campo. Â¿CuÃ¡nto, seÃ±or?",
                },
                {
                    "kind": "scene",
                    "text": "ðŸŠ Um mercador de meia-idade com avental de couro aponta trÃªs laranjas brilhantes numa banca.",
                },
                {
                    "kind": "npc",
                    "npc": "El Mercader",
                    "line": "Tres naranjas â€” dos monedas. Â¿Quieres?",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¿CuÃ¡nto? Â¿Dos monedas? Eso es mucho para tres naranjas.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc",
                    "npc": "El Mercader",
                    "line": "Â¡No, no! Es poco. Las naranjas son grandes.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o entendeu os nÃºmeros nem o preÃ§o. Mas 'mucho' e 'poco' â€” muito e pouco â€” ficaram claros pelo tom.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Bien â€” tres naranjas. Toma, forastero.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel te entregou uma fruta laranja e brilhante que o mercader estava vendendo. Como ela se chama?",
                    "options": [
                        {"id": "a", "text": "Naranja"},
                        {"id": "b", "text": "Manzana"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "Piedra"},
                    ],
                    "correct": "a",
                    "word_id": "es_naranja", "target": "naranja", "native": "laranja",
                    "npc_reaction": "Naranja. Dulce. Boa aqui no calor.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse que o preÃ§o era 'mucho' para trÃªs laranjas. O que significa 'mucho'?",
                    "options": [
                        {"id": "a", "text": "Muito"},
                        {"id": "b", "text": "Pouco"},
                        {"id": "c", "text": "Nada"},
                        {"id": "d", "text": "Bom"},
                    ],
                    "correct": "a",
                    "word_id": "es_mucho", "target": "mucho", "native": "muito",
                    "npc_reaction": "Mucho = muito. Sempre que achar o preÃ§o alto â€” mucho.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercader rebateu que o preÃ§o era 'poco' â€” que as laranjas eram grandes. O que significa 'poco'?",
                    "options": [
                        {"id": "a", "text": "Pouco"},
                        {"id": "b", "text": "Muito"},
                        {"id": "c", "text": "Caro"},
                        {"id": "d", "text": "Barato"},
                    ],
                    "correct": "a",
                    "word_id": "es_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco = pouco. No mercado Ã© sempre assim: mucho ou poco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercader disse 'tres naranjas'. VocÃª olhou â€” tinha exatamente trÃªs frutas na banca. 'Tres' significa:",
                    "options": [
                        {"id": "a", "text": "TrÃªs"},
                        {"id": "b", "text": "Um"},
                        {"id": "c", "text": "Dois"},
                        {"id": "d", "text": "Cinco"},
                    ],
                    "correct": "a",
                    "word_id": "es_tres", "target": "tres", "native": "trÃªs",
                    "npc_reaction": "Tres. Uno, dos, tres â€” conta com os dedos primeiro.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel passeia pelo mercado com o protagonista. RevisÃ£o de F1+F2+F3
    # vocab em contexto de mercado. Cada exercÃ­cio Ã© uma situaÃ§Ã£o real.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "O mercado estÃ¡ barulhento e cheio. Don Miguel te deu uma naranja "
                    "e comeÃ§ou a andar pelo corredor de bancas. VocÃª seguiu carregando "
                    "a fruta na mÃ£o, observando tudo.\n\n"
                    "Ontem vocÃªs foram ao rÃ­o e vocÃª conheceu o velho Ernesto. Antes "
                    "disso, vocÃª aprendeu 'hay', 'Ã¡rbol', 'piedra', 'rÃ­o'. E desde o "
                    "comeÃ§o: 'hola', 'gracias', 'bien', 'tengo hambre', 'pan', 'agua'."
                ),
                "now": "Don Miguel quer saber se tudo que vocÃª aprendeu ainda estÃ¡ na cabeÃ§a.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel para na frente de uma banca com frutas e legumes. Aponta pro ambiente ao redor.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿QuÃ© hay en el mercado? Mira alrededor y dime.",
                    "translation": "O que tem no mercado? Olha ao redor e me fala.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Bancas cheias, gente, frutas, tecidos. Don Miguel quer saber se vocÃª sabe usar 'hay'. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Hay naranjas y mucha gente"},
                        {"id": "b", "text": "No hay nada"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Hay Ã¡rboles"},
                    ],
                    "correct": "a",
                    "word_id": "es_naranja", "target": "naranja", "native": "laranja",
                    "npc_reaction": "Hay naranjas. E muita gente. Correto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Una seÃ±ora pasa con una cesta de pan. TÃº la ves y...",
                    "translation": "Uma senhora passa com uma cesta de pÃ£o. VocÃª a vÃª e...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "A senhora olha pra vocÃª ao passar. Como vocÃª cumprimenta â€” Ã© de manhÃ£:",
                    "options": [
                        {"id": "a", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "b", "text": "Â¡Buenas noches!"},
                        {"id": "c", "text": "Â¡AdiÃ³s!"},
                        {"id": "d", "text": "Â¡Mal!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. Ela acenou de volta. JÃ¡ nÃ£o Ã©s mais um estranho.",
                },
                {
                    "kind": "narrative",
                    "text": "Na cesta da senhora: pÃ£o escuro, cheiroso. Seu estÃ´mago roncou.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O pÃ£o na cesta da senhora cheirava bem. Seu estÃ´mago avisou antes de vocÃª. Como vocÃª fala pra Don Miguel?",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Hay pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. VocÃª comeu a naranja, nÃ£o? â€” 'SÃ­, Don Miguel, pero...'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Rosa tiene pan. DespuÃ©s compramos. Primero hay que caminar mÃ¡s.",
                    "translation": "Rosa tem pÃ£o. Depois compramos. Primeiro tem que caminhar mais.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel mencionou que Rosa tem pÃ£o. VocÃª foi na casa dela pela manhÃ£. Ela tem mesmo â€” como vocÃª confirma?",
                    "options": [
                        {"id": "a", "text": "SÃ­, hay pan en la casa de Rosa"},
                        {"id": "b", "text": "No hay pan"},
                        {"id": "c", "text": "Hay Ã¡rboles en la casa"},
                        {"id": "d", "text": "No hay agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pÃ£o",
                    "npc_reaction": "Hay pan. Sempre hay pan na casa dela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿Y ayer en el campo â€” quÃ© habÃ­a cerca del rÃ­o?",
                    "translation": "E ontem no campo â€” o que havia perto do rÃ­o?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Ontem no rÃ­o â€” vocÃª viu Ã¡rboles, piedras, e Ã¡gua correndo. Don Miguel pergunta o que havia:",
                    "options": [
                        {"id": "a", "text": "HabÃ­a Ã¡rboles y piedras"},
                        {"id": "b", "text": "HabÃ­a naranjas"},
                        {"id": "c", "text": "No habÃ­a nada"},
                        {"id": "d", "text": "HabÃ­a pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "Ã¡rbol", "native": "Ã¡rvore",
                    "npc_reaction": "Ãrboles y piedras. E o leÃ±ador tambÃ©m estava.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'Â¿Eres el forastero de San CristÃ³bal ahora â€” o todavÃ­a eres un extraÃ±o?'",
                    "options": [
                        {"id": "a", "text": "Sigo siendo forastero â€” pero menos"},
                        {"id": "b", "text": "Soy campesino"},
                        {"id": "c", "text": "No hay forastero"},
                        {"id": "d", "text": "Tengo sed"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero â€” pero menos. Isso Ã© crescimento.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel para numa banca e ensina os nÃºmeros 1â€“5 em contexto de mercado.
    # Depois ensina mucho/poco com objetos concretos da banca.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "VocÃªs caminharam pelo mercado. Don Miguel foi apresentando tudo "
                    "o que via â€” frutas, panos, ferramentas. VocÃª foi absorvendo.\n\n"
                    "Numa certa banca, ele parou e te chamou. 'Aqui vocÃª precisa "
                    "saber contar. SenÃ£o, te enganam.'"
                ),
                "now": "Don Miguel vai ensinar os nÃºmeros 1â€“5 e mucho/poco.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel ergue um dedo. 'Uno.' Dois dedos. 'Dos.' TrÃªs. 'Tres.' Quatro. 'Cuatro.' Cinco. 'Cinco.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Uno Â· dos Â· tres Â· cuatro Â· cinco",
                    "meaning": "Um Â· dois Â· trÃªs Â· quatro Â· cinco",
                    "note": "Conta com os dedos. O mercado exige isso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ahora â€” cuÃ¡ntas naranjas hay aquÃ­?",
                    "translation": "Agora â€” quantas laranjas tem aqui?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra banca. VocÃª conta â€” uma, duas, trÃªs laranjas. Como vocÃª diz?",
                    "options": [
                        {"id": "a", "text": "Tres naranjas"},
                        {"id": "b", "text": "Dos naranjas"},
                        {"id": "c", "text": "Cinco naranjas"},
                        {"id": "d", "text": "Una naranja"},
                    ],
                    "correct": "a",
                    "word_id": "es_tres", "target": "tres", "native": "trÃªs",
                    "npc_reaction": "Tres. Correto. O mercador nÃ£o vai te enganar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y si hay solo una â€” 'Â¿hay una naranja?' â€” quÃ© dices?",
                    "translation": "E se hÃ¡ sÃ³ uma â€” 'hay una naranja?' â€” o que vocÃª fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Sobrou sÃ³ uma laranja na banca â€” o mercador vendeu todas as outras. Don Miguel: 'Â¿CuÃ¡ntas hay?'",
                    "options": [
                        {"id": "a", "text": "Una naranja"},
                        {"id": "b", "text": "Dos naranjas"},
                        {"id": "c", "text": "Tres naranjas"},
                        {"id": "d", "text": "Cinco naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_uno", "target": "uno", "native": "um",
                    "npc_reaction": "Una. Una naranja. Conta certo e o mercador respeita.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y 'mucho' â€” eso es cuando hay demasiado. 'Poco' â€” cuando casi no hay.",
                    "translation": "E 'mucho' â€” Ã© quando tem demais. 'Poco' â€” quando quase nÃ£o tem.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Mucho",   "isKey": True},
                        {"text": " â†” ",     "isKey": False},
                        {"text": "Poco",    "isKey": True},
                    ],
                    "example": "Hay mucho pan hoy. / Hay poco pan â€” solo uno.",
                    "translation": "Tem muito pÃ£o hoje. / Tem pouco pÃ£o â€” sÃ³ um.",
                    "note": "No mercado: mucho = exagero no preÃ§o | poco = quase nada",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercador pede cinco moedas por uma laranja. Don Miguel franzia a testa. O preÃ§o estava:",
                    "options": [
                        {"id": "a", "text": "Mucho â€” muy caro"},
                        {"id": "b", "text": "Poco â€” muy barato"},
                        {"id": "c", "text": "Bien â€” justo"},
                        {"id": "d", "text": "Dos â€” normal"},
                    ],
                    "correct": "a",
                    "word_id": "es_mucho", "target": "mucho", "native": "muito",
                    "npc_reaction": "Mucho. Cinco moedas por uma naranja Ã© demais.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercador tem quase nada na banca â€” sÃ³ meia dÃºzia de frutas murchas. Don Miguel: 'Â¿Hay mucho aquÃ­?'",
                    "options": [
                        {"id": "a", "text": "No â€” hay poco"},
                        {"id": "b", "text": "SÃ­ â€” hay mucho"},
                        {"id": "c", "text": "Hay tres Ã¡rboles"},
                        {"id": "d", "text": "No hay naranja"},
                    ],
                    "correct": "a",
                    "word_id": "es_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Quase nada. Esse mercador nÃ£o preparou bem o estoque.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra banca mais cheia do mercado â€” frutas empilhadas atÃ© cair. 'Â¿Mucho o poco?'",
                    "options": [
                        {"id": "a", "text": "Mucho"},
                        {"id": "b", "text": "Poco"},
                        {"id": "c", "text": "Tres"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_mucho", "target": "mucho", "native": "muito",
                    "npc_reaction": "Mucho. Esse aqui preparou bem.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # PrÃ¡tica intensa de nÃºmeros + mucho/poco em contexto de compra no mercado.
    # Don Miguel presente em cada exercÃ­cio, simulando situaÃ§Ãµes reais de barganha.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel te ensinou uno, dos, tres, cuatro, cinco â€” e mucho/poco. "
                    "'No mercado vocÃª precisa dos dois. Contar e avaliar preÃ§o.' Agora "
                    "ele vai te por Ã  prova com situaÃ§Ãµes reais."
                ),
                "now": "PrÃ¡tica rÃ¡pida â€” Don Miguel manda situaÃ§Ã£o, vocÃª responde.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "RÃ¡pido â€” el mercador te muestra dos naranjas. Â¿CuÃ¡ntas hay?",
                    "translation": "RÃ¡pido â€” o mercador te mostra duas laranjas. Quantas tem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercador levantou duas laranjas, uma em cada mÃ£o. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Dos naranjas"},
                        {"id": "b", "text": "Tres naranjas"},
                        {"id": "c", "text": "Una naranja"},
                        {"id": "d", "text": "Cinco naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_dos", "target": "dos", "native": "dois",
                    "npc_reaction": "Dos. Certo. Contar Ã© sobrevivÃªncia no mercado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª quer comprar cinco naranjas. Como vocÃª pede?",
                    "options": [
                        {"id": "a", "text": "Cinco naranjas, por favor"},
                        {"id": "b", "text": "Mucho naranjas"},
                        {"id": "c", "text": "Tres naranjas"},
                        {"id": "d", "text": "Una naranja"},
                    ],
                    "correct": "a",
                    "word_id": "es_cinco", "target": "cinco", "native": "cinco",
                    "npc_reaction": "Cinco. E 'por favor' â€” sempre bem recebido no mercado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercador pede quatro moedas por uma naranja. Don Miguel franzeu a testa. O preÃ§o Ã©:",
                    "options": [
                        {"id": "a", "text": "Mucho â€” demais"},
                        {"id": "b", "text": "Poco â€” muito barato"},
                        {"id": "c", "text": "Tres â€” normal"},
                        {"id": "d", "text": "Bien â€” justo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mucho", "target": "mucho", "native": "muito",
                    "npc_reaction": "Mucho. Tenta oferecer menos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª oferece uma moeda. O mercador sorriu â€” price muito baixo pra ele. 'Â¿Es poco?'",
                    "options": [
                        {"id": "a", "text": "SÃ­, es poco"},
                        {"id": "b", "text": "No, es mucho"},
                        {"id": "c", "text": "Hay cuatro"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Uma moeda Ã© muito pouco. Precisa oferecer mais.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Dos monedas â€” ese es el precio justo. Â¿Hay dos naranjas o tres?",
                    "translation": "Duas moedas â€” esse Ã© o preÃ§o justo. Tem duas laranjas ou trÃªs?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel apontou â€” vocÃª contou: trÃªs laranjas na banca. 'Â¿Hay dos naranjas?'",
                    "options": [
                        {"id": "a", "text": "No â€” hay tres"},
                        {"id": "b", "text": "SÃ­ â€” hay dos"},
                        {"id": "c", "text": "Hay mucho"},
                        {"id": "d", "text": "No hay naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_tres", "target": "tres", "native": "trÃªs",
                    "npc_reaction": "Tres. Correto. NÃ£o Ã© dois â€” Ã© trÃªs.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª comprou as laranjas. O mercador ficou satisfeito e disse algo. VocÃª entendeu 'Â¿CÃ³mo estÃ¡s?' Como vocÃª responde?",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Hay mucho"},
                        {"id": "d", "text": "Tres naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien, gracias. O mercador sorriu. VocÃª aprendeu o bÃ¡sico.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel acena pro mercador e vocÃªs vÃ£o embora. VocÃª agradece ao se despedir:",
                    "options": [
                        {"id": "a", "text": "Â¡Gracias!"},
                        {"id": "b", "text": "Â¡Mucho!"},
                        {"id": "c", "text": "Â¡Poco!"},
                        {"id": "d", "text": "Â¡Cinco!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Gracias. O mercador: 'De nada â€” vuelve cuando quieras.'",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # SeÃ±ora Carmen aparece no mercado. Ela puxa Don Miguel de lado e faz um
    # aviso em voz baixa. O protagonista nÃ£o ouve tudo, mas vÃª a expressÃ£o de
    # Miguel mudar. Depois Carmen te olha diretamente â€” de um jeito diferente.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Carmen"],
                "story": (
                    "Don Miguel te ensinou a barganhar no mercado. VocÃªs compraram "
                    "naranjas, vocÃª aprendeu os nÃºmeros e mucho/poco. Enquanto "
                    "saÃ­am da banca do mercador, Don Miguel acenou pra alguÃ©m.\n\n"
                    "SeÃ±ora Carmen veio pela sombra das bancas. Ela te reconheceu "
                    "imediatamente â€” estava procurando vocÃªs."
                ),
                "now": "Carmen faz um aviso. O humor do Don Miguel muda.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Don Miguel",
                    "situation": "Saindo do mercado, Don Miguel para. Faz horas que ele nÃ£o come â€” vocÃª ouve o estÃ´mago dele roncar.",
                    "npc_line": "Forastero â€” Â¿tienes algo de comer en la bolsa? Se me hizo tarde el desayuno.",
                    "item_tag": "comida",
                    "on_use": {
                        "narrative": "VocÃª tira algo da mochila e passa pra Don Miguel. Ele parte ao meio sem cerimÃ´nia e devolve a sua metade.",
                        "npc_reaction": "Â¡Eso! Compartir comida â€” asÃ­ se hace amistad en este pueblo. Gracias, forastero.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Aguanto hasta la posada. El campesino aguanta.",
                    },
                },
                {
                    "kind": "narrative",
                    "text": "Carmen chega rÃ¡pido, sem a cesta de costura desta vez. Ela veio sÃ³ falar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Â¡Miguel! Menos mal que te encuentro. Hay algo que tienes que saber.",
                    "translation": "Miguel! Ainda bem que te encontro. Tem algo que vocÃª precisa saber.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿QuÃ© pasa, Carmen?",
                    "translation": "O que acontece, Carmen?",
                },
                {
                    "kind": "narrative",
                    "text": "Carmen inclinou a cabeÃ§a em direÃ§Ã£o a vocÃª â€” um gesto que disse claramente: Ã© sobre ele. Depois puxou Don Miguel pra um pouco mais longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "(em voz baixa) Hay un hombre nuevo en el pueblo. EstÃ¡ haciendo preguntas. Sobre el forastero.",
                    "translation": "(em voz baixa) Tem um homem novo no pueblo. EstÃ¡ fazendo perguntas. Sobre o forasteiro.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o ouviu tudo. Mas 'forastero' ficou claro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'hay un hombre nuevo'. O que isso significa â€” 'hay' + 'un hombre nuevo'?",
                    "options": [
                        {"id": "a", "text": "Tem um homem novo â€” alguÃ©m que nÃ£o estava antes"},
                        {"id": "b", "text": "NÃ£o tem homem"},
                        {"id": "c", "text": "Um homem foi embora"},
                        {"id": "d", "text": "Muitos homens chegaram"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Hay. Tem. Agora tem alguÃ©m novo. E ele estÃ¡ fazendo perguntas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿Sabes quiÃ©n es?",
                    "translation": "VocÃª sabe quem Ã©?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "No. Pero tiene malas preguntas. Â¿Entiendes lo que digo, Miguel?",
                    "translation": "NÃ£o. Mas ele faz perguntas ruins. Entende o que estou dizendo, Miguel?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel acenou com a cabeÃ§a. Carmen te olhou por Ãºltimo â€” direto nos olhos. Um segundo mais que o necessÃ¡rio.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel voltou pra vocÃª. 'Â¿CÃ³mo estÃ¡s?' â€” mas pelo tom, era mais do que cortesia. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Bien... Â¿quÃ© dijo Carmen?"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Hay mucho"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "npc_reaction": "'Nada que te preocupe.' Mas o rosto dele disse outra coisa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Carmen disse que o homem faz 'preguntas' â€” perguntas. Sobre quem ele estÃ¡ perguntando?",
                    "options": [
                        {"id": "a", "text": "Sobre o forastero â€” vocÃª"},
                        {"id": "b", "text": "Sobre Carmen"},
                        {"id": "c", "text": "Sobre Don Miguel"},
                        {"id": "d", "text": "Sobre Rosa"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Sobre vocÃª. Forastero. AlguÃ©m quer saber quem vocÃª Ã©.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel olhou pro mercado ao redor â€” as bancas, os compradores, "
                        "os rostos. VocÃª fez o mesmo. NinguÃ©m Ã³bvio. Mas o feeling de ser "
                        "observado nÃ£o foi embora."
                    ),
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel foi buscar uma coisa em outra banca. O protagonista estÃ¡ sozinho
    # numa banca de frutas. Precisa comprar naranjas sem ajuda.
    # Enquanto faz isso, o Homem Novo passa. Olha. Segue.
    # SeÃ§Ã£o gated â€” errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Depois de falar com Carmen, Don Miguel ficou mais quieto. Ele "
                    "te levou de volta pelo mercado, mas ficou na frente desta vez, "
                    "verificando as bancas com mais atenÃ§Ã£o do que antes.\n\n"
                    "Perto da saÃ­da do mercado, ele parou. 'Espera aqui. Preciso "
                    "buscar uma coisa. Cinco minutos.'"
                ),
                "now": "VocÃª estÃ¡ sozinho na banca de frutas. Precisa comprar sem ajuda.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŠ Banca de frutas. O mercador te olha esperando. Don Miguel sumiu entre as pessoas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Mercader",
                    "line": "Â¡Hola, forastero! Â¿QuÃ© vas a llevar hoy?",
                    "translation": "OlÃ¡, forasteiro! O que vai levar hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Mercader",
                    "question": "O mercador te cumprimentou com 'Â¡Hola!' e quer saber o que vocÃª vai comprar. VocÃª responde primeiro com:",
                    "options": [
                        {"id": "a", "text": "Â¡Hola! Naranjas, por favor"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Hay mucho"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_naranja", "target": "naranja", "native": "laranja",
                    "npc_reaction": "Naranjas. Â¿CuÃ¡ntas?",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Mercader",
                    "line": "Â¿CuÃ¡ntas naranjas â€” una, dos, tres?",
                    "translation": "Quantas laranjas â€” uma, duas, trÃªs?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Mercader",
                    "question": "VocÃª quer trÃªs laranjas pra vocÃª e Don Miguel. Como vocÃª pede?",
                    "options": [
                        {"id": "a", "text": "Tres naranjas"},
                        {"id": "b", "text": "Mucho naranjas"},
                        {"id": "c", "text": "Una naranja"},
                        {"id": "d", "text": "Cinco naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_tres", "target": "tres", "native": "trÃªs",
                    "npc_reaction": "Tres naranjas â€” aquÃ­. Duas moedas.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Mercader",
                    "line": "Dos monedas. Â¿Mucho o poco para ti?",
                    "translation": "Duas moedas. Muito ou pouco pra vocÃª?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Mercader",
                    "question": "Don Miguel te disse que duas moedas por trÃªs laranjas Ã© o preÃ§o justo. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "EstÃ¡ bien â€” dos monedas"},
                        {"id": "b", "text": "Es mucho â€” no quiero"},
                        {"id": "c", "text": "No hay naranjas"},
                        {"id": "d", "text": "Tengo sed"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bien. AquÃ­ tienes las tres. Buen forastero.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸ‘ï¸ Um homem para no corredor entre as bancas. ChapÃ©u baixo. Olha pra vocÃª por tempo demais â€” o mesmo homem da plaza de ontem.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Mercader",
                    "line": "Â¿EstÃ¡s bien, forastero? Te ves raro.",
                    "translation": "VocÃª estÃ¡ bem, forasteiro? VocÃª parece estranho.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Mercader",
                    "question": "O mercador percebeu que vocÃª ficou parado olhando pro corredor. Ele pergunta 'Â¿EstÃ¡s bien?' Como vocÃª responde?",
                    "options": [
                        {"id": "a", "text": "SÃ­, bien. Gracias"},
                        {"id": "b", "text": "Mal â€” tengo miedo"},
                        {"id": "c", "text": "Hay mucho hombre"},
                        {"id": "d", "text": "Tres naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. O mercador aceita a resposta. O homem jÃ¡ foi embora quando vocÃª olhou de volta.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel voltou com um saco pequeno. Olhou as laranjas "
                        "nas suas mÃ£os, depois pra sua expressÃ£o. 'VocÃª comprou "
                        "sozinho.'\n\n"
                        "Era orgulho. Mas por algum motivo, vocÃª nÃ£o conseguia "
                        "parar de pensar no homem do chapÃ©u baixo."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
