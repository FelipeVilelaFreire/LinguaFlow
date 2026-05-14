"""
Seed das 6 seções da Fase 11 Espanhol A1 — "El Ayuntamiento".

Primeira aparição de El Alcalde — boss da T1. Os quatro vão ao ayuntamiento
ao amanhecer pedir o pase do forastero. El Alcalde recebe sem se levantar,
ouve, calcula. Não concede o pase — exige que voltem em 3 dias com
testemunhas.

Vocab novo (2): testigo · sello  (+ papel apresentado em vocab_list)
Linguagem nova: "Voy a..." — quando o personagem diz o que vai fazer.
                Apresentado pelos próprios NPCs sem nomear regra.

Revisão F1-F10 (maioria dos exercícios):
  · me llamo / soy forastero (F1, F8)
  · ¿cómo estás? / estoy bien (F1, F8)
  · tengo veinte años (F7)
  · gracias / por favor (F1)
  · buenos días / buenas tardes (F1)
  · mira / ven (F10)
  · me gusta (F9)

NPC principais: El Alcalde (1ª aparição) · Don Miguel · os 4
Arco emocional: preparação → confronto frio → pequena vitória (volvemos)
Transição: F12 abre logo após sair do ayuntamiento.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f11_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Chegada ao ayuntamiento. Apresentação rápida + 1 palavra nova (testigo).
    # Demais exercícios são revisão de F1-F10 — saudação formal, identidade,
    # idade, estado.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🏛️ Ayuntamiento de San Cristóbal · Amanhecer · Sala fria\n\n"
                        "Pedra de cantaria nas paredes. Bandeira pendurada. Mesa "
                        "longa de madeira com tinta seca, papéis empilhados e um "
                        "selo de cera vermelha à mão direita."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "Vocês cinco entram. Don Miguel à frente. O Alcalde está sentado — não se levanta.",
                },
                {
                    "kind": "npc",
                    "npc": "El Alcalde",
                    "line": "Don Miguel. Tan temprano. ¿A qué debo el honor?",
                    "is_new_npc": True,
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Buenos días, señor Alcalde. El forastero necesita el pase. Vino conmigo desde la primera mañana.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "El Alcalde te olha de cima a baixo. Não cordial, não hostil. Calculista.",
                },
                {
                    "kind": "npc",
                    "npc": "El Alcalde",
                    "line": "Ven aquí, joven. Cerca de la mesa. Que te vea.",
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
                    "npc": "El Alcalde",
                    "question": "Sol acabou de subir. Você cumprimenta com respeito formal:",
                    "options": [
                        {"id": "a", "text": "Buenos días, señor Alcalde"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. Cortés. Eso ya cuenta — un poco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Ele te avalia em silêncio. 'Dime — ¿quién eres tú aquí?'",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Estoy forastero"},
                        {"id": "c", "text": "Tengo forastero"},
                        {"id": "d", "text": "Me llamo forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_soy", "target": "soy", "native": "sou",
                    "npc_reaction": "Forastero. Sin documentos. Sin sello. Eso es lo que eres oficialmente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "El pase no se da sin testigos. Necesito a alguien que pueda hablar por ti.",
                    "translation": "O pase não se dá sem testigos. Preciso de alguém que possa falar por você.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "El Alcalde acabou de usar uma palavra nova — quem pode falar a favor de outra pessoa diante de uma autoridade. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Testigo"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Campesino"},
                        {"id": "d", "text": "Vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_testigo", "target": "testigo", "native": "testemunha",
                    "npc_reaction": "Testigo. Tres mínimo. Personas que te hayan visto en el pueblo más de una semana.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Alcalde interroga formalmente — cada pergunta dele é
    # revisão direta de F1-F10. Sem palavras novas aqui.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["El Alcalde", "Don Miguel"],
                "story": (
                    "El Alcalde tem o papel e o sello na sua frente. Não vai assinar "
                    "nada sem antes te conhecer. Faz perguntas precisas, anota numa "
                    "folha pequena ao lado.\n\n"
                    "'No es interrogatorio. Es protocolo.' — diz sem olhar nos seus olhos."
                ),
                "now": "Interrogatório formal. Cada pergunta dele é uma revisão.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Primero — ¿cómo te llamas?",
                    "translation": "Primeiro — como você se chama?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Sem hesitar. Você responde como sempre:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Anotado. Siguiente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "¿Cuántos años tienes?",
                    "translation": "Quantos anos você tem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Resposta exata, com a estrutura que María já te ensinou:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Me llamo veinte"},
                        {"id": "d", "text": "Estoy veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Edad de servir o de huir. ¿Cuál de las dos?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "¿De dónde vienes? Quiero la verdad — no historias.",
                    "translation": "De onde você vem? Quero a verdade — não histórias.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Você não lembra. Mentir aqui seria pior. Resposta honesta:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo"},
                        {"id": "b", "text": "Soy del pueblo"},
                        {"id": "c", "text": "Tengo veinte años"},
                        {"id": "d", "text": "Me llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                    "npc_reaction": "Conveniente o sospechoso. Aún no decido cuál.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "¿Cómo estás aquí, en mi pueblo, después de tantos días? ¿Bien? ¿Mal?",
                    "translation": "Como você está aqui, no meu pueblo, depois de tantos dias? Bem? Mal?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Você está bem — apesar de tudo. O grupo acolheu. Resposta com 'estoy':",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Significa que el pueblo te trata mejor de lo que mereces — o así pareces creer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "¿Te gusta el pueblo? Sé sincero — el papel lleva la verdad.",
                    "translation": "Você gosta do pueblo? Seja sincero — o papel leva a verdade.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "A plaza, Carmen, Rosa, o cheiro de pão. Honesto:",
                    "options": [
                        {"id": "a", "text": "Sí, me gusta"},
                        {"id": "b", "text": "No me gusta"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Bueno. La sinceridad cuenta. Aunque no salva.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Y la última pregunta — ¿qué eres tú aquí?",
                    "translation": "E a última pergunta — o que você é aqui?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "O rótulo oficial — o que está nos papéis dele:",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Soy campesino"},
                        {"id": "c", "text": "Soy vecino"},
                        {"id": "d", "text": "Soy alcalde"},
                    ],
                    "correct": "a",
                    "word_id": "es_soy", "target": "soy forastero", "native": "sou forasteiro",
                    "npc_reaction": "Forastero. Lo que pensaba. Ese es el problema.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Negociação. Alcalde impõe condições. María intervém. O grupo decide
    # dividir as tarefas. Aqui aparecem alguns "Voy a..." organicamente —
    # personagens dizendo o que vão fazer logo. Sem nomear regra. Mistura
    # exercícios sobre o novo padrão com REVISÃO PESADA.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["El Alcalde", "Don Miguel", "María"],
                "story": (
                    "El Alcalde escreveu três linhas no papel. Não te olhou enquanto "
                    "escrevia. Quando terminou, deixou a pena e cruzou as mãos sobre "
                    "a mesa.\n\n"
                    "'Bien. Ahora hablamos de condiciones.'"
                ),
                "now": "Negociação difícil. Cada palavra do grupo conta.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Sin testigos, no hay sello. Sin sello, no hay pase. Sin pase, sales del pueblo.",
                    "translation": "Sem testigos, não tem selo. Sem selo, não tem pase. Sem pase, você sai do pueblo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel se levanta. 'Yo te ayudo' — fala pra você firme. O cumprimento que você devolve à Don Miguel:",
                    "options": [
                        {"id": "a", "text": "Gracias, Don Miguel"},
                        {"id": "b", "text": "Adiós Miguel"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Estoy"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. No te dejo solo en esto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Voy a buscar a doña Carmen ahora mismo. Y a Eduardo el herrero.",
                    "translation": "Vou buscar dona Carmen agora mesmo. E Eduardo o ferreiro.",
                },
                {
                    "kind": "player",
                    "text": "Sofía disse 'voy a buscar'. Você nunca ouviu esse jeito antes — mas entende: ela vai fazer algo logo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía disse 'voy a buscar'. Ela está falando:",
                    "options": [
                        {"id": "a", "text": "Do que vai fazer logo"},
                        {"id": "b", "text": "Do que já fez ontem"},
                        {"id": "c", "text": "De quem ela é"},
                        {"id": "d", "text": "De onde ela está"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a buscar", "native": "vou buscar",
                    "npc_reaction": "Eso. 'Voy a' es para algo que sale ahora — algo cercano. Tan simple como decir 'vou' en portugués.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Yo voy a hablar con Eduardo. El forastero viene conmigo — Eduardo lo recuerda de la calle.",
                    "translation": "Eu vou falar com Eduardo. O forasteiro vai comigo — Eduardo lembra dele da rua.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel acabou de explicar o plano. Você confirma que vai com ele:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy"},
                        {"id": "b", "text": "No tengo miedo"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Bueno. Vamos juntos. Eduardo va a aceptar — confío en eso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Yo me quedo aquí. Voy a hablar con el señor Alcalde a solas, si me permite.",
                    "translation": "Eu fico aqui. Vou falar com o senhor Alcalde a sós, se ele permitir.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Silêncio. El Alcalde olha pra María por meio segundo a mais "
                        "do que pra qualquer outra pessoa naquela sala. Não recusa, "
                        "não aceita. Apenas espera."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta pro grupo: '¿Y vosotros — los tres juntos — qué hacemos?' Você responde sobre o que TODO o grupo vai fazer:",
                    "options": [
                        {"id": "a", "text": "Vamos a buscar testigos"},
                        {"id": "b", "text": "Voy a buscar testigos"},
                        {"id": "c", "text": "Va a buscar testigos"},
                        {"id": "d", "text": "Vas a buscar testigos"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos — los tres. Igual que 'vamos' en portugués, pero antes de un verbo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Antes de sair, El Alcalde pergunta pro grupo: 'Estos tres días — ¿cómo van a vivir aquí?' Você responde simples — o grupo cuida de você. Resposta com 'estoy':",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Ya veremos cuánto duran las cosas buenas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Saindo, Don Miguel olha pro Alcalde e cumprimenta formalmente — manhã ainda. Como ele diz adeus?",
                    "options": [
                        {"id": "a", "text": "Buenos días, señor Alcalde"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "El Alcalde acena apenas com a cabeça. Não devolve a saudação.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Saindo do ayuntamiento. Don Miguel para o grupo na escada e explica
    # 'voy a' SEM nomear "futuro próximo". Apenas: "isso é o que você vai
    # fazer logo". Foco em ENTENDER pelo uso. ~3-4 exercícios apenas.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Miguel", "Sofía"],
                "story": (
                    "Vocês saíram do ayuntamiento. María ficou com o Alcalde — "
                    "ainda lá dentro. Os outros quatro sentaram na escada de pedra "
                    "do lado de fora. Don Miguel respirou fundo.\n\n"
                    "'Bueno. Tenemos tres días. Voy a enseñarles algo simple antes "
                    "de que se separen.'"
                ),
                "now": "Don Miguel explica como cada um pode dizer o que VAI fazer.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Lo que usaron ahí dentro — 'voy a buscar', 'voy a hablar' — sirve para decir lo que va a pasar pronto. No hoy ni mañana, exactamente — lo que sale ya.",
                    "translation": "O que vocês usaram lá dentro — 'voy a buscar', 'voy a hablar' — serve para dizer o que vai acontecer logo. Não hoje nem amanhã, exatamente — o que sai já.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Voy a + verbo",
                    "meaning": "Vou + verbo",
                    "note": "para algo que sai logo: voy a comer, voy a salir, voy a hablar",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Cambia con quien lo dice. Si soy yo — 'voy'. Si eres tú — 'vas'. Si es Sofía — 'va'. Si somos nosotros — 'vamos'.",
                    "translation": "Muda com quem diz. Se sou eu — 'voy'. Se é você — 'vas'. Se é Sofía — 'va'. Se somos nós — 'vamos'.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo voy ", "isKey": True},
                        {"text": "· Tú vas ", "isKey": True},
                        {"text": "· Ella va ", "isKey": True},
                        {"text": "· Vamos ", "isKey": True},
                        {"text": "+ a + verbo", "isKey": False},
                    ],
                    "example": "Voy a comer. Vas a hablar. Va a llegar. Vamos a salir.",
                    "translation": "Vou comer. Vais falar. Vai chegar. Vamos sair.",
                    "note": "ya conoces 'voy, vas, va, vamos' (de F6 y F10). Ahora junto con 'a' + outro verbo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía está prestes a sair pra buscar Carmen. Pra dizer o que ela vai fazer agora:",
                    "options": [
                        {"id": "a", "text": "Voy a buscar a Carmen"},
                        {"id": "b", "text": "Vas a buscar a Carmen"},
                        {"id": "c", "text": "Va a buscar a Carmen"},
                        {"id": "d", "text": "Vamos a buscar"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a", "native": "vou (algo logo)",
                    "npc_reaction": "Yo — voy. Lo dice cuando salgo yo misma.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel pergunta pra você: 'Forastero — tú ___ con mi padre, ¿no?' Pra dizer o que você vai fazer (vem com Don Miguel):",
                    "options": [
                        {"id": "a", "text": "vas a venir"},
                        {"id": "b", "text": "voy a venir"},
                        {"id": "c", "text": "va a venir"},
                        {"id": "d", "text": "vamos a venir"},
                    ],
                    "correct": "a",
                    "word_id": "es_vas_a", "target": "vas a", "native": "vais",
                    "npc_reaction": "Tú — vas. Cuando le hablas a alguien.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pergunta pro grupo: 'Y nosotros — los tres — ¿qué ___ a hacer juntos?' (todos vão sair em direções diferentes mas juntos no plano):",
                    "options": [
                        {"id": "a", "text": "vamos"},
                        {"id": "b", "text": "voy"},
                        {"id": "c", "text": "vas"},
                        {"id": "d", "text": "va"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Nosotros — vamos. Cuando es el grupo entero.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Conversa do grupo sentados na escada. Cada um diz o que vai fazer.
    # Sofía sai correndo. Miguel decide vir junto com você e Don Miguel.
    # Foco em USAR o novo + revisão pesada de F1-F10.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Miguel", "Sofía"],
                "story": (
                    "Don Miguel acabou a pequena explicação. Sofía já estava de "
                    "pé, ansiosa pra ir buscar Carmen. Miguel se levantou junto.\n\n"
                    "'Bueno. ¿Quién va a hacer qué? Lo decimos en voz alta para "
                    "no olvidar.'"
                ),
                "now": "Cada um diz o que vai fazer. Você acompanha.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Yo voy a buscar a Carmen ahora. Ella estaba bordando en la plaza esta mañana — sigue ahí.",
                    "translation": "Eu vou buscar Carmen agora. Ela tava bordando na plaza essa manhã — continua lá.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você concorda com o plano de Sofía. Quer dizer pra ela 'tá bom, vai':",
                    "options": [
                        {"id": "a", "text": "Vale, sí"},
                        {"id": "b", "text": "No, mal"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_vale", "target": "vale", "native": "tá bom",
                    "npc_reaction": "Vale. Palabra corta del pueblo — sirve para todo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Forastero — tú y yo vamos a la herrería. Eduardo te conoce. Si lo saludas bien, va a aceptar.",
                    "translation": "Forasteiro — você e eu vamos à ferraria. Eduardo te conhece. Se você cumprimentar bem, ele vai aceitar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'vamos a la herrería'. Pra quem ele se refere?",
                    "options": [
                        {"id": "a", "text": "Pra ele e pro forastero (nós dois)"},
                        {"id": "b", "text": "Só pra Sofía"},
                        {"id": "c", "text": "Pra María sozinha"},
                        {"id": "d", "text": "Pro pueblo todo"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos", "native": "vamos (nós)",
                    "npc_reaction": "Tú y yo. Eso es 'nosotros'. Mismo grupo de F10 cuando fuimos a la posada.",
                },
                {
                    "kind": "narrative",
                    "text": "Sofía já saiu correndo pela rua. Miguel olhou pra dentro do ayuntamiento — María ainda lá com o Alcalde.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "¿Y María? Está adentro hace ya bastante. ¿Está bien?",
                    "translation": "E María? Tá dentro faz tempo. Tá bem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel responde calmo: 'María sabe lo que hace'. Como Miguel devolve o agradecimento da Don Miguel pela calma?",
                    "options": [
                        {"id": "a", "text": "Gracias, papá"},
                        {"id": "b", "text": "Adiós papá"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, mijo. Vamos — el día va a ser largo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero — ¿estás bien con todo esto? El Alcalde, los testigos, los tres días.",
                    "translation": "Forasteiro — você tá bem com tudo isso? O Alcalde, os testigos, os três dias.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Honesto — você tá nervoso, mas o grupo tá junto:",
                    "options": [
                        {"id": "a", "text": "Estoy bien, pero tengo miedo"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Estado bien, sensación miedo. Las dos cosas a la vez — eso es ser humano.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Don Miguel + protagonista caminham até a ferraria. Eduardo recebe.
    # Conversa difícil — Eduardo aceita com condição estranha (ver María).
    # Gate: errar trava. Closing prepara F12.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Eduardo"],
                "story": (
                    "Vocês caminharam três quadras até a herrería de Eduardo. "
                    "Fumaça do carvão saindo da chaminé. Som de martelo no metal. "
                    "Eduardo trabalhava com as costas voltadas.\n\n"
                    "Don Miguel: 'Hablo yo primero. Cuando te pregunte, hablas tú.'"
                ),
                "now": "Convencer Eduardo. Errar trava.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🔨 Herrería · Fogo aceso · Eduardo trabalhando com martelo",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Eduardo. Buenos días.",
                    "translation": "Eduardo. Bom dia.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Don Miguel. Joven forastero. ¿Qué los trae a mi taller temprano?",
                    "translation": "Don Miguel. Jovem forasteiro. O que traz vocês na minha oficina cedo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo cumprimentou — formal mas amistoso. Você cumprimenta de volta, sol da manhã:",
                    "options": [
                        {"id": "a", "text": "Buenos días, señor Eduardo"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. Te recuerdo del segundo día — cuando Sofía te enseñaba los vecinos.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Eduardo — necesitamos algo. El Alcalde pide testigos para el pase del forastero. Pensamos en ti.",
                    "translation": "Eduardo — a gente precisa de algo. O Alcalde pede testigos pro pase do forasteiro. Pensamos em ti.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Espera — antes que hables. ¿Cuántos años tienes tú, joven?",
                    "translation": "Espera — antes de você falar. Quantos anos você tem, jovem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Resposta exata — vinte:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Estoy veinte"},
                        {"id": "d", "text": "Me llamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Igual que mi hijo mayor. Está en la otra ciudad.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Eduardo coloca o martelo na bigorna. Limpa as mãos no avental. "
                        "Olha pra você diferente — sem desconfiança, sem amizade. "
                        "Avaliando."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Bueno. Voy a testificar. Pero tengo una condición.",
                    "translation": "Bom. Vou testemunhar. Mas tenho uma condição.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo acabou de aceitar. Você agradece formal:",
                    "options": [
                        {"id": "a", "text": "Gracias, señor Eduardo"},
                        {"id": "b", "text": "Adiós Eduardo"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Pero escucha la condición — ahora.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Voy a testificar — pero el día que vayamos al ayuntamiento, ustedes van a llevarme con María. Ella tiene que ver una cosa que tengo en la espalda.",
                    "translation": "Vou testemunhar — mas no dia que formos ao ayuntamiento, vocês vão me levar até María. Ela tem que ver uma coisa que tenho nas costas.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você não entende o pedido. Don Miguel não pergunta — apenas aceita. "
                        "Eduardo tem algo que precisa que María veja. Não é hora de "
                        "perguntar por quê."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aceita pelo grupo. 'Bueno. Nosotros ___ a llevarte con María.' Quando é o grupo inteiro, qual forma usar?",
                    "options": [
                        {"id": "a", "text": "vamos"},
                        {"id": "b", "text": "voy"},
                        {"id": "c", "text": "van"},
                        {"id": "d", "text": "vas"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Nosotros — vamos. Trato hecho, Eduardo.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F12 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🌅 Saindo da herrería · Sol já alto · Don Miguel e você caminhando de volta",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Uno conseguido. Carmen ya está con Sofía. Falta uno más — alguien imparcial.",
                    "translation": "Um conseguido. Carmen já tá com Sofía. Falta mais um — alguém imparcial.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês passam pela esquina do mercado. El Vigilante encostado "
                        "numa parede do outro lado da rua — fingindo conversar com "
                        "outro homem. Mas você sabe que ele te viu.\n\n"
                        "Don Miguel também viu. Não comentou."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
