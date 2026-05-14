"""
Seed das 6 seÃ§Ãµes da Fase 7 Espanhol A1 â€” "El dÃ­a normal".

Fase de respiraÃ§Ã£o â€” falsa normalidade. Depois da noite do dom (F5) e da
entrada da SofÃ­a (F6), o grupo decide passar um dia inteiro como se nada
tivesse acontecido. SofÃ­a aparece na plaza como amiga de anos. Miguel
leva o grupo a Carmen pra aprender a 'viver como gente daqui'. Carmen
ensina perguntar idade.

No final da fase: febre. SofÃ­a sussurra sobre a 'dor de cabeÃ§a da primeira
vez'. O dom tem custo fÃ­sico. Miguel sai Ã  noite buscar uma curandera.

Novos vocab (3): hoy Â· maÃ±ana Â· vecino
GramÃ¡tica nova:  tener + idade  (tengo veinte aÃ±os)
RevisÃ£o F1-F6:   saudaÃ§Ãµes, Â¿cÃ³mo estÃ¡s?, me llamo, gracias, luz, yo voy
NPC principais:  SofÃ­a (no grupo agora) Â· Miguel Â· Carmen (reaparece)
Cameo:           Rosa la Panadera (acena)
Arco emocional:  alÃ­vio enganoso â†’ primeira pontada de fadiga
TransiÃ§Ã£o:       febre â†’ Miguel sai pela rua escura buscar MarÃ­a (F8)

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f7_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # ManhÃ£ na plaza. SofÃ­a aparece como se nada tivesse acontecido â€” alegre,
    # rÃ¡pida, falando alto. O grupo decide gastar o dia em coisas pequenas.
    # Cameo de Rosa na padaria. ImersÃ£o â€” falas dos NPCs sem traduÃ§Ã£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ… Plaza central Â· ManhÃ£ clara Â· Dia depois\n\n"
                        "O sol jÃ¡ estÃ¡ alto. Cheiro de pÃ£o da padaria de Rosa, "
                        "vozes de mulheres no mercado, crianÃ§a correndo atrÃ¡s "
                        "de um cÃ£o. San CristÃ³bal acordou inteiro."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "Â¡Forastero! Â¡AquÃ­ estÃ¡s! Â¿Dormiste algo?",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": (
                        "SofÃ­a aparece da esquina como se vocÃªs fossem amigos hÃ¡ "
                        "anos. Nenhuma menÃ§Ã£o da noite anterior. Nenhum peso na cara."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Buenos dÃ­as. Hoy nada raro, Â¿eh? SÃ³lo pueblo.",
                    "pace": "normal",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel chega devagar. Olhos cansados de quem nÃ£o dormiu direito â€” mas sorriso firme.",
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "Tienes que aprender a vivir aquÃ­ como gente normal. Hoy te enseÃ±o.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸž Rosa na porta da padaria, farinha nas mÃ£os, acena ao ver vocÃªs.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Â¡Buenos dÃ­as, hijos! Â¡El pan estÃ¡ caliente!",
                },
                {
                    "kind": "player",
                    "text": "Rosa estende trÃªs pÃ£es pequenos pra SofÃ­a. NÃ£o cobra. SofÃ­a sorri e devolve um aceno.",
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "Â¡Gracias, Rosa! Que tengas un buen dÃ­a.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "hoy",     "native": "hoje"},
                        {"target": "maÃ±ana",  "native": "amanhÃ£ / manhÃ£"},
                        {"target": "vecino",  "native": "vizinho"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a estende um pÃ£o pra vocÃª dizendo 'CÃ³mete esto. AÃºn sin almuerzo, Â¿no?'. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, forastero. Hoy comemos juntos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pro sol. 'Es...' â€” Qual palavra ela usa pra dizer 'hoje'?",
                    "options": [
                        {"id": "a", "text": "Hoy"},
                        {"id": "b", "text": "MaÃ±ana"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_hoy", "target": "hoy", "native": "hoje",
                    "npc_reaction": "Hoy. El dÃ­a que estamos viviendo ahora mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Um senhor da casa ao lado passa de bicicleta e acena. Miguel: 'Es nuestro...' â€” quem Ã© esse senhor pra Miguel?",
                    "options": [
                        {"id": "a", "text": "Vecino"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Campesino"},
                        {"id": "d", "text": "Padre"},
                    ],
                    "correct": "a",
                    "word_id": "es_vecino", "target": "vecino", "native": "vizinho",
                    "npc_reaction": "Vecino. Vive en la casa de al lado. Lo conozco desde niÃ±o.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a diz 'Carmen estÃ¡ cosiendo en la plaza. Â¿Vamos a verla?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy"},
                        {"id": "b", "text": "No tengo hambre"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vale. Vamos los tres.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Caminhada pela plaza. Vizinhos cumprimentam. RevisÃ£o de saudaÃ§Ãµes,
    # nome, estado fÃ­sico â€” F1 vocab em mÃºltiplas situaÃ§Ãµes reais. SofÃ­a e
    # Miguel se revezam testando.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Miguel"],
                "story": (
                    "VocÃªs caminham pra Carmen. Pelo caminho, SofÃ­a decide testar "
                    "se 'el pueblo conoce al forastero ya o no'. Aponta pessoas, "
                    "espera que vocÃª cumprimente cada uma."
                ),
                "now": "Pratique cumprimentos vivos â€” uma rua cheia de vizinhos.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Mira â€” son las nueve. AÃºn es maÃ±ana. Â¿CÃ³mo saludas?",
                    "translation": "Olha â€” sÃ£o nove horas. Ainda Ã© manhÃ£. Como vocÃª cumprimenta?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Uma vizinha de SofÃ­a passa carregando uma cesta. Sol da manhÃ£, dia novo. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "b", "text": "Â¡Buenas tardes!"},
                        {"id": "c", "text": "Â¡Buenas noches!"},
                        {"id": "d", "text": "Â¡AdiÃ³s!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Bueno. Ella va a recordar tu cara.",
                },
                {
                    "kind": "narrative",
                    "text": "A vizinha sorri pra vocÃª e responde com a mesma saudaÃ§Ã£o. Continua o caminho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Ahora ese seÃ±or â€” el del sombrero â€” te va a preguntar tu nombre. Te aviso.",
                    "translation": "Agora aquele senhor â€” o do chapÃ©u â€” vai te perguntar seu nome. Te aviso.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Vecino",
                    "line": "Buenos dÃ­as, joven. Â¿CÃ³mo te llamas? Eres nuevo aquÃ­, Â¿no?",
                    "translation": "Bom dia, jovem. Como vocÃª se chama? VocÃª Ã© novo aqui, nÃ©?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecino",
                    "question": "O senhor para na sua frente, olhando educado. Quer saber seu nome. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Mucho gusto. Yo soy Eduardo. Tengo la herrerÃ­a al fondo de la calle.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecino",
                    "question": "Eduardo se apresentou: 'Yo soy Eduardo.' Para descrever a profissÃ£o dele que ele mencionou â€” ferreiro â€” vocÃª completa: 'Eduardo ___ herrero.'",
                    "options": [
                        {"id": "a", "text": "es"},
                        {"id": "b", "text": "tiene"},
                        {"id": "c", "text": "estÃ¡"},
                        {"id": "d", "text": "voy"},
                    ],
                    "correct": "a",
                    "word_id": "es_es", "target": "es", "native": "Ã© (de SER, ele/ela)",
                    "npc_reaction": "Eduardo es herrero. 'Es' es 'soy' cuando hablamos de otra persona. Soy yo, eres tÃº, es Ã©l.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Ahora Ã©l te va a preguntar si te gusta el pueblo. Â¿CÃ³mo le respondes?",
                    "translation": "Agora ele vai te perguntar como vocÃª estÃ¡. Como vocÃª responde?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecino",
                    "question": "'Â¿Y cÃ³mo estÃ¡s hoy, joven? Â¿El pueblo te trata bien?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo sed"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Si necesitas algo de hierro o herramienta â€” ya sabes dÃ³nde estoy.",
                },
                {
                    "kind": "narrative",
                    "text": "Eduardo o ferreiro acena e segue. Miguel ri baixinho: 'Te lo dije.'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Vamos por el otro lado de la plaza. MÃ¡s vecinos para conocer.",
                    "translation": "Vamos pelo outro lado da plaza. Mais vizinhos pra conhecer.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Uma crianÃ§a passa correndo, para de repente, te olha e ri. VocÃª cumprimenta de volta:",
                    "options": [
                        {"id": "a", "text": "Â¡Hola!"},
                        {"id": "b", "text": "Â¡AdiÃ³s!"},
                        {"id": "c", "text": "Â¡Mal!"},
                        {"id": "d", "text": "Â¡Forastero!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olÃ¡",
                    "npc_reaction": "Hola. Simple. La niÃ±a ya te aceptÃ³.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y si alguien te da algo en este pueblo â€” Â¿quÃ© dices siempre?",
                    "translation": "E se alguÃ©m te dÃ¡ algo nesse pueblo â€” o que vocÃª fala sempre?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a te dÃ¡ metade do pÃ£o que sobrou da Rosa. Quente ainda. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, forastero. TÃº harÃ­as lo mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pro outro lado da plaza: 'Carmen estÃ¡ allÃ¡, sentada en su banco.' VocÃª caminha pra lÃ¡. SofÃ­a pergunta: 'Â¿TÃº vienes conmigo?' VocÃª:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo sed"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vamos juntos. Carmen va a estar feliz de verte de nuevo.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # No banco da Carmen. Carmen pergunta sobre o forastero. SofÃ­a e Miguel
    # respondem por ele Ã s vezes, mas o protagonista tambÃ©m fala. Rapid-fire.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Miguel"],
                "story": (
                    "Carmen tÃ¡ no banco de pedra com o bordado, como sempre. Ergue "
                    "os Ã³culos pequenos do nariz ao ver vocÃªs trÃªs chegando.\n\n"
                    "'Â¡Hola, hijos! Â¡Y tÃº â€” el forastero! Â¿CÃ³mo estÃ¡s hoy?'"
                ),
                "now": "Carmen vai fazer vÃ¡rias perguntas â€” vocÃª responde sem hesitar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Â¡Hola, joven! Â¿CÃ³mo estÃ¡s hoy? Te ves mÃ¡s asentado que ayer.",
                    "translation": "OlÃ¡, jovem! Como vocÃª estÃ¡ hoje? TÃ¡ com cara mais firme que ontem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "VocÃª dormiu pouco, mas comeu pÃ£o da Rosa e tÃ¡ na sombra da plaza. Carmen quer uma resposta direta:",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Me alegro. SiÃ©ntate aquÃ­, dÃ©jame verte.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Ya sÃ© tu nombre â€” SofÃ­a me lo dijo. Pero quiero oÃ­rlo de tu boca.",
                    "translation": "JÃ¡ sei seu nome â€” SofÃ­a me falou. Mas quero ouvir da sua boca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen larga o bordado e te olha de frente. Quer ouvir seu nome dito por vocÃª.",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Tengo sed"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Mucho gusto, hijo. Ya eres parte de la plaza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Â¿Y de dÃ³nde vienes, joven? Â¿Es lejos?",
                    "translation": "E de onde vocÃª vem, jovem? Ã‰ longe?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "VocÃª nÃ£o lembra de onde vem â€” Ã© a verdade. Mas Carmen sabe que vocÃª Ã© de fora. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Soy campesino"},
                        {"id": "c", "text": "Soy vecino"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero. AquÃ­ los recibimos, hijo. Si te quedas, dejas de ser forastero pronto.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "SofÃ­a senta no chÃ£o de pernas cruzadas perto do banco. "
                        "Miguel apoia no muro atrÃ¡s. Carmen volta ao bordado, "
                        "mas continua falando."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "SofÃ­a, Â¿le diste pan hoy?",
                    "translation": "SofÃ­a, vocÃª deu pÃ£o pra ele hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a olha pra vocÃª esperando que vocÃª responda por ela. VocÃª diz pra Carmen:",
                    "options": [
                        {"id": "a", "text": "SÃ­, gracias"},
                        {"id": "b", "text": "No, mal"},
                        {"id": "c", "text": "AdiÃ³s Carmen"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Bueno. AquÃ­ no se anda con hambre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Â¿Tienes sed, hijo? Hay agua del pozo fresca.",
                    "translation": "VocÃª tÃ¡ com sede, filho? Tem Ã¡gua do poÃ§o fresca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Sol jÃ¡ a pino, garganta seca de tanto falar. Carmen te oferece Ã¡gua. VocÃª responde honestamente:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Vete al pozo, hijo. AllÃ¡ la sacas tÃº mismo.",
                },
                {
                    "kind": "narrative",
                    "text": "VocÃª vai atÃ© o poÃ§o de pedra no centro da plaza, tira Ã¡gua com a corda. Volta com a cantil cheia. Carmen acena aprovando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Bueno. Y ahora â€” Â¿ya conoces a algÃºn vecino mÃ¡s?",
                    "translation": "Bom. E agora â€” vocÃª jÃ¡ conhece algum vizinho mais?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "VocÃª conheceu Eduardo o ferreiro na rua. Pra Carmen vocÃª diz: 'SÃ­, Eduardo es mi...'",
                    "options": [
                        {"id": "a", "text": "Vecino"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Campesino"},
                        {"id": "d", "text": "Padre"},
                    ],
                    "correct": "a",
                    "word_id": "es_vecino", "target": "vecino", "native": "vizinho",
                    "npc_reaction": "Eduardo. Buen hombre. Habla poco, trabaja mucho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "SofÃ­a me dijo algo extraÃ±o anoche. Que viste un fuego que no era de hogar. Â¿Es verdad?",
                    "translation": "SofÃ­a me disse uma coisa estranha ontem Ã  noite. Que vocÃª viu um fogo que nÃ£o era de fogueira. Ã‰ verdade?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen sabe parte. VocÃª nÃ£o pode mentir mas tambÃ©m nÃ£o pode contar tudo. Sobre o que aconteceu, o que vocÃª sentiu primeiro foi:",
                    "options": [
                        {"id": "a", "text": "Miedo"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Luz"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Lo entiendo. SofÃ­a te ayuda a no sentirlo solo. Eso es bueno.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen aponta pra lamparina de aceite que SofÃ­a te deu â€” vocÃª levou ao bolso. 'Esa lÃ¡mpara da...' Que palavra completa?",
                    "options": [
                        {"id": "a", "text": "Luz"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "Agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "Luz. PequeÃ±a, segura. Las que mÃ¡s cuidan son las que menos asustan.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Â¿Y tÃº vas a quedarte hoy con SofÃ­a y Miguel?",
                    "translation": "E vocÃª vai ficar hoje com SofÃ­a e Miguel?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "SofÃ­a levanta a cabeÃ§a esperando sua resposta. Miguel sorri. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy con ellos"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s Carmen"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Bueno. Los tres juntos. Eso me gusta verlo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pra vocÃª: 'Â¿Y maÃ±ana â€” quÃ© hacemos?' Como vocÃª diz 'amanhÃ£' em espanhol pra continuar a conversa?",
                    "options": [
                        {"id": "a", "text": "MaÃ±ana"},
                        {"id": "b", "text": "Hoy"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_manana", "target": "maÃ±ana", "native": "amanhÃ£",
                    "npc_reaction": "MaÃ±ana. El dÃ­a que viene despuÃ©s de hoy. La misma palabra que 'manhÃ£' del portuguÃ©s.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Carmen ensina perguntar idade. Tener + aÃ±os â€” extensÃ£o direta de
    # 'tengo hambre' que o protagonista jÃ¡ conhece. SofÃ­a e Miguel
    # exemplificam falando as prÃ³prias idades.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Carmen", "SofÃ­a", "Miguel"],
                "story": (
                    "Carmen quer saber tudo. Bordando devagar, ela faz perguntas "
                    "como quem comenta o clima â€” mas cada pergunta Ã© precisa.\n\n"
                    "Os trÃªs sentaram em volta dela. SofÃ­a no chÃ£o de pernas "
                    "cruzadas. Miguel apoiado no muro. VocÃª no banco do lado."
                ),
                "now": "Carmen vai te ensinar a falar idade â€” e quer saber a sua.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Ya sabes 'tengo hambre' y 'tengo sed'. Hay otro 'tengo' importante: 'tengo X aÃ±os'.",
                    "translation": "VocÃª jÃ¡ sabe 'tengo hambre' e 'tengo sed'. Tem outro 'tengo' importante: 'tengo X aÃ±os' (tenho X anos).",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tengo X aÃ±os",
                    "meaning": "Eu tenho X anos",
                    "note": "mesmo padrÃ£o de 'tengo hambre' â€” o que vocÃª 'tem' aqui Ã© a idade",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Yo tengo dieciocho aÃ±os. Joven todavÃ­a.",
                    "translation": "Eu tenho dezoito anos. Jovem ainda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y yo tengo veinte. Igual que tÃº, Â¿no, forastero?",
                    "translation": "E eu tenho vinte. Igual a vocÃª, nÃ©, forasteiro?",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Tengo",   "isKey": True},
                        {"text": " + ",     "isKey": False},
                        {"text": "veinte",  "isKey": True},
                        {"text": " ",       "isKey": False},
                        {"text": "aÃ±os",    "isKey": True},
                    ],
                    "example": "â€” Â¿CuÃ¡ntos aÃ±os tienes? â€” Tengo veinte aÃ±os.",
                    "translation": "â€” Quantos anos vocÃª tem? â€” Tenho vinte anos.",
                    "note": "nÃºmero + 'aÃ±os' depois de 'tengo'. Sempre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen tira os Ã³culos do nariz pra te olhar de frente. 'Â¿Y tÃº? Â¿CuÃ¡ntos aÃ±os tienes?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Soy forastero"},
                        {"id": "d", "text": "Me llamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. La edad en que un hombre todavÃ­a cree que sabe todo. Espera, hijo. Espera.",
                },
                {
                    "kind": "narrative",
                    "text": "SofÃ­a ri da resposta da Carmen. Miguel ri tambÃ©m, baixo. VocÃª nÃ£o entende exatamente â€” mas ri junto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Â¿Y ahora pregunta tÃº a Miguel â€” 'Â¿cuÃ¡ntos aÃ±os tienes?'.",
                    "translation": "E agora pergunta vocÃª pro Miguel â€” 'quantos anos vocÃª tem?'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "VocÃª se vira pra Miguel e quer saber a idade dele. A pergunta comeÃ§a com:",
                    "options": [
                        {"id": "a", "text": "Â¿CuÃ¡ntos aÃ±os tienes?"},
                        {"id": "b", "text": "Â¿CÃ³mo te llamas?"},
                        {"id": "c", "text": "Â¿DÃ³nde estÃ¡s?"},
                        {"id": "d", "text": "Â¿TÃº vienes?"},
                    ],
                    "correct": "a",
                    "word_id": "es_cuantos_anos", "target": "Â¿cuÃ¡ntos aÃ±os tienes?", "native": "quantos anos vocÃª tem?",
                    "npc_reaction": "Tengo veinte, forastero. Como tÃº. Por eso conectamos rÃ¡pido.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Y la respuesta â€” recuerda â€” siempre 'tengo X aÃ±os'.",
                    "translation": "E a resposta â€” lembra â€” sempre 'tengo X aÃ±os'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a repete pra fixar: 'Si alguien te pregunta cuÃ¡ntos aÃ±os tienes, tÃº dices:'",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Mi veinte aÃ±os"},
                        {"id": "d", "text": "Veinte tengo aÃ±os"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Eso. Memoriza ese 'tengo'. Vas a usarlo mucho.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Tarde caindo. Voltando pra casa de Don Miguel. SofÃ­a sussurra sobre a
    # primeira vez da avÃ³ dela â€” 'duele la cabeza'. Primeira pista de que o
    # dom tem custo fÃ­sico. Conversa Ã­ntima â€” poucos exercÃ­cios, foco em
    # desenvolver lore e personagem.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Miguel", "Carmen"],
                "story": (
                    "VocÃªs ficaram com Carmen atÃ© o sol comeÃ§ar a baixar. A tarde "
                    "passou em conversa â€” vizinhos parando pra cumprimentar, "
                    "SofÃ­a testando vocÃª de leve, Miguel rindo Ã s vezes do que "
                    "vocÃª falava errado.\n\n"
                    "Quando a sombra do banco virou metade da plaza, Carmen "
                    "guardou o bordado. 'Vayan, hijos. MaÃ±ana otro dÃ­a.'"
                ),
                "now": "Voltando pra posada â€” SofÃ­a caminha do seu lado, vira a voz baixa.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ‡ Rua estreita, luz alaranjada batendo nas paredes de adobe. Miguel uns passos Ã  frente.",
                },
                {
                    "kind": "item_moment",
                    "npc": "SofÃ­a",
                    "situation": "O calor da tarde ainda pesa. SofÃ­a passa a mÃ£o na testa, garganta seca de tanto falar o dia inteiro.",
                    "npc_line": "Forastero â€” Â¿tienes algo de beber? HablÃ© todo el dÃ­a y la garganta me arde.",
                    "item_tag": "bebida",
                    "on_use": {
                        "narrative": "VocÃª tira algo de beber da mochila e estende pra SofÃ­a. Ela bebe um gole longo, devolve, respira.",
                        "npc_reaction": "Gracias. Ahora sÃ­ â€” puedo seguir hablando sin sonar a cuervo.",
                        "bonus": "extra_dialogue",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Hay una fuente cerca de casa de Don Miguel. Aguanto.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” Â¿no te duele la cabeza? La primera vez a mi abuela le doliÃ³ por dÃ­as, dicen.",
                    "translation": "Forasteiro â€” sua cabeÃ§a nÃ£o estÃ¡ doendo? A primeira vez da minha avÃ³ doeu por dias, dizem.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª parou. Uma pontada atrÃ¡s dos olhos que vocÃª tinha ignorado todo o dia. Como se ela tivesse acabado de nomeÃ¡-la.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Mi abuela decÃ­a que era el cuerpo aprendiendo a cargar la palabra. Como un mÃºsculo nuevo.",
                    "translation": "Minha avÃ³ dizia que era o corpo aprendendo a carregar a palavra. Como um mÃºsculo novo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pra sua testa, esperando uma resposta honesta. VocÃª sente a dor â€” pequena, mas real:",
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bien"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Mal. Lo pensÃ©. Mi abuela hablaba de eso â€” todavÃ­a me acuerdo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs continuam caminhando. Miguel olha pra trÃ¡s de vez "
                        "em quando, sem perguntar. Sabe que tem coisa sendo dita "
                        "que nÃ£o precisa entrar nela ainda."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Ella dormÃ­a mucho la primera semana. ComÃ­a menos. Hablaba poco. DespuÃ©s se le pasaba.",
                    "translation": "Ela dormia muito a primeira semana. Comia menos. Falava pouco. Depois passava.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pro bolso onde vocÃª guarda a lamparina dela. 'Si tienes miedo de noche, enciÃ©ndela. La luz cura mÃ¡s que las palabras.' Sobre a lamparina, o que ela faz?",
                    "options": [
                        {"id": "a", "text": "Da luz"},
                        {"id": "b", "text": "Tiene miedo"},
                        {"id": "c", "text": "Tiene hambre"},
                        {"id": "d", "text": "Es vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "Eso. Si te despiertas con miedo â€” la enciendes. Funciona.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Hoy descansas. MaÃ±ana â€” vamos a ver cÃ³mo estÃ¡s. Â¿Vale?",
                    "translation": "Hoje vocÃª descansa. AmanhÃ£ â€” a gente vÃª como vocÃª tÃ¡. Beleza?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a espera sua resposta. VocÃªs param na porta da casa de Don Miguel. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Gracias, SofÃ­a"},
                        {"id": "b", "text": "AdiÃ³s Carmen"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Para esto estoy yo en esto contigo, Â¿no?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Entra, forastero. Come algo. DespuÃ©s duermes.",
                    "translation": "Entra, forasteiro. Come alguma coisa. Depois dorme.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Sua cabeÃ§a pesa mais agora. A pontada virou uma pressÃ£o. VocÃª responde a Miguel honestamente sobre como estÃ¡:",
                    "options": [
                        {"id": "a", "text": "Mal, la cabeza"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "La cabeza. SofÃ­a me habÃ­a avisado. Vamos â€” descansa.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Noite. Febre subindo. SofÃ­a e Miguel cuidando. O protagonista precisa
    # responder mesmo com a cabeÃ§a queimando. SofÃ­a decide: vai buscar uma
    # curandera que ela conhece â€” MarÃ­a. TransiÃ§Ã£o direta pra F8.
    # Gate: errar trava. Mas situaÃ§Ã£o extrema, exercÃ­cios curtos.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Miguel"],
                "story": (
                    "VocÃª entrou na casa, comeu metade do pÃ£o que sobrou, deitou "
                    "no quarto. SofÃ­a nÃ£o foi embora â€” ficou na sala com Miguel. "
                    "Acertaram entre eles em voz baixa que nÃ£o te deixariam sÃ³.\n\n"
                    "A febre comeÃ§ou ao escurecer. AtrÃ¡s dos olhos primeiro. "
                    "Depois cabeÃ§a inteira. SofÃ­a bateu na sua porta."
                ),
                "now": "VocÃª precisa responder mesmo doente. SofÃ­a precisa decidir o que fazer.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ™ Noite Â· Quarto Â· Lamparina baixa\n\nVocÃª deitado, suando frio. SofÃ­a senta na beira da cama. Miguel encostado no batente da porta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” Â¿cÃ³mo estÃ¡s? Necesito que me digas.",
                    "translation": "Forasteiro â€” como vocÃª tÃ¡? Preciso que vocÃª me fale.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "CabeÃ§a queimando, corpo pesado, garganta seca. VocÃª diz a verdade â€” nÃ£o dÃ¡ pra esconder:",
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bien"},
                        {"id": "c", "text": "Buenos dÃ­as"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Mal. Lo veo. Tienes fiebre â€” la frente caliente.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Â¿Tienes sed? Â¿Quieres agua?",
                    "translation": "TÃ¡ com sede? Quer Ã¡gua?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Sua boca seca como pedra. SofÃ­a jÃ¡ estende a cantil. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. Toma â€” bebe despacio.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "SofÃ­a levanta. Vai atÃ© Miguel na porta, fala baixo: 'Esto no "
                        "es sÃ³lo cansancio. Es lo que decÃ­a mi abuela. Hay que "
                        "buscarla.'"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Miguel â€” conozco a una. Llega de fuera, pero cura bien. Ve a buscarla.",
                    "translation": "Miguel â€” conheÃ§o uma. Vem de fora, mas cura bem. Vai buscar ela.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Â¿QuiÃ©n?",
                    "translation": "Quem?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Una curandera. MarÃ­a. LlegÃ³ al pueblo hace dos meses. PregÃºntale a Carmen â€” sabe dÃ³nde estÃ¡.",
                    "translation": "Uma curandera. MarÃ­a. Chegou ao pueblo faz dois meses. Pergunta pra Carmen â€” ela sabe onde tÃ¡.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel jÃ¡ vestiu o casaco. Aperta seu ombro antes de sair. 'Aguanta, forastero. Vuelvo pronto.' VocÃª responde com o que consegue:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Ve a dormir un poco â€” yo vuelvo con ella.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Miguel sai correndo. Passos rÃ¡pidos na rua, depois silÃªncio. "
                        "SofÃ­a senta de novo na beira da cama. Coloca a mÃ£o fria na "
                        "sua testa quente."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Mi abuela decÃ­a que despuÃ©s de la primera, viene la fiebre. Y despuÃ©s la fiebre se va. Aguanta hasta maÃ±ana.",
                    "translation": "Minha avÃ³ dizia que depois da primeira, vem a febre. E depois a febre passa. Aguenta atÃ© amanhÃ£.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Sua cabeÃ§a pesa, os olhos fecham. VocÃª quer perguntar o nome da curandera que vem. A pergunta Ã©:",
                    "options": [
                        {"id": "a", "text": "Â¿CÃ³mo se llama?"},
                        {"id": "b", "text": "Â¿CÃ³mo estÃ¡s?"},
                        {"id": "c", "text": "Â¿TÃº vienes?"},
                        {"id": "d", "text": "Â¿Tengo sed?"},
                    ],
                    "correct": "a",
                    "word_id": "es_como_se_llama", "target": "Â¿cÃ³mo se llama?", "native": "como se chama?",
                    "npc_reaction": "Se llama MarÃ­a. Vas a conocerla pronto, forastero.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F8 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸ•¯ï¸ Quarto escuro Â· A febre subindo Â· SofÃ­a velando",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Duerme, forastero. Cuando despiertes ella ya estarÃ¡ aquÃ­.",
                    "translation": "Dorme, forasteiro. Quando vocÃª acordar ela jÃ¡ vai estar aqui.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª fecha os olhos. A Ãºltima coisa que ouve antes de "
                        "dormir Ã© o pano molhado da SofÃ­a na sua testa.\n\n"
                        "LÃ¡ fora â€” passos correndo na rua escura. Miguel batendo "
                        "na porta de Carmen pra perguntar onde encontrar uma "
                        "mulher chamada MarÃ­a."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
