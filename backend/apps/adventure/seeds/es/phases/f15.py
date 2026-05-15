"""
Seed das 6 seções da Fase 15 Espanhol A1 — "El primer testigo".

Manhã do quarto dia. Vocês quatro + Don Miguel + 3 testigos (Rosa, Carmen,
Eduardo) chegam ao ayuntamiento. Carmen testemunha primeiro. O Alcalde
recebe Carmen mais frio do que vocês esperavam.

NOVA TENSÃO REVELADA NO FIM:
    Saindo, Carmen sussurra pra María: 'Ese hombre y yo — tenemos
    historia.' Não conta agora o que é. Plantado pra próximas fases.

ABORDAGEM PEDAGÓGICA:
    Apresenta palabras pra descrever pessoas — alto, bajo, joven, viejo.
    O aluno aprende que essas palavras MUDAM dependendo de quem é
    descrito (homem ou mulher). SEM nomear "adjetivo" ou "concordância".
    Apenas mostrar: "Sofía es alta" / "Miguel es alto".

Vocab novo (3): alto · bajo · joven
Apresentação adicional: viejo · delgado (em vocab_list)

Revisão F1-F14 dominante:
  · vi/hablé/oí (F12) — Carmen relata
  · mi/tu/su (F13) — possessivos
  · el/la/los/las (F14) — gênero
  · voy a / vamos a (F11) — futuro próximo
  · soy/estoy/tengo (F8)

NPC principais: Carmen · El Alcalde · El Vigilante (fundo) · os 4
Arco emocional: tensão antes → testemunho corajoso → Alcalde frio →
                pase provisional + pista da Carmen
Transição:      F16 abre com Carmen contando ao grupo qual é a 'historia'
                dela com o Alcalde.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f15_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Chegada ao ayuntamiento. Apresentação dos adjetivos descritivos — Carmen
    # descreve o forastero usando palavras simples (alto, joven). 3 exer novos
    # + 1 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "investigacion",
                    "min_level": 2,
                    "uses_item_tag": "documento",
                    "success": "Voce compara o testemunho com detalhes vistos antes e percebe uma contradicao pequena.",
                    "fallback": "A contradicao escapa, mas a testemunha ainda entrega a pista principal.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🌄 Manhã do quarto dia · Ayuntamiento · Porta de ferro\n\n"
                        "Vocês são oito. Don Miguel à frente. Carmen — a primeira "
                        "testigo — vestida com a melhor blusa, cabelo penteado, "
                        "andando devagar mas decidida. Rosa e Eduardo atrás. Os "
                        "4 do grupo no final."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "El Alcalde já estava na sala — sentado, esperando. Reconheceu Carmen no instante em que ela entrou.",
                },
                {
                    "kind": "npc",
                    "npc": "El Alcalde",
                    "line": "Doña Carmen. No esperaba verla a usted aquí.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Buenos días, señor Alcalde. Vine como testigo.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "O Alcalde ficou sério. Carmen ficou em pé. Os dois se "
                        "olharam por meio segundo a mais do que precisariam."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "El Alcalde",
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
                        {"target": "joven",   "native": "jovem"},
                        {"target": "viejo",   "native": "velho"},
                        {"target": "delgado", "native": "magro"},
                    ],
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Doña Carmen — para empezar — describa al forastero. ¿Cómo es físicamente?",
                    "translation": "Dona Carmen — para começar — descreva o forasteiro. Como ele é fisicamente?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen olha pra você. Você é mais alto que Don Miguel. Como ela descreve sua altura?",
                    "options": [
                        {"id": "a", "text": "Es alto"},
                        {"id": "b", "text": "Es bajo"},
                        {"id": "c", "text": "Es viejo"},
                        {"id": "d", "text": "Es vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_alto", "target": "alto", "native": "alto",
                    "npc_reaction": "Anotado: alto. Sigamos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Você tem vinte anos. Carmen descreve sua idade:",
                    "options": [
                        {"id": "a", "text": "Es joven"},
                        {"id": "b", "text": "Es viejo"},
                        {"id": "c", "text": "Es bajo"},
                        {"id": "d", "text": "Es vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_joven", "target": "joven", "native": "jovem",
                    "npc_reaction": "Joven. Veinte años — eso ya está en el papel.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "El Alcalde: 'Y Don Miguel — el padre.' Don Miguel é mais baixo que você:",
                    "options": [
                        {"id": "a", "text": "Es bajo"},
                        {"id": "b", "text": "Es alto"},
                        {"id": "c", "text": "Es joven"},
                        {"id": "d", "text": "Es delgado"},
                    ],
                    "correct": "a",
                    "word_id": "es_bajo", "target": "bajo", "native": "baixo",
                    "npc_reaction": "Bajo y trabajador.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Carmen testemunha — relato em passado. O Alcalde anota.
    # Mistura F1-F14: pretérito, possessivos, gênero, soy/estoy/tengo.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Carmen", "El Alcalde"],
                "story": (
                    "Alcalde escreveu três linhas. Levantou a pena. Olhou pra "
                    "Carmen — agora calculista, não pessoal.\n\n"
                    "'Continuemos. Cuénteme — desde el primer día. Cómo encontró "
                    "al forastero. Qué hizo. Qué dijo.'"
                ),
                "now": "Carmen relata em passado. Você acompanha — pode ser chamado.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Lo conocí el primer día. Miguel — mi vecino — lo llevó hasta mi banco en la plaza.",
                    "translation": "Conheci ele no primeiro dia. Miguel — meu vizinho — levou ele até o meu banco na plaza.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'lo conocí'. Pra você confirmar pra ela que tu também lembra do primeiro encontro (já aconteceu, você viu Carmen):",
                    "options": [
                        {"id": "a", "text": "Sí, te vi ese día"},
                        {"id": "b", "text": "Sí, te veo"},
                        {"id": "c", "text": "Voy a verte"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Tú me viste. Yo te vi. Igual.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Hablé con él. Le pregunté su nombre — me lo dijo claro. Educado.",
                    "translation": "Falei com ele. Perguntei o nome — disse claro. Educado.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'hablé con él'. Significa que ela:",
                    "options": [
                        {"id": "a", "text": "Falou (já aconteceu)"},
                        {"id": "b", "text": "Fala (presente)"},
                        {"id": "c", "text": "Vai falar"},
                        {"id": "d", "text": "Quer falar"},
                    ],
                    "correct": "a",
                    "word_id": "es_hable", "target": "hablé", "native": "falei",
                    "npc_reaction": "Hablé. Yo, ya hecho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "¿Y le pareció peligroso, doña Carmen?",
                    "translation": "E pareceu perigoso pra você, dona Carmen?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "No, señor Alcalde. Me pareció perdido — no peligroso.",
                    "translation": "Não, senhor Alcalde. Pareceu perdido — não perigoso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "El Alcalde se vira pra você: 'Joven — ¿cómo te llamas?' Resposta firme:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo veinte años"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Anotado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "¿Y tu edad?",
                    "translation": "E sua idade?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Resposta exata:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Estoy veinte"},
                        {"id": "d", "text": "Voy veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Mismo que dijo Doña Carmen.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "¿Cómo estás hoy aquí, después de todo?",
                    "translation": "Como você está hoje aqui, depois de tudo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Estado de agora — com nervosismo mas firme:",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bien. Anotado.",
                },
                {
                    "kind": "narrative",
                    "text": "Uma porta abre no fundo. El Vigilante entra silencioso. Senta no fundo. Não cumprimenta.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "El Alcalde: 'Y María — la curandera. ¿Te gusta ella?' (você tem que escolher se é HONESTO ou SEGURO). Você prefere a resposta segura:",
                    "options": [
                        {"id": "a", "text": "Sí, me ayudó cuando estuve enfermo"},
                        {"id": "b", "text": "No, no me gusta"},
                        {"id": "c", "text": "Soy María"},
                        {"id": "d", "text": "Voy a María"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me ayudó", "native": "me ajudou",
                    "npc_reaction": "Ayudó. Anotado.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Alcalde quer ouvir o forastero direto. Você descreve outras pessoas
    # do grupo — Sofía (mulher), Miguel (homem), María (mulher). O aluno
    # ENXERGA que "alto" muda pra "alta" dependendo de quem é. SEM nomear.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["El Alcalde", "Carmen"],
                "story": (
                    "Carmen terminou. Foi pro banco do lado, perto de Don Miguel. "
                    "El Alcalde fechou a primeira página do livro de actas. Abriu "
                    "a segunda.\n\n"
                    "'Joven forastero — siéntese aquí. Conteste mis preguntas. "
                    "Sin ayuda.'"
                ),
                "now": "Você descreve as pessoas do grupo. Cada palavra muda dependendo de quem.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🪑 Cadeira de testigo · Você sentado · Alcalde com pena no papel",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Describe a Sofía — la joven que vino contigo. ¿Cómo es ella?",
                    "translation": "Descreve Sofía — a jovem que veio contigo. Como ela é?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Sofía é alta, da sua altura quase. Jovem. Magra. Pra ela "
                        "(mulher), a palavra 'alto' vira 'alta' — termina como "
                        "ela mesma."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Pra falar da altura de Sofía (mulher):",
                    "options": [
                        {"id": "a", "text": "Es alta"},
                        {"id": "b", "text": "Es alto"},
                        {"id": "c", "text": "Soy alta"},
                        {"id": "d", "text": "Estoy alta"},
                    ],
                    "correct": "a",
                    "word_id": "es_alta", "target": "alta", "native": "alta (mulher)",
                    "npc_reaction": "Alta. La palabra termina como ella — en '-a'. Igual que 'la' (de mujer).",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Sofía também é jovem — 18 anos. 'Joven' não termina em -a nem -o. Como você usa pra Sofía?",
                    "options": [
                        {"id": "a", "text": "Es joven"},
                        {"id": "b", "text": "Es jóvena"},
                        {"id": "c", "text": "Es jovena"},
                        {"id": "d", "text": "Es alta joven"},
                    ],
                    "correct": "a",
                    "word_id": "es_joven", "target": "joven", "native": "jovem",
                    "npc_reaction": "Joven. Esa palabra no cambia con hombre o mujer — sirve igual para los dos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Y Miguel — el hijo de Don Miguel. ¿Cómo es él?",
                    "translation": "E Miguel — o filho de Don Miguel. Como ele é?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Miguel é alto (igual a você). Pra descrever ele (homem):",
                    "options": [
                        {"id": "a", "text": "Es alto"},
                        {"id": "b", "text": "Es alta"},
                        {"id": "c", "text": "Soy alto"},
                        {"id": "d", "text": "Estoy alto"},
                    ],
                    "correct": "a",
                    "word_id": "es_alto", "target": "alto", "native": "alto (homem)",
                    "npc_reaction": "Alto. La palabra termina en '-o' — igual que 'el' (de hombre).",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Miguel também tem vinte anos — jovem. Pra ele:",
                    "options": [
                        {"id": "a", "text": "Es joven"},
                        {"id": "b", "text": "Es vejo"},
                        {"id": "c", "text": "Soy joven"},
                        {"id": "d", "text": "Es jovena"},
                    ],
                    "correct": "a",
                    "word_id": "es_joven", "target": "joven", "native": "jovem",
                    "npc_reaction": "Joven. Misma palabra para hombre o mujer.",
                },
                {
                    "kind": "narrative",
                    "text": "Você ouve a porta abrir de novo. El Vigilante chegou mais perto — está logo atrás de Don Miguel agora. Carmen aperta a mão de Don Miguel.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Ahora describe a María — la curandera.",
                    "translation": "Agora descreve María — a curandera.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "El Alcalde sabe que María chegou faz dois meses. Você nunca "
                        "disse isso pra ele. Quem disse? Nem Carmen disse. Mas você "
                        "lembra — María entrou no ayuntamiento sozinha na F11."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "María tem 24 anos. É jovem ainda. Magra. Descrição segura — sem comprometer. Pra ela (mulher), 'magra' fica:",
                    "options": [
                        {"id": "a", "text": "Es delgada"},
                        {"id": "b", "text": "Es delgado"},
                        {"id": "c", "text": "Soy delgada"},
                        {"id": "d", "text": "Estoy delgada"},
                    ],
                    "correct": "a",
                    "word_id": "es_delgada", "target": "delgada", "native": "magra (mulher)",
                    "npc_reaction": "Delgada. Eso me lo confirma usted — pero ya lo sabía.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Don Miguel — pra contraste, mais velho que vocês:",
                    "options": [
                        {"id": "a", "text": "Es viejo"},
                        {"id": "b", "text": "Es vieja"},
                        {"id": "c", "text": "Soy viejo"},
                        {"id": "d", "text": "Estoy viejo"},
                    ],
                    "correct": "a",
                    "word_id": "es_viejo", "target": "viejo", "native": "velho",
                    "npc_reaction": "Viejo. Pero todavía con buena cabeza. Eso lo confirmo yo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Carmen olha pra María — que está no fundo da sala. María "
                        "acena de leve pra Carmen. Carmen acena de volta. Algo entre "
                        "as duas que você não decifrou ainda."
                    ),
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Pausa nas testemunhas. El Alcalde sai. Carmen aproveita pra explicar
    # devagar — "as palavras de descrever pessoas terminam como elas mesmas".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Carmen", "Sofía"],
                "story": (
                    "El Alcalde se levantou — disse que ia escrever outras "
                    "actas e voltava em dez minutos. El Vigilante voltou pro "
                    "fundo.\n\n"
                    "Carmen aproveitou: 'Joven — antes que vuelva el Alcalde, "
                    "vamos a aclarar algo importante.'"
                ),
                "now": "Carmen explica como as palavras de descrever mudam.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Notaste — para Sofía dijiste 'alta'. Para Miguel dijiste 'alto'. Es la misma palabra — solo cambia el final.",
                    "translation": "Notou — para Sofía você disse 'alta'. Para Miguel você disse 'alto'. É a mesma palavra — só muda o final.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Alto (de hombre) · Alta (de mujer)",
                    "meaning": "A palavra de descrever termina igual à pessoa que ela descreve.",
                    "note": "como 'el/la' — termina en -o para hombre, -a para mujer",
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
                    "npc": "Carmen",
                    "question": "Don Miguel e Doña Lucía são dois — um homem e uma mulher. Pra dizer 'baixos' juntos (quando mistura homem e mulher, usa a forma de homem):",
                    "options": [
                        {"id": "a", "text": "Son bajos"},
                        {"id": "b", "text": "Son bajas"},
                        {"id": "c", "text": "Es bajo"},
                        {"id": "d", "text": "Está bajo"},
                    ],
                    "correct": "a",
                    "word_id": "es_bajos", "target": "bajos", "native": "baixos",
                    "npc_reaction": "Bajos. Cuando hay hombre y mujer mezclados, gana la forma de hombre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Pero ojo — algunas palabras no terminan en -o ni -a. Como 'joven'. Esa no cambia.",
                    "translation": "Mas atenção — algumas palavras não terminam em -o nem -a. Como 'joven'. Essa não muda.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Joven (não muda) · Jóvenes (muitos)",
                    "meaning": "Pra homem ou pra mulher é igual. Só muda se forem muitos.",
                    "note": "lo mismo con 'fácil', 'difícil' — terminan en consonante y no cambian",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Sofía e Catalina (que vai aparecer depois) são duas mulheres jovens. Plural:",
                    "options": [
                        {"id": "a", "text": "Son jóvenes"},
                        {"id": "b", "text": "Son jóvenas"},
                        {"id": "c", "text": "Es jovenas"},
                        {"id": "d", "text": "Estoy jóvenes"},
                    ],
                    "correct": "a",
                    "word_id": "es_jovenes", "target": "jóvenes", "native": "jovens",
                    "npc_reaction": "Jóvenes. 'Joven' no se hace 'jóvena' — solo suma '-es' al plural.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Carmen — y la palabra de descripción va antes o después?",
                    "translation": "Carmen — e a palavra de descrição vai antes ou depois?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Normalmente DEPOIS — diferente do português às vezes. Como você diz 'a casa grande':",
                    "options": [
                        {"id": "a", "text": "La casa grande"},
                        {"id": "b", "text": "La grande casa"},
                        {"id": "c", "text": "Casa la grande"},
                        {"id": "d", "text": "Grande la casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_orden", "target": "casa grande", "native": "casa primero",
                    "npc_reaction": "La casa grande. La cosa primero, la descripción después.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Alcalde volta. Rosa testifica curto. Eduardo idem. Alcalde NÃO concede
    # sello completo — pase provisional (1 mês). Negociação tensa.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["El Alcalde", "Rosa", "Eduardo", "Don Miguel"],
                "story": (
                    "El Alcalde voltou. Rosa subiu na cadeira de testigo — "
                    "depoimento curto. 'Le vendí pan el primer día. Le di "
                    "gratis el segundo. Es educado.'\n\n"
                    "Eduardo subiu depois — ainda mais curto. 'Lo vi en la "
                    "calle. Saludó bien. No vi nada raro.'"
                ),
                "now": "Tudo dito. Alcalde decide. Mas não como vocês esperavam.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "⚖️ Sala de actas · Três depoimentos no papel · Alcalde lendo em silêncio",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Tres testigos. Doña Carmen — respetada. Doña Rosa — vecina. Don Eduardo — trabajador. Aceptables.",
                    "translation": "Três testigos. Dona Carmen — respeitada. Dona Rosa — vizinha. Don Eduardo — trabalhador. Aceitáveis.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Pero — los tres lo vieron poco. Una semana, máximo dos. No me dan certeza para sellar.",
                    "translation": "Mas — os três o viram pouco. Uma semana, máximo duas. Não me dão certeza pra carimbar.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você sente o peito apertar. O peso do 'no'. Sofía olha pra Don Miguel. Don Miguel não desviou os olhos do Alcalde.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Pase provisional — válido un mes. Después: o el pase definitivo, o sale del pueblo.",
                    "translation": "Pase provisório — vale um mês. Depois: ou o pase definitivo, ou sai do pueblo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Não é a vitória total — mas não é a derrota. Você aceita formalmente:",
                    "options": [
                        {"id": "a", "text": "Sí, acepto"},
                        {"id": "b", "text": "No, no acepto"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Estoy"},
                    ],
                    "correct": "a",
                    "word_id": "es_acepto", "target": "acepto", "native": "aceito",
                    "npc_reaction": "Aceptado. El sello provisional sale ahora.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "El Alcalde derrete cera vermelha sobre o papel. Aperta o "
                        "selo de bronze. Esfria. Entrega o papel pra você.\n\n"
                        "Você segura. Pequeno triunfo. Quente nas mãos."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Un mes. Y aviso — el Vigilante seguirá observando. No me sorprenda.",
                    "translation": "Um mês. E aviso — El Vigilante vai continuar observando. Não me surpreenda.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Você agradece — formal, sem exagero:",
                    "options": [
                        {"id": "a", "text": "Gracias, señor Alcalde"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Vayan. Buenos días.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Bueno. Salimos.",
                    "translation": "Bom. Saímos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'Forastero — ¿cómo te sientes ahora?'",
                    "options": [
                        {"id": "a", "text": "Estoy mejor que antes"},
                        {"id": "b", "text": "Soy mejor"},
                        {"id": "c", "text": "Tengo mejor"},
                        {"id": "d", "text": "Voy mejor"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mejor", "target": "estoy mejor", "native": "estou melhor",
                    "npc_reaction": "Mejor. Un mes — pero algo es algo.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Saindo do ayuntamiento. Carmen sussurra pra María sobre o Alcalde.
    # Gate: errar trava. Closing prepara F16.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Carmen", "María", "Sofía"],
                "story": (
                    "Vocês saem do ayuntamiento. Pase provisório no bolso. "
                    "Don Miguel à frente. Carmen anda devagar — está ao "
                    "lado de María. Você está atrás dos dois. Vai ouvir o "
                    "que ela vai dizer."
                ),
                "now": "Cena rápida na escada. Você precisa reagir certo a cada momento.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🪨 Escada do ayuntamiento · Saindo · Carmen e María lado a lado",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "María — ese hombre y yo. Tenemos historia.",
                    "translation": "María — esse homem e eu. Temos história.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você ouviu — claro, baixo, mas claro. Carmen sussurrou "
                        "pra María. Você olha pra frente — fingindo não ouvir. "
                        "Sofía ao seu lado também ouviu — você sente."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Quieres contarme?",
                    "translation": "Você quer me contar?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Hoy no. Pero pronto. Si te pueden ayudar a entender al Alcalde — sí.",
                    "translation": "Hoje não. Mas logo. Se podem te ajudar a entender o Alcalde — sim.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Forastero — ¿oíste?",
                    "translation": "Forasteiro — você ouviu?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Você ouviu. Resposta direta:",
                    "options": [
                        {"id": "a", "text": "Sí, oí todo"},
                        {"id": "b", "text": "No oigo nada"},
                        {"id": "c", "text": "Voy a oír"},
                        {"id": "d", "text": "Soy oír"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Bueno. Esto se complica más. Lo hablamos en casa — no aquí.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "🚶 Os 8 caminhando juntos pra fora da plaza · El Vigilante atrás, longe · Sol da manhã clara",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Tres testigos aceptados. Pase provisional. Para hoy — eso es triunfo.",
                    "translation": "Três testigos aceitos. Pase provisório. Pra hoje — isso é triunfo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você concorda — vitória parcial é melhor que nada:",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Estoy mal"},
                        {"id": "c", "text": "Soy bien"},
                        {"id": "d", "text": "Tengo bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Aprovechemos. Pero un mes pasa rápido.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía sugere: 'Vamos a hablar con Carmen — hoy mismo, sin María.' Você concorda:",
                    "options": [
                        {"id": "a", "text": "Sí, vamos a hablar con ella"},
                        {"id": "b", "text": "Voy a hablar"},
                        {"id": "c", "text": "Va a hablar"},
                        {"id": "d", "text": "Soy hablar"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos los tres — sin María. Mejor cuando ella no esté escuchando.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'Forastero — ¿cómo estás después de toda la mañana?' Resposta honesta (bem mas cansado):",
                    "options": [
                        {"id": "a", "text": "Estoy bien, pero cansado"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Voy bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_cansado", "target": "estoy cansado", "native": "estou cansado",
                    "npc_reaction": "Lo entiendo. Vamos a casa — descansa una hora. Después salimos a buscar a Carmen.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F16 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🏡 Caminhando de volta · Plaza vazia · Sol da manhã alta · O pase no bolso",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você passa a mão pelo bolso. O papel ainda está quente "
                        "do selo de cera. Pase provisório. Um mês.\n\n"
                        "Um mês pra entender por que Carmen e o Alcalde têm "
                        "história. Um mês pra entender por que María sabe "
                        "coisas que ninguém contou pra ela. Um mês pra "
                        "entender por que Doña Lucía reconheceu María sem "
                        "saber de onde."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Forastero — hoy ganaste un mes. Úsalo bien.",
                    "translation": "Forasteiro — hoje você ganhou um mês. Use bem.",
                    "pace": "slow",
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
