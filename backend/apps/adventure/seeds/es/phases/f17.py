"""
Seed das 6 seções da Fase 17 Espanhol A1 — "Eduardo y la marca".

Don Miguel marca o encontro no pátio da herrería ao fim do dia. Eduardo,
María, Don Miguel e você. Sofía e Miguel ficam de fora (Eduardo pediu
discrição).

Eduardo abre a camisa parcialmente — uma marca tatuada nas costas.
Símbolo antigo. María reconhece sem disfarçar. María explica: é o
símbolo dos Buscadores — uma irmandade que rastreava palavras antigas.
Eduardo saiu décadas atrás. Mas reconheceu María quando ela chegou
ao pueblo.

María admite: 'Mi familia tenía relación con esa gente.'
Don Miguel olha pra María diferente. Nada igual depois.

VOCAB NOVO (3): espalda · marca · familia
LINGUAGEM NOVA: ya / todavía no  (já / ainda não)
    ya lo sé · todavía no entiendo · ya no me acuerdo

Revisão F1-F16 dominante:
  · quiero + verbo (F16) — recém aprendido
  · vi/hablé/oí (F12)
  · mi/tu/su (F13)
  · el/la (F14)
  · soy/estoy/tengo (F8)

NPC principais: Eduardo · María · Don Miguel · você (silencioso a maior parte)
Arco emocional: descoberta → tensão silenciosa → fissura no grupo
Transição: F18 abre com você decidindo contar a Sofía e Miguel.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f17_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Amanhecer. Encontro no pátio da herrería. Apresentações tensas. 3 novos
    # exer + 2 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "investigacion",
                    "min_level": 2,
                    "uses_item_tag": "documento",
                    "success": "Voce reconhece o sinal antigo antes que Eduardo toque na marca.",
                    "fallback": "A marca parece so uma cicatriz, mas Eduardo explica o bastante para seguir.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🌄 Pátio da herrería · Amanhecer · Fogo ainda apagado\n\n"
                        "Don Miguel acordou você antes do sol. Saíram juntos sem "
                        "barulho. María estava na cozinha — chá pronto, esperando. "
                        "'Bueno. Eduardo nos espera ahora.'\n\n"
                        "Os três caminharam três quadras. Sem palavras."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "Eduardo estava no pátio. Camisa solta. Mãos cruzadas atrás das costas.",
                },
                {
                    "kind": "npc",
                    "npc": "Eduardo",
                    "line": "Don Miguel. María. Forastero. Gracias por venir tan temprano.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "María",
                    "line": "Eduardo. Buenos días.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "María olha pra Eduardo. Eduardo olha pra María. Como dois pelagantes que se reconhecem mas fingem o contrário.",
                },
                {
                    "kind": "npc",
                    "npc": "Eduardo",
                    "line": "Lo que voy a mostrar — lo cargo en la espalda hace cuarenta años.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "espalda", "native": "costas"},
                        {"target": "marca",   "native": "marca / símbolo"},
                        {"target": "familia", "native": "família"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo disse 'lo cargo en la espalda'. A palavra 'espalda' significa:",
                    "options": [
                        {"id": "a", "text": "Costas"},
                        {"id": "b", "text": "Cabeça"},
                        {"id": "c", "text": "Mãos"},
                        {"id": "d", "text": "Pés"},
                    ],
                    "correct": "a",
                    "word_id": "es_espalda", "target": "espalda", "native": "costas",
                    "npc_reaction": "La espalda. Donde guardamos lo que no queremos enseñar a nadie.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Você cumprimenta Eduardo — amanhecer, formal:",
                    "options": [
                        {"id": "a", "text": "Buenos días, Eduardo"},
                        {"id": "b", "text": "Buenas tardes"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días, joven. Hoy es día de verdades.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Voy a quitarme la camisa. No del todo — solo lo suficiente.",
                    "translation": "Vou tirar a camisa. Não toda — só o suficiente.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Eduardo desabotoa devagar. Vira de costas. Empurra a camisa "
                        "pra baixo até o meio das costas — sem revelar tudo.\n\n"
                        "Você vê. María vê. Don Miguel vê.\n\n"
                        "Uma tatuagem velha. Linhas finas formando um símbolo "
                        "que parece um sol partido."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo mostra um desenho velho tatuado nas costas — um símbolo que significa algo antigo. Como se chama essa coisa nas costas dele?",
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
                    "npc": "María",
                    "question": "María olha fixo pra marca. Murmura algo. Pra você descrever o que sente em italiano simples:",
                    "options": [
                        {"id": "a", "text": "Estoy mal"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "estoy mal", "native": "estou mal",
                    "npc_reaction": "Tranquilo, forastero. Mira sin moverte.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # María reconhece. Não disfarça. Confronto inicial. 100% revisão F1-F16.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Eduardo", "María", "Don Miguel"],
                "story": (
                    "María olha pra marca por longo segundo. Quando fala, "
                    "fala mais baixo do que costuma.\n\n"
                    "'Eduardo — esa marca. Yo conozco.'"
                ),
                "now": "María reconhece. Eduardo testa. Cada palavra dela é avaliada.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Ya lo sé que la conoces. Por eso te pedí que vinieras.",
                    "translation": "Já sei que você conhece. Por isso pedi pra você vir.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo disse 'ya lo sé que la conoces'. Pra você confirmar pra Don Miguel que ouviu (já passou — ouvi):",
                    "options": [
                        {"id": "a", "text": "Sí, lo oí"},
                        {"id": "b", "text": "Sí, lo oigo"},
                        {"id": "c", "text": "Voy a oír"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oíste. Bueno. Esto debe ser dicho — y oído.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "María — explica. ¿Qué es esa marca?",
                    "translation": "María — explica. O que é essa marca?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María diz 'voy a contarlo'. Como Don Miguel responde — esperando (algo que vamos fazer logo):",
                    "options": [
                        {"id": "a", "text": "Vamos a escuchar"},
                        {"id": "b", "text": "Voy a escuchar"},
                        {"id": "c", "text": "Va a escuchar"},
                        {"id": "d", "text": "Soy escuchar"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos. Los tres — Eduardo, Don Miguel y yo. Y el forastero también.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Es la marca de los Buscadores. Una hermandad antigua. Buscaban palabras viejas — palabras que cambian el mundo si se dicen bien.",
                    "translation": "É a marca dos Buscadores. Uma irmandade antiga. Buscavam palavras velhas — palavras que mudam o mundo se ditas bem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel processa: 'Mi padre me contó historias de esa gente.' Pra você confirmar pra Don Miguel que entendeu (estado de agora — você está bem, atento):",
                    "options": [
                        {"id": "a", "text": "Estoy bien, te escucho"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Sigue atento — esto te concierne más de lo que crees.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Yo entré en la hermandad cuando tenía dieciocho. Salí cuando tenía treinta. Hace cuarenta años de eso.",
                    "translation": "Eu entrei na irmandade quando tinha dezoito. Saí quando tinha trinta. Faz quarenta anos disso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo agora tem... quantos anos? Vocês contam: 30 quando saiu + 40 anos depois = 70 anos. Pra confirmar (usando tener + idade):",
                    "options": [
                        {"id": "a", "text": "Eduardo tiene setenta años"},
                        {"id": "b", "text": "Eduardo es setenta"},
                        {"id": "c", "text": "Eduardo va a tener"},
                        {"id": "d", "text": "Eduardo soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tener años", "native": "ter anos",
                    "npc_reaction": "Tengo. Setenta. Viejo, sí — pero todavía con dos manos firmes.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Cuando vi a María en el mercado hace dos meses, la reconocí. Pero no por su cara — por su forma de mirar las cosas. Eso lo aprenden los Buscadores.",
                    "translation": "Quando vi María no mercado faz dois meses, reconheci ela. Mas não pela cara — pelo jeito dela de olhar as coisas. Isso os Buscadores aprendem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo disse 'la reconocí' — algo que ele já fez. Pra você confirmar a Don Miguel — você reconheceu Carmen no primeiro dia também:",
                    "options": [
                        {"id": "a", "text": "Yo reconocí a Carmen también"},
                        {"id": "b", "text": "Yo reconozco"},
                        {"id": "c", "text": "Voy a reconocer"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_reconoci", "target": "reconocí", "native": "reconheci",
                    "npc_reaction": "Reconocí — yo, ya pasado. La 'í' fuerte.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # María admite a relação da família dela com os Buscadores. Eduardo
    # pergunta o sobrenome real. María nega. Apresentação de "ya / todavía no"
    # natural — Eduardo e María usam várias vezes.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Eduardo", "María", "Don Miguel"],
                "story": (
                    "Eduardo ainda de costas, camisa metade pra cima. Não se "
                    "vira. Don Miguel pega a camisa dele, ajuda a fechar.\n\n"
                    "'Bueno — me cubro. Pero antes — María. Te pregunto "
                    "directamente.'"
                ),
                "now": "Eduardo confronta María. Vocês ouvem. Pode ser chamado.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "María — ¿tú también eras de la hermandad?",
                    "translation": "María — você também era da irmandade?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "No. Yo no. Pero mi familia tenía relación con esa gente.",
                    "translation": "Não. Eu não. Mas minha família tinha relação com essa gente.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María disse 'mi familia tenía relación'. A palavra 'familia' significa:",
                    "options": [
                        {"id": "a", "text": "Família (mãe, pai, irmãos)"},
                        {"id": "b", "text": "Casa"},
                        {"id": "c", "text": "Vizinho"},
                        {"id": "d", "text": "Amigo"},
                    ],
                    "correct": "a",
                    "word_id": "es_familia", "target": "familia", "native": "família",
                    "npc_reaction": "Familia. La sangre — los que vinieron antes y los que vienen después.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "¿Tu apellido — es Sangra?",
                    "translation": "Teu sobrenome — é Sangra?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Silêncio. María não responde rápido. Don Miguel olha "
                        "pra ela. Você olha pra ela.\n\n"
                        "Ela acaba decidindo não responder. Mas o silêncio fala."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Ya no uso ese apellido. Hace años.",
                    "translation": "Já não uso esse sobrenome. Faz anos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María disse 'ya no uso ese apellido'. A palavrinha 'ya' significa:",
                    "options": [
                        {"id": "a", "text": "Já (algo que mudou, agora é assim)"},
                        {"id": "b", "text": "Ainda não"},
                        {"id": "c", "text": "Vou"},
                        {"id": "d", "text": "Sou"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya. Antes lo usaba — hoy no. Esa palabrita marca cambio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Pero el apellido — ¿era Sangra?",
                    "translation": "Mas o sobrenome — era Sangra?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Todavía no te lo confirmo. No es momento.",
                    "translation": "Ainda não te confirmo. Não é momento.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María disse 'todavía no te lo confirmo'. A junção 'todavía no' significa:",
                    "options": [
                        {"id": "a", "text": "Ainda não (talvez depois)"},
                        {"id": "b", "text": "Já não"},
                        {"id": "c", "text": "Nunca"},
                        {"id": "d", "text": "Sempre"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Es 'todavía' + 'no'. Significa que algo aún no pasa — pero podría pasar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Entiendo. Pero — algún día vas a tener que decirlo. Aquí o en otro lugar.",
                    "translation": "Entendo. Mas — algum dia vai ter que dizer. Aqui ou em outro lugar.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo aponta pra ele mesmo. 'Yo soy más viejo que tú — pero ya no soy ___.' Eduardo tem 70. Pra falar que ele NÃO é jovem:",
                    "options": [
                        {"id": "a", "text": "joven"},
                        {"id": "b", "text": "alto"},
                        {"id": "c", "text": "bajo"},
                        {"id": "d", "text": "delgado"},
                    ],
                    "correct": "a",
                    "word_id": "es_joven", "target": "joven", "native": "jovem",
                    "npc_reaction": "Joven. Ya no. Pero la palabra no cambia con hombre o mujer — siempre 'joven'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Pero ya entiendes que hay algo grande detrás de todo esto, ¿verdad?",
                    "translation": "Mas você já entende que tem algo grande por trás de tudo isso, né?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Confirmação simples — sim, você já entende isso pelo menos:",
                    "options": [
                        {"id": "a", "text": "Sí, ya entiendo eso"},
                        {"id": "b", "text": "No, todavía no"},
                        {"id": "c", "text": "Voy a entender"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya. Eso es lo mínimo que necesitas saber por ahora.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Você precisa agradecer Eduardo pela coragem de mostrar a marca:",
                    "options": [
                        {"id": "a", "text": "Gracias, Eduardo"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Soy gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Si necesitan saber más — yo cuento. Pero quien decide cuándo es María.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Saindo da herrería. Don Miguel para você na rua e explica devagar
    # "ya / todavía no". Sem nomear "advérbio". Apenas: palavrinhas que dizem
    # quando algo mudou ou ainda não mudou.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Vocês 3 (María separada à frente, andando rápido sozinha) "
                    "saem da herrería. Don Miguel encosta na parede de adobe e "
                    "te chama com a mão.\n\n"
                    "'Joven — quiero enseñarte una cosa que oíste mucho ahí dentro.'"
                ),
                "now": "Don Miguel mostra como 'ya' e 'todavía no' funcionam.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "'Ya' y 'todavía no'. Son palabras del tiempo. Pero diferentes de 'hoy', 'ayer', 'mañana'.",
                    "translation": "'Ya' e 'todavía no'. São palavras do tempo. Mas diferentes de 'hoy', 'ayer', 'mañana'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ya = já (mudou pra esse estado)",
                    "meaning": "algo aconteceu, mudou de estado, agora é assim",
                    "note": "ya entiendo (entendi e continuo entendendo) · ya no uso (parei de usar)",
                },
                {
                    "kind": "reveal",
                    "phrase": "Todavía no = ainda não (talvez depois)",
                    "meaning": "algo ainda não aconteceu, mas pode acontecer",
                    "note": "todavía no entiendo (não entendo agora — mas vou) · todavía no acepto",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "YA ",       "isKey": True},
                        {"text": "entiendo · ", "isKey": False},
                        {"text": "TODAVÍA NO ", "isKey": True},
                        {"text": "entiendo",   "isKey": False},
                    ],
                    "example": "Ya entiendo el pueblo. Todavía no entiendo a María. Ya hablo poco español. Todavía no leo bien.",
                    "translation": "Já entendo o pueblo. Ainda não entendo María. Já falo um pouco de espanhol. Ainda não leio bem.",
                    "note": "'ya' = cambio que ya pasó · 'todavía no' = cambio que falta",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você já conhece Carmen, Rosa, Eduardo, Don Miguel, Sofía, Miguel, María. Pra dizer 'já conheço o pueblo':",
                    "options": [
                        {"id": "a", "text": "Ya conozco el pueblo"},
                        {"id": "b", "text": "Todavía no conozco"},
                        {"id": "c", "text": "Voy a conocer"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya. Eso es. Conoces — ya no eres extraño.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Mas você ainda não sabe ler a carta da Don Miguel (que vai aparecer logo). Pra dizer 'ainda não leio':",
                    "options": [
                        {"id": "a", "text": "Todavía no leo bien"},
                        {"id": "b", "text": "Ya leo bien"},
                        {"id": "c", "text": "Voy a leer"},
                        {"id": "d", "text": "Soy leer"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Pero pronto. Esa palabra te dice — espera, hay tiempo aún.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Si alguien te pregunta '¿estás listo?' y todavía no — dices 'todavía no'. Si ya estás — dices 'ya estoy'.",
                    "translation": "Se alguém te pergunta 'está pronto?' e ainda não — diz 'todavía no'. Se já está — diz 'ya estoy'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel testa: '¿Estás listo para hablar con María sobre todo esto?' Você ainda não tá:",
                    "options": [
                        {"id": "a", "text": "Todavía no"},
                        {"id": "b", "text": "Ya"},
                        {"id": "c", "text": "Voy a"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Bueno. Tomas tu tiempo — eso es sabiduría.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Caminho de volta. María à frente — silenciosa. Don Miguel ao seu lado.
    # Conversa baixa. Decisão silenciosa: vão observar mais antes de confrontar.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "María"],
                "story": (
                    "Vocês caminham de volta. María vai na frente — 20 passos "
                    "adiante. Sem olhar pra trás. Don Miguel ao seu lado.\n\n"
                    "'Hijo — voy a hablarte de algo. En voz baja. Que ella no oiga.'"
                ),
                "now": "Decisão silenciosa entre você e Don Miguel sobre o que fazer.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Hoy supimos mucho. Pero todavía no sabemos lo más importante — quién era la familia de María antes.",
                    "translation": "Hoje soubemos muito. Mas ainda não sabemos o mais importante — quem era a família de María antes.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel diz 'ya supimos mucho'. Pra você concordar que SIM, vocês já sabem muito:",
                    "options": [
                        {"id": "a", "text": "Sí, ya sabemos mucho"},
                        {"id": "b", "text": "No, todavía no sabemos"},
                        {"id": "c", "text": "Vamos a saber"},
                        {"id": "d", "text": "Soy mucho"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya. Pero hace falta más.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Yo quiero que tú no le digas a María que estuvimos hablando solos en el camino.",
                    "translation": "Eu quero que você não fale pra María que estivemos falando sozinhos no caminho.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'yo quiero que tú no le digas'. Pra você confirmar que NÃO vai contar (querer + verbo):",
                    "options": [
                        {"id": "a", "text": "No quiero decirle nada"},
                        {"id": "b", "text": "Quiero decirle todo"},
                        {"id": "c", "text": "Voy a decirle"},
                        {"id": "d", "text": "Soy decirle"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero decirle", "native": "quero contar",
                    "npc_reaction": "Bueno. 'No quiero decirle' — clara la posición. Eso me tranquiliza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Sofía y Miguel — ¿qué hacemos con ellos? ¿Les contamos?",
                    "translation": "Sofía e Miguel — o que fazemos com eles? Contamos pra eles?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Don Miguel tá te dando o poder de decidir isso. Sofía e "
                        "Miguel já sabem o passado de Carmen com o Alcalde (F16). "
                        "Agora vocês têm a marca. Eles merecem saber tudo."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Sua decisão — sim, contar pra eles (algo que vamos fazer):",
                    "options": [
                        {"id": "a", "text": "Sí, vamos a decirles"},
                        {"id": "b", "text": "No, no quiero"},
                        {"id": "c", "text": "Voy a decirles"},
                        {"id": "d", "text": "Soy decirles"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos a decirles. Esta noche. Cuando María se duerma — los reunimos.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "María já estava chegando na esquina da rua. Vocês "
                        "apertaram o passo pra alcançá-la. Quando chegaram do "
                        "lado dela, ela estava tranquila — como se a manhã "
                        "tivesse sido normal."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Ya está hecho. Eduardo está tranquilo. Don Miguel — gracias por organizar el encuentro.",
                    "translation": "Já está feito. Eduardo está tranquilo. Don Miguel — obrigada por organizar o encontro.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Don Miguel responde calmo — 'de nada':",
                    "options": [
                        {"id": "a", "text": "De nada, María"},
                        {"id": "b", "text": "Adiós María"},
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

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Noite. Você espera María dormir. Sai com Don Miguel pra falar com Sofía
    # e Miguel. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Sofía", "Miguel"],
                "story": (
                    "A casa silenciou. María foi pro quarto cedo — disse que "
                    "queria descansar muito. Vocês esperaram uma hora. Quando "
                    "ouviram a respiração dela fundo do outro lado da parede, "
                    "Don Miguel acenou.\n\n"
                    "Saíram baixo pela porta dos fundos. Foram até a casa de "
                    "Sofía — onde Miguel já tinha avisado que ia estar."
                ),
                "now": "Reunião secreta dos 4. Você precisa contar tudo.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌙 Casa de Sofía · Noite · Lamparina baixa · Quatro sentados em volta de uma mesa pequena",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Hablen. ¿Qué pasó esta mañana?",
                    "translation": "Falem. O que aconteceu essa manhã?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Você começa — sim, vocês viram a marca:",
                    "options": [
                        {"id": "a", "text": "Sí, vi la marca de Eduardo"},
                        {"id": "b", "text": "No vi nada"},
                        {"id": "c", "text": "Voy a verla"},
                        {"id": "d", "text": "Soy marca"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. ¿Y María — qué dijo?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Pra contar o que María disse (já passou, sobre ela):",
                    "options": [
                        {"id": "a", "text": "Dijo que conoce esa marca"},
                        {"id": "b", "text": "Dice que conoce"},
                        {"id": "c", "text": "Va a decir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_dijo", "target": "dijo", "native": "ele/ela disse",
                    "npc_reaction": "Dijo. Bueno. ¿Y Eduardo le preguntó algo más?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Você conta — Eduardo perguntou o sobrenome dela. María disse 'todavía no te confirmo'. Para confirmar pra Miguel a posição dela:",
                    "options": [
                        {"id": "a", "text": "Todavía no confirma"},
                        {"id": "b", "text": "Ya confirma"},
                        {"id": "c", "text": "Va a confirmar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Bien escogió tus palabras — eso es exacto.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Tres pistas tenemos ya: lo que Carmen contó del Alcalde, lo que mi mujer Lucía sintió, y ahora la marca de Eduardo. Tres puntos en una línea.",
                    "translation": "Três pistas já temos: o que Carmen contou do Alcalde, o que minha mulher Lucía sentiu, e agora a marca de Eduardo. Três pontos numa linha.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Sofía pergunta: '¿Y qué vamos a hacer ahora?' Don Miguel responde — vamos observar. Como Sofía concorda?",
                    "options": [
                        {"id": "a", "text": "Vamos a observar"},
                        {"id": "b", "text": "Voy a observar"},
                        {"id": "c", "text": "Va a observar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos a observar. Pero hay algo más — algo que ya no podemos posponer.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel respirou fundo. Olhou pra você. Pra Sofía. Pra Miguel. Decidiu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Mañana — voy a enseñarles la carta. La que tengo guardada hace veinte años. El forastero ya la necesita.",
                    "translation": "Amanhã — vou mostrar pra vocês a carta. A que tenho guardada faz vinte anos. O forasteiro já precisa dela.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'Una carta tuya, papá? ¿De qué carta hablas?' Don Miguel: 'Mañana. Ahora todos a dormir.' Você responde — concorda, vão dormir:",
                    "options": [
                        {"id": "a", "text": "Vamos a dormir"},
                        {"id": "b", "text": "Voy a dormir"},
                        {"id": "c", "text": "Va a dormir"},
                        {"id": "d", "text": "Soy dormir"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos. Mañana al amanecer — los cuatro. La carta cambia todo.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F18 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🌃 Caminho de volta · Você e Don Miguel · María dormindo profundo",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês voltaram baixo. Entraram pela porta dos fundos. "
                        "María dormindo profundo — você ouviu a respiração dela "
                        "calma na parede.\n\n"
                        "Você deitou. Não dormiu. A palavra 'carta' girava na "
                        "cabeça. Don Miguel — homem que guardou um segredo "
                        "vinte anos — ia abrir um baú amanhã."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
