"""
Seed das 6 seções da Fase 7 Espanhol A1 — "El día normal".

Fase de respiração — falsa normalidade. Depois da noite do dom (F5) e da
entrada da Sofía (F6), o grupo decide passar um dia inteiro como se nada
tivesse acontecido. Sofía aparece na plaza como amiga de anos. Miguel
leva o grupo a Carmen pra aprender a 'viver como gente daqui'. Carmen
ensina perguntar idade.

No final da fase: febre. Sofía sussurra sobre a 'dor de cabeça da primeira
vez'. O dom tem custo físico. Miguel sai à noite buscar uma curandera.

Novos vocab (3): hoy · mañana · vecino
Gramática nova:  tener + idade  (tengo veinte años)
Revisão F1-F6:   saudações, ¿cómo estás?, me llamo, gracias, luz, yo voy
NPC principais:  Sofía (no grupo agora) · Miguel · Carmen (reaparece)
Cameo:           Rosa la Panadera (acena)
Arco emocional:  alívio enganoso → primeira pontada de fadiga
Transição:       febre → Miguel sai pela rua escura buscar María (F8)

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f7_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Manhã na plaza. Sofía aparece como se nada tivesse acontecido — alegre,
    # rápida, falando alto. O grupo decide gastar o dia em coisas pequenas.
    # Cameo de Rosa na padaria. Imersão — falas dos NPCs sem tradução.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌅 Plaza central · Manhã clara · Dia depois\n\n"
                        "O sol já está alto. Cheiro de pão da padaria de Rosa, "
                        "vozes de mulheres no mercado, criança correndo atrás "
                        "de um cão. San Cristóbal acordou inteiro."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "¡Forastero! ¡Aquí estás! ¿Dormiste algo?",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": (
                        "Sofía aparece da esquina como se vocês fossem amigos há "
                        "anos. Nenhuma menção da noite anterior. Nenhum peso na cara."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Buenos días. Hoy nada raro, ¿eh? Sólo pueblo.",
                    "pace": "normal",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel chega devagar. Olhos cansados de quem não dormiu direito — mas sorriso firme.",
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "Tienes que aprender a vivir aquí como gente normal. Hoy te enseño.",
                },
                {
                    "kind": "scene",
                    "text": "🍞 Rosa na porta da padaria, farinha nas mãos, acena ao ver vocês.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "¡Buenos días, hijos! ¡El pan está caliente!",
                },
                {
                    "kind": "player",
                    "text": "Rosa estende três pães pequenos pra Sofía. Não cobra. Sofía sorri e devolve um aceno.",
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "¡Gracias, Rosa! Que tengas un buen día.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "hoy",     "native": "hoje"},
                        {"target": "mañana",  "native": "amanhã / manhã"},
                        {"target": "vecino",  "native": "vizinho"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía estende um pão pra você dizendo 'Cómete esto. Aún sin almuerzo, ¿no?'. Você diz:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, forastero. Hoy comemos juntos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pro sol. 'Es...' — Qual palavra ela usa pra dizer 'hoje'?",
                    "options": [
                        {"id": "a", "text": "Hoy"},
                        {"id": "b", "text": "Mañana"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_hoy", "target": "hoy", "native": "hoje",
                    "npc_reaction": "Hoy. El día que estamos viviendo ahora mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Um senhor da casa ao lado passa de bicicleta e acena. Miguel: 'Es nuestro...' — quem é esse senhor pra Miguel?",
                    "options": [
                        {"id": "a", "text": "Vecino"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Campesino"},
                        {"id": "d", "text": "Padre"},
                    ],
                    "correct": "a",
                    "word_id": "es_vecino", "target": "vecino", "native": "vizinho",
                    "npc_reaction": "Vecino. Vive en la casa de al lado. Lo conozco desde niño.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía diz 'Carmen está cosiendo en la plaza. ¿Vamos a verla?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy"},
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

    # ── Seção 2: Revisão SRS ─────────────────────────────────────────────────
    # Caminhada pela plaza. Vizinhos cumprimentam. Revisão de saudações,
    # nome, estado físico — F1 vocab em múltiplas situações reais. Sofía e
    # Miguel se revezam testando.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Sofía", "Miguel"],
                "story": (
                    "Vocês caminham pra Carmen. Pelo caminho, Sofía decide testar "
                    "se 'el pueblo conoce al forastero ya o no'. Aponta pessoas, "
                    "espera que você cumprimente cada uma."
                ),
                "now": "Pratique cumprimentos vivos — uma rua cheia de vizinhos.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Mira — son las nueve. Aún es mañana. ¿Cómo saludas?",
                    "translation": "Olha — são nove horas. Ainda é manhã. Como você cumprimenta?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Uma vizinha de Sofía passa carregando uma cesta. Sol da manhã, dia novo. Você diz:",
                    "options": [
                        {"id": "a", "text": "¡Buenos días!"},
                        {"id": "b", "text": "¡Buenas tardes!"},
                        {"id": "c", "text": "¡Buenas noches!"},
                        {"id": "d", "text": "¡Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Bueno. Ella va a recordar tu cara.",
                },
                {
                    "kind": "narrative",
                    "text": "A vizinha sorri pra você e responde com a mesma saudação. Continua o caminho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Ahora ese señor — el del sombrero — te va a preguntar tu nombre. Te aviso.",
                    "translation": "Agora aquele senhor — o do chapéu — vai te perguntar seu nome. Te aviso.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Vecino",
                    "line": "Buenos días, joven. ¿Cómo te llamas? Eres nuevo aquí, ¿no?",
                    "translation": "Bom dia, jovem. Como você se chama? Você é novo aqui, né?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecino",
                    "question": "O senhor para na sua frente, olhando educado. Quer saber seu nome. Você responde:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto. Yo soy Eduardo. Tengo la herrería al fondo de la calle.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecino",
                    "question": "Eduardo se apresentou: 'Yo soy Eduardo.' Para descrever a profissão dele que ele mencionou — ferreiro — você completa: 'Eduardo ___ herrero.'",
                    "options": [
                        {"id": "a", "text": "es"},
                        {"id": "b", "text": "tiene"},
                        {"id": "c", "text": "está"},
                        {"id": "d", "text": "voy"},
                    ],
                    "correct": "a",
                    "word_id": "es_es", "target": "es", "native": "é (de SER, ele/ela)",
                    "npc_reaction": "Eduardo es herrero. 'Es' es 'soy' cuando hablamos de otra persona. Soy yo, eres tú, es él.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Ahora él te va a preguntar si te gusta el pueblo. ¿Cómo le respondes?",
                    "translation": "Agora ele vai te perguntar como você está. Como você responde?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecino",
                    "question": "'¿Y cómo estás hoy, joven? ¿El pueblo te trata bien?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo sed"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Si necesitas algo de hierro o herramienta — ya sabes dónde estoy.",
                },
                {
                    "kind": "narrative",
                    "text": "Eduardo o ferreiro acena e segue. Miguel ri baixinho: 'Te lo dije.'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Vamos por el otro lado de la plaza. Más vecinos para conocer.",
                    "translation": "Vamos pelo outro lado da plaza. Mais vizinhos pra conhecer.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Uma criança passa correndo, para de repente, te olha e ri. Você cumprimenta de volta:",
                    "options": [
                        {"id": "a", "text": "¡Hola!"},
                        {"id": "b", "text": "¡Adiós!"},
                        {"id": "c", "text": "¡Mal!"},
                        {"id": "d", "text": "¡Forastero!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olá",
                    "npc_reaction": "Hola. Simple. La niña ya te aceptó.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y si alguien te da algo en este pueblo — ¿qué dices siempre?",
                    "translation": "E se alguém te dá algo nesse pueblo — o que você fala sempre?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía te dá metade do pão que sobrou da Rosa. Quente ainda. Você diz:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, forastero. Tú harías lo mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pro outro lado da plaza: 'Carmen está allá, sentada en su banco.' Você caminha pra lá. Sofía pergunta: '¿Tú vienes conmigo?' Você:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy"},
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

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # No banco da Carmen. Carmen pergunta sobre o forastero. Sofía e Miguel
    # respondem por ele às vezes, mas o protagonista também fala. Rapid-fire.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Sofía", "Miguel"],
                "story": (
                    "Carmen tá no banco de pedra com o bordado, como sempre. Ergue "
                    "os óculos pequenos do nariz ao ver vocês três chegando.\n\n"
                    "'¡Hola, hijos! ¡Y tú — el forastero! ¿Cómo estás hoy?'"
                ),
                "now": "Carmen vai fazer várias perguntas — você responde sem hesitar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¡Hola, joven! ¿Cómo estás hoy? Te ves más asentado que ayer.",
                    "translation": "Olá, jovem! Como você está hoje? Tá com cara mais firme que ontem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Você dormiu pouco, mas comeu pão da Rosa e tá na sombra da plaza. Carmen quer uma resposta direta:",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Me alegro. Siéntate aquí, déjame verte.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Ya sé tu nombre — Sofía me lo dijo. Pero quiero oírlo de tu boca.",
                    "translation": "Já sei seu nome — Sofía me falou. Mas quero ouvir da sua boca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen larga o bordado e te olha de frente. Quer ouvir seu nome dito por você.",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Tengo sed"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto, hijo. Ya eres parte de la plaza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¿Y de dónde vienes, joven? ¿Es lejos?",
                    "translation": "E de onde você vem, jovem? É longe?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Você não lembra de onde vem — é a verdade. Mas Carmen sabe que você é de fora. Você responde:",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Soy campesino"},
                        {"id": "c", "text": "Soy vecino"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero. Aquí los recibimos, hijo. Si te quedas, dejas de ser forastero pronto.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Sofía senta no chão de pernas cruzadas perto do banco. "
                        "Miguel apoia no muro atrás. Carmen volta ao bordado, "
                        "mas continua falando."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Sofía, ¿le diste pan hoy?",
                    "translation": "Sofía, você deu pão pra ele hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía olha pra você esperando que você responda por ela. Você diz pra Carmen:",
                    "options": [
                        {"id": "a", "text": "Sí, gracias"},
                        {"id": "b", "text": "No, mal"},
                        {"id": "c", "text": "Adiós Carmen"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Bueno. Aquí no se anda con hambre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¿Tienes sed, hijo? Hay agua del pozo fresca.",
                    "translation": "Você tá com sede, filho? Tem água do poço fresca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Sol já a pino, garganta seca de tanto falar. Carmen te oferece água. Você responde honestamente:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Vete al pozo, hijo. Allá la sacas tú mismo.",
                },
                {
                    "kind": "narrative",
                    "text": "Você vai até o poço de pedra no centro da plaza, tira água com a corda. Volta com a cantil cheia. Carmen acena aprovando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Bueno. Y ahora — ¿ya conoces a algún vecino más?",
                    "translation": "Bom. E agora — você já conhece algum vizinho mais?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Você conheceu Eduardo o ferreiro na rua. Pra Carmen você diz: 'Sí, Eduardo es mi...'",
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
                    "line": "Sofía me dijo algo extraño anoche. Que viste un fuego que no era de hogar. ¿Es verdad?",
                    "translation": "Sofía me disse uma coisa estranha ontem à noite. Que você viu um fogo que não era de fogueira. É verdade?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen sabe parte. Você não pode mentir mas também não pode contar tudo. Sobre o que aconteceu, o que você sentiu primeiro foi:",
                    "options": [
                        {"id": "a", "text": "Miedo"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Luz"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Lo entiendo. Sofía te ayuda a no sentirlo solo. Eso es bueno.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen aponta pra lamparina de aceite que Sofía te deu — você levou ao bolso. 'Esa lámpara da...' Que palavra completa?",
                    "options": [
                        {"id": "a", "text": "Luz"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "Agua"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "Luz. Pequeña, segura. Las que más cuidan son las que menos asustan.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¿Y tú vas a quedarte hoy con Sofía y Miguel?",
                    "translation": "E você vai ficar hoje com Sofía e Miguel?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Sofía levanta a cabeça esperando sua resposta. Miguel sorri. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy con ellos"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Adiós Carmen"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Bueno. Los tres juntos. Eso me gusta verlo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pra você: '¿Y mañana — qué hacemos?' Como você diz 'amanhã' em espanhol pra continuar a conversa?",
                    "options": [
                        {"id": "a", "text": "Mañana"},
                        {"id": "b", "text": "Hoy"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_manana", "target": "mañana", "native": "amanhã",
                    "npc_reaction": "Mañana. El día que viene después de hoy. La misma palabra que 'manhã' del portugués.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Carmen ensina perguntar idade. Tener + años — extensão direta de
    # 'tengo hambre' que o protagonista já conhece. Sofía e Miguel
    # exemplificam falando as próprias idades.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Carmen", "Sofía", "Miguel"],
                "story": (
                    "Carmen quer saber tudo. Bordando devagar, ela faz perguntas "
                    "como quem comenta o clima — mas cada pergunta é precisa.\n\n"
                    "Os três sentaram em volta dela. Sofía no chão de pernas "
                    "cruzadas. Miguel apoiado no muro. Você no banco do lado."
                ),
                "now": "Carmen vai te ensinar a falar idade — e quer saber a sua.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Ya sabes 'tengo hambre' y 'tengo sed'. Hay otro 'tengo' importante: 'tengo X años'.",
                    "translation": "Você já sabe 'tengo hambre' e 'tengo sed'. Tem outro 'tengo' importante: 'tengo X años' (tenho X anos).",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tengo X años",
                    "meaning": "Eu tenho X anos",
                    "note": "mesmo padrão de 'tengo hambre' — o que você 'tem' aqui é a idade",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Yo tengo dieciocho años. Joven todavía.",
                    "translation": "Eu tenho dezoito anos. Jovem ainda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y yo tengo veinte. Igual que tú, ¿no, forastero?",
                    "translation": "E eu tenho vinte. Igual a você, né, forasteiro?",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Tengo",   "isKey": True},
                        {"text": " + ",     "isKey": False},
                        {"text": "veinte",  "isKey": True},
                        {"text": " ",       "isKey": False},
                        {"text": "años",    "isKey": True},
                    ],
                    "example": "— ¿Cuántos años tienes? — Tengo veinte años.",
                    "translation": "— Quantos anos você tem? — Tenho vinte anos.",
                    "note": "número + 'años' depois de 'tengo'. Sempre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen tira os óculos do nariz pra te olhar de frente. '¿Y tú? ¿Cuántos años tienes?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Soy forastero"},
                        {"id": "d", "text": "Me llamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. La edad en que un hombre todavía cree que sabe todo. Espera, hijo. Espera.",
                },
                {
                    "kind": "narrative",
                    "text": "Sofía ri da resposta da Carmen. Miguel ri também, baixo. Você não entende exatamente — mas ri junto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¿Y ahora pregunta tú a Miguel — '¿cuántos años tienes?'.",
                    "translation": "E agora pergunta você pro Miguel — 'quantos anos você tem?'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Você se vira pra Miguel e quer saber a idade dele. A pergunta começa com:",
                    "options": [
                        {"id": "a", "text": "¿Cuántos años tienes?"},
                        {"id": "b", "text": "¿Cómo te llamas?"},
                        {"id": "c", "text": "¿Dónde estás?"},
                        {"id": "d", "text": "¿Tú vienes?"},
                    ],
                    "correct": "a",
                    "word_id": "es_cuantos_anos", "target": "¿cuántos años tienes?", "native": "quantos anos você tem?",
                    "npc_reaction": "Tengo veinte, forastero. Como tú. Por eso conectamos rápido.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Y la respuesta — recuerda — siempre 'tengo X años'.",
                    "translation": "E a resposta — lembra — sempre 'tengo X años'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía repete pra fixar: 'Si alguien te pregunta cuántos años tienes, tú dices:'",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Mi veinte años"},
                        {"id": "d", "text": "Veinte tengo años"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Eso. Memoriza ese 'tengo'. Vas a usarlo mucho.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Tarde caindo. Voltando pra casa de Don Miguel. Sofía sussurra sobre a
    # primeira vez da avó dela — 'duele la cabeza'. Primeira pista de que o
    # dom tem custo físico. Conversa íntima — poucos exercícios, foco em
    # desenvolver lore e personagem.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Sofía", "Miguel", "Carmen"],
                "story": (
                    "Vocês ficaram com Carmen até o sol começar a baixar. A tarde "
                    "passou em conversa — vizinhos parando pra cumprimentar, "
                    "Sofía testando você de leve, Miguel rindo às vezes do que "
                    "você falava errado.\n\n"
                    "Quando a sombra do banco virou metade da plaza, Carmen "
                    "guardou o bordado. 'Vayan, hijos. Mañana otro día.'"
                ),
                "now": "Voltando pra posada — Sofía caminha do seu lado, vira a voz baixa.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌇 Rua estreita, luz alaranjada batendo nas paredes de adobe. Miguel uns passos à frente.",
                },
                {
                    "kind": "item_moment",
                    "npc": "Sofía",
                    "situation": "O calor da tarde ainda pesa. Sofía passa a mão na testa, garganta seca de tanto falar o dia inteiro.",
                    "npc_line": "Forastero — ¿tienes algo de beber? Hablé todo el día y la garganta me arde.",
                    "item_tag": "bebida",
                    "on_use": {
                        "narrative": "Você tira algo de beber da mochila e estende pra Sofía. Ela bebe um gole longo, devolve, respira.",
                        "npc_reaction": "Gracias. Ahora sí — puedo seguir hablando sin sonar a cuervo.",
                        "bonus": "extra_dialogue",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Hay una fuente cerca de casa de Don Miguel. Aguanto.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Forastero — ¿no te duele la cabeza? La primera vez a mi abuela le dolió por días, dicen.",
                    "translation": "Forasteiro — sua cabeça não está doendo? A primeira vez da minha avó doeu por dias, dizem.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você parou. Uma pontada atrás dos olhos que você tinha ignorado todo o dia. Como se ela tivesse acabado de nomeá-la.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Mi abuela decía que era el cuerpo aprendiendo a cargar la palabra. Como un músculo nuevo.",
                    "translation": "Minha avó dizia que era o corpo aprendendo a carregar a palavra. Como um músculo novo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pra sua testa, esperando uma resposta honesta. Você sente a dor — pequena, mas real:",
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bien"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Mal. Lo pensé. Mi abuela hablaba de eso — todavía me acuerdo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês continuam caminhando. Miguel olha pra trás de vez "
                        "em quando, sem perguntar. Sabe que tem coisa sendo dita "
                        "que não precisa entrar nela ainda."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Ella dormía mucho la primera semana. Comía menos. Hablaba poco. Después se le pasaba.",
                    "translation": "Ela dormia muito a primeira semana. Comia menos. Falava pouco. Depois passava.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta pro bolso onde você guarda a lamparina dela. 'Si tienes miedo de noche, enciéndela. La luz cura más que las palabras.' Sobre a lamparina, o que ela faz?",
                    "options": [
                        {"id": "a", "text": "Da luz"},
                        {"id": "b", "text": "Tiene miedo"},
                        {"id": "c", "text": "Tiene hambre"},
                        {"id": "d", "text": "Es vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "Eso. Si te despiertas con miedo — la enciendes. Funciona.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Hoy descansas. Mañana — vamos a ver cómo estás. ¿Vale?",
                    "translation": "Hoje você descansa. Amanhã — a gente vê como você tá. Beleza?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía espera sua resposta. Vocês param na porta da casa de Don Miguel. Você diz:",
                    "options": [
                        {"id": "a", "text": "Gracias, Sofía"},
                        {"id": "b", "text": "Adiós Carmen"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Para esto estoy yo en esto contigo, ¿no?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Entra, forastero. Come algo. Después duermes.",
                    "translation": "Entra, forasteiro. Come alguma coisa. Depois dorme.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Sua cabeça pesa mais agora. A pontada virou uma pressão. Você responde a Miguel honestamente sobre como está:",
                    "options": [
                        {"id": "a", "text": "Mal, la cabeza"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "La cabeza. Sofía me había avisado. Vamos — descansa.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Noite. Febre subindo. Sofía e Miguel cuidando. O protagonista precisa
    # responder mesmo com a cabeça queimando. Sofía decide: vai buscar uma
    # curandera que ela conhece — María. Transição direta pra F8.
    # Gate: errar trava. Mas situação extrema, exercícios curtos.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Sofía", "Miguel"],
                "story": (
                    "Você entrou na casa, comeu metade do pão que sobrou, deitou "
                    "no quarto. Sofía não foi embora — ficou na sala com Miguel. "
                    "Acertaram entre eles em voz baixa que não te deixariam só.\n\n"
                    "A febre começou ao escurecer. Atrás dos olhos primeiro. "
                    "Depois cabeça inteira. Sofía bateu na sua porta."
                ),
                "now": "Você precisa responder mesmo doente. Sofía precisa decidir o que fazer.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌙 Noite · Quarto · Lamparina baixa\n\nVocê deitado, suando frio. Sofía senta na beira da cama. Miguel encostado no batente da porta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Forastero — ¿cómo estás? Necesito que me digas.",
                    "translation": "Forasteiro — como você tá? Preciso que você me fale.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Cabeça queimando, corpo pesado, garganta seca. Você diz a verdade — não dá pra esconder:",
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bien"},
                        {"id": "c", "text": "Buenos días"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Mal. Lo veo. Tienes fiebre — la frente caliente.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "¿Tienes sed? ¿Quieres agua?",
                    "translation": "Tá com sede? Quer água?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sua boca seca como pedra. Sofía já estende a cantil. Você diz:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. Toma — bebe despacio.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Sofía levanta. Vai até Miguel na porta, fala baixo: 'Esto no "
                        "es sólo cansancio. Es lo que decía mi abuela. Hay que "
                        "buscarla.'"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Miguel — conozco a una. Llega de fuera, pero cura bien. Ve a buscarla.",
                    "translation": "Miguel — conheço uma. Vem de fora, mas cura bem. Vai buscar ela.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "¿Quién?",
                    "translation": "Quem?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Una curandera. María. Llegó al pueblo hace dos meses. Pregúntale a Carmen — sabe dónde está.",
                    "translation": "Uma curandera. María. Chegou ao pueblo faz dois meses. Pergunta pra Carmen — ela sabe onde tá.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel já vestiu o casaco. Aperta seu ombro antes de sair. 'Aguanta, forastero. Vuelvo pronto.' Você responde com o que consegue:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Ve a dormir un poco — yo vuelvo con ella.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Miguel sai correndo. Passos rápidos na rua, depois silêncio. "
                        "Sofía senta de novo na beira da cama. Coloca a mão fria na "
                        "sua testa quente."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Mi abuela decía que después de la primera, viene la fiebre. Y después la fiebre se va. Aguanta hasta mañana.",
                    "translation": "Minha avó dizia que depois da primeira, vem a febre. E depois a febre passa. Aguenta até amanhã.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sua cabeça pesa, os olhos fecham. Você quer perguntar o nome da curandera que vem. A pergunta é:",
                    "options": [
                        {"id": "a", "text": "¿Cómo se llama?"},
                        {"id": "b", "text": "¿Cómo estás?"},
                        {"id": "c", "text": "¿Tú vienes?"},
                        {"id": "d", "text": "¿Tengo sed?"},
                    ],
                    "correct": "a",
                    "word_id": "es_como_se_llama", "target": "¿cómo se llama?", "native": "como se chama?",
                    "npc_reaction": "Se llama María. Vas a conocerla pronto, forastero.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F8 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🕯️ Quarto escuro · A febre subindo · Sofía velando",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Duerme, forastero. Cuando despiertes ella ya estará aquí.",
                    "translation": "Dorme, forasteiro. Quando você acordar ela já vai estar aqui.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você fecha os olhos. A última coisa que ouve antes de "
                        "dormir é o pano molhado da Sofía na sua testa.\n\n"
                        "Lá fora — passos correndo na rua escura. Miguel batendo "
                        "na porta de Carmen pra perguntar onde encontrar uma "
                        "mulher chamada María."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
