"""
Seed das 6 seÃ§Ãµes da Fase 10 Espanhol A1 â€” "La sombra del Vigilante".

Fechamento do mini-arco F6-F10. NÃ£o hÃ¡ milestone interno do grupo â€”
mas planta o gancho temÃ¡tico da T1 inteira: a hostilidade institucional
do pueblo. El Vigilante reaparece como ameaÃ§a funcional â€” pista para o
boss da T1 (El Alcalde / El Jefe del Pueblo).

SequÃªncia: amanhecer cedo. Grupo decidiu na noite anterior ir falar com
o Alcalde. No caminho, El Vigilante bloqueia uma rua estreita. Pede o
"pase de forastero". O protagonista nÃ£o tem. El Vigilante diz que sem
pase, sai do pueblo atÃ© o pÃ´r do sol. Miguel grita. SofÃ­a aparece de
outra esquina com MarÃ­a. MarÃ­a se aproxima de El Vigilante e fala trÃªs
frases baixinho â€” o jogador nÃ£o escuta. El Vigilante recua, lanÃ§a um
olhar duro pro protagonista, vai embora. Miguel olha pra MarÃ­a. MarÃ­a
sorri: "Conocidos antiguos. No te preocupes." â€” primeira pista DIRETA
pro jogador (nÃ£o pros personagens) de que MarÃ­a tem ligaÃ§Ãµes que
ninguÃ©m imagina.

Ã€ noite, Don Miguel diz que o pase sÃ³ Ã© dado pelo Alcalde â€” e que isso
vai ser um problema.

Novos vocab (2-3): pase Â· alcalde Â· ven/para/mira (imperativo simples)
GramÃ¡tica nova: 1. Imperativo simples (ven, para, mira, habla) â€” ecoa o
                   que El Vigilante usa pra dar ordens
                2. ExpansÃ£o do paradigma IR â€” F6 ensinou yo voy / tÃº vienes /
                   Ã©l Â· ella va. F10 fecha com NOSOTROS VAMOS e ELLOS VAN
                   (grupo se locomove pro ayuntamiento)
RevisÃ£o F1-F9:  saudaÃ§Ãµes, Â¿cÃ³mo estÃ¡s?, me llamo, tengo X aÃ±os,
                no me gusta, hay, yo voy, lugares (calle, plaza, fuente)
NPC principais: Os 4 do grupo Â· Don Miguel Â· El Vigilante (antagonista)
Arco emocional: falsa seguranÃ§a (F9) â†’ ameaÃ§a institucional explÃ­cita
                â†’ identificaÃ§Ã£o do antagonista da temporada
TransiÃ§Ã£o:      F11 abre na manhÃ£ seguinte com o grupo decidindo
                ir pedir o pase ao Alcalde. ComeÃ§a a estrada
                que termina no boss da T1.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f10_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Amanhecer. O grupo se prepara em silÃªncio. Don Miguel passa as
    # instruÃ§Ãµes. Os quatro saem. Pelo caminho, encontram a primeira
    # tensÃ£o da manhÃ£. ImersÃ£o â€” falas sem traduÃ§Ã£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ„ Amanhecer cedo Â· Casa de Don Miguel Â· Mesa baixa de madeira\n\n"
                        "O cÃ©u ainda escuro pelas frestas. Lamparina baixa. Os quatro "
                        "sentados em volta da mesa, junto com Don Miguel. PÃ£o da "
                        "noite anterior, cafÃ© morno. NinguÃ©m com fome de verdade."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Hoy van al ayuntamiento. El Alcalde da el pase a los forasteros â€” sin pase, hay problema.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "El Vigilante ya escalÃ³ esto. Si te encuentran sin pase, te sacan del pueblo. Por eso vamos temprano.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª ouve as palavras 'pase' e 'Alcalde' pela primeira vez. NÃ£o sabe exatamente o que sÃ£o â€” mas pelo tom, sÃ£o portas.",
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "Â¿Y si el Alcalde se niega? Â¿QuÃ© hacemos?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Eso lo vemos cuando lleguemos. Una cosa a la vez.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a come metade do pÃ£o em silÃªncio. NÃ£o estÃ¡ preocupada â€” estÃ¡ pensando.",
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Vamos juntos. Si paran al forastero â€” paran a los cuatro.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸŒ«ï¸ Rua deserta Â· Primeira luz azulada Â· VocÃªs saem pela porta",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs quatro andam pela rua principal, sem pressa mas "
                        "sem parar. MarÃ­a lidera â€” passos certos como se jÃ¡ "
                        "soubesse o caminho. SofÃ­a do seu lado. Miguel atrÃ¡s "
                        "vigiando atrÃ¡s."
                    ),
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "pase",     "native": "passe / permissÃ£o"},
                        {"target": "alcalde",  "native": "alcaide / prefeito (a maior autoridade do pueblo)"},
                        {"target": "ayuntamiento", "native": "cÃ¢mara / prefeitura"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel acabou de explicar que o forastero precisa de um documento pra ficar no pueblo. Como esse documento se chama?",
                    "options": [
                        {"id": "a", "text": "Pase"},
                        {"id": "b", "text": "LÃ¡mpara"},
                        {"id": "c", "text": "Naranja"},
                        {"id": "d", "text": "MaÃ±ana"},
                    ],
                    "correct": "a",
                    "word_id": "es_pase", "target": "pase", "native": "passe",
                    "npc_reaction": "Pase. Un papel con sello. Sin Ã©l no eres legal aquÃ­.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Quem dÃ¡ o pase no pueblo? A maior autoridade polÃ­tica â€” se chama:",
                    "options": [
                        {"id": "a", "text": "Alcalde"},
                        {"id": "b", "text": "Campesino"},
                        {"id": "c", "text": "Mercader"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_alcalde", "target": "alcalde", "native": "alcaide / prefeito",
                    "npc_reaction": "Alcalde. Hombre polÃ­tico. Vamos a tener que tratarlo con respeto â€” y con cuidado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel olha pra vocÃª caminhando. 'Forastero â€” Â¿estÃ¡s listo para esto?' VocÃª responde com honestidade:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vale. Si caminas con miedo, lo escondes. Si caminas con calma, ganas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pra esquina que dobra na rua estreita. 'Por aquÃ­ es mÃ¡s rÃ¡pido. Â¿TÃº vienes?' VocÃª confirma:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy"},
                        {"id": "b", "text": "No tengo hambre"},
                        {"id": "c", "text": "AdiÃ³s SofÃ­a"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vamos. La calle estrecha pasa cerca del ayuntamiento.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Caminho atÃ© o ayuntamiento. RevisÃ£o pesada â€” saudaÃ§Ãµes, estado fÃ­sico,
    # vizinhos que cumprimentam, MarÃ­a testando enquanto caminha. F1-F9.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "VocÃªs cortaram caminho pela rua estreita. Pedras desniveladas, "
                    "vasos de barro nas janelas. Algumas pessoas jÃ¡ abrindo "
                    "lojas â€” saudaÃ§Ãµes trocadas pelos cantos.\n\n"
                    "MarÃ­a se vira pra vocÃª enquanto andam. 'Mientras llegamos â€” "
                    "repaso. Si te paran, no quiero que tartamudees.'"
                ),
                "now": "MarÃ­a testa rapidamente F1-F9 â€” saudaÃ§Ãµes, identidade, idade.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Primero â€” si te paran y te preguntan tu nombre. Â¿QuÃ© dices?",
                    "translation": "Primeiro â€” se te param e te perguntam seu nome. O que vocÃª fala?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Pergunta direta: 'Me llamo + nome'. VocÃª responde com seu nome:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo veinte aÃ±os"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Bueno. Sin titubear. Tu nombre es tuyo â€” di que es tuyo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Si te preguntan tu edad â€” Â¿quÃ© dices?",
                    "translation": "Se te perguntam sua idade â€” o que vocÃª fala?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "A idade Ã© fÃ¡cil â€” vocÃª tem vinte. Resposta correta Ã©:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Me llamo veinte"},
                        {"id": "d", "text": "Estoy veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Hombre joven, no niÃ±o. Eso le importa al Alcalde.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Antes de seguir â€” Â¿cÃ³mo estÃ¡ la cabeza hoy?",
                    "translation": "Antes de continuar â€” como estÃ¡ a cabeÃ§a hoje?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª dormiu bem, sem febre. A cabeÃ§a tÃ¡ clara. VocÃª responde com a palavra de F8:",
                    "options": [
                        {"id": "a", "text": "Estoy mejor"},
                        {"id": "b", "text": "Tengo fiebre"},
                        {"id": "c", "text": "Estoy enfermo"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Bueno. Hoy necesitamos esa cabeza despejada.",
                },
                {
                    "kind": "narrative",
                    "text": "Uma vizinha abre a janela do segundo andar pra estender lenÃ§Ã³is. Cumprimenta vocÃªs.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Vecina",
                    "line": "Â¡Buenos dÃ­as, MarÃ­a! Â¡Y los jÃ³venes!",
                    "translation": "Bom dia, MarÃ­a! E os jovens!",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecina",
                    "question": "A vizinha cumprimenta de manhÃ£ cedo. VocÃª responde do mesmo jeito:",
                    "options": [
                        {"id": "a", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "b", "text": "Â¡Buenas tardes!"},
                        {"id": "c", "text": "Â¡Buenas noches!"},
                        {"id": "d", "text": "Â¡AdiÃ³s!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Eso. Si gentes te ven cumpliendo el saludo, te suman â€” no te restan.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Mira esa casa allÃ¡ â€” la de las macetas rojas. Es de un vecino mÃ­o. Â¿CÃ³mo lo describes?",
                    "translation": "Olha aquela casa ali â€” a dos vasos vermelhos. Ã‰ de um vizinho meu. Como vocÃª descreve?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a espera que vocÃª junte 'hay' (tem) + objeto. 'Hay flores rojas allÃ­.' Mas pra falar sobre o dono, como vocÃª diz que Ã© um vizinho?",
                    "options": [
                        {"id": "a", "text": "Es un vecino"},
                        {"id": "b", "text": "Tengo vecino"},
                        {"id": "c", "text": "Soy vecino"},
                        {"id": "d", "text": "Me llamo vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_vecino", "target": "vecino", "native": "vizinho",
                    "npc_reaction": "Eso. Cada casa tiene su gente. AquÃ­ nadie es anÃ³nimo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿CÃ³mo te sientes ahora? Estamos por llegar a la plaza grande.",
                    "translation": "Como vocÃª se sente agora? Tamos quase chegando na plaza grande.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª sente nervosismo â€” mas pelo menos nÃ£o tem febre nem dor. VocÃª estÃ¡... funcional. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Estoy bien"},
                        {"id": "b", "text": "Estoy mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Si necesitas decir 'tengo miedo', dilo â€” pero no hace falta esconderlo bajo 'mal'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero â€” Â¿te gusta caminar por este pueblo? DespuÃ©s de todo lo que vivimos.",
                    "translation": "Forasteiro â€” vocÃª gosta de caminhar por esse pueblo? Depois de tudo que a gente viveu.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "VocÃª gosta â€” apesar de tudo. As ruas, os cheiros, as pessoas. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me gusta"},
                        {"id": "b", "text": "No me gusta"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Bueno. Ya es 'tu' pueblo tambiÃ©n â€” aunque no quiera el Vigilante.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # CONFRONTO. El Vigilante bloqueia a rua estreita. Exige o pase. Cada
    # exercÃ­cio Ã© uma fala dele â€” gated quando crÃ­tico. TensÃ£o alta, ritmo
    # rÃ¡pido. MarÃ­a intervÃ©m no final. Falas de Vigilante autoritÃ¡rias.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "VocÃªs dobraram a esquina pra outra rua. Estreita, paredes "
                    "altas de adobe nos dois lados. No fundo â€” uma silhueta no "
                    "meio do caminho. ChapÃ©u baixo. Casaco escuro.\n\n"
                    "El Vigilante del Mercado bloqueia a passagem."
                ),
                "now": "Confronto. Cada palavra importa. Errar trava â€” vocÃª tem que se sair.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸ‘¤ El Vigilante Â· Meio da rua Â· Sem desviar",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Para. No avancen mÃ¡s.",
                    "translation": "Para. NÃ£o avancem mais.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "MarÃ­a estende o braÃ§o pra trÃ¡s â€” gesto de parar SofÃ­a e vocÃª. Miguel se posiciona meio passo Ã  frente de MarÃ­a.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Ustedes â€” yo no quiero problema. SÃ³lo el forastero. Forastero â€” ven aquÃ­.",
                    "translation": "VocÃªs â€” eu nÃ£o quero problema. SÃ³ o forasteiro. Forasteiro â€” vem aqui.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": "Ele te chama. VocÃª precisa cumprimentar primeiro pra ganhar tempo â€” formal, sem provocaÃ§Ã£o:",
                    "options": [
                        {"id": "a", "text": "Buenos dÃ­as, seÃ±or"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "El Vigilante mira con desprecio. 'Buenos dÃ­as no me cubre la espalda. Â¿Tienes el pase?'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Â¿CÃ³mo te llamas, forastero?",
                    "translation": "Como vocÃª se chama, forasteiro?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": "Pergunta direta. Mentir agora seria pior. VocÃª responde claro:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "No tengo nombre"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Anotado. Â¿CuÃ¡ntos aÃ±os tienes?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": "El Vigilante quer sua idade â€” exata. Vinte anos:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "No me acuerdo"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Edad de servir o de huir. Â¿De dÃ³nde vienes?",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Â¿De dÃ³nde vienes? Habla.",
                    "translation": "De onde vocÃª vem? Fala.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "El Vigilante",
                    "question": "VocÃª nÃ£o lembra. Mentir agora seria pego. A verdade pode ajudar â€” vocÃª nÃ£o tem nada a esconder mesmo:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo. Soy forastero."},
                        {"id": "b", "text": "Soy del pueblo"},
                        {"id": "c", "text": "Tengo veinte aÃ±os"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "El Vigilante levanta una ceja. 'Conveniente. Â¿Tienes el pase o no?'",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Sin pase del Alcalde, sales del pueblo antes del atardecer. Es la ley.",
                    "translation": "Sem pase do Alcalde, vocÃª sai do pueblo antes do entardecer. Ã‰ a lei.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Vamos ahora mismo al ayuntamiento. Lo estamos llevando.",
                    "translation": "Vamos agora mesmo na prefeitura. Tamos levando ele.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "Conmigo. Yo lo llevo.",
                    "translation": "Comigo. Eu levo ele.",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "VocÃª sente o ar virar pesado. MarÃ­a dÃ¡ um passo Ã  frente â€” nÃ£o rÃ¡pido, mas firme. SofÃ­a aperta o seu braÃ§o atrÃ¡s.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Vigilante â€” un momento.",
                    "translation": "Vigilante â€” um momento.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "MarÃ­a passa do lado de Miguel e se aproxima de El Vigilante "
                        "a passos curtos. Para a um metro dele. Fala trÃªs frases "
                        "baixinho â€” voz tÃ£o baixa que ninguÃ©m do grupo escuta.\n\n"
                        "El Vigilante muda a expressÃ£o. A primeira coisa Ã© "
                        "surpresa. Depois alguma coisa mais difÃ­cil de nomear â€” "
                        "respeito? medo? cÃ¡lculo?\n\n"
                        "Ele recua meio passo."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "El Vigilante",
                    "line": "...MaÃ±ana. Si no hay pase maÃ±ana â€” lo busco yo mismo.",
                    "translation": "...AmanhÃ£. Se nÃ£o tiver pase amanhÃ£ â€” eu mesmo procuro ele.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "El Vigilante lanÃ§a um olhar duro pra vocÃª. Vira. Vai embora pela rua. MarÃ­a nÃ£o se vira pra ver ele sair â€” espera que os passos sumam.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a vira pro grupo. 'Vamos a la fuente. Necesitamos sentarnos un momento.' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s MarÃ­a"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Sigan caminando como si nada. Esta calle todavÃ­a tiene ojos.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel, baixo, do seu lado enquanto caminham: 'Forastero â€” Â¿estÃ¡s bien?' VocÃª responde verdade â€” nÃ£o tÃ¡ 100%, mas tÃ¡:",
                    "options": [
                        {"id": "a", "text": "Mejor que hace cinco minutos"},
                        {"id": "b", "text": "Tengo veinte aÃ±os"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Soy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Lo creo. Aguanta hasta la fuente.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Na fonte da plaza. MarÃ­a ensina o imperativo â€” porque o protagonista
    # acabou de ouvir El Vigilante usando: 'Para', 'Habla', 'Ven aquÃ­'.
    # Ela quer que ele reconheÃ§a quando alguÃ©m dÃ¡ ordem.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "VocÃªs chegaram Ã  fonte de pedra do centro da plaza. MarÃ­a "
                    "se senta na beira. SofÃ­a bebe Ã¡gua com as mÃ£os. Miguel fica "
                    "de pÃ© olhando ao redor.\n\n"
                    "MarÃ­a: 'Ya viste cÃ³mo te hablÃ³ El Vigilante? Todas las "
                    "palabras eran cortas. Ã“rdenes. Eso es importante que "
                    "reconozcas.'"
                ),
                "now": "MarÃ­a vai te ensinar imperativo â€” como ouvir ordens e dar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "El Vigilante dijo 'para', 'habla', 'ven aquÃ­'. Esas son Ã³rdenes. Cortas, directas. Sin 'por favor'.",
                    "translation": "El Vigilante disse 'para', 'fala', 'vem aqui'. Essas sÃ£o ordens. Curtas, diretas. Sem 'por favor'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ven aquÃ­",
                    "meaning": "Vem aqui",
                    "note": "ordem de movimento â€” do verbo 'venir'",
                },
                {
                    "kind": "reveal",
                    "phrase": "Para",
                    "meaning": "Para (de parar)",
                    "note": "ordem pra parar de fazer algo â€” uma das mais comuns",
                },
                {
                    "kind": "reveal",
                    "phrase": "Mira",
                    "meaning": "Olha",
                    "note": "chamar a atenÃ§Ã£o pra alguma coisa â€” 'mira' Ã© amigÃ¡vel OU autoritÃ¡rio pelo tom",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Ven",   "isKey": True},
                        {"text": " / ",   "isKey": False},
                        {"text": "Para",  "isKey": True},
                        {"text": " / ",   "isKey": False},
                        {"text": "Mira",  "isKey": True},
                        {"text": " / ",   "isKey": False},
                        {"text": "Habla", "isKey": True},
                    ],
                    "example": "â€” Para. Mira. Habla. Ven.",
                    "translation": "â€” Para. Olha. Fala. Vem.",
                    "note": "imperativo informal â€” quem dÃ¡ ordem usa estas formas curtas",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "El Vigilante usou esta palavra quando vocÃªs se aproximaram. 'No avancen mÃ¡s.' A palavra curta dele foi:",
                    "options": [
                        {"id": "a", "text": "Para"},
                        {"id": "b", "text": "Ven"},
                        {"id": "c", "text": "Mira"},
                        {"id": "d", "text": "Habla"},
                    ],
                    "correct": "a",
                    "word_id": "es_para", "target": "para", "native": "para",
                    "npc_reaction": "Para. Es para detener un movimiento. Reconoce esa palabra siempre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Depois ele te chamou: 'Forastero â€” ___ aquÃ­'. A palavra de chamada foi:",
                    "options": [
                        {"id": "a", "text": "Ven"},
                        {"id": "b", "text": "Para"},
                        {"id": "c", "text": "Mira"},
                        {"id": "d", "text": "Habla"},
                    ],
                    "correct": "a",
                    "word_id": "es_ven", "target": "ven", "native": "vem",
                    "npc_reaction": "Ven. Movimiento hacia el que habla. Cuando alguien te dice 'ven' â€” decide rÃ¡pido si vas o no.",
                },
                {
                    "kind": "narrative",
                    "text": "SofÃ­a senta do lado de MarÃ­a na beira da fonte. Olha pra vocÃª atenta â€” quer ver se vocÃª tÃ¡ pegando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Y si yo quiero que tÃº mires algo importante â€” te digo:",
                    "translation": "E se eu quero que vocÃª olhe alguma coisa importante â€” eu digo:",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta pra um pombo na fonte. 'Forastero â€” ___' â€” a palavra pra chamar sua atenÃ§Ã£o Ã©:",
                    "options": [
                        {"id": "a", "text": "Mira"},
                        {"id": "b", "text": "Ven"},
                        {"id": "c", "text": "Para"},
                        {"id": "d", "text": "Habla"},
                    ],
                    "correct": "a",
                    "word_id": "es_mira", "target": "mira", "native": "olha",
                    "npc_reaction": "Mira. Se usa para seÃ±alar â€” entre amigos, entre extraÃ±os, en cualquier sitio.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel se levanta da beira da fonte, sacode a poeira da calÃ§a. Olha pros trÃªs e diz uma palavra sÃ³, decidida.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Bueno â€” vamos. Los cuatro. Yo voy delante, MarÃ­a atrÃ¡s, SofÃ­a y el forastero en medio.",
                    "translation": "Bom â€” vamos. Os quatro. Eu vou na frente, MarÃ­a atrÃ¡s, SofÃ­a e o forasteiro no meio.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Vamos / vais / van",
                    "meaning": "NÃ³s vamos / vocÃªs vÃ£o / eles vÃ£o",
                    "note": "expansÃ£o de 'yo voy / tÃº vienes' (F6). Quando o grupo se move: vamos. Quando outros se movem: van.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo voy", "isKey": True},
                        {"text": " Â· ",    "isKey": False},
                        {"text": "TÃº vas", "isKey": True},
                        {"text": " Â· ",    "isKey": False},
                        {"text": "Ella va","isKey": True},
                        {"text": " Â· ",    "isKey": False},
                        {"text": "Nosotros vamos", "isKey": True},
                        {"text": " Â· ",    "isKey": False},
                        {"text": "Ellos van",      "isKey": True},
                    ],
                    "example": "Yo voy a la fuente. TÃº vas conmigo. Ella va detrÃ¡s. Nosotros vamos juntos. Los vecinos van por otra calle.",
                    "translation": "Eu vou Ã  fonte. Tu vais comigo. Ela vai atrÃ¡s. NÃ³s vamos juntos. Os vizinhos vÃ£o por outra rua.",
                    "note": "MESMO verbo (IR) â€” muda com quem faz: yo / tÃº / Ã©l Â· ella / nosotros / ellos",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel quer confirmar que vÃ£o JUNTOS. 'Los cuatro â€” ___ al ayuntamiento maÃ±ana.' A palavra do verbo IR para 'nÃ³s' Ã©:",
                    "options": [
                        {"id": "a", "text": "vamos"},
                        {"id": "b", "text": "voy"},
                        {"id": "c", "text": "vas"},
                        {"id": "d", "text": "va"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos", "target": "nosotros vamos", "native": "nÃ³s vamos",
                    "npc_reaction": "Vamos. Cuando es el grupo, no eres tÃº solo â€” 'vamos'. Nunca 'yo vamos'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Uns vizinhos passam do outro lado da plaza indo pro mercado. Como SofÃ­a descreve o que eles fazem? 'Ellos ___ al mercado.'",
                    "options": [
                        {"id": "a", "text": "van"},
                        {"id": "b", "text": "vamos"},
                        {"id": "c", "text": "voy"},
                        {"id": "d", "text": "vas"},
                    ],
                    "correct": "a",
                    "word_id": "es_van", "target": "ellos van", "native": "eles vÃ£o",
                    "npc_reaction": "Van. Otros â€” 'ellos van'. La forma cambia con la gente, no contigo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Y si vienes a buscarme y no sabes dÃ³nde estoy â€” pregÃºntame con voz fuerte: 'MarÃ­a â€” Â¿dÃ³nde estÃ¡s?'",
                    "translation": "E se vocÃª vem me buscar e nÃ£o sabe onde estou â€” me pergunta com voz forte: 'MarÃ­a â€” onde vocÃª estÃ¡?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a explica que perguntar onde alguÃ©m estÃ¡ Ã© simples. A pergunta Ã©:",
                    "options": [
                        {"id": "a", "text": "Â¿DÃ³nde estÃ¡s?"},
                        {"id": "b", "text": "Â¿CÃ³mo estÃ¡s?"},
                        {"id": "c", "text": "Â¿CuÃ¡ntos aÃ±os?"},
                        {"id": "d", "text": "Â¿TÃº vienes?"},
                    ],
                    "correct": "a",
                    "word_id": "es_donde_estas", "target": "Â¿dÃ³nde estÃ¡s?", "native": "onde vocÃª estÃ¡?",
                    "npc_reaction": "Eso. Si gritas 'Â¿dÃ³nde estÃ¡s?' en este pueblo, alguien te responde. Te lo prometo.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # De volta pra casa de Don Miguel. Tarde. Don Miguel ouve o relato.
    # DecisÃ£o sobre o que fazer amanhÃ£ com o Alcalde. MarÃ­a sutilmente
    # se posiciona â€” confiÃ¡vel, calma, indispensÃ¡vel. Poucos exercÃ­cios,
    # foco em dinÃ¢mica de grupo e tensÃ£o.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel", "Don Miguel"],
                "story": (
                    "VocÃªs voltaram pra casa de Don Miguel sem ir ao ayuntamiento "
                    "hoje. MarÃ­a decidiu: 'MaÃ±ana â€” con calma, no con sustos.' "
                    "Don Miguel jÃ¡ estava esperando â€” Carmen tinha mandado um "
                    "recado.\n\n"
                    "Agora os cinco sentados em volta da mesa, tarde caindo. "
                    "MarÃ­a contando a Don Miguel o que aconteceu â€” em espanhol "
                    "lento, palavra por palavra."
                ),
                "now": "DecisÃ£o do grupo sobre como abordar o Alcalde amanhÃ£.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ‡ Tarde Â· Casa de Don Miguel Â· Cinco em volta da mesa baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "MarÃ­a â€” me contaste todo. Pero hay algo que no me contaste. Â¿QuÃ© le dijiste al Vigilante para que se fuera?",
                    "translation": "MarÃ­a â€” vocÃª me contou tudo. Mas tem algo que nÃ£o me contou. O que vocÃª falou pro Vigilante pra ele ir embora?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a olha pra Don Miguel um momento mais longo que o normal. Pondera. Decide responder uma versÃ£o.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Lo conocÃ­ hace aÃ±os, antes de venir al pueblo. SÃ© cosas de Ã©l que Ã©l prefiere no recordar. Nada mÃ¡s.",
                    "translation": "Eu o conheci faz anos, antes de vir pro pueblo. Sei coisas dele que ele prefere nÃ£o lembrar. Nada mais.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "A resposta Ã© razoÃ¡vel. Don Miguel aceita. Mas Miguel â€” "
                        "do seu lado â€” nÃ£o acredita. VocÃª vÃª na cara dele. "
                        "Ele nÃ£o diz nada."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel se vira pra vocÃª. 'Forastero â€” maÃ±ana al amanecer vamos al ayuntamiento. Â¿TÃº vienes con calma?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Bueno. Pero esta vez vas tÃº adelante, no atrÃ¡s. El Alcalde tiene que verte la cara.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Yo voy tambiÃ©n. Y MarÃ­a. Y Miguel. Los cuatro al frente del Alcalde, no sÃ³lo el forastero.",
                    "translation": "Eu vou tambÃ©m. E MarÃ­a. E Miguel. Os quatro na frente do Alcalde, nÃ£o sÃ³ o forasteiro.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Cenamos algo simple â€” sobrÃ³ comida de ayer. Â¿Te gusta el guiso?",
                    "translation": "Jantamos algo simples â€” sobrou comida de ontem. VocÃª gosta de ensopado?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a coloca uma tigela na sua frente. Cheiro de ensopado quente. VocÃª prova â€” vocÃª gosta:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me gusta"},
                        {"id": "b", "text": "No tengo miedo"},
                        {"id": "c", "text": "Estoy enfermo"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Bueno. Necesitas energÃ­a. MaÃ±ana es dÃ­a largo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta 'Â¿CuÃ¡ndo vamos al ayuntamiento?'. Don Miguel responde com a palavra que indica o dia que vem:",
                    "options": [
                        {"id": "a", "text": "MaÃ±ana"},
                        {"id": "b", "text": "Hoy"},
                        {"id": "c", "text": "Ayer"},
                        {"id": "d", "text": "Vecino"},
                    ],
                    "correct": "a",
                    "word_id": "es_manana", "target": "maÃ±ana", "native": "amanhÃ£",
                    "npc_reaction": "MaÃ±ana al amanecer. Antes de que el pueblo despierte del todo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Mejor. El Alcalde respeta grupo mÃ¡s que solo. Pero hablar â€” habla el forastero.",
                    "translation": "Melhor. O Alcalde respeita grupo mais que sozinho. Mas falar â€” fala o forasteiro.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel quer que VOCÃŠ fale com o Alcalde â€” nÃ£o eles. VocÃª precisa aceitar a responsabilidade:",
                    "options": [
                        {"id": "a", "text": "Yo voy a hablar"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "No me gusta"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Bueno. Si tartamudeas, te corregimos en silencio. Pero la voz tiene que salir de ti.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Miguel se levanta da mesa. Vai atÃ© a janela. Olha pra rua "
                        "que jÃ¡ tÃ¡ escurecendo. NÃ£o diz nada por um tempo.\n\n"
                        "Volta. Senta. Olha pra MarÃ­a sem disfarÃ§ar."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "MarÃ­a â€” gracias. Por lo del Vigilante. No sÃ© quÃ© le dijiste pero funcionÃ³.",
                    "translation": "MarÃ­a â€” obrigado. Pelo que aconteceu com o Vigilante. NÃ£o sei o que vocÃª falou pra ele mas funcionou.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Miguel agradeceu â€” mas o tom nÃ£o foi 100% gratidÃ£o pura. MarÃ­a sorri sem pressa e responde:",
                    "options": [
                        {"id": "a", "text": "De nada, Miguel"},
                        {"id": "b", "text": "AdiÃ³s Miguel"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Para esto estoy. Y voy a estar maÃ±ana tambiÃ©n.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lamparina baixa. Don Miguel olha pra cada um deles em volta "
                        "da mesa. Para um momento em MarÃ­a. Outro em vocÃª. "
                        "NÃ£o decide nada â€” mas pensou em decidir alguma coisa."
                    ),
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Noite tarde. Don Miguel, MarÃ­a e Miguel saem pra organizar coisas pra
    # manhÃ£. VocÃª fica com SofÃ­a na sala. Conversa difÃ­cil sobre o que ela
    # viu â€” e o que ela acha que estÃ¡ acontecendo. Gate: errar trava.
    # TransiÃ§Ã£o direta pra F11.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel", "Don Miguel"],
                "story": (
                    "Don Miguel saiu pra ver dois vizinhos â€” pedir que servissem "
                    "de testemunha amanhÃ£. MarÃ­a saiu com ele â€” disse que precisa "
                    "ver algo na casa de hÃ³spedes. Miguel saiu atrÃ¡s dela 'para "
                    "ayudar', mas vocÃª sabe â€” ele tÃ¡ seguindo.\n\n"
                    "Sobrou vocÃª e SofÃ­a na sala. Ela fechou a porta da frente."
                ),
                "now": "Conversa difÃ­cil. Cada palavra importa. VocÃª precisa estar presente.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸ•¯ï¸ Sala Â· Noite Â· SofÃ­a sentada na cadeira em frente Â· Lamparina baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” necesito hablar contigo. Solos.",
                    "translation": "Forasteiro â€” preciso falar com vocÃª. Sozinhos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a parece sÃ©ria â€” diferente do jeito dela. VocÃª confirma que tÃ¡ ouvindo:",
                    "options": [
                        {"id": "a", "text": "SÃ­, te escucho"},
                        {"id": "b", "text": "No tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_si", "target": "sÃ­", "native": "sim",
                    "npc_reaction": "Bueno. Lo que voy a decirte â€” no se lo cuentes a nadie. Ni a Miguel.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "SofÃ­a olha pra porta â€” fechada. Pra janela â€” vazia. Volta pra vocÃª. Voz baixa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Yo vi lo que MarÃ­a le dijo al Vigilante. Estaba mÃ¡s cerca que ustedes.",
                    "translation": "Eu vi o que MarÃ­a falou pro Vigilante. Eu tava mais perto que vocÃªs.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª gela. SofÃ­a vai dizer alguma coisa que muda tudo. VocÃª nÃ£o sabe ainda se quer saber.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "No oÃ­ las palabras â€” pero leÃ­ la cara del Vigilante. Y conozco esa cara. Es la cara de quien recibe orden de un superior.",
                    "translation": "NÃ£o ouvi as palavras â€” mas li o rosto do Vigilante. E conheÃ§o esse rosto. Ã‰ o rosto de quem recebe ordem de um superior.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a espera vocÃª processar. A informaÃ§Ã£o Ã© pesada. VocÃª pergunta â€” em palavras que vocÃª tem:",
                    "options": [
                        {"id": "a", "text": "Â¿MarÃ­a es...?"},
                        {"id": "b", "text": "Estoy bien"},
                        {"id": "c", "text": "AdiÃ³s SofÃ­a"},
                        {"id": "d", "text": "Tengo veinte aÃ±os"},
                    ],
                    "correct": "a",
                    "word_id": "es_es", "target": "es", "native": "Ã©",
                    "npc_reaction": "No sÃ© quÃ© es. Pero no es sÃ³lo una curandera. Eso sÃ­.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Por eso te digo â€” no se lo cuentes a nadie. Ni a Miguel. Si Miguel sabe, va a hacer algo. Y si MarÃ­a descubre que sabemos â€” no sÃ© quÃ© hace.",
                    "translation": "Por isso te digo â€” nÃ£o conta pra ninguÃ©m. Nem pro Miguel. Se Miguel souber, ele vai fazer alguma coisa. E se MarÃ­a descobrir que sabemos â€” nÃ£o sei o que ela faz.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a precisa da sua promessa. VocÃª diz que entendeu, que vai guardar:",
                    "options": [
                        {"id": "a", "text": "No le digo a nadie"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "nÃ£o",
                    "npc_reaction": "Bueno. MaÃ±ana al ayuntamiento â€” todo normal. Como si nada. DespuÃ©s â€” los dos vigilamos.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸ‘ï¸ SofÃ­a olha pra porta. Passos vindo. MarÃ­a e Miguel voltando juntos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Como si nada, forastero. Mira normal â€” habla normal.",
                    "translation": "Como se nada. Olha normal â€” fala normal.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "A porta abre. MarÃ­a entra primeiro. Sorri ao ver vocÃªs "
                        "dois. 'Ya volvieron Don Miguel y los vecinos. MaÃ±ana al "
                        "amanecer vamos.'\n\n"
                        "Miguel vem atrÃ¡s. Olha pra SofÃ­a. Olha pra vocÃª. Pensa "
                        "em perguntar algo â€” mas nÃ£o pergunta."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a se aproxima de vocÃª normal â€” calorosa como sempre. 'Forastero â€” Â¿cÃ³mo estÃ¡s? Tienes que dormir temprano hoy.' VocÃª responde como se nada tivesse acontecido:",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "No me gusta"},
                        {"id": "d", "text": "AdiÃ³s MarÃ­a"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Voy a preparar una infusiÃ³n suave para que duermas profundo. MaÃ±ana es dÃ­a largo.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F11 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸŒ™ Casa silenciosa Â· Lamparina apagada Â· Quarto",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª deitou na cama com a infusÃ£o de MarÃ­a nas mÃ£os. "
                        "Olhou pro frasco por um longo tempo antes de tomar. "
                        "Aquele que ela tinha deixado na F8.\n\n"
                        "Tomou. NÃ£o tinha como recusar sem levantar suspeita. "
                        "O gosto era diferente esta noite â€” mais amargo. Ou era "
                        "a sua imaginaÃ§Ã£o."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "MaÃ±ana, forastero. MaÃ±ana.",
                    "translation": "AmanhÃ£, forasteiro. AmanhÃ£.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "SofÃ­a sussurrou da cadeira no canto onde ela dormiu de "
                        "novo â€” ela tinha avisado que ia ficar. VocÃª fechou os "
                        "olhos.\n\n"
                        "O sono veio rÃ¡pido. Sonho com mÃ£os de MarÃ­a na sua "
                        "testa. Com o rosto de El Vigilante recuando. Com a "
                        "palavra 'fuego' queimando atrÃ¡s dos olhos.\n\n"
                        "AmanhÃ£ â€” o Alcalde."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
