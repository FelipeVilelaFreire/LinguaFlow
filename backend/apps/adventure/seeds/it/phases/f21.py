"""
Seed das 6 seções da Fase 21 Italiano A1 — "El confronto a Lucia".

Continuação direta da F20. Amanhecer. Lucia estava sentada na cadeira
da casa de hóspedes — esperando o grupo. Não foge. Não nega. Mas
também não revela o nome verdadeiro. 'Cuando puedan saber, sabrán.'

Vocab novo (2): cuando · verdad
Linguagem nova: cuando + verbo  (tempo condicional simples)
    "Cuando puedan, sabrán." / "Cuando arrivi, hablamos."

Revisão F1-F20 dominante.

Item dinâmica: 1 item_moment — Hierba de Lucia (epico). Se o player
tem na mochila (do baú F15+), pode usar pra "calmar" Lucia e ganhar
mais informação. Se não tem, ela ainda revela parte.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [
    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene",     "text": "🌄 Casa de hóspedes · Amanhecer · Lucia sentada esperando"},
                {"kind": "npc",       "npc": "Lucia", "line": "Sé por qué viniste. Hace días que sé.", "pace": "slow"},
                {"kind": "player",    "text": "Chiara atrás de você. Nico atrás dela. Antonio il Contadino na porta. Cinco contra uma — piu a vantagem real está toda do lado dela."},
                {"kind": "npc",       "npc": "Lucia", "line": "Pregúntame lo que quieras. Yo decido qué contesto.", "pace": "slow"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "cuando", "native": "quando"},
                    {"target": "verdad", "native": "verdade"},
                    {"target": "saber",  "native": "saber"},
                ]},
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você cumprimenta — manhã, formale:",
                    "options": [
                        {"id": "a", "text": "Benes días, Lucia"},
                        {"id": "b", "text": "Buona notte"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Benes días. Empieza tu.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia disse 'cuando puedan saber, sabrán'. Pra você reagir — você ainda não sabe (todavía + no):",
                    "options": [
                        {"id": "a", "text": "Todavía no sé"},
                        {"id": "b", "text": "Ya sé todo"},
                        {"id": "c", "text": "Vado a saber"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ancora_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Ma algunos pedazos puedo darte hoy.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS — 100% revisão ──────────────────────────────────
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Lucia"],
                "story": "Lucia quer ouvir o que VOCÊS sabem prima de revelar o que ELA sabe. Faz perguntas — vocês respondem.",
                "now": "Revisão completa. Cada resposta tua precisa ser direta.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "Lucia", "line": "¿Cómo te chiami?", "translation": "Como você se chama?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Mi chiamo [seu nome]"},
                     {"id": "b", "text": "Sono forestiero"},
                     {"id": "c", "text": "Ho años"},
                     {"id": "d", "text": "Adiós"},
                 ], "correct": "a",
                 "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                 "npc_reaction": "Bene."},
                {"kind": "npc_speak", "npc": "Lucia", "line": "¿Cuántos años hai?", "translation": "Quantos anni você tem?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Idade:",
                 "options": [
                     {"id": "a", "text": "Ho veinte años"},
                     {"id": "b", "text": "Sono veinte"},
                     {"id": "c", "text": "Sto veinte"},
                     {"id": "d", "text": "Vado veinte"},
                 ], "correct": "a",
                 "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                 "npc_reaction": "Veinte."},
                {"kind": "npc_speak", "npc": "Lucia", "line": "¿Y qué viste — la notte del fuoco?Cuéntamelo en pasado.", "translation": "E o que você viu — a noite do fogo?Conta no passado.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Você viu fogo. Pretérito 1ª pessoa de ver:",
                 "options": [
                     {"id": "a", "text": "Vi fuoco"},
                     {"id": "b", "text": "Veo fuoco"},
                     {"id": "c", "text": "Vado a ver"},
                     {"id": "d", "text": "Sono fuoco"},
                 ], "correct": "a",
                 "word_id": "it_vi", "target": "vi", "native": "vi",
                 "npc_reaction": "Vi. Yo también lo vi, esa notte — desde lejos."},
                {"kind": "npc_speak", "npc": "Lucia", "line": "¿Y la carta de Antonio il Contadino — qué palabra leíste?", "translation": "E a carta de Antonio il Contadino — que palavra você leu?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "A palavra que ficou clara no centro da carta:",
                 "options": [
                     {"id": "a", "text": "Vuelves"},
                     {"id": "b", "text": "Forestiero"},
                     {"id": "c", "text": "Benes días"},
                     {"id": "d", "text": "Vi"},
                 ], "correct": "a",
                 "word_id": "it_vuelves", "target": "vuelves", "native": "você volta",
                 "npc_reaction": "Vuelves. Sí. Esa palabra te lleva al pasado — al sitio que tu testa no recuerda."},
                {"kind": "npc_speak", "npc": "Lucia", "line": "¿Y adesso — cómo estás con todo esto?", "translation": "E agora — come você está com tudo isso?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Honesto — confuso piu firme:",
                 "options": [
                     {"id": "a", "text": "Sto bene, ma confundido"},
                     {"id": "b", "text": "Sono bene"},
                     {"id": "c", "text": "Ho bene"},
                     {"id": "d", "text": "Vado bene"},
                 ], "correct": "a",
                 "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                 "npc_reaction": "Confundido es normale. Yo también lo estuve cuando tenía tu edad y supe lo que pertenecía a mi familia."},
            ],
        },
    },

    # ── Seção 3: Prática Aplicada — item_moment com Hierba de Lucia ──────────
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Lucia"],
                "story": "Lucia se levantou. Acendeu o fogão. Vai fazer chá — piu pede um momento sozinha com você. Chiara e Nico saem.",
                "now": "Conversa íntima. Lucia pede algo — e você pode oferecer um item da mochila.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "Lucia", "line": "Me cansé. Llevo dos meses fingiendo. Si hai algo en la bolsa — una hierba, algo — me ayudaría a hablar más fácil.", "translation": "Me cansei. Faz dois meses fingindo. Se você tem algo na mochila — uma erva, algo — me ajudaria a falar mais fácil.", "pace": "slow"},
                {
                    "kind": "item_moment",
                    "npc": "Lucia",
                    "situation": "Lucia estende a mão aberta. Cansada come nunca esteve.",
                    "npc_line": "¿Hai algún remedio o hierba?Si no — no importa.",
                    "item_tag": "remedio",
                    "on_use": {
                        "narrative": "Você tira a Hierba de Lucia do bolso. Coloca na mão dela. Os olhos dela amoleceram um instante.",
                        "npc_reaction": "Mi propia hierba. Curioso — ma grazie. Vado a contar más de lo que pensaba.",
                        "bonus": "extra_dialogue",
                    },
                    "on_skip": {
                        "npc_reaction": "Está bene. Vado a hablar igual — ma menos.",
                    },
                },
                {"kind": "npc_speak", "npc": "Lucia", "line": "Yo no mi chiamo Lucia. Mi apellido era Sangra — Pietro lo adivinó.", "translation": "Eu não me chamo Lucia. Meu sobrenome era Sangra — Pietro adivinhou.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Você processa. Pergunta direta: 'E qual é teu nome verdadeiro?' Como você pergunta?",
                 "options": [
                     {"id": "a", "text": "¿Cuál es tu nombre verdadero?"},
                     {"id": "b", "text": "¿Cómo estás?"},
                     {"id": "c", "text": "¿Cuántos años?"},
                     {"id": "d", "text": "¿Tu vieni?"},
                 ], "correct": "a",
                 "word_id": "it_cual", "target": "¿cuál?", "native": "qual?",
                 "npc_reaction": "Esatto preguntará Antonio il Contadino mañana en otro tono. Hoy te respondo: cuando esté segura de que están seguros — te lo digo. No prima."},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Lucia disse 'cuando esté segura...'. A palavra 'cuando' significa:",
                 "options": [
                     {"id": "a", "text": "Quando (no momento que)"},
                     {"id": "b", "text": "Onde"},
                     {"id": "c", "text": "Por quê"},
                     {"id": "d", "text": "Quem"},
                 ], "correct": "a",
                 "word_id": "it_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando. Marca tiempo de condición — algo va a pasar, ma no adesso."},
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa — cuando + verbo ─────────────────────────
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Lucia"],
                "story": "Lucia serviu chá. Sentou na sua fronte. Decidiu mostrar uma coisa que os Buscadores ensenzaavam — come falar do que ainda não aconteceu piu vai.",
                "now": "Lucia explica 'cuando + verbo' — quando você quer falar de algo condicional.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "Lucia", "line": "Cuando arrivi el día — vado a contarte todo. Cuando puedas leer la carta entera — entenderás. La palabra es 'cuando'.", "translation": "Quando chegar o dia — vou te contar tudo. Quando você puder ler a carta inteira — entenderás. A palavra é 'cuando'.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Cuando + verbo", "meaning": "Quando (algo acontecer)", "note": "marca uma condição no futuro — o que vai acontecer DEPENDE disso acontecer primeiro"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Cuando ",        "isKey": True},
                     {"text": "arrivi · ",      "isKey": False},
                     {"text": "Cuando ",        "isKey": True},
                     {"text": "puedas · ",      "isKey": False},
                     {"text": "Cuando ",        "isKey": True},
                     {"text": "sepas",          "isKey": False},
                 ],
                 "example": "Cuando arrivi el día, hablamos. Cuando puedas leer, entenderás.",
                 "translation": "Quando chegar o dia, falamos. Quando você puder ler, entenderás.",
                 "note": "cuando + verbo do futuro condicional — espera o momento certo."},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Pra dizer 'quando você puder, falamos':",
                 "options": [
                     {"id": "a", "text": "Cuando puedas, hablamos"},
                     {"id": "b", "text": "Puedes hablamos"},
                     {"id": "c", "text": "Vado hablamos"},
                     {"id": "d", "text": "Sono hablamos"},
                 ], "correct": "a",
                 "word_id": "it_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando puedas. Esatto es."},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Pra dizer 'quando chegar a hora, sabe':",
                 "options": [
                     {"id": "a", "text": "Cuando arrivi la hora, sabrás"},
                     {"id": "b", "text": "Llega la hora sabrás"},
                     {"id": "c", "text": "Sabes la hora"},
                     {"id": "d", "text": "Sono hora"},
                 ], "correct": "a",
                 "word_id": "it_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando arrivi. Esperar es la mitad del trabajo."},
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico", "Antonio il Contadino"],
                "story": "Chiara e Nico voltaram. Antonio il Contadino também. Lucia convida todos a sentar.",
                "now": "Conversa de fechamento. Lucia dá uma pista a mais — só uma.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "Lucia", "line": "Una cosa más prima de que se vayan. Hay alguien en el norte — que sabe quién es el forestiero.", "translation": "Uma coisa prima de vocês irem. Tem alguém no norte — que sabe quem é o forasteiro.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Antonio il Contadino reage. Pra você confirmar pra Lucia que entendeu (já passou — 'oí'):",
                 "options": [
                     {"id": "a", "text": "Lo oí"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Vado a oír"},
                     {"id": "d", "text": "Sono"},
                 ], "correct": "a",
                 "word_id": "it_oi", "target": "oí", "native": "ouvi",
                 "npc_reaction": "Oíste. Cuando termine todo aquí — vayan al norte. Encuentren a esa persona."},
                {"kind": "npc_speak", "npc": "Chiara", "line": "¿Quién es?", "translation": "Quem é?", "pace": "urgent"},
                {"kind": "npc_speak", "npc": "Lucia", "line": "Cuando vayan, lo sabrán. Hoy no es el día.", "translation": "Quando forem, saberão. Hoje não é o dia.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Você concorda — vão quando puderem (futuro próximo plural):",
                 "options": [
                     {"id": "a", "text": "Andiamo a ir"},
                     {"id": "b", "text": "Vado a ir"},
                     {"id": "c", "text": "Va a ir"},
                     {"id": "d", "text": "Sono ir"},
                 ], "correct": "a",
                 "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                 "npc_reaction": "Andiamo. Ma prima — el Podesta. Algo va a venire."},
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": "Lucia terminou. Vocês saíram da casa de hóspedes em silêncio. Bianca estava na esquina — esperando.",
                "now": "Decisão difícil sobre come agir nos próximos dias. Errar trava.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "Bianca", "line": "Vi al Ispettore hace una hora — volvió al borgo con tres hombres uniformados.", "translation": "Vi L'Ispettore há uma hora — voltou ao borgo com três homens uniformizados.", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Você confirma — ouviu sim:",
                 "options": [
                     {"id": "a", "text": "Lo oí"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Vado a oír"},
                     {"id": "d", "text": "Sono"},
                 ], "correct": "a",
                 "word_id": "it_oi", "target": "oí", "native": "ouvi",
                 "npc_reaction": "Oíste. Cuando vienigan a por ti — y van a venire — yo estaré allí.", "gated": True},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Você agradece formale pela ajuda dela:",
                 "options": [
                     {"id": "a", "text": "Grazie, Bianca"},
                     {"id": "b", "text": "Adiós Bianca"},
                     {"id": "c", "text": "Male Bianca"},
                     {"id": "d", "text": "Vado Bianca"},
                 ], "correct": "a",
                 "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                 "npc_reaction": "De nada. Cuando esto acabe — y andiamo a terminar bene — me cuentas todo.", "gated": True},
                {"kind": "scene", "text": "🌅 Piazza · Sol já alto · L'Ispettore visto ao longe atravessando a praça"},
                {"kind": "narrative", "text": "Vocês voltaram pra casa de Antonio il Contadino. Antonio il Contadino pegou a carta do baú. Chiara pegou faca. Nico trancou portas. Lucia sentou na cadeira da cozinha — esperando."},
            ],
        },
    },
]


