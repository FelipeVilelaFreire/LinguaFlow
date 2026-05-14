"""
Seed das 6 seÃ§Ãµes da Fase 8 Espanhol A1 â€” "La curandera".

âš ï¸ MILESTONE OBRIGATÃ“RIO (canÃ´nico â€” story.md, characters.md):
    MarÃ­a entra no grupo na F8. Ao tocar o protagonista (curando-o),
    reconhece a assinatura do dom roubado da famÃ­lia dela. Sabe quem ele
    Ã© desde este momento. **O protagonista nÃ£o percebe nada.**
    A janela de 3 meses agora tem alguÃ©m contando os dias por dentro.

SofÃ­a traz MarÃ­a Ã  casa de Don Miguel. MarÃ­a tem 24 anos, mÃ£os firmes,
olhar paciente. Examina o protagonista, prepara uma infusÃ£o amarga.
Quando pousa a mÃ£o na tÃªmpora dele, **a expressÃ£o muda por um segundo**.
RecompÃµe. Sorri. Pergunta o nome dele com uma doÃ§ura que sÃ³ o jogador
(que leu os docs) entende como predaÃ§Ã£o. Fica atÃ© a febre baixar.
Quando vai embora, Don Miguel oferece a casa de hÃ³spedes. MarÃ­a aceita.

REGRA NARRATIVA DA F8:
- O jogador NÃƒO deve saber ainda que MarÃ­a Ã© a VilÃ£. O reconhecimento dela
  acontece em UM beat ('expressÃ£o muda por um segundo') que pode passar
  despercebido na primeira jogada. Releitura revela.
- MarÃ­a fala apenas espanhol â€” sem portuguÃªs.
- O carinho dela Ã© genuÃ­no na superfÃ­cie. O cÃ¡lculo Ã© por baixo.

Novos vocab (3): cabeza Â· fiebre Â· manos  (+ enfermo, mejor, descansa)
GramÃ¡tica nova: TRIO CENTRAL DO ESPANHOL â€” MarÃ­a contrasta os 3 verbos
                que o protagonista jÃ¡ usava sem saber separar:
                Â· SOY  (identidad: soy forastero / yo soy MarÃ­a)
                Â· ESTOY (estado: estoy bien / estoy enfermo / estoy mejor)
                Â· TENGO (sensaciÃ³n + edad: tengo hambre / tengo veinte aÃ±os)
                TambÃ©m planta passado simple: 'estaba' como pasado de 'estoy'.
RevisÃ£o F1-F7:  hola, gracias, bien/mal, me llamo, tengo X aÃ±os,
                yo voy, tÃº vienes
NPC principais: MarÃ­a (entra no grupo) Â· SofÃ­a Â· Miguel Â· Don Miguel
Arco emocional: vulnerabilidade real â†’ cuidado recebido â†’ falsa seguranÃ§a
                (que o jogador vai depois entender como armadilha)
TransiÃ§Ã£o:      F9 abre na manhÃ£ seguinte com MarÃ­a jÃ¡ fazendo cafÃ© como
                se sempre tivesse morado ali.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f8_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # MarÃ­a chega. Examina. O toque revela o que ela jÃ¡ sabia procurar.
    # O beat do reconhecimento â€” 'expressÃ£o muda por um segundo' â€” estÃ¡ aqui.
    # Falas dela em espanhol, sem traduÃ§Ã£o. ImersÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸŒ™ Madrugada Â· Quarto Â· Febre alta\n\n"
                        "VocÃª acorda com vozes baixas na sala. SofÃ­a conversando "
                        "com alguÃ©m em espanhol rÃ¡pido. Miguel respondendo. "
                        "E uma terceira voz â€” feminina, calma, mais grave que "
                        "a de SofÃ­a. Uma voz que ouve antes de falar."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "AquÃ­ estÃ¡. Lleva horas con la fiebre subiendo.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "A porta do quarto abre devagar. SofÃ­a entra primeiro, depois alguÃ©m atrÃ¡s dela.",
                },
                {
                    "kind": "npc",
                    "npc": "MarÃ­a",
                    "line": "Buenas noches. Â¿Puedo acercarme?",
                    "is_new_npc": True,
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Uma mulher de uns 24 anos. Cabelo escuro preso atrÃ¡s. "
                        "MÃ£os com cicatrizes pequenas de quem trabalha com facas e "
                        "ervas. Olhos calmos â€” nÃ£o de quem Ã© calma. De quem aprendeu "
                        "a ser."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "MarÃ­a",
                    "line": "Soy MarÃ­a. SofÃ­a me llamÃ³. Voy a ver quÃ© tienes.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Ela se aproxima da cama devagar. Senta na beira, abre uma "
                        "bolsa de tecido â€” frascos pequenos, ervas secas amarradas "
                        "com barbante."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "MarÃ­a",
                    "line": "Voy a tocarte la frente. Sin susto, Â¿sÃ­?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Ela coloca a mÃ£o na sua testa. Pele fria. Firme.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Por um segundo â€” um Ãºnico segundo â€” a expressÃ£o de MarÃ­a muda. "
                        "Os olhos nÃ£o se movem mas algo passa pelo rosto. NÃ£o dor. "
                        "NÃ£o surpresa. Reconhecimento.\n\n"
                        "Ela recompÃµe antes que vocÃª termine de notar."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "MarÃ­a",
                    "line": "Fiebre alta. Pero el cuerpo estÃ¡ peleanÂ­do bien. Va a pasar.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "MarÃ­a",
                    "line": "Â¿CÃ³mo te llamas, forastero?",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "cabeza",  "native": "cabeÃ§a"},
                        {"target": "fiebre",  "native": "febre"},
                        {"target": "manos",   "native": "mÃ£os"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": (
                        "MarÃ­a espera. A pergunta Ã© simples â€” ela quer saber seu "
                        "nome com calma. VocÃª responde do jeito que sempre aprendeu:"
                    ),
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Mucho gusto. Yo soy MarÃ­a. Voy a cuidarte esta noche.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a pousa a mÃ£o na sua testa de novo. Pergunta o que estÃ¡ quente. A palavra Ã©:",
                    "options": [
                        {"id": "a", "text": "Cabeza"},
                        {"id": "b", "text": "Manos"},
                        {"id": "c", "text": "Fuego"},
                        {"id": "d", "text": "Luz"},
                    ],
                    "correct": "a",
                    "word_id": "es_cabeza", "target": "cabeza", "native": "cabeÃ§a",
                    "npc_reaction": "Cabeza. Caliente. Eso es la fiebre subiendo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Ela pÃµe um pano frio na sua testa pra baixar o que ela acabou de nomear. Como se chama o que vocÃª tem agora?",
                    "options": [
                        {"id": "a", "text": "Fiebre"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_fiebre", "target": "fiebre", "native": "febre",
                    "npc_reaction": "Fiebre. La cabeza quema, el cuerpo tiembla. Va a pasar â€” yo me quedo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a mostra as prÃ³prias mÃ£os calejadas pra vocÃª ver: 'Con esto trabajo.' O que sÃ£o essas?",
                    "options": [
                        {"id": "a", "text": "Manos"},
                        {"id": "b", "text": "Cabeza"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "LÃ¡mpara"},
                    ],
                    "correct": "a",
                    "word_id": "es_manos", "target": "manos", "native": "mÃ£os",
                    "npc_reaction": "Manos. Las mÃ­as curan. Las tuyas â€” ya hablaremos de las tuyas otro dÃ­a.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # MarÃ­a prepara a infusÃ£o e conversa. Faz perguntas pequenas, suaves,
    # parecidas com as que SofÃ­a e Carmen jÃ¡ fizeram â€” mas calibradas pra
    # medir vocÃª. O jogador nÃ£o percebe. RevisÃ£o F1-F7.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a"],
                "story": (
                    "MarÃ­a nomeou tudo: cabeza, fiebre, manos. Levantou da cama, "
                    "abriu a bolsa, espalhou ervas na mesinha do canto. SofÃ­a "
                    "trouxe uma panela pequena com Ã¡gua quente que Miguel deixou "
                    "preparada.\n\n"
                    "Enquanto a infusÃ£o fica pronta, MarÃ­a conversa baixo. "
                    "Faz perguntas â€” nÃ£o pra curar. Pra conhecer."
                ),
                "now": "MarÃ­a quer saber quem vocÃª Ã©. Cada pergunta Ã© simples â€” mas ela escuta tudo.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "SofÃ­a me contÃ³ que llegaste hace pocos dÃ­as. Â¿De dÃ³nde vienes, forastero?",
                    "translation": "SofÃ­a me contou que vocÃª chegou faz poucos dias. De onde vocÃª vem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª nÃ£o lembra de onde vem â€” nunca lembrou. A resposta honesta sobre o que vocÃª Ã© aqui:",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Soy campesino"},
                        {"id": "c", "text": "Soy vecino"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero. Yo tambiÃ©n lleguÃ© hace poco â€” hace dos meses. SÃ© lo que es.",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a sorri pequeno enquanto fala. Continua quebrando ervas com as mÃ£os firmes.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Y cuÃ¡ntos aÃ±os tienes? Pareces joven.",
                    "translation": "E quantos anos vocÃª tem? VocÃª parece jovem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a quer saber sua idade. VocÃª responde do jeito que Carmen acabou de te ensinar:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Veinte aÃ±os tengo"},
                        {"id": "d", "text": "Me llamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Yo tengo veinticuatro. Cuatro aÃ±os de diferencia â€” casi como hermanos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Y cÃ³mo te sientes ahora â€” comparado con hace una hora? Mejor o peor?",
                    "translation": "E como vocÃª se sente agora â€” comparado com uma hora atrÃ¡s? Melhor ou pior?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "O pano frio na testa ajudou. A pressÃ£o atrÃ¡s dos olhos diminuiu. VocÃª responde honestamente:",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. La infusiÃ³n va a ayudarte mÃ¡s. Aguanta unos minutos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "MarÃ­a â€” Â¿tÃº vienes a quedarte aquÃ­ esta noche?",
                    "translation": "MarÃ­a â€” vocÃª vem ficar aqui essa noite?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "SofÃ­a pergunta se MarÃ­a vai ficar. Para MarÃ­a, ficar Ã© decisÃ£o simples e necessÃ¡ria. Como ela responde?",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy a quedarme"},
                        {"id": "b", "text": "No tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s SofÃ­a"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Hasta que la fiebre baje. No se deja a un enfermo solo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "SofÃ­a me contÃ³ que ayer pasaron por el mercado de maÃ±ana. Â¿Te gustÃ³?",
                    "translation": "SofÃ­a me contou que vocÃªs passaram pelo mercado de manhÃ£. VocÃª gostou?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª se lembra das laranjas, do mercader, da plaza cheia. MarÃ­a quer saber. VocÃª responde â€” a palavra que sempre vale quando alguÃ©m pergunta como vocÃª se sente sobre algo:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me gustÃ³"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "No me acuerdo"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Hay dÃ­as que el mercado se hace pesado. Otros dÃ­as â€” uno se siente parte.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Y la lÃ¡mpara que SofÃ­a te dio? La vi en tu bolsillo.",
                    "translation": "E a lamparina que SofÃ­a te deu? Vi no seu bolso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a se interessou pela lamparina. VocÃª nÃ£o consegue mentir bem com febre â€” diz a verdade simples:",
                    "options": [
                        {"id": "a", "text": "Da luz"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Es forastero"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "Luz pequeÃ±a â€” para no caer en la oscuridad. La abuela de SofÃ­a era sabia.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel volta da cozinha com mais panos limpos. Olha pra MarÃ­a â€” agradece com um aceno de cabeÃ§a que ele faz raramente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Miguel â€” gracias por avisarme. Y por la calma. La calma cura tanto como las hierbas.",
                    "translation": "Miguel â€” obrigada por me avisar. E pela calma. A calma cura tanto quanto as ervas.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel ouve com a paciÃªncia dele. Aceita o agradecimento com uma palavra simples:",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "De nada, MarÃ­a. El forastero es como hermano para nosotros.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a olha pra vocÃª â€” vocÃª tÃ¡ quase dormindo de novo. 'Una cosa mÃ¡s â€” Â¿cÃ³mo te llamas tÃº?' VocÃª responde mais uma vez, sonolento:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Tengo veinte aÃ±os"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Mucho gusto otra vez. Te lo digo para que sepas â€” no es por la fiebre que te pregunto. Es para no olvidarte.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Madrugada profunda. Febre oscilando. MarÃ­a testa o protagonista
    # com perguntas rÃ¡pidas pra ver o estado mental â€” mas tambÃ©m usa as
    # perguntas pra medir o nÃ­vel dele com a lÃ­ngua. Rapid-fire.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a"],
                "story": (
                    "A infusÃ£o amarga jÃ¡ tÃ¡ nas suas mÃ£os. Cheira a hierba seca, "
                    "alecrim, alguma raiz que vocÃª nunca viu. MarÃ­a nÃ£o te deixa "
                    "dormir antes de beber tudo.\n\n"
                    "SofÃ­a dormiu na cadeira da sala â€” cansada demais. Miguel "
                    "encostou no batente da porta. Sobrou vocÃª e MarÃ­a acordados."
                ),
                "now": "MarÃ­a vai te fazer responder pra continuar acordado. Cada pergunta Ã© teste.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Tienes que beber esto. Te vas a dormir despuÃ©s â€” pero antes, hablamos un poco. Para que no caigas en sueÃ±o profundo aÃºn.",
                    "translation": "VocÃª tem que beber isso. Depois vocÃª dorme â€” mas antes, a gente conversa um pouco. Pra vocÃª nÃ£o cair em sono profundo ainda.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Ela pÃµe a tigela quente nas suas mÃ£os. VocÃª bebe um gole â€” amargo. Ela espera. Pra agradecer vocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Sigue bebiendo, despacio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Mira â€” voy a tocarte la frente otra vez. Â¿EstÃ¡ mÃ¡s frÃ­a?",
                    "translation": "Olha â€” eu vou tocar sua testa de novo. TÃ¡ mais fria?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "A mÃ£o dela pousa de novo na sua testa. VocÃª sente alÃ­vio. A febre tÃ¡ baixando. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Mejor"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo sed"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. Las hierbas estÃ¡n trabajando. Sigue.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Y la cabeza? Â¿Sigue doliendo?",
                    "translation": "E a cabeÃ§a? Ainda tÃ¡ doendo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "A pressÃ£o atrÃ¡s dos olhos diminuiu pra metade. Ainda tem, mas nÃ£o impede vocÃª de pensar. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "La cabeza estÃ¡ mejor"},
                        {"id": "b", "text": "Mal, todo mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Bueno. MaÃ±ana en la maÃ±ana va a estar como nueva. ConfÃ­a.",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a senta na cadeira ao lado da cama. Cruza as pernas. Vai ficar mesmo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "CuÃ©ntame algo simple â€” para que sepa cÃ³mo estÃ¡ tu cabeza. Â¿QuiÃ©n es SofÃ­a para ti?",
                    "translation": "Me conta uma coisa simples â€” pra eu saber como tÃ¡ sua cabeÃ§a. Quem Ã© SofÃ­a pra vocÃª?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª lembra que SofÃ­a entrou no grupo ontem. Ela disse que vinha com vocÃªs. Pra MarÃ­a, vocÃª descreve assim:",
                    "options": [
                        {"id": "a", "text": "Ella va con nosotros"},
                        {"id": "b", "text": "Ella tiene miedo"},
                        {"id": "c", "text": "Ella es Carmen"},
                        {"id": "d", "text": "Ella tiene fiebre"},
                    ],
                    "correct": "a",
                    "word_id": "es_ella_va", "target": "ella va", "native": "ela vai",
                    "npc_reaction": "Bueno. Tu cabeza funciona. La fiebre no comiÃ³ las palabras.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Y Miguel? Â¿QuÃ© es de ti?",
                    "translation": "E Miguel? O que ele Ã© pra vocÃª?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Miguel Ã© o jovem do pueblo que fala um pouco da sua lÃ­ngua. Companheiro desde a F1. VocÃª diz pra MarÃ­a:",
                    "options": [
                        {"id": "a", "text": "Es mi amigo"},
                        {"id": "b", "text": "Es vecino"},
                        {"id": "c", "text": "Es forastero"},
                        {"id": "d", "text": "Es campesino"},
                    ],
                    "correct": "a",
                    "word_id": "es_amigo", "target": "amigo", "native": "amigo",
                    "npc_reaction": "Amigo. Bueno saberlo. La palabra mÃ¡s fuerte de este pueblo, despuÃ©s de 'gracias'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Tienes hambre? La infusiÃ³n a veces despierta el estÃ³mago.",
                    "translation": "TÃ¡ com fome? A infusÃ£o Ã s vezes acorda o estÃ´mago.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª nÃ£o comeu nada alÃ©m de meio pÃ£o antes da febre subir. O estÃ´mago ronca. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Buenas noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. Buena seÃ±al. SofÃ­a dejÃ³ pan en la mesa â€” voy a partirte un pedazo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "MarÃ­a se levanta. Vai atÃ© a cozinha. Volta com meio pÃ£o "
                        "fresco e um copo de Ã¡gua. Coloca tudo na mesinha do "
                        "lado da cama."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Come despacio. Bebe el agua despuÃ©s. Tu cuerpo estÃ¡ aprendiendo a recuperarse â€” no lo apures.",
                    "translation": "Come devagar. Bebe a Ã¡gua depois. Seu corpo tÃ¡ aprendendo a se recuperar â€” nÃ£o apressa ele.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª come o pÃ£o devagar. Sente o corpo voltar ao normal pouco a pouco. MarÃ­a pergunta sem virar o rosto: 'Â¿CÃ³mo estÃ¡s ahora?' VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Mejor, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "AdiÃ³s MarÃ­a"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. Pan, agua, hierbas, calma. Las cuatro cosas que cura el cuerpo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a pergunta uma Ãºltima pergunta antes de vocÃª dormir. 'Una Ãºltima cosa â€” Â¿tienes miedo aÃºn?' VocÃª pensa um pouco. A febre baixou. SofÃ­a dorme na cadeira. Miguel na porta. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "No, estoy bien"},
                        {"id": "b", "text": "SÃ­, tengo mucho miedo"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Si vuelves a tener miedo en la noche â€” me llamas. Yo me quedo cerca.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # MarÃ­a ensina 'estoy + adjetivo de estado'. Pra que o protagonista
    # consiga descrever como se sente em diferentes situaÃ§Ãµes.
    # Beats narrativos suaves entre exercÃ­cios â€” MarÃ­a paciente.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a"],
                "story": (
                    "VocÃª comeu, bebeu, voltou pra cama. A febre baixou. MarÃ­a "
                    "ficou na cadeira, cuidando â€” calada na maior parte do tempo, "
                    "atenta o tempo inteiro.\n\n"
                    "Quando a primeira luz da manhÃ£ comeÃ§ou a entrar pela janela "
                    "ela falou: 'Voy a enseÃ±arte una cosa simple. Para que sepas "
                    "decir cÃ³mo te sientes â€” sin tener que pensar.'"
                ),
                "now": "MarÃ­a vai te ensinar os 3 verbos centrais do espanhol â€” tengo, estoy, soy.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Mira â€” has usado tres verbos sin saber que son tres. Te los voy a separar.",
                    "translation": "Olha â€” vocÃª usou trÃªs verbos sem saber que sÃ£o trÃªs. Vou separar pra vocÃª.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Primero: 'soy'. Yo soy MarÃ­a. TÃº eres forastero. Don Miguel es campesino. 'Soy' es lo que eres siempre â€” tu identidad.",
                    "translation": "Primeiro: 'soy' (sou). Yo soy MarÃ­a. TÃº eres forastero. Don Miguel es campesino. 'Soy' Ã© o que vocÃª Ã© sempre â€” sua identidade.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Soy / eres / es",
                    "meaning": "Sou / Ã©s / Ã© â€” identidade que nÃ£o muda",
                    "note": "Yo soy [quien] Â· TÃº eres [quien] Â· Ã‰l/Ella es [quien]. Quem vocÃª Ã‰: forastero, campesino, panadera.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Segundo: 'estoy'. Yo estoy bien hoy, maÃ±ana estarÃ© mal â€” quien sabe. 'Estoy' es cÃ³mo te encuentras AHORA. Cambia.",
                    "translation": "Segundo: 'estoy' (estou). Yo estoy bien hoje, maÃ±ana estarÃ© mal â€” sabe-se lÃ¡. 'Estoy' Ã© como vocÃª se encontra AGORA. Muda.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Estoy / estÃ¡s / estÃ¡",
                    "meaning": "Estou / estÃ¡s / estÃ¡ â€” estado que muda",
                    "note": "Yo estoy [como] Â· TÃº estÃ¡s [como] Â· Ã‰l/Ella estÃ¡ [como]. Como vocÃª ESTÃ: bien, mal, mejor, cansado, enfermo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Tercero: 'tengo'. Tengo hambre, tengo sed, tengo miedo, tengo veinte aÃ±os. 'Tengo' es lo que el cuerpo PIDE â€” sensaciÃ³n o edad.",
                    "translation": "Terceiro: 'tengo' (tenho). Tengo hambre, sed, miedo, veinte aÃ±os. 'Tengo' Ã© o que o corpo PEDE â€” sensaÃ§Ã£o ou idade.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tengo / tienes / tiene",
                    "meaning": "Tenho / tens / tem â€” sensaÃ§Ã£o ou posse",
                    "note": "Yo tengo [sensaciÃ³n/edad] Â· TÃº tienes Â· Ã‰l/Ella tiene. Para fome, sede, medo, frio, calor, idade.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Soy",   "isKey": True},
                        {"text": " forastero (identidad) Â· ", "isKey": False},
                        {"text": "Estoy", "isKey": True},
                        {"text": " cansado (estado) Â· ",       "isKey": False},
                        {"text": "Tengo", "isKey": True},
                        {"text": " hambre (sensaciÃ³n)",         "isKey": False},
                    ],
                    "example": "Soy forastero, pero estoy cansado y tengo hambre.",
                    "translation": "Sou forasteiro, mas estou cansado e tenho fome.",
                    "note": "SOY = quem vocÃª Ã© (nÃ£o muda) Â· ESTOY = como vocÃª estÃ¡ (muda) Â· TENGO = o que sente/tem",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a aponta pra vocÃª. 'TÃº â€” Â¿quiÃ©n eres en este pueblo? No cÃ³mo estÃ¡s, quÃ© eres.' VocÃª responde com SER (identidade):",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Estoy forastero"},
                        {"id": "c", "text": "Tengo forastero"},
                        {"id": "d", "text": "Me llamo forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_soy", "target": "soy", "native": "sou",
                    "npc_reaction": "Soy. Eso eres â€” un forastero. No cambia con el dÃ­a.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Agora ela pergunta 'Â¿Y cÃ³mo te encuentras ahora â€” despuÃ©s de la fiebre?' VocÃª responde com ESTAR (estado):",
                    "options": [
                        {"id": "a", "text": "Estoy mejor"},
                        {"id": "b", "text": "Soy mejor"},
                        {"id": "c", "text": "Tengo mejor"},
                        {"id": "d", "text": "Me llamo mejor"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mejor", "target": "estoy mejor", "native": "estou melhor",
                    "npc_reaction": "Estoy mejor. Eso es estado â€” maÃ±ana puedes estar peor o aÃºn mejor.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Ãšltima do trio â€” vocÃª nÃ£o comeu desde a noite passada. EstÃ´mago vazio. Com TENER (sensaÃ§Ã£o):",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Estoy hambre"},
                        {"id": "c", "text": "Soy hambre"},
                        {"id": "d", "text": "Me llamo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Tengo. Nunca 'estoy hambre' â€” el portuguÃ©s engaÃ±a aquÃ­. En espaÃ±ol el cuerpo TIENE.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Anoche vocÃª tava com febre â€” temporÃ¡rio, vai passar. NÃ£o era sua identidade. Como descreve a noite passada?",
                    "options": [
                        {"id": "a", "text": "Estaba enfermo"},
                        {"id": "b", "text": "Era enfermo"},
                        {"id": "c", "text": "TenÃ­a enfermo"},
                        {"id": "d", "text": "Me llamaba enfermo"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_enfermo", "target": "estoy enfermo", "native": "estou doente",
                    "npc_reaction": "Eso â€” 'estaba' es 'estoy' en el pasado. Estado pasado. Si dijeras 'era enfermo' parecerÃ­as eternamente enfermo. No es eso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Y ahora â€” la luz ya entra, comiste, dormiste un poco. Â¿CÃ³mo estÃ¡s?",
                    "translation": "E agora â€” a luz jÃ¡ entra, vocÃª comeu, dormiu um pouco. Como vocÃª estÃ¡?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "A cabeÃ§a tÃ¡ mais leve. VocÃª sente o corpo voltando. NÃ£o estÃ¡ 100% â€” mas nÃ£o estÃ¡ mais ruim. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Estoy mejor"},
                        {"id": "b", "text": "Tengo mejor"},
                        {"id": "c", "text": "Soy mejor"},
                        {"id": "d", "text": "Me llamo mejor"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mejor", "target": "estoy mejor", "native": "estou melhor",
                    "npc_reaction": "Mejor. La palabra que cura mÃ¡s rÃ¡pido que mis hierbas.",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a se aproxima, toca de leve seu ombro. NÃ£o hÃ¡ mais aquela expressÃ£o da primeira vez â€” sÃ³ firmeza calma.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Y un dÃ­a â€” quizÃ¡ hoy â€” vas a sentirte 'cansado'. Pasaste noche entera con fiebre, no comiste bien. DormirÃ¡s mucho.",
                    "translation": "E um dia â€” talvez hoje â€” vocÃª vai se sentir 'cansado'. Passou a noite inteira com febre, nÃ£o comeu direito. Vai dormir muito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a aponta pros seus olhos com olheiras escuras. VocÃª sente o corpo pesado. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Estoy cansado"},
                        {"id": "b", "text": "Tengo cansado"},
                        {"id": "c", "text": "Soy cansado"},
                        {"id": "d", "text": "Me llamo cansado"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_cansado", "target": "estoy cansado", "native": "estou cansado",
                    "npc_reaction": "Cansado. Descansa. La fiebre se llevÃ³ energÃ­a â€” el cuerpo necesita rellenar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Ãšltima prÃ¡tica â€” MarÃ­a quer ver se vocÃª junta tudo. 'Anoche estabas enfermo. Esta maÃ±ana estÃ¡s...' VocÃª termina:",
                    "options": [
                        {"id": "a", "text": "Mejor, pero cansado"},
                        {"id": "b", "text": "Bien, pero mal"},
                        {"id": "c", "text": "Forastero, pero amigo"},
                        {"id": "d", "text": "Tengo mejor cansado"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mejor", "target": "estoy mejor", "native": "estou melhor",
                    "npc_reaction": "Mejor pero cansado. Eso es exacto. Aprendiste rÃ¡pido, forastero.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # ManhÃ£ cedo. MarÃ­a, SofÃ­a e Miguel conversam baixo na sala. Don Miguel
    # acorda, vÃª a cena, oferece a casa de hÃ³spedes a MarÃ­a. Ela aceita. O
    # protagonista observa do quarto, ainda meio sonolento â€” sente que algo
    # importante acaba de ser decidido sobre o grupo.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel", "Don Miguel"],
                "story": (
                    "VocÃª dormiu mais um pouco. Quando acordou de novo, SofÃ­a jÃ¡ tinha "
                    "saÃ­do da cadeira. MarÃ­a estava na sala falando baixo com Miguel. "
                    "Don Miguel acabava de chegar da porta.\n\n"
                    "VocÃª abriu os olhos sem fazer barulho. Ficou ouvindo."
                ),
                "now": "Observa do quarto â€” algo importante estÃ¡ sendo decidido na sala.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "â˜€ï¸ ManhÃ£ clara Â· A casa toda iluminada Â· Vozes baixas na sala",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Gracias por venir, MarÃ­a. SofÃ­a tenÃ­a razÃ³n en llamarte.",
                    "translation": "Obrigado por vir, MarÃ­a. SofÃ­a teve razÃ£o de te chamar.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "De nada, Don Miguel. La fiebre fue intensa. Pero pasÃ³.",
                    "translation": "De nada, Don Miguel. A febre foi intensa. Mas passou.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "SofÃ­a me dijo que ayer hablaron con Carmen en la plaza. Que pasaron el dÃ­a como vecinos.",
                    "translation": "SofÃ­a me disse que ontem vocÃªs falaram com Carmen na plaza. Que passaram o dia como vizinhos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel quer saber sobre o dia anterior â€” antes da febre. VocÃª responde quando foi:",
                    "options": [
                        {"id": "a", "text": "Ayer, todo el dÃ­a"},
                        {"id": "b", "text": "MaÃ±ana, todo el dÃ­a"},
                        {"id": "c", "text": "Hoy, todo el dÃ­a"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_hoy", "target": "hoy/ayer", "native": "hoje/ontem",
                    "npc_reaction": "Bueno. Carmen es paciente. Buena con los nuevos.",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel olha pra MarÃ­a por um segundo a mais que o necessÃ¡rio. Pondera alguma coisa. Depois decide.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Tengo una casa de huÃ©spedes atrÃ¡s. VacÃ­a hace tiempo. Si necesitas un sitio mientras estÃ©s en el pueblo â€” es tuya.",
                    "translation": "Tenho uma casa de hÃ³spedes atrÃ¡s. Vazia faz tempo. Se vocÃª precisa de um lugar enquanto tiver no pueblo â€” Ã© sua.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª sente o ar parar por um segundo. Don Miguel oferecendo casa. Aceitar nÃ£o Ã© apenas dormir lÃ¡ â€” Ã© entrar no cÃ­rculo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Eso es mucho, Don Miguel. Â¿EstÃ¡ seguro?",
                    "translation": "Isso Ã© muito, Don Miguel. VocÃª tem certeza?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Estoy seguro. Una curandera cerca â€” eso le hace bien al pueblo. Acepta.",
                    "translation": "Estou seguro. Uma curandera por perto â€” isso faz bem ao pueblo. Aceita.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Pausa. MarÃ­a olha pra SofÃ­a, depois pra Miguel, depois pra direÃ§Ã£o do quarto onde vocÃª dorme. Decide.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Acepto. Gracias.",
                    "translation": "Aceito. Obrigada.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a se aproxima da porta do seu quarto. VÃª vocÃª acordado. 'Buenos dÃ­as, forastero. Â¿CÃ³mo estÃ¡s?' VocÃª responde com tudo que MarÃ­a te ensinou:",
                    "options": [
                        {"id": "a", "text": "Estoy mejor, gracias"},
                        {"id": "b", "text": "Tengo mejor"},
                        {"id": "c", "text": "Buenos noches"},
                        {"id": "d", "text": "Mal, todo mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mejor", "target": "estoy mejor", "native": "estou melhor",
                    "npc_reaction": "Eso me alegra. Voy a estar atrÃ¡s â€” en la casa de huÃ©spedes de Don Miguel. Si necesitas algo, me llamas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” MarÃ­a se queda. Cerca. Â¿EstÃ¡ bien?",
                    "translation": "Forasteiro â€” MarÃ­a vai ficar. Perto. TÃ¡ bem?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta pra vocÃª se a presenÃ§a de MarÃ­a perto estÃ¡ bem. VocÃª sente â€” algo de bom. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "SÃ­, estÃ¡ bien"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "AdiÃ³s MarÃ­a"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Entonces somos cuatro ahora.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel olha pra todos eles â€” vocÃª, Miguel, SofÃ­a, MarÃ­a. "
                        "Acena com a cabeÃ§a pra ninguÃ©m em particular. Como se ele "
                        "tivesse aprovado alguma coisa que ele mesmo nÃ£o estava "
                        "esperando aprovar."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a acena pra vocÃª e sai com Don Miguel pela porta dos fundos pra ver a casa de hÃ³spedes. Antes de sair, ela diz: 'Descansa el dÃ­a entero, forastero.' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Gracias, MarÃ­a"},
                        {"id": "b", "text": "AdiÃ³s para siempre"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Pasamos esta noche juntos â€” eso se cuenta.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Tarde. MarÃ­a jÃ¡ se instalou na casa de hÃ³spedes. Volta pra ver
    # o protagonista. Confere os sinais. Faz as Ãºltimas perguntas â€” meio
    # avaliaÃ§Ã£o, meio carinho. Gate: errar trava. Encerra com transiÃ§Ã£o
    # pra F9 â€” o grupo de 4 comeÃ§ando a funcionar de verdade.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "VocÃª dormiu o dia todo. Quando acordou de tarde, MarÃ­a tinha "
                    "voltado â€” instalou as coisas dela na casa de hÃ³spedes, varreu "
                    "o pÃ¡tio, conversou com Don Miguel. Agora volta pra fazer a "
                    "Ãºltima checagem do dia.\n\n"
                    "SofÃ­a senta no chÃ£o do seu quarto desenhando alguma coisa na "
                    "lasca de madeira. Miguel da cozinha gritando sobre o jantar."
                ),
                "now": "MarÃ­a vai te avaliar uma Ãºltima vez. Sem erro, sem hesitaÃ§Ã£o.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ† Tarde Â· Sol baixo entrando pela janela Â· MarÃ­a na cadeira ao lado da cama",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Descansaste bien. Lo veo en los ojos. Â¿CÃ³mo te sientes ahora?",
                    "translation": "Descansou bem. Vejo nos olhos. Como vocÃª se sente agora?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "CabeÃ§a leve, corpo descansado, fome de quem dormiu o dia inteiro. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Estoy bien"},
                        {"id": "b", "text": "Estoy mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Soy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Mejor que esta maÃ±ana, Â¿no? El cuerpo recordÃ³ cÃ³mo curar solo.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿La cabeza? TÃ³cala â€” Â¿caliente todavÃ­a?",
                    "translation": "A cabeÃ§a? Toca â€” ainda quente?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª toca a testa â€” fria, normal. MarÃ­a olha esperando vocÃª confirmar que melhorou.",
                    "options": [
                        {"id": "a", "text": "La cabeza estÃ¡ mejor"},
                        {"id": "b", "text": "Tengo fiebre"},
                        {"id": "c", "text": "Estoy enfermo"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. La fiebre se fue. La cabeza es tuya otra vez.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a tira do bolso um frasco pequeno de vidro. LÃ­quido escuro dentro. Coloca na mesinha do lado da cama.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Si la fiebre vuelve â€” y a veces vuelve la primera semana â€” bebe esto. Es para ti. Lo dejo aquÃ­.",
                    "translation": "Se a febre voltar â€” e Ã s vezes volta na primeira semana â€” bebe isso. Ã‰ pra vocÃª. Deixo aqui.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Ela pÃµe a mÃ£o em cima do frasco como quem entrega responsabilidade. VocÃª agradece o cuidado:",
                    "options": [
                        {"id": "a", "text": "Gracias, MarÃ­a"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Para esto vine al pueblo â€” para curar a quien lo necesita.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "MarÃ­a â€” Â¿tÃº vienes con nosotros maÃ±ana al mercado? Hay que reponer cosas.",
                    "translation": "MarÃ­a â€” vocÃª vem com a gente amanhÃ£ no mercado? Tem que repor coisas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "SofÃ­a convida MarÃ­a pra ir ao mercado amanhÃ£ com o grupo. Pra ela, ir junto Ã© o passo natural agora. Como ela responde?",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy con ustedes"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s SofÃ­a"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vamos. Necesito sal y otra cosa. Y conocer mejor el pueblo de dÃ­a.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel chega na porta do quarto: 'Cena lista. Forastero â€” Â¿tÃº vienes a comer?' VocÃª se levanta da cama. Responde:",
                    "options": [
                        {"id": "a", "text": "SÃ­, tengo hambre"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s Miguel"},
                        {"id": "d", "text": "Buenos dÃ­as"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Vamos. SofÃ­a hizo sopa â€” algo de su madre. MarÃ­a, vienes.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F9 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸ² Cozinha Â· Quatro pratos na mesa Â· Vapor subindo",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Os quatro sentaram Ã  mesa pela primeira vez. Don Miguel "
                        "encostado na parede observando, sem comer com vocÃªs â€” "
                        "deixou o espaÃ§o pros jovens.\n\n"
                        "SofÃ­a conta uma piada e ri primeiro da prÃ³pria piada. "
                        "Miguel ri junto. MarÃ­a sorri pequeno. VocÃª ouviu sem "
                        "entender tudo mas riu com eles."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "MaÃ±ana al mercado. Comprar lo que falta. Y despuÃ©s â€” el pueblo va a empezar a vernos como grupo. Hay que cuidar lo que decimos.",
                    "translation": "AmanhÃ£ no mercado. Comprar o que falta. E depois â€” o pueblo vai comeÃ§ar a ver a gente como grupo. Tem que cuidar do que a gente fala.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª olhou pra MarÃ­a enquanto ela falava. A luz da "
                        "lamparina batendo no rosto dela mostrava paciÃªncia, "
                        "carinho, alguma coisa parecida com alegria.\n\n"
                        "VocÃª nÃ£o tinha como saber ainda â€” nÃ£o tinha palavras "
                        "pra isso ainda â€” que ela tinha decidido tudo no segundo "
                        "em que tocou sua testa pela primeira vez."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
