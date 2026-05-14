"""
Seed das 6 seÃ§Ãµes da Fase 15 Espanhol A1 â€” "El primer testigo".

ManhÃ£ do quarto dia. VocÃªs quatro + Don Miguel + 3 testigos (Rosa, Carmen,
Eduardo) chegam ao ayuntamiento. Carmen testemunha primeiro. O Alcalde
recebe Carmen mais frio do que vocÃªs esperavam.

NOVA TENSÃƒO REVELADA NO FIM:
    Saindo, Carmen sussurra pra MarÃ­a: 'Ese hombre y yo â€” tenemos
    historia.' NÃ£o conta agora o que Ã©. Plantado pra prÃ³ximas fases.

ABORDAGEM PEDAGÃ“GICA:
    Apresenta palabras pra descrever pessoas â€” alto, bajo, joven, viejo.
    O aluno aprende que essas palavras MUDAM dependendo de quem Ã©
    descrito (homem ou mulher). SEM nomear "adjetivo" ou "concordÃ¢ncia".
    Apenas mostrar: "SofÃ­a es alta" / "Miguel es alto".

Vocab novo (3): alto Â· bajo Â· joven
ApresentaÃ§Ã£o adicional: viejo Â· delgado (em vocab_list)

RevisÃ£o F1-F14 dominante:
  Â· vi/hablÃ©/oÃ­ (F12) â€” Carmen relata
  Â· mi/tu/su (F13) â€” possessivos
  Â· el/la/los/las (F14) â€” gÃªnero
  Â· voy a / vamos a (F11) â€” futuro prÃ³ximo
  Â· soy/estoy/tengo (F8)

NPC principais: Carmen Â· El Alcalde Â· El Vigilante (fundo) Â· os 4
Arco emocional: tensÃ£o antes â†’ testemunho corajoso â†’ Alcalde frio â†’
                pase provisional + pista da Carmen
TransiÃ§Ã£o:      F16 abre com Carmen contando ao grupo qual Ã© a 'historia'
                dela com o Alcalde.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f15_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Chegada ao ayuntamiento. ApresentaÃ§Ã£o dos adjetivos descritivos â€” Carmen
    # descreve o forastero usando palavras simples (alto, joven). 3 exer novos
    # + 1 revisÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ„ ManhÃ£ do quarto dia Â· Ayuntamiento Â· Porta de ferro\n\n"
                        "VocÃªs sÃ£o oito. Don Miguel Ã  frente. Carmen â€” a primeira "
                        "testigo â€” vestida com a melhor blusa, cabelo penteado, "
                        "andando devagar mas decidida. Rosa e Eduardo atrÃ¡s. Os "
                        "4 do grupo no final."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "El Alcalde jÃ¡ estava na sala â€” sentado, esperando. Reconheceu Carmen no instante em que ela entrou.",
                },
                {
                    "kind": "npc",
                    "npc": "El Alcalde",
                    "line": "DoÃ±a Carmen. No esperaba verla a usted aquÃ­.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Buenos dÃ­as, seÃ±or Alcalde. Vine como testigo.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "O Alcalde ficou sÃ©rio. Carmen ficou em pÃ©. Os dois se "
                        "olharam por meio segundo a mais do que precisariam."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "El Alcalde",
                    "line": "Como guste. SiÃ©ntese. Empezamos por usted.",
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
                    "line": "DoÃ±a Carmen â€” para empezar â€” describa al forastero. Â¿CÃ³mo es fÃ­sicamente?",
                    "translation": "Dona Carmen â€” para comeÃ§ar â€” descreva o forasteiro. Como ele Ã© fisicamente?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen olha pra vocÃª. VocÃª Ã© mais alto que Don Miguel. Como ela descreve sua altura?",
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
                    "question": "VocÃª tem vinte anos. Carmen descreve sua idade:",
                    "options": [
                        {"id": "a", "text": "Es joven"},
                        {"id": "b", "text": "Es viejo"},
                        {"id": "c", "text": "Es bajo"},
                        {"id": "d", "text": "Es vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_joven", "target": "joven", "native": "jovem",
                    "npc_reaction": "Joven. Veinte aÃ±os â€” eso ya estÃ¡ en el papel.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "El Alcalde: 'Y Don Miguel â€” el padre.' Don Miguel Ã© mais baixo que vocÃª:",
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

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # 100% revisÃ£o. Carmen testemunha â€” relato em passado. O Alcalde anota.
    # Mistura F1-F14: pretÃ©rito, possessivos, gÃªnero, soy/estoy/tengo.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Carmen", "El Alcalde"],
                "story": (
                    "Alcalde escreveu trÃªs linhas. Levantou a pena. Olhou pra "
                    "Carmen â€” agora calculista, nÃ£o pessoal.\n\n"
                    "'Continuemos. CuÃ©nteme â€” desde el primer dÃ­a. CÃ³mo encontrÃ³ "
                    "al forastero. QuÃ© hizo. QuÃ© dijo.'"
                ),
                "now": "Carmen relata em passado. VocÃª acompanha â€” pode ser chamado.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Lo conocÃ­ el primer dÃ­a. Miguel â€” mi vecino â€” lo llevÃ³ hasta mi banco en la plaza.",
                    "translation": "Conheci ele no primeiro dia. Miguel â€” meu vizinho â€” levou ele atÃ© o meu banco na plaza.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'lo conocÃ­'. Pra vocÃª confirmar pra ela que tu tambÃ©m lembra do primeiro encontro (jÃ¡ aconteceu, vocÃª viu Carmen):",
                    "options": [
                        {"id": "a", "text": "SÃ­, te vi ese dÃ­a"},
                        {"id": "b", "text": "SÃ­, te veo"},
                        {"id": "c", "text": "Voy a verte"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. TÃº me viste. Yo te vi. Igual.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "HablÃ© con Ã©l. Le preguntÃ© su nombre â€” me lo dijo claro. Educado.",
                    "translation": "Falei com ele. Perguntei o nome â€” disse claro. Educado.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'hablÃ© con Ã©l'. Significa que ela:",
                    "options": [
                        {"id": "a", "text": "Falou (jÃ¡ aconteceu)"},
                        {"id": "b", "text": "Fala (presente)"},
                        {"id": "c", "text": "Vai falar"},
                        {"id": "d", "text": "Quer falar"},
                    ],
                    "correct": "a",
                    "word_id": "es_hable", "target": "hablÃ©", "native": "falei",
                    "npc_reaction": "HablÃ©. Yo, ya hecho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Â¿Y le pareciÃ³ peligroso, doÃ±a Carmen?",
                    "translation": "E pareceu perigoso pra vocÃª, dona Carmen?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "No, seÃ±or Alcalde. Me pareciÃ³ perdido â€” no peligroso.",
                    "translation": "NÃ£o, senhor Alcalde. Pareceu perdido â€” nÃ£o perigoso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "El Alcalde se vira pra vocÃª: 'Joven â€” Â¿cÃ³mo te llamas?' Resposta firme:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo veinte aÃ±os"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Anotado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Â¿Y tu edad?",
                    "translation": "E sua idade?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Resposta exata:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Estoy veinte"},
                        {"id": "d", "text": "Voy veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Mismo que dijo DoÃ±a Carmen.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Â¿CÃ³mo estÃ¡s hoy aquÃ­, despuÃ©s de todo?",
                    "translation": "Como vocÃª estÃ¡ hoje aqui, depois de tudo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Estado de agora â€” com nervosismo mas firme:",
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
                    "text": "Uma porta abre no fundo. El Vigilante entra silencioso. Senta no fundo. NÃ£o cumprimenta.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "El Alcalde: 'Y MarÃ­a â€” la curandera. Â¿Te gusta ella?' (vocÃª tem que escolher se Ã© HONESTO ou SEGURO). VocÃª prefere a resposta segura:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me ayudÃ³ cuando estuve enfermo"},
                        {"id": "b", "text": "No, no me gusta"},
                        {"id": "c", "text": "Soy MarÃ­a"},
                        {"id": "d", "text": "Voy a MarÃ­a"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me ayudÃ³", "native": "me ajudou",
                    "npc_reaction": "AyudÃ³. Anotado.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Alcalde quer ouvir o forastero direto. VocÃª descreve outras pessoas
    # do grupo â€” SofÃ­a (mulher), Miguel (homem), MarÃ­a (mulher). O aluno
    # ENXERGA que "alto" muda pra "alta" dependendo de quem Ã©. SEM nomear.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["El Alcalde", "Carmen"],
                "story": (
                    "Carmen terminou. Foi pro banco do lado, perto de Don Miguel. "
                    "El Alcalde fechou a primeira pÃ¡gina do livro de actas. Abriu "
                    "a segunda.\n\n"
                    "'Joven forastero â€” siÃ©ntese aquÃ­. Conteste mis preguntas. "
                    "Sin ayuda.'"
                ),
                "now": "VocÃª descreve as pessoas do grupo. Cada palavra muda dependendo de quem.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸª‘ Cadeira de testigo Â· VocÃª sentado Â· Alcalde com pena no papel",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Describe a SofÃ­a â€” la joven que vino contigo. Â¿CÃ³mo es ella?",
                    "translation": "Descreve SofÃ­a â€” a jovem que veio contigo. Como ela Ã©?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "SofÃ­a Ã© alta, da sua altura quase. Jovem. Magra. Pra ela "
                        "(mulher), a palavra 'alto' vira 'alta' â€” termina como "
                        "ela mesma."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Pra falar da altura de SofÃ­a (mulher):",
                    "options": [
                        {"id": "a", "text": "Es alta"},
                        {"id": "b", "text": "Es alto"},
                        {"id": "c", "text": "Soy alta"},
                        {"id": "d", "text": "Estoy alta"},
                    ],
                    "correct": "a",
                    "word_id": "es_alta", "target": "alta", "native": "alta (mulher)",
                    "npc_reaction": "Alta. La palabra termina como ella â€” en '-a'. Igual que 'la' (de mujer).",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "SofÃ­a tambÃ©m Ã© jovem â€” 18 anos. 'Joven' nÃ£o termina em -a nem -o. Como vocÃª usa pra SofÃ­a?",
                    "options": [
                        {"id": "a", "text": "Es joven"},
                        {"id": "b", "text": "Es jÃ³vena"},
                        {"id": "c", "text": "Es jovena"},
                        {"id": "d", "text": "Es alta joven"},
                    ],
                    "correct": "a",
                    "word_id": "es_joven", "target": "joven", "native": "jovem",
                    "npc_reaction": "Joven. Esa palabra no cambia con hombre o mujer â€” sirve igual para los dos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Y Miguel â€” el hijo de Don Miguel. Â¿CÃ³mo es Ã©l?",
                    "translation": "E Miguel â€” o filho de Don Miguel. Como ele Ã©?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Miguel Ã© alto (igual a vocÃª). Pra descrever ele (homem):",
                    "options": [
                        {"id": "a", "text": "Es alto"},
                        {"id": "b", "text": "Es alta"},
                        {"id": "c", "text": "Soy alto"},
                        {"id": "d", "text": "Estoy alto"},
                    ],
                    "correct": "a",
                    "word_id": "es_alto", "target": "alto", "native": "alto (homem)",
                    "npc_reaction": "Alto. La palabra termina en '-o' â€” igual que 'el' (de hombre).",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Miguel tambÃ©m tem vinte anos â€” jovem. Pra ele:",
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
                    "text": "VocÃª ouve a porta abrir de novo. El Vigilante chegou mais perto â€” estÃ¡ logo atrÃ¡s de Don Miguel agora. Carmen aperta a mÃ£o de Don Miguel.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Ahora describe a MarÃ­a â€” la curandera.",
                    "translation": "Agora descreve MarÃ­a â€” a curandera.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "El Alcalde sabe que MarÃ­a chegou faz dois meses. VocÃª nunca "
                        "disse isso pra ele. Quem disse? Nem Carmen disse. Mas vocÃª "
                        "lembra â€” MarÃ­a entrou no ayuntamiento sozinha na F11."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "MarÃ­a tem 24 anos. Ã‰ jovem ainda. Magra. DescriÃ§Ã£o segura â€” sem comprometer. Pra ela (mulher), 'magra' fica:",
                    "options": [
                        {"id": "a", "text": "Es delgada"},
                        {"id": "b", "text": "Es delgado"},
                        {"id": "c", "text": "Soy delgada"},
                        {"id": "d", "text": "Estoy delgada"},
                    ],
                    "correct": "a",
                    "word_id": "es_delgada", "target": "delgada", "native": "magra (mulher)",
                    "npc_reaction": "Delgada. Eso me lo confirma usted â€” pero ya lo sabÃ­a.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "Don Miguel â€” pra contraste, mais velho que vocÃªs:",
                    "options": [
                        {"id": "a", "text": "Es viejo"},
                        {"id": "b", "text": "Es vieja"},
                        {"id": "c", "text": "Soy viejo"},
                        {"id": "d", "text": "Estoy viejo"},
                    ],
                    "correct": "a",
                    "word_id": "es_viejo", "target": "viejo", "native": "velho",
                    "npc_reaction": "Viejo. Pero todavÃ­a con buena cabeza. Eso lo confirmo yo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Carmen olha pra MarÃ­a â€” que estÃ¡ no fundo da sala. MarÃ­a "
                        "acena de leve pra Carmen. Carmen acena de volta. Algo entre "
                        "as duas que vocÃª nÃ£o decifrou ainda."
                    ),
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Pausa nas testemunhas. El Alcalde sai. Carmen aproveita pra explicar
    # devagar â€” "as palavras de descrever pessoas terminam como elas mesmas".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Carmen", "SofÃ­a"],
                "story": (
                    "El Alcalde se levantou â€” disse que ia escrever outras "
                    "actas e voltava em dez minutos. El Vigilante voltou pro "
                    "fundo.\n\n"
                    "Carmen aproveitou: 'Joven â€” antes que vuelva el Alcalde, "
                    "vamos a aclarar algo importante.'"
                ),
                "now": "Carmen explica como as palavras de descrever mudam.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Notaste â€” para SofÃ­a dijiste 'alta'. Para Miguel dijiste 'alto'. Es la misma palabra â€” solo cambia el final.",
                    "translation": "Notou â€” para SofÃ­a vocÃª disse 'alta'. Para Miguel vocÃª disse 'alto'. Ã‰ a mesma palavra â€” sÃ³ muda o final.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Alto (de hombre) Â· Alta (de mujer)",
                    "meaning": "A palavra de descrever termina igual Ã  pessoa que ela descreve.",
                    "note": "como 'el/la' â€” termina en -o para hombre, -a para mujer",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "el hombre ", "isKey": False},
                        {"text": "alto",       "isKey": True},
                        {"text": " Â· la mujer ", "isKey": False},
                        {"text": "alta",       "isKey": True},
                        {"text": " Â· los hombres ", "isKey": False},
                        {"text": "altos",      "isKey": True},
                        {"text": " Â· las mujeres ", "isKey": False},
                        {"text": "altas",      "isKey": True},
                    ],
                    "example": "El hombre alto. La mujer alta. Los hombres altos. Las mujeres altas.",
                    "translation": "O homem alto. A mulher alta. Os homens altos. As mulheres altas.",
                    "note": "la palabra de descripciÃ³n termina igual que la persona â€” '-o', '-a', '-os', '-as'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Don Miguel e DoÃ±a LucÃ­a sÃ£o dois â€” um homem e uma mulher. Pra dizer 'baixos' juntos (quando mistura homem e mulher, usa a forma de homem):",
                    "options": [
                        {"id": "a", "text": "Son bajos"},
                        {"id": "b", "text": "Son bajas"},
                        {"id": "c", "text": "Es bajo"},
                        {"id": "d", "text": "EstÃ¡ bajo"},
                    ],
                    "correct": "a",
                    "word_id": "es_bajos", "target": "bajos", "native": "baixos",
                    "npc_reaction": "Bajos. Cuando hay hombre y mujer mezclados, gana la forma de hombre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Pero ojo â€” algunas palabras no terminan en -o ni -a. Como 'joven'. Esa no cambia.",
                    "translation": "Mas atenÃ§Ã£o â€” algumas palavras nÃ£o terminam em -o nem -a. Como 'joven'. Essa nÃ£o muda.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Joven (nÃ£o muda) Â· JÃ³venes (muitos)",
                    "meaning": "Pra homem ou pra mulher Ã© igual. SÃ³ muda se forem muitos.",
                    "note": "lo mismo con 'fÃ¡cil', 'difÃ­cil' â€” terminan en consonante y no cambian",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "SofÃ­a e Catalina (que vai aparecer depois) sÃ£o duas mulheres jovens. Plural:",
                    "options": [
                        {"id": "a", "text": "Son jÃ³venes"},
                        {"id": "b", "text": "Son jÃ³venas"},
                        {"id": "c", "text": "Es jovenas"},
                        {"id": "d", "text": "Estoy jÃ³venes"},
                    ],
                    "correct": "a",
                    "word_id": "es_jovenes", "target": "jÃ³venes", "native": "jovens",
                    "npc_reaction": "JÃ³venes. 'Joven' no se hace 'jÃ³vena' â€” solo suma '-es' al plural.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Carmen â€” y la palabra de descripciÃ³n va antes o despuÃ©s?",
                    "translation": "Carmen â€” e a palavra de descriÃ§Ã£o vai antes ou depois?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Normalmente DEPOIS â€” diferente do portuguÃªs Ã s vezes. Como vocÃª diz 'a casa grande':",
                    "options": [
                        {"id": "a", "text": "La casa grande"},
                        {"id": "b", "text": "La grande casa"},
                        {"id": "c", "text": "Casa la grande"},
                        {"id": "d", "text": "Grande la casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_orden", "target": "casa grande", "native": "casa primero",
                    "npc_reaction": "La casa grande. La cosa primero, la descripciÃ³n despuÃ©s.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Alcalde volta. Rosa testifica curto. Eduardo idem. Alcalde NÃƒO concede
    # sello completo â€” pase provisional (1 mÃªs). NegociaÃ§Ã£o tensa.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["El Alcalde", "Rosa", "Eduardo", "Don Miguel"],
                "story": (
                    "El Alcalde voltou. Rosa subiu na cadeira de testigo â€” "
                    "depoimento curto. 'Le vendÃ­ pan el primer dÃ­a. Le di "
                    "gratis el segundo. Es educado.'\n\n"
                    "Eduardo subiu depois â€” ainda mais curto. 'Lo vi en la "
                    "calle. SaludÃ³ bien. No vi nada raro.'"
                ),
                "now": "Tudo dito. Alcalde decide. Mas nÃ£o como vocÃªs esperavam.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "âš–ï¸ Sala de actas Â· TrÃªs depoimentos no papel Â· Alcalde lendo em silÃªncio",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Tres testigos. DoÃ±a Carmen â€” respetada. DoÃ±a Rosa â€” vecina. Don Eduardo â€” trabajador. Aceptables.",
                    "translation": "TrÃªs testigos. Dona Carmen â€” respeitada. Dona Rosa â€” vizinha. Don Eduardo â€” trabalhador. AceitÃ¡veis.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Pero â€” los tres lo vieron poco. Una semana, mÃ¡ximo dos. No me dan certeza para sellar.",
                    "translation": "Mas â€” os trÃªs o viram pouco. Uma semana, mÃ¡ximo duas. NÃ£o me dÃ£o certeza pra carimbar.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª sente o peito apertar. O peso do 'no'. SofÃ­a olha pra Don Miguel. Don Miguel nÃ£o desviou os olhos do Alcalde.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Pase provisional â€” vÃ¡lido un mes. DespuÃ©s: o el pase definitivo, o sale del pueblo.",
                    "translation": "Pase provisÃ³rio â€” vale um mÃªs. Depois: ou o pase definitivo, ou sai do pueblo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "NÃ£o Ã© a vitÃ³ria total â€” mas nÃ£o Ã© a derrota. VocÃª aceita formalmente:",
                    "options": [
                        {"id": "a", "text": "SÃ­, acepto"},
                        {"id": "b", "text": "No, no acepto"},
                        {"id": "c", "text": "AdiÃ³s"},
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
                        "selo de bronze. Esfria. Entrega o papel pra vocÃª.\n\n"
                        "VocÃª segura. Pequeno triunfo. Quente nas mÃ£os."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Alcalde",
                    "line": "Un mes. Y aviso â€” el Vigilante seguirÃ¡ observando. No me sorprenda.",
                    "translation": "Um mÃªs. E aviso â€” El Vigilante vai continuar observando. NÃ£o me surpreenda.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Alcalde",
                    "question": "VocÃª agradece â€” formal, sem exagero:",
                    "options": [
                        {"id": "a", "text": "Gracias, seÃ±or Alcalde"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Vayan. Buenos dÃ­as.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Bueno. Salimos.",
                    "translation": "Bom. SaÃ­mos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'Forastero â€” Â¿cÃ³mo te sientes ahora?'",
                    "options": [
                        {"id": "a", "text": "Estoy mejor que antes"},
                        {"id": "b", "text": "Soy mejor"},
                        {"id": "c", "text": "Tengo mejor"},
                        {"id": "d", "text": "Voy mejor"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mejor", "target": "estoy mejor", "native": "estou melhor",
                    "npc_reaction": "Mejor. Un mes â€” pero algo es algo.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Saindo do ayuntamiento. Carmen sussurra pra MarÃ­a sobre o Alcalde.
    # Gate: errar trava. Closing prepara F16.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Carmen", "MarÃ­a", "SofÃ­a"],
                "story": (
                    "VocÃªs saem do ayuntamiento. Pase provisÃ³rio no bolso. "
                    "Don Miguel Ã  frente. Carmen anda devagar â€” estÃ¡ ao "
                    "lado de MarÃ­a. VocÃª estÃ¡ atrÃ¡s dos dois. Vai ouvir o "
                    "que ela vai dizer."
                ),
                "now": "Cena rÃ¡pida na escada. VocÃª precisa reagir certo a cada momento.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸª¨ Escada do ayuntamiento Â· Saindo Â· Carmen e MarÃ­a lado a lado",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "MarÃ­a â€” ese hombre y yo. Tenemos historia.",
                    "translation": "MarÃ­a â€” esse homem e eu. Temos histÃ³ria.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "VocÃª ouviu â€” claro, baixo, mas claro. Carmen sussurrou "
                        "pra MarÃ­a. VocÃª olha pra frente â€” fingindo nÃ£o ouvir. "
                        "SofÃ­a ao seu lado tambÃ©m ouviu â€” vocÃª sente."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Quieres contarme?",
                    "translation": "VocÃª quer me contar?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Hoy no. Pero pronto. Si te pueden ayudar a entender al Alcalde â€” sÃ­.",
                    "translation": "Hoje nÃ£o. Mas logo. Se podem te ajudar a entender o Alcalde â€” sim.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” Â¿oÃ­ste?",
                    "translation": "Forasteiro â€” vocÃª ouviu?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "VocÃª ouviu. Resposta direta:",
                    "options": [
                        {"id": "a", "text": "SÃ­, oÃ­ todo"},
                        {"id": "b", "text": "No oigo nada"},
                        {"id": "c", "text": "Voy a oÃ­r"},
                        {"id": "d", "text": "Soy oÃ­r"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                    "npc_reaction": "Bueno. Esto se complica mÃ¡s. Lo hablamos en casa â€” no aquÃ­.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸš¶ Os 8 caminhando juntos pra fora da plaza Â· El Vigilante atrÃ¡s, longe Â· Sol da manhÃ£ clara",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Tres testigos aceptados. Pase provisional. Para hoy â€” eso es triunfo.",
                    "translation": "TrÃªs testigos aceitos. Pase provisÃ³rio. Pra hoje â€” isso Ã© triunfo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª concorda â€” vitÃ³ria parcial Ã© melhor que nada:",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Estoy mal"},
                        {"id": "c", "text": "Soy bien"},
                        {"id": "d", "text": "Tengo bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Aprovechemos. Pero un mes pasa rÃ¡pido.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a sugere: 'Vamos a hablar con Carmen â€” hoy mismo, sin MarÃ­a.' VocÃª concorda:",
                    "options": [
                        {"id": "a", "text": "SÃ­, vamos a hablar con ella"},
                        {"id": "b", "text": "Voy a hablar"},
                        {"id": "c", "text": "Va a hablar"},
                        {"id": "d", "text": "Soy hablar"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos los tres â€” sin MarÃ­a. Mejor cuando ella no estÃ© escuchando.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'Forastero â€” Â¿cÃ³mo estÃ¡s despuÃ©s de toda la maÃ±ana?' Resposta honesta (bem mas cansado):",
                    "options": [
                        {"id": "a", "text": "Estoy bien, pero cansado"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Voy bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_cansado", "target": "estoy cansado", "native": "estou cansado",
                    "npc_reaction": "Lo entiendo. Vamos a casa â€” descansa una hora. DespuÃ©s salimos a buscar a Carmen.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F16 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸ¡ Caminhando de volta Â· Plaza vazia Â· Sol da manhÃ£ alta Â· O pase no bolso",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª passa a mÃ£o pelo bolso. O papel ainda estÃ¡ quente "
                        "do selo de cera. Pase provisÃ³rio. Um mÃªs.\n\n"
                        "Um mÃªs pra entender por que Carmen e o Alcalde tÃªm "
                        "histÃ³ria. Um mÃªs pra entender por que MarÃ­a sabe "
                        "coisas que ninguÃ©m contou pra ela. Um mÃªs pra "
                        "entender por que DoÃ±a LucÃ­a reconheceu MarÃ­a sem "
                        "saber de onde."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Forastero â€” hoy ganaste un mes. Ãšsalo bien.",
                    "translation": "Forasteiro â€” hoje vocÃª ganhou um mÃªs. Use bem.",
                    "pace": "slow",
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
