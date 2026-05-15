"""
Seed das 6 seções da Fase 24 Espanhol A1 — "La víspera del juicio".

Cela do ayuntamiento. Frio. Pedra úmida. Don Miguel suborna o guarda
da noite — uma hora. Sofía, Miguel e María entram. Última revisão
antes do julgamento.

Vocab novo (2): juicio · cárcel
Linguagem nova: deber + verbo (dever / é provável)
    "Debes estar listo." / "Debe llegar pronto."

Item dinâmica: item_moment crítico — Hierba de María (sleep aid).
Pra dormir antes do dia mais difícil.
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "armas",
                    "min_level": 3,
                    "uses_item_tag": "arma",
                    "success": "Voce prepara uma ferramenta simples para abrir caminho se a vespera virar armadilha.",
                    "fallback": "Sem preparo perfeito, voce ainda fica perto do grupo e chega ao julgamento.",
                },
                {"kind": "scene", "text": "🌒 Cela do ayuntamiento · Noite · Pedra úmida · Lamparina baixa"},
                {"kind": "narrative", "text": "Você sentado no banco de pedra. Frio entrando pelas paredes. Ouve passos no corredor — quatro pares."},
                {"kind": "npc", "npc": "Don Miguel", "line": "Le pagué al guardia. Una hora. Hablamos rápido.", "pace": "urgent"},
                {"kind": "player", "text": "Sofía, Miguel e María entram atrás dele. Carmen ficou de fora — ela vai testemunhar amanhã, não pode ser vista visitando."},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "juicio", "native": "julgamento"},
                    {"target": "cárcel", "native": "prisão / cela"},
                    {"target": "deber",  "native": "dever (obrigação moral / probabilidade)"},
                ]},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Você cumprimenta — noite tarde:",
                 "options": [
                     {"id": "a", "text": "Buenas noches"},
                     {"id": "b", "text": "Buenos días"},
                     {"id": "c", "text": "Adiós"},
                     {"id": "d", "text": "Mal"},
                 ], "correct": "a",
                 "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                 "npc_reaction": "Buenas noches. Esta es la última noche aquí — sea como sea."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "'Juicio' significa:",
                 "options": [
                     {"id": "a", "text": "Julgamento"},
                     {"id": "b", "text": "Festa"},
                     {"id": "c", "text": "Comida"},
                     {"id": "d", "text": "Carta"},
                 ], "correct": "a",
                 "word_id": "es_juicio", "target": "juicio", "native": "julgamento",
                 "npc_reaction": "Juicio. Mañana. Y tienes que estar listo."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Don Miguel", "María", "Sofía"], "story": "María revisou tudo. Don Miguel ensaiou três respostas-padrão. Sofía decorou a ordem das testemunhas. Última revisão.", "now": "Revisão sob pressão. Errar nada importante."},
            "steps": [
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "¿Cómo te llamas?", "translation": "Como você se chama?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Resposta:",
                 "options": [
                     {"id": "a", "text": "Me llamo [seu nome]"},
                     {"id": "b", "text": "Soy forastero"},
                     {"id": "c", "text": "Tengo años"},
                     {"id": "d", "text": "Adiós"},
                 ], "correct": "a",
                 "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                 "npc_reaction": "Bien."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "¿Cuántos años?", "translation": "Quantos anos?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Idade:",
                 "options": [
                     {"id": "a", "text": "Tengo veinte años"},
                     {"id": "b", "text": "Soy veinte"},
                     {"id": "c", "text": "Estoy veinte"},
                     {"id": "d", "text": "Voy veinte"},
                 ], "correct": "a",
                 "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                 "npc_reaction": "Veinte. Joven — pero el Alcalde no respeta jóvenes."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "¿De dónde vienes?", "translation": "De onde você vem?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Resposta segura (não revelar o nome da F22):",
                 "options": [
                     {"id": "a", "text": "No me acuerdo"},
                     {"id": "b", "text": "Soy de aquí"},
                     {"id": "c", "text": "Voy lejos"},
                     {"id": "d", "text": "Tengo lejos"},
                 ], "correct": "a",
                 "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                 "npc_reaction": "Bueno. Si dice 'mientes', dile que María te examinó la cabeza y confirmó la pérdida de memoria."},
                {"kind": "npc_speak", "npc": "María", "line": "¿Y de mí — qué dices?", "translation": "E sobre mim — o que você diz?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Resposta segura — você sabe pouco dela:",
                 "options": [
                     {"id": "a", "text": "Es la curandera"},
                     {"id": "b", "text": "Es mi familia"},
                     {"id": "c", "text": "Era Sangra"},
                     {"id": "d", "text": "Vi a María"},
                 ], "correct": "a",
                 "word_id": "es_es", "target": "es", "native": "é",
                 "npc_reaction": "Es la curandera. Nada más."},
                {"kind": "npc_speak", "npc": "Sofía", "line": "¿Y cómo estás ahora?", "translation": "E como você está agora?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Sofía",
                 "question": "Honesto — nervoso, mas firme:",
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
            "recap": {"characters": ["María", "Don Miguel"], "story": "María tira do bolso o frasco da Hierba — versão concentrada. Pra dormir essa última noite.", "now": "item_moment crítico — usar a hierba pra dormir bem antes do juicio."},
            "steps": [
                {"kind": "npc_speak", "npc": "María", "line": "Mañana necesitas cabeza clara. Si tienes algo en la bolsa que te calme — úsalo ahora.", "translation": "Amanhã você precisa de cabeça clara. Se você tem algo na mochila que te acalme — usa agora.", "pace": "slow"},
                {
                    "kind": "item_moment",
                    "npc": "María",
                    "situation": "Você tem que dormir. Não tem como ser bom amanhã sem dormir hoje.",
                    "npc_line": "Bébete una hierba si tienes. O agua, si no.",
                    "item_tag": "remedio",
                    "on_use": {
                        "narrative": "Você abriu a hierba. Cheiro forte de eucalipto e algo amargo. Tomou em três goles.",
                        "npc_reaction": "Bueno. Vas a dormir profundo. Mañana — la cabeza te va a obedecer.",
                        "bonus": "reduce_gated",
                    },
                    "on_skip": {
                        "npc_reaction": "Está bien — agua y respiración profunda también funcionan. Pero menos.",
                    },
                },
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Una cosa más — el Alcalde debe estar nervioso también. Mucho está en juego para él. Si pierde — pierde poder.", "translation": "Mais uma coisa — o Alcalde deve estar nervoso também. Muito tá em jogo pra ele. Se ele perder — perde poder.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Don Miguel disse 'el Alcalde debe estar nervioso'. A palavra 'debe' significa:",
                 "options": [
                     {"id": "a", "text": "Deve estar (provavelmente está)"},
                     {"id": "b", "text": "Pode estar"},
                     {"id": "c", "text": "Vai estar"},
                     {"id": "d", "text": "Era nervoso"},
                 ], "correct": "a",
                 "word_id": "es_debe", "target": "debe", "native": "deve (provavelmente)",
                 "npc_reaction": "Debe — probabilidad. 'Debe estar' = 'es probable que esté'. No es certeza."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Pra você dizer 'devo dormir agora' (obrigação suave):",
                 "options": [
                     {"id": "a", "text": "Debo dormir"},
                     {"id": "b", "text": "Voy dormir"},
                     {"id": "c", "text": "Soy dormir"},
                     {"id": "d", "text": "Tengo dormir"},
                 ], "correct": "a",
                 "word_id": "es_debo", "target": "debo", "native": "devo",
                 "npc_reaction": "Debo. Yo — primera. Pero 'tengo que dormir' también sirve."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["Don Miguel"], "story": "Última explicação. Don Miguel quer que você entenda a diferença entre 'debo' (obrigação suave / probabilidade) e 'tengo que' (obrigação forte).", "now": "Diferença prática."},
            "steps": [
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "'Tengo que' es fuerte — la situación obliga. 'Debo' es más suave — moral, decisión propia. Las dos sirven.", "translation": "'Tengo que' é forte — a situação obriga. 'Debo' é mais suave — moral, decisão própria. As duas servem.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Debo / debes / debe + verbo", "meaning": "Devo / deves / deve — obrigação moral OU probabilidade", "note": "diferente de 'tengo que' (situação obriga) e 'puedo' (capaz de)"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Yo debo ", "isKey": True}, {"text": "decir la verdad · ", "isKey": False},
                     {"text": "Tú debes ", "isKey": True}, {"text": "estar listo · ", "isKey": False},
                     {"text": "Él debe ", "isKey": True}, {"text": "estar nervioso", "isKey": False},
                 ],
                 "example": "Yo debo decir la verdad. Tú debes estar listo. El Alcalde debe estar nervioso.",
                 "translation": "Eu devo dizer a verdade. Você deve estar pronto. O Alcalde deve estar nervoso.",
                 "note": "debo / debes / debe — pode ser dever moral OU 'provavelmente está'."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Você quer dizer 'devo estar pronto' (dever pessoal):",
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
                 "npc_reaction": "Debe. Probabilidad — no certeza. Útil pra hablar de los otros."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["María", "Sofía", "Miguel"], "story": "Hora acaba. Guarda volta. Vocês se despedem — sem drama, sem promessas.", "now": "Última conversa antes do amanhecer."},
            "steps": [
                {"kind": "npc_speak", "npc": "Sofía", "line": "Mañana. Carmen ya tiene su discurso preparado.", "translation": "Amanhã. Carmen já tem o discurso preparado.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Sofía",
                 "question": "Você agradece todo o grupo pela ajuda:",
                 "options": [
                     {"id": "a", "text": "Gracias a los cuatro"},
                     {"id": "b", "text": "Adiós a todos"},
                     {"id": "c", "text": "Mal a todos"},
                     {"id": "d", "text": "Soy gracias"},
                 ], "correct": "a",
                 "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                 "npc_reaction": "De nada. Cuando termine el juicio — todos juntos. Tomamos algo."},
                {"kind": "npc_speak", "npc": "Miguel", "line": "Forastero — recuerda. Tu nombre verdadero está en el envelope. Cuando salgas — léelo.", "translation": "Forasteiro — lembra. Teu nome verdadeiro tá no envelope. Quando sair — lê.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Miguel",
                 "question": "Você confirma — vai ler quando puder (futuro com 'cuando'):",
                 "options": [
                     {"id": "a", "text": "Cuando salga, lo leo"},
                     {"id": "b", "text": "Ya leo"},
                     {"id": "c", "text": "Voy leer"},
                     {"id": "d", "text": "Soy leer"},
                 ], "correct": "a",
                 "word_id": "es_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando salgas. Vas a salir — eso lo sabemos."},
                {"kind": "npc_speak", "npc": "María", "line": "Y si te preguntan por la primera palabra de la carta — di 'no recuerdo'.", "translation": "E se te perguntarem pela primeira palavra da carta — diz 'não me lembro'.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Si me preguntan, digo 'no recuerdo'"},
                     {"id": "b", "text": "Cuando me preguntan, voy"},
                     {"id": "c", "text": "Soy preguntar"},
                     {"id": "d", "text": "Tengo no recuerdo"},
                 ], "correct": "a",
                 "word_id": "es_si_condicional", "target": "si", "native": "se (condição)",
                 "npc_reaction": "Si me preguntan. Bueno."},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["María"], "story": "Os três saíram. Você ficou sozinho na cela com a infusão de María. A noite mais longa de todas.", "now": "Você precisa dormir. Mas antes — uma decisão final. Errar trava."},
            "steps": [
                {"kind": "scene", "text": "🌙 Cela escura · Lamparina apagada · Você sozinho · O envelope com o nome dentro"},
                {"kind": "player", "text": "Você abre o envelope mais uma vez. Lê o nome em voz baixa. Sente algo no peito — não memória, ainda. Mas reconhecimento."},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Pra você descrever como se sente — uma palavra. Honesto:",
                 "options": [
                     {"id": "a", "text": "Estoy nervioso, pero también listo"},
                     {"id": "b", "text": "Soy bien"},
                     {"id": "c", "text": "Tengo bien"},
                     {"id": "d", "text": "Voy bien"},
                 ], "correct": "a",
                 "word_id": "es_estoy_nervioso", "target": "estoy nervioso", "native": "estou nervoso",
                 "npc_reaction": "Las dos cosas. Eso es ser humano.", "gated": True},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Você precisa decidir — vai contar tudo pro Alcalde se ele perguntar? Decisão firme: 'só vou contar o que tenho que contar' (obrigação):",
                 "options": [
                     {"id": "a", "text": "Sólo cuento lo que tengo que contar"},
                     {"id": "b", "text": "Cuento todo"},
                     {"id": "c", "text": "Soy contar"},
                     {"id": "d", "text": "Voy contar"},
                 ], "correct": "a",
                 "word_id": "es_tengo_que", "target": "tengo que", "native": "tenho que",
                 "npc_reaction": "Bueno. Tienes que cuidar a Carmen, a Don Miguel, a María. Tu silencio los protege.", "gated": True},
                {"kind": "scene", "text": "🌅 Você adormece com o envelope na mão · A primeira luz começa a entrar"},
                {"kind": "narrative", "text": "Você dormiu profundo. Não sonhou. Quando acordou — guardas batendo na porta. Amanheceu. Juicio."},
            ],
        },
    },
]
