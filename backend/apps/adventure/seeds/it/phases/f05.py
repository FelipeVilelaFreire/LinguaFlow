"""
Seed das 6 seÃ§Ãµes da Fase 5 Italiano A1 â€” "La Prima Scintilla".

Algo estÃ errado no borgo. La Guardia â€” o homem do chapÃ©u baixo
visto em F2 e F4 â€” age mais abertamente. Antonio comeÃ§a a preparar o
protagonista. E na S6, sozinho numa rua escura, o protagonista usa uma
palavra pela primeira vez de verdade â€” fuoco â€” e ela se torna fÃ­sica.

Esta Ã© a primeira apariÃ§Ã£o de La Palabra Viva. NÃ£o Ã© herÃ³ica. Ã‰ acidental,
aterrorizante, e muda tudo.

REGRA DO SISTEMA DE PODER:
Acertar a palavra â‰  matar o inimigo.
Acertar a palavra = entendeu de verdade = a palavra se torna real = poder manifesto.
DEPOIS, com o poder em mÃ£os, o protagonista pode agir.
Nunca: "vocÃª acertou, portanto venceu." Sempre: "vocÃª acertou â†’ poder ganho â†’ vocÃª escolhe."

Novos vocab (3): paura · fuoco · correre
RevisÃ£o F1â€“F4: ciao, buongiorno, grazie, bene/male, mi chiamo, straniero,
               c'e/non c'e, pane, acqua, Ãrbol, pietra, mela, tre, molto/poco
NPC principal:   Antonio (fio condutor â€” mais sÃ©rio a partir daqui)
NPC antagonista: La Guardia (agente â€” confronto na S6)
Arco emocional:  seguro â†’ ameaÃ§ado â†’ poder acidental â†’ assustado com si mesmo
TransiÃ§Ã£o:       Nico olha pro protagonista de um jeito diferente. A fase seguinte
                 comeÃ§a com uma conversa sÃ©ria.

PrÃ©-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Tarde fechada. Nico mais quieto que o normale. Leva o protagonista por
    # uma rota diferente â€” ruas menos movimentadas. Mostra algo no caminho:
    # uma fogueira de oleiros, crianÃ§as corrindo com medo de cachorro.
    # Vocab (paura/fuoco/correre) aparece sem traduÃ§Ã£o â€” imersÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ† Tarde fechada em Santa Chiara. Nuvens pesadas, sem sol. "
                        "Antonio chegou na locanda mais cedo que o normale e te chamou "
                        "sem explicaÃ§Ã£o â€” 'Vem.' Uma rota diferente pelo borgo."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Ci sono cose che devi sapere. Non mi piace il borgo oggi.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª seguiu sem perguntar. O tom dele era diferente â€” nÃ£o amigÃvel, nÃ£o preocupado. Alerta.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸ”¥ Num beco lateral, um grupo de oleiros mantÃ©m uma fogueira grande â€” fumaÃ§a escura subindo pelo beco.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Fuoco. Lo controllano, per ora. Ma il fuoco non avvisa.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Fuoco. A chama era enorme, quente, barulhenta. VocÃª ficou parado olhando.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Che cosa senti quando lo guardi?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o tinha a palavra ainda. Mas o cheiro, o calor, o som â€” algo no fogo te puxava.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸƒ TrÃªs crianÃ§as dobram a esquina gritando â€” um cachorro latindo atrÃs. Elas corrim, rindo de susto.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Corrin! El cane solo ladra â€” no muerde. Pero el paura hace correre igual.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Corrin. Paura. Duas palavras novas num segundo. O cachorro passou pelo lado de vocÃªs sem parar.",
                },
            ],
            "exercises": [
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "A fogueira dos oleiros era enorme, quente, iluminava o beco inteiro. Como essa coisa se chama?",
                    "options": [
                        {"id": "a", "text": "Fuoco"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Pietra"},
                        {"id": "d", "text": "Ãrbol"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": "Fuoco. Quente. NÃ£o avisa â€” sÃ³ aparece.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "As crianÃ§as viram o cachorro e saÃ­ram disparadas â€” pernas rÃpidas, gritos. O que elas fizeram?",
                    "options": [
                        {"id": "a", "text": "Corrieron â€” elas correream"},
                        {"id": "b", "text": "Comieron â€” elas comeram"},
                        {"id": "c", "text": "Cantaron â€” elas cantaram"},
                        {"id": "d", "text": "Durmieron â€” elas dorguardam"},
                    ],
                    "correct": "a",
                    "word_id": "it_correre", "target": "correre", "native": "correre",
                    "npc_reaction": "Corrieron. O cachorro faz isso com todo mundo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio disse que o paura faz as crianÃ§as correre mesmo sem perigo real. O que Ã© 'paura'?",
                    "options": [
                        {"id": "a", "text": "Medo"},
                        {"id": "b", "text": "Alegria"},
                        {"id": "c", "text": "Fome"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Todo mundo tem. O que importa Ã© o que vocÃª faz com ele.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio para, olha ao redor, e diz 'Non mi piace il borgo oggi'. Como vocÃª estÃ se sentindo?",
                    "options": [
                        {"id": "a", "text": "Un poco de paura"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "C'e mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Bom â€” o paura avisa. Escuta ele.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Antonio leva o protagonista por um caminho mais seguro â€” perto da
    # iglesia. RevisÃ£o F1â€“F4 com contexto de tensÃ£o crescente.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "VocÃªs saÃ­ram do beco das fogueiras. Antonio caminha perto, "
                    "mais de perto que de costume. VocÃª aprendeu 'fuoco', 'correre' "
                    "e 'paura' pela observaÃ§Ã£o â€” sem liÃ§Ã£o.\n\n"
                    "As outras palavras estÃ£o lÃ: ciao, buongiorno, grazie, bene, "
                    "ho fame, ho sete, c'e, Ãrbol, pietra, mela, tre, "
                    "molto, poco. Antonio continua te testando â€” mesmo com esse humor."
                ),
                "now": "RevisÃ£o das fases anteriores num contexto mais tenso.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio para na sombra da iglesia. Olha a praÃ§a vazia. Uma vela dentro pela janela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Enquanto caminhamos â€” vamos revisar. O que vocÃª aprendeu que pode ajudar agora?",
                    "translation": "Enquanto caminhamos â€” vamos revisar. O que vocÃª aprendeu que pode ajudar agora?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um homem desconhecido para na outra ponta da rua e olha pra vocÃªs. Como vocÃª cumprimenta â€” Ã© de tarde:",
                    "options": [
                        {"id": "a", "text": "Buonasera!"},
                        {"id": "b", "text": "Buongiorno!"},
                        {"id": "c", "text": "Buonanotte!"},
                        {"id": "d", "text": "Ciao noche!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenas_tardes", "target": "buonasera", "native": "boa tarde",
                    "npc_reaction": "Buonasera. O homem nÃ£o respondeu. Seguiu em frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y si alguien nuevo llega al borgo y pregunta tu nombre?",
                    "translation": "E se alguÃ©m novo chegar ao borgo e perguntar seu nome?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um straniero novo para perto de vocÃªs: 'Come ti chiami?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "C'e fuoco"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "Mi chiamo. Sempre diga seu nome â€” nÃ£o esconde.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "QuÃ© habÃ­a ayer en il campo â€” cerca del rÃ­o?",
                    "translation": "O que havia ontem no campo â€” perto do rÃ­o?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "No campo ontem havia Ãrvores, pedras e o rÃ­o. Antonio: 'C'e Ãrboles cerca del rÃ­o?'",
                    "options": [
                        {"id": "a", "text": "SÃ­, c'e Ãrboles y pietre"},
                        {"id": "b", "text": "Non c'e nada"},
                        {"id": "c", "text": "C'e fuoco"},
                        {"id": "d", "text": "C'e mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "Ãrbol", "native": "Ãrvore",
                    "npc_reaction": "C'e Ãrboles. E pietre. E o velho Pietro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio tirou do bolso uma mela e te deu. Quantas laranjas ele deu?",
                    "options": [
                        {"id": "a", "text": "Una mela"},
                        {"id": "b", "text": "Due mele"},
                        {"id": "c", "text": "Tre mele"},
                        {"id": "d", "text": "Cinco mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_uno", "target": "uno", "native": "um",
                    "npc_reaction": "Una. SÃ³ uma. Guarda pro caminho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y come stai â€” con todo esto?",
                    "translation": "E como vocÃª estÃ â€” com tudo isso?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O borgo estÃ estranho, Nico estÃ tenso, hÃ um homem que te observa hÃ dias. Como vocÃª estÃ?",
                    "options": [
                        {"id": "a", "text": "Ho un poco de paura"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "C'e molto"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Normale. Eu tambÃ©m. Mas fica perto de mim.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra fogueira dos oleiros ao longe. 'Che cosa c e laggiu?' VocÃª vÃª a chama:",
                    "options": [
                        {"id": "a", "text": "C'e fuoco"},
                        {"id": "b", "text": "C'e acqua"},
                        {"id": "c", "text": "C'e mele"},
                        {"id": "d", "text": "C'e pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": "Fuoco. Distante â€” tudo bem. Longe do borgo â€” melhor.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: GramÃtica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Antonio para em frente Ã  iglesia e ensina o imperativo bÃsico:
    # Corri! / Fermo! / Guarda! â€” verbos de aÃ§Ã£o urgente.
    # Ele diz que o protagonista pode precisar entender ordens gritadas.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Antonio parou na frente da iglesia. Olhou pra vocÃª com "
                    "aquela seriedade nova. 'Tem coisa que vocÃª precisa entender "
                    "quando alguÃ©m grita. NÃ£o Ã© vocabulÃrio â€” Ã© sobrevivÃªncia.'"
                ),
                "now": "Antonio ensina comandos urgentes: Corri! Fermo! Guarda!",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio chegou perto e falou baixo. 'Aqui no campo, quando as coisas ficam feias, as pessoas gritam.'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Se qualcuno grida 'Corri!', corri. Non chiedi. Corri.",
                    "translation": "Se alguÃ©m gritar 'Corri!' â€” vocÃª corri. NÃ£o pergunta. Corri.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "Corri!",
                    "meaning": "Corri! (imperativo â€” ordem imediata)",
                    "note": "correre = correre | Corri! = ordem pra vocÃª correre agora",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y si gritan 'Fermo!' â€” paras. Quieto. Sin moverse.",
                    "translation": "E se gritarem 'Fermo!' â€” vocÃª para. Quieto. Sem se mover.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "Fermo!",
                    "meaning": "Fermo! (imperativo â€” ordem pra parar imediatamente)",
                    "note": "Oposto de Corri! â€” um te move, o outro te imobiliza",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y 'Guarda!' â€” alguien vuole que veas algo. Importante. Guardas.",
                    "translation": "E 'Guarda!' â€” alguÃ©m quer que vocÃª veja algo. Importante. VocÃª olha.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "Guarda!",
                    "meaning": "Olha! / VÃª isso! (imperativo â€” ordem pra prestar atenÃ§Ã£o)",
                    "note": "guardar = olhar | Guarda! = olha agora",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Corri!",  "isKey": True},
                        {"text": " · ",      "isKey": False},
                        {"text": "Fermo!",   "isKey": True},
                        {"text": " · ",      "isKey": False},
                        {"text": "Guarda!",   "isKey": True},
                    ],
                    "example": "Nico grita: Corri! â€” corris. Grita Fermo! â€” paras.",
                    "translation": "Nico grita: Corri! â€” vocÃª corri. Grita Fermo! â€” vocÃª para.",
                    "note": "NÃ£o traduz â€” sÃ³ age. O corpo entende antes da cabeÃ§a.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio grita repentinamente: 'Corri!' O que vocÃª faz?",
                    "options": [
                        {"id": "a", "text": "Corro â€” sem perguntar"},
                        {"id": "b", "text": "Fico parado esperando"},
                        {"id": "c", "text": "Pergunto o que aconteceu"},
                        {"id": "d", "text": "Falo 'buongiorno'"},
                    ],
                    "correct": "a",
                    "word_id": "it_correre", "target": "correre", "native": "correre",
                    "npc_reaction": "Corro. Sem perguntar. Isso salva vidas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio sussurra 'Fermo!' no meio do caminho. VocÃª:",
                    "options": [
                        {"id": "a", "text": "Paro. Quieto. Escuto."},
                        {"id": "b", "text": "Continuo caminhando"},
                        {"id": "c", "text": "ComeÃ§o a correre"},
                        {"id": "d", "text": "Pergunto 'come stai?'"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Para. Quieto. Ele ouviu algo. VocÃª ouviu tambÃ©m â€” depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra uma sombra no fim da rua e sussurra 'Guarda!' O que ele quer?",
                    "options": [
                        {"id": "a", "text": "Que eu olhe â€” ele viu algo"},
                        {"id": "b", "text": "Que eu corra"},
                        {"id": "c", "text": "Que eu coma"},
                        {"id": "d", "text": "Que eu durma"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Guarda. VocÃª olhou. A sombra era sÃ³ uma crianÃ§a com uma vela.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um cachorro latiu do nada perto de vocÃªs â€” ruÃ­do alto. Antonio grita: 'Corri!' VocÃª:",
                    "options": [
                        {"id": "a", "text": "Corro â€” instinto antes de pensar"},
                        {"id": "b", "text": "Fico quieto com medo"},
                        {"id": "c", "text": "Cumprimento o cachorro"},
                        {"id": "d", "text": "Pergunto o que Ã© 'corri'"},
                    ],
                    "correct": "a",
                    "word_id": "it_correre", "target": "correre", "native": "correre",
                    "npc_reaction": "Corriu. Bom. O corpo aprendeu antes da cabeÃ§a.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: PrÃtica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Antonio treina o protagonista em situaÃ§Ãµes de urgÃªncia:
    # reaÃ§Ã£o a comandos, uso de paura/fuoco/correre em frases.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Antonio te ensinou os trÃªs comandos que vocÃª vai ouvir quando "
                    "as coisas ficarem feias: Corri!, Fermo!, Guarda!. E vocÃª aprendeu "
                    "fuoco, paura, correre esta tarde â€” sem querer.\n\n"
                    "'Agora vou ver se ficou.' Ele ainda estÃ muito sÃ©rio."
                ),
                "now": "PrÃtica rÃpida â€” situaÃ§Ãµes urgentes, respostas rÃpidas.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Scena 1: C'e fuoco in una casa. Che fai?",
                    "translation": "Cena 1: Tem fogo numa casa. O que vocÃª faz?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "FumaÃ§a saindo pela janela de uma casa. Chamas visÃ­veis. O que vocÃª faz?",
                    "options": [
                        {"id": "a", "text": "Corro! Busco ayuda."},
                        {"id": "b", "text": "Me quedo â€” c'e molto fuoco"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_correre", "target": "correre", "native": "correre",
                    "npc_reaction": "Corro! Corrito. Fogo = corri, grita, busca ajuda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª estÃ corrindo de uma ameaÃ§a. Seu coraÃ§Ã£o dispara, suas mÃ£os tremem. O que vocÃª sente?",
                    "options": [
                        {"id": "a", "text": "Ho paura"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Estoy bene"},
                        {"id": "d", "text": "C'e mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Normale. Mas o corpo corri mesmo com paura â€” lembra disso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Scena 2: Qualcuno grida 'Fermo!' detrÃs de ti. Che fai?",
                    "translation": "Cena 2: AlguÃ©m grita 'Fermo!' atrÃs de vocÃª. O que faz?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "'PARA!' â€” grito atrÃs de vocÃª. O que vocÃª faz?",
                    "options": [
                        {"id": "a", "text": "Paro. Imediatamente."},
                        {"id": "b", "text": "Corro mais rÃpido"},
                        {"id": "c", "text": "Pergunto quem estÃ gritando"},
                        {"id": "d", "text": "Falo 'buongiorno'"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Para. Antes de pensar. Isso.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra uma fogueira dos oleiros ainda ativa: 'Che cosa c e laggiu?'",
                    "options": [
                        {"id": "a", "text": "C'e fuoco"},
                        {"id": "b", "text": "C'e acqua"},
                        {"id": "c", "text": "C'e mele"},
                        {"id": "d", "text": "Non c'e nada"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": "Fuoco. Controlado. Por enquanto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "El fuoco â€” molto o poco?",
                    "translation": "O fogo â€” muito ou pouco?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "A fogueira dos oleiros Ã© enorme â€” chamas de dois metros, calor sentido de longe. O fuoco Ã©:",
                    "options": [
                        {"id": "a", "text": "Molto fuoco"},
                        {"id": "b", "text": "Poco fuoco"},
                        {"id": "c", "text": "Una mela"},
                        {"id": "d", "text": "Tre fuocos"},
                    ],
                    "correct": "a",
                    "word_id": "it_molto", "target": "molto", "native": "muito",
                    "npc_reaction": "Molto fuoco. Longe Ã© bonito. Perto â€” perigo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "VocÃª estÃ com medo de alguma coisa mas nÃ£o sabe nomear bem. Antonio olha: 'Stai bene?' VocÃª responde honestamente:",
                    "options": [
                        {"id": "a", "text": "No... ho paura"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "C'e fuoco"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Eu tambÃ©m. Isso significa que estamos prestando atenÃ§Ã£o.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ben fatto. Ora andiamo alla locanda. Resta vicino.",
                    "translation": "Bem feito. Agora vamos pra locanda. Fica perto de mim.",
                    "pace": "slow",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Noite. Locanda. Antonio estÃ mais sÃ©rio que nunca. Ele faz o protagonista
    # revisar tudo â€” as palavras do comeÃ§o e as novas de hoje. A narrativa Ã© mais
    # pesada. VocÃª percebe que ele estÃ te preparando pra algo.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "VocÃªs voltaram pra locanda com o sol se pondo. Antonio trancou "
                    "a porta da locanda por dentro â€” algo que nÃ£o fazia antes.\n\n"
                    "Sentaram na mesa de madeira com uma vela no meio. Ele te olhou "
                    "direto. 'O homem que Bianca me contou â€” eu vi ele hoje. Ele "
                    "sabe onde vocÃª dorme.'"
                ),
                "now": "Antonio faz uma revisÃ£o final â€” como se fosse a Ãºltima antes de algo acontecer.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "A vela tremeu com um vento de baixo da porta. Antonio nÃ£o se mexeu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ultimo ripasso prima di dormire. Devo sapere che lo sai.",
                    "translation": "Ãšltima revisÃ£o antes de dormir. Preciso saber que vocÃª tem isso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra vocÃª: 'Se qualcuno chiede chi sei, dici...'",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [nome]. Soy el straniero de Nico."},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Non c'e nadie"},
                        {"id": "d", "text": "C'e fuoco"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "De Nico. Corrito. Isso muda como tratam vocÃª.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra prÃ³pria cabeÃ§a. 'Si alguien grita Corri! â€” sin pensar, tÃº...'",
                    "options": [
                        {"id": "a", "text": "Corro"},
                        {"id": "b", "text": "Fico parado"},
                        {"id": "c", "text": "Pergunto o que aconteceu"},
                        {"id": "d", "text": "Digo 'buongiorno'"},
                    ],
                    "correct": "a",
                    "word_id": "it_correre", "target": "correre", "native": "correre",
                    "npc_reaction": "Corro. Antes de pensar. Sempre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "A vela apagou. Escuro total. CoraÃ§Ã£o disparou. O que vocÃª sente?",
                    "options": [
                        {"id": "a", "text": "Paura"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "AlegrÃ­a"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Normale. Mas a vela acendeu de novo â€” estava sÃ³ com vento.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Bene. Duerme. Si c'e algÃºn problema â€” grito tu nombre.",
                    "translation": "Bem. Dorme. Se houver qualquer problema â€” grito seu nome.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio disse 'si c'e algÃºn problema'. 'C'e algÃºn problema ora?' â€” como vocÃª responde honestamente?",
                    "options": [
                        {"id": "a", "text": "No sÃ©... c'e algo raro nel borgo"},
                        {"id": "b", "text": "Non c'e nada, estoy bene"},
                        {"id": "c", "text": "C'e muchas mele"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "npc_reaction": "C'e algo raro. SÃ­. VocÃª estÃ sentindo certo. Fica alerta.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio apagou a vela principal, ficou sÃ³ com uma "
                        "pequena na janela. VocÃª deitou sem conseguir dormir, "
                        "ouvindo o vento e os passos lÃ fora."
                    ),
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃculo â€” La Primera Chispa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Madrugada. O protagonista ouviu um barulho e saiu pro corridor da locanda.
    # La Guardia estÃ lÃ. Nico estÃ dormindo e nÃ£o vai ouvir.
    #
    # SISTEMA DE PODER â€” LA PALABRA VIVA:
    # Cada exercÃ­cio certo = entendeu a palavra de verdade = poder manifesto.
    # "Fuoco" acertado sob pressÃ£o extrema â†’ a palavra se torna fÃ­sica.
    # O protagonista NÃƒO controla. NÃƒO quis. Aconteceu.
    # La Guardia recua. Nico aparece. Olha pras mÃ£os do protagonista.
    #
    # SeÃ§Ã£o gated â€” errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Madrugada. VocÃª acordou com um som â€” madeira rangendo no "
                    "corridor. Pensou que era vento. Mas o som voltou. VocÃª se "
                    "levantou devagar, empurrou a porta do quarto."
                ),
                "now": "VocÃª estÃ no corridor escuro da locanda. La Guardia estÃ ali.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ‘ Corridor da locanda. SÃ³ uma fresta de luar pela janela. Uma silhueta parada no fim do corridor.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "Te encontrÃ©, straniero.",
                    "translation": "Te encontrei, straniero.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Suas pernas queriam correre. Mas vocÃª estava de costas pra porta do quarto de Nico.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "La Guardia",
                    "question": "O homem avanÃ§ou dois passos. Seu estÃ´mago afundou. O que vocÃª sente?",
                    "options": [
                        {"id": "a", "text": "Paura â€” muito paura"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Bene, grazie"},
                        {"id": "d", "text": "C'e mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": (
                        "Paura. A palavra Ã© real â€” vocÃª a sentiu inteira, do estÃ´mago "
                        "Ã s pontas dos dedos. E de algum jeito, sentir a palavra de "
                        "verdade mudou algo no ar."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸ—ï¸ La Guardia parou. Olhou pras suas mÃ£os. VocÃª tambÃ©m olhou. Nada de diferente. Mas ele hesitou.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "Che cosa sei tu, straniero?",
                    "translation": "O que vocÃª Ã©, straniero?",
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
                    "npc": "La Guardia",
                    "question": (
                        "La Guardia avanÃ§a. VocÃª precisa de algo â€” proteÃ§Ã£o, luz, calor, "
                        "barreira. Uma palavra pulsa no peito. Qual Ã© ela?"
                    ),
                    "options": [
                        {"id": "a", "text": "ðŸ”¥ Fuoco"},
                        {"id": "b", "text": "ðŸ’§ Acqua"},
                        {"id": "c", "text": "ðŸª¨ Pietra"},
                        {"id": "d", "text": "ðŸŠ Mela"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": (
                        "FUOCO â€” a palavra saiu antes de vocÃª pensar.\n\n"
                        "E o corridor explodiu em luz.\n\n"
                        "NÃ£o uma fogueira. NÃ£o uma faÃ­sca. Uma parede de fogo "
                        "entre vocÃª e o vigilante â€” alta, quente, real. SaÃ­da das "
                        "suas mÃ£os abertas.\n\n"
                        "La Guardia caiu pra trÃs gritando. VocÃª olhou pras "
                        "prÃ³prias mÃ£os â€” pele intacta, sem queimadura. Como se "
                        "o fogo nÃ£o fosse seu pra queimar."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸ”¥ O fogo durou trÃªs segundos. Depois sumiu. O corridor estava escuro de novo. La Guardia tinha ido embora.",
                },
                {
                    "kind": "player",
                    "text": "VocÃª ficou parado olhando pras mÃ£os. Tremendo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Che cos era?! Straniero! Stai bene?",
                    "translation": "O que foi isso?! Forasteiro! VocÃª estÃ bem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio abriu a porta gritando. Viu o corridor vazio e vocÃª parado tremendo. 'Stai bene?'",
                    "options": [
                        {"id": "a", "text": "Non lo so... fuoco. E uscito dalle mie mani."},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Buonanotte"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": (
                        "Antonio ficou em silÃªncio. Olhou pras suas mÃ£os. "
                        "Olhou pro corridor. Olhou de volta pra vocÃª.\n\n"
                        "NÃ£o era a expressÃ£o de quem duvidava. Era a expressÃ£o "
                        "de quem jÃ sabia que algo assim ia acontecer."
                    ),
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "...Entra. Chiudi la porta. Dobbiamo parlare.",
                    "translation": "...Entra. Fecha a porta. A gente precisa conversar.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª entrou no quarto de Antonio. Ele trancou a porta "
                        "e ficou de costas pra vocÃª por um longo momento.\n\n"
                        "Quando virou, o rosto era diferente. NÃ£o mais o contadino "
                        "paciente que te ensinava saudaÃ§Ãµes. Era alguÃ©m que guardava "
                        "segredo faz muito tempo e acabou de decidir parar."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
