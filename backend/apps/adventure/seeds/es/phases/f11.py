"""
Seed das 6 seÃ§Ãµes da Fase 11 Espanhol A1 â€” "El Ayuntamiento".

Primeira apariÃ§Ã£o de El Alcalde â€” boss da T1. Os quatro vÃ£o ao ayuntamiento
ao amanhecer pedir o pase do forastero. El Alcalde recebe sem se levantar,
ouve, calcula. NÃ£o concede o pase â€” exige que voltem em 3 dias com
testemunhas.

Vocab novo (2): testigo Â· sello  (+ papel apresentado em vocab_list)
Linguagem nova: "Voy a..." â€” quando o personagem diz o que vai fazer.
                Apresentado pelos prÃ³prios NPCs sem nomear regra.

RevisÃ£o F1-F10 (maioria dos exercÃ­cios):
  Â· me llamo / soy forastero (F1, F8)
  Â· Â¿cÃ³mo estÃ¡s? / estoy bien (F1, F8)
  Â· tengo veinte aÃ±os (F7)
  Â· gracias / por favor (F1)
  Â· buenos dÃ­as / buenas tardes (F1)
  Â· mira / ven (F10)
  Â· me gusta (F9)

NPC principais: El Alcalde (1Âª apariÃ§Ã£o) Â· Don Miguel Â· os 4
Arco emocional: preparaÃ§Ã£o â†’ confronto frio â†’ pequena vitÃ³ria (volvemos)
TransiÃ§Ã£o: F12 abre logo apÃ³s sair do ayuntamiento.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f11_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Chegada ao ayuntamiento. ApresentaÃ§Ã£o rÃ¡pida + 1 palavra nova (testigo).
    # Demais exercÃ­cios sÃ£o revisÃ£o de F1-F10 â€” saudaÃ§Ã£o formal, identidade,
    # idade, estado.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸ›ï¸ Ayuntamiento de San CristÃ³bal Â· Amanhecer Â· Sala fria\n\n"
                        "Pedra de cantaria nas paredes. Bandeira pendurada. Mesa "
                        "longa de madeira com tinta seca, papÃ©is empilhados e um "
                        "selo de cera vermelha Ã  mÃ£o direita."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "VocÃªs cinco entram. Don Miguel Ã  frente. O Alcalde estÃ¡ sentado â€” nÃ£o se levanta.",
                },
                {
                    "kind": "npc",
                    "npc": "El Alcalde",
                    "line": "Don Miguel. Tan temprano. Â¿A quÃ© debo el honor?",
                    "is_new_npc": True,
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Buenos dÃ­as, seÃ±or Alcalde. El forastero necesita el pase. Vino conmigo desde la primera maÃ±ana.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "El Alcalde te olha de cima a baixo. NÃ£o cordial, nÃ£o hostil. Calculista.",
                },
                {
                    "kind": "npc",
                    "npc": "El Alcalde",
                    "line": "Ven aquÃ­, joven. Cerca de la mesa. Que te vea.",
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
                    "question": "Sol acabou de subir. VocÃª cumprimenta com respeito formal:",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, seÃ±or Alcalde"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. CortÃ©s. Eso ya cuenta â€” un poco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Ele te avalia em silÃªncio. 'Dime â€” Â¿quiÃ©n eres tÃº aquÃ­?'",
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
                    "translation": "O pase nÃ£o se dÃ¡ sem testigos. Preciso de alguÃ©m que possa falar por vocÃª.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "El Alcalde acabou de usar uma palavra nova â€” quem pode falar a favor de outra pessoa diante de uma autoridade. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Testigo"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Campesino"},
                        {"id": "d", "text": "Vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_testigo", "target": "testigo", "native": "testemunha",
                    "npc_reaction": "Testigo. Tres mÃ­nimo. Personas que te hayan visto en el pueblo mÃ¡s de una semana.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # 100% revisÃ£o. Alcalde interroga formalmente â€” cada pergunta dele Ã©
    # revisÃ£o direta de F1-F10. Sem palavras novas aqui.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["El Alcalde", "Don Miguel"],
                "story": (
                    "El Alcalde tem o papel e o sello na sua frente. NÃ£o vai assinar "
                    "nada sem antes te conhecer. Faz perguntas precisas, anota numa "
                    "folha pequena ao lado.\n\n"
                    "'No es interrogatorio. Es protocolo.' â€” diz sem olhar nos seus olhos."
                ),
                "now": "InterrogatÃ³rio formal. Cada pergunta dele Ã© uma revisÃ£o.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Primero â€” Â¿cÃ³mo te llamas?",
                    "translation": "Primeiro â€” como vocÃª se chama?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Sem hesitar. VocÃª responde como sempre:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Anotado. Siguiente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Â¿CuÃ¡ntos aÃ±os tienes?",
                    "translation": "Quantos anos vocÃª tem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Resposta exata, com a estrutura que MarÃ­a jÃ¡ te ensinou:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Me llamo veinte"},
                        {"id": "d", "text": "Estoy veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Edad de servir o de huir. Â¿CuÃ¡l de las dos?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Â¿De dÃ³nde vienes? Quiero la verdad â€” no historias.",
                    "translation": "De onde vocÃª vem? Quero a verdade â€” nÃ£o histÃ³rias.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "VocÃª nÃ£o lembra. Mentir aqui seria pior. Resposta honesta:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo"},
                        {"id": "b", "text": "Soy del pueblo"},
                        {"id": "c", "text": "Tengo veinte aÃ±os"},
                        {"id": "d", "text": "Me llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "nÃ£o me lembro",
                    "npc_reaction": "Conveniente o sospechoso. AÃºn no decido cuÃ¡l.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Â¿CÃ³mo estÃ¡s aquÃ­, en mi pueblo, despuÃ©s de tantos dÃ­as? Â¿Bien? Â¿Mal?",
                    "translation": "Como vocÃª estÃ¡ aqui, no meu pueblo, depois de tantos dias? Bem? Mal?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "VocÃª estÃ¡ bem â€” apesar de tudo. O grupo acolheu. Resposta com 'estoy':",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Significa que el pueblo te trata mejor de lo que mereces â€” o asÃ­ pareces creer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Â¿Te gusta el pueblo? SÃ© sincero â€” el papel lleva la verdad.",
                    "translation": "VocÃª gosta do pueblo? Seja sincero â€” o papel leva a verdade.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "A plaza, Carmen, Rosa, o cheiro de pÃ£o. Honesto:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me gusta"},
                        {"id": "b", "text": "No me gusta"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Bueno. La sinceridad cuenta. Aunque no salva.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Y la Ãºltima pregunta â€” Â¿quÃ© eres tÃº aquÃ­?",
                    "translation": "E a Ãºltima pergunta â€” o que vocÃª Ã© aqui?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "O rÃ³tulo oficial â€” o que estÃ¡ nos papÃ©is dele:",
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

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # NegociaÃ§Ã£o. Alcalde impÃµe condiÃ§Ãµes. MarÃ­a intervÃ©m. O grupo decide
    # dividir as tarefas. Aqui aparecem alguns "Voy a..." organicamente â€”
    # personagens dizendo o que vÃ£o fazer logo. Sem nomear regra. Mistura
    # exercÃ­cios sobre o novo padrÃ£o com REVISÃƒO PESADA.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["El Alcalde", "Don Miguel", "MarÃ­a"],
                "story": (
                    "El Alcalde escreveu trÃªs linhas no papel. NÃ£o te olhou enquanto "
                    "escrevia. Quando terminou, deixou a pena e cruzou as mÃ£os sobre "
                    "a mesa.\n\n"
                    "'Bien. Ahora hablamos de condiciones.'"
                ),
                "now": "NegociaÃ§Ã£o difÃ­cil. Cada palavra do grupo conta.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Sin testigos, no hay sello. Sin sello, no hay pase. Sin pase, sales del pueblo.",
                    "translation": "Sem testigos, nÃ£o tem selo. Sem selo, nÃ£o tem pase. Sem pase, vocÃª sai do pueblo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel se levanta. 'Yo te ayudo' â€” fala pra vocÃª firme. O cumprimento que vocÃª devolve Ã  Don Miguel:",
                    "options": [
                        {"id": "a", "text": "Gracias, Don Miguel"},
                        {"id": "b", "text": "AdiÃ³s Miguel"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Estoy"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. No te dejo solo en esto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Voy a buscar a doÃ±a Carmen ahora mismo. Y a Eduardo el herrero.",
                    "translation": "Vou buscar dona Carmen agora mesmo. E Eduardo o ferreiro.",
                },
                {
                    "kind": "player",
                    "text": "SofÃ­a disse 'voy a buscar'. VocÃª nunca ouviu esse jeito antes â€” mas entende: ela vai fazer algo logo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a disse 'voy a buscar'. Ela estÃ¡ falando:",
                    "options": [
                        {"id": "a", "text": "Do que vai fazer logo"},
                        {"id": "b", "text": "Do que jÃ¡ fez ontem"},
                        {"id": "c", "text": "De quem ela Ã©"},
                        {"id": "d", "text": "De onde ela estÃ¡"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a buscar", "native": "vou buscar",
                    "npc_reaction": "Eso. 'Voy a' es para algo que sale ahora â€” algo cercano. Tan simple como decir 'vou' en portuguÃ©s.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Yo voy a hablar con Eduardo. El forastero viene conmigo â€” Eduardo lo recuerda de la calle.",
                    "translation": "Eu vou falar com Eduardo. O forasteiro vai comigo â€” Eduardo lembra dele da rua.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel acabou de explicar o plano. VocÃª confirma que vai com ele:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy"},
                        {"id": "b", "text": "No tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Bueno. Vamos juntos. Eduardo va a aceptar â€” confÃ­o en eso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Yo me quedo aquÃ­. Voy a hablar con el seÃ±or Alcalde a solas, si me permite.",
                    "translation": "Eu fico aqui. Vou falar com o senhor Alcalde a sÃ³s, se ele permitir.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "SilÃªncio. El Alcalde olha pra MarÃ­a por meio segundo a mais "
                        "do que pra qualquer outra pessoa naquela sala. NÃ£o recusa, "
                        "nÃ£o aceita. Apenas espera."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta pro grupo: 'Â¿Y vosotros â€” los tres juntos â€” quÃ© hacemos?' VocÃª responde sobre o que TODO o grupo vai fazer:",
                    "options": [
                        {"id": "a", "text": "Vamos a buscar testigos"},
                        {"id": "b", "text": "Voy a buscar testigos"},
                        {"id": "c", "text": "Va a buscar testigos"},
                        {"id": "d", "text": "Vas a buscar testigos"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos â€” los tres. Igual que 'vamos' en portuguÃ©s, pero antes de un verbo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Antes de sair, El Alcalde pergunta pro grupo: 'Estos tres dÃ­as â€” Â¿cÃ³mo van a vivir aquÃ­?' VocÃª responde simples â€” o grupo cuida de vocÃª. Resposta com 'estoy':",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Ya veremos cuÃ¡nto duran las cosas buenas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Saindo, Don Miguel olha pro Alcalde e cumprimenta formalmente â€” manhÃ£ ainda. Como ele diz adeus?",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, seÃ±or Alcalde"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "El Alcalde acena apenas com a cabeÃ§a. NÃ£o devolve a saudaÃ§Ã£o.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Saindo do ayuntamiento. Don Miguel para o grupo na escada e explica
    # 'voy a' SEM nomear "futuro prÃ³ximo". Apenas: "isso Ã© o que vocÃª vai
    # fazer logo". Foco em ENTENDER pelo uso. ~3-4 exercÃ­cios apenas.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Miguel", "SofÃ­a"],
                "story": (
                    "VocÃªs saÃ­ram do ayuntamiento. MarÃ­a ficou com o Alcalde â€” "
                    "ainda lÃ¡ dentro. Os outros quatro sentaram na escada de pedra "
                    "do lado de fora. Don Miguel respirou fundo.\n\n"
                    "'Bueno. Tenemos tres dÃ­as. Voy a enseÃ±arles algo simple antes "
                    "de que se separen.'"
                ),
                "now": "Don Miguel explica como cada um pode dizer o que VAI fazer.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Lo que usaron ahÃ­ dentro â€” 'voy a buscar', 'voy a hablar' â€” sirve para decir lo que va a pasar pronto. No hoy ni maÃ±ana, exactamente â€” lo que sale ya.",
                    "translation": "O que vocÃªs usaram lÃ¡ dentro â€” 'voy a buscar', 'voy a hablar' â€” serve para dizer o que vai acontecer logo. NÃ£o hoje nem amanhÃ£, exatamente â€” o que sai jÃ¡.",
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
                    "line": "Cambia con quien lo dice. Si soy yo â€” 'voy'. Si eres tÃº â€” 'vas'. Si es SofÃ­a â€” 'va'. Si somos nosotros â€” 'vamos'.",
                    "translation": "Muda com quem diz. Se sou eu â€” 'voy'. Se Ã© vocÃª â€” 'vas'. Se Ã© SofÃ­a â€” 'va'. Se somos nÃ³s â€” 'vamos'.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo voy ", "isKey": True},
                        {"text": "Â· TÃº vas ", "isKey": True},
                        {"text": "Â· Ella va ", "isKey": True},
                        {"text": "Â· Vamos ", "isKey": True},
                        {"text": "+ a + verbo", "isKey": False},
                    ],
                    "example": "Voy a comer. Vas a hablar. Va a llegar. Vamos a salir.",
                    "translation": "Vou comer. Vais falar. Vai chegar. Vamos sair.",
                    "note": "ya conoces 'voy, vas, va, vamos' (de F6 y F10). Ahora junto con 'a' + outro verbo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a estÃ¡ prestes a sair pra buscar Carmen. Pra dizer o que ela vai fazer agora:",
                    "options": [
                        {"id": "a", "text": "Voy a buscar a Carmen"},
                        {"id": "b", "text": "Vas a buscar a Carmen"},
                        {"id": "c", "text": "Va a buscar a Carmen"},
                        {"id": "d", "text": "Vamos a buscar"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a", "native": "vou (algo logo)",
                    "npc_reaction": "Yo â€” voy. Lo dice cuando salgo yo misma.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel pergunta pra vocÃª: 'Forastero â€” tÃº ___ con mi padre, Â¿no?' Pra dizer o que vocÃª vai fazer (vem com Don Miguel):",
                    "options": [
                        {"id": "a", "text": "vas a venir"},
                        {"id": "b", "text": "voy a venir"},
                        {"id": "c", "text": "va a venir"},
                        {"id": "d", "text": "vamos a venir"},
                    ],
                    "correct": "a",
                    "word_id": "es_vas_a", "target": "vas a", "native": "vais",
                    "npc_reaction": "TÃº â€” vas. Cuando le hablas a alguien.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pergunta pro grupo: 'Y nosotros â€” los tres â€” Â¿quÃ© ___ a hacer juntos?' (todos vÃ£o sair em direÃ§Ãµes diferentes mas juntos no plano):",
                    "options": [
                        {"id": "a", "text": "vamos"},
                        {"id": "b", "text": "voy"},
                        {"id": "c", "text": "vas"},
                        {"id": "d", "text": "va"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Nosotros â€” vamos. Cuando es el grupo entero.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Conversa do grupo sentados na escada. Cada um diz o que vai fazer.
    # SofÃ­a sai correndo. Miguel decide vir junto com vocÃª e Don Miguel.
    # Foco em USAR o novo + revisÃ£o pesada de F1-F10.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Miguel", "SofÃ­a"],
                "story": (
                    "Don Miguel acabou a pequena explicaÃ§Ã£o. SofÃ­a jÃ¡ estava de "
                    "pÃ©, ansiosa pra ir buscar Carmen. Miguel se levantou junto.\n\n"
                    "'Bueno. Â¿QuiÃ©n va a hacer quÃ©? Lo decimos en voz alta para "
                    "no olvidar.'"
                ),
                "now": "Cada um diz o que vai fazer. VocÃª acompanha.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Yo voy a buscar a Carmen ahora. Ella estaba bordando en la plaza esta maÃ±ana â€” sigue ahÃ­.",
                    "translation": "Eu vou buscar Carmen agora. Ela tava bordando na plaza essa manhÃ£ â€” continua lÃ¡.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª concorda com o plano de SofÃ­a. Quer dizer pra ela 'tÃ¡ bom, vai':",
                    "options": [
                        {"id": "a", "text": "Vale, sÃ­"},
                        {"id": "b", "text": "No, mal"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_vale", "target": "vale", "native": "tÃ¡ bom",
                    "npc_reaction": "Vale. Palabra corta del pueblo â€” sirve para todo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Forastero â€” tÃº y yo vamos a la herrerÃ­a. Eduardo te conoce. Si lo saludas bien, va a aceptar.",
                    "translation": "Forasteiro â€” vocÃª e eu vamos Ã  ferraria. Eduardo te conhece. Se vocÃª cumprimentar bem, ele vai aceitar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'vamos a la herrerÃ­a'. Pra quem ele se refere?",
                    "options": [
                        {"id": "a", "text": "Pra ele e pro forastero (nÃ³s dois)"},
                        {"id": "b", "text": "SÃ³ pra SofÃ­a"},
                        {"id": "c", "text": "Pra MarÃ­a sozinha"},
                        {"id": "d", "text": "Pro pueblo todo"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos", "native": "vamos (nÃ³s)",
                    "npc_reaction": "TÃº y yo. Eso es 'nosotros'. Mismo grupo de F10 cuando fuimos a la posada.",
                },
                {
                    "kind": "narrative",
                    "text": "SofÃ­a jÃ¡ saiu correndo pela rua. Miguel olhou pra dentro do ayuntamiento â€” MarÃ­a ainda lÃ¡ com o Alcalde.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Â¿Y MarÃ­a? EstÃ¡ adentro hace ya bastante. Â¿EstÃ¡ bien?",
                    "translation": "E MarÃ­a? TÃ¡ dentro faz tempo. TÃ¡ bem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel responde calmo: 'MarÃ­a sabe lo que hace'. Como Miguel devolve o agradecimento da Don Miguel pela calma?",
                    "options": [
                        {"id": "a", "text": "Gracias, papÃ¡"},
                        {"id": "b", "text": "AdiÃ³s papÃ¡"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, mijo. Vamos â€” el dÃ­a va a ser largo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero â€” Â¿estÃ¡s bien con todo esto? El Alcalde, los testigos, los tres dÃ­as.",
                    "translation": "Forasteiro â€” vocÃª tÃ¡ bem com tudo isso? O Alcalde, os testigos, os trÃªs dias.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Honesto â€” vocÃª tÃ¡ nervoso, mas o grupo tÃ¡ junto:",
                    "options": [
                        {"id": "a", "text": "Estoy bien, pero tengo miedo"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Estado bien, sensaciÃ³n miedo. Las dos cosas a la vez â€” eso es ser humano.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel + protagonista caminham atÃ© a ferraria. Eduardo recebe.
    # Conversa difÃ­cil â€” Eduardo aceita com condiÃ§Ã£o estranha (ver MarÃ­a).
    # Gate: errar trava. Closing prepara F12.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Eduardo"],
                "story": (
                    "VocÃªs caminharam trÃªs quadras atÃ© a herrerÃ­a de Eduardo. "
                    "FumaÃ§a do carvÃ£o saindo da chaminÃ©. Som de martelo no metal. "
                    "Eduardo trabalhava com as costas voltadas.\n\n"
                    "Don Miguel: 'Hablo yo primero. Cuando te pregunte, hablas tÃº.'"
                ),
                "now": "Convencer Eduardo. Errar trava.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸ”¨ HerrerÃ­a Â· Fogo aceso Â· Eduardo trabalhando com martelo",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Eduardo. Buenos dÃ­as.",
                    "translation": "Eduardo. Bom dia.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Don Miguel. Joven forastero. Â¿QuÃ© los trae a mi taller temprano?",
                    "translation": "Don Miguel. Jovem forasteiro. O que traz vocÃªs na minha oficina cedo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo cumprimentou â€” formal mas amistoso. VocÃª cumprimenta de volta, sol da manhÃ£:",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, seÃ±or Eduardo"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. Te recuerdo del segundo dÃ­a â€” cuando SofÃ­a te enseÃ±aba los vecinos.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Eduardo â€” necesitamos algo. El Alcalde pide testigos para el pase del forastero. Pensamos en ti.",
                    "translation": "Eduardo â€” a gente precisa de algo. O Alcalde pede testigos pro pase do forasteiro. Pensamos em ti.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Espera â€” antes que hables. Â¿CuÃ¡ntos aÃ±os tienes tÃº, joven?",
                    "translation": "Espera â€” antes de vocÃª falar. Quantos anos vocÃª tem, jovem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Resposta exata â€” vinte:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Estoy veinte"},
                        {"id": "d", "text": "Me llamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Igual que mi hijo mayor. EstÃ¡ en la otra ciudad.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Eduardo coloca o martelo na bigorna. Limpa as mÃ£os no avental. "
                        "Olha pra vocÃª diferente â€” sem desconfianÃ§a, sem amizade. "
                        "Avaliando."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Bueno. Voy a testificar. Pero tengo una condiciÃ³n.",
                    "translation": "Bom. Vou testemunhar. Mas tenho uma condiÃ§Ã£o.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo acabou de aceitar. VocÃª agradece formal:",
                    "options": [
                        {"id": "a", "text": "Gracias, seÃ±or Eduardo"},
                        {"id": "b", "text": "AdiÃ³s Eduardo"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Pero escucha la condiciÃ³n â€” ahora.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Voy a testificar â€” pero el dÃ­a que vayamos al ayuntamiento, ustedes van a llevarme con MarÃ­a. Ella tiene que ver una cosa que tengo en la espalda.",
                    "translation": "Vou testemunhar â€” mas no dia que formos ao ayuntamiento, vocÃªs vÃ£o me levar atÃ© MarÃ­a. Ela tem que ver uma coisa que tenho nas costas.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "VocÃª nÃ£o entende o pedido. Don Miguel nÃ£o pergunta â€” apenas aceita. "
                        "Eduardo tem algo que precisa que MarÃ­a veja. NÃ£o Ã© hora de "
                        "perguntar por quÃª."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aceita pelo grupo. 'Bueno. Nosotros ___ a llevarte con MarÃ­a.' Quando Ã© o grupo inteiro, qual forma usar?",
                    "options": [
                        {"id": "a", "text": "vamos"},
                        {"id": "b", "text": "voy"},
                        {"id": "c", "text": "van"},
                        {"id": "d", "text": "vas"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Nosotros â€” vamos. Trato hecho, Eduardo.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F12 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸŒ… Saindo da herrerÃ­a Â· Sol jÃ¡ alto Â· Don Miguel e vocÃª caminhando de volta",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Uno conseguido. Carmen ya estÃ¡ con SofÃ­a. Falta uno mÃ¡s â€” alguien imparcial.",
                    "translation": "Um conseguido. Carmen jÃ¡ tÃ¡ com SofÃ­a. Falta mais um â€” alguÃ©m imparcial.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs passam pela esquina do mercado. El Vigilante encostado "
                        "numa parede do outro lado da rua â€” fingindo conversar com "
                        "outro homem. Mas vocÃª sabe que ele te viu.\n\n"
                        "Don Miguel tambÃ©m viu. NÃ£o comentou."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
