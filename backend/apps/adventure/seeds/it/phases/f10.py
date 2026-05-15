"""
Seed das 6 seções da Fase 10 Italiano A1 — "La sombra del Guardia".

Fechamento do mini-arco F6-F10. Não há milestone interno do grupo —
piu planta o gancho temático da T1 inteira: a hostilidade institucional
do borgo. La Guardia reaparece come ameaça funcional — pista para o
boss da T1 (Il Podesta / El Jefe del Borgo).

Sequência: amanhecer cedo. Grupo decidiu na noite anterior ir falar com
o Podesta. No caminho, La Guardia bloqueia uma rua estreita. Pede o
"pase de forestiero". O protagonista não tem. La Guardia diz que sem
pase, sai do borgo até o pôr do sol. Nico grita. Chiara aparece de
outra esquina com Lucia. Lucia se aproxima de La Guardia e fala três
frases baixinho — o jogador não escuta. La Guardia recua, lança um
olhar duro pro protagonista, vai embora. Nico olha pra Lucia. Lucia
sorri: "Conocidos antiguos. No te preocupes." — primeira pista DIRETA
pro jogador (não pros personagens) de que Lucia tem ligações que
ninguém imagina.

À noite, Antonio il Contadino diz que o pase só é dado pelo Podesta — e que isso
vai ser um problema.

Novos vocab (2-3): pase · alcalde · vieni/para/guarda (imperativo simples)
Gramática nova: 1. Imperativo simples (vieni, para, guarda, habla) — ecoa o
                   que La Guardia usa pra dar ordines
                2. Expanesão do paradigma IR — F6 ensenzaou io vado / tu vieni /
                   él · lei va. F10 fecha com NOSOTROS VAMOS e ELLOS VAN
                   (grupo se locomeve pro municipio)
Revisão F1-F9:  saudações, ¿cómo estás?, mi chiamo, ho X años,
                no mi piace, hay, io vado, lugares (strada, piazza, fuente)
NPC principais: Os 4 do grupo · Antonio il Contadino · La Guardia (antagonista)
Arco emocional: falsa segurança (F9) → ameaça institucional explícita
                → identificação do antagonista da temporada
Transição:      F11 abre na manhã seguinte com o grupo decidindo
                ir pedir o pase ao Podesta. Começa a estrada
                que termina no boss da T1.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Amanhecer. O grupo se prepara em silêncio. Antonio il Contadino passa as
    # instruções. Os quatro saem. Pelo caminho, encontram a primeira
    # tensão da manhã. Imersão — falas sem tradução.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌄 Amanhecer cedo · Casa de Antonio il Contadino · Mesa baixa de madeira\n\n"
                        "O céu ainda escuro pelas frestas. Lamparina baixa. Os quatro "
                        "sentados em volta da mesa, junto com Antonio il Contadino. Pão da "
                        "noite anterior, café morno. Ninguém com fome de verdade."
                    ),
                },
                {
                    "kind": "skill_check",
                    "skill": "persuasao",
                    "min_level": 2,
                    "uses_item_tag": "moneda",
                    "success": "Voce escolhe a palavra e o gesto certos; a resistencia baixa um pouco.",
                    "fallback": "A conversa nao abre de imediato, mas Nico segura o clima e a historia continua.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Hoy van al municipio. Il Podesta da el pase a los forestieros — senza pase, hay problema.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "La Guardia ya escaló esto. Si te encuentran senza pase, te sacan del borgo. Por questo andiamo temprano.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você ouve as palavras 'pase' e 'Podesta' pela primeira vez. Não sabe exatamente o que são — piu pelo tom, são portas.",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "¿Y si el Podesta se niega?¿Qué hacemos?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Esatto lo vemos cuando arrivimos. Una cosa a la vez.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia come metade do pão em silêncio. Não está preocupada — está pensando.",
                },
                {
                    "kind": "npc",
                    "npc": "Nico",
                    "line": "Andiamo juntos. Si paran al forestiero — paran a los cuatro.",
                },
                {
                    "kind": "scene",
                    "text": "🌫️ Rua deserta · Primeira luce azulada · Vocês saem pela porta",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês quatro andam pela rua principal, sem pressa piu "
                        "sem parar. Lucia lidera — passos certos come se já "
                        "soubesse o caminho. Chiara do seu lado. Nico atrás "
                        "vigiando atrás."
                    ),
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "pase",     "native": "passe / permissão"},
                        {"target": "alcalde",  "native": "alcaide / prefeito (a maior autoridade do borgo)"},
                        {"target": "municipio", "native": "câmara / prefeitura"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino acabou de explicar que o forestiero precisa de um documento pra ficar no borgo. Como esse documento se chama?",
                    "options": [
                        {"id": "a", "text": "Pase"},
                        {"id": "b", "text": "Lampada"},
                        {"id": "c", "text": "Naranja"},
                        {"id": "d", "text": "Mañana"},
                    ],
                    "correct": "a",
                    "word_id": "it_pase", "target": "pase", "native": "passe",
                    "npc_reaction": "Pase. Un papel con sello. Senza él no eres legal aquí.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Quem dá o pase no borgo?A maior autoridade política — se chama:",
                    "options": [
                        {"id": "a", "text": "Podesta"},
                        {"id": "b", "text": "Campesenzao"},
                        {"id": "c", "text": "Mercante"},
                        {"id": "d", "text": "Forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_alcalde", "target": "alcalde", "native": "alcaide / prefeito",
                    "npc_reaction": "Podesta. Hombre político. Andiamo a tener que tratarlo con respeto — y con cuidado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico olha pra você caminhando. 'Forestiero — ¿estás listo para esto?' Você responde com honestidade:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado"},
                        {"id": "b", "text": "No, ho paura"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Vale. Si caminas con paura, lo escondes. Si caminas con calma, ganas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pra esquina que dobra na rua estreita. 'Por aquí es más rápido. ¿Tu vieni?' Você confirma:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado"},
                        {"id": "b", "text": "No ho fame"},
                        {"id": "c", "text": "Adiós Chiara"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Andiamo. La strada estrecha pasa cerca del municipio.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ─────────────────────────────────────────────────
    # Caminho até o municipio. Revisão pesada — saudações, estado físico,
    # vizinhos que cumprimentam, Lucia testando enquanto caminha. F1-F9.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Vocês cortaram caminho pela rua estreita. Pedras desniveladas, "
                    "vasos de barro nas janelas. Algupiu pessoas já abrindo "
                    "lojas — saudações trocadas pelos cantos.\n\n"
                    "Lucia se vira pra você enquanto andam. 'Mientras llegamos — "
                    "repaso. Si te paran, no quiero que tartamudees.'"
                ),
                "now": "Lucia testa rapidamente F1-F9 — saudações, identidade, idade.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Primero — si te paran y te preguntan tu nombre. ¿Qué dices?",
                    "translation": "Primeiro — se te param e te perguntam seu nome. O que você fala?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Pergunta direta: 'Mi chiamo + nome'. Você responde com seu nome:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Ho veinte años"},
                        {"id": "d", "text": "Benes días"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Bene. Senza titubear. Tu nombre es tuyo — di que es tuyo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Si te preguntan tu edad — ¿qué dices?",
                    "translation": "Se te perguntam sua idade — o que você fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "A idade é fácil — você tem vinte. Resposta correta é:",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Sono veinte"},
                        {"id": "c", "text": "Mi chiamo veinte"},
                        {"id": "d", "text": "Sto veinte"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Veinte. Hombre giovane, no niño. Esatto le importa al Podesta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Prima de seguir — ¿cómo está la testa hoy?",
                    "translation": "Prima de continuar — come está a cabeça hoje?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você dormiu bem, sem febre. A cabeça tá clara. Você responde com a palavra de F8:",
                    "options": [
                        {"id": "a", "text": "Sto meglio"},
                        {"id": "b", "text": "Ho febbre"},
                        {"id": "c", "text": "Sto malato"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Bene. Hoy necesitamos esa testa despejada.",
                },
                {
                    "kind": "narrative",
                    "text": "Uma vizinha abre a janela do segundo andar pra estender lençóis. Cumprimenta vocês.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Vecina",
                    "line": "¡Benes días, Lucia! ¡Y los jóvienies!",
                    "translation": "Bom dia, Lucia! E os giovanes!",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecina",
                    "question": "A vizinha cumprimenta de manhã cedo. Você responde do mesmo jeito:",
                    "options": [
                        {"id": "a", "text": "¡Benes días!"},
                        {"id": "b", "text": "¡Buon pomeriggio!"},
                        {"id": "c", "text": "¡Buona notte!"},
                        {"id": "d", "text": "¡Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Esatto. Si gentes te vieni cumpliendo el saleudo, te suman — no te restan.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Guarda esa casa allá — la de las macetas rojas. Es de un vecino mío. ¿Cómo lo describes?",
                    "translation": "Olha aquela casa ali — a dos vasos vermelhos. É de um vizinho meu. Como você descreve?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara espera que você junte 'hay' (tem) + objeto. 'Hay flores rojas allí.' Mas pra falar sobre o dono, come você diz que é um vizinho?",
                    "options": [
                        {"id": "a", "text": "Es un vecino"},
                        {"id": "b", "text": "Ho un vicino"},
                        {"id": "c", "text": "Sono vecino"},
                        {"id": "d", "text": "Mi chiamo vecino"},
                    ],
                    "correct": "a",
                    "word_id": "it_vecino", "target": "vecino", "native": "vizinho",
                    "npc_reaction": "Esatto. Cada casa ha su gente. Aquí nadie es anónimo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Cómo te sientes adesso?Estamos por llegar a la piazza grande.",
                    "translation": "Como você se sente agora?Tamos quase chegando na piazza grande.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você sente nervosismo — piu pelo menos não tem febre nem dor. Você está... funcional. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sto bene"},
                        {"id": "b", "text": "Sto male"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Si necesitas decir 'ho paura', dilo — ma no hace falta esconderlo bajo 'male'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Forestiero — ¿te gusta caminar por este borgo?Después de todo lo que vivimos.",
                    "translation": "Forasteiro — você gosta de caminhar por esse borgo?Depois de tudo que a gente viveu.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Você gosta — apesar de tudo. As ruas, os cheiros, as pessoas. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sí, mi piace"},
                        {"id": "b", "text": "Non mi piace"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto",
                    "npc_reaction": "Bene. Ya es 'tu' borgo también — ancoraque no quiera el Guardia.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # CONFRONTO. La Guardia bloqueia a rua estreita. Exige o pase. Cada
    # exercício é uma fala dele — gated quando crítico. Tensão alta, ritmo
    # rápido. Lucia intervém no final. Falas de Guardia autoritárias.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Vocês dobraram a esquina pra outra rua. Estreita, paredes "
                    "altas de adobe nos dois lados. No fundo — uma silhueta no "
                    "meio do caminho. Chapéu baixo. Casaco escuro.\n\n"
                    "La Guardia del Mercato bloqueia a passagem."
                ),
                "now": "Confronto. Cada palavra importa. Errar trava — você tem que se sair.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "👤 La Guardia · Meio da rua · Sem desviar",
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "Para. No avancen más.",
                    "translation": "Para. Não avancem mais.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Lucia estende o braço pra trás — gesto de parar Chiara e você. Nico se posiciona meio passo à fronte de Lucia.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "Ustedes — yo no quiero problema. Sólo el forestiero. Forestiero — vieni aquí.",
                    "translation": "Vocês — eu não quero problema. Só o forasteiro. Forasteiro — vem aqui.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "La Guardia",
                    "question": "Ele te chama. Você precisa cumprimentar primeiro pra ganhar tempo — formale, sem provocação:",
                    "options": [
                        {"id": "a", "text": "Benes días, señor"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "La Guardia guarda con desprecio. 'Benes días no me cubre la espalda. ¿Hai el pase?'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "¿Cómo te chiami, forestiero?",
                    "translation": "Como você se chama, forasteiro?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "La Guardia",
                    "question": "Pergunta direta. Mentir agora seria pior. Você responde claro:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "No ho nombre"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Anotado. ¿Cuántos años hai?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "La Guardia",
                    "question": "La Guardia quer sua idade — exata. Vinte anni:",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Sono veinte"},
                        {"id": "c", "text": "Non ricordo"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Veinte. Edad de servir o de huir. ¿De dónde vieni?",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "¿De dónde vieni?Habla.",
                    "translation": "De onde você vem?Fala.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "La Guardia",
                    "question": "Você não lembra. Mentir agora seria pego. A verdade pode ajudar — você não tem nada a esconder mesmo:",
                    "options": [
                        {"id": "a", "text": "Non ricordo. Sono forestiero."},
                        {"id": "b", "text": "Sono del borgo"},
                        {"id": "c", "text": "Ho veinte años"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_forestiero", "target": "forestiero", "native": "estrangeiro",
                    "npc_reaction": "La Guardia levanta una ceja. 'Convieniiente. ¿Hai el pase o no?'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "Senza pase del Podesta, salees del borgo prima del atardecer. Es la ley.",
                    "translation": "Sem pase do Podesta, você sai do borgo prima do entardecer. É a lei.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Andiamo adesso mismo al municipio. Lo estamos llevando.",
                    "translation": "Andiamo agora mesmo na prefeitura. Tamos levando ele.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "Conmigo. Yo lo llevo.",
                    "translation": "Comigo. Eu levo ele.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Você sente o ar virar pesado. Lucia dá um passo à fronte — não rápido, piu firme. Chiara aperta o seu braço atrás.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Guardia — un momento.",
                    "translation": "Guardia — um momento.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lucia passa do lado de Nico e se aproxima de La Guardia "
                        "a passos curtos. Para a um metro dele. Fala três frases "
                        "baixinho — voz tão baixa que ninguém do grupo escuta.\n\n"
                        "La Guardia muda a expressão. A primeira coisa é "
                        "surpresa. Depois alguma coisa mais difícil de nomear — "
                        "respeito?medo?cálculo?\n\n"
                        "Ele recua meio passo."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "...Mañana. Si no hay pase mañana — lo busco yo mismo.",
                    "translation": "...Amanhã. Se não tiver pase amanhã — eu mesmo procuro ele.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "La Guardia lança um olhar duro pra você. Vira. Vai embora pela rua. Lucia não se vira pra ver ele sair — espera que os passos sumam.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia vira pro grupo. 'Andiamo a la fuente. Necesitamos sentarnos un momento.' Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado"},
                        {"id": "b", "text": "No, ho paura"},
                        {"id": "c", "text": "Adiós Lucia"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Sigan caminando come si nada. Esta strada todavía ha ojos.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico, baixo, do seu lado enquanto caminham: 'Forestiero — ¿estás bene?' Você responde verdade — não tá 100%, piu tá:",
                    "options": [
                        {"id": "a", "text": "Mejor que hace cinco minutos"},
                        {"id": "b", "text": "Ho veinte años"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Sono forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Lo creo. Resisti hasta la fuente.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Na fonte da piazza. Lucia ensenzaa o imperativo — porque o protagonista
    # acabou de ouvir La Guardia usando: 'Para', 'Habla', 'Vieni aquí'.
    # Ela quer que ele reconheça quando alguém dá ordem.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Vocês chegaram à fonte de pedra do centro da piazza. Lucia "
                    "se senta na beira. Chiara bebe água com as mãos. Nico fica "
                    "de pé olhando ao redor.\n\n"
                    "Lucia: 'Ya viste cómo te habló La Guardia?Todas las "
                    "parole eran cortas. Órdenes. Esatto es importante que "
                    "reconozcas.'"
                ),
                "now": "Lucia vai te ensenzaar imperativo — come ouvir ordines e dar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "La Guardia ha detto 'para', 'habla', 'vieni aquí'. Esas son órdenes. Cortas, directas. Senza 'por favor'.",
                    "translation": "La Guardia disse 'para', 'fala', 'vem aqui'. Essas são ordines. Curtas, diretas. Sem 'por favor'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Vieni aquí",
                    "meaning": "Vem aqui",
                    "note": "ordem de movimento — do verbo 'venire'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Para",
                    "meaning": "Para (de parar)",
                    "note": "ordem pra parar de fazer algo — uma das mais comuns",
                },
                {
                    "kind": "reveal",
                    "phrase": "Guarda",
                    "meaning": "Olha",
                    "note": "chamar a atenção pra alguma coisa — 'guarda' é amigável OU autoritário pelo tom",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Vieni",   "isKey": True},
                        {"text": " / ",   "isKey": False},
                        {"text": "Para",  "isKey": True},
                        {"text": " / ",   "isKey": False},
                        {"text": "Guarda",  "isKey": True},
                        {"text": " / ",   "isKey": False},
                        {"text": "Habla", "isKey": True},
                    ],
                    "example": "— Para. Guarda. Habla. Vieni.",
                    "translation": "— Para. Olha. Fala. Vem.",
                    "note": "imperativo informale — quem dá ordem usa estas forpiu curtas",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "La Guardia usou esta palavra quando vocês se aproximaram. 'No avancen más.' A palavra curta dele foi:",
                    "options": [
                        {"id": "a", "text": "Para"},
                        {"id": "b", "text": "Vieni"},
                        {"id": "c", "text": "Guarda"},
                        {"id": "d", "text": "Habla"},
                    ],
                    "correct": "a",
                    "word_id": "it_para", "target": "para", "native": "para",
                    "npc_reaction": "Para. Es para detener un movimiento. Reconoce esa palabra siempre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Depois ele te chamou: 'Forestiero — ___ aquí'. A palavra de chamada foi:",
                    "options": [
                        {"id": "a", "text": "Vieni"},
                        {"id": "b", "text": "Para"},
                        {"id": "c", "text": "Guarda"},
                        {"id": "d", "text": "Habla"},
                    ],
                    "correct": "a",
                    "word_id": "it_vieni", "target": "vieni", "native": "vem",
                    "npc_reaction": "Vieni. Movimiento hacia el que habla. Cuando alguien te dice 'vieni' — decide rápido si vas o no.",
                },
                {
                    "kind": "narrative",
                    "text": "Chiara senta do lado de Lucia na beira da fonte. Olha pra você atenta — quer ver se você tá pegando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Y si yo quiero que tu mires algo importante — te digo:",
                    "translation": "E se eu quero que você olhe alguma coisa importante — eu digo:",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pra um pombo na fonte. 'Forestiero — ___' — a palavra pra chamar sua atenção é:",
                    "options": [
                        {"id": "a", "text": "Guarda"},
                        {"id": "b", "text": "Vieni"},
                        {"id": "c", "text": "Para"},
                        {"id": "d", "text": "Habla"},
                    ],
                    "correct": "a",
                    "word_id": "it_guarda", "target": "guarda", "native": "olha",
                    "npc_reaction": "Guarda. Se usa para señalar — entre amigos, entre extraños, en cualquier sitio.",
                },
                {
                    "kind": "narrative",
                    "text": "Nico se levanta da beira da fonte, sacode a poeira da calça. Olha pros três e diz uma palavra só, decidida.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Bene — andiamo. Los cuatro. Io vado delante, Lucia atrás, Chiara y el forestiero en medio.",
                    "translation": "Bom — andiamo. Os quatro. Eu vou na fronte, Lucia atrás, Chiara e o forasteiro no meio.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Andiamo / vais / van",
                    "meaning": "Nós andiamo / vocês vão / eles vão",
                    "note": "expanesão de 'io vado / tu vieni' (F6). Quando o grupo se move: andiamo. Quando outros se movem: van.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Io vado", "isKey": True},
                        {"text": " · ",    "isKey": False},
                        {"text": "Tu vas", "isKey": True},
                        {"text": " · ",    "isKey": False},
                        {"text": "Lei va","isKey": True},
                        {"text": " · ",    "isKey": False},
                        {"text": "Nosotros andiamo", "isKey": True},
                        {"text": " · ",    "isKey": False},
                        {"text": "Ellos van",      "isKey": True},
                    ],
                    "example": "Io vado a la fuente. Tu vas con me. Lei va detrás. Nosotros andiamo juntos. Los vecinos van por otra strada.",
                    "translation": "Eu vou à fonte. Tu vais comigo. Ela vai atrás. Nós andiamo juntos. Os vizinhos vão por outra rua.",
                    "note": "MESMO verbo (IR) — muda com quem faz: yo / tu / él · ella / noi / ellos",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico quer confirmar que vão JUNTOS. 'Los cuatro — ___ al municipio mañana.' A palavra do verbo IR para 'nós' é:",
                    "options": [
                        {"id": "a", "text": "andiamo"},
                        {"id": "b", "text": "vado"},
                        {"id": "c", "text": "vas"},
                        {"id": "d", "text": "va"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo", "target": "noi andiamo", "native": "nós andiamo",
                    "npc_reaction": "Andiamo. Cuando es el grupo, no eres tu solo — 'andiamo'. Nunca 'yo andiamo'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Uns vizinhos passam do outro lado da piazza indo pro mercato. Como Chiara descreve o que eles fazem?'Ellos ___ al mercato.'",
                    "options": [
                        {"id": "a", "text": "van"},
                        {"id": "b", "text": "andiamo"},
                        {"id": "c", "text": "vado"},
                        {"id": "d", "text": "vas"},
                    ],
                    "correct": "a",
                    "word_id": "it_van", "target": "ellos van", "native": "eles vão",
                    "npc_reaction": "Van. Otros — 'ellos van'. La forma cambia con la gente, no con te.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Y si vieni a buscarme y no sabes dónde sto — pregúntame con voz fuerte: 'Lucia — ¿dónde estás?'",
                    "translation": "E se você vem me buscar e não sabe onde estou — me pergunta com voz forte: 'Lucia — onde você está?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia explica que perguntar onde alguém está é simples. A pergunta é:",
                    "options": [
                        {"id": "a", "text": "¿Dónde estás?"},
                        {"id": "b", "text": "¿Cómo estás?"},
                        {"id": "c", "text": "¿Cuántos años?"},
                        {"id": "d", "text": "¿Tu vieni?"},
                    ],
                    "correct": "a",
                    "word_id": "it_dove_estas", "target": "¿dónde estás?", "native": "onde você está?",
                    "npc_reaction": "Esatto. Si gritas '¿dónde estás?' en este borgo, alguien te responde. Te lo prometo.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # De volta pra casa de Antonio il Contadino. Tarde. Antonio il Contadino ouve o relato.
    # Decisão sobre o que fazer amanhã com o Podesta. Lucia sutilmente
    # se posiciona — confiável, calma, indispensável. Poucos exercícios,
    # foco em dinâmica de grupo e tensão.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico", "Antonio il Contadino"],
                "story": (
                    "Vocês voltaram pra casa de Antonio il Contadino sem ir ao municipio "
                    "hoje. Lucia decidiu: 'Mañana — con calma, no con sustos.' "
                    "Antonio il Contadino já estava esperando — Bianca tinha mandado um "
                    "recado.\n\n"
                    "Agora os cinco sentados em volta da mesa, tarde caindo. "
                    "Lucia contando a Antonio il Contadino o que aconteceu — em italiano "
                    "lento, palavra por palavra."
                ),
                "now": "Decisão do grupo sobre come abordar o Podesta amanhã.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌇 Tarde · Casa de Antonio il Contadino · Cinco em volta da mesa baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Lucia — me contaste todo. Ma hay algo que no me contaste. ¿Qué le hai detto al Guardia para que se fuera?",
                    "translation": "Lucia — você mi ha raccontatou tudo. Mas tem algo que não mi ha raccontatou. O que você falou pro Guardia pra ele ir embora?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia olha pra Antonio il Contadino um momento mais longo que o normale. Pondera. Decide responder uma versão.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Lo conocí hace años, prima de venire al borgo. Sé cose de él que él prefiere no recordar. Nada más.",
                    "translation": "Eu o conheci faz anni, prima de vir pro borgo. Sei coisas dele que ele prefere não lembrar. Nada mais.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "A resposta é razoável. Antonio il Contadino aceita. Mas Nico — "
                        "do seu lado — não acredita. Você vê na cara dele. "
                        "Ele não diz nada."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino se vira pra você. 'Forestiero — mañana al amanecer andiamo al municipio. ¿Tu vieni con calma?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado"},
                        {"id": "b", "text": "No, ho paura"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Bene. Ma esta vez vas tu adelante, no atrás. Il Podesta ha que verte la cara.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Io vado también. Y Lucia. Y Nico. Los cuatro al fronte del Podesta, no sólo el forestiero.",
                    "translation": "Eu vou também. E Lucia. E Nico. Os quatro na fronte do Podesta, não só o forasteiro.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Cenamos algo simple — sobró cibo de ayer. ¿Te gusta el guiso?",
                    "translation": "Jantamos algo simples — sobrou cibo de ontem. Você gosta de ensopado?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia coloca uma tigela na sua fronte. Cheiro de ensopado quente. Você prova — você gosta:",
                    "options": [
                        {"id": "a", "text": "Sí, mi piace"},
                        {"id": "b", "text": "Non ho paura"},
                        {"id": "c", "text": "Sto malato"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto",
                    "npc_reaction": "Bene. Necesitas energía. Mañana es día largo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta '¿Cuándo andiamo al municipio?'. Antonio il Contadino responde com a palavra que indica o dia que vem:",
                    "options": [
                        {"id": "a", "text": "Mañana"},
                        {"id": "b", "text": "Hoy"},
                        {"id": "c", "text": "Ayer"},
                        {"id": "d", "text": "Vecino"},
                    ],
                    "correct": "a",
                    "word_id": "it_domani", "target": "mañana", "native": "amanhã",
                    "npc_reaction": "Mañana al amanecer. Prima de que el borgo despierte del todo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Mejor. Il Podesta respeta grupo más que solo. Ma hablar — habla el forestiero.",
                    "translation": "Melhor. O Podesta respeita grupo mais que sozinho. Mas falar — fala o forasteiro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino quer que VOCÊ fale com o Podesta — não eles. Você precisa aceitar a responsabilidade:",
                    "options": [
                        {"id": "a", "text": "Io vado a hablar"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Non mi piace"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Bene. Si tartamudeas, te corregimos en silencio. Ma la voz ha que uscire de ti.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Nico se levanta da mesa. Vai até a janela. Olha pra rua "
                        "que já tá escurecendo. Não diz nada por um tempo.\n\n"
                        "Volta. Senta. Olha pra Lucia sem disfarçar."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Lucia — grazie. Por lo del Guardia. No sé qué le hai detto ma funcionó.",
                    "translation": "Lucia — obrigado. Pelo que aconteceu com o Guardia. Não sei o que você falou pra ele piu funcionou.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Nico agradeceu — piu o tom não foi 100% gratidão pura. Lucia sorri sem pressa e responde:",
                    "options": [
                        {"id": "a", "text": "De nada, Nico"},
                        {"id": "b", "text": "Adiós Nico"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Para esto sto. Y vado a estar mañana también.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lamparina baixa. Antonio il Contadino olha pra cada um deles em volta "
                        "da mesa. Para um momento em Lucia. Outro em você. "
                        "Não decide nada — piu pensou em decidir alguma coisa."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Noite tarde. Antonio il Contadino, Lucia e Nico saem pra organizar coisas pra
    # manhã. Você fica com Chiara na salea. Conversa difícil sobre o que ela
    # viu — e o que ela acha que está acontecendo. Gate: errar trava.
    # Transição direta pra F11.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico", "Antonio il Contadino"],
                "story": (
                    "Antonio il Contadino saiu pra ver dois vizinhos — pedir que servissem "
                    "de testemunha amanhã. Lucia saiu com ele — disse que precisa "
                    "ver algo na casa de hóspedes. Nico saiu atrás dela 'para "
                    "ayudar', piu você sabe — ele tá seguindo.\n\n"
                    "Sobrou você e Chiara na salea. Ela fechou a porta da fronte."
                ),
                "now": "Conversa difícil. Cada palavra importa. Você precisa estar presente.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🕯️ Sala · Noite · Chiara sentada na cadeira em fronte · Lamparina baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Forestiero — necesito hablar con te. Solos.",
                    "translation": "Forasteiro — preciso falar com você. Sozinhos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara parece séria — diferente do jeito dela. Você confirma que tá ouvindo:",
                    "options": [
                        {"id": "a", "text": "Sí, te escucho"},
                        {"id": "b", "text": "Non ho paura"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_si", "target": "sí", "native": "sim",
                    "npc_reaction": "Bene. Lo que vado a decirte — no se lo cuentes a nadie. Ni a Nico.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Chiara olha pra porta — fechada. Pra janela — vazia. Volta pra você. Voz baixa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Yo vi lo que Lucia le ha detto al Guardia. Stavo más cerca que voi.",
                    "translation": "Eu vi o que Lucia falou pro Guardia. Eu tava mais perto que vocês.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você gela. Chiara vai dizer alguma coisa que muda tudo. Você não sabe ainda se quer saber.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "No oí las parole — ma leí la cara del Guardia. Y conozco esa cara. Es la cara de chi recibe ordine de un superiore.",
                    "translation": "Não ouvi as palavras — piu li o rosto do Guardia. E conheço esse rosto. É o rosto de quem recebe ordem de um superiore.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara espera você processar. A informação é pesada. Você pergunta — em palavras que você tem:",
                    "options": [
                        {"id": "a", "text": "¿Lucia es...?"},
                        {"id": "b", "text": "Sto bene"},
                        {"id": "c", "text": "Adiós Chiara"},
                        {"id": "d", "text": "Ho veinte años"},
                    ],
                    "correct": "a",
                    "word_id": "it_es", "target": "es", "native": "é",
                    "npc_reaction": "No sé qué es. Ma no es sólo una guaritrice. Esatto sí.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Por questo te digo — no se lo cuentes a nadie. Ni a Nico. Si Nico sabe, va a hacer algo. Y si Lucia descubre que sabemos — no sé qué hace.",
                    "translation": "Por isso te digo — não conta pra ninguém. Nem pro Nico. Se Nico souber, ele vai fazer alguma coisa. E se Lucia descobrir que sabemos — não sei o que ela faz.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara precisa da sua promessa. Você diz que entendeu, que vai guardar:",
                    "options": [
                        {"id": "a", "text": "Non lo dico a nessuno"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Benes nottes"},
                    ],
                    "correct": "a",
                    "word_id": "it_no", "target": "no", "native": "não",
                    "npc_reaction": "Bene. Mañana al municipio — todo normale. Como si nada. Después — los dos vigilamos.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "??? Chiara olha pra porta. Passos vindo. Lucia e Nico voltando juntos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Como si nada, forestiero. Guarda normale — habla normale.",
                    "translation": "Como se nada. Olha normale — fala normale.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "A porta abre. Lucia entra primeiro. Sorri ao ver vocês "
                        "dois. 'Ya volvieron Antonio il Contadino y los vecinos. Mañana al "
                        "amanecer andiamo.'\n\n"
                        "Nico vem atrás. Olha pra Chiara. Olha pra você. Pensa "
                        "em perguntar algo — piu não pergunta."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia se aproxima de você normale — calorosa come sempre. 'Forestiero — ¿cómo estás?Hai que dormir temprano hoy.' Você responde come se nada tivesse acontecido:",
                    "options": [
                        {"id": "a", "text": "Sto bene, grazie"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Non mi piace"},
                        {"id": "d", "text": "Adiós Lucia"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Vado a preparar una infusión suave para que duerpiu profundo. Mañana es día largo.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F11 ───────────────────────
                {
                    "kind": "scene",
                    "text": "🌙 Casa silenciosa · Lamparina apagada · Quarto",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você deitou na cama com a infusão de Lucia nas mãos. "
                        "Olhou pro frasco por um longo tempo prima de tomar. "
                        "Aquele que ela tinha deixado na F8.\n\n"
                        "Tomou. Não tinha come recusar sem levantar suspeita. "
                        "O gosto era diferente esta noite — mais amargo. Ou era "
                        "a sua imaginação."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Mañana, forestiero. Mañana.",
                    "translation": "Amanhã, forasteiro. Amanhã.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Chiara sussurrou da cadeira no canto onde ela dormiu de "
                        "novo — ela tinha avisado que ia ficar. Você fechou os "
                        "olhos.\n\n"
                        "O sono veio rápido. Sonho com mãos de Lucia na sua "
                        "testa. Com o rosto de La Guardia recuando. Com a "
                        "palavra 'fuoco' queimando atrás dos olhos.\n\n"
                        "Amanhã — o Podesta."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




