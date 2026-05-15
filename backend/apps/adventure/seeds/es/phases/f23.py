"""
Seed das 6 seções da Fase 23 Espanhol A1 — "El plan del Alcalde".

El Inspector volta com 3 guardas. Cercam a casa. María vai falar com
eles — volta com 'ordem de levar o forastero ao Alcalde, pacificamente
ou não'.

Vocab novo (2): orden · acompañar
Linguagem nova: 'si + verbo' (condicional simples)
    "Si vienes pacíficamente, no hay sangre."

Item dinâmica: 1 item_moment — moneda (qualquer tipo). Soborno de
guarda. Funciona se tem; se não tem, María negocia.
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "persuasao",
                    "min_level": 3,
                    "uses_item_tag": "moneda",
                    "success": "Voce mede cada palavra diante do plano do Alcalde e evita uma ordem pior.",
                    "fallback": "Sua fala nao muda a ordem, mas o grupo entende melhor o risco e segue junto.",
                },
                {"kind": "scene", "text": "🏚️ Casa de Don Miguel · Cercada · Três guardas + Inspector na porta"},
                {"kind": "npc", "npc": "El Inspector", "line": "Don Miguel — abra. Tenemos orden del Alcalde.", "pace": "urgent"},
                {"kind": "player", "text": "Vocês cinco do lado de dentro. María sentada na cadeira da cozinha como se fosse manhã normal."},
                {"kind": "npc", "npc": "Don Miguel", "line": "Voy a abrir. Pero el forastero no sale solo.", "pace": "slow"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "orden",     "native": "ordem"},
                    {"target": "acompañar", "native": "acompanhar"},
                    {"target": "si",        "native": "se (condicional)"},
                ]},
                {"kind": "multiple_choice", "npc": "El Inspector",
                 "question": "El Inspector entra. Cumprimenta formal — não amistoso. Você devolve:",
                 "options": [
                     {"id": "a", "text": "Buenos días, señor"},
                     {"id": "b", "text": "Adiós"},
                     {"id": "c", "text": "Mal"},
                     {"id": "d", "text": "Tengo miedo"},
                 ], "correct": "a",
                 "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                 "npc_reaction": "Buenos días. Brevemente — el Alcalde te llama."},
                {"kind": "multiple_choice", "npc": "El Inspector",
                 "question": "El Inspector menciona 'orden del Alcalde'. A palavra 'orden' significa:",
                 "options": [
                     {"id": "a", "text": "Ordem (mandato oficial)"},
                     {"id": "b", "text": "Pergunta"},
                     {"id": "c", "text": "Pedido suave"},
                     {"id": "d", "text": "Sugestão"},
                 ], "correct": "a",
                 "word_id": "es_orden", "target": "orden", "native": "ordem",
                 "npc_reaction": "Orden. No negociable."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["El Inspector", "María"], "story": "El Inspector quer levar você imediatamente. María intervém — propõe acompanhar até a praça.", "now": "Revisão sob pressão."},
            "steps": [
                {"kind": "npc_speak", "npc": "El Inspector", "line": "¿Cómo te llamas? Para el registro.", "translation": "Como você se chama? Pro registro.", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "El Inspector",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Me llamo [seu nome]"},
                     {"id": "b", "text": "Soy forastero"},
                     {"id": "c", "text": "Tengo años"},
                     {"id": "d", "text": "Adiós"},
                 ], "correct": "a",
                 "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                 "npc_reaction": "Anotado."},
                {"kind": "npc_speak", "npc": "El Inspector", "line": "¿Edad?", "translation": "Idade?", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "El Inspector",
                 "question": "Resposta exata:",
                 "options": [
                     {"id": "a", "text": "Tengo veinte años"},
                     {"id": "b", "text": "Soy veinte"},
                     {"id": "c", "text": "Estoy veinte"},
                     {"id": "d", "text": "Voy veinte"},
                 ], "correct": "a",
                 "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                 "npc_reaction": "Veinte."},
                {"kind": "npc_speak", "npc": "María", "line": "Inspector — yo lo acompaño hasta la plaza. Allí decides qué hacer.", "translation": "Inspector — eu o acompanho até a plaza. Ali decide o que fazer.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Pra você expressar concordância — 'eu vou com vocês':",
                 "options": [
                     {"id": "a", "text": "Yo voy con vosotros"},
                     {"id": "b", "text": "Tú vienes"},
                     {"id": "c", "text": "Ella va"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                 "npc_reaction": "Bien. Tenemos que parecer cooperativos."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "¿Cómo estás, hijo? Sin mentir.", "translation": "Como você está, filho? Sem mentir.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Você tá com medo, mas firme:",
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
            "recap": {"characters": ["El Inspector", "María", "Don Miguel"], "story": "Vocês saem da casa. O Inspector na frente. Vocês quatro atrás, escoltados pelos guardas. Caminham pela rua principal — gente parando pra ver.", "now": "Caminhada tensa. item_moment com moeda — soborno opcional."},
            "steps": [
                {"kind": "scene", "text": "🚶 Rua principal · Vocês escoltados · Vizinhos observando das janelas"},
                {
                    "kind": "item_moment",
                    "npc": "Don Miguel",
                    "situation": "Um dos guardas — mais jovem, nervoso — fica próximo de Don Miguel. Don Miguel sussurra pra você.",
                    "npc_line": "Si tienes una moneda — dásela. Una sola. A veces eso compra tiempo.",
                    "item_tag": "moneda",
                    "on_use": {
                        "narrative": "Você tira a moeda do bolso, passa pra Don Miguel, que entrega ao guarda jovem. O guarda guarda no bolso sem encarar você.",
                        "npc_reaction": "Eso. Si vienen a separarnos cuando lleguemos al ayuntamiento — él mira a otro lado.",
                        "bonus": "reduce_gated",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. María tiene otros recursos.",
                    },
                },
                {"kind": "npc_speak", "npc": "María", "line": "Si llegamos a la plaza, hablamos. Si no — Carmen se entera.", "translation": "Se chegarmos na plaza, falamos. Se não — Carmen descobre.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "María usou 'si' duas vezes. A palavra 'si' significa:",
                 "options": [
                     {"id": "a", "text": "Se (condição — depende disso)"},
                     {"id": "b", "text": "Sim (afirmação)"},
                     {"id": "c", "text": "Mas"},
                     {"id": "d", "text": "Quando exato"},
                 ], "correct": "a",
                 "word_id": "es_si_condicional", "target": "si", "native": "se (condição)",
                 "npc_reaction": "Si — condicional. Sem acento. 'Sí' com acento é otra cosa — 'sim'."},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Si nos paran ahora, mantén la calma. Si pasamos — mejor.", "translation": "Se nos parem agora, mantém a calma. Se passarmos — melhor.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Você responde — 'sim, vou manter calma' (afirmação simples):",
                 "options": [
                     {"id": "a", "text": "Sí, voy a mantener calma"},
                     {"id": "b", "text": "Si voy"},
                     {"id": "c", "text": "Soy calma"},
                     {"id": "d", "text": "Adiós"},
                 ], "correct": "a",
                 "word_id": "es_si", "target": "sí", "native": "sim",
                 "npc_reaction": "Sí. Con acento — afirmas. Sin acento — pones condición. Las dos sirven."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["Don Miguel"], "story": "Vocês param numa esquina. Os guardas pararam de andar — esperam o Inspector ler algo. Don Miguel usa o momento.", "now": "Don Miguel explica 'si + verbo' rápido."},
            "steps": [
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "'Si' — sin acento — pone una condición. 'Si pasa esto, hacemos aquello.' Útil cuando todo es inseguro.", "translation": "'Si' — sem acento — põe uma condição. 'Se acontece isso, fazemos aquilo.' Útil quando tudo é incerto.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Si + verbo, ... ", "meaning": "Se (condição) + consequência", "note": "diferente de 'cuando' (espera tempo) — 'si' é DEPENDE de acontecer"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Si ", "isKey": True}, {"text": "vienes, ", "isKey": False},
                     {"text": "hablamos · ", "isKey": False},
                     {"text": "Si ", "isKey": True}, {"text": "tienes miedo, ", "isKey": False},
                     {"text": "espera", "isKey": False},
                 ],
                 "example": "Si vienes, hablamos. Si pasa algo malo, corre.",
                 "translation": "Se você vier, falamos. Se algo ruim acontecer, corre.",
                 "note": "si + verbo presente, depois consequência. Condição simples."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Pra dizer 'se você quiser, te conto' (condição):",
                 "options": [
                     {"id": "a", "text": "Si quieres, te cuento"},
                     {"id": "b", "text": "Cuando quieres, cuento"},
                     {"id": "c", "text": "Sí quieres cuento"},
                     {"id": "d", "text": "Voy contar"},
                 ], "correct": "a",
                 "word_id": "es_si_condicional", "target": "si", "native": "se",
                 "npc_reaction": "Si quieres. Sem acento."},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Diferença entre 'si' e 'cuando' — qual a regra?",
                 "options": [
                     {"id": "a", "text": "'si' = condição (pode não acontecer) · 'cuando' = tempo (vai acontecer)"},
                     {"id": "b", "text": "São iguais"},
                     {"id": "c", "text": "'si' é só pergunta"},
                     {"id": "d", "text": "'cuando' é negativo"},
                 ], "correct": "a",
                 "word_id": "es_si_cuando", "target": "si vs cuando", "native": "se vs quando",
                 "npc_reaction": "Eso. Útil distinguir — 'cuando llegues' (sé que vas a llegar) vs 'si llegas' (no sé si vas a llegar)."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["El Inspector", "María"], "story": "Chegaram à plaza do ayuntamiento. El Inspector se vira pra María — diz que ela não pode entrar com vocês.", "now": "Negociação final antes do julgamento."},
            "steps": [
                {"kind": "npc_speak", "npc": "El Inspector", "line": "María — tú esperas afuera. Solo el forastero entra.", "translation": "María — você espera fora. Só o forasteiro entra.", "pace": "urgent"},
                {"kind": "npc_speak", "npc": "María", "line": "Si entra solo, no responde. Si entramos los cuatro — habla.", "translation": "Se entrar sozinho, não responde. Se entrarmos os quatro — fala.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "El Inspector",
                 "question": "El Inspector pondera. Pra você confirmar pra ele — 'estoy listo' (estado de agora):",
                 "options": [
                     {"id": "a", "text": "Estoy listo"},
                     {"id": "b", "text": "Soy listo"},
                     {"id": "c", "text": "Tengo listo"},
                     {"id": "d", "text": "Voy listo"},
                 ], "correct": "a",
                 "word_id": "es_estoy_listo", "target": "estoy listo", "native": "estou pronto",
                 "npc_reaction": "Listo. Bueno. Pero recuerda — el Alcalde no es como yo. Él tiene rencor."},
                {"kind": "npc_speak", "npc": "El Inspector", "line": "Está bien — los cuatro. Pero solo el forastero habla. Los demás callan.", "translation": "Tá bom — os quatro. Mas só o forasteiro fala. Os outros calam.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Você confirma pra María — vai falar você, eles ficam quietos. Resposta com 'voy a + verbo':",
                 "options": [
                     {"id": "a", "text": "Voy a hablar yo"},
                     {"id": "b", "text": "Hablo yo"},
                     {"id": "c", "text": "Soy hablar"},
                     {"id": "d", "text": "Tengo hablar"},
                 ], "correct": "a",
                 "word_id": "es_voy_a", "target": "voy a hablar", "native": "vou falar",
                 "npc_reaction": "Voy a hablar yo. Bueno. Carmen va a estar en el público — eso ya es algo."},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["María", "Don Miguel"], "story": "Antes de entrar — María te pega pelo cotovelo. Última conversa.", "now": "Preparação final. Errar trava."},
            "steps": [
                {"kind": "scene", "text": "🚪 Porta do ayuntamiento · Vocês quatro · Guardas atrás"},
                {"kind": "npc_speak", "npc": "María", "line": "Si te preguntan tu nombre — di tu nombre. Si te preguntan tu origen — di que no recuerdas. Si te preguntan por mí — di que soy curandera. Nada más.", "translation": "Se te perguntarem teu nome — diz teu nome. Se te perguntarem tua origem — diz que não lembras. Se te perguntarem por mim — diz que sou curandera. Nada mais.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "María",
                 "question": "Você confirma — ouviu:",
                 "options": [
                     {"id": "a", "text": "Lo oí, María"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Voy a oír"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_oi", "target": "oí", "native": "ouvi",
                 "npc_reaction": "Cuando salgas — habrá un cambio. Tienes que estar listo para sentirlo.", "gated": True},
                {"kind": "npc_speak", "npc": "Don Miguel", "line": "Y si te preguntan por Carmen — di que es vecina. Solo eso.", "translation": "E se te perguntarem por Carmen — diz que é vizinha. Só isso.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Don Miguel",
                 "question": "Sua promessa final — vai obedecer:",
                 "options": [
                     {"id": "a", "text": "Sí, voy a hacer eso"},
                     {"id": "b", "text": "No voy"},
                     {"id": "c", "text": "Voy"},
                     {"id": "d", "text": "Soy"},
                 ], "correct": "a",
                 "word_id": "es_si", "target": "sí", "native": "sim",
                 "npc_reaction": "Bueno. Entremos.", "gated": True},
                {"kind": "scene", "text": "🏛️ Porta de ferro · Entrando · Alcalde sentado no trono de madeira"},
            ],
        },
    },
]
