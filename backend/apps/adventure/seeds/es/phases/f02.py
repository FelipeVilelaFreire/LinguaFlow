"""
Seed das 6 seÃ§Ãµes da Fase 2 Espanhol A1 â€” "El Pueblo Despierta".

Dia seguinte Ã  chegada. Don Miguel mostra a posada pela manhÃ£, leva o
protagonista por um circuito curto pelo pueblo e ensina as primeiras
necessidades fÃ­sicas: tengo hambre, tengo sed, pan, agua.

Novos vocab (2): pan Â· agua Â· tengo hambre Â· tengo sed
RevisÃ£o F1: hola, buenos dÃ­as, gracias, de nada, me llamo, Â¿cÃ³mo estÃ¡s?, bien/mal, forastero
NPC principal:   Don Miguel (fio condutor)
NPC cameo:       Rosa la Panadera (reaparece brevemente)
Itens:           pan_fresco (word_id: es_pan) Â· agua_del_pozo (word_id: es_agua)
Arco emocional:  desorientado â†’ comeÃ§a a entender o ritmo do pueblo
TransiÃ§Ã£o:       anoitecer na posada; uma sombra passa pela janela â€” alguÃ©m observou

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f2_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # ManhÃ£ na posada. Protagonista acorda sem saber onde estÃ¡ â€” cheiro de pÃ£o,
    # luz pela janela. Don Miguel chega, Rosa aparece com pÃ£o quente.
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
                        "Ã¡spero, cheiro de pÃ£o no ar. VocÃª levanta, desorientado â€” "
                        "pelos telhados de telha laranja do pueblo de San CristÃ³bal."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¡Buenos dÃ­as, forastero! Â¿Dormiste bien?",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o tem resposta rÃ¡pida. Mas sim â€” dormiu. Faz tempo que nÃ£o dormia assim.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Rosa estÃ¡ abajo. Tiene pan fresco para nosotros.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸž Escada de madeira que range. Rosa na cozinha da posada â€” farinha nas mÃ£os, dois pÃ£es na mesa.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Â¡Hola! Â¡Buenos dÃ­as! SiÃ©ntate, forastero. El pan estÃ¡ caliente.",
                },
                {
                    "kind": "player",
                    "text": "Seu estÃ´mago ronca antes de vocÃª responder qualquer coisa.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Â¡Ja! Â¡Tienes hambre! Come, come.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Rosa aponta pro pÃ£o, pro seu estÃ´mago, ri de novo.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Pan. Se dice 'pan'. Â¿Ves? â€” pan.",
                },
                {
                    "kind": "player",
                    "text": "â€” Pan.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¡Bien! Y el agua tambiÃ©n. Toma.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Rosa empurrou uma tigela de barro com lÃ­quido claro e fresco. O que ela te deu?",
                    "options": [
                        {"id": "a", "text": "Agua"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "Leche"},
                        {"id": "d", "text": "Vino"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "Ã¡gua",
                    "npc_reaction": "Agua. FrÃ­a y buena. La mejor cosa del pueblo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O cheiro que te acordou, a coisa quente na mesa, a razÃ£o do seu estÃ´mago roncar. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Pan"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Fuego"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pÃ£o",
                    "npc_reaction": "Pan. Cada maÃ±ana, Rosa tiene pan. Ya sabe dÃ³nde venir.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª acabou de acordar, nÃ£o comeu nada. Rosa aponta pra sua barriga sorrindo. O que ela disse?",
                    "options": [
                        {"id": "a", "text": "Â¡Tienes hambre!"},
                        {"id": "b", "text": "Â¡Tienes sed!"},
                        {"id": "c", "text": "Â¡EstÃ¡s bien!"},
                        {"id": "d", "text": "Â¡Buenos dÃ­as!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. El cuerpo pide comida. Eso todo el mundo entiende.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Sua garganta estÃ¡ seca depois de dormir. Don Miguel te empurra a tigela de barro. VocÃª diria:",
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

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel leva o protagonista de volta pelo caminho do dia anterior.
    # RevisÃ£o contextual: F1 vocab em situaÃ§Ãµes reais (vizinho que passa,
    # crianÃ§a correndo, a plaza central). Cada exercÃ­cio Ã© uma pergunta
    # dele numa situaÃ§Ã£o viva.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Ontem vocÃª chegou sem saber nada â€” 'forastero', sem nome, sem "
                    "idioma. Don Miguel te ensinou 'hola', 'me llamo', 'buenos dÃ­as', "
                    "'buenas tardes', 'gracias', 'de nada', 'Â¿cÃ³mo estÃ¡s?', 'bien' "
                    "e 'mal'.\n\n"
                    "Esta manhÃ£ vocÃª acordou com fome, comeu pÃ£o de Rosa e bebeu "
                    "Ã¡gua fresca da tigela. 'Pan' e 'agua' â€” as duas primeiras "
                    "palavras que seu corpo pediu antes de qualquer liÃ§Ã£o."
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
                    "line": "Vamos a caminar un poco. Y tÃº vas a hablar â€” Â¿eh?",
                    "translation": "Vamos caminhar um pouco. E vocÃª vai falar â€” tÃ¡?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Uma mulher passa pela rua carregando uma cesta. Ela sorri. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Â¡Hola!"},
                        {"id": "b", "text": "Â¡Gracias!"},
                        {"id": "c", "text": "Â¡Mal!"},
                        {"id": "d", "text": "Â¡AdiÃ³s!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olÃ¡",
                    "npc_reaction": "Eso. Simple y suficiente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Mira â€” ya son las nueve de la maÃ±ana. Â¿CÃ³mo saludas?",
                    "translation": "Olha â€” jÃ¡ sÃ£o nove da manhÃ£. Como vocÃª cumprimenta?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sol estÃ¡ subindo, ainda cedo. Um senhor velho de bengala te olha ao passar. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "b", "text": "Â¡Buenas tardes!"},
                        {"id": "c", "text": "Â¡Buenas noches!"},
                        {"id": "d", "text": "Â¡Hola noche!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Bueno. El viejo RamÃ­rez sempre responde 'buenos dÃ­as' de volta. Aprendiste.",
                },
                {
                    "kind": "narrative",
                    "text": "VocÃªs param na beira de uma fonte de pedra no centro da plaza. Pombos na borda, Ã¡gua limpa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿Y si alguien te pregunta cÃ³mo te llamas? Â¿QuÃ© dices?",
                    "translation": "E se alguÃ©m perguntar como vocÃª se chama? O que vocÃª fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Uma crianÃ§a para e te olha com olhos curiosos: 'Â¿CÃ³mo te llamas?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Llamo Miguel"},
                        {"id": "c", "text": "Soy forastero"},
                        {"id": "d", "text": "Bien, gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Exacto. La niÃ±a vai repetir seu nome pra mÃ£e dela hoje Ã  noite.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿Y cÃ³mo le respondes a alguien que te ayudÃ³?",
                    "translation": "E como vocÃª responde a alguÃ©m que te ajudou?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um homem te ajuda a apanhar uma moeda que caiu. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Â¡Gracias!"},
                        {"id": "b", "text": "Â¡Hola!"},
                        {"id": "c", "text": "Â¡Bien!"},
                        {"id": "d", "text": "Â¡Buenos dÃ­as!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Bien. Y ele vai falar 'de nada' â€” jÃ¡ sabe o que vem depois.",
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
                    "npc_reaction": "Eso. El ciclo. Gracias â€” de nada. Simple.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Oye, forastero â€” Â¿cÃ³mo estÃ¡s hoy?",
                    "translation": "Ei, forasteiro â€” como vocÃª estÃ¡ hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª dormiu bem, comeu pÃ£o quente, bebeu Ã¡gua. Don Miguel olha pra vocÃª esperando. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Forastero"},
                        {"id": "d", "text": "Me llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Bem Ã© bom. Continua assim.",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel olha pro relÃ³gio de sol na parede da iglesia. Acena pra vocÃª continuar andando.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra vocÃª: 'AquÃ­ eres un...' Qual palavra ele usa?",
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
                    "question": "Don Miguel aponta pro campo e pro prÃ³prio peito: 'Yo soy...'",
                    "options": [
                        {"id": "a", "text": "Campesino"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Doctor"},
                    ],
                    "correct": "a",
                    "word_id": "es_campesino", "target": "campesino", "native": "camponÃªs",
                    "npc_reaction": "Eso. Toda mi vida trabajando la tierra. Como mi padre.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel para perto de uma fonte e ensina o verbo 'tener' de forma prÃ¡tica:
    # tengo hambre / tengo sed / tengo [coisa]. Beats explicativos intercalados.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "VocÃªs caminharam pelo pueblo, vocÃª cumprimentou vizinhos, "
                    "respondeu perguntas sobre seu nome, disse 'gracias' pro homem "
                    "da moeda. Don Miguel ficou satisfeito.\n\n"
                    "'Bem. As palabras de ontem ainda tÃ£o na sua cabeÃ§a. Agora tem "
                    "mais coisa pra aprender â€” o que acontece quando seu corpo precisa "
                    "de algo.'"
                ),
                "now": "Don Miguel vai ensinar como falar sobre o que vocÃª precisa.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel para perto da fonte, joga um pouco d'Ã¡gua no rosto, e te olha.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Oye â€” sabes decir 'tengo'. 'Tengo' es 'eu tenho' o 'eu sinto'. Mira:",
                    "translation": "Ei â€” vocÃª sabe falar 'tengo'. 'Tengo' Ã© 'eu tenho' ou 'eu sinto'. Olha:",
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
                    "translation": "E se Ã© Ã¡gua que o corpo pede:",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tengo sed",
                    "meaning": "Estou com sede (lit: 'tenho sede')",
                    "note": "sed = sede | mesmo padrÃ£o: tengo + o que falta",
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
                    "example": "Tengo hambre â€” dame pan. / Tengo sed â€” dame agua.",
                    "translation": "Estou com fome â€” me dÃ¡ pÃ£o. / Estou com sede â€” me dÃ¡ Ã¡gua.",
                    "note": "O corpo sempre pede. Agora vocÃª pode nomear o que pede.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª nÃ£o come desde ontem Ã  noite. EstÃ´mago vazio, cabeÃ§a leve. Como vocÃª fala?",
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
                    "line": "Y el agua â€” la boca seca, la garganta apretada. Â¿CÃ³mo se llama?",
                    "translation": "E a Ã¡gua â€” boca seca, garganta apertada. Como se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sol da manhÃ£ jÃ¡ esquenta. VocÃª caminhou bastante. A boca estÃ¡ seca. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Tengo pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. Agua â€” aÃ­. Sempre tem na fonte.",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel coloca as mÃ£os nos joelhos, levanta. 'Bien. Agora o corpo fala. VocÃª responde.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra fonte: 'AquÃ­ estÃ¡ el agua frÃ­a.' VocÃª estava com sede. O que vocÃª tem agora?",
                    "options": [
                        {"id": "a", "text": "Agua"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Leche"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "Ã¡gua",
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
                    "word_id": "es_pan", "target": "pan", "native": "pÃ£o",
                    "npc_reaction": "Pan. El suyo es el mejor del pueblo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um menino passa correndo e para, ofegante. Don Miguel faz sinal que o menino pode falar. O menino diz 'Tengo sed!' â€” o que ele precisa?",
                    "options": [
                        {"id": "a", "text": "Agua"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "Descanso"},
                        {"id": "d", "text": "Hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "Ã¡gua",
                    "npc_reaction": "Agua. OyÃ³ 'tengo sed' y supo lo que necesitaba. Igual que tÃº ahora.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Pratica intensa do vocab novo (pan/agua/tengo hambre/tengo sed) junto com
    # F1 vocab em situaÃ§Ãµes reais. NPC presente em cada exercÃ­cio, rapidez de fogo.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel te ensinou 'tengo hambre' e 'tengo sed' â€” as duas "
                    "primeiras frases que seu prÃ³prio corpo pediu esta manhÃ£. 'Pan' "
                    "pra comida, 'agua' pra bebida. Ele disse que agora vai praticar "
                    "atÃ© sair sem pensar."
                ),
                "now": "PrÃ¡tica rÃ¡pida â€” Don Miguel manda situaÃ§Ã£o, vocÃª responde.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Vamos rÃ¡pido. Yo digo la situaciÃ³n, tÃº usas la palabra. Â¿Listo?",
                    "translation": "Vamos rÃ¡pido. Eu digo a situaÃ§Ã£o, vocÃª usa a palavra. Pronto?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª nÃ£o come desde a manhÃ£. SÃ£o trÃªs da tarde. VocÃª fala pra Don Miguel:",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. Vamos buscar pan.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Rosa te passa um pedaÃ§o de pÃ£o. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Â¡Gracias!"},
                        {"id": "b", "text": "Â¡Hola!"},
                        {"id": "c", "text": "Â¡Bien!"},
                        {"id": "d", "text": "Â¡Mal!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Rosa sorri. 'De nada, hijo.'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel vÃª vocÃª comendo o pÃ£o. Ele pergunta: 'Â¿CÃ³mo estÃ¡s ahora?'",
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
                    "question": "O caminheiro que passou antes era de fora do pueblo â€” olhos diferentes, nÃ£o conhece as ruas. Don Miguel aponta: 'Ese hombre es un...'",
                    "options": [
                        {"id": "a", "text": "Forastero"},
                        {"id": "b", "text": "Campesino"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Doctor"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero. Como vocÃª era ontem. Mas menos agora, Â¿no?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Oye â€” Â¿y yo? Â¿QuÃ© soy yo en este pueblo?",
                    "translation": "Ei â€” e eu? O que sou eu nesse pueblo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel espalha a terra dos sapatos na calÃ§ada. Trabalha no campo toda a vida. Ele Ã©:",
                    "options": [
                        {"id": "a", "text": "Campesino"},
                        {"id": "b", "text": "Forastero"},
                        {"id": "c", "text": "Doctor"},
                        {"id": "d", "text": "Maestro"},
                    ],
                    "correct": "a",
                    "word_id": "es_campesino", "target": "campesino", "native": "camponÃªs",
                    "npc_reaction": "Eso. Campesino. Toda mi vida.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y si llega un nuevo forastero â€” Â¿quÃ© le dices primero?",
                    "translation": "E se chega um novo forasteiro â€” o que vocÃª fala primeiro?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um homem novo chega pelo portÃ£o do pueblo, perdido. VocÃª vai atÃ© ele e diz:",
                    "options": [
                        {"id": "a", "text": "Â¡Hola! Â¿CÃ³mo te llamas?"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Buenos noches"},
                        {"id": "d", "text": "De nada"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olÃ¡",
                    "npc_reaction": "Â¡AsÃ­ es! Hola abre a conversa. Nome vem depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sol estÃ¡ a pino, calor forte. VocÃª e Miguel caminharam muito. Sua garganta estÃ¡ seca. VocÃª fala:",
                    "options": [
                        {"id": "a", "text": "Tengo sed"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Sed. Agua aÃ­ na fonte. JÃ¡ sabe o caminho.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel tira uma maÃ§Ã£ do bolso e te oferece. Mas vocÃª precisa de Ã¡gua, nÃ£o de comida. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Tengo sed, agua"},
                        {"id": "b", "text": "Tengo hambre, gracias"},
                        {"id": "c", "text": "De nada"},
                        {"id": "d", "text": "Bien, gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Agua. Claro. A maÃ§Ã£ fica pra depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª vai atÃ© a fonte e bebe. Voltando, Don Miguel: 'Â¿Y ahora, forastero?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo sed"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Agua frÃ­a Ã© isso.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Tarde na plaza. Rosa reaparece com pÃ£o sobrando da padaria.
    # HistÃ³ria usa o vocab de F1+F2 de forma orgÃ¢nica â€” menos aula, mais vida.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Rosa"],
                "story": (
                    "Depois de uma manhÃ£ praticando, vocÃªs voltaram pra plaza. O sol "
                    "ainda alto, sombra das Ã¡rvores. Don Miguel deixou vocÃª descansar "
                    "enquanto ele foi falar com um vizinho.\n\n"
                    "Rosa aparece do nada carregando uma cesta com pÃ£o que sobrou "
                    "da padaria."
                ),
                "now": "Uma conversa real com Rosa e Miguel â€” sem exercÃ­cio, sÃ³ vida.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Rosa chega pela sombra das Ã¡rvores, cesta no braÃ§o, cabelos presos com um pano.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Â¡Miguel! Â¡Forastero! Tengo pan que sobrÃ³. Â¿Quieren?",
                    "translation": "Miguel! Forasteiro! Tenho pÃ£o que sobrou. VocÃªs querem?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¡Rosa! SÃ­, claro. El forastero tiene hambre desde esta maÃ±ana.",
                    "translation": "Rosa! Sim, claro. O forasteiro estÃ¡ com fome desde essa manhÃ£.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa estende um pÃ£o pra vocÃª direto. Ela estÃ¡ te oferecendo o quÃª?",
                    "options": [
                        {"id": "a", "text": "Pan"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Fruta"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pÃ£o",
                    "npc_reaction": "Pan. Pega, pega.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Rosa esperou vocÃª pegar o pÃ£o e ficou olhando. O que vocÃª fala pra ela?",
                    "options": [
                        {"id": "a", "text": "Â¡Gracias!"},
                        {"id": "b", "text": "Â¡Hola!"},
                        {"id": "c", "text": "Â¡Bien!"},
                        {"id": "d", "text": "Â¡AdiÃ³s!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, hijo. Siempre hay pan pra quem precisa.",
                },
                {
                    "kind": "narrative",
                    "text": "Rosa se senta no banco ao lado, tira um pÃ£o pra ela mesma. Don Miguel inclina o chapÃ©u.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Â¿Y el forastero â€” cÃ³mo se llama?",
                    "translation": "E o forasteiro â€” como ele se chama?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa olha pra vocÃª esperando. Ela quer saber seu nome. O que vocÃª fala?",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Soy campesino"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Mucho gusto. Yo soy Rosa. Ya sÃ© que comeÃ§a pelo pan.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Â¡Buenas tardes! â€” digo yo cuando ya pasa el almuerzo. Â¿CÃ³mo estÃ¡s?",
                    "translation": "Boa tarde! â€” digo eu quando jÃ¡ passou o almoÃ§o. Como vocÃª estÃ¡?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa te pergunta diretamente: 'Â¿CÃ³mo estÃ¡s?' com um sorriso genuÃ­no. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Con pan y agua siempre estÃ¡s bien.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel ri de algo que Rosa disse baixinho. O pueblo vai "
                        "ganhando ritmo â€” sinos da iglesia ao longe, crianÃ§as correndo, "
                        "o cheiro de terra molhada voltando com a brisa da tarde."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O sino da iglesia bateu seis vezes. O sol estÃ¡ baixo. Como Don Miguel vai cumprimentar o prÃ³ximo vizinho que passar?",
                    "options": [
                        {"id": "a", "text": "Â¡Buenas tardes!"},
                        {"id": "b", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "c", "text": "Â¡Buenas noches!"},
                        {"id": "d", "text": "Â¡Hola noche!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_tardes", "target": "buenas tardes", "native": "boa tarde",
                    "npc_reaction": "Buenas tardes. El sol te dice cuÃ¡ndo cambiar.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Entardecer. Don Miguel precisa falar com um vizinho â€” deixa o protagonista
    # sozinho por alguns minutos num ponto da rua. Uma crianÃ§a passa com sede,
    # um senhor pergunta onde fica a posada, um homem novo (futuro antagonista)
    # passa e olha demais.
    # SeÃ§Ã£o gated: errar trava. O protagonista estÃ¡ sÃ³ â€” precisa se virar.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Rosa foi embora com a cesta vazia. Don Miguel avistou um vizinho "
                    "no outro lado da plaza â€” alguÃ©m que ele precisa falar. 'Espera "
                    "aqui dois minutos. NÃ£o vai a lugar nenhum.' E foi."
                ),
                "now": "VocÃª estÃ¡ sozinho. O pueblo continua ao redor. Tem que se virar.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel some pela sombra das Ã¡rvores. VocÃª estÃ¡ parado na beira da plaza, sozinho pela primeira vez no pueblo.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸŒ‡ A luz fica alaranjada. Uma crianÃ§a de uns seis anos corre atÃ© vocÃª e para â€” bochechas vermelhas, respiraÃ§Ã£o ofegante.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "NiÃ±a",
                    "line": "Â¡SeÃ±or! Â¿Tienes agua? Â¡Tengo sed!",
                    "translation": "Senhor! VocÃª tem Ã¡gua? Estou com sede!",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "NiÃ±a",
                    "question": "A menina disse 'Â¡Tengo sed!' e olhou pra sua cantil. Ela precisa de:",
                    "options": [
                        {"id": "a", "text": "Agua"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Descanso"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "Ã¡gua",
                    "npc_reaction": "Ãgua! VocÃª entendeu 'tengo sed'. DÃ¡ a cantil pra ela.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "A menina bebe, devolve a cantil com um sorriso enorme e sai correndo. VocÃª ficou sem Ã¡gua, mas com um sorriso no rosto.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸ§“ Um senhor idoso se aproxima com um mapa dobrado na mÃ£o â€” parece perdido.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SeÃ±or Mayor",
                    "line": "Joven, Â¿cÃ³mo estÃ¡s? Â¿Sabes dÃ³nde estÃ¡ la posada?",
                    "translation": "Jovem, como vai? Sabe onde fica a posada?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SeÃ±or Mayor",
                    "question": "O senhor perguntou 'Â¿CÃ³mo estÃ¡s?' antes de pedir ajuda. Como vocÃª responde primeiro?",
                    "options": [
                        {"id": "a", "text": "Bien, gracias"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Buenos noches"},
                        {"id": "d", "text": "Me llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "O senhor acena satisfeito. Agora vocÃª pode tentar explicar onde fica a posada.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "VocÃª aponta pro caminho que Don Miguel te mostrou ontem â€” a casa de dois andares no canto da plaza. O senhor agradece e vai embora.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸš¶ Um homem para na entrada da plaza. ChapÃ©u baixo. Olha pra vocÃª por tempo demais antes de seguir em frente.",
                },
                {
                    "kind": "narrative",
                    "text": "Algo no jeito dele nÃ£o estava certo. Mas vocÃª nÃ£o tem palavra pra isso ainda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel voltou. 'Forastero â€” Â¿cÃ³mo estÃ¡s? Â¿Todo bien?' VocÃª responde honestamente:",
                    "options": [
                        {"id": "a", "text": "Bien... pero hay algo raro"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Hola, buenos dÃ­as"},
                        {"id": "d", "text": "De nada"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Miguel olha pro mesmo lado que vocÃª olhou. Franze a testa um segundo. Depois: 'Vamos pra posada.'",
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
                        "VocÃªs caminham de volta pra posada. As janelas acendem uma a "
                        "uma. Don Miguel nÃ£o fala nada sobre o homem do chapÃ©u baixo.\n\n"
                        "Mas vocÃª viu ele olhar pro mesmo lado que vocÃª olhou."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
