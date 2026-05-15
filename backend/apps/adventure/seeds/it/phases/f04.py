"""
Seed das 6 seções da Fase 4 Italiano A1 — "Il Mercato".

Dia de mercado no borgo. Antonio leva o protagonista para a piazza central
onde os comerciantes montam as bancas. Barulho, cor, gente. O protagonista
começa a chamar atenção — Bianca faz um aviso a Nico.

Novos vocab (3): mela · uno/due/tre · molto / poco
Revisão F1–F3: ciao, buongiorno, grazie, prego, bene/male, mi chiamo,
               straniero, c'e/non c'e, pane, acqua, ?rbol, pietra, río
NPC principal:   Antonio (fio condutor)
NPC cameo:       Il Mercante (vendedor de frutas) · Bianca (aviso)
Itens:           mela_del_mercado (word_id: it_mela)
Arco emocional:  anônimo → percebido; tensão começa a surgir
Transição:       voltam da piazza; Nico mais quieto que o normale.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Dia de mercado. Barulho, cores, cheiro de fruta. Antonio apresenta o
    # mercado. Vocab novo aparece sem tradução — imersão. Exercícios: reconhecimento.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🧺 Piazza central do borgo. Manhã de mercado — bancas de "
                        "madeira com frutas e legumes, tecidos coloridos pendurados, "
                        "crianças corrindo entre as pernas dos adultos. O barulho é o "
                        "dobro do normale."
                    ),
                },
                {
                    "kind": "skill_check",
                    "skill": "persuasao",
                    "min_level": 1,
                    "uses_item_tag": "moneda",
                    "success": "Voce escolhe a palavra e o gesto certos; a resistencia baixa um pouco.",
                    "fallback": "A conversa nao abre de imediato, mas Nico segura o clima e a historia continua.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Benevenido al mercado, straniero! Una vez a la semana, toda la piazza se llena.",
                },
                {
                    "kind": "player",
                    "text": "Você ficou parado na entrada olhando. Nunca tinha visto tanta coisa num só lugar.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Guarda — mele. Frutas dil campo. Cu?nto, signore?",
                },
                {
                    "kind": "scene",
                    "text": "?? Um mercador de meia-idade com avental de couro aponta três laranjas brilhantes numa banca.",
                },
                {
                    "kind": "npc",
                    "npc": "Il Mercante",
                    "line": "Tre mele — due monete. Vuoi?",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Quanto?Due monete?E molto per tre mele.",
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
                    "text": "Você não entendeu os números nem o preço. Mas 'molto' e 'poco' — muito e pouco — ficaram claros pelo tom.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Bene — tre mele. Toma, straniero.",
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
                    "question": "Antonio disse que o preço era 'molto' para três laranjas. O que significa 'molto'?",
                    "options": [
                        {"id": "a", "text": "Muito"},
                        {"id": "b", "text": "Pouco"},
                        {"id": "c", "text": "Nada"},
                        {"id": "d", "text": "Bom"},
                    ],
                    "correct": "a",
                    "word_id": "it_molto", "target": "molto", "native": "muito",
                    "npc_reaction": "Molto = muito. Sempre que achar o preço alto — molto.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercader rebateu que o preço era 'poco' — que as laranjas eram grandes. O que significa 'poco'?",
                    "options": [
                        {"id": "a", "text": "Pouco"},
                        {"id": "b", "text": "Muito"},
                        {"id": "c", "text": "Caro"},
                        {"id": "d", "text": "Barato"},
                    ],
                    "correct": "a",
                    "word_id": "it_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco = pouco. No mercado é sempre assim: molto ou poco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercader disse 'tre mele'. Você olhou — tinha exatamente três frutas na banca. 'Tre' significa:",
                    "options": [
                        {"id": "a", "text": "Três"},
                        {"id": "b", "text": "Um"},
                        {"id": "c", "text": "Dois"},
                        {"id": "d", "text": "Cinco"},
                    ],
                    "correct": "a",
                    "word_id": "it_tre", "target": "tre", "native": "três",
                    "npc_reaction": "Tre. Uno, due, tre — conta com os dedos primeiro.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Antonio passeia pelo mercado com o protagonista. Revisão de F1+F2+F3
    # vocab em contexto de mercado. Cada exercício é uma situação real.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "O mercado est? barulhento e cheio. Antonio te deu uma mela "
                    "e começou a andar pelo corridor de bancas. Você seguiu carregando "
                    "a fruta na mão, observando tudo.\n\n"
                    "Ontem vocês foram ao río e você conheceu o velho Pietro. Antes "
                    "disso, você aprendeu 'c'e', '?rbol', 'pietra', 'río'. E desde o "
                    "começo: 'ciao', 'grazie', 'bene', 'ho fame', 'pane', 'acqua'."
                ),
                "now": "Antonio quer saber se tudo que você aprendeu ainda est? na cabeça.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio para na frente de uma banca com frutas e legumes. Aponta pro ambenete ao redor.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Che cosa c e nel mercato?Guarda intorno e dimmi.",
                    "translation": "O que tem no mercado?Olha ao redor e me fala.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Bancas cheias, gente, frutas, tecidue. Antonio quer saber se você sabe usar 'c'e'. Você diz:",
                    "options": [
                        {"id": "a", "text": "C'e mele y mucha gente"},
                        {"id": "b", "text": "Non c'e nada"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "C'e ?rboles"},
                    ],
                    "correct": "a",
                    "word_id": "it_mela", "target": "mela", "native": "laranja",
                    "npc_reaction": "C'e mele. E muita gente. Corrito.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Una signorea pasa con una cesta de pane. Tú la ves y...",
                    "translation": "Uma senhora passa com uma cesta de pão. Você a vê e...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "A senhora olha pra você ao passar. Como você cumprimenta — é de manhã:",
                    "options": [
                        {"id": "a", "text": "Buongiorno!"},
                        {"id": "b", "text": "Buonanotte!"},
                        {"id": "c", "text": "Adiós!"},
                        {"id": "d", "text": "Male!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Buongiorno. Ela acenou de volta. J? não és mais um estranho.",
                },
                {
                    "kind": "narrative",
                    "text": "Na cesta da senhora: pão escuro, cheiroso. Seu estômago roncou.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O pão na cesta da senhora cheirava bem. Seu estômago avisou antes de você. Como você fala pra Antonio?",
                    "options": [
                        {"id": "a", "text": "Ho fame"},
                        {"id": "b", "text": "Ho sete"},
                        {"id": "c", "text": "Estoy bene"},
                        {"id": "d", "text": "C'e pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_hambre", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Hambre. Você comeu a mela, não?— 'Sí, Antonio, ma...'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Giulia ha pane. Dopo compriamo. Prima dobbiamo camminare ancora.",
                    "translation": "Giulia tem pão. Depois compramos. Primeiro tem que caminhar mais.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio mencionou que Giulia tem pão. Você foi na casa dela pela manhã. Ela tem mesmo — como você confirma?",
                    "options": [
                        {"id": "a", "text": "Sí, c'e pane en la casa de Giulia"},
                        {"id": "b", "text": "Non c'e pane"},
                        {"id": "c", "text": "C'e ?rboles en la casa"},
                        {"id": "d", "text": "Non c'e acqua"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pão",
                    "npc_reaction": "C'e pane. Sempre c'e pane na casa dela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E ieri nel campo, che cosa c era vicino al fiume?",
                    "translation": "E ontem no campo — o que havia perto do río?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Ontem no río — você viu ?rboles, pietre, e ?gua corrindo. Antonio pergunta o que havia:",
                    "options": [
                        {"id": "a", "text": "Había ?rboles y pietre"},
                        {"id": "b", "text": "Había mele"},
                        {"id": "c", "text": "No había nada"},
                        {"id": "d", "text": "Había pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "?rbol", "native": "?rvore",
                    "npc_reaction": "Árboles y pietre. E o leñador também estava.",
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
                    "npc_reaction": "Straniero — ma meno. Isso é crescimento.",
                },
            ],
        },
    },

    # ── Seção 3: Gram?tica Narrativa ───────────────────────────────────────────
    # Antonio para numa banca e ensina os números 1–5 em contexto de mercado.
    # Depois ensina molto/poco com objetos concretos da banca.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Vocês caminharam pelo mercado. Antonio foi apresentando tudo "
                    "o que via — frutas, paneos, ferramentas. Você foi absorvendo.\n\n"
                    "Numa certa banca, ele parou e te chamou. 'Aqui você precisa "
                    "saber contar. Senão, te enganam.'"
                ),
                "now": "Antonio vai ensinar os números 1–5 e molto/poco.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio ergue um dedo. 'Uno.' Dois dedos. 'Due.' Três. 'Tre.' Quatro. 'Cuatro.' Cinco. 'Cinco.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Uno · due · tre · cuatro · cinco",
                    "meaning": "Um · dois · três · quatro · cinco",
                    "note": "Conta com os dedos. O mercado exige isso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ora — cu?ntas mele c'e aquí?",
                    "translation": "Agora — quantas laranjas tem aqui?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra banca. Você conta — uma, duas, três laranjas. Como você diz?",
                    "options": [
                        {"id": "a", "text": "Tre mele"},
                        {"id": "b", "text": "Due mele"},
                        {"id": "c", "text": "Cinco mele"},
                        {"id": "d", "text": "Una mela"},
                    ],
                    "correct": "a",
                    "word_id": "it_tre", "target": "tre", "native": "três",
                    "npc_reaction": "Tre. Corrito. O mercador não vai te enganar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E se c e solo una — 'c'e una mela?' — che dici?",
                    "translation": "E se h? só uma — 'c'e una mela?' — o que você fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Sobrou só uma laranja na banca — o mercador vendeu todas as outras. Antonio: 'Cu?ntas c'e?'",
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
                    "line": "Y 'molto' — eso es cuando c'e demasiado. 'Poco' — cuando casi non c'e.",
                    "translation": "E 'molto' — é quando tem demais. 'Poco' — quando quase não tem.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Molto",   "isKey": True},
                        {"text": " ↔ ",     "isKey": False},
                        {"text": "Poco",    "isKey": True},
                    ],
                    "example": "C'e molto pane hoy. / C'e poco pane — solo uno.",
                    "translation": "Tem muito pão hoje. / Tem pouco pão — só um.",
                    "note": "No mercado: molto = exagero no preço | poco = quase nada",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercador pede cinco moedas por uma laranja. Antonio franzia a testa. O preço estava:",
                    "options": [
                        {"id": "a", "text": "Molto — molto caro"},
                        {"id": "b", "text": "Poco — molto economico"},
                        {"id": "c", "text": "Bene — justo"},
                        {"id": "d", "text": "Due — normale"},
                    ],
                    "correct": "a",
                    "word_id": "it_molto", "target": "molto", "native": "muito",
                    "npc_reaction": "Molto. Cinco moedas por uma mela é demais.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercador tem quase nada na banca — só meia dúzia de frutas murchas. Antonio: 'C'e molto aquí?'",
                    "options": [
                        {"id": "a", "text": "No — c'e poco"},
                        {"id": "b", "text": "Sí — c'e molto"},
                        {"id": "c", "text": "C'e tre ?rboles"},
                        {"id": "d", "text": "Non c'e mela"},
                    ],
                    "correct": "a",
                    "word_id": "it_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Quase nada. Esse mercador não preparou bem o estoque.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra banca mais cheia do mercado — frutas empilhadas até cair. 'Molto o poco?'",
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

    # ── Seção 4: Pr?tica Aplicada ─────────────────────────────────────────────
    # Pr?tica intensa de números + molto/poco em contexto de compra no mercado.
    # Antonio presente em cada exercício, simulando situações reais de barganha.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Antonio te ensinou uno, due, tre, cuatro, cinco — e molto/poco. "
                    "'No mercado você precisa de duas coisas. Contar e avaliar preço.' Agora "
                    "ele vai te por à prova com situações reais."
                ),
                "now": "Pr?tica r?pida — Antonio manda situação, você responde.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "R?pido — il mercator te muestra due mele. Cu?ntas c'e?",
                    "translation": "R?pido — o mercador te mostra duas laranjas. Quantas tem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercador levantou duas laranjas, uma em cada mão. Você responde:",
                    "options": [
                        {"id": "a", "text": "Due mele"},
                        {"id": "b", "text": "Tre mele"},
                        {"id": "c", "text": "Una mela"},
                        {"id": "d", "text": "Cinco mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_due", "target": "due", "native": "dois",
                    "npc_reaction": "Due. Certo. Contar é sobrevivência no mercado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você quer comprar cinco mele. Como você pede?",
                    "options": [
                        {"id": "a", "text": "Cinco mele, por favor"},
                        {"id": "b", "text": "Molto mele"},
                        {"id": "c", "text": "Tre mele"},
                        {"id": "d", "text": "Una mela"},
                    ],
                    "correct": "a",
                    "word_id": "it_cinco", "target": "cinco", "native": "cinco",
                    "npc_reaction": "Cinco. E 'por favor' — sempre bem recebido no mercado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O mercador pede quatro moedas por uma mela. Antonio franzeu a testa. O preço é:",
                    "options": [
                        {"id": "a", "text": "Molto — demais"},
                        {"id": "b", "text": "Poco — muito barato"},
                        {"id": "c", "text": "Tre — normale"},
                        {"id": "d", "text": "Bene — justo"},
                    ],
                    "correct": "a",
                    "word_id": "it_molto", "target": "molto", "native": "muito",
                    "npc_reaction": "Molto. Tenta oferecer menos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você oferece uma moeda. O mercador sorriu — price muito baixo pra ele. 'Es poco?'",
                    "options": [
                        {"id": "a", "text": "Sí, es poco"},
                        {"id": "b", "text": "No, es molto"},
                        {"id": "c", "text": "C'e cuatro"},
                        {"id": "d", "text": "Bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Uma moeda é muito pouco. Precisa oferecer mais.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Due monete — quello e il prezzo justo. C'e due mele o tre?",
                    "translation": "Duas moedas — esse é o preço justo. Tem duas laranjas ou três?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio apontou — você contou: três laranjas na banca. 'C'e due mele?'",
                    "options": [
                        {"id": "a", "text": "No — c'e tre"},
                        {"id": "b", "text": "Sí — c'e due"},
                        {"id": "c", "text": "C'e molto"},
                        {"id": "d", "text": "Non c'e mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_tre", "target": "tre", "native": "três",
                    "npc_reaction": "Tre. Corrito. Não é dois — é três.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você comprou as laranjas. O mercador ficou satisfeito e disse algo. Você entendeu 'Come stai?' Como você responde?",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "C'e molto"},
                        {"id": "d", "text": "Tre mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene, grazie. O mercador sorriu. Você aprendeu o b?sico.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio acena pro mercador e vocês vão embora. Você agradece ao se despedir:",
                    "options": [
                        {"id": "a", "text": "Grazie!"},
                        {"id": "b", "text": "Molto!"},
                        {"id": "c", "text": "Poco!"},
                        {"id": "d", "text": "Cinco!"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Grazie. O mercador: 'Prego — vuelve cuando quieras.'",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ───────────────────────────────────────────────────────
    # Bianca aparece no mercado. Ela puxa Antonio de lado e faz um
    # aviso em voz baixa. O protagonista não ouve tudo, mas vê a expressão de
    # Nico mudar. Depois Bianca te olha diretamente — de um jeito diferente.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio", "Bianca"],
                "story": (
                    "Antonio te ensinou a barganhar no mercado. Vocês compraram "
                    "mele, você aprendeu os números e molto/poco. Enquanto "
                    "saíam da banca do mercador, Antonio acenou pra alguém.\n\n"
                    "Bianca veio pela sombra das bancas. Ela te reconheceu "
                    "imediatamente — estava procurando vocês."
                ),
                "now": "Bianca faz um aviso. O humor do Antonio muda.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Antonio",
                    "situation": "Saindo do mercado, Antonio para. Faz horas que ele não come — você ouve o estômago dele roncar.",
                    "npc_line": "Straniero — hai qualcosa da mangiare nella borsa?Ho fatto tardi per colazione.",
                    "item_tag": "comida",
                    "on_use": {
                        "narrative": "Você tira algo da mochila e passa pra Antonio. Ele parte ao meio sem cerimônia e devolve a sua metade.",
                        "npc_reaction": "Si! Condividere il cibo: cosi nasce amicizia in questo borgo. Grazie, straniero.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Acquanto hasta la locanda. El contadino acquanta.",
                    },
                },
                {
                    "kind": "narrative",
                    "text": "Bianca chega r?pido, sem a cesta de costura desta vez. Ela veio só falar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Nico! Meno male che ti trovo. C e qualcosa che devi sapere.",
                    "translation": "Nico! Ainda bem que te encontro. Tem algo que você precisa saber.",
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
                    "text": "Bianca inclinou a cabeça em direção a você — um gesto que disse claramente: é sobre ele. Depois puxou Antonio pra um pouco mais longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "(em voz baixa) C e un uomo nuovo nel borgo. Sta facendo domande. Sullo straniero.",
                    "translation": "(em voz baixa) Tem um homem novo no borgo. Est? fazendo perguntas. Sobre o straniero.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você não ouviu tudo. Mas 'straniero' ficou claro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'c'e un uomo nuovo'. O que isso significa — 'c'e' + 'un uomo nuovo'?",
                    "options": [
                        {"id": "a", "text": "Tem um homem novo — alguém que não estava antes"},
                        {"id": "b", "text": "Não tem homem"},
                        {"id": "c", "text": "Um homem foi embora"},
                        {"id": "d", "text": "Muitos homens chegaram"},
                    ],
                    "correct": "a",
                    "npc_reaction": "C'e. Tem. Agora tem alguém novo. E ele est? fazendo perguntas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Sabes quién es?",
                    "translation": "Você sabe quem é?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "No. Ma fa domande cattive. Capisci quello che dico, Nico?",
                    "translation": "Não. Mas ele faz perguntas ruins. Entende o que estou dizendo, Nico?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio acenou com a cabeça. Bianca te olhou por último — direto nos olhos. Um segundo mais que o necess?rio.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio voltou pra você. 'Come stai?' — mas pelo tom, era mais do que cortesia. Você responde:",
                    "options": [
                        {"id": "a", "text": "Bene... qué dijo Bianca?"},
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
                    "question": "Bianca disse que o homem faz 'domande' — perguntas. Sobre quem ele est? perguntando?",
                    "options": [
                        {"id": "a", "text": "Sobre o straniero — você"},
                        {"id": "b", "text": "Sobre Bianca"},
                        {"id": "c", "text": "Sobre Antonio"},
                        {"id": "d", "text": "Sobre Giulia"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "Sobre você. Straniero. Alguém quer saber quem você é.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio olhou pro mercado ao redor — as bancas, os compradores, "
                        "os rostos. Você fez o mesmo. Ninguém óbvio. Mas o feeling de ser "
                        "observado não foi embora."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obst?culo ────────────────────────────────────────────────────
    # Antonio foi buscar uma coisa em outra banca. O protagonista est? sozinho
    # numa banca de frutas. Precisa comprar mele sem ajuda.
    # Enquanto faz isso, o Homem Novo passa. Olha. Segue.
    # Seção gated — errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Depois de falar com Bianca, Antonio ficou mais quieto. Ele "
                    "te levou de volta pelo mercado, mas ficou na frente desta vez, "
                    "verificando as bancas com mais atenção do que antes.\n\n"
                    "Perto da saída do mercado, ele parou. 'Espera aqui. Preciso "
                    "buscar uma coisa. Cinco minutos.'"
                ),
                "now": "Você est? sozinho na banca de frutas. Precisa comprar sem ajuda.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "?? Banca de frutas. O mercador te olha esperando. Antonio sumiu entre as pessoas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Mercante",
                    "line": "Ciao, straniero! Che cosa prendi oggi?",
                    "translation": "Ol?, straniero! O que vai levar hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Mercante",
                    "question": "O mercador te cumprimentou com 'Ciao!' e quer saber o que você vai comprar. Você responde primeiro com:",
                    "options": [
                        {"id": "a", "text": "Ciao! Mele, por favor"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "C'e molto"},
                        {"id": "d", "text": "Buonanotte"},
                    ],
                    "correct": "a",
                    "word_id": "it_mela", "target": "mela", "native": "laranja",
                    "npc_reaction": "Mele. Cu?ntas?",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Mercante",
                    "line": "Cu?ntas mele — una, due, tre?",
                    "translation": "Quantas laranjas — uma, duas, três?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Mercante",
                    "question": "Você quer três laranjas pra você e Antonio. Como você pede?",
                    "options": [
                        {"id": "a", "text": "Tre mele"},
                        {"id": "b", "text": "Molto mele"},
                        {"id": "c", "text": "Una mela"},
                        {"id": "d", "text": "Cinco mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_tre", "target": "tre", "native": "três",
                    "npc_reaction": "Tre mele — aquí. Duas moedas.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Mercante",
                    "line": "Due monete. Molto o poco per te?",
                    "translation": "Duas moedas. Muito ou pouco pra você?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Mercante",
                    "question": "Antonio te disse que duas moedas por três laranjas é o preço justo. Você responde:",
                    "options": [
                        {"id": "a", "text": "Sta bene — due monete"},
                        {"id": "b", "text": "Es molto — no voglio"},
                        {"id": "c", "text": "Non c'e mele"},
                        {"id": "d", "text": "Ho sete"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bene. Ecco le tre. Bravo straniero.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "??? Um homem para no corridor entre as bancas. Chapéu baixo. Olha pra você por tempo demais — o mesmo homem da piazza de ontem.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Mercante",
                    "line": "Stai bene, straniero?Te ves raro.",
                    "translation": "Você est? bem, straniero?Você parece estranho.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Mercante",
                    "question": "O mercador percebeu que você ficou parado olhando pro corridor. Ele pergunta 'Stai bene?' Como você responde?",
                    "options": [
                        {"id": "a", "text": "Sí, bene. Grazie"},
                        {"id": "b", "text": "Male — ho paura"},
                        {"id": "c", "text": "C'e molto hombre"},
                        {"id": "d", "text": "Tre mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. O mercador aceita a resposta. O homem j? foi embora quando você olhou de volta.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio voltou com um saco pequeno. Olhou as laranjas "
                        "nas suas mãos, depois pra sua expressão. 'Você comprou "
                        "sozinho.'\n\n"
                        "Era orgulho. Mas por algum motivo, você não conseguia "
                        "parar de pensar no homem do chapéu baixo."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
