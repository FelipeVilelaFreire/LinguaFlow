"""
Seed das 6 seções da Fase 19 Espanhol A1 — "La carta".

⚠️ MILESTONE OBRIGATÓRIO (canônico — story.md):
    F19 = 4ª fase de revisão. A primera palabra da carta torna-se
    legível. O protagonista já fala o suficiente.

Don Miguel abre o baú. Mostra o envelope selado. Os 4 jovens reunidos
ao amanhecer (María saiu cedo de novo — Don Miguel arranjou).

Quase tudo na carta está ilegível pro forastero. Mas no centro — uma
palavra ficou clara. Escura. Pulsando. Você LÊ.

A palavra é: **"Vuelves."** (você volta)

Não entende o sentido completo. Mas sabe que isso muda tudo.

ABORDAGEM PEDAGÓGICA:
    Fase de REVISÃO PESADA. Apresenta apenas vocab narrativo (carta,
    leer, palabra, abrir). Sem nova linguagem gramatical relevante.
    Foco em REVISÃO de F1-F18 — soy/estoy/tengo, voy a, mi/tu/su,
    el/la, vi/hablé/oí, ya/todavía no, puedo, quiero.

VOCAB NOVO (3): carta · leer · abrir
Apresentação adicional: palabra (já conhecido em uso geral)

NPC principais: Don Miguel · Sofía · Miguel · você
Arco emocional: expectativa → revelação parcial → confusão → começar a
                aceitar que tem origem e propósito desconhecidos
Transição: F20 abre com o grupo decidindo o próximo passo — confrontar
            María ou continuar observando.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f19_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Amanhecer. Os 4 reunidos. Don Miguel abre o baú. Cara da carta selada.
    # 2 novos + 2 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌄 Casa de Don Miguel · Amanhecer · Cozinha\n\n"
                        "Don Miguel arranjou que María fosse ao mercado bem cedo "
                        "— pediu coisas que só vendem ao amanhecer. María saiu "
                        "às cinco. Sofía e Miguel chegaram às cinco e meia. Os "
                        "quatro sentados em volta do baú aberto."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Aquí está. Veinte años en este baúl.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Ele pega o envelope. Cera vermelha grossa selando. Símbolo do sol partido — igual à marca de Eduardo.",
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "Ese sello — es el mismo símbolo de la espalda de Eduardo.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Sí. La carta vino del viejo Buscador que llegó al pueblo hace veinte años.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Don Miguel pousa a carta no centro da mesa. Não abriu ainda. Só pousou. Quatro olhos fixos nela.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "carta",   "native": "carta / mensagem escrita"},
                        {"target": "leer",    "native": "ler"},
                        {"target": "abrir",   "native": "abrir"},
                        {"target": "palabra", "native": "palavra"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pousou um envelope grosso, fechado com cera. Como se chama essa coisa?",
                    "options": [
                        {"id": "a", "text": "Carta"},
                        {"id": "b", "text": "Marca"},
                        {"id": "c", "text": "Familia"},
                        {"id": "d", "text": "Espalda"},
                    ],
                    "correct": "a",
                    "word_id": "es_carta", "target": "carta", "native": "carta",
                    "npc_reaction": "Carta. Lo que tiene palabras dentro — pero todavía cerrada.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta a Don Miguel — '¿La vamos a ___?' Pra dizer 'abrir' (verbo base):",
                    "options": [
                        {"id": "a", "text": "abrir"},
                        {"id": "b", "text": "cerrar"},
                        {"id": "c", "text": "comer"},
                        {"id": "d", "text": "ver"},
                    ],
                    "correct": "a",
                    "word_id": "es_abrir", "target": "abrir", "native": "abrir",
                    "npc_reaction": "Abrir. Vamos a abrirla — ahora mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel agradece pela paciência de vocês. Vocês cumprimentam — amanhecer:",
                    "options": [
                        {"id": "a", "text": "Buenos días, Don Miguel"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. Vamos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pergunta 'forastero — ¿cómo estás ahora?':",
                    "options": [
                        {"id": "a", "text": "Tengo miedo, pero estoy listo"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_miedo", "target": "tengo miedo", "native": "tenho medo",
                    "npc_reaction": "Las dos cosas a la vez — eso es lo correcto. Honesto.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Don Miguel pede que cada um diga em voz alta o que sabe
    # — pra que todos estejam na mesma página antes da carta. Revisão da
    # história até aqui.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Sofía", "Miguel"],
                "story": (
                    "Don Miguel pousou a mão na carta. Não vai abrir ainda.\n\n"
                    "'Antes de abrir — quiero que cada uno diga lo que sabe. Para "
                    "que estemos todos en la misma página.'"
                ),
                "now": "Revisão narrativa. Cada um conta o que viu/ouviu/sentiu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Forastero — empieza tú. ¿Cuándo llegaste al pueblo?",
                    "translation": "Forasteiro — começa você. Quando você chegou ao pueblo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você chegou faz duas semanas. Pra falar simples — 'cheguei sem memória, sem nome':",
                    "options": [
                        {"id": "a", "text": "Llegué sin memoria"},
                        {"id": "b", "text": "Llego sin memoria"},
                        {"id": "c", "text": "Voy a llegar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_llegue", "target": "llegué", "native": "cheguei",
                    "npc_reaction": "Llegué. Bueno. Y conociste a Rosa primero — y después a mí.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra confirmar — você viu Rosa primeiro:",
                    "options": [
                        {"id": "a", "text": "Sí, vi a Rosa primero"},
                        {"id": "b", "text": "Sí, veo a Rosa"},
                        {"id": "c", "text": "Voy a ver"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Y la palabra primera que aprendiste fue 'pan'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Sofía — y tú. ¿Cuándo lo viste por primera vez?",
                    "translation": "Sofía — e você. Quando o viu pela primeira vez?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Yo lo vi en tu cuarto la noche del fuego. La noche de la primera chispa.",
                    "translation": "Eu o vi no teu quarto na noite do fogo. A noite da primeira chispa.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Sofía disse 'lo vi'. Você confirma — Sofía também viu o fogo:",
                    "options": [
                        {"id": "a", "text": "Sí, ella vio el fuego"},
                        {"id": "b", "text": "Sí, ella ve el fuego"},
                        {"id": "c", "text": "Va a ver"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vio", "target": "vio", "native": "viu (3ª)",
                    "npc_reaction": "Vio. Tercera persona. Sofía vio — ya pasado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Miguel — y tú. ¿Lo conoces desde cuándo?",
                    "translation": "Miguel — e você. Conhece ele desde quando?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Desde el primer día. Mi padre me llamó — '¡MIGUEL! ¡HAY UN FORASTERO!'. Y vine corriendo.",
                    "translation": "Desde o primeiro dia. Meu pai me chamou — '¡MIGUEL! ¡TEM UM FORASTERO!'. E vim correndo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel disse 'mi padre me llamó'. Pra você responder pra Miguel — sim, ele veio correndo (já passou):",
                    "options": [
                        {"id": "a", "text": "Sí, viniste corriendo"},
                        {"id": "b", "text": "Sí, vienes corriendo"},
                        {"id": "c", "text": "Voy a venir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_viniste", "target": "viniste", "native": "vieste",
                    "npc_reaction": "Viniste. Tú — segunda. Como 'hablaste' o 'viste'. Forma del pasado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y María llegó al pueblo hace dos meses. Eso nos lo dijo ella misma — la noche que cuidó al forastero.",
                    "translation": "E María chegou ao pueblo faz dois meses. Isso ela mesma nos disse — na noite que cuidou do forasteiro.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pergunta: '¿Por qué llegó al pueblo? ¿Saben alguien?' Resposta honesta — vocês ainda não sabem:",
                    "options": [
                        {"id": "a", "text": "Todavía no sabemos"},
                        {"id": "b", "text": "Ya sabemos"},
                        {"id": "c", "text": "Vamos a saber"},
                        {"id": "d", "text": "Somos"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Pero la carta puede ayudarnos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía: '¿Cómo te sientes ahora, forastero — antes de abrir la carta?'",
                    "options": [
                        {"id": "a", "text": "Estoy nervioso"},
                        {"id": "b", "text": "Soy nervioso"},
                        {"id": "c", "text": "Tengo nervioso"},
                        {"id": "d", "text": "Voy nervioso"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_nervioso", "target": "estoy nervioso", "native": "estou nervoso",
                    "npc_reaction": "Nervioso. Estado de ahora — bien usado. Eso pasa rápido cuando ya sabes lo que viene.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Don Miguel abre a carta. Quebra o selo. Tira o papel. Você lê. Quase
    # tudo ilegível. Apenas 1 palavra clara: 'Vuelves'. Foco em revisão de
    # F1-F18 com situações de leitura.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Sofía", "Miguel"],
                "story": (
                    "Don Miguel pegou a faca pequena que sempre tem na cinta. "
                    "Cortou o selo de cera. Quebrou em dois. Tirou o papel "
                    "amarelado de dentro.\n\n"
                    "'Mira tú primero. Solo. Después nosotros.'"
                ),
                "now": "Você lê a carta. Quase tudo confuso. Mas uma palavra fica clara.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "📄 Papel amarelado · Tinta velha · Algumas linhas borradas · Você segurando",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você olha. Há linhas escritas — mas as letras se misturam, "
                        "se borram quando você foca. Como se as palavras não "
                        "quisessem ser lidas ainda.\n\n"
                        "Exceto uma — no centro. Mais escura. Mais grossa.\n\n"
                        "**VUELVES.**"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Puedes leer algo?",
                    "translation": "Você pode ler algo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel pergunta se você pode ler. Honesto — uma palavra só. Pra dizer 'posso ler una palabra':",
                    "options": [
                        {"id": "a", "text": "Puedo leer una palabra"},
                        {"id": "b", "text": "No puedo leer"},
                        {"id": "c", "text": "Voy a leer"},
                        {"id": "d", "text": "Soy leer"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo leer", "native": "posso ler",
                    "npc_reaction": "Puedo leer. Una palabra es suficiente. ¿Cuál?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você fala a palavra em voz alta — 'Vuelves'. Como você descreve isso? Esta palavra significa:",
                    "options": [
                        {"id": "a", "text": "Você volta"},
                        {"id": "b", "text": "Eu vou"},
                        {"id": "c", "text": "Ele come"},
                        {"id": "d", "text": "Nós saímos"},
                    ],
                    "correct": "a",
                    "word_id": "es_vuelves", "target": "vuelves", "native": "você volta",
                    "npc_reaction": "Vuelves. Tú — vuelves. Esa es la palabra. ¿Y te dice algo?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Vuelves. Como si dijera — 'tú regresas a algún sitio'. Pero — ¿adónde?",
                    "translation": "Vuelves. Como se dissesse — 'você retorna a algum lugar'. Mas — pra onde?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta pra você — você lembra de algum lugar de antes? Honesto:",
                    "options": [
                        {"id": "a", "text": "Todavía no me acuerdo"},
                        {"id": "b", "text": "Ya me acuerdo"},
                        {"id": "c", "text": "Voy a acordarme"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                    "npc_reaction": "Todavía no. Pero la palabra está ahí — esperando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "El resto — ¿puedes leer? Inténtalo otra vez.",
                    "translation": "O resto — você pode ler? Tenta outra vez.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você tenta. Quase nada. Resposta honesta — ainda não:",
                    "options": [
                        {"id": "a", "text": "Todavía no puedo leer más"},
                        {"id": "b", "text": "Ya puedo leer todo"},
                        {"id": "c", "text": "Voy a leer"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. La carta se abre solo cuando ya puedes leerla. El Buscador me lo dijo así.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Cada vez que aprendas más — más palabras se van a ver. Eso es lo que él me dijo hace veinte años.",
                    "translation": "Cada vez que você aprender mais — mais palavras vão ficar visíveis. Isso ele me disse há vinte anos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'Forastero — esa palabra — vuelves — ¿qué sientes cuando la lees?' Honesto:",
                    "options": [
                        {"id": "a", "text": "Siento algo en el pecho"},
                        {"id": "b", "text": "No siento nada"},
                        {"id": "c", "text": "Voy a sentir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_siento", "target": "siento", "native": "sinto",
                    "npc_reaction": "Sientes. Eso es lo que importa. Tu cuerpo recuerda lo que tu cabeza ya no.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía: '¿Cómo estás ahora — después de leer eso?'",
                    "options": [
                        {"id": "a", "text": "Estoy mareado, pero bien"},
                        {"id": "b", "text": "Soy mareado"},
                        {"id": "c", "text": "Tengo mareado"},
                        {"id": "d", "text": "Voy mareado"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_mareado", "target": "estoy mareado", "native": "estou tonto",
                    "npc_reaction": "Mareado. Es la palabra que abre por dentro. Es normal sentir algo al leerla.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'Voy a guardarla otra vez. Pero — ¿quieres tocarla una vez más antes?'",
                    "options": [
                        {"id": "a", "text": "Sí, quiero tocarla"},
                        {"id": "b", "text": "No quiero"},
                        {"id": "c", "text": "Voy a guardarla"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero tocarla", "native": "quero tocá-la",
                    "npc_reaction": "Bueno. Tócala. Suavemente.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Don Miguel guarda a carta. Tira do baú um livro velho — registros do
    # pueblo. Quer mostrar uma coisa pro forastero. Aparição de "el/la/los/las"
    # em prática + apresentação suave de quem/lo que (palavras que ligam).
    # ABORDAGEM: revisão dominante + 1 conceito pequeno.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel guardou a carta no baú. Mas tirou um livro velho "
                    "também — capa de couro, páginas amareladas. Registros do "
                    "pueblo dos últimos cinquenta anos.\n\n"
                    "'Antes de que María vuelva — voy a enseñarte algo aquí.'"
                ),
                "now": "Don Miguel mostra o registro do pueblo. Você aprende a navegar pelos nomes.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Este libro tiene los nombres de cada persona que pasó por el pueblo. Las familias. Los visitantes. Los Buscadores que vinieron.",
                    "translation": "Este livro tem os nomes de cada pessoa que passou pelo pueblo. As famílias. Os visitantes. Os Buscadores que vieram.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'las familias'. As palavras 'el/la/los/las' que você viu na F14 — quando algo é mulher e plural:",
                    "options": [
                        {"id": "a", "text": "las"},
                        {"id": "b", "text": "los"},
                        {"id": "c", "text": "el"},
                        {"id": "d", "text": "la"},
                    ],
                    "correct": "a",
                    "word_id": "es_las", "target": "las", "native": "as (mulheres / muitas)",
                    "npc_reaction": "Las. Muchas familias — femenino plural.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Aquí — el viejo Buscador. Su nombre era Tomás. Igual que mi padre. Vino en 1845 — hace veinte años.",
                    "translation": "Aqui — o velho Buscador. O nome dele era Tomás. Igual ao meu pai. Veio em 1845 — faz vinte anos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra confirmar — esse Tomás VIO algo. Quem era ele?",
                    "options": [
                        {"id": "a", "text": "Era el Buscador"},
                        {"id": "b", "text": "Es el Buscador"},
                        {"id": "c", "text": "Va a ser"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_era", "target": "era", "native": "era",
                    "npc_reaction": "Era. Antes — ya pasado. El Buscador.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Quien / Lo que",
                    "meaning": "Palavras que ligam pessoas/coisas a histórias.",
                    "note": "el hombre QUIEN te dio la carta · LO QUE dice la carta es importante",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "El viejo ", "isKey": False},
                        {"text": "QUIEN ",   "isKey": True},
                        {"text": "trajo la carta · ", "isKey": False},
                        {"text": "LO QUE ", "isKey": True},
                        {"text": "dijo la carta",     "isKey": False},
                    ],
                    "example": "El viejo quien trajo la carta murió. Lo que dijo es importante.",
                    "translation": "O velho que trouxe a carta morreu. O que ele disse é importante.",
                    "note": "'quien' = pra pessoas · 'lo que' = pra coisas/ideias.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'El viejo ___ trajo la carta era Buscador.' Pra ligar à pessoa (homem):",
                    "options": [
                        {"id": "a", "text": "quien"},
                        {"id": "b", "text": "lo que"},
                        {"id": "c", "text": "el"},
                        {"id": "d", "text": "la"},
                    ],
                    "correct": "a",
                    "word_id": "es_quien", "target": "quien", "native": "que / quem",
                    "npc_reaction": "Quien. Para personas — siempre. El que / la que también sirven.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "'___ leíste hoy es solo el principio.' Pra ligar à coisa (a carta, o que estava nela):",
                    "options": [
                        {"id": "a", "text": "Lo que"},
                        {"id": "b", "text": "Quien"},
                        {"id": "c", "text": "El"},
                        {"id": "d", "text": "La"},
                    ],
                    "correct": "a",
                    "word_id": "es_lo_que", "target": "lo que", "native": "o que",
                    "npc_reaction": "Lo que. Para cosas o ideas. Esa frase entra mucho en la cabeza.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você confirma — entende isso ainda parcialmente:",
                    "options": [
                        {"id": "a", "text": "Ya entiendo un poco"},
                        {"id": "b", "text": "Todavía no entiendo nada"},
                        {"id": "c", "text": "Voy a entender"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya un poco. Eso es suficiente por hoy.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Don Miguel guarda tudo. María chega — pega vocês 4 reunidos. Tensão.
    # Don Miguel reage rápido. Conversa de coversãod. 100% revisão.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Sofía", "Miguel", "María"],
                "story": (
                    "Don Miguel já tinha guardado a carta no baú. Tinha fechado. "
                    "Coberto com o pano. Quando ouviu os passos de María na rua "
                    "lá fora.\n\n"
                    "'Sofía — pasa a mi cuarto, finge que estás lavando algo. "
                    "Miguel — junto al fogón. Forastero — tú quédate aquí.'\n\n"
                    "María entrou com a cesta cheia."
                ),
                "now": "Encontro inesperado com María. Vocês precisam disfarçar.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌅 Cozinha · María entrando com cesta · Você, Don Miguel · Sofía e Miguel escondidos",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Buenos días. ¿Y los demás? Vi luces aquí desde lejos.",
                    "translation": "Bom dia. E os outros? Vi luzes aqui de longe.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você cumprimenta — manhã clara:",
                    "options": [
                        {"id": "a", "text": "Buenos días, María"},
                        {"id": "b", "text": "Buenas tardes"},
                        {"id": "c", "text": "Buenas noches"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. ¿Don Miguel — cómo amaneció?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Sofía y Miguel vinieron temprano. Sofía está lavando ropa en mi cuarto. Miguel arregla el fogón.",
                    "translation": "Sofía e Miguel vieram cedo. Sofía está lavando roupa no meu quarto. Miguel arruma o fogão.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María pergunta — você sabe o motivo? Resposta segura (vaga):",
                    "options": [
                        {"id": "a", "text": "Quería ayudar a Don Miguel"},
                        {"id": "b", "text": "Voy a ayudar"},
                        {"id": "c", "text": "Soy ayuda"},
                        {"id": "d", "text": "Tengo ayuda"},
                    ],
                    "correct": "a",
                    "word_id": "es_queria", "target": "quería ayudar", "native": "queria ajudar",
                    "npc_reaction": "Querían ayudar. Bueno. Aprovechemos — yo traje hierbas, voy a hacer infusión.",
                },
                {
                    "kind": "narrative",
                    "text": "María vai pra cozinha. Você nota — ela olha pra mesa onde estava o baú. O baú está coberto, fechado. Ela parece satisfeita com o que vê — ou pelo menos não suspeita.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Forastero — ¿dormiste bien anoche? Te vi pálido al despertar.",
                    "translation": "Forasteiro — dormiu bem ontem à noite? Te vi pálido ao acordar.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você dormiu mal — pensando na carta. Mas vai mentir parcialmente — diz que estava cansado:",
                    "options": [
                        {"id": "a", "text": "Sí, estuve cansado"},
                        {"id": "b", "text": "Sí, dormí bien"},
                        {"id": "c", "text": "Voy a dormir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_estuve", "target": "estuve cansado", "native": "estive cansado",
                    "npc_reaction": "Estuve cansado. Bueno. La infusión te va a ayudar hoy.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Don Miguel — encontré algo raro en el mercado esta mañana. Un hombre extranjero — preguntando por nombres.",
                    "translation": "Don Miguel — encontrei algo estranho no mercado essa manhã. Um homem estrangeiro — perguntando por nomes.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel fica atento. Pergunta — 'qué nombres?'. Pra você processar — Don Miguel quer saber o que aconteceu (passado):",
                    "options": [
                        {"id": "a", "text": "¿Qué nombres preguntó?"},
                        {"id": "b", "text": "¿Qué nombres pregunta?"},
                        {"id": "c", "text": "Va a preguntar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_pregunto", "target": "preguntó", "native": "perguntou",
                    "npc_reaction": "Preguntó. Tercera persona pasado. Don Miguel quiere saber.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "No supe los nombres. Pero el hombre me vio — y se fijó en mí más de lo que quería. Por eso volví rápido.",
                    "translation": "Não soube os nomes. Mas o homem me viu — e me notou mais do que eu queria. Por isso voltei rápido.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "María falou isso sem disfarçar — uma pequena admissão. "
                        "Don Miguel olhou pra você por um segundo. Você "
                        "entendeu — alguém de fora chegou. E reconhece María."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # María sai pra fazer infusão na cozinha do fundo. Sofía sai do quarto.
    # Miguel também. Reunião rápida dos 4. Decisão: vão atrás desse hombre.
    # Gate: errar trava. Closing prepara F20.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Sofía", "Miguel"],
                "story": (
                    "María foi pra cozinha do fundo — diz que precisa de fogo "
                    "específico pra infusão. Vocês 4 reunidos rapidamente na "
                    "cozinha principal. Conversa baixa, urgente.\n\n"
                    "'Hay un hombre nuevo en el pueblo. Buscando nombres. Y "
                    "María lo vio.'"
                ),
                "now": "Decisão rápida. O que fazer com a informação?",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🕯️ Cozinha principal · María na cozinha do fundo · Os 4 conversando baixo",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "¿Oíste lo que dijo María? Un hombre extranjero — pregunta por nombres.",
                    "translation": "Ouviu o que María disse? Um homem estrangeiro — pergunta por nomes.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Você confirma — ouviu sim:",
                    "options": [
                        {"id": "a", "text": "Sí, oí lo que dijo"},
                        {"id": "b", "text": "No oí nada"},
                        {"id": "c", "text": "Voy a oír"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oíste. Bueno. Esto cambia las cosas.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Podemos buscarlo antes de que se vaya. ¿Vamos a la plaza ahora mismo?",
                    "translation": "Podemos procurá-lo antes que ele vá embora. Vamos pra plaza agora mesmo?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Pra você concordar — vamos juntos (algo que sai logo):",
                    "options": [
                        {"id": "a", "text": "Sí, vamos a buscarlo"},
                        {"id": "b", "text": "Voy a buscarlo"},
                        {"id": "c", "text": "Va a buscarlo"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos a buscarlo. Pero ¿cómo lo encontramos sin que María sospeche?",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Yo me quedo aquí — con María. Ustedes tres salen — Sofía a la plaza, Miguel a la herrería, el forastero a la padaria. Buscan al hombre.",
                    "translation": "Eu fico aqui — com María. Vocês três saem — Sofía à plaza, Miguel à ferraria, o forasteiro à padaria. Procuram o homem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra você confirmar — pode ir à padaria sozinho? Sim, pode:",
                    "options": [
                        {"id": "a", "text": "Sí, puedo ir solo"},
                        {"id": "b", "text": "No puedo"},
                        {"id": "c", "text": "Voy a ir"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedes. Rosa te conoce — pregúntale si vio al hombre. Discreto.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Si lo encuentras — fíjate cómo es. Alto, bajo, joven, viejo. Y de dónde viene.",
                    "translation": "Se você encontrar — repara como ele é. Alto, baixo, jovem, velho. E de onde vem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pediu pra você reparar. Você confirma — vai prestar atenção:",
                    "options": [
                        {"id": "a", "text": "Sí, voy a observarlo"},
                        {"id": "b", "text": "No voy"},
                        {"id": "c", "text": "Soy observar"},
                        {"id": "d", "text": "Estoy observar"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a observarlo", "native": "vou observá-lo",
                    "npc_reaction": "Bien. Y volvemos aquí a las dos de la tarde. María se distrae a esa hora — siempre.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F20 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🏃 Saindo da cozinha · Cada um pra sua direção · Sol já alto",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês 4 se separaram em silêncio. Sofía pra plaza. "
                        "Miguel pra herrería. Você pra padaria de Rosa.\n\n"
                        "Don Miguel ficou na cozinha — María fazendo infusão. "
                        "Como se fosse uma manhã normal. Mas dentro do peito de "
                        "todos vocês, uma palavra pulsava — 'vuelves'. E uma "
                        "pergunta — 'quién es ese hombre?'"
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
