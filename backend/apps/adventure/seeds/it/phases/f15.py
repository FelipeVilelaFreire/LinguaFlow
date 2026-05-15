"""
Seed das 6 seções da Fase 15 Italiano A1 — "El primer testigo".

Manhã do quarto dia. Vocês quatro + Antonio il Contadino + 3 testigos (Giulia, Bianca,
Pietro) chegam ao municipio. Bianca testemunha primeiro. O Podesta
recebe Bianca mais frio do que vocês esperavam.

NOVA TENSÃO REVELADA NO FIM:
    Saindo, Bianca sussurra pra Lucia: 'Ese hombre y yo — tenemos
    historia.' Não conta agora o que é. Plantado pra próxipiu fases.

ABORDAGEM PEDAGÓGICA:
    Apresenta parole pra descrever pessoas — alto, bajo, giovane, viejo.
    O aluno aprende que essas palavras MUDAM dependendo de quem é
    descrito (homem ou mulher). SEM nomear "adjetivo" ou "concordância".
    Apenas mostrar: "Chiara es alta" / "Nico es alto".

Vocab novo (3): alto · bajo · giovane
Apresentação adicional: viejo · delgado (em vocab_list)

Revisão F1-F14 dominante:
  · vi/hablé/oí (F12) — Bianca relata
  · mi/tu/su (F13) — possessivos
  · el/la/los/las (F14) — gênero
  · vado a / andiamo a (F11) — futuro próximo
  · sono/sto/ho (F8)

NPC principais: Bianca · Il Podesta · La Guardia (fundo) · os 4
Arco emocional: tensão prima → testemunho corajoso → Podesta frio →
                pase provisional + pista da Bianca
Transição:      F16 abre com Bianca contando ao grupo qual é a 'historia'
                dela com o Podesta.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Chegada ao municipio. Apresentação dos adjetivos descritivos — Bianca
    # descreve o forestiero usando palavras simples (alto, giovane). 3 exer novos
    # + 1 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌄 Manhã do quarto dia · Ayuntamiento · Porta de ferro\n\n"
                        "Vocês são oito. Antonio il Contadino à fronte. Bianca — a primeira "
                        "testigo — vestida com a melhor blusa, cabelo penteado, "
                        "andando devagar piu decidida. Giulia e Pietro atrás. Os "
                        "4 do grupo no final."
                    ),
                },
                {
                    "kind": "skill_check",
                    "skill": "investigacao",
                    "min_level": 2,
                    "uses_item_tag": "documento",
                    "success": "Voce nota uma marca pequena no papel antes que ela desapareca na confusao.",
                    "fallback": "A pista passa quase despercebida, mas a cena ainda deixa caminho para perguntar depois.",
                },
                {
                    "kind": "narrative",
                    "text": "Il Podesta já estava na salea — sentado, esperando. Reconheceu Bianca no instante em que ela entrou.",
                },
                {
                    "kind": "npc",
                    "npc": "Il Podesta",
                    "line": "Doña Bianca. No esperaba verla a usted aquí.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Bianca",
                    "line": "Benes días, señor Podesta. Vine come testigo.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "O Podesta ficou sério. Bianca ficou em pé. Os dois se "
                        "olharam por meio segundo a mais do que precisariam."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Il Podesta",
                    "line": "Como guste. Siéntese. Empezamos por usted.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "alto",    "native": "alto"},
                        {"target": "bajo",    "native": "baixo"},
                        {"target": "giovane",   "native": "jovem"},
                        {"target": "viejo",   "native": "velho"},
                        {"target": "delgado", "native": "magro"},
                    ],
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Doña Bianca — para empezar — describa al forestiero. ¿Cómo es físicamente?",
                    "translation": "Dona Bianca — para começar — descreva o forasteiro. Como ele é fisicamente?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca olha pra você. Você é mais alto que Antonio il Contadino. Como ela descreve sua altura?",
                    "options": [
                        {"id": "a", "text": "Es alto"},
                        {"id": "b", "text": "Es bajo"},
                        {"id": "c", "text": "Es viejo"},
                        {"id": "d", "text": "Es vecino"},
                    ],
                    "correct": "a",
                    "word_id": "it_alto", "target": "alto", "native": "alto",
                    "npc_reaction": "Anotado: alto. Sigamos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Você tem vinte anni. Bianca descreve sua idade:",
                    "options": [
                        {"id": "a", "text": "Es giovane"},
                        {"id": "b", "text": "Es viejo"},
                        {"id": "c", "text": "Es bajo"},
                        {"id": "d", "text": "Es vecino"},
                    ],
                    "correct": "a",
                    "word_id": "it_giovane", "target": "giovane", "native": "jovem",
                    "npc_reaction": "Jovieni. Veinte años — questo ya está en el papel.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Il Podesta: 'Y Antonio il Contadino — el padre.' Antonio il Contadino é mais baixo que você:",
                    "options": [
                        {"id": "a", "text": "Es bajo"},
                        {"id": "b", "text": "Es alto"},
                        {"id": "c", "text": "Es giovane"},
                        {"id": "d", "text": "Es delgado"},
                    ],
                    "correct": "a",
                    "word_id": "it_bajo", "target": "bajo", "native": "baixo",
                    "npc_reaction": "Bajo y trabajador.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Bianca testemunha — relato em passado. O Podesta anota.
    # Mistura F1-F14: pretérito, possessivos, gênero, sono/sto/ho.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Bianca", "Il Podesta"],
                "story": (
                    "Podesta escreveu três linhas. Levantou a pena. Olhou pra "
                    "Bianca — agora calculista, não pessoal.\n\n"
                    "'Continuemos. Cuénteme — desde el primer día. Cómo encontró "
                    "al forestiero. Qué hizo. Qué ha detto.'"
                ),
                "now": "Bianca relata em passado. Você acompaneha — pode ser chamado.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Lo conocí el primer día. Nico — mi vecino — lo llevó hasta mi banco en la piazza.",
                    "translation": "Conheci ele no primeiro dia. Nico — meu vizinho — levou ele até o meu banco na piazza.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'lo conocí'. Pra você confirmar pra ela que tu também lembra do primeiro encontro (já aconteceu, você viu Bianca):",
                    "options": [
                        {"id": "a", "text": "Sí, te vi ese día"},
                        {"id": "b", "text": "Sí, te veo"},
                        {"id": "c", "text": "Vado a verte"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Tu me viste. Yo te vi. Igual.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Hablé con él. Le pregunté su nombre — me lo ha detto claro. Educado.",
                    "translation": "Falei com ele. Perguntei o nome — disse claro. Educado.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'hablé con él'. Significa que ela:",
                    "options": [
                        {"id": "a", "text": "Falou (já aconteceu)"},
                        {"id": "b", "text": "Fala (presente)"},
                        {"id": "c", "text": "Vai falar"},
                        {"id": "d", "text": "Quer falar"},
                    ],
                    "correct": "a",
                    "word_id": "it_hable", "target": "hablé", "native": "falei",
                    "npc_reaction": "Hablé. Yo, ya hecho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "¿Y le pareció peligroso, doña Bianca?",
                    "translation": "E pareceu perigoso pra você, dona Bianca?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "No, señor Podesta. Me pareció perdido — no peligroso.",
                    "translation": "Não, senhor Podesta. Pareceu perdido — não perigoso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Il Podesta se vira pra você: 'Jovieni — ¿cómo te chiami?' Resposta firme:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Ho veinte años"},
                        {"id": "d", "text": "Benes días"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Anotado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "¿Y tu edad?",
                    "translation": "E sua idade?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Resposta exata:",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Sono veinte"},
                        {"id": "c", "text": "Sto veinte"},
                        {"id": "d", "text": "Vado veinte"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Veinte. Mismo que ha detto Doña Bianca.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "¿Cómo estás hoy aquí, después de todo?",
                    "translation": "Como você está hoje aqui, depois de tudo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Estado de agora — com nervosismo piu firme:",
                    "options": [
                        {"id": "a", "text": "Sto bene, grazie"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Vado bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Bene. Anotado.",
                },
                {
                    "kind": "narrative",
                    "text": "Uma porta abre no fundo. La Guardia entra silencioso. Senta no fundo. Não cumprimenta.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Il Podesta: 'Y Lucia — la guaritrice. ¿Te gusta ella?' (você tem que escolher se é HONESTO ou SEGURO). Você prefere a resposta segura:",
                    "options": [
                        {"id": "a", "text": "Sí, me ayudó cuando estuve malato"},
                        {"id": "b", "text": "No, no mi piace"},
                        {"id": "c", "text": "Sono Lucia"},
                        {"id": "d", "text": "Vado a Lucia"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "me ayudó", "native": "me ajudou",
                    "npc_reaction": "Ayudó. Anotado.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Podesta quer ouvir o forestiero direto. Você descreve outras pessoas
    # do grupo — Chiara (mulher), Nico (homem), Lucia (mulher). O aluno
    # ENXERGA que "alto" muda pra "alta" dependendo de quem é. SEM nomear.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Il Podesta", "Bianca"],
                "story": (
                    "Bianca terminou. Foi pro banco do lado, perto de Antonio il Contadino. "
                    "Il Podesta fechou a primeira página do livro de actas. Abriu "
                    "a segunda.\n\n"
                    "'Jovieni forestiero — siéntese aquí. Conteste mis preguntas. "
                    "Senza ayuda.'"
                ),
                "now": "Você descreve as pessoas do grupo. Cada palavra muda dependendo de quem.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🪑 Cadeira de testigo · Você sentado · Podesta com pena no papel",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Describe a Chiara — la giovane que vino con te. ¿Cómo es ella?",
                    "translation": "Descreve Chiara — a jovem que veio con te. Como ela é?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Chiara é alta, da sua altura quase. Jovem. Magra. Pra ela "
                        "(mulher), a palavra 'alto' vira 'alta' — termina come "
                        "ela mesma."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Pra falar da altura de Chiara (mulher):",
                    "options": [
                        {"id": "a", "text": "Es alta"},
                        {"id": "b", "text": "Es alto"},
                        {"id": "c", "text": "Sono alta"},
                        {"id": "d", "text": "Sto alta"},
                    ],
                    "correct": "a",
                    "word_id": "it_alta", "target": "alta", "native": "alta (mulher)",
                    "npc_reaction": "Alta. La palabra termina come ella — en '-a'. Igual que 'la' (de mujer).",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Chiara também é jovem — 18 anni. 'Jovieni' não termina em -a nem -o. Como você usa pra Chiara?",
                    "options": [
                        {"id": "a", "text": "Es giovane"},
                        {"id": "b", "text": "Es jóvienia"},
                        {"id": "c", "text": "Es giovanea"},
                        {"id": "d", "text": "Es alta giovane"},
                    ],
                    "correct": "a",
                    "word_id": "it_giovane", "target": "giovane", "native": "jovem",
                    "npc_reaction": "Jovieni. Esa palabra no cambia con hombre o mujer — sirve igual para los dos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Y Nico — el hijo de Antonio il Contadino. ¿Cómo es él?",
                    "translation": "E Nico — o filho de Antonio il Contadino. Como ele é?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Nico é alto (igual a você). Pra descrever ele (homem):",
                    "options": [
                        {"id": "a", "text": "Es alto"},
                        {"id": "b", "text": "Es alta"},
                        {"id": "c", "text": "Sono alto"},
                        {"id": "d", "text": "Sto alto"},
                    ],
                    "correct": "a",
                    "word_id": "it_alto", "target": "alto", "native": "alto (homem)",
                    "npc_reaction": "Alto. La palabra termina en '-o' — igual que 'el' (de hombre).",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Nico também tem vinte anni — jovem. Pra ele:",
                    "options": [
                        {"id": "a", "text": "Es giovane"},
                        {"id": "b", "text": "Es vejo"},
                        {"id": "c", "text": "Sono giovane"},
                        {"id": "d", "text": "Es giovanea"},
                    ],
                    "correct": "a",
                    "word_id": "it_giovane", "target": "giovane", "native": "jovem",
                    "npc_reaction": "Jovieni. Misma palabra para hombre o mujer.",
                },
                {
                    "kind": "narrative",
                    "text": "Você ouve a porta abrir de novo. La Guardia chegou mais perto — está logo atrás de Antonio il Contadino agora. Bianca aperta a mão de Antonio il Contadino.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Adesso describe a Lucia — la guaritrice.",
                    "translation": "Agora descreve Lucia — a guaritrice.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Il Podesta sabe que Lucia chegou faz dois meses. Você nunca "
                        "disse isso pra ele. Quem disse?Nem Bianca disse. Mas você "
                        "lembra — Lucia entrou no municipio sozinha na F11."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Lucia tem 24 anni. É jovem ainda. Magra. Descrição segura — sem comprometer. Pra ela (mulher), 'magra' fica:",
                    "options": [
                        {"id": "a", "text": "Es delgada"},
                        {"id": "b", "text": "Es delgado"},
                        {"id": "c", "text": "Sono delgada"},
                        {"id": "d", "text": "Sto delgada"},
                    ],
                    "correct": "a",
                    "word_id": "it_delgada", "target": "delgada", "native": "magra (mulher)",
                    "npc_reaction": "Delgada. Esatto me lo confirma usted — ma ya lo sabía.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Antonio il Contadino — pra contraste, mais velho que vocês:",
                    "options": [
                        {"id": "a", "text": "Es viejo"},
                        {"id": "b", "text": "Es vieja"},
                        {"id": "c", "text": "Sono viejo"},
                        {"id": "d", "text": "Sto viejo"},
                    ],
                    "correct": "a",
                    "word_id": "it_viejo", "target": "viejo", "native": "velho",
                    "npc_reaction": "Viejo. Ma todavía con buena testa. Esatto lo confirmo yo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Bianca olha pra Lucia — que está no fundo da salea. Lucia "
                        "acena de leve pra Bianca. Bianca acena de volta. Algo entre "
                        "as duas que você não decifrou ainda."
                    ),
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Pausa nas testemunhas. Il Podesta sai. Bianca aproveita pra explicar
    # devagar — "as palavras de descrever pessoas terminam come elas mespiu".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Bianca", "Chiara"],
                "story": (
                    "Il Podesta se levantou — disse que ia escrever outras "
                    "actas e voltava em dez minutos. La Guardia voltou pro "
                    "fundo.\n\n"
                    "Bianca aproveitou: 'Jovieni — prima que vuelva el Podesta, "
                    "andiamo a aclarar algo importante.'"
                ),
                "now": "Bianca explica come as palavras de descrever mudam.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Notaste — para Chiara hai detto 'alta'. Para Nico hai detto 'alto'. Es la misma palabra — solo cambia el final.",
                    "translation": "Notou — para Chiara você disse 'alta'. Para Nico você disse 'alto'. É a mesma palavra — só muda o final.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Alto (de hombre) · Alta (de mujer)",
                    "meaning": "A palavra de descrever termina igual à pessoa que ela descreve.",
                    "note": "come 'el/la' — termina en -o para hombre, -a para mujer",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "el hombre ", "isKey": False},
                        {"text": "alto",       "isKey": True},
                        {"text": " · la mujer ", "isKey": False},
                        {"text": "alta",       "isKey": True},
                        {"text": " · los hombres ", "isKey": False},
                        {"text": "altos",      "isKey": True},
                        {"text": " · las mujeres ", "isKey": False},
                        {"text": "altas",      "isKey": True},
                    ],
                    "example": "El hombre alto. La mujer alta. Los hombres altos. Las mujeres altas.",
                    "translation": "O homem alto. A mulher alta. Os homens altos. As mulheres altas.",
                    "note": "la palabra de descripción termina igual que la persona — '-o', '-a', '-os', '-as'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Antonio il Contadino e Doña Lucía são dois — um homem e uma mulher. Pra dizer 'baixos' juntos (quando mistura homem e mulher, usa a forma de homem):",
                    "options": [
                        {"id": "a", "text": "Son bajos"},
                        {"id": "b", "text": "Son bajas"},
                        {"id": "c", "text": "Es bajo"},
                        {"id": "d", "text": "Está bajo"},
                    ],
                    "correct": "a",
                    "word_id": "it_bajos", "target": "bajos", "native": "baixos",
                    "npc_reaction": "Bajos. Cuando hay hombre y mujer mezclados, gana la forma de hombre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Ma ojo — algunas parole no terminan en -o ni -a. Como 'giovane'. Esa no cambia.",
                    "translation": "Mas atenção — algupiu palavras não terminam em -o nem -a. Como 'giovane'. Essa não muda.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Jovieni (não muda) · Jóvienies (muitos)",
                    "meaning": "Pra homem ou pra mulher é igual. Só muda se forem muitos.",
                    "note": "lo mismo con 'fácil', 'difícil' — terminan en consonante y no cambian",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Chiara e Sally (que vai aparecer depois) são duas mulheres giovanes. Plural:",
                    "options": [
                        {"id": "a", "text": "Son jóvienies"},
                        {"id": "b", "text": "Son jóvienias"},
                        {"id": "c", "text": "Es giovaneas"},
                        {"id": "d", "text": "Sto jóvienies"},
                    ],
                    "correct": "a",
                    "word_id": "it_giovanees", "target": "jóvienies", "native": "giovanes",
                    "npc_reaction": "Jóvienies. 'Jovieni' no se hace 'jóvienia' — solo suma '-es' al plural.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Bianca — y la palabra de descripción va prima o después?",
                    "translation": "Bianca — e a palavra de descrição vai prima ou depois?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Normalemente DEPOIS — diferente do português às vezes. Como você diz 'a casa grande':",
                    "options": [
                        {"id": "a", "text": "La casa grande"},
                        {"id": "b", "text": "La grande casa"},
                        {"id": "c", "text": "Casa la grande"},
                        {"id": "d", "text": "Grande la casa"},
                    ],
                    "correct": "a",
                    "word_id": "it_ordine", "target": "casa grande", "native": "casa primero",
                    "npc_reaction": "La casa grande. La cosa primero, la descripción después.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Podesta volta. Giulia testifica curto. Pietro idem. Podesta NÃO concede
    # sello completo — pase provisional (1 mês). Negociação tensa.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Il Podesta", "Giulia", "Pietro", "Antonio il Contadino"],
                "story": (
                    "Il Podesta voltou. Giulia subiu na cadeira de testigo — "
                    "depoimento curto. 'Le vienidí pane el primer día. Le di "
                    "gratis el segundo. Es educado.'\n\n"
                    "Pietro subiu depois — ainda mais curto. 'Lo vi en la "
                    "strada. Saludó bene. No vi nada raro.'"
                ),
                "now": "Tudo dito. Podesta decide. Mas não come vocês esperavam.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "⚖️ Sala de actas · Três depoimentos no papel · Podesta lendo em silêncio",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Tres testigos. Doña Bianca — respetada. Doña Giulia — vecina. Don Pietro — trabajador. Aceptables.",
                    "translation": "Três testigos. Dona Bianca — respeitada. Dona Giulia — vizinha. Don Pietro — trabalhador. Aceitáveis.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Ma — los tres lo vieron poco. Una semana, máximo dos. No me dan certeza para sellar.",
                    "translation": "Mas — os três o viram pouco. Uma semana, máximo duas. Não me dão certeza pra carimbar.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você sente o peito apertar. O pquesto do 'no'. Chiara olha pra Antonio il Contadino. Antonio il Contadino não desviou os olhos do Podesta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Pase provisional — válido un mes. Después: o el pase definitivo, o salee del borgo.",
                    "translation": "Pase provisório — vale um mês. Depois: ou o pase definitivo, ou sai do borgo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Não é a vitória total — piu não é a derrota. Você aceita formalemente:",
                    "options": [
                        {"id": "a", "text": "Sí, acepto"},
                        {"id": "b", "text": "No, no acepto"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Sto"},
                    ],
                    "correct": "a",
                    "word_id": "it_acepto", "target": "acepto", "native": "aceito",
                    "npc_reaction": "Aceptado. El sello provisional salee adesso.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Il Podesta derrete cera vermelha sobre o papel. Aperta o "
                        "selo de bronze. Esfria. Entrega o papel pra você.\n\n"
                        "Você segura. Pequeno triunfo. Quente nas mãos."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Il Podesta",
                    "line": "Un mes. Y aviso — el Guardia seguirá observando. No me sorprenda.",
                    "translation": "Um mês. E aviso — La Guardia vai continuar observando. Não me surpreenda.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Il Podesta",
                    "question": "Você agradece — formale, sem exagero:",
                    "options": [
                        {"id": "a", "text": "Grazie, señor Podesta"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Vayan. Benes días.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Bene. Salimos.",
                    "translation": "Bom. Saímos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino: 'Forestiero — ¿cómo te sientes adesso?'",
                    "options": [
                        {"id": "a", "text": "Sto meglio que prima"},
                        {"id": "b", "text": "Sono mejor"},
                        {"id": "c", "text": "Sto meglio"},
                        {"id": "d", "text": "Vado mejor"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_mejor", "target": "sto mejor", "native": "estou melhor",
                    "npc_reaction": "Mejor. Un mes — ma algo es algo.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Saindo do municipio. Bianca sussurra pra Lucia sobre o Podesta.
    # Gate: errar trava. Closenzag prepara F16.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Bianca", "Lucia", "Chiara"],
                "story": (
                    "Vocês saem do municipio. Pase provisório no bolso. "
                    "Antonio il Contadino à fronte. Bianca anda devagar — está ao "
                    "lado de Lucia. Você está atrás dos dois. Vai ouvir o "
                    "que ela vai dizer."
                ),
                "now": "Cena rápida na escada. Você precisa reagir certo a cada momento.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🪨 Escada do municipio · Saindo · Bianca e Lucia lado a lado",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Lucia — ese hombre y yo. Tenemos historia.",
                    "translation": "Lucia — esse homem e eu. Temos história.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você ouviu — claro, baixo, piu claro. Bianca sussurrou "
                        "pra Lucia. Você olha pra fronte — fingindo não ouvir. "
                        "Chiara ao seu lado também ouviu — você sente."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Quieres contarme?",
                    "translation": "Você quer me contar?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Hoy no. Ma pronto. Si te pueden ayudar a entender al Podesta — sí.",
                    "translation": "Hoje não. Mas logo. Se podem te ajudar a entender o Podesta — sim.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Forestiero — ¿oíste?",
                    "translation": "Forasteiro — você ouviu?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Você ouviu. Resposta direta:",
                    "options": [
                        {"id": "a", "text": "Sí, oí todo"},
                        {"id": "b", "text": "No oigo nada"},
                        {"id": "c", "text": "Vado a oír"},
                        {"id": "d", "text": "Sono oír"},
                    ],
                    "correct": "a",
                    "word_id": "it_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Bene. Esto se complica más. Lo hablamos en casa — no aquí.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "🚶 Os 8 caminhando juntos pra fora da piazza · La Guardia atrás, longe · Sol da manhã clara",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Tres testigos aceptados. Pase provisional. Para hoy — questo es triunfo.",
                    "translation": "Três testigos aceitos. Pase provisório. Pra hoje — isso é triunfo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você concorda — vitória parcial é melhor que nada:",
                    "options": [
                        {"id": "a", "text": "Sto bene, grazie"},
                        {"id": "b", "text": "Sto male"},
                        {"id": "c", "text": "Sono bene"},
                        {"id": "d", "text": "Ho bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Bene. Aprovechemos. Ma un mes pasa rápido.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara sugere: 'Andiamo a hablar con Bianca — hoy mismo, senza Lucia.' Você concorda:",
                    "options": [
                        {"id": "a", "text": "Sí, andiamo a hablar con ella"},
                        {"id": "b", "text": "Vado a hablar"},
                        {"id": "c", "text": "Va a hablar"},
                        {"id": "d", "text": "Sono hablar"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo los tres — senza Lucia. Mejor cuando ella no esté ascoltando.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico: 'Forestiero — ¿cómo estás después de toda la mañana?' Resposta honesta (bem piu cansado):",
                    "options": [
                        {"id": "a", "text": "Sto bene, ma cansado"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Vado bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_cansado", "target": "sto cansado", "native": "estou cansado",
                    "npc_reaction": "Lo entiendo. Andiamo a casa — descansa una hora. Después saleimos a buscar a Bianca.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F16 ────────────────────────
                {
                    "kind": "scene",
                    "text": "?? Caminhando de volta · Piazza vazia · Sol da manhã alta · O pase no bolso",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você passa a mão pelo bolso. O papel ainda está quente "
                        "do selo de cera. Pase provisório. Um mês.\n\n"
                        "Um mês pra entender por que Bianca e o Podesta têm "
                        "história. Um mês pra entender por que Lucia sabe "
                        "coisas que ninguém contou pra ela. Um mês pra "
                        "entender por que Doña Lucía reconheceu Lucia sem "
                        "saber de onde."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Forestiero — hoy ganaste un mes. Úsaleo bene.",
                    "translation": "Forasteiro — hoje você ganhou um mês. Use bem.",
                    "pace": "slow",
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




