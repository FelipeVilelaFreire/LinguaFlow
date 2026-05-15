"""
Seed das 6 seções da Fase 22 Espanhol A1 — "La verdad parcial".

Carmen entrega um envelope guardado há 20 anos pelo Buscador — pertence
ao forastero, não a Don Miguel. Dentro: um NOME. Não 'forastero'.

Vocab novo (2): nombre · contar
Linguagem nova: contar / contar de / contar a (verbo 'contar' em diferentes usos)

Item dinâmica: 1 baú aberto durante a fase (S5 — Carmen entrega Carta Sellada
do pool raro). Sistema escolhe item pra esse user.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f22_sections [--reset]
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "investigacion",
                    "min_level": 3,
                    "uses_item_tag": "documento",
                    "success": "Voce percebe a dobra falsa do envelope antes de Greta mudar de assunto.",
                    "fallback": "Greta muda de assunto rapido, mas a verdade parcial ainda passa pela fresta.",
                },
                {"kind": "scene",     "text": "🌞 Plaza · Sol alto · Carmen no banco com um envelope nos joelhos"},
                {"kind": "npc",       "npc": "Carmen", "line": "Lo guardo hace veinte años. Pertenece al forastero — no a Don Miguel.", "pace": "slow"},
                {"kind": "player",    "text": "Sofía e Miguel atrás. Don Miguel ao seu lado. Vocês quatro encarando o envelope."},
                {"kind": "npc",       "npc": "Carmen", "line": "Ábrelo tú. Antes que llegue el Inspector.", "pace": "urgent"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "nombre", "native": "nome"},
                    {"target": "contar", "native": "contar / narrar"},
                ]},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Você cumprimenta Carmen:",
                 "options": [
                     {"id": "a", "text": "Buenos días, Carmen"},
                     {"id": "b", "text": "Buenas noches"},
                     {"id": "c", "text": "Adiós"},
                     {"id": "d", "text": "Mal"},
                 ], "correct": "a",
                 "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                 "npc_reaction": "Buenos días. Pero hoy no es día de saludos largos."},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Carmen entrega o envelope. Você agradece — formal, sincero:",
                 "options": [
                     {"id": "a", "text": "Gracias, Carmen"},
                     {"id": "b", "text": "Adiós Carmen"},
                     {"id": "c", "text": "Tengo Carmen"},
                     {"id": "d", "text": "Mal"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "De nada. Veinte años guardándolo. Hoy es tuyo."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Carmen"], "story": "Você ainda não abriu o envelope. Carmen quer testar primeiro — pra ver se você tá pronto pra ouvir.", "now": "Revisão. Carmen mistura tudo."},
            "steps": [
                {"kind": "npc_speak", "npc": "Carmen", "line": "Antes — dime quién eres en este pueblo.", "translation": "Antes — me diz quem você é nesse pueblo.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Identidade (SER):",
                 "options": [
                     {"id": "a", "text": "Soy forastero"},
                     {"id": "b", "text": "Estoy forastero"},
                     {"id": "c", "text": "Tengo forastero"},
                     {"id": "d", "text": "Voy forastero"},
                 ], "correct": "a",
                 "word_id": "es_soy", "target": "soy", "native": "sou",
                 "npc_reaction": "Hoy. Mañana — quizá no."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "¿Cuándo llegaste al pueblo? Cuéntame en pasado.", "translation": "Quando você chegou no pueblo? Conta no passado.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Pretérito (você chegou):",
                 "options": [
                     {"id": "a", "text": "Llegué hace tres semanas"},
                     {"id": "b", "text": "Llego hace tres semanas"},
                     {"id": "c", "text": "Voy a llegar"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_llegue", "target": "llegué", "native": "cheguei",
                 "npc_reaction": "Tres semanas. Y mucho cambió en ti en este tiempo."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "¿Y la palabra de la carta — qué leíste?", "translation": "E a palavra da carta — o que você leu?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "A palavra que você leu na F19:",
                 "options": [
                     {"id": "a", "text": "Leí 'vuelves'"},
                     {"id": "b", "text": "Leo 'vuelves'"},
                     {"id": "c", "text": "Voy a leer"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_lei", "target": "leí", "native": "li",
                 "npc_reaction": "Leíste. Pasado. Y hoy — vas a leer una segunda."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "¿Cómo te sientes ahora?", "translation": "Como você se sente agora?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Honesto — nervoso, mas firme:",
                 "options": [
                     {"id": "a", "text": "Estoy nervioso, pero listo"},
                     {"id": "b", "text": "Soy nervioso"},
                     {"id": "c", "text": "Tengo nervioso"},
                     {"id": "d", "text": "Voy nervioso"},
                 ], "correct": "a",
                 "word_id": "es_estoy_nervioso", "target": "estoy nervioso", "native": "estou nervoso",
                 "npc_reaction": "Bueno. Ábrelo cuando estés listo. Toma tu tiempo."},
            ],
        },
    },
    {
        "section_number": 3, "section_type": "pratica_aplicada",
        "content": {
            "recap": {"characters": ["Carmen", "Don Miguel"], "story": "Você abre o envelope com a navaja que Don Miguel passou. Papel velho, amarelado. Uma única palavra escrita no meio.", "now": "Você lê. Tudo muda."},
            "steps": [
                {"kind": "scene", "text": "📜 Papel amarelado · Letra firme · No centro, um nome"},
                {"kind": "player", "text": "Você lê. O nome NÃO é 'forastero'. É um nome próprio. Você sente o peito apertar — você reconhece, mas não lembra de onde."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "Cuéntame — ¿lo reconoces?", "translation": "Me conta — você reconhece?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Você reconhece — mas não consegue lembrar de onde. Resposta híbrida (sim e ainda não):",
                 "options": [
                     {"id": "a", "text": "Sí, pero todavía no me acuerdo"},
                     {"id": "b", "text": "No, no conozco"},
                     {"id": "c", "text": "Voy a recordar"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_si", "target": "sí", "native": "sim",
                 "npc_reaction": "Sí pero todavía no. Eso es lo más honesto que puedes decir hoy."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "¿Vas a contarles a Sofía y Miguel ese nombre?", "translation": "Você vai contar pra Sofía e Miguel esse nome?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Sim — eles merecem saber (futuro próximo, 1ª pessoa):",
                 "options": [
                     {"id": "a", "text": "Sí, voy a contarles"},
                     {"id": "b", "text": "Sí, cuento"},
                     {"id": "c", "text": "Sí, soy contar"},
                     {"id": "d", "text": "Sí, tengo contar"},
                 ], "correct": "a",
                 "word_id": "es_voy_a", "target": "voy a contar", "native": "vou contar",
                 "npc_reaction": "Bueno. Sin guardar nada — eso ya no sirve."},
                {"kind": "npc_speak", "npc": "Carmen", "line": "El verbo 'contar' tiene varios usos — te lo explico cuando termines.", "translation": "O verbo 'contar' tem vários usos — te explico quando você terminar.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Pra agradecer Carmen pelo envelope, depois de tantos anos:",
                 "options": [
                     {"id": "a", "text": "Gracias por guardarlo tanto tiempo"},
                     {"id": "b", "text": "Adiós Carmen"},
                     {"id": "c", "text": "Soy gracias"},
                     {"id": "d", "text": "Voy gracias"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "Lo guardé porque me lo pidió un buen hombre. Hoy lo entrego al heredero correcto."},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Carmen pergunta '¿qué vas a hacer con el nombre?'. Sua resposta — vai contar pros amigos:",
                 "options": [
                     {"id": "a", "text": "Voy a contarles a Sofía y Miguel"},
                     {"id": "b", "text": "Voy contar"},
                     {"id": "c", "text": "Soy contar"},
                     {"id": "d", "text": "Tengo contar"},
                 ], "correct": "a",
                 "word_id": "es_contar", "target": "contar", "native": "contar",
                 "npc_reaction": "Bien. 'Contar' a alguien — dirigir tu historia a otra persona. Importante."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["Carmen"], "story": "Carmen quer te ensinar 'contar' direito — verbo simples mas com várias caras. Vai te servir muito.", "now": "Carmen explica 'contar'."},
            "steps": [
                {"kind": "npc_speak", "npc": "Carmen", "line": "'Contar' sirve para tres cosas — números, historias y secretos. Y cambia con quien.", "translation": "'Contar' serve para três coisas — números, histórias e segredos. E muda com quem.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Contar = contar / narrar / confiar segredo", "meaning": "verbo de múltiplos usos", "note": "cuento, cuentas, cuenta, contamos — cambia con quien hace"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Yo cuento ", "isKey": True}, {"text": "una historia · ", "isKey": False},
                     {"text": "Tú cuentas ", "isKey": True}, {"text": "monedas · ", "isKey": False},
                     {"text": "Ella cuenta ", "isKey": True}, {"text": "un secreto · ", "isKey": False},
                     {"text": "Contamos ", "isKey": True}, {"text": "juntos", "isKey": False},
                 ],
                 "example": "Yo cuento la historia. Tú cuentas las monedas. María cuenta secretos.",
                 "translation": "Eu conto a história. Você conta as moedas. María conta segredos.",
                 "note": "cuento / cuentas / cuenta / contamos — sempre algo depois (a coisa contada)"},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Você quer dizer 'eu conto pra você' (1ª pessoa):",
                 "options": [
                     {"id": "a", "text": "Yo te cuento"},
                     {"id": "b", "text": "Tú cuentas"},
                     {"id": "c", "text": "Yo contamos"},
                     {"id": "d", "text": "Soy cuento"},
                 ], "correct": "a",
                 "word_id": "es_cuento", "target": "cuento", "native": "conto",
                 "npc_reaction": "Cuento — yo. Primera persona."},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "E pra perguntar 'você me conta?' (2ª pessoa, pergunta):",
                 "options": [
                     {"id": "a", "text": "¿Me cuentas?"},
                     {"id": "b", "text": "¿Me cuento?"},
                     {"id": "c", "text": "¿Voy a contar?"},
                     {"id": "d", "text": "¿Soy contar?"},
                 ], "correct": "a",
                 "word_id": "es_cuentas", "target": "cuentas", "native": "contas",
                 "npc_reaction": "Cuentas — tú. La pregunta es directa."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["Carmen", "Don Miguel"], "story": "Carmen entrega uma segunda coisa antes de vocês irem — um envelope menor, lacrado, do bolso interno do vestido dela.", "now": "Você recebe um item raro. O baú abre aqui (sistema sorteia)."},
            "steps": [
                {"kind": "npc_speak", "npc": "Carmen", "line": "Esto también es tuyo. Algo que ella te dejó — no sé qué es, pero pesa.", "translation": "Isso também é teu. Algo que ela te deixou — não sei o que é, mas pesa.", "pace": "slow"},
                {"kind": "scene", "text": "🎁 Envelope pequeno · Cera vermelha · Símbolo do sol partido"},
                {"kind": "narrative", "text": "Você recebe um item raro — o sistema escolhe qual da fila do baú raro do seu user."},
                {"kind": "multiple_choice", "npc": "Carmen",
                 "question": "Você agradece Carmen pela segunda entrega:",
                 "options": [
                     {"id": "a", "text": "Gracias por todo"},
                     {"id": "b", "text": "Adiós"},
                     {"id": "c", "text": "Soy gracias"},
                     {"id": "d", "text": "Voy gracias"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "De nada. Y cuando termine todo — ven a verme."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Carmen — gracias. Hoy entendemos más que en veinte años.", "translation": "Carmen — obrigado. Hoje entendemos mais do que em vinte anos.", "pace": "slow"},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Don Miguel", "Sofía", "Miguel"], "story": "Voltando da plaza, vocês veem fumaça subindo do lado da casa de Don Miguel. Sofía corre.", "now": "Crise. Errar trava."},
            "steps": [
                {"kind": "scene", "text": "🔥 Fumaça subindo · Casa de Don Miguel · Três homens uniformizados na porta"},
                {"kind": "npc_speak", "npc": "Sofía", "line": "¡Vinieron! ¡Antes de lo esperado!", "translation": "Vieram! Antes do esperado!", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "Sofía",
                 "question": "Você reage rápido. Pra dizer 'preciso ir' (obrigação, 1ª pessoa):",
                 "options": [
                     {"id": "a", "text": "Tengo que ir"},
                     {"id": "b", "text": "Voy a ir"},
                     {"id": "c", "text": "Quiero ir"},
                     {"id": "d", "text": "Soy ir"},
                 ], "correct": "a",
                 "word_id": "es_tengo_que", "target": "tengo que", "native": "tenho que",
                 "npc_reaction": "Tienes que. Pero no solo — vamos los cuatro.", "gated": True},
                {"kind": "multiple_choice", "npc": "Miguel",
                 "question": "Miguel: 'Espera — ¿qué dice el nombre que leíste?' Você ainda não vai dizer:",
                 "options": [
                     {"id": "a", "text": "Cuando estemos seguros — te cuento"},
                     {"id": "b", "text": "Ya te cuento"},
                     {"id": "c", "text": "Voy a leer"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando — bien. Hoy guardas. Mañana cuentas.", "gated": True},
                {"kind": "narrative", "text": "Vocês quatro correm. María sai pela porta de trás. O Alcalde está no meio da rua — atrás dos três guardas. 'Mañana es el juicio.'"},
            ],
        },
    },
]
