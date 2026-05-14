"""
Seed das 6 seÃ§Ãµes da Fase 18 Espanhol A1 â€” "Don Miguel se entera".

Os trÃªs jovens reuniram tudo. Don Miguel ouviu. DecisÃ£o pendente:
o que fazer com MarÃ­a agora que existem trÃªs pistas concretas
(passado dela com Alcalde via Carmen, marca dos Buscadores, sussurro
de LucÃ­a).

DecisÃ£o final: continuar observando â€” sem confrontar. Mas Don Miguel
revela que tem uma carta guardada faz 20 anos. Vai mostrar amanhÃ£.

VOCAB NOVO (3): verdad Â· mentir Â· confiar
LINGUAGEM NOVA: poder + verbo (puedo / puedes / puede / podemos)
    Apresentado pelo uso natural â€” "no puedo decirle, todavÃ­a no"

RevisÃ£o F1-F17 dominante:
  Â· ya / todavÃ­a no (F17)
  Â· quiero + verbo (F16)
  Â· vi/hablÃ©/oÃ­ (F12)
  Â· mi/tu/su (F13)
  Â· el/la (F14)
  Â· soy/estoy/tengo (F8)

NPC principais: Don Miguel Â· SofÃ­a Â· Miguel Â· vocÃª
Arco emocional: dÃºvida â†’ reuniÃ£o â†’ decisÃ£o coletiva â†’ tensÃ£o crescente
TransiÃ§Ã£o: F19 abre logo apÃ³s â€” Don Miguel jÃ¡ indo atÃ© o baÃº.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f18_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # ManhÃ£ cedo. SofÃ­a e Miguel chegam Ã  casa de Don Miguel. MarÃ­a saiu
    # cedo â€” disse que ia ao mercado. Os 4 (Don Miguel + 3 jovens) na cozinha.
    # 2 novos exer + 2 revisÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ… Casa de Don Miguel Â· ManhÃ£ cedo Â· Cozinha\n\n"
                        "MarÃ­a saiu antes do amanhecer â€” disse que ia ao mercado "
                        "comprar hierbas. SofÃ­a e Miguel chegaram logo depois. "
                        "Don Miguel preparou cafÃ© forte. Quatro tigelas humeantes "
                        "na mesa baixa."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Bueno. Antes de que vuelva â€” vamos a juntar todo lo que sabemos.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "Empezamos por Carmen, despuÃ©s la marca, despuÃ©s lo de tu mujer.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "SÃ­. Pero antes â€” quiero saber quÃ© creen ustedes. Sin que yo influya.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Don Miguel quer ouvir vocÃªs primeiro. SofÃ­a olha pra Miguel. Miguel olha pra vocÃª. VocÃª decide comeÃ§ar.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "verdad",  "native": "verdade"},
                        {"target": "mentir",  "native": "mentir"},
                        {"target": "confiar", "native": "confiar"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel cumprimentou vocÃªs â€” amanhecer cedo:",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, Don Miguel"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as. Hijo â€” empieza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Lo que tenemos que decidir hoy es importante. Pero la verdad â€” Â¿quÃ© sentimos sobre MarÃ­a?",
                    "translation": "O que temos que decidir hoje Ã© importante. Mas a verdade â€” o que sentimos sobre MarÃ­a?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel falou 'la verdad'. Significa:",
                    "options": [
                        {"id": "a", "text": "Verdade (o que Ã© real)"},
                        {"id": "b", "text": "Mentira"},
                        {"id": "c", "text": "Pergunta"},
                        {"id": "d", "text": "Resposta"},
                    ],
                    "correct": "a",
                    "word_id": "es_verdad", "target": "verdad", "native": "verdade",
                    "npc_reaction": "Verdad. La cosa que es. Aunque duela.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "SofÃ­a responde â€” 'no es que MarÃ­a mienta. Es que oculta cosas.' A palavra 'mentir' significa:",
                    "options": [
                        {"id": "a", "text": "Dizer algo falso"},
                        {"id": "b", "text": "Dizer a verdade"},
                        {"id": "c", "text": "Estar quieto"},
                        {"id": "d", "text": "Sair correndo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mentir", "target": "mentir", "native": "mentir",
                    "npc_reaction": "Mentir. Decir algo falso. SofÃ­a hace bien la distinciÃ³n â€” MarÃ­a no miente. Calla.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'La pregunta es â€” Â¿podemos confiar en ella?' A palavra 'confiar' significa:",
                    "options": [
                        {"id": "a", "text": "Acreditar que alguÃ©m Ã© seguro"},
                        {"id": "b", "text": "Esconder coisas"},
                        {"id": "c", "text": "Lutar"},
                        {"id": "d", "text": "Sair"},
                    ],
                    "correct": "a",
                    "word_id": "es_confiar", "target": "confiar", "native": "confiar",
                    "npc_reaction": "Confiar. Creer que alguien no te va a hacer daÃ±o. Esa palabra siempre se gana â€” nunca se da.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Os 3 contam pra Don Miguel as 3 pistas em detalhe. 100% revisÃ£o F1-F17.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "SofÃ­a", "Miguel"],
                "story": (
                    "Don Miguel pegou um pedaÃ§o de papel velho e uma pena. "
                    "Quer anotar â€” pra ter clareza.\n\n"
                    "'Empezamos. Primero â€” lo de Carmen. SofÃ­a â€” cuÃ©ntalo tÃº.'"
                ),
                "now": "Cada pista Ã© contada do que jÃ¡ passou. Don Miguel anota.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Carmen nos contÃ³ que fue novia del Alcalde hace veinticinco aÃ±os. El padre del Alcalde rompiÃ³ el compromiso.",
                    "translation": "Carmen nos contou que foi noiva do Alcalde hÃ¡ vinte e cinco anos. O pai do Alcalde quebrou o noivado.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "SofÃ­a disse 'Carmen nos contÃ³'. 'ContÃ³' significa que Carmen:",
                    "options": [
                        {"id": "a", "text": "Contou (jÃ¡ passou)"},
                        {"id": "b", "text": "Conta (agora)"},
                        {"id": "c", "text": "Vai contar"},
                        {"id": "d", "text": "Sou contar"},
                    ],
                    "correct": "a",
                    "word_id": "es_conto", "target": "contÃ³", "native": "contou",
                    "npc_reaction": "ContÃ³. Ya pasÃ³. Anotando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y mi madre â€” anoche en la cocina â€” me dijo que conoce a MarÃ­a de algÃºn sitio. No recuerda de dÃ³nde.",
                    "translation": "E minha mÃ£e â€” ontem Ã  noite na cozinha â€” me disse que conhece MarÃ­a de algum lugar. NÃ£o lembra de onde.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Miguel disse 'me dijo'. Pra vocÃª confirmar pra Don Miguel â€” vocÃª ouviu o sussurro tambÃ©m:",
                    "options": [
                        {"id": "a", "text": "Yo tambiÃ©n lo oÃ­"},
                        {"id": "b", "text": "Yo oigo"},
                        {"id": "c", "text": "Voy a oÃ­r"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                    "npc_reaction": "OÃ­. Bueno. Dos puntos confirmados.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y ayer â€” la marca de Eduardo. MarÃ­a la reconociÃ³ sin disfrazar. Dijo que su familia tenÃ­a relaciÃ³n con esa gente.",
                    "translation": "E ontem â€” a marca de Eduardo. MarÃ­a a reconheceu sem disfarÃ§ar. Disse que sua famÃ­lia tinha relaÃ§Ã£o com essa gente.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel resumiu trÃªs pistas. Pra vocÃª confirmar que entendeu:",
                    "options": [
                        {"id": "a", "text": "SÃ­, ya entiendo las tres"},
                        {"id": "b", "text": "TodavÃ­a no entiendo"},
                        {"id": "c", "text": "Voy a entender"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "jÃ¡",
                    "npc_reaction": "Ya entiendes. Bueno.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Y hay otra cosa que solo el forastero y yo sabemos. Lo de la cena con MarÃ­a â€” ella sabÃ­a cosas que el forastero nunca contÃ³.",
                    "translation": "E tem outra coisa que sÃ³ o forasteiro e eu sabemos. Aquilo do jantar com MarÃ­a â€” ela sabia coisas que o forasteiro nunca contou.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'Cuatro pistas. Â¿Y quÃ© siente cada uno?' VocÃª responde honesto â€” tem medo:",
                    "options": [
                        {"id": "a", "text": "Tengo miedo"},
                        {"id": "b", "text": "Estoy miedo"},
                        {"id": "c", "text": "Soy miedo"},
                        {"id": "d", "text": "Voy miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_miedo", "target": "tengo miedo", "native": "tenho medo",
                    "npc_reaction": "Tengo miedo. Es vÃ¡lido â€” y necesario.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta â€” 'Don Miguel â€” Â¿tÃº la conoces de antes?' Pra Don Miguel ela usa 'tu' formal? NÃ£o â€” informal. Resposta dela:",
                    "options": [
                        {"id": "a", "text": "No, no la conozco de antes"},
                        {"id": "b", "text": "SÃ­, la conozco"},
                        {"id": "c", "text": "Voy a conocerla"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "nÃ£o",
                    "npc_reaction": "No. Pero mi mujer sÃ­. Y eso pesa.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel apresenta "poder + verbo" pelo uso. "Â¿Podemos confrontarla?
    # Â¿Podemos echarla? Â¿Puedo confiar?" Cada exercÃ­cio uma situaÃ§Ã£o. Mistura
    # revisÃ£o pesada com nova linguagem.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "SofÃ­a", "Miguel"],
                "story": (
                    "Don Miguel pousou a pena. Cruzou as mÃ£os. Pensa.\n\n"
                    "'Tenemos cuatro pistas. Pero la pregunta es â€” Â¿podemos "
                    "hacer algo con esto ahora?'"
                ),
                "now": "DiscussÃ£o tensa. DecisÃ£o pendente. Don Miguel orienta.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿Podemos confrontarla hoy mismo?",
                    "translation": "Podemos confrontÃ¡-la hoje mesmo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'podemos confrontarla'. A palavra 'podemos' significa:",
                    "options": [
                        {"id": "a", "text": "NÃ³s podemos (se quisermos / temos a opÃ§Ã£o)"},
                        {"id": "b", "text": "NÃ³s devemos"},
                        {"id": "c", "text": "NÃ³s vamos"},
                        {"id": "d", "text": "NÃ³s somos"},
                    ],
                    "correct": "a",
                    "word_id": "es_podemos", "target": "podemos", "native": "podemos",
                    "npc_reaction": "Podemos. Significa que tenemos la opciÃ³n â€” pero no la obligaciÃ³n.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Yo creo que no podemos. Si la enfrentamos ahora sin pruebas, ella se va a defender â€” y vamos a perder lo poco que sabemos.",
                    "translation": "Eu acho que nÃ£o podemos. Se a enfrentarmos agora sem provas, ela vai se defender â€” e vamos perder o pouco que sabemos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a disse 'no podemos'. Pra Miguel concordar â€” ele tambÃ©m acha que nÃ£o podem:",
                    "options": [
                        {"id": "a", "text": "Tienes razÃ³n â€” no podemos"},
                        {"id": "b", "text": "Vamos a confrontarla"},
                        {"id": "c", "text": "Yo voy"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_podemos", "target": "no podemos", "native": "nÃ£o podemos",
                    "npc_reaction": "No podemos. Por ahora. Bueno â€” pensemos quÃ© sÃ­ podemos hacer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Yo puedo seguir observÃ¡ndola. SofÃ­a puede hablar mÃ¡s con Carmen â€” quizÃ¡ Carmen sabe algo mÃ¡s.",
                    "translation": "Eu posso seguir observando ela. SofÃ­a pode falar mais com Carmen â€” talvez Carmen saiba algo mais.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'yo puedo seguir observÃ¡ndola'. A palavra 'puedo' significa:",
                    "options": [
                        {"id": "a", "text": "Eu posso (tenho a opÃ§Ã£o)"},
                        {"id": "b", "text": "Tu podes"},
                        {"id": "c", "text": "Ele pode"},
                        {"id": "d", "text": "NÃ³s podemos"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedo. Yo â€” primera. Cuando hablo de mÃ­ mismo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero â€” tÃº puedes seguir cerca de ella. TÃº eres quien le importa mÃ¡s. Si te abres un poco, ella va a decirte mÃ¡s.",
                    "translation": "Forasteiro â€” vocÃª pode seguir perto dela. VocÃª Ã© quem mais interessa pra ela. Se vocÃª se abrir um pouco, ela vai te dizer mais.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel disse 'tÃº puedes seguir cerca'. A palavra 'puedes' significa:",
                    "options": [
                        {"id": "a", "text": "Tu podes / vocÃª pode"},
                        {"id": "b", "text": "Eu posso"},
                        {"id": "c", "text": "Ela pode"},
                        {"id": "d", "text": "NÃ³s podemos"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedes", "target": "puedes", "native": "podes",
                    "npc_reaction": "Puedes. TÃº â€” segunda. Cuando le hablas a alguien.",
                },
                {
                    "kind": "player",
                    "text": (
                        "VocÃª pensa. Ficar perto de MarÃ­a. Pegar mais informaÃ§Ã£o. "
                        "Mas sem comprometer o grupo. Ã‰ possÃ­vel? VocÃª nÃ£o sabe."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "VocÃª concorda â€” pode tentar. Mas vocÃª nÃ£o quer mentir muito pra ela. Honesto:",
                    "options": [
                        {"id": "a", "text": "Puedo intentarlo, pero todavÃ­a no sÃ© bien"},
                        {"id": "b", "text": "Voy a mentir mucho"},
                        {"id": "c", "text": "Soy bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo intentarlo", "native": "posso tentar",
                    "npc_reaction": "Bueno. Honestidad â€” eso es lo que vale. Si no puedes â€” paras. Nadie te obliga.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Bueno. Plan â€” SofÃ­a habla con Carmen. Miguel observa por las calles. Yo me quedo en casa con MarÃ­a cuando vuelva. Y el forastero â€” habla conmigo aparte.",
                    "translation": "Bom. Plano â€” SofÃ­a fala com Carmen. Miguel observa pelas ruas. Eu fico em casa com MarÃ­a quando ela voltar. E o forasteiro â€” fala comigo separado.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra vocÃª confirmar pra Don Miguel â€” vocÃª concorda em ficar separado com ele:",
                    "options": [
                        {"id": "a", "text": "SÃ­, contigo"},
                        {"id": "b", "text": "Voy a salir"},
                        {"id": "c", "text": "Soy aparte"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_si", "target": "sÃ­", "native": "sim",
                    "npc_reaction": "Bueno. Antes de que vuelva â€” quiero enseÃ±arte la carta.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a: 'Â¿QuÃ© carta?' Don Miguel: 'Una que guardo hace veinte aÃ±os.' Pra vocÃª expressar que NÃƒO sabe o que Ã© ainda:",
                    "options": [
                        {"id": "a", "text": "TodavÃ­a no sÃ© quÃ© es"},
                        {"id": "b", "text": "Ya sÃ© quÃ© es"},
                        {"id": "c", "text": "Voy a saber"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavÃ­a no", "native": "ainda nÃ£o",
                    "npc_reaction": "TodavÃ­a no sabes. Pero pronto. Hoy mismo.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # SofÃ­a e Miguel saem. VocÃª fica com Don Miguel. ApresentaÃ§Ã£o formal de
    # "poder + verbo" â€” sem nomear "verbo modal". Apenas: "puedo, puedes,
    # podemos â€” quando algo Ã© possÃ­vel ou nÃ£o".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "SofÃ­a saiu pra falar com Carmen. Miguel saiu pelo lado dos "
                    "fundos pra circular pela praÃ§a. Sobrou vocÃª e Don Miguel "
                    "na cozinha.\n\n"
                    "'Antes de enseÃ±arte la carta â€” quiero aclararte algo de las "
                    "palabras que oÃ­ste mucho esta maÃ±ana. Puedo, puedes, podemos.'"
                ),
                "now": "Don Miguel explica como 'puedo + verbo' funciona.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "'Poder' es lo que te dice si algo es posible o no. Yo puedo hablar â€” quiere decir, soy capaz de hablar. Yo no puedo volar â€” quiere decir, no soy capaz.",
                    "translation": "'Poder' Ã© o que te diz se algo Ã© possÃ­vel ou nÃ£o. Yo puedo hablar â€” quer dizer, sou capaz de falar. Yo no puedo volar â€” quer dizer, nÃ£o sou capaz.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Puedo + verbo",
                    "meaning": "O que vocÃª Ã© capaz de fazer / tem permissÃ£o de fazer",
                    "note": "junta dos palabras â€” puedo hablar, puedo entrar, puedo confiar",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo puedo ", "isKey": True},
                        {"text": "hablar Â· ", "isKey": False},
                        {"text": "TÃº puedes ","isKey": True},
                        {"text": "ver Â· ",    "isKey": False},
                        {"text": "Ella puede ","isKey": True},
                        {"text": "decidir Â· ", "isKey": False},
                        {"text": "Podemos ",  "isKey": True},
                        {"text": "salir",     "isKey": False},
                    ],
                    "example": "Yo puedo cuidarte. TÃº puedes confiar en mÃ­. Ella puede salir cuando quiera. Podemos hablar maÃ±ana.",
                    "translation": "Eu posso cuidar de vocÃª. Tu podes confiar em mim. Ela pode sair quando quiser. Podemos falar amanhÃ£.",
                    "note": "puedo / puedes / puede / podemos â€” cambia con quien puede.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra vocÃª dizer que pode tentar ficar perto de MarÃ­a:",
                    "options": [
                        {"id": "a", "text": "Yo puedo intentarlo"},
                        {"id": "b", "text": "TÃº puedes intentar"},
                        {"id": "c", "text": "Ella puede"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedo. Cuando hablas de ti mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'CuÃ©ntame sobre ___ familia ahora â€” la tuya, lo que recuerdes.' Pra falar da SUA famÃ­lia (tua):",
                    "options": [
                        {"id": "a", "text": "tu"},
                        {"id": "b", "text": "mi"},
                        {"id": "c", "text": "su"},
                        {"id": "d", "text": "nuestra"},
                    ],
                    "correct": "a",
                    "word_id": "es_tu", "target": "tu familia", "native": "tua famÃ­lia",
                    "npc_reaction": "Tu familia. Cuando te hablo a ti â€” lo tuyo es 'tu'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra SofÃ­a: 'Mira a SofÃ­a â€” es ___' (SofÃ­a tem 18 anos, alta, magra). Pra descrever a altura dela (mulher):",
                    "options": [
                        {"id": "a", "text": "alta"},
                        {"id": "b", "text": "alto"},
                        {"id": "c", "text": "altos"},
                        {"id": "d", "text": "altas"},
                    ],
                    "correct": "a",
                    "word_id": "es_alta", "target": "alta", "native": "alta",
                    "npc_reaction": "Alta. SofÃ­a â€” mujer, alta. La palabra termina en '-a'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "E pra vocÃª descrever a casa de Don Miguel â€” 'palavra de mulher, uma sÃ³':",
                    "options": [
                        {"id": "a", "text": "la casa"},
                        {"id": "b", "text": "el casa"},
                        {"id": "c", "text": "los casa"},
                        {"id": "d", "text": "las casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_la", "target": "la casa", "native": "a casa",
                    "npc_reaction": "La casa. Mi casa â€” y por estos dÃ­as, tambiÃ©n tuya.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y la forma negativa â€” 'no puedo'. 'No puedo decirte todavÃ­a' significa que aÃºn no eres capaz, o que aÃºn no tienes permiso.",
                    "translation": "E a forma negativa â€” 'no puedo'. 'No puedo decirte todavÃ­a' significa que ainda nÃ£o Ã©s capaz, ou que ainda nÃ£o tens permissÃ£o.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª quer dizer que NÃƒO pode mentir pra MarÃ­a descaradamente â€” nÃ£o Ã© capaz:",
                    "options": [
                        {"id": "a", "text": "No puedo mentirle"},
                        {"id": "b", "text": "Puedo mentirle"},
                        {"id": "c", "text": "Voy a mentir"},
                        {"id": "d", "text": "Soy mentir"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_puedo", "target": "no puedo", "native": "nÃ£o posso",
                    "npc_reaction": "No puedes. Eso es honesto contigo mismo. Te ayuda a no romperte.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel finalmente abre o assunto da carta. Ainda nÃ£o mostra â€” sÃ³
    # explica como ela chegou nas mÃ£os dele. Conversa Ã­ntima. Foco em revisÃ£o
    # orgÃ¢nica + uso de poder/quero/ya/todavÃ­a no.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel se levantou da mesa. Foi atÃ© o canto da cozinha "
                    "onde fica o baÃº velho â€” coberto por um pano grosso. NÃ£o "
                    "abriu ainda. SÃ³ pousou a mÃ£o nele.\n\n"
                    "'Esta carta llegÃ³ a mis manos hace veinte aÃ±os. Te voy a "
                    "contar cÃ³mo.'"
                ),
                "now": "Don Miguel conta a histÃ³ria da carta. VocÃª ouve.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Yo tenÃ­a veintiocho aÃ±os. Trabajaba en el campo de mi padre. Un dÃ­a llegÃ³ un viejo al pueblo â€” viajero, cansado, con una capa rota.",
                    "translation": "Eu tinha vinte e oito anos. Trabalhava no campo do meu pai. Um dia chegou um velho ao pueblo â€” viajante, cansado, com uma capa rota.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'yo tenÃ­a veintiocho'. 'TenÃ­a' significa:",
                    "options": [
                        {"id": "a", "text": "Tinha (idade dele naquele tempo)"},
                        {"id": "b", "text": "Tem (agora)"},
                        {"id": "c", "text": "Vai ter"},
                        {"id": "d", "text": "Ã‰"},
                    ],
                    "correct": "a",
                    "word_id": "es_tenia", "target": "tenÃ­a", "native": "tinha",
                    "npc_reaction": "TenÃ­a. Como 'tengo' del pasado lejano. Yo tenÃ­a esa edad cuando pasÃ³ esto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "El viejo tenÃ­a la marca de los Buscadores â€” igual que Eduardo. Yo entonces no la conocÃ­a. Pero la vi.",
                    "translation": "O velho tinha a marca dos Buscadores â€” igual a Eduardo. Eu naquela Ã©poca nÃ£o conhecia. Mas vi.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'no la conocÃ­a'. Pra vocÃª reagir â€” vocÃª AGORA jÃ¡ conhece a marca (depois de F17):",
                    "options": [
                        {"id": "a", "text": "Ya la conozco yo tambiÃ©n"},
                        {"id": "b", "text": "TodavÃ­a no la conozco"},
                        {"id": "c", "text": "Voy a conocer"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "jÃ¡",
                    "npc_reaction": "Ya la conoces. Eso me alegra â€” vas mÃ¡s rÃ¡pido que yo a tu edad.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "El viejo se quedÃ³ tres dÃ­as. Me observÃ³. Me preguntÃ³ cosas â€” 'puedes guardar silencio?', 'puedes esperar veinte aÃ±os?'",
                    "translation": "O velho ficou trÃªs dias. Me observou. Me perguntou coisas â€” 'podes guardar silÃªncio?', 'podes esperar vinte anos?'",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O velho perguntou 'puedes guardar silencio?'. Pra Don Miguel responder ao velho â€” sim, ele podia:",
                    "options": [
                        {"id": "a", "text": "SÃ­, puedo"},
                        {"id": "b", "text": "TÃº puedes"},
                        {"id": "c", "text": "Voy a poder"},
                        {"id": "d", "text": "Soy puedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "SÃ­, puedo. Dije eso. Y cumplÃ­. Veinte aÃ±os.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Me dio la carta. Me dijo: 'Cuando llegue alguien al pueblo con la palabra encendida â€” abrÃ­rsela.' Me marchÃ©. MuriÃ³ a la semana siguiente.",
                    "translation": "Me deu a carta. Me disse: 'Quando chegar alguÃ©m ao pueblo com a palavra acesa â€” abrir pra ele.' Foi embora. Morreu na semana seguinte.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'cuando llegue alguien con la palabra encendida'. Pra vocÃª processar â€” vocÃª Ã© quem fez o fogo aparecer na F5. VocÃª confirma:",
                    "options": [
                        {"id": "a", "text": "Soy yo. Ya entiendo"},
                        {"id": "b", "text": "TodavÃ­a no soy"},
                        {"id": "c", "text": "Voy a ser"},
                        {"id": "d", "text": "Tengo"},
                    ],
                    "correct": "a",
                    "word_id": "es_soy", "target": "soy yo", "native": "sou eu",
                    "npc_reaction": "Soy yo. Eso es. Eres tÃº.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "EsperÃ© veinte aÃ±os. Cuando vi el fuego en el pasillo aquella noche â€” supe que ya era el momento. Pero querÃ­a estar seguro. Ahora â€” con todo lo que sabemos â€” ya no tengo dudas.",
                    "translation": "Esperei vinte anos. Quando vi o fogo no corredor aquela noite â€” soube que jÃ¡ era o momento. Mas queria ter certeza. Agora â€” com tudo que sabemos â€” jÃ¡ nÃ£o tenho dÃºvidas.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra vocÃª responder firme â€” vocÃª confia em Don Miguel (verbo confiar, com 'en'):",
                    "options": [
                        {"id": "a", "text": "ConfÃ­o en ti"},
                        {"id": "b", "text": "ConfÃ­as en ti"},
                        {"id": "c", "text": "Voy a confiar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_confiar", "target": "confÃ­o", "native": "confio",
                    "npc_reaction": "ConfÃ­as. Bueno. Eso me importa. Vamos al baÃºl.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Don Miguel se aproxima do baÃº. Hesita. Pergunta uma Ãºltima vez se vocÃª
    # estÃ¡ pronto. Gate: errar trava. Closing prepara F19 (carta revelada).
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel estÃ¡ em pÃ© do lado do baÃº. A mÃ£o sobre a tampa. "
                    "VocÃª sentado na mesa, cafÃ© frio na frente. Nenhum dos dois "
                    "falou nos Ãºltimos dois minutos.\n\n"
                    "'Antes de abrirlo â€” quiero preguntarte algo. Y quiero la "
                    "verdad.'"
                ),
                "now": "DecisÃ£o final. VocÃª precisa estar pronto.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸ“¦ BaÃº velho Â· Tampa fechada Â· Don Miguel com a mÃ£o sobre ele",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Â¿EstÃ¡s listo para ver una cosa que va a cambiar lo que sabes de ti?",
                    "translation": "EstÃ¡ pronto pra ver uma coisa que vai mudar o que sabe de vocÃª?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª precisa decidir. Honesto â€” tem medo, mas quer ver. Resposta com ya / todavÃ­a no e querer:",
                    "options": [
                        {"id": "a", "text": "Tengo miedo, pero ya quiero verla"},
                        {"id": "b", "text": "TodavÃ­a no quiero"},
                        {"id": "c", "text": "Soy listo"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya quiero", "native": "jÃ¡ quero",
                    "npc_reaction": "Bueno. Es la respuesta correcta. El miedo no se va â€” pero el querer es mÃ¡s fuerte.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Una pregunta mÃ¡s â€” Â¿puedes guardar lo que vamos a ver? Aunque MarÃ­a pregunte directamente?",
                    "translation": "Uma pergunta mais â€” vocÃª pode guardar o que vamos ver? Mesmo se MarÃ­a perguntar diretamente?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª responde â€” sim, pode. Junte 'puedo' com 'guardar':",
                    "options": [
                        {"id": "a", "text": "SÃ­, puedo guardarlo"},
                        {"id": "b", "text": "SÃ­, tÃº puedes"},
                        {"id": "c", "text": "Voy a guardar"},
                        {"id": "d", "text": "Soy guardar"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedo guardarlo. Bueno. Cuando dices 'puedo', te haces responsable.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Ãšltima â€” Â¿confÃ­as en mÃ­?",
                    "translation": "Ãšltima â€” confia em mim?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Resposta firme â€” sim, confia em Don Miguel:",
                    "options": [
                        {"id": "a", "text": "SÃ­, confÃ­o en ti"},
                        {"id": "b", "text": "No confÃ­o"},
                        {"id": "c", "text": "Voy a confiar"},
                        {"id": "d", "text": "Soy confÃ­o"},
                    ],
                    "correct": "a",
                    "word_id": "es_confiar", "target": "confÃ­o", "native": "confio",
                    "npc_reaction": "ConfÃ­as. Y yo en ti tambiÃ©n. Bueno â€” vamos.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F19 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸ“¦ Don Miguel levanta a tampa do baÃº Â· Dentro: papÃ©is velhos, livros, um envelope selado em cera vermelha",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel pegou o envelope. Mostrou pra vocÃª. O selo em "
                        "cera tinha o mesmo sÃ­mbolo da marca de Eduardo â€” o sol "
                        "partido.\n\n"
                        "VocÃª nunca tinha visto. Mas sentiu o peito apertar â€” "
                        "como quando 'fuego' saiu na F5. Algo dentro reconheceu."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "MaÃ±ana â€” al amanecer â€” la abrimos juntos. Hoy dormimos. Necesitas la cabeza clara.",
                    "translation": "AmanhÃ£ â€” ao amanhecer â€” abrimos juntos. Hoje dormimos. VocÃª precisa da cabeÃ§a clara.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel fechou o baÃº. Trancou. PÃ´s o pano em cima. "
                        "MarÃ­a nÃ£o tinha voltado ainda do mercado.\n\n"
                        "VocÃª foi pro quarto. Deitou de olhos abertos. A imagem do "
                        "envelope com cera vermelha nÃ£o saÃ­a da cabeÃ§a.\n\n"
                        "AmanhÃ£."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
