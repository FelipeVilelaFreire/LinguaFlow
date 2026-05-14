"""
Seed das 6 seÃ§Ãµes da Fase 17 Espanhol A1 â€” "Eduardo y la marca".

Don Miguel marca o encontro no pÃ¡tio da herrerÃ­a ao fim do dia. Eduardo,
MarÃ­a, Don Miguel e vocÃª. SofÃ­a e Miguel ficam de fora (Eduardo pediu
discriÃ§Ã£o).

Eduardo abre a camisa parcialmente â€” uma marca tatuada nas costas.
SÃ­mbolo antigo. MarÃ­a reconhece sem disfarÃ§ar. MarÃ­a explica: Ã© o
sÃ­mbolo dos Buscadores â€” uma irmandade que rastreava palavras antigas.
Eduardo saiu dÃ©cadas atrÃ¡s. Mas reconheceu MarÃ­a quando ela chegou
ao pueblo.

MarÃ­a admite: 'Mi familia tenÃ­a relaciÃ³n con esa gente.'
Don Miguel olha pra MarÃ­a diferente. Nada igual depois.

VOCAB NOVO (3): espalda Â· marca Â· familia
LINGUAGEM NOVA: ya / todavÃ­a no  (jÃ¡ / ainda nÃ£o)
    ya lo sÃ© Â· todavÃ­a no entiendo Â· ya no me acuerdo

RevisÃ£o F1-F16 dominante:
  Â· quiero + verbo (F16) â€” recÃ©m aprendido
  Â· vi/hablÃ©/oÃ­ (F12)
  Â· mi/tu/su (F13)
  Â· el/la (F14)
  Â· soy/estoy/tengo (F8)

NPC principais: Eduardo Â· MarÃ­a Â· Don Miguel Â· vocÃª (silencioso a maior parte)
Arco emocional: descoberta â†’ tensÃ£o silenciosa â†’ fissura no grupo
TransiÃ§Ã£o: F18 abre com vocÃª decidindo contar a SofÃ­a e Miguel.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f17_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Amanhecer. Encontro no pÃ¡tio da herrerÃ­a. ApresentaÃ§Ãµes tensas. 3 novos
    # exer + 2 revisÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ„ PÃ¡tio da herrerÃ­a Â· Amanhecer Â· Fogo ainda apagado\n\n"
                        "Don Miguel acordou vocÃª antes do sol. SaÃ­ram juntos sem "
                        "barulho. MarÃ­a estava na cozinha â€” chÃ¡ pronto, esperando. "
                        "'Bueno. Eduardo nos espera ahora.'\n\n"
                        "Os trÃªs caminharam trÃªs quadras. Sem palavras."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "Eduardo estava no pÃ¡tio. Camisa solta. MÃ£os cruzadas atrÃ¡s das costas.",
                },
                {
                    "kind": "npc",
                    "npc": "Eduardo",
                    "line": "Don Miguel. MarÃ­a. Forastero. Gracias por venir tan temprano.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "MarÃ­a",
                    "line": "Eduardo. Buenos dÃ­as.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "MarÃ­a olha pra Eduardo. Eduardo olha pra MarÃ­a. Como dois pelagantes que se reconhecem mas fingem o contrÃ¡rio.",
                },
                {
                    "kind": "npc",
                    "npc": "Eduardo",
                    "line": "Lo que voy a mostrar â€” lo cargo en la espalda hace cuarenta aÃ±os.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "espalda", "native": "costas"},
                        {"target": "marca",   "native": "marca / sÃ­mbolo"},
                        {"target": "familia", "native": "famÃ­lia"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo disse 'lo cargo en la espalda'. A palavra 'espalda' significa:",
                    "options": [
                        {"id": "a", "text": "Costas"},
                        {"id": "b", "text": "CabeÃ§a"},
                        {"id": "c", "text": "MÃ£os"},
                        {"id": "d", "text": "PÃ©s"},
                    ],
                    "correct": "a",
                    "word_id": "es_espalda", "target": "espalda", "native": "costas",
                    "npc_reaction": "La espalda. Donde guardamos lo que no queremos enseÃ±ar a nadie.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "VocÃª cumprimenta Eduardo â€” amanhecer, formal:",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, Eduardo"},
                        {"id": "b", "text": "Buenas tardes"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as, joven. Hoy es dÃ­a de verdades.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Voy a quitarme la camisa. No del todo â€” solo lo suficiente.",
                    "translation": "Vou tirar a camisa. NÃ£o toda â€” sÃ³ o suficiente.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Eduardo desabotoa devagar. Vira de costas. Empurra a camisa "
                        "pra baixo atÃ© o meio das costas â€” sem revelar tudo.\n\n"
                        "VocÃª vÃª. MarÃ­a vÃª. Don Miguel vÃª.\n\n"
                        "Uma tatuagem velha. Linhas finas formando um sÃ­mbolo "
                        "que parece um sol partido."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo mostra um desenho velho tatuado nas costas â€” um sÃ­mbolo que significa algo antigo. Como se chama essa coisa nas costas dele?",
                    "options": [
                        {"id": "a", "text": "Marca"},
                        {"id": "b", "text": "Mano"},
                        {"id": "c", "text": "Naranja"},
                        {"id": "d", "text": "Casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_marca", "target": "marca", "native": "marca",
                    "npc_reaction": "Marca. Lo que llevo escrito en la piel. Nadie me lo borra.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a olha fixo pra marca. Murmura algo. Pra vocÃª descrever o que sente em italiano simples:",
                    "options": [
                        {"id": "a", "text": "Estoy mal"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "estoy mal", "native": "estou mal",
                    "npc_reaction": "Tranquilo, forastero. Mira sin moverte.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # MarÃ­a reconhece. NÃ£o disfarÃ§a. Confronto inicial. 100% revisÃ£o F1-F16.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Eduardo", "MarÃ­a", "Don Miguel"],
                "story": (
                    "MarÃ­a olha pra marca por longo segundo. Quando fala, "
                    "fala mais baixo do que costuma.\n\n"
                    "'Eduardo â€” esa marca. Yo conozco.'"
                ),
                "now": "MarÃ­a reconhece. Eduardo testa. Cada palavra dela Ã© avaliada.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Ya lo sÃ© que la conoces. Por eso te pedÃ­ que vinieras.",
                    "translation": "JÃ¡ sei que vocÃª conhece. Por isso pedi pra vocÃª vir.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo disse 'ya lo sÃ© que la conoces'. Pra vocÃª confirmar pra Don Miguel que ouviu (jÃ¡ passou â€” ouvi):",
                    "options": [
                        {"id": "a", "text": "SÃ­, lo oÃ­"},
                        {"id": "b", "text": "SÃ­, lo oigo"},
                        {"id": "c", "text": "Voy a oÃ­r"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                    "npc_reaction": "OÃ­ste. Bueno. Esto debe ser dicho â€” y oÃ­do.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "MarÃ­a â€” explica. Â¿QuÃ© es esa marca?",
                    "translation": "MarÃ­a â€” explica. O que Ã© essa marca?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a diz 'voy a contarlo'. Como Don Miguel responde â€” esperando (algo que vamos fazer logo):",
                    "options": [
                        {"id": "a", "text": "Vamos a escuchar"},
                        {"id": "b", "text": "Voy a escuchar"},
                        {"id": "c", "text": "Va a escuchar"},
                        {"id": "d", "text": "Soy escuchar"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos. Los tres â€” Eduardo, Don Miguel y yo. Y el forastero tambiÃ©n.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Es la marca de los Buscadores. Una hermandad antigua. Buscaban palabras viejas â€” palabras que cambian el mundo si se dicen bien.",
                    "translation": "Ã‰ a marca dos Buscadores. Uma irmandade antiga. Buscavam palavras velhas â€” palavras que mudam o mundo se ditas bem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel processa: 'Mi padre me contÃ³ historias de esa gente.' Pra vocÃª confirmar pra Don Miguel que entendeu (estado de agora â€” vocÃª estÃ¡ bem, atento):",
                    "options": [
                        {"id": "a", "text": "Estoy bien, te escucho"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Sigue atento â€” esto te concierne mÃ¡s de lo que crees.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Yo entrÃ© en la hermandad cuando tenÃ­a dieciocho. SalÃ­ cuando tenÃ­a treinta. Hace cuarenta aÃ±os de eso.",
                    "translation": "Eu entrei na irmandade quando tinha dezoito. SaÃ­ quando tinha trinta. Faz quarenta anos disso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo agora tem... quantos anos? VocÃªs contam: 30 quando saiu + 40 anos depois = 70 anos. Pra confirmar (usando tener + idade):",
                    "options": [
                        {"id": "a", "text": "Eduardo tiene setenta aÃ±os"},
                        {"id": "b", "text": "Eduardo es setenta"},
                        {"id": "c", "text": "Eduardo va a tener"},
                        {"id": "d", "text": "Eduardo soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tener aÃ±os", "native": "ter anos",
                    "npc_reaction": "Tengo. Setenta. Viejo, sÃ­ â€” pero todavÃ­a con dos manos firmes.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Cuando vi a MarÃ­a en el mercado hace dos meses, la reconocÃ­. Pero no por su cara â€” por su forma de mirar las cosas. Eso lo aprenden los Buscadores.",
                    "translation": "Quando vi MarÃ­a no mercado faz dois meses, reconheci ela. Mas nÃ£o pela cara â€” pelo jeito dela de olhar as coisas. Isso os Buscadores aprendem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo disse 'la reconocÃ­' â€” algo que ele jÃ¡ fez. Pra vocÃª confirmar a Don Miguel â€” vocÃª reconheceu Carmen no primeiro dia tambÃ©m:",
                    "options": [
                        {"id": "a", "text": "Yo reconocÃ­ a Carmen tambiÃ©n"},
                        {"id": "b", "text": "Yo reconozco"},
                        {"id": "c", "text": "Voy a reconocer"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_reconoci", "target": "reconocÃ­", "native": "reconheci",
                    "npc_reaction": "ReconocÃ­ â€” yo, ya pasado. La 'Ã­' fuerte.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # MarÃ­a admite a relaÃ§Ã£o da famÃ­lia dela com os Buscadores. Eduardo
    # pergunta o sobrenome real. MarÃ­a nega. ApresentaÃ§Ã£o de "ya / todavÃ­a no"
    # natural â€” Eduardo e MarÃ­a usam vÃ¡rias vezes.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Eduardo", "MarÃ­a", "Don Miguel"],
                "story": (
                    "Eduardo ainda de costas, camisa metade pra cima. NÃ£o se "
                    "vira. Don Miguel pega a camisa dele, ajuda a fechar.\n\n"
                    "'Bueno â€” me cubro. Pero antes â€” MarÃ­a. Te pregunto "
                    "directamente.'"
                ),
                "now": "Eduardo confronta MarÃ­a. VocÃªs ouvem. Pode ser chamado.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "MarÃ­a â€” Â¿tÃº tambiÃ©n eras de la hermandad?",
                    "translation": "MarÃ­a â€” vocÃª tambÃ©m era da irmandade?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "No. Yo no. Pero mi familia tenÃ­a relaciÃ³n con esa gente.",
                    "translation": "NÃ£o. Eu nÃ£o. Mas minha famÃ­lia tinha relaÃ§Ã£o com essa gente.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a disse 'mi familia tenÃ­a relaciÃ³n'. A palavra 'familia' significa:",
                    "options": [
                        {"id": "a", "text": "FamÃ­lia (mÃ£e, pai, irmÃ£os)"},
                        {"id": "b", "text": "Casa"},
                        {"id": "c", "text": "Vizinho"},
                        {"id": "d", "text": "Amigo"},
                    ],
                    "correct": "a",
                    "word_id": "es_familia", "target": "familia", "native": "famÃ­lia",
                    "npc_reaction": "Familia. La sangre â€” los que vinieron antes y los que vienen despuÃ©s.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Â¿Tu apellido â€” es Sangra?",
                    "translation": "Teu sobrenome â€” Ã© Sangra?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "SilÃªncio. MarÃ­a nÃ£o responde rÃ¡pido. Don Miguel olha "
                        "pra ela. VocÃª olha pra ela.\n\n"
                        "Ela acaba decidindo nÃ£o responder. Mas o silÃªncio fala."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Ya no uso ese apellido. Hace aÃ±os.",
                    "translation": "JÃ¡ nÃ£o uso esse sobrenome. Faz anos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a disse 'ya no uso ese apellido'. A palavrinha 'ya' significa:",
                    "options": [
                        {"id": "a", "text": "JÃ¡ (algo que mudou, agora Ã© assim)"},
                        {"id": "b", "text": "Ainda nÃ£o"},
                        {"id": "c", "text": "Vou"},
                        {"id": "d", "text": "Sou"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "jÃ¡",
                    "npc_reaction": "Ya. Antes lo usaba â€” hoy no. Esa palabrita marca cambio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Pero el apellido â€” Â¿era Sangra?",
                    "translation": "Mas o sobrenome â€” era Sangra?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "TodavÃ­a no te lo confirmo. No es momento.",
                    "translation": "Ainda nÃ£o te confirmo. NÃ£o Ã© momento.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a disse 'todavÃ­a no te lo confirmo'. A junÃ§Ã£o 'todavÃ­a no' significa:",
                    "options": [
                        {"id": "a", "text": "Ainda nÃ£o (talvez depois)"},
                        {"id": "b", "text": "JÃ¡ nÃ£o"},
                        {"id": "c", "text": "Nunca"},
                        {"id": "d", "text": "Sempre"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavÃ­a no", "native": "ainda nÃ£o",
                    "npc_reaction": "TodavÃ­a no. Es 'todavÃ­a' + 'no'. Significa que algo aÃºn no pasa â€” pero podrÃ­a pasar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Entiendo. Pero â€” algÃºn dÃ­a vas a tener que decirlo. AquÃ­ o en otro lugar.",
                    "translation": "Entendo. Mas â€” algum dia vai ter que dizer. Aqui ou em outro lugar.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo aponta pra ele mesmo. 'Yo soy mÃ¡s viejo que tÃº â€” pero ya no soy ___.' Eduardo tem 70. Pra falar que ele NÃƒO Ã© jovem:",
                    "options": [
                        {"id": "a", "text": "joven"},
                        {"id": "b", "text": "alto"},
                        {"id": "c", "text": "bajo"},
                        {"id": "d", "text": "delgado"},
                    ],
                    "correct": "a",
                    "word_id": "es_joven", "target": "joven", "native": "jovem",
                    "npc_reaction": "Joven. Ya no. Pero la palabra no cambia con hombre o mujer â€” siempre 'joven'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Pero ya entiendes que hay algo grande detrÃ¡s de todo esto, Â¿verdad?",
                    "translation": "Mas vocÃª jÃ¡ entende que tem algo grande por trÃ¡s de tudo isso, nÃ©?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "ConfirmaÃ§Ã£o simples â€” sim, vocÃª jÃ¡ entende isso pelo menos:",
                    "options": [
                        {"id": "a", "text": "SÃ­, ya entiendo eso"},
                        {"id": "b", "text": "No, todavÃ­a no"},
                        {"id": "c", "text": "Voy a entender"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "jÃ¡",
                    "npc_reaction": "Ya. Eso es lo mÃ­nimo que necesitas saber por ahora.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "VocÃª precisa agradecer Eduardo pela coragem de mostrar a marca:",
                    "options": [
                        {"id": "a", "text": "Gracias, Eduardo"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Soy gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Si necesitan saber mÃ¡s â€” yo cuento. Pero quien decide cuÃ¡ndo es MarÃ­a.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Saindo da herrerÃ­a. Don Miguel para vocÃª na rua e explica devagar
    # "ya / todavÃ­a no". Sem nomear "advÃ©rbio". Apenas: palavrinhas que dizem
    # quando algo mudou ou ainda nÃ£o mudou.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "VocÃªs 3 (MarÃ­a separada Ã  frente, andando rÃ¡pido sozinha) "
                    "saem da herrerÃ­a. Don Miguel encosta na parede de adobe e "
                    "te chama com a mÃ£o.\n\n"
                    "'Joven â€” quiero enseÃ±arte una cosa que oÃ­ste mucho ahÃ­ dentro.'"
                ),
                "now": "Don Miguel mostra como 'ya' e 'todavÃ­a no' funcionam.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "'Ya' y 'todavÃ­a no'. Son palabras del tiempo. Pero diferentes de 'hoy', 'ayer', 'maÃ±ana'.",
                    "translation": "'Ya' e 'todavÃ­a no'. SÃ£o palavras do tempo. Mas diferentes de 'hoy', 'ayer', 'maÃ±ana'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ya = jÃ¡ (mudou pra esse estado)",
                    "meaning": "algo aconteceu, mudou de estado, agora Ã© assim",
                    "note": "ya entiendo (entendi e continuo entendendo) Â· ya no uso (parei de usar)",
                },
                {
                    "kind": "reveal",
                    "phrase": "TodavÃ­a no = ainda nÃ£o (talvez depois)",
                    "meaning": "algo ainda nÃ£o aconteceu, mas pode acontecer",
                    "note": "todavÃ­a no entiendo (nÃ£o entendo agora â€” mas vou) Â· todavÃ­a no acepto",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "YA ",       "isKey": True},
                        {"text": "entiendo Â· ", "isKey": False},
                        {"text": "TODAVÃA NO ", "isKey": True},
                        {"text": "entiendo",   "isKey": False},
                    ],
                    "example": "Ya entiendo el pueblo. TodavÃ­a no entiendo a MarÃ­a. Ya hablo poco espaÃ±ol. TodavÃ­a no leo bien.",
                    "translation": "JÃ¡ entendo o pueblo. Ainda nÃ£o entendo MarÃ­a. JÃ¡ falo um pouco de espanhol. Ainda nÃ£o leio bem.",
                    "note": "'ya' = cambio que ya pasÃ³ Â· 'todavÃ­a no' = cambio que falta",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª jÃ¡ conhece Carmen, Rosa, Eduardo, Don Miguel, SofÃ­a, Miguel, MarÃ­a. Pra dizer 'jÃ¡ conheÃ§o o pueblo':",
                    "options": [
                        {"id": "a", "text": "Ya conozco el pueblo"},
                        {"id": "b", "text": "TodavÃ­a no conozco"},
                        {"id": "c", "text": "Voy a conocer"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "jÃ¡",
                    "npc_reaction": "Ya. Eso es. Conoces â€” ya no eres extraÃ±o.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Mas vocÃª ainda nÃ£o sabe ler a carta da Don Miguel (que vai aparecer logo). Pra dizer 'ainda nÃ£o leio':",
                    "options": [
                        {"id": "a", "text": "TodavÃ­a no leo bien"},
                        {"id": "b", "text": "Ya leo bien"},
                        {"id": "c", "text": "Voy a leer"},
                        {"id": "d", "text": "Soy leer"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavÃ­a no", "native": "ainda nÃ£o",
                    "npc_reaction": "TodavÃ­a no. Pero pronto. Esa palabra te dice â€” espera, hay tiempo aÃºn.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Si alguien te pregunta 'Â¿estÃ¡s listo?' y todavÃ­a no â€” dices 'todavÃ­a no'. Si ya estÃ¡s â€” dices 'ya estoy'.",
                    "translation": "Se alguÃ©m te pergunta 'estÃ¡ pronto?' e ainda nÃ£o â€” diz 'todavÃ­a no'. Se jÃ¡ estÃ¡ â€” diz 'ya estoy'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel testa: 'Â¿EstÃ¡s listo para hablar con MarÃ­a sobre todo esto?' VocÃª ainda nÃ£o tÃ¡:",
                    "options": [
                        {"id": "a", "text": "TodavÃ­a no"},
                        {"id": "b", "text": "Ya"},
                        {"id": "c", "text": "Voy a"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavÃ­a no", "native": "ainda nÃ£o",
                    "npc_reaction": "TodavÃ­a no. Bueno. Tomas tu tiempo â€” eso es sabidurÃ­a.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Caminho de volta. MarÃ­a Ã  frente â€” silenciosa. Don Miguel ao seu lado.
    # Conversa baixa. DecisÃ£o silenciosa: vÃ£o observar mais antes de confrontar.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "MarÃ­a"],
                "story": (
                    "VocÃªs caminham de volta. MarÃ­a vai na frente â€” 20 passos "
                    "adiante. Sem olhar pra trÃ¡s. Don Miguel ao seu lado.\n\n"
                    "'Hijo â€” voy a hablarte de algo. En voz baja. Que ella no oiga.'"
                ),
                "now": "DecisÃ£o silenciosa entre vocÃª e Don Miguel sobre o que fazer.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Hoy supimos mucho. Pero todavÃ­a no sabemos lo mÃ¡s importante â€” quiÃ©n era la familia de MarÃ­a antes.",
                    "translation": "Hoje soubemos muito. Mas ainda nÃ£o sabemos o mais importante â€” quem era a famÃ­lia de MarÃ­a antes.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel diz 'ya supimos mucho'. Pra vocÃª concordar que SIM, vocÃªs jÃ¡ sabem muito:",
                    "options": [
                        {"id": "a", "text": "SÃ­, ya sabemos mucho"},
                        {"id": "b", "text": "No, todavÃ­a no sabemos"},
                        {"id": "c", "text": "Vamos a saber"},
                        {"id": "d", "text": "Soy mucho"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "jÃ¡",
                    "npc_reaction": "Ya. Pero hace falta mÃ¡s.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Yo quiero que tÃº no le digas a MarÃ­a que estuvimos hablando solos en el camino.",
                    "translation": "Eu quero que vocÃª nÃ£o fale pra MarÃ­a que estivemos falando sozinhos no caminho.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'yo quiero que tÃº no le digas'. Pra vocÃª confirmar que NÃƒO vai contar (querer + verbo):",
                    "options": [
                        {"id": "a", "text": "No quiero decirle nada"},
                        {"id": "b", "text": "Quiero decirle todo"},
                        {"id": "c", "text": "Voy a decirle"},
                        {"id": "d", "text": "Soy decirle"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero decirle", "native": "quero contar",
                    "npc_reaction": "Bueno. 'No quiero decirle' â€” clara la posiciÃ³n. Eso me tranquiliza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "SofÃ­a y Miguel â€” Â¿quÃ© hacemos con ellos? Â¿Les contamos?",
                    "translation": "SofÃ­a e Miguel â€” o que fazemos com eles? Contamos pra eles?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Don Miguel tÃ¡ te dando o poder de decidir isso. SofÃ­a e "
                        "Miguel jÃ¡ sabem o passado de Carmen com o Alcalde (F16). "
                        "Agora vocÃªs tÃªm a marca. Eles merecem saber tudo."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Sua decisÃ£o â€” sim, contar pra eles (algo que vamos fazer):",
                    "options": [
                        {"id": "a", "text": "SÃ­, vamos a decirles"},
                        {"id": "b", "text": "No, no quiero"},
                        {"id": "c", "text": "Voy a decirles"},
                        {"id": "d", "text": "Soy decirles"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos a decirles. Esta noche. Cuando MarÃ­a se duerma â€” los reunimos.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "MarÃ­a jÃ¡ estava chegando na esquina da rua. VocÃªs "
                        "apertaram o passo pra alcanÃ§Ã¡-la. Quando chegaram do "
                        "lado dela, ela estava tranquila â€” como se a manhÃ£ "
                        "tivesse sido normal."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Ya estÃ¡ hecho. Eduardo estÃ¡ tranquilo. Don Miguel â€” gracias por organizar el encuentro.",
                    "translation": "JÃ¡ estÃ¡ feito. Eduardo estÃ¡ tranquilo. Don Miguel â€” obrigada por organizar o encontro.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Don Miguel responde calmo â€” 'de nada':",
                    "options": [
                        {"id": "a", "text": "De nada, MarÃ­a"},
                        {"id": "b", "text": "AdiÃ³s MarÃ­a"},
                        {"id": "c", "text": "Tengo nada"},
                        {"id": "d", "text": "Soy nada"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Vamos a casa. Quiero descansar.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Noite. VocÃª espera MarÃ­a dormir. Sai com Don Miguel pra falar com SofÃ­a
    # e Miguel. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "SofÃ­a", "Miguel"],
                "story": (
                    "A casa silenciou. MarÃ­a foi pro quarto cedo â€” disse que "
                    "queria descansar muito. VocÃªs esperaram uma hora. Quando "
                    "ouviram a respiraÃ§Ã£o dela fundo do outro lado da parede, "
                    "Don Miguel acenou.\n\n"
                    "SaÃ­ram baixo pela porta dos fundos. Foram atÃ© a casa de "
                    "SofÃ­a â€” onde Miguel jÃ¡ tinha avisado que ia estar."
                ),
                "now": "ReuniÃ£o secreta dos 4. VocÃª precisa contar tudo.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ™ Casa de SofÃ­a Â· Noite Â· Lamparina baixa Â· Quatro sentados em volta de uma mesa pequena",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Hablen. Â¿QuÃ© pasÃ³ esta maÃ±ana?",
                    "translation": "Falem. O que aconteceu essa manhÃ£?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "VocÃª comeÃ§a â€” sim, vocÃªs viram a marca:",
                    "options": [
                        {"id": "a", "text": "SÃ­, vi la marca de Eduardo"},
                        {"id": "b", "text": "No vi nada"},
                        {"id": "c", "text": "Voy a verla"},
                        {"id": "d", "text": "Soy marca"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Â¿Y MarÃ­a â€” quÃ© dijo?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Pra contar o que MarÃ­a disse (jÃ¡ passou, sobre ela):",
                    "options": [
                        {"id": "a", "text": "Dijo que conoce esa marca"},
                        {"id": "b", "text": "Dice que conoce"},
                        {"id": "c", "text": "Va a decir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_dijo", "target": "dijo", "native": "ele/ela disse",
                    "npc_reaction": "Dijo. Bueno. Â¿Y Eduardo le preguntÃ³ algo mÃ¡s?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "VocÃª conta â€” Eduardo perguntou o sobrenome dela. MarÃ­a disse 'todavÃ­a no te confirmo'. Para confirmar pra Miguel a posiÃ§Ã£o dela:",
                    "options": [
                        {"id": "a", "text": "TodavÃ­a no confirma"},
                        {"id": "b", "text": "Ya confirma"},
                        {"id": "c", "text": "Va a confirmar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavÃ­a no", "native": "ainda nÃ£o",
                    "npc_reaction": "TodavÃ­a no. Bien escogiÃ³ tus palabras â€” eso es exacto.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Tres pistas tenemos ya: lo que Carmen contÃ³ del Alcalde, lo que mi mujer LucÃ­a sintiÃ³, y ahora la marca de Eduardo. Tres puntos en una lÃ­nea.",
                    "translation": "TrÃªs pistas jÃ¡ temos: o que Carmen contou do Alcalde, o que minha mulher LucÃ­a sentiu, e agora a marca de Eduardo. TrÃªs pontos numa linha.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "SofÃ­a pergunta: 'Â¿Y quÃ© vamos a hacer ahora?' Don Miguel responde â€” vamos observar. Como SofÃ­a concorda?",
                    "options": [
                        {"id": "a", "text": "Vamos a observar"},
                        {"id": "b", "text": "Voy a observar"},
                        {"id": "c", "text": "Va a observar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos a observar. Pero hay algo mÃ¡s â€” algo que ya no podemos posponer.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel respirou fundo. Olhou pra vocÃª. Pra SofÃ­a. Pra Miguel. Decidiu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "MaÃ±ana â€” voy a enseÃ±arles la carta. La que tengo guardada hace veinte aÃ±os. El forastero ya la necesita.",
                    "translation": "AmanhÃ£ â€” vou mostrar pra vocÃªs a carta. A que tenho guardada faz vinte anos. O forasteiro jÃ¡ precisa dela.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'Una carta tuya, papÃ¡? Â¿De quÃ© carta hablas?' Don Miguel: 'MaÃ±ana. Ahora todos a dormir.' VocÃª responde â€” concorda, vÃ£o dormir:",
                    "options": [
                        {"id": "a", "text": "Vamos a dormir"},
                        {"id": "b", "text": "Voy a dormir"},
                        {"id": "c", "text": "Va a dormir"},
                        {"id": "d", "text": "Soy dormir"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos. MaÃ±ana al amanecer â€” los cuatro. La carta cambia todo.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F18 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸŒƒ Caminho de volta Â· VocÃª e Don Miguel Â· MarÃ­a dormindo profundo",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs voltaram baixo. Entraram pela porta dos fundos. "
                        "MarÃ­a dormindo profundo â€” vocÃª ouviu a respiraÃ§Ã£o dela "
                        "calma na parede.\n\n"
                        "VocÃª deitou. NÃ£o dormiu. A palavra 'carta' girava na "
                        "cabeÃ§a. Don Miguel â€” homem que guardou um segredo "
                        "vinte anos â€” ia abrir um baÃº amanhÃ£."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
