"""
Seed das 6 seÃ§Ãµes da Fase 24 Espanhol A1 â€” "La vÃ­spera del juicio".

Cela do ayuntamiento. Frio. Pedra Ãºmida. Don Miguel suborna o guarda
da noite â€” uma hora. SofÃ­a, Miguel e MarÃ­a entram. Ãšltima revisÃ£o
antes do julgamento.

Vocab novo (2): juicio Â· cÃ¡rcel
Linguagem nova: deber + verbo (dever / Ã© provÃ¡vel)
    "Debes estar listo." / "Debe llegar pronto."

Item dinÃ¢mica: item_moment crÃ­tico â€” Hierba de MarÃ­a (sleep aid).
Pra dormir antes do dia mais difÃ­cil.
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "ðŸŒ’ Cela do ayuntamiento Â· Noite Â· Pedra Ãºmida Â· Lamparina baixa"},
                {"kind": "narrative", "text": "VocÃª sentado no banco de pedra. Frio entrando pelas paredes. Ouve passos no corredor â€” quatro pares."},
                {"kind": "npc", "npc": "Don Miguel", "line": "Le paguÃ© al guardia. Una hora. Hablamos rÃ¡pido.", "pace": "urgent"},
                {"kind": "player", "text": "SofÃ­a, Miguel e MarÃ­a entram atrÃ¡s dele. Carmen ficou de fora â€” ela vai testemunhar amanhÃ£, nÃ£o pode ser vista visitando."},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "juicio", "native": "julgamento"},
                    {"target": "cÃ¡rcel", "native": "prisÃ£o / cela"},
                    {"target": "deber",  "native": "dever (obrigaÃ§Ã£o moral / probabilidade)"},
                ]},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "VocÃª cumprimenta â€” noite tarde:",
                 "options": [
                     {"id": "a", "text": "Buenas noches"},
                     {"id": "b", "text": "Buenos dÃ­as"},
                     {"id": "c", "text": "AdiÃ³s"},
                     {"id": "d", "text": "Mal"},
                 ], "correct": "a",
                 "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                 "npc_reaction": "Buenas noches. Esta es la Ãºltima noche aquÃ­ â€” sea como sea."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "'Juicio' significa:",
                 "options": [
                     {"id": "a", "text": "Julgamento"},
                     {"id": "b", "text": "Festa"},
                     {"id": "c", "text": "Comida"},
                     {"id": "d", "text": "Carta"},
                 ], "correct": "a",
                 "word_id": "es_juicio", "target": "juicio", "native": "julgamento",
                 "npc_reaction": "Juicio. MaÃ±ana. Y tienes que estar listo."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Don Miguel", "MarÃ­a", "SofÃ­a"], "story": "MarÃ­a revisou tudo. Don Miguel ensaiou trÃªs respostas-padrÃ£o. SofÃ­a decorou a ordem das testemunhas. Ãšltima revisÃ£o.", "now": "RevisÃ£o sob pressÃ£o. Errar nada importante."},
            "steps": [
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Â¿CÃ³mo te llamas?", "translation": "Como vocÃª se chama?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Resposta:",
                 "options": [
                     {"id": "a", "text": "Me llamo [seu nome]"},
                     {"id": "b", "text": "Soy forastero"},
                     {"id": "c", "text": "Tengo aÃ±os"},
                     {"id": "d", "text": "AdiÃ³s"},
                 ], "correct": "a",
                 "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                 "npc_reaction": "Bien."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Â¿CuÃ¡ntos aÃ±os?", "translation": "Quantos anos?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Idade:",
                 "options": [
                     {"id": "a", "text": "Tengo veinte aÃ±os"},
                     {"id": "b", "text": "Soy veinte"},
                     {"id": "c", "text": "Estoy veinte"},
                     {"id": "d", "text": "Voy veinte"},
                 ], "correct": "a",
                 "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                 "npc_reaction": "Veinte. Joven â€” pero el Alcalde no respeta jÃ³venes."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Â¿De dÃ³nde vienes?", "translation": "De onde vocÃª vem?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Resposta segura (nÃ£o revelar o nome da F22):",
                 "options": [
                     {"id": "a", "text": "No me acuerdo"},
                     {"id": "b", "text": "Soy de aquÃ­"},
                     {"id": "c", "text": "Voy lejos"},
                     {"id": "d", "text": "Tengo lejos"},
                 ], "correct": "a",
                 "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "nÃ£o me lembro",
                 "npc_reaction": "Bueno. Si dice 'mientes', dile que MarÃ­a te examinÃ³ la cabeza y confirmÃ³ la pÃ©rdida de memoria."},
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Â¿Y de mÃ­ â€” quÃ© dices?", "translation": "E sobre mim â€” o que vocÃª diz?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Resposta segura â€” vocÃª sabe pouco dela:",
                 "options": [
                     {"id": "a", "text": "Es la curandera"},
                     {"id": "b", "text": "Es mi familia"},
                     {"id": "c", "text": "Era Sangra"},
                     {"id": "d", "text": "Vi a MarÃ­a"},
                 ], "correct": "a",
                 "word_id": "es_es", "target": "es", "native": "Ã©",
                 "npc_reaction": "Es la curandera. Nada mÃ¡s."},
                {"kind": "npc_speak", "npc": "SofÃ­a", "line": "Â¿Y cÃ³mo estÃ¡s ahora?", "translation": "E como vocÃª estÃ¡ agora?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "SofÃ­a",
                 "question": "Honesto â€” nervoso, mas firme:",
                 "options": [
                     {"id": "a", "text": "Tengo miedo, pero estoy listo"},
                     {"id": "b", "text": "Estoy bien sin miedo"},
                     {"id": "c", "text": "Soy miedo"},
                     {"id": "d", "text": "Voy listo"},
                 ], "correct": "a",
                 "word_id": "es_tengo_miedo", "target": "tengo miedo", "native": "tenho medo",
                 "npc_reaction": "Las dos cosas. Lo correcto."},
            ],
        },
    },
    {
        "section_number": 3, "section_type": "pratica_aplicada",
        "content": {
            "recap": {"characters": ["MarÃ­a", "Don Miguel"], "story": "MarÃ­a tira do bolso o frasco da Hierba â€” versÃ£o concentrada. Pra dormir essa Ãºltima noite.", "now": "item_moment crÃ­tico â€” usar a hierba pra dormir bem antes do juicio."},
            "steps": [
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "MaÃ±ana necesitas cabeza clara. Si tienes algo en la bolsa que te calme â€” Ãºsalo ahora.", "translation": "AmanhÃ£ vocÃª precisa de cabeÃ§a clara. Se vocÃª tem algo na mochila que te acalme â€” usa agora.", "pace": "slow"},
                {
                    "kind": "item_moment",
                    "npc": "MarÃ­a",
                    "situation": "VocÃª tem que dormir. NÃ£o tem como ser bom amanhÃ£ sem dormir hoje.",
                    "npc_line": "BÃ©bete una hierba si tienes. O agua, si no.",
                    "item_tag": "remedio",
                    "on_use": {
                        "narrative": "VocÃª abriu a hierba. Cheiro forte de eucalipto e algo amargo. Tomou em trÃªs goles.",
                        "npc_reaction": "Bueno. Vas a dormir profundo. MaÃ±ana â€” la cabeza te va a obedecer.",
                        "bonus": "reduce_gated",
                    },
                    "on_skip": {
                        "npc_reaction": "EstÃ¡ bien â€” agua y respiraciÃ³n profunda tambiÃ©n funcionan. Pero menos.",
                    },
                },
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Una cosa mÃ¡s â€” el Alcalde debe estar nervioso tambiÃ©n. Mucho estÃ¡ en juego para Ã©l. Si pierde â€” pierde poder.", "translation": "Mais uma coisa â€” o Alcalde deve estar nervoso tambÃ©m. Muito tÃ¡ em jogo pra ele. Se ele perder â€” perde poder.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Don Miguel disse 'el Alcalde debe estar nervioso'. A palavra 'debe' significa:",
                 "options": [
                     {"id": "a", "text": "Deve estar (provavelmente estÃ¡)"},
                     {"id": "b", "text": "Pode estar"},
                     {"id": "c", "text": "Vai estar"},
                     {"id": "d", "text": "Era nervoso"},
                 ], "correct": "a",
                 "word_id": "es_debe", "target": "debe", "native": "deve (provavelmente)",
                 "npc_reaction": "Debe â€” probabilidad. 'Debe estar' = 'es probable que estÃ©'. No es certeza."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Pra vocÃª dizer 'devo dormir agora' (obrigaÃ§Ã£o suave):",
                 "options": [
                     {"id": "a", "text": "Debo dormir"},
                     {"id": "b", "text": "Voy dormir"},
                     {"id": "c", "text": "Soy dormir"},
                     {"id": "d", "text": "Tengo dormir"},
                 ], "correct": "a",
                 "word_id": "es_debo", "target": "debo", "native": "devo",
                 "npc_reaction": "Debo. Yo â€” primera. Pero 'tengo que dormir' tambiÃ©n sirve."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["Don Miguel"], "story": "Ãšltima explicaÃ§Ã£o. Don Miguel quer que vocÃª entenda a diferenÃ§a entre 'debo' (obrigaÃ§Ã£o suave / probabilidade) e 'tengo que' (obrigaÃ§Ã£o forte).", "now": "DiferenÃ§a prÃ¡tica."},
            "steps": [
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "'Tengo que' es fuerte â€” la situaciÃ³n obliga. 'Debo' es mÃ¡s suave â€” moral, decisiÃ³n propia. Las dos sirven.", "translation": "'Tengo que' Ã© forte â€” a situaÃ§Ã£o obriga. 'Debo' Ã© mais suave â€” moral, decisÃ£o prÃ³pria. As duas servem.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Debo / debes / debe + verbo", "meaning": "Devo / deves / deve â€” obrigaÃ§Ã£o moral OU probabilidade", "note": "diferente de 'tengo que' (situaÃ§Ã£o obriga) e 'puedo' (capaz de)"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Yo debo ", "isKey": True}, {"text": "decir la verdad Â· ", "isKey": False},
                     {"text": "TÃº debes ", "isKey": True}, {"text": "estar listo Â· ", "isKey": False},
                     {"text": "Ã‰l debe ", "isKey": True}, {"text": "estar nervioso", "isKey": False},
                 ],
                 "example": "Yo debo decir la verdad. TÃº debes estar listo. El Alcalde debe estar nervioso.",
                 "translation": "Eu devo dizer a verdade. VocÃª deve estar pronto. O Alcalde deve estar nervoso.",
                 "note": "debo / debes / debe â€” pode ser dever moral OU 'provavelmente estÃ¡'."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "VocÃª quer dizer 'devo estar pronto' (dever pessoal):",
                 "options": [
                     {"id": "a", "text": "Debo estar listo"},
                     {"id": "b", "text": "Soy listo"},
                     {"id": "c", "text": "Voy listo"},
                     {"id": "d", "text": "Tengo listo"},
                 ], "correct": "a",
                 "word_id": "es_debo", "target": "debo", "native": "devo",
                 "npc_reaction": "Debo. Yo. Bueno."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Pra falar do Alcalde (provavelmente nervoso):",
                 "options": [
                     {"id": "a", "text": "El Alcalde debe estar nervioso"},
                     {"id": "b", "text": "Yo debo nervioso"},
                     {"id": "c", "text": "Voy nervioso"},
                     {"id": "d", "text": "Soy nervioso"},
                 ], "correct": "a",
                 "word_id": "es_debe", "target": "debe", "native": "deve (provavelmente)",
                 "npc_reaction": "Debe. Probabilidad â€” no certeza. Ãštil pra hablar de los otros."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["MarÃ­a", "SofÃ­a", "Miguel"], "story": "Hora acaba. Guarda volta. VocÃªs se despedem â€” sem drama, sem promessas.", "now": "Ãšltima conversa antes do amanhecer."},
            "steps": [
                {"kind": "npc_speak", "npc": "SofÃ­a", "line": "MaÃ±ana. Carmen ya tiene su discurso preparado.", "translation": "AmanhÃ£. Carmen jÃ¡ tem o discurso preparado.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "SofÃ­a",
                 "question": "VocÃª agradece todo o grupo pela ajuda:",
                 "options": [
                     {"id": "a", "text": "Gracias a los cuatro"},
                     {"id": "b", "text": "AdiÃ³s a todos"},
                     {"id": "c", "text": "Mal a todos"},
                     {"id": "d", "text": "Soy gracias"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "De nada. Cuando termine el juicio â€” todos juntos. Tomamos algo."},
                {"kind": "npc_speak", "npc": "Miguel", "line": "Forastero â€” recuerda. Tu nombre verdadero estÃ¡ en el envelope. Cuando salgas â€” lÃ©elo.", "translation": "Forasteiro â€” lembra. Teu nome verdadeiro tÃ¡ no envelope. Quando sair â€” lÃª.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Miguel",
                 "question": "VocÃª confirma â€” vai ler quando puder (futuro com 'cuando'):",
                 "options": [
                     {"id": "a", "text": "Cuando salga, lo leo"},
                     {"id": "b", "text": "Ya leo"},
                     {"id": "c", "text": "Voy leer"},
                     {"id": "d", "text": "Soy leer"},
                 ], "correct": "a",
                 "word_id": "es_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando salgas. Vas a salir â€” eso lo sabemos."},
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Y si te preguntan por la primera palabra de la carta â€” di 'no recuerdo'.", "translation": "E se te perguntarem pela primeira palavra da carta â€” diz 'nÃ£o me lembro'.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Si me preguntan, digo 'no recuerdo'"},
                     {"id": "b", "text": "Cuando me preguntan, voy"},
                     {"id": "c", "text": "Soy preguntar"},
                     {"id": "d", "text": "Tengo no recuerdo"},
                 ], "correct": "a",
                 "word_id": "es_si_condicional", "target": "si", "native": "se (condiÃ§Ã£o)",
                 "npc_reaction": "Si me preguntan. Bueno."},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["MarÃ­a"], "story": "Os trÃªs saÃ­ram. VocÃª ficou sozinho na cela com a infusÃ£o de MarÃ­a. A noite mais longa de todas.", "now": "VocÃª precisa dormir. Mas antes â€” uma decisÃ£o final. Errar trava."},
            "steps": [
                {"kind": "scene", "text": "ðŸŒ™ Cela escura Â· Lamparina apagada Â· VocÃª sozinho Â· O envelope com o nome dentro"},
                {"kind": "player", "text": "VocÃª abre o envelope mais uma vez. LÃª o nome em voz baixa. Sente algo no peito â€” nÃ£o memÃ³ria, ainda. Mas reconhecimento."},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Pra vocÃª descrever como se sente â€” uma palavra. Honesto:",
                 "options": [
                     {"id": "a", "text": "Estoy nervioso, pero tambiÃ©n listo"},
                     {"id": "b", "text": "Soy bien"},
                     {"id": "c", "text": "Tengo bien"},
                     {"id": "d", "text": "Voy bien"},
                 ], "correct": "a",
                 "word_id": "es_estoy_nervioso", "target": "estoy nervioso", "native": "estou nervoso",
                 "npc_reaction": "Las dos cosas. Eso es ser humano.", "gated": True},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "VocÃª precisa decidir â€” vai contar tudo pro Alcalde se ele perguntar? DecisÃ£o firme: 'sÃ³ vou contar o que tenho que contar' (obrigaÃ§Ã£o):",
                 "options": [
                     {"id": "a", "text": "SÃ³lo cuento lo que tengo que contar"},
                     {"id": "b", "text": "Cuento todo"},
                     {"id": "c", "text": "Soy contar"},
                     {"id": "d", "text": "Voy contar"},
                 ], "correct": "a",
                 "word_id": "es_tengo_que", "target": "tengo que", "native": "tenho que",
                 "npc_reaction": "Bueno. Tienes que cuidar a Carmen, a Don Miguel, a MarÃ­a. Tu silencio los protege.", "gated": True},
                {"kind": "scene", "text": "ðŸŒ… VocÃª adormece com o envelope na mÃ£o Â· A primeira luz comeÃ§a a entrar"},
                {"kind": "narrative", "text": "VocÃª dormiu profundo. NÃ£o sonhou. Quando acordou â€” guardas batendo na porta. Amanheceu. Juicio."},
            ],
        },
    },
]
