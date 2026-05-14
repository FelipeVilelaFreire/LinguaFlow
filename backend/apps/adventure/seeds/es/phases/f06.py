"""
Seed das 6 seÃ§Ãµes da Fase 6 Espanhol A1 â€” "Lo que vio SofÃ­a".

ContinuaÃ§Ã£o direta da F5. Dentro do quarto de Don Miguel na posada, depois
de o protagonista ter feito o fogo aparecer no corredor. Don Miguel tranca
a porta, tenta explicar em espanhol simples, percebe que nÃ£o tem palavras
pra isso â€” e decide buscar alguÃ©m que tenha. Sai. Volta com SofÃ­a. SofÃ­a
nÃ£o recua: pede pra ele dizer a palavra de novo. Uma lamparina apagada se
acende. SofÃ­a decide entrar no grupo.

âš ï¸ MILESTONE OBRIGATÃ“RIO (canÃ´nico â€” characters.md, story.md):
    SofÃ­a entra no grupo na F6. "A Local" â€” viu o dom funcionar. CrÃª.

Novos vocab (2): luz Â· chispa  (+ lÃ¡mpara como objeto cotidiano)
RevisÃ£o F1-F5: hola, gracias, bien/mal, me llamo, tengo sed/hambre,
               forastero, fuego, miedo, correr
GramÃ¡tica nova: presente afirmativo simples (yo voy, tÃº vienes, ella va)
NPCs principais: Don Miguel (sai cedo) Â· Miguel (chega) Â· SofÃ­a (entra no grupo)
Arco emocional: choque pelo prÃ³prio corpo â†’ reconhecimento ("nÃ£o estou sozinho")
TransiÃ§Ã£o:      saem da casa de Don Miguel ao amanhecer; F7 abre na plaza.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f6_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Dentro do quarto de Don Miguel. Ele acabou de trancar a porta apÃ³s o
    # incidente da F5. Tenta explicar â€” nÃ£o tem palavras. Decide buscar
    # alguÃ©m que tenha. Sai. O protagonista fica sozinho com Miguel-filho,
    # que chegou correndo ao ouvir o pai chamar.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸ•¯ï¸ Quarto de Don Miguel Â· Noite Â· A porta trancada\n\n"
                        "A lamparina na mesa tremeluz. Don Miguel estÃ¡ de costas pra "
                        "vocÃª, parado, pensando. As mÃ£os dele apertam as costas de "
                        "uma cadeira de madeira."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Lo que pasÃ³ allÃ¡ afuera... yo no sÃ© explicarlo, forastero. No tengo palabras.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª ainda olha pras prÃ³prias mÃ£os. Pele intacta. Como se o fogo nÃ£o fosse seu pra queimar.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Pero hay alguien. Una joven del pueblo. Su abuela hablaba de estas cosas â€” palabras viejas, palabras que pesan.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel se vira e te olha. Pela primeira vez nÃ£o hÃ¡ paciÃªncia no rosto dele â€” hÃ¡ cÃ¡lculo.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Voy a buscarla. TÃº quedate aquÃ­. Mi mijo va a venir contigo.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Ele abre a porta um vÃ£o estreito. Grita pra rua escura:",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¡MIGUEL! Â¡VEN AQUÃ! Â¡RÃPIDO!",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Passos correndo na rua. A voz de Miguel respondendo de longe, sem fÃ´lego.",
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Â¡PapÃ¡! Â¡Â¿QuÃ© pasÃ³?! Â¿EstÃ¡s bien?",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel entra correndo, ofegante. VÃª vocÃª sentado tremendo. VÃª o pai mais sÃ©rio que nunca.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Cuida del forastero. No salgas. Yo vuelvo pronto.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel sai. A porta fecha. Miguel olha pra vocÃª sem entender nada â€” mas sem fazer pergunta tambÃ©m.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": (
                        "Miguel senta no chÃ£o de costas pra parede, do seu lado. "
                        "Olha pra suas mÃ£os tremendo. VocÃª sente que ele quer perguntar mas "
                        "nÃ£o vai. VocÃª decide falar primeiro. Como vocÃª cumprimenta â€” "
                        "mesmo que pareÃ§a absurdo agora?"
                    ),
                    "options": [
                        {"id": "a", "text": "Hola..."},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olÃ¡",
                    "npc_reaction": "Hola, amigo. TÃ¡ bem agora? Respira.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel te olha de lado, esperando. 'Forastero â€” Â¿cÃ³mo estÃ¡s?' VocÃª responde honestamente â€” vocÃª nÃ£o tÃ¡ bem:",
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bien"},
                        {"id": "c", "text": "Buenos dÃ­as"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Mal. Entendo. Eu tambÃ©m tÃ´ estranho com isso.",
                },
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "luz",     "native": "luz"},
                        {"target": "chispa",  "native": "centelha / faÃ­sca"},
                        {"target": "lÃ¡mpara", "native": "lamparina / lampiÃ£o"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": (
                        "Miguel olha pra lamparina na mesa. A chama tremeluz. Ele aponta "
                        "e diz sÃ³ uma palavra, devagar â€” 'luz'. O que Ã© 'luz'?"
                    ),
                    "options": [
                        {"id": "a", "text": "Luz"},
                        {"id": "b", "text": "Ãgua"},
                        {"id": "c", "text": "Fogo"},
                        {"id": "d", "text": "PÃ£o"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "Luz. Da lamparina, do sol, do que ilumina. Aprende rÃ¡pido.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Miguel sentado no chÃ£o com o protagonista, esperando Don Miguel voltar.
    # Conversa baixa, revisÃ£o de F1-F5 em forma de situaÃ§Ãµes vividas.
    # Cada exercÃ­cio Ã© uma pergunta dele â€” Miguel falando portuguÃªs quebrado
    # como ponte natural.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Miguel"],
                "story": (
                    "Don Miguel saiu correndo pelas ruas escuras dizendo que ia "
                    "buscar alguÃ©m que sabia 'ler estas cosas'. Miguel chegou "
                    "ofegante. Sentou no chÃ£o do seu lado. NÃ£o fez pergunta.\n\n"
                    "A lamparina tremeluz. VocÃª ainda sente o calor da palavra "
                    "que saiu da boca â€” 'fuego' â€” mesmo agora, horas depois."
                ),
                "now": "Miguel quer fazer vocÃª falar enquanto esperam. Tirar a cabeÃ§a do que aconteceu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Vamo falar normal um pouco. SenÃ£o vocÃª fica doido aÃ­ pensando.",
                    "translation": "Vamos falar normal um pouco. SenÃ£o vocÃª fica doido aÃ­ pensando.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Olha â€” Rosa te deu pan hoy de maÃ±ana. Â¿Verdad?",
                    "translation": "Olha â€” Rosa te deu pÃ£o de manhÃ£. NÃ©?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel quer ver se sua cabeÃ§a ainda tÃ¡ funcionando. 'O que Rosa te deu de manhÃ£, antes de tudo isso?'",
                    "options": [
                        {"id": "a", "text": "Pan"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Fuego"},
                        {"id": "d", "text": "Luz"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pÃ£o",
                    "npc_reaction": "Pan. Ainda no estÃ´mago. Sua cabeÃ§a tÃ¡ funcionando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Bom. Â¿Y antes de comer, quÃ© dijo Rosa cuando viste el pan caliente?",
                    "translation": "Bom. E antes de comer, o que Rosa falou ao ver vocÃª com cara de fome?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Sua barriga roncou. Rosa apontou e riu. Ela disse:",
                    "options": [
                        {"id": "a", "text": "Â¡Tienes hambre!"},
                        {"id": "b", "text": "Â¡Tienes miedo!"},
                        {"id": "c", "text": "Â¡Tienes luz!"},
                        {"id": "d", "text": "Â¡Tienes fuego!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. Coisa simples. Hoje Ã  noite virou complicado, nÃ©?",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel se mexe no chÃ£o. Cruza as pernas, apoia os cotovelos nos joelhos. Continua.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y la sed â€” Â¿cuÃ¡l fue la palabra para sed?",
                    "translation": "E a sede â€” qual foi a palavra pra sede?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "VocÃª lembrou da fonte da plaza. Da Ã¡gua fria da tigela na cozinha da Rosa. A palavra:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Tengo luz"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. Agua. Isso continua simples â€” Ã© bom continuar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y hace unas horas, en el corredor... Â¿quÃ© sentiste antes de la palabra?",
                    "translation": "E hÃ¡ umas horas, no corredor... o que vocÃª sentiu antes da palavra?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Antes do fogo, antes da palavra, o que pulsou no seu peito. A palavra Ã©:",
                    "options": [
                        {"id": "a", "text": "Miedo"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Hola"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. SÃ­. Lo entiendo, forastero.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y la palabra que saiu da sua boca â€” Â¿la recuerdas?",
                    "translation": "E a palavra que saiu da sua boca â€” vocÃª lembra?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "A palavra ainda queima no fundo da garganta. VocÃª diz baixinho:",
                    "options": [
                        {"id": "a", "text": "Fuego"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": "Fuego. Sim. E saiu de vocÃª, forastero. Saiu mesmo.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel olha pra lamparina por um segundo. Depois pra vocÃª. NÃ£o desvia.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Una Ãºltima pregunta antes que llegue papÃ¡ â€” Â¿cÃ³mo te llamas tÃº?",
                    "translation": "Uma Ãºltima pergunta antes do papai chegar â€” como vocÃª se chama?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel te olha de frente. Quer ouvir seu nome de novo â€” pra reafirmar que vocÃª ainda Ã© vocÃª.",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Hola Miguel"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Eso. NÃ£o esquece. VocÃª Ã© vocÃª, antes de qualquer outra coisa.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel volta â€” com SofÃ­a. SofÃ­a nÃ£o recua ao ouvir a histÃ³ria.
    # Faz perguntas diretas. Pratica intensa: revisÃ£o pesada do que jÃ¡ aprendeu
    # + apresentaÃ§Ã£o de luz/chispa. Cada exercÃ­cio Ã© uma pergunta dela.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Miguel"],
                "story": (
                    "Passos no corredor. A porta abriu. Don Miguel entra â€” atrÃ¡s "
                    "dele, uma garota da sua idade. Cabelos presos, olhos rÃ¡pidos. "
                    "Ela entra na sala olhando vocÃª como se jÃ¡ tivesse decidido alguma "
                    "coisa.\n\n"
                    "'Este es el forastero. SofÃ­a â€” gracias por venir.'"
                ),
                "now": "SofÃ­a vai te testar. Quer ver se vocÃª fala â€” e se a cabeÃ§a funciona.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Hola, forastero. Soy SofÃ­a. Mi abuela hablaba de palabras como las que dijiste.",
                    "translation": "OlÃ¡, forasteiro. Eu sou SofÃ­a. Minha avÃ³ falava de palavras como as que vocÃª disse.",
                    "is_new_npc": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a se apresentou: 'Soy SofÃ­a' â€” dela mesma. Apontando pra vocÃª ela pergunta 'Â¿Y tÃº? Â¿QuiÃ©n eres?' VocÃª responde com a mesma estrutura, dizendo o que VOCÃŠ Ã© aqui:",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Tengo forastero"},
                        {"id": "c", "text": "Estoy forastero"},
                        {"id": "d", "text": "Me llamo forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_soy", "target": "soy", "native": "sou",
                    "npc_reaction": "Soy forastero. Eso eres â€” por ahora. Ya tienes la palabra para decirlo.",
                },
                {
                    "kind": "narrative",
                    "text": "Ela senta na cadeira de madeira em frente a vocÃª. Don Miguel fica de pÃ© na porta. Miguel nÃ£o se mexe do chÃ£o.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Antes que nada â€” Â¿cÃ³mo te llamas tÃº?",
                    "translation": "Antes de tudo â€” como vocÃª se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a espera com os braÃ§os cruzados. Quer ouvir o nome dito por vocÃª.",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Hola SofÃ­a"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Mucho gusto. Ahora dime â€” Â¿cÃ³mo estÃ¡s?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": (
                        "Suas mÃ£os ainda tremem de leve. Seu peito apertado. Mas SofÃ­a quer "
                        "uma resposta honesta, nÃ£o educada. VocÃª diz:"
                    ),
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bien"},
                        {"id": "c", "text": "Forastero"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Mal. Claro que mal. Cualquier persona estarÃ­a mal.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Don Miguel me contÃ³ lo del corredor. Antes de la palabra â€” Â¿quÃ© sentiste?",
                    "translation": "Don Miguel me contou do corredor. Antes da palavra â€” o que vocÃª sentiu?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "O peito apertado, o coraÃ§Ã£o na garganta â€” SofÃ­a espera a palavra exata.",
                    "options": [
                        {"id": "a", "text": "Miedo"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Luz"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. SÃ­. Mi abuela decÃ­a que el miedo abre la puerta. La palabra cruza despuÃ©s.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Â¿Y la palabra que cruzÃ³ la puerta? Â¿CuÃ¡l fue?",
                    "translation": "E a palavra que cruzou a porta? Qual foi?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "A mesma palavra. NÃ£o hÃ¡ outra. VocÃª diz, com cuidado:",
                    "options": [
                        {"id": "a", "text": "Fuego"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": "Fuego. Eso pensÃ©. La mÃ¡s simple. La mÃ¡s vieja.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "SofÃ­a levanta. Anda atÃ© a lamparina na mesa. Olha pra chama, "
                        "depois pra vocÃª. Estende a mÃ£o pra vocÃª se aproximar."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Ven. Mira la lÃ¡mpara â€” y dime quÃ© hace.",
                    "translation": "Vem. Olha a lamparina â€” e me fala o que ela faz.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "A chama da lamparina ilumina o quarto inteiro. Ela te dÃ¡:",
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
                    "npc": "SofÃ­a",
                    "line": "Y la primera vez que un fuego nace â€” eso es una 'chispa'. PequeÃ±ita. Antes de hacerse grande.",
                    "translation": "chispa = centelha / faÃ­sca (o primeiro segundo do fogo)",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": (
                        "SofÃ­a esfrega dois pedaÃ§os de madeira que tira do bolso. Sai uma faÃ­sca "
                        "pequena na mesa. Apaga rÃ¡pido. Como se chama?"
                    ),
                    "options": [
                        {"id": "a", "text": "Chispa"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Luz"},
                        {"id": "d", "text": "LÃ¡mpara"},
                    ],
                    "correct": "a",
                    "word_id": "es_chispa", "target": "chispa", "native": "centelha",
                    "npc_reaction": "Chispa. El primer segundo del fuego. TÃº diste chispa, forastero â€” la siguiente serÃ­a fuego.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Â¿Tienes miedo ahora?",
                    "translation": "VocÃª tem medo agora?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "A pergunta Ã© direta. SofÃ­a quer a verdade. VocÃª sente medo â€” claro que sente. Como vocÃª fala?",
                    "options": [
                        {"id": "a", "text": "Tengo miedo"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Estoy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "tengo miedo", "native": "tenho medo",
                    "npc_reaction": "Bueno. El que no tiene miedo aquÃ­ es el peligro â€” no tÃº.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Miguel, do chÃ£o, te oferece a cantil dele. Sua garganta estÃ¡ seca de tanto falar. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Hola"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, amigo. Sigue respirando. TÃ¡ tudo bem.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pra lamparina da mesa â€” chama tremeluzindo. 'Mira â€” el objeto que sostiene la luz. Â¿CÃ³mo se llama?'",
                    "options": [
                        {"id": "a", "text": "LÃ¡mpara"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Chispa"},
                        {"id": "d", "text": "Agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_lampara", "target": "lÃ¡mpara", "native": "lamparina",
                    "npc_reaction": "LÃ¡mpara. Algo que guarda la luz. Como tu boca guardÃ³ la palabra hasta ahora.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # SofÃ­a ensina o presente afirmativo simples â€” pra que o protagonista
    # consiga falar 'eu vou', 'vocÃª vem', 'ela vai'. Ãštil pra prÃ³xima fase
    # quando o grupo se locomove. Beats narrativos intercalados.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Don Miguel", "Miguel"],
                "story": (
                    "SofÃ­a te fez repetir 'fuego', 'miedo', 'luz', 'chispa' atÃ© que "
                    "as palavras saÃ­ssem sem peso na boca. Don Miguel ouviu encostado "
                    "na porta sem dizer nada.\n\n"
                    "Agora SofÃ­a sente que vocÃª tÃ¡ pronto pra mais uma coisa. "
                    "'Si vas a salir de este pueblo con nosotros, tienes que decir hacia dÃ³nde.'"
                ),
                "now": "SofÃ­a vai te ensinar como falar de movimento â€” 'eu vou', 'vocÃª vem'.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Mira esto â€” es simple. Cuando yo me muevo, digo: 'yo voy'.",
                    "translation": "Olha isso â€” Ã© simples. Quando eu me movo, digo: 'yo voy' (eu vou).",
                },
                {
                    "kind": "reveal",
                    "phrase": "Yo voy",
                    "meaning": "Eu vou",
                    "note": "do verbo 'ir' â€” usado pra qualquer movimento ('eu vou pra plaza', 'eu vou agora')",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Y cuando hablo contigo, te digo: 'tÃº vienes'. TÃº â€” vienes.",
                    "translation": "tÃº vienes = vocÃª vem",
                },
                {
                    "kind": "reveal",
                    "phrase": "TÃº vienes",
                    "meaning": "VocÃª vem",
                    "note": "do verbo 'venir' â€” chegar a algum lugar perto de quem fala",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo voy",       "isKey": True},
                        {"text": " / ",          "isKey": False},
                        {"text": "TÃº vienes",    "isKey": True},
                        {"text": " / ",          "isKey": False},
                        {"text": "Ella va",      "isKey": True},
                    ],
                    "example": "â€” Â¿Vienes conmigo? â€” SÃ­, yo voy. â€” Bueno. SofÃ­a tambiÃ©n va.",
                    "translation": "â€” VocÃª vem comigo? â€” Sim, eu vou. â€” Beleza. SofÃ­a tambÃ©m vai.",
                    "note": "yo voy (eu vou) | tÃº vienes (vocÃª vem) | ella va (ela vai)",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pra porta: 'Vamos a salir todos. Â¿TÃº vienes conmigo?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy"},
                        {"id": "b", "text": "No tengo hambre"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "AdiÃ³s, SofÃ­a"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Bien. Entonces tÃº vienes. Y nosotros vamos juntos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Y si pregunto por Miguel â€” Â¿quÃ© dices? Mira a Ã©l en el piso.",
                    "translation": "E se eu pergunto sobre o Miguel â€” o que vocÃª fala? Olha ele no chÃ£o.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Miguel se levanta, espreguiÃ§a. 'Yo voy con ustedes', ele diz. Como vocÃª descreve isso pra SofÃ­a em uma palavra?",
                    "options": [
                        {"id": "a", "text": "Ã‰l va"},
                        {"id": "b", "text": "TÃº vienes"},
                        {"id": "c", "text": "Yo voy"},
                        {"id": "d", "text": "Ella va"},
                    ],
                    "correct": "a",
                    "word_id": "es_el_va", "target": "Ã©l va", "native": "ele vai",
                    "npc_reaction": "Eso. Ã‰l va. Cualquier hombre â€” Ã©l va.",
                },
                {
                    "kind": "narrative",
                    "text": "SofÃ­a aponta pra ela mesma com o polegar e levanta uma sobrancelha.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "'Y yo, Â¿quÃ© soy en este verbo?' â€” ela espera. VocÃª diz, sobre ela:",
                    "options": [
                        {"id": "a", "text": "Ella va"},
                        {"id": "b", "text": "Ã‰l va"},
                        {"id": "c", "text": "Yo voy"},
                        {"id": "d", "text": "TÃº vienes"},
                    ],
                    "correct": "a",
                    "word_id": "es_ella_va", "target": "ella va", "native": "ela vai",
                    "npc_reaction": "Ella va. Cualquier mujer â€” ella va. Yo voy, tÃº vienes, ella va. Simple.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a te dÃ¡ um teste rÃ¡pido: 'Si yo te llamo y tÃº llegas â€” Â¿quÃ© haces tÃº?'",
                    "options": [
                        {"id": "a", "text": "Yo voy"},
                        {"id": "b", "text": "TÃº vienes"},
                        {"id": "c", "text": "Ella va"},
                        {"id": "d", "text": "Ã‰l va"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Eso. TÃº diras 'yo voy' cuando alguien te llame.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Amanhecer. Os quatro saem do quarto pela primeira vez desde a noite.
    # SofÃ­a conta o que ela ouvia da avÃ³ dela sobre 'palabras que despiertan'.
    # ConvivÃªncia â€” vocab orgÃ¢nico. Poucos exercÃ­cios, foco em desenvolver o
    # personagem da SofÃ­a e plantar lore.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Don Miguel", "Miguel"],
                "story": (
                    "VocÃª praticou 'yo voy', 'tÃº vienes', 'Ã©l va', 'ella va' atÃ© "
                    "as palavras saÃ­rem rÃ¡pido. SofÃ­a cruzou os braÃ§os satisfeita.\n\n"
                    "O cÃ©u jÃ¡ comeÃ§ava a clarear pela janela. Don Miguel olhou pra "
                    "fora e disse â€” 'Mejor salir antes de que se llene la calle.'"
                ),
                "now": "Os quatro saem juntos. SofÃ­a conta o que sabe enquanto andam.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ„ A rua deserta, primeira luz. Cheiro de terra molhada, sinos da iglesia ao longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Mi abuela hablaba de esto cuando yo era pequeÃ±a. DecÃ­a que algunas palabras 'despiertan' â€” que no son sÃ³lo palabras.",
                    "translation": "Minha avÃ³ falava disso quando eu era pequena. Dizia que algumas palavras 'acordam' â€” que nÃ£o sÃ£o sÃ³ palavras.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel anda do seu lado em silÃªncio. Don Miguel vai um pouco Ã  frente, olhando as esquinas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Cuando yo era niÃ±a pensaba que era cuento. Hoy en la noche entendÃ­ que no.",
                    "translation": "Quando eu era crianÃ§a achava que era histÃ³ria inventada. Hoje Ã  noite entendi que nÃ£o.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pro nascer do sol â€” luz nova entrando entre os telhados. 'Mira â€” la primera...' Que palavra ela usa?",
                    "options": [
                        {"id": "a", "text": "Luz"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Chispa"},
                        {"id": "d", "text": "Pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "La primera luz del dÃ­a. La menos peligrosa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero â€” antes de salir, Â¿quieres algo? Tengo agua en la cantimplora.",
                    "translation": "Forasteiro â€” antes de sair, quer alguma coisa? Tenho Ã¡gua na cantil.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Sua boca estÃ¡ seca depois da noite inteira falando. VocÃª responde a Miguel:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Toma. DespuÃ©s del miedo de anoche, el cuerpo pide agua. Es normal.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Tengo algo para ti, forastero. Para que no olvides lo que pasÃ³ esta noche.",
                    "translation": "Tenho uma coisa pra vocÃª, forasteiro. Pra que nÃ£o esqueÃ§a o que aconteceu essa noite.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "SofÃ­a tira do bolso uma lamparina de aceite pequena, de metal "
                        "envelhecido. A chama dentro tremeluz fraca."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Ela coloca o objeto na sua mÃ£o. Quente, leve. Como se chama isso?",
                    "options": [
                        {"id": "a", "text": "LÃ¡mpara"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Chispa"},
                        {"id": "d", "text": "Agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_lampara", "target": "lÃ¡mpara", "native": "lamparina",
                    "npc_reaction": "LÃ¡mpara. Era de mi abuela. Ahora es tuya. Para recordar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pra vocÃª ao receber a lamparina e diz: 'No me la devuelves â€” es regalo.' VocÃª responde com a palavra que sempre vale:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Hola"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. CuÃ­dala. Y cuÃ­date tÃº.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "SofÃ­a... Â¿tÃº vienes con nosotros entonces? Â¿Vas a quedarte cerca?",
                    "translation": "SofÃ­a... vocÃª vem com a gente entÃ£o? Vai ficar perto?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a olha pro grupo. Pra vocÃª. Pra Miguel. Pra Don Miguel um passo Ã  frente. Responde firme:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy con vosotros"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vale. Yo voy con vosotros. Hasta donde haga falta.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel para na esquina e se vira. Olha pros trÃªs jovens "
                        "atrÃ¡s dele â€” Miguel, SofÃ­a, e o forastero que faz a noite arder.\n\n"
                        "NÃ£o sorri. Mas acena com a cabeÃ§a. Aceitou."
                    ),
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate final â€” gated) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # SofÃ­a decide ver se o protagonista pode chamar a palavra de novo â€”
    # dessa vez, em paz, sem perigo. Lamparina apagada. Acender com 'luz'.
    # Gate: errar trava. Closing beats fazem transiÃ§Ã£o pra F7 (manhÃ£ na plaza).
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Don Miguel", "Miguel"],
                "story": (
                    "VocÃªs pararam num pÃ¡tio interno escondido â€” paredes de adobe, "
                    "uma fonte velha quebrada, ninguÃ©m ali a essa hora. SofÃ­a tirou "
                    "do bolso uma lamparina segunda â€” a chama dessa estava apagada.\n\n"
                    "'Quiero ver una cosa. Sin peligro esta vez. SÃ³lo tÃº y la palabra.'"
                ),
                "now": "Teste final. Errar trava â€” vocÃª precisa acertar pra passar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "La lÃ¡mpara estÃ¡ apagada. Sin chispa, sin fuego. Â¿Puedes encenderla con la palabra?",
                    "translation": "A lamparina tÃ¡ apagada. Sem faÃ­sca, sem fogo. VocÃª consegue acender com a palavra?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Despacio, forastero. No tienes que hacerlo. Si no sale â€” no sale.",
                    "translation": "Devagar, forasteiro. VocÃª nÃ£o precisa fazer. Se nÃ£o sair â€” nÃ£o sai.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": (
                        "SofÃ­a pousa a lamparina apagada na sua mÃ£o. Pavio limpo, "
                        "sem chama. VocÃª fecha os olhos. Sente a palavra que quer "
                        "soltar. Qual Ã© ela?"
                    ),
                    "options": [
                        {"id": "a", "text": "ðŸ”¥ Luz"},
                        {"id": "b", "text": "ðŸ’§ Agua"},
                        {"id": "c", "text": "ðŸž Pan"},
                        {"id": "d", "text": "ðŸ˜¨ Miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": (
                        "LUZ â€” a palavra saiu mais firme que da Ãºltima vez.\n\n"
                        "O pavio da lamparina pegou fogo sozinho â€” pequeno, "
                        "estÃ¡vel. Sem explosÃ£o. Sem barulho.\n\n"
                        "SofÃ­a respirou fundo. Don Miguel tirou o chapÃ©u por um segundo. "
                        "Miguel olhou pra vocÃª como se vocÃª fosse outra coisa agora."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸ•¯ï¸ A chama tremeluz na lamparina. Pequena, mas real.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Bueno. No estaba loca mi abuela.",
                    "translation": "Bom. Minha avÃ³ nÃ£o era doida.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a olha pra vocÃª esperando. 'Forastero â€” Â¿cÃ³mo estÃ¡s ahora?' Honesto, sem maquiagem:",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Quem acabou de fazer um milagre tem o direito de estar bem.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel se aproxima e estende a mÃ£o pra te ajudar a levantar. 'Vamos. El pueblo va a despertar.' Pra ele vocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Yo voy"},
                        {"id": "b", "text": "Yo no"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Eso. Yo voy con vosotros â€” los cuatro juntos.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel te dÃ¡ um soco leve no ombro, sorrindo pela primeira vez desde a noite. 'Tranquilo, forastero. Agora vocÃª nÃ£o tÃ¡ sozinho nisso.' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, amigo. Pra isso que serve amigo.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F7 (plaza pela manhÃ£) â”€â”€â”€â”€â”€
                {
                    "kind": "narrative",
                    "text": (
                        "Os quatro saem do pÃ¡tio. SofÃ­a vai Ã  frente â€” passos rÃ¡pidos. "
                        "Don Miguel acena pro vizinho que abre a janela do segundo andar. "
                        "Miguel anda do seu lado, em silÃªncio confortÃ¡vel."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Vamos a la plaza. Si vamos a vivir esto, hay que vivir como gente normal mientras se pueda.",
                    "translation": "Vamos pra plaza. Se a gente vai viver isso, tem que viver como gente normal enquanto dÃ¡.",
                    "pace": "slow",
                },
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ… A primeira fumaÃ§a das padarias comeÃ§a a subir pelos telhados. "
                        "San CristÃ³bal vai acordando. VocÃªs quatro caminham pela rua "
                        "principal â€” um grupo agora, mesmo que ninguÃ©m saiba ainda."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
