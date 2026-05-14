"""
Seed das 6 seções da Fase 21 Espanhol A1 — "El confronto a María".

Continuação direta da F20. Amanhecer. María estava sentada na cadeira
da casa de hóspedes — esperando o grupo. Não foge. Não nega. Mas
também não revela o nome verdadeiro. 'Cuando puedan saber, sabrán.'

Vocab novo (2): cuando · verdad
Linguagem nova: cuando + verbo  (tempo condicional simples)
    "Cuando puedan, sabrán." / "Cuando llegue, hablamos."

Revisão F1-F20 dominante.

Item dinâmica: 1 item_moment — Hierba de María (epico). Se o player
tem na mochila (do baú F15+), pode usar pra "calmar" María e ganhar
mais informação. Se não tem, ela ainda revela parte.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f21_sections [--reset]
"""

SECTIONS = [
    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene",     "text": "🌄 Casa de hóspedes · Amanhecer · María sentada esperando"},
                {"kind": "npc",       "npc": "María", "line": "Sé por qué viniste. Hace días que sé.", "pace": "slow"},
                {"kind": "player",    "text": "Sofía atrás de você. Miguel atrás dela. Don Miguel na porta. Cinco contra uma — mas a vantagem real está toda do lado dela."},
                {"kind": "npc",       "npc": "María", "line": "Pregúntame lo que quieras. Yo decido qué contesto.", "pace": "slow"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "cuando", "native": "quando"},
                    {"target": "verdad", "native": "verdade"},
                    {"target": "saber",  "native": "saber"},
                ]},
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você cumprimenta — manhã, formal:",
                    "options": [
                        {"id": "a", "text": "Buenos días, María"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. Empieza tú.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María disse 'cuando puedan saber, sabrán'. Pra você reagir — você ainda não sabe (todavía + no):",
                    "options": [
                        {"id": "a", "text": "Todavía no sé"},
                        {"id": "b", "text": "Ya sé todo"},
                        {"id": "c", "text": "Voy a saber"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Pero algunos pedazos puedo darte hoy.",
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
                "characters": ["María"],
                "story": "María quer ouvir o que VOCÊS sabem antes de revelar o que ELA sabe. Faz perguntas — vocês respondem.",
                "now": "Revisão completa. Cada resposta tua precisa ser direta.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "María", "line": "¿Cómo te llamas?", "translation": "Como você se chama?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Me llamo [seu nome]"},
                     {"id": "b", "text": "Soy forastero"},
                     {"id": "c", "text": "Tengo años"},
                     {"id": "d", "text": "Adiós"},
                 ], "correct": "a",
                 "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                 "npc_reaction": "Bien."},
                {"kind": "npc_speak", "npc": "María", "line": "¿Cuántos años tienes?", "translation": "Quantos anos você tem?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Idade:",
                 "options": [
                     {"id": "a", "text": "Tengo veinte años"},
                     {"id": "b", "text": "Soy veinte"},
                     {"id": "c", "text": "Estoy veinte"},
                     {"id": "d", "text": "Voy veinte"},
                 ], "correct": "a",
                 "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                 "npc_reaction": "Veinte."},
                {"kind": "npc_speak", "npc": "María", "line": "¿Y qué viste — la noche del fuego? Cuéntamelo en pasado.", "translation": "E o que você viu — a noite do fogo? Conta no passado.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Você viu fogo. Pretérito 1ª pessoa de ver:",
                 "options": [
                     {"id": "a", "text": "Vi fuego"},
                     {"id": "b", "text": "Veo fuego"},
                     {"id": "c", "text": "Voy a ver"},
                     {"id": "d", "text": "Soy fuego"},
                 ], "correct": "a",
                 "word_id": "es_vi", "target": "vi", "native": "vi",
                 "npc_reaction": "Vi. Yo también lo vi, esa noche — desde lejos."},
                {"kind": "npc_speak", "npc": "María", "line": "¿Y la carta de Don Miguel — qué palabra leíste?", "translation": "E a carta de Don Miguel — que palavra você leu?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "A palavra que ficou clara no centro da carta:",
                 "options": [
                     {"id": "a", "text": "Vuelves"},
                     {"id": "b", "text": "Forastero"},
                     {"id": "c", "text": "Buenos días"},
                     {"id": "d", "text": "Vi"},
                 ], "correct": "a",
                 "word_id": "es_vuelves", "target": "vuelves", "native": "você volta",
                 "npc_reaction": "Vuelves. Sí. Esa palabra te lleva al pasado — al sitio que tu cabeza no recuerda."},
                {"kind": "npc_speak", "npc": "María", "line": "¿Y ahora — cómo estás con todo esto?", "translation": "E agora — como você está com tudo isso?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Honesto — confuso mas firme:",
                 "options": [
                     {"id": "a", "text": "Estoy bien, pero confundido"},
                     {"id": "b", "text": "Soy bien"},
                     {"id": "c", "text": "Tengo bien"},
                     {"id": "d", "text": "Voy bien"},
                 ], "correct": "a",
                 "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                 "npc_reaction": "Confundido es normal. Yo también lo estuve cuando tenía tu edad y supe lo que pertenecía a mi familia."},
            ],
        },
    },

    # ── Seção 3: Prática Aplicada — item_moment com Hierba de María ──────────
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["María"],
                "story": "María se levantou. Acendeu o fogão. Vai fazer chá — mas pede um momento sozinha com você. Sofía e Miguel saem.",
                "now": "Conversa íntima. María pede algo — e você pode oferecer um item da mochila.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "María", "line": "Me cansé. Llevo dos meses fingiendo. Si tienes algo en la bolsa — una hierba, algo — me ayudaría a hablar más fácil.", "translation": "Me cansei. Faz dois meses fingindo. Se você tem algo na mochila — uma erva, algo — me ajudaria a falar mais fácil.", "pace": "slow"},
                {
                    "kind": "item_moment",
                    "npc": "María",
                    "situation": "María estende a mão aberta. Cansada como nunca esteve.",
                    "npc_line": "¿Tienes algún remedio o hierba? Si no — no importa.",
                    "item_tag": "remedio",
                    "on_use": {
                        "narrative": "Você tira a Hierba de María do bolso. Coloca na mão dela. Os olhos dela amoleceram um instante.",
                        "npc_reaction": "Mi propia hierba. Curioso — pero gracias. Voy a contar más de lo que pensaba.",
                        "bonus": "extra_dialogue",
                    },
                    "on_skip": {
                        "npc_reaction": "Está bien. Voy a hablar igual — pero menos.",
                    },
                },
                {"kind": "npc_speak", "npc": "María", "line": "Yo no me llamo María. Mi apellido era Sangra — Eduardo lo adivinó.", "translation": "Eu não me chamo María. Meu sobrenome era Sangra — Eduardo adivinhou.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Você processa. Pergunta direta: 'E qual é teu nome verdadeiro?' Como você pergunta?",
                 "options": [
                     {"id": "a", "text": "¿Cuál es tu nombre verdadero?"},
                     {"id": "b", "text": "¿Cómo estás?"},
                     {"id": "c", "text": "¿Cuántos años?"},
                     {"id": "d", "text": "¿Tú vienes?"},
                 ], "correct": "a",
                 "word_id": "es_cual", "target": "¿cuál?", "native": "qual?",
                 "npc_reaction": "Eso preguntará Don Miguel mañana en otro tono. Hoy te respondo: cuando esté segura de que están seguros — te lo digo. No antes."},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "María disse 'cuando esté segura...'. A palavra 'cuando' significa:",
                 "options": [
                     {"id": "a", "text": "Quando (no momento que)"},
                     {"id": "b", "text": "Onde"},
                     {"id": "c", "text": "Por quê"},
                     {"id": "d", "text": "Quem"},
                 ], "correct": "a",
                 "word_id": "es_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando. Marca tiempo de condición — algo va a pasar, pero no ahora."},
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa — cuando + verbo ─────────────────────────
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["María"],
                "story": "María serviu chá. Sentou na sua frente. Decidiu mostrar uma coisa que os Buscadores ensinavam — como falar do que ainda não aconteceu mas vai.",
                "now": "María explica 'cuando + verbo' — quando você quer falar de algo condicional.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "María", "line": "Cuando llegue el día — voy a contarte todo. Cuando puedas leer la carta entera — entenderás. La palabra es 'cuando'.", "translation": "Quando chegar o dia — vou te contar tudo. Quando você puder ler a carta inteira — entenderás. A palavra é 'cuando'.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Cuando + verbo", "meaning": "Quando (algo acontecer)", "note": "marca uma condição no futuro — o que vai acontecer DEPENDE disso acontecer primeiro"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Cuando ",        "isKey": True},
                     {"text": "llegue · ",      "isKey": False},
                     {"text": "Cuando ",        "isKey": True},
                     {"text": "puedas · ",      "isKey": False},
                     {"text": "Cuando ",        "isKey": True},
                     {"text": "sepas",          "isKey": False},
                 ],
                 "example": "Cuando llegue el día, hablamos. Cuando puedas leer, entenderás.",
                 "translation": "Quando chegar o dia, falamos. Quando você puder ler, entenderás.",
                 "note": "cuando + verbo do futuro condicional — espera o momento certo."},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Pra dizer 'quando você puder, falamos':",
                 "options": [
                     {"id": "a", "text": "Cuando puedas, hablamos"},
                     {"id": "b", "text": "Puedes hablamos"},
                     {"id": "c", "text": "Voy hablamos"},
                     {"id": "d", "text": "Soy hablamos"},
                 ], "correct": "a",
                 "word_id": "es_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando puedas. Eso es."},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Pra dizer 'quando chegar a hora, sabe':",
                 "options": [
                     {"id": "a", "text": "Cuando llegue la hora, sabrás"},
                     {"id": "b", "text": "Llega la hora sabrás"},
                     {"id": "c", "text": "Sabes la hora"},
                     {"id": "d", "text": "Soy hora"},
                 ], "correct": "a",
                 "word_id": "es_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando llegue. Esperar es la mitad del trabajo."},
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel", "Don Miguel"],
                "story": "Sofía e Miguel voltaram. Don Miguel também. María convida todos a sentar.",
                "now": "Conversa de fechamento. María dá uma pista a mais — só uma.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "María", "line": "Una cosa más antes de que se vayan. Hay alguien en el norte — que sabe quién es el forastero.", "translation": "Uma coisa antes de vocês irem. Tem alguém no norte — que sabe quem é o forasteiro.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Don Miguel reage. Pra você confirmar pra María que entendeu (já passou — 'oí'):",
                 "options": [
                     {"id": "a", "text": "Lo oí"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Voy a oír"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_oi", "target": "oí", "native": "ouvi",
                 "npc_reaction": "Oíste. Cuando termine todo aquí — vayan al norte. Encuentren a esa persona."},
                {"kind": "npc_speak", "npc": "Sofía", "line": "¿Quién es?", "translation": "Quem é?", "pace": "urgent"},
                {"kind": "npc_speak", "npc": "María", "line": "Cuando vayan, lo sabrán. Hoy no es el día.", "translation": "Quando forem, saberão. Hoje não é o dia.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Você concorda — vão quando puderem (futuro próximo plural):",
                 "options": [
                     {"id": "a", "text": "Vamos a ir"},
                     {"id": "b", "text": "Voy a ir"},
                     {"id": "c", "text": "Va a ir"},
                     {"id": "d", "text": "Soy ir"},
                 ], "correct": "a",
                 "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                 "npc_reaction": "Vamos. Pero antes — el Alcalde. Algo va a venir."},
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": "María terminou. Vocês saíram da casa de hóspedes em silêncio. Carmen estava na esquina — esperando.",
                "now": "Decisão difícil sobre como agir nos próximos dias. Errar trava.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "Carmen", "line": "Vi al Inspector hace una hora — volvió al pueblo con tres hombres uniformados.", "translation": "Vi El Inspector há uma hora — voltou ao pueblo com três homens uniformizados.", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Você confirma — ouviu sim:",
                 "options": [
                     {"id": "a", "text": "Lo oí"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Voy a oír"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_oi", "target": "oí", "native": "ouvi",
                 "npc_reaction": "Oíste. Cuando vengan a por ti — y van a venir — yo estaré allí.", "gated": True},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Você agradece formal pela ajuda dela:",
                 "options": [
                     {"id": "a", "text": "Gracias, Carmen"},
                     {"id": "b", "text": "Adiós Carmen"},
                     {"id": "c", "text": "Mal Carmen"},
                     {"id": "d", "text": "Voy Carmen"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "De nada. Cuando esto acabe — y vamos a terminar bien — me cuentas todo.", "gated": True},
                {"kind": "scene", "text": "🌅 Plaza · Sol já alto · El Inspector visto ao longe atravessando a praça"},
                {"kind": "narrative", "text": "Vocês voltaram pra casa de Don Miguel. Don Miguel pegou a carta do baú. Sofía pegou faca. Miguel trancou portas. María sentou na cadeira da cozinha — esperando."},
            ],
        },
    },
]
