"""
Seed das 6 seções da Fase 2 Italiano A1 — "Il Borgo Desperta".

Dia seguinte à chegada. Antonio mostra a locanda pela manhã, leva o
protagonista por um circuito curto pelo borgo e ensina as primeiras
necessidades físicas: ho fame, ho sete, pane, acqua.

Novos vocab (2): pane · acqua · ho fame · ho sete
Revisão F1: ciao, buongiorno, grazie, prego, mi chiamo, come stai?, bene/male, straniero
NPC principal:   Antonio (fio condutor)
NPC cameo:       Giulia la Fornaia (reaparece brevemente)
Itens:           pane_fresco (word_id: it_pane) · acqua_del_pozo (word_id: it_acqua)
Arco emocional:  desorientado → começa a entender o ritmo do borgo
Transição:       anoitecer na locanda; uma sombra passa pela janela — alguém observou

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Manhã na locanda. Protagonista acorda sem saber onde est? — cheiro de pão,
    # luz pela janela. Antonio chega, Giulia aparece com pão quente.
    # Falas dos NPCs SEM tradução — imersão. Exercícios: reconhecimento contextual.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌅 A luz da manhã entra pela janela de madeira. Cobertor "
                        "Cama, cheiro de pão no ar. Você levanta, desorientado — "
                        "pelos telhados de telha terracota do borgo de Santa Chiara."
                    ),
                },
                {
                    "kind": "skill_check",
                    "skill": "agua",
                    "min_level": 1,
                    "uses_item_tag": "bebida",
                    "success": "Voce percebe cedo quem esta com sede e evita que a caminhada perca ritmo.",
                    "fallback": "A sede pesa por alguns minutos, mas o grupo reduz o passo e continua.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Buongiorno, straniero! Dormiste bene?",
                },
                {
                    "kind": "player",
                    "text": "Você não tem resposta r?pida. Mas sim — dormiu. Faz tempo que não dormia assim.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Giulia est? abajo. Tiene pane fresco para nosotros.",
                },
                {
                    "kind": "scene",
                    "text": "?? Escada de madeira que range. Giulia na cozinha da locanda — farinha nas mãos, dois pães na mesa.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Ciao! Buongiorno! Siéntate, straniero. El pane est? caliente.",
                },
                {
                    "kind": "player",
                    "text": "Seu estômago ronca antes de você responder qualquer coisa.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Ja! Hai fame! Mangia, mangia.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Giulia aponta pro pão, pro seu estômago, ri de novo.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Pane. Se dice 'pane'. Ves?— pane.",
                },
                {
                    "kind": "player",
                    "text": "— Pane.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Bene! Y el acqua también. Toma.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Giulia empurrou uma tigela de barro com líquido claro e fresco. O que ela te deu?",
                    "options": [
                        {"id": "a", "text": "Acqua"},
                        {"id": "b", "text": "Pane"},
                        {"id": "c", "text": "Leche"},
                        {"id": "d", "text": "Vino"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "?gua",
                    "npc_reaction": "Acqua. Fría y buena. La mejor cosa del borgo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O cheiro que te acordou, a coisa quente na mesa, a razão do seu estômago roncar. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Pane"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Fuoco"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pão",
                    "npc_reaction": "Pane. Cada domani, Giulia tiene pane. Sa gia dónde venir.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você acabou de acordar, não comeu nada. Giulia aponta pra sua barriga sorrindo. O que ela disse?",
                    "options": [
                        {"id": "a", "text": "Hai fame!"},
                        {"id": "b", "text": "Hai sete!"},
                        {"id": "c", "text": "Stai bene!"},
                        {"id": "d", "text": "Buongiorno!"},
                    ],
                    "correct": "a",
                    "word_id": "it_hambre", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Hambre. El cuerpo pide comida. Eso todo el mundo entiende.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Sua garganta est? seca depois de dormir. Antonio te empurra a tigela de barro. Você diria:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Estoy bene"},
                        {"id": "d", "text": "Mi chiamo"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. El cuerpo pide acqua. Ora ya puedes decirlo.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Antonio leva o protagonista de volta pelo caminho do dia anterior.
    # Revisão contextual: F1 vocab em situações reais (vizinho que passa,
    # criança corrindo, a piazza central). Cada exercício é uma pergunta
    # dele numa situação viva.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Ontem você chegou sem saber nada — 'straniero', sem nome, sem "
                    "idioma. Antonio te ensinou 'ciao', 'mi chiamo', 'buongiorno', "
                    "'buonasera', 'grazie', 'prego', 'come stai?', 'bene' "
                    "e 'male'.\n\n"
                    "Esta manhã você acordou com fome, comeu pão de Giulia e bebeu "
                    "?gua fresca da tigela. 'Pane' e 'acqua' — as duas primeiras "
                    "palavras que seu corpo pediu antes de qualquer lição."
                ),
                "now": "Antonio quer ver se as palavras do dia anterior grudaram.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio empurra a porta da locanda. Luz forte, rua de pedra, cheiro de terra molhada.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Andiamo a camminare un poco. E tu parlerai, eh?",
                    "translation": "Vamos caminhar um pouco. E você vai falar — t??",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Uma mulher passa pela rua carregando uma cesta. Ela sorri. Você diz:",
                    "options": [
                        {"id": "a", "text": "Ciao!"},
                        {"id": "b", "text": "Grazie!"},
                        {"id": "c", "text": "Male!"},
                        {"id": "d", "text": "Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "it_ciao", "target": "ciao", "native": "ol?",
                    "npc_reaction": "Eso. Simple y suficiente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Guarda — ya son las nueve de la domani. Cómo saludas?",
                    "translation": "Olha — j? são nove da manhã. Como você cumprimenta?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O sol est? subindo, ainda cedo. Um senhor velho de bengala te olha ao passar. Você diz:",
                    "options": [
                        {"id": "a", "text": "Buongiorno!"},
                        {"id": "b", "text": "Buonasera!"},
                        {"id": "c", "text": "Buonanotte!"},
                        {"id": "d", "text": "Ciao noche!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Bueno. El viejo Ramírez sempre responde 'buongiorno' de volta. Aprendiste.",
                },
                {
                    "kind": "narrative",
                    "text": "Vocês param na beira de uma fonte de pedra no centro da piazza. Pombos na borda, ?gua limpa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E se qualcuno ti chiede come ti chiami?Che dici?",
                    "translation": "E se alguém perguntar como você se chama?O que você fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Uma criança para e te olha com olhos curiosos: 'Come ti chiami?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Llamo Nico"},
                        {"id": "c", "text": "Soy straniero"},
                        {"id": "d", "text": "Bene, grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Exacto. La niña vai repetir seu nome pra mãe dela hoje à noite.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E come rispondi a alguien que te ayudó?",
                    "translation": "E como você responde a alguém que te ajudou?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um homem te ajuda a apanehar uma moeda que caiu. Você diz:",
                    "options": [
                        {"id": "a", "text": "Grazie!"},
                        {"id": "b", "text": "Ciao!"},
                        {"id": "c", "text": "Bene!"},
                        {"id": "d", "text": "Buongiorno!"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Bene. Y ele vai falar 'prego' — j? sabe o que vem depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O homem sorri e responde ao seu 'grazie'. O que ele diz?",
                    "options": [
                        {"id": "a", "text": "Prego"},
                        {"id": "b", "text": "Grazie"},
                        {"id": "c", "text": "Ciao"},
                        {"id": "d", "text": "Piacere"},
                    ],
                    "correct": "a",
                    "word_id": "it_de_nada", "target": "prego", "native": "prego",
                    "npc_reaction": "Eso. El ciclo. Grazie — prego. Simple.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ehi, straniero — come stai oggi?",
                    "translation": "Ei, straniero — como você est? hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você dormiu bem, comeu pão quente, bebeu ?gua. Antonio olha pra você esperando. Você responde:",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Straniero"},
                        {"id": "d", "text": "Mi chiamo"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bueno. Bem é bom. Continua assim.",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio olha pro relógio de sol na parede da iglesia. Acena pra você continuar andando.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra você: 'Aquí eres un...' Qual palavra ele usa?",
                    "options": [
                        {"id": "a", "text": "Straniero"},
                        {"id": "b", "text": "Contadino"},
                        {"id": "c", "text": "Amico"},
                        {"id": "d", "text": "Vecino"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "Straniero. Por ora. Depois de uns dias, menos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pro campo e pro próprio peito: 'Io sono...'",
                    "options": [
                        {"id": "a", "text": "Contadino"},
                        {"id": "b", "text": "Straniero"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Doctor"},
                    ],
                    "correct": "a",
                    "word_id": "it_contadino", "target": "contadino", "native": "camponês",
                    "npc_reaction": "Eso. Toda mi vida trabajando la tierra. Como mi padre.",
                },
            ],
        },
    },

    # ── Seção 3: Gram?tica Narrativa ───────────────────────────────────────────
    # Antonio para perto de uma fonte e ensina o verbo 'tener' de forma pr?tica:
    # ho fame / ho sete / ho [coisa]. Beats explicativos intercalados.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Vocês caminharam pelo borgo, você cumprimentou vizinhos, "
                    "respondeu perguntas sobre seu nome, disse 'grazie' pro homem "
                    "da moeda. Antonio ficou satisfeito.\n\n"
                    "'Bem. As palabras de ontem ainda tão na sua cabeça. Agora tem "
                    "mais coisa pra aprender — o que acontece quando seu corpo precisa "
                    "de algo.'"
                ),
                "now": "Antonio vai ensinar como falar sobre o que você precisa.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio para perto da fonte, joga um pouco d'?gua no rosto, e te olha.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Oye — sabes decir 'ho'. 'Ho' es 'eu tenho' o 'eu sinto'. Guarda:",
                    "translation": "Ei — você sabe falar 'ho'. 'Ho' é 'eu tenho' ou 'eu sinto'. Olha:",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ho fame",
                    "meaning": "Estou com fome (lit: 'tenho fome')",
                    "note": "hambre = fome | ho = eu tenho / sinto",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y si es acqua lo que pide el cuerpo:",
                    "translation": "E se é ?gua que o corpo pede:",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ho sete",
                    "meaning": "Estou com sede (lit: 'tenho sede')",
                    "note": "sed = sede | mesmo padrão: ho + o que falta",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Ho",  "isKey": True},
                        {"text": " + ",    "isKey": False},
                        {"text": "hambre", "isKey": True},
                        {"text": " / ",    "isKey": False},
                        {"text": "sed",    "isKey": True},
                    ],
                    "example": "Ho fame — dame pane. / Ho sete — dame acqua.",
                    "translation": "Estou com fome — me d? pão. / Estou com sede — me d? ?gua.",
                    "note": "O corpo sempre pede. Agora você pode nomear o que pede.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você não come desde ontem à noite. Estômago vazio, cabeça leve. Como você fala?",
                    "options": [
                        {"id": "a", "text": "Ho fame"},
                        {"id": "b", "text": "Ho sete"},
                        {"id": "c", "text": "Estoy bene"},
                        {"id": "d", "text": "Mi chiamo"},
                    ],
                    "correct": "a",
                    "word_id": "it_hambre", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Hambre. Il corpo parla per primo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y el acqua — la boca seca, la garganta apretada. Cómo se llama?",
                    "translation": "E a ?gua — boca seca, garganta apertada. Como se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O sol da manhã j? esquenta. Você caminhou bastante. A boca est? seca. Você diz:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Estoy male"},
                        {"id": "d", "text": "Ho pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. Acqua — aí. Sempre tem na fonte.",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio coloca as mãos nos joelhos, levanta. 'Bene. Agora o corpo fala. Você responde.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra fonte: 'Aquí est? el acqua fría.' Você estava com sede. O que você tem agora?",
                    "options": [
                        {"id": "a", "text": "Acqua"},
                        {"id": "b", "text": "Pane"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Leche"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "?gua",
                    "npc_reaction": "Acqua. E ora ya no hai sete.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Giulia vai te dar algo pra comer mais tarde. O que ela sempre tem fresquinho?",
                    "options": [
                        {"id": "a", "text": "Pane"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Vino"},
                        {"id": "d", "text": "Leche"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pão",
                    "npc_reaction": "Pane. El suyo es el mejor del borgo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um menino passa corrindo e para, ofegante. Antonio faz sinal que o menino pode falar. O menino diz 'Ho sete!' — o que ele precisa?",
                    "options": [
                        {"id": "a", "text": "Acqua"},
                        {"id": "b", "text": "Pane"},
                        {"id": "c", "text": "Descanso"},
                        {"id": "d", "text": "Hambre"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "?gua",
                    "npc_reaction": "Acqua. Oyó 'ho sete' y supo lo que necesitaba. Igual que tú ora.",
                },
            ],
        },
    },

    # ── Seção 4: Pr?tica Aplicada ─────────────────────────────────────────────
    # Pratica intensa do vocab novo (pane/acqua/ho fame/ho sete) junto com
    # F1 vocab em situações reais. NPC presente em cada exercício, rapidez de fogo.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Antonio te ensinou 'ho fame' e 'ho sete' — as duas "
                    "primeiras frases que seu próprio corpo pediu esta manhã. 'Pane' "
                    "pra comida, 'acqua' pra bebida. Ele disse que agora vai praticar "
                    "até sair sem pensar."
                ),
                "now": "Pr?tica r?pida — Antonio manda situação, você responde.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Facciamo veloce. Io dico la situazione, tu usi la parola. Pronto?",
                    "translation": "Vamos r?pido. Eu digo a situação, você usa a palavra. Pronto?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você não come desde a manhã. São três da tarde. Você fala pra Antonio:",
                    "options": [
                        {"id": "a", "text": "Ho fame"},
                        {"id": "b", "text": "Ho sete"},
                        {"id": "c", "text": "Estoy bene"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_hambre", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Hambre. Vamos buscar pane.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Giulia te passa um pedaço de pão. Você responde:",
                    "options": [
                        {"id": "a", "text": "Grazie!"},
                        {"id": "b", "text": "Ciao!"},
                        {"id": "c", "text": "Bene!"},
                        {"id": "d", "text": "Male!"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Giulia sorri. 'Prego, figlio.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio vê você comendo o pão. Ele pergunta: 'Come stai ora?'",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Straniero"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Pane e 'bene' andam juntos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O caminheiro que passou antes era de fora do borgo — olhos diferentes, não conhece as ruas. Antonio aponta: 'Ese hombre es un...'",
                    "options": [
                        {"id": "a", "text": "Straniero"},
                        {"id": "b", "text": "Contadino"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Doctor"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "Straniero. Como você era ontem. Mas menos agora, no?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ehi, e io?Che cosa sono io in questo borgo?",
                    "translation": "Ei — e eu?O que sou eu nesse borgo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio espalha a terra dos sapatos na calçada. Trabalha no campo toda a vida. Ele é:",
                    "options": [
                        {"id": "a", "text": "Contadino"},
                        {"id": "b", "text": "Straniero"},
                        {"id": "c", "text": "Doctor"},
                        {"id": "d", "text": "Maestro"},
                    ],
                    "correct": "a",
                    "word_id": "it_contadino", "target": "contadino", "native": "camponês",
                    "npc_reaction": "Eso. Contadino. Toda mi vida.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E se arriva un nuovo straniero, che cosa gli dici per prima cosa?",
                    "translation": "E se chega um novo straniero — o que você fala primeiro?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um homem novo chega pelo portão do borgo, perdido. Você vai até ele e diz:",
                    "options": [
                        {"id": "a", "text": "Ciao! Come ti chiami?"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Buonanotte"},
                        {"id": "d", "text": "Prego"},
                    ],
                    "correct": "a",
                    "word_id": "it_ciao", "target": "ciao", "native": "ol?",
                    "npc_reaction": "Así es! Ciao abre a conversa. Nome vem depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O sol est? a pino, calor forte. Você e Nico caminharam muito. Sua garganta est? seca. Você fala:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Estoy male"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. Acqua aí na fonte. J? sabe o caminho.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio tira uma maçã do bolso e te oferece. Mas você precisa de ?gua, não de comida. Você diz:",
                    "options": [
                        {"id": "a", "text": "Ho sete, acqua"},
                        {"id": "b", "text": "Ho fame, grazie"},
                        {"id": "c", "text": "Prego"},
                        {"id": "d", "text": "Bene, grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Acqua. Claro. A maçã fica pra depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você vai até a fonte e bebe. Voltando, Antonio: 'E ora, straniero?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Bene"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho sete"},
                        {"id": "d", "text": "Straniero"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Acqua fría é isso.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ───────────────────────────────────────────────────────
    # Tarde na piazza. Giulia reaparece com pão sobrando da padaria.
    # História usa o vocab de F1+F2 de forma orgânica — menos aula, mais vida.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio", "Giulia"],
                "story": (
                    "Depois de uma manhã praticando, vocês voltaram pra piazza. O sol "
                    "ainda alto, sombra das ?rvores. Antonio deixou você descansar "
                    "enquanto ele foi falar com um vizinho.\n\n"
                    "Giulia aparece do nada carregando uma cesta com pão que sobrou "
                    "da padaria."
                ),
                "now": "Uma conversa real com Giulia e Nico — sem exercício, só vida.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Giulia chega pela sombra das ?rvores, cesta no braço, cabelos presos com um paneo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Nico! Straniero! Ho pane que sobró. Vuolen?",
                    "translation": "Nico! Forasteiro! Tenho pão que sobrou. Vocês querem?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Giulia! Sí, claro. El straniero tiene hambre desde esta domani.",
                    "translation": "Giulia! Sim, claro. O straniero est? com fome desde essa manhã.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia estende um pão pra você direto. Ela est? te oferecendo o quê?",
                    "options": [
                        {"id": "a", "text": "Pane"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Fruta"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pão",
                    "npc_reaction": "Pane. Pega, pega.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Giulia esmau você pegar o pão e ficou olhando. O que você fala pra ela?",
                    "options": [
                        {"id": "a", "text": "Grazie!"},
                        {"id": "b", "text": "Ciao!"},
                        {"id": "c", "text": "Bene!"},
                        {"id": "d", "text": "Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Prego, figlio. Siempre c'e pane pra quem precisa.",
                },
                {
                    "kind": "narrative",
                    "text": "Giulia se senta no banco ao lado, tira um pão pra ela mesma. Antonio inclina o chapéu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Y el straniero — cómo se llama?",
                    "translation": "E o straniero — como ele se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia olha pra você esperando. Ela quer saber seu nome. O que você fala?",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Bene, grazie"},
                        {"id": "d", "text": "Soy contadino"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Piacere. Io sono Giulia. So gia que começa pelo pane.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Buonasera! Lo dico quando il pranzo e gia passato. Come stai?",
                    "translation": "Boa tarde! — digo eu quando j? passou o almoço. Como você est??",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia te pergunta diretamente: 'Come stai?' com um sorriso genuíno. Você responde:",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Con pane y acqua siempre stai bene.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio ri de algo que Giulia disse baixinho. O borgo vai "
                        "ganhando ritmo — sinos da iglesia ao longe, crianças corrindo, "
                        "o cheiro de terra molhada voltando com a brisa da tarde."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O sino da iglesia bateu seis vezes. O sol est? baixo. Como Antonio vai cumprimentar o próximo vizinho que passar?",
                    "options": [
                        {"id": "a", "text": "Buonasera!"},
                        {"id": "b", "text": "Buongiorno!"},
                        {"id": "c", "text": "Buonanotte!"},
                        {"id": "d", "text": "Ciao noche!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenas_tardes", "target": "buonasera", "native": "boa tarde",
                    "npc_reaction": "Buonasera. El sol te dice cu?ndo cambiar.",
                },
            ],
        },
    },

    # ── Seção 6: Obst?culo ────────────────────────────────────────────────────
    # Entardecer. Antonio precisa falar com um vizinho — deixa o protagonista
    # sozinho por alguns minutos num ponto da rua. Uma criança passa com sede,
    # um senhor pergunta onde fica a locanda, um homem novo (futuro antagonista)
    # passa e olha demais.
    # Seção gated: errar trava. O protagonista est? só — precisa se virar.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Giulia foi embora com a cesta vazia. Antonio avistou um vizinho "
                    "no outro lado da piazza — alguém que ele precisa falar. 'Espera "
                    "aqui dois minutos. Não vai a lugar nenhum.' E foi."
                ),
                "now": "Você est? sozinho. O borgo continua ao redor. Tem que se virar.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio some pela sombra das ?rvores. Você est? parado na beira da piazza, sozinho pela primeira vez no borgo.",
                },
                {
                    "kind": "scene",
                    "text": "🌇 A luz fica alaranjada. Uma criança de uns seis anos corri até você e para — bochechas vermelhas, respiração ofegante.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Niña",
                    "line": "Signore! Tienes acqua?Ho sete!",
                    "translation": "Senhor! Você tem ?gua?Estou com sede!",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Niña",
                    "question": "A menina disse 'Ho sete!' e olhou pra sua cantil. Ela precisa de:",
                    "options": [
                        {"id": "a", "text": "Acqua"},
                        {"id": "b", "text": "Pane"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Descanso"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "?gua",
                    "npc_reaction": "Água! Você entendeu 'ho sete'. D? a cantil pra ela.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "A menina bebe, devolve a cantil com um sorriso enorme e sai corrindo. Você ficou sem ?gua, mas com um sorriso no rosto.",
                },
                {
                    "kind": "scene",
                    "text": "🧓 Um senhor idueo se aproxima com um mapa dobrado na mão — parece perdido.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Signore Anziano",
                    "line": "Joven, come stai?Sabes dónde est? la locanda?",
                    "translation": "Jovem, como vai?Sabe onde fica a locanda?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Signore Anziano",
                    "question": "O senhor perguntou 'Come stai?' antes de pedir ajuda. Como você responde primeiro?",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Ho sete"},
                        {"id": "c", "text": "Buonanotte"},
                        {"id": "d", "text": "Mi chiamo"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "O senhor acena satisfeito. Agora você pode tentar explicar onde fica a locanda.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Você aponta pro caminho que Antonio te mostrou ontem — a casa de dois andares no canto da piazza. O senhor agradece e vai embora.",
                },
                {
                    "kind": "scene",
                    "text": "🚶 Um homem para na entrada da piazza. Chapéu baixo. Olha pra você por tempo demais antes de seguir em frente.",
                },
                {
                    "kind": "narrative",
                    "text": "Algo no jeito dele não estava certo. Mas você não tem palavra pra isso ainda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio voltou. 'Straniero — come stai?Todo bene?' Você responde honestamente:",
                    "options": [
                        {"id": "a", "text": "Bene... ma c'e algo raro"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Ciao, buongiorno"},
                        {"id": "d", "text": "Prego"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Nico olha pro mesmo lado que você olhou. Franze a testa um segundo. Depois: 'Vamos pra locanda.'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Bene hecho, straniero. Estuviste solo y te manejaste.",
                    "translation": "Bem feito, straniero. Ficou sozinho e se virou.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês caminham de volta pra locanda. As janelas acendem uma a "
                        "uma. Antonio não fala nada sobre o homem do chapéu baixo.\n\n"
                        "Mas você viu ele olhar pro mesmo lado que você olhou."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
