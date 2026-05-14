"""
Seed das 6 seções da Fase 20 Espanhol A1 — "La visita inesperada".

Continuação direta da F19. Os 3 jovens se separaram pra buscar o hombre
extranjero. Você vai à padaria de Rosa. Sofía à plaza. Miguel à herrería.

Você encontra o hombre primeiro. Rosa o aponta — está na esquina,
falando com um vendedor. Você observa de longe. Roupa de fora.
Documento na mão. Sotaque do distrito.

Sofía e Miguel chegam. Os 3 seguem ele de longe. Ele encontra María
na plaza. Trocam papéis. Conversa de 10 minutos. Ele sai antes do
meio-dia.

À noite, María volta calorosa. 'Hoy fue tranquilo, ¿no?' Ninguém
responde direto.

VOCAB NOVO (3): visita · llegar · esperar
LINGUAGEM NOVA: tener que + verbo (obrigação)
    tengo que decir / tienes que entender / tenemos que confrontarla

Revisão F1-F19:
  · puedo + verbo (F18)
  · quiero + verbo (F16)
  · ya / todavía no (F17)
  · vi/hablé/oí (F12)
  · mi/tu/su (F13)
  · el/la (F14)

NPC principais: El Inspector (1ª aparição) · os 4 · Rosa · Carmen
Arco emocional: caça → confronto silencioso → frustração crescente
Transição: F21 abre com decisão difícil — confrontar María diretamente.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f20_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Você chega à padaria de Rosa. Pergunta dele. Rosa aponta. 2 novos
    # exer + 3 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🍞 Padaria de Rosa · Manhã alta · Cheiro de pão fresco\n\n"
                        "Você chegou correndo. Rosa estava na porta — farinha "
                        "nas mãos, pão recém saído do forno. Te viu chegar e "
                        "fez sinal pra entrar."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "¡Joven! ¿Pasó algo? Estás corriendo.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Você ofegando. Tem que falar baixo — outras pessoas no balcão. Sofía te avisou: discrição.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Ven detrás. Aquí no.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Rosa te leva pra trás do balcão. Cozinha pequena, fogo aceso. Você senta no banco.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Dime. Sin susto.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "visita",  "native": "visita"},
                        {"target": "llegar",  "native": "chegar"},
                        {"target": "esperar", "native": "esperar"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Você cumprimenta Rosa — manhã ainda:",
                    "options": [
                        {"id": "a", "text": "Buenos días, Rosa"},
                        {"id": "b", "text": "Buenas tardes"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. Habla — ¿qué pasa?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Você pergunta direto — 'Rosa, há um homem novo no pueblo. Você o viu?' (algo que já aconteceu):",
                    "options": [
                        {"id": "a", "text": "¿Lo viste?"},
                        {"id": "b", "text": "¿Lo ves?"},
                        {"id": "c", "text": "¿Vas a verlo?"},
                        {"id": "d", "text": "¿Soy?"},
                    ],
                    "correct": "a",
                    "word_id": "es_viste", "target": "viste", "native": "viste",
                    "npc_reaction": "Lo vi. Acaba de pasar — fue al mercado. Hombre alto, joven, ropa de fuera.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Vino esta mañana — temprano. Llegó al pueblo en burro. Y ahora espera en la esquina del mercado — junto a la fuente.",
                    "translation": "Veio essa manhã — cedo. Chegou ao pueblo em burro. E agora espera na esquina do mercado — perto da fonte.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa disse 'llegó al pueblo en burro'. A palavra 'llegó' significa que o homem:",
                    "options": [
                        {"id": "a", "text": "Chegou (já aconteceu)"},
                        {"id": "b", "text": "Chega (todo dia)"},
                        {"id": "c", "text": "Vai chegar"},
                        {"id": "d", "text": "É chegada"},
                    ],
                    "correct": "a",
                    "word_id": "es_llego", "target": "llegó", "native": "chegou",
                    "npc_reaction": "Llegó. Esta mañana. Como tú llegaste hace dos semanas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "E Rosa disse 'espera en la esquina'. A palavra 'espera' significa que o homem:",
                    "options": [
                        {"id": "a", "text": "Espera (está parado, sem se mexer)"},
                        {"id": "b", "text": "Sai correndo"},
                        {"id": "c", "text": "Já foi"},
                        {"id": "d", "text": "Quer ir"},
                    ],
                    "correct": "a",
                    "word_id": "es_espera", "target": "espera", "native": "espera",
                    "npc_reaction": "Espera. Está quieto — quizá espera a alguien. Pero esa quietud no es de paseo.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Você sai. Encontra Sofía na plaza. Os 2 vão atrás do
    # homem. Miguel chega. Os 3 observam de longe. F1-F19 puro.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Sofía", "Miguel"],
                "story": (
                    "Você saiu da padaria. Sofía já estava na esquina perto da "
                    "iglesia — ela tinha visto o homem de longe. Miguel chegou "
                    "uns segundos depois.\n\n"
                    "'Está allá — el de la chaqueta marrón. Junto a la fuente.'"
                ),
                "now": "Os 3 observam de longe. Conversa baixa.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌳 Sombra dos arcos da iglesia · Os 3 escondidos · Um homem alto, jovem, junto à fonte",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Forastero — Rosa te dijo que llegó esta mañana, ¿verdad?",
                    "translation": "Forasteiro — Rosa te disse que ele chegou essa manhã, né?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Você confirma — Rosa te disse:",
                    "options": [
                        {"id": "a", "text": "Sí, me lo dijo Rosa"},
                        {"id": "b", "text": "Sí, me lo dice"},
                        {"id": "c", "text": "Voy a decir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_dijo", "target": "me lo dijo", "native": "me disse",
                    "npc_reaction": "Me lo dijo. Tercera persona pasado. Bien usado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía descreve o homem. Olha de longe. Alto e magro, jovem (uns 35 anos). Pra confirmar — você vê também:",
                    "options": [
                        {"id": "a", "text": "Sí, lo veo — es alto y delgado"},
                        {"id": "b", "text": "Sí, lo vi"},
                        {"id": "c", "text": "Voy a verlo"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_alto", "target": "alto", "native": "alto",
                    "npc_reaction": "Alto y delgado. Bien observado. Joven también — quizá treinta y cinco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: '¿Cómo estás? ¿Listo para seguirlo?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien, listo"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Sin acercarnos demasiado.",
                },
                {
                    "kind": "narrative",
                    "text": "O homem se mexe. Tira algo do bolso — papel dobrado. Lê. Olha pra rua. Espera.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Está esperando a alguien. Y tiene un papel — quizá una lista de nombres.",
                    "translation": "Está esperando alguém. E tem um papel — talvez uma lista de nomes.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Você pergunta pra Sofía — 'quem ele espera?'. Sofía: 'no sé. Pero quien sea — viene del distrito.' Pra você confirmar o que sabe (puedo + saber):",
                    "options": [
                        {"id": "a", "text": "Todavía no sé"},
                        {"id": "b", "text": "Ya sé"},
                        {"id": "c", "text": "Voy a saber"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavía no sé", "native": "ainda não sei",
                    "npc_reaction": "Todavía no. Pero pronto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "¿Y si lo seguimos hasta que se encuentre con quien sea?",
                    "translation": "E se a gente segue ele até encontrar com quem for?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Você concorda — sim, vamos seguir (algo que sai logo):",
                    "options": [
                        {"id": "a", "text": "Sí, vamos a seguirlo"},
                        {"id": "b", "text": "Voy a seguirlo"},
                        {"id": "c", "text": "Va a seguir"},
                        {"id": "d", "text": "Soy seguir"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos. Separados — para no llamar la atención.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Você quer dar uma volta — observar Carmen no caminho talvez. Sofía pergunta: '¿adónde quieres ir tú primero?' (quiero + verbo):",
                    "options": [
                        {"id": "a", "text": "Quiero ver a Carmen"},
                        {"id": "b", "text": "Voy a Carmen"},
                        {"id": "c", "text": "Soy a Carmen"},
                        {"id": "d", "text": "Tengo Carmen"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero ver", "native": "quero ver",
                    "npc_reaction": "Bien — Carmen puede tener más información. Vete tú. Nosotros seguimos al hombre.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Você vai à plaza onde Carmen está. Carmen confirma — o homem é primo do
    # Alcalde, conhecido como Inspector del Distrito. Vem fazer "auditorias".
    # Apresentação de "tener que + verbo" pelo uso natural.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Carmen"],
                "story": (
                    "Você foi à plaza pelo lado oposto — pra não passar pelo "
                    "homem da fonte. Carmen tava no banco dela, bordando. "
                    "Como sempre.\n\n"
                    "Ela te viu chegar — leu a sua cara. Pôs o bordado de lado."
                ),
                "now": "Carmen confirma quem é o homem. Apresentação de 'tener que'.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Forastero — algo pasó. Lo veo en tu cara.",
                    "translation": "Forasteiro — algo aconteceu. Vejo na tua cara.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Você cumprimenta e vai direto ao ponto:",
                    "options": [
                        {"id": "a", "text": "Buenos días, Carmen. Necesito preguntarte algo"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "Adiós Carmen"},
                        {"id": "d", "text": "Estoy mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. Habla — ¿qué pasa?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Antes que digas — sé qué quieres preguntarme. El hombre del mercado. Lo conozco.",
                    "translation": "Antes que você diga — sei o que vai me perguntar. O homem do mercado. Conheço.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'lo conozco'. Você responde — 'quem é ele?':",
                    "options": [
                        {"id": "a", "text": "¿Quién es?"},
                        {"id": "b", "text": "¿Cómo es?"},
                        {"id": "c", "text": "¿Dónde estás?"},
                        {"id": "d", "text": "¿Soy?"},
                    ],
                    "correct": "a",
                    "word_id": "es_quien", "target": "¿quién es?", "native": "quem é?",
                    "npc_reaction": "¿Quién es? Es el primo del Alcalde. Vino del distrito hace muchos años — y ahora viene de tanto en tanto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Es conocido como El Inspector. Su trabajo es controlar lo que pasa en los pueblos pequeños. Si hay forasteros sin pase, si hay sangres mezcladas, si hay 'cosas raras'.",
                    "translation": "É conhecido como El Inspector. O trabalho dele é controlar o que se passa nos pueblos pequenos. Se há forasteiros sem pase, se há sangues misturados, se há 'coisas estranhas'.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Você processa. Pra dizer 'então el Alcalde lo llamó' (já passou):",
                    "options": [
                        {"id": "a", "text": "Entonces el Alcalde lo llamó"},
                        {"id": "b", "text": "Entonces el Alcalde lo llama"},
                        {"id": "c", "text": "Va a llamarlo"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_llamo", "target": "llamó", "native": "chamou (ele)",
                    "npc_reaction": "Llamó. Quizá. O quizá vino solo — esa familia siempre se ayuda entre sí.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Tienes que hacer una cosa, joven. Tienes que avisarle a Don Miguel. Hoy mismo — antes que se vaya el Inspector.",
                    "translation": "Você tem que fazer uma coisa, jovem. Tem que avisar Don Miguel. Hoje mesmo — antes que o Inspector vá embora.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'tienes que avisarle'. A palavrinha 'tienes que' significa:",
                    "options": [
                        {"id": "a", "text": "Tens que / precisa (obrigação)"},
                        {"id": "b", "text": "Podes (se quiser)"},
                        {"id": "c", "text": "Vais"},
                        {"id": "d", "text": "És"},
                    ],
                    "correct": "a",
                    "word_id": "es_tienes_que", "target": "tienes que", "native": "tens que",
                    "npc_reaction": "Tienes que. Es obligación — no opción. La diferencia con 'puedes' es importante.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Yo tengo que quedarme aquí — si me ve, va a sospechar más. Pero tú tienes que correr.",
                    "translation": "Eu tenho que ficar aqui — se me vir, vai suspeitar mais. Mas você tem que correr.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'yo tengo que quedarme'. Pra você responder — sim, você tem que ir agora:",
                    "options": [
                        {"id": "a", "text": "Tengo que ir ya"},
                        {"id": "b", "text": "Voy a ir"},
                        {"id": "c", "text": "Quiero ir"},
                        {"id": "d", "text": "Soy ir"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_que", "target": "tengo que", "native": "tenho que",
                    "npc_reaction": "Tengo que. Sí — obligación. Y tienes que ir solo — nadie contigo. Más rápido.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen pergunta — você consegue correr até a casa de Don Miguel sem chamar atenção? Sim, você consegue (puedo + verbo):",
                    "options": [
                        {"id": "a", "text": "Sí, puedo correr"},
                        {"id": "b", "text": "No puedo"},
                        {"id": "c", "text": "Voy a correr"},
                        {"id": "d", "text": "Soy correr"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo correr", "native": "posso correr",
                    "npc_reaction": "Puedes. Ve por las callejuelas — no la calle principal. El Inspector la observa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Você agradece Carmen — formal, sincero:",
                    "options": [
                        {"id": "a", "text": "Gracias, Carmen"},
                        {"id": "b", "text": "Adiós Carmen"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Tengo gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Ve — y cuidate.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Correndo pelas vielas. Você encontra Don Miguel a meio caminho — ele já
    # tinha visto o Inspector pela janela. Conversa rápida onde Don Miguel
    # explica "tener que" formalmente. SEM nomear "verbo modal".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Você correu pelas vielas. Quase tropeçou duas vezes. "
                    "Don Miguel estava na esquina — esperando você. Já tinha "
                    "saído de casa.\n\n"
                    "'Ya lo vi por la ventana hace media hora. Espera — antes "
                    "de seguir, dime algo.'"
                ),
                "now": "Don Miguel explica 'tener que + verbo' antes de prosseguir.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Carmen te dijo 'tienes que avisar', ¿verdad?",
                    "translation": "Carmen te disse 'tienes que avisar', né?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você confirma — sim, ela disse:",
                    "options": [
                        {"id": "a", "text": "Sí, me lo dijo"},
                        {"id": "b", "text": "No me lo dijo"},
                        {"id": "c", "text": "Voy a decirlo"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_dijo", "target": "me lo dijo", "native": "me disse",
                    "npc_reaction": "Bueno. Antes de seguir — quiero que entiendas 'tengo que' bien. Lo vas a usar mucho hoy.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tengo que + verbo",
                    "meaning": "Obrigação — você é forçado a fazer",
                    "note": "diferente de 'puedo' (posso, se quero) e 'quiero' (quero fazer)",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "'Puedo' es lo que soy capaz. 'Quiero' es lo que deseo. 'Tengo que' es lo que no puedo evitar — la situación me obliga.",
                    "translation": "'Puedo' é o que sou capaz. 'Quiero' é o que desejo. 'Tengo que' é o que não posso evitar — a situação me obriga.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo tengo que ",     "isKey": True},
                        {"text": "ir · ",             "isKey": False},
                        {"text": "Tú tienes que ",    "isKey": True},
                        {"text": "saber · ",          "isKey": False},
                        {"text": "Ella tiene que ",   "isKey": True},
                        {"text": "callar · ",         "isKey": False},
                        {"text": "Tenemos que ",      "isKey": True},
                        {"text": "decidir",           "isKey": False},
                    ],
                    "example": "Tengo que ir. Tienes que saber esto. Carmen tiene que quedarse. Tenemos que decidir.",
                    "translation": "Tenho que ir. Você tem que saber isso. Carmen tem que ficar. Temos que decidir.",
                    "note": "tengo / tienes / tiene / tenemos + 'que' + outro verbo. La obligación.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você não tem escolha — precisa avisar todos. Pra dizer 'tengo que avisar' (obrigação):",
                    "options": [
                        {"id": "a", "text": "Tengo que avisar a todos"},
                        {"id": "b", "text": "Puedo avisar"},
                        {"id": "c", "text": "Quiero avisar"},
                        {"id": "d", "text": "Voy a avisar"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_que", "target": "tengo que", "native": "tenho que",
                    "npc_reaction": "Tengo que. La situación te obliga — no es algo que decides hacer.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'Y nosotros — ___ confrontar a María esta noche.' (obrigação, plural):",
                    "options": [
                        {"id": "a", "text": "tenemos que"},
                        {"id": "b", "text": "podemos"},
                        {"id": "c", "text": "queremos"},
                        {"id": "d", "text": "vamos"},
                    ],
                    "correct": "a",
                    "word_id": "es_tenemos_que", "target": "tenemos que", "native": "temos que",
                    "npc_reaction": "Tenemos que. Sin esperar más. Después que el Inspector se vaya — hablamos con ella.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra Carmen — alta, magra. Pra descrever a altura dela (mulher):",
                    "options": [
                        {"id": "a", "text": "Es alta"},
                        {"id": "b", "text": "Es alto"},
                        {"id": "c", "text": "Es altos"},
                        {"id": "d", "text": "Es altas"},
                    ],
                    "correct": "a",
                    "word_id": "es_alta", "target": "alta", "native": "alta",
                    "npc_reaction": "Alta. Carmen — mujer, alta. Termina en '-a'.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Você e Don Miguel vão até a plaza juntos. Sofía e Miguel já estão lá.
    # Os 4 observam de longe — María encontra o Inspector. Conversa de 10
    # minutos. Documento trocado. Ninguém escuta. Inspector vai embora.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Sofía", "Miguel", "El Inspector"],
                "story": (
                    "Vocês 2 chegaram à plaza. Sofía e Miguel já tavam escondidos "
                    "na sombra das árvores. Os 4 reunidos.\n\n"
                    "'Mira — María está llegando ahora.'"
                ),
                "now": "Vocês observam o encontro. Cada detalhe importa.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌳 Sombra das árvores · Os 4 observando · María cruzando a plaza",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "María llega — y él la espera. Como si fueran conocidos.",
                    "translation": "María chega — e ele a espera. Como se fossem conhecidos.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía disse 'él la espera'. Você confirma — sim, o Inspector está esperando:",
                    "options": [
                        {"id": "a", "text": "Sí, la espera"},
                        {"id": "b", "text": "Sí, la esperó"},
                        {"id": "c", "text": "Va a esperar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_espera", "target": "la espera", "native": "a espera",
                    "npc_reaction": "Espera. Sin moverse. Esperando algo específico.",
                },
                {
                    "kind": "narrative",
                    "text": "María chega perto. Não troca abraços. Apenas inclinação de cabeça — como dois conhecidos que não querem chamar atenção.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Inspector",
                    "line": "María. Has crecido — pero te reconozco igual. ¿Cómo estás?",
                    "translation": "María. Cresceste — mas te reconheço igual. Como estás?",
                    "is_new_npc": True,
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Estoy bien. Pero todavía no contesto preguntas oficiales aquí en la plaza.",
                    "translation": "Estou bem. Mas ainda não respondo perguntas oficiais aqui na plaza.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel sussurra: 'Él la conoce desde antes — ¿oíste?'",
                    "options": [
                        {"id": "a", "text": "Sí, lo oí"},
                        {"id": "b", "text": "No lo oigo"},
                        {"id": "c", "text": "Voy a oír"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "lo oí", "native": "ouvi",
                    "npc_reaction": "Oíste. Bueno. 'Has crecido' — eso es de alguien que la conoció de niña.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "O Inspector tira um papel do bolso. Mostra pra María. "
                        "Ela olha. Devolve. Os dois falam mais — vocês não "
                        "escutam, mas vêem María acenar com a cabeça."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Inspector",
                    "line": "Y el forastero. ¿Lo tienes controlado?",
                    "translation": "E o forasteiro. Tem ele controlado?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Lo tengo cerca. Eso es suficiente por ahora.",
                    "translation": "Tenho ele perto. Isso é suficiente por agora.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você ouviu isso. Claro. Don Miguel também. Sofía e Miguel "
                        "também. 'Lo tengo controlado'. Você é um item no plano "
                        "dela.\n\n"
                        "A frase girou pelo seu peito como o fuego da F5 — mas "
                        "fria desta vez."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pousa a mão no seu ombro. Pergunta baixo: '¿Cómo estás?'. Honesto:",
                    "options": [
                        {"id": "a", "text": "Estoy mal"},
                        {"id": "b", "text": "Estoy bien"},
                        {"id": "c", "text": "Soy mal"},
                        {"id": "d", "text": "Voy mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mal", "target": "estoy mal", "native": "estou mal",
                    "npc_reaction": "Lo entiendo, hijo. Esa frase duele. Pero ahora ya no podemos esperar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel diz: 'Esta noche — la confrontamos.' Você concorda — sim, temos que (obrigação):",
                    "options": [
                        {"id": "a", "text": "Sí, tenemos que"},
                        {"id": "b", "text": "Sí, podemos"},
                        {"id": "c", "text": "Sí, queremos"},
                        {"id": "d", "text": "Voy a"},
                    ],
                    "correct": "a",
                    "word_id": "es_tenemos_que", "target": "tenemos que", "native": "temos que",
                    "npc_reaction": "Tenemos que. Sin más esperas.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Noite. María volta calorosa. Vocês fingem normalidade. Don Miguel decide
    # que vão confrontar amanhã ao amanhecer. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["María", "Don Miguel"],
                "story": (
                    "O Inspector saiu do pueblo antes do meio-dia — pela mesma "
                    "estrada por onde entrou. María voltou pra casa de Don Miguel "
                    "à tarde, como se nada tivesse acontecido.\n\n"
                    "À noite, jantar tranquilo. María serviu — calorosa, "
                    "sorridente. 'Hoy fue tranquilo, ¿no?'"
                ),
                "now": "Vocês precisam fingir normalidade. Última noite antes do confronto.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🍲 Mesa do jantar · María servindo · Os 4 sentados · Lamparina baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Forastero — ¿cómo estuvo tu día? Saliste mucho.",
                    "translation": "Forasteiro — como foi seu dia? Você saiu muito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Mentira parcial — você passou na padaria, depois na plaza, foi cansativo:",
                    "options": [
                        {"id": "a", "text": "Estuve cansado, pero bien"},
                        {"id": "b", "text": "Estoy bien sin cansancio"},
                        {"id": "c", "text": "Soy bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estuve", "target": "estuve cansado", "native": "estive cansado",
                    "npc_reaction": "Estuviste cansado. Mañana descansas un poco más.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Sofía — ¿y tú? Pareces preocupada.",
                    "translation": "Sofía — e você? Pareces preocupada.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Tengo dolor de cabeza. Pero ya se me pasa.",
                    "translation": "Tenho dor de cabeça. Mas já me passa.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María oferece infusão. Pra dizer pra ela 'no, gracias' simples:",
                    "options": [
                        {"id": "a", "text": "No, gracias"},
                        {"id": "b", "text": "Sí, mucha"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Voy infusión"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_gracias", "target": "no, gracias", "native": "não, obrigado",
                    "npc_reaction": "Como queráis.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "María — hoy fue tranquilo, como dijiste. Mañana — quizá no tan tranquilo. Tendremos que hablar.",
                    "translation": "María — hoje foi tranquilo, como disse. Amanhã — talvez não tão tranquilo. Teremos que falar.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "María olha pra Don Miguel. Sem disfarçar. Não pergunta "
                        "o que ele quer dizer. Apenas acena de leve. Como quem "
                        "esperava esse momento."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Mañana entonces. Yo también tengo que decirles cosas.",
                    "translation": "Amanhã então. Eu também tenho que dizer coisas a vocês.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María disse 'tengo que decirles cosas'. Pra você confirmar pra Don Miguel — entendeu. Não responde María agora, só Don Miguel:",
                    "options": [
                        {"id": "a", "text": "Sí, lo oí"},
                        {"id": "b", "text": "No lo oigo"},
                        {"id": "c", "text": "Voy a oír"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "lo oí", "native": "ouvi",
                    "npc_reaction": "Bueno. Mañana entonces — todos.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Forastero — vete a dormir. Mañana es día largo. Quiero la cabeza fresca.",
                    "translation": "Forasteiro — vai dormir. Amanhã é dia longo. Quero a cabeça fresca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você se levanta pra ir dormir. Cumprimento de noite:",
                    "options": [
                        {"id": "a", "text": "Buenas noches"},
                        {"id": "b", "text": "Buenos días"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                    "npc_reaction": "Buenas noches, hijo. Mañana — hablamos.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F21 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🌙 Quarto · Você deitado · Lamparina apagada",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você ficou deitado. Os olhos abertos. A frase de María "
                        "girando — 'lo tengo controlado'.\n\n"
                        "Você lembrou da palavra na carta — 'vuelves'. Lembrou "
                        "da marca do Eduardo. Do sussurro de Lucía. Do Alcalde "
                        "frio. Da história de Carmen.\n\n"
                        "Tudo girando como uma engrenagem que finalmente "
                        "começou a fazer sentido.\n\n"
                        "Amanhã — confronto. Pela primeira vez vocês todos juntos. "
                        "Frente a frente com María. E você ainda não sabe se ela "
                        "vai sorrir ou se vai mudar de cara — pela primeira vez "
                        "em dez semanas."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Hijo — duerme. Mañana al amanecer, todos despiertos. Y ya no hay vuelta atrás.",
                    "translation": "Filho — dorme. Amanhã ao amanhecer, todos acordados. E já não há volta atrás.",
                    "pace": "slow",
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
