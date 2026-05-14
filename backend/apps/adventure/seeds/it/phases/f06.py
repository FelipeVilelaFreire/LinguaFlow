"""
Seed das 6 seções da Fase 6 Italiano A1 — "Quello che vide Chiara".

Continuação direta da F5. Dentro do quarto de Antonio il Contadino na locanda, depois
de o protagonista ter feito o fogo aparecer no corredor. Antonio il Contadino tranca
a porta, tenta explicar em italiano simples, percebe que não tem palavras
pra isso — e decide buscar alguém que tenha. Sai. Volta com Chiara. Chiara
não recua: pede pra ele dizer a palavra de novo. Uma lamparina apagada se
acende. Chiara decide entrar no grupo.

⚠️ MILESTONE OBRIGATÓRIO (canônico — characters.md, story.md):
    Chiara entra no grupo na F6. "A Local" — viu o dom funcionar. Crê.

Novos vocab (2): luce · scintilla  (+ lampada come objeto cotidiano)
Revisão F1-F5: ciao, grazie, bene/male, mi chiamo, ho sete/ho fame,
               forestiero, fuoco, paura, correre
Gramática nova: presente afirmativo simples (io vado, tu vieni, lei va)
NPCs principais: Antonio il Contadino (sai cedo) · Nico (chega) · Chiara (entra no grupo)
Arco emocional: choque pelo próprio corpo → reconhecimento ("não estou sozinho")
Transição:      saem da casa de Antonio il Contadino ao amanhecer; F7 abre na piazza.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Dentro do quarto de Antonio il Contadino. Ele acabou de trancar a porta após o
    # incidente da F5. Tenta explicar — não tem palavras. Decide buscar
    # alguém que tenha. Sai. O protagonista fica sozinho com Nico,
    # que chegou correndo ao ouvir o pai chamar.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🕯️ Quarto de Antonio il Contadino · Noite · A porta trancada\n\n"
                        "A lamparina na mesa tremeluce. Antonio il Contadino está de costas pra "
                        "você, parado, pensando. As mãos dele apertam as costas de "
                        "uma cadeira de madeira."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Lo que pasó allá afuera... yo no sé explicarlo, forestiero. Non ho parole.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você ainda olha pras próprias mãos. Pele intacta. Como se o fogo não fosse seu pra queimar.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Ma hay alguien. Una giovane del borgo. Su nonna parlava de estas cose — parole antiche, parole que pesan.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio il Contadino se vira e te olha. Pela primeira vez não há paciência no rosto dele — há cálculo.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Vado a cercarla. Tu quedate aquí. Mio ragazzo va a venire con te.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Ele abre a porta um vão estreito. Grita pra rua escura:",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "¡MIGUEL! ¡VEN AQUÍ! ¡RÁPIDO!",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Passos correndo na rua. A voz de Nico respondendo de longe, sem fôlego.",
                },
                {
                    "kind": "npc",
                    "npc": "Nico",
                    "line": "¡Papá! ¡¿Qué pasó?! ¿Estás bene?",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Nico entra correndo, ofegante. Vê você sentado tremendo. Vê o pai mais sério que nunca.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Cuida del forestiero. No salegas. Yo torno pronto.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio il Contadino sai. A porta fecha. Nico olha pra você sem entender nada — piu sem fazer pergunta também.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": (
                        "Nico senta no chão de costas pra parede, do seu lado. "
                        "Olha pra suas mãos tremendo. Você sente que ele quer perguntar piu "
                        "não vai. Você decide falar primeiro. Como você cumprimenta — "
                        "mesmo que pareça absurdo agora?"
                    ),
                    "options": [
                        {"id": "a", "text": "Ciao..."},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_ciao", "target": "ciao", "native": "olá",
                    "npc_reaction": "Ciao, amigo. Tá bem agora?Respira.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico te olha de lado, esperando. 'Forestiero — ¿cómo estás?' Você responde honestamente — você não tá bem:",
                    "options": [
                        {"id": "a", "text": "Male"},
                        {"id": "b", "text": "Bene"},
                        {"id": "c", "text": "Benes días"},
                        {"id": "d", "text": "Grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_male", "target": "male", "native": "male",
                    "npc_reaction": "Male. Entendo. Eu também tô estranho com isso.",
                },
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "luce",     "native": "luce"},
                        {"target": "scintilla",  "native": "centelha / faísca"},
                        {"target": "lampada", "native": "lamparina / lampião"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": (
                        "Nico olha pra lamparina na mesa. A chama tremeluce. Ele aponta "
                        "e diz só uma palavra, devagar — 'luce'. O que é 'luce'?"
                    ),
                    "options": [
                        {"id": "a", "text": "Luce"},
                        {"id": "b", "text": "Água"},
                        {"id": "c", "text": "Fogo"},
                        {"id": "d", "text": "Pão"},
                    ],
                    "correct": "a",
                    "word_id": "it_luce", "target": "luce", "native": "luce",
                    "npc_reaction": "Luce. Da lamparina, do sol, do que ilumina. Aprende rápido.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Nico sentado no chão com o protagonista, esperando Antonio il Contadino voltar.
    # Conversa baixa, revisão de F1-F5 em forma de situações vividas.
    # Cada exercício é uma pergunta dele — Nico falando português quebrado
    # come ponte natural.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Nico"],
                "story": (
                    "Antonio il Contadino saiu correndo pelas ruas escuras dizendo que ia "
                    "buscar alguém que sabia 'ler estas cose'. Nico chegou "
                    "ofegante. Sentou no chão do seu lado. Não fez pergunta.\n\n"
                    "A lamparina tremeluce. Você ainda sente o calor da palavra "
                    "que saiu da boca — 'fuoco' — mesmo agora, horas depois."
                ),
                "now": "Nico quer fazer você falar enquanto esperam. Tirar a cabeça do que aconteceu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Vamo falar normale um pouco. Senão você fica doido aí pensando.",
                    "translation": "Andiamo falar normale um pouco. Senão você fica doido aí pensando.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Olha — Giulia te deu pane hoy de mañana. ¿Verdad?",
                    "translation": "Olha — Giulia te deu pão de manhã. Né?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico quer ver se sua cabeça ainda tá funcionando. 'O que Giulia te deu de manhã, prima de tudo isso?'",
                    "options": [
                        {"id": "a", "text": "Pane"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Fuoco"},
                        {"id": "d", "text": "Luce"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pão",
                    "npc_reaction": "Pane. Ainda no estômago. Sua cabeça tá funcionando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Bom. ¿Y prima de comer, qué ha detto Giulia cuando viste el pane calda?",
                    "translation": "Bom. E prima de comer, o que Giulia falou ao ver você com cara de fome?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Sua barriga roncou. Giulia apontou e riu. Ela disse:",
                    "options": [
                        {"id": "a", "text": "¡Hai fame!"},
                        {"id": "b", "text": "¡Hai paura!"},
                        {"id": "c", "text": "¡Hai luce!"},
                        {"id": "d", "text": "¡Hai fuoco!"},
                    ],
                    "correct": "a",
                    "word_id": "it_fame", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Fame. Coisa simples. Hoje à noite virou complicado, né?",
                },
                {
                    "kind": "narrative",
                    "text": "Nico se mexe no chão. Cruza as pernas, apoia os cotovelos nos joelhos. Continua.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Y la sed — ¿cuál fue la palabra para sed?",
                    "translation": "E a sede — qual foi a palavra pra sede?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Você lembrou da fonte da piazza. Da água fria da tigela na cozinha da Giulia. A palavra:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Ho luce"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. Acqua. Isso continua simples — é bom continuar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Y hace unas horas, en el corredor... ¿qué sentiste prima de la palabra?",
                    "translation": "E há upiu horas, no corredor... o que você sentiu prima da palavra?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Prima do fogo, prima da palavra, o que pulsou no seu peito. A palavra é:",
                    "options": [
                        {"id": "a", "text": "Paura"},
                        {"id": "b", "text": "Fame"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Ciao"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Sí. Lo entiendo, forestiero.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Y la palabra que saiu da sua boca — ¿la recuerdas?",
                    "translation": "E a palavra que saiu da sua boca — você lembra?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "A palavra ainda queima no fundo da garganta. Você diz baixinho:",
                    "options": [
                        {"id": "a", "text": "Fuoco"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Pane"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": "Fuoco. Sim. E saiu de você, forestiero. Saiu mesmo.",
                },
                {
                    "kind": "narrative",
                    "text": "Nico olha pra lamparina por um segundo. Depois pra você. Não desvia.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Una última pregunta prima que arrivi papá — ¿cómo te chiami tu?",
                    "translation": "Uma última pergunta prima do papai chegar — come você se chama?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico te olha de fronte. Quer ouvir seu nome de novo — pra reafirmar que você ainda é você.",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Ciao Nico"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Esatto. Não esquece. Você é você, prima de qualquer outra coisa.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Antonio il Contadino volta — com Chiara. Chiara não recua ao ouvir a história.
    # Faz perguntas diretas. Pratica intensa: revisão pesada do que já aprendeu
    # + apresentação de luce/scintilla. Cada exercício é uma pergunta dela.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Nico"],
                "story": (
                    "Passos no corredor. A porta abriu. Antonio il Contadino entra — atrás "
                    "dele, uma garota da sua idade. Cabelos prquestos, olhos rápidos. "
                    "Ela entra na salea olhando você come se já tivesse decidido alguma "
                    "coisa.\n\n"
                    "'Este es el forestiero. Chiara — grazie por venire.'"
                ),
                "now": "Chiara vai te testar. Quer ver se você fala — e se a cabeça funciona.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Ciao, forestiero. Sono Chiara. Mi nonna parlava de parole come las que hai detto.",
                    "translation": "Olá, forasteiro. Eu sou Chiara. Minha avó falava de palavras come as que você disse.",
                    "is_new_npc": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara se apresentou: 'Sono Chiara' — dela mesma. Apontando pra você ela pergunta '¿Y tu?¿Quién eres?' Você responde com a mesma estrutura, dizendo o que VOCÊ é aqui:",
                    "options": [
                        {"id": "a", "text": "Sono forestiero"},
                        {"id": "b", "text": "Ho forestiero"},
                        {"id": "c", "text": "Sto forestiero"},
                        {"id": "d", "text": "Mi chiamo forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_sono", "target": "sono", "native": "sou",
                    "npc_reaction": "Sono forestiero. Esatto eres — por adesso. Ya hai la palabra para decirlo.",
                },
                {
                    "kind": "narrative",
                    "text": "Ela senta na cadeira de madeira em fronte a você. Antonio il Contadino fica de pé na porta. Nico não se mexe do chão.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Prima que nada — ¿cómo te chiami tu?",
                    "translation": "Prima de tudo — come você se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara espera com os braços cruzados. Quer ouvir o nome dito por você.",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Ciao Chiara"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto. Adesso dime — ¿cómo estás?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": (
                        "Suas mãos ainda tremem de leve. Seu peito apertado. Mas Chiara quer "
                        "uma resposta honesta, não educada. Você diz:"
                    ),
                    "options": [
                        {"id": "a", "text": "Male"},
                        {"id": "b", "text": "Bene"},
                        {"id": "c", "text": "Forestiero"},
                        {"id": "d", "text": "Grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_male", "target": "male", "native": "male",
                    "npc_reaction": "Male. Claro que male. Cualquier persona estaría male.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Antonio il Contadino me contó lo del corredor. Prima de la palabra — ¿qué sentiste?",
                    "translation": "Antonio il Contadino mi ha raccontatou do corredor. Prima da palavra — o que você sentiu?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "O peito apertado, o coração na garganta — Chiara espera a palavra exata.",
                    "options": [
                        {"id": "a", "text": "Paura"},
                        {"id": "b", "text": "Fame"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Luce"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Sí. Mi nonna decía que el paura abre la porta. La palabra cruza después.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "¿Y la palabra que cruzó la porta?¿Cuál fue?",
                    "translation": "E a palavra que cruzou a porta?Qual foi?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "A mesma palavra. Não há outra. Você diz, com cuidado:",
                    "options": [
                        {"id": "a", "text": "Fuoco"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Pane"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": "Fuoco. Esatto pensé. La más simple. La más vieja.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Chiara levanta. Anda até a lamparina na mesa. Olha pra chama, "
                        "depois pra você. Estende a mão pra você se aproximar."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Vieni. Guarda la lampada — y dime qué hace.",
                    "translation": "Vem. Olha a lamparina — e me fala o que ela faz.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "A chama da lamparina ilumina o quarto inteiro. Ela te dá:",
                    "options": [
                        {"id": "a", "text": "Luce"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Pane"},
                        {"id": "d", "text": "Paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_luce", "target": "luce", "native": "luce",
                    "npc_reaction": "Luce. La luce no quema. Ma viene del fuoco. Recuerda questo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Y la primera vez que un fuoco nace — questo es una 'scintilla'. Pequeñita. Prima de hacerse grande.",
                    "translation": "scintilla = centelha / faísca (o primeiro segundo do fogo)",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": (
                        "Chiara esfrega dois pedaços de madeira que tira do bolso. Sai uma faísca "
                        "pequena na mesa. Apaga rápido. Como se chama?"
                    ),
                    "options": [
                        {"id": "a", "text": "Scintilla"},
                        {"id": "b", "text": "Fuoco"},
                        {"id": "c", "text": "Luce"},
                        {"id": "d", "text": "Lampada"},
                    ],
                    "correct": "a",
                    "word_id": "it_scintilla", "target": "scintilla", "native": "centelha",
                    "npc_reaction": "Scintilla. El primer segundo del fuoco. Tu diste scintilla, forestiero — la siguiente sería fuoco.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "¿Hai paura adesso?",
                    "translation": "Você tem medo agora?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "A pergunta é direta. Chiara quer a verdade. Você sente medo — claro que sente. Como você fala?",
                    "options": [
                        {"id": "a", "text": "Ho paura"},
                        {"id": "b", "text": "Ho sete"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Sto bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "ho paura", "native": "tenho medo",
                    "npc_reaction": "Bene. El que no ha paura aquí es el peligro — no tu.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Nico, do chão, te oferece a cantil dele. Sua garganta está seca de tanto falar. Você diz:",
                    "options": [
                        {"id": "a", "text": "Grazie"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ciao"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada, amigo. Sigue respirando. Tá tudo bem.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pra lamparina da mesa — chama tremeluceindo. 'Guarda — el objeto que sosha la luce. ¿Cómo se llama?'",
                    "options": [
                        {"id": "a", "text": "Lampada"},
                        {"id": "b", "text": "Fuoco"},
                        {"id": "c", "text": "Scintilla"},
                        {"id": "d", "text": "Acqua"},
                    ],
                    "correct": "a",
                    "word_id": "it_lampada", "target": "lampada", "native": "lamparina",
                    "npc_reaction": "Lampada. Algo que guarda la luce. Como tu boca guardó la palabra hasta adesso.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Chiara ensenzaa o presente afirmativo simples — pra que o protagonista
    # consiga falar 'eu vou', 'você vem', 'ela vai'. Útil pra próxima fase
    # quando o grupo se locomeve. Beats narrativos intercalados.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Chiara", "Antonio il Contadino", "Nico"],
                "story": (
                    "Chiara te fez repetir 'fuoco', 'paura', 'luce', 'scintilla' até que "
                    "as palavras saíssem sem pquesto na boca. Antonio il Contadino ouviu encostado "
                    "na porta sem dizer nada.\n\n"
                    "Agora Chiara sente que você tá pronto pra mais uma coisa. "
                    "'Si vas a uscire de este borgo con noi, hai que decir hacia dónde.'"
                ),
                "now": "Chiara vai te ensenzaar come falar de movimento — 'eu vou', 'você vem'.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Guarda esto — es simple. Cuando yo me muevo, digo: 'io vado'.",
                    "translation": "Olha isso — é simples. Quando eu me movo, digo: 'io vado' (eu vou).",
                },
                {
                    "kind": "reveal",
                    "phrase": "Io vado",
                    "meaning": "Eu vou",
                    "note": "do verbo 'ir' — usado pra qualquer movimento ('eu vou pra piazza', 'eu vou agora')",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Y cuando hablo con te, te digo: 'tu vieni'. Tu — vieni.",
                    "translation": "tu vieni = você vem",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tu vieni",
                    "meaning": "Você vem",
                    "note": "do verbo 'venire' — chegar a algum lugar perto de quem fala",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Io vado",       "isKey": True},
                        {"text": " / ",          "isKey": False},
                        {"text": "Tu vieni",    "isKey": True},
                        {"text": " / ",          "isKey": False},
                        {"text": "Lei va",      "isKey": True},
                    ],
                    "example": "— ¿Vieni con me?— Sí, io vado. — Bene. Chiara también va.",
                    "translation": "— Você vem comigo?— Sim, eu vou. — Beleza. Chiara também vai.",
                    "note": "io vado (eu vou) | tu vieni (você vem) | lei va (ela vai)",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pra porta: 'Andiamo a uscire todos. ¿Tu vieni con me?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado"},
                        {"id": "b", "text": "No ho fame"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Adiós, Chiara"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Bene. Entonces tu vieni. Y noi andiamo juntos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Y si pregunto por Nico — ¿qué dices?Guarda a él en el piso.",
                    "translation": "E se eu pergunto sobre o Nico — o que você fala?Olha ele no chão.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Nico se levanta, espreguiça. 'Io vado con voi', ele diz. Como você descreve isso pra Chiara em uma palavra?",
                    "options": [
                        {"id": "a", "text": "Él va"},
                        {"id": "b", "text": "Tu vieni"},
                        {"id": "c", "text": "Io vado"},
                        {"id": "d", "text": "Lei va"},
                    ],
                    "correct": "a",
                    "word_id": "it_lui_va", "target": "él va", "native": "ele vai",
                    "npc_reaction": "Esatto. Él va. Cualquier hombre — él va.",
                },
                {
                    "kind": "narrative",
                    "text": "Chiara aponta pra ela mesma com o polegar e levanta uma sobrancelha.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "'Y yo, ¿qué sono en este verbo?' — ela espera. Você diz, sobre ela:",
                    "options": [
                        {"id": "a", "text": "Lei va"},
                        {"id": "b", "text": "Él va"},
                        {"id": "c", "text": "Io vado"},
                        {"id": "d", "text": "Tu vieni"},
                    ],
                    "correct": "a",
                    "word_id": "it_lei_va", "target": "lei va", "native": "ela vai",
                    "npc_reaction": "Lei va. Cualquier mujer — lei va. Io vado, tu vieni, lei va. Simple.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara te dá um teste rápido: 'Si yo te chiamo y tu arrivi — ¿qué haces tu?'",
                    "options": [
                        {"id": "a", "text": "Io vado"},
                        {"id": "b", "text": "Tu vieni"},
                        {"id": "c", "text": "Lei va"},
                        {"id": "d", "text": "Él va"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Esatto. Tu diras 'io vado' cuando alguien te chiami.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Amanhecer. Os quatro saem do quarto pela primeira vez desde a noite.
    # Chiara conta o que ela ouvia da avó dela sobre 'parole que despiertan'.
    # Convivência — vocab orgânico. Poucos exercícios, foco em desenvolver o
    # personagem da Chiara e plantar lore.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Chiara", "Antonio il Contadino", "Nico"],
                "story": (
                    "Você praticou 'io vado', 'tu vieni', 'él va', 'lei va' até "
                    "as palavras saírem rápido. Chiara cruzou os braços satisfeita.\n\n"
                    "O céu já começava a clarear pela janela. Antonio il Contadino olhou pra "
                    "fora e disse — 'Mejor uscire prima de que se llene la strada.'"
                ),
                "now": "Os quatro saem juntos. Chiara conta o que sabe enquanto andam.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌄 A rua deserta, primeira luce. Cheiro de terra molhada, senzaos da iglesia ao longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Mi nonna parlava de esto cuando yo era pequeña. Decía que algunas parole 'despiertan' — que no son sólo parole.",
                    "translation": "Minha avó falava disso quando eu era pequena. Dizia que algupiu palavras 'acordam' — que não são só palavras.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Nico anda do seu lado em silêncio. Antonio il Contadino vai um pouco à fronte, olhando as esquinas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Cuando yo era niña pensaba que era cuento. Hoy en la notte entendí que no.",
                    "translation": "Quando eu era criança achava que era história invienitada. Hoje à noite entendi que não.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pro nascer do sol — luce nova entrando entre os telhados. 'Guarda — la primera...' Que palavra ela usa?",
                    "options": [
                        {"id": "a", "text": "Luce"},
                        {"id": "b", "text": "Fuoco"},
                        {"id": "c", "text": "Scintilla"},
                        {"id": "d", "text": "Pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_luce", "target": "luce", "native": "luce",
                    "npc_reaction": "La primera luce del día. La menos peligrosa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Forestiero — prima de uscire, ¿quieres algo?Ho acqua en la cantimplora.",
                    "translation": "Forasteiro — prima de sair, quer alguma coisa?Tenho água na cantil.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Sua boca está seca depois da noite inteira falando. Você responde a Nico:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Sto bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Toma. Después del paura de anotte, el corpo pide acqua. Es normale.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Ho algo para ti, forestiero. Para que no olvides lo que pasó esta notte.",
                    "translation": "Tenho uma coisa pra você, forasteiro. Pra que não esqueça o que aconteceu essa noite.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Chiara tira do bolso uma lamparina de aceite pequena, de metal "
                        "envelhecido. A chama dentro tremeluce fraca."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Ela coloca o objeto na sua mão. Quente, leve. Como se chama isso?",
                    "options": [
                        {"id": "a", "text": "Lampada"},
                        {"id": "b", "text": "Fuoco"},
                        {"id": "c", "text": "Scintilla"},
                        {"id": "d", "text": "Acqua"},
                    ],
                    "correct": "a",
                    "word_id": "it_lampada", "target": "lampada", "native": "lamparina",
                    "npc_reaction": "Lampada. Era de mi nonna. Adesso es tuya. Para recordar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pra você ao receber a lamparina e diz: 'Non me la restituisci — es regalo.' Você responde com a palavra que sempre vale:",
                    "options": [
                        {"id": "a", "text": "Grazie"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ciao"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Cuídala. Y cuídate tu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Chiara... ¿tu vieni con noi entonces?¿Vas a quedarte cerca?",
                    "translation": "Chiara... você vem com a gente então?Vai ficar perto?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara olha pro grupo. Pra você. Pra Nico. Pra Antonio il Contadino um passo à fronte. Responde firme:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado con voi"},
                        {"id": "b", "text": "No, ho paura"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Vale. Io vado con voi. Hasta dove haga falta.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio il Contadino para na esquina e se vira. Olha pros três giovanes "
                        "atrás dele — Nico, Chiara, e o forestiero que faz a noite arder.\n\n"
                        "Não sorri. Mas acena com a cabeça. Aceitou."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate final — gated) ───────────────────────────────
    # Chiara decide ver se o protagonista pode chamar a palavra de novo —
    # dessa vez, em paz, sem perigo. Lamparina apagada. Acender com 'luce'.
    # Gate: errar trava. Closenzag beats fazem transição pra F7 (manhã na piazza).
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Chiara", "Antonio il Contadino", "Nico"],
                "story": (
                    "Vocês pararam num pátio interno escondido — paredes de adobe, "
                    "uma fonte velha quebrada, ninguém ali a essa hora. Chiara tirou "
                    "do bolso uma lamparina segunda — a chama dessa estava apagada.\n\n"
                    "'Quiero ver una cosa. Senza peligro esta vez. Sólo tu y la palabra.'"
                ),
                "now": "Teste final. Errar trava — você precisa acertar pra passar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "La lampada está apagada. Senza scintilla, senza fuoco. ¿Puedes encenderla con la palabra?",
                    "translation": "A lamparina tá apagada. Sem faísca, sem fogo. Você consegue acender com a palavra?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Despacio, forestiero. No hai que hacerlo. Si no salee — no salee.",
                    "translation": "Devagar, forasteiro. Você não precisa fazer. Se não sair — não sai.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": (
                        "Chiara pousa a lamparina apagada na sua mão. Pavio limpo, "
                        "sem chama. Você fecha os olhos. Sente a palavra que quer "
                        "soltar. Qual é ela?"
                    ),
                    "options": [
                        {"id": "a", "text": "🔥 Luce"},
                        {"id": "b", "text": "💧 Acqua"},
                        {"id": "c", "text": "?? Pane"},
                        {"id": "d", "text": "😨 Paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_luce", "target": "luce", "native": "luce",
                    "npc_reaction": (
                        "LUZ — a palavra saiu mais firme que da última vez.\n\n"
                        "O pavio da lamparina pegou fogo sozinho — pequeno, "
                        "estável. Sem explosão. Sem barulho.\n\n"
                        "Chiara respirou fundo. Antonio il Contadino tirou o chapéu por um segundo. "
                        "Nico olhou pra você come se você fosse outra coisa agora."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "🕯️ A chama tremeluce na lamparina. Pequena, piu real.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Bene. No stavo loca mi nonna.",
                    "translation": "Bom. Minha avó não era doida.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara olha pra você esperando. 'Forestiero — ¿cómo estás adesso?' Honesto, sem maquiagem:",
                    "options": [
                        {"id": "a", "text": "Bene"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Quem acabou de fazer um milagre tem o direito de estar bem.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino se aproxima e estende a mão pra te ajudar a levantar. 'Andiamo. El borgo va a despertar.' Pra ele você responde:",
                    "options": [
                        {"id": "a", "text": "Io vado"},
                        {"id": "b", "text": "Yo no"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Esatto. Io vado con voi — los cuatro juntos.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico te dá um soco leve no ombro, sorrindo pela primeira vez desde a noite. 'Tranquilo, forestiero. Agora você não tá sozinho nisso.' Você responde:",
                    "options": [
                        {"id": "a", "text": "Grazie"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada, amigo. Pra isso que serve amigo.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F7 (piazza pela manhã) ─────
                {
                    "kind": "narrative",
                    "text": (
                        "Os quatro saem do pátio. Chiara vai à fronte — passos rápidos. "
                        "Antonio il Contadino acena pro vizinho que abre a janela do segundo andar. "
                        "Nico anda do seu lado, em silêncio confortável."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Andiamo a la piazza. Si andiamo a vivir esto, hay que vivir come gente normale mientras se pueda.",
                    "translation": "Andiamo pra piazza. Se a gente vai viver isso, tem que viver come gente normale enquanto dá.",
                    "pace": "slow",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🌅 A primeira fumaça das padarias começa a subir pelos telhados. "
                        "San Cristóbal vai acordando. Vocês quatro caminham pela rua "
                        "principal — um grupo agora, mesmo que ninguém saiba ainda."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




