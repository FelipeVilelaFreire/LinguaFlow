"""
Seed das 6 seÃ§Ãµes da Fase 16 Espanhol A1 â€” "Lo que Carmen no contÃ³".

Os trÃªs jovens (vocÃª, SofÃ­a, Miguel) vÃ£o encontrar Carmen sozinha na
plaza pra ouvir o passado dela com o Alcalde. MarÃ­a fica em casa.

Carmen revela: foi noiva do Alcalde hÃ¡ 25 anos. O pai dele quebrou
o noivado porque ela era filha de moleiro â€” nÃ£o da elite. Ela nunca
casou depois. Ele casou com outra. Agora ele tem medo dela â€”
porque ela sabe como ele se subjugou ao pai.

VOCAB NOVO (3): amor Â· novio Â· casarse
LINGUAGEM NOVA: quiero + verbo (querer + outro verbo)
    quiero hablar / quiero saber / quiero quedarme
    Apresentado pelos NPCs no uso natural.

RevisÃ£o F1-F15 dominante:
  Â· vi/hablÃ©/oÃ­ (F12) â€” Carmen relata o passado
  Â· mi/tu/su (F13) â€” possessivos
  Â· el/la (F14) â€” gÃªnero
  Â· alto/joven (F15) â€” descriÃ§Ãµes fÃ­sicas
  Â· voy a / vamos a (F11) â€” futuro prÃ³ximo
  Â· soy/estoy/tengo (F8)

NPC principais: Carmen (protagonista da fase) Â· SofÃ­a Â· Miguel
Arco emocional: confianÃ§a â†’ revelaÃ§Ã£o â†’ peso do passado â†’ primeira
                mentira deliberada do protagonista pra MarÃ­a
TransiÃ§Ã£o: F17 abre com Don Miguel marcando o encontro de Eduardo com MarÃ­a.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f16_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Os 3 chegam Ã  plaza. Carmen sozinha. Convite pra sentar. ApresentaÃ§Ã£o
    # natural de "quiero" â€” Carmen usa primeiro. 2 novos + 2 revisÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒž Plaza central Â· InÃ­cio da tarde Â· Carmen sozinha no banco\n\n"
                        "VocÃªs trÃªs chegaram. MarÃ­a tinha saÃ­do de casa logo apÃ³s "
                        "o almoÃ§o â€” disse que ia 'ver una hierba en el campo'. "
                        "Foi a abertura que esperavam.\n\n"
                        "Carmen viu vocÃªs ao longe. Pousou o bordado. Esperou."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Vinieron. Bueno. Yo tambiÃ©n querÃ­a hablar con ustedes.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "VocÃªs sentam â€” SofÃ­a no chÃ£o de pernas cruzadas, Miguel encostado no muro, vocÃª no banco do lado dela.",
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Lo que escucharon ayer en la escalera del ayuntamiento â€” eso es solo el principio. Voy a contarles todo.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "Carmen â€” gracias por confiar en nosotros.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Hace veinticinco aÃ±os â€” yo tenÃ­a veintitrÃ©s. Era joven, alta, delgada. Y tenÃ­a novio.",
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
                    "question": "Carmen disse 'yo querÃ­a hablar con ustedes'. A palavrinha 'querÃ­a' significa que ela:",
                    "options": [
                        {"id": "a", "text": "Queria (antes, ela queria)"},
                        {"id": "b", "text": "Quer (agora)"},
                        {"id": "c", "text": "Vai querer"},
                        {"id": "d", "text": "NÃ£o quer"},
                    ],
                    "correct": "a",
                    "word_id": "es_queria", "target": "querÃ­a", "native": "queria",
                    "npc_reaction": "QuerÃ­a. Antes â€” ya pasado. 'QuerÃ­a' es como 'quiero' pero del pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen mencionou 'tenÃ­a novio'. A palavra 'novio' significa:",
                    "options": [
                        {"id": "a", "text": "Noivo / namorado dela"},
                        {"id": "b", "text": "IrmÃ£o"},
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
                    "question": "VocÃªs cumprimentam Carmen â€” comeÃ§o da tarde:",
                    "options": [
                        {"id": "a", "text": "Buenas tardes, Carmen"},
                        {"id": "b", "text": "Buenos dÃ­as"},
                        {"id": "c", "text": "Buenas noches"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_tardes", "target": "buenas tardes", "native": "boa tarde",
                    "npc_reaction": "Buenas tardes. AquÃ­, sentados â€” empezamos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta pra vocÃª: 'Forastero â€” Â¿estÃ¡s bien para escuchar esto?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Carmen â€” continÃºa.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # 100% revisÃ£o. Carmen narra o noivado em pretÃ©rito. VocÃªs ouvem, fazem
    # perguntas em pretÃ©rito. F12 + F13 + F8 misturados.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Carmen"],
                "story": (
                    "Carmen comeÃ§ou a contar. Sem pausa. Como quem guardou "
                    "essas palavras dÃ©cadas e finalmente encontrou ouvidos "
                    "que merecem.\n\n"
                    "VocÃªs trÃªs ouvem em silÃªncio. SofÃ­a Ã s vezes faz "
                    "perguntas pequenas. Miguel nÃ£o interrompe."
                ),
                "now": "Carmen narra. Cada pergunta dela espera que vocÃªs respondam â€” em passado.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "El Alcalde y yo crecimos juntos. Su padre era el alcalde anterior. Mi padre era el molinero â€” humilde pero honesto.",
                    "translation": "O Alcalde e eu crescemos juntos. O pai dele era o alcalde anterior. Meu pai era o moleiro â€” humilde mas honesto.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'mi padre era el molinero'. Pra vocÃª confirmar que entendeu (era = antes, sempre):",
                    "options": [
                        {"id": "a", "text": "Tu padre era molinero (antes)"},
                        {"id": "b", "text": "Tu padre es molinero (hoy)"},
                        {"id": "c", "text": "Va a ser molinero"},
                        {"id": "d", "text": "Voy molinero"},
                    ],
                    "correct": "a",
                    "word_id": "es_era", "target": "era", "native": "era (antes, sempre)",
                    "npc_reaction": "Era. Antes. Mi padre ya muriÃ³ hace aÃ±os. 'Era' es como 'es' pero del tiempo viejo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Nos veÃ­amos cada dÃ­a. En la plaza, en la iglesia, en las fiestas. HablÃ¡bamos mucho.",
                    "translation": "Nos vÃ­amos todo dia. Na plaza, na igreja, nas festas. FalÃ¡vamos muito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen menciona 'mi familia y la suya'. Pra vocÃª expressar que tua famÃ­lia (da sua boca) Ã© diferente da dela:",
                    "options": [
                        {"id": "a", "text": "Mi familia"},
                        {"id": "b", "text": "Tu familia"},
                        {"id": "c", "text": "Su familia"},
                        {"id": "d", "text": "Nuestra familia"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi familia", "native": "minha famÃ­lia",
                    "npc_reaction": "Mi familia. Cuando hablas desde ti â€” siempre 'mi'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta pra Carmen: 'Â¿Y Ã©l te ___?' (verbo amar no passado â€” pra ELE, ela)",
                    "options": [
                        {"id": "a", "text": "amaba"},
                        {"id": "b", "text": "ama"},
                        {"id": "c", "text": "voy a amar"},
                        {"id": "d", "text": "soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_amaba", "target": "amaba", "native": "amava",
                    "npc_reaction": "Amaba. SÃ­, me amaba. Y yo lo amaba a Ã©l. De eso no tengo duda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Cuando Ã©l tenÃ­a veintidÃ³s, me pidiÃ³ en matrimonio. Yo dije que sÃ­.",
                    "translation": "Quando ele tinha vinte e dois, me pediu em casamento. Eu disse que sim.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'yo dije que sÃ­'. 'Dije' significa:",
                    "options": [
                        {"id": "a", "text": "Eu disse (jÃ¡ passou)"},
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
                    "question": "Miguel pergunta baixo: 'Â¿Y cuÃ¡ntos aÃ±os tenÃ­as tÃº?' Carmen confirma â€” vinte e trÃªs. Pra vocÃª expressar quantos anos VOCÃŠ tem agora:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "TenÃ­a veinte aÃ±os"},
                        {"id": "c", "text": "Soy veinte"},
                        {"id": "d", "text": "Voy veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Tengo â€” ahora. 'TenÃ­a' es lo que era antes. Carmen tenÃ­a veintitrÃ©s. TÃº tienes veinte.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Pero entonces â€” su padre se enterÃ³. Y todo cambiÃ³.",
                    "translation": "Mas entÃ£o â€” o pai dele descobriu. E tudo mudou.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Pra perguntar pra Carmen o que aconteceu (jÃ¡ passou):",
                    "options": [
                        {"id": "a", "text": "Â¿QuÃ© pasÃ³?"},
                        {"id": "b", "text": "Â¿QuÃ© pasa?"},
                        {"id": "c", "text": "Â¿QuÃ© va a pasar?"},
                        {"id": "d", "text": "Â¿QuÃ© soy?"},
                    ],
                    "correct": "a",
                    "word_id": "es_paso", "target": "pasÃ³", "native": "aconteceu",
                    "npc_reaction": "PasÃ³. La palabra del pasado. Lo que pasÃ³ fue cruel y rÃ¡pido.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta pra Carmen com cuidado: 'Carmen â€” Â¿cÃ³mo estÃ¡s contÃ¡ndonos esto?' (estado de agora):",
                    "options": [
                        {"id": "a", "text": "Carmen responde â€” estoy bien"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Estoy bien. Pasaron veinticinco aÃ±os. Ya duele menos.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Carmen continua o relato. O pai do Alcalde proibiu o noivado. Apresenta
    # "querer + verbo" pelo uso natural. Mistura revisÃ£o + nova linguagem.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Carmen", "SofÃ­a", "Miguel"],
                "story": (
                    "Carmen continua. Voz mais baixa. Os dedos dela mexem na "
                    "borda do bordado guardado â€” sem desfiar, sem rasgar. "
                    "Apenas tocando.\n\n"
                    "'El padre era hombre antiguo. QuerÃ­a que su hijo se "
                    "casara con alguien de la Ã©lite del distrito. No con "
                    "una hija de molinero.'"
                ),
                "now": "Carmen explica como tudo mudou. VocÃªs reagem.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Yo querÃ­a casarme con Ã©l. Ã‰l querÃ­a casarse conmigo. Los dos querÃ­amos.",
                    "translation": "Eu queria casar com ele. Ele queria casar comigo. Os dois querÃ­amos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'yo querÃ­a casarme'. Aqui ela usa duas palavras juntas â€” 'querÃ­a' + 'casarme'. Significa:",
                    "options": [
                        {"id": "a", "text": "Eu queria casar (uma coisa sÃ³)"},
                        {"id": "b", "text": "JÃ¡ casei"},
                        {"id": "c", "text": "Vou casar"},
                        {"id": "d", "text": "Sou casada"},
                    ],
                    "correct": "a",
                    "word_id": "es_queria", "target": "querÃ­a casarme", "native": "queria casar",
                    "npc_reaction": "QuerÃ­a casarme. Cuando junta 'querÃ­a' con otro verbo â€” uno explica el otro. La fuerza estÃ¡ en 'querÃ­a'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Pero su padre dijo: 'No. Tienes que casarte con la hija del juez.' Y mi novio dijo que sÃ­ â€” al padre.",
                    "translation": "Mas o pai dele disse: 'NÃ£o. VocÃª tem que casar com a filha do juiz.' E meu noivo disse que sim â€” pro pai.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aperta o punho. 'Y tÃº â€” Â¿quÃ© hiciste?' (vocÃª fez, no passado)",
                    "options": [
                        {"id": "a", "text": "Carmen responde â€” yo llorÃ© mucho"},
                        {"id": "b", "text": "Yo lloro mucho"},
                        {"id": "c", "text": "Voy a llorar"},
                        {"id": "d", "text": "Soy llorar"},
                    ],
                    "correct": "a",
                    "word_id": "es_llore", "target": "llorÃ©", "native": "chorei",
                    "npc_reaction": "LlorÃ©. Mucho. Pero al final me levantÃ©.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Mi padre querÃ­a que me fuera del pueblo. 'AquÃ­ siempre vas a ser la novia desechada', dijo. Pero yo querÃ­a quedarme.",
                    "translation": "Meu pai queria que eu fosse embora do pueblo. 'Aqui sempre vais ser a noiva rejeitada', disse. Mas eu queria ficar.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'yo querÃ­a quedarme'. Duas palavras juntas â€” 'querÃ­a' + 'quedarme'. Significa:",
                    "options": [
                        {"id": "a", "text": "Eu queria ficar (uma coisa sÃ³)"},
                        {"id": "b", "text": "Eu fico (agora)"},
                        {"id": "c", "text": "Vou ficar"},
                        {"id": "d", "text": "Sou ficar"},
                    ],
                    "correct": "a",
                    "word_id": "es_queria", "target": "querÃ­a quedarme", "native": "queria ficar",
                    "npc_reaction": "QuerÃ­a quedarme. La razÃ³n es lo que viene despuÃ©s de 'querÃ­a'. Y me quedÃ©.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Ã‰l se casÃ³ con la otra. Tuvieron una hija. Yo nunca me casÃ©. Nunca tuve hijos.",
                    "translation": "Ele se casou com a outra. Tiveram uma filha. Eu nunca casei. Nunca tive filhos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel pergunta baixo: 'Carmen â€” Â¿y todavÃ­a lo amas?' Carmen responde firme:",
                    "options": [
                        {"id": "a", "text": "No. Ya no lo amo"},
                        {"id": "b", "text": "SÃ­, todavÃ­a lo amo"},
                        {"id": "c", "text": "Voy a amarlo"},
                        {"id": "d", "text": "Soy amor"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "nÃ£o",
                    "npc_reaction": "No. Hace dÃ©cadas que no. Pero recuerdo. Y Ã©l recuerda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Por eso me trata frÃ­o en el ayuntamiento. Tiene miedo de que yo cuente â€” al pueblo entero â€” cÃ³mo se sometiÃ³ a su padre.",
                    "translation": "Por isso ele me trata frio no ayuntamiento. Tem medo que eu conte â€” pro pueblo inteiro â€” como se subjugou ao pai.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a processa. 'Entonces â€” el Alcalde tiene una debilidad. El miedo a la vergÃ¼enza.' Pra vocÃª concordar com SofÃ­a (algo que vamos fazer):",
                    "options": [
                        {"id": "a", "text": "Vamos a usar eso si hace falta"},
                        {"id": "b", "text": "Voy a usar"},
                        {"id": "c", "text": "Va a usar"},
                        {"id": "d", "text": "Soy usar"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos. Pero con cuidado â€” Carmen no quiere usar esto como arma.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "No. No es para usar como arma. Es para que entiendan al hombre. El miedo lo mueve.",
                    "translation": "NÃ£o. NÃ£o Ã© pra usar como arma. Ã‰ pra vocÃªs entenderem o homem. O medo o move.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen agradece o esforÃ§o de vocÃªs. VocÃª devolve formal:",
                    "options": [
                        {"id": "a", "text": "Gracias, Carmen"},
                        {"id": "b", "text": "AdiÃ³s Carmen"},
                        {"id": "c", "text": "Tengo Carmen"},
                        {"id": "d", "text": "Soy gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, joven. Eso era lo que tenÃ­a que decir.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Caminho de volta pra casa. Os 3 jovens conversando baixo. ApresentaÃ§Ã£o
    # formal de "quiero/quieres/quiere + verbo". Sem nomear "querer infinitivo".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Miguel"],
                "story": (
                    "VocÃªs saÃ­ram da plaza. Carmen voltou ao bordado. O sol jÃ¡ "
                    "comeÃ§ava a baixar. Andaram em silÃªncio pelas primeiras "
                    "ruas â€” depois SofÃ­a comeÃ§ou a falar.\n\n"
                    "'Carmen dijo varias veces â€” querÃ­a casarme, querÃ­a quedarme. "
                    "Es algo Ãºtil â€” lo voy a explicar.'"
                ),
                "now": "SofÃ­a mostra como dizer o que se quer fazer.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Cuando juntas 'quiero' con otro verbo, dices lo que quieres hacer. Yo quiero comer. Yo quiero dormir. Yo quiero hablar.",
                    "translation": "Quando vocÃª junta 'quiero' com outro verbo, diz o que vocÃª quer fazer. Eu quero comer. Eu quero dormir. Eu quero falar.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Quiero + verbo",
                    "meaning": "O que vocÃª quer fazer",
                    "note": "junta dos palabras â€” quiero comer, quiero hablar, quiero saber",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo quiero ",  "isKey": True},
                        {"text": "comer Â· ",    "isKey": False},
                        {"text": "TÃº quieres ", "isKey": True},
                        {"text": "saber Â· ",    "isKey": False},
                        {"text": "Ella quiere ","isKey": True},
                        {"text": "hablar",      "isKey": False},
                    ],
                    "example": "Quiero comer pan. Â¿Quieres saber la verdad? Carmen quiere hablar.",
                    "translation": "Quero comer pÃ£o. VocÃª quer saber a verdade? Carmen quer falar.",
                    "note": "quiero / quieres / quiere â€” cambia con quien quiere. Igual que voy/vas/va de F11.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Pra dizer que VOCÃŠ quer voltar pra casa agora:",
                    "options": [
                        {"id": "a", "text": "Yo quiero volver a casa"},
                        {"id": "b", "text": "TÃº quieres volver a casa"},
                        {"id": "c", "text": "Ella quiere volver"},
                        {"id": "d", "text": "Voy a volver"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero volver", "native": "quero voltar",
                    "npc_reaction": "Quiero â€” yo, primera. Cuando hablas de ti mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel pergunta pra SofÃ­a: 'TÃº ___ saber mÃ¡s, Â¿verdad?' (SofÃ­a sempre quer saber mais)",
                    "options": [
                        {"id": "a", "text": "quieres"},
                        {"id": "b", "text": "quiero"},
                        {"id": "c", "text": "quiere"},
                        {"id": "d", "text": "queremos"},
                    ],
                    "correct": "a",
                    "word_id": "es_quieres", "target": "quieres", "native": "queres",
                    "npc_reaction": "Quieres â€” tÃº, segunda. Cuando le hablas a alguien.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pra casa onde Carmen mora hÃ¡ 40 anos â€” palavra de mulher, uma sÃ³:",
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
                    "question": "Miguel aponta pra SofÃ­a: 'Y eso que ella te dijo â€” ___ palabras de Carmen son importantes.' Mulheres + muitas â€” qual palavrinha vai na frente?",
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

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # VocÃªs 3 chegam Ã  casa de Don Miguel. MarÃ­a estava na porta. Pergunta
    # onde estiveram. VocÃª mente pela primeira vez. TensÃ£o silenciosa.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "VocÃªs trÃªs chegaram Ã  porta da casa de Don Miguel. "
                    "Estava aberta. MarÃ­a sentada na soleira â€” tomando uma "
                    "infusÃ£o. Ela os viu chegar.\n\n"
                    "'Forastero â€” Â¿dÃ³nde estuviste? Te busquÃ© en la herrerÃ­a.'"
                ),
                "now": "Primeira mentira deliberada do protagonista pra MarÃ­a.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Forastero â€” Â¿dÃ³nde estuvieron los tres? Te busquÃ©.",
                    "translation": "Forasteiro â€” onde vocÃªs trÃªs estiveram? Te procurei.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "SofÃ­a olha pra vocÃª. Miguel olha pra vocÃª. VocÃª Ã© quem "
                        "precisa responder. MarÃ­a espera â€” calma, sem pressÃ£o "
                        "Ã³bvia. Mas o silÃªncio dela Ã© peso."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª decide mentir. Resposta segura â€” vocÃªs estavam na herrerÃ­a com Eduardo (algo que MarÃ­a pode verificar mas que nÃ£o tem grande consequÃªncia se descobrir):",
                    "options": [
                        {"id": "a", "text": "Fuimos a la herrerÃ­a"},
                        {"id": "b", "text": "Fuimos a casa de Carmen"},
                        {"id": "c", "text": "Vamos a la plaza"},
                        {"id": "d", "text": "Soy herrerÃ­a"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuimos", "target": "fuimos", "native": "fomos",
                    "npc_reaction": "A la herrerÃ­a. Mmm. Â¿Y quÃ© querÃ­an allÃ¡?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª continua a mentira â€” usando 'querer + verbo' (querer ver Eduardo):",
                    "options": [
                        {"id": "a", "text": "QuerÃ­amos ver a Eduardo"},
                        {"id": "b", "text": "Voy a ver"},
                        {"id": "c", "text": "Tengo Eduardo"},
                        {"id": "d", "text": "Soy Eduardo"},
                    ],
                    "correct": "a",
                    "word_id": "es_queriamos", "target": "querÃ­amos", "native": "querÃ­amos",
                    "npc_reaction": "QuerÃ­amos ver a Eduardo. Bueno. Â¿Para quÃ©?",
                },
                {
                    "kind": "narrative",
                    "text": "SofÃ­a intervÃ©m â€” rÃ¡pida, como sempre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Yo querÃ­a pedirle que me hiciera un cuchillo nuevo. El mÃ­o se me rompiÃ³ ayer.",
                    "translation": "Eu queria pedir pra ele me fazer uma faca nova. A minha quebrou ontem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a aceita â€” visivelmente. 'Bueno. Y tÃº â€” forastero â€” Â¿cÃ³mo estÃ¡s despuÃ©s de tanta caminata?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Voy a hacer un tÃ© de hierbas para todos. Entren.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "MarÃ­a se levantou. Foi pra cozinha. VocÃªs trÃªs entraram "
                        "atrÃ¡s dela â€” em silÃªncio.\n\n"
                        "VocÃª nunca tinha mentido antes pra ela. Sentiu o peso. "
                        "SofÃ­a apertou seu braÃ§o discretamente â€” 'aguanta'."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Hijo de mi padre â€” ya estamos en esto contigo. No es solo tuyo.",
                    "translation": "Filho do meu pai â€” jÃ¡ estamos nisso contigo. NÃ£o Ã© sÃ³ seu.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "VocÃª agradece Miguel â€” baixo, sincero:",
                    "options": [
                        {"id": "a", "text": "Gracias, Miguel"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Soy gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Pra isso somos hermanos en esto.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Noite. MarÃ­a faz o tÃ©. VocÃªs 4 sentados. MarÃ­a comeÃ§a a fazer perguntas
    # outra vez â€” sobre o forastero. VocÃª precisa responder sem entregar.
    # Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "MarÃ­a serviu o tÃ©. Quente, aromÃ¡tico. Hierba conocida â€” "
                    "talvez. VocÃªs 4 sentados em volta da mesa baixa. Lamparina "
                    "no centro.\n\n"
                    "'Aprovecho â€” querÃ­a preguntarles algunas cosas.'"
                ),
                "now": "MarÃ­a testa. Cada resposta sua precisa proteger o grupo.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸ•¯ï¸ Cozinha Â· Lamparina baixa Â· TÃ© quente Â· Quatro Ã  mesa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Forastero â€” Â¿quieres mÃ¡s tÃ©?",
                    "translation": "Forasteiro â€” quer mais chÃ¡?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª nÃ£o quer â€” mas quer responder educado. NegaÃ§Ã£o simples:",
                    "options": [
                        {"id": "a", "text": "No, gracias"},
                        {"id": "b", "text": "SÃ­, mucho"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_gracias", "target": "no, gracias", "native": "nÃ£o, obrigado",
                    "npc_reaction": "Como quieras. Bueno â€” pregunta. Carmen estuvo en la plaza esta tarde â€” Don Miguel me lo dijo cuando volviÃ³ del campo. Â¿TÃº la viste?",
                    "gated": True,
                },
                {
                    "kind": "player",
                    "text": (
                        "MarÃ­a sabe que vocÃªs viram Carmen. VocÃª precisa dizer SIM â€” "
                        "mas controlar como muito ela ouviu. SofÃ­a aperta o copo "
                        "discretamente."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Resposta segura â€” vocÃªs viram Carmen mas sÃ³ de longe:",
                    "options": [
                        {"id": "a", "text": "SÃ­, la vi de lejos"},
                        {"id": "b", "text": "No la vi"},
                        {"id": "c", "text": "Voy a verla"},
                        {"id": "d", "text": "Soy Carmen"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "De lejos. Bueno. Â¿Y hablaste con ella?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª responde â€” nÃ£o, nÃ£o falou (vocÃªs falaram, mas vocÃª nega):",
                    "options": [
                        {"id": "a", "text": "No, no hablÃ© con ella"},
                        {"id": "b", "text": "SÃ­, hablÃ© mucho"},
                        {"id": "c", "text": "Voy a hablar"},
                        {"id": "d", "text": "Soy hablar"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "nÃ£o",
                    "npc_reaction": "No. Mmm. Carmen es de pocas palabras cuando borda. Hace bien.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "MarÃ­a dÃ¡ um sorriso pequeno. Aceitou. VocÃª sente o suor "
                        "frio nas costas â€” nÃ£o sabe se ela acreditou. SofÃ­a olha "
                        "pra Miguel â€” Miguel acena baixo."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Bueno â€” Â¿cÃ³mo estÃ¡s ahora, despuÃ©s de tanto dÃ­a?",
                    "translation": "Bom â€” como vocÃª estÃ¡ agora, depois de tanto dia?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Honestidade dupla â€” cansado mas firme:",
                    "options": [
                        {"id": "a", "text": "Estoy cansado, pero bien"},
                        {"id": "b", "text": "Soy cansado"},
                        {"id": "c", "text": "Tengo cansado"},
                        {"id": "d", "text": "Voy cansado"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_cansado", "target": "estoy cansado", "native": "estou cansado",
                    "npc_reaction": "Cansado. Voy a darte una infusiÃ³n para que duermas bien. Esta noche necesitas descansar.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F17 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸŒ™ Quarto Â· Frasco da infusÃ£o de MarÃ­a na mesinha Â· VocÃª sozinho",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª olhou pra infusÃ£o de MarÃ­a. Lembrou â€” ela tambÃ©m "
                        "te deu uma da Ãºltima vez (F10). Naquela noite, dormiu "
                        "profundo demais.\n\n"
                        "Hoje vocÃª nÃ£o bebeu. Despejou pela janela em silÃªncio.\n\n"
                        "Quando dormiu â€” Don Miguel bateu na porta. Acordou vocÃª. "
                        "'Hijo â€” maÃ±ana al amanecer. Vamos a hacer lo de Eduardo. "
                        "Lo de la espalda.'"
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
