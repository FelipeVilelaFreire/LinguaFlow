"""
Seed das 6 seções da Fase 11 Italiano A1 — "El Ayuntamiento".

Primeira aparição de Il Podesta — boss da T1. Os quatro vão ao municipio
ao amanhecer pedir o pase do forestiero. Il Podesta recebe sem se levantar,
ouve, calcula. Não concede o pase — exige que voltem em 3 dias com
testemunhas.

Vocab novo (2): testigo · sello  (+ papel apresentado em vocab_list)
Linguagem nova: "Vado a..." — quando o personagem diz o que vai fazer.
                Apresentado pelos próprios NPCs sem nomear regra.

Revisão F1-F10 (maioria dos exercícios):
  · mi chiamo / sono forestiero (F1, F8)
  · ¿cómo estás?/ sto bene (F1, F8)
  · ho veinte años (F7)
  · grazie / por favor (F1)
  · buongiorno / buon pomeriggio (F1)
  · guarda / vieni (F10)
  · mi piace (F9)

NPC principais: Il Podesta (1ª aparição) · Antonio il Contadino · os 4
Arco emocional: preparação → confronto frio → pequena vitória (volvemos)
Transição: F12 abre logo após sair do municipio.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Chegada ao municipio. Apresentação rápida + 1 palavra nova (testigo).
    # Demais exercícios são revisão de F1-F10 — saudação formale, identidade,
    # idade, estado.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "??? Ayuntamiento de San Cristóbal · Amanhecer · Sala fria\n\n"
                        "Pedra de cantaria nas paredes. Bandeira pendurada. Mesa "
                        "longa de madeira com tinta seca, papéis empilhados e um "
                        "selo de cera vermelha à mão direita."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "Vocês cinco entram. Antonio il Contadino à fronte. O Podesta está sentado — não se levanta.",
                },
                {
                    "kind": "npc",
                    "npc": "Il Podesta",
                    "line": "Antonio il Contadino. Tan temprano. ¿A qué debo el honor?",
                    "is_new_npc": True,
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Benes días, señor Podesta. El forestiero necesita el pase. Vino con me desde la primera mañana.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Il Podesta te olha de cima a baixo. Não cordial, não hostil. Calculista.",
                },
                {
                    "kind": "npc",
                    "npc": "Il Podesta",
                    "line": "Vieni aquí, giovane. Cerca de la mesa. Que te vea.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "testigo", "native": "testemunha"},
                        {"target": "sello",   "native": "selo / carimbo"},
                        {"target": "papel",   "native": "papel / documento"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Sol acabou de subir. Você cumprimenta com respeito formale:",
                    "options": [
                        {"id": "a", "text": "Benes días, señor Podesta"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Benes días. Cortés. Esatto ya cuenta — un poco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Ele te avalia em silêncio. 'Dime — ¿quién eres tu aquí?'",
                    "options": [
                        {"id": "a", "text": "Sono forestiero"},
                        {"id": "b", "text": "Sto forestiero"},
                        {"id": "c", "text": "Ho forestiero"},
                        {"id": "d", "text": "Mi chiamo forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_sono", "target": "sono", "native": "sou",
                    "npc_reaction": "Forestiero. Senza documentos. Senza sello. Esatto es lo que eres oficialmente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "El pase no se da senza testigos. Necesito a alguien que pueda hablar por ti.",
                    "translation": "O pase não se dá sem testigos. Preciso de alguém que possa falar por você.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Il Podesta acabou de usar uma palavra nova — quem pode falar a favor de outra pessoa diante de uma autoridade. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Testigo"},
                        {"id": "b", "text": "Forestiero"},
                        {"id": "c", "text": "Campesenzao"},
                        {"id": "d", "text": "Vecino"},
                    ],
                    "correct": "a",
                    "word_id": "it_testigo", "target": "testigo", "native": "testemunha",
                    "npc_reaction": "Testigo. Tres mínimo. Personas que te hayan visto en el borgo más de una semana.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Podesta interroga formalemente — cada pergunta dele é
    # revisão direta de F1-F10. Sem palavras novas aqui.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Il Podesta", "Antonio il Contadino"],
                "story": (
                    "Il Podesta tem o papel e o sello na sua fronte. Não vai assenzaar "
                    "nada sem prima te conhecer. Faz perguntas precisas, anota numa "
                    "folha pequena ao lado.\n\n"
                    "'No es interrogatorio. Es protocolo.' — diz sem olhar nos seus olhos."
                ),
                "now": "Interrogatório formale. Cada pergunta dele é uma revisão.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Primero — ¿cómo te chiami?",
                    "translation": "Primeiro — come você se chama?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Sem hesitar. Você responde come sempre:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Benes días"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Anotado. Siguiente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "¿Cuántos años hai?",
                    "translation": "Quantos anni você tem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Resposta exata, com a estrutura que Lucia já te ensenzaou:",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Sono veinte"},
                        {"id": "c", "text": "Mi chiamo veinte"},
                        {"id": "d", "text": "Sto veinte"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Veinte. Edad de servir o de huir. ¿Cuál de las dos?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "¿De dónde vieni?Quiero la verdad — no historias.",
                    "translation": "De onde você vem?Quero a verdade — não histórias.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Você não lembra. Mentir aqui seria pior. Resposta honesta:",
                    "options": [
                        {"id": "a", "text": "Non ricordo"},
                        {"id": "b", "text": "Sono del borgo"},
                        {"id": "c", "text": "Ho veinte años"},
                        {"id": "d", "text": "Mi chiamo"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                    "npc_reaction": "Convieniiente o sospechoso. Aún no decido cuál.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "¿Cómo estás aquí, en mi borgo, después de tantos días?¿Bene?¿Male?",
                    "translation": "Como você está aqui, no meu borgo, depois de tantos dias?Bem?Male?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Você está bem — apesar de tudo. O grupo acolheu. Resposta com 'sto':",
                    "options": [
                        {"id": "a", "text": "Sto bene, grazie"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Significa que el borgo te trata mejor de lo que mereces — o así pareces creer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "¿Te gusta el borgo?Sé senzacero — el papel lleva la verdad.",
                    "translation": "Você gosta do borgo?Seja senzacero — o papel leva a verdade.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "A piazza, Bianca, Giulia, o cheiro de pão. Honesto:",
                    "options": [
                        {"id": "a", "text": "Sí, mi piace"},
                        {"id": "b", "text": "Non mi piace"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto",
                    "npc_reaction": "Bene. La senzaceridad cuenta. Aunque no saleva.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Y la última pregunta — ¿qué eres tu aquí?",
                    "translation": "E a última pergunta — o que você é aqui?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "O rótulo oficial — o que está nos papéis dele:",
                    "options": [
                        {"id": "a", "text": "Sono forestiero"},
                        {"id": "b", "text": "Sono campesenzao"},
                        {"id": "c", "text": "Sono vecino"},
                        {"id": "d", "text": "Sono alcalde"},
                    ],
                    "correct": "a",
                    "word_id": "it_sono", "target": "sono forestiero", "native": "sou forasteiro",
                    "npc_reaction": "Forestiero. Lo que pensaba. Ese es el problema.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Negociação. Podesta impõe condições. Lucia intervém. O grupo decide
    # dividir as tarefas. Aqui aparecem alguns "Vado a..." organicamente —
    # personagens dizendo o que vão fazer logo. Sem nomear regra. Mistura
    # exercícios sobre o novo padrão com REVISÃO PESADA.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Il Podesta", "Antonio il Contadino", "Lucia"],
                "story": (
                    "Il Podesta escreveu três linhas no papel. Não te olhou enquanto "
                    "escrevia. Quando terminou, deixou a pena e cruzou as mãos sobre "
                    "a mesa.\n\n"
                    "'Bene. Adesso hablamos de condiciones.'"
                ),
                "now": "Negociação difícil. Cada palavra do grupo conta.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Senza testigos, no hay sello. Senza sello, no hay pase. Senza pase, salees del borgo.",
                    "translation": "Sem testigos, não tem selo. Sem selo, não tem pase. Sem pase, você sai do borgo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino se levanta. 'Yo te ayudo' — fala pra você firme. O cumprimento que você devolve à Antonio il Contadino:",
                    "options": [
                        {"id": "a", "text": "Grazie, Antonio il Contadino"},
                        {"id": "b", "text": "Adiós Nico"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Sto"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. No te dejo solo en esto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Vado a buscar a doña Bianca adesso mismo. Y a Pietro el herrero.",
                    "translation": "Vou buscar dona Bianca agora mesmo. E Pietro o ferreiro.",
                },
                {
                    "kind": "player",
                    "text": "Chiara disse 'vado a buscar'. Você nunca ouviu esse jeito prima — piu entende: ela vai fazer algo logo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara disse 'vado a buscar'. Ela está falando:",
                    "options": [
                        {"id": "a", "text": "Do que vai fazer logo"},
                        {"id": "b", "text": "Do que já fez ontem"},
                        {"id": "c", "text": "De quem ela é"},
                        {"id": "d", "text": "De onde ela está"},
                    ],
                    "correct": "a",
                    "word_id": "it_vado_a", "target": "vado a buscar", "native": "vou buscar",
                    "npc_reaction": "Esatto. 'Vado a' es para algo que salee adesso — algo cercano. Tan simple come decir 'vou' en portugués.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Io vado a hablar con Pietro. El forestiero viene con me — Pietro lo recuerda de la strada.",
                    "translation": "Eu vou falar com Pietro. O forasteiro vai comigo — Pietro lembra dele da rua.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino acabou de explicar o plano. Você confirma que vai com ele:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado"},
                        {"id": "b", "text": "Non ho paura"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Bene. Andiamo juntos. Pietro va a aceptar — confío en questo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Yo me quedo aquí. Vado a hablar con el señor Podesta a solas, si me permite.",
                    "translation": "Eu fico aqui. Vou falar com o senhor Podesta a sós, se ele permitir.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Silêncio. Il Podesta olha pra Lucia por meio segundo a mais "
                        "do que pra qualquer outra pessoa naquela salea. Não recusa, "
                        "não aceita. Apenas espera."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta pro grupo: '¿Y voi — los tres juntos — qué hacemos?' Você responde sobre o que TODO o grupo vai fazer:",
                    "options": [
                        {"id": "a", "text": "Andiamo a buscar testigos"},
                        {"id": "b", "text": "Vado a buscar testigos"},
                        {"id": "c", "text": "Va a buscar testigos"},
                        {"id": "d", "text": "Vas a buscar testigos"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo — los tres. Igual que 'andiamo' en portugués, ma prima de un verbo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Prima de sair, Il Podesta pergunta pro grupo: 'Estos tres días — ¿cómo van a vivir aquí?' Você responde simples — o grupo cuida de você. Resposta com 'sto':",
                    "options": [
                        {"id": "a", "text": "Sto bene, grazie"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Ya veremos cuánto duran las cose buenas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Saindo, Antonio il Contadino olha pro Podesta e cumprimenta formalemente — manhã ainda. Como ele diz adeus?",
                    "options": [
                        {"id": "a", "text": "Benes días, señor Podesta"},
                        {"id": "b", "text": "Buona notte"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Il Podesta acena apenas com a cabeça. Não devolve a saudação.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Saindo do municipio. Antonio il Contadino para o grupo na escada e explica
    # 'vado a' SEM nomear "futuro próximo". Apenas: "isso é o que você vai
    # fazer logo". Foco em ENTENDER pelo uso. ~3-4 exercícios apenas.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Nico", "Chiara"],
                "story": (
                    "Vocês saíram do municipio. Lucia ficou com o Podesta — "
                    "ainda lá dentro. Os outros quatro sentaram na escada de pedra "
                    "do lado de fora. Antonio il Contadino respirou fundo.\n\n"
                    "'Bene. Tenemos tres días. Vado a enseñarles algo simple prima "
                    "de que se separen.'"
                ),
                "now": "Antonio il Contadino explica come cada um pode dizer o que VAI fazer.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Lo que usaron ahí dentro — 'vado a buscar', 'vado a hablar' — sirve para decir lo que va a pasar pronto. No hoy ni mañana, exactamente — lo que salee ya.",
                    "translation": "O que vocês usaram lá dentro — 'vado a buscar', 'vado a hablar' — serve para dizer o que vai acontecer logo. Não hoje nem amanhã, exatamente — o que sai já.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Vado a + verbo",
                    "meaning": "Vou + verbo",
                    "note": "para algo que sai logo: vado a comer, vado a uscire, vado a hablar",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Cambia con chi lo dice. Si sono yo — 'vado'. Si eres tu — 'vas'. Si es Chiara — 'va'. Si somos noi — 'andiamo'.",
                    "translation": "Muda com quem diz. Se sou eu — 'vado'. Se é você — 'vas'. Se é Chiara — 'va'. Se somos nós — 'andiamo'.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Io vado ", "isKey": True},
                        {"text": "· Tu vas ", "isKey": True},
                        {"text": "· Lei va ", "isKey": True},
                        {"text": "· Andiamo ", "isKey": True},
                        {"text": "+ a + verbo", "isKey": False},
                    ],
                    "example": "Vado a comer. Vas a hablar. Va a llegar. Andiamo a uscire.",
                    "translation": "Vou comer. Vais falar. Vai chegar. Andiamo sair.",
                    "note": "ya conoces 'vado, vas, va, andiamo' (de F6 y F10). Adesso junto con 'a' + outro verbo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara está prestes a sair pra buscar Bianca. Pra dizer o que ela vai fazer agora:",
                    "options": [
                        {"id": "a", "text": "Vado a buscar a Bianca"},
                        {"id": "b", "text": "Vas a buscar a Bianca"},
                        {"id": "c", "text": "Va a buscar a Bianca"},
                        {"id": "d", "text": "Andiamo a buscar"},
                    ],
                    "correct": "a",
                    "word_id": "it_vado_a", "target": "vado a", "native": "vou (algo logo)",
                    "npc_reaction": "Yo — vado. Lo dice cuando salego yo misma.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico pergunta pra você: 'Forestiero — tu ___ con mi padre, ¿no?' Pra dizer o que você vai fazer (vem com Antonio il Contadino):",
                    "options": [
                        {"id": "a", "text": "vas a venire"},
                        {"id": "b", "text": "vado a venire"},
                        {"id": "c", "text": "va a venire"},
                        {"id": "d", "text": "andiamo a venire"},
                    ],
                    "correct": "a",
                    "word_id": "it_vas_a", "target": "vas a", "native": "vais",
                    "npc_reaction": "Tu — vas. Cuando le hablas a alguien.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino pergunta pro grupo: 'Y noi — los tres — ¿qué ___ a hacer juntos?' (todos vão sair em direções diferentes piu juntos no plano):",
                    "options": [
                        {"id": "a", "text": "andiamo"},
                        {"id": "b", "text": "vado"},
                        {"id": "c", "text": "vas"},
                        {"id": "d", "text": "va"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Nosotros — andiamo. Cuando es el grupo entero.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Conversa do grupo sentados na escada. Cada um diz o que vai fazer.
    # Chiara sai correndo. Nico decide vir junto com você e Antonio il Contadino.
    # Foco em USAR o novo + revisão pesada de F1-F10.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Nico", "Chiara"],
                "story": (
                    "Antonio il Contadino acabou a pequena explicação. Chiara já estava de "
                    "pé, ansiosa pra ir buscar Bianca. Nico se levantou junto.\n\n"
                    "'Bene. ¿Quién va a hacer qué?Lo decimos en voz alta para "
                    "no olvidar.'"
                ),
                "now": "Cada um diz o que vai fazer. Você acompaneha.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Io vado a buscar a Bianca adesso. Ella stavo bordando en la piazza esta mañana — sigue ahí.",
                    "translation": "Eu vou buscar Bianca agora. Ela tava bordando na piazza essa manhã — continua lá.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você concorda com o plano de Chiara. Quer dizer pra ela 'tá bom, vai':",
                    "options": [
                        {"id": "a", "text": "Vale, sí"},
                        {"id": "b", "text": "No, male"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_vale", "target": "vale", "native": "tá bom",
                    "npc_reaction": "Vale. Palabra corta del borgo — sirve para todo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Forestiero — tu y yo andiamo a la herrería. Pietro te conoce. Si lo saleudas bene, va a aceptar.",
                    "translation": "Forasteiro — você e eu andiamo à ferraria. Pietro te conhece. Se você cumprimentar bem, ele vai aceitar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino disse 'andiamo a la herrería'. Pra quem ele se refere?",
                    "options": [
                        {"id": "a", "text": "Pra ele e pro forestiero (nós dois)"},
                        {"id": "b", "text": "Só pra Chiara"},
                        {"id": "c", "text": "Pra Lucia sozinha"},
                        {"id": "d", "text": "Pro borgo todo"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo", "native": "andiamo (nós)",
                    "npc_reaction": "Tu y yo. Esatto es 'noi'. Mismo grupo de F10 cuando fuimos a la locanda.",
                },
                {
                    "kind": "narrative",
                    "text": "Chiara já saiu correndo pela rua. Nico olhou pra dentro do municipio — Lucia ainda lá com o Podesta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "¿Y Lucia?Está adentro hace ya bastante. ¿Está bene?",
                    "translation": "E Lucia?Tá dentro faz tempo. Tá bem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino responde calmo: 'Lucia sabe lo que hace'. Como Nico devolve o agradecimento da Antonio il Contadino pela calma?",
                    "options": [
                        {"id": "a", "text": "Grazie, papá"},
                        {"id": "b", "text": "Adiós papá"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada, mijo. Andiamo — el día va a ser largo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Forestiero — ¿estás bene con todo esto?Il Podesta, los testigos, los tres días.",
                    "translation": "Forasteiro — você tá bem com tudo isso?O Podesta, os testigos, os três dias.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Honesto — você tá nervoso, piu o grupo tá junto:",
                    "options": [
                        {"id": "a", "text": "Sto bene, ma ho paura"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Estado bene, sensación paura. Las dos cose a la vez — questo es ser humano.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Antonio il Contadino + protagonista caminham até a ferraria. Pietro recebe.
    # Conversa difícil — Pietro aceita com condição estranha (ver Lucia).
    # Gate: errar trava. Closenzag prepara F12.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Pietro"],
                "story": (
                    "Vocês caminharam três quadras até a herrería de Pietro. "
                    "Fumaça do carvão saindo da chaminé. Som de martelo no metal. "
                    "Pietro trabalhava com as costas voltadas.\n\n"
                    "Antonio il Contadino: 'Hablo yo primero. Cuando te pregunte, hablas tu.'"
                ),
                "now": "Convienicer Pietro. Errar trava.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🔨 Herrería · Fogo acquesto · Pietro trabalhando com martelo",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Pietro. Benes días.",
                    "translation": "Pietro. Bom dia.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Antonio il Contadino. Jovieni forestiero. ¿Qué los trae a mi taller temprano?",
                    "translation": "Antonio il Contadino. Jovem forasteiro. O que traz vocês na minha oficina cedo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro cumprimentou — formale piu amistoso. Você cumprimenta de volta, sol da manhã:",
                    "options": [
                        {"id": "a", "text": "Benes días, señor Pietro"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Benes días. Te recuerdo del segundo día — cuando Chiara te enseñaba los vecinos.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Pietro — necesitamos algo. Il Podesta pide testigos para el pase del forestiero. Pensamos en ti.",
                    "translation": "Pietro — a gente precisa de algo. O Podesta pede testigos pro pase do forasteiro. Pensamos em ti.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Espera — prima que hables. ¿Cuántos años hai tu, giovane?",
                    "translation": "Espera — prima de você falar. Quantos anni você tem, jovem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Resposta exata — vinte:",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Sono veinte"},
                        {"id": "c", "text": "Sto veinte"},
                        {"id": "d", "text": "Mi chiamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Veinte. Igual que mi hijo mayor. Está en la otra ciudad.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Pietro coloca o martelo na bigorna. Limpa as mãos no avienital. "
                        "Olha pra você diferente — sem desconfiança, sem amizade. "
                        "Avaliando."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Bene. Vado a testificar. Ma ho una condición.",
                    "translation": "Bom. Vou testemunhar. Mas tenho uma condição.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro acabou de aceitar. Você agradece formale:",
                    "options": [
                        {"id": "a", "text": "Grazie, señor Pietro"},
                        {"id": "b", "text": "Adiós Pietro"},
                        {"id": "c", "text": "Sto male"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Ma ascolta la condición — adesso.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Vado a testificar — ma el día que vayamos al municipio, voi van a llevarme con Lucia. Ella ha que ver una cosa que ho en la espalda.",
                    "translation": "Vou testemunhar — piu no dia que formos ao municipio, vocês vão me levar até Lucia. Ela tem que ver uma coisa que tenho nas costas.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você não entende o pedido. Antonio il Contadino não pergunta — apenas aceita. "
                        "Pietro tem algo que precisa que Lucia veja. Não é hora de "
                        "perguntar por quê."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino aceita pelo grupo. 'Bene. Nosotros ___ a llevarte con Lucia.' Quando é o grupo inteiro, qual forma usar?",
                    "options": [
                        {"id": "a", "text": "andiamo"},
                        {"id": "b", "text": "vado"},
                        {"id": "c", "text": "van"},
                        {"id": "d", "text": "vas"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Nosotros — andiamo. Trato hecho, Pietro.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F12 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🌅 Saindo da herrería · Sol já alto · Antonio il Contadino e você caminhando de volta",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Uno conseguido. Bianca ya está con Chiara. Falta uno más — alguien imparcial.",
                    "translation": "Um conseguido. Bianca já tá com Chiara. Falta mais um — alguém imparcial.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês passam pela esquina do mercato. La Guardia encostado "
                        "numa parede do outro lado da rua — fingindo conversar com "
                        "outro homem. Mas você sabe que ele te viu.\n\n"
                        "Antonio il Contadino também viu. Não comentou."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




