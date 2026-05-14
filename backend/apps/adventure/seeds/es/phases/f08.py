"""
Seed das 6 seções da Fase 8 Espanhol A1 — "La curandera".

⚠️ MILESTONE OBRIGATÓRIO (canônico — story.md, characters.md):
    María entra no grupo na F8. Ao tocar o protagonista (curando-o),
    reconhece a assinatura do dom roubado da família dela. Sabe quem ele
    é desde este momento. **O protagonista não percebe nada.**
    A janela de 3 meses agora tem alguém contando os dias por dentro.

Sofía traz María à casa de Don Miguel. María tem 24 anos, mãos firmes,
olhar paciente. Examina o protagonista, prepara uma infusão amarga.
Quando pousa a mão na têmpora dele, **a expressão muda por um segundo**.
Recompõe. Sorri. Pergunta o nome dele com uma doçura que só o jogador
(que leu os docs) entende como predação. Fica até a febre baixar.
Quando vai embora, Don Miguel oferece a casa de hóspedes. María aceita.

REGRA NARRATIVA DA F8:
- O jogador NÃO deve saber ainda que María é a Vilã. O reconhecimento dela
  acontece em UM beat ('expressão muda por um segundo') que pode passar
  despercebido na primeira jogada. Releitura revela.
- María fala apenas espanhol — sem português.
- O carinho dela é genuíno na superfície. O cálculo é por baixo.

Novos vocab (3): cabeza · fiebre · manos  (+ enfermo, mejor, descansa)
Gramática nova: TRIO CENTRAL DO ESPANHOL — María contrasta os 3 verbos
                que o protagonista já usava sem saber separar:
                · SOY  (identidad: soy forastero / yo soy María)
                · ESTOY (estado: estoy bien / estoy enfermo / estoy mejor)
                · TENGO (sensación + edad: tengo hambre / tengo veinte años)
                Também planta passado simple: 'estaba' como pasado de 'estoy'.
Revisão F1-F7:  hola, gracias, bien/mal, me llamo, tengo X años,
                yo voy, tú vienes
NPC principais: María (entra no grupo) · Sofía · Miguel · Don Miguel
Arco emocional: vulnerabilidade real → cuidado recebido → falsa segurança
                (que o jogador vai depois entender como armadilha)
Transição:      F9 abre na manhã seguinte com María já fazendo café como
                se sempre tivesse morado ali.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f8_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # María chega. Examina. O toque revela o que ela já sabia procurar.
    # O beat do reconhecimento — 'expressão muda por um segundo' — está aqui.
    # Falas dela em espanhol, sem tradução. Imersão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌙 Madrugada · Quarto · Febre alta\n\n"
                        "Você acorda com vozes baixas na sala. Sofía conversando "
                        "com alguém em espanhol rápido. Miguel respondendo. "
                        "E uma terceira voz — feminina, calma, mais grave que "
                        "a de Sofía. Uma voz que ouve antes de falar."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "Aquí está. Lleva horas con la fiebre subiendo.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "A porta do quarto abre devagar. Sofía entra primeiro, depois alguém atrás dela.",
                },
                {
                    "kind": "npc",
                    "npc": "María",
                    "line": "Buenas noches. ¿Puedo acercarme?",
                    "is_new_npc": True,
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Uma mulher de uns 24 anos. Cabelo escuro preso atrás. "
                        "Mãos com cicatrizes pequenas de quem trabalha com facas e "
                        "ervas. Olhos calmos — não de quem é calma. De quem aprendeu "
                        "a ser."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "María",
                    "line": "Soy María. Sofía me llamó. Voy a ver qué tienes.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Ela se aproxima da cama devagar. Senta na beira, abre uma "
                        "bolsa de tecido — frascos pequenos, ervas secas amarradas "
                        "com barbante."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "María",
                    "line": "Voy a tocarte la frente. Sin susto, ¿sí?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Ela coloca a mão na sua testa. Pele fria. Firme.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Por um segundo — um único segundo — a expressão de María muda. "
                        "Os olhos não se movem mas algo passa pelo rosto. Não dor. "
                        "Não surpresa. Reconhecimento.\n\n"
                        "Ela recompõe antes que você termine de notar."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "María",
                    "line": "Fiebre alta. Pero el cuerpo está pelean­do bien. Va a pasar.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "María",
                    "line": "¿Cómo te llamas, forastero?",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "cabeza",  "native": "cabeça"},
                        {"target": "fiebre",  "native": "febre"},
                        {"target": "manos",   "native": "mãos"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": (
                        "María espera. A pergunta é simples — ela quer saber seu "
                        "nome com calma. Você responde do jeito que sempre aprendeu:"
                    ),
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto. Yo soy María. Voy a cuidarte esta noche.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María pousa a mão na sua testa de novo. Pergunta o que está quente. A palavra é:",
                    "options": [
                        {"id": "a", "text": "Cabeza"},
                        {"id": "b", "text": "Manos"},
                        {"id": "c", "text": "Fuego"},
                        {"id": "d", "text": "Luz"},
                    ],
                    "correct": "a",
                    "word_id": "es_cabeza", "target": "cabeza", "native": "cabeça",
                    "npc_reaction": "Cabeza. Caliente. Eso es la fiebre subiendo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Ela põe um pano frio na sua testa pra baixar o que ela acabou de nomear. Como se chama o que você tem agora?",
                    "options": [
                        {"id": "a", "text": "Fiebre"},
                        {"id": "b", "text": "Hambre"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_fiebre", "target": "fiebre", "native": "febre",
                    "npc_reaction": "Fiebre. La cabeza quema, el cuerpo tiembla. Va a pasar — yo me quedo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María mostra as próprias mãos calejadas pra você ver: 'Con esto trabajo.' O que são essas?",
                    "options": [
                        {"id": "a", "text": "Manos"},
                        {"id": "b", "text": "Cabeza"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "Lámpara"},
                    ],
                    "correct": "a",
                    "word_id": "es_manos", "target": "manos", "native": "mãos",
                    "npc_reaction": "Manos. Las mías curan. Las tuyas — ya hablaremos de las tuyas otro día.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ─────────────────────────────────────────────────
    # María prepara a infusão e conversa. Faz perguntas pequenas, suaves,
    # parecidas com as que Sofía e Carmen já fizeram — mas calibradas pra
    # medir você. O jogador não percebe. Revisão F1-F7.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["María", "Sofía"],
                "story": (
                    "María nomeou tudo: cabeza, fiebre, manos. Levantou da cama, "
                    "abriu a bolsa, espalhou ervas na mesinha do canto. Sofía "
                    "trouxe uma panela pequena com água quente que Miguel deixou "
                    "preparada.\n\n"
                    "Enquanto a infusão fica pronta, María conversa baixo. "
                    "Faz perguntas — não pra curar. Pra conhecer."
                ),
                "now": "María quer saber quem você é. Cada pergunta é simples — mas ela escuta tudo.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Sofía me contó que llegaste hace pocos días. ¿De dónde vienes, forastero?",
                    "translation": "Sofía me contou que você chegou faz poucos dias. De onde você vem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você não lembra de onde vem — nunca lembrou. A resposta honesta sobre o que você é aqui:",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Soy campesino"},
                        {"id": "c", "text": "Soy vecino"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero. Yo también llegué hace poco — hace dos meses. Sé lo que es.",
                },
                {
                    "kind": "narrative",
                    "text": "María sorri pequeno enquanto fala. Continua quebrando ervas com as mãos firmes.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Y cuántos años tienes? Pareces joven.",
                    "translation": "E quantos anos você tem? Você parece jovem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María quer saber sua idade. Você responde do jeito que Carmen acabou de te ensinar:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Veinte años tengo"},
                        {"id": "d", "text": "Me llamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Yo tengo veinticuatro. Cuatro años de diferencia — casi como hermanos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Y cómo te sientes ahora — comparado con hace una hora? Mejor o peor?",
                    "translation": "E como você se sente agora — comparado com uma hora atrás? Melhor ou pior?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "O pano frio na testa ajudou. A pressão atrás dos olhos diminuiu. Você responde honestamente:",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. La infusión va a ayudarte más. Aguanta unos minutos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "María — ¿tú vienes a quedarte aquí esta noche?",
                    "translation": "María — você vem ficar aqui essa noite?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Sofía pergunta se María vai ficar. Para María, ficar é decisão simples e necessária. Como ela responde?",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy a quedarme"},
                        {"id": "b", "text": "No tengo miedo"},
                        {"id": "c", "text": "Adiós Sofía"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Hasta que la fiebre baje. No se deja a un enfermo solo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Sofía me contó que ayer pasaron por el mercado de mañana. ¿Te gustó?",
                    "translation": "Sofía me contou que vocês passaram pelo mercado de manhã. Você gostou?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você se lembra das laranjas, do mercader, da plaza cheia. María quer saber. Você responde — a palavra que sempre vale quando alguém pergunta como você se sente sobre algo:",
                    "options": [
                        {"id": "a", "text": "Sí, me gustó"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "No me acuerdo"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Hay días que el mercado se hace pesado. Otros días — uno se siente parte.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Y la lámpara que Sofía te dio? La vi en tu bolsillo.",
                    "translation": "E a lamparina que Sofía te deu? Vi no seu bolso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María se interessou pela lamparina. Você não consegue mentir bem com febre — diz a verdade simples:",
                    "options": [
                        {"id": "a", "text": "Da luz"},
                        {"id": "b", "text": "Tengo hambre"},
                        {"id": "c", "text": "Es forastero"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_luz", "target": "luz", "native": "luz",
                    "npc_reaction": "Luz pequeña — para no caer en la oscuridad. La abuela de Sofía era sabia.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel volta da cozinha com mais panos limpos. Olha pra María — agradece com um aceno de cabeça que ele faz raramente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Miguel — gracias por avisarme. Y por la calma. La calma cura tanto como las hierbas.",
                    "translation": "Miguel — obrigada por me avisar. E pela calma. A calma cura tanto quanto as ervas.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel ouve com a paciência dele. Aceita o agradecimento com uma palavra simples:",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "De nada, María. El forastero es como hermano para nosotros.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María olha pra você — você tá quase dormindo de novo. 'Una cosa más — ¿cómo te llamas tú?' Você responde mais uma vez, sonolento:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Bien, gracias"},
                        {"id": "d", "text": "Tengo veinte años"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto otra vez. Te lo digo para que sepas — no es por la fiebre que te pregunto. Es para no olvidarte.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Madrugada profunda. Febre oscilando. María testa o protagonista
    # com perguntas rápidas pra ver o estado mental — mas também usa as
    # perguntas pra medir o nível dele com a língua. Rapid-fire.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["María", "Sofía"],
                "story": (
                    "A infusão amarga já tá nas suas mãos. Cheira a hierba seca, "
                    "alecrim, alguma raiz que você nunca viu. María não te deixa "
                    "dormir antes de beber tudo.\n\n"
                    "Sofía dormiu na cadeira da sala — cansada demais. Miguel "
                    "encostou no batente da porta. Sobrou você e María acordados."
                ),
                "now": "María vai te fazer responder pra continuar acordado. Cada pergunta é teste.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Tienes que beber esto. Te vas a dormir después — pero antes, hablamos un poco. Para que no caigas en sueño profundo aún.",
                    "translation": "Você tem que beber isso. Depois você dorme — mas antes, a gente conversa um pouco. Pra você não cair em sono profundo ainda.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Ela põe a tigela quente nas suas mãos. Você bebe um gole — amargo. Ela espera. Pra agradecer você diz:",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Sigue bebiendo, despacio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Mira — voy a tocarte la frente otra vez. ¿Está más fría?",
                    "translation": "Olha — eu vou tocar sua testa de novo. Tá mais fria?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "A mão dela pousa de novo na sua testa. Você sente alívio. A febre tá baixando. Você responde:",
                    "options": [
                        {"id": "a", "text": "Mejor"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo sed"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. Las hierbas están trabajando. Sigue.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Y la cabeza? ¿Sigue doliendo?",
                    "translation": "E a cabeça? Ainda tá doendo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "A pressão atrás dos olhos diminuiu pra metade. Ainda tem, mas não impede você de pensar. Você diz:",
                    "options": [
                        {"id": "a", "text": "La cabeza está mejor"},
                        {"id": "b", "text": "Mal, todo mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Bueno. Mañana en la mañana va a estar como nueva. Confía.",
                },
                {
                    "kind": "narrative",
                    "text": "María senta na cadeira ao lado da cama. Cruza as pernas. Vai ficar mesmo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Cuéntame algo simple — para que sepa cómo está tu cabeza. ¿Quién es Sofía para ti?",
                    "translation": "Me conta uma coisa simples — pra eu saber como tá sua cabeça. Quem é Sofía pra você?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você lembra que Sofía entrou no grupo ontem. Ela disse que vinha com vocês. Pra María, você descreve assim:",
                    "options": [
                        {"id": "a", "text": "Ella va con nosotros"},
                        {"id": "b", "text": "Ella tiene miedo"},
                        {"id": "c", "text": "Ella es Carmen"},
                        {"id": "d", "text": "Ella tiene fiebre"},
                    ],
                    "correct": "a",
                    "word_id": "es_ella_va", "target": "ella va", "native": "ela vai",
                    "npc_reaction": "Bueno. Tu cabeza funciona. La fiebre no comió las palabras.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Y Miguel? ¿Qué es de ti?",
                    "translation": "E Miguel? O que ele é pra você?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Miguel é o jovem do pueblo que fala um pouco da sua língua. Companheiro desde a F1. Você diz pra María:",
                    "options": [
                        {"id": "a", "text": "Es mi amigo"},
                        {"id": "b", "text": "Es vecino"},
                        {"id": "c", "text": "Es forastero"},
                        {"id": "d", "text": "Es campesino"},
                    ],
                    "correct": "a",
                    "word_id": "es_amigo", "target": "amigo", "native": "amigo",
                    "npc_reaction": "Amigo. Bueno saberlo. La palabra más fuerte de este pueblo, después de 'gracias'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Tienes hambre? La infusión a veces despierta el estómago.",
                    "translation": "Tá com fome? A infusão às vezes acorda o estômago.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você não comeu nada além de meio pão antes da febre subir. O estômago ronca. Você diz:",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Tengo sed"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Buenas noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Hambre. Buena señal. Sofía dejó pan en la mesa — voy a partirte un pedazo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "María se levanta. Vai até a cozinha. Volta com meio pão "
                        "fresco e um copo de água. Coloca tudo na mesinha do "
                        "lado da cama."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Come despacio. Bebe el agua después. Tu cuerpo está aprendiendo a recuperarse — no lo apures.",
                    "translation": "Come devagar. Bebe a água depois. Seu corpo tá aprendendo a se recuperar — não apressa ele.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você come o pão devagar. Sente o corpo voltar ao normal pouco a pouco. María pergunta sem virar o rosto: '¿Cómo estás ahora?' Você diz:",
                    "options": [
                        {"id": "a", "text": "Mejor, gracias"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Adiós María"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. Pan, agua, hierbas, calma. Las cuatro cosas que cura el cuerpo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María pergunta uma última pergunta antes de você dormir. 'Una última cosa — ¿tienes miedo aún?' Você pensa um pouco. A febre baixou. Sofía dorme na cadeira. Miguel na porta. Você responde:",
                    "options": [
                        {"id": "a", "text": "No, estoy bien"},
                        {"id": "b", "text": "Sí, tengo mucho miedo"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Si vuelves a tener miedo en la noche — me llamas. Yo me quedo cerca.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # María ensina 'estoy + adjetivo de estado'. Pra que o protagonista
    # consiga descrever como se sente em diferentes situações.
    # Beats narrativos suaves entre exercícios — María paciente.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["María", "Sofía"],
                "story": (
                    "Você comeu, bebeu, voltou pra cama. A febre baixou. María "
                    "ficou na cadeira, cuidando — calada na maior parte do tempo, "
                    "atenta o tempo inteiro.\n\n"
                    "Quando a primeira luz da manhã começou a entrar pela janela "
                    "ela falou: 'Voy a enseñarte una cosa simple. Para que sepas "
                    "decir cómo te sientes — sin tener que pensar.'"
                ),
                "now": "María vai te ensinar os 3 verbos centrais do espanhol — tengo, estoy, soy.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Mira — has usado tres verbos sin saber que son tres. Te los voy a separar.",
                    "translation": "Olha — você usou três verbos sem saber que são três. Vou separar pra você.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Primero: 'soy'. Yo soy María. Tú eres forastero. Don Miguel es campesino. 'Soy' es lo que eres siempre — tu identidad.",
                    "translation": "Primeiro: 'soy' (sou). Yo soy María. Tú eres forastero. Don Miguel es campesino. 'Soy' é o que você é sempre — sua identidade.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Soy / eres / es",
                    "meaning": "Sou / és / é — identidade que não muda",
                    "note": "Yo soy [quien] · Tú eres [quien] · Él/Ella es [quien]. Quem você É: forastero, campesino, panadera.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Segundo: 'estoy'. Yo estoy bien hoy, mañana estaré mal — quien sabe. 'Estoy' es cómo te encuentras AHORA. Cambia.",
                    "translation": "Segundo: 'estoy' (estou). Yo estoy bien hoje, mañana estaré mal — sabe-se lá. 'Estoy' é como você se encontra AGORA. Muda.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Estoy / estás / está",
                    "meaning": "Estou / estás / está — estado que muda",
                    "note": "Yo estoy [como] · Tú estás [como] · Él/Ella está [como]. Como você ESTÁ: bien, mal, mejor, cansado, enfermo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Tercero: 'tengo'. Tengo hambre, tengo sed, tengo miedo, tengo veinte años. 'Tengo' es lo que el cuerpo PIDE — sensación o edad.",
                    "translation": "Terceiro: 'tengo' (tenho). Tengo hambre, sed, miedo, veinte años. 'Tengo' é o que o corpo PEDE — sensação ou idade.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Tengo / tienes / tiene",
                    "meaning": "Tenho / tens / tem — sensação ou posse",
                    "note": "Yo tengo [sensación/edad] · Tú tienes · Él/Ella tiene. Para fome, sede, medo, frio, calor, idade.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Soy",   "isKey": True},
                        {"text": " forastero (identidad) · ", "isKey": False},
                        {"text": "Estoy", "isKey": True},
                        {"text": " cansado (estado) · ",       "isKey": False},
                        {"text": "Tengo", "isKey": True},
                        {"text": " hambre (sensación)",         "isKey": False},
                    ],
                    "example": "Soy forastero, pero estoy cansado y tengo hambre.",
                    "translation": "Sou forasteiro, mas estou cansado e tenho fome.",
                    "note": "SOY = quem você é (não muda) · ESTOY = como você está (muda) · TENGO = o que sente/tem",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María aponta pra você. 'Tú — ¿quién eres en este pueblo? No cómo estás, qué eres.' Você responde com SER (identidade):",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Estoy forastero"},
                        {"id": "c", "text": "Tengo forastero"},
                        {"id": "d", "text": "Me llamo forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_soy", "target": "soy", "native": "sou",
                    "npc_reaction": "Soy. Eso eres — un forastero. No cambia con el día.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Agora ela pergunta '¿Y cómo te encuentras ahora — después de la fiebre?' Você responde com ESTAR (estado):",
                    "options": [
                        {"id": "a", "text": "Estoy mejor"},
                        {"id": "b", "text": "Soy mejor"},
                        {"id": "c", "text": "Tengo mejor"},
                        {"id": "d", "text": "Me llamo mejor"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mejor", "target": "estoy mejor", "native": "estou melhor",
                    "npc_reaction": "Estoy mejor. Eso es estado — mañana puedes estar peor o aún mejor.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Última do trio — você não comeu desde a noite passada. Estômago vazio. Com TENER (sensação):",
                    "options": [
                        {"id": "a", "text": "Tengo hambre"},
                        {"id": "b", "text": "Estoy hambre"},
                        {"id": "c", "text": "Soy hambre"},
                        {"id": "d", "text": "Me llamo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Tengo. Nunca 'estoy hambre' — el portugués engaña aquí. En español el cuerpo TIENE.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Anoche você tava com febre — temporário, vai passar. Não era sua identidade. Como descreve a noite passada?",
                    "options": [
                        {"id": "a", "text": "Estaba enfermo"},
                        {"id": "b", "text": "Era enfermo"},
                        {"id": "c", "text": "Tenía enfermo"},
                        {"id": "d", "text": "Me llamaba enfermo"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_enfermo", "target": "estoy enfermo", "native": "estou doente",
                    "npc_reaction": "Eso — 'estaba' es 'estoy' en el pasado. Estado pasado. Si dijeras 'era enfermo' parecerías eternamente enfermo. No es eso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Y ahora — la luz ya entra, comiste, dormiste un poco. ¿Cómo estás?",
                    "translation": "E agora — a luz já entra, você comeu, dormiu um pouco. Como você está?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "A cabeça tá mais leve. Você sente o corpo voltando. Não está 100% — mas não está mais ruim. Você diz:",
                    "options": [
                        {"id": "a", "text": "Estoy mejor"},
                        {"id": "b", "text": "Tengo mejor"},
                        {"id": "c", "text": "Soy mejor"},
                        {"id": "d", "text": "Me llamo mejor"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mejor", "target": "estoy mejor", "native": "estou melhor",
                    "npc_reaction": "Mejor. La palabra que cura más rápido que mis hierbas.",
                },
                {
                    "kind": "narrative",
                    "text": "María se aproxima, toca de leve seu ombro. Não há mais aquela expressão da primeira vez — só firmeza calma.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Y un día — quizá hoy — vas a sentirte 'cansado'. Pasaste noche entera con fiebre, no comiste bien. Dormirás mucho.",
                    "translation": "E um dia — talvez hoje — você vai se sentir 'cansado'. Passou a noite inteira com febre, não comeu direito. Vai dormir muito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María aponta pros seus olhos com olheiras escuras. Você sente o corpo pesado. Você diz:",
                    "options": [
                        {"id": "a", "text": "Estoy cansado"},
                        {"id": "b", "text": "Tengo cansado"},
                        {"id": "c", "text": "Soy cansado"},
                        {"id": "d", "text": "Me llamo cansado"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_cansado", "target": "estoy cansado", "native": "estou cansado",
                    "npc_reaction": "Cansado. Descansa. La fiebre se llevó energía — el cuerpo necesita rellenar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Última prática — María quer ver se você junta tudo. 'Anoche estabas enfermo. Esta mañana estás...' Você termina:",
                    "options": [
                        {"id": "a", "text": "Mejor, pero cansado"},
                        {"id": "b", "text": "Bien, pero mal"},
                        {"id": "c", "text": "Forastero, pero amigo"},
                        {"id": "d", "text": "Tengo mejor cansado"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mejor", "target": "estoy mejor", "native": "estou melhor",
                    "npc_reaction": "Mejor pero cansado. Eso es exacto. Aprendiste rápido, forastero.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Manhã cedo. María, Sofía e Miguel conversam baixo na sala. Don Miguel
    # acorda, vê a cena, oferece a casa de hóspedes a María. Ela aceita. O
    # protagonista observa do quarto, ainda meio sonolento — sente que algo
    # importante acaba de ser decidido sobre o grupo.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel", "Don Miguel"],
                "story": (
                    "Você dormiu mais um pouco. Quando acordou de novo, Sofía já tinha "
                    "saído da cadeira. María estava na sala falando baixo com Miguel. "
                    "Don Miguel acabava de chegar da porta.\n\n"
                    "Você abriu os olhos sem fazer barulho. Ficou ouvindo."
                ),
                "now": "Observa do quarto — algo importante está sendo decidido na sala.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "☀️ Manhã clara · A casa toda iluminada · Vozes baixas na sala",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Gracias por venir, María. Sofía tenía razón en llamarte.",
                    "translation": "Obrigado por vir, María. Sofía teve razão de te chamar.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "De nada, Don Miguel. La fiebre fue intensa. Pero pasó.",
                    "translation": "De nada, Don Miguel. A febre foi intensa. Mas passou.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Sofía me dijo que ayer hablaron con Carmen en la plaza. Que pasaron el día como vecinos.",
                    "translation": "Sofía me disse que ontem vocês falaram com Carmen na plaza. Que passaram o dia como vizinhos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel quer saber sobre o dia anterior — antes da febre. Você responde quando foi:",
                    "options": [
                        {"id": "a", "text": "Ayer, todo el día"},
                        {"id": "b", "text": "Mañana, todo el día"},
                        {"id": "c", "text": "Hoy, todo el día"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_hoy", "target": "hoy/ayer", "native": "hoje/ontem",
                    "npc_reaction": "Bueno. Carmen es paciente. Buena con los nuevos.",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel olha pra María por um segundo a mais que o necessário. Pondera alguma coisa. Depois decide.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Tengo una casa de huéspedes atrás. Vacía hace tiempo. Si necesitas un sitio mientras estés en el pueblo — es tuya.",
                    "translation": "Tenho uma casa de hóspedes atrás. Vazia faz tempo. Se você precisa de um lugar enquanto tiver no pueblo — é sua.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você sente o ar parar por um segundo. Don Miguel oferecendo casa. Aceitar não é apenas dormir lá — é entrar no círculo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Eso es mucho, Don Miguel. ¿Está seguro?",
                    "translation": "Isso é muito, Don Miguel. Você tem certeza?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Estoy seguro. Una curandera cerca — eso le hace bien al pueblo. Acepta.",
                    "translation": "Estou seguro. Uma curandera por perto — isso faz bem ao pueblo. Aceita.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Pausa. María olha pra Sofía, depois pra Miguel, depois pra direção do quarto onde você dorme. Decide.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Acepto. Gracias.",
                    "translation": "Aceito. Obrigada.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María se aproxima da porta do seu quarto. Vê você acordado. 'Buenos días, forastero. ¿Cómo estás?' Você responde com tudo que María te ensinou:",
                    "options": [
                        {"id": "a", "text": "Estoy mejor, gracias"},
                        {"id": "b", "text": "Tengo mejor"},
                        {"id": "c", "text": "Buenos noches"},
                        {"id": "d", "text": "Mal, todo mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mejor", "target": "estoy mejor", "native": "estou melhor",
                    "npc_reaction": "Eso me alegra. Voy a estar atrás — en la casa de huéspedes de Don Miguel. Si necesitas algo, me llamas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Forastero — María se queda. Cerca. ¿Está bien?",
                    "translation": "Forasteiro — María vai ficar. Perto. Tá bem?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta pra você se a presença de María perto está bem. Você sente — algo de bom. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sí, está bien"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "Tengo hambre"},
                        {"id": "d", "text": "Adiós María"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Entonces somos cuatro ahora.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel olha pra todos eles — você, Miguel, Sofía, María. "
                        "Acena com a cabeça pra ninguém em particular. Como se ele "
                        "tivesse aprovado alguma coisa que ele mesmo não estava "
                        "esperando aprovar."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María acena pra você e sai com Don Miguel pela porta dos fundos pra ver a casa de hóspedes. Antes de sair, ela diz: 'Descansa el día entero, forastero.' Você responde:",
                    "options": [
                        {"id": "a", "text": "Gracias, María"},
                        {"id": "b", "text": "Adiós para siempre"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Pasamos esta noche juntos — eso se cuenta.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Tarde. María já se instalou na casa de hóspedes. Volta pra ver
    # o protagonista. Confere os sinais. Faz as últimas perguntas — meio
    # avaliação, meio carinho. Gate: errar trava. Encerra com transição
    # pra F9 — o grupo de 4 começando a funcionar de verdade.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "Você dormiu o dia todo. Quando acordou de tarde, María tinha "
                    "voltado — instalou as coisas dela na casa de hóspedes, varreu "
                    "o pátio, conversou com Don Miguel. Agora volta pra fazer a "
                    "última checagem do dia.\n\n"
                    "Sofía senta no chão do seu quarto desenhando alguma coisa na "
                    "lasca de madeira. Miguel da cozinha gritando sobre o jantar."
                ),
                "now": "María vai te avaliar uma última vez. Sem erro, sem hesitação.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌆 Tarde · Sol baixo entrando pela janela · María na cadeira ao lado da cama",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Descansaste bien. Lo veo en los ojos. ¿Cómo te sientes ahora?",
                    "translation": "Descansou bem. Vejo nos olhos. Como você se sente agora?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Cabeça leve, corpo descansado, fome de quem dormiu o dia inteiro. Você diz:",
                    "options": [
                        {"id": "a", "text": "Estoy bien"},
                        {"id": "b", "text": "Estoy mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Soy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien. Mejor que esta mañana, ¿no? El cuerpo recordó cómo curar solo.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿La cabeza? Tócala — ¿caliente todavía?",
                    "translation": "A cabeça? Toca — ainda quente?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você toca a testa — fria, normal. María olha esperando você confirmar que melhorou.",
                    "options": [
                        {"id": "a", "text": "La cabeza está mejor"},
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
                    "text": "María tira do bolso um frasco pequeno de vidro. Líquido escuro dentro. Coloca na mesinha do lado da cama.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Si la fiebre vuelve — y a veces vuelve la primera semana — bebe esto. Es para ti. Lo dejo aquí.",
                    "translation": "Se a febre voltar — e às vezes volta na primeira semana — bebe isso. É pra você. Deixo aqui.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Ela põe a mão em cima do frasco como quem entrega responsabilidade. Você agradece o cuidado:",
                    "options": [
                        {"id": "a", "text": "Gracias, María"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Para esto vine al pueblo — para curar a quien lo necesita.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "María — ¿tú vienes con nosotros mañana al mercado? Hay que reponer cosas.",
                    "translation": "María — você vem com a gente amanhã no mercado? Tem que repor coisas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Sofía convida María pra ir ao mercado amanhã com o grupo. Pra ela, ir junto é o passo natural agora. Como ela responde?",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy con ustedes"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "Adiós Sofía"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vamos. Necesito sal y otra cosa. Y conocer mejor el pueblo de día.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel chega na porta do quarto: 'Cena lista. Forastero — ¿tú vienes a comer?' Você se levanta da cama. Responde:",
                    "options": [
                        {"id": "a", "text": "Sí, tengo hambre"},
                        {"id": "b", "text": "No, tengo miedo"},
                        {"id": "c", "text": "Adiós Miguel"},
                        {"id": "d", "text": "Buenos días"},
                    ],
                    "correct": "a",
                    "word_id": "es_hambre", "target": "tengo hambre", "native": "tenho fome",
                    "npc_reaction": "Vamos. Sofía hizo sopa — algo de su madre. María, vienes.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F9 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🍲 Cozinha · Quatro pratos na mesa · Vapor subindo",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Os quatro sentaram à mesa pela primeira vez. Don Miguel "
                        "encostado na parede observando, sem comer com vocês — "
                        "deixou o espaço pros jovens.\n\n"
                        "Sofía conta uma piada e ri primeiro da própria piada. "
                        "Miguel ri junto. María sorri pequeno. Você ouviu sem "
                        "entender tudo mas riu com eles."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Mañana al mercado. Comprar lo que falta. Y después — el pueblo va a empezar a vernos como grupo. Hay que cuidar lo que decimos.",
                    "translation": "Amanhã no mercado. Comprar o que falta. E depois — o pueblo vai começar a ver a gente como grupo. Tem que cuidar do que a gente fala.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você olhou pra María enquanto ela falava. A luz da "
                        "lamparina batendo no rosto dela mostrava paciência, "
                        "carinho, alguma coisa parecida com alegria.\n\n"
                        "Você não tinha como saber ainda — não tinha palavras "
                        "pra isso ainda — que ela tinha decidido tudo no segundo "
                        "em que tocou sua testa pela primeira vez."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
