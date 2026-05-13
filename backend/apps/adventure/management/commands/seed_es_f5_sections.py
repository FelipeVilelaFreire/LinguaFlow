"""
Seed das 6 seções da Fase 5 Espanhol A1 — "La Primera Chispa".

Algo está errado no pueblo. El Vigilante Oscuro — o homem do chapéu baixo
visto em F2 e F4 — age mais abertamente. Don Miguel começa a preparar o
protagonista. E na S6, sozinho numa rua escura, o protagonista usa uma
palavra pela primeira vez de verdade — fuego — e ela se torna física.

Esta é a primeira aparição de La Palabra Viva. Não é heróica. É acidental,
aterrorizante, e muda tudo.

REGRA DO SISTEMA DE PODER:
Acertar a palavra ≠ matar o inimigo.
Acertar a palavra = entendeu de verdade = a palavra se torna real = poder manifesto.
DEPOIS, com o poder em mãos, o protagonista pode agir.
Nunca: "você acertou, portanto venceu." Sempre: "você acertou → poder ganho → você escolhe."

Novos vocab (3): miedo · fuego · correr
Revisão F1–F4: hola, buenos días, gracias, bien/mal, me llamo, forastero,
               hay/no hay, pan, agua, árbol, piedra, naranja, tres, mucho/poco
NPC principal:   Don Miguel (fio condutor — mais sério a partir daqui)
NPC antagonista: El Vigilante Oscuro (agente — confronto na S6)
Arco emocional:  seguro → ameaçado → poder acidental → assustado com si mesmo
Transição:       Miguel olha pro protagonista de um jeito diferente. A fase seguinte
                 começa com uma conversa séria.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f5_sections [--reset]
"""
from django.core.management.base import BaseCommand, CommandError

from apps.adventure.models import AdventureChapter, AdventurePhase, PhaseSection
from apps.adventure.management.commands.seed_voice import hydrate_section_content


SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Tarde fechada. Miguel mais quieto que o normal. Leva o protagonista por
    # uma rota diferente — ruas menos movimentadas. Mostra algo no caminho:
    # uma fogueira de oleiros, crianças correndo com medo de cachorro.
    # Vocab (miedo/fuego/correr) aparece sem tradução — imersão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌆 Tarde fechada em San Cristóbal. Nuvens pesadas, sem sol. "
                        "Don Miguel chegou na posada mais cedo que o normal e te chamou "
                        "sem explicação — 'Vem.' Uma rota diferente pelo pueblo."
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
                    "text": "Você seguiu sem perguntar. O tom dele era diferente — não amigável, não preocupado. Alerta.",
                },
                {
                    "kind": "scene",
                    "text": "🔥 Num beco lateral, um grupo de oleiros mantém uma fogueira grande — fumaça escura subindo pelo beco.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Fuego. Lo controlan — por ahora. Pero el fuego no avisa.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Fuego. A chama era enorme, quente, barulhenta. Você ficou parado olhando.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¿Qué sientes cuando lo miras?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você não tinha a palavra ainda. Mas o cheiro, o calor, o som — algo no fogo te puxava.",
                },
                {
                    "kind": "scene",
                    "text": "🏃 Três crianças dobram a esquina gritando — um cachorro latindo atrás. Elas correm, rindo de susto.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¡Corren! El perro solo ladra — no muerde. Pero el miedo hace correr igual.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Corren. Miedo. Duas palavras novas num segundo. O cachorro passou pelo lado de vocês sem parar.",
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
                        {"id": "d", "text": "Árbol"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": "Fuego. Quente. Não avisa — só aparece.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "As crianças viram o cachorro e saíram disparadas — pernas rápidas, gritos. O que elas fizeram?",
                    "options": [
                        {"id": "a", "text": "Corrieron — elas correram"},
                        {"id": "b", "text": "Comieron — elas comeram"},
                        {"id": "c", "text": "Cantaron — elas cantaram"},
                        {"id": "d", "text": "Durmieron — elas dormiram"},
                    ],
                    "correct": "a",
                    "word_id": "es_correr", "target": "correr", "native": "correr",
                    "npc_reaction": "Corrieron. O cachorro faz isso com todo mundo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse que o miedo faz as crianças correr mesmo sem perigo real. O que é 'miedo'?",
                    "options": [
                        {"id": "a", "text": "Medo"},
                        {"id": "b", "text": "Alegria"},
                        {"id": "c", "text": "Fome"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Todo mundo tem. O que importa é o que você faz com ele.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel para, olha ao redor, e diz 'No me gusta el pueblo hoy'. Como você está se sentindo?",
                    "options": [
                        {"id": "a", "text": "Un poco de miedo"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Hay naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Bom — o miedo avisa. Escuta ele.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Don Miguel leva o protagonista por um caminho mais seguro — perto da
    # iglesia. Revisão F1–F4 com contexto de tensão crescente.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Vocês saíram do beco das fogueiras. Don Miguel caminha perto, "
                    "mais de perto que de costume. Você aprendeu 'fuego', 'correr' "
                    "e 'miedo' pela observação — sem lição.\n\n"
                    "As outras palavras estão lá: hola, buenos días, gracias, bien, "
                    "tengo hambre, tengo sed, hay, árbol, piedra, naranja, tres, "
                    "mucho, poco. Don Miguel continua te testando — mesmo com esse humor."
                ),
                "now": "Revisão das fases anteriores num contexto mais tenso.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel para na sombra da iglesia. Olha a praça vazia. Uma vela dentro pela janela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Enquanto caminhamos — vamos revisar. O que você aprendeu que pode ajudar agora?",
                    "translation": "Enquanto caminhamos — vamos revisar. O que você aprendeu que pode ajudar agora?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um homem desconhecido para na outra ponta da rua e olha pra vocês. Como você cumprimenta — é de tarde:",
                    "options": [
                        {"id": "a", "text": "¡Buenas tardes!"},
                        {"id": "b", "text": "¡Buenos días!"},
                        {"id": "c", "text": "¡Buenas noches!"},
                        {"id": "d", "text": "¡Hola noche!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_tardes", "target": "buenas tardes", "native": "boa tarde",
                    "npc_reaction": "Buenas tardes. O homem não respondeu. Seguiu em frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Y si alguien nuevo llega al pueblo y pregunta tu nombre?",
                    "translation": "E se alguém novo chegar ao pueblo e perguntar seu nome?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um forasteiro novo para perto de vocês: '¿Cómo te llamas?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Hay fuego"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Me llamo. Sempre diga seu nome — não esconde.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Qué había ayer en el campo — cerca del río?",
                    "translation": "O que havia ontem no campo — perto do río?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "No campo ontem havia árvores, pedras e o río. Don Miguel: '¿Hay árboles cerca del río?'",
                    "options": [
                        {"id": "a", "text": "Sí, hay árboles y piedras"},
                        {"id": "b", "text": "No hay nada"},
                        {"id": "c", "text": "Hay fuego"},
                        {"id": "d", "text": "Hay naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_arbol", "target": "árbol", "native": "árvore",
                    "npc_reaction": "Hay árboles. E piedras. E o velho Ernesto.",
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
                    "npc_reaction": "Una. Só uma. Guarda pro caminho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Y cómo estás — con todo esto?",
                    "translation": "E como você está — com tudo isso?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O pueblo está estranho, Miguel está tenso, há um homem que te observa há dias. Como você está?",
                    "options": [
                        {"id": "a", "text": "Tengo un poco de miedo"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Hay mucho"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Normal. Eu também. Mas fica perto de mim.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra fogueira dos oleiros ao longe. '¿Qué hay allá?' Você vê a chama:",
                    "options": [
                        {"id": "a", "text": "Hay fuego"},
                        {"id": "b", "text": "Hay agua"},
                        {"id": "c", "text": "Hay naranjas"},
                        {"id": "d", "text": "Hay pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": "Fuego. Distante — tudo bem. Longe do pueblo — melhor.",
                },
            ],
        },
    },

    # ── Seção 3: Gramática Narrativa ───────────────────────────────────────────
    # Don Miguel para em frente à iglesia e ensina o imperativo básico:
    # ¡Corre! / ¡Para! / ¡Mira! — verbos de ação urgente.
    # Ele diz que o protagonista pode precisar entender ordens gritadas.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel parou na frente da iglesia. Olhou pra você com "
                    "aquela seriedade nova. 'Tem coisa que você precisa entender "
                    "quando alguém grita. Não é vocabulário — é sobrevivência.'"
                ),
                "now": "Don Miguel ensina comandos urgentes: ¡Corre! ¡Para! ¡Mira!",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Don Miguel chegou perto e falou baixo. 'Aqui no campo, quando as coisas ficam feias, as pessoas gritam.'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Si alguien grita '¡Corre!' — corres. No preguntas. Corres.",
                    "translation": "Se alguém gritar '¡Corre!' — você corre. Não pergunta. Corre.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "¡Corre!",
                    "meaning": "Corre! (imperativo — ordem imediata)",
                    "note": "correr = correr | ¡Corre! = ordem pra você correr agora",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y si gritan '¡Para!' — paras. Quieto. Sin moverse.",
                    "translation": "E se gritarem '¡Para!' — você para. Quieto. Sem se mover.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "¡Para!",
                    "meaning": "Para! (imperativo — ordem pra parar imediatamente)",
                    "note": "Oposto de ¡Corre! — um te move, o outro te imobiliza",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y '¡Mira!' — alguien quiere que veas algo. Importante. Miras.",
                    "translation": "E '¡Mira!' — alguém quer que você veja algo. Importante. Você olha.",
                    "pace": "urgent",
                },
                {
                    "kind": "reveal",
                    "phrase": "¡Mira!",
                    "meaning": "Olha! / Vê isso! (imperativo — ordem pra prestar atenção)",
                    "note": "mirar = olhar | ¡Mira! = olha agora",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "¡Corre!",  "isKey": True},
                        {"text": " · ",      "isKey": False},
                        {"text": "¡Para!",   "isKey": True},
                        {"text": " · ",      "isKey": False},
                        {"text": "¡Mira!",   "isKey": True},
                    ],
                    "example": "¡Miguel grita: ¡Corre! — corres. Grita ¡Para! — paras.",
                    "translation": "Miguel grita: ¡Corre! — você corre. Grita ¡Para! — você para.",
                    "note": "Não traduz — só age. O corpo entende antes da cabeça.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel grita repentinamente: '¡Corre!' O que você faz?",
                    "options": [
                        {"id": "a", "text": "Corro — sem perguntar"},
                        {"id": "b", "text": "Fico parado esperando"},
                        {"id": "c", "text": "Pergunto o que aconteceu"},
                        {"id": "d", "text": "Falo 'buenos días'"},
                    ],
                    "correct": "a",
                    "word_id": "es_correr", "target": "correr", "native": "correr",
                    "npc_reaction": "Corro. Sem perguntar. Isso salva vidas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel sussurra '¡Para!' no meio do caminho. Você:",
                    "options": [
                        {"id": "a", "text": "Paro. Quieto. Escuto."},
                        {"id": "b", "text": "Continuo caminhando"},
                        {"id": "c", "text": "Começo a correr"},
                        {"id": "d", "text": "Pergunto '¿cómo estás?'"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Para. Quieto. Ele ouviu algo. Você ouviu também — depois.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra uma sombra no fim da rua e sussurra '¡Mira!' O que ele quer?",
                    "options": [
                        {"id": "a", "text": "Que eu olhe — ele viu algo"},
                        {"id": "b", "text": "Que eu corra"},
                        {"id": "c", "text": "Que eu coma"},
                        {"id": "d", "text": "Que eu durma"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Mira. Você olhou. A sombra era só uma criança com uma vela.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Um cachorro latiu do nada perto de vocês — ruído alto. Don Miguel grita: '¡Corre!' Você:",
                    "options": [
                        {"id": "a", "text": "Corro — instinto antes de pensar"},
                        {"id": "b", "text": "Fico quieto com medo"},
                        {"id": "c", "text": "Cumprimento o cachorro"},
                        {"id": "d", "text": "Pergunto o que é 'corre'"},
                    ],
                    "correct": "a",
                    "word_id": "es_correr", "target": "correr", "native": "correr",
                    "npc_reaction": "Correu. Bom. O corpo aprendeu antes da cabeça.",
                },
            ],
        },
    },

    # ── Seção 4: Prática Aplicada ─────────────────────────────────────────────
    # Don Miguel treina o protagonista em situações de urgência:
    # reação a comandos, uso de miedo/fuego/correr em frases.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel te ensinou os três comandos que você vai ouvir quando "
                    "as coisas ficarem feias: ¡Corre!, ¡Para!, ¡Mira!. E você aprendeu "
                    "fuego, miedo, correr esta tarde — sem querer.\n\n"
                    "'Agora vou ver se ficou.' Ele ainda está muito sério."
                ),
                "now": "Prática rápida — situações urgentes, respostas rápidas.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Escena 1: Hay fuego en una casa. ¿Qué haces?",
                    "translation": "Cena 1: Tem fogo numa casa. O que você faz?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Fumaça saindo pela janela de uma casa. Chamas visíveis. O que você faz?",
                    "options": [
                        {"id": "a", "text": "¡Corro! Busco ayuda."},
                        {"id": "b", "text": "Me quedo — hay mucho fuego"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_correr", "target": "correr", "native": "correr",
                    "npc_reaction": "¡Corro! Correto. Fogo = corre, grita, busca ajuda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você está correndo de uma ameaça. Seu coração dispara, suas mãos tremem. O que você sente?",
                    "options": [
                        {"id": "a", "text": "Tengo miedo"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Hay naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Normal. Mas o corpo corre mesmo com miedo — lembra disso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Escena 2: Alguien grita '¡Para!' detrás de ti. ¿Qué haces?",
                    "translation": "Cena 2: Alguém grita '¡Para!' atrás de você. O que faz?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'¡PARA!' — grito atrás de você. O que você faz?",
                    "options": [
                        {"id": "a", "text": "Paro. Imediatamente."},
                        {"id": "b", "text": "Corro mais rápido"},
                        {"id": "c", "text": "Pergunto quem está gritando"},
                        {"id": "d", "text": "Falo 'buenos días'"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Para. Antes de pensar. Isso.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra uma fogueira dos oleiros ainda ativa: '¿Qué hay allá?'",
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
                    "line": "El fuego — ¿mucho o poco?",
                    "translation": "O fogo — muito ou pouco?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "A fogueira dos oleiros é enorme — chamas de dois metros, calor sentido de longe. O fuego é:",
                    "options": [
                        {"id": "a", "text": "Mucho fuego"},
                        {"id": "b", "text": "Poco fuego"},
                        {"id": "c", "text": "Una naranja"},
                        {"id": "d", "text": "Tres fuegos"},
                    ],
                    "correct": "a",
                    "word_id": "es_mucho", "target": "mucho", "native": "muito",
                    "npc_reaction": "Mucho fuego. Longe é bonito. Perto — perigo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você está com medo de alguma coisa mas não sabe nomear bem. Don Miguel olha: '¿Estás bien?' Você responde honestamente:",
                    "options": [
                        {"id": "a", "text": "No... tengo miedo"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Hay fuego"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Eu também. Isso significa que estamos prestando atenção.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Bien hecho. Ahora vamos a la posada. Quédate cerca.",
                    "translation": "Bem feito. Agora vamos pra posada. Fica perto de mim.",
                    "pace": "slow",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ───────────────────────────────────────────────────────
    # Noite. Posada. Don Miguel está mais sério que nunca. Ele faz o protagonista
    # revisar tudo — as palavras do começo e as novas de hoje. A narrativa é mais
    # pesada. Você percebe que ele está te preparando pra algo.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Vocês voltaram pra posada com o sol se pondo. Don Miguel trancou "
                    "a porta da posada por dentro — algo que não fazia antes.\n\n"
                    "Sentaram na mesa de madeira com uma vela no meio. Ele te olhou "
                    "direto. 'O homem que Carmen me contou — eu vi ele hoje. Ele "
                    "sabe onde você dorme.'"
                ),
                "now": "Don Miguel faz uma revisão final — como se fosse a última antes de algo acontecer.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "A vela tremeu com um vento de baixo da porta. Don Miguel não se mexeu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Último repaso antes de dormir. Necesito saber que lo tienes.",
                    "translation": "Última revisão antes de dormir. Preciso saber que você tem isso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra você: 'Si alguien pregunta quién eres — dices...'",
                    "options": [
                        {"id": "a", "text": "Me llamo [nome]. Soy el forastero de Miguel."},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "No hay nadie"},
                        {"id": "d", "text": "Hay fuego"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "De Miguel. Correto. Isso muda como tratam você.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra própria cabeça. 'Si alguien grita ¡Corre! — sin pensar, tú...'",
                    "options": [
                        {"id": "a", "text": "Corro"},
                        {"id": "b", "text": "Fico parado"},
                        {"id": "c", "text": "Pergunto o que aconteceu"},
                        {"id": "d", "text": "Digo 'buenos días'"},
                    ],
                    "correct": "a",
                    "word_id": "es_correr", "target": "correr", "native": "correr",
                    "npc_reaction": "Corro. Antes de pensar. Sempre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "A vela apagou. Escuro total. Coração disparou. O que você sente?",
                    "options": [
                        {"id": "a", "text": "Miedo"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Alegría"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": "Miedo. Normal. Mas a vela acendeu de novo — estava só com vento.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Bien. Duerme. Si hay algún problema — grito tu nombre.",
                    "translation": "Bem. Dorme. Se houver qualquer problema — grito seu nome.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'si hay algún problema'. '¿Hay algún problema ahora?' — como você responde honestamente?",
                    "options": [
                        {"id": "a", "text": "No sé... hay algo raro en el pueblo"},
                        {"id": "b", "text": "No hay nada, estoy bien"},
                        {"id": "c", "text": "Hay muchas naranjas"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Hay algo raro. Sí. Você está sentindo certo. Fica alerta.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel apagou a vela principal, ficou só com uma "
                        "pequena na janela. Você deitou sem conseguir dormir, "
                        "ouvindo o vento e os passos lá fora."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo — La Primera Chispa ───────────────────────────────
    # Madrugada. O protagonista ouviu um barulho e saiu pro corredor da posada.
    # El Vigilante Oscuro está lá. Miguel está dormindo e não vai ouvir.
    #
    # SISTEMA DE PODER — LA PALABRA VIVA:
    # Cada exercício certo = entendeu a palavra de verdade = poder manifesto.
    # "Fuego" acertado sob pressão extrema → a palavra se torna física.
    # O protagonista NÃO controla. NÃO quis. Aconteceu.
    # El Vigilante recua. Miguel aparece. Olha pras mãos do protagonista.
    #
    # Seção gated — errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Madrugada. Você acordou com um som — madeira rangendo no "
                    "corredor. Pensou que era vento. Mas o som voltou. Você se "
                    "levantou devagar, empurrou a porta do quarto."
                ),
                "now": "Você está no corredor escuro da posada. El Vigilante Oscuro está ali.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌑 Corredor da posada. Só uma fresta de luar pela janela. Uma silhueta parada no fim do corredor.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Te encontré, forastero.",
                    "translation": "Te encontrei, forasteiro.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Suas pernas queriam correr. Mas você estava de costas pra porta do quarto de Miguel.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": "O homem avançou dois passos. Seu estômago afundou. O que você sente?",
                    "options": [
                        {"id": "a", "text": "Miedo — muito miedo"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Hay naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "miedo", "native": "medo",
                    "npc_reaction": (
                        "Miedo. A palavra é real — você a sentiu inteira, do estômago "
                        "às pontas dos dedos. E de algum jeito, sentir a palavra de "
                        "verdade mudou algo no ar."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "🗡️ El Vigilante parou. Olhou pras suas mãos. Você também olhou. Nada de diferente. Mas ele hesitou.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "¿Qué eres tú, forastero?",
                    "translation": "O que você é, forasteiro?",
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
                    "npc": "El Vigilante",
                    "question": (
                        "El Vigilante avança. Você precisa de algo — proteção, luz, calor, "
                        "barreira. Uma palavra pulsa no peito. Qual é ela?"
                    ),
                    "options": [
                        {"id": "a", "text": "🔥 Fuego"},
                        {"id": "b", "text": "💧 Agua"},
                        {"id": "c", "text": "🪨 Piedra"},
                        {"id": "d", "text": "🍊 Naranja"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": (
                        "FUEGO — a palavra saiu antes de você pensar.\n\n"
                        "E o corredor explodiu em luz.\n\n"
                        "Não uma fogueira. Não uma faísca. Uma parede de fogo "
                        "entre você e o vigilante — alta, quente, real. Saída das "
                        "suas mãos abertas.\n\n"
                        "El Vigilante caiu pra trás gritando. Você olhou pras "
                        "próprias mãos — pele intacta, sem queimadura. Como se "
                        "o fogo não fosse seu pra queimar."
                    ),
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "🔥 O fogo durou três segundos. Depois sumiu. O corredor estava escuro de novo. El Vigilante tinha ido embora.",
                },
                {
                    "kind": "player",
                    "text": "Você ficou parado olhando pras mãos. Tremendo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¡¿Qué fue eso?! ¡Forastero! ¿Estás bien?",
                    "translation": "O que foi isso?! Forasteiro! Você está bem?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel abriu a porta gritando. Viu o corredor vazio e você parado tremendo. '¿Estás bien?'",
                    "options": [
                        {"id": "a", "text": "No sé... fuego. Salió de mis manos."},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_fuego", "target": "fuego", "native": "fogo",
                    "npc_reaction": (
                        "Don Miguel ficou em silêncio. Olhou pras suas mãos. "
                        "Olhou pro corredor. Olhou de volta pra você.\n\n"
                        "Não era a expressão de quem duvidava. Era a expressão "
                        "de quem já sabia que algo assim ia acontecer."
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
                        "Você entrou no quarto de Don Miguel. Ele trancou a porta "
                        "e ficou de costas pra você por um longo momento.\n\n"
                        "Quando virou, o rosto era diferente. Não mais o campesino "
                        "paciente que te ensinava saudações. Era alguém que guardava "
                        "segredo faz muito tempo e acabou de decidir parar."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────

class Command(BaseCommand):
    help = "Seed das 6 seções da Fase 5 Espanhol A1 — La Primera Chispa"

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Apaga e recria as seções (default: pula se já existem)",
        )

    def handle(self, *args, **options):
        self.stdout.write("\n📦 Seeding seções — ES A1 T1 Fase 5\n")

        try:
            chapter = AdventureChapter.objects.get(slug="es-a1-t1")
        except AdventureChapter.DoesNotExist:
            raise CommandError(
                "Chapter 'es-a1-t1' não encontrado. Rode 'seed_es_full' primeiro."
            )

        try:
            phase = AdventurePhase.objects.get(chapter=chapter, number=5)
        except AdventurePhase.DoesNotExist:
            raise CommandError(
                "Fase 5 do chapter 'es-a1-t1' não encontrada. Rode 'seed_es_full' primeiro."
            )

        existing = PhaseSection.objects.filter(phase=phase).count()
        if existing and not options["reset"]:
            self.stdout.write(
                self.style.WARNING(
                    f"  Fase 5 já tem {existing} seções. Use --reset para recriar."
                )
            )
            return

        if options["reset"]:
            deleted, _ = PhaseSection.objects.filter(phase=phase).delete()
            self.stdout.write(f"  ↻ {deleted} seções apagadas")

        created_count = 0
        for sec in SECTIONS:
            PhaseSection.objects.create(
                phase=phase,
                section_number=sec["section_number"],
                section_type=sec["section_type"],
                content=hydrate_section_content(sec["content"]),
            )
            self.stdout.write(
                f"  ✓ Seção {sec['section_number']}: {sec['section_type']}"
            )
            created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"\n✅ {created_count} seções criadas para Fase 5 · ES A1 T1\n"
            "   Endpoint: GET /api/adventure/phases/{phase_id}/sections/\n"
            "   ⚡ Esta fase contém La Primera Chispa — primeira manifestação\n"
            "      de La Palabra Viva. Ver seção 6 para o sistema de poder.\n"
        ))
