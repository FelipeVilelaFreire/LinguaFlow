"""
Seed das 6 seÃ§Ãµes da Fase 21 Espanhol A1 â€” "El confronto a MarÃ­a".

ContinuaÃ§Ã£o direta da F20. Amanhecer. MarÃ­a estava sentada na cadeira
da casa de hÃ³spedes â€” esperando o grupo. NÃ£o foge. NÃ£o nega. Mas
tambÃ©m nÃ£o revela o nome verdadeiro. 'Cuando puedan saber, sabrÃ¡n.'

Vocab novo (2): cuando Â· verdad
Linguagem nova: cuando + verbo  (tempo condicional simples)
    "Cuando puedan, sabrÃ¡n." / "Cuando llegue, hablamos."

RevisÃ£o F1-F20 dominante.

Item dinÃ¢mica: 1 item_moment â€” Hierba de MarÃ­a (epico). Se o player
tem na mochila (do baÃº F15+), pode usar pra "calmar" MarÃ­a e ganhar
mais informaÃ§Ã£o. Se nÃ£o tem, ela ainda revela parte.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f21_sections [--reset]
"""

SECTIONS = [
    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene",     "text": "ðŸŒ„ Casa de hÃ³spedes Â· Amanhecer Â· MarÃ­a sentada esperando"},
                {"kind": "npc",       "npc": "MarÃ­a", "line": "SÃ© por quÃ© viniste. Hace dÃ­as que sÃ©.", "pace": "slow"},
                {"kind": "player",    "text": "SofÃ­a atrÃ¡s de vocÃª. Miguel atrÃ¡s dela. Don Miguel na porta. Cinco contra uma â€” mas a vantagem real estÃ¡ toda do lado dela."},
                {"kind": "npc",       "npc": "MarÃ­a", "line": "PregÃºntame lo que quieras. Yo decido quÃ© contesto.", "pace": "slow"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "cuando", "native": "quando"},
                    {"target": "verdad", "native": "verdade"},
                    {"target": "saber",  "native": "saber"},
                ]},
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª cumprimenta â€” manhÃ£, formal:",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, MarÃ­a"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. Empieza tÃº.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a disse 'cuando puedan saber, sabrÃ¡n'. Pra vocÃª reagir â€” vocÃª ainda nÃ£o sabe (todavÃ­a + no):",
                    "options": [
                        {"id": "a", "text": "TodavÃ­a no sÃ©"},
                        {"id": "b", "text": "Ya sÃ© todo"},
                        {"id": "c", "text": "Voy a saber"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavÃ­a no", "native": "ainda nÃ£o",
                    "npc_reaction": "TodavÃ­a no. Pero algunos pedazos puedo darte hoy.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â€” 100% revisÃ£o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["MarÃ­a"],
                "story": "MarÃ­a quer ouvir o que VOCÃŠS sabem antes de revelar o que ELA sabe. Faz perguntas â€” vocÃªs respondem.",
                "now": "RevisÃ£o completa. Cada resposta tua precisa ser direta.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Â¿CÃ³mo te llamas?", "translation": "Como vocÃª se chama?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Me llamo [seu nome]"},
                     {"id": "b", "text": "Soy forastero"},
                     {"id": "c", "text": "Tengo aÃ±os"},
                     {"id": "d", "text": "AdiÃ³s"},
                 ], "correct": "a",
                 "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                 "npc_reaction": "Bien."},
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Â¿CuÃ¡ntos aÃ±os tienes?", "translation": "Quantos anos vocÃª tem?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Idade:",
                 "options": [
                     {"id": "a", "text": "Tengo veinte aÃ±os"},
                     {"id": "b", "text": "Soy veinte"},
                     {"id": "c", "text": "Estoy veinte"},
                     {"id": "d", "text": "Voy veinte"},
                 ], "correct": "a",
                 "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                 "npc_reaction": "Veinte."},
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Â¿Y quÃ© viste â€” la noche del fuego? CuÃ©ntamelo en pasado.", "translation": "E o que vocÃª viu â€” a noite do fogo? Conta no passado.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "VocÃª viu fogo. PretÃ©rito 1Âª pessoa de ver:",
                 "options": [
                     {"id": "a", "text": "Vi fuego"},
                     {"id": "b", "text": "Veo fuego"},
                     {"id": "c", "text": "Voy a ver"},
                     {"id": "d", "text": "Soy fuego"},
                 ], "correct": "a",
                 "word_id": "es_vi", "target": "vi", "native": "vi",
                 "npc_reaction": "Vi. Yo tambiÃ©n lo vi, esa noche â€” desde lejos."},
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Â¿Y la carta de Don Miguel â€” quÃ© palabra leÃ­ste?", "translation": "E a carta de Don Miguel â€” que palavra vocÃª leu?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "A palavra que ficou clara no centro da carta:",
                 "options": [
                     {"id": "a", "text": "Vuelves"},
                     {"id": "b", "text": "Forastero"},
                     {"id": "c", "text": "Buenos dÃ­as"},
                     {"id": "d", "text": "Vi"},
                 ], "correct": "a",
                 "word_id": "es_vuelves", "target": "vuelves", "native": "vocÃª volta",
                 "npc_reaction": "Vuelves. SÃ­. Esa palabra te lleva al pasado â€” al sitio que tu cabeza no recuerda."},
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Â¿Y ahora â€” cÃ³mo estÃ¡s con todo esto?", "translation": "E agora â€” como vocÃª estÃ¡ com tudo isso?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Honesto â€” confuso mas firme:",
                 "options": [
                     {"id": "a", "text": "Estoy bien, pero confundido"},
                     {"id": "b", "text": "Soy bien"},
                     {"id": "c", "text": "Tengo bien"},
                     {"id": "d", "text": "Voy bien"},
                 ], "correct": "a",
                 "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                 "npc_reaction": "Confundido es normal. Yo tambiÃ©n lo estuve cuando tenÃ­a tu edad y supe lo que pertenecÃ­a a mi familia."},
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â€” item_moment com Hierba de MarÃ­a â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["MarÃ­a"],
                "story": "MarÃ­a se levantou. Acendeu o fogÃ£o. Vai fazer chÃ¡ â€” mas pede um momento sozinha com vocÃª. SofÃ­a e Miguel saem.",
                "now": "Conversa Ã­ntima. MarÃ­a pede algo â€” e vocÃª pode oferecer um item da mochila.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Me cansÃ©. Llevo dos meses fingiendo. Si tienes algo en la bolsa â€” una hierba, algo â€” me ayudarÃ­a a hablar mÃ¡s fÃ¡cil.", "translation": "Me cansei. Faz dois meses fingindo. Se vocÃª tem algo na mochila â€” uma erva, algo â€” me ajudaria a falar mais fÃ¡cil.", "pace": "slow"},
                {
                    "kind": "item_moment",
                    "npc": "MarÃ­a",
                    "situation": "MarÃ­a estende a mÃ£o aberta. Cansada como nunca esteve.",
                    "npc_line": "Â¿Tienes algÃºn remedio o hierba? Si no â€” no importa.",
                    "item_tag": "remedio",
                    "on_use": {
                        "narrative": "VocÃª tira a Hierba de MarÃ­a do bolso. Coloca na mÃ£o dela. Os olhos dela amoleceram um instante.",
                        "npc_reaction": "Mi propia hierba. Curioso â€” pero gracias. Voy a contar mÃ¡s de lo que pensaba.",
                        "bonus": "extra_dialogue",
                    },
                    "on_skip": {
                        "npc_reaction": "EstÃ¡ bien. Voy a hablar igual â€” pero menos.",
                    },
                },
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Yo no me llamo MarÃ­a. Mi apellido era Sangra â€” Eduardo lo adivinÃ³.", "translation": "Eu nÃ£o me chamo MarÃ­a. Meu sobrenome era Sangra â€” Eduardo adivinhou.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "VocÃª processa. Pergunta direta: 'E qual Ã© teu nome verdadeiro?' Como vocÃª pergunta?",
                 "options": [
                     {"id": "a", "text": "Â¿CuÃ¡l es tu nombre verdadero?"},
                     {"id": "b", "text": "Â¿CÃ³mo estÃ¡s?"},
                     {"id": "c", "text": "Â¿CuÃ¡ntos aÃ±os?"},
                     {"id": "d", "text": "Â¿TÃº vienes?"},
                 ], "correct": "a",
                 "word_id": "es_cual", "target": "Â¿cuÃ¡l?", "native": "qual?",
                 "npc_reaction": "Eso preguntarÃ¡ Don Miguel maÃ±ana en otro tono. Hoy te respondo: cuando estÃ© segura de que estÃ¡n seguros â€” te lo digo. No antes."},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "MarÃ­a disse 'cuando estÃ© segura...'. A palavra 'cuando' significa:",
                 "options": [
                     {"id": "a", "text": "Quando (no momento que)"},
                     {"id": "b", "text": "Onde"},
                     {"id": "c", "text": "Por quÃª"},
                     {"id": "d", "text": "Quem"},
                 ], "correct": "a",
                 "word_id": "es_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando. Marca tiempo de condiciÃ³n â€” algo va a pasar, pero no ahora."},
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â€” cuando + verbo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["MarÃ­a"],
                "story": "MarÃ­a serviu chÃ¡. Sentou na sua frente. Decidiu mostrar uma coisa que os Buscadores ensinavam â€” como falar do que ainda nÃ£o aconteceu mas vai.",
                "now": "MarÃ­a explica 'cuando + verbo' â€” quando vocÃª quer falar de algo condicional.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Cuando llegue el dÃ­a â€” voy a contarte todo. Cuando puedas leer la carta entera â€” entenderÃ¡s. La palabra es 'cuando'.", "translation": "Quando chegar o dia â€” vou te contar tudo. Quando vocÃª puder ler a carta inteira â€” entenderÃ¡s. A palavra Ã© 'cuando'.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Cuando + verbo", "meaning": "Quando (algo acontecer)", "note": "marca uma condiÃ§Ã£o no futuro â€” o que vai acontecer DEPENDE disso acontecer primeiro"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Cuando ",        "isKey": True},
                     {"text": "llegue Â· ",      "isKey": False},
                     {"text": "Cuando ",        "isKey": True},
                     {"text": "puedas Â· ",      "isKey": False},
                     {"text": "Cuando ",        "isKey": True},
                     {"text": "sepas",          "isKey": False},
                 ],
                 "example": "Cuando llegue el dÃ­a, hablamos. Cuando puedas leer, entenderÃ¡s.",
                 "translation": "Quando chegar o dia, falamos. Quando vocÃª puder ler, entenderÃ¡s.",
                 "note": "cuando + verbo do futuro condicional â€” espera o momento certo."},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Pra dizer 'quando vocÃª puder, falamos':",
                 "options": [
                     {"id": "a", "text": "Cuando puedas, hablamos"},
                     {"id": "b", "text": "Puedes hablamos"},
                     {"id": "c", "text": "Voy hablamos"},
                     {"id": "d", "text": "Soy hablamos"},
                 ], "correct": "a",
                 "word_id": "es_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando puedas. Eso es."},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Pra dizer 'quando chegar a hora, sabe':",
                 "options": [
                     {"id": "a", "text": "Cuando llegue la hora, sabrÃ¡s"},
                     {"id": "b", "text": "Llega la hora sabrÃ¡s"},
                     {"id": "c", "text": "Sabes la hora"},
                     {"id": "d", "text": "Soy hora"},
                 ], "correct": "a",
                 "word_id": "es_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando llegue. Esperar es la mitad del trabajo."},
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel", "Don Miguel"],
                "story": "SofÃ­a e Miguel voltaram. Don Miguel tambÃ©m. MarÃ­a convida todos a sentar.",
                "now": "Conversa de fechamento. MarÃ­a dÃ¡ uma pista a mais â€” sÃ³ uma.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Una cosa mÃ¡s antes de que se vayan. Hay alguien en el norte â€” que sabe quiÃ©n es el forastero.", "translation": "Uma coisa antes de vocÃªs irem. Tem alguÃ©m no norte â€” que sabe quem Ã© o forasteiro.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Don Miguel reage. Pra vocÃª confirmar pra MarÃ­a que entendeu (jÃ¡ passou â€” 'oÃ­'):",
                 "options": [
                     {"id": "a", "text": "Lo oÃ­"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Voy a oÃ­r"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                 "npc_reaction": "OÃ­ste. Cuando termine todo aquÃ­ â€” vayan al norte. Encuentren a esa persona."},
                {"kind": "npc_speak", "npc": "SofÃ­a", "line": "Â¿QuiÃ©n es?", "translation": "Quem Ã©?", "pace": "urgent"},
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Cuando vayan, lo sabrÃ¡n. Hoy no es el dÃ­a.", "translation": "Quando forem, saberÃ£o. Hoje nÃ£o Ã© o dia.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "VocÃª concorda â€” vÃ£o quando puderem (futuro prÃ³ximo plural):",
                 "options": [
                     {"id": "a", "text": "Vamos a ir"},
                     {"id": "b", "text": "Voy a ir"},
                     {"id": "c", "text": "Va a ir"},
                     {"id": "d", "text": "Soy ir"},
                 ], "correct": "a",
                 "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                 "npc_reaction": "Vamos. Pero antes â€” el Alcalde. Algo va a venir."},
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": "MarÃ­a terminou. VocÃªs saÃ­ram da casa de hÃ³spedes em silÃªncio. Carmen estava na esquina â€” esperando.",
                "now": "DecisÃ£o difÃ­cil sobre como agir nos prÃ³ximos dias. Errar trava.",
            },
            "steps": [
                {"kind": "npc_speak", "npc": "Carmen", "line": "Vi al Inspector hace una hora â€” volviÃ³ al pueblo con tres hombres uniformados.", "translation": "Vi El Inspector hÃ¡ uma hora â€” voltou ao pueblo com trÃªs homens uniformizados.", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "VocÃª confirma â€” ouviu sim:",
                 "options": [
                     {"id": "a", "text": "Lo oÃ­"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Voy a oÃ­r"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                 "npc_reaction": "OÃ­ste. Cuando vengan a por ti â€” y van a venir â€” yo estarÃ© allÃ­.", "gated": True},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "VocÃª agradece formal pela ajuda dela:",
                 "options": [
                     {"id": "a", "text": "Gracias, Carmen"},
                     {"id": "b", "text": "AdiÃ³s Carmen"},
                     {"id": "c", "text": "Mal Carmen"},
                     {"id": "d", "text": "Voy Carmen"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "De nada. Cuando esto acabe â€” y vamos a terminar bien â€” me cuentas todo.", "gated": True},
                {"kind": "scene", "text": "ðŸŒ… Plaza Â· Sol jÃ¡ alto Â· El Inspector visto ao longe atravessando a praÃ§a"},
                {"kind": "narrative", "text": "VocÃªs voltaram pra casa de Don Miguel. Don Miguel pegou a carta do baÃº. SofÃ­a pegou faca. Miguel trancou portas. MarÃ­a sentou na cadeira da cozinha â€” esperando."},
            ],
        },
    },
]
