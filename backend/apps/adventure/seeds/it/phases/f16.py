"""
Seed das 6 seções da Fase 16 Italiano A1 — "Lo que Bianca no contó".

Os três giovanes (você, Chiara, Nico) vão encontrar Bianca sozinha na
piazza pra ouvir o passado dela com o Podesta. Lucia fica em casa.

Bianca revela: foi noiva do Podesta há 25 anni. O pai dele quebrou
o noivado porque ela era filha de moleiro — não da elite. Ela nunca
casou depois. Ele casou com outra. Agora ele tem medo dela —
porque ela sabe come ele se subjugou ao pai.

VOCAB NOVO (3): amor · novio · casarse
LINGUAGEM NOVA: quiero + verbo (querer + outro verbo)
    quiero hablar / quiero saber / quiero quedarme
    Apresentado pelos NPCs no uso natural.

Revisão F1-F15 dominante:
  · vi/hablé/oí (F12) — Bianca relata o passado
  · mi/tu/su (F13) — possessivos
  · el/la (F14) — gênero
  · alto/giovane (F15) — descrições físicas
  · vado a / andiamo a (F11) — futuro próximo
  · sono/sto/ho (F8)

NPC principais: Bianca (protagonista da fase) · Chiara · Nico
Arco emocional: confiança → revelação → pquesto do passado → primeira
                mentira deliberada do protagonista pra Lucia
Transição: F17 abre com Antonio il Contadino marcando o encontro de Pietro com Lucia.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Os 3 chegam à piazza. Bianca sozinha. Convite pra sentar. Apresentação
    # natural de "quiero" — Bianca usa primeiro. 2 novos + 2 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌞 Piazza central · Início da tarde · Bianca sozinha no banco\n\n"
                        "Vocês três chegaram. Lucia tinha saído de casa logo após "
                        "o almoço — disse que ia 'ver una hierba en el campo'. "
                        "Foi a abertura que esperavam.\n\n"
                        "Bianca viu vocês ao longe. Pousou o bordado. Esmau."
                    ),
                },
                {
                    "kind": "skill_check",
                    "skill": "persuasao",
                    "min_level": 2,
                    "uses_item_tag": "moneda",
                    "success": "Voce escolhe a palavra e o gesto certos; a resistencia baixa um pouco.",
                    "fallback": "A conversa nao abre de imediato, mas Nico segura o clima e a historia continua.",
                },
                {
                    "kind": "npc",
                    "npc": "Bianca",
                    "line": "Vinieron. Bene. Yo también quería hablar con voi.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Vocês sentam — Chiara no chão de pernas cruzadas, Nico encostado no muro, você no banco do lado dela.",
                },
                {
                    "kind": "npc",
                    "npc": "Bianca",
                    "line": "Lo que ascoltaron ayer en la escalera del municipio — questo es solo el principio. Vado a contarles todo.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "Bianca — grazie por confiar en noi.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Bianca",
                    "line": "Hace veinticinco años — yo tenía veintitrés. Era giovane, alta, delgada. Y tenía novio.",
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
                    "npc": "Bianca",
                    "question": "Bianca disse 'yo quería hablar con voi'. A palavrinha 'quería' significa que ela:",
                    "options": [
                        {"id": "a", "text": "Queria (prima, ela queria)"},
                        {"id": "b", "text": "Quer (agora)"},
                        {"id": "c", "text": "Vai querer"},
                        {"id": "d", "text": "Não quer"},
                    ],
                    "correct": "a",
                    "word_id": "it_queria", "target": "quería", "native": "queria",
                    "npc_reaction": "Quería. Prima — ya pasado. 'Quería' es come 'quiero' ma del pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca mencionou 'tenía novio'. A palavra 'novio' significa:",
                    "options": [
                        {"id": "a", "text": "Noivo / namorado dela"},
                        {"id": "b", "text": "Irmão"},
                        {"id": "c", "text": "Vizinho"},
                        {"id": "d", "text": "Pai"},
                    ],
                    "correct": "a",
                    "word_id": "it_novio", "target": "novio", "native": "noivo",
                    "npc_reaction": "Novio. El hombre con chi pensaba casarme.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Vocês cumprimentam Bianca — começo da tarde:",
                    "options": [
                        {"id": "a", "text": "Buon pomeriggio, Bianca"},
                        {"id": "b", "text": "Benes días"},
                        {"id": "c", "text": "Buona notte"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenas_tardes", "target": "buon pomeriggio", "native": "boa tarde",
                    "npc_reaction": "Buon pomeriggio. Aquí, sentados — empezamos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta pra você: 'Forestiero — ¿estás bene para ascoltar esto?'",
                    "options": [
                        {"id": "a", "text": "Sto bene"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Bene. Bianca — continúa.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Bianca narra o noivado em pretérito. Vocês ouvem, fazem
    # perguntas em pretérito. F12 + F13 + F8 misturados.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Bianca"],
                "story": (
                    "Bianca começou a contar. Sem pausa. Como quem guardou "
                    "essas palavras décadas e finalmente encontrou ouvidos "
                    "que merecem.\n\n"
                    "Vocês três ouvem em silêncio. Chiara às vezes faz "
                    "perguntas pequenas. Nico não interrompe."
                ),
                "now": "Bianca narra. Cada pergunta dela espera que vocês respondam — em passado.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Il Podesta y yo crecimos juntos. Su padre era el alcalde anterior. Mi padre era el molinero — humilde ma honesto.",
                    "translation": "O Podesta e eu crescemos juntos. O pai dele era o alcalde anterior. Meu pai era o moleiro — humilde piu honesto.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'mi padre era el molinero'. Pra você confirmar que entendeu (era = prima, sempre):",
                    "options": [
                        {"id": "a", "text": "Tu padre era molinero (prima)"},
                        {"id": "b", "text": "Tu padre es molinero (hoy)"},
                        {"id": "c", "text": "Va a ser molinero"},
                        {"id": "d", "text": "Vado molinero"},
                    ],
                    "correct": "a",
                    "word_id": "it_era", "target": "era", "native": "era (prima, sempre)",
                    "npc_reaction": "Era. Prima. Mi padre ya murió hace años. 'Era' es come 'es' ma del tiempo viejo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Nos veíamos cada día. En la piazza, en la iglesia, en las fiestas. Hablábamos mucho.",
                    "translation": "Nos víamos todo dia. Na piazza, na igreja, nas festas. Faláandiamo muito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca menciona 'mi familia y la suya'. Pra você expressar que tua família (da sua boca) é diferente da dela:",
                    "options": [
                        {"id": "a", "text": "Mi familia"},
                        {"id": "b", "text": "Tu familia"},
                        {"id": "c", "text": "Su familia"},
                        {"id": "d", "text": "Nuestra familia"},
                    ],
                    "correct": "a",
                    "word_id": "it_mi", "target": "mi familia", "native": "minha família",
                    "npc_reaction": "Mi familia. Cuando hablas desde ti — siempre 'mi'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta pra Bianca: '¿Y él te ___?' (verbo amar no passado — pra ELE, ela)",
                    "options": [
                        {"id": "a", "text": "amaba"},
                        {"id": "b", "text": "ama"},
                        {"id": "c", "text": "vado a amar"},
                        {"id": "d", "text": "sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_amaba", "target": "amaba", "native": "amava",
                    "npc_reaction": "Amaba. Sí, me amaba. Y yo lo amaba a él. De questo no ho duda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Cuando él tenía veintidós, me pidió en matrimonio. Yo dije que sí.",
                    "translation": "Quando ele tinha vinte e dois, me pediu em casamento. Eu disse que sim.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'yo dije que sí'. 'Dije' significa:",
                    "options": [
                        {"id": "a", "text": "Eu disse (já passou)"},
                        {"id": "b", "text": "Eu digo (agora)"},
                        {"id": "c", "text": "Vou dizer"},
                        {"id": "d", "text": "Eu sou"},
                    ],
                    "correct": "a",
                    "word_id": "it_dije", "target": "dije", "native": "disse",
                    "npc_reaction": "Dije. Yo, ya pasado. Una palabra corta para algo grande.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico pergunta baixo: '¿Y cuántos años tenías tu?' Bianca confirma — vinte e três. Pra você expressar quantos anni VOCÊ tem agora:",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Tenía veinte años"},
                        {"id": "c", "text": "Sono veinte"},
                        {"id": "d", "text": "Vado veinte"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Ho — adesso. 'Tenía' es lo que era prima. Bianca tenía veintitrés. Tu hai veinte.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Ma entonces — su padre se enteró. Y todo cambió.",
                    "translation": "Mas então — o pai dele descobriu. E tudo mudou.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Pra perguntar pra Bianca o que aconteceu (já passou):",
                    "options": [
                        {"id": "a", "text": "¿Qué pasó?"},
                        {"id": "b", "text": "¿Qué pasa?"},
                        {"id": "c", "text": "¿Qué va a pasar?"},
                        {"id": "d", "text": "¿Qué sono?"},
                    ],
                    "correct": "a",
                    "word_id": "it_paso", "target": "pasó", "native": "aconteceu",
                    "npc_reaction": "Pasó. La palabra del pasado. Lo que pasó fue cruel y rápido.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta pra Bianca com cuidado: 'Bianca — ¿cómo estás contándonos esto?' (estado de agora):",
                    "options": [
                        {"id": "a", "text": "Bianca responde — sto bene"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Vado bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Sto bene. Pasaron veinticinco años. Ya duele menos.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Bianca continua o relato. O pai do Podesta proibiu o noivado. Apresenta
    # "querer + verbo" pelo uso natural. Mistura revisão + nova linguagem.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Bianca", "Chiara", "Nico"],
                "story": (
                    "Bianca continua. Voz mais baixa. Os dedos dela mexem na "
                    "borda do bordado guardado — sem desfiar, sem rasgar. "
                    "Apenas tocando.\n\n"
                    "'El padre era hombre antiguo. Quería que su hijo se "
                    "casara con alguien de la élite del distrito. No con "
                    "una hija de molinero.'"
                ),
                "now": "Bianca explica come tudo mudou. Vocês reagem.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Yo quería casarme con él. Él quería casarse con me. Los dos queríamos.",
                    "translation": "Eu queria casar com ele. Ele queria casar comigo. Os dois queríamos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'yo quería casarme'. Aqui ela usa duas palavras juntas — 'quería' + 'casarme'. Significa:",
                    "options": [
                        {"id": "a", "text": "Eu queria casar (uma coisa só)"},
                        {"id": "b", "text": "Já casei"},
                        {"id": "c", "text": "Vou casar"},
                        {"id": "d", "text": "Sou casada"},
                    ],
                    "correct": "a",
                    "word_id": "it_queria", "target": "quería casarme", "native": "queria casar",
                    "npc_reaction": "Quería casarme. Cuando junta 'quería' con otro verbo — uno explica el otro. La fuerza está en 'quería'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Ma su padre ha detto: 'No. Hai que casarte con la hija del juez.' Y mi novio ha detto que sí — al padre.",
                    "translation": "Mas o pai dele disse: 'Não. Você tem que casar com a filha do juiz.' E meu noivo disse que sim — pro pai.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aperta o punho. 'Y tu — ¿qué hiciste?' (você fez, no passado)",
                    "options": [
                        {"id": "a", "text": "Bianca responde — yo lloré mucho"},
                        {"id": "b", "text": "Yo lloro mucho"},
                        {"id": "c", "text": "Vado a llorar"},
                        {"id": "d", "text": "Sono llorar"},
                    ],
                    "correct": "a",
                    "word_id": "it_llore", "target": "lloré", "native": "chorei",
                    "npc_reaction": "Lloré. Mucho. Ma al final me levanté.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Mi padre quería que me fuera del borgo. 'Aquí siempre vas a ser la novia desechada', ha detto. Ma yo quería quedarme.",
                    "translation": "Meu pai queria que eu fosse embora do borgo. 'Aqui sempre vais ser a noiva rejeitada', disse. Mas eu queria ficar.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'yo quería quedarme'. Duas palavras juntas — 'quería' + 'quedarme'. Significa:",
                    "options": [
                        {"id": "a", "text": "Eu queria ficar (uma coisa só)"},
                        {"id": "b", "text": "Eu fico (agora)"},
                        {"id": "c", "text": "Vou ficar"},
                        {"id": "d", "text": "Sou ficar"},
                    ],
                    "correct": "a",
                    "word_id": "it_queria", "target": "quería quedarme", "native": "queria ficar",
                    "npc_reaction": "Quería quedarme. La razón es lo que viene después de 'quería'. Y me quedé.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Él se casó con la otra. Tuvieron una hija. Yo nunca me casé. Nunca tuve hijos.",
                    "translation": "Ele se casou com a outra. Tiveram uma filha. Eu nunca casei. Nunca tive filhos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico pergunta baixo: 'Bianca — ¿y todavía lo apiu?' Bianca responde firme:",
                    "options": [
                        {"id": "a", "text": "No. Ya no lo amo"},
                        {"id": "b", "text": "Sí, todavía lo amo"},
                        {"id": "c", "text": "Vado a amarlo"},
                        {"id": "d", "text": "Sono amor"},
                    ],
                    "correct": "a",
                    "word_id": "it_no", "target": "no", "native": "não",
                    "npc_reaction": "No. Hace décadas que no. Ma recuerdo. Y él recuerda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Por questo me trata frío en el municipio. Ha paura de que yo cuente — al borgo entero — cómo se sometió a su padre.",
                    "translation": "Por isso ele me trata frio no municipio. Tem medo que eu conte — pro borgo inteiro — come se subjugou ao pai.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara processa. 'Entonces — el Podesta ha una debilidad. El paura a la vergüenza.' Pra você concordar com Chiara (algo que andiamo fazer):",
                    "options": [
                        {"id": "a", "text": "Andiamo a usar questo si hace falta"},
                        {"id": "b", "text": "Vado a usar"},
                        {"id": "c", "text": "Va a usar"},
                        {"id": "d", "text": "Sono usar"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo. Ma con cuidado — Bianca no quiere usar esto come arma.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "No. No es para usar come arma. Es para que entiendan al hombre. El paura lo mueve.",
                    "translation": "Não. Não é pra usar come arma. É pra vocês entenderem o homem. O medo o move.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca agradece o esforço de vocês. Você devolve formale:",
                    "options": [
                        {"id": "a", "text": "Grazie, Bianca"},
                        {"id": "b", "text": "Adiós Bianca"},
                        {"id": "c", "text": "Ho Bianca"},
                        {"id": "d", "text": "Sono grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada, giovane. Esatto era lo que tenía que decir.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Caminho de volta pra casa. Os 3 giovanes conversando baixo. Apresentação
    # formale de "quiero/quieres/quiere + verbo". Sem nomear "querer infinitivo".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Chiara", "Nico"],
                "story": (
                    "Vocês saíram da piazza. Bianca voltou ao bordado. O sol já "
                    "começava a baixar. Andaram em silêncio pelas primeiras "
                    "ruas — depois Chiara começou a falar.\n\n"
                    "'Bianca ha detto varias veces — quería casarme, quería quedarme. "
                    "Es algo útil — lo vado a explicar.'"
                ),
                "now": "Chiara mostra come dizer o que se quer fazer.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Cuando juntas 'quiero' con otro verbo, dices lo que quieres hacer. Yo quiero comer. Yo quiero dormir. Yo quiero hablar.",
                    "translation": "Quando você junta 'quiero' com outro verbo, diz o que você quer fazer. Eu quero comer. Eu quero dormir. Eu quero falar.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Quiero + verbo",
                    "meaning": "O que você quer fazer",
                    "note": "junta dos parole — quiero comer, quiero hablar, quiero saber",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo quiero ",  "isKey": True},
                        {"text": "comer · ",    "isKey": False},
                        {"text": "Tu quieres ", "isKey": True},
                        {"text": "saber · ",    "isKey": False},
                        {"text": "Ella quiere ","isKey": True},
                        {"text": "hablar",      "isKey": False},
                    ],
                    "example": "Quiero comer pane. ¿Quieres saber la verdad?Bianca quiere hablar.",
                    "translation": "Quero comer pão. Você quer saber a verdade?Bianca quer falar.",
                    "note": "quiero / quieres / quiere — cambia con chi quiere. Igual que vado/vas/va de F11.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Pra dizer que VOCÊ quer voltar pra casa agora:",
                    "options": [
                        {"id": "a", "text": "Yo quiero volver a casa"},
                        {"id": "b", "text": "Tu quieres volver a casa"},
                        {"id": "c", "text": "Ella quiere volver"},
                        {"id": "d", "text": "Vado a volver"},
                    ],
                    "correct": "a",
                    "word_id": "it_quiero", "target": "quiero volver", "native": "quero voltar",
                    "npc_reaction": "Quiero — yo, primera. Cuando hablas de ti mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico pergunta pra Chiara: 'Tu ___ saber más, ¿verdad?' (Chiara sempre quer saber mais)",
                    "options": [
                        {"id": "a", "text": "quieres"},
                        {"id": "b", "text": "quiero"},
                        {"id": "c", "text": "quiere"},
                        {"id": "d", "text": "queremos"},
                    ],
                    "correct": "a",
                    "word_id": "it_quieres", "target": "quieres", "native": "queres",
                    "npc_reaction": "Quieres — tu, segunda. Cuando le hablas a alguien.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pra casa onde Bianca mora há 40 anni — palavra de mulher, uma só:",
                    "options": [
                        {"id": "a", "text": "la casa"},
                        {"id": "b", "text": "el casa"},
                        {"id": "c", "text": "los casa"},
                        {"id": "d", "text": "las casa"},
                    ],
                    "correct": "a",
                    "word_id": "it_la", "target": "la casa", "native": "a casa",
                    "npc_reaction": "La casa. Femenina. Como tantas otras del borgo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico aponta pra Chiara: 'Y questo que ella te ha detto — ___ parole de Bianca son importprima.' Mulheres + muitas — qual palavrinha vai na fronte?",
                    "options": [
                        {"id": "a", "text": "las"},
                        {"id": "b", "text": "los"},
                        {"id": "c", "text": "el"},
                        {"id": "d", "text": "la"},
                    ],
                    "correct": "a",
                    "word_id": "it_las", "target": "las parole", "native": "as palavras",
                    "npc_reaction": "Las parole. Femenino plural. Hay que guardarlas bene.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Vocês 3 chegam à casa de Antonio il Contadino. Lucia estava na porta. Pergunta
    # onde estiveram. Você mente pela primeira vez. Tensão silenciosa.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Vocês três chegaram à porta da casa de Antonio il Contadino. "
                    "Estava aberta. Lucia sentada na soleira — tomando uma "
                    "infusão. Ela os viu chegar.\n\n"
                    "'Forestiero — ¿dónde estuviste?Te busqué en la herrería.'"
                ),
                "now": "Primeira mentira deliberada do protagonista pra Lucia.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Forestiero — ¿dónde estuvieron los tres?Te busqué.",
                    "translation": "Forasteiro — onde vocês três estiveram?Te procurei.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Chiara olha pra você. Nico olha pra você. Você é quem "
                        "precisa responder. Lucia espera — calma, sem pressão "
                        "óbvia. Mas o silêncio dela é pquesto."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você decide mentir. Resposta segura — vocês estavam na herrería com Pietro (algo que Lucia pode verificar piu que não tem grande consequência se descobrir):",
                    "options": [
                        {"id": "a", "text": "Fuimos a la herrería"},
                        {"id": "b", "text": "Fuimos a casa de Bianca"},
                        {"id": "c", "text": "Andiamo a la piazza"},
                        {"id": "d", "text": "Sono herrería"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuimos", "target": "fuimos", "native": "fomos",
                    "npc_reaction": "A la herrería. Mmm. ¿Y qué querían allá?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você continua a mentira — usando 'querer + verbo' (querer ver Pietro):",
                    "options": [
                        {"id": "a", "text": "Queríamos ver a Pietro"},
                        {"id": "b", "text": "Vado a ver"},
                        {"id": "c", "text": "Ho Pietro"},
                        {"id": "d", "text": "Sono Pietro"},
                    ],
                    "correct": "a",
                    "word_id": "it_queriamos", "target": "queríamos", "native": "queríamos",
                    "npc_reaction": "Queríamos ver a Pietro. Bene. ¿Para qué?",
                },
                {
                    "kind": "narrative",
                    "text": "Chiara intervém — rápida, come sempre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Yo quería pedirle que me hiciera un cuchillo nuevo. El mío se me rompió ayer.",
                    "translation": "Eu queria pedir pra ele me fazer uma faca nova. A minha quebrou ontem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia aceita — visivelmente. 'Bene. Y tu — forestiero — ¿cómo estás después de tanta caminata?'",
                    "options": [
                        {"id": "a", "text": "Sto bene, grazie"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Vado bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Bene. Vado a hacer un té de erbe para todos. Entren.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lucia se levantou. Foi pra cozinha. Vocês três entraram "
                        "atrás dela — em silêncio.\n\n"
                        "Você nunca tinha mentido prima pra ela. Sentiu o pquesto. "
                        "Chiara apertou seu braço discretamente — 'acquanta'."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Hijo de mi padre — ya estamos en esto con te. No es solo tuyo.",
                    "translation": "Filho do meu pai — já estamos nisso con te. Não é só seu.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Você agradece Nico — baixo, senzacero:",
                    "options": [
                        {"id": "a", "text": "Grazie, Nico"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Sto male"},
                        {"id": "d", "text": "Sono grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Pra isso somos hermanni en esto.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Noite. Lucia faz o té. Vocês 4 sentados. Lucia começa a fazer perguntas
    # outra vez — sobre o forestiero. Você precisa responder sem entregar.
    # Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Lucia serviu o té. Quente, aromático. Hierba conocida — "
                    "talvez. Vocês 4 sentados em volta da mesa baixa. Lamparina "
                    "no centro.\n\n"
                    "'Aprovecho — quería preguntarles algunas cose.'"
                ),
                "now": "Lucia testa. Cada resposta sua precisa proteger o grupo.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🕯️ Cozinha · Lamparina baixa · Té quente · Quatro à mesa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Forestiero — ¿quieres más té?",
                    "translation": "Forasteiro — quer mais chá?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você não quer — piu quer responder educado. Negação simples:",
                    "options": [
                        {"id": "a", "text": "No, grazie"},
                        {"id": "b", "text": "Sí, mucho"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_grazie", "target": "no, grazie", "native": "não, obrigado",
                    "npc_reaction": "Como quieras. Bene — pregunta. Bianca estuvo en la piazza esta tarde — Antonio il Contadino me lo ha detto cuando volvió del campo. ¿Tu la viste?",
                    "gated": True,
                },
                {
                    "kind": "player",
                    "text": (
                        "Lucia sabe que vocês viram Bianca. Você precisa dizer SIM — "
                        "piu controlar come muito ela ouviu. Chiara aperta o copo "
                        "discretamente."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Resposta segura — vocês viram Bianca piu só de longe:",
                    "options": [
                        {"id": "a", "text": "Sí, la vi de lejos"},
                        {"id": "b", "text": "No la vi"},
                        {"id": "c", "text": "Vado a verla"},
                        {"id": "d", "text": "Sono Bianca"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "De lejos. Bene. ¿Y hablaste con ella?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você responde — não, não falou (vocês falaram, piu você nega):",
                    "options": [
                        {"id": "a", "text": "No, no hablé con ella"},
                        {"id": "b", "text": "Sí, hablé mucho"},
                        {"id": "c", "text": "Vado a hablar"},
                        {"id": "d", "text": "Sono hablar"},
                    ],
                    "correct": "a",
                    "word_id": "it_no", "target": "no", "native": "não",
                    "npc_reaction": "No. Mmm. Bianca es de pocas parole cuando borda. Hace bene.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lucia dá um sorriso pequeno. Aceitou. Você sente o suor "
                        "frio nas costas — não sabe se ela acreditou. Chiara olha "
                        "pra Nico — Nico acena baixo."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Bene — ¿cómo estás adesso, después de tanto día?",
                    "translation": "Bom — come você está agora, depois de tanto dia?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Honestidade dupla — cansado piu firme:",
                    "options": [
                        {"id": "a", "text": "Sono stanco, ma bene"},
                        {"id": "b", "text": "Sono cansado"},
                        {"id": "c", "text": "Sono stanco"},
                        {"id": "d", "text": "Vado cansado"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_cansado", "target": "sto cansado", "native": "estou cansado",
                    "npc_reaction": "Cansado. Vado a darte una infusión para que duerpiu bene. Esta notte necesitas descansar.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F17 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🌙 Quarto · Frasco da infusão de Lucia na mesenzaha · Você sozinho",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você olhou pra infusão de Lucia. Lembrou — ela também "
                        "te deu uma da última vez (F10). Naquela noite, dormiu "
                        "profundo demais.\n\n"
                        "Hoje você não bebeu. Despejou pela janela em silêncio.\n\n"
                        "Quando dormiu — Antonio il Contadino bateu na porta. Acordou você. "
                        "'Hijo — mañana al amanecer. Andiamo a hacer lo de Pietro. "
                        "Lo de la espalda.'"
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────


