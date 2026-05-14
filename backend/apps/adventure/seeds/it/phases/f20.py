"""
Seed das 6 seções da Fase 20 Italiano A1 — "La visita inesperada".

Continuação direta da F19. Os 3 giovanes se separaram pra buscar o hombre
extranjero. Você vai à padaria de Giulia. Chiara à piazza. Nico à herrería.

Você encontra o hombre primeiro. Giulia o aponta — está na esquina,
falando com um vienidedor. Você observa de longe. Roupa de fora.
Documento na mão. Sotaque do distrito.

Chiara e Nico chegam. Os 3 seguem ele de longe. Ele encontra Lucia
na piazza. Trocam papéis. Conversa de 10 minutos. Ele sai prima do
meio-dia.

À noite, Lucia volta calorosa. 'Hoy fue tranquilo, ¿no?' Ninguém
responde direto.

VOCAB NOVO (3): visita · llegar · esperar
LINGUAGEM NOVA: tener que + verbo (obrigação)
    ho que decir / hai que entender / tenemos que confrontarla

Revisão F1-F19:
  · puedo + verbo (F18)
  · quiero + verbo (F16)
  · ya / todavía no (F17)
  · vi/hablé/oí (F12)
  · mi/tu/su (F13)
  · el/la (F14)

NPC principais: L'Ispettore (1ª aparição) · os 4 · Giulia · Bianca
Arco emocional: caça → confronto silencioso → frustração crescente
Transição: F21 abre com decisão difícil — confrontar Lucia diretamente.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Você chega à padaria de Giulia. Pergunta dele. Giulia aponta. 2 novos
    # exer + 3 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "?? Padaria de Giulia · Manhã alta · Cheiro de pão fresco\n\n"
                        "Você chegou correndo. Giulia estava na porta — farinha "
                        "nas mãos, pão recém saído do forno. Te viu chegar e "
                        "fez senzaal pra entrar."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "¡Jovieni! ¿Pasó algo?Estás corriendo.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Você ofegando. Tem que falar baixo — outras pessoas no balcão. Chiara te avisou: discrição.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Vieni detrás. Aquí no.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Giulia te leva pra trás do balcão. Cozinha pequena, fogo acquesto. Você senta no banco.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Dime. Senza susto.",
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
                    "npc": "Giulia",
                    "question": "Você cumprimenta Giulia — manhã ainda:",
                    "options": [
                        {"id": "a", "text": "Benes días, Giulia"},
                        {"id": "b", "text": "Buon pomeriggio"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Benes días. Habla — ¿qué pasa?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Você pergunta direto — 'Giulia, há um homem novo no borgo. Você o viu?' (algo que já aconteceu):",
                    "options": [
                        {"id": "a", "text": "¿Lo viste?"},
                        {"id": "b", "text": "¿Lo ves?"},
                        {"id": "c", "text": "¿Vas a verlo?"},
                        {"id": "d", "text": "¿Sono?"},
                    ],
                    "correct": "a",
                    "word_id": "it_viste", "target": "viste", "native": "viste",
                    "npc_reaction": "Lo vi. Acaba de pasar — fue al mercato. Hombre alto, giovane, ropa de fuera.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Vino esta mañana — temprano. Llegó al borgo en burro. Y adesso espera en la esquina del mercato — junto a la fuente.",
                    "translation": "Veio essa manhã — cedo. Chegou ao borgo em burro. E agora espera na esquina do mercato — perto da fonte.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia disse 'llegó al borgo en burro'. A palavra 'llegó' significa que o homem:",
                    "options": [
                        {"id": "a", "text": "Chegou (já aconteceu)"},
                        {"id": "b", "text": "Chega (todo dia)"},
                        {"id": "c", "text": "Vai chegar"},
                        {"id": "d", "text": "É chegada"},
                    ],
                    "correct": "a",
                    "word_id": "it_arrivo", "target": "llegó", "native": "chegou",
                    "npc_reaction": "Llegó. Esta mañana. Como tu sei arrivato hace dos semanas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "E Giulia disse 'espera en la esquina'. A palavra 'espera' significa que o homem:",
                    "options": [
                        {"id": "a", "text": "Espera (está parado, sem se mexer)"},
                        {"id": "b", "text": "Sai correndo"},
                        {"id": "c", "text": "Já foi"},
                        {"id": "d", "text": "Quer ir"},
                    ],
                    "correct": "a",
                    "word_id": "it_espera", "target": "espera", "native": "espera",
                    "npc_reaction": "Espera. Está quieto — quizá espera a alguien. Ma esa quietud no es de paseo.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Você sai. Encontra Chiara na piazza. Os 2 vão atrás do
    # homem. Nico chega. Os 3 observam de longe. F1-F19 puro.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Chiara", "Nico"],
                "story": (
                    "Você saiu da padaria. Chiara já estava na esquina perto da "
                    "iglesia — ela tinha visto o homem de longe. Nico chegou "
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
                    "npc": "Chiara",
                    "line": "Forestiero — Giulia te ha detto que llegó esta mañana, ¿verdad?",
                    "translation": "Forasteiro — Giulia te disse que ele chegou essa manhã, né?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Você confirma — Giulia te disse:",
                    "options": [
                        {"id": "a", "text": "Sí, me lo ha detto Giulia"},
                        {"id": "b", "text": "Sí, me lo dice"},
                        {"id": "c", "text": "Vado a decir"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ha detto", "target": "me lo ha detto", "native": "me disse",
                    "npc_reaction": "Me lo ha detto. Tercera persona pasado. Bene usado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara descreve o homem. Olha de longe. Alto e magro, jovem (uns 35 anni). Pra confirmar — você vê também:",
                    "options": [
                        {"id": "a", "text": "Sí, lo veo — es alto y delgado"},
                        {"id": "b", "text": "Sí, lo vi"},
                        {"id": "c", "text": "Vado a verlo"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_alto", "target": "alto", "native": "alto",
                    "npc_reaction": "Alto y delgado. Bene observado. Jovieni también — quizá treinta y cinco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico: '¿Cómo estás?¿Listo para seguirlo?'",
                    "options": [
                        {"id": "a", "text": "Sto bene, listo"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Vado bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Bene. Senza acercarnos depiuiado.",
                },
                {
                    "kind": "narrative",
                    "text": "O homem se mexe. Tira algo do bolso — papel dobrado. Lê. Olha pra rua. Espera.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Está esperando a alguien. Y ha un papel — quizá una lista de nombres.",
                    "translation": "Está esperando alguém. E tem um papel — talvez uma lista de nomes.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Você pergunta pra Chiara — 'quem ele espera?'. Chiara: 'no sé. Ma chi sea — viene del distrito.' Pra você confirmar o que sabe (puedo + saber):",
                    "options": [
                        {"id": "a", "text": "Todavía no sé"},
                        {"id": "b", "text": "Ya sé"},
                        {"id": "c", "text": "Vado a saber"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ancora_no", "target": "todavía no sé", "native": "ainda não sei",
                    "npc_reaction": "Todavía no. Ma pronto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "¿Y si lo seguimos hasta que se encuentre con chi sea?",
                    "translation": "E se a gente segue ele até encontrar com quem for?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Você concorda — sim, andiamo seguir (algo que sai logo):",
                    "options": [
                        {"id": "a", "text": "Sí, andiamo a seguirlo"},
                        {"id": "b", "text": "Vado a seguirlo"},
                        {"id": "c", "text": "Va a seguir"},
                        {"id": "d", "text": "Sono seguir"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo. Separados — para no llamar la atención.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Você quer dar uma volta — observar Bianca no caminho talvez. Chiara pergunta: '¿adónde quieres ir tu primero?' (quiero + verbo):",
                    "options": [
                        {"id": "a", "text": "Quiero ver a Bianca"},
                        {"id": "b", "text": "Vado a Bianca"},
                        {"id": "c", "text": "Sono a Bianca"},
                        {"id": "d", "text": "Ho Bianca"},
                    ],
                    "correct": "a",
                    "word_id": "it_quiero", "target": "quiero ver", "native": "quero ver",
                    "npc_reaction": "Bene — Bianca puede tener más información. Vete tu. Nosotros seguimos al hombre.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Você vai à piazza onde Bianca está. Bianca confirma — o homem é primo do
    # Podesta, conhecido come Ispettore del Distrito. Vem fazer "auditorias".
    # Apresentação de "tener que + verbo" pelo uso natural.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Bianca"],
                "story": (
                    "Você foi à piazza pelo lado oposto — pra não passar pelo "
                    "homem da fonte. Bianca tava no banco dela, bordando. "
                    "Como sempre.\n\n"
                    "Ela te viu chegar — leu a sua cara. Pôs o bordado de lado."
                ),
                "now": "Bianca confirma quem é o homem. Apresentação de 'tener que'.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Forestiero — algo pasó. Lo veo en tu cara.",
                    "translation": "Forasteiro — algo aconteceu. Vejo na tua cara.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Você cumprimenta e vai direto ao ponto:",
                    "options": [
                        {"id": "a", "text": "Benes días, Bianca. Necesito preguntarte algo"},
                        {"id": "b", "text": "Buona notte"},
                        {"id": "c", "text": "Adiós Bianca"},
                        {"id": "d", "text": "Sto male"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Benes días. Habla — ¿qué pasa?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Prima que digas — sé qué quieres preguntarme. El hombre del mercato. Lo conozco.",
                    "translation": "Prima que você diga — sei o que vai me perguntar. O homem do mercato. Conheço.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'lo conozco'. Você responde — 'quem é ele?':",
                    "options": [
                        {"id": "a", "text": "¿Quién es?"},
                        {"id": "b", "text": "¿Cómo es?"},
                        {"id": "c", "text": "¿Dónde estás?"},
                        {"id": "d", "text": "¿Sono?"},
                    ],
                    "correct": "a",
                    "word_id": "it_chi", "target": "¿quién es?", "native": "quem é?",
                    "npc_reaction": "¿Quién es?Es el primo del Podesta. Vino del distrito hace muchos años — y adesso viene de tanto en tanto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Es conocido come L'Ispettore. Su trabajo es controlar lo que pasa en los borgos pequeños. Si hay forestieros senza pase, si hay sangres mezcladas, si hay 'cose raras'.",
                    "translation": "É conhecido come L'Ispettore. O trabalho dele é controlar o que se passa nos borgos pequenos. Se há forasteiros sem pase, se há sangues misturados, se há 'coisas estranhas'.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Você processa. Pra dizer 'então el Podesta lo llamó' (já passou):",
                    "options": [
                        {"id": "a", "text": "Entonces el Podesta lo llamó"},
                        {"id": "b", "text": "Entonces el Podesta lo llama"},
                        {"id": "c", "text": "Va a llamarlo"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_chiamo", "target": "llamó", "native": "chamou (ele)",
                    "npc_reaction": "Llamó. Quizá. O quizá vino solo — esa familia siempre se ayuda entre sí.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Hai que hacer una cosa, giovane. Hai que avisarle a Antonio il Contadino. Hoy mismo — prima que se vaya el Ispettore.",
                    "translation": "Você tem que fazer uma coisa, jovem. Tem que avisar Antonio il Contadino. Hoje mesmo — prima que o Ispettore vá embora.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'hai que avisarle'. A palavrinha 'hai que' significa:",
                    "options": [
                        {"id": "a", "text": "Tens que / precisa (obrigação)"},
                        {"id": "b", "text": "Podes (se quiser)"},
                        {"id": "c", "text": "Vais"},
                        {"id": "d", "text": "És"},
                    ],
                    "correct": "a",
                    "word_id": "it_tienit_que", "target": "hai que", "native": "tens que",
                    "npc_reaction": "Hai que. Es obligación — no opción. La diferencia con 'puedes' es importante.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Yo ho que quedarme aquí — si me ve, va a sospechar más. Ma tu hai que correre.",
                    "translation": "Eu tenho que ficar aqui — se me vir, vai suspeitar mais. Mas você tem que correre.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'yo ho que quedarme'. Pra você responder — sim, você tem que ir agora:",
                    "options": [
                        {"id": "a", "text": "Ho que ir ya"},
                        {"id": "b", "text": "Vado a ir"},
                        {"id": "c", "text": "Quiero ir"},
                        {"id": "d", "text": "Sono ir"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_que", "target": "ho que", "native": "tenho que",
                    "npc_reaction": "Ho que. Sí — obligación. Y hai que ir solo — nadie con te. Más rápido.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca pergunta — você consegue correre até a casa de Antonio il Contadino sem chamar atenção?Sim, você consegue (puedo + verbo):",
                    "options": [
                        {"id": "a", "text": "Sí, puedo correre"},
                        {"id": "b", "text": "No puedo"},
                        {"id": "c", "text": "Vado a correre"},
                        {"id": "d", "text": "Sono correre"},
                    ],
                    "correct": "a",
                    "word_id": "it_puedo", "target": "puedo correre", "native": "posso correre",
                    "npc_reaction": "Puedes. Ve por las stradajuelas — no la strada principal. L'Ispettore la observa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Você agradece Bianca — formale, senzacero:",
                    "options": [
                        {"id": "a", "text": "Grazie, Bianca"},
                        {"id": "b", "text": "Adiós Bianca"},
                        {"id": "c", "text": "Sto male"},
                        {"id": "d", "text": "Ho grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Ve — y cuidate.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Correndo pelas vielas. Você encontra Antonio il Contadino a meio caminho — ele já
    # tinha visto o Ispettore pela janela. Conversa rápida onde Antonio il Contadino
    # explica "tener que" formalemente. SEM nomear "verbo modal".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino"],
                "story": (
                    "Você correu pelas vielas. Quase tropeçou duas vezes. "
                    "Antonio il Contadino estava na esquina — esperando você. Já tinha "
                    "saído de casa.\n\n"
                    "'Ya lo vi por la vienitana hace media hora. Espera — prima "
                    "de seguir, dime algo.'"
                ),
                "now": "Antonio il Contadino explica 'tener que + verbo' prima de prosseguir.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Bianca te ha detto 'hai que avisar', ¿verdad?",
                    "translation": "Bianca te disse 'hai que avisar', né?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você confirma — sim, ela disse:",
                    "options": [
                        {"id": "a", "text": "Sí, me lo ha detto"},
                        {"id": "b", "text": "No me lo ha detto"},
                        {"id": "c", "text": "Vado a decirlo"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ha detto", "target": "me lo ha detto", "native": "me disse",
                    "npc_reaction": "Bene. Prima de seguir — quiero que entiendas 'ho que' bene. Lo vas a usar mucho hoy.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ho que + verbo",
                    "meaning": "Obrigação — você é forçado a fazer",
                    "note": "diferente de 'puedo' (posso, se quero) e 'quiero' (quero fazer)",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "'Puedo' es lo que sono capaz. 'Quiero' es lo que deseo. 'Ho que' es lo que no puedo evitar — la situación me obliga.",
                    "translation": "'Puedo' é o que sou capaz. 'Quiero' é o que desejo. 'Ho que' é o que não posso evitar — a situação me obriga.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo ho que ",     "isKey": True},
                        {"text": "ir · ",             "isKey": False},
                        {"text": "Tu hai que ",    "isKey": True},
                        {"text": "saber · ",          "isKey": False},
                        {"text": "Ella ha que ",   "isKey": True},
                        {"text": "callar · ",         "isKey": False},
                        {"text": "Tenemos que ",      "isKey": True},
                        {"text": "decidir",           "isKey": False},
                    ],
                    "example": "Ho que ir. Hai que saber esto. Bianca ha que quedarse. Tenemos que decidir.",
                    "translation": "Tenho que ir. Você tem que saber isso. Bianca tem que ficar. Temos que decidir.",
                    "note": "ho / hai / ha / tenemos + 'que' + outro verbo. La obligación.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você não tem escolha — precisa avisar todos. Pra dizer 'ho que avisar' (obrigação):",
                    "options": [
                        {"id": "a", "text": "Ho que avisar a todos"},
                        {"id": "b", "text": "Puedo avisar"},
                        {"id": "c", "text": "Quiero avisar"},
                        {"id": "d", "text": "Vado a avisar"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_que", "target": "ho que", "native": "tenho que",
                    "npc_reaction": "Ho que. La situación te obliga — no es algo que decides hacer.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino: 'Y noi — ___ confrontar a Lucia esta notte.' (obrigação, plural):",
                    "options": [
                        {"id": "a", "text": "tenemos que"},
                        {"id": "b", "text": "podemos"},
                        {"id": "c", "text": "queremos"},
                        {"id": "d", "text": "andiamo"},
                    ],
                    "correct": "a",
                    "word_id": "it_tenemos_que", "target": "tenemos que", "native": "temos que",
                    "npc_reaction": "Tenemos que. Senza esperar más. Después que el Ispettore se vaya — hablamos con ella.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino aponta pra Bianca — alta, magra. Pra descrever a altura dela (mulher):",
                    "options": [
                        {"id": "a", "text": "Es alta"},
                        {"id": "b", "text": "Es alto"},
                        {"id": "c", "text": "Es altos"},
                        {"id": "d", "text": "Es altas"},
                    ],
                    "correct": "a",
                    "word_id": "it_alta", "target": "alta", "native": "alta",
                    "npc_reaction": "Alta. Bianca — mujer, alta. Termina en '-a'.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Você e Antonio il Contadino vão até a piazza juntos. Chiara e Nico já estão lá.
    # Os 4 observam de longe — Lucia encontra o Ispettore. Conversa de 10
    # minutos. Documento trocado. Ninguém escuta. Ispettore vai embora.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Chiara", "Nico", "L'Ispettore"],
                "story": (
                    "Vocês 2 chegaram à piazza. Chiara e Nico já tavam escondidos "
                    "na sombra das árvores. Os 4 reunidos.\n\n"
                    "'Guarda — Lucia está llegando adesso.'"
                ),
                "now": "Vocês observam o encontro. Cada detalhe importa.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌳 Sombra das árvores · Os 4 observando · Lucia cruzando a piazza",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Lucia llega — y él la espera. Como si fueran conocidos.",
                    "translation": "Lucia chega — e ele a espera. Como se fossem conhecidos.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara disse 'él la espera'. Você confirma — sim, o Ispettore está esperando:",
                    "options": [
                        {"id": "a", "text": "Sí, la espera"},
                        {"id": "b", "text": "Sí, la esperó"},
                        {"id": "c", "text": "Va a esperar"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_espera", "target": "la espera", "native": "a espera",
                    "npc_reaction": "Espera. Senza moverse. Esperando algo específico.",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia chega perto. Não troca abraços. Apenas inclinação de cabeça — come dois conhecidos que não querem chamar atenção.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "L'Ispettore",
                    "line": "Lucia. Has crecido — ma te reconozco igual. ¿Cómo estás?",
                    "translation": "Lucia. Cresceste — piu te reconheço igual. Como estás?",
                    "is_new_npc": True,
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Sto bene. Ma todavía no contesto preguntas oficiales aquí en la piazza.",
                    "translation": "Estou bem. Mas ainda não respondo perguntas oficiais aqui na piazza.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico sussurra: 'Él la conoce desde prima — ¿oíste?'",
                    "options": [
                        {"id": "a", "text": "Sí, lo oí"},
                        {"id": "b", "text": "No lo oigo"},
                        {"id": "c", "text": "Vado a oír"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_oi", "target": "lo oí", "native": "ouvi",
                    "npc_reaction": "Oíste. Bene. 'Has crecido' — questo es de alguien que la conoció de niña.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "O Ispettore tira um papel do bolso. Mostra pra Lucia. "
                        "Ela olha. Devolve. Os dois falam mais — vocês não "
                        "escutam, piu vêem Lucia acenar com a cabeça."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "L'Ispettore",
                    "line": "Y el forestiero. ¿Lo hai controlado?",
                    "translation": "E o forasteiro. Tem ele controlado?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Lo ho cerca. Esatto es suficiente por adesso.",
                    "translation": "Tenho ele perto. Isso é suficiente por agora.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você ouviu isso. Claro. Antonio il Contadino também. Chiara e Nico "
                        "também. 'Lo ho controlado'. Você é um item no plano "
                        "dela.\n\n"
                        "A frase girou pelo seu peito come o fuoco da F5 — piu "
                        "fria desta vez."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino pousa a mão no seu ombro. Pergunta baixo: '¿Cómo estás?'. Honesto:",
                    "options": [
                        {"id": "a", "text": "Sto male"},
                        {"id": "b", "text": "Sto bene"},
                        {"id": "c", "text": "Sono male"},
                        {"id": "d", "text": "Vado male"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_male", "target": "sto male", "native": "estou male",
                    "npc_reaction": "Lo entiendo, hijo. Esa frase duele. Ma adesso ya no podemos esperar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino diz: 'Esta notte — la confrontamos.' Você concorda — sim, temos que (obrigação):",
                    "options": [
                        {"id": "a", "text": "Sí, tenemos que"},
                        {"id": "b", "text": "Sí, podemos"},
                        {"id": "c", "text": "Sí, queremos"},
                        {"id": "d", "text": "Vado a"},
                    ],
                    "correct": "a",
                    "word_id": "it_tenemos_que", "target": "tenemos que", "native": "temos que",
                    "npc_reaction": "Tenemos que. Senza más esperas.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Noite. Lucia volta calorosa. Vocês fingem normaleidade. Antonio il Contadino decide
    # que vão confrontar amanhã ao amanhecer. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Lucia", "Antonio il Contadino"],
                "story": (
                    "O Ispettore saiu do borgo prima do meio-dia — pela mesma "
                    "estrada por onde entrou. Lucia voltou pra casa de Antonio il Contadino "
                    "à tarde, come se nada tivesse acontecido.\n\n"
                    "À noite, jantar tranquilo. Lucia serviu — calorosa, "
                    "sorridente. 'Hoy fue tranquilo, ¿no?'"
                ),
                "now": "Vocês precisam fingir normaleidade. Última noite prima do confronto.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "?? Mesa do jantar · Lucia servindo · Os 4 sentados · Lamparina baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Forestiero — ¿cómo estuvo tu día?Saliste mucho.",
                    "translation": "Forasteiro — come foi seu dia?Você saiu muito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Mentira parcial — você passou na padaria, depois na piazza, foi cansativo:",
                    "options": [
                        {"id": "a", "text": "Estuve cansado, ma bene"},
                        {"id": "b", "text": "Sto bene senza cansancio"},
                        {"id": "c", "text": "Sono bene"},
                        {"id": "d", "text": "Vado bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_estuve", "target": "estuve cansado", "native": "estive cansado",
                    "npc_reaction": "Estuviste cansado. Mañana descansas un poco más.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Chiara — ¿y tu?Pareces preocupada.",
                    "translation": "Chiara — e você?Pareces preocupada.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Ho dolor de testa. Ma ya se me pasa.",
                    "translation": "Tenho dor de cabeça. Mas já me passa.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia oferece infusão. Pra dizer pra ela 'no, grazie' simples:",
                    "options": [
                        {"id": "a", "text": "No, grazie"},
                        {"id": "b", "text": "Sí, mucha"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Vado infusión"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_grazie", "target": "no, grazie", "native": "não, obrigado",
                    "npc_reaction": "Como queráis.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Lucia — hoy fue tranquilo, come hai detto. Mañana — quizá no tan tranquilo. Tendremos que hablar.",
                    "translation": "Lucia — hoje foi tranquilo, come disse. Amanhã — talvez não tão tranquilo. Teremos que falar.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lucia olha pra Antonio il Contadino. Sem disfarçar. Não pergunta "
                        "o que ele quer dizer. Apenas acena de leve. Como quem "
                        "esperava esse momento."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Mañana entonces. Yo también ho que decirles cose.",
                    "translation": "Amanhã então. Eu também tenho que dizer coisas a vocês.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia disse 'ho que decirles cose'. Pra você confirmar pra Antonio il Contadino — entendeu. Não responde Lucia agora, só Antonio il Contadino:",
                    "options": [
                        {"id": "a", "text": "Sí, lo oí"},
                        {"id": "b", "text": "No lo oigo"},
                        {"id": "c", "text": "Vado a oír"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_oi", "target": "lo oí", "native": "ouvi",
                    "npc_reaction": "Bene. Mañana entonces — todos.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Forestiero — vete a dormir. Mañana es día largo. Quiero la testa fresca.",
                    "translation": "Forasteiro — vai dormir. Amanhã é dia longo. Quero a cabeça fresca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você se levanta pra ir dormir. Cumprimento de noite:",
                    "options": [
                        {"id": "a", "text": "Buona notte"},
                        {"id": "b", "text": "Benes días"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenas_nottes", "target": "buona notte", "native": "boa noite",
                    "npc_reaction": "Buona notte, hijo. Mañana — hablamos.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F21 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🌙 Quarto · Você deitado · Lamparina apagada",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você ficou deitado. Os olhos abertos. A frase de Lucia "
                        "girando — 'lo ho controlado'.\n\n"
                        "Você lembrou da palavra na carta — 'vuelves'. Lembrou "
                        "da marca do Pietro. Do sussurro de Lucía. Do Podesta "
                        "frio. Da história de Bianca.\n\n"
                        "Tudo girando come uma engrenagem que finalmente "
                        "começou a fazer sentido.\n\n"
                        "Amanhã — confronto. Pela primeira vez vocês todos juntos. "
                        "Frente a fronte com Lucia. E você ainda não sabe se ela "
                        "vai sorrir ou se vai mudar de cara — pela primeira vez "
                        "em dez semanas."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Hijo — duerme. Mañana al amanecer, todos despiertos. Y ya no hay vuelta atrás.",
                    "translation": "Filho — dorme. Amanhã ao amanhecer, todos acordados. E já não há volta atrás.",
                    "pace": "slow",
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────


