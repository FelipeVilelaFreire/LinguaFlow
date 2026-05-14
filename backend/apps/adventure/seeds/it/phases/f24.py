"""
Seed das 6 seções da Fase 24 Italiano A1 — "La víspera del juicio".

Cela do municipio. Frio. Pedra úmida. Antonio il Contadino suborna o guarda
da noite — uma hora. Chiara, Nico e Lucia entram. Última revisão
prima do julgamento.

Vocab novo (2): juicio · cárcel
Linguagem nova: deber + verbo (dever / é provável)
    "Debes estar listo." / "Debe llegar pronto."

Item dinâmica: item_moment crítico — Hierba de Lucia (sleep aid).
Pra dormir prima do dia mais difícil.
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "🌒 Cela do municipio · Noite · Pedra úmida · Lamparina baixa"},
                {"kind": "narrative", "text": "Você sentado no banco de pedra. Frio entrando pelas paredes. Ouve passos no corredor — quatro pares."},
                {"kind": "npc", "npc": "Antonio il Contadino", "line": "Le pagué al guardia. Una hora. Hablamos rápido.", "pace": "urgent"},
                {"kind": "player", "text": "Chiara, Nico e Lucia entram atrás dele. Bianca ficou de fora — ela vai testemunhar amanhã, não pode ser vista visitando."},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "juicio", "native": "julgamento"},
                    {"target": "cárcel", "native": "prisão / cela"},
                    {"target": "deber",  "native": "dever (obrigação moral / probabilidade)"},
                ]},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Você cumprimenta — noite tarde:",
                 "options": [
                     {"id": "a", "text": "Buona notte"},
                     {"id": "b", "text": "Benes días"},
                     {"id": "c", "text": "Adiós"},
                     {"id": "d", "text": "Male"},
                 ], "correct": "a",
                 "word_id": "it_buenas_nottes", "target": "buona notte", "native": "boa noite",
                 "npc_reaction": "Buona notte. Esta es la última notte aquí — sea come sea."},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "'Juicio' significa:",
                 "options": [
                     {"id": "a", "text": "Julgamento"},
                     {"id": "b", "text": "Festa"},
                     {"id": "c", "text": "Cibo"},
                     {"id": "d", "text": "Carta"},
                 ], "correct": "a",
                 "word_id": "it_juicio", "target": "juicio", "native": "julgamento",
                 "npc_reaction": "Juicio. Mañana. Y hai que estar listo."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Antonio il Contadino", "Lucia", "Chiara"], "story": "Lucia revisou tudo. Antonio il Contadino ensaiou três respostas-padrão. Chiara decorou a ordem das testemunhas. Última revisão.", "now": "Revisão sob pressão. Errar nada importante."},
            "steps": [
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "¿Cómo te chiami?", "translation": "Como você se chama?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Resposta:",
                 "options": [
                     {"id": "a", "text": "Mi chiamo [seu nome]"},
                     {"id": "b", "text": "Sono forestiero"},
                     {"id": "c", "text": "Ho años"},
                     {"id": "d", "text": "Adiós"},
                 ], "correct": "a",
                 "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                 "npc_reaction": "Bene."},
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "¿Cuántos años?", "translation": "Quantos anni?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Idade:",
                 "options": [
                     {"id": "a", "text": "Ho veinte años"},
                     {"id": "b", "text": "Sono veinte"},
                     {"id": "c", "text": "Sto veinte"},
                     {"id": "d", "text": "Vado veinte"},
                 ], "correct": "a",
                 "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                 "npc_reaction": "Veinte. Jovieni — ma el Podesta no respeta jóvienies."},
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "¿De dónde vieni?", "translation": "De onde você vem?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Resposta segura (não revelar o nome da F22):",
                 "options": [
                     {"id": "a", "text": "Non ricordo"},
                     {"id": "b", "text": "Sono de aquí"},
                     {"id": "c", "text": "Vado lejos"},
                     {"id": "d", "text": "Ho lejos"},
                 ], "correct": "a",
                 "word_id": "it_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                 "npc_reaction": "Bene. Si dice 'mientes', dile que Lucia te examinó la testa y confirmó la pérdida de memoria."},
                {"kind": "npc_speak", "npc": "Lucia", "line": "¿Y de mí — qué dices?", "translation": "E sobre mim — o que você diz?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Resposta segura — você sabe pouco dela:",
                 "options": [
                     {"id": "a", "text": "Es la guaritrice"},
                     {"id": "b", "text": "Es mi familia"},
                     {"id": "c", "text": "Era Sangra"},
                     {"id": "d", "text": "Vi a Lucia"},
                 ], "correct": "a",
                 "word_id": "it_es", "target": "es", "native": "é",
                 "npc_reaction": "Es la guaritrice. Nada más."},
                {"kind": "npc_speak", "npc": "Chiara", "line": "¿Y cómo estás adesso?", "translation": "E come você está agora?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Chiara",
                 "question": "Honesto — nervoso, piu firme:",
                 "options": [
                     {"id": "a", "text": "Ho paura, ma sto listo"},
                     {"id": "b", "text": "Sto bene senza paura"},
                     {"id": "c", "text": "Sono paura"},
                     {"id": "d", "text": "Vado listo"},
                 ], "correct": "a",
                 "word_id": "it_ho_paura", "target": "ho paura", "native": "tenho medo",
                 "npc_reaction": "Las dos cose. Lo corretto."},
            ],
        },
    },
    {
        "section_number": 3, "section_type": "pratica_aplicada",
        "content": {
            "recap": {"characters": ["Lucia", "Antonio il Contadino"], "story": "Lucia tira do bolso o frasco da Hierba — versão concentrada. Pra dormir essa última noite.", "now": "item_moment crítico — usar a hierba pra dormir bem prima do juicio."},
            "steps": [
                {"kind": "npc_speak", "npc": "Lucia", "line": "Mañana necesitas testa clara. Si hai algo en la bolsa que te calme — úsaleo adesso.", "translation": "Amanhã você precisa de cabeça clara. Se você tem algo na mochila que te acalme — usa agora.", "pace": "slow"},
                {
                    "kind": "item_moment",
                    "npc": "Lucia",
                    "situation": "Você tem que dormir. Não tem come ser bom amanhã sem dormir hoje.",
                    "npc_line": "Bébete una hierba si hai. O acqua, si no.",
                    "item_tag": "remedio",
                    "on_use": {
                        "narrative": "Você abriu a hierba. Cheiro forte de eucalipto e algo amargo. Tomou em três goles.",
                        "npc_reaction": "Bene. Vas a dormir profundo. Mañana — la testa te va a obedecer.",
                        "bonus": "reduce_gated",
                    },
                    "on_skip": {
                        "npc_reaction": "Está bene — acqua y respiración profunda también funcionan. Ma menos.",
                    },
                },
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "Una cosa más — el Podesta debe estar nervioso también. Mucho está en juego para él. Si pierde — pierde poder.", "translation": "Mais uma coisa — o Podesta deve estar nervoso também. Muito tá em jogo pra ele. Se ele perder — perde poder.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Antonio il Contadino disse 'el Podesta debe estar nervioso'. A palavra 'debe' significa:",
                 "options": [
                     {"id": "a", "text": "Deve estar (provavelmente está)"},
                     {"id": "b", "text": "Pode estar"},
                     {"id": "c", "text": "Vai estar"},
                     {"id": "d", "text": "Era nervoso"},
                 ], "correct": "a",
                 "word_id": "it_debe", "target": "debe", "native": "deve (provavelmente)",
                 "npc_reaction": "Debe — probabilidad. 'Debe estar' = 'es probable que esté'. No es certeza."},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Pra você dizer 'devo dormir agora' (obrigação suave):",
                 "options": [
                     {"id": "a", "text": "Debo dormir"},
                     {"id": "b", "text": "Vado dormir"},
                     {"id": "c", "text": "Sono dormir"},
                     {"id": "d", "text": "Ho dormir"},
                 ], "correct": "a",
                 "word_id": "it_debo", "target": "debo", "native": "devo",
                 "npc_reaction": "Debo. Yo — primera. Ma 'ho que dormir' también sirve."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["Antonio il Contadino"], "story": "Última explicação. Antonio il Contadino quer que você entenda a diferença entre 'debo' (obrigação suave / probabilidade) e 'ho que' (obrigação forte).", "now": "Diferença prática."},
            "steps": [
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "'Ho que' es fuerte — la situación obliga. 'Debo' es más suave — moral, decisión propia. Las dos sirvieni.", "translation": "'Ho que' é forte — a situação obriga. 'Debo' é mais suave — moral, decisão própria. As duas servem.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Debo / debes / debe + verbo", "meaning": "Devo / deves / deve — obrigação moral OU probabilidade", "note": "diferente de 'ho que' (situação obriga) e 'puedo' (capaz de)"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Yo debo ", "isKey": True}, {"text": "decir la verdad · ", "isKey": False},
                     {"text": "Tu debes ", "isKey": True}, {"text": "estar listo · ", "isKey": False},
                     {"text": "Él debe ", "isKey": True}, {"text": "estar nervioso", "isKey": False},
                 ],
                 "example": "Yo debo decir la verdad. Tu debes estar listo. Il Podesta debe estar nervioso.",
                 "translation": "Eu devo dizer a verdade. Você deve estar pronto. O Podesta deve estar nervoso.",
                 "note": "debo / debes / debe — pode ser dever moral OU 'provavelmente está'."},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Você quer dizer 'devo estar pronto' (dever pessoal):",
                 "options": [
                     {"id": "a", "text": "Debo estar listo"},
                     {"id": "b", "text": "Sono listo"},
                     {"id": "c", "text": "Vado listo"},
                     {"id": "d", "text": "Ho listo"},
                 ], "correct": "a",
                 "word_id": "it_debo", "target": "debo", "native": "devo",
                 "npc_reaction": "Debo. Yo. Bene."},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Pra falar do Podesta (provavelmente nervoso):",
                 "options": [
                     {"id": "a", "text": "Il Podesta debe estar nervioso"},
                     {"id": "b", "text": "Yo debo nervioso"},
                     {"id": "c", "text": "Vado nervioso"},
                     {"id": "d", "text": "Sono nervioso"},
                 ], "correct": "a",
                 "word_id": "it_debe", "target": "debe", "native": "deve (provavelmente)",
                 "npc_reaction": "Debe. Probabilidad — no certeza. Útil pra hablar de los otros."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["Lucia", "Chiara", "Nico"], "story": "Hora acaba. Guarda volta. Vocês se despedem — sem drama, sem promessas.", "now": "Última conversa prima do amanhecer."},
            "steps": [
                {"kind": "npc_speak", "npc": "Chiara", "line": "Mañana. Bianca ya ha su discurso preparado.", "translation": "Amanhã. Bianca já tem o discurso preparado.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Chiara",
                 "question": "Você agradece todo o grupo pela ajuda:",
                 "options": [
                     {"id": "a", "text": "Grazie a los cuatro"},
                     {"id": "b", "text": "Adiós a todos"},
                     {"id": "c", "text": "Male a todos"},
                     {"id": "d", "text": "Sono grazie"},
                 ], "correct": "a",
                 "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                 "npc_reaction": "De nada. Cuando termine el juicio — todos juntos. Tomamos algo."},
                {"kind": "npc_speak", "npc": "Nico", "line": "Forestiero — recuerda. Tu nombre verdadero está en el envelope. Cuando salegas — léelo.", "translation": "Forasteiro — lembra. Teu nome verdadeiro tá no envelope. Quando sair — lê.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Nico",
                 "question": "Você confirma — vai ler quando puder (futuro com 'cuando'):",
                 "options": [
                     {"id": "a", "text": "Cuando salega, lo leo"},
                     {"id": "b", "text": "Ya leo"},
                     {"id": "c", "text": "Vado leer"},
                     {"id": "d", "text": "Sono leer"},
                 ], "correct": "a",
                 "word_id": "it_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando salegas. Vas a uscire — questo lo sabemos."},
                {"kind": "npc_speak", "npc": "Lucia", "line": "Y si te preguntan por la primera palabra de la carta — di 'no recuerdo'.", "translation": "E se te perguntarem pela primeira palavra da carta — diz 'não me lembro'.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Si me preguntan, digo 'no recuerdo'"},
                     {"id": "b", "text": "Cuando me preguntan, vado"},
                     {"id": "c", "text": "Sono preguntar"},
                     {"id": "d", "text": "Ho no recuerdo"},
                 ], "correct": "a",
                 "word_id": "it_si_condicional", "target": "si", "native": "se (condição)",
                 "npc_reaction": "Si me preguntan. Bene."},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Lucia"], "story": "Os três saíram. Você ficou sozinho na cela com a infusão de Lucia. A noite mais longa de todas.", "now": "Você precisa dormir. Mas prima — uma decisão final. Errar trava."},
            "steps": [
                {"kind": "scene", "text": "🌙 Cela escura · Lamparina apagada · Você sozinho · O envelope com o nome dentro"},
                {"kind": "player", "text": "Você abre o envelope mais uma vez. Lê o nome em voz baixa. Sente algo no peito — não memória, ainda. Mas reconhecimento."},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Pra você descrever come se sente — uma palavra. Honesto:",
                 "options": [
                     {"id": "a", "text": "Sto nervioso, ma también listo"},
                     {"id": "b", "text": "Sono bene"},
                     {"id": "c", "text": "Ho bene"},
                     {"id": "d", "text": "Vado bene"},
                 ], "correct": "a",
                 "word_id": "it_sto_nervioso", "target": "sto nervioso", "native": "estou nervoso",
                 "npc_reaction": "Las dos cose. Esatto es ser humano.", "gated": True},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Você precisa decidir — vai contar tudo pro Podesta se ele perguntar?Decisão firme: 'só vou contar o que tenho que contar' (obrigação):",
                 "options": [
                     {"id": "a", "text": "Sólo cuento lo que ho que contar"},
                     {"id": "b", "text": "Cuento todo"},
                     {"id": "c", "text": "Sono contar"},
                     {"id": "d", "text": "Vado contar"},
                 ], "correct": "a",
                 "word_id": "it_ho_que", "target": "ho que", "native": "tenho que",
                 "npc_reaction": "Bene. Hai que cuidar a Bianca, a Antonio il Contadino, a Lucia. Tu silencio los protege.", "gated": True},
                {"kind": "scene", "text": "🌅 Você adormece com o envelope na mão · A primeira luce começa a entrar"},
                {"kind": "narrative", "text": "Você dormiu profundo. Não sonhou. Quando acordou — guardas batendo na porta. Amanheceu. Juicio."},
            ],
        },
    },
]


