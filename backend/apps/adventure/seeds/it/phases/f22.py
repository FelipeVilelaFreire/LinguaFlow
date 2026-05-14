"""
Seed das 6 seções da Fase 22 Italiano A1 — "La verdad parcial".

Bianca entrega um envelope guardado há 20 anni pelo Buscador — pertence
ao forestiero, não a Antonio il Contadino. Dentro: um NOME. Não 'forestiero'.

Vocab novo (2): nombre · contar
Linguagem nova: contar / contar de / contar a (verbo 'contar' em diferentes usos)

Item dinâmica: 1 baú aberto durante a fase (S5 — Bianca entrega Carta Sellada
do pool raro). Sistema escolhe item pra esse user.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [
    {
        "section_number": 1, "section_type": "narrativa",
        "content": {
            "beats": [
                {"kind": "scene",     "text": "🌞 Piazza · Sol alto · Bianca no banco com um envelope nos joelhos"},
                {"kind": "npc",       "npc": "Bianca", "line": "Lo guardo hace veinte años. Pertenece al forestiero — no a Antonio il Contadino.", "pace": "slow"},
                {"kind": "player",    "text": "Chiara e Nico atrás. Antonio il Contadino ao seu lado. Vocês quatro encarando o envelope."},
                {"kind": "npc",       "npc": "Bianca", "line": "Ábrelo tu. Prima que arrivi el Ispettore.", "pace": "urgent"},
            ],
            "exercises": [
                {"kind": "vocab_list", "items": [
                    {"target": "nombre", "native": "nome"},
                    {"target": "contar", "native": "contar / narrar"},
                ]},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Você cumprimenta Bianca:",
                 "options": [
                     {"id": "a", "text": "Benes días, Bianca"},
                     {"id": "b", "text": "Buona notte"},
                     {"id": "c", "text": "Adiós"},
                     {"id": "d", "text": "Male"},
                 ], "correct": "a",
                 "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                 "npc_reaction": "Benes días. Ma hoy no es día de saleudos largos."},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Bianca entrega o envelope. Você agradece — formale, senzacero:",
                 "options": [
                     {"id": "a", "text": "Grazie, Bianca"},
                     {"id": "b", "text": "Adiós Bianca"},
                     {"id": "c", "text": "Ho Bianca"},
                     {"id": "d", "text": "Male"},
                 ], "correct": "a",
                 "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                 "npc_reaction": "De nada. Veinte años guardándolo. Hoy es tuyo."},
            ],
        },
    },
    {
        "section_number": 2, "section_type": "revisao_srs",
        "content": {
            "recap": {"characters": ["Bianca"], "story": "Você ainda não abriu o envelope. Bianca quer testar primeiro — pra ver se você tá pronto pra ouvir.", "now": "Revisão. Bianca mistura tudo."},
            "steps": [
                {"kind": "npc_speak", "npc": "Bianca", "line": "Prima — dime quién eres en este borgo.", "translation": "Prima — me diz quem você é nesse borgo.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Identidade (SER):",
                 "options": [
                     {"id": "a", "text": "Sono forestiero"},
                     {"id": "b", "text": "Sto forestiero"},
                     {"id": "c", "text": "Ho forestiero"},
                     {"id": "d", "text": "Vado forestiero"},
                 ], "correct": "a",
                 "word_id": "it_sono", "target": "sono", "native": "sou",
                 "npc_reaction": "Hoy. Mañana — quizá no."},
                {"kind": "npc_speak", "npc": "Bianca", "line": "¿Cuándo sei arrivato al borgo?Cuéntame en pasado.", "translation": "Quando você chegou no borgo?Conta no passado.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Pretérito (você chegou):",
                 "options": [
                     {"id": "a", "text": "Llegué hace tres semanas"},
                     {"id": "b", "text": "Llego hace tres semanas"},
                     {"id": "c", "text": "Vado a llegar"},
                     {"id": "d", "text": "Sono"},
                 ], "correct": "a",
                 "word_id": "it_arrivi", "target": "llegué", "native": "cheguei",
                 "npc_reaction": "Tres semanas. Y mucho cambió en ti en este tiempo."},
                {"kind": "npc_speak", "npc": "Bianca", "line": "¿Y la palabra de la carta — qué leíste?", "translation": "E a palavra da carta — o que você leu?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "A palavra que você leu na F19:",
                 "options": [
                     {"id": "a", "text": "Leí 'vuelves'"},
                     {"id": "b", "text": "Leo 'vuelves'"},
                     {"id": "c", "text": "Vado a leer"},
                     {"id": "d", "text": "Sono"},
                 ], "correct": "a",
                 "word_id": "it_lei", "target": "leí", "native": "li",
                 "npc_reaction": "Leíste. Pasado. Y hoy — vas a leer una segunda."},
                {"kind": "npc_speak", "npc": "Bianca", "line": "¿Cómo te sientes adesso?", "translation": "Como você se sente agora?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Honesto — nervoso, piu firme:",
                 "options": [
                     {"id": "a", "text": "Sto nervioso, ma listo"},
                     {"id": "b", "text": "Sono nervioso"},
                     {"id": "c", "text": "Ho nervioso"},
                     {"id": "d", "text": "Vado nervioso"},
                 ], "correct": "a",
                 "word_id": "it_sto_nervioso", "target": "sto nervioso", "native": "estou nervoso",
                 "npc_reaction": "Bene. Ábrelo cuando estés listo. Toma tu tiempo."},
            ],
        },
    },
    {
        "section_number": 3, "section_type": "pratica_aplicada",
        "content": {
            "recap": {"characters": ["Bianca", "Antonio il Contadino"], "story": "Você abre o envelope com a navaja que Antonio il Contadino passou. Papel velho, amarelado. Uma única palavra escrita no meio.", "now": "Você lê. Tudo muda."},
            "steps": [
                {"kind": "scene", "text": "📜 Papel amarelado · Letra firme · No centro, um nome"},
                {"kind": "player", "text": "Você lê. O nome NÃO é 'forestiero'. É um nome próprio. Você sente o peito apertar — você reconhece, piu não lembra de onde."},
                {"kind": "npc_speak", "npc": "Bianca", "line": "Cuéntame — ¿lo reconoces?", "translation": "Me conta — você reconhece?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Você reconhece — piu não consegue lembrar de onde. Resposta híbrida (sim e ainda não):",
                 "options": [
                     {"id": "a", "text": "Sí, ma todavía no me acuerdo"},
                     {"id": "b", "text": "No, no conozco"},
                     {"id": "c", "text": "Vado a recordar"},
                     {"id": "d", "text": "Sono"},
                 ], "correct": "a",
                 "word_id": "it_si", "target": "sí", "native": "sim",
                 "npc_reaction": "Sí ma todavía no. Esatto es lo más honesto que puedes decir hoy."},
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "¿Vas a contarles a Chiara y Nico ese nombre?", "translation": "Você vai contar pra Chiara e Nico esse nome?", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Antonio il Contadino",
                 "question": "Sim — eles merecem saber (futuro próximo, 1ª pessoa):",
                 "options": [
                     {"id": "a", "text": "Sí, vado a contarles"},
                     {"id": "b", "text": "Sí, cuento"},
                     {"id": "c", "text": "Sí, sono contar"},
                     {"id": "d", "text": "Sí, ho contar"},
                 ], "correct": "a",
                 "word_id": "it_vado_a", "target": "vado a contar", "native": "vou contar",
                 "npc_reaction": "Bene. Senza guardar nada — questo ya no sirve."},
                {"kind": "npc_speak", "npc": "Bianca", "line": "El verbo 'contar' ha varios usos — te lo explico cuando termines.", "translation": "O verbo 'contar' tem vários usos — te explico quando você terminar.", "pace": "slow"},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Pra agradecer Bianca pelo envelope, depois de tantos anni:",
                 "options": [
                     {"id": "a", "text": "Grazie por guardarlo tanto tiempo"},
                     {"id": "b", "text": "Adiós Bianca"},
                     {"id": "c", "text": "Sono grazie"},
                     {"id": "d", "text": "Vado grazie"},
                 ], "correct": "a",
                 "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                 "npc_reaction": "Lo guardé porque me lo pidió un buen hombre. Hoy lo entrego al heredero corretto."},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Bianca pergunta '¿qué vas a hacer con el nombre?'. Sua resposta — vai contar pros amigos:",
                 "options": [
                     {"id": "a", "text": "Vado a contarles a Chiara y Nico"},
                     {"id": "b", "text": "Vado contar"},
                     {"id": "c", "text": "Sono contar"},
                     {"id": "d", "text": "Ho contar"},
                 ], "correct": "a",
                 "word_id": "it_contar", "target": "contar", "native": "contar",
                 "npc_reaction": "Bene. 'Contar' a alguien — dirigir tu historia a otra persona. Importante."},
            ],
        },
    },
    {
        "section_number": 4, "section_type": "gramatica_narrativa",
        "content": {
            "recap": {"characters": ["Bianca"], "story": "Bianca quer te ensenzaar 'contar' direito — verbo simples piu com várias caras. Vai te servir muito.", "now": "Bianca explica 'contar'."},
            "steps": [
                {"kind": "npc_speak", "npc": "Bianca", "line": "'Contar' sirve para tres cose — números, historias y secretos. Y cambia con chi.", "translation": "'Contar' serve para três coisas — números, histórias e segredos. E muda com quem.", "pace": "slow"},
                {"kind": "reveal", "phrase": "Contar = contar / narrar / confiar segredo", "meaning": "verbo de múltiplos usos", "note": "cuento, cuentas, cuenta, contamos — cambia con chi hace"},
                {"kind": "pattern",
                 "parts": [
                     {"text": "Yo cuento ", "isKey": True}, {"text": "una historia · ", "isKey": False},
                     {"text": "Tu cuentas ", "isKey": True}, {"text": "monedas · ", "isKey": False},
                     {"text": "Ella cuenta ", "isKey": True}, {"text": "un secreto · ", "isKey": False},
                     {"text": "Contamos ", "isKey": True}, {"text": "juntos", "isKey": False},
                 ],
                 "example": "Yo cuento la historia. Tu cuentas las monedas. Lucia cuenta secretos.",
                 "translation": "Eu conto a história. Você conta as moedas. Lucia conta segredos.",
                 "note": "cuento / cuentas / cuenta / contamos — sempre algo depois (a coisa contada)"},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Você quer dizer 'eu conto pra você' (1ª pessoa):",
                 "options": [
                     {"id": "a", "text": "Yo te cuento"},
                     {"id": "b", "text": "Tu cuentas"},
                     {"id": "c", "text": "Yo contamos"},
                     {"id": "d", "text": "Sono cuento"},
                 ], "correct": "a",
                 "word_id": "it_cuento", "target": "cuento", "native": "conto",
                 "npc_reaction": "Cuento — yo. Primera persona."},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "E pra perguntar 'você me conta?' (2ª pessoa, pergunta):",
                 "options": [
                     {"id": "a", "text": "¿Me cuentas?"},
                     {"id": "b", "text": "¿Me cuento?"},
                     {"id": "c", "text": "¿Vado a contar?"},
                     {"id": "d", "text": "¿Sono contar?"},
                 ], "correct": "a",
                 "word_id": "it_cuentas", "target": "cuentas", "native": "contas",
                 "npc_reaction": "Cuentas — tu. La pregunta es directa."},
            ],
        },
    },
    {
        "section_number": 5, "section_type": "reforco",
        "content": {
            "recap": {"characters": ["Bianca", "Antonio il Contadino"], "story": "Bianca entrega uma segunda coisa prima de vocês irem — um envelope menor, lacrado, do bolso interno do vestido dela.", "now": "Você recebe um item raro. O baú abre aqui (sistema sorteia)."},
            "steps": [
                {"kind": "npc_speak", "npc": "Bianca", "line": "Esto también es tuyo. Algo que ella te dejó — no sé qué es, ma pesa.", "translation": "Isso também é teu. Algo que ela te deixou — não sei o que é, piu pesa.", "pace": "slow"},
                {"kind": "scene", "text": "?? Envelope pequeno · Cera vermelha · Símbolo do sol partido"},
                {"kind": "narrative", "text": "Você recebe um item raro — o sistema escolhe qual da fila do baú raro do seu user."},
                {"kind": "multiple_choice", "npc": "Bianca",
                 "question": "Você agradece Bianca pela segunda entrega:",
                 "options": [
                     {"id": "a", "text": "Grazie por todo"},
                     {"id": "b", "text": "Adiós"},
                     {"id": "c", "text": "Sono grazie"},
                     {"id": "d", "text": "Vado grazie"},
                 ], "correct": "a",
                 "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                 "npc_reaction": "De nada. Y cuando termine todo — vieni a verme."},
                {"kind": "npc_speak", "npc": "Antonio il Contadino", "line": "Bianca — grazie. Hoy entendemos más que en veinte años.", "translation": "Bianca — obrigado. Hoje entendemos mais do que em vinte anni.", "pace": "slow"},
            ],
        },
    },
    {
        "section_number": 6, "section_type": "obstaculo",
        "content": {
            "recap": {"characters": ["Antonio il Contadino", "Chiara", "Nico"], "story": "Voltando da piazza, vocês veem fumaça subindo do lado da casa de Antonio il Contadino. Chiara corre.", "now": "Crise. Errar trava."},
            "steps": [
                {"kind": "scene", "text": "🔥 Fumaça subindo · Casa de Antonio il Contadino · Três homens uniformizados na porta"},
                {"kind": "npc_speak", "npc": "Chiara", "line": "¡Vinieron! ¡Prima de lo esperado!", "translation": "Vieram! Prima do esperado!", "pace": "urgent"},
                {"kind": "multiple_choice", "npc": "Chiara",
                 "question": "Você reage rápido. Pra dizer 'preciso ir' (obrigação, 1ª pessoa):",
                 "options": [
                     {"id": "a", "text": "Ho que ir"},
                     {"id": "b", "text": "Vado a ir"},
                     {"id": "c", "text": "Quiero ir"},
                     {"id": "d", "text": "Sono ir"},
                 ], "correct": "a",
                 "word_id": "it_ho_que", "target": "ho que", "native": "tenho que",
                 "npc_reaction": "Hai que. Ma no solo — andiamo los cuatro.", "gated": True},
                {"kind": "multiple_choice", "npc": "Nico",
                 "question": "Nico: 'Espera — ¿qué dice el nombre que leíste?' Você ainda não vai dizer:",
                 "options": [
                     {"id": "a", "text": "Cuando estemos seguros — te cuento"},
                     {"id": "b", "text": "Ya te cuento"},
                     {"id": "c", "text": "Vado a leer"},
                     {"id": "d", "text": "Sono"},
                 ], "correct": "a",
                 "word_id": "it_cuando", "target": "cuando", "native": "quando",
                 "npc_reaction": "Cuando — bene. Hoy guardas. Mañana cuentas.", "gated": True},
                {"kind": "narrative", "text": "Vocês quatro correm. Lucia sai pela porta de trás. O Podesta está no meio da rua — atrás dos três guardas. 'Mañana es el juicio.'"},
            ],
        },
    },
]


