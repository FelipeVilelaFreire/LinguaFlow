"""
Seed das 6 seÃ§Ãµes da Fase 2 Italiano A1 â€” "Il Borgo Desperta".

Dia seguinte Ã  chegada. Antonio mostra a locanda pela manhÃ£, leva o
protagonista por um circuito curto pelo borgo e ensina as primeiras
necessidades fÃ­sicas: ho fame, ho sete, pane, acqua.

Novos vocab (2): pane · acqua · ho fame · ho sete
RevisÃ£o F1: ciao, buongiorno, grazie, prego, mi chiamo, come stai?, bene/male, straniero
NPC principal:   Antonio (fio condutor)
NPC cameo:       Giulia la Fornaia (reaparece brevemente)
Itens:           pane_fresco (word_id: it_pane) · acqua_del_pozo (word_id: it_acqua)
Arco emocional:  desorientado â†’ comeÃ§a a entender o ritmo do borgo
TransiÃ§Ã£o:       anoitecer na locanda; uma sombra passa pela janela â€” alguÃ©m observou

PrÃ©-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # ManhÃ£ na locanda. Protagonista acorda sem saber onde estÃ â€” cheiro de pÃ£o,
    # luz pela janela. Antonio chega, Giulia aparece com pÃ£o quente.
    # Falas dos NPCs SEM traduÃ§Ã£o â€” imersÃ£o. ExercÃ­cios: reconhecimento contextual.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ… A luz da manhÃ£ entra pela janela de madeira. Cobertor "
                        "Ãsma, cheiro de pÃ£o no ar. VocÃª levanta, desorientado â€” "
                        "pelos telhados de telha terracota do borgo de Santa Chiara."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Buongiorno, straniero! Dormiste bene?",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o tem resposta rÃpida. Mas sim â€” dormiu. Faz tempo que nÃ£o dormia assim.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Giulia estÃ abajo. Tiene pane fresco para nosotros.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸž Escada de madeira que range. Giulia na cozinha da locanda â€” farinha nas mÃ£os, dois pÃ£es na mesa.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Ciao! Buongiorno! SiÃ©ntate, straniero. El pane estÃ caliente.",
                },
                {
                    "kind": "player",
                    "text": "Seu estÃ´mago ronca antes de vocÃª responder qualquer coisa.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Ja! Hai fame! Mangia, mangia.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Giulia aponta pro pÃ£o, pro seu estÃ´mago, ri de novo.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Pane. Se dice 'pane'. Ves? â€” pane.",
                },
                {
                    "kind": "player",
                    "text": "â€” Pane.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Bene! Y el acqua tambiÃ©n. Toma.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Giulia empurrou uma tigela de barro com lÃ­quido claro e fresco. O que ela te deu?",
                    "options": [
                        {"id": "a", "text": "Acqua"},
                        {"id": "b", "text": "Pane"},
                        {"id": "c", "text": "Leche"},
                        {"id": "d", "text": "Vino"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "Ãgua",
                    "npc_reaction": "Acqua. FrÃ­a y buena. La mejor cosa del borgo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O cheiro que te acordou, a coisa quente na mesa, a razÃ£o do seu estÃ´mago roncar. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Pane"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Fuoco"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pÃ£o",
                    "npc_reaction": "Pane. Cada domani, Giulia tiene pane. Sa gia dÃ³nde venir.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª acabou de acordar, nÃ£o comeu nada. Giulia aponta pra sua barriga sorrindo. O que ela disse?",
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
                    "question": "Sua garganta estÃ seca depois de dormir. Antonio te empurra a tigela de barro. VocÃª diria:",
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

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Antonio leva o protagonista de volta pelo caminho do dia anterior.
    # RevisÃ£o contextual: F1 vocab em situaÃ§Ãµes reais (vizinho que passa,
    # crianÃ§a corrindo, a piazza central). Cada exercÃ­cio Ã© uma pergunta
    # dele numa situaÃ§Ã£o viva.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Ontem vocÃª chegou sem saber nada â€” 'straniero', sem nome, sem "
                    "idioma. Antonio te ensinou 'ciao', 'mi chiamo', 'buongiorno', "
                    "'buonasera', 'grazie', 'prego', 'come stai?', 'bene' "
                    "e 'male'.\n\n"
                    "Esta manhÃ£ vocÃª acordou com fome, comeu pÃ£o de Giulia e bebeu "
                    "Ãgua fresca da tigela. 'Pane' e 'acqua' â€” as duas primeiras "
                    "palavras que seu corpo pediu antes de qualquer liÃ§Ã£o."
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
                    "translation": "Vamos caminhar um pouco. E vocÃª vai falar â€” tÃ?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Uma mulher passa pela rua carregando uma cesta. Ela sorri. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Ciao!"},
                        {"id": "b", "text": "Grazie!"},
                        {"id": "c", "text": "Male!"},
                        {"id": "d", "text": "AdiÃ³s!"},
                    ],
                    "correct": "a",
                    "word_id": "it_ciao", "target": "ciao", "native": "olÃ",
                    "npc_reaction": "Eso. Simple y suficiente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Guarda â€” ya son las nueve de la domani. CÃ³mo saludas?",
                    "translation": "Olha â€” jÃ sÃ£o nove da manhÃ£. Como vocÃª cumprimenta?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O sol estÃ subindo, ainda cedo. Um senhor velho de bengala te olha ao passar. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Buongiorno!"},
                        {"id": "b", "text": "Buonasera!"},
                        {"id": "c", "text": "Buonanotte!"},
                        {"id": "d", "text": "Ciao noche!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Bueno. El viejo RamÃ­rez sempre responde 'buongiorno' de volta. Aprendiste.",
                },
                {
                    "kind": "narrative",
                    "text": "VocÃªs param na beira de uma fonte de pedra no centro da piazza. Pombos na borda, Ãgua limpa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E se qualcuno ti chiede come ti chiami? Che dici?",
                    "translation": "E se alguÃ©m perguntar como vocÃª se chama? O que vocÃª fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Uma crianÃ§a para e te olha com olhos curiosos: 'Come ti chiami?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Llamo Nico"},
                        {"id": "c", "text": "Soy straniero"},
                        {"id": "d", "text": "Bene, grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "Exacto. La niÃ±a vai repetir seu nome pra mÃ£e dela hoje Ã  noite.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E come rispondi a alguien que te ayudÃ³?",
                    "translation": "E como vocÃª responde a alguÃ©m que te ajudou?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um homem te ajuda a apanehar uma moeda que caiu. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Grazie!"},
                        {"id": "b", "text": "Ciao!"},
                        {"id": "c", "text": "Bene!"},
                        {"id": "d", "text": "Buongiorno!"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Bene. Y ele vai falar 'prego' â€” jÃ sabe o que vem depois.",
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
                    "npc_reaction": "Eso. El ciclo. Grazie â€” prego. Simple.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ehi, straniero â€” come stai oggi?",
                    "translation": "Ei, straniero â€” como vocÃª estÃ hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª dormiu bem, comeu pÃ£o quente, bebeu Ãgua. Antonio olha pra vocÃª esperando. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Straniero"},
                        {"id": "d", "text": "Mi chiamo"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bueno. Bem Ã© bom. Continua assim.",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio olha pro relÃ³gio de sol na parede da iglesia. Acena pra vocÃª continuar andando.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra vocÃª: 'AquÃ­ eres un...' Qual palavra ele usa?",
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
                    "question": "Antonio aponta pro campo e pro prÃ³prio peito: 'Io sono...'",
                    "options": [
                        {"id": "a", "text": "Contadino"},
                        {"id": "b", "text": "Straniero"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Doctor"},
                    ],
                    "correct": "a",
                    "word_id": "it_contadino", "target": "contadino", "native": "camponÃªs",
                    "npc_reaction": "Eso. Toda mi vida trabajando la tierra. Como mi padre.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: GramÃtica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Antonio para perto de uma fonte e ensina o verbo 'tener' de forma prÃtica:
    # ho fame / ho sete / ho [coisa]. Beats explicativos intercalados.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "VocÃªs caminharam pelo borgo, vocÃª cumprimentou vizinhos, "
                    "respondeu perguntas sobre seu nome, disse 'grazie' pro homem "
                    "da moeda. Antonio ficou satisfeito.\n\n"
                    "'Bem. As palabras de ontem ainda tÃ£o na sua cabeÃ§a. Agora tem "
                    "mais coisa pra aprender â€” o que acontece quando seu corpo precisa "
                    "de algo.'"
                ),
                "now": "Antonio vai ensinar como falar sobre o que vocÃª precisa.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio para perto da fonte, joga um pouco d'Ãgua no rosto, e te olha.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Oye â€” sabes decir 'ho'. 'Ho' es 'eu tenho' o 'eu sinto'. Guarda:",
                    "translation": "Ei â€” vocÃª sabe falar 'ho'. 'Ho' Ã© 'eu tenho' ou 'eu sinto'. Olha:",
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
                    "translation": "E se Ã© Ãgua que o corpo pede:",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ho sete",
                    "meaning": "Estou com sede (lit: 'tenho sede')",
                    "note": "sed = sede | mesmo padrÃ£o: ho + o que falta",
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
                    "example": "Ho fame â€” dame pane. / Ho sete â€” dame acqua.",
                    "translation": "Estou com fome â€” me dÃ pÃ£o. / Estou com sede â€” me dÃ Ãgua.",
                    "note": "O corpo sempre pede. Agora vocÃª pode nomear o que pede.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª nÃ£o come desde ontem Ã  noite. EstÃ´mago vazio, cabeÃ§a leve. Como vocÃª fala?",
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
                    "line": "Y el acqua â€” la boca seca, la garganta apretada. CÃ³mo se llama?",
                    "translation": "E a Ãgua â€” boca seca, garganta apertada. Como se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O sol da manhÃ£ jÃ esquenta. VocÃª caminhou bastante. A boca estÃ seca. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Estoy male"},
                        {"id": "d", "text": "Ho pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. Acqua â€” aÃ­. Sempre tem na fonte.",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio coloca as mÃ£os nos joelhos, levanta. 'Bene. Agora o corpo fala. VocÃª responde.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra fonte: 'AquÃ­ estÃ el acqua frÃ­a.' VocÃª estava com sede. O que vocÃª tem agora?",
                    "options": [
                        {"id": "a", "text": "Acqua"},
                        {"id": "b", "text": "Pane"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Leche"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "Ãgua",
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
                    "word_id": "it_pane", "target": "pane", "native": "pÃ£o",
                    "npc_reaction": "Pane. El suyo es el mejor del borgo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um menino passa corrindo e para, ofegante. Antonio faz sinal que o menino pode falar. O menino diz 'Ho sete!' â€” o que ele precisa?",
                    "options": [
                        {"id": "a", "text": "Acqua"},
                        {"id": "b", "text": "Pane"},
                        {"id": "c", "text": "Descanso"},
                        {"id": "d", "text": "Hambre"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "Ãgua",
                    "npc_reaction": "Acqua. OyÃ³ 'ho sete' y supo lo que necesitaba. Igual que tÃº ora.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: PrÃtica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Pratica intensa do vocab novo (pane/acqua/ho fame/ho sete) junto com
    # F1 vocab em situaÃ§Ãµes reais. NPC presente em cada exercÃ­cio, rapidez de fogo.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Antonio te ensinou 'ho fame' e 'ho sete' â€” as duas "
                    "primeiras frases que seu prÃ³prio corpo pediu esta manhÃ£. 'Pane' "
                    "pra comida, 'acqua' pra bebida. Ele disse que agora vai praticar "
                    "atÃ© sair sem pensar."
                ),
                "now": "PrÃtica rÃpida â€” Antonio manda situaÃ§Ã£o, vocÃª responde.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Facciamo veloce. Io dico la situazione, tu usi la parola. Pronto?",
                    "translation": "Vamos rÃpido. Eu digo a situaÃ§Ã£o, vocÃª usa a palavra. Pronto?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª nÃ£o come desde a manhÃ£. SÃ£o trÃªs da tarde. VocÃª fala pra Antonio:",
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
                    "question": "Giulia te passa um pedaÃ§o de pÃ£o. VocÃª responde:",
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
                    "question": "Antonio vÃª vocÃª comendo o pÃ£o. Ele pergunta: 'Come stai ora?'",
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
                    "question": "O caminheiro que passou antes era de fora do borgo â€” olhos diferentes, nÃ£o conhece as ruas. Antonio aponta: 'Ese hombre es un...'",
                    "options": [
                        {"id": "a", "text": "Straniero"},
                        {"id": "b", "text": "Contadino"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Doctor"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "Straniero. Como vocÃª era ontem. Mas menos agora, no?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ehi, e io? Che cosa sono io in questo borgo?",
                    "translation": "Ei â€” e eu? O que sou eu nesse borgo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio espalha a terra dos sapatos na calÃ§ada. Trabalha no campo toda a vida. Ele Ã©:",
                    "options": [
                        {"id": "a", "text": "Contadino"},
                        {"id": "b", "text": "Straniero"},
                        {"id": "c", "text": "Doctor"},
                        {"id": "d", "text": "Maestro"},
                    ],
                    "correct": "a",
                    "word_id": "it_contadino", "target": "contadino", "native": "camponÃªs",
                    "npc_reaction": "Eso. Contadino. Toda mi vida.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "E se arriva un nuovo straniero, che cosa gli dici per prima cosa?",
                    "translation": "E se chega um novo straniero â€” o que vocÃª fala primeiro?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um homem novo chega pelo portÃ£o do borgo, perdido. VocÃª vai atÃ© ele e diz:",
                    "options": [
                        {"id": "a", "text": "Ciao! Come ti chiami?"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Buonanotte"},
                        {"id": "d", "text": "Prego"},
                    ],
                    "correct": "a",
                    "word_id": "it_ciao", "target": "ciao", "native": "olÃ",
                    "npc_reaction": "AsÃ­ es! Ciao abre a conversa. Nome vem depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O sol estÃ a pino, calor forte. VocÃª e Nico caminharam muito. Sua garganta estÃ seca. VocÃª fala:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Estoy male"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. Acqua aÃ­ na fonte. JÃ sabe o caminho.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio tira uma maÃ§Ã£ do bolso e te oferece. Mas vocÃª precisa de Ãgua, nÃ£o de comida. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Ho sete, acqua"},
                        {"id": "b", "text": "Ho fame, grazie"},
                        {"id": "c", "text": "Prego"},
                        {"id": "d", "text": "Bene, grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Acqua. Claro. A maÃ§Ã£ fica pra depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª vai atÃ© a fonte e bebe. Voltando, Antonio: 'E ora, straniero?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Bene"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho sete"},
                        {"id": "d", "text": "Straniero"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Acqua frÃ­a Ã© isso.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Tarde na piazza. Giulia reaparece com pÃ£o sobrando da padaria.
    # HistÃ³ria usa o vocab de F1+F2 de forma orgÃ¢nica â€” menos aula, mais vida.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio", "Giulia"],
                "story": (
                    "Depois de uma manhÃ£ praticando, vocÃªs voltaram pra piazza. O sol "
                    "ainda alto, sombra das Ãrvores. Antonio deixou vocÃª descansar "
                    "enquanto ele foi falar com um vizinho.\n\n"
                    "Giulia aparece do nada carregando uma cesta com pÃ£o que sobrou "
                    "da padaria."
                ),
                "now": "Uma conversa real com Giulia e Nico â€” sem exercÃ­cio, sÃ³ vida.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Giulia chega pela sombra das Ãrvores, cesta no braÃ§o, cabelos presos com um paneo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Nico! Straniero! Ho pane que sobrÃ³. Vuolen?",
                    "translation": "Nico! Forasteiro! Tenho pÃ£o que sobrou. VocÃªs querem?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Giulia! SÃ­, claro. El straniero tiene hambre desde esta domani.",
                    "translation": "Giulia! Sim, claro. O straniero estÃ com fome desde essa manhÃ£.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia estende um pÃ£o pra vocÃª direto. Ela estÃ te oferecendo o quÃª?",
                    "options": [
                        {"id": "a", "text": "Pane"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Fruta"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pÃ£o",
                    "npc_reaction": "Pane. Pega, pega.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Giulia esmau vocÃª pegar o pÃ£o e ficou olhando. O que vocÃª fala pra ela?",
                    "options": [
                        {"id": "a", "text": "Grazie!"},
                        {"id": "b", "text": "Ciao!"},
                        {"id": "c", "text": "Bene!"},
                        {"id": "d", "text": "AdiÃ³s!"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Prego, figlio. Siempre c'e pane pra quem precisa.",
                },
                {
                    "kind": "narrative",
                    "text": "Giulia se senta no banco ao lado, tira um pÃ£o pra ela mesma. Antonio inclina o chapÃ©u.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Y el straniero â€” cÃ³mo se llama?",
                    "translation": "E o straniero â€” como ele se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia olha pra vocÃª esperando. Ela quer saber seu nome. O que vocÃª fala?",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Bene, grazie"},
                        {"id": "d", "text": "Soy contadino"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "Piacere. Io sono Giulia. So gia que comeÃ§a pelo pane.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Buonasera! Lo dico quando il pranzo e gia passato. Come stai?",
                    "translation": "Boa tarde! â€” digo eu quando jÃ passou o almoÃ§o. Como vocÃª estÃ?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia te pergunta diretamente: 'Come stai?' com um sorriso genuÃ­no. VocÃª responde:",
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
                        "ganhando ritmo â€” sinos da iglesia ao longe, crianÃ§as corrindo, "
                        "o cheiro de terra molhada voltando com a brisa da tarde."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O sino da iglesia bateu seis vezes. O sol estÃ baixo. Como Antonio vai cumprimentar o prÃ³ximo vizinho que passar?",
                    "options": [
                        {"id": "a", "text": "Buonasera!"},
                        {"id": "b", "text": "Buongiorno!"},
                        {"id": "c", "text": "Buonanotte!"},
                        {"id": "d", "text": "Ciao noche!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenas_tardes", "target": "buonasera", "native": "boa tarde",
                    "npc_reaction": "Buonasera. El sol te dice cuÃndo cambiar.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃculo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Entardecer. Antonio precisa falar com um vizinho â€” deixa o protagonista
    # sozinho por alguns minutos num ponto da rua. Uma crianÃ§a passa com sede,
    # um senhor pergunta onde fica a locanda, um homem novo (futuro antagonista)
    # passa e olha demais.
    # SeÃ§Ã£o gated: errar trava. O protagonista estÃ sÃ³ â€” precisa se virar.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Giulia foi embora com a cesta vazia. Antonio avistou um vizinho "
                    "no outro lado da piazza â€” alguÃ©m que ele precisa falar. 'Espera "
                    "aqui dois minutos. NÃ£o vai a lugar nenhum.' E foi."
                ),
                "now": "VocÃª estÃ sozinho. O borgo continua ao redor. Tem que se virar.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio some pela sombra das Ãrvores. VocÃª estÃ parado na beira da piazza, sozinho pela primeira vez no borgo.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸŒ‡ A luz fica alaranjada. Uma crianÃ§a de uns seis anos corri atÃ© vocÃª e para â€” bochechas vermelhas, respiraÃ§Ã£o ofegante.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "NiÃ±a",
                    "line": "Signore! Tienes acqua? Ho sete!",
                    "translation": "Senhor! VocÃª tem Ãgua? Estou com sede!",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "NiÃ±a",
                    "question": "A menina disse 'Ho sete!' e olhou pra sua cantil. Ela precisa de:",
                    "options": [
                        {"id": "a", "text": "Acqua"},
                        {"id": "b", "text": "Pane"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Descanso"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "Ãgua",
                    "npc_reaction": "Ãgua! VocÃª entendeu 'ho sete'. DÃ a cantil pra ela.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "A menina bebe, devolve a cantil com um sorriso enorme e sai corrindo. VocÃª ficou sem Ãgua, mas com um sorriso no rosto.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸ§“ Um senhor idueo se aproxima com um mapa dobrado na mÃ£o â€” parece perdido.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Signore Anziano",
                    "line": "Joven, come stai? Sabes dÃ³nde estÃ la locanda?",
                    "translation": "Jovem, como vai? Sabe onde fica a locanda?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Signore Anziano",
                    "question": "O senhor perguntou 'Come stai?' antes de pedir ajuda. Como vocÃª responde primeiro?",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Ho sete"},
                        {"id": "c", "text": "Buonanotte"},
                        {"id": "d", "text": "Mi chiamo"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "O senhor acena satisfeito. Agora vocÃª pode tentar explicar onde fica a locanda.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "VocÃª aponta pro caminho que Antonio te mostrou ontem â€” a casa de dois andares no canto da piazza. O senhor agradece e vai embora.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸš¶ Um homem para na entrada da piazza. ChapÃ©u baixo. Olha pra vocÃª por tempo demais antes de seguir em frente.",
                },
                {
                    "kind": "narrative",
                    "text": "Algo no jeito dele nÃ£o estava certo. Mas vocÃª nÃ£o tem palavra pra isso ainda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio voltou. 'Straniero â€” come stai? Todo bene?' VocÃª responde honestamente:",
                    "options": [
                        {"id": "a", "text": "Bene... ma c'e algo raro"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Ciao, buongiorno"},
                        {"id": "d", "text": "Prego"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Nico olha pro mesmo lado que vocÃª olhou. Franze a testa um segundo. Depois: 'Vamos pra locanda.'",
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
                        "VocÃªs caminham de volta pra locanda. As janelas acendem uma a "
                        "uma. Antonio nÃ£o fala nada sobre o homem do chapÃ©u baixo.\n\n"
                        "Mas vocÃª viu ele olhar pro mesmo lado que vocÃª olhou."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
