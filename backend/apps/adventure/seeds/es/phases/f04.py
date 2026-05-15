"""
Seed das 6 seções da Fase 4 Espanhol A1 — "El Mercado".

Dia de mercado no pueblo. Don Miguel leva o protagonista para a plaza central
onde os comerciantes montam as bancas. Barulho, cor, gente. O protagonista
começa a chamar atenção — Carmen faz um aviso a Miguel.

Novos vocab (3): naranja · uno/dos/tres · mucho / poco
Revisão F1–F3: hola, buenos días, gracias, de nada, bien/mal, me llamo,
               forastero, hay/no hay, pan, agua, árbol, piedra, río
NPC principal:   Don Miguel (fio condutor)
NPC cameo:       El Mercader (vendedor de frutas) · Señora Carmen (aviso)
Itens:           naranja_del_mercado (word_id: es_naranja)
Arco emocional:  anônimo → percebido; tensão começa a surgir
Transição:       voltam da plaza; Miguel mais quieto que o normal.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f4_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Dia de mercado. Barulho, cores, cheiro de fruta. Don Miguel apresenta o
    # mercado. Vocab novo aparece sem tradução — imersão. Exercícios: reconhecimento.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "persuasao",
                    "min_level": 1,
                    "uses_item_tag": "moneda",
                    "success": "A moeda certa e um saludo educado fazem o vendedor falar mais baixo.",
                    "fallback": "O vendedor nao confia de primeira, mas a proxima pergunta ainda abre o mercado.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🧺 Plaza central do pueblo. Manhã de mercado — bancas de "
                        "madeira com frutas e legumes, tecidos coloridos pendurados, "
                        "crianças correndo entre as pernas dos adultos. O barulho é o "
                        "dobro do normal."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¡Bienvenido al mercado, forastero! Una vez a la semana, toda la plaza se llena.",
                },
                {
                    "kind": "player",
                    "text": "Você ficou parado na entrada olhando. Nunca tinha visto tanta coisa num só lugar.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Mira — naranjas. Frutas del campo. ¿Cuánto, señor?",
                },
                {
                    "kind": "scene",
                    "text": "🍊 Um mercador de meia-idade com avental de couro aponta três laranjas brilhantes numa banca.",
                },
                {
                    "kind": "npc",
                    "npc": "El Mercader",
                    "line": "Tres naranjas — dos monedas. ¿Quieres?",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¿Cuánto? ¿Dos monedas? Eso es mucho para tres naranjas.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc",
                    "npc": "El Mercader",
                    "line": "¡No, no! Es poco. Las naranjas son grandes.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Você não entendeu os números nem o preço. Mas 'mucho' e 'poco' — muito e pouco — ficaram claros pelo tom.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Bien — tres naranjas. Toma, forastero.",
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
                    "question": "Don Miguel disse que o preço era 'mucho' para três laranjas. O que significa 'mucho'?",
                    "options": [
                        {"id": "a", "text": "Muito"},
                        {"id": "b", "text": "Pouco"},
                        {"id": "c", "text": "Nada"},
                        {"id": "d", "text": "Bom"},
                    ],
                    "correct": "a",
                    "word_id": "es_mucho", "target": "mucho", "native": "muito",
                    "npc_reaction": "Mucho = muito. Sempre que achar o preço alto — mucho.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercader rebateu que o preço era 'poco' — que as laranjas eram grandes. O que significa 'poco'?",
                    "options": [
                        {"id": "a", "text": "Pouco"},
                        {"id": "b", "text": "Muito"},
                        {"id": "c", "text": "Caro"},
                        {"id": "d", "text": "Barato"},
                    ],
                    "correct": "a",
                    "word_id": "es_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco = pouco. No mercado é sempre assim: mucho ou poco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercader disse 'tres naranjas'. Você olhou — tinha exatamente três frutas na banca. 'Tres' significa:",
                    "options": [
                        {"id": "a", "text": "Três"},
                        {"id": "b", "text": "Um"},
                        {"id": "c", "text": "Dois"},
                        {"id": "d", "text": "Cinco"},
                    ],
                    "correct": "a",
                    "word_id": "es_tres", "target": "tres", "native": "três",
                    "npc_reaction": "Tres. Uno, dos, tres — conta com os dedos primeiro.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Don Miguel passeia pelo mercado com o protagonista. Revisão de F1+F2+F3
    # vocab em contexto de mercado. Cada exercício é uma situação real.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "O mercado está barulhento e cheio. Don Miguel te deu uma naranja "
                    "e começou a andar pelo corredor de bancas. Você seguiu carregando "
                    "a fruta na mão, observando tudo.\n\n"
                    "Ontem vocês foram ao río e você conheceu o velho Ernesto. Antes "
                    "disso, você aprendeu 'hay', 'árbol', 'piedra', 'río'. E desde o "
                    "começo: 'hola', 'gracias', 'bien', 'tengo hambre', 'pan', 'agua'."
                ),
                "now": "Don Miguel quer saber se tudo que você aprendeu ainda está na cabeça.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel para na frente de uma banca com frutas e legumes. Aponta pro ambiente ao redor.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Qué hay en el mercado? Mira alrededor y dime.",
                    "translation": "O que tem no mercado? Olha ao redor e me fala.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Bancas cheias, gente, frutas, tecidos. Don Miguel quer saber se você sabe usar 'hay'. Você diz:",
                    "options": [
                        {"id": "a", "text": "Hay naranjas y mucha gente"},
                        {"id": "b", "text": "No hay nada"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Hay árboles"},
                    ],
                    "correct": "a",
                    "word_id": "es_naranja", "target": "naranja", "native": "laranja",
                    "npc_reaction": "Hay naranjas. E muita gente. Correto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Una señora pasa con una cesta de pan. Tú la ves y...",
                    "translation": "Uma senhora passa com uma cesta de pão. Você a vê e...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "A senhora olha pra você ao passar. Como você cumprimenta — é de manhã:",
                    "options": [
                        {"id": "a", "text": "¡Buenos días!"},
                        {"id": "b", "text": "¡Buenas noches!"},
                        {"id": "c", "text": "¡Adiós!"},
                        {"id": "d", "text": "¡Mal!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. Ela acenou de volta. Já não és mais um estranho.",
                },
                {
                    "kind": "narrative",
                    "text": "Na cesta da senhora: pão escuro, cheiroso. Seu estômago roncou.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O pão na cesta da senhora cheirava bem. Seu estômago avisou antes de você. Como você fala pra Don Miguel?",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Hay pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. Você comeu a naranja, não? — 'Sí, Don Miguel, pero...'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Rosa tiene pan. Después compramos. Primero hay que caminar más.",
                    "translation": "Rosa tem pão. Depois compramos. Primeiro tem que caminhar mais.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel mencionou que Rosa tem pão. Você foi na casa dela pela manhã. Ela tem mesmo — como você confirma?",
                    "options": [
                        {"id": "a", "text": "Sí, hay pan en la casa de Rosa"},
                        {"id": "b", "text": "No hay pan"},
                        {"id": "c", "text": "Hay árboles en la casa"},
                        {"id": "d", "text": "No hay agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pão",
                    "npc_reaction": "Hay pan. Sempre hay pan na casa dela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Y ayer en el campo — qué había cerca del río?",
                    "translation": "E ontem no campo — o que havia perto do río?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Ontem no río — você viu árboles, piedras, e água correndo. Don Miguel pergunta o que havia:",
                    "options": [
                        {"id": "a", "text": "Había árboles y piedras"},
                        {"id": "b", "text": "Había naranjas"},
                        {"id": "c", "text": "No había nada"},
                        {"id": "d", "text": "Había pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "árbol", "native": "árvore",
                    "npc_reaction": "Árboles y piedras. E o leñador também estava.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: '¿Eres el forastero de San Cristóbal ahora — o todavía eres un extraño?'",
                    "options": [
                        {"id": "a", "text": "Sigo siendo forastero — pero menos"},
                        {"id": "b", "text": "Soy campesino"},
                        {"id": "c", "text": "No hay forastero"},
                        {"id": "d", "text": "Tengo sed"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero — pero menos. Isso é crescimento.",
                },
            ],
        },
    },

    # ── Seção 3: Gramática Narrativa ───────────────────────────────────────────
    # Don Miguel para numa banca e ensina os números 1–5 em contexto de mercado.
    # Depois ensina mucho/poco com objetos concretos da banca.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Vocês caminharam pelo mercado. Don Miguel foi apresentando tudo "
                    "o que via — frutas, panos, ferramentas. Você foi absorvendo.\n\n"
                    "Numa certa banca, ele parou e te chamou. 'Aqui você precisa "
                    "saber contar. Senão, te enganam.'"
                ),
                "now": "Don Miguel vai ensinar os números 1–5 e mucho/poco.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel ergue um dedo. 'Uno.' Dois dedos. 'Dos.' Três. 'Tres.' Quatro. 'Cuatro.' Cinco. 'Cinco.'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Uno · dos · tres · cuatro · cinco",
                    "meaning": "Um · dois · três · quatro · cinco",
                    "note": "Conta com os dedos. O mercado exige isso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ahora — cuántas naranjas hay aquí?",
                    "translation": "Agora — quantas laranjas tem aqui?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra banca. Você conta — uma, duas, três laranjas. Como você diz?",
                    "options": [
                        {"id": "a", "text": "Tres naranjas"},
                        {"id": "b", "text": "Dos naranjas"},
                        {"id": "c", "text": "Cinco naranjas"},
                        {"id": "d", "text": "Una naranja"},
                    ],
                    "correct": "a",
                    "word_id": "es_tres", "target": "tres", "native": "três",
                    "npc_reaction": "Tres. Correto. O mercador não vai te enganar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y si hay solo una — '¿hay una naranja?' — qué dices?",
                    "translation": "E se há só uma — 'hay una naranja?' — o que você fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Sobrou só uma laranja na banca — o mercador vendeu todas as outras. Don Miguel: '¿Cuántas hay?'",
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
                    "line": "Y 'mucho' — eso es cuando hay demasiado. 'Poco' — cuando casi no hay.",
                    "translation": "E 'mucho' — é quando tem demais. 'Poco' — quando quase não tem.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Mucho",   "isKey": True},
                        {"text": " ↔ ",     "isKey": False},
                        {"text": "Poco",    "isKey": True},
                    ],
                    "example": "Hay mucho pan hoy. / Hay poco pan — solo uno.",
                    "translation": "Tem muito pão hoje. / Tem pouco pão — só um.",
                    "note": "No mercado: mucho = exagero no preço | poco = quase nada",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercador pede cinco moedas por uma laranja. Don Miguel franzia a testa. O preço estava:",
                    "options": [
                        {"id": "a", "text": "Mucho — muy caro"},
                        {"id": "b", "text": "Poco — muy barato"},
                        {"id": "c", "text": "Bien — justo"},
                        {"id": "d", "text": "Dos — normal"},
                    ],
                    "correct": "a",
                    "word_id": "es_mucho", "target": "mucho", "native": "muito",
                    "npc_reaction": "Mucho. Cinco moedas por uma naranja é demais.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercador tem quase nada na banca — só meia dúzia de frutas murchas. Don Miguel: '¿Hay mucho aquí?'",
                    "options": [
                        {"id": "a", "text": "No — hay poco"},
                        {"id": "b", "text": "Sí — hay mucho"},
                        {"id": "c", "text": "Hay tres árboles"},
                        {"id": "d", "text": "No hay naranja"},
                    ],
                    "correct": "a",
                    "word_id": "es_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Quase nada. Esse mercador não preparou bem o estoque.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra banca mais cheia do mercado — frutas empilhadas até cair. '¿Mucho o poco?'",
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

    # ── Seção 4: Prática Aplicada ─────────────────────────────────────────────
    # Prática intensa de números + mucho/poco em contexto de compra no mercado.
    # Don Miguel presente em cada exercício, simulando situações reais de barganha.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel te ensinou uno, dos, tres, cuatro, cinco — e mucho/poco. "
                    "'No mercado você precisa dos dois. Contar e avaliar preço.' Agora "
                    "ele vai te por à prova com situações reais."
                ),
                "now": "Prática rápida — Don Miguel manda situação, você responde.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Rápido — el mercador te muestra dos naranjas. ¿Cuántas hay?",
                    "translation": "Rápido — o mercador te mostra duas laranjas. Quantas tem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercador levantou duas laranjas, uma em cada mão. Você responde:",
                    "options": [
                        {"id": "a", "text": "Dos naranjas"},
                        {"id": "b", "text": "Tres naranjas"},
                        {"id": "c", "text": "Una naranja"},
                        {"id": "d", "text": "Cinco naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_dos", "target": "dos", "native": "dois",
                    "npc_reaction": "Dos. Certo. Contar é sobrevivência no mercado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você quer comprar cinco naranjas. Como você pede?",
                    "options": [
                        {"id": "a", "text": "Cinco naranjas, por favor"},
                        {"id": "b", "text": "Mucho naranjas"},
                        {"id": "c", "text": "Tres naranjas"},
                        {"id": "d", "text": "Una naranja"},
                    ],
                    "correct": "a",
                    "word_id": "es_cinco", "target": "cinco", "native": "cinco",
                    "npc_reaction": "Cinco. E 'por favor' — sempre bem recebido no mercado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O mercador pede quatro moedas por uma naranja. Don Miguel franzeu a testa. O preço é:",
                    "options": [
                        {"id": "a", "text": "Mucho — demais"},
                        {"id": "b", "text": "Poco — muito barato"},
                        {"id": "c", "text": "Tres — normal"},
                        {"id": "d", "text": "Bien — justo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mucho", "target": "mucho", "native": "muito",
                    "npc_reaction": "Mucho. Tenta oferecer menos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você oferece uma moeda. O mercador sorriu — price muito baixo pra ele. '¿Es poco?'",
                    "options": [
                        {"id": "a", "text": "Sí, es poco"},
                        {"id": "b", "text": "No, es mucho"},
                        {"id": "c", "text": "Hay cuatro"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Uma moeda é muito pouco. Precisa oferecer mais.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Dos monedas — ese es el precio justo. ¿Hay dos naranjas o tres?",
                    "translation": "Duas moedas — esse é o preço justo. Tem duas laranjas ou três?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel apontou — você contou: três laranjas na banca. '¿Hay dos naranjas?'",
                    "options": [
                        {"id": "a", "text": "No — hay tres"},
                        {"id": "b", "text": "Sí — hay dos"},
                        {"id": "c", "text": "Hay mucho"},
                        {"id": "d", "text": "No hay naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_tres", "target": "tres", "native": "três",
                    "npc_reaction": "Tres. Correto. Não é dois — é três.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você comprou as laranjas. O mercador ficou satisfeito e disse algo. Você entendeu '¿Cómo estás?' Como você responde?",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Hay mucho"},
                        {"id": "d", "text": "Tres naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien, gracias. O mercador sorriu. Você aprendeu o básico.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel acena pro mercador e vocês vão embora. Você agradece ao se despedir:",
                    "options": [
                        {"id": "a", "text": "¡Gracias!"},
                        {"id": "b", "text": "¡Mucho!"},
                        {"id": "c", "text": "¡Poco!"},
                        {"id": "d", "text": "¡Cinco!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Gracias. O mercador: 'De nada — vuelve cuando quieras.'",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ───────────────────────────────────────────────────────
    # Señora Carmen aparece no mercado. Ela puxa Don Miguel de lado e faz um
    # aviso em voz baixa. O protagonista não ouve tudo, mas vê a expressão de
    # Miguel mudar. Depois Carmen te olha diretamente — de um jeito diferente.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Carmen"],
                "story": (
                    "Don Miguel te ensinou a barganhar no mercado. Vocês compraram "
                    "naranjas, você aprendeu os números e mucho/poco. Enquanto "
                    "saíam da banca do mercador, Don Miguel acenou pra alguém.\n\n"
                    "Señora Carmen veio pela sombra das bancas. Ela te reconheceu "
                    "imediatamente — estava procurando vocês."
                ),
                "now": "Carmen faz um aviso. O humor do Don Miguel muda.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Don Miguel",
                    "situation": "Saindo do mercado, Don Miguel para. Faz horas que ele não come — você ouve o estômago dele roncar.",
                    "npc_line": "Forastero — ¿tienes algo de comer en la bolsa? Se me hizo tarde el desayuno.",
                    "item_tag": "comida",
                    "on_use": {
                        "narrative": "Você tira algo da mochila e passa pra Don Miguel. Ele parte ao meio sem cerimônia e devolve a sua metade.",
                        "npc_reaction": "¡Eso! Compartir comida — así se hace amistad en este pueblo. Gracias, forastero.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Aguanto hasta la posada. El campesino aguanta.",
                    },
                },
                {
                    "kind": "narrative",
                    "text": "Carmen chega rápido, sem a cesta de costura desta vez. Ela veio só falar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¡Miguel! Menos mal que te encuentro. Hay algo que tienes que saber.",
                    "translation": "Miguel! Ainda bem que te encontro. Tem algo que você precisa saber.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Qué pasa, Carmen?",
                    "translation": "O que acontece, Carmen?",
                },
                {
                    "kind": "narrative",
                    "text": "Carmen inclinou a cabeça em direção a você — um gesto que disse claramente: é sobre ele. Depois puxou Don Miguel pra um pouco mais longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "(em voz baixa) Hay un hombre nuevo en el pueblo. Está haciendo preguntas. Sobre el forastero.",
                    "translation": "(em voz baixa) Tem um homem novo no pueblo. Está fazendo perguntas. Sobre o forasteiro.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você não ouviu tudo. Mas 'forastero' ficou claro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'hay un hombre nuevo'. O que isso significa — 'hay' + 'un hombre nuevo'?",
                    "options": [
                        {"id": "a", "text": "Tem um homem novo — alguém que não estava antes"},
                        {"id": "b", "text": "Não tem homem"},
                        {"id": "c", "text": "Um homem foi embora"},
                        {"id": "d", "text": "Muitos homens chegaram"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Hay. Tem. Agora tem alguém novo. E ele está fazendo perguntas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Sabes quién es?",
                    "translation": "Você sabe quem é?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "No. Pero tiene malas preguntas. ¿Entiendes lo que digo, Miguel?",
                    "translation": "Não. Mas ele faz perguntas ruins. Entende o que estou dizendo, Miguel?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel acenou com a cabeça. Carmen te olhou por último — direto nos olhos. Um segundo mais que o necessário.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel voltou pra você. '¿Cómo estás?' — mas pelo tom, era mais do que cortesia. Você responde:",
                    "options": [
                        {"id": "a", "text": "Bien... ¿qué dijo Carmen?"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Hay mucho"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "npc_reaction": "'Nada que te preocupe.' Mas o rosto dele disse outra coisa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Carmen disse que o homem faz 'preguntas' — perguntas. Sobre quem ele está perguntando?",
                    "options": [
                        {"id": "a", "text": "Sobre o forastero — você"},
                        {"id": "b", "text": "Sobre Carmen"},
                        {"id": "c", "text": "Sobre Don Miguel"},
                        {"id": "d", "text": "Sobre Rosa"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Sobre você. Forastero. Alguém quer saber quem você é.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel olhou pro mercado ao redor — as bancas, os compradores, "
                        "os rostos. Você fez o mesmo. Ninguém óbvio. Mas o feeling de ser "
                        "observado não foi embora."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Don Miguel foi buscar uma coisa em outra banca. O protagonista está sozinho
    # numa banca de frutas. Precisa comprar naranjas sem ajuda.
    # Enquanto faz isso, o Homem Novo passa. Olha. Segue.
    # Seção gated — errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Depois de falar com Carmen, Don Miguel ficou mais quieto. Ele "
                    "te levou de volta pelo mercado, mas ficou na frente desta vez, "
                    "verificando as bancas com mais atenção do que antes.\n\n"
                    "Perto da saída do mercado, ele parou. 'Espera aqui. Preciso "
                    "buscar uma coisa. Cinco minutos.'"
                ),
                "now": "Você está sozinho na banca de frutas. Precisa comprar sem ajuda.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🍊 Banca de frutas. O mercador te olha esperando. Don Miguel sumiu entre as pessoas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Mercader",
                    "line": "¡Hola, forastero! ¿Qué vas a llevar hoy?",
                    "translation": "Olá, forasteiro! O que vai levar hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Mercader",
                    "question": "O mercador te cumprimentou com '¡Hola!' e quer saber o que você vai comprar. Você responde primeiro com:",
                    "options": [
                        {"id": "a", "text": "¡Hola! Naranjas, por favor"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Hay mucho"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_naranja", "target": "naranja", "native": "laranja",
                    "npc_reaction": "Naranjas. ¿Cuántas?",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Mercader",
                    "line": "¿Cuántas naranjas — una, dos, tres?",
                    "translation": "Quantas laranjas — uma, duas, três?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Mercader",
                    "question": "Você quer três laranjas pra você e Don Miguel. Como você pede?",
                    "options": [
                        {"id": "a", "text": "Tres naranjas"},
                        {"id": "b", "text": "Mucho naranjas"},
                        {"id": "c", "text": "Una naranja"},
                        {"id": "d", "text": "Cinco naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_tres", "target": "tres", "native": "três",
                    "npc_reaction": "Tres naranjas — aquí. Duas moedas.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Mercader",
                    "line": "Dos monedas. ¿Mucho o poco para ti?",
                    "translation": "Duas moedas. Muito ou pouco pra você?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Mercader",
                    "question": "Don Miguel te disse que duas moedas por três laranjas é o preço justo. Você responde:",
                    "options": [
                        {"id": "a", "text": "Está bien — dos monedas"},
                        {"id": "b", "text": "Es mucho — no quiero"},
                        {"id": "c", "text": "No hay naranjas"},
                        {"id": "d", "text": "Tengo sed"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bien. Aquí tienes las tres. Buen forastero.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "👁️ Um homem para no corredor entre as bancas. Chapéu baixo. Olha pra você por tempo demais — o mesmo homem da plaza de ontem.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Mercader",
                    "line": "¿Estás bien, forastero? Te ves raro.",
                    "translation": "Você está bem, forasteiro? Você parece estranho.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Mercader",
                    "question": "O mercador percebeu que você ficou parado olhando pro corredor. Ele pergunta '¿Estás bien?' Como você responde?",
                    "options": [
                        {"id": "a", "text": "Sí, bien. Gracias"},
                        {"id": "b", "text": "Mal — tengo miedo"},
                        {"id": "c", "text": "Hay mucho hombre"},
                        {"id": "d", "text": "Tres naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. O mercador aceita a resposta. O homem já foi embora quando você olhou de volta.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel voltou com um saco pequeno. Olhou as laranjas "
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
