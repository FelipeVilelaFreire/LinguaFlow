"""
Seed das 6 seções da Fase 5 Italiano A1 — "La Prima Scintilla".

Algo est? errado no borgo. La Guardia — o homem do chapéu baixo
visto em F2 e F4 — age mais abertamente. Antonio começa a preparar o
protagonista. E na S6, sozinho numa rua escura, o protagonista usa uma
palavra pela primeira vez de verdade — fuoco — e ela se torna física.

Esta é a primeira aparição de La Palabra Viva. Não é heróica. É acidental,
aterrorizante, e muda tudo.

REGRA DO SISTEMA DE PODER:
Acertar a palavra ≠ matar o inimigo.
Acertar a palavra = entendeu de verdade = a palavra se torna real = poder manifesto.
DEPOIS, com o poder em mãos, o protagonista pode agir.
Nunca: "você acertou, portanto venceu." Sempre: "você acertou → poder ganho → você escolhe."

Novos vocab (3): paura · fuoco · correre
Revisão F1–F4: ciao, buongiorno, grazie, bene/male, mi chiamo, straniero,
               c'e/non c'e, pane, acqua, ?rbol, pietra, mela, tre, molto/poco
NPC principal:   Antonio (fio condutor — mais sério a partir daqui)
NPC antagonista: La Guardia (agente — confronto na S6)
Arco emocional:  seguro → ameaçado → poder acidental → assustado com si mesmo
Transição:       Nico olha pro protagonista de um jeito diferente. A fase seguinte
                 começa com uma conversa séria.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Tarde fechada. Nico mais quieto que o normale. Leva o protagonista por
    # uma rota diferente — ruas menos movimentadas. Mostra algo no caminho:
    # uma fogueira de oleiros, crianças corrindo com medo de cachorro.
    # Vocab (paura/fuoco/correre) aparece sem tradução — imersão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌆 Tarde fechada em Santa Chiara. Nuvens pesadas, sem sol. "
                        "Antonio chegou na locanda mais cedo que o normale e te chamou "
                        "sem explicação — 'Vem.' Uma rota diferente pelo borgo."
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
                    "text": "Você seguiu sem perguntar. O tom dele era diferente — não amig?vel, não preocupado. Alerta.",
                },
                {
                    "kind": "scene",
                    "text": "🔥 Num beco lateral, um grupo de oleiros mantém uma fogueira grande — fumaça escura subindo pelo beco.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Fuoco. Lo controllano, per ora. Ma il fuoco non avvisa.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Fuoco. A chama era enorme, quente, barulhenta. Você ficou parado olhando.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Che cosa senti quando lo guardi?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você não tinha a palavra ainda. Mas o cheiro, o calor, o som — algo no fogo te puxava.",
                },
                {
                    "kind": "scene",
                    "text": "?? Três crianças dobram a esquina gritando — um cachorro latindo atr?s. Elas correm, rindo de susto.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Corrin! El cane solo ladra — no muerde. Pero el paura hace correre igual.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Corrin. Paura. Duas palavras novas num segundo. O cachorro passou pelo lado de vocês sem parar.",
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
                        {"id": "d", "text": "Árbol"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": "Fuoco. Quente. Não avisa — só aparece.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "As crianças viram o cachorro e saíram disparadas — pernas r?pidas, gritos. O que elas fizeram?",
                    "options": [
                        {"id": "a", "text": "Corrieron — elas correream"},
                        {"id": "b", "text": "Comieron — elas comeram"},
                        {"id": "c", "text": "Cantaron — elas cantaram"},
                        {"id": "d", "text": "Durmieron — elas dorguardam"},
                    ],
                    "correct": "a",
                    "word_id": "it_correre", "target": "correre", "native": "correre",
                    "npc_reaction": "Corrieron. O cachorro faz isso com todo mundo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio disse que o paura faz as crianças correre mesmo sem perigo real. O que é 'paura'?",
                    "options": [
                        {"id": "a", "text": "Medo"},
                        {"id": "b", "text": "Alegria"},
                        {"id": "c", "text": "Fome"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Todo mundo tem. O que importa é o que você faz com ele.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio para, olha ao redor, e diz 'Non mi piace il borgo oggi'. Como você est? se sentindo?",
                    "options": [
                        {"id": "a", "text": "Un poco de paura"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "C'e mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Bom — o paura avisa. Escuta ele.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Antonio leva o protagonista por um caminho mais seguro — perto da
    # iglesia. Revisão F1–F4 com contexto de tensão crescente.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Vocês saíram do beco das fogueiras. Antonio caminha perto, "
                    "mais de perto que de costume. Você aprendeu 'fuoco', 'correre' "
                    "e 'paura' pela observação — sem lição.\n\n"
                    "As outras palavras estão l?: ciao, buongiorno, grazie, bene, "
                    "ho fame, ho sete, c'e, ?rbol, pietra, mela, tre, "
                    "molto, poco. Antonio continua te testando — mesmo com esse humor."
                ),
                "now": "Revisão das fases anteriores num contexto mais tenso.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Antonio para na sombra da iglesia. Olha a praça vazia. Uma vela dentro pela janela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Enquanto caminhamos — vamos revisar. O que você aprendeu que pode ajudar agora?",
                    "translation": "Enquanto caminhamos — vamos revisar. O que você aprendeu que pode ajudar agora?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um homem desconhecido para na outra ponta da rua e olha pra vocês. Como você cumprimenta — é de tarde:",
                    "options": [
                        {"id": "a", "text": "Buonasera!"},
                        {"id": "b", "text": "Buongiorno!"},
                        {"id": "c", "text": "Buonanotte!"},
                        {"id": "d", "text": "Ciao noche!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenas_tardes", "target": "buonasera", "native": "boa tarde",
                    "npc_reaction": "Buonasera. O homem não respondeu. Seguiu em frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y si alguien nuevo llega al borgo y pregunta tu nombre?",
                    "translation": "E se alguém novo chegar ao borgo e perguntar seu nome?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um straniero novo para perto de vocês: 'Come ti chiami?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "C'e fuoco"},
                        {"id": "d", "text": "Buongiorno"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Mi chiamo. Sempre diga seu nome — não esconde.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Qué había ayer en il campo — cerca del río?",
                    "translation": "O que havia ontem no campo — perto do río?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "No campo ontem havia ?rvores, pedras e o río. Antonio: 'C'e ?rboles cerca del río?'",
                    "options": [
                        {"id": "a", "text": "Sí, c'e ?rboles y pietre"},
                        {"id": "b", "text": "Non c'e nada"},
                        {"id": "c", "text": "C'e fuoco"},
                        {"id": "d", "text": "C'e mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_arbol", "target": "?rbol", "native": "?rvore",
                    "npc_reaction": "C'e ?rboles. E pietre. E o velho Pietro.",
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
                    "npc_reaction": "Una. Só uma. Guarda pro caminho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y come stai — con todo esto?",
                    "translation": "E como você est? — com tudo isso?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "O borgo est? estranho, Nico est? tenso, h? um homem que te observa h? dias. Como você est??",
                    "options": [
                        {"id": "a", "text": "Ho un poco de paura"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "C'e molto"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Normale. Eu também. Mas fica perto de mim.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra fogueira dos oleiros ao longe. 'Che cosa c e laggiu?' Você vê a chama:",
                    "options": [
                        {"id": "a", "text": "C'e fuoco"},
                        {"id": "b", "text": "C'e acqua"},
                        {"id": "c", "text": "C'e mele"},
                        {"id": "d", "text": "C'e pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": "Fuoco. Distante — tudo bem. Longe do borgo — melhor.",
                },
            ],
        },
    },

    # ── Seção 3: Gram?tica Narrativa ───────────────────────────────────────────
    # Antonio para em frente à iglesia e ensina o imperativo b?sico:
    # Corri! / Fermo! / Guarda! — verbos de ação urgente.
    # Ele diz que o protagonista pode precisar entender ordens gritadas.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Antonio parou na frente da iglesia. Olhou pra você com "
                    "aquela seriedade nova. 'Tem coisa que você precisa entender "
                    "quando alguém grita. Não é vocabul?rio — é sobrevivência.'"
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
                    "translation": "Se alguém gritar 'Corri!' — você corri. Não pergunta. Corri.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "Corri!",
                    "meaning": "Corri! (imperativo — ordem imediata)",
                    "note": "correre = correre | Corri! = ordem pra você correre agora",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y si gritan 'Fermo!' — paras. Quieto. Sin moverse.",
                    "translation": "E se gritarem 'Fermo!' — você para. Quieto. Sem se mover.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "Fermo!",
                    "meaning": "Fermo! (imperativo — ordem pra parar imediatamente)",
                    "note": "Oposto de Corri! — um te move, o outro te imobiliza",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Y 'Guarda!' — alguien vuole que veas algo. Importante. Guardas.",
                    "translation": "E 'Guarda!' — alguém quer que você veja algo. Importante. Você olha.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "Guarda!",
                    "meaning": "Olha! / Vê isso! (imperativo — ordem pra prestar atenção)",
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
                    "example": "Nico grita: Corri! — corris. Grita Fermo! — paras.",
                    "translation": "Nico grita: Corri! — você corri. Grita Fermo! — você para.",
                    "note": "Não traduz — só age. O corpo entende antes da cabeça.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio grita repentinamente: 'Corri!' O que você faz?",
                    "options": [
                        {"id": "a", "text": "Corro — sem perguntar"},
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
                    "question": "Antonio sussurra 'Fermo!' no meio do caminho. Você:",
                    "options": [
                        {"id": "a", "text": "Paro. Quieto. Escuto."},
                        {"id": "b", "text": "Continuo caminhando"},
                        {"id": "c", "text": "Começo a correre"},
                        {"id": "d", "text": "Pergunto 'come stai?'"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Para. Quieto. Ele ouviu algo. Você ouviu também — depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra uma sombra no fim da rua e sussurra 'Guarda!' O que ele quer?",
                    "options": [
                        {"id": "a", "text": "Que eu olhe — ele viu algo"},
                        {"id": "b", "text": "Que eu corra"},
                        {"id": "c", "text": "Que eu coma"},
                        {"id": "d", "text": "Que eu durma"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Guarda. Você olhou. A sombra era só uma criança com uma vela.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Um cachorro latiu do nada perto de vocês — ruído alto. Antonio grita: 'Corri!' Você:",
                    "options": [
                        {"id": "a", "text": "Corro — instinto antes de pensar"},
                        {"id": "b", "text": "Fico quieto com medo"},
                        {"id": "c", "text": "Cumprimento o cachorro"},
                        {"id": "d", "text": "Pergunto o que é 'corri'"},
                    ],
                    "correct": "a",
                    "word_id": "it_correre", "target": "correre", "native": "correre",
                    "npc_reaction": "Corriu. Bom. O corpo aprendeu antes da cabeça.",
                },
            ],
        },
    },

    # ── Seção 4: Pr?tica Aplicada ─────────────────────────────────────────────
    # Antonio treina o protagonista em situações de urgência:
    # reação a comandos, uso de paura/fuoco/correre em frases.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Antonio te ensinou os três comandos que você vai ouvir quando "
                    "as coisas ficarem feias: Corri!, Fermo!, Guarda!. E você aprendeu "
                    "fuoco, paura, correre esta tarde — sem querer.\n\n"
                    "'Agora vou ver se ficou.' Ele ainda est? muito sério."
                ),
                "now": "Pr?tica r?pida — situações urgentes, respostas r?pidas.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Scena 1: C'e fuoco in una casa. Che fai?",
                    "translation": "Cena 1: Tem fogo numa casa. O que você faz?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Fumaça saindo pela janela de uma casa. Chamas visíveis. O que você faz?",
                    "options": [
                        {"id": "a", "text": "Corro! Busco ayuda."},
                        {"id": "b", "text": "Me quedo — c'e molto fuoco"},
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
                    "question": "Você est? corrindo de uma ameaça. Seu coração dispara, suas mãos tremem. O que você sente?",
                    "options": [
                        {"id": "a", "text": "Ho paura"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Estoy bene"},
                        {"id": "d", "text": "C'e mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Normale. Mas o corpo corri mesmo com paura — lembra disso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Scena 2: Qualcuno grida 'Fermo!' detr?s de ti. Che fai?",
                    "translation": "Cena 2: Alguém grita 'Fermo!' atr?s de você. O que faz?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "'PARA!' — grito atr?s de você. O que você faz?",
                    "options": [
                        {"id": "a", "text": "Paro. Imediatamente."},
                        {"id": "b", "text": "Corro mais r?pido"},
                        {"id": "c", "text": "Pergunto quem est? gritando"},
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
                    "line": "El fuoco — molto o poco?",
                    "translation": "O fogo — muito ou pouco?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "A fogueira dos oleiros é enorme — chamas de dois metros, calor sentido de longe. O fuoco é:",
                    "options": [
                        {"id": "a", "text": "Molto fuoco"},
                        {"id": "b", "text": "Poco fuoco"},
                        {"id": "c", "text": "Una mela"},
                        {"id": "d", "text": "Tre fuocos"},
                    ],
                    "correct": "a",
                    "word_id": "it_molto", "target": "molto", "native": "muito",
                    "npc_reaction": "Molto fuoco. Longe é bonito. Perto — perigo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Você est? com medo de alguma coisa mas não sabe nomear bem. Antonio olha: 'Stai bene?' Você responde honestamente:",
                    "options": [
                        {"id": "a", "text": "No... ho paura"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "C'e fuoco"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Eu também. Isso significa que estamos prestando atenção.",
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

    # ── Seção 5: Reforço ───────────────────────────────────────────────────────
    # Noite. Locanda. Antonio est? mais sério que nunca. Ele faz o protagonista
    # revisar tudo — as palavras do começo e as novas de hoje. A narrativa é mais
    # pesada. Você percebe que ele est? te preparando pra algo.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Vocês voltaram pra locanda com o sol se pondo. Antonio trancou "
                    "a porta da locanda por dentro — algo que não fazia antes.\n\n"
                    "Sentaram na mesa de madeira com uma vela no meio. Ele te olhou "
                    "direto. 'O homem que Bianca me contou — eu vi ele hoje. Ele "
                    "sabe onde você dorme.'"
                ),
                "now": "Antonio faz uma revisão final — como se fosse a última antes de algo acontecer.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "A vela tremeu com um vento de baixo da porta. Antonio não se mexeu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Ultimo ripasso prima di dormire. Devo sapere che lo sai.",
                    "translation": "Última revisão antes de dormir. Preciso saber que você tem isso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra você: 'Se qualcuno chiede chi sei, dici...'",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [nome]. Soy el straniero de Nico."},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Non c'e nadie"},
                        {"id": "d", "text": "C'e fuoco"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "De Nico. Corrito. Isso muda como tratam você.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio aponta pra própria cabeça. 'Si alguien grita Corri! — sin pensar, tú...'",
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
                    "question": "A vela apagou. Escuro total. Coração disparou. O que você sente?",
                    "options": [
                        {"id": "a", "text": "Paura"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Alegría"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Normale. Mas a vela acendeu de novo — estava só com vento.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Bene. Duerme. Si c'e algún problema — grito tu nombre.",
                    "translation": "Bem. Dorme. Se houver qualquer problema — grito seu nome.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio disse 'si c'e algún problema'. 'C'e algún problema ora?' — como você responde honestamente?",
                    "options": [
                        {"id": "a", "text": "No sé... c'e algo raro nel borgo"},
                        {"id": "b", "text": "Non c'e nada, estoy bene"},
                        {"id": "c", "text": "C'e muchas mele"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "npc_reaction": "C'e algo raro. Sí. Você est? sentindo certo. Fica alerta.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio apagou a vela principal, ficou só com uma "
                        "pequena na janela. Você deitou sem conseguir dormir, "
                        "ouvindo o vento e os passos l? fora."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obst?culo — La Primera Chispa ───────────────────────────────
    # Madrugada. O protagonista ouviu um barulho e saiu pro corridor da locanda.
    # La Guardia est? l?. Nico est? dormindo e não vai ouvir.
    #
    # SISTEMA DE PODER — LA PALABRA VIVA:
    # Cada exercício certo = entendeu a palavra de verdade = poder manifesto.
    # "Fuoco" acertado sob pressão extrema → a palavra se torna física.
    # O protagonista NÃO controla. NÃO quis. Aconteceu.
    # La Guardia recua. Nico aparece. Olha pras mãos do protagonista.
    #
    # Seção gated — errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio"],
                "story": (
                    "Madrugada. Você acordou com um som — madeira rangendo no "
                    "corridor. Pensou que era vento. Mas o som voltou. Você se "
                    "levantou devagar, empurrou a porta do quarto."
                ),
                "now": "Você est? no corridor escuro da locanda. La Guardia est? ali.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌑 Corridor da locanda. Só uma fresta de luar pela janela. Uma silhueta parada no fim do corridor.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "Te encontré, straniero.",
                    "translation": "Te encontrei, straniero.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Suas pernas queriam correre. Mas você estava de costas pra porta do quarto de Nico.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "La Guardia",
                    "question": "O homem avançou dois passos. Seu estômago afundou. O que você sente?",
                    "options": [
                        {"id": "a", "text": "Paura — muito paura"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Bene, grazie"},
                        {"id": "d", "text": "C'e mele"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": (
                        "Paura. A palavra é real — você a sentiu inteira, do estômago "
                        "às pontas dos dedos. E de algum jeito, sentir a palavra de "
                        "verdade mudou algo no ar."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "??? La Guardia parou. Olhou pras suas mãos. Você também olhou. Nada de diferente. Mas ele hesitou.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "La Guardia",
                    "line": "Che cosa sei tu, straniero?",
                    "translation": "O que você é, straniero?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você não tinha resposta. Mas uma palavra surgiu — não "
                        "com a cabeça. Com o peito. Com o calor que você sentiu "
                        "olhando pra fogueira dos oleiros mais cedo."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "La Guardia",
                    "question": (
                        "La Guardia avança. Você precisa de algo — proteção, luz, calor, "
                        "barreira. Uma palavra pulsa no peito. Qual é ela?"
                    ),
                    "options": [
                        {"id": "a", "text": "🔥 Fuoco"},
                        {"id": "b", "text": "💧 Acqua"},
                        {"id": "c", "text": "🪨 Pietra"},
                        {"id": "d", "text": "?? Mela"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": (
                        "FUOCO — a palavra saiu antes de você pensar.\n\n"
                        "E o corridor explodiu em luz.\n\n"
                        "Não uma fogueira. Não uma faísca. Uma parede de fogo "
                        "entre você e o vigilante — alta, quente, real. Saída das "
                        "suas mãos abertas.\n\n"
                        "La Guardia caiu pra tr?s gritando. Você olhou pras "
                        "próprias mãos — pele intacta, sem queimadura. Como se "
                        "o fogo não fosse seu pra queimar."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "🔥 O fogo durou três segundos. Depois sumiu. O corridor estava escuro de novo. La Guardia tinha ido embora.",
                },
                {
                    "kind": "player",
                    "text": "Você ficou parado olhando pras mãos. Tremendo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Che cos era?! Straniero! Stai bene?",
                    "translation": "O que foi isso?! Forasteiro! Você est? bem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio abriu a porta gritando. Viu o corridor vazio e você parado tremendo. 'Stai bene?'",
                    "options": [
                        {"id": "a", "text": "Non lo so... fuoco. E uscito dalle mie mani."},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Buonanotte"},
                    ],
                    "correct": "a",
                    "word_id": "it_fuoco", "target": "fuoco", "native": "fogo",
                    "npc_reaction": (
                        "Antonio ficou em silêncio. Olhou pras suas mãos. "
                        "Olhou pro corridor. Olhou de volta pra você.\n\n"
                        "Não era a expressão de quem duvidava. Era a expressão "
                        "de quem j? sabia que algo assim ia acontecer."
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
                        "Você entrou no quarto de Antonio. Ele trancou a porta "
                        "e ficou de costas pra você por um longo momento.\n\n"
                        "Quando virou, o rosto era diferente. Não mais o contadino "
                        "paciente que te ensinava saudações. Era alguém que guardava "
                        "segredo faz muito tempo e acabou de decidir parar."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
