"""
Seed das 6 seÃ§Ãµes da Fase 22 Espanhol A1 â€” "La verdad parcial".

Carmen entrega um envelope guardado hÃ¡ 20 anos pelo Buscador â€” pertence
ao forastero, nÃ£o a Don Miguel. Dentro: um NOME. NÃ£o 'forastero'.

Vocab novo (2): nombre Â· contar
Linguagem nova: contar / contar de / contar a (verbo 'contar' em diferentes usos)

Item dinÃ¢mica: 1 baÃº aberto durante a fase (S5 â€” Carmen entrega Carta Sellada
do pool raro). Sistema escolhe item pra esse user.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f22_sections [--reset]
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene",     "text": "ðŸŒž Plaza Â· Sol alto Â· Carmen no banco com um envelope nos joelhos"},
                {"kind": "npc",       "npc": "Carmen", "line": "Lo guardo hace veinte aÃ±os. Pertenece al forastero â€” no a Don Miguel.", "pace": "slow"},
                {"kind": "player",    "text": "SofÃ­a e Miguel atrÃ¡s. Don Miguel ao seu lado. VocÃªs quatro encarando o envelope."},
                {"kind": "npc",       "npc": "Carmen", "line": "Ãbrelo tÃº. Antes que llegue el Inspector.", "pace": "urgent"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "nombre", "native": "nome"},
                    {"target": "contar", "native": "contar / narrar"},
                ]},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "VocÃª cumprimenta Carmen:",
                 "options": [
                     {"id": "a", "text": "Buenos dÃ­as, Carmen"},
                     {"id": "b", "text": "Buenas noches"},
                     {"id": "c", "text": "AdiÃ³s"},
                     {"id": "d", "text": "Mal"},
                 ], "correct": "a",
                 "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                 "npc_reaction": "Buenos dÃ­as. Pero hoy no es dÃ­a de saludos largos."},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Carmen entrega o envelope. VocÃª agradece â€” formal, sincero:",
                 "options": [
                     {"id": "a", "text": "Gracias, Carmen"},
                     {"id": "b", "text": "AdiÃ³s Carmen"},
                     {"id": "c", "text": "Tengo Carmen"},
                     {"id": "d", "text": "Mal"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "De nada. Veinte aÃ±os guardÃ¡ndolo. Hoy es tuyo."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Carmen"], "story": "VocÃª ainda nÃ£o abriu o envelope. Carmen quer testar primeiro â€” pra ver se vocÃª tÃ¡ pronto pra ouvir.", "now": "RevisÃ£o. Carmen mistura tudo."},
            "steps": [
                {"kind": "npc_speak", "npc": "Carmen", "line": "Antes â€” dime quiÃ©n eres en este pueblo.", "translation": "Antes â€” me diz quem vocÃª Ã© nesse pueblo.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Identidade (SER):",
                 "options": [
                     {"id": "a", "text": "Soy forastero"},
                     {"id": "b", "text": "Estoy forastero"},
                     {"id": "c", "text": "Tengo forastero"},
                     {"id": "d", "text": "Voy forastero"},
                 ], "correct": "a",
                 "word_id": "es_soy", "target": "soy", "native": "sou",
                 "npc_reaction": "Hoy. MaÃ±ana â€” quizÃ¡ no."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "Â¿CuÃ¡ndo llegaste al pueblo? CuÃ©ntame en pasado.", "translation": "Quando vocÃª chegou no pueblo? Conta no passado.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "PretÃ©rito (vocÃª chegou):",
                 "options": [
                     {"id": "a", "text": "LleguÃ© hace tres semanas"},
                     {"id": "b", "text": "Llego hace tres semanas"},
                     {"id": "c", "text": "Voy a llegar"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_llegue", "target": "lleguÃ©", "native": "cheguei",
                 "npc_reaction": "Tres semanas. Y mucho cambiÃ³ en ti en este tiempo."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "Â¿Y la palabra de la carta â€” quÃ© leÃ­ste?", "translation": "E a palavra da carta â€” o que vocÃª leu?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "A palavra que vocÃª leu na F19:",
                 "options": [
                     {"id": "a", "text": "LeÃ­ 'vuelves'"},
                     {"id": "b", "text": "Leo 'vuelves'"},
                     {"id": "c", "text": "Voy a leer"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_lei", "target": "leÃ­", "native": "li",
                 "npc_reaction": "LeÃ­ste. Pasado. Y hoy â€” vas a leer una segunda."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "Â¿CÃ³mo te sientes ahora?", "translation": "Como vocÃª se sente agora?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Honesto â€” nervoso, mas firme:",
                 "options": [
                     {"id": "a", "text": "Estoy nervioso, pero listo"},
                     {"id": "b", "text": "Soy nervioso"},
                     {"id": "c", "text": "Tengo nervioso"},
                     {"id": "d", "text": "Voy nervioso"},
                 ], "correct": "a",
                 "word_id": "es_estoy_nervioso", "target": "estoy nervioso", "native": "estou nervoso",
                 "npc_reaction": "Bueno. Ãbrelo cuando estÃ©s listo. Toma tu tiempo."},
            ],
        },
    },
    {
        "section_number": 3, "section_type": "pratica_aplicada",
        "content": {
            "recap": {"characters": ["Carmen", "Don Miguel"], "story": "VocÃª abre o envelope com a navaja que Don Miguel passou. Papel velho, amarelado. Uma Ãºnica palavra escrita no meio.", "now": "VocÃª lÃª. Tudo muda."},
            "steps": [
                {"kind": "scene", "text": "ðŸ“œ Papel amarelado Â· Letra firme Â· No centro, um nome"},
                {"kind": "player", "text": "VocÃª lÃª. O nome NÃƒO Ã© 'forastero'. Ã‰ um nome prÃ³prio. VocÃª sente o peito apertar â€” vocÃª reconhece, mas nÃ£o lembra de onde."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "CuÃ©ntame â€” Â¿lo reconoces?", "translation": "Me conta â€” vocÃª reconhece?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "VocÃª reconhece â€” mas nÃ£o consegue lembrar de onde. Resposta hÃ­brida (sim e ainda nÃ£o):",
                 "options": [
                     {"id": "a", "text": "SÃ­, pero todavÃ­a no me acuerdo"},
                     {"id": "b", "text": "No, no conozco"},
                     {"id": "c", "text": "Voy a recordar"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_si", "target": "sÃ­", "native": "sim",
                 "npc_reaction": "SÃ­ pero todavÃ­a no. Eso es lo mÃ¡s honesto que puedes decir hoy."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Â¿Vas a contarles a SofÃ­a y Miguel ese nombre?", "translation": "VocÃª vai contar pra SofÃ­a e Miguel esse nome?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Sim â€” eles merecem saber (futuro prÃ³ximo, 1Âª pessoa):",
                 "options": [
                     {"id": "a", "text": "SÃ­, voy a contarles"},
                     {"id": "b", "text": "SÃ­, cuento"},
                     {"id": "c", "text": "SÃ­, soy contar"},
                     {"id": "d", "text": "SÃ­, tengo contar"},
                 ], "correct": "a",
                 "word_id": "es_voy_a", "target": "voy a contar", "native": "vou contar",
                 "npc_reaction": "Bueno. Sin guardar nada â€” eso ya no sirve."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "El verbo 'contar' tiene varios usos â€” te lo explico cuando termines.", "translation": "O verbo 'contar' tem vÃ¡rios usos â€” te explico quando vocÃª terminar.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Pra agradecer Carmen pelo envelope, depois de tantos anos:",
                 "options": [
                     {"id": "a", "text": "Gracias por guardarlo tanto tiempo"},
                     {"id": "b", "text": "AdiÃ³s Carmen"},
                     {"id": "c", "text": "Soy gracias"},
                     {"id": "d", "text": "Voy gracias"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "Lo guardÃ© porque me lo pidiÃ³ un buen hombre. Hoy lo entrego al heredero correcto."},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Carmen pergunta 'Â¿quÃ© vas a hacer con el nombre?'. Sua resposta â€” vai contar pros amigos:",
                 "options": [
                     {"id": "a", "text": "Voy a contarles a SofÃ­a y Miguel"},
                     {"id": "b", "text": "Voy contar"},
                     {"id": "c", "text": "Soy contar"},
                     {"id": "d", "text": "Tengo contar"},
                 ], "correct": "a",
                 "word_id": "es_contar", "target": "contar", "native": "contar",
                 "npc_reaction": "Bien. 'Contar' a alguien â€” dirigir tu historia a otra persona. Importante."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["Carmen"], "story": "Carmen quer te ensinar 'contar' direito â€” verbo simples mas com vÃ¡rias caras. Vai te servir muito.", "now": "Carmen explica 'contar'."},
            "steps": [
                {"kind": "npc_speak", "npc": "Carmen", "line": "'Contar' sirve para tres cosas â€” nÃºmeros, historias y secretos. Y cambia con quien.", "translation": "'Contar' serve para trÃªs coisas â€” nÃºmeros, histÃ³rias e segredos. E muda com quem.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Contar = contar / narrar / confiar segredo", "meaning": "verbo de mÃºltiplos usos", "note": "cuento, cuentas, cuenta, contamos â€” cambia con quien hace"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Yo cuento ", "isKey": True}, {"text": "una historia Â· ", "isKey": False},
                     {"text": "TÃº cuentas ", "isKey": True}, {"text": "monedas Â· ", "isKey": False},
                     {"text": "Ella cuenta ", "isKey": True}, {"text": "un secreto Â· ", "isKey": False},
                     {"text": "Contamos ", "isKey": True}, {"text": "juntos", "isKey": False},
                 ],
                 "example": "Yo cuento la historia. TÃº cuentas las monedas. MarÃ­a cuenta secretos.",
                 "translation": "Eu conto a histÃ³ria. VocÃª conta as moedas. MarÃ­a conta segredos.",
                 "note": "cuento / cuentas / cuenta / contamos â€” sempre algo depois (a coisa contada)"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "VocÃª quer dizer 'eu conto pra vocÃª' (1Âª pessoa):",
                 "options": [
                     {"id": "a", "text": "Yo te cuento"},
                     {"id": "b", "text": "TÃº cuentas"},
                     {"id": "c", "text": "Yo contamos"},
                     {"id": "d", "text": "Soy cuento"},
                 ], "correct": "a",
                 "word_id": "es_cuento", "target": "cuento", "native": "conto",
                 "npc_reaction": "Cuento â€” yo. Primera persona."},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "E pra perguntar 'vocÃª me conta?' (2Âª pessoa, pergunta):",
                 "options": [
                     {"id": "a", "text": "Â¿Me cuentas?"},
                     {"id": "b", "text": "Â¿Me cuento?"},
                     {"id": "c", "text": "Â¿Voy a contar?"},
                     {"id": "d", "text": "Â¿Soy contar?"},
                 ], "correct": "a",
                 "word_id": "es_cuentas", "target": "cuentas", "native": "contas",
                 "npc_reaction": "Cuentas â€” tÃº. La pregunta es directa."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["Carmen", "Don Miguel"], "story": "Carmen entrega uma segunda coisa antes de vocÃªs irem â€” um envelope menor, lacrado, do bolso interno do vestido dela.", "now": "VocÃª recebe um item raro. O baÃº abre aqui (sistema sorteia)."},
            "steps": [
                {"kind": "npc_speak", "npc": "Carmen", "line": "Esto tambiÃ©n es tuyo. Algo que ella te dejÃ³ â€” no sÃ© quÃ© es, pero pesa.", "translation": "Isso tambÃ©m Ã© teu. Algo que ela te deixou â€” nÃ£o sei o que Ã©, mas pesa.", "pace": "slow"},
                {"kind": "scene", "text": "ðŸŽ Envelope pequeno Â· Cera vermelha Â· SÃ­mbolo do sol partido"},
                {"kind": "narrative", "text": "VocÃª recebe um item raro â€” o sistema escolhe qual da fila do baÃº raro do seu user."},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "VocÃª agradece Carmen pela segunda entrega:",
                 "options": [
                     {"id": "a", "text": "Gracias por todo"},
                     {"id": "b", "text": "AdiÃ³s"},
                     {"id": "c", "text": "Soy gracias"},
                     {"id": "d", "text": "Voy gracias"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "De nada. Y cuando termine todo â€” ven a verme."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Carmen â€” gracias. Hoy entendemos mÃ¡s que en veinte aÃ±os.", "translation": "Carmen â€” obrigado. Hoje entendemos mais do que em vinte anos.", "pace": "slow"},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Don Miguel", "SofÃ­a", "Miguel"], "story": "Voltando da plaza, vocÃªs veem fumaÃ§a subindo do lado da casa de Don Miguel. SofÃ­a corre.", "now": "Crise. Errar trava."},
            "steps": [
                {"kind": "scene", "text": "ðŸ”¥ FumaÃ§a subindo Â· Casa de Don Miguel Â· TrÃªs homens uniformizados na porta"},
                {"kind": "npc_speak", "npc": "SofÃ­a", "line": "Â¡Vinieron! Â¡Antes de lo esperado!", "translation": "Vieram! Antes do esperado!", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "SofÃ­a",
                 "question": "VocÃª reage rÃ¡pido. Pra dizer 'preciso ir' (obrigaÃ§Ã£o, 1Âª pessoa):",
                 "options": [
                     {"id": "a", "text": "Tengo que ir"},
                     {"id": "b", "text": "Voy a ir"},
                     {"id": "c", "text": "Quiero ir"},
                     {"id": "d", "text": "Soy ir"},
                 ], "correct": "a",
                 "word_id": "es_tengo_que", "target": "tengo que", "native": "tenho que",
                 "npc_reaction": "Tienes que. Pero no solo â€” vamos los cuatro.", "gated": True},
                {"kind": "multiple_choice", "npc": "Miguel",
                 "question": "Miguel: 'Espera â€” Â¿quÃ© dice el nombre que leÃ­ste?' VocÃª ainda nÃ£o vai dizer:",
                 "options": [
                     {"id": "a", "text": "Cuando estemos seguros â€” te cuento"},
                     {"id": "b", "text": "Ya te cuento"},
                     {"id": "c", "text": "Voy a leer"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando â€” bien. Hoy guardas. MaÃ±ana cuentas.", "gated": True},
                {"kind": "narrative", "text": "VocÃªs quatro correm. MarÃ­a sai pela porta de trÃ¡s. O Alcalde estÃ¡ no meio da rua â€” atrÃ¡s dos trÃªs guardas. 'MaÃ±ana es el juicio.'"},
            ],
        },
    },
]
