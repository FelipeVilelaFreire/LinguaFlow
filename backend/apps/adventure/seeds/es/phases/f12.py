"""
Seed das 6 seÃ§Ãµes da Fase 12 Espanhol A1 â€” "Tres dÃ­as".

Carmen aceitou testemunhar. Eduardo aceitou (com a condiÃ§Ã£o estranha
sobre as costas). Falta um terceiro testigo imparcial. Esta fase
apresenta o PASSADO de forma natural â€” porque pra testemunhar Ã©
preciso contar o que aconteceu antes.

ABORDAGEM PEDAGÃ“GICA:
    Os NPCs usam o passado naturalmente. O aluno aprende pelo uso â€”
    "vi", "oÃ­", "hablÃ©" aparecem em situaÃ§Ãµes claras. Sem termo
    tÃ©cnico. Sem tabela de conjugaÃ§Ã£o. Carmen e Eduardo sÃ£o quem
    usam, e o jogador entende pelo contexto.

Vocab novo (2): ayer Â· vi
ApresentaÃ§Ã£o adicional: oÃ­ Â· hablÃ© (no vocab_list, sem foco em todos)

RevisÃ£o F1-F11 dominante:
  Â· me llamo / soy forastero (F1, F8, F11)
  Â· tengo veinte aÃ±os (F7, F11)
  Â· estoy bien (F8, F11)
  Â· me gusta / no me gusta (F9)
  Â· vamos a (F11) â€” futuro prÃ³ximo jÃ¡ conhecido
  Â· gracias / buenos dÃ­as (F1)
  Â· vecino (F7) â€” Carmen e Eduardo sÃ£o vecinos imparciales

NPC principais: Carmen Â· Eduardo Â· SofÃ­a Â· Don Miguel Â· MarÃ­a
NPC tensÃ£o:     El Vigilante (vigia o grupo)
Arco emocional: trabalho em equipe â†’ tensÃ£o sobre o 3Âº testigo
TransiÃ§Ã£o:      F13 abre com Miguel propondo levar o grupo pra casa
                da mÃ£e dele essa noite.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f12_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # ManhÃ£ do segundo dia. Carmen ensaiando com SofÃ­a. ApresentaÃ§Ã£o suave
    # do passado â€” Carmen usa "vi", "hablÃ©" em conversa real. 1 exercÃ­cio
    # novo sobre 'ayer' + revisÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "â˜€ï¸ ManhÃ£ do segundo dia Â· Casa de Don Miguel Â· Cozinha cheia\n\n"
                        "Carmen sentada Ã  mesa com SofÃ­a explicando o protocolo do "
                        "ayuntamiento. Miguel servindo cafÃ© pra todos. MarÃ­a na "
                        "panela do fundo â€” quieta desde que voltou ontem Ã  noite."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Ya he testificado dos veces antes en mi vida. SÃ© cÃ³mo se hace.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "CuÃ©ntale al forastero quÃ© van a preguntar. Para que sepa.",
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Primero â€” 'Â¿CuÃ¡ndo lo conociÃ³?' Y yo digo: 'Lo conocÃ­ el segundo dÃ­a. HablÃ© con Ã©l. Lo vi cumplir saludos.'",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "VocÃª ouve as palavras 'hablÃ©' e 'vi' pela primeira vez "
                        "com esse formato. NÃ£o Ã© 'hablo' (falo agora) â€” Ã© 'hablÃ©' "
                        "(falei antes). Algo mudou no fim da palavra."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Es para hablar de cosas que ya pasaron. Ayer pasÃ³ â€” entonces hablamos asÃ­.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "ayer",  "native": "ontem"},
                        {"target": "vi",    "native": "vi (jÃ¡ aconteceu)"},
                        {"target": "oÃ­",    "native": "ouvi (jÃ¡ aconteceu)"},
                        {"target": "hablÃ©", "native": "falei (jÃ¡ aconteceu)"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen quer falar do dia que jÃ¡ passou â€” o anterior a hoje. A palavra que ela usa:",
                    "options": [
                        {"id": "a", "text": "Ayer"},
                        {"id": "b", "text": "Hoy"},
                        {"id": "c", "text": "MaÃ±ana"},
                        {"id": "d", "text": "Siempre"},
                    ],
                    "correct": "a",
                    "word_id": "es_ayer", "target": "ayer", "native": "ontem",
                    "npc_reaction": "Ayer. El dÃ­a que ya pasÃ³. Quando hablamos del 'ayer', las palavras cambian un poco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'lo **vi** cumplir saludos'. 'Vi' significa que ela:",
                    "options": [
                        {"id": "a", "text": "Viu (algo jÃ¡ aconteceu)"},
                        {"id": "b", "text": "VÃª (acontece agora)"},
                        {"id": "c", "text": "Vai ver (amanhÃ£)"},
                        {"id": "d", "text": "Quer ver"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Yo vi â€” y ya pasÃ³. La 'i' final con acento te dice que es algo del pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a bebe cafÃ© e olha pra vocÃª: 'Forastero â€” Â¿cÃ³mo estÃ¡s hoy?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Hoy es dÃ­a de mucho movimiento â€” vas a necesitar fuerza.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # 100% revisÃ£o. Carmen ensaiando com o forastero â€” testa o que o Alcalde
    # pode perguntar. Nenhum exercÃ­cio de palavra nova. F1-F11 puro.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Carmen", "SofÃ­a"],
                "story": (
                    "Carmen vai testemunhar amanhÃ£. Pra nÃ£o se contradizer, ela "
                    "quer ensaiar â€” pede que o forastero responda as mesmas "
                    "perguntas que o Alcalde fez ontem. Ela ouve sem interromper."
                ),
                "now": "Carmen testa. VocÃª responde tudo de novo â€” com mais firmeza.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Empezamos. 'Â¿CÃ³mo te llamas tÃº?'",
                    "translation": "ComeÃ§amos. 'Como vocÃª se chama?'",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen quer te ouvir sem hesitar:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo veinte aÃ±os"},
                        {"id": "d", "text": "Vamos a hablar"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Bien. Sin pausa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "'Â¿QuÃ© eres tÃº aquÃ­?'",
                    "translation": "'O que vocÃª Ã© aqui?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Identidade â€” o que vocÃª Ã‰ no pueblo:",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Estoy forastero"},
                        {"id": "c", "text": "Tengo forastero"},
                        {"id": "d", "text": "Voy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_soy", "target": "soy", "native": "sou",
                    "npc_reaction": "Soy. Eso eres â€” y eso queda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "'Â¿CÃ³mo estÃ¡s aquÃ­, despuÃ©s de tantos dÃ­as?'",
                    "translation": "'Como vocÃª estÃ¡ aqui, depois de tantos dias?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Como vocÃª se sente hoje, neste momento:",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Voy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Estoy bien. Estado de ahora.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Ahora la trampa â€” 'Â¿CuÃ¡ntos aÃ±os tienes?'",
                    "translation": "Agora a pegadinha â€” 'Quantos anos vocÃª tem?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Resposta exata. Tenho vinte:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "Soy veinte aÃ±os"},
                        {"id": "c", "text": "Estoy veinte"},
                        {"id": "d", "text": "Me llamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Tengo. La edad va con 'tengo' siempre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Una mÃ¡s: 'Â¿Te gusta el pueblo?'",
                    "translation": "Mais uma: 'VocÃª gosta do pueblo?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Sincero. VocÃª gosta:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me gusta"},
                        {"id": "b", "text": "SÃ­, soy gusta"},
                        {"id": "c", "text": "SÃ­, estoy gusta"},
                        {"id": "d", "text": "SÃ­, tengo gusta"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Me gusta. La cosa que te gusta actÃºa sobre ti â€” MarÃ­a ya te lo enseÃ±Ã³ hace tiempo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Y 'Â¿quÃ© vas a hacer en mi pueblo?' â€” esa tambiÃ©n la van a preguntar.",
                    "translation": "E 'Â¿quÃ© vas a hacer en mi pueblo?' â€” essa tambÃ©m vÃ£o perguntar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "VocÃª precisa dizer o que vai fazer logo â€” buscar o terceiro testigo:",
                    "options": [
                        {"id": "a", "text": "Voy a buscar al tercer testigo"},
                        {"id": "b", "text": "Soy a buscar"},
                        {"id": "c", "text": "Estoy a buscar"},
                        {"id": "d", "text": "Tengo a buscar"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a buscar", "native": "vou buscar",
                    "npc_reaction": "Voy a. Lo que sale ahora. Bien usado.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Visita a Eduardo na herrerÃ­a pra ensaiar o testemunho dele. Eduardo
    # conta ONTEM o que viu â€” usando passado naturalmente. O aluno OUVE
    # passado em contexto e reconhece. Foco em REVISÃƒO + apresentaÃ§Ã£o suave
    # de 'vi' e 'hablÃ©' usados pelos NPCs.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Eduardo", "Don Miguel"],
                "story": (
                    "Foram Ã  herrerÃ­a. Eduardo recebeu, trancou a porta â€” nÃ£o "
                    "quer testemunhar com gente passando. Sentou no banco baixo "
                    "e disse: 'Voy a contarte lo que vi. MemorÃ­zalo â€” porque "
                    "es lo que repetirÃ© al Alcalde.'"
                ),
                "now": "Eduardo conta o que viu. VocÃª reconhece o que ele usou ontem.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Eduardo",
                    "situation": "Eduardo trabalhou a manhÃ£ inteira na fragua. O fogo do carvÃ£o deixa a garganta seca. Ele aponta pra mochila do forastero.",
                    "npc_line": "Antes de empezar â€” Â¿tienes algo de beber? La fragua seca la garganta como el desierto.",
                    "item_tag": "bebida",
                    "on_use": {
                        "narrative": "VocÃª passa algo de beber pra Eduardo. Ele bebe devagar, olhando vocÃª por cima do copo.",
                        "npc_reaction": "Gracias, joven. Quien comparte agua con un herrero â€” ese tiene mi palabra. Voy a testificar bien.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Hay un balde de agua en el rincÃ³n. Pero gracias por pensar.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Ayer por la maÃ±ana yo estaba en mi taller. SalÃ­ a las ocho â€” vi al forastero en la plaza con SofÃ­a.",
                    "translation": "Ontem de manhÃ£ eu estava no meu taller. SaÃ­ Ã s oito â€” vi o forasteiro na plaza com SofÃ­a.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo disse 'vi al forastero'. Aqui ele tÃ¡ falando de:",
                    "options": [
                        {"id": "a", "text": "Algo que aconteceu ontem"},
                        {"id": "b", "text": "Algo que acontece todo dia"},
                        {"id": "c", "text": "Algo que ainda vai acontecer"},
                        {"id": "d", "text": "Algo que ele vai fazer"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Yo vi â€” y se acabÃ³. La 'i' con acento dice que ya pasÃ³.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "HablÃ© con el joven. Le preguntÃ© si tenÃ­a hambre. Me respondiÃ³ que sÃ­.",
                    "translation": "Falei com o jovem. Perguntei se ele tinha fome. Ele respondeu que sim.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo disse 'hablÃ© contigo'. Significa que ele:",
                    "options": [
                        {"id": "a", "text": "Falou (jÃ¡ aconteceu)"},
                        {"id": "b", "text": "Fala (todo dia)"},
                        {"id": "c", "text": "Vai falar (amanhÃ£)"},
                        {"id": "d", "text": "Quer falar"},
                    ],
                    "correct": "a",
                    "word_id": "es_hable", "target": "hablÃ©", "native": "falei",
                    "npc_reaction": "HablÃ©. Yo hablÃ© â€” ya pasÃ³. Misma idea: lo del 'ayer' lleva 'Ã©' final.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "VocÃª lembra do encontro. Pra confirmar pra Eduardo que VOCÃŠ TAMBÃ‰M viu ele:",
                    "options": [
                        {"id": "a", "text": "Yo te vi tambiÃ©n"},
                        {"id": "b", "text": "Yo te veo"},
                        {"id": "c", "text": "Voy a verte"},
                        {"id": "d", "text": "Soy ver"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Bien. Yo vi. TÃº viste. Igual de simple.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Eduardo â€” ahora dile al forastero quÃ© le vas a decir al Alcalde maÃ±ana.",
                    "translation": "Eduardo â€” agora diz pro forasteiro o que vocÃª vai dizer pro Alcalde amanhÃ£.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Eduardo vai testemunhar amanhÃ£. Pra confirmar que ele VAI fazer isso:",
                    "options": [
                        {"id": "a", "text": "Eduardo va a testificar"},
                        {"id": "b", "text": "Eduardo voy a testificar"},
                        {"id": "c", "text": "Eduardo vamos a testificar"},
                        {"id": "d", "text": "Eduardo soy testificar"},
                    ],
                    "correct": "a",
                    "word_id": "es_va_a", "target": "va a", "native": "vai (algo logo)",
                    "npc_reaction": "Va â€” Eduardo, Ã©l. Lo que aprendiste con Don Miguel: voy, vas, va.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Voy a decirle: 'ConocÃ­ al joven el segundo dÃ­a. HablÃ© con Ã©l. SaludÃ³ con respeto. No vi nada raro.'",
                    "translation": "Vou dizer pra ele: 'Conheci o jovem no segundo dia. Falei com ele. Cumprimentou com respeito. NÃ£o vi nada estranho.'",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo termina dizendo 'no vi nada raro'. Pra negar algo que NÃƒO aconteceu antes â€” a palavra 'no' fica:",
                    "options": [
                        {"id": "a", "text": "Antes do verbo (no vi)"},
                        {"id": "b", "text": "Depois do verbo (vi no)"},
                        {"id": "c", "text": "NÃ£o existe negaÃ§Ã£o"},
                        {"id": "d", "text": "SÃ³ no fim da frase"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "nÃ£o",
                    "npc_reaction": "No al principio. Igual que 'no me gusta'. Simple.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel comenta: 'Ayer la plaza estaba llena. El Vigilante tambiÃ©n te vio.' VocÃª confirma â€” vocÃª sabe que ele viu (jÃ¡ aconteceu):",
                    "options": [
                        {"id": "a", "text": "SÃ­, Ã©l me vio"},
                        {"id": "b", "text": "SÃ­, Ã©l me ve"},
                        {"id": "c", "text": "SÃ­, Ã©l va a verme"},
                        {"id": "d", "text": "SÃ­, soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vio", "target": "vio", "native": "viu",
                    "npc_reaction": "Vio. Ã‰l vio â€” ya pasÃ³. Aprendiste rÃ¡pido: 'yo vi, tÃº viste, Ã©l vio'. La forma cambia con quien hizo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Una pregunta mÃ¡s â€” Â¿tÃº me viste anteayer? Yo te saludÃ© y tÃº me respondiste.",
                    "translation": "Mais uma pergunta â€” vocÃª me viu anteontem? Eu te cumprimentei e vocÃª me respondeu.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Sim, vocÃª viu Eduardo no mercado. Resposta firme:",
                    "options": [
                        {"id": "a", "text": "SÃ­, te vi"},
                        {"id": "b", "text": "SÃ­, te veo"},
                        {"id": "c", "text": "Voy a verte"},
                        {"id": "d", "text": "Soy verte"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Te vi. Y yo te vi a ti tambiÃ©n â€” por eso voy a testificar maÃ±ana.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Saindo da herrerÃ­a. Don Miguel para o grupo na plaza e explica devagar
    # como contar algo do passado. SEM nomear "pretÃ©rito". Apenas: "as palavras
    # mudam quando vocÃª fala de algo que jÃ¡ aconteceu". ~3-4 exercÃ­cios.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "SofÃ­a"],
                "story": (
                    "VocÃªs voltam da herrerÃ­a pela praÃ§a. Don Miguel decide parar "
                    "perto do poÃ§o â€” quer que o forastero entenda o que Eduardo "
                    "tava fazendo com as palavras. 'Si lo entiendes ahora, maÃ±ana "
                    "en el ayuntamiento vas a entender todo lo que digan.'"
                ),
                "now": "Don Miguel explica como falar do que jÃ¡ aconteceu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Eduardo dijo 'hablÃ©', 'vi', 'salÃ­'. Lo que ya pasÃ³. Las palabras cambian al final cuando es 'ayer' y no 'hoy'.",
                    "translation": "Eduardo disse 'hablÃ©', 'vi', 'salÃ­'. O que jÃ¡ passou. As palavras mudam no final quando Ã© 'ayer' e nÃ£o 'hoy'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Hoy hablo Â· Ayer hablÃ©",
                    "meaning": "Hoje eu falo Â· Ontem eu falei",
                    "note": "a palavra termina diferente quando algo jÃ¡ aconteceu",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo habl",  "isKey": False},
                        {"text": "Ã©",        "isKey": True},
                        {"text": " Â· Yo v",  "isKey": False},
                        {"text": "i",        "isKey": True},
                        {"text": " Â· Yo o",  "isKey": False},
                        {"text": "Ã­",        "isKey": True},
                    ],
                    "example": "Yo hablÃ© con Carmen. Yo vi al Vigilante. Yo oÃ­ su voz.",
                    "translation": "Eu falei com Carmen. Eu vi El Vigilante. Eu ouvi a voz dele.",
                    "note": "quando ya pasÃ³: la palabra termina con sonido fuerte â€” Ã© Â· Ã­",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "VocÃª falou com Carmen ontem. Pra contar isso pra alguÃ©m:",
                    "options": [
                        {"id": "a", "text": "HablÃ© con Carmen ayer"},
                        {"id": "b", "text": "Hablo con Carmen ayer"},
                        {"id": "c", "text": "Voy a hablar ayer"},
                        {"id": "d", "text": "Soy con Carmen"},
                    ],
                    "correct": "a",
                    "word_id": "es_hable", "target": "hablÃ©", "native": "falei",
                    "npc_reaction": "HablÃ©. Yo, ya pasado, ya hecho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y cambia con quien lo hizo â€” igual que con 'voy/vas/va' cuando algo va a salir.",
                    "translation": "E muda com quem fez â€” igual a 'voy/vas/va' quando algo vai sair.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo vi Â· ", "isKey": True},
                        {"text": "TÃº viste Â· ", "isKey": True},
                        {"text": "Ã‰l/Ella vio", "isKey": True},
                    ],
                    "example": "Yo vi a Carmen. TÃº viste a Eduardo. MarÃ­a vio al Alcalde.",
                    "translation": "Eu vi Carmen. VocÃª viu Eduardo. MarÃ­a viu El Alcalde.",
                    "note": "es el verbo 'ver' cuando ya pasÃ³. Las terminaciones cambian con la persona.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Eduardo viu o forastero ontem. Pra contar (sobre ELE):",
                    "options": [
                        {"id": "a", "text": "Eduardo vio al forastero"},
                        {"id": "b", "text": "Eduardo vi al forastero"},
                        {"id": "c", "text": "Eduardo viste al forastero"},
                        {"id": "d", "text": "Eduardo ve al forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_vio", "target": "vio", "native": "viu (ele/ela)",
                    "npc_reaction": "Vio â€” Ã©l, ella. Como 'va' cuando algo sale, pero del pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a testa: 'Forastero â€” Â¿tÃº me viste con Carmen anoche?' Pra vocÃª responder que sim, vocÃª viu:",
                    "options": [
                        {"id": "a", "text": "SÃ­, te vi"},
                        {"id": "b", "text": "SÃ­, te veo"},
                        {"id": "c", "text": "SÃ­, voy a verte"},
                        {"id": "d", "text": "SÃ­, soy verte"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Igual que Eduardo usÃ³. Lo entendiste rÃ¡pido.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Tarde. Voltando pra casa. Conversa do grupo. MarÃ­a aparece finalmente
    # â€” calada. NÃ£o quer falar do Alcalde. Foco em REVISÃƒO ORGÃ‚NICA F1-F11.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Miguel", "SofÃ­a", "MarÃ­a"],
                "story": (
                    "VocÃªs voltam pra casa de Don Miguel ao fim da tarde. "
                    "Dois testigos garantidos: Carmen e Eduardo. Falta um.\n\n"
                    "MarÃ­a estava esperando na porta. Cabelo preso, vestido "
                    "diferente â€” mais formal. NÃ£o disse nada sobre ontem."
                ),
                "now": "ReuniÃ£o Ã  mesa. MarÃ­a quieta. VocÃª tenta entender.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ… Casa de Don Miguel Â· Fim de tarde Â· Os cinco em volta da mesa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Hoy hablamos con Carmen y con Eduardo. Los dos aceptan. MarÃ­a â€” Â¿y tÃº? Â¿QuÃ© pasÃ³ ayer con el Alcalde?",
                    "translation": "Hoje falamos com Carmen e com Eduardo. Os dois aceitam. MarÃ­a â€” e vocÃª? O que aconteceu ontem com o Alcalde?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "HablÃ© con Ã©l. Le contÃ© lo que necesitaba saber. Eso es todo.",
                    "translation": "Falei com ele. Contei o que ele precisava saber. Isso Ã© tudo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a disse 'hablÃ© con Ã©l' â€” confirmou que falou. VocÃª comenta com SofÃ­a baixinho que ouviu MarÃ­a falar isso:",
                    "options": [
                        {"id": "a", "text": "SÃ­, la oÃ­ decir eso"},
                        {"id": "b", "text": "SÃ­, la oigo"},
                        {"id": "c", "text": "Voy a oÃ­r"},
                        {"id": "d", "text": "Soy oÃ­r"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                    "npc_reaction": "OÃ­. Yo oÃ­ â€” ya pasÃ³. La 'Ã­' con acento, como Eduardo te enseÃ±Ã³.",
                },
                {
                    "kind": "narrative",
                    "text": "SofÃ­a olha pra vocÃª por um segundo. Miguel nÃ£o levanta os olhos do prato. MarÃ­a continua serena.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "MarÃ­a â€” Â¿el Vigilante estuvo allÃ­ cuando hablaste con Ã©l?",
                    "translation": "MarÃ­a â€” El Vigilante estava lÃ¡ quando vocÃª falou com ele?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "No. Solo estuvimos los dos. Yo y Ã©l.",
                    "translation": "NÃ£o. SÃ³ estÃ¡vamos os dois. Eu e ele.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel pergunta pra vocÃª: 'Forastero â€” Â¿cÃ³mo estÃ¡s con todo esto?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien, pero tengo miedo"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Vamos bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Las dos cosas a la vez â€” estado bien, sensaciÃ³n miedo. Eso es ser humano.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Falta uno mÃ¡s. Â¿En quiÃ©n pensamos?",
                    "translation": "Falta mais um. Em quem pensamos?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a sugere: 'Rosa te vio el primer dÃ­a'. VocÃª concorda. SofÃ­a sai pra falar com Rosa â€” pra dizer o que ELA vai fazer (jÃ¡ saindo agora):",
                    "options": [
                        {"id": "a", "text": "Voy a buscar a Rosa"},
                        {"id": "b", "text": "Vamos a buscar a Rosa"},
                        {"id": "c", "text": "Vas a buscar"},
                        {"id": "d", "text": "Soy buscar"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a", "native": "vou (algo logo)",
                    "npc_reaction": "Voy a â€” yo, ahora. SofÃ­a nunca pierde tiempo.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Noite. VÃ£o atrÃ¡s do terceiro testigo. Rosa la Panadera â€” quem viu o
    # forastero no primeiro dia. Chegam na padaria. Rosa hesita. Tem medo.
    # Gate: errar trava. Closing prepara F13.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Miguel", "Don Miguel"],
                "story": (
                    "Ã€ noite, SofÃ­a: 'Rosa la Panadera te vio el primer dÃ­a. "
                    "Si alguien tiene memoria exacta de tu llegada, es ella.'\n\n"
                    "SaÃ­ram os quatro. MarÃ­a ficou em casa â€” disse que precisava "
                    "descansar. VocÃªs andam trÃªs quadras atÃ© a padaria de Rosa. "
                    "Luz acesa lÃ¡ dentro â€” estÃ¡ fechando o forno."
                ),
                "now": "Convencer Rosa. Errar trava â€” palavras certas, situaÃ§Ã£o real.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ™ Padaria de Rosa Â· Noite Â· Forno apagado Â· Luz baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Â¡Hijos! Â¿A esta hora? Â¿PasÃ³ algo?",
                    "translation": "Filhos! A essa hora? Aconteceu alguma coisa?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa abriu a porta preocupada. Sol jÃ¡ se pÃ´s. VocÃª cumprimenta calmo:",
                    "options": [
                        {"id": "a", "text": "Buenas noches, Rosa"},
                        {"id": "b", "text": "Buenos dÃ­as"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                    "npc_reaction": "Buenas noches, hijo. Entren â€” la noche estÃ¡ frÃ­a.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Rosa â€” necesitamos algo. El Alcalde pide testigos del forastero. TÃº lo viste el primer dÃ­a.",
                    "translation": "Rosa â€” a gente precisa de algo. O Alcalde pede testigos do forasteiro. VocÃª viu ele no primeiro dia.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "...El Alcalde. Mmm.",
                    "translation": "...O Alcalde. Mmm.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Rosa olha pra porta da frente â€” fechada, mas ela checa de "
                        "novo. Tem medo. VocÃª consegue ver."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Yo te vi ese dÃ­a, joven. Llegaste perdido. Yo te ofrecÃ­ pan â€” y al dÃ­a siguiente te lo di gratis.",
                    "translation": "Eu te vi naquele dia, jovem. VocÃª chegou perdido. Eu te ofereci pÃ£o â€” e no dia seguinte te dei de graÃ§a.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa lembra de tudo. Pra confirmar que VOCÃŠ TAMBÃ‰M lembra dela te dando pÃ£o (vocÃª viu Rosa):",
                    "options": [
                        {"id": "a", "text": "SÃ­, te vi"},
                        {"id": "b", "text": "SÃ­, te veo"},
                        {"id": "c", "text": "Voy a verte"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Te vi. SÃ­ â€” y yo te vi a ti. Eso ya es suficiente.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Rosa â€” Â¿vas a testificar maÃ±ana o pasado maÃ±ana?",
                    "translation": "Rosa â€” vocÃª vai testemunhar amanhÃ£ ou depois de amanhÃ£?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Rosa olha pro chÃ£o. Pra Don Miguel. Pra SofÃ­a. Pra vocÃª. "
                        "Pensa. Pensa muito tempo."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Voy a hacerlo. Pero quiero ir el primero dÃ­a â€” antes que el Vigilante se entere. MaÃ±ana mismo.",
                    "translation": "Vou fazer. Mas quero ir no primeiro dia â€” antes do Vigilante saber. AmanhÃ£ mesmo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa aceitou com coragem. VocÃª agradece formal:",
                    "options": [
                        {"id": "a", "text": "Gracias, Rosa"},
                        {"id": "b", "text": "AdiÃ³s Rosa"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, joven. Lo hago por Don Miguel â€” y porque te vi llegar perdido. Eso pesa.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel propÃµe ao grupo o que VAMOS fazer amanhÃ£ cedo (todos juntos):",
                    "options": [
                        {"id": "a", "text": "Vamos al ayuntamiento maÃ±ana"},
                        {"id": "b", "text": "Voy al ayuntamiento maÃ±ana"},
                        {"id": "c", "text": "Va al ayuntamiento"},
                        {"id": "d", "text": "Soy ayuntamiento"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos â€” los siete. Tres testigos, los cuatro nuestros. MaÃ±ana al amanecer.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F13 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸŒƒ Saindo da padaria Â· Rua escura Â· Os quatro caminhando",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Tres testigos. MaÃ±ana al ayuntamiento. Pero esta noche â€” mejor que durmamos en casa de mi madre. MÃ¡s lejos, mÃ¡s seguro.",
                    "translation": "TrÃªs testigos. AmanhÃ£ no ayuntamiento. Mas essa noite â€” melhor dormir na casa da minha mÃ£e. Mais longe, mais seguro.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel concorda com a cabeÃ§a. SofÃ­a corre na frente "
                        "pra avisar MarÃ­a. VocÃª caminha com Miguel pelo lado mais "
                        "escuro da rua.\n\n"
                        "'MaÃ±ana vas a conocer a mi madre. Y a mis hermanas.'"
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
