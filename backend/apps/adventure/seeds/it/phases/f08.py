"""
Seed das 6 seções da Fase 8 Italiano A1 — "La guaritrice".

⚠️ MILESTONE OBRIGATÓRIO (canônico — story.md, characters.md):
    Lucia entra no grupo na F8. Ao tocar o protagonista (curando-o),
    reconhece a assenzaatura do dom roubado da família dela. Sabe quem ele
    é desde este momento. **O protagonista não percebe nada.**
    A janela de 3 meses agora tem alguém contando os dias por dentro.

Chiara traz Lucia à casa de Antonio il Contadino. Lucia tem 24 anni, mãos firmes,
olhar paciente. Examina o protagonista, prepara uma infusão amarga.
Quando pousa a mão na têmpora dele, **a expressão muda por um segundo**.
Recompõe. Sorri. Pergunta o nome dele com uma doçura que só o jogador
(que leu os docs) entende come predação. Fica até a febre baixar.
Quando vai embora, Antonio il Contadino oferece a casa de hóspedes. Lucia aceita.

REGRA NARRATIVA DA F8:
- O jogador NÃO deve saber ainda que Lucia é a Vilã. O reconhecimento dela
  acontece em UM beat ('expressão muda por um segundo') que pode passar
  despercebido na primeira jogada. Releitura revela.
- Lucia fala apenas italiano — sem português.
- O carinho dela é genuíno na superfície. O cálculo é por baixo.

Novos vocab (3): testa · febbre · mani  (+ malato, meglio, riposa)
Gramática nova: TRIO CENTRAL DO ITALIANO — Lucia contrasta os 3 verbos
                que o protagonista já usava sem saber separar:
                · SONO (identidade: sono forestiero / io sono Lucia)
                · STO  (estado: sto bene / sto male / sto meglio)
                · HO   (sensação + idade: ho fame / ho vent'anni)
                Também planta passado simples: 'stavo' como passado de 'sto'.
Revisão F1-F7:  ciao, grazie, bene/male, mi chiamo, ho X anni,
                io vado, tu vieni
NPC principais: Lucia (entra no grupo) · Chiara · Nico · Antonio il Contadino
Arco emocional: vulnerabilidade real → cuidado recebido → falsa segurança
                (que o jogador vai depois entender come armadilha)
Transição:      F9 abre na manhã seguinte com Lucia já fazendo café come
                se sempre tivesse morado ali.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Lucia chega. Examina. O toque revela o que ela já sabia procurar.
    # O beat do reconhecimento — 'expressão muda por um segundo' — está aqui.
    # Falas dela em italiano, sem tradução. Imersão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌙 Madrugada · Quarto · Febre alta\n\n"
                        "Você acorda com vozes baixas na salea. Chiara conversando "
                        "com alguém em italiano rápido. Nico respondendo. "
                        "E uma terceira voz — feminina, calma, mais grave que "
                        "a de Chiara. Uma voz que ouve prima de falar."
                    ),
                },
                {
                    "kind": "skill_check",
                    "skill": "cura",
                    "min_level": 1,
                    "uses_item_tag": "remedio",
                    "success": "Voce improvisa cuidado limpo antes que a dor vire problema maior.",
                    "fallback": "Sem tecnica suficiente, voce faz o basico e aceita ajuda para seguir.",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "Aquí está. Lleva horas con la febbre subenedo.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "A porta do quarto abre devagar. Chiara entra primeiro, depois alguém atrás dela.",
                },
                {
                    "kind": "npc",
                    "npc": "Lucia",
                    "line": "Buona notte. ¿Puedo acercarme?",
                    "is_new_npc": True,
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Uma mulher de uns 24 anni. Cabelo escuro prquesto atrás. "
                        "Mãos com cicatrizes pequenas de quem trabalha com facas e "
                        "ervas. Olhos calmos — não de quem é calma. De quem aprendeu "
                        "a ser."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Lucia",
                    "line": "Sono Lucia. Chiara me llamó. Vado a ver qué hai.",
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
                    "npc": "Lucia",
                    "line": "Vado a tocarte la fronte. Senza susto, ¿sí?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Ela coloca a mão na sua testa. Pele fria. Firme.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Por um segundo — um único segundo — a expressão de Lucia muda. "
                        "Os olhos não se movem piu algo passa pelo rosto. Não dor. "
                        "Não surpresa. Reconhecimento.\n\n"
                        "Ela recompõe prima que você termine de notar."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Lucia",
                    "line": "Febbre alta. Ma el corpo está pelean­do bene. Va a pasar.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Lucia",
                    "line": "¿Cómo te chiami, forestiero?",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "testa",  "native": "cabeça"},
                        {"target": "febbre",  "native": "febre"},
                        {"target": "manni",   "native": "mãos"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": (
                        "Lucia espera. A pergunta é simples — ela quer saber seu "
                        "nome com calma. Você responde do jeito que sempre aprendeu:"
                    ),
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Bene, grazie"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto. Io sono Lucia. Vado a cuidarte esta notte.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia pousa a mão na sua testa de novo. Pergunta o que está quente. A palavra é:",
                    "options": [
                        {"id": "a", "text": "Cabeza"},
                        {"id": "b", "text": "Manni"},
                        {"id": "c", "text": "Fuoco"},
                        {"id": "d", "text": "Luce"},
                    ],
                    "correct": "a",
                    "word_id": "it_testa", "target": "testa", "native": "cabeça",
                    "npc_reaction": "Cabeza. Caliente. Esatto es la febbre subenedo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Ela põe um paneo frio na sua testa pra baixar o que ela acabou de nomear. Como se chama o que você tem agora?",
                    "options": [
                        {"id": "a", "text": "Febbre"},
                        {"id": "b", "text": "Fame"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_febbre", "target": "febbre", "native": "febre",
                    "npc_reaction": "Febbre. La testa quema, el corpo tiembla. Va a pasar — yo me quedo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia mostra as próprias mãos calejadas pra você ver: 'Con esto trabajo.' O que são essas?",
                    "options": [
                        {"id": "a", "text": "Manni"},
                        {"id": "b", "text": "Cabeza"},
                        {"id": "c", "text": "Pane"},
                        {"id": "d", "text": "Lampada"},
                    ],
                    "correct": "a",
                    "word_id": "it_manni", "target": "manni", "native": "mãos",
                    "npc_reaction": "Manni. Las mías curan. Las tuyas — ya hablaremos de las tuyas otro día.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ─────────────────────────────────────────────────
    # Lucia prepara a infusão e conversa. Faz perguntas pequenas, suaves,
    # parecidas com as que Chiara e Bianca já fizeram — piu calibradas pra
    # medir você. O jogador não percebe. Revisão F1-F7.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara"],
                "story": (
                    "Lucia nomeou tudo: testa, febbre, manni. Levantou da cama, "
                    "abriu a bolsa, espalhou ervas na mesenzaha do canto. Chiara "
                    "trouxe uma paneela pequena com água quente que Nico deixou "
                    "preparada.\n\n"
                    "Enquanto a infusão fica pronta, Lucia conversa baixo. "
                    "Faz perguntas — não pra curar. Pra conhecer."
                ),
                "now": "Lucia quer saber quem você é. Cada pergunta é simples — piu ela escuta tudo.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Chiara me contó que sei arrivato hace pocos días. ¿De dónde vieni, forestiero?",
                    "translation": "Chiara mi ha raccontatou que você chegou faz poucos dias. De onde você vem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você não lembra de onde vem — nunca lembrou. A resposta honesta sobre o que você é aqui:",
                    "options": [
                        {"id": "a", "text": "Sono forestiero"},
                        {"id": "b", "text": "Sono campesenzao"},
                        {"id": "c", "text": "Sono vecino"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_forestiero", "target": "forestiero", "native": "estrangeiro",
                    "npc_reaction": "Forestiero. Yo también llegué hace poco — hace dos meses. Sé lo que es.",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia sorri pequeno enquanto fala. Continua quebrando ervas com as mãos firmes.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Y cuántos años hai?Pareces giovane.",
                    "translation": "E quantos anni você tem?Você parece jovem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia quer saber sua idade. Você responde do jeito que Bianca acabou de te ensenzaar:",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Sono veinte"},
                        {"id": "c", "text": "Veinte años ho"},
                        {"id": "d", "text": "Mi chiamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Veinte. Yo ho veinticuatro. Cuatro años de diferencia — casi come hermanni.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Y cómo te sientes adesso — comparado con hace una hora?Mejor o peor?",
                    "translation": "E come você se sente agora — comparado com uma hora atrás?Melhor ou pior?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "O paneo frio na testa ajudou. A pressão atrás dos olhos diminuiu. Você responde honestamente:",
                    "options": [
                        {"id": "a", "text": "Bene"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. La infusión va a ayudarte más. Resisti unos minutos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Lucia — ¿tu vieni a quedarte aquí esta notte?",
                    "translation": "Lucia — você vem ficar aqui essa noite?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Chiara pergunta se Lucia vai ficar. Para Lucia, ficar é decisão simples e necessária. Como ela responde?",
                    "options": [
                        {"id": "a", "text": "Sí, io vado a quedarme"},
                        {"id": "b", "text": "Non ho paura"},
                        {"id": "c", "text": "Adiós Chiara"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Hasta que la febbre baje. No se deja a un malato solo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Chiara me contó que ayer pasaron por el mercato de mañana. ¿Te gustó?",
                    "translation": "Chiara mi ha raccontatou que vocês passaram pelo mercato de manhã. Você gostou?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você se lembra das laranjas, do mercader, da piazza cheia. Lucia quer saber. Você responde — a palavra que sempre vale quando alguém pergunta come você se sente sobre algo:",
                    "options": [
                        {"id": "a", "text": "Sí, me gustó"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Non ricordo"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Hay días que el mercato se hace pesado. Otros días — uno se siente parte.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Y la lampada que Chiara te dio?La vi en tu bolsillo.",
                    "translation": "E a lamparina que Chiara te deu?Vi no seu bolso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia se interessou pela lamparina. Você não consegue mentir bem com febre — diz a verdade simples:",
                    "options": [
                        {"id": "a", "text": "Da luce"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Es forestiero"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_luce", "target": "luce", "native": "luce",
                    "npc_reaction": "Luce pequeña — para no caer en la oscuridad. La nonna de Chiara era sabia.",
                },
                {
                    "kind": "narrative",
                    "text": "Nico volta da cozinha com mais paneos limpos. Olha pra Lucia — agradece com um aceno de cabeça que ele faz raramente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Nico — grazie por avisarme. Y por la calma. La calma cura tanto come las erbe.",
                    "translation": "Nico — obrigada por me avisar. E pela calma. A calma cura tanto quanto as ervas.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico ouve com a paciência dele. Aceita o agradecimento com uma palavra simples:",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Benes días"},
                    ],
                    "correct": "a",
                    "word_id": "it_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "De nada, Lucia. El forestiero es come hermano para noi.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia olha pra você — você tá quase dormindo de novo. 'Una cosa más — ¿cómo te chiami tu?' Você responde mais uma vez, sonolento:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Bene, grazie"},
                        {"id": "d", "text": "Ho veinte años"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto otra vez. Te lo digo para que sepas — no es por la febbre que te pregunto. Es para no olvidarte.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Madrugada profunda. Febre oscilando. Lucia testa o protagonista
    # com perguntas rápidas pra ver o estado mental — piu também usa as
    # perguntas pra medir o nível dele com a língua. Rapid-fire.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara"],
                "story": (
                    "A infusão amarga já tá nas suas mãos. Cheira a hierba seca, "
                    "alecrim, alguma raiz que você nunca viu. Lucia não te deixa "
                    "dormir prima de beber tudo.\n\n"
                    "Chiara dormiu na cadeira da salea — cansada demais. Nico "
                    "encostou no batente da porta. Sobrou você e Lucia acordados."
                ),
                "now": "Lucia vai te fazer responder pra continuar acordado. Cada pergunta é teste.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Hai que beber esto. Te vas a dormir después — ma prima, hablamos un poco. Para que no caigas en sueño profundo aún.",
                    "translation": "Você tem que beber isso. Depois você dorme — piu prima, a gente conversa um pouco. Pra você não cair em sono profundo ainda.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Ela põe a tigela quente nas suas mãos. Você bebe um gole — amargo. Ela espera. Pra agradecer você diz:",
                    "options": [
                        {"id": "a", "text": "Grazie"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Sigue bebenedo, despacio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Guarda — vado a tocarte la fronte otra vez. ¿Está más fría?",
                    "translation": "Olha — eu vou tocar sua testa de novo. Tá mais fria?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "A mão dela pousa de novo na sua testa. Você sente alívio. A febre tá baixando. Você responde:",
                    "options": [
                        {"id": "a", "text": "Mejor"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho sete"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. Las erbe están trabajando. Sigue.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Y la testa?¿Sigue doliendo?",
                    "translation": "E a cabeça?Ainda tá doendo?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "A pressão atrás dos olhos diminuiu pra metade. Ainda tem, piu não impede você de pensar. Você diz:",
                    "options": [
                        {"id": "a", "text": "La testa está mejor"},
                        {"id": "b", "text": "Male, todo male"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Benes nottes"},
                    ],
                    "correct": "a",
                    "word_id": "it_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Bene. Mañana en la mañana va a estar come nueva. Confía.",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia senta na cadeira ao lado da cama. Cruza as pernas. Vai ficar mesmo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Cuéntame algo simple — para que sepa cómo está tu testa. ¿Quién es Chiara para ti?",
                    "translation": "Me conta uma coisa simples — pra eu saber come tá sua cabeça. Quem é Chiara pra você?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você lembra que Chiara entrou no grupo ontem. Ela disse que vinha com vocês. Pra Lucia, você descreve assim:",
                    "options": [
                        {"id": "a", "text": "Lei va con noi"},
                        {"id": "b", "text": "Ella ha paura"},
                        {"id": "c", "text": "Ella es Bianca"},
                        {"id": "d", "text": "Ella ha febbre"},
                    ],
                    "correct": "a",
                    "word_id": "it_lei_va", "target": "lei va", "native": "ela vai",
                    "npc_reaction": "Bene. Tu testa funciona. La febbre no comió las parole.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Y Nico?¿Qué es de ti?",
                    "translation": "E Nico?O que ele é pra você?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Nico é o jovem do borgo que fala um pouco da sua língua. Companeheiro desde a F1. Você diz pra Lucia:",
                    "options": [
                        {"id": "a", "text": "Es mi amigo"},
                        {"id": "b", "text": "Es vecino"},
                        {"id": "c", "text": "Es forestiero"},
                        {"id": "d", "text": "Es campesenzao"},
                    ],
                    "correct": "a",
                    "word_id": "it_amigo", "target": "amigo", "native": "amigo",
                    "npc_reaction": "Amigo. Bene saberlo. La palabra más fuerte de este borgo, después de 'grazie'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Hai fame?La infusión a veces despierta el estómago.",
                    "translation": "Tá com fome?A infusão às vezes acorda o estômago.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você não comeu nada além de meio pão prima da febre subir. O estômago ronca. Você diz:",
                    "options": [
                        {"id": "a", "text": "Ho fame"},
                        {"id": "b", "text": "Ho sete"},
                        {"id": "c", "text": "Sto bene"},
                        {"id": "d", "text": "Buona notte"},
                    ],
                    "correct": "a",
                    "word_id": "it_fame", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Fame. Buena señal. Chiara dejó pane en la mesa — vado a partirte un pedazo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lucia se levanta. Vai até a cozinha. Volta com meio pão "
                        "fresco e um copo de água. Coloca tudo na mesenzaha do "
                        "lado da cama."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Come despacio. Bebe el acqua después. Tu corpo está aprendiendo a recuperarse — no lo apures.",
                    "translation": "Come devagar. Bebe a água depois. Seu corpo tá aprendendo a se recuperar — não apressa ele.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você come o pão devagar. Sente o corpo voltar ao normale pouco a pouco. Lucia pergunta sem virar o rosto: '¿Cómo estás adesso?' Você diz:",
                    "options": [
                        {"id": "a", "text": "Mejor, grazie"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Adiós Lucia"},
                    ],
                    "correct": "a",
                    "word_id": "it_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. Pane, acqua, erbe, calma. Las cuatro cose que cura el corpo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia pergunta uma última pergunta prima de você dormir. 'Una última cosa — ¿hai paura aún?' Você pensa um pouco. A febre baixou. Chiara dorme na cadeira. Nico na porta. Você responde:",
                    "options": [
                        {"id": "a", "text": "No, sto bene"},
                        {"id": "b", "text": "Sí, ho mucho paura"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Si vuelves a tener paura en la notte — me chiami. Yo me quedo cerca.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Lucia ensenzaa 'sto + adjetivo de estado'. Pra que o protagonista
    # consiga descrever come se sente em diferentes situações.
    # Beats narrativos suaves entre exercícios — Lucia paciente.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara"],
                "story": (
                    "Você comeu, bebeu, voltou pra cama. A febre baixou. Lucia "
                    "ficou na cadeira, cuidando — calada na maior parte do tempo, "
                    "atenta o tempo inteiro.\n\n"
                    "Quando a primeira luce da manhã começou a entrar pela janela "
                    "ela falou: 'Vado a enseñarte una cosa simple. Para que sepas "
                    "decir cómo te sientes — senza tener que pensar.'"
                ),
                "now": "Lucia vai te ensenzaar os 3 verbos centrais do italiano — ho, sto, sono.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Guarda — has usado tres verbos senza saber que son tres. Te los vado a separar.",
                    "translation": "Olha — você usou três verbos sem saber que são três. Vou separar pra você.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Primero: 'sono'. Io sono Lucia. Tu eres forestiero. Antonio il Contadino es campesenzao. 'Sono' es lo que eres siempre — tu identidad.",
                    "translation": "Primeiro: 'sono' (sou). Io sono Lucia. Tu eres forestiero. Antonio il Contadino es campesenzao. 'Sono' é o que você é sempre — sua identidade.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Sono / eres / es",
                    "meaning": "Sou / és / é — identidade que não muda",
                    "note": "Io sono [chi] · Tu eres [chi] · Él/Ella es [chi]. Quem você É: forestiero, campesenzao, paneadera.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Segundo: 'sto'. Yo sto bene hoy, mañana estaré male — chi sabe. 'Sto' es cómo te encuentras AHORA. Cambia.",
                    "translation": "Segundo: 'sto' (estou). Yo sto bene hoje, mañana estaré male — sabe-se lá. 'Sto' é come você se encontra AGORA. Muda.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Sto / estás / está",
                    "meaning": "Estou / estás / está — estado que muda",
                    "note": "Yo sto [come] · Tu estás [come] · Él/Ella está [come]. Como você ESTÁ: bene, male, mejor, cansado, malato.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Tercero: 'ho'. Ho fame, ho sete, ho paura, ho veinte años. 'Ho' es lo que el corpo PIDE — sensación o edad.",
                    "translation": "Terceiro: 'ho' (tenho). Ho fame, sed, paura, veinte años. 'Ho' é o que o corpo PEDE — sensação ou idade.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ho / hai / ha",
                    "meaning": "Tenho / tens / tem — sensação ou posse",
                    "note": "Yo ho [sensación/edad] · Tu hai · Él/Ella ha. Para fome, sede, medo, frio, calor, idade.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Sono",   "isKey": True},
                        {"text": " forestiero (identidad) · ", "isKey": False},
                        {"text": "Sto", "isKey": True},
                        {"text": " cansado (estado) · ",       "isKey": False},
                        {"text": "Ho", "isKey": True},
                        {"text": " fame (sensación)",         "isKey": False},
                    ],
                    "example": "Sono forestiero, ma sto cansado y ho fame.",
                    "translation": "Sou forasteiro, piu estou cansado e tenho fome.",
                    "note": "SONO = quem você é (não muda) · STO = come você está (muda) · HO = o que sente/tem",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia aponta pra você. 'Tu — ¿quién eres en este borgo?No cómo estás, qué eres.' Você responde com SER (identidade):",
                    "options": [
                        {"id": "a", "text": "Sono forestiero"},
                        {"id": "b", "text": "Sto forestiero"},
                        {"id": "c", "text": "Ho forestiero"},
                        {"id": "d", "text": "Mi chiamo forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_sono", "target": "sono", "native": "sou",
                    "npc_reaction": "Sono. Esatto eres — un forestiero. No cambia con el día.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Agora ela pergunta '¿Y cómo te encuentras adesso — después de la febbre?' Você responde com ESTAR (estado):",
                    "options": [
                        {"id": "a", "text": "Sto meglio"},
                        {"id": "b", "text": "Sono mejor"},
                        {"id": "c", "text": "Sto meglio"},
                        {"id": "d", "text": "Mi chiamo mejor"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_mejor", "target": "sto mejor", "native": "estou melhor",
                    "npc_reaction": "Sto meglio. Esatto es estado — mañana puedes estar peor o aún mejor.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Última do trio — você não comeu desde a noite passada. Estômago vazio. Com TENER (sensação):",
                    "options": [
                        {"id": "a", "text": "Ho fame"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Sono fame"},
                        {"id": "d", "text": "Mi chiamo fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_fame", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Ho. Nunca 'sto fame' — o português engana aqui. Em italiano o corpo usa avere: ho fame.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Anotte você tava com febre — temporário, vai passar. Não era sua identidade. Como descreve a noite passada?",
                    "options": [
                        {"id": "a", "text": "Stavo malato"},
                        {"id": "b", "text": "Era malato"},
                        {"id": "c", "text": "Tenía malato"},
                        {"id": "d", "text": "Me llamaba malato"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_malato", "target": "sto malato", "native": "estou doente",
                    "npc_reaction": "Esatto — 'stavo' es 'sto' en el pasado. Estado pasado. Si dijeras 'ero malato' parecerías eternamente malato. No es questo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Y adesso — la luce ya entra, comiste, dormiste un poco. ¿Cómo estás?",
                    "translation": "E agora — a luce já entra, você comeu, dormiu um pouco. Como você está?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "A cabeça tá mais leve. Você sente o corpo voltando. Não está 100% — piu não está mais ruim. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sto meglio"},
                        {"id": "b", "text": "Sto meglio"},
                        {"id": "c", "text": "Sono mejor"},
                        {"id": "d", "text": "Mi chiamo mejor"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_mejor", "target": "sto mejor", "native": "estou melhor",
                    "npc_reaction": "Mejor. La palabra que cura más rápido que mis erbe.",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia se aproxima, toca de leve seu ombro. Não há mais aquela expressão da primeira vez — só firmeza calma.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Y un día — quizá hoy — vas a sentirte 'cansado'. Pasaste notte entera con febbre, no comiste bene. Dormirás mucho.",
                    "translation": "E um dia — talvez hoje — você vai se sentir 'cansado'. Passou a noite inteira com febre, não comeu direito. Vai dormir muito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia aponta pros seus olhos com olheiras escuras. Você sente o corpo pesado. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sono stanco"},
                        {"id": "b", "text": "Sono stanco"},
                        {"id": "c", "text": "Sono cansado"},
                        {"id": "d", "text": "Mi chiamo cansado"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_cansado", "target": "sto cansado", "native": "estou cansado",
                    "npc_reaction": "Cansado. Descansa. La febbre se llevó energía — el corpo necesita rellenar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Última prática — Lucia quer ver se você junta tudo. 'Anotte stavos malato. Esta mañana estás...' Você termina:",
                    "options": [
                        {"id": "a", "text": "Mejor, ma cansado"},
                        {"id": "b", "text": "Bene, ma male"},
                        {"id": "c", "text": "Forestiero, ma amigo"},
                        {"id": "d", "text": "Sto meglio cansado"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_mejor", "target": "sto mejor", "native": "estou melhor",
                    "npc_reaction": "Mejor ma cansado. Esatto es exacto. Aprendiste rápido, forestiero.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Manhã cedo. Lucia, Chiara e Nico conversam baixo na salea. Antonio il Contadino
    # acorda, vê a cena, oferece a casa de hóspedes a Lucia. Ela aceita. O
    # protagonista observa do quarto, ainda meio sonolento — sente que algo
    # importante acaba de ser decidido sobre o grupo.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico", "Antonio il Contadino"],
                "story": (
                    "Você dormiu mais um pouco. Quando acordou de novo, Chiara já tinha "
                    "saído da cadeira. Lucia estava na salea falando baixo com Nico. "
                    "Antonio il Contadino acabava de chegar da porta.\n\n"
                    "Você abriu os olhos sem fazer barulho. Ficou ouvindo."
                ),
                "now": "Observa do quarto — algo importante está sendo decidido na salea.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "☀️ Manhã clara · A casa toda iluminada · Vozes baixas na salea",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Grazie por venire, Lucia. Chiara tenía razón en llamarte.",
                    "translation": "Obrigado por vir, Lucia. Chiara teve razão de te chamar.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "De nada, Antonio il Contadino. La febbre fue intensa. Ma pasó.",
                    "translation": "De nada, Antonio il Contadino. A febre foi intensa. Mas passou.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Chiara me ha detto que ayer hablaron con Bianca en la piazza. Que pasaron el día come vecinos.",
                    "translation": "Chiara me disse que ontem vocês falaram com Bianca na piazza. Que passaram o dia come vizinhos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino quer saber sobre o dia anterior — prima da febre. Você responde quando foi:",
                    "options": [
                        {"id": "a", "text": "Ayer, todo el día"},
                        {"id": "b", "text": "Mañana, todo el día"},
                        {"id": "c", "text": "Hoy, todo el día"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_hoy", "target": "hoy/ayer", "native": "hoje/ontem",
                    "npc_reaction": "Bene. Bianca es paciente. Buena con los nuevos.",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio il Contadino olha pra Lucia por um segundo a mais que o necessário. Pondera alguma coisa. Depois decide.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Ho una casa de huéspedes atrás. Vacía hace tiempo. Si necesitas un sitio mientras estés en el borgo — es tuya.",
                    "translation": "Tenho uma casa de hóspedes atrás. Vazia faz tempo. Se você precisa de um lugar enquanto tiver no borgo — é sua.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você sente o ar parar por um segundo. Antonio il Contadino oferecendo casa. Aceitar não é apenas dormir lá — é entrar no círculo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Esatto es mucho, Antonio il Contadino. ¿Está seguro?",
                    "translation": "Isso é muito, Antonio il Contadino. Você tem certeza?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Sono sicuro. Una guaritrice cerca — questo le hace bene al borgo. Acepta.",
                    "translation": "Estou seguro. Uma guaritrice por perto — isso faz bem ao borgo. Aceita.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Pausa. Lucia olha pra Chiara, depois pra Nico, depois pra direção do quarto onde você dorme. Decide.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Acepto. Grazie.",
                    "translation": "Aceito. Obrigada.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia se aproxima da porta do seu quarto. Vê você acordado. 'Benes días, forestiero. ¿Cómo estás?' Você responde com tudo que Lucia te ensenzaou:",
                    "options": [
                        {"id": "a", "text": "Sto meglio, grazie"},
                        {"id": "b", "text": "Sto meglio"},
                        {"id": "c", "text": "Benes nottes"},
                        {"id": "d", "text": "Male, todo male"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_mejor", "target": "sto mejor", "native": "estou melhor",
                    "npc_reaction": "Esatto me alegra. Vado a estar atrás — en la casa de huéspedes de Antonio il Contadino. Si necesitas algo, me chiami.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Forestiero — Lucia se queda. Cerca. ¿Está bene?",
                    "translation": "Forasteiro — Lucia vai ficar. Perto. Tá bem?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta pra você se a presença de Lucia perto está bem. Você sente — algo de bom. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sí, está bene"},
                        {"id": "b", "text": "No, ho paura"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Adiós Lucia"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Entonces somos cuatro adesso.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio il Contadino olha pra todos eles — você, Nico, Chiara, Lucia. "
                        "Acena com a cabeça pra ninguém em particular. Como se ele "
                        "tivesse aprovado alguma coisa que ele mesmo não estava "
                        "esperando aprovar."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia acena pra você e sai com Antonio il Contadino pela porta dos fundos pra ver a casa de hóspedes. Prima de sair, ela diz: 'Descansa el día entero, forestiero.' Você responde:",
                    "options": [
                        {"id": "a", "text": "Grazie, Lucia"},
                        {"id": "b", "text": "Adiós para siempre"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Pasamos esta notte juntos — questo se cuenta.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Tarde. Lucia já se instalou na casa de hóspedes. Volta pra ver
    # o protagonista. Confere os senzaais. Faz as últipiu perguntas — meio
    # avaliação, meio carinho. Gate: errar trava. Encerra com transição
    # pra F9 — o grupo de 4 começando a funcionar de verdade.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Você dormiu o dia todo. Quando acordou de tarde, Lucia tinha "
                    "voltado — instalou as coisas dela na casa de hóspedes, varreu "
                    "o pátio, conversou com Antonio il Contadino. Agora volta pra fazer a "
                    "última checagem do dia.\n\n"
                    "Chiara senta no chão do seu quarto desenhando alguma coisa na "
                    "lasca de madeira. Nico da cozinha gritando sobre o jantar."
                ),
                "now": "Lucia vai te avaliar uma última vez. Sem erro, sem hesitação.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌆 Tarde · Sol baixo entrando pela janela · Lucia na cadeira ao lado da cama",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Descansaste bene. Lo veo en los ojos. ¿Cómo te sientes adesso?",
                    "translation": "Descansou bem. Vejo nos olhos. Como você se sente agora?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Cabeça leve, corpo descansado, fome de quem dormiu o dia inteiro. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sto bene"},
                        {"id": "b", "text": "Sto male"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Sono forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Mejor que esta mañana, ¿no?El corpo recordó cómo curar solo.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿La testa?Tócala — ¿calda todavía?",
                    "translation": "A cabeça?Toca — ainda quente?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você toca a testa — fria, normale. Lucia olha esperando você confirmar que melhorou.",
                    "options": [
                        {"id": "a", "text": "La testa está mejor"},
                        {"id": "b", "text": "Ho febbre"},
                        {"id": "c", "text": "Sto malato"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. La febbre se fue. La testa es tuya otra vez.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Lucia tira do bolso um frasco pequeno de vidro. Líquido escuro dentro. Coloca na mesenzaha do lado da cama.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Si la febbre vuelve — y a veces vuelve la primera semana — bebe esto. Es para ti. Lo dejo aquí.",
                    "translation": "Se a febre voltar — e às vezes volta na primeira semana — bebe isso. É pra você. Deixo aqui.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Ela põe a mão em cima do frasco come quem entrega responsabilidade. Você agradece o cuidado:",
                    "options": [
                        {"id": "a", "text": "Grazie, Lucia"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Para esto vine al borgo — para curar a chi lo necesita.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Lucia — ¿tu vieni con noi mañana al mercato?Hay que reponer cose.",
                    "translation": "Lucia — você vem com a gente amanhã no mercato?Tem que repor coisas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Chiara convida Lucia pra ir ao mercato amanhã com o grupo. Pra ela, ir junto é o passo natural agora. Como ela responde?",
                    "options": [
                        {"id": "a", "text": "Sí, io vado con voi"},
                        {"id": "b", "text": "No, ho paura"},
                        {"id": "c", "text": "Adiós Chiara"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Andiamo. Necesito sale y otra cosa. Y conocer mejor el borgo de día.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico chega na porta do quarto: 'Cena lista. Forestiero — ¿tu vieni a comer?' Você se levanta da cama. Responde:",
                    "options": [
                        {"id": "a", "text": "Sí, ho fame"},
                        {"id": "b", "text": "No, ho paura"},
                        {"id": "c", "text": "Adiós Nico"},
                        {"id": "d", "text": "Benes días"},
                    ],
                    "correct": "a",
                    "word_id": "it_fame", "target": "ho fame", "native": "tenho fome",
                    "npc_reaction": "Andiamo. Chiara hizo sopa — algo de su madre. Lucia, vieni.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F9 ────────────────────────
                {
                    "kind": "scene",
                    "text": "?? Cozinha · Quatro pratos na mesa · Vapor subindo",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Os quatro sentaram à mesa pela primeira vez. Antonio il Contadino "
                        "encostado na parede observando, sem comer com vocês — "
                        "deixou o espaço pros giovanes.\n\n"
                        "Chiara conta uma piada e ri primeiro da própria piada. "
                        "Nico ri junto. Lucia sorri pequeno. Você ouviu sem "
                        "entender tudo piu riu com eles."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Mañana al mercato. Comprar lo que falta. Y después — el borgo va a empezar a vernos come grupo. Hay que cuidar lo que decimos.",
                    "translation": "Amanhã no mercato. Comprar o que falta. E depois — o borgo vai começar a ver a gente come grupo. Tem que cuidar do que a gente fala.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você olhou pra Lucia enquanto ela falava. A luce da "
                        "lamparina batendo no rosto dela mostrava paciência, "
                        "carinho, alguma coisa parecida com alegria.\n\n"
                        "Você não tinha come saber ainda — não tinha palavras "
                        "pra isso ainda — que ela tinha decidido tudo no segundo "
                        "em que tocou sua testa pela primeira vez."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




