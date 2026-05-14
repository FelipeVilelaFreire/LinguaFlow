"""
Seed das 6 seÃ§Ãµes da Fase 23 Espanhol A1 â€” "El plan del Alcalde".

El Inspector volta com 3 guardas. Cercam a casa. MarÃ­a vai falar com
eles â€” volta com 'ordem de levar o forastero ao Alcalde, pacificamente
ou nÃ£o'.

Vocab novo (2): orden Â· acompaÃ±ar
Linguagem nova: 'si + verbo' (condicional simples)
    "Si vienes pacÃ­ficamente, no hay sangre."

Item dinÃ¢mica: 1 item_moment â€” moneda (qualquer tipo). Soborno de
guarda. Funciona se tem; se nÃ£o tem, MarÃ­a negocia.
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "ðŸšï¸ Casa de Don Miguel Â· Cercada Â· TrÃªs guardas + Inspector na porta"},
                {"kind": "npc", "npc": "El Inspector", "line": "Don Miguel â€” abra. Tenemos orden del Alcalde.", "pace": "urgent"},
                {"kind": "player", "text": "VocÃªs cinco do lado de dentro. MarÃ­a sentada na cadeira da cozinha como se fosse manhÃ£ normal."},
                {"kind": "npc", "npc": "Don Miguel", "line": "Voy a abrir. Pero el forastero no sale solo.", "pace": "slow"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "orden",     "native": "ordem"},
                    {"target": "acompaÃ±ar", "native": "acompanhar"},
                    {"target": "si",        "native": "se (condicional)"},
                ]},
                {"kind": "multiple_choice", "npc": "El Inspector",
                 "question": "El Inspector entra. Cumprimenta formal â€” nÃ£o amistoso. VocÃª devolve:",
                 "options": [
                     {"id": "a", "text": "Buenos dÃ­as, seÃ±or"},
                     {"id": "b", "text": "AdiÃ³s"},
                     {"id": "c", "text": "Mal"},
                     {"id": "d", "text": "Tengo miedo"},
                 ], "correct": "a",
                 "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                 "npc_reaction": "Buenos dÃ­as. Brevemente â€” el Alcalde te llama."},
                {"kind": "multiple_choice", "npc": "El Inspector",
                 "question": "El Inspector menciona 'orden del Alcalde'. A palavra 'orden' significa:",
                 "options": [
                     {"id": "a", "text": "Ordem (mandato oficial)"},
                     {"id": "b", "text": "Pergunta"},
                     {"id": "c", "text": "Pedido suave"},
                     {"id": "d", "text": "SugestÃ£o"},
                 ], "correct": "a",
                 "word_id": "es_orden", "target": "orden", "native": "ordem",
                 "npc_reaction": "Orden. No negociable."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["El Inspector", "MarÃ­a"], "story": "El Inspector quer levar vocÃª imediatamente. MarÃ­a intervÃ©m â€” propÃµe acompanhar atÃ© a praÃ§a.", "now": "RevisÃ£o sob pressÃ£o."},
            "steps": [
                {"kind": "npc_speak", "npc": "El Inspector", "line": "Â¿CÃ³mo te llamas? Para el registro.", "translation": "Como vocÃª se chama? Pro registro.", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "El Inspector",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Me llamo [seu nome]"},
                     {"id": "b", "text": "Soy forastero"},
                     {"id": "c", "text": "Tengo aÃ±os"},
                     {"id": "d", "text": "AdiÃ³s"},
                 ], "correct": "a",
                 "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                 "npc_reaction": "Anotado."},
                {"kind": "npc_speak", "npc": "El Inspector", "line": "Â¿Edad?", "translation": "Idade?", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "El Inspector",
                 "question": "Resposta exata:",
                 "options": [
                     {"id": "a", "text": "Tengo veinte aÃ±os"},
                     {"id": "b", "text": "Soy veinte"},
                     {"id": "c", "text": "Estoy veinte"},
                     {"id": "d", "text": "Voy veinte"},
                 ], "correct": "a",
                 "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                 "npc_reaction": "Veinte."},
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Inspector â€” yo lo acompaÃ±o hasta la plaza. AllÃ­ decides quÃ© hacer.", "translation": "Inspector â€” eu o acompanho atÃ© a plaza. Ali decide o que fazer.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "Pra vocÃª expressar concordÃ¢ncia â€” 'eu vou com vocÃªs':",
                 "options": [
                     {"id": "a", "text": "Yo voy con vosotros"},
                     {"id": "b", "text": "TÃº vienes"},
                     {"id": "c", "text": "Ella va"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                 "npc_reaction": "Bien. Tenemos que parecer cooperativos."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Â¿CÃ³mo estÃ¡s, hijo? Sin mentir.", "translation": "Como vocÃª estÃ¡, filho? Sem mentir.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "VocÃª tÃ¡ com medo, mas firme:",
                 "options": [
                     {"id": "a", "text": "Tengo miedo, pero estoy bien"},
                     {"id": "b", "text": "Estoy miedo"},
                     {"id": "c", "text": "Soy miedo"},
                     {"id": "d", "text": "Voy miedo"},
                 ], "correct": "a",
                 "word_id": "es_tengo_miedo", "target": "tengo miedo", "native": "tenho medo",
                 "npc_reaction": "Lo entiendo. Vamos juntos."},
            ],
        },
    },
    {
        "section_number": 3, "section_type": "pratica_aplicada",
        "content": {
            "recap": {"characters": ["El Inspector", "MarÃ­a", "Don Miguel"], "story": "VocÃªs saem da casa. O Inspector na frente. VocÃªs quatro atrÃ¡s, escoltados pelos guardas. Caminham pela rua principal â€” gente parando pra ver.", "now": "Caminhada tensa. item_moment com moeda â€” soborno opcional."},
            "steps": [
                {"kind": "scene", "text": "ðŸš¶ Rua principal Â· VocÃªs escoltados Â· Vizinhos observando das janelas"},
                {
                    "kind": "item_moment",
                    "npc": "Don Miguel",
                    "situation": "Um dos guardas â€” mais jovem, nervoso â€” fica prÃ³ximo de Don Miguel. Don Miguel sussurra pra vocÃª.",
                    "npc_line": "Si tienes una moneda â€” dÃ¡sela. Una sola. A veces eso compra tiempo.",
                    "item_tag": "moneda",
                    "on_use": {
                        "narrative": "VocÃª tira a moeda do bolso, passa pra Don Miguel, que entrega ao guarda jovem. O guarda guarda no bolso sem encarar vocÃª.",
                        "npc_reaction": "Eso. Si vienen a separarnos cuando lleguemos al ayuntamiento â€” Ã©l mira a otro lado.",
                        "bonus": "reduce_gated",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. MarÃ­a tiene otros recursos.",
                    },
                },
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Si llegamos a la plaza, hablamos. Si no â€” Carmen se entera.", "translation": "Se chegarmos na plaza, falamos. Se nÃ£o â€” Carmen descobre.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "MarÃ­a usou 'si' duas vezes. A palavra 'si' significa:",
                 "options": [
                     {"id": "a", "text": "Se (condiÃ§Ã£o â€” depende disso)"},
                     {"id": "b", "text": "Sim (afirmaÃ§Ã£o)"},
                     {"id": "c", "text": "Mas"},
                     {"id": "d", "text": "Quando exato"},
                 ], "correct": "a",
                 "word_id": "es_si_condicional", "target": "si", "native": "se (condiÃ§Ã£o)",
                 "npc_reaction": "Si â€” condicional. Sem acento. 'SÃ­' com acento Ã© otra cosa â€” 'sim'."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Si nos paran ahora, mantÃ©n la calma. Si pasamos â€” mejor.", "translation": "Se nos parem agora, mantÃ©m a calma. Se passarmos â€” melhor.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "VocÃª responde â€” 'sim, vou manter calma' (afirmaÃ§Ã£o simples):",
                 "options": [
                     {"id": "a", "text": "SÃ­, voy a mantener calma"},
                     {"id": "b", "text": "Si voy"},
                     {"id": "c", "text": "Soy calma"},
                     {"id": "d", "text": "AdiÃ³s"},
                 ], "correct": "a",
                 "word_id": "es_si", "target": "sÃ­", "native": "sim",
                 "npc_reaction": "SÃ­. Con acento â€” afirmas. Sin acento â€” pones condiciÃ³n. Las dos sirven."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["Don Miguel"], "story": "VocÃªs param numa esquina. Os guardas pararam de andar â€” esperam o Inspector ler algo. Don Miguel usa o momento.", "now": "Don Miguel explica 'si + verbo' rÃ¡pido."},
            "steps": [
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "'Si' â€” sin acento â€” pone una condiciÃ³n. 'Si pasa esto, hacemos aquello.' Ãštil cuando todo es inseguro.", "translation": "'Si' â€” sem acento â€” pÃµe uma condiÃ§Ã£o. 'Se acontece isso, fazemos aquilo.' Ãštil quando tudo Ã© incerto.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Si + verbo, ... ", "meaning": "Se (condiÃ§Ã£o) + consequÃªncia", "note": "diferente de 'cuando' (espera tempo) â€” 'si' Ã© DEPENDE de acontecer"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Si ", "isKey": True}, {"text": "vienes, ", "isKey": False},
                     {"text": "hablamos Â· ", "isKey": False},
                     {"text": "Si ", "isKey": True}, {"text": "tienes miedo, ", "isKey": False},
                     {"text": "espera", "isKey": False},
                 ],
                 "example": "Si vienes, hablamos. Si pasa algo malo, corre.",
                 "translation": "Se vocÃª vier, falamos. Se algo ruim acontecer, corre.",
                 "note": "si + verbo presente, depois consequÃªncia. CondiÃ§Ã£o simples."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Pra dizer 'se vocÃª quiser, te conto' (condiÃ§Ã£o):",
                 "options": [
                     {"id": "a", "text": "Si quieres, te cuento"},
                     {"id": "b", "text": "Cuando quieres, cuento"},
                     {"id": "c", "text": "SÃ­ quieres cuento"},
                     {"id": "d", "text": "Voy contar"},
                 ], "correct": "a",
                 "word_id": "es_si_condicional", "target": "si", "native": "se",
                 "npc_reaction": "Si quieres. Sem acento."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "DiferenÃ§a entre 'si' e 'cuando' â€” qual a regra?",
                 "options": [
                     {"id": "a", "text": "'si' = condiÃ§Ã£o (pode nÃ£o acontecer) Â· 'cuando' = tempo (vai acontecer)"},
                     {"id": "b", "text": "SÃ£o iguais"},
                     {"id": "c", "text": "'si' Ã© sÃ³ pergunta"},
                     {"id": "d", "text": "'cuando' Ã© negativo"},
                 ], "correct": "a",
                 "word_id": "es_si_cuando", "target": "si vs cuando", "native": "se vs quando",
                 "npc_reaction": "Eso. Ãštil distinguir â€” 'cuando llegues' (sÃ© que vas a llegar) vs 'si llegas' (no sÃ© si vas a llegar)."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["El Inspector", "MarÃ­a"], "story": "Chegaram Ã  plaza do ayuntamiento. El Inspector se vira pra MarÃ­a â€” diz que ela nÃ£o pode entrar com vocÃªs.", "now": "NegociaÃ§Ã£o final antes do julgamento."},
            "steps": [
                {"kind": "npc_speak", "npc": "El Inspector", "line": "MarÃ­a â€” tÃº esperas afuera. Solo el forastero entra.", "translation": "MarÃ­a â€” vocÃª espera fora. SÃ³ o forasteiro entra.", "pace": "urgent"},
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Si entra solo, no responde. Si entramos los cuatro â€” habla.", "translation": "Se entrar sozinho, nÃ£o responde. Se entrarmos os quatro â€” fala.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Inspector",
                 "question": "El Inspector pondera. Pra vocÃª confirmar pra ele â€” 'estoy listo' (estado de agora):",
                 "options": [
                     {"id": "a", "text": "Estoy listo"},
                     {"id": "b", "text": "Soy listo"},
                     {"id": "c", "text": "Tengo listo"},
                     {"id": "d", "text": "Voy listo"},
                 ], "correct": "a",
                 "word_id": "es_estoy_listo", "target": "estoy listo", "native": "estou pronto",
                 "npc_reaction": "Listo. Bueno. Pero recuerda â€” el Alcalde no es como yo. Ã‰l tiene rencor."},
                {"kind": "npc_speak", "npc": "El Inspector", "line": "EstÃ¡ bien â€” los cuatro. Pero solo el forastero habla. Los demÃ¡s callan.", "translation": "TÃ¡ bom â€” os quatro. Mas sÃ³ o forasteiro fala. Os outros calam.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "VocÃª confirma pra MarÃ­a â€” vai falar vocÃª, eles ficam quietos. Resposta com 'voy a + verbo':",
                 "options": [
                     {"id": "a", "text": "Voy a hablar yo"},
                     {"id": "b", "text": "Hablo yo"},
                     {"id": "c", "text": "Soy hablar"},
                     {"id": "d", "text": "Tengo hablar"},
                 ], "correct": "a",
                 "word_id": "es_voy_a", "target": "voy a hablar", "native": "vou falar",
                 "npc_reaction": "Voy a hablar yo. Bueno. Carmen va a estar en el pÃºblico â€” eso ya es algo."},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["MarÃ­a", "Don Miguel"], "story": "Antes de entrar â€” MarÃ­a te pega pelo cotovelo. Ãšltima conversa.", "now": "PreparaÃ§Ã£o final. Errar trava."},
            "steps": [
                {"kind": "scene", "text": "ðŸšª Porta do ayuntamiento Â· VocÃªs quatro Â· Guardas atrÃ¡s"},
                {"kind": "npc_speak", "npc": "MarÃ­a", "line": "Si te preguntan tu nombre â€” di tu nombre. Si te preguntan tu origen â€” di que no recuerdas. Si te preguntan por mÃ­ â€” di que soy curandera. Nada mÃ¡s.", "translation": "Se te perguntarem teu nome â€” diz teu nome. Se te perguntarem tua origem â€” diz que nÃ£o lembras. Se te perguntarem por mim â€” diz que sou curandera. Nada mais.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "MarÃ­a",
                 "question": "VocÃª confirma â€” ouviu:",
                 "options": [
                     {"id": "a", "text": "Lo oÃ­, MarÃ­a"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Voy a oÃ­r"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                 "npc_reaction": "Cuando salgas â€” habrÃ¡ un cambio. Tienes que estar listo para sentirlo.", "gated": True},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Y si te preguntan por Carmen â€” di que es vecina. Solo eso.", "translation": "E se te perguntarem por Carmen â€” diz que Ã© vizinha. SÃ³ isso.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Sua promessa final â€” vai obedecer:",
                 "options": [
                     {"id": "a", "text": "SÃ­, voy a hacer eso"},
                     {"id": "b", "text": "No voy"},
                     {"id": "c", "text": "Voy"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_si", "target": "sÃ­", "native": "sim",
                 "npc_reaction": "Bueno. Entremos.", "gated": True},
                {"kind": "scene", "text": "ðŸ›ï¸ Porta de ferro Â· Entrando Â· Alcalde sentado no trono de madeira"},
            ],
        },
    },
]
