"""
Seed das 6 seções da Fase 16 Espanhol A1 — "Lo que Carmen no contó".

Os três jovens (você, Sofía, Miguel) vão encontrar Carmen sozinha na
plaza pra ouvir o passado dela com o Alcalde. María fica em casa.

Carmen revela: foi noiva do Alcalde há 25 anos. O pai dele quebrou
o noivado porque ela era filha de moleiro — não da elite. Ela nunca
casou depois. Ele casou com outra. Agora ele tem medo dela —
porque ela sabe como ele se subjugou ao pai.

VOCAB NOVO (3): amor · novio · casarse
LINGUAGEM NOVA: quiero + verbo (querer + outro verbo)
    quiero hablar / quiero saber / quiero quedarme
    Apresentado pelos NPCs no uso natural.

Revisão F1-F15 dominante:
  · vi/hablé/oí (F12) — Carmen relata o passado
  · mi/tu/su (F13) — possessivos
  · el/la (F14) — gênero
  · alto/joven (F15) — descrições físicas
  · voy a / vamos a (F11) — futuro próximo
  · soy/estoy/tengo (F8)

NPC principais: Carmen (protagonista da fase) · Sofía · Miguel
Arco emocional: confiança → revelação → peso do passado → primeira
                mentira deliberada do protagonista pra María
Transição: F17 abre com Don Miguel marcando o encontro de Eduardo com María.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f16_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Os 3 chegam à plaza. Carmen sozinha. Convite pra sentar. Apresentação
    # natural de "quiero" — Carmen usa primeiro. 2 novos + 2 revisão.
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
                    "success": "Voce entende o aviso de Bianca como negociacao, nao como ameaca.",
                    "fallback": "Bianca nao entrega tudo, mas deixa uma frase solta para voces seguirem.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🌞 Plaza central · Início da tarde · Carmen sozinha no banco\n\n"
                        "Vocês três chegaram. María tinha saído de casa logo após "
                        "o almoço — disse que ia 'ver una hierba en el campo'. "
                        "Foi a abertura que esperavam.\n\n"
                        "Carmen viu vocês ao longe. Pousou o bordado. Esperou."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Vinieron. Bueno. Yo también quería hablar con ustedes.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Vocês sentam — Sofía no chão de pernas cruzadas, Miguel encostado no muro, você no banco do lado dela.",
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Lo que escucharon ayer en la escalera del ayuntamiento — eso es solo el principio. Voy a contarles todo.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "Carmen — gracias por confiar en nosotros.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Hace veinticinco años — yo tenía veintitrés. Era joven, alta, delgada. Y tenía novio.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "amor",    "native": "amor"},
                        {"target": "novio",   "native": "noivo / namorado"},
                        {"target": "casarse", "native": "casar"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'yo quería hablar con ustedes'. A palavrinha 'quería' significa que ela:",
                    "options": [
                        {"id": "a", "text": "Queria (antes, ela queria)"},
                        {"id": "b", "text": "Quer (agora)"},
                        {"id": "c", "text": "Vai querer"},
                        {"id": "d", "text": "Não quer"},
                    ],
                    "correct": "a",
                    "word_id": "es_queria", "target": "quería", "native": "queria",
                    "npc_reaction": "Quería. Antes — ya pasado. 'Quería' es como 'quiero' pero del pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen mencionou 'tenía novio'. A palavra 'novio' significa:",
                    "options": [
                        {"id": "a", "text": "Noivo / namorado dela"},
                        {"id": "b", "text": "Irmão"},
                        {"id": "c", "text": "Vizinho"},
                        {"id": "d", "text": "Pai"},
                    ],
                    "correct": "a",
                    "word_id": "es_novio", "target": "novio", "native": "noivo",
                    "npc_reaction": "Novio. El hombre con quien pensaba casarme.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Vocês cumprimentam Carmen — começo da tarde:",
                    "options": [
                        {"id": "a", "text": "Buenas tardes, Carmen"},
                        {"id": "b", "text": "Buenos días"},
                        {"id": "c", "text": "Buenas noches"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_tardes", "target": "buenas tardes", "native": "boa tarde",
                    "npc_reaction": "Buenas tardes. Aquí, sentados — empezamos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta pra você: 'Forastero — ¿estás bien para escuchar esto?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Carmen — continúa.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Carmen narra o noivado em pretérito. Vocês ouvem, fazem
    # perguntas em pretérito. F12 + F13 + F8 misturados.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Carmen"],
                "story": (
                    "Carmen começou a contar. Sem pausa. Como quem guardou "
                    "essas palavras décadas e finalmente encontrou ouvidos "
                    "que merecem.\n\n"
                    "Vocês três ouvem em silêncio. Sofía às vezes faz "
                    "perguntas pequenas. Miguel não interrompe."
                ),
                "now": "Carmen narra. Cada pergunta dela espera que vocês respondam — em passado.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "El Alcalde y yo crecimos juntos. Su padre era el alcalde anterior. Mi padre era el molinero — humilde pero honesto.",
                    "translation": "O Alcalde e eu crescemos juntos. O pai dele era o alcalde anterior. Meu pai era o moleiro — humilde mas honesto.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'mi padre era el molinero'. Pra você confirmar que entendeu (era = antes, sempre):",
                    "options": [
                        {"id": "a", "text": "Tu padre era molinero (antes)"},
                        {"id": "b", "text": "Tu padre es molinero (hoy)"},
                        {"id": "c", "text": "Va a ser molinero"},
                        {"id": "d", "text": "Voy molinero"},
                    ],
                    "correct": "a",
                    "word_id": "es_era", "target": "era", "native": "era (antes, sempre)",
                    "npc_reaction": "Era. Antes. Mi padre ya murió hace años. 'Era' es como 'es' pero del tiempo viejo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Nos veíamos cada día. En la plaza, en la iglesia, en las fiestas. Hablábamos mucho.",
                    "translation": "Nos víamos todo dia. Na plaza, na igreja, nas festas. Falávamos muito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen menciona 'mi familia y la suya'. Pra você expressar que tua família (da sua boca) é diferente da dela:",
                    "options": [
                        {"id": "a", "text": "Mi familia"},
                        {"id": "b", "text": "Tu familia"},
                        {"id": "c", "text": "Su familia"},
                        {"id": "d", "text": "Nuestra familia"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi familia", "native": "minha família",
                    "npc_reaction": "Mi familia. Cuando hablas desde ti — siempre 'mi'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta pra Carmen: '¿Y él te ___?' (verbo amar no passado — pra ELE, ela)",
                    "options": [
                        {"id": "a", "text": "amaba"},
                        {"id": "b", "text": "ama"},
                        {"id": "c", "text": "voy a amar"},
                        {"id": "d", "text": "soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_amaba", "target": "amaba", "native": "amava",
                    "npc_reaction": "Amaba. Sí, me amaba. Y yo lo amaba a él. De eso no tengo duda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Cuando él tenía veintidós, me pidió en matrimonio. Yo dije que sí.",
                    "translation": "Quando ele tinha vinte e dois, me pediu em casamento. Eu disse que sim.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'yo dije que sí'. 'Dije' significa:",
                    "options": [
                        {"id": "a", "text": "Eu disse (já passou)"},
                        {"id": "b", "text": "Eu digo (agora)"},
                        {"id": "c", "text": "Vou dizer"},
                        {"id": "d", "text": "Eu sou"},
                    ],
                    "correct": "a",
                    "word_id": "es_dije", "target": "dije", "native": "disse",
                    "npc_reaction": "Dije. Yo, ya pasado. Una palabra corta para algo grande.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel pergunta baixo: '¿Y cuántos años tenías tú?' Carmen confirma — vinte e três. Pra você expressar quantos anos VOCÊ tem agora:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Tenía veinte años"},
                        {"id": "c", "text": "Soy veinte"},
                        {"id": "d", "text": "Voy veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Tengo — ahora. 'Tenía' es lo que era antes. Carmen tenía veintitrés. Tú tienes veinte.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Pero entonces — su padre se enteró. Y todo cambió.",
                    "translation": "Mas então — o pai dele descobriu. E tudo mudou.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Pra perguntar pra Carmen o que aconteceu (já passou):",
                    "options": [
                        {"id": "a", "text": "¿Qué pasó?"},
                        {"id": "b", "text": "¿Qué pasa?"},
                        {"id": "c", "text": "¿Qué va a pasar?"},
                        {"id": "d", "text": "¿Qué soy?"},
                    ],
                    "correct": "a",
                    "word_id": "es_paso", "target": "pasó", "native": "aconteceu",
                    "npc_reaction": "Pasó. La palabra del pasado. Lo que pasó fue cruel y rápido.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta pra Carmen com cuidado: 'Carmen — ¿cómo estás contándonos esto?' (estado de agora):",
                    "options": [
                        {"id": "a", "text": "Carmen responde — estoy bien"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Estoy bien. Pasaron veinticinco años. Ya duele menos.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Carmen continua o relato. O pai do Alcalde proibiu o noivado. Apresenta
    # "querer + verbo" pelo uso natural. Mistura revisão + nova linguagem.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Carmen", "Sofía", "Miguel"],
                "story": (
                    "Carmen continua. Voz mais baixa. Os dedos dela mexem na "
                    "borda do bordado guardado — sem desfiar, sem rasgar. "
                    "Apenas tocando.\n\n"
                    "'El padre era hombre antiguo. Quería que su hijo se "
                    "casara con alguien de la élite del distrito. No con "
                    "una hija de molinero.'"
                ),
                "now": "Carmen explica como tudo mudou. Vocês reagem.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Yo quería casarme con él. Él quería casarse conmigo. Los dos queríamos.",
                    "translation": "Eu queria casar com ele. Ele queria casar comigo. Os dois queríamos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'yo quería casarme'. Aqui ela usa duas palavras juntas — 'quería' + 'casarme'. Significa:",
                    "options": [
                        {"id": "a", "text": "Eu queria casar (uma coisa só)"},
                        {"id": "b", "text": "Já casei"},
                        {"id": "c", "text": "Vou casar"},
                        {"id": "d", "text": "Sou casada"},
                    ],
                    "correct": "a",
                    "word_id": "es_queria", "target": "quería casarme", "native": "queria casar",
                    "npc_reaction": "Quería casarme. Cuando junta 'quería' con otro verbo — uno explica el otro. La fuerza está en 'quería'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Pero su padre dijo: 'No. Tienes que casarte con la hija del juez.' Y mi novio dijo que sí — al padre.",
                    "translation": "Mas o pai dele disse: 'Não. Você tem que casar com a filha do juiz.' E meu noivo disse que sim — pro pai.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aperta o punho. 'Y tú — ¿qué hiciste?' (você fez, no passado)",
                    "options": [
                        {"id": "a", "text": "Carmen responde — yo lloré mucho"},
                        {"id": "b", "text": "Yo lloro mucho"},
                        {"id": "c", "text": "Voy a llorar"},
                        {"id": "d", "text": "Soy llorar"},
                    ],
                    "correct": "a",
                    "word_id": "es_llore", "target": "lloré", "native": "chorei",
                    "npc_reaction": "Lloré. Mucho. Pero al final me levanté.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Mi padre quería que me fuera del pueblo. 'Aquí siempre vas a ser la novia desechada', dijo. Pero yo quería quedarme.",
                    "translation": "Meu pai queria que eu fosse embora do pueblo. 'Aqui sempre vais ser a noiva rejeitada', disse. Mas eu queria ficar.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'yo quería quedarme'. Duas palavras juntas — 'quería' + 'quedarme'. Significa:",
                    "options": [
                        {"id": "a", "text": "Eu queria ficar (uma coisa só)"},
                        {"id": "b", "text": "Eu fico (agora)"},
                        {"id": "c", "text": "Vou ficar"},
                        {"id": "d", "text": "Sou ficar"},
                    ],
                    "correct": "a",
                    "word_id": "es_queria", "target": "quería quedarme", "native": "queria ficar",
                    "npc_reaction": "Quería quedarme. La razón es lo que viene después de 'quería'. Y me quedé.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Él se casó con la otra. Tuvieron una hija. Yo nunca me casé. Nunca tuve hijos.",
                    "translation": "Ele se casou com a outra. Tiveram uma filha. Eu nunca casei. Nunca tive filhos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel pergunta baixo: 'Carmen — ¿y todavía lo amas?' Carmen responde firme:",
                    "options": [
                        {"id": "a", "text": "No. Ya no lo amo"},
                        {"id": "b", "text": "Sí, todavía lo amo"},
                        {"id": "c", "text": "Voy a amarlo"},
                        {"id": "d", "text": "Soy amor"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "não",
                    "npc_reaction": "No. Hace décadas que no. Pero recuerdo. Y él recuerda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Por eso me trata frío en el ayuntamiento. Tiene miedo de que yo cuente — al pueblo entero — cómo se sometió a su padre.",
                    "translation": "Por isso ele me trata frio no ayuntamiento. Tem medo que eu conte — pro pueblo inteiro — como se subjugou ao pai.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía processa. 'Entonces — el Alcalde tiene una debilidad. El miedo a la vergüenza.' Pra você concordar com Sofía (algo que vamos fazer):",
                    "options": [
                        {"id": "a", "text": "Vamos a usar eso si hace falta"},
                        {"id": "b", "text": "Voy a usar"},
                        {"id": "c", "text": "Va a usar"},
                        {"id": "d", "text": "Soy usar"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos. Pero con cuidado — Carmen no quiere usar esto como arma.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "No. No es para usar como arma. Es para que entiendan al hombre. El miedo lo mueve.",
                    "translation": "Não. Não é pra usar como arma. É pra vocês entenderem o homem. O medo o move.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen agradece o esforço de vocês. Você devolve formal:",
                    "options": [
                        {"id": "a", "text": "Gracias, Carmen"},
                        {"id": "b", "text": "Adiós Carmen"},
                        {"id": "c", "text": "Tengo Carmen"},
                        {"id": "d", "text": "Soy gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, joven. Eso era lo que tenía que decir.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Caminho de volta pra casa. Os 3 jovens conversando baixo. Apresentação
    # formal de "quiero/quieres/quiere + verbo". Sem nomear "querer infinitivo".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Sofía", "Miguel"],
                "story": (
                    "Vocês saíram da plaza. Carmen voltou ao bordado. O sol já "
                    "começava a baixar. Andaram em silêncio pelas primeiras "
                    "ruas — depois Sofía começou a falar.\n\n"
                    "'Carmen dijo varias veces — quería casarme, quería quedarme. "
                    "Es algo útil — lo voy a explicar.'"
                ),
                "now": "Sofía mostra como dizer o que se quer fazer.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Cuando juntas 'quiero' con otro verbo, dices lo que quieres hacer. Yo quiero comer. Yo quiero dormir. Yo quiero hablar.",
                    "translation": "Quando você junta 'quiero' com outro verbo, diz o que você quer fazer. Eu quero comer. Eu quero dormir. Eu quero falar.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Quiero + verbo",
                    "meaning": "O que você quer fazer",
                    "note": "junta dos palabras — quiero comer, quiero hablar, quiero saber",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo quiero ",  "isKey": True},
                        {"text": "comer · ",    "isKey": False},
                        {"text": "Tú quieres ", "isKey": True},
                        {"text": "saber · ",    "isKey": False},
                        {"text": "Ella quiere ","isKey": True},
                        {"text": "hablar",      "isKey": False},
                    ],
                    "example": "Quiero comer pan. ¿Quieres saber la verdad? Carmen quiere hablar.",
                    "translation": "Quero comer pão. Você quer saber a verdade? Carmen quer falar.",
                    "note": "quiero / quieres / quiere — cambia con quien quiere. Igual que voy/vas/va de F11.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Pra dizer que VOCÊ quer voltar pra casa agora:",
                    "options": [
                        {"id": "a", "text": "Yo quiero volver a casa"},
                        {"id": "b", "text": "Tú quieres volver a casa"},
                        {"id": "c", "text": "Ella quiere volver"},
                        {"id": "d", "text": "Voy a volver"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero volver", "native": "quero voltar",
                    "npc_reaction": "Quiero — yo, primera. Cuando hablas de ti mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel pergunta pra Sofía: 'Tú ___ saber más, ¿verdad?' (Sofía sempre quer saber mais)",
                    "options": [
                        {"id": "a", "text": "quieres"},
                        {"id": "b", "text": "quiero"},
                        {"id": "c", "text": "quiere"},
                        {"id": "d", "text": "queremos"},
                    ],
                    "correct": "a",
                    "word_id": "es_quieres", "target": "quieres", "native": "queres",
                    "npc_reaction": "Quieres — tú, segunda. Cuando le hablas a alguien.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pra casa onde Carmen mora há 40 anos — palavra de mulher, uma só:",
                    "options": [
                        {"id": "a", "text": "la casa"},
                        {"id": "b", "text": "el casa"},
                        {"id": "c", "text": "los casa"},
                        {"id": "d", "text": "las casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_la", "target": "la casa", "native": "a casa",
                    "npc_reaction": "La casa. Femenina. Como tantas otras del pueblo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel aponta pra Sofía: 'Y eso que ella te dijo — ___ palabras de Carmen son importantes.' Mulheres + muitas — qual palavrinha vai na frente?",
                    "options": [
                        {"id": "a", "text": "las"},
                        {"id": "b", "text": "los"},
                        {"id": "c", "text": "el"},
                        {"id": "d", "text": "la"},
                    ],
                    "correct": "a",
                    "word_id": "es_las", "target": "las palabras", "native": "as palavras",
                    "npc_reaction": "Las palabras. Femenino plural. Hay que guardarlas bien.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Vocês 3 chegam à casa de Don Miguel. María estava na porta. Pergunta
    # onde estiveram. Você mente pela primeira vez. Tensão silenciosa.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "Vocês três chegaram à porta da casa de Don Miguel. "
                    "Estava aberta. María sentada na soleira — tomando uma "
                    "infusão. Ela os viu chegar.\n\n"
                    "'Forastero — ¿dónde estuviste? Te busqué en la herrería.'"
                ),
                "now": "Primeira mentira deliberada do protagonista pra María.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Forastero — ¿dónde estuvieron los tres? Te busqué.",
                    "translation": "Forasteiro — onde vocês três estiveram? Te procurei.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Sofía olha pra você. Miguel olha pra você. Você é quem "
                        "precisa responder. María espera — calma, sem pressão "
                        "óbvia. Mas o silêncio dela é peso."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você decide mentir. Resposta segura — vocês estavam na herrería com Eduardo (algo que María pode verificar mas que não tem grande consequência se descobrir):",
                    "options": [
                        {"id": "a", "text": "Fuimos a la herrería"},
                        {"id": "b", "text": "Fuimos a casa de Carmen"},
                        {"id": "c", "text": "Vamos a la plaza"},
                        {"id": "d", "text": "Soy herrería"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuimos", "target": "fuimos", "native": "fomos",
                    "npc_reaction": "A la herrería. Mmm. ¿Y qué querían allá?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você continua a mentira — usando 'querer + verbo' (querer ver Eduardo):",
                    "options": [
                        {"id": "a", "text": "Queríamos ver a Eduardo"},
                        {"id": "b", "text": "Voy a ver"},
                        {"id": "c", "text": "Tengo Eduardo"},
                        {"id": "d", "text": "Soy Eduardo"},
                    ],
                    "correct": "a",
                    "word_id": "es_queriamos", "target": "queríamos", "native": "queríamos",
                    "npc_reaction": "Queríamos ver a Eduardo. Bueno. ¿Para qué?",
                },
                {
                    "kind": "narrative",
                    "text": "Sofía intervém — rápida, como sempre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Yo quería pedirle que me hiciera un cuchillo nuevo. El mío se me rompió ayer.",
                    "translation": "Eu queria pedir pra ele me fazer uma faca nova. A minha quebrou ontem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María aceita — visivelmente. 'Bueno. Y tú — forastero — ¿cómo estás después de tanta caminata?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Voy a hacer un té de hierbas para todos. Entren.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "María se levantou. Foi pra cozinha. Vocês três entraram "
                        "atrás dela — em silêncio.\n\n"
                        "Você nunca tinha mentido antes pra ela. Sentiu o peso. "
                        "Sofía apertou seu braço discretamente — 'aguanta'."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Hijo de mi padre — ya estamos en esto contigo. No es solo tuyo.",
                    "translation": "Filho do meu pai — já estamos nisso contigo. Não é só seu.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Você agradece Miguel — baixo, sincero:",
                    "options": [
                        {"id": "a", "text": "Gracias, Miguel"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Soy gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Para eso somos hermanos en esto.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Noite. María faz o té. Vocês 4 sentados. María começa a fazer perguntas
    # outra vez — sobre o forastero. Você precisa responder sem entregar.
    # Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "María serviu o té. Quente, aromático. Hierba conocida — "
                    "talvez. Vocês 4 sentados em volta da mesa baixa. Lamparina "
                    "no centro.\n\n"
                    "'Aprovecho — quería preguntarles algunas cosas.'"
                ),
                "now": "María testa. Cada resposta sua precisa proteger o grupo.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🕯️ Cozinha · Lamparina baixa · Té quente · Quatro à mesa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Forastero — ¿quieres más té?",
                    "translation": "Forasteiro — quer mais chá?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você não quer — mas quer responder educado. Negação simples:",
                    "options": [
                        {"id": "a", "text": "No, gracias"},
                        {"id": "b", "text": "Sí, mucho"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_gracias", "target": "no, gracias", "native": "não, obrigado",
                    "npc_reaction": "Como quieras. Bueno — pregunta. Carmen estuvo en la plaza esta tarde — Don Miguel me lo dijo cuando volvió del campo. ¿Tú la viste?",
                    "gated": True,
                },
                {
                    "kind": "player",
                    "text": (
                        "María sabe que vocês viram Carmen. Você precisa dizer SIM — "
                        "mas controlar como muito ela ouviu. Sofía aperta o copo "
                        "discretamente."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Resposta segura — vocês viram Carmen mas só de longe:",
                    "options": [
                        {"id": "a", "text": "Sí, la vi de lejos"},
                        {"id": "b", "text": "No la vi"},
                        {"id": "c", "text": "Voy a verla"},
                        {"id": "d", "text": "Soy Carmen"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "De lejos. Bueno. ¿Y hablaste con ella?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você responde — não, não falou (vocês falaram, mas você nega):",
                    "options": [
                        {"id": "a", "text": "No, no hablé con ella"},
                        {"id": "b", "text": "Sí, hablé mucho"},
                        {"id": "c", "text": "Voy a hablar"},
                        {"id": "d", "text": "Soy hablar"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "não",
                    "npc_reaction": "No. Mmm. Carmen es de pocas palabras cuando borda. Hace bien.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "María dá um sorriso pequeno. Aceitou. Você sente o suor "
                        "frio nas costas — não sabe se ela acreditou. Sofía olha "
                        "pra Miguel — Miguel acena baixo."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Bueno — ¿cómo estás ahora, después de tanto día?",
                    "translation": "Bom — como você está agora, depois de tanto dia?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Honestidade dupla — cansado mas firme:",
                    "options": [
                        {"id": "a", "text": "Estoy cansado, pero bien"},
                        {"id": "b", "text": "Soy cansado"},
                        {"id": "c", "text": "Tengo cansado"},
                        {"id": "d", "text": "Voy cansado"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_cansado", "target": "estoy cansado", "native": "estou cansado",
                    "npc_reaction": "Cansado. Voy a darte una infusión para que duermas bien. Esta noche necesitas descansar.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F17 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🌙 Quarto · Frasco da infusão de María na mesinha · Você sozinho",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você olhou pra infusão de María. Lembrou — ela também "
                        "te deu uma da última vez (F10). Naquela noite, dormiu "
                        "profundo demais.\n\n"
                        "Hoje você não bebeu. Despejou pela janela em silêncio.\n\n"
                        "Quando dormiu — Don Miguel bateu na porta. Acordou você. "
                        "'Hijo — mañana al amanecer. Vamos a hacer lo de Eduardo. "
                        "Lo de la espalda.'"
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
