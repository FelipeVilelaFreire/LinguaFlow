"""
Seed das 6 seções da Fase 10 Espanhol A1 — "La sombra del Vigilante".

Fechamento do mini-arco F6-F10. Não há milestone interno do grupo —
mas planta o gancho temático da T1 inteira: a hostilidade institucional
do pueblo. El Vigilante reaparece como ameaça funcional — pista para o
boss da T1 (El Alcalde / El Jefe del Pueblo).

Sequência: amanhecer cedo. Grupo decidiu na noite anterior ir falar com
o Alcalde. No caminho, El Vigilante bloqueia uma rua estreita. Pede o
"pase de forastero". O protagonista não tem. El Vigilante diz que sem
pase, sai do pueblo até o pôr do sol. Miguel grita. Sofía aparece de
outra esquina com María. María se aproxima de El Vigilante e fala três
frases baixinho — o jogador não escuta. El Vigilante recua, lança um
olhar duro pro protagonista, vai embora. Miguel olha pra María. María
sorri: "Conocidos antiguos. No te preocupes." — primeira pista DIRETA
pro jogador (não pros personagens) de que María tem ligações que
ninguém imagina.

À noite, Don Miguel diz que o pase só é dado pelo Alcalde — e que isso
vai ser um problema.

Novos vocab (2-3): pase · alcalde · ven/para/mira (imperativo simples)
Gramática nova: 1. Imperativo simples (ven, para, mira, habla) — ecoa o
                   que El Vigilante usa pra dar ordens
                2. Expansão do paradigma IR — F6 ensinou yo voy / tú vienes /
                   él · ella va. F10 fecha com NOSOTROS VAMOS e ELLOS VAN
                   (grupo se locomove pro ayuntamiento)
Revisão F1-F9:  saudações, ¿cómo estás?, me llamo, tengo X años,
                no me gusta, hay, yo voy, lugares (calle, plaza, fuente)
NPC principais: Os 4 do grupo · Don Miguel · El Vigilante (antagonista)
Arco emocional: falsa segurança (F9) → ameaça institucional explícita
                → identificação do antagonista da temporada
Transição:      F11 abre na manhã seguinte com o grupo decidindo
                ir pedir o pase ao Alcalde. Começa a estrada
                que termina no boss da T1.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f10_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Amanhecer. O grupo se prepara em silêncio. Don Miguel passa as
    # instruções. Os quatro saem. Pelo caminho, encontram a primeira
    # tensão da manhã. Imersão — falas sem tradução.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "persuasao",
                    "min_level": 2,
                    "uses_item_tag": "moneda",
                    "success": "Voce usa tom firme e respeito para atrasar a ordem do Vigilante.",
                    "fallback": "O Vigilante nao cede, mas Maria aparece antes que a rua feche de vez.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🌄 Amanhecer cedo · Casa de Don Miguel · Mesa baixa de madeira\n\n"
                        "O céu ainda escuro pelas frestas. Lamparina baixa. Os quatro "
                        "sentados em volta da mesa, junto com Don Miguel. Pão da "
                        "noite anterior, café morno. Ninguém com fome de verdade."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Hoy van al ayuntamiento. El Alcalde da el pase a los forasteros — sin pase, hay problema.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "El Vigilante ya escaló esto. Si te encuentran sin pase, te sacan del pueblo. Por eso vamos temprano.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você ouve as palavras 'pase' e 'Alcalde' pela primeira vez. Não sabe exatamente o que são — mas pelo tom, são portas.",
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "¿Y si el Alcalde se niega? ¿Qué hacemos?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Eso lo vemos cuando lleguemos. Una cosa a la vez.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "María come metade do pão em silêncio. Não está preocupada — está pensando.",
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Vamos juntos. Si paran al forastero — paran a los cuatro.",
                },
                {
                    "kind": "scene",
                    "text": "🌫️ Rua deserta · Primeira luz azulada · Vocês saem pela porta",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês quatro andam pela rua principal, sem pressa mas "
                        "sem parar. María lidera — passos certos como se já "
                        "soubesse o caminho. Sofía do seu lado. Miguel atrás "
                        "vigiando atrás."
                    ),
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "pase",     "native": "passe / permissão"},
                        {"target": "alcalde",  "native": "alcaide / prefeito (a maior autoridade do pueblo)"},
                        {"target": "ayuntamiento", "native": "câmara / prefeitura"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel acabou de explicar que o forastero precisa de um documento pra ficar no pueblo. Como esse documento se chama?",
                    "options": [
                        {"id": "a", "text": "Pase"},
                        {"id": "b", "text": "Lámpara"},
                        {"id": "c", "text": "Naranja"},
                        {"id": "d", "text": "Mañana"},
                    ],
                    "correct": "a",
                    "word_id": "es_pase", "target": "pase", "native": "passe",
                    "npc_reaction": "Pase. Un papel con sello. Sin él no eres legal aquí.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Quem dá o pase no pueblo? A maior autoridade política — se chama:",
                    "options": [
                        {"id": "a", "text": "Alcalde"},
                        {"id": "b", "text": "Campesino"},
                        {"id": "c", "text": "Mercader"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_alcalde", "target": "alcalde", "native": "alcaide / prefeito",
                    "npc_reaction": "Alcalde. Hombre político. Vamos a tener que tratarlo con respeto — y con cuidado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel olha pra você caminhando. 'Forastero — ¿estás listo para esto?' Você responde com honestidade:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vale. Si caminas con miedo, lo escondes. Si caminas con calma, ganas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pra esquina que dobra na rua estreita. 'Por aquí es más rápido. ¿Tú vienes?' Você confirma:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy"},
                        {"id": "b", "text": "No tengo hambre"},
                        {"id": "c", "text": "Adiós Sofía"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vamos. La calle estrecha pasa cerca del ayuntamiento.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ─────────────────────────────────────────────────
    # Caminho até o ayuntamiento. Revisão pesada — saudações, estado físico,
    # vizinhos que cumprimentam, María testando enquanto caminha. F1-F9.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "Vocês cortaram caminho pela rua estreita. Pedras desniveladas, "
                    "vasos de barro nas janelas. Algumas pessoas já abrindo "
                    "lojas — saudações trocadas pelos cantos.\n\n"
                    "María se vira pra você enquanto andam. 'Mientras llegamos — "
                    "repaso. Si te paran, no quiero que tartamudees.'"
                ),
                "now": "María testa rapidamente F1-F9 — saudações, identidade, idade.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Primero — si te paran y te preguntan tu nombre. ¿Qué dices?",
                    "translation": "Primeiro — se te param e te perguntam seu nome. O que você fala?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Pergunta direta: 'Me llamo + nome'. Você responde com seu nome:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo veinte años"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Bueno. Sin titubear. Tu nombre es tuyo — di que es tuyo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Si te preguntan tu edad — ¿qué dices?",
                    "translation": "Se te perguntam sua idade — o que você fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "A idade é fácil — você tem vinte. Resposta correta é:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Me llamo veinte"},
                        {"id": "d", "text": "Estoy veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Hombre joven, no niño. Eso le importa al Alcalde.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Antes de seguir — ¿cómo está la cabeza hoy?",
                    "translation": "Antes de continuar — como está a cabeça hoje?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você dormiu bem, sem febre. A cabeça tá clara. Você responde com a palavra de F8:",
                    "options": [
                        {"id": "a", "text": "Estoy mejor"},
                        {"id": "b", "text": "Tengo fiebre"},
                        {"id": "c", "text": "Estoy enfermo"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Bueno. Hoy necesitamos esa cabeza despejada.",
                },
                {
                    "kind": "narrative",
                    "text": "Uma vizinha abre a janela do segundo andar pra estender lençóis. Cumprimenta vocês.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Vecina",
                    "line": "¡Buenos días, María! ¡Y los jóvenes!",
                    "translation": "Bom dia, María! E os jovens!",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecina",
                    "question": "A vizinha cumprimenta de manhã cedo. Você responde do mesmo jeito:",
                    "options": [
                        {"id": "a", "text": "¡Buenos días!"},
                        {"id": "b", "text": "¡Buenas tardes!"},
                        {"id": "c", "text": "¡Buenas noches!"},
                        {"id": "d", "text": "¡Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Eso. Si gentes te ven cumpliendo el saludo, te suman — no te restan.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Mira esa casa allá — la de las macetas rojas. Es de un vecino mío. ¿Cómo lo describes?",
                    "translation": "Olha aquela casa ali — a dos vasos vermelhos. É de um vizinho meu. Como você descreve?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía espera que você junte 'hay' (tem) + objeto. 'Hay flores rojas allí.' Mas pra falar sobre o dono, como você diz que é um vizinho?",
                    "options": [
                        {"id": "a", "text": "Es un vecino"},
                        {"id": "b", "text": "Tengo vecino"},
                        {"id": "c", "text": "Soy vecino"},
                        {"id": "d", "text": "Me llamo vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_vecino", "target": "vecino", "native": "vizinho",
                    "npc_reaction": "Eso. Cada casa tiene su gente. Aquí nadie es anónimo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Cómo te sientes ahora? Estamos por llegar a la plaza grande.",
                    "translation": "Como você se sente agora? Tamos quase chegando na plaza grande.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você sente nervosismo — mas pelo menos não tem febre nem dor. Você está... funcional. Você diz:",
                    "options": [
                        {"id": "a", "text": "Estoy bien"},
                        {"id": "b", "text": "Estoy mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Si necesitas decir 'tengo miedo', dilo — pero no hace falta esconderlo bajo 'mal'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero — ¿te gusta caminar por este pueblo? Después de todo lo que vivimos.",
                    "translation": "Forasteiro — você gosta de caminhar por esse pueblo? Depois de tudo que a gente viveu.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Você gosta — apesar de tudo. As ruas, os cheiros, as pessoas. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sí, me gusta"},
                        {"id": "b", "text": "No me gusta"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Bueno. Ya es 'tu' pueblo también — aunque no quiera el Vigilante.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # CONFRONTO. El Vigilante bloqueia a rua estreita. Exige o pase. Cada
    # exercício é uma fala dele — gated quando crítico. Tensão alta, ritmo
    # rápido. María intervém no final. Falas de Vigilante autoritárias.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "Vocês dobraram a esquina pra outra rua. Estreita, paredes "
                    "altas de adobe nos dois lados. No fundo — uma silhueta no "
                    "meio do caminho. Chapéu baixo. Casaco escuro.\n\n"
                    "El Vigilante del Mercado bloqueia a passagem."
                ),
                "now": "Confronto. Cada palavra importa. Errar trava — você tem que se sair.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "👤 El Vigilante · Meio da rua · Sem desviar",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Para. No avancen más.",
                    "translation": "Para. Não avancem mais.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "María estende o braço pra trás — gesto de parar Sofía e você. Miguel se posiciona meio passo à frente de María.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Ustedes — yo no quiero problema. Sólo el forastero. Forastero — ven aquí.",
                    "translation": "Vocês — eu não quero problema. Só o forasteiro. Forasteiro — vem aqui.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": "Ele te chama. Você precisa cumprimentar primeiro pra ganhar tempo — formal, sem provocação:",
                    "options": [
                        {"id": "a", "text": "Buenos días, señor"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "El Vigilante mira con desprecio. 'Buenos días no me cubre la espalda. ¿Tienes el pase?'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "¿Cómo te llamas, forastero?",
                    "translation": "Como você se chama, forasteiro?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": "Pergunta direta. Mentir agora seria pior. Você responde claro:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "No tengo nombre"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Anotado. ¿Cuántos años tienes?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": "El Vigilante quer sua idade — exata. Vinte anos:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "No me acuerdo"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Edad de servir o de huir. ¿De dónde vienes?",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "¿De dónde vienes? Habla.",
                    "translation": "De onde você vem? Fala.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": "Você não lembra. Mentir agora seria pego. A verdade pode ajudar — você não tem nada a esconder mesmo:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo. Soy forastero."},
                        {"id": "b", "text": "Soy del pueblo"},
                        {"id": "c", "text": "Tengo veinte años"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "El Vigilante levanta una ceja. 'Conveniente. ¿Tienes el pase o no?'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Sin pase del Alcalde, sales del pueblo antes del atardecer. Es la ley.",
                    "translation": "Sem pase do Alcalde, você sai do pueblo antes do entardecer. É a lei.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Vamos ahora mismo al ayuntamiento. Lo estamos llevando.",
                    "translation": "Vamos agora mesmo na prefeitura. Tamos levando ele.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Conmigo. Yo lo llevo.",
                    "translation": "Comigo. Eu levo ele.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Você sente o ar virar pesado. María dá um passo à frente — não rápido, mas firme. Sofía aperta o seu braço atrás.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Vigilante — un momento.",
                    "translation": "Vigilante — um momento.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "María passa do lado de Miguel e se aproxima de El Vigilante "
                        "a passos curtos. Para a um metro dele. Fala três frases "
                        "baixinho — voz tão baixa que ninguém do grupo escuta.\n\n"
                        "El Vigilante muda a expressão. A primeira coisa é "
                        "surpresa. Depois alguma coisa mais difícil de nomear — "
                        "respeito? medo? cálculo?\n\n"
                        "Ele recua meio passo."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "...Mañana. Si no hay pase mañana — lo busco yo mismo.",
                    "translation": "...Amanhã. Se não tiver pase amanhã — eu mesmo procuro ele.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "El Vigilante lança um olhar duro pra você. Vira. Vai embora pela rua. María não se vira pra ver ele sair — espera que os passos sumam.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María vira pro grupo. 'Vamos a la fuente. Necesitamos sentarnos un momento.' Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "Adiós María"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Sigan caminando como si nada. Esta calle todavía tiene ojos.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel, baixo, do seu lado enquanto caminham: 'Forastero — ¿estás bien?' Você responde verdade — não tá 100%, mas tá:",
                    "options": [
                        {"id": "a", "text": "Mejor que hace cinco minutos"},
                        {"id": "b", "text": "Tengo veinte años"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Soy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Lo creo. Aguanta hasta la fuente.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Na fonte da plaza. María ensina o imperativo — porque o protagonista
    # acabou de ouvir El Vigilante usando: 'Para', 'Habla', 'Ven aquí'.
    # Ela quer que ele reconheça quando alguém dá ordem.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "Vocês chegaram à fonte de pedra do centro da plaza. María "
                    "se senta na beira. Sofía bebe água com as mãos. Miguel fica "
                    "de pé olhando ao redor.\n\n"
                    "María: 'Ya viste cómo te habló El Vigilante? Todas las "
                    "palabras eran cortas. Órdenes. Eso es importante que "
                    "reconozcas.'"
                ),
                "now": "María vai te ensinar imperativo — como ouvir ordens e dar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "El Vigilante dijo 'para', 'habla', 'ven aquí'. Esas son órdenes. Cortas, directas. Sin 'por favor'.",
                    "translation": "El Vigilante disse 'para', 'fala', 'vem aqui'. Essas são ordens. Curtas, diretas. Sem 'por favor'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ven aquí",
                    "meaning": "Vem aqui",
                    "note": "ordem de movimento — do verbo 'venir'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Para",
                    "meaning": "Para (de parar)",
                    "note": "ordem pra parar de fazer algo — uma das mais comuns",
                },
                {
                    "kind": "reveal",
                    "phrase": "Mira",
                    "meaning": "Olha",
                    "note": "chamar a atenção pra alguma coisa — 'mira' é amigável OU autoritário pelo tom",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Ven",   "isKey": True},
                        {"text": " / ",   "isKey": False},
                        {"text": "Para",  "isKey": True},
                        {"text": " / ",   "isKey": False},
                        {"text": "Mira",  "isKey": True},
                        {"text": " / ",   "isKey": False},
                        {"text": "Habla", "isKey": True},
                    ],
                    "example": "— Para. Mira. Habla. Ven.",
                    "translation": "— Para. Olha. Fala. Vem.",
                    "note": "imperativo informal — quem dá ordem usa estas formas curtas",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "El Vigilante usou esta palavra quando vocês se aproximaram. 'No avancen más.' A palavra curta dele foi:",
                    "options": [
                        {"id": "a", "text": "Para"},
                        {"id": "b", "text": "Ven"},
                        {"id": "c", "text": "Mira"},
                        {"id": "d", "text": "Habla"},
                    ],
                    "correct": "a",
                    "word_id": "es_para", "target": "para", "native": "para",
                    "npc_reaction": "Para. Es para detener un movimiento. Reconoce esa palabra siempre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Depois ele te chamou: 'Forastero — ___ aquí'. A palavra de chamada foi:",
                    "options": [
                        {"id": "a", "text": "Ven"},
                        {"id": "b", "text": "Para"},
                        {"id": "c", "text": "Mira"},
                        {"id": "d", "text": "Habla"},
                    ],
                    "correct": "a",
                    "word_id": "es_ven", "target": "ven", "native": "vem",
                    "npc_reaction": "Ven. Movimiento hacia el que habla. Cuando alguien te dice 'ven' — decide rápido si vas o no.",
                },
                {
                    "kind": "narrative",
                    "text": "Sofía senta do lado de María na beira da fonte. Olha pra você atenta — quer ver se você tá pegando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Y si yo quiero que tú mires algo importante — te digo:",
                    "translation": "E se eu quero que você olhe alguma coisa importante — eu digo:",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pra um pombo na fonte. 'Forastero — ___' — a palavra pra chamar sua atenção é:",
                    "options": [
                        {"id": "a", "text": "Mira"},
                        {"id": "b", "text": "Ven"},
                        {"id": "c", "text": "Para"},
                        {"id": "d", "text": "Habla"},
                    ],
                    "correct": "a",
                    "word_id": "es_mira", "target": "mira", "native": "olha",
                    "npc_reaction": "Mira. Se usa para señalar — entre amigos, entre extraños, en cualquier sitio.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel se levanta da beira da fonte, sacode a poeira da calça. Olha pros três e diz uma palavra só, decidida.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Bueno — vamos. Los cuatro. Yo voy delante, María atrás, Sofía y el forastero en medio.",
                    "translation": "Bom — vamos. Os quatro. Eu vou na frente, María atrás, Sofía e o forasteiro no meio.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Vamos / vais / van",
                    "meaning": "Nós vamos / vocês vão / eles vão",
                    "note": "expansão de 'yo voy / tú vienes' (F6). Quando o grupo se move: vamos. Quando outros se movem: van.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo voy", "isKey": True},
                        {"text": " · ",    "isKey": False},
                        {"text": "Tú vas", "isKey": True},
                        {"text": " · ",    "isKey": False},
                        {"text": "Ella va","isKey": True},
                        {"text": " · ",    "isKey": False},
                        {"text": "Nosotros vamos", "isKey": True},
                        {"text": " · ",    "isKey": False},
                        {"text": "Ellos van",      "isKey": True},
                    ],
                    "example": "Yo voy a la fuente. Tú vas conmigo. Ella va detrás. Nosotros vamos juntos. Los vecinos van por otra calle.",
                    "translation": "Eu vou à fonte. Tu vais comigo. Ela vai atrás. Nós vamos juntos. Os vizinhos vão por outra rua.",
                    "note": "MESMO verbo (IR) — muda com quem faz: yo / tú / él · ella / nosotros / ellos",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel quer confirmar que vão JUNTOS. 'Los cuatro — ___ al ayuntamiento mañana.' A palavra do verbo IR para 'nós' é:",
                    "options": [
                        {"id": "a", "text": "vamos"},
                        {"id": "b", "text": "voy"},
                        {"id": "c", "text": "vas"},
                        {"id": "d", "text": "va"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos", "target": "nosotros vamos", "native": "nós vamos",
                    "npc_reaction": "Vamos. Cuando es el grupo, no eres tú solo — 'vamos'. Nunca 'yo vamos'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Uns vizinhos passam do outro lado da plaza indo pro mercado. Como Sofía descreve o que eles fazem? 'Ellos ___ al mercado.'",
                    "options": [
                        {"id": "a", "text": "van"},
                        {"id": "b", "text": "vamos"},
                        {"id": "c", "text": "voy"},
                        {"id": "d", "text": "vas"},
                    ],
                    "correct": "a",
                    "word_id": "es_van", "target": "ellos van", "native": "eles vão",
                    "npc_reaction": "Van. Otros — 'ellos van'. La forma cambia con la gente, no contigo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Y si vienes a buscarme y no sabes dónde estoy — pregúntame con voz fuerte: 'María — ¿dónde estás?'",
                    "translation": "E se você vem me buscar e não sabe onde estou — me pergunta com voz forte: 'María — onde você está?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María explica que perguntar onde alguém está é simples. A pergunta é:",
                    "options": [
                        {"id": "a", "text": "¿Dónde estás?"},
                        {"id": "b", "text": "¿Cómo estás?"},
                        {"id": "c", "text": "¿Cuántos años?"},
                        {"id": "d", "text": "¿Tú vienes?"},
                    ],
                    "correct": "a",
                    "word_id": "es_donde_estas", "target": "¿dónde estás?", "native": "onde você está?",
                    "npc_reaction": "Eso. Si gritas '¿dónde estás?' en este pueblo, alguien te responde. Te lo prometo.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # De volta pra casa de Don Miguel. Tarde. Don Miguel ouve o relato.
    # Decisão sobre o que fazer amanhã com o Alcalde. María sutilmente
    # se posiciona — confiável, calma, indispensável. Poucos exercícios,
    # foco em dinâmica de grupo e tensão.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel", "Don Miguel"],
                "story": (
                    "Vocês voltaram pra casa de Don Miguel sem ir ao ayuntamiento "
                    "hoje. María decidiu: 'Mañana — con calma, no con sustos.' "
                    "Don Miguel já estava esperando — Carmen tinha mandado um "
                    "recado.\n\n"
                    "Agora os cinco sentados em volta da mesa, tarde caindo. "
                    "María contando a Don Miguel o que aconteceu — em espanhol "
                    "lento, palavra por palavra."
                ),
                "now": "Decisão do grupo sobre como abordar o Alcalde amanhã.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌇 Tarde · Casa de Don Miguel · Cinco em volta da mesa baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "María — me contaste todo. Pero hay algo que no me contaste. ¿Qué le dijiste al Vigilante para que se fuera?",
                    "translation": "María — você me contou tudo. Mas tem algo que não me contou. O que você falou pro Vigilante pra ele ir embora?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "María olha pra Don Miguel um momento mais longo que o normal. Pondera. Decide responder uma versão.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Lo conocí hace años, antes de venir al pueblo. Sé cosas de él que él prefiere no recordar. Nada más.",
                    "translation": "Eu o conheci faz anos, antes de vir pro pueblo. Sei coisas dele que ele prefere não lembrar. Nada mais.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "A resposta é razoável. Don Miguel aceita. Mas Miguel — "
                        "do seu lado — não acredita. Você vê na cara dele. "
                        "Ele não diz nada."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel se vira pra você. 'Forastero — mañana al amanecer vamos al ayuntamiento. ¿Tú vienes con calma?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Bueno. Pero esta vez vas tú adelante, no atrás. El Alcalde tiene que verte la cara.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Yo voy también. Y María. Y Miguel. Los cuatro al frente del Alcalde, no sólo el forastero.",
                    "translation": "Eu vou também. E María. E Miguel. Os quatro na frente do Alcalde, não só o forasteiro.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Cenamos algo simple — sobró comida de ayer. ¿Te gusta el guiso?",
                    "translation": "Jantamos algo simples — sobrou comida de ontem. Você gosta de ensopado?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María coloca uma tigela na sua frente. Cheiro de ensopado quente. Você prova — você gosta:",
                    "options": [
                        {"id": "a", "text": "Sí, me gusta"},
                        {"id": "b", "text": "No tengo miedo"},
                        {"id": "c", "text": "Estoy enfermo"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Bueno. Necesitas energía. Mañana es día largo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta '¿Cuándo vamos al ayuntamiento?'. Don Miguel responde com a palavra que indica o dia que vem:",
                    "options": [
                        {"id": "a", "text": "Mañana"},
                        {"id": "b", "text": "Hoy"},
                        {"id": "c", "text": "Ayer"},
                        {"id": "d", "text": "Vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_manana", "target": "mañana", "native": "amanhã",
                    "npc_reaction": "Mañana al amanecer. Antes de que el pueblo despierte del todo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Mejor. El Alcalde respeta grupo más que solo. Pero hablar — habla el forastero.",
                    "translation": "Melhor. O Alcalde respeita grupo mais que sozinho. Mas falar — fala o forasteiro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel quer que VOCÊ fale com o Alcalde — não eles. Você precisa aceitar a responsabilidade:",
                    "options": [
                        {"id": "a", "text": "Yo voy a hablar"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "No me gusta"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Bueno. Si tartamudeas, te corregimos en silencio. Pero la voz tiene que salir de ti.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Miguel se levanta da mesa. Vai até a janela. Olha pra rua "
                        "que já tá escurecendo. Não diz nada por um tempo.\n\n"
                        "Volta. Senta. Olha pra María sem disfarçar."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "María — gracias. Por lo del Vigilante. No sé qué le dijiste pero funcionó.",
                    "translation": "María — obrigado. Pelo que aconteceu com o Vigilante. Não sei o que você falou pra ele mas funcionou.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Miguel agradeceu — mas o tom não foi 100% gratidão pura. María sorri sem pressa e responde:",
                    "options": [
                        {"id": "a", "text": "De nada, Miguel"},
                        {"id": "b", "text": "Adiós Miguel"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Para esto estoy. Y voy a estar mañana también.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lamparina baixa. Don Miguel olha pra cada um deles em volta "
                        "da mesa. Para um momento em María. Outro em você. "
                        "Não decide nada — mas pensou em decidir alguma coisa."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Noite tarde. Don Miguel, María e Miguel saem pra organizar coisas pra
    # manhã. Você fica com Sofía na sala. Conversa difícil sobre o que ela
    # viu — e o que ela acha que está acontecendo. Gate: errar trava.
    # Transição direta pra F11.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel", "Don Miguel"],
                "story": (
                    "Don Miguel saiu pra ver dois vizinhos — pedir que servissem "
                    "de testemunha amanhã. María saiu com ele — disse que precisa "
                    "ver algo na casa de hóspedes. Miguel saiu atrás dela 'para "
                    "ayudar', mas você sabe — ele tá seguindo.\n\n"
                    "Sobrou você e Sofía na sala. Ela fechou a porta da frente."
                ),
                "now": "Conversa difícil. Cada palavra importa. Você precisa estar presente.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🕯️ Sala · Noite · Sofía sentada na cadeira em frente · Lamparina baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Forastero — necesito hablar contigo. Solos.",
                    "translation": "Forasteiro — preciso falar com você. Sozinhos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía parece séria — diferente do jeito dela. Você confirma que tá ouvindo:",
                    "options": [
                        {"id": "a", "text": "Sí, te escucho"},
                        {"id": "b", "text": "No tengo miedo"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_si", "target": "sí", "native": "sim",
                    "npc_reaction": "Bueno. Lo que voy a decirte — no se lo cuentes a nadie. Ni a Miguel.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Sofía olha pra porta — fechada. Pra janela — vazia. Volta pra você. Voz baixa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Yo vi lo que María le dijo al Vigilante. Estaba más cerca que ustedes.",
                    "translation": "Eu vi o que María falou pro Vigilante. Eu tava mais perto que vocês.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você gela. Sofía vai dizer alguma coisa que muda tudo. Você não sabe ainda se quer saber.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "No oí las palabras — pero leí la cara del Vigilante. Y conozco esa cara. Es la cara de quien recibe orden de un superior.",
                    "translation": "Não ouvi as palavras — mas li o rosto do Vigilante. E conheço esse rosto. É o rosto de quem recebe ordem de um superior.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía espera você processar. A informação é pesada. Você pergunta — em palavras que você tem:",
                    "options": [
                        {"id": "a", "text": "¿María es...?"},
                        {"id": "b", "text": "Estoy bien"},
                        {"id": "c", "text": "Adiós Sofía"},
                        {"id": "d", "text": "Tengo veinte años"},
                    ],
                    "correct": "a",
                    "word_id": "es_es", "target": "es", "native": "é",
                    "npc_reaction": "No sé qué es. Pero no es sólo una curandera. Eso sí.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Por eso te digo — no se lo cuentes a nadie. Ni a Miguel. Si Miguel sabe, va a hacer algo. Y si María descubre que sabemos — no sé qué hace.",
                    "translation": "Por isso te digo — não conta pra ninguém. Nem pro Miguel. Se Miguel souber, ele vai fazer alguma coisa. E se María descobrir que sabemos — não sei o que ela faz.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía precisa da sua promessa. Você diz que entendeu, que vai guardar:",
                    "options": [
                        {"id": "a", "text": "No le digo a nadie"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "não",
                    "npc_reaction": "Bueno. Mañana al ayuntamiento — todo normal. Como si nada. Después — los dos vigilamos.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "👁️ Sofía olha pra porta. Passos vindo. María e Miguel voltando juntos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Como si nada, forastero. Mira normal — habla normal.",
                    "translation": "Como se nada. Olha normal — fala normal.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "A porta abre. María entra primeiro. Sorri ao ver vocês "
                        "dois. 'Ya volvieron Don Miguel y los vecinos. Mañana al "
                        "amanecer vamos.'\n\n"
                        "Miguel vem atrás. Olha pra Sofía. Olha pra você. Pensa "
                        "em perguntar algo — mas não pergunta."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María se aproxima de você normal — calorosa como sempre. 'Forastero — ¿cómo estás? Tienes que dormir temprano hoy.' Você responde como se nada tivesse acontecido:",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "No me gusta"},
                        {"id": "d", "text": "Adiós María"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Voy a preparar una infusión suave para que duermas profundo. Mañana es día largo.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F11 ───────────────────────
                {
                    "kind": "scene",
                    "text": "🌙 Casa silenciosa · Lamparina apagada · Quarto",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você deitou na cama com a infusão de María nas mãos. "
                        "Olhou pro frasco por um longo tempo antes de tomar. "
                        "Aquele que ela tinha deixado na F8.\n\n"
                        "Tomou. Não tinha como recusar sem levantar suspeita. "
                        "O gosto era diferente esta noite — mais amargo. Ou era "
                        "a sua imaginação."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Mañana, forastero. Mañana.",
                    "translation": "Amanhã, forasteiro. Amanhã.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Sofía sussurrou da cadeira no canto onde ela dormiu de "
                        "novo — ela tinha avisado que ia ficar. Você fechou os "
                        "olhos.\n\n"
                        "O sono veio rápido. Sonho com mãos de María na sua "
                        "testa. Com o rosto de El Vigilante recuando. Com a "
                        "palavra 'fuego' queimando atrás dos olhos.\n\n"
                        "Amanhã — o Alcalde."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
