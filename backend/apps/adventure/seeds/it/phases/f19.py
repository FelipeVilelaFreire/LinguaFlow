"""
Seed das 6 seções da Fase 19 Italiano A1 — "La carta".

⚠️ MILESTONE OBRIGATÓRIO (canônico — story.md):
    F19 = 4ª fase de revisão. A primera palabra da carta torna-se
    legível. O protagonista já fala o suficiente.

Antonio il Contadino abre o baú. Mostra o envelope selado. Os 4 giovanes reunidos
ao amanhecer (Lucia saiu cedo de novo — Antonio il Contadino arranjou).

Quase tudo na carta está ilegível pro forestiero. Mas no centro — uma
palavra ficou clara. Escura. Pulsando. Você LÊ.

A palavra é: **"TORNI."** (você volta)

Não entende o sentido completo. Mas sabe que isso muda tudo.

ABORDAGEM PEDAGÓGICA:
    Fase de REVISÃO PESADA. Apresenta apenas vocab narrativo (carta,
    leer, palabra, abrir). Sem nova linguagem gramatical relevante.
    Foco em REVISÃO de F1-F18 — sono/sto/ho, vado a, mi/tu/su,
    el/la, vi/hablé/oí, ya/todavía no, puedo, quiero.

VOCAB NOVO (3): carta · leer · abrir
Apresentação adicional: palabra (já conhecido em uso geral)

NPC principais: Antonio il Contadino · Chiara · Nico · você
Arco emocional: expectativa → revelação parcial → confusão → começar a
                aceitar que tem origem e propósito desconhecidos
Transição: F20 abre com o grupo decidindo o próximo passo — confrontar
            Lucia ou continuar observando.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Amanhecer. Os 4 reunidos. Antonio il Contadino abre o baú. Cara da carta selada.
    # 2 novos + 2 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌄 Casa de Antonio il Contadino · Amanhecer · Cozinha\n\n"
                        "Antonio il Contadino arranjou que Lucia fosse ao mercato bem cedo "
                        "— pediu coisas que só vienidem ao amanhecer. Lucia saiu "
                        "às cinco. Chiara e Nico chegaram às cinco e meia. Os "
                        "quatro sentados em volta do baú aberto."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Aquí está. Veinte años en este baúl.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Ele pega o envelope. Cera vermelha grossa selando. Símbolo do sol partido — igual à marca de Pietro.",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "Ese sello — es el mismo símbolo de la espalda de Pietro.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Sí. La carta vino del viejo Buscador que llegó al borgo hace veinte años.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Antonio il Contadino pousa a carta no centro da mesa. Não abriu ainda. Só pousou. Quatro olhos fixos nela.",
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
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino pousou um envelope grosso, fechado com cera. Como se chama essa coisa?",
                    "options": [
                        {"id": "a", "text": "Carta"},
                        {"id": "b", "text": "Marca"},
                        {"id": "c", "text": "Familia"},
                        {"id": "d", "text": "Espalda"},
                    ],
                    "correct": "a",
                    "word_id": "it_carta", "target": "carta", "native": "carta",
                    "npc_reaction": "Carta. Lo que ha parole dentro — ma todavía cerrada.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta a Antonio il Contadino — '¿La andiamo a ___?' Pra dizer 'abrir' (verbo base):",
                    "options": [
                        {"id": "a", "text": "abrir"},
                        {"id": "b", "text": "cerrar"},
                        {"id": "c", "text": "comer"},
                        {"id": "d", "text": "ver"},
                    ],
                    "correct": "a",
                    "word_id": "it_abrir", "target": "abrir", "native": "abrir",
                    "npc_reaction": "Abrir. Andiamo a abrirla — adesso mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino agradece pela paciência de vocês. Vocês cumprimentam — amanhecer:",
                    "options": [
                        {"id": "a", "text": "Benes días, Antonio il Contadino"},
                        {"id": "b", "text": "Buona notte"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Benes días. Andiamo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino pergunta 'forestiero — ¿cómo estás adesso?':",
                    "options": [
                        {"id": "a", "text": "Ho paura, ma sto listo"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_paura", "target": "ho paura", "native": "tenho medo",
                    "npc_reaction": "Las dos cose a la vez — questo es lo corretto. Honesto.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Antonio il Contadino pede que cada um diga em voz alta o que sabe
    # — pra que todos estejam na mesma página prima da carta. Revisão da
    # história até aqui.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Chiara", "Nico"],
                "story": (
                    "Antonio il Contadino pousou a mão na carta. Não vai abrir ainda.\n\n"
                    "'Prima de abrir — quiero que cada uno diga lo que sabe. Para "
                    "que estemos todos en la misma página.'"
                ),
                "now": "Revisão narrativa. Cada um conta o que viu/ouviu/sentiu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Forestiero — empieza tu. ¿Cuándo sei arrivato al borgo?",
                    "translation": "Forasteiro — começa você. Quando você chegou ao borgo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você chegou faz duas semanas. Pra falar simples — 'cheguei sem memória, sem nome':",
                    "options": [
                        {"id": "a", "text": "Llegué senza memoria"},
                        {"id": "b", "text": "Llego senza memoria"},
                        {"id": "c", "text": "Vado a llegar"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_arrivi", "target": "llegué", "native": "cheguei",
                    "npc_reaction": "Llegué. Bene. Y conociste a Giulia primero — y después a mí.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Pra confirmar — você viu Giulia primeiro:",
                    "options": [
                        {"id": "a", "text": "Sí, vi a Giulia primero"},
                        {"id": "b", "text": "Sí, veo a Giulia"},
                        {"id": "c", "text": "Vado a ver"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Y la palabra primera que aprendiste fue 'pane'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Chiara — y tu. ¿Cuándo lo viste por primera vez?",
                    "translation": "Chiara — e você. Quando o viu pela primeira vez?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Yo lo vi en tu cuarto la notte del fuoco. La notte de la primera scintilla.",
                    "translation": "Eu o vi no teu quarto na noite do fogo. A noite da primeira scintilla.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Chiara disse 'lo vi'. Você confirma — Chiara também viu o fogo:",
                    "options": [
                        {"id": "a", "text": "Sí, ella vio el fuoco"},
                        {"id": "b", "text": "Sí, ella ve el fuoco"},
                        {"id": "c", "text": "Va a ver"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_vio", "target": "vio", "native": "viu (3ª)",
                    "npc_reaction": "Vio. Tercera persona. Chiara vio — ya pasado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Nico — y tu. ¿Lo conoces desde cuándo?",
                    "translation": "Nico — e você. Conhece ele desde quando?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Desde el primer día. Mi padre me llamó — '¡MIGUEL! ¡HAY UN FORASTERO!'. Y vine corriendo.",
                    "translation": "Desde o primeiro dia. Meu pai me chamou — '¡MIGUEL! ¡TEM UM FORASTERO!'. E vim correndo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico disse 'mi padre me llamó'. Pra você responder pra Nico — sim, ele veio correndo (já passou):",
                    "options": [
                        {"id": "a", "text": "Sí, viniste corriendo"},
                        {"id": "b", "text": "Sí, vieni corriendo"},
                        {"id": "c", "text": "Vado a venire"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_viniste", "target": "viniste", "native": "vieste",
                    "npc_reaction": "Viniste. Tu — segunda. Como 'hablaste' o 'viste'. Forma del pasado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Y Lucia llegó al borgo hace dos meses. Esatto nos lo ha detto ella misma — la notte que cuidó al forestiero.",
                    "translation": "E Lucia chegou ao borgo faz dois meses. Isso ela mesma nos disse — na noite que cuidou do forasteiro.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino pergunta: '¿Por qué llegó al borgo?¿Saben alguien?' Resposta honesta — vocês ainda não sabem:",
                    "options": [
                        {"id": "a", "text": "Todavía no sabemos"},
                        {"id": "b", "text": "Ya sabemos"},
                        {"id": "c", "text": "Andiamo a saber"},
                        {"id": "d", "text": "Somos"},
                    ],
                    "correct": "a",
                    "word_id": "it_ancora_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Ma la carta puede ayudarnos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara: '¿Cómo te sientes adesso, forestiero — prima de abrir la carta?'",
                    "options": [
                        {"id": "a", "text": "Sto nervioso"},
                        {"id": "b", "text": "Sono nervioso"},
                        {"id": "c", "text": "Ho nervioso"},
                        {"id": "d", "text": "Vado nervioso"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_nervioso", "target": "sto nervioso", "native": "estou nervoso",
                    "npc_reaction": "Nervioso. Estado de adesso — bene usado. Esatto pasa rápido cuando ya sabes lo que viene.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Antonio il Contadino abre a carta. Quebra o selo. Tira o papel. Você lê. Quase
    # tudo ilegível. Apenas 1 palavra clara: 'TORNI'. Foco em revisão de
    # F1-F18 com situações de leitura.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Chiara", "Nico"],
                "story": (
                    "Antonio il Contadino pegou a faca pequena que sempre tem na cinta. "
                    "Cortou o selo de cera. Quebrou em dois. Tirou o papel "
                    "amarelado de dentro.\n\n"
                    "'Guarda tu primero. Solo. Después noi.'"
                ),
                "now": "Você lê a carta. Quase tudo confuso. Mas uma palavra fica clara.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "📄 Papel amarelado · Tinta velha · Algupiu linhas borradas · Você segurando",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você olha. Há linhas escritas — piu as letras se misturam, "
                        "se borram quando você foca. Como se as palavras não "
                        "quisessem ser lidas ainda.\n\n"
                        "Exceto uma — no centro. Mais escura. Mais grossa.\n\n"
                        "**TORNI.**"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "¿Puedes leer algo?",
                    "translation": "Você pode ler algo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino pergunta se você pode ler. Honesto — uma palavra só. Pra dizer 'posso ler una palabra':",
                    "options": [
                        {"id": "a", "text": "Puedo leer una palabra"},
                        {"id": "b", "text": "No puedo leer"},
                        {"id": "c", "text": "Vado a leer"},
                        {"id": "d", "text": "Sono leer"},
                    ],
                    "correct": "a",
                    "word_id": "it_puedo", "target": "puedo leer", "native": "posso ler",
                    "npc_reaction": "Puedo leer. Una palabra es suficiente. ¿Cuál?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você fala a palavra em voz alta — 'TORNI'. Como você descreve isso?Esta palavra significa:",
                    "options": [
                        {"id": "a", "text": "Você volta"},
                        {"id": "b", "text": "Eu vou"},
                        {"id": "c", "text": "Ele come"},
                        {"id": "d", "text": "Nós saímos"},
                    ],
                    "correct": "a",
                    "word_id": "it_torni", "target": "TORNI", "native": "você volta",
                    "npc_reaction": "TORNI. Tu — TORNI. Esa es la palabra. ¿Y te dice algo?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "TORNI. Como si dijera — 'tu regresas a algún sitio'. Ma — ¿adónde?",
                    "translation": "TORNI. Como se dissesse — 'você retorna a algum lugar'. Mas — pra onde?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta pra você — você lembra de algum lugar de prima?Honesto:",
                    "options": [
                        {"id": "a", "text": "Todavía no me acuerdo"},
                        {"id": "b", "text": "Ya me acuerdo"},
                        {"id": "c", "text": "Vado a acordarme"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                    "npc_reaction": "Todavía no. Ma la palabra está ahí — esperando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "El resto — ¿puedes leer?Inténtalo otra vez.",
                    "translation": "O resto — você pode ler?Tenta outra vez.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você tenta. Quase nada. Resposta honesta — ainda não:",
                    "options": [
                        {"id": "a", "text": "Todavía no puedo leer más"},
                        {"id": "b", "text": "Ya puedo leer todo"},
                        {"id": "c", "text": "Vado a leer"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ancora_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. La carta se abre solo cuando ya puedes leerla. El Buscador me lo ha detto así.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Cada vez que aprendas más — más parole se van a ver. Esatto es lo que él me ha detto hace veinte años.",
                    "translation": "Cada vez que você aprender mais — mais palavras vão ficar visíveis. Isso ele me disse há vinte anni.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico: 'Forestiero — esa palabra — TORNI — ¿qué sientes cuando la lees?' Honesto:",
                    "options": [
                        {"id": "a", "text": "Siento algo en el pecho"},
                        {"id": "b", "text": "No siento nada"},
                        {"id": "c", "text": "Vado a sentir"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_siento", "target": "siento", "native": "senzato",
                    "npc_reaction": "Sientes. Esatto es lo que importa. Tu corpo recuerda lo que tu testa ya no.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara: '¿Cómo estás adesso — después de leer questo?'",
                    "options": [
                        {"id": "a", "text": "Sto mareado, ma bene"},
                        {"id": "b", "text": "Sono mareado"},
                        {"id": "c", "text": "Ho mareado"},
                        {"id": "d", "text": "Vado mareado"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_mareado", "target": "sto mareado", "native": "estou tonto",
                    "npc_reaction": "Mareado. Es la palabra que abre por dentro. Es normale sentir algo al leerla.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino: 'Vado a guardarla otra vez. Ma — ¿quieres tocarla una vez más prima?'",
                    "options": [
                        {"id": "a", "text": "Sí, quiero tocarla"},
                        {"id": "b", "text": "No quiero"},
                        {"id": "c", "text": "Vado a guardarla"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_quiero", "target": "quiero tocarla", "native": "quero tocá-la",
                    "npc_reaction": "Bene. Tócala. Suavemente.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Antonio il Contadino guarda a carta. Tira do baú um livro velho — registros do
    # borgo. Quer mostrar uma coisa pro forestiero. Aparição de "el/la/los/las"
    # em prática + apresentação suave de quem/lo que (palavras que ligam).
    # ABORDAGEM: revisão dominante + 1 conceito pequeno.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino"],
                "story": (
                    "Antonio il Contadino guardou a carta no baú. Mas tirou um livro velho "
                    "também — capa de couro, páginas amareladas. Registros do "
                    "borgo dos últimos cinquenta anni.\n\n"
                    "'Prima de que Lucia vuelva — vado a enseñarte algo aquí.'"
                ),
                "now": "Antonio il Contadino mostra o registro do borgo. Você aprende a navegar pelos nomes.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Este libro ha los nombres de cada persona que pasó por el borgo. Las familias. Los visitprima. Los Buscadores que vinieron.",
                    "translation": "Este livro tem os nomes de cada pessoa que passou pelo borgo. As famílias. Os visitprima. Os Buscadores que vieram.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino disse 'las familias'. As palavras 'el/la/los/las' que você viu na F14 — quando algo é mulher e plural:",
                    "options": [
                        {"id": "a", "text": "las"},
                        {"id": "b", "text": "los"},
                        {"id": "c", "text": "el"},
                        {"id": "d", "text": "la"},
                    ],
                    "correct": "a",
                    "word_id": "it_las", "target": "las", "native": "as (mulheres / muitas)",
                    "npc_reaction": "Las. Muchas familias — femenino plural.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Aquí — el viejo Buscador. Su nombre era Tomás. Igual que mi padre. Vino en 1845 — hace veinte años.",
                    "translation": "Aqui — o velho Buscador. O nome dele era Tomás. Igual ao meu pai. Veio em 1845 — faz vinte anni.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Pra confirmar — esse Tomás VIO algo. Quem era ele?",
                    "options": [
                        {"id": "a", "text": "Era el Buscador"},
                        {"id": "b", "text": "Es el Buscador"},
                        {"id": "c", "text": "Va a ser"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_era", "target": "era", "native": "era",
                    "npc_reaction": "Era. Prima — ya pasado. El Buscador.",
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
                        {"text": "ha detto la carta",     "isKey": False},
                    ],
                    "example": "El viejo chi trajo la carta murió. Lo que ha detto es importante.",
                    "translation": "O velho que trouxe a carta morreu. O que ele disse é importante.",
                    "note": "'chi' = pra pessoas · 'lo que' = pra coisas/ideias.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino: 'El viejo ___ trajo la carta era Buscador.' Pra ligar à pessoa (homem):",
                    "options": [
                        {"id": "a", "text": "chi"},
                        {"id": "b", "text": "lo que"},
                        {"id": "c", "text": "el"},
                        {"id": "d", "text": "la"},
                    ],
                    "correct": "a",
                    "word_id": "it_chi", "target": "chi", "native": "que / quem",
                    "npc_reaction": "Quien. Para personas — siempre. El que / la que también sirvieni.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "'___ leíste hoy es solo el principio.' Pra ligar à coisa (a carta, o que estava nela):",
                    "options": [
                        {"id": "a", "text": "Lo que"},
                        {"id": "b", "text": "Quien"},
                        {"id": "c", "text": "El"},
                        {"id": "d", "text": "La"},
                    ],
                    "correct": "a",
                    "word_id": "it_lo_que", "target": "lo que", "native": "o que",
                    "npc_reaction": "Lo que. Para cose o ideas. Esa frase entra mucho en la testa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você confirma — entende isso ainda parcialmente:",
                    "options": [
                        {"id": "a", "text": "Ya entiendo un poco"},
                        {"id": "b", "text": "Todavía no entiendo nada"},
                        {"id": "c", "text": "Vado a entender"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya un poco. Esatto es suficiente por hoy.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Antonio il Contadino guarda tudo. Lucia chega — pega vocês 4 reunidos. Tensão.
    # Antonio il Contadino reage rápido. Conversa de coversãod. 100% revisão.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Chiara", "Nico", "Lucia"],
                "story": (
                    "Antonio il Contadino já tinha guardado a carta no baú. Tinha fechado. "
                    "Coberto com o paneo. Quando ouviu os passos de Lucia na rua "
                    "lá fora.\n\n"
                    "'Chiara — pasa a mi cuarto, finge que estás lavando algo. "
                    "Nico — junto al fogón. Forestiero — tu quédate aquí.'\n\n"
                    "Lucia entrou com a cesta cheia."
                ),
                "now": "Encontro inesperado com Lucia. Vocês precisam disfarçar.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌅 Cozinha · Lucia entrando com cesta · Você, Antonio il Contadino · Chiara e Nico escondidos",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Benes días. ¿Y los demás?Vi luces aquí desde lejos.",
                    "translation": "Bom dia. E os outros?Vi lucees aqui de longe.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você cumprimenta — manhã clara:",
                    "options": [
                        {"id": "a", "text": "Benes días, Lucia"},
                        {"id": "b", "text": "Buon pomeriggio"},
                        {"id": "c", "text": "Buona notte"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Benes días. ¿Antonio il Contadino — cómo amaneció?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Chiara y Nico vinieron temprano. Chiara está lavando ropa en mi cuarto. Nico arregla el fogón.",
                    "translation": "Chiara e Nico vieram cedo. Chiara está lavando roupa no meu quarto. Nico arruma o fogão.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia pergunta — você sabe o motivo?Resposta segura (vaga):",
                    "options": [
                        {"id": "a", "text": "Quería ayudar a Antonio il Contadino"},
                        {"id": "b", "text": "Vado a ayudar"},
                        {"id": "c", "text": "Sono ayuda"},
                        {"id": "d", "text": "Ho ayuda"},
                    ],
                    "correct": "a",
                    "word_id": "it_queria", "target": "quería ayudar", "native": "queria ajudar",
                    "npc_reaction": "Querían ayudar. Bene. Aprovechemos — yo traje erbe, vado a hacer infusión.",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia vai pra cozinha. Você nota — ela olha pra mesa onde estava o baú. O baú está coberto, fechado. Ela parece satisfeita com o que vê — ou pelo menos não suspeita.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Forestiero — ¿dormiste bene anotte?Te vi pálido al despertar.",
                    "translation": "Forasteiro — dormiu bem ontem à noite?Te vi pálido ao acordar.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você dormiu male — pensando na carta. Mas vai mentir parcialmente — diz que estava cansado:",
                    "options": [
                        {"id": "a", "text": "Sí, estuve cansado"},
                        {"id": "b", "text": "Sí, dormí bene"},
                        {"id": "c", "text": "Vado a dormir"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_estuve", "target": "estuve cansado", "native": "estive cansado",
                    "npc_reaction": "Estuve cansado. Bene. La infusión te va a ayudar hoy.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Antonio il Contadino — encontré algo raro en el mercato esta mañana. Un hombre extranjero — preguntando por nombres.",
                    "translation": "Antonio il Contadino — encontrei algo estranho no mercato essa manhã. Um homem estrangeiro — perguntando por nomes.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino fica atento. Pergunta — 'qué nombres?'. Pra você processar — Antonio il Contadino quer saber o que aconteceu (passado):",
                    "options": [
                        {"id": "a", "text": "¿Qué nombres preguntó?"},
                        {"id": "b", "text": "¿Qué nombres pregunta?"},
                        {"id": "c", "text": "Va a preguntar"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_pregunto", "target": "preguntó", "native": "perguntou",
                    "npc_reaction": "Preguntó. Tercera persona pasado. Antonio il Contadino quiere saber.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "No supe los nombres. Ma el hombre me vio — y se fijó en mí más de lo que quería. Por questo volví rápido.",
                    "translation": "Não soube os nomes. Mas o homem me viu — e me notou mais do que eu queria. Por isso voltei rápido.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lucia falou isso sem disfarçar — uma pequena admissão. "
                        "Antonio il Contadino olhou pra você por um segundo. Você "
                        "entendeu — alguém de fora chegou. E reconhece Lucia."
                    ),
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Lucia sai pra fazer infusão na cozinha do fundo. Chiara sai do quarto.
    # Nico também. Reunião rápida dos 4. Decisão: vão atrás desse hombre.
    # Gate: errar trava. Closenzag prepara F20.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Chiara", "Nico"],
                "story": (
                    "Lucia foi pra cozinha do fundo — diz que precisa de fogo "
                    "específico pra infusão. Vocês 4 reunidos rapidamente na "
                    "cozinha principal. Conversa baixa, urgente.\n\n"
                    "'Hay un hombre nuevo en el borgo. Buscando nombres. Y "
                    "Lucia lo vio.'"
                ),
                "now": "Decisão rápida. O que fazer com a informação?",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🕯️ Cozinha principal · Lucia na cozinha do fundo · Os 4 conversando baixo",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "¿Oíste lo que ha detto Lucia?Un hombre extranjero — pregunta por nombres.",
                    "translation": "Ouviu o que Lucia disse?Um homem estrangeiro — pergunta por nomes.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Você confirma — ouviu sim:",
                    "options": [
                        {"id": "a", "text": "Sí, oí lo que ha detto"},
                        {"id": "b", "text": "No oí nada"},
                        {"id": "c", "text": "Vado a oír"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oíste. Bene. Esto cambia las cose.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Podemos buscarlo prima de que se vaya. ¿Andiamo a la piazza adesso mismo?",
                    "translation": "Podemos procurá-lo prima que ele vá embora. Andiamo pra piazza agora mesmo?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Pra você concordar — andiamo juntos (algo que sai logo):",
                    "options": [
                        {"id": "a", "text": "Sí, andiamo a buscarlo"},
                        {"id": "b", "text": "Vado a buscarlo"},
                        {"id": "c", "text": "Va a buscarlo"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo a buscarlo. Ma ¿cómo lo encontramos senza que Lucia sospeche?",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Yo me quedo aquí — con Lucia. Ustedes tres saleen — Chiara a la piazza, Nico a la herrería, el forestiero a la padaria. Buscan al hombre.",
                    "translation": "Eu fico aqui — com Lucia. Vocês três saem — Chiara à piazza, Nico à ferraria, o forasteiro à padaria. Procuram o homem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Pra você confirmar — pode ir à padaria sozinho?Sim, pode:",
                    "options": [
                        {"id": "a", "text": "Sí, puedo ir solo"},
                        {"id": "b", "text": "No puedo"},
                        {"id": "c", "text": "Vado a ir"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedes. Giulia te conoce — pregúntale si vio al hombre. Discreto.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Si lo encuentras — fíjate cómo es. Alto, bajo, giovane, viejo. Y de dónde viene.",
                    "translation": "Se você encontrar — repara come ele é. Alto, baixo, jovem, velho. E de onde vem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pediu pra você reparar. Você confirma — vai prestar atenção:",
                    "options": [
                        {"id": "a", "text": "Sí, vado a observarlo"},
                        {"id": "b", "text": "No vado"},
                        {"id": "c", "text": "Sono observar"},
                        {"id": "d", "text": "Sto observar"},
                    ],
                    "correct": "a",
                    "word_id": "it_vado_a", "target": "vado a observarlo", "native": "vou observá-lo",
                    "npc_reaction": "Bene. Y volvemos aquí a las dos de la tarde. Lucia se distrae a esa hora — siempre.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F20 ────────────────────────
                {
                    "kind": "scene",
                    "text": "?? Saindo da cozinha · Cada um pra sua direção · Sol já alto",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês 4 se separaram em silêncio. Chiara pra piazza. "
                        "Nico pra herrería. Você pra padaria de Giulia.\n\n"
                        "Antonio il Contadino ficou na cozinha — Lucia fazendo infusão. "
                        "Como se fosse uma manhã normale. Mas dentro do peito de "
                        "todos vocês, uma palavra pulsava — 'TORNI'. E uma "
                        "pergunta — 'quién es ese hombre?'"
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




