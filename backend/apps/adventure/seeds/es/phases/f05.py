"""
Seed das 6 seÃ§Ãµes da Fase 5 Espanhol A1 â€” "La Primera Chispa".

Algo estÃ¡ errado no pueblo. El Vigilante Oscuro â€” o homem do chapÃ©u baixo
visto em F2 e F4 â€” age mais abertamente. Don Miguel comeÃ§a a preparar o
protagonista. E na S6, sozinho numa rua escura, o protagonista usa uma
palavra pela primeira vez de verdade â€” fuego â€” e ela se torna fÃ­sica.

Esta Ã© a primeira apariÃ§Ã£o de La Palabra Viva. NÃ£o Ã© herÃ³ica. Ã‰ acidental,
aterrorizante, e muda tudo.

REGRA DO SISTEMA DE PODER:
Acertar a palavra â‰  matar o inimigo.
Acertar a palavra = entendeu de verdade = a palavra se torna real = poder manifesto.
DEPOIS, com o poder em mÃ£os, o protagonista pode agir.
Nunca: "vocÃª acertou, portanto venceu." Sempre: "vocÃª acertou â†’ poder ganho â†’ vocÃª escolhe."

Novos vocab (3): miedo Â· fuego Â· correr
RevisÃ£o F1â€“F4: hola, buenos dÃ­as, gracias, bien/mal, me llamo, forastero,
               hay/no hay, pan, agua, Ã¡rbol, piedra, naranja, tres, mucho/poco
NPC principal:   Don Miguel (fio condutor â€” mais sÃ©rio a partir daqui)
NPC antagonista: El Vigilante Oscuro (agente â€” confronto na S6)
Arco emocional:  seguro â†’ ameaÃ§ado â†’ poder acidental â†’ assustado com si mesmo
TransiÃ§Ã£o:       Miguel olha pro protagonista de um jeito diferente. A fase seguinte
                 comeÃ§a com uma conversa sÃ©ria.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f5_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Tarde fechada. Miguel mais quieto que o normal. Leva o protagonista por
    # uma rota diferente â€” ruas menos movimentadas. Mostra algo no caminho:
    # uma fogueira de oleiros, crianÃ§as correndo com medo de cachorro.
    # Vocab (miedo/fuego/correr) aparece sem traduÃ§Ã£o â€” imersÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ† Tarde fechada em San CristÃ³bal. Nuvens pesadas, sem sol. "
                        "Don Miguel chegou na posada mais cedo que o normal e te chamou "
                        "sem explicaÃ§Ã£o â€” 'Vem.' Uma rota diferente pelo pueblo."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Hay cosas que tienes que saber. No me gusta el pueblo hoy.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª seguiu sem perguntar. O tom dele era diferente â€” nÃ£o amigÃ¡vel, nÃ£o preocupado. Alerta.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸ”¥ Num beco lateral, um grupo de oleiros mantÃ©m uma fogueira grande â€” fumaÃ§a escura subindo pelo beco.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Fuego. Lo controlan â€” por ahora. Pero el fuego no avisa.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Fuego. A chama era enorme, quente, barulhenta. VocÃª ficou parado olhando.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¿QuÃ© sientes cuando lo miras?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o tinha a palavra ainda. Mas o cheiro, o calor, o som â€” algo no fogo te puxava.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸƒ TrÃªs crianÃ§as dobram a esquina gritando â€” um cachorro latindo atrÃ¡s. Elas correm, rindo de susto.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¡Corren! El perro solo ladra â€” no muerde. Pero el miedo hace correr igual.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Corren. Miedo. Duas palavras novas num segundo. O cachorro passou pelo lado de vocÃªs sem parar.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "A fogueira dos oleiros era enorme, quente, iluminava o beco inteiro. Como essa coisa se chama?",
                    "options": [
                        {"id": "a", "text": "Fuego"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Piedra"},
                        {"id": "d", "text": "Ãrbol"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": "Fuego. Quente. NÃ£o avisa â€” sÃ³ aparece.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "As crianÃ§as viram o cachorro e saÃ­ram disparadas â€” pernas rÃ¡pidas, gritos. O que elas fizeram?",
                    "options": [
                        {"id": "a", "text": "Corrieron â€” elas correram"},
                        {"id": "b", "text": "Comieron â€” elas comeram"},
                        {"id": "c", "text": "Cantaron â€” elas cantaram"},
                        {"id": "d", "text": "Durmieron â€” elas dormiram"},
                    ],
                    "correct": "a",
                    "word_id": "es_correr", "target": "correr", "native": "correr",
                    "npc_reaction": "Corrieron. O cachorro faz isso com todo mundo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse que o miedo faz as crianÃ§as correr mesmo sem perigo real. O que Ã© 'miedo'?",
                    "options": [
                        {"id": "a", "text": "Medo"},
                        {"id": "b", "text": "Alegria"},
                        {"id": "c", "text": "Fome"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Todo mundo tem. O que importa Ã© o que vocÃª faz com ele.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel para, olha ao redor, e diz 'No me gusta el pueblo hoy'. Como vocÃª estÃ¡ se sentindo?",
                    "options": [
                        {"id": "a", "text": "Un poco de miedo"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Hay naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Bom â€” o miedo avisa. Escuta ele.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel leva o protagonista por um caminho mais seguro â€” perto da
    # iglesia. RevisÃ£o F1â€“F4 com contexto de tensÃ£o crescente.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "VocÃªs saÃ­ram do beco das fogueiras. Don Miguel caminha perto, "
                    "mais de perto que de costume. VocÃª aprendeu 'fuego', 'correr' "
                    "e 'miedo' pela observaÃ§Ã£o â€” sem liÃ§Ã£o.\n\n"
                    "As outras palavras estÃ£o lÃ¡: hola, buenos dÃ­as, gracias, bien, "
                    "tengo hambre, tengo sed, hay, Ã¡rbol, piedra, naranja, tres, "
                    "mucho, poco. Don Miguel continua te testando â€” mesmo com esse humor."
                ),
                "now": "RevisÃ£o das fases anteriores num contexto mais tenso.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel para na sombra da iglesia. Olha a praÃ§a vazia. Uma vela dentro pela janela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Enquanto caminhamos â€” vamos revisar. O que vocÃª aprendeu que pode ajudar agora?",
                    "translation": "Enquanto caminhamos â€” vamos revisar. O que vocÃª aprendeu que pode ajudar agora?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um homem desconhecido para na outra ponta da rua e olha pra vocÃªs. Como vocÃª cumprimenta â€” Ã© de tarde:",
                    "options": [
                        {"id": "a", "text": "Â¡Buenas tardes!"},
                        {"id": "b", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "c", "text": "Â¡Buenas noches!"},
                        {"id": "d", "text": "Â¡Hola noche!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_tardes", "target": "buenas tardes", "native": "boa tarde",
                    "npc_reaction": "Buenas tardes. O homem nÃ£o respondeu. Seguiu em frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿Y si alguien nuevo llega al pueblo y pregunta tu nombre?",
                    "translation": "E se alguÃ©m novo chegar ao pueblo e perguntar seu nome?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um forasteiro novo para perto de vocÃªs: 'Â¿CÃ³mo te llamas?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Hay fuego"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Me llamo. Sempre diga seu nome â€” nÃ£o esconde.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿QuÃ© habÃ­a ayer en el campo â€” cerca del rÃ­o?",
                    "translation": "O que havia ontem no campo â€” perto do rÃ­o?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "No campo ontem havia Ã¡rvores, pedras e o rÃ­o. Don Miguel: 'Â¿Hay Ã¡rboles cerca del rÃ­o?'",
                    "options": [
                        {"id": "a", "text": "SÃ­, hay Ã¡rboles y piedras"},
                        {"id": "b", "text": "No hay nada"},
                        {"id": "c", "text": "Hay fuego"},
                        {"id": "d", "text": "Hay naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "Ã¡rbol", "native": "Ã¡rvore",
                    "npc_reaction": "Hay Ã¡rboles. E piedras. E o velho Ernesto.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel tirou do bolso uma naranja e te deu. Quantas laranjas ele deu?",
                    "options": [
                        {"id": "a", "text": "Una naranja"},
                        {"id": "b", "text": "Dos naranjas"},
                        {"id": "c", "text": "Tres naranjas"},
                        {"id": "d", "text": "Cinco naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_uno", "target": "uno", "native": "um",
                    "npc_reaction": "Una. SÃ³ uma. Guarda pro caminho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿Y cÃ³mo estÃ¡s â€” con todo esto?",
                    "translation": "E como vocÃª estÃ¡ â€” com tudo isso?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O pueblo estÃ¡ estranho, Miguel estÃ¡ tenso, hÃ¡ um homem que te observa hÃ¡ dias. Como vocÃª estÃ¡?",
                    "options": [
                        {"id": "a", "text": "Tengo un poco de miedo"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Hay mucho"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Normal. Eu tambÃ©m. Mas fica perto de mim.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra fogueira dos oleiros ao longe. 'Â¿QuÃ© hay allÃ¡?' VocÃª vÃª a chama:",
                    "options": [
                        {"id": "a", "text": "Hay fuego"},
                        {"id": "b", "text": "Hay agua"},
                        {"id": "c", "text": "Hay naranjas"},
                        {"id": "d", "text": "Hay pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": "Fuego. Distante â€” tudo bem. Longe do pueblo â€” melhor.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel para em frente Ã  iglesia e ensina o imperativo bÃ¡sico:
    # Â¡Corre! / Â¡Para! / Â¡Mira! â€” verbos de aÃ§Ã£o urgente.
    # Ele diz que o protagonista pode precisar entender ordens gritadas.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel parou na frente da iglesia. Olhou pra vocÃª com "
                    "aquela seriedade nova. 'Tem coisa que vocÃª precisa entender "
                    "quando alguÃ©m grita. NÃ£o Ã© vocabulÃ¡rio â€” Ã© sobrevivÃªncia.'"
                ),
                "now": "Don Miguel ensina comandos urgentes: Â¡Corre! Â¡Para! Â¡Mira!",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel chegou perto e falou baixo. 'Aqui no campo, quando as coisas ficam feias, as pessoas gritam.'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Si alguien grita 'Â¡Corre!' â€” corres. No preguntas. Corres.",
                    "translation": "Se alguÃ©m gritar 'Â¡Corre!' â€” vocÃª corre. NÃ£o pergunta. Corre.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "Â¡Corre!",
                    "meaning": "Corre! (imperativo â€” ordem imediata)",
                    "note": "correr = correr | Â¡Corre! = ordem pra vocÃª correr agora",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y si gritan 'Â¡Para!' â€” paras. Quieto. Sin moverse.",
                    "translation": "E se gritarem 'Â¡Para!' â€” vocÃª para. Quieto. Sem se mover.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "Â¡Para!",
                    "meaning": "Para! (imperativo â€” ordem pra parar imediatamente)",
                    "note": "Oposto de Â¡Corre! â€” um te move, o outro te imobiliza",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y 'Â¡Mira!' â€” alguien quiere que veas algo. Importante. Miras.",
                    "translation": "E 'Â¡Mira!' â€” alguÃ©m quer que vocÃª veja algo. Importante. VocÃª olha.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "Â¡Mira!",
                    "meaning": "Olha! / VÃª isso! (imperativo â€” ordem pra prestar atenÃ§Ã£o)",
                    "note": "mirar = olhar | Â¡Mira! = olha agora",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Â¡Corre!",  "isKey": True},
                        {"text": " Â· ",      "isKey": False},
                        {"text": "Â¡Para!",   "isKey": True},
                        {"text": " Â· ",      "isKey": False},
                        {"text": "Â¡Mira!",   "isKey": True},
                    ],
                    "example": "Â¡Miguel grita: Â¡Corre! â€” corres. Grita Â¡Para! â€” paras.",
                    "translation": "Miguel grita: Â¡Corre! â€” vocÃª corre. Grita Â¡Para! â€” vocÃª para.",
                    "note": "NÃ£o traduz â€” sÃ³ age. O corpo entende antes da cabeÃ§a.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel grita repentinamente: 'Â¡Corre!' O que vocÃª faz?",
                    "options": [
                        {"id": "a", "text": "Corro â€” sem perguntar"},
                        {"id": "b", "text": "Fico parado esperando"},
                        {"id": "c", "text": "Pergunto o que aconteceu"},
                        {"id": "d", "text": "Falo 'buenos dÃ­as'"},
                    ],
                    "correct": "a",
                    "word_id": "es_correr", "target": "correr", "native": "correr",
                    "npc_reaction": "Corro. Sem perguntar. Isso salva vidas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel sussurra 'Â¡Para!' no meio do caminho. VocÃª:",
                    "options": [
                        {"id": "a", "text": "Paro. Quieto. Escuto."},
                        {"id": "b", "text": "Continuo caminhando"},
                        {"id": "c", "text": "ComeÃ§o a correr"},
                        {"id": "d", "text": "Pergunto 'Â¿cÃ³mo estÃ¡s?'"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Para. Quieto. Ele ouviu algo. VocÃª ouviu tambÃ©m â€” depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra uma sombra no fim da rua e sussurra 'Â¡Mira!' O que ele quer?",
                    "options": [
                        {"id": "a", "text": "Que eu olhe â€” ele viu algo"},
                        {"id": "b", "text": "Que eu corra"},
                        {"id": "c", "text": "Que eu coma"},
                        {"id": "d", "text": "Que eu durma"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Mira. VocÃª olhou. A sombra era sÃ³ uma crianÃ§a com uma vela.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um cachorro latiu do nada perto de vocÃªs â€” ruÃ­do alto. Don Miguel grita: 'Â¡Corre!' VocÃª:",
                    "options": [
                        {"id": "a", "text": "Corro â€” instinto antes de pensar"},
                        {"id": "b", "text": "Fico quieto com medo"},
                        {"id": "c", "text": "Cumprimento o cachorro"},
                        {"id": "d", "text": "Pergunto o que Ã© 'corre'"},
                    ],
                    "correct": "a",
                    "word_id": "es_correr", "target": "correr", "native": "correr",
                    "npc_reaction": "Correu. Bom. O corpo aprendeu antes da cabeÃ§a.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel treina o protagonista em situaÃ§Ãµes de urgÃªncia:
    # reaÃ§Ã£o a comandos, uso de miedo/fuego/correr em frases.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel te ensinou os trÃªs comandos que vocÃª vai ouvir quando "
                    "as coisas ficarem feias: Â¡Corre!, Â¡Para!, Â¡Mira!. E vocÃª aprendeu "
                    "fuego, miedo, correr esta tarde â€” sem querer.\n\n"
                    "'Agora vou ver se ficou.' Ele ainda estÃ¡ muito sÃ©rio."
                ),
                "now": "PrÃ¡tica rÃ¡pida â€” situaÃ§Ãµes urgentes, respostas rÃ¡pidas.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Escena 1: Hay fuego en una casa. Â¿QuÃ© haces?",
                    "translation": "Cena 1: Tem fogo numa casa. O que vocÃª faz?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "FumaÃ§a saindo pela janela de uma casa. Chamas visÃ­veis. O que vocÃª faz?",
                    "options": [
                        {"id": "a", "text": "Â¡Corro! Busco ayuda."},
                        {"id": "b", "text": "Me quedo â€” hay mucho fuego"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_correr", "target": "correr", "native": "correr",
                    "npc_reaction": "Â¡Corro! Correto. Fogo = corre, grita, busca ajuda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª estÃ¡ correndo de uma ameaÃ§a. Seu coraÃ§Ã£o dispara, suas mÃ£os tremem. O que vocÃª sente?",
                    "options": [
                        {"id": "a", "text": "Tengo miedo"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Hay naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Normal. Mas o corpo corre mesmo com miedo â€” lembra disso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Escena 2: Alguien grita 'Â¡Para!' detrÃ¡s de ti. Â¿QuÃ© haces?",
                    "translation": "Cena 2: AlguÃ©m grita 'Â¡Para!' atrÃ¡s de vocÃª. O que faz?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'Â¡PARA!' â€” grito atrÃ¡s de vocÃª. O que vocÃª faz?",
                    "options": [
                        {"id": "a", "text": "Paro. Imediatamente."},
                        {"id": "b", "text": "Corro mais rÃ¡pido"},
                        {"id": "c", "text": "Pergunto quem estÃ¡ gritando"},
                        {"id": "d", "text": "Falo 'buenos dÃ­as'"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Para. Antes de pensar. Isso.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra uma fogueira dos oleiros ainda ativa: 'Â¿QuÃ© hay allÃ¡?'",
                    "options": [
                        {"id": "a", "text": "Hay fuego"},
                        {"id": "b", "text": "Hay agua"},
                        {"id": "c", "text": "Hay naranjas"},
                        {"id": "d", "text": "No hay nada"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": "Fuego. Controlado. Por enquanto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "El fuego â€” Â¿mucho o poco?",
                    "translation": "O fogo â€” muito ou pouco?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "A fogueira dos oleiros Ã© enorme â€” chamas de dois metros, calor sentido de longe. O fuego Ã©:",
                    "options": [
                        {"id": "a", "text": "Mucho fuego"},
                        {"id": "b", "text": "Poco fuego"},
                        {"id": "c", "text": "Una naranja"},
                        {"id": "d", "text": "Tres fuegos"},
                    ],
                    "correct": "a",
                    "word_id": "es_mucho", "target": "mucho", "native": "muito",
                    "npc_reaction": "Mucho fuego. Longe Ã© bonito. Perto â€” perigo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª estÃ¡ com medo de alguma coisa mas nÃ£o sabe nomear bem. Don Miguel olha: 'Â¿EstÃ¡s bien?' VocÃª responde honestamente:",
                    "options": [
                        {"id": "a", "text": "No... tengo miedo"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Hay fuego"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Eu tambÃ©m. Isso significa que estamos prestando atenÃ§Ã£o.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Bien hecho. Ahora vamos a la posada. QuÃ©date cerca.",
                    "translation": "Bem feito. Agora vamos pra posada. Fica perto de mim.",
                    "pace": "slow",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Noite. Posada. Don Miguel estÃ¡ mais sÃ©rio que nunca. Ele faz o protagonista
    # revisar tudo â€” as palavras do comeÃ§o e as novas de hoje. A narrativa Ã© mais
    # pesada. VocÃª percebe que ele estÃ¡ te preparando pra algo.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "VocÃªs voltaram pra posada com o sol se pondo. Don Miguel trancou "
                    "a porta da posada por dentro â€” algo que nÃ£o fazia antes.\n\n"
                    "Sentaram na mesa de madeira com uma vela no meio. Ele te olhou "
                    "direto. 'O homem que Carmen me contou â€” eu vi ele hoje. Ele "
                    "sabe onde vocÃª dorme.'"
                ),
                "now": "Don Miguel faz uma revisÃ£o final â€” como se fosse a Ãºltima antes de algo acontecer.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "A vela tremeu com um vento de baixo da porta. Don Miguel nÃ£o se mexeu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ãšltimo repaso antes de dormir. Necesito saber que lo tienes.",
                    "translation": "Ãšltima revisÃ£o antes de dormir. Preciso saber que vocÃª tem isso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra vocÃª: 'Si alguien pregunta quiÃ©n eres â€” dices...'",
                    "options": [
                        {"id": "a", "text": "Me llamo [nome]. Soy el forastero de Miguel."},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "No hay nadie"},
                        {"id": "d", "text": "Hay fuego"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "De Miguel. Correto. Isso muda como tratam vocÃª.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra prÃ³pria cabeÃ§a. 'Si alguien grita Â¡Corre! â€” sin pensar, tÃº...'",
                    "options": [
                        {"id": "a", "text": "Corro"},
                        {"id": "b", "text": "Fico parado"},
                        {"id": "c", "text": "Pergunto o que aconteceu"},
                        {"id": "d", "text": "Digo 'buenos dÃ­as'"},
                    ],
                    "correct": "a",
                    "word_id": "es_correr", "target": "correr", "native": "correr",
                    "npc_reaction": "Corro. Antes de pensar. Sempre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "A vela apagou. Escuro total. CoraÃ§Ã£o disparou. O que vocÃª sente?",
                    "options": [
                        {"id": "a", "text": "Miedo"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "AlegrÃ­a"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Normal. Mas a vela acendeu de novo â€” estava sÃ³ com vento.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Bien. Duerme. Si hay algÃºn problema â€” grito tu nombre.",
                    "translation": "Bem. Dorme. Se houver qualquer problema â€” grito seu nome.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'si hay algÃºn problema'. 'Â¿Hay algÃºn problema ahora?' â€” como vocÃª responde honestamente?",
                    "options": [
                        {"id": "a", "text": "No sÃ©... hay algo raro en el pueblo"},
                        {"id": "b", "text": "No hay nada, estoy bien"},
                        {"id": "c", "text": "Hay muchas naranjas"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Hay algo raro. SÃ­. VocÃª estÃ¡ sentindo certo. Fica alerta.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel apagou a vela principal, ficou sÃ³ com uma "
                        "pequena na janela. VocÃª deitou sem conseguir dormir, "
                        "ouvindo o vento e os passos lÃ¡ fora."
                    ),
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo â€” La Primera Chispa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Madrugada. O protagonista ouviu um barulho e saiu pro corredor da posada.
    # El Vigilante Oscuro estÃ¡ lÃ¡. Miguel estÃ¡ dormindo e nÃ£o vai ouvir.
    #
    # SISTEMA DE PODER â€” LA PALABRA VIVA:
    # Cada exercÃ­cio certo = entendeu a palavra de verdade = poder manifesto.
    # "Fuego" acertado sob pressÃ£o extrema â†’ a palavra se torna fÃ­sica.
    # O protagonista NÃƒO controla. NÃƒO quis. Aconteceu.
    # El Vigilante recua. Miguel aparece. Olha pras mÃ£os do protagonista.
    #
    # SeÃ§Ã£o gated â€” errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Madrugada. VocÃª acordou com um som â€” madeira rangendo no "
                    "corredor. Pensou que era vento. Mas o som voltou. VocÃª se "
                    "levantou devagar, empurrou a porta do quarto."
                ),
                "now": "VocÃª estÃ¡ no corredor escuro da posada. El Vigilante Oscuro estÃ¡ ali.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ‘ Corredor da posada. SÃ³ uma fresta de luar pela janela. Uma silhueta parada no fim do corredor.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Te encontrÃ©, forastero.",
                    "translation": "Te encontrei, forasteiro.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Suas pernas queriam correr. Mas vocÃª estava de costas pra porta do quarto de Miguel.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": "O homem avanÃ§ou dois passos. Seu estÃ´mago afundou. O que vocÃª sente?",
                    "options": [
                        {"id": "a", "text": "Miedo â€” muito miedo"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Hay naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": (
                        "Miedo. A palavra Ã© real â€” vocÃª a sentiu inteira, do estÃ´mago "
                        "Ã s pontas dos dedos. E de algum jeito, sentir a palavra de "
                        "verdade mudou algo no ar."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸ—¡ï¸ El Vigilante parou. Olhou pras suas mÃ£os. VocÃª tambÃ©m olhou. Nada de diferente. Mas ele hesitou.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Â¿QuÃ© eres tÃº, forastero?",
                    "translation": "O que vocÃª Ã©, forasteiro?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª nÃ£o tinha resposta. Mas uma palavra surgiu â€” nÃ£o "
                        "com a cabeÃ§a. Com o peito. Com o calor que vocÃª sentiu "
                        "olhando pra fogueira dos oleiros mais cedo."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": (
                        "El Vigilante avanÃ§a. VocÃª precisa de algo â€” proteÃ§Ã£o, luz, calor, "
                        "barreira. Uma palavra pulsa no peito. Qual Ã© ela?"
                    ),
                    "options": [
                        {"id": "a", "text": "ðŸ”¥ Fuego"},
                        {"id": "b", "text": "ðŸ’§ Agua"},
                        {"id": "c", "text": "ðŸª¨ Piedra"},
                        {"id": "d", "text": "ðŸŠ Naranja"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": (
                        "FUEGO â€” a palavra saiu antes de vocÃª pensar.\n\n"
                        "E o corredor explodiu em luz.\n\n"
                        "NÃ£o uma fogueira. NÃ£o uma faÃ­sca. Uma parede de fogo "
                        "entre vocÃª e o vigilante â€” alta, quente, real. SaÃ­da das "
                        "suas mÃ£os abertas.\n\n"
                        "El Vigilante caiu pra trÃ¡s gritando. VocÃª olhou pras "
                        "prÃ³prias mÃ£os â€” pele intacta, sem queimadura. Como se "
                        "o fogo nÃ£o fosse seu pra queimar."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸ”¥ O fogo durou trÃªs segundos. Depois sumiu. O corredor estava escuro de novo. El Vigilante tinha ido embora.",
                },
                {
                    "kind": "player",
                    "text": "VocÃª ficou parado olhando pras mÃ£os. Tremendo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¡Â¿QuÃ© fue eso?! Â¡Forastero! Â¿EstÃ¡s bien?",
                    "translation": "O que foi isso?! Forasteiro! VocÃª estÃ¡ bem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel abriu a porta gritando. Viu o corredor vazio e vocÃª parado tremendo. 'Â¿EstÃ¡s bien?'",
                    "options": [
                        {"id": "a", "text": "No sÃ©... fuego. SaliÃ³ de mis manos."},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": (
                        "Don Miguel ficou em silÃªncio. Olhou pras suas mÃ£os. "
                        "Olhou pro corredor. Olhou de volta pra vocÃª.\n\n"
                        "NÃ£o era a expressÃ£o de quem duvidava. Era a expressÃ£o "
                        "de quem jÃ¡ sabia que algo assim ia acontecer."
                    ),
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "...Entra. Cierra la puerta. Tenemos que hablar.",
                    "translation": "...Entra. Fecha a porta. A gente precisa conversar.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª entrou no quarto de Don Miguel. Ele trancou a porta "
                        "e ficou de costas pra vocÃª por um longo momento.\n\n"
                        "Quando virou, o rosto era diferente. NÃ£o mais o campesino "
                        "paciente que te ensinava saudaÃ§Ãµes. Era alguÃ©m que guardava "
                        "segredo faz muito tempo e acabou de decidir parar."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
