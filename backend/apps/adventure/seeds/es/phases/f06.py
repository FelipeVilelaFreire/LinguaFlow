"""
Seed das 6 seções da Fase 6 Espanhol A1 — "Lo que vio Sofía".

Continuação direta da F5. Dentro do quarto de Don Miguel na posada, depois
de o protagonista ter feito o fogo aparecer no corredor. Don Miguel tranca
a porta, tenta explicar em espanhol simples, percebe que não tem palavras
pra isso — e decide buscar alguém que tenha. Sai. Volta com Sofía. Sofía
não recua: pede pra ele dizer a palavra de novo. Uma lamparina apagada se
acende. Sofía decide entrar no grupo.

⚠️ MILESTONE OBRIGATÓRIO (canônico — characters.md, story.md):
    Sofía entra no grupo na F6. "A Local" — viu o dom funcionar. Crê.

Novos vocab (2): luz · chispa  (+ lámpara como objeto cotidiano)
Revisão F1-F5: hola, gracias, bien/mal, me llamo, tengo sed/hambre,
               forastero, fuego, miedo, correr
Gramática nova: presente afirmativo simples (yo voy, tú vienes, ella va)
NPCs principais: Don Miguel (sai cedo) · Miguel (chega) · Sofía (entra no grupo)
Arco emocional: choque pelo próprio corpo → reconhecimento ("não estou sozinho")
Transição:      saem da casa de Don Miguel ao amanhecer; F7 abre na plaza.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f6_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Dentro do quarto de Don Miguel. Ele acabou de trancar a porta após o
    # incidente da F5. Tenta explicar — não tem palavras. Decide buscar
    # alguém que tenha. Sai. O protagonista fica sozinho com Miguel-filho,
    # que chegou correndo ao ouvir o pai chamar.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "investigacion",
                    "min_level": 1,
                    "uses_item_tag": "documento",
                    "success": "Voce percebe que a luz responde a palavra antes de Sofia terminar a frase.",
                    "fallback": "Voce nao entende a luz ainda, mas Sofia viu o bastante para seguir com voce.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🕯️ Quarto de Don Miguel · Noite · A porta trancada\n\n"
                        "A lamparina na mesa tremeluz. Don Miguel está de costas pra "
                        "você, parado, pensando. As mãos dele apertam as costas de "
                        "uma cadeira de madeira."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Lo que pasó allá afuera... yo no sé explicarlo, forastero. No tengo palabras.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você ainda olha pras próprias mãos. Pele intacta. Como se o fogo não fosse seu pra queimar.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Pero hay alguien. Una joven del pueblo. Su abuela hablaba de estas cosas — palabras viejas, palabras que pesan.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel se vira e te olha. Pela primeira vez não há paciência no rosto dele — há cálculo.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Voy a buscarla. Tú quedate aquí. Mi mijo va a venir contigo.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Ele abre a porta um vão estreito. Grita pra rua escura:",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¡MIGUEL! ¡VEN AQUÍ! ¡RÁPIDO!",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Passos correndo na rua. A voz de Miguel respondendo de longe, sem fôlego.",
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "¡Papá! ¡¿Qué pasó?! ¿Estás bien?",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel entra correndo, ofegante. Vê você sentado tremendo. Vê o pai mais sério que nunca.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Cuida del forastero. No salgas. Yo vuelvo pronto.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel sai. A porta fecha. Miguel olha pra você sem entender nada — mas sem fazer pergunta também.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": (
                        "Miguel senta no chão de costas pra parede, do seu lado. "
                        "Olha pra suas mãos tremendo. Você sente que ele quer perguntar mas "
                        "não vai. Você decide falar primeiro. Como você cumprimenta — "
                        "mesmo que pareça absurdo agora?"
                    ),
                    "options": [
                        {"id": "a", "text": "Hola..."},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olá",
                    "npc_reaction": "Hola, amigo. ¿Estás bien ahora? Respira.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel te olha de lado, esperando. 'Forastero — ¿cómo estás?' Você responde honestamente — você não tá bem:",
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bien"},
                        {"id": "c", "text": "Buenos días"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Mal. Entiendo. Yo también estoy raro con esto.",
                },
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "luz",     "native": "luz"},
                        {"target": "chispa",  "native": "centelha / faísca"},
                        {"target": "lámpara", "native": "lamparina / lampião"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": (
                        "Miguel olha pra lamparina na mesa. A chama tremeluz. Ele aponta "
                        "e diz só uma palavra, devagar — 'luz'. O que é 'luz'?"
                    ),
                    "options": [
                        {"id": "a", "text": "Luz"},
                        {"id": "b", "text": "Água"},
                        {"id": "c", "text": "Fogo"},
                        {"id": "d", "text": "Pão"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "Luz. De la lámpara, del sol, de lo que ilumina. Aprendes rápido.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Miguel sentado no chão com o protagonista, esperando Don Miguel voltar.
    # Conversa baixa, revisão de F1-F5 em forma de situações vividas.
    # Cada exercício é uma pergunta dele — Miguel falando português quebrado
    # como ponte natural.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Miguel"],
                "story": (
                    "Don Miguel saiu correndo pelas ruas escuras dizendo que ia "
                    "buscar alguém que sabia 'ler estas cosas'. Miguel chegou "
                    "ofegante. Sentou no chão do seu lado. Não fez pergunta.\n\n"
                    "A lamparina tremeluz. Você ainda sente o calor da palavra "
                    "que saiu da boca — 'fuego' — mesmo agora, horas depois."
                ),
                "now": "Miguel quer fazer você falar enquanto esperam. Tirar a cabeça do que aconteceu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Vamos falar normal um pouco.",
                    "translation": "(português quebrado)",
                    "voice": {"lang": "pt-BR", "gender": "male", "pitch": 0.98, "rate": 0.86},
                    "speech_rate": 0.88,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Senão você fica doido aí pensando.",
                    "translation": "Vamos falar normal um pouco. Senão você fica doido aí pensando.",
                    "voice": {"lang": "pt-BR", "gender": "male", "pitch": 0.98, "rate": 0.86},
                    "speech_rate": 0.88,
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Rosa te dio pan esta mañana.",
                    "translation": "Rosa te deu pão esta manhã.",
                    "speech_rate": 0.92,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "¿Verdad?",
                    "translation": "Né?",
                    "speech_rate": 0.9,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel quer ver se sua cabeça ainda tá funcionando. 'O que Rosa te deu de manhã, antes de tudo isso?'",
                    "options": [
                        {"id": "a", "text": "Pan"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Fuego"},
                        {"id": "d", "text": "Luz"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pão",
                    "npc_reaction": "Pan. Todavía en el estómago. Tu cabeza funciona.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Bien.",
                    "translation": "Bom.",
                    "speech_rate": 0.9,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "¿Y antes de comer, qué dijo Rosa cuando vio tu cara de hambre?",
                    "translation": "E antes de comer, o que Rosa falou ao ver você com cara de fome?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Sua barriga roncou. Rosa apontou e riu. Ela disse:",
                    "options": [
                        {"id": "a", "text": "¡Tienes hambre!"},
                        {"id": "b", "text": "¡Tienes miedo!"},
                        {"id": "c", "text": "¡Tienes luz!"},
                        {"id": "d", "text": "¡Tienes fuego!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. Cosa simple. Esta noche se volvió complicada, ¿no?",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel se mexe no chão. Cruza as pernas, apoia os cotovelos nos joelhos. Continua.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y la sed — ¿cuál fue la palabra para sed?",
                    "translation": "E a sede — qual foi a palavra pra sede?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Você lembrou da fonte da plaza. Da água fria da tigela na cozinha da Rosa. A palavra:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Tengo luz"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. Agua. Eso sigue siendo simple — es bueno que algo siga así.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y hace unas horas, en el corredor... ¿qué sentiste antes de la palabra?",
                    "translation": "E há umas horas, no corredor... o que você sentiu antes da palavra?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Antes do fogo, antes da palavra, o que pulsou no seu peito. A palavra é:",
                    "options": [
                        {"id": "a", "text": "Miedo"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Hola"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Sí. Lo entiendo, forastero.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y la palabra que salió de tu boca...",
                    "translation": "E a palavra que saiu da sua boca...",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "¿La recuerdas?",
                    "translation": "E a palavra que saiu da sua boca — você lembra?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "A palavra ainda queima no fundo da garganta. Você diz baixinho:",
                    "options": [
                        {"id": "a", "text": "Fuego"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": "Fuego. Sí. Y salió de ti, forastero. Salió de verdad.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel olha pra lamparina por um segundo. Depois pra você. Não desvia.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Una última pregunta antes que llegue papá — ¿cómo te llamas tú?",
                    "translation": "Uma última pergunta antes do papai chegar — como você se chama?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel te olha de frente. Quer ouvir seu nome de novo — pra reafirmar que você ainda é você.",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Hola Miguel"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Eso. No lo olvides. Eres tú antes que cualquier otra cosa.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Don Miguel volta — com Sofía. Sofía não recua ao ouvir a história.
    # Faz perguntas diretas. Pratica intensa: revisão pesada do que já aprendeu
    # + apresentação de luz/chispa. Cada exercício é uma pergunta dela.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Miguel"],
                "story": (
                    "Passos no corredor. A porta abriu. Don Miguel entra — atrás "
                    "dele, uma garota da sua idade. Cabelos presos, olhos rápidos. "
                    "Ela entra na sala olhando você como se já tivesse decidido alguma "
                    "coisa.\n\n"
                    "'Este es el forastero. Sofía — gracias por venir.'"
                ),
                "now": "Sofía vai te testar. Quer ver se você fala — e se a cabeça funciona.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Hola, forastero. Soy Sofía. Mi abuela hablaba de palabras como las que dijiste.",
                    "translation": "Olá, forasteiro. Eu sou Sofía. Minha avó falava de palavras como as que você disse.",
                    "is_new_npc": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía se apresentou: 'Soy Sofía' — dela mesma. Apontando pra você ela pergunta '¿Y tú? ¿Quién eres?' Você responde com a mesma estrutura, dizendo o que VOCÊ é aqui:",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Tengo forastero"},
                        {"id": "c", "text": "Estoy forastero"},
                        {"id": "d", "text": "Me llamo forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_soy", "target": "soy", "native": "sou",
                    "npc_reaction": "Soy forastero. Eso eres — por ahora. Ya tienes la palabra para decirlo.",
                },
                {
                    "kind": "narrative",
                    "text": "Ela senta na cadeira de madeira em frente a você. Don Miguel fica de pé na porta. Miguel não se mexe do chão.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Antes que nada — ¿cómo te llamas tú?",
                    "translation": "Antes de tudo — como você se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía espera com os braços cruzados. Quer ouvir o nome dito por você.",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Hola Sofía"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto. Ahora dime — ¿cómo estás?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": (
                        "Suas mãos ainda tremem de leve. Seu peito apertado. Mas Sofía quer "
                        "uma resposta honesta, não educada. Você diz:"
                    ),
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bien"},
                        {"id": "c", "text": "Forastero"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Mal. Claro que mal. Cualquier persona estaría mal.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Don Miguel me contó lo del corredor. Antes de la palabra — ¿qué sentiste?",
                    "translation": "Don Miguel me contou do corredor. Antes da palavra — o que você sentiu?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "O peito apertado, o coração na garganta — Sofía espera a palavra exata.",
                    "options": [
                        {"id": "a", "text": "Miedo"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Luz"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Sí. Mi abuela decía que el miedo abre la puerta. La palabra cruza después.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "¿Y la palabra que cruzó la puerta? ¿Cuál fue?",
                    "translation": "E a palavra que cruzou a porta? Qual foi?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "A mesma palavra. Não há outra. Você diz, com cuidado:",
                    "options": [
                        {"id": "a", "text": "Fuego"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": "Fuego. Eso pensé. La más simple. La más vieja.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Sofía levanta. Anda até a lamparina na mesa. Olha pra chama, "
                        "depois pra você. Estende a mão pra você se aproximar."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Ven. Mira la lámpara — y dime qué hace.",
                    "translation": "Vem. Olha a lamparina — e me fala o que ela faz.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "A chama da lamparina ilumina o quarto inteiro. Ela te dá:",
                    "options": [
                        {"id": "a", "text": "Luz"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "Miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "Luz. La luz no quema. Pero viene del fuego. Recuerda eso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Y la primera vez que un fuego nace — eso es una 'chispa'. Pequeñita. Antes de hacerse grande.",
                    "translation": "chispa = centelha / faísca (o primeiro segundo do fogo)",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": (
                        "Sofía esfrega dois pedaços de madeira que tira do bolso. Sai uma faísca "
                        "pequena na mesa. Apaga rápido. Como se chama?"
                    ),
                    "options": [
                        {"id": "a", "text": "Chispa"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Luz"},
                        {"id": "d", "text": "Lámpara"},
                    ],
                    "correct": "a",
                    "word_id": "es_chispa", "target": "chispa", "native": "centelha",
                    "npc_reaction": "Chispa. El primer segundo del fuego. Tú diste chispa, forastero — la siguiente sería fuego.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "¿Tienes miedo ahora?",
                    "translation": "Você tem medo agora?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "A pergunta é direta. Sofía quer a verdade. Você sente medo — claro que sente. Como você fala?",
                    "options": [
                        {"id": "a", "text": "Tengo miedo"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Estoy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "tengo miedo", "native": "tenho medo",
                    "npc_reaction": "Bueno. El que no tiene miedo aquí es el peligro — no tú.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Miguel, do chão, te oferece a cantil dele. Sua garganta está seca de tanto falar. Você diz:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Hola"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, amigo. Sigue respirando. Todo está bien.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pra lamparina da mesa — chama tremeluzindo. 'Mira — el objeto que sostiene la luz. ¿Cómo se llama?'",
                    "options": [
                        {"id": "a", "text": "Lámpara"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Chispa"},
                        {"id": "d", "text": "Agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_lampara", "target": "lámpara", "native": "lamparina",
                    "npc_reaction": "Lámpara. Algo que guarda la luz. Como tu boca guardó la palabra hasta ahora.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Sofía ensina o presente afirmativo simples — pra que o protagonista
    # consiga falar 'eu vou', 'você vem', 'ela vai'. Útil pra próxima fase
    # quando o grupo se locomove. Beats narrativos intercalados.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Sofía", "Don Miguel", "Miguel"],
                "story": (
                    "Sofía te fez repetir 'fuego', 'miedo', 'luz', 'chispa' até que "
                    "as palavras saíssem sem peso na boca. Don Miguel ouviu encostado "
                    "na porta sem dizer nada.\n\n"
                    "Agora Sofía sente que você tá pronto pra mais uma coisa. "
                    "'Si vas a salir de este pueblo con nosotros, tienes que decir hacia dónde.'"
                ),
                "now": "Sofía vai te ensinar como falar de movimento — 'eu vou', 'você vem'.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Mira esto — es simple. Cuando yo me muevo, digo: 'yo voy'.",
                    "translation": "Olha isso — é simples. Quando eu me movo, digo: 'yo voy' (eu vou).",
                },
                {
                    "kind": "reveal",
                    "phrase": "Yo voy",
                    "meaning": "Eu vou",
                    "note": "do verbo 'ir' — usado pra qualquer movimento ('eu vou pra plaza', 'eu vou agora')",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Y cuando hablo contigo, te digo: 'tú vienes'. Tú — vienes.",
                    "translation": "tú vienes = você vem",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tú vienes",
                    "meaning": "Você vem",
                    "note": "do verbo 'venir' — chegar a algum lugar perto de quem fala",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo voy",       "isKey": True},
                        {"text": " / ",          "isKey": False},
                        {"text": "Tú vienes",    "isKey": True},
                        {"text": " / ",          "isKey": False},
                        {"text": "Ella va",      "isKey": True},
                    ],
                    "example": "— ¿Vienes conmigo? — Sí, yo voy. — Bueno. Sofía también va.",
                    "translation": "— Você vem comigo? — Sim, eu vou. — Beleza. Sofía também vai.",
                    "note": "yo voy (eu vou) | tú vienes (você vem) | ella va (ela vai)",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pra porta: 'Vamos a salir todos. ¿Tú vienes conmigo?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy"},
                        {"id": "b", "text": "No tengo hambre"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Adiós, Sofía"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Bien. Entonces tú vienes. Y nosotros vamos juntos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Y si pregunto por Miguel — ¿qué dices? Mira a él en el piso.",
                    "translation": "E se eu pergunto sobre o Miguel — o que você fala? Olha ele no chão.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Miguel se levanta, espreguiça. 'Yo voy con ustedes', ele diz. Como você descreve isso pra Sofía em uma palavra?",
                    "options": [
                        {"id": "a", "text": "Él va"},
                        {"id": "b", "text": "Tú vienes"},
                        {"id": "c", "text": "Yo voy"},
                        {"id": "d", "text": "Ella va"},
                    ],
                    "correct": "a",
                    "word_id": "es_el_va", "target": "él va", "native": "ele vai",
                    "npc_reaction": "Eso. Él va. Cualquier hombre — él va.",
                },
                {
                    "kind": "narrative",
                    "text": "Sofía aponta pra ela mesma com o polegar e levanta uma sobrancelha.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "'Y yo, ¿qué soy en este verbo?' — ela espera. Você diz, sobre ela:",
                    "options": [
                        {"id": "a", "text": "Ella va"},
                        {"id": "b", "text": "Él va"},
                        {"id": "c", "text": "Yo voy"},
                        {"id": "d", "text": "Tú vienes"},
                    ],
                    "correct": "a",
                    "word_id": "es_ella_va", "target": "ella va", "native": "ela vai",
                    "npc_reaction": "Ella va. Cualquier mujer — ella va. Yo voy, tú vienes, ella va. Simple.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía te dá um teste rápido: 'Si yo te llamo y tú llegas — ¿qué haces tú?'",
                    "options": [
                        {"id": "a", "text": "Yo voy"},
                        {"id": "b", "text": "Tú vienes"},
                        {"id": "c", "text": "Ella va"},
                        {"id": "d", "text": "Él va"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Eso. Tú diras 'yo voy' cuando alguien te llame.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Amanhecer. Os quatro saem do quarto pela primeira vez desde a noite.
    # Sofía conta o que ela ouvia da avó dela sobre 'palabras que despiertan'.
    # Convivência — vocab orgânico. Poucos exercícios, foco em desenvolver o
    # personagem da Sofía e plantar lore.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Sofía", "Don Miguel", "Miguel"],
                "story": (
                    "Você praticou 'yo voy', 'tú vienes', 'él va', 'ella va' até "
                    "as palavras saírem rápido. Sofía cruzou os braços satisfeita.\n\n"
                    "O céu já começava a clarear pela janela. Don Miguel olhou pra "
                    "fora e disse — 'Mejor salir antes de que se llene la calle.'"
                ),
                "now": "Os quatro saem juntos. Sofía conta o que sabe enquanto andam.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌄 A rua deserta, primeira luz. Cheiro de terra molhada, sinos da iglesia ao longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Mi abuela hablaba de esto cuando yo era pequeña. Decía que algunas palabras 'despiertan' — que no son sólo palabras.",
                    "translation": "Minha avó falava disso quando eu era pequena. Dizia que algumas palavras 'acordam' — que não são só palavras.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel anda do seu lado em silêncio. Don Miguel vai um pouco à frente, olhando as esquinas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Cuando yo era niña pensaba que era cuento. Hoy en la noche entendí que no.",
                    "translation": "Quando eu era criança achava que era história inventada. Hoje à noite entendi que não.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pro nascer do sol — luz nova entrando entre os telhados. 'Mira — la primera...' Que palavra ela usa?",
                    "options": [
                        {"id": "a", "text": "Luz"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Chispa"},
                        {"id": "d", "text": "Pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "La primera luz del día. La menos peligrosa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero — antes de salir, ¿quieres algo? Tengo agua en la cantimplora.",
                    "translation": "Forasteiro — antes de sair, quer alguma coisa? Tenho água na cantil.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Sua boca está seca depois da noite inteira falando. Você responde a Miguel:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Toma. Después del miedo de anoche, el cuerpo pide agua. Es normal.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Tengo algo para ti, forastero. Para que no olvides lo que pasó esta noche.",
                    "translation": "Tenho uma coisa pra você, forasteiro. Pra que não esqueça o que aconteceu essa noite.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Sofía tira do bolso uma lamparina de aceite pequena, de metal "
                        "envelhecido. A chama dentro tremeluz fraca."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Ela coloca o objeto na sua mão. Quente, leve. Como se chama isso?",
                    "options": [
                        {"id": "a", "text": "Lámpara"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Chispa"},
                        {"id": "d", "text": "Agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_lampara", "target": "lámpara", "native": "lamparina",
                    "npc_reaction": "Lámpara. Era de mi abuela. Ahora es tuya. Para recordar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pra você ao receber a lamparina e diz: 'No me la devuelves — es regalo.' Você responde com a palavra que sempre vale:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Hola"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Cuídala. Y cuídate tú.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Sofía... ¿tú vienes con nosotros entonces? ¿Vas a quedarte cerca?",
                    "translation": "Sofía... você vem com a gente então? Vai ficar perto?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía olha pro grupo. Pra você. Pra Miguel. Pra Don Miguel um passo à frente. Responde firme:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy con vosotros"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vale. Yo voy con vosotros. Hasta donde haga falta.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel para na esquina e se vira. Olha pros três jovens "
                        "atrás dele — Miguel, Sofía, e o forastero que faz a noite arder.\n\n"
                        "Não sorri. Mas acena com a cabeça. Aceitou."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate final — gated) ───────────────────────────────
    # Sofía decide ver se o protagonista pode chamar a palavra de novo —
    # dessa vez, em paz, sem perigo. Lamparina apagada. Acender com 'luz'.
    # Gate: errar trava. Closing beats fazem transição pra F7 (manhã na plaza).
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Sofía", "Don Miguel", "Miguel"],
                "story": (
                    "Vocês pararam num pátio interno escondido — paredes de adobe, "
                    "uma fonte velha quebrada, ninguém ali a essa hora. Sofía tirou "
                    "do bolso uma lamparina segunda — a chama dessa estava apagada.\n\n"
                    "'Quiero ver una cosa. Sin peligro esta vez. Sólo tú y la palabra.'"
                ),
                "now": "Teste final. Errar trava — você precisa acertar pra passar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "La lámpara está apagada. Sin chispa, sin fuego. ¿Puedes encenderla con la palabra?",
                    "translation": "A lamparina tá apagada. Sem faísca, sem fogo. Você consegue acender com a palavra?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Despacio, forastero. No tienes que hacerlo. Si no sale — no sale.",
                    "translation": "Devagar, forasteiro. Você não precisa fazer. Se não sair — não sai.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": (
                        "Sofía pousa a lamparina apagada na sua mão. Pavio limpo, "
                        "sem chama. Você fecha os olhos. Sente a palavra que quer "
                        "soltar. Qual é ela?"
                    ),
                    "options": [
                        {"id": "a", "text": "🔥 Luz"},
                        {"id": "b", "text": "💧 Agua"},
                        {"id": "c", "text": "🍞 Pan"},
                        {"id": "d", "text": "😨 Miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": (
                        "LUZ — la palabra salió más firme que la última vez.\n\n"
                        "La mecha de la lámpara prendió sola — pequeña, "
                        "estable. Sin explosión. Sin ruido.\n\n"
                        "Sofía respiró hondo. Don Miguel se quitó el sombrero un segundo. "
                        "Miguel te miró como si ahora fueras otra cosa."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "🕯️ A chama tremeluz na lamparina. Pequena, mas real.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Bueno. No estaba loca mi abuela.",
                    "translation": "Bom. Minha avó não era doida.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía olha pra você esperando. 'Forastero — ¿cómo estás ahora?' Honesto, sem maquiagem:",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Quien acaba de hacer un milagro tiene derecho a estar bien.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel se aproxima e estende a mão pra te ajudar a levantar. 'Vamos. El pueblo va a despertar.' Pra ele você responde:",
                    "options": [
                        {"id": "a", "text": "Yo voy"},
                        {"id": "b", "text": "Yo no"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Eso. Yo voy con vosotros — los cuatro juntos.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel te dá um soco leve no ombro, sorrindo pela primeira vez desde a noite. 'Tranquilo, forastero. Agora você não tá sozinho nisso.' Você responde:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, amigo. Para eso sirve un amigo.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F7 (plaza pela manhã) ─────
                {
                    "kind": "narrative",
                    "text": (
                        "Os quatro saem do pátio. Sofía vai à frente — passos rápidos. "
                        "Don Miguel acena pro vizinho que abre a janela do segundo andar. "
                        "Miguel anda do seu lado, em silêncio confortável."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Vamos a la plaza. Si vamos a vivir esto, hay que vivir como gente normal mientras se pueda.",
                    "translation": "Vamos pra plaza. Se a gente vai viver isso, tem que viver como gente normal enquanto dá.",
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
