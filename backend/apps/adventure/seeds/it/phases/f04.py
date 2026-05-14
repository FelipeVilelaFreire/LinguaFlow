"""
Seed das 6 seÃ§Ãµes da Fase 4 Italiano A1 â€” "Il Mercato".

Dia de mercado no borgo. Antonio leva o protagonista para a piazza central
onde os comerciantes montam as bancas. Barulho, cor, gente. O protagonista
comeÃ§a a chamar atenÃ§Ã£o â€” Bianca faz um aviso a Nico.

Novos vocab (3): mela · uno/due/tre · molto / poco
RevisÃ£o F1â€“F3: ciao, buongiorno, grazie, prego, bene/male, mi chiamo,
               straniero, c'e/non c'e, pane, acqua, Ãrbol, pietra, rÃ­o
NPC principal:   Antonio (fio condutor)
NPC cameo:       Il Mercante (vendedor de frutas) · Bianca (aviso)
Itens:           mela_del_mercado (word_id: it_mela)
Arco emocional:  anÃ´nimo â†’ percebido; tensÃ£o comeÃ§a a surgir
TransiÃ§Ã£o:       voltam da piazza; Nico mais quieto que o normale.

PrÃ©-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Dia de mercado. Barulho, cores, cheiro de fruta. Antonio apresenta o
    # mercado. Vocab novo aparece sem traduÃ§Ã£o â€” imersÃ£o. ExercÃ­cios: reconhecimento.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸ§º Piazza central do borgo. ManhÃ£ de mercado â€” bancas de "
                        "madeira com frutas e legumes, tecidos coloridos pendurados, "
                        "crianÃ§as corrindo entre as pernas dos adultos. O barulho Ã© o "
                        "dobro do normale."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Benevenido al mercado, straniero! Una vez a la semana, toda la piazza se llena.",
                },
                {
                    "kind": "player",
                    "text": "VocÃª ficou parado na entrada olhando. Nunca tinha visto tanta coisa num sÃ³ lugar.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Guarda â€” mele. Frutas dil campo. CuÃnto, signore?",
                },
                {
                    "kind": "scene",
                    "text": "ðŸŠ Um mercador de meia-idade com avental de couro aponta trÃªs laranjas brilhantes numa banca.",
                },
                {
                    "kind": "npc",
                    "npc": "Il Mercante",
                    "line": "Tre mele â€” due monete. Vuoi?",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Quanto? Due monete? E molto per tre mele.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc",
                    "npc": "Il Mercante",
                    "line": "No, no! E poco. Le mele sono grandi.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o entendeu os nÃºmeros nem o preÃ§o. Mas 'molto' e 'poco' â€” muito e pouco â€” ficaram claros pelo tom.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Bene â€” tre mele. Toma, straniero.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio te entregou uma fruta laranja e brilhante que o mercader estava vendendo. Como ela se chama?",
                    "options": [
                        {"id": "a", "text": "Mela"},
                        {"id": "b", "text": "Manzana"},
                        {"id": "c", "text": "Pane"},
                        {"id": "d", "text": "Pietra"},
                    ],
                    "correct": "a",
                    "word_id": "it_mela", "target": "mela", "native": "laranja",
                    "npc_reaction": "Mela. Dulce. Boa aqui no calor.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio disse que o preÃ§o era 'molto' para trÃªs laranjas. O que significa 'molto'?",
                    "options": [
                        {"id": "a", "text": "Muito"},
                        {"id": "b", "text": "Pouco"},
                        {"id": "c", "text": "Nada"},
                        {"id": "d", "text": "Bom"},
                    ],
                    "correct": "a",
                    "word_id": "it_molto", "target": "molto", "native": "muito",
                    "npc_reaction": "Molto = muito. Sempre que achar o preÃ§o alto â€” molto.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercader rebateu que o preÃ§o era 'poco' â€” que as laranjas eram grandes. O que significa 'poco'?",
                    "options": [
                        {"id": "a", "text": "Pouco"},
                        {"id": "b", "text": "Muito"},
                        {"id": "c", "text": "Caro"},
                        {"id": "d", "text": "Barato"},
                    ],
                    "correct": "a",
                    "word_id": "it_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco = pouco. No mercado Ã© sempre assim: molto ou poco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercader disse 'tre mele'. VocÃª olhou â€” tinha exatamente trÃªs frutas na banca. 'Tre' significa:",
                    "options": [
                        {"id": "a", "text": "TrÃªs"},
                        {"id": "b", "text": "Um"},
                        {"id": "c", "text": "Dois"},
                        {"id": "d", "text": "Cinco"},
                    ],
                    "correct": "a",
                    "word_id": "it_tre", "target": "tre", "native": "trÃªs",
                    "npc_reaction": "Tre. Uno, due, tre â€” conta com os dedos primeiro.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Antonio passeia pelo mercado com o protagonista. RevisÃ£o de F1+F2+F3
    # vocab em contexto de mercado. Cada exercÃ­cio Ã© uma situaÃ§Ã£o real.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "O mercado estÃ barulhento e cheio. Antonio te deu uma mela "
                    "e comeÃ§ou a andar pelo corridor de bancas. VocÃª seguiu carregando "
                    "a fruta na mÃ£o, observando tudo.\n\n"
                    "Ontem vocÃªs foram ao rÃ­o e vocÃª conheceu o velho Pietro. Antes "
                    "disso, vocÃª aprendeu 'c'e', 'Ãrbol', 'pietra', 'rÃ­o'. E desde o "
                    "comeÃ§o: 'ciao', 'grazie', 'bene', 'ho fame', 'pane', 'acqua'."
                ),
                "now": "Antonio quer saber se tudo que vocÃª aprendeu ainda estÃ na cabeÃ§a.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio para na frente de uma banca com frutas e legumes. Aponta pro ambenete ao redor.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Che cosa c e nel mercato? Guarda intorno e dimmi.",
                    "translation": "O que tem no mercado? Olha ao redor e me fala.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Bancas cheias, gente, frutas, tecidue. Antonio quer saber se vocÃª sabe usar 'c'e'. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "C'e mele y mucha gente"},
                        {"id": "b", "text": "Non c'e nada"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "C'e Ãrboles"},
                    ],
                    "correct": "a",
                    "word_id": "it_mela", "target": "mela", "native": "laranja",
                    "npc_reaction": "C'e mele. E muita gente. Corrito.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Una signorea pasa con una cesta de pane. TÃº la ves y...",
                    "translation": "Uma senhora passa com uma cesta de pÃ£o. VocÃª a vÃª e...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "A senhora olha pra vocÃª ao passar. Como vocÃª cumprimenta â€” Ã© de manhÃ£:",
                    "options": [
                        {"id": "a", "text": "Buongiorno!"},
                        {"id": "b", "text": "Buonanotte!"},
                        {"id": "c", "text": "AdiÃ³s!"},
                        {"id": "d", "text": "Male!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Buongiorno. Ela acenou de volta. JÃ nÃ£o Ã©s mais um estranho.",
                },
                {
                    "kind": "narrative",
                    "text": "Na cesta da senhora: pÃ£o escuro, cheiroso. Seu estÃ´mago roncou.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O pÃ£o na cesta da senhora cheirava bem. Seu estÃ´mago avisou antes de vocÃª. Como vocÃª fala pra Antonio?",
                    "options": [
                        {"id": "a", "text": "Ho fame"},
                        {"id": "b", "text": "Ho sete"},
                        {"id": "c", "text": "Estoy bene"},
                        {"id": "d", "text": "C'e pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_hambre", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Hambre. VocÃª comeu a mela, nÃ£o? â€” 'SÃ­, Antonio, ma...'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Giulia ha pane. Dopo compriamo. Prima dobbiamo camminare ancora.",
                    "translation": "Giulia tem pÃ£o. Depois compramos. Primeiro tem que caminhar mais.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio mencionou que Giulia tem pÃ£o. VocÃª foi na casa dela pela manhÃ£. Ela tem mesmo â€” como vocÃª confirma?",
                    "options": [
                        {"id": "a", "text": "SÃ­, c'e pane en la casa de Giulia"},
                        {"id": "b", "text": "Non c'e pane"},
                        {"id": "c", "text": "C'e Ãrboles en la casa"},
                        {"id": "d", "text": "Non c'e acqua"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pÃ£o",
                    "npc_reaction": "C'e pane. Sempre c'e pane na casa dela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E ieri nel campo, che cosa c era vicino al fiume?",
                    "translation": "E ontem no campo â€” o que havia perto do rÃ­o?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Ontem no rÃ­o â€” vocÃª viu Ãrboles, pietre, e Ãgua corrindo. Antonio pergunta o que havia:",
                    "options": [
                        {"id": "a", "text": "HabÃ­a Ãrboles y pietre"},
                        {"id": "b", "text": "HabÃ­a mele"},
                        {"id": "c", "text": "No habÃ­a nada"},
                        {"id": "d", "text": "HabÃ­a pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "Ãrbol", "native": "Ãrvore",
                    "npc_reaction": "Ãrboles y pietre. E o leÃ±ador tambÃ©m estava.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio: 'Sei lo straniero di Santa Chiara adesso, o sei ancora un estraneo?'",
                    "options": [
                        {"id": "a", "text": "Sono ancora straniero, ma meno"},
                        {"id": "b", "text": "Soy contadino"},
                        {"id": "c", "text": "Non c'e straniero"},
                        {"id": "d", "text": "Ho sete"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "Straniero â€” ma meno. Isso Ã© crescimento.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: GramÃtica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Antonio para numa banca e ensina os nÃºmeros 1â€“5 em contexto de mercado.
    # Depois ensina molto/poco com objetos concretos da banca.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "VocÃªs caminharam pelo mercado. Antonio foi apresentando tudo "
                    "o que via â€” frutas, paneos, ferramentas. VocÃª foi absorvendo.\n\n"
                    "Numa certa banca, ele parou e te chamou. 'Aqui vocÃª precisa "
                    "saber contar. SenÃ£o, te enganam.'"
                ),
                "now": "Antonio vai ensinar os nÃºmeros 1â€“5 e molto/poco.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio ergue um dedo. 'Uno.' Dois dedos. 'Due.' TrÃªs. 'Tre.' Quatro. 'Cuatro.' Cinco. 'Cinco.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Uno · due · tre · cuatro · cinco",
                    "meaning": "Um · dois · trÃªs · quatro · cinco",
                    "note": "Conta com os dedos. O mercado exige isso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ora â€” cuÃntas mele c'e aquÃ­?",
                    "translation": "Agora â€” quantas laranjas tem aqui?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra banca. VocÃª conta â€” uma, duas, trÃªs laranjas. Como vocÃª diz?",
                    "options": [
                        {"id": "a", "text": "Tre mele"},
                        {"id": "b", "text": "Due mele"},
                        {"id": "c", "text": "Cinco mele"},
                        {"id": "d", "text": "Una mela"},
                    ],
                    "correct": "a",
                    "word_id": "it_tre", "target": "tre", "native": "trÃªs",
                    "npc_reaction": "Tre. Corrito. O mercador nÃ£o vai te enganar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E se c e solo una â€” 'c'e una mela?' â€” che dici?",
                    "translation": "E se hÃ sÃ³ uma â€” 'c'e una mela?' â€” o que vocÃª fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Sobrou sÃ³ uma laranja na banca â€” o mercador vendeu todas as outras. Antonio: 'CuÃntas c'e?'",
                    "options": [
                        {"id": "a", "text": "Una mela"},
                        {"id": "b", "text": "Due mele"},
                        {"id": "c", "text": "Tre mele"},
                        {"id": "d", "text": "Cinco mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_uno", "target": "uno", "native": "um",
                    "npc_reaction": "Una. Una mela. Conta certo e o mercador respeita.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y 'molto' â€” eso es cuando c'e demasiado. 'Poco' â€” cuando casi non c'e.",
                    "translation": "E 'molto' â€” Ã© quando tem demais. 'Poco' â€” quando quase nÃ£o tem.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Molto",   "isKey": True},
                        {"text": " â†” ",     "isKey": False},
                        {"text": "Poco",    "isKey": True},
                    ],
                    "example": "C'e molto pane hoy. / C'e poco pane â€” solo uno.",
                    "translation": "Tem muito pÃ£o hoje. / Tem pouco pÃ£o â€” sÃ³ um.",
                    "note": "No mercado: molto = exagero no preÃ§o | poco = quase nada",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercador pede cinco moedas por uma laranja. Antonio franzia a testa. O preÃ§o estava:",
                    "options": [
                        {"id": "a", "text": "Molto â€” molto caro"},
                        {"id": "b", "text": "Poco â€” molto economico"},
                        {"id": "c", "text": "Bene â€” justo"},
                        {"id": "d", "text": "Due â€” normale"},
                    ],
                    "correct": "a",
                    "word_id": "it_molto", "target": "molto", "native": "muito",
                    "npc_reaction": "Molto. Cinco moedas por uma mela Ã© demais.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercador tem quase nada na banca â€” sÃ³ meia dÃºzia de frutas murchas. Antonio: 'C'e molto aquÃ­?'",
                    "options": [
                        {"id": "a", "text": "No â€” c'e poco"},
                        {"id": "b", "text": "SÃ­ â€” c'e molto"},
                        {"id": "c", "text": "C'e tre Ãrboles"},
                        {"id": "d", "text": "Non c'e mela"},
                    ],
                    "correct": "a",
                    "word_id": "it_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Quase nada. Esse mercador nÃ£o preparou bem o estoque.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra banca mais cheia do mercado â€” frutas empilhadas atÃ© cair. 'Molto o poco?'",
                    "options": [
                        {"id": "a", "text": "Molto"},
                        {"id": "b", "text": "Poco"},
                        {"id": "c", "text": "Tre"},
                        {"id": "d", "text": "Bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_molto", "target": "molto", "native": "muito",
                    "npc_reaction": "Molto. Esse aqui preparou bem.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: PrÃtica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # PrÃtica intensa de nÃºmeros + molto/poco em contexto de compra no mercado.
    # Antonio presente em cada exercÃ­cio, simulando situaÃ§Ãµes reais de barganha.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Antonio te ensinou uno, due, tre, cuatro, cinco â€” e molto/poco. "
                    "'No mercado vocÃª precisa de duas coisas. Contar e avaliar preÃ§o.' Agora "
                    "ele vai te por Ã  prova com situaÃ§Ãµes reais."
                ),
                "now": "PrÃtica rÃpida â€” Antonio manda situaÃ§Ã£o, vocÃª responde.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "RÃpido â€” il mercator te muestra due mele. CuÃntas c'e?",
                    "translation": "RÃpido â€” o mercador te mostra duas laranjas. Quantas tem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercador levantou duas laranjas, uma em cada mÃ£o. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Due mele"},
                        {"id": "b", "text": "Tre mele"},
                        {"id": "c", "text": "Una mela"},
                        {"id": "d", "text": "Cinco mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_due", "target": "due", "native": "dois",
                    "npc_reaction": "Due. Certo. Contar Ã© sobrevivÃªncia no mercado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª quer comprar cinco mele. Como vocÃª pede?",
                    "options": [
                        {"id": "a", "text": "Cinco mele, por favor"},
                        {"id": "b", "text": "Molto mele"},
                        {"id": "c", "text": "Tre mele"},
                        {"id": "d", "text": "Una mela"},
                    ],
                    "correct": "a",
                    "word_id": "it_cinco", "target": "cinco", "native": "cinco",
                    "npc_reaction": "Cinco. E 'por favor' â€” sempre bem recebido no mercado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercador pede quatro moedas por uma mela. Antonio franzeu a testa. O preÃ§o Ã©:",
                    "options": [
                        {"id": "a", "text": "Molto â€” demais"},
                        {"id": "b", "text": "Poco â€” muito barato"},
                        {"id": "c", "text": "Tre â€” normale"},
                        {"id": "d", "text": "Bene â€” justo"},
                    ],
                    "correct": "a",
                    "word_id": "it_molto", "target": "molto", "native": "muito",
                    "npc_reaction": "Molto. Tenta oferecer menos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª oferece uma moeda. O mercador sorriu â€” price muito baixo pra ele. 'Es poco?'",
                    "options": [
                        {"id": "a", "text": "SÃ­, es poco"},
                        {"id": "b", "text": "No, es molto"},
                        {"id": "c", "text": "C'e cuatro"},
                        {"id": "d", "text": "Bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Uma moeda Ã© muito pouco. Precisa oferecer mais.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Due monete â€” quello e il prezzo justo. C'e due mele o tre?",
                    "translation": "Duas moedas â€” esse Ã© o preÃ§o justo. Tem duas laranjas ou trÃªs?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio apontou â€” vocÃª contou: trÃªs laranjas na banca. 'C'e due mele?'",
                    "options": [
                        {"id": "a", "text": "No â€” c'e tre"},
                        {"id": "b", "text": "SÃ­ â€” c'e due"},
                        {"id": "c", "text": "C'e molto"},
                        {"id": "d", "text": "Non c'e mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_tre", "target": "tre", "native": "trÃªs",
                    "npc_reaction": "Tre. Corrito. NÃ£o Ã© dois â€” Ã© trÃªs.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª comprou as laranjas. O mercador ficou satisfeito e disse algo. VocÃª entendeu 'Come stai?' Como vocÃª responde?",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "C'e molto"},
                        {"id": "d", "text": "Tre mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene, grazie. O mercador sorriu. VocÃª aprendeu o bÃsico.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio acena pro mercador e vocÃªs vÃ£o embora. VocÃª agradece ao se despedir:",
                    "options": [
                        {"id": "a", "text": "Grazie!"},
                        {"id": "b", "text": "Molto!"},
                        {"id": "c", "text": "Poco!"},
                        {"id": "d", "text": "Cinco!"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Grazie. O mercador: 'Prego â€” vuelve cuando quieras.'",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Bianca aparece no mercado. Ela puxa Antonio de lado e faz um
    # aviso em voz baixa. O protagonista nÃ£o ouve tudo, mas vÃª a expressÃ£o de
    # Nico mudar. Depois Bianca te olha diretamente â€” de um jeito diferente.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio", "Bianca"],
                "story": (
                    "Antonio te ensinou a barganhar no mercado. VocÃªs compraram "
                    "mele, vocÃª aprendeu os nÃºmeros e molto/poco. Enquanto "
                    "saÃ­am da banca do mercador, Antonio acenou pra alguÃ©m.\n\n"
                    "Bianca veio pela sombra das bancas. Ela te reconheceu "
                    "imediatamente â€” estava procurando vocÃªs."
                ),
                "now": "Bianca faz um aviso. O humor do Antonio muda.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Antonio",
                    "situation": "Saindo do mercado, Antonio para. Faz horas que ele nÃ£o come â€” vocÃª ouve o estÃ´mago dele roncar.",
                    "npc_line": "Straniero â€” hai qualcosa da mangiare nella borsa? Ho fatto tardi per colazione.",
                    "item_tag": "comida",
                    "on_use": {
                        "narrative": "VocÃª tira algo da mochila e passa pra Antonio. Ele parte ao meio sem cerimÃ´nia e devolve a sua metade.",
                        "npc_reaction": "Si! Condividere il cibo: cosi nasce amicizia in questo borgo. Grazie, straniero.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Acquanto hasta la locanda. El contadino acquanta.",
                    },
                },
                {
                    "kind": "narrative",
                    "text": "Bianca chega rÃpido, sem a cesta de costura desta vez. Ela veio sÃ³ falar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Nico! Meno male che ti trovo. C e qualcosa che devi sapere.",
                    "translation": "Nico! Ainda bem que te encontro. Tem algo que vocÃª precisa saber.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Che succede, Bianca?",
                    "translation": "O que acontece, Bianca?",
                },
                {
                    "kind": "narrative",
                    "text": "Bianca inclinou a cabeÃ§a em direÃ§Ã£o a vocÃª â€” um gesto que disse claramente: Ã© sobre ele. Depois puxou Antonio pra um pouco mais longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "(em voz baixa) C e un uomo nuovo nel borgo. Sta facendo domande. Sullo straniero.",
                    "translation": "(em voz baixa) Tem um homem novo no borgo. EstÃ fazendo perguntas. Sobre o straniero.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o ouviu tudo. Mas 'straniero' ficou claro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'c'e un uomo nuovo'. O que isso significa â€” 'c'e' + 'un uomo nuovo'?",
                    "options": [
                        {"id": "a", "text": "Tem um homem novo â€” alguÃ©m que nÃ£o estava antes"},
                        {"id": "b", "text": "NÃ£o tem homem"},
                        {"id": "c", "text": "Um homem foi embora"},
                        {"id": "d", "text": "Muitos homens chegaram"},
                    ],
                    "correct": "a",
                    "npc_reaction": "C'e. Tem. Agora tem alguÃ©m novo. E ele estÃ fazendo perguntas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Sabes quiÃ©n es?",
                    "translation": "VocÃª sabe quem Ã©?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "No. Ma fa domande cattive. Capisci quello che dico, Nico?",
                    "translation": "NÃ£o. Mas ele faz perguntas ruins. Entende o que estou dizendo, Nico?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio acenou com a cabeÃ§a. Bianca te olhou por Ãºltimo â€” direto nos olhos. Um segundo mais que o necessÃrio.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio voltou pra vocÃª. 'Come stai?' â€” mas pelo tom, era mais do que cortesia. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Bene... quÃ© dijo Bianca?"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "C'e molto"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "npc_reaction": "'Nada que te preocupe.' Mas o rosto dele disse outra coisa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Bianca disse que o homem faz 'domande' â€” perguntas. Sobre quem ele estÃ perguntando?",
                    "options": [
                        {"id": "a", "text": "Sobre o straniero â€” vocÃª"},
                        {"id": "b", "text": "Sobre Bianca"},
                        {"id": "c", "text": "Sobre Antonio"},
                        {"id": "d", "text": "Sobre Giulia"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "Sobre vocÃª. Straniero. AlguÃ©m quer saber quem vocÃª Ã©.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio olhou pro mercado ao redor â€” as bancas, os compradores, "
                        "os rostos. VocÃª fez o mesmo. NinguÃ©m Ã³bvio. Mas o feeling de ser "
                        "observado nÃ£o foi embora."
                    ),
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃculo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Antonio foi buscar uma coisa em outra banca. O protagonista estÃ sozinho
    # numa banca de frutas. Precisa comprar mele sem ajuda.
    # Enquanto faz isso, o Homem Novo passa. Olha. Segue.
    # SeÃ§Ã£o gated â€” errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Depois de falar com Bianca, Antonio ficou mais quieto. Ele "
                    "te levou de volta pelo mercado, mas ficou na frente desta vez, "
                    "verificando as bancas com mais atenÃ§Ã£o do que antes.\n\n"
                    "Perto da saÃ­da do mercado, ele parou. 'Espera aqui. Preciso "
                    "buscar uma coisa. Cinco minutos.'"
                ),
                "now": "VocÃª estÃ sozinho na banca de frutas. Precisa comprar sem ajuda.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŠ Banca de frutas. O mercador te olha esperando. Antonio sumiu entre as pessoas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Mercante",
                    "line": "Ciao, straniero! Che cosa prendi oggi?",
                    "translation": "OlÃ, straniero! O que vai levar hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Mercante",
                    "question": "O mercador te cumprimentou com 'Ciao!' e quer saber o que vocÃª vai comprar. VocÃª responde primeiro com:",
                    "options": [
                        {"id": "a", "text": "Ciao! Mele, por favor"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "C'e molto"},
                        {"id": "d", "text": "Buonanotte"},
                    ],
                    "correct": "a",
                    "word_id": "it_mela", "target": "mela", "native": "laranja",
                    "npc_reaction": "Mele. CuÃntas?",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Mercante",
                    "line": "CuÃntas mele â€” una, due, tre?",
                    "translation": "Quantas laranjas â€” uma, duas, trÃªs?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Mercante",
                    "question": "VocÃª quer trÃªs laranjas pra vocÃª e Antonio. Como vocÃª pede?",
                    "options": [
                        {"id": "a", "text": "Tre mele"},
                        {"id": "b", "text": "Molto mele"},
                        {"id": "c", "text": "Una mela"},
                        {"id": "d", "text": "Cinco mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_tre", "target": "tre", "native": "trÃªs",
                    "npc_reaction": "Tre mele â€” aquÃ­. Duas moedas.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Mercante",
                    "line": "Due monete. Molto o poco per te?",
                    "translation": "Duas moedas. Muito ou pouco pra vocÃª?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Mercante",
                    "question": "Antonio te disse que duas moedas por trÃªs laranjas Ã© o preÃ§o justo. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Sta bene â€” due monete"},
                        {"id": "b", "text": "Es molto â€” no voglio"},
                        {"id": "c", "text": "Non c'e mele"},
                        {"id": "d", "text": "Ho sete"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bene. Ecco le tre. Bravo straniero.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸ‘ï¸ Um homem para no corridor entre as bancas. ChapÃ©u baixo. Olha pra vocÃª por tempo demais â€” o mesmo homem da piazza de ontem.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Mercante",
                    "line": "Stai bene, straniero? Te ves raro.",
                    "translation": "VocÃª estÃ bem, straniero? VocÃª parece estranho.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Mercante",
                    "question": "O mercador percebeu que vocÃª ficou parado olhando pro corridor. Ele pergunta 'Stai bene?' Como vocÃª responde?",
                    "options": [
                        {"id": "a", "text": "SÃ­, bene. Grazie"},
                        {"id": "b", "text": "Male â€” ho paura"},
                        {"id": "c", "text": "C'e molto hombre"},
                        {"id": "d", "text": "Tre mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. O mercador aceita a resposta. O homem jÃ foi embora quando vocÃª olhou de volta.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio voltou com um saco pequeno. Olhou as laranjas "
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
