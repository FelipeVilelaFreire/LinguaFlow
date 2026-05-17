"""
Seed das 6 seções da Fase 2 Espanhol A1 — "El Pueblo Despierta".

Dia seguinte à chegada. Don Miguel mostra a posada pela manhã, leva o
protagonista por um circuito curto pelo pueblo e ensina as primeiras
necessidades físicas: tengo hambre, tengo sed, pan, agua.

Novos vocab (2): pan · agua · tengo hambre · tengo sed
Revisão F1: hola, buenos días, gracias, de nada, me llamo, ¿cómo estás?, bien/mal, forastero
NPC principal:   Don Miguel (fio condutor)
NPC cameo:       Rosa la Panadera (reaparece brevemente)
Itens:           pan_fresco · agua_del_pozo
Arco emocional:  desorientado → começa a entender o ritmo do pueblo
Transição:       anoitecer na posada; uma sombra passa pela janela — alguém observou

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f2_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Manhã na posada. Protagonista acorda sem saber onde está — cheiro de pão,
    # luz pela janela. Don Miguel chega, Rosa aparece com pão quente.
    # Falas dos NPCs SEM tradução — imersão. Exercícios: reconhecimento contextual.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "agua",
                    "min_level": 1,
                    "uses_item_tag": "bebida",
                    "success": "Voce encontra agua antes da caminhada esquentar e chega mais atento a mesa.",
                    "fallback": "A sede aperta um pouco, mas Miguel divide o caminho e a cena continua.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🌅 A luz da manhã entra pela janela de madeira. Cobertor "
                        "áspero, cheiro de pão no ar. Você levanta, desorientado — "
                        "pelos telhados de telha laranja do pueblo de San Cristóbal."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¡Buenos días, forastero! ¿Dormiste bien?",
                },
                {
                    "kind": "player",
                    "text": "Você não tem resposta rápida. Mas sim — dormiu. Faz tempo que não dormia assim.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Rosa está abajo. Tiene pan fresco para nosotros.",
                },
                {
                    "kind": "scene",
                    "text": "🍞 Escada de madeira que range. Rosa na cozinha da posada — farinha nas mãos, dois pães na mesa.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "¡Hola! ¡Buenos días! Siéntate, forastero. El pan está caliente.",
                },
                {
                    "kind": "player",
                    "text": "Seu estômago ronca antes de você responder qualquer coisa.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "¡Ja! ¡Tienes hambre! Come, come.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Rosa aponta pro pão, pro seu estômago, ri de novo.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Pan. Se dice 'pan'. ¿Ves? — pan.",
                },
                {
                    "kind": "player",
                    "text": "— Pan.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¡Bien! Y el agua también. Toma.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Rosa empurrou uma tigela de barro com líquido claro e fresco. O que ela te deu?",
                    "options": [
                        {"id": "a", "text": "Agua"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "Leche"},
                        {"id": "d", "text": "Vino"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "água",
                    "npc_reaction": "Agua. Fría y buena. La mejor cosa del pueblo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O cheiro que te acordou, a coisa quente na mesa, a razão do seu estômago roncar. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Pan"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Fuego"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pão",
                    "npc_reaction": "Pan. Cada mañana, Rosa tiene pan. Ya sabe dónde venir.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você acabou de acordar, não comeu nada. Rosa aponta pra sua barriga sorrindo. O que ela disse?",
                    "options": [
                        {"id": "a", "text": "¡Tienes hambre!"},
                        {"id": "b", "text": "¡Tienes sed!"},
                        {"id": "c", "text": "¡Estás bien!"},
                        {"id": "d", "text": "¡Buenos días!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. El cuerpo pide comida. Eso todo el mundo entiende.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Sua garganta está seca depois de dormir. Don Miguel te empurra a tigela de barro. Você diria:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Me llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. El cuerpo pide agua. Ahora ya puedes decirlo.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Don Miguel leva o protagonista de volta pelo caminho do dia anterior.
    # Revisão contextual: F1 vocab em situações reais (vizinho que passa,
    # criança correndo, a plaza central). Cada exercício é uma pergunta
    # dele numa situação viva.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Ontem você chegou sem saber nada — 'forastero', sem nome, sem "
                    "idioma. Don Miguel te ensinou 'hola', 'me llamo', 'buenos días', "
                    "'buenas tardes', 'gracias', 'de nada', '¿cómo estás?', 'bien' "
                    "e 'mal'.\n\n"
                    "Esta manhã você acordou com fome, comeu pão de Rosa e bebeu "
                    "água fresca da tigela. 'Pan' e 'agua' — as duas primeiras "
                    "palavras que seu corpo pediu antes de qualquer lição."
                ),
                "now": "Don Miguel quer ver se as palavras do dia anterior grudaram.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel empurra a porta da posada. Luz forte, rua de pedra, cheiro de terra molhada.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Vamos a caminar un poco. Y tú vas a hablar — ¿eh?",
                    "translation": "Vamos caminhar um pouco. E você vai falar — tá?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Uma mulher passa pela rua carregando uma cesta. Ela sorri. Você diz:",
                    "options": [
                        {"id": "a", "text": "¡Hola!"},
                        {"id": "b", "text": "¡Gracias!"},
                        {"id": "c", "text": "¡Mal!"},
                        {"id": "d", "text": "¡Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olá",
                    "npc_reaction": "Eso. Simple y suficiente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Mira — ya son las nueve de la mañana. ¿Cómo saludas?",
                    "translation": "Olha — já são nove da manhã. Como você cumprimenta?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sol está subindo, ainda cedo. Um senhor velho de bengala te olha ao passar. Você diz:",
                    "options": [
                        {"id": "a", "text": "¡Buenos días!"},
                        {"id": "b", "text": "¡Buenas tardes!"},
                        {"id": "c", "text": "¡Buenas noches!"},
                        {"id": "d", "text": "¡Hola noche!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Bueno. El viejo Ramírez sempre responde 'buenos días' de volta. Aprendiste.",
                },
                {
                    "kind": "narrative",
                    "text": "Vocês param na beira de uma fonte de pedra no centro da plaza. Pombos na borda, água limpa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Y si alguien te pregunta cómo te llamas? ¿Qué dices?",
                    "translation": "E se alguém perguntar como você se chama? O que você fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Uma criança para e te olha com olhos curiosos: '¿Cómo te llamas?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Llamo Miguel"},
                        {"id": "c", "text": "Soy forastero"},
                        {"id": "d", "text": "Bien, gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Exacto. La niña va a repetir tu nombre a su madre esta noche.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Y cómo le respondes a alguien que te ayudó?",
                    "translation": "E como você responde a alguém que te ajudou?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um homem te ajuda a apanhar uma moeda que caiu. Você diz:",
                    "options": [
                        {"id": "a", "text": "¡Gracias!"},
                        {"id": "b", "text": "¡Hola!"},
                        {"id": "c", "text": "¡Bien!"},
                        {"id": "d", "text": "¡Buenos días!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Bien. Y él va a decir 'de nada' — ya sabes lo que viene después.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O homem sorri e responde ao seu 'gracias'. O que ele diz?",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "Gracias"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Mucho gusto"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Eso. El ciclo. Gracias — de nada. Simple.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Oye, forastero — ¿cómo estás hoy?",
                    "translation": "Ei, forasteiro — como você está hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você dormiu bem, comeu pão quente, bebeu água. Don Miguel olha pra você esperando. Você responde:",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Forastero"},
                        {"id": "d", "text": "Me llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Bien es bueno. Sigue así.",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel olha pro relógio de sol na parede da iglesia. Acena pra você continuar andando.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra você: 'Aquí eres un...' Qual palavra ele usa?",
                    "options": [
                        {"id": "a", "text": "Forastero"},
                        {"id": "b", "text": "Campesino"},
                        {"id": "c", "text": "Amigo"},
                        {"id": "d", "text": "Vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero. Por ahora. Depois de uns dias, menos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pro campo e pro próprio peito: 'Yo soy...'",
                    "options": [
                        {"id": "a", "text": "Campesino"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Doctor"},
                    ],
                    "correct": "a",
                    "word_id": "es_campesino", "target": "campesino", "native": "camponês",
                    "npc_reaction": "Eso. Toda mi vida trabajando la tierra. Como mi padre.",
                },
            ],
        },
    },

    # ── Seção 3: Gramática Narrativa ───────────────────────────────────────────
    # Don Miguel para perto de uma fonte e ensina o verbo 'tener' de forma prática:
    # tengo hambre / tengo sed / tengo [coisa]. Beats explicativos intercalados.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Vocês caminharam pelo pueblo, você cumprimentou vizinhos, "
                    "respondeu perguntas sobre seu nome, disse 'gracias' pro homem "
                    "da moeda. Don Miguel ficou satisfeito.\n\n"
                    "'Bem. As palabras de ontem ainda tão na sua cabeça. Agora tem "
                    "mais coisa pra aprender — o que acontece quando seu corpo precisa "
                    "de algo.'"
                ),
                "now": "Don Miguel vai ensinar como falar sobre o que você precisa.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel para perto da fonte, joga um pouco d'água no rosto, e te olha.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Oye — ya sabes decir 'tengo'. Sirve para lo que tienes y lo que sientes. Mira:",
                    "translation": "Ei — você já sabe falar 'tengo'. Serve para o que você tem e o que você sente. Olha:",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tengo hambre",
                    "meaning": "Estou com fome (lit: 'tenho fome')",
                    "note": "hambre = fome | tengo = eu tenho / sinto",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y si es agua lo que pide el cuerpo:",
                    "translation": "E se é água que o corpo pede:",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tengo sed",
                    "meaning": "Estou com sede (lit: 'tenho sede')",
                    "note": "sed = sede | mesmo padrão: tengo + o que falta",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Tengo",  "isKey": True},
                        {"text": " + ",    "isKey": False},
                        {"text": "hambre", "isKey": True},
                        {"text": " / ",    "isKey": False},
                        {"text": "sed",    "isKey": True},
                    ],
                    "example": "Tengo hambre — dame pan. / Tengo sed — dame agua.",
                    "translation": "Estou com fome — me dá pão. / Estou com sede — me dá água.",
                    "note": "O corpo sempre pede. Agora você pode nomear o que pede.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você não come desde ontem à noite. Estômago vazio, cabeça leve. Como você fala?",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Me llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. El cuerpo habla primero.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y el agua — la boca seca, la garganta apretada. ¿Cómo se llama?",
                    "translation": "E a água — boca seca, garganta apertada. Como se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sol da manhã já esquenta. Você caminhou bastante. A boca está seca. Você diz:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Tengo pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. Agua — ahí. Siempre hay en la fuente.",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel coloca as mãos nos joelhos, levanta. 'Bien. Agora o corpo fala. Você responde.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra fonte: 'Aquí está el agua fría.' Você estava com sede. O que você tem agora?",
                    "options": [
                        {"id": "a", "text": "Agua"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Leche"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "água",
                    "npc_reaction": "Agua. Y ahora ya no tienes sed.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Rosa vai te dar algo pra comer mais tarde. O que ela sempre tem fresquinho?",
                    "options": [
                        {"id": "a", "text": "Pan"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Vino"},
                        {"id": "d", "text": "Leche"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pão",
                    "npc_reaction": "Pan. El suyo es el mejor del pueblo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um menino passa correndo e para, ofegante. Don Miguel faz sinal que o menino pode falar. O menino diz 'Tengo sed!' — o que ele precisa?",
                    "options": [
                        {"id": "a", "text": "Agua"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "Descanso"},
                        {"id": "d", "text": "Hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "água",
                    "npc_reaction": "Agua. Oyó 'tengo sed' y supo lo que necesitaba. Igual que tú ahora.",
                },
            ],
        },
    },

    # ── Seção 4: Prática Aplicada ─────────────────────────────────────────────
    # Pratica intensa do vocab novo (pan/agua/tengo hambre/tengo sed) junto com
    # F1 vocab em situações reais. NPC presente em cada exercício, rapidez de fogo.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel te ensinou 'tengo hambre' e 'tengo sed' — as duas "
                    "primeiras frases que seu próprio corpo pediu esta manhã. 'Pan' "
                    "pra comida, 'agua' pra bebida. Ele disse que agora vai praticar "
                    "até sair sem pensar."
                ),
                "now": "Prática rápida — Don Miguel manda situação, você responde.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Vamos rápido. Yo digo la situación, tú usas la palabra. ¿Listo?",
                    "translation": "Vamos rápido. Eu digo a situação, você usa a palavra. Pronto?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você não come desde a manhã. São três da tarde. Você fala pra Don Miguel:",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. Vamos buscar pan.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Rosa te passa um pedaço de pão. Você responde:",
                    "options": [
                        {"id": "a", "text": "¡Gracias!"},
                        {"id": "b", "text": "¡Hola!"},
                        {"id": "c", "text": "¡Bien!"},
                        {"id": "d", "text": "¡Mal!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Rosa sorri. 'De nada, hijo.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel vê você comendo o pão. Ele pergunta: '¿Cómo estás ahora?'",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Pan e 'bien' andam juntos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O caminheiro que passou antes era de fora do pueblo — olhos diferentes, não conhece as ruas. Don Miguel aponta: 'Ese hombre es un...'",
                    "options": [
                        {"id": "a", "text": "Forastero"},
                        {"id": "b", "text": "Campesino"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Doctor"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero. Como eras ayer. Pero menos ahora, ¿no?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Oye — ¿y yo? ¿Qué soy yo en este pueblo?",
                    "translation": "Ei — e eu? O que sou eu nesse pueblo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel espalha a terra dos sapatos na calçada. Trabalha no campo toda a vida. Ele é:",
                    "options": [
                        {"id": "a", "text": "Campesino"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Doctor"},
                        {"id": "d", "text": "Maestro"},
                    ],
                    "correct": "a",
                    "word_id": "es_campesino", "target": "campesino", "native": "camponês",
                    "npc_reaction": "Eso. Campesino. Toda mi vida.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y si llega un nuevo forastero — ¿qué le dices primero?",
                    "translation": "E se chega um novo forasteiro — o que você fala primeiro?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um homem novo chega pelo portão do pueblo, perdido. Você vai até ele e diz:",
                    "options": [
                        {"id": "a", "text": "¡Hola! ¿Cómo te llamas?"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Buenos noches"},
                        {"id": "d", "text": "De nada"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olá",
                    "npc_reaction": "¡Así es! Hola abre a conversa. Nome vem depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sol está a pino, calor forte. Você e Miguel caminharam muito. Sua garganta está seca. Você fala:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. Agua aí na fonte. Já sabe o caminho.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel tira uma maçã do bolso e te oferece. Mas você precisa de água, não de comida. Você diz:",
                    "options": [
                        {"id": "a", "text": "Tengo sed, agua"},
                        {"id": "b", "text": "Tengo hambre, gracias"},
                        {"id": "c", "text": "De nada"},
                        {"id": "d", "text": "Bien, gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Agua. Claro. La manzana queda para después.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você vai até a fonte e bebe. Voltando, Don Miguel: '¿Y ahora, forastero?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo sed"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Agua fría é isso.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ───────────────────────────────────────────────────────
    # Tarde na plaza. Rosa reaparece com pão sobrando da padaria.
    # História usa o vocab de F1+F2 de forma orgânica — menos aula, mais vida.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Rosa"],
                "story": (
                    "Depois de uma manhã praticando, vocês voltaram pra plaza. O sol "
                    "ainda alto, sombra das árvores. Don Miguel deixou você descansar "
                    "enquanto ele foi falar com um vizinho.\n\n"
                    "Rosa aparece do nada carregando uma cesta com pão que sobrou "
                    "da padaria."
                ),
                "now": "Uma conversa real com Rosa e Miguel — sem exercício, só vida.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Rosa chega pela sombra das árvores, cesta no braço, cabelos presos com um pano.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "¡Miguel! ¡Forastero! Tengo pan que sobró. ¿Quieren?",
                    "translation": "Miguel! Forasteiro! Tenho pão que sobrou. Vocês querem?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¡Rosa! Sí, claro. El forastero tiene hambre desde esta mañana.",
                    "translation": "Rosa! Sim, claro. O forasteiro está com fome desde essa manhã.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa estende um pão pra você direto. Ela está te oferecendo o quê?",
                    "options": [
                        {"id": "a", "text": "Pan"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Fruta"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pão",
                    "npc_reaction": "Pan. Pega, pega.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Rosa esperou você pegar o pão e ficou olhando. O que você fala pra ela?",
                    "options": [
                        {"id": "a", "text": "¡Gracias!"},
                        {"id": "b", "text": "¡Hola!"},
                        {"id": "c", "text": "¡Bien!"},
                        {"id": "d", "text": "¡Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, hijo. Siempre hay pan para quien lo necesita.",
                },
                {
                    "kind": "narrative",
                    "text": "Rosa se senta no banco ao lado, tira um pão pra ela mesma. Don Miguel inclina o chapéu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "¿Y el forastero — cómo se llama?",
                    "translation": "E o forasteiro — como ele se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa olha pra você esperando. Ela quer saber seu nome. O que você fala?",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Soy campesino"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto. Yo soy Rosa. Ya sé que começa pelo pan.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "¡Buenas tardes! — digo yo cuando ya pasa el almuerzo. ¿Cómo estás?",
                    "translation": "Boa tarde! — digo eu quando já passou o almoço. Como você está?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa te pergunta diretamente: '¿Cómo estás?' com um sorriso genuíno. Você responde:",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Con pan y agua siempre estás bien.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel ri de algo que Rosa disse baixinho. O pueblo vai "
                        "ganhando ritmo — sinos da iglesia ao longe, crianças correndo, "
                        "o cheiro de terra molhada voltando com a brisa da tarde."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sino da iglesia bateu seis vezes. O sol está baixo. Como Don Miguel vai cumprimentar o próximo vizinho que passar?",
                    "options": [
                        {"id": "a", "text": "¡Buenas tardes!"},
                        {"id": "b", "text": "¡Buenos días!"},
                        {"id": "c", "text": "¡Buenas noches!"},
                        {"id": "d", "text": "¡Hola noche!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_tardes", "target": "buenas tardes", "native": "boa tarde",
                    "npc_reaction": "Buenas tardes. El sol te dice cuándo cambiar.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Entardecer. Don Miguel precisa falar com um vizinho — deixa o protagonista
    # sozinho por alguns minutos num ponto da rua. Uma criança passa com sede,
    # um senhor pergunta onde fica a posada, um homem novo (futuro antagonista)
    # passa e olha demais.
    # Seção gated: errar trava. O protagonista está só — precisa se virar.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Rosa foi embora com a cesta vazia. Don Miguel avistou um vizinho "
                    "no outro lado da plaza — alguém que ele precisa falar. 'Espera "
                    "aqui dois minutos. Não vai a lugar nenhum.' E foi."
                ),
                "now": "Você está sozinho. O pueblo continua ao redor. Tem que se virar.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel some pela sombra das árvores. Você está parado na beira da plaza, sozinho pela primeira vez no pueblo.",
                },
                {
                    "kind": "scene",
                    "text": "🌇 A luz fica alaranjada. Uma criança de uns seis anos corre até você e para — bochechas vermelhas, respiração ofegante.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Niña",
                    "line": "¡Señor! ¿Tienes agua? ¡Tengo sed!",
                    "translation": "Senhor! Você tem água? Estou com sede!",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Niña",
                    "question": "A menina disse '¡Tengo sed!' e olhou pra sua cantil. Ela precisa de:",
                    "options": [
                        {"id": "a", "text": "Agua"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Descanso"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "água",
                    "npc_reaction": "¡Agua! Entendiste 'tengo sed'. Dale la cantimplora.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "A menina bebe, devolve a cantil com um sorriso enorme e sai correndo. Você ficou sem água, mas com um sorriso no rosto.",
                },
                {
                    "kind": "scene",
                    "text": "🧓 Um senhor idoso se aproxima com um mapa dobrado na mão — parece perdido.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Señor Mayor",
                    "line": "Joven, ¿cómo estás? ¿Sabes dónde está la posada?",
                    "translation": "Jovem, como vai? Sabe onde fica a posada?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Señor Mayor",
                    "question": "O senhor perguntou '¿Cómo estás?' antes de pedir ajuda. Como você responde primeiro?",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Buenos noches"},
                        {"id": "d", "text": "Me llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "El señor asiente satisfecho. Ahora puedes intentar explicar dónde está la posada.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Você aponta pro caminho que Don Miguel te mostrou ontem — a casa de dois andares no canto da plaza. O senhor agradece e vai embora.",
                },
                {
                    "kind": "scene",
                    "text": "🚶 Um homem para na entrada da plaza. Chapéu baixo. Olha pra você por tempo demais antes de seguir em frente.",
                },
                {
                    "kind": "narrative",
                    "text": "Algo no jeito dele não estava certo. Mas você não tem palavra pra isso ainda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel voltou. 'Forastero — ¿cómo estás? ¿Todo bien?' Você responde honestamente:",
                    "options": [
                        {"id": "a", "text": "Bien... pero hay algo raro"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Hola, buenos días"},
                        {"id": "d", "text": "De nada"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Miguel mira hacia el mismo lado que tú. Frunce el ceño un segundo. Después: 'Vamos a la posada.'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Bien hecho, forastero. Estuviste solo y te manejaste.",
                    "translation": "Bem feito, forasteiro. Ficou sozinho e se virou.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês caminham de volta pra posada. As janelas acendem uma a "
                        "uma. Don Miguel não fala nada sobre o homem do chapéu baixo.\n\n"
                        "Mas você viu ele olhar pro mesmo lado que você olhou."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
