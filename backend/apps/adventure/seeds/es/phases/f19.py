"""
Seed das 6 seÃ§Ãµes da Fase 19 Espanhol A1 â€” "La carta".

âš ï¸ MILESTONE OBRIGATÃ“RIO (canÃ´nico â€” story.md):
    F19 = 4Âª fase de revisÃ£o. A primera palabra da carta torna-se
    legÃ­vel. O protagonista jÃ¡ fala o suficiente.

Don Miguel abre o baÃº. Mostra o envelope selado. Os 4 jovens reunidos
ao amanhecer (MarÃ­a saiu cedo de novo â€” Don Miguel arranjou).

Quase tudo na carta estÃ¡ ilegÃ­vel pro forastero. Mas no centro â€” uma
palavra ficou clara. Escura. Pulsando. VocÃª LÃŠ.

A palavra Ã©: **"Vuelves."** (vocÃª volta)

NÃ£o entende o sentido completo. Mas sabe que isso muda tudo.

ABORDAGEM PEDAGÃ“GICA:
    Fase de REVISÃƒO PESADA. Apresenta apenas vocab narrativo (carta,
    leer, palabra, abrir). Sem nova linguagem gramatical relevante.
    Foco em REVISÃƒO de F1-F18 â€” soy/estoy/tengo, voy a, mi/tu/su,
    el/la, vi/hablÃ©/oÃ­, ya/todavÃ­a no, puedo, quiero.

VOCAB NOVO (3): carta Â· leer Â· abrir
ApresentaÃ§Ã£o adicional: palabra (jÃ¡ conhecido em uso geral)

NPC principais: Don Miguel Â· SofÃ­a Â· Miguel Â· vocÃª
Arco emocional: expectativa â†’ revelaÃ§Ã£o parcial â†’ confusÃ£o â†’ comeÃ§ar a
                aceitar que tem origem e propÃ³sito desconhecidos
TransiÃ§Ã£o: F20 abre com o grupo decidindo o prÃ³ximo passo â€” confrontar
            MarÃ­a ou continuar observando.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f19_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Amanhecer. Os 4 reunidos. Don Miguel abre o baÃº. Cara da carta selada.
    # 2 novos + 2 revisÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ„ Casa de Don Miguel Â· Amanhecer Â· Cozinha\n\n"
                        "Don Miguel arranjou que MarÃ­a fosse ao mercado bem cedo "
                        "â€” pediu coisas que sÃ³ vendem ao amanhecer. MarÃ­a saiu "
                        "Ã s cinco. SofÃ­a e Miguel chegaram Ã s cinco e meia. Os "
                        "quatro sentados em volta do baÃº aberto."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "AquÃ­ estÃ¡. Veinte aÃ±os en este baÃºl.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Ele pega o envelope. Cera vermelha grossa selando. SÃ­mbolo do sol partido â€” igual Ã  marca de Eduardo.",
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "Ese sello â€” es el mismo sÃ­mbolo de la espalda de Eduardo.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "SÃ­. La carta vino del viejo Buscador que llegÃ³ al pueblo hace veinte aÃ±os.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Don Miguel pousa a carta no centro da mesa. NÃ£o abriu ainda. SÃ³ pousou. Quatro olhos fixos nela.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "carta",   "native": "carta / mensagem escrita"},
                        {"target": "leer",    "native": "ler"},
                        {"target": "abrir",   "native": "abrir"},
                        {"target": "palabra", "native": "palavra"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pousou um envelope grosso, fechado com cera. Como se chama essa coisa?",
                    "options": [
                        {"id": "a", "text": "Carta"},
                        {"id": "b", "text": "Marca"},
                        {"id": "c", "text": "Familia"},
                        {"id": "d", "text": "Espalda"},
                    ],
                    "correct": "a",
                    "word_id": "es_carta", "target": "carta", "native": "carta",
                    "npc_reaction": "Carta. Lo que tiene palabras dentro â€” pero todavÃ­a cerrada.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta a Don Miguel â€” 'Â¿La vamos a ___?' Pra dizer 'abrir' (verbo base):",
                    "options": [
                        {"id": "a", "text": "abrir"},
                        {"id": "b", "text": "cerrar"},
                        {"id": "c", "text": "comer"},
                        {"id": "d", "text": "ver"},
                    ],
                    "correct": "a",
                    "word_id": "es_abrir", "target": "abrir", "native": "abrir",
                    "npc_reaction": "Abrir. Vamos a abrirla â€” ahora mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel agradece pela paciÃªncia de vocÃªs. VocÃªs cumprimentam â€” amanhecer:",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, Don Miguel"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. Vamos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pergunta 'forastero â€” Â¿cÃ³mo estÃ¡s ahora?':",
                    "options": [
                        {"id": "a", "text": "Tengo miedo, pero estoy listo"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_miedo", "target": "tengo miedo", "native": "tenho medo",
                    "npc_reaction": "Las dos cosas a la vez â€” eso es lo correcto. Honesto.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # 100% revisÃ£o. Don Miguel pede que cada um diga em voz alta o que sabe
    # â€” pra que todos estejam na mesma pÃ¡gina antes da carta. RevisÃ£o da
    # histÃ³ria atÃ© aqui.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "SofÃ­a", "Miguel"],
                "story": (
                    "Don Miguel pousou a mÃ£o na carta. NÃ£o vai abrir ainda.\n\n"
                    "'Antes de abrir â€” quiero que cada uno diga lo que sabe. Para "
                    "que estemos todos en la misma pÃ¡gina.'"
                ),
                "now": "RevisÃ£o narrativa. Cada um conta o que viu/ouviu/sentiu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Forastero â€” empieza tÃº. Â¿CuÃ¡ndo llegaste al pueblo?",
                    "translation": "Forasteiro â€” comeÃ§a vocÃª. Quando vocÃª chegou ao pueblo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª chegou faz duas semanas. Pra falar simples â€” 'cheguei sem memÃ³ria, sem nome':",
                    "options": [
                        {"id": "a", "text": "LleguÃ© sin memoria"},
                        {"id": "b", "text": "Llego sin memoria"},
                        {"id": "c", "text": "Voy a llegar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_llegue", "target": "lleguÃ©", "native": "cheguei",
                    "npc_reaction": "LleguÃ©. Bueno. Y conociste a Rosa primero â€” y despuÃ©s a mÃ­.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra confirmar â€” vocÃª viu Rosa primeiro:",
                    "options": [
                        {"id": "a", "text": "SÃ­, vi a Rosa primero"},
                        {"id": "b", "text": "SÃ­, veo a Rosa"},
                        {"id": "c", "text": "Voy a ver"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Y la palabra primera que aprendiste fue 'pan'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "SofÃ­a â€” y tÃº. Â¿CuÃ¡ndo lo viste por primera vez?",
                    "translation": "SofÃ­a â€” e vocÃª. Quando o viu pela primeira vez?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Yo lo vi en tu cuarto la noche del fuego. La noche de la primera chispa.",
                    "translation": "Eu o vi no teu quarto na noite do fogo. A noite da primeira chispa.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "SofÃ­a disse 'lo vi'. VocÃª confirma â€” SofÃ­a tambÃ©m viu o fogo:",
                    "options": [
                        {"id": "a", "text": "SÃ­, ella vio el fuego"},
                        {"id": "b", "text": "SÃ­, ella ve el fuego"},
                        {"id": "c", "text": "Va a ver"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vio", "target": "vio", "native": "viu (3Âª)",
                    "npc_reaction": "Vio. Tercera persona. SofÃ­a vio â€” ya pasado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Miguel â€” y tÃº. Â¿Lo conoces desde cuÃ¡ndo?",
                    "translation": "Miguel â€” e vocÃª. Conhece ele desde quando?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Desde el primer dÃ­a. Mi padre me llamÃ³ â€” 'Â¡MIGUEL! Â¡HAY UN FORASTERO!'. Y vine corriendo.",
                    "translation": "Desde o primeiro dia. Meu pai me chamou â€” 'Â¡MIGUEL! Â¡TEM UM FORASTERO!'. E vim correndo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel disse 'mi padre me llamÃ³'. Pra vocÃª responder pra Miguel â€” sim, ele veio correndo (jÃ¡ passou):",
                    "options": [
                        {"id": "a", "text": "SÃ­, viniste corriendo"},
                        {"id": "b", "text": "SÃ­, vienes corriendo"},
                        {"id": "c", "text": "Voy a venir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_viniste", "target": "viniste", "native": "vieste",
                    "npc_reaction": "Viniste. TÃº â€” segunda. Como 'hablaste' o 'viste'. Forma del pasado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y MarÃ­a llegÃ³ al pueblo hace dos meses. Eso nos lo dijo ella misma â€” la noche que cuidÃ³ al forastero.",
                    "translation": "E MarÃ­a chegou ao pueblo faz dois meses. Isso ela mesma nos disse â€” na noite que cuidou do forasteiro.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pergunta: 'Â¿Por quÃ© llegÃ³ al pueblo? Â¿Saben alguien?' Resposta honesta â€” vocÃªs ainda nÃ£o sabem:",
                    "options": [
                        {"id": "a", "text": "TodavÃ­a no sabemos"},
                        {"id": "b", "text": "Ya sabemos"},
                        {"id": "c", "text": "Vamos a saber"},
                        {"id": "d", "text": "Somos"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavÃ­a no", "native": "ainda nÃ£o",
                    "npc_reaction": "TodavÃ­a no. Pero la carta puede ayudarnos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a: 'Â¿CÃ³mo te sientes ahora, forastero â€” antes de abrir la carta?'",
                    "options": [
                        {"id": "a", "text": "Estoy nervioso"},
                        {"id": "b", "text": "Soy nervioso"},
                        {"id": "c", "text": "Tengo nervioso"},
                        {"id": "d", "text": "Voy nervioso"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_nervioso", "target": "estoy nervioso", "native": "estou nervoso",
                    "npc_reaction": "Nervioso. Estado de ahora â€” bien usado. Eso pasa rÃ¡pido cuando ya sabes lo que viene.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel abre a carta. Quebra o selo. Tira o papel. VocÃª lÃª. Quase
    # tudo ilegÃ­vel. Apenas 1 palavra clara: 'Vuelves'. Foco em revisÃ£o de
    # F1-F18 com situaÃ§Ãµes de leitura.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "SofÃ­a", "Miguel"],
                "story": (
                    "Don Miguel pegou a faca pequena que sempre tem na cinta. "
                    "Cortou o selo de cera. Quebrou em dois. Tirou o papel "
                    "amarelado de dentro.\n\n"
                    "'Mira tÃº primero. Solo. DespuÃ©s nosotros.'"
                ),
                "now": "VocÃª lÃª a carta. Quase tudo confuso. Mas uma palavra fica clara.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸ“„ Papel amarelado Â· Tinta velha Â· Algumas linhas borradas Â· VocÃª segurando",
                },
                {
                    "kind": "player",
                    "text": (
                        "VocÃª olha. HÃ¡ linhas escritas â€” mas as letras se misturam, "
                        "se borram quando vocÃª foca. Como se as palavras nÃ£o "
                        "quisessem ser lidas ainda.\n\n"
                        "Exceto uma â€” no centro. Mais escura. Mais grossa.\n\n"
                        "**VUELVES.**"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿Puedes leer algo?",
                    "translation": "VocÃª pode ler algo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pergunta se vocÃª pode ler. Honesto â€” uma palavra sÃ³. Pra dizer 'posso ler una palabra':",
                    "options": [
                        {"id": "a", "text": "Puedo leer una palabra"},
                        {"id": "b", "text": "No puedo leer"},
                        {"id": "c", "text": "Voy a leer"},
                        {"id": "d", "text": "Soy leer"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo leer", "native": "posso ler",
                    "npc_reaction": "Puedo leer. Una palabra es suficiente. Â¿CuÃ¡l?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª fala a palavra em voz alta â€” 'Vuelves'. Como vocÃª descreve isso? Esta palavra significa:",
                    "options": [
                        {"id": "a", "text": "VocÃª volta"},
                        {"id": "b", "text": "Eu vou"},
                        {"id": "c", "text": "Ele come"},
                        {"id": "d", "text": "NÃ³s saÃ­mos"},
                    ],
                    "correct": "a",
                    "word_id": "es_vuelves", "target": "vuelves", "native": "vocÃª volta",
                    "npc_reaction": "Vuelves. TÃº â€” vuelves. Esa es la palabra. Â¿Y te dice algo?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Vuelves. Como si dijera â€” 'tÃº regresas a algÃºn sitio'. Pero â€” Â¿adÃ³nde?",
                    "translation": "Vuelves. Como se dissesse â€” 'vocÃª retorna a algum lugar'. Mas â€” pra onde?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta pra vocÃª â€” vocÃª lembra de algum lugar de antes? Honesto:",
                    "options": [
                        {"id": "a", "text": "TodavÃ­a no me acuerdo"},
                        {"id": "b", "text": "Ya me acuerdo"},
                        {"id": "c", "text": "Voy a acordarme"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "nÃ£o me lembro",
                    "npc_reaction": "TodavÃ­a no. Pero la palabra estÃ¡ ahÃ­ â€” esperando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "El resto â€” Â¿puedes leer? IntÃ©ntalo otra vez.",
                    "translation": "O resto â€” vocÃª pode ler? Tenta outra vez.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª tenta. Quase nada. Resposta honesta â€” ainda nÃ£o:",
                    "options": [
                        {"id": "a", "text": "TodavÃ­a no puedo leer mÃ¡s"},
                        {"id": "b", "text": "Ya puedo leer todo"},
                        {"id": "c", "text": "Voy a leer"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavÃ­a no", "native": "ainda nÃ£o",
                    "npc_reaction": "TodavÃ­a no. La carta se abre solo cuando ya puedes leerla. El Buscador me lo dijo asÃ­.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Cada vez que aprendas mÃ¡s â€” mÃ¡s palabras se van a ver. Eso es lo que Ã©l me dijo hace veinte aÃ±os.",
                    "translation": "Cada vez que vocÃª aprender mais â€” mais palavras vÃ£o ficar visÃ­veis. Isso ele me disse hÃ¡ vinte anos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'Forastero â€” esa palabra â€” vuelves â€” Â¿quÃ© sientes cuando la lees?' Honesto:",
                    "options": [
                        {"id": "a", "text": "Siento algo en el pecho"},
                        {"id": "b", "text": "No siento nada"},
                        {"id": "c", "text": "Voy a sentir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_siento", "target": "siento", "native": "sinto",
                    "npc_reaction": "Sientes. Eso es lo que importa. Tu cuerpo recuerda lo que tu cabeza ya no.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a: 'Â¿CÃ³mo estÃ¡s ahora â€” despuÃ©s de leer eso?'",
                    "options": [
                        {"id": "a", "text": "Estoy mareado, pero bien"},
                        {"id": "b", "text": "Soy mareado"},
                        {"id": "c", "text": "Tengo mareado"},
                        {"id": "d", "text": "Voy mareado"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mareado", "target": "estoy mareado", "native": "estou tonto",
                    "npc_reaction": "Mareado. Es la palabra que abre por dentro. Es normal sentir algo al leerla.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'Voy a guardarla otra vez. Pero â€” Â¿quieres tocarla una vez mÃ¡s antes?'",
                    "options": [
                        {"id": "a", "text": "SÃ­, quiero tocarla"},
                        {"id": "b", "text": "No quiero"},
                        {"id": "c", "text": "Voy a guardarla"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero tocarla", "native": "quero tocÃ¡-la",
                    "npc_reaction": "Bueno. TÃ³cala. Suavemente.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel guarda a carta. Tira do baÃº um livro velho â€” registros do
    # pueblo. Quer mostrar uma coisa pro forastero. ApariÃ§Ã£o de "el/la/los/las"
    # em prÃ¡tica + apresentaÃ§Ã£o suave de quem/lo que (palavras que ligam).
    # ABORDAGEM: revisÃ£o dominante + 1 conceito pequeno.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel guardou a carta no baÃº. Mas tirou um livro velho "
                    "tambÃ©m â€” capa de couro, pÃ¡ginas amareladas. Registros do "
                    "pueblo dos Ãºltimos cinquenta anos.\n\n"
                    "'Antes de que MarÃ­a vuelva â€” voy a enseÃ±arte algo aquÃ­.'"
                ),
                "now": "Don Miguel mostra o registro do pueblo. VocÃª aprende a navegar pelos nomes.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Este libro tiene los nombres de cada persona que pasÃ³ por el pueblo. Las familias. Los visitantes. Los Buscadores que vinieron.",
                    "translation": "Este livro tem os nomes de cada pessoa que passou pelo pueblo. As famÃ­lias. Os visitantes. Os Buscadores que vieram.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'las familias'. As palavras 'el/la/los/las' que vocÃª viu na F14 â€” quando algo Ã© mulher e plural:",
                    "options": [
                        {"id": "a", "text": "las"},
                        {"id": "b", "text": "los"},
                        {"id": "c", "text": "el"},
                        {"id": "d", "text": "la"},
                    ],
                    "correct": "a",
                    "word_id": "es_las", "target": "las", "native": "as (mulheres / muitas)",
                    "npc_reaction": "Las. Muchas familias â€” femenino plural.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "AquÃ­ â€” el viejo Buscador. Su nombre era TomÃ¡s. Igual que mi padre. Vino en 1845 â€” hace veinte aÃ±os.",
                    "translation": "Aqui â€” o velho Buscador. O nome dele era TomÃ¡s. Igual ao meu pai. Veio em 1845 â€” faz vinte anos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra confirmar â€” esse TomÃ¡s VIO algo. Quem era ele?",
                    "options": [
                        {"id": "a", "text": "Era el Buscador"},
                        {"id": "b", "text": "Es el Buscador"},
                        {"id": "c", "text": "Va a ser"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_era", "target": "era", "native": "era",
                    "npc_reaction": "Era. Antes â€” ya pasado. El Buscador.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Quien / Lo que",
                    "meaning": "Palavras que ligam pessoas/coisas a histÃ³rias.",
                    "note": "el hombre QUIEN te dio la carta Â· LO QUE dice la carta es importante",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "El viejo ", "isKey": False},
                        {"text": "QUIEN ",   "isKey": True},
                        {"text": "trajo la carta Â· ", "isKey": False},
                        {"text": "LO QUE ", "isKey": True},
                        {"text": "dijo la carta",     "isKey": False},
                    ],
                    "example": "El viejo quien trajo la carta muriÃ³. Lo que dijo es importante.",
                    "translation": "O velho que trouxe a carta morreu. O que ele disse Ã© importante.",
                    "note": "'quien' = pra pessoas Â· 'lo que' = pra coisas/ideias.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'El viejo ___ trajo la carta era Buscador.' Pra ligar Ã  pessoa (homem):",
                    "options": [
                        {"id": "a", "text": "quien"},
                        {"id": "b", "text": "lo que"},
                        {"id": "c", "text": "el"},
                        {"id": "d", "text": "la"},
                    ],
                    "correct": "a",
                    "word_id": "es_quien", "target": "quien", "native": "que / quem",
                    "npc_reaction": "Quien. Para personas â€” siempre. El que / la que tambiÃ©n sirven.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'___ leÃ­ste hoy es solo el principio.' Pra ligar Ã  coisa (a carta, o que estava nela):",
                    "options": [
                        {"id": "a", "text": "Lo que"},
                        {"id": "b", "text": "Quien"},
                        {"id": "c", "text": "El"},
                        {"id": "d", "text": "La"},
                    ],
                    "correct": "a",
                    "word_id": "es_lo_que", "target": "lo que", "native": "o que",
                    "npc_reaction": "Lo que. Para cosas o ideas. Esa frase entra mucho en la cabeza.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª confirma â€” entende isso ainda parcialmente:",
                    "options": [
                        {"id": "a", "text": "Ya entiendo un poco"},
                        {"id": "b", "text": "TodavÃ­a no entiendo nada"},
                        {"id": "c", "text": "Voy a entender"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "jÃ¡",
                    "npc_reaction": "Ya un poco. Eso es suficiente por hoy.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel guarda tudo. MarÃ­a chega â€” pega vocÃªs 4 reunidos. TensÃ£o.
    # Don Miguel reage rÃ¡pido. Conversa de coversÃ£od. 100% revisÃ£o.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "SofÃ­a", "Miguel", "MarÃ­a"],
                "story": (
                    "Don Miguel jÃ¡ tinha guardado a carta no baÃº. Tinha fechado. "
                    "Coberto com o pano. Quando ouviu os passos de MarÃ­a na rua "
                    "lÃ¡ fora.\n\n"
                    "'SofÃ­a â€” pasa a mi cuarto, finge que estÃ¡s lavando algo. "
                    "Miguel â€” junto al fogÃ³n. Forastero â€” tÃº quÃ©date aquÃ­.'\n\n"
                    "MarÃ­a entrou com a cesta cheia."
                ),
                "now": "Encontro inesperado com MarÃ­a. VocÃªs precisam disfarÃ§ar.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ… Cozinha Â· MarÃ­a entrando com cesta Â· VocÃª, Don Miguel Â· SofÃ­a e Miguel escondidos",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Buenos dÃ­as. Â¿Y los demÃ¡s? Vi luces aquÃ­ desde lejos.",
                    "translation": "Bom dia. E os outros? Vi luzes aqui de longe.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª cumprimenta â€” manhÃ£ clara:",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, MarÃ­a"},
                        {"id": "b", "text": "Buenas tardes"},
                        {"id": "c", "text": "Buenas noches"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. Â¿Don Miguel â€” cÃ³mo amaneciÃ³?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "SofÃ­a y Miguel vinieron temprano. SofÃ­a estÃ¡ lavando ropa en mi cuarto. Miguel arregla el fogÃ³n.",
                    "translation": "SofÃ­a e Miguel vieram cedo. SofÃ­a estÃ¡ lavando roupa no meu quarto. Miguel arruma o fogÃ£o.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a pergunta â€” vocÃª sabe o motivo? Resposta segura (vaga):",
                    "options": [
                        {"id": "a", "text": "QuerÃ­a ayudar a Don Miguel"},
                        {"id": "b", "text": "Voy a ayudar"},
                        {"id": "c", "text": "Soy ayuda"},
                        {"id": "d", "text": "Tengo ayuda"},
                    ],
                    "correct": "a",
                    "word_id": "es_queria", "target": "querÃ­a ayudar", "native": "queria ajudar",
                    "npc_reaction": "QuerÃ­an ayudar. Bueno. Aprovechemos â€” yo traje hierbas, voy a hacer infusiÃ³n.",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a vai pra cozinha. VocÃª nota â€” ela olha pra mesa onde estava o baÃº. O baÃº estÃ¡ coberto, fechado. Ela parece satisfeita com o que vÃª â€” ou pelo menos nÃ£o suspeita.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Forastero â€” Â¿dormiste bien anoche? Te vi pÃ¡lido al despertar.",
                    "translation": "Forasteiro â€” dormiu bem ontem Ã  noite? Te vi pÃ¡lido ao acordar.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª dormiu mal â€” pensando na carta. Mas vai mentir parcialmente â€” diz que estava cansado:",
                    "options": [
                        {"id": "a", "text": "SÃ­, estuve cansado"},
                        {"id": "b", "text": "SÃ­, dormÃ­ bien"},
                        {"id": "c", "text": "Voy a dormir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_estuve", "target": "estuve cansado", "native": "estive cansado",
                    "npc_reaction": "Estuve cansado. Bueno. La infusiÃ³n te va a ayudar hoy.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Don Miguel â€” encontrÃ© algo raro en el mercado esta maÃ±ana. Un hombre extranjero â€” preguntando por nombres.",
                    "translation": "Don Miguel â€” encontrei algo estranho no mercado essa manhÃ£. Um homem estrangeiro â€” perguntando por nomes.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel fica atento. Pergunta â€” 'quÃ© nombres?'. Pra vocÃª processar â€” Don Miguel quer saber o que aconteceu (passado):",
                    "options": [
                        {"id": "a", "text": "Â¿QuÃ© nombres preguntÃ³?"},
                        {"id": "b", "text": "Â¿QuÃ© nombres pregunta?"},
                        {"id": "c", "text": "Va a preguntar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_pregunto", "target": "preguntÃ³", "native": "perguntou",
                    "npc_reaction": "PreguntÃ³. Tercera persona pasado. Don Miguel quiere saber.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "No supe los nombres. Pero el hombre me vio â€” y se fijÃ³ en mÃ­ mÃ¡s de lo que querÃ­a. Por eso volvÃ­ rÃ¡pido.",
                    "translation": "NÃ£o soube os nomes. Mas o homem me viu â€” e me notou mais do que eu queria. Por isso voltei rÃ¡pido.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "MarÃ­a falou isso sem disfarÃ§ar â€” uma pequena admissÃ£o. "
                        "Don Miguel olhou pra vocÃª por um segundo. VocÃª "
                        "entendeu â€” alguÃ©m de fora chegou. E reconhece MarÃ­a."
                    ),
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # MarÃ­a sai pra fazer infusÃ£o na cozinha do fundo. SofÃ­a sai do quarto.
    # Miguel tambÃ©m. ReuniÃ£o rÃ¡pida dos 4. DecisÃ£o: vÃ£o atrÃ¡s desse hombre.
    # Gate: errar trava. Closing prepara F20.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "SofÃ­a", "Miguel"],
                "story": (
                    "MarÃ­a foi pra cozinha do fundo â€” diz que precisa de fogo "
                    "especÃ­fico pra infusÃ£o. VocÃªs 4 reunidos rapidamente na "
                    "cozinha principal. Conversa baixa, urgente.\n\n"
                    "'Hay un hombre nuevo en el pueblo. Buscando nombres. Y "
                    "MarÃ­a lo vio.'"
                ),
                "now": "DecisÃ£o rÃ¡pida. O que fazer com a informaÃ§Ã£o?",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸ•¯ï¸ Cozinha principal Â· MarÃ­a na cozinha do fundo Â· Os 4 conversando baixo",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Â¿OÃ­ste lo que dijo MarÃ­a? Un hombre extranjero â€” pregunta por nombres.",
                    "translation": "Ouviu o que MarÃ­a disse? Um homem estrangeiro â€” pergunta por nomes.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "VocÃª confirma â€” ouviu sim:",
                    "options": [
                        {"id": "a", "text": "SÃ­, oÃ­ lo que dijo"},
                        {"id": "b", "text": "No oÃ­ nada"},
                        {"id": "c", "text": "Voy a oÃ­r"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                    "npc_reaction": "OÃ­ste. Bueno. Esto cambia las cosas.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Podemos buscarlo antes de que se vaya. Â¿Vamos a la plaza ahora mismo?",
                    "translation": "Podemos procurÃ¡-lo antes que ele vÃ¡ embora. Vamos pra plaza agora mesmo?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Pra vocÃª concordar â€” vamos juntos (algo que sai logo):",
                    "options": [
                        {"id": "a", "text": "SÃ­, vamos a buscarlo"},
                        {"id": "b", "text": "Voy a buscarlo"},
                        {"id": "c", "text": "Va a buscarlo"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos a buscarlo. Pero Â¿cÃ³mo lo encontramos sin que MarÃ­a sospeche?",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Yo me quedo aquÃ­ â€” con MarÃ­a. Ustedes tres salen â€” SofÃ­a a la plaza, Miguel a la herrerÃ­a, el forastero a la padaria. Buscan al hombre.",
                    "translation": "Eu fico aqui â€” com MarÃ­a. VocÃªs trÃªs saem â€” SofÃ­a Ã  plaza, Miguel Ã  ferraria, o forasteiro Ã  padaria. Procuram o homem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra vocÃª confirmar â€” pode ir Ã  padaria sozinho? Sim, pode:",
                    "options": [
                        {"id": "a", "text": "SÃ­, puedo ir solo"},
                        {"id": "b", "text": "No puedo"},
                        {"id": "c", "text": "Voy a ir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedes. Rosa te conoce â€” pregÃºntale si vio al hombre. Discreto.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Si lo encuentras â€” fÃ­jate cÃ³mo es. Alto, bajo, joven, viejo. Y de dÃ³nde viene.",
                    "translation": "Se vocÃª encontrar â€” repara como ele Ã©. Alto, baixo, jovem, velho. E de onde vem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pediu pra vocÃª reparar. VocÃª confirma â€” vai prestar atenÃ§Ã£o:",
                    "options": [
                        {"id": "a", "text": "SÃ­, voy a observarlo"},
                        {"id": "b", "text": "No voy"},
                        {"id": "c", "text": "Soy observar"},
                        {"id": "d", "text": "Estoy observar"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a observarlo", "native": "vou observÃ¡-lo",
                    "npc_reaction": "Bien. Y volvemos aquÃ­ a las dos de la tarde. MarÃ­a se distrae a esa hora â€” siempre.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F20 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸƒ Saindo da cozinha Â· Cada um pra sua direÃ§Ã£o Â· Sol jÃ¡ alto",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs 4 se separaram em silÃªncio. SofÃ­a pra plaza. "
                        "Miguel pra herrerÃ­a. VocÃª pra padaria de Rosa.\n\n"
                        "Don Miguel ficou na cozinha â€” MarÃ­a fazendo infusÃ£o. "
                        "Como se fosse uma manhÃ£ normal. Mas dentro do peito de "
                        "todos vocÃªs, uma palavra pulsava â€” 'vuelves'. E uma "
                        "pergunta â€” 'quiÃ©n es ese hombre?'"
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
