"""
Seed das 6 seÃ§Ãµes da Fase 20 Espanhol A1 â€” "La visita inesperada".

ContinuaÃ§Ã£o direta da F19. Os 3 jovens se separaram pra buscar o hombre
extranjero. VocÃª vai Ã  padaria de Rosa. SofÃ­a Ã  plaza. Miguel Ã  herrerÃ­a.

VocÃª encontra o hombre primeiro. Rosa o aponta â€” estÃ¡ na esquina,
falando com um vendedor. VocÃª observa de longe. Roupa de fora.
Documento na mÃ£o. Sotaque do distrito.

SofÃ­a e Miguel chegam. Os 3 seguem ele de longe. Ele encontra MarÃ­a
na plaza. Trocam papÃ©is. Conversa de 10 minutos. Ele sai antes do
meio-dia.

Ã€ noite, MarÃ­a volta calorosa. 'Hoy fue tranquilo, Â¿no?' NinguÃ©m
responde direto.

VOCAB NOVO (3): visita Â· llegar Â· esperar
LINGUAGEM NOVA: tener que + verbo (obrigaÃ§Ã£o)
    tengo que decir / tienes que entender / tenemos que confrontarla

RevisÃ£o F1-F19:
  Â· puedo + verbo (F18)
  Â· quiero + verbo (F16)
  Â· ya / todavÃ­a no (F17)
  Â· vi/hablÃ©/oÃ­ (F12)
  Â· mi/tu/su (F13)
  Â· el/la (F14)

NPC principais: El Inspector (1Âª apariÃ§Ã£o) Â· os 4 Â· Rosa Â· Carmen
Arco emocional: caÃ§a â†’ confronto silencioso â†’ frustraÃ§Ã£o crescente
TransiÃ§Ã£o: F21 abre com decisÃ£o difÃ­cil â€” confrontar MarÃ­a diretamente.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f20_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # VocÃª chega Ã  padaria de Rosa. Pergunta dele. Rosa aponta. 2 novos
    # exer + 3 revisÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸž Padaria de Rosa Â· ManhÃ£ alta Â· Cheiro de pÃ£o fresco\n\n"
                        "VocÃª chegou correndo. Rosa estava na porta â€” farinha "
                        "nas mÃ£os, pÃ£o recÃ©m saÃ­do do forno. Te viu chegar e "
                        "fez sinal pra entrar."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Â¡Joven! Â¿PasÃ³ algo? EstÃ¡s corriendo.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "VocÃª ofegando. Tem que falar baixo â€” outras pessoas no balcÃ£o. SofÃ­a te avisou: discriÃ§Ã£o.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Ven detrÃ¡s. AquÃ­ no.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Rosa te leva pra trÃ¡s do balcÃ£o. Cozinha pequena, fogo aceso. VocÃª senta no banco.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Dime. Sin susto.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "visita",  "native": "visita"},
                        {"target": "llegar",  "native": "chegar"},
                        {"target": "esperar", "native": "esperar"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "VocÃª cumprimenta Rosa â€” manhÃ£ ainda:",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, Rosa"},
                        {"id": "b", "text": "Buenas tardes"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. Habla â€” Â¿quÃ© pasa?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "VocÃª pergunta direto â€” 'Rosa, hÃ¡ um homem novo no pueblo. VocÃª o viu?' (algo que jÃ¡ aconteceu):",
                    "options": [
                        {"id": "a", "text": "Â¿Lo viste?"},
                        {"id": "b", "text": "Â¿Lo ves?"},
                        {"id": "c", "text": "Â¿Vas a verlo?"},
                        {"id": "d", "text": "Â¿Soy?"},
                    ],
                    "correct": "a",
                    "word_id": "es_viste", "target": "viste", "native": "viste",
                    "npc_reaction": "Lo vi. Acaba de pasar â€” fue al mercado. Hombre alto, joven, ropa de fuera.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Vino esta maÃ±ana â€” temprano. LlegÃ³ al pueblo en burro. Y ahora espera en la esquina del mercado â€” junto a la fuente.",
                    "translation": "Veio essa manhÃ£ â€” cedo. Chegou ao pueblo em burro. E agora espera na esquina do mercado â€” perto da fonte.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa disse 'llegÃ³ al pueblo en burro'. A palavra 'llegÃ³' significa que o homem:",
                    "options": [
                        {"id": "a", "text": "Chegou (jÃ¡ aconteceu)"},
                        {"id": "b", "text": "Chega (todo dia)"},
                        {"id": "c", "text": "Vai chegar"},
                        {"id": "d", "text": "Ã‰ chegada"},
                    ],
                    "correct": "a",
                    "word_id": "es_llego", "target": "llegÃ³", "native": "chegou",
                    "npc_reaction": "LlegÃ³. Esta maÃ±ana. Como tÃº llegaste hace dos semanas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "E Rosa disse 'espera en la esquina'. A palavra 'espera' significa que o homem:",
                    "options": [
                        {"id": "a", "text": "Espera (estÃ¡ parado, sem se mexer)"},
                        {"id": "b", "text": "Sai correndo"},
                        {"id": "c", "text": "JÃ¡ foi"},
                        {"id": "d", "text": "Quer ir"},
                    ],
                    "correct": "a",
                    "word_id": "es_espera", "target": "espera", "native": "espera",
                    "npc_reaction": "Espera. EstÃ¡ quieto â€” quizÃ¡ espera a alguien. Pero esa quietud no es de paseo.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # 100% revisÃ£o. VocÃª sai. Encontra SofÃ­a na plaza. Os 2 vÃ£o atrÃ¡s do
    # homem. Miguel chega. Os 3 observam de longe. F1-F19 puro.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Miguel"],
                "story": (
                    "VocÃª saiu da padaria. SofÃ­a jÃ¡ estava na esquina perto da "
                    "iglesia â€” ela tinha visto o homem de longe. Miguel chegou "
                    "uns segundos depois.\n\n"
                    "'EstÃ¡ allÃ¡ â€” el de la chaqueta marrÃ³n. Junto a la fuente.'"
                ),
                "now": "Os 3 observam de longe. Conversa baixa.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ³ Sombra dos arcos da iglesia Â· Os 3 escondidos Â· Um homem alto, jovem, junto Ã  fonte",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” Rosa te dijo que llegÃ³ esta maÃ±ana, Â¿verdad?",
                    "translation": "Forasteiro â€” Rosa te disse que ele chegou essa manhÃ£, nÃ©?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "VocÃª confirma â€” Rosa te disse:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me lo dijo Rosa"},
                        {"id": "b", "text": "SÃ­, me lo dice"},
                        {"id": "c", "text": "Voy a decir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_dijo", "target": "me lo dijo", "native": "me disse",
                    "npc_reaction": "Me lo dijo. Tercera persona pasado. Bien usado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a descreve o homem. Olha de longe. Alto e magro, jovem (uns 35 anos). Pra confirmar â€” vocÃª vÃª tambÃ©m:",
                    "options": [
                        {"id": "a", "text": "SÃ­, lo veo â€” es alto y delgado"},
                        {"id": "b", "text": "SÃ­, lo vi"},
                        {"id": "c", "text": "Voy a verlo"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_alto", "target": "alto", "native": "alto",
                    "npc_reaction": "Alto y delgado. Bien observado. Joven tambiÃ©n â€” quizÃ¡ treinta y cinco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'Â¿CÃ³mo estÃ¡s? Â¿Listo para seguirlo?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien, listo"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Sin acercarnos demasiado.",
                },
                {
                    "kind": "narrative",
                    "text": "O homem se mexe. Tira algo do bolso â€” papel dobrado. LÃª. Olha pra rua. Espera.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "EstÃ¡ esperando a alguien. Y tiene un papel â€” quizÃ¡ una lista de nombres.",
                    "translation": "EstÃ¡ esperando alguÃ©m. E tem um papel â€” talvez uma lista de nomes.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "VocÃª pergunta pra SofÃ­a â€” 'quem ele espera?'. SofÃ­a: 'no sÃ©. Pero quien sea â€” viene del distrito.' Pra vocÃª confirmar o que sabe (puedo + saber):",
                    "options": [
                        {"id": "a", "text": "TodavÃ­a no sÃ©"},
                        {"id": "b", "text": "Ya sÃ©"},
                        {"id": "c", "text": "Voy a saber"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavÃ­a no sÃ©", "native": "ainda nÃ£o sei",
                    "npc_reaction": "TodavÃ­a no. Pero pronto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Â¿Y si lo seguimos hasta que se encuentre con quien sea?",
                    "translation": "E se a gente segue ele atÃ© encontrar com quem for?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "VocÃª concorda â€” sim, vamos seguir (algo que sai logo):",
                    "options": [
                        {"id": "a", "text": "SÃ­, vamos a seguirlo"},
                        {"id": "b", "text": "Voy a seguirlo"},
                        {"id": "c", "text": "Va a seguir"},
                        {"id": "d", "text": "Soy seguir"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos. Separados â€” para no llamar la atenciÃ³n.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "VocÃª quer dar uma volta â€” observar Carmen no caminho talvez. SofÃ­a pergunta: 'Â¿adÃ³nde quieres ir tÃº primero?' (quiero + verbo):",
                    "options": [
                        {"id": "a", "text": "Quiero ver a Carmen"},
                        {"id": "b", "text": "Voy a Carmen"},
                        {"id": "c", "text": "Soy a Carmen"},
                        {"id": "d", "text": "Tengo Carmen"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero ver", "native": "quero ver",
                    "npc_reaction": "Bien â€” Carmen puede tener mÃ¡s informaciÃ³n. Vete tÃº. Nosotros seguimos al hombre.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # VocÃª vai Ã  plaza onde Carmen estÃ¡. Carmen confirma â€” o homem Ã© primo do
    # Alcalde, conhecido como Inspector del Distrito. Vem fazer "auditorias".
    # ApresentaÃ§Ã£o de "tener que + verbo" pelo uso natural.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Carmen"],
                "story": (
                    "VocÃª foi Ã  plaza pelo lado oposto â€” pra nÃ£o passar pelo "
                    "homem da fonte. Carmen tava no banco dela, bordando. "
                    "Como sempre.\n\n"
                    "Ela te viu chegar â€” leu a sua cara. PÃ´s o bordado de lado."
                ),
                "now": "Carmen confirma quem Ã© o homem. ApresentaÃ§Ã£o de 'tener que'.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Forastero â€” algo pasÃ³. Lo veo en tu cara.",
                    "translation": "Forasteiro â€” algo aconteceu. Vejo na tua cara.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "VocÃª cumprimenta e vai direto ao ponto:",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, Carmen. Necesito preguntarte algo"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "AdiÃ³s Carmen"},
                        {"id": "d", "text": "Estoy mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. Habla â€” Â¿quÃ© pasa?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Antes que digas â€” sÃ© quÃ© quieres preguntarme. El hombre del mercado. Lo conozco.",
                    "translation": "Antes que vocÃª diga â€” sei o que vai me perguntar. O homem do mercado. ConheÃ§o.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'lo conozco'. VocÃª responde â€” 'quem Ã© ele?':",
                    "options": [
                        {"id": "a", "text": "Â¿QuiÃ©n es?"},
                        {"id": "b", "text": "Â¿CÃ³mo es?"},
                        {"id": "c", "text": "Â¿DÃ³nde estÃ¡s?"},
                        {"id": "d", "text": "Â¿Soy?"},
                    ],
                    "correct": "a",
                    "word_id": "es_quien", "target": "Â¿quiÃ©n es?", "native": "quem Ã©?",
                    "npc_reaction": "Â¿QuiÃ©n es? Es el primo del Alcalde. Vino del distrito hace muchos aÃ±os â€” y ahora viene de tanto en tanto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Es conocido como El Inspector. Su trabajo es controlar lo que pasa en los pueblos pequeÃ±os. Si hay forasteros sin pase, si hay sangres mezcladas, si hay 'cosas raras'.",
                    "translation": "Ã‰ conhecido como El Inspector. O trabalho dele Ã© controlar o que se passa nos pueblos pequenos. Se hÃ¡ forasteiros sem pase, se hÃ¡ sangues misturados, se hÃ¡ 'coisas estranhas'.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "VocÃª processa. Pra dizer 'entÃ£o el Alcalde lo llamÃ³' (jÃ¡ passou):",
                    "options": [
                        {"id": "a", "text": "Entonces el Alcalde lo llamÃ³"},
                        {"id": "b", "text": "Entonces el Alcalde lo llama"},
                        {"id": "c", "text": "Va a llamarlo"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_llamo", "target": "llamÃ³", "native": "chamou (ele)",
                    "npc_reaction": "LlamÃ³. QuizÃ¡. O quizÃ¡ vino solo â€” esa familia siempre se ayuda entre sÃ­.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Tienes que hacer una cosa, joven. Tienes que avisarle a Don Miguel. Hoy mismo â€” antes que se vaya el Inspector.",
                    "translation": "VocÃª tem que fazer uma coisa, jovem. Tem que avisar Don Miguel. Hoje mesmo â€” antes que o Inspector vÃ¡ embora.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'tienes que avisarle'. A palavrinha 'tienes que' significa:",
                    "options": [
                        {"id": "a", "text": "Tens que / precisa (obrigaÃ§Ã£o)"},
                        {"id": "b", "text": "Podes (se quiser)"},
                        {"id": "c", "text": "Vais"},
                        {"id": "d", "text": "Ã‰s"},
                    ],
                    "correct": "a",
                    "word_id": "es_tienes_que", "target": "tienes que", "native": "tens que",
                    "npc_reaction": "Tienes que. Es obligaciÃ³n â€” no opciÃ³n. La diferencia con 'puedes' es importante.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Yo tengo que quedarme aquÃ­ â€” si me ve, va a sospechar mÃ¡s. Pero tÃº tienes que correr.",
                    "translation": "Eu tenho que ficar aqui â€” se me vir, vai suspeitar mais. Mas vocÃª tem que correr.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'yo tengo que quedarme'. Pra vocÃª responder â€” sim, vocÃª tem que ir agora:",
                    "options": [
                        {"id": "a", "text": "Tengo que ir ya"},
                        {"id": "b", "text": "Voy a ir"},
                        {"id": "c", "text": "Quiero ir"},
                        {"id": "d", "text": "Soy ir"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_que", "target": "tengo que", "native": "tenho que",
                    "npc_reaction": "Tengo que. SÃ­ â€” obligaciÃ³n. Y tienes que ir solo â€” nadie contigo. MÃ¡s rÃ¡pido.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen pergunta â€” vocÃª consegue correr atÃ© a casa de Don Miguel sem chamar atenÃ§Ã£o? Sim, vocÃª consegue (puedo + verbo):",
                    "options": [
                        {"id": "a", "text": "SÃ­, puedo correr"},
                        {"id": "b", "text": "No puedo"},
                        {"id": "c", "text": "Voy a correr"},
                        {"id": "d", "text": "Soy correr"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo correr", "native": "posso correr",
                    "npc_reaction": "Puedes. Ve por las callejuelas â€” no la calle principal. El Inspector la observa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "VocÃª agradece Carmen â€” formal, sincero:",
                    "options": [
                        {"id": "a", "text": "Gracias, Carmen"},
                        {"id": "b", "text": "AdiÃ³s Carmen"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Tengo gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Ve â€” y cuidate.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Correndo pelas vielas. VocÃª encontra Don Miguel a meio caminho â€” ele jÃ¡
    # tinha visto o Inspector pela janela. Conversa rÃ¡pida onde Don Miguel
    # explica "tener que" formalmente. SEM nomear "verbo modal".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "VocÃª correu pelas vielas. Quase tropeÃ§ou duas vezes. "
                    "Don Miguel estava na esquina â€” esperando vocÃª. JÃ¡ tinha "
                    "saÃ­do de casa.\n\n"
                    "'Ya lo vi por la ventana hace media hora. Espera â€” antes "
                    "de seguir, dime algo.'"
                ),
                "now": "Don Miguel explica 'tener que + verbo' antes de prosseguir.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Carmen te dijo 'tienes que avisar', Â¿verdad?",
                    "translation": "Carmen te disse 'tienes que avisar', nÃ©?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª confirma â€” sim, ela disse:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me lo dijo"},
                        {"id": "b", "text": "No me lo dijo"},
                        {"id": "c", "text": "Voy a decirlo"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_dijo", "target": "me lo dijo", "native": "me disse",
                    "npc_reaction": "Bueno. Antes de seguir â€” quiero que entiendas 'tengo que' bien. Lo vas a usar mucho hoy.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tengo que + verbo",
                    "meaning": "ObrigaÃ§Ã£o â€” vocÃª Ã© forÃ§ado a fazer",
                    "note": "diferente de 'puedo' (posso, se quero) e 'quiero' (quero fazer)",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "'Puedo' es lo que soy capaz. 'Quiero' es lo que deseo. 'Tengo que' es lo que no puedo evitar â€” la situaciÃ³n me obliga.",
                    "translation": "'Puedo' Ã© o que sou capaz. 'Quiero' Ã© o que desejo. 'Tengo que' Ã© o que nÃ£o posso evitar â€” a situaÃ§Ã£o me obriga.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo tengo que ",     "isKey": True},
                        {"text": "ir Â· ",             "isKey": False},
                        {"text": "TÃº tienes que ",    "isKey": True},
                        {"text": "saber Â· ",          "isKey": False},
                        {"text": "Ella tiene que ",   "isKey": True},
                        {"text": "callar Â· ",         "isKey": False},
                        {"text": "Tenemos que ",      "isKey": True},
                        {"text": "decidir",           "isKey": False},
                    ],
                    "example": "Tengo que ir. Tienes que saber esto. Carmen tiene que quedarse. Tenemos que decidir.",
                    "translation": "Tenho que ir. VocÃª tem que saber isso. Carmen tem que ficar. Temos que decidir.",
                    "note": "tengo / tienes / tiene / tenemos + 'que' + outro verbo. La obligaciÃ³n.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª nÃ£o tem escolha â€” precisa avisar todos. Pra dizer 'tengo que avisar' (obrigaÃ§Ã£o):",
                    "options": [
                        {"id": "a", "text": "Tengo que avisar a todos"},
                        {"id": "b", "text": "Puedo avisar"},
                        {"id": "c", "text": "Quiero avisar"},
                        {"id": "d", "text": "Voy a avisar"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_que", "target": "tengo que", "native": "tenho que",
                    "npc_reaction": "Tengo que. La situaciÃ³n te obliga â€” no es algo que decides hacer.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'Y nosotros â€” ___ confrontar a MarÃ­a esta noche.' (obrigaÃ§Ã£o, plural):",
                    "options": [
                        {"id": "a", "text": "tenemos que"},
                        {"id": "b", "text": "podemos"},
                        {"id": "c", "text": "queremos"},
                        {"id": "d", "text": "vamos"},
                    ],
                    "correct": "a",
                    "word_id": "es_tenemos_que", "target": "tenemos que", "native": "temos que",
                    "npc_reaction": "Tenemos que. Sin esperar mÃ¡s. DespuÃ©s que el Inspector se vaya â€” hablamos con ella.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra Carmen â€” alta, magra. Pra descrever a altura dela (mulher):",
                    "options": [
                        {"id": "a", "text": "Es alta"},
                        {"id": "b", "text": "Es alto"},
                        {"id": "c", "text": "Es altos"},
                        {"id": "d", "text": "Es altas"},
                    ],
                    "correct": "a",
                    "word_id": "es_alta", "target": "alta", "native": "alta",
                    "npc_reaction": "Alta. Carmen â€” mujer, alta. Termina en '-a'.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # VocÃª e Don Miguel vÃ£o atÃ© a plaza juntos. SofÃ­a e Miguel jÃ¡ estÃ£o lÃ¡.
    # Os 4 observam de longe â€” MarÃ­a encontra o Inspector. Conversa de 10
    # minutos. Documento trocado. NinguÃ©m escuta. Inspector vai embora.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "SofÃ­a", "Miguel", "El Inspector"],
                "story": (
                    "VocÃªs 2 chegaram Ã  plaza. SofÃ­a e Miguel jÃ¡ tavam escondidos "
                    "na sombra das Ã¡rvores. Os 4 reunidos.\n\n"
                    "'Mira â€” MarÃ­a estÃ¡ llegando ahora.'"
                ),
                "now": "VocÃªs observam o encontro. Cada detalhe importa.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ³ Sombra das Ã¡rvores Â· Os 4 observando Â· MarÃ­a cruzando a plaza",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "MarÃ­a llega â€” y Ã©l la espera. Como si fueran conocidos.",
                    "translation": "MarÃ­a chega â€” e ele a espera. Como se fossem conhecidos.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a disse 'Ã©l la espera'. VocÃª confirma â€” sim, o Inspector estÃ¡ esperando:",
                    "options": [
                        {"id": "a", "text": "SÃ­, la espera"},
                        {"id": "b", "text": "SÃ­, la esperÃ³"},
                        {"id": "c", "text": "Va a esperar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_espera", "target": "la espera", "native": "a espera",
                    "npc_reaction": "Espera. Sin moverse. Esperando algo especÃ­fico.",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a chega perto. NÃ£o troca abraÃ§os. Apenas inclinaÃ§Ã£o de cabeÃ§a â€” como dois conhecidos que nÃ£o querem chamar atenÃ§Ã£o.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Inspector",
                    "line": "MarÃ­a. Has crecido â€” pero te reconozco igual. Â¿CÃ³mo estÃ¡s?",
                    "translation": "MarÃ­a. Cresceste â€” mas te reconheÃ§o igual. Como estÃ¡s?",
                    "is_new_npc": True,
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Estoy bien. Pero todavÃ­a no contesto preguntas oficiales aquÃ­ en la plaza.",
                    "translation": "Estou bem. Mas ainda nÃ£o respondo perguntas oficiais aqui na plaza.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel sussurra: 'Ã‰l la conoce desde antes â€” Â¿oÃ­ste?'",
                    "options": [
                        {"id": "a", "text": "SÃ­, lo oÃ­"},
                        {"id": "b", "text": "No lo oigo"},
                        {"id": "c", "text": "Voy a oÃ­r"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "lo oÃ­", "native": "ouvi",
                    "npc_reaction": "OÃ­ste. Bueno. 'Has crecido' â€” eso es de alguien que la conociÃ³ de niÃ±a.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "O Inspector tira um papel do bolso. Mostra pra MarÃ­a. "
                        "Ela olha. Devolve. Os dois falam mais â€” vocÃªs nÃ£o "
                        "escutam, mas vÃªem MarÃ­a acenar com a cabeÃ§a."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Inspector",
                    "line": "Y el forastero. Â¿Lo tienes controlado?",
                    "translation": "E o forasteiro. Tem ele controlado?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Lo tengo cerca. Eso es suficiente por ahora.",
                    "translation": "Tenho ele perto. Isso Ã© suficiente por agora.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "VocÃª ouviu isso. Claro. Don Miguel tambÃ©m. SofÃ­a e Miguel "
                        "tambÃ©m. 'Lo tengo controlado'. VocÃª Ã© um item no plano "
                        "dela.\n\n"
                        "A frase girou pelo seu peito como o fuego da F5 â€” mas "
                        "fria desta vez."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pousa a mÃ£o no seu ombro. Pergunta baixo: 'Â¿CÃ³mo estÃ¡s?'. Honesto:",
                    "options": [
                        {"id": "a", "text": "Estoy mal"},
                        {"id": "b", "text": "Estoy bien"},
                        {"id": "c", "text": "Soy mal"},
                        {"id": "d", "text": "Voy mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mal", "target": "estoy mal", "native": "estou mal",
                    "npc_reaction": "Lo entiendo, hijo. Esa frase duele. Pero ahora ya no podemos esperar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel diz: 'Esta noche â€” la confrontamos.' VocÃª concorda â€” sim, temos que (obrigaÃ§Ã£o):",
                    "options": [
                        {"id": "a", "text": "SÃ­, tenemos que"},
                        {"id": "b", "text": "SÃ­, podemos"},
                        {"id": "c", "text": "SÃ­, queremos"},
                        {"id": "d", "text": "Voy a"},
                    ],
                    "correct": "a",
                    "word_id": "es_tenemos_que", "target": "tenemos que", "native": "temos que",
                    "npc_reaction": "Tenemos que. Sin mÃ¡s esperas.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Noite. MarÃ­a volta calorosa. VocÃªs fingem normalidade. Don Miguel decide
    # que vÃ£o confrontar amanhÃ£ ao amanhecer. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "Don Miguel"],
                "story": (
                    "O Inspector saiu do pueblo antes do meio-dia â€” pela mesma "
                    "estrada por onde entrou. MarÃ­a voltou pra casa de Don Miguel "
                    "Ã  tarde, como se nada tivesse acontecido.\n\n"
                    "Ã€ noite, jantar tranquilo. MarÃ­a serviu â€” calorosa, "
                    "sorridente. 'Hoy fue tranquilo, Â¿no?'"
                ),
                "now": "VocÃªs precisam fingir normalidade. Ãšltima noite antes do confronto.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸ² Mesa do jantar Â· MarÃ­a servindo Â· Os 4 sentados Â· Lamparina baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Forastero â€” Â¿cÃ³mo estuvo tu dÃ­a? Saliste mucho.",
                    "translation": "Forasteiro â€” como foi seu dia? VocÃª saiu muito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Mentira parcial â€” vocÃª passou na padaria, depois na plaza, foi cansativo:",
                    "options": [
                        {"id": "a", "text": "Estuve cansado, pero bien"},
                        {"id": "b", "text": "Estoy bien sin cansancio"},
                        {"id": "c", "text": "Soy bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estuve", "target": "estuve cansado", "native": "estive cansado",
                    "npc_reaction": "Estuviste cansado. MaÃ±ana descansas un poco mÃ¡s.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "SofÃ­a â€” Â¿y tÃº? Pareces preocupada.",
                    "translation": "SofÃ­a â€” e vocÃª? Pareces preocupada.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Tengo dolor de cabeza. Pero ya se me pasa.",
                    "translation": "Tenho dor de cabeÃ§a. Mas jÃ¡ me passa.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a oferece infusÃ£o. Pra dizer pra ela 'no, gracias' simples:",
                    "options": [
                        {"id": "a", "text": "No, gracias"},
                        {"id": "b", "text": "SÃ­, mucha"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Voy infusiÃ³n"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_gracias", "target": "no, gracias", "native": "nÃ£o, obrigado",
                    "npc_reaction": "Como querÃ¡is.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "MarÃ­a â€” hoy fue tranquilo, como dijiste. MaÃ±ana â€” quizÃ¡ no tan tranquilo. Tendremos que hablar.",
                    "translation": "MarÃ­a â€” hoje foi tranquilo, como disse. AmanhÃ£ â€” talvez nÃ£o tÃ£o tranquilo. Teremos que falar.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "MarÃ­a olha pra Don Miguel. Sem disfarÃ§ar. NÃ£o pergunta "
                        "o que ele quer dizer. Apenas acena de leve. Como quem "
                        "esperava esse momento."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "MaÃ±ana entonces. Yo tambiÃ©n tengo que decirles cosas.",
                    "translation": "AmanhÃ£ entÃ£o. Eu tambÃ©m tenho que dizer coisas a vocÃªs.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a disse 'tengo que decirles cosas'. Pra vocÃª confirmar pra Don Miguel â€” entendeu. NÃ£o responde MarÃ­a agora, sÃ³ Don Miguel:",
                    "options": [
                        {"id": "a", "text": "SÃ­, lo oÃ­"},
                        {"id": "b", "text": "No lo oigo"},
                        {"id": "c", "text": "Voy a oÃ­r"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "lo oÃ­", "native": "ouvi",
                    "npc_reaction": "Bueno. MaÃ±ana entonces â€” todos.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Forastero â€” vete a dormir. MaÃ±ana es dÃ­a largo. Quiero la cabeza fresca.",
                    "translation": "Forasteiro â€” vai dormir. AmanhÃ£ Ã© dia longo. Quero a cabeÃ§a fresca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª se levanta pra ir dormir. Cumprimento de noite:",
                    "options": [
                        {"id": "a", "text": "Buenas noches"},
                        {"id": "b", "text": "Buenos dÃ­as"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                    "npc_reaction": "Buenas noches, hijo. MaÃ±ana â€” hablamos.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F21 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸŒ™ Quarto Â· VocÃª deitado Â· Lamparina apagada",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª ficou deitado. Os olhos abertos. A frase de MarÃ­a "
                        "girando â€” 'lo tengo controlado'.\n\n"
                        "VocÃª lembrou da palavra na carta â€” 'vuelves'. Lembrou "
                        "da marca do Eduardo. Do sussurro de LucÃ­a. Do Alcalde "
                        "frio. Da histÃ³ria de Carmen.\n\n"
                        "Tudo girando como uma engrenagem que finalmente "
                        "comeÃ§ou a fazer sentido.\n\n"
                        "AmanhÃ£ â€” confronto. Pela primeira vez vocÃªs todos juntos. "
                        "Frente a frente com MarÃ­a. E vocÃª ainda nÃ£o sabe se ela "
                        "vai sorrir ou se vai mudar de cara â€” pela primeira vez "
                        "em dez semanas."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Hijo â€” duerme. MaÃ±ana al amanecer, todos despiertos. Y ya no hay vuelta atrÃ¡s.",
                    "translation": "Filho â€” dorme. AmanhÃ£ ao amanhecer, todos acordados. E jÃ¡ nÃ£o hÃ¡ volta atrÃ¡s.",
                    "pace": "slow",
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
