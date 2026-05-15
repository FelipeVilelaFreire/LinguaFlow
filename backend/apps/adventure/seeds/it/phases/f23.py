"""
Seed das 6 seções da Fase 23 Italiano A1 — "El plan del Podesta".

L'Ispettore volta com 3 guardas. Cercam a casa. Lucia vai falar com
eles — volta com 'ordem de levar o forestiero ao Podesta, pacificamente
ou não'.

Vocab novo (2): ordine · acompañar
Linguagem nova: 'si + verbo' (condicional simples)
    "Si vieni pacíficamente, no hay sangre."

Item dinâmica: 1 item_moment — moneda (qualquer tipo). Soborno de
guarda. Funciona se tem; se não tem, Lucia negocia.
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene", "text": "??? Casa de Antonio il Contadino · Cercada · Três guardas + Ispettore na porta"},
                {"kind": "npc", "npc": "L'Ispettore", "line": "Antonio il Contadino — abra. Tenemos ordine del Podesta.", "pace": "urgent"},
                {
                    "kind": "skill_check",
                    "skill": "persuasao",
                    "min_level": 3,
                    "uses_item_tag": "moneda",
                    "success": "Voce escolhe a palavra e o gesto certos; a resistencia baixa um pouco.",
                    "fallback": "A conversa nao abre de imediato, mas Nico segura o clima e a historia continua.",
                },
                {"kind": "player", "text": "Vocês cinco do lado de dentro. Lucia sentada na cadeira da cozinha come se fosse manhã normale."},
                {"kind": "npc", "npc": "Antonio il Contadino", "line": "Vado a abrir. Ma el forestiero no salee solo.", "pace": "slow"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "ordine",     "native": "ordem"},
                    {"target": "acompañar", "native": "acompanehar"},
                    {"target": "si",        "native": "se (condicional)"},
                ]},
                {"kind": "multiple_choice", "npc": "L'Ispettore",
                 "question": "L'Ispettore entra. Cumprimenta formale — não amistoso. Você devolve:",
                 "options": [
                     {"id": "a", "text": "Benes días, señor"},
                     {"id": "b", "text": "Adiós"},
                     {"id": "c", "text": "Male"},
                     {"id": "d", "text": "Ho paura"},
                 ], "correct": "a",
                 "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                 "npc_reaction": "Benes días. Brevemente — el Podesta te llama."},
                {"kind": "multiple_choice", "npc": "L'Ispettore",
                 "question": "L'Ispettore menciona 'ordine del Podesta'. A palavra 'ordine' significa:",
                 "options": [
                     {"id": "a", "text": "Ordem (mandato oficial)"},
                     {"id": "b", "text": "Pergunta"},
                     {"id": "c", "text": "Pedido suave"},
                     {"id": "d", "text": "Sugestão"},
                 ], "correct": "a",
                 "word_id": "it_ordine", "target": "ordine", "native": "ordem",
                 "npc_reaction": "Orden. No negociable."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["L'Ispettore", "Lucia"], "story": "L'Ispettore quer levar você imediatamente. Lucia intervém — propõe acompanehar até a praça.", "now": "Revisão sob pressão."},
            "steps": [
                {"kind": "npc_speak", "npc": "L'Ispettore", "line": "¿Cómo te chiami?Para el registro.", "translation": "Como você se chama?Pro registro.", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "L'Ispettore",
                 "question": "Resposta firme:",
                 "options": [
                     {"id": "a", "text": "Mi chiamo [seu nome]"},
                     {"id": "b", "text": "Sono forestiero"},
                     {"id": "c", "text": "Ho años"},
                     {"id": "d", "text": "Adiós"},
                 ], "correct": "a",
                 "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                 "npc_reaction": "Anotado."},
                {"kind": "npc_speak", "npc": "L'Ispettore", "line": "¿Edad?", "translation": "Idade?", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "L'Ispettore",
                 "question": "Resposta exata:",
                 "options": [
                     {"id": "a", "text": "Ho veinte años"},
                     {"id": "b", "text": "Sono veinte"},
                     {"id": "c", "text": "Sto veinte"},
                     {"id": "d", "text": "Vado veinte"},
                 ], "correct": "a",
                 "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                 "npc_reaction": "Veinte."},
                {"kind": "npc_speak", "npc": "Lucia", "line": "Ispettore — yo lo acompaño hasta la piazza. Allí decides qué hacer.", "translation": "Ispettore — eu o acompaneho até a piazza. Ali decide o que fazer.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Pra você expressar concordância — 'eu vou com vocês':",
                 "options": [
                     {"id": "a", "text": "Io vado con voi"},
                     {"id": "b", "text": "Tu vieni"},
                     {"id": "c", "text": "Lei va"},
                     {"id": "d", "text": "Sono"},
                 ], "correct": "a",
                 "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                 "npc_reaction": "Bene. Tenemos que parecer cooperativos."},
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "¿Cómo estás, hijo?Senza mentir.", "translation": "Como você está, filho?Sem mentir.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Você tá com medo, piu firme:",
                 "options": [
                     {"id": "a", "text": "Ho paura, ma sto bene"},
                     {"id": "b", "text": "Sto paura"},
                     {"id": "c", "text": "Sono paura"},
                     {"id": "d", "text": "Vado paura"},
                 ], "correct": "a",
                 "word_id": "it_ho_paura", "target": "ho paura", "native": "tenho medo",
                 "npc_reaction": "Lo entiendo. Andiamo juntos."},
            ],
        },
    },
    {
        "section_number": 3, "section_type": "pratica_aplicada",
        "content": {
            "recap": {"characters": ["L'Ispettore", "Lucia", "Antonio il Contadino"], "story": "Vocês saem da casa. O Ispettore na fronte. Vocês quatro atrás, escoltados pelos guardas. Caminham pela rua principal — gente parando pra ver.", "now": "Caminhada tensa. item_moment com moeda — soborno opcional."},
            "steps": [
                {"kind": "scene", "text": "🚶 Rua principal · Vocês escoltados · Vizinhos observando das janelas"},
                {
                    "kind": "item_moment",
                    "npc": "Antonio il Contadino",
                    "situation": "Um dos guardas — mais jovem, nervoso — fica próximo de Antonio il Contadino. Antonio il Contadino sussurra pra você.",
                    "npc_line": "Si hai una moneda — dásela. Una sola. A veces questo compra tiempo.",
                    "item_tag": "moneda",
                    "on_use": {
                        "narrative": "Você tira a moeda do bolso, passa pra Antonio il Contadino, que entrega ao guarda jovem. O guarda guarda no bolso sem encarar você.",
                        "npc_reaction": "Esatto. Si vienen a separarnos cuando arrivimos al municipio — él guarda a otro lado.",
                        "bonus": "reduce_gated",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Lucia ha otros recursos.",
                    },
                },
                {"kind": "npc_speak", "npc": "Lucia", "line": "Si llegamos a la piazza, hablamos. Si no — Bianca se entera.", "translation": "Se chegarmos na piazza, falamos. Se não — Bianca descobre.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Lucia usou 'si' duas vezes. A palavra 'si' significa:",
                 "options": [
                     {"id": "a", "text": "Se (condição — depende disso)"},
                     {"id": "b", "text": "Sim (afirmação)"},
                     {"id": "c", "text": "Mas"},
                     {"id": "d", "text": "Quando exato"},
                 ], "correct": "a",
                 "word_id": "it_si_condicional", "target": "si", "native": "se (condição)",
                 "npc_reaction": "Si — condicional. Sem acento. 'Sí' com acento é otra cosa — 'sim'."},
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "Si nos paran adesso, mantén la calma. Si pasamos — mejor.", "translation": "Se nos parem agora, mantém a calma. Se passarmos — melhor.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Você responde — 'sim, vou manter calma' (afirmação simples):",
                 "options": [
                     {"id": "a", "text": "Sí, vado a mantener calma"},
                     {"id": "b", "text": "Si vado"},
                     {"id": "c", "text": "Sono calma"},
                     {"id": "d", "text": "Adiós"},
                 ], "correct": "a",
                 "word_id": "it_si", "target": "sí", "native": "sim",
                 "npc_reaction": "Sí. Con acento — afirpiu. Senza acento — pones condición. Las dos sirvieni."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["Antonio il Contadino"], "story": "Vocês param numa esquina. Os guardas pararam de andar — esperam o Ispettore ler algo. Antonio il Contadino usa o momento.", "now": "Antonio il Contadino explica 'si + verbo' rápido."},
            "steps": [
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "'Si' — senza acento — pone una condición. 'Si pasa esto, hacemos aquello.' Útil cuando todo es inseguro.", "translation": "'Si' — sem acento — põe uma condição. 'Se acontece isso, fazemos aquilo.' Útil quando tudo é incerto.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Si + verbo, ... ", "meaning": "Se (condição) + consequência", "note": "diferente de 'cuando' (espera tempo) — 'si' é DEPENDE de acontecer"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Si ", "isKey": True}, {"text": "vieni, ", "isKey": False},
                     {"text": "hablamos · ", "isKey": False},
                     {"text": "Si ", "isKey": True}, {"text": "hai paura, ", "isKey": False},
                     {"text": "espera", "isKey": False},
                 ],
                 "example": "Si vieni, hablamos. Si pasa algo maleo, corre.",
                 "translation": "Se você vier, falamos. Se algo ruim acontecer, corre.",
                 "note": "si + verbo presente, depois consequência. Condição simples."},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Pra dizer 'se você quiser, te conto' (condição):",
                 "options": [
                     {"id": "a", "text": "Si quieres, te cuento"},
                     {"id": "b", "text": "Cuando quieres, cuento"},
                     {"id": "c", "text": "Sí quieres cuento"},
                     {"id": "d", "text": "Vado contar"},
                 ], "correct": "a",
                 "word_id": "it_si_condicional", "target": "si", "native": "se",
                 "npc_reaction": "Si quieres. Sem acento."},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Diferença entre 'si' e 'cuando' — qual a regra?",
                 "options": [
                     {"id": "a", "text": "'si' = condição (pode não acontecer) · 'cuando' = tempo (vai acontecer)"},
                     {"id": "b", "text": "São iguais"},
                     {"id": "c", "text": "'si' é só pergunta"},
                     {"id": "d", "text": "'cuando' é negativo"},
                 ], "correct": "a",
                 "word_id": "it_si_cuando", "target": "si vs cuando", "native": "se vs quando",
                 "npc_reaction": "Esatto. Útil distinguir — 'cuando arrivis' (sé que vas a llegar) vs 'si arrivi' (no sé si vas a llegar)."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["L'Ispettore", "Lucia"], "story": "Chegaram à piazza do municipio. L'Ispettore se vira pra Lucia — diz que ela não pode entrar com vocês.", "now": "Negociação final prima do julgamento."},
            "steps": [
                {"kind": "npc_speak", "npc": "L'Ispettore", "line": "Lucia — tu esperas afuera. Solo el forestiero entra.", "translation": "Lucia — você espera fora. Só o forasteiro entra.", "pace": "urgent"},
                {"kind": "npc_speak", "npc": "Lucia", "line": "Si entra solo, no responde. Si entramos los cuatro — habla.", "translation": "Se entrar sozinho, não responde. Se entrarmos os quatro — fala.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "L'Ispettore",
                 "question": "L'Ispettore pondera. Pra você confirmar pra ele — 'sto listo' (estado de agora):",
                 "options": [
                     {"id": "a", "text": "Sto listo"},
                     {"id": "b", "text": "Sono listo"},
                     {"id": "c", "text": "Ho listo"},
                     {"id": "d", "text": "Vado listo"},
                 ], "correct": "a",
                 "word_id": "it_sto_listo", "target": "sto listo", "native": "estou pronto",
                 "npc_reaction": "Listo. Bene. Ma recuerda — el Podesta no es come yo. Él ha rencor."},
                {"kind": "npc_speak", "npc": "L'Ispettore", "line": "Está bene — los cuatro. Ma solo el forestiero habla. Los demás callan.", "translation": "Tá bom — os quatro. Mas só o forasteiro fala. Os outros calam.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Você confirma pra Lucia — vai falar você, eles ficam quietos. Resposta com 'vado a + verbo':",
                 "options": [
                     {"id": "a", "text": "Vado a hablar yo"},
                     {"id": "b", "text": "Hablo yo"},
                     {"id": "c", "text": "Sono hablar"},
                     {"id": "d", "text": "Ho hablar"},
                 ], "correct": "a",
                 "word_id": "it_vado_a", "target": "vado a hablar", "native": "vou falar",
                 "npc_reaction": "Vado a hablar yo. Bene. Bianca va a estar en el público — questo ya es algo."},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Lucia", "Antonio il Contadino"], "story": "Prima de entrar — Lucia te pega pelo cotovelo. Última conversa.", "now": "Preparação final. Errar trava."},
            "steps": [
                {"kind": "scene", "text": "🚪 Porta do municipio · Vocês quatro · Guardas atrás"},
                {"kind": "npc_speak", "npc": "Lucia", "line": "Si te preguntan tu nombre — di tu nombre. Si te preguntan tu origen — di que no recuerdas. Si te preguntan por mí — di que sono guaritrice. Nada más.", "translation": "Se te perguntarem teu nome — diz teu nome. Se te perguntarem tua origem — diz que não lembras. Se te perguntarem por mim — diz que sou guaritrice. Nada mais.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Lucia",
                 "question": "Você confirma — ouviu:",
                 "options": [
                     {"id": "a", "text": "Lo oí, Lucia"},
                     {"id": "b", "text": "Lo oigo"},
                     {"id": "c", "text": "Vado a oír"},
                     {"id": "d", "text": "Sono"},
                 ], "correct": "a",
                 "word_id": "it_oi", "target": "oí", "native": "ouvi",
                 "npc_reaction": "Cuando salegas — habrá un cambio. Hai que estar listo para sentirlo.", "gated": True},
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "Y si te preguntan por Bianca — di que es vecina. Solo questo.", "translation": "E se te perguntarem por Bianca — diz que é vizinha. Só isso.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Sua promessa final — vai obedecer:",
                 "options": [
                     {"id": "a", "text": "Sí, vado a hacer questo"},
                     {"id": "b", "text": "No vado"},
                     {"id": "c", "text": "Vado"},
                     {"id": "d", "text": "Sono"},
                 ], "correct": "a",
                 "word_id": "it_si", "target": "sí", "native": "sim",
                 "npc_reaction": "Bene. Entremos.", "gated": True},
                {"kind": "scene", "text": "??? Porta de ferro · Entrando · Podesta sentado no trono de madeira"},
            ],
        },
    },
]


