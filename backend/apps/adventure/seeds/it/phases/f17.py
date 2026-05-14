"""
Seed das 6 seções da Fase 17 Italiano A1 — "Pietro y la marca".

Antonio il Contadino marca o encontro no pátio da herrería ao fim do dia. Pietro,
Lucia, Antonio il Contadino e você. Chiara e Nico ficam de fora (Pietro pediu
discrição).

Pietro abre a camisa parcialmente — uma marca tatuada nas costas.
Símbolo antigo. Lucia reconhece sem disfarçar. Lucia explica: é o
símbolo dos Buscadores — uma irmandade que rastreava palavras antigas.
Pietro saiu décadas atrás. Mas reconheceu Lucia quando ela chegou
ao borgo.

Lucia admite: 'Mi familia tenía relación con esa gente.'
Antonio il Contadino olha pra Lucia diferente. Nada igual depois.

VOCAB NOVO (3): espalda · marca · familia
LINGUAGEM NOVA: ya / todavía no  (já / ainda não)
    ya lo sé · todavía no entiendo · ya no me acuerdo

Revisão F1-F16 dominante:
  · quiero + verbo (F16) — recém aprendido
  · vi/hablé/oí (F12)
  · mi/tu/su (F13)
  · el/la (F14)
  · sono/sto/ho (F8)

NPC principais: Pietro · Lucia · Antonio il Contadino · você (silencioso a maior parte)
Arco emocional: descoberta → tensão silenciosa → fissura no grupo
Transição: F18 abre com você decidindo contar a Chiara e Nico.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Amanhecer. Encontro no pátio da herrería. Apresentações tensas. 3 novos
    # exer + 2 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌄 Pátio da herrería · Amanhecer · Fogo ainda apagado\n\n"
                        "Antonio il Contadino acordou você prima do sol. Saíram juntos sem "
                        "barulho. Lucia estava na cozinha — chá pronto, esperando. "
                        "'Bene. Pietro nos espera adesso.'\n\n"
                        "Os três caminharam três quadras. Sem palavras."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "Pietro estava no pátio. Camisa solta. Mãos cruzadas atrás das costas.",
                },
                {
                    "kind": "npc",
                    "npc": "Pietro",
                    "line": "Antonio il Contadino. Lucia. Forestiero. Grazie por venire tan temprano.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Lucia",
                    "line": "Pietro. Benes días.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Lucia olha pra Pietro. Pietro olha pra Lucia. Como dois pelagprima que se reconhecem piu fingem o contrário.",
                },
                {
                    "kind": "npc",
                    "npc": "Pietro",
                    "line": "Lo que vado a mostrar — lo cargo en la espalda hace cuarenta años.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "espalda", "native": "costas"},
                        {"target": "marca",   "native": "marca / símbolo"},
                        {"target": "familia", "native": "família"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro disse 'lo cargo en la espalda'. A palavra 'espalda' significa:",
                    "options": [
                        {"id": "a", "text": "Costas"},
                        {"id": "b", "text": "Cabeça"},
                        {"id": "c", "text": "Mãos"},
                        {"id": "d", "text": "Pés"},
                    ],
                    "correct": "a",
                    "word_id": "it_espalda", "target": "espalda", "native": "costas",
                    "npc_reaction": "La espalda. Donde guardamos lo que no queremos enseñar a nadie.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Você cumprimenta Pietro — amanhecer, formale:",
                    "options": [
                        {"id": "a", "text": "Benes días, Pietro"},
                        {"id": "b", "text": "Buon pomeriggio"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Benes días, giovane. Hoy es día de verdades.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Vado a quitarme la camisa. No del todo — solo lo suficiente.",
                    "translation": "Vou tirar a camisa. Não toda — só o suficiente.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Pietro desabotoa devagar. Vira de costas. Empurra a camisa "
                        "pra baixo até o meio das costas — sem revelar tudo.\n\n"
                        "Você vê. Lucia vê. Antonio il Contadino vê.\n\n"
                        "Uma tatuagem velha. Linhas finas formando um símbolo "
                        "que parece um sol partido."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro mostra um desenho velho tatuado nas costas — um símbolo que significa algo antigo. Como se chama essa coisa nas costas dele?",
                    "options": [
                        {"id": "a", "text": "Marca"},
                        {"id": "b", "text": "Mano"},
                        {"id": "c", "text": "Naranja"},
                        {"id": "d", "text": "Casa"},
                    ],
                    "correct": "a",
                    "word_id": "it_marca", "target": "marca", "native": "marca",
                    "npc_reaction": "Marca. Lo que llevo escrito en la piel. Nadie me lo borra.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia olha fixo pra marca. Murmura algo. Pra você descrever o que sente em italiano simples:",
                    "options": [
                        {"id": "a", "text": "Sto male"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_male", "target": "sto male", "native": "estou male",
                    "npc_reaction": "Tranquilo, forestiero. Guarda senza moverte.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Lucia reconhece. Não disfarça. Confronto inicial. 100% revisão F1-F16.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Pietro", "Lucia", "Antonio il Contadino"],
                "story": (
                    "Lucia olha pra marca por longo segundo. Quando fala, "
                    "fala mais baixo do que costuma.\n\n"
                    "'Pietro — esa marca. Yo conozco.'"
                ),
                "now": "Lucia reconhece. Pietro testa. Cada palavra dela é avaliada.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Ya lo sé que la conoces. Por questo te pedí que vinieras.",
                    "translation": "Já sei que você conhece. Por isso pedi pra você vir.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro disse 'ya lo sé que la conoces'. Pra você confirmar pra Antonio il Contadino que ouviu (já passou — ouvi):",
                    "options": [
                        {"id": "a", "text": "Sí, lo oí"},
                        {"id": "b", "text": "Sí, lo oigo"},
                        {"id": "c", "text": "Vado a oír"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oíste. Bene. Esto debe ser dicho — y oído.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Lucia — explica. ¿Qué es esa marca?",
                    "translation": "Lucia — explica. O que é essa marca?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia diz 'vado a contarlo'. Como Antonio il Contadino responde — esperando (algo que andiamo fazer logo):",
                    "options": [
                        {"id": "a", "text": "Andiamo a ascoltar"},
                        {"id": "b", "text": "Vado a ascoltar"},
                        {"id": "c", "text": "Va a ascoltar"},
                        {"id": "d", "text": "Sono ascoltar"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo. Los tres — Pietro, Antonio il Contadino y yo. Y el forestiero también.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Es la marca de los Buscadores. Una hermandad antigua. Buscaban parole antiche — parole que cambian el mundo si se dicen bene.",
                    "translation": "É a marca dos Buscadores. Uma irmandade antiga. Buscavam palavras velhas — palavras que mudam o mundo se ditas bem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino processa: 'Mi padre me contó historias de esa gente.' Pra você confirmar pra Antonio il Contadino que entendeu (estado de agora — você está bem, atento):",
                    "options": [
                        {"id": "a", "text": "Sto bene, te escucho"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Vado bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Bene. Sigue atento — esto te concierne más de lo que crees.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Yo entré en la hermandad cuando tenía dieciocho. Salí cuando tenía treinta. Hace cuarenta años de questo.",
                    "translation": "Eu entrei na irmandade quando tinha dezoito. Saí quando tinha trinta. Faz quarenta anni disso.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro agora tem... quantos anni?Vocês contam: 30 quando saiu + 40 anni depois = 70 anni. Pra confirmar (usando tener + idade):",
                    "options": [
                        {"id": "a", "text": "Pietro ha setenta años"},
                        {"id": "b", "text": "Pietro es setenta"},
                        {"id": "c", "text": "Pietro va a tener"},
                        {"id": "d", "text": "Pietro sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "tener años", "native": "ter anni",
                    "npc_reaction": "Ho. Setenta. Viejo, sí — ma todavía con dos manni firmes.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Cuando vi a Lucia en el mercato hace dos meses, la reconocí. Ma no por su cara — por su forma de guardar las cose. Esatto lo aprenden los Buscadores.",
                    "translation": "Quando vi Lucia no mercato faz dois meses, reconheci ela. Mas não pela cara — pelo jeito dela de olhar as coisas. Isso os Buscadores aprendem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro disse 'la reconocí' — algo que ele já fez. Pra você confirmar a Antonio il Contadino — você reconheceu Bianca no primeiro dia também:",
                    "options": [
                        {"id": "a", "text": "Yo reconocí a Bianca también"},
                        {"id": "b", "text": "Yo reconozco"},
                        {"id": "c", "text": "Vado a reconocer"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_reconoci", "target": "reconocí", "native": "reconheci",
                    "npc_reaction": "Reconocí — yo, ya pasado. La 'í' fuerte.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Lucia admite a relação da família dela com os Buscadores. Pietro
    # pergunta o sobrenome real. Lucia nega. Apresentação de "ya / todavía no"
    # natural — Pietro e Lucia usam várias vezes.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Pietro", "Lucia", "Antonio il Contadino"],
                "story": (
                    "Pietro ainda de costas, camisa metade pra cima. Não se "
                    "vira. Antonio il Contadino pega a camisa dele, ajuda a fechar.\n\n"
                    "'Bene — me cubro. Ma prima — Lucia. Te pregunto "
                    "directamente.'"
                ),
                "now": "Pietro confronta Lucia. Vocês ouvem. Pode ser chamado.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Lucia — ¿tu también eras de la hermandad?",
                    "translation": "Lucia — você também era da irmandade?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "No. Yo no. Ma mi familia tenía relación con esa gente.",
                    "translation": "Não. Eu não. Mas minha família tinha relação com essa gente.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia disse 'mi familia tenía relación'. A palavra 'familia' significa:",
                    "options": [
                        {"id": "a", "text": "Família (mãe, pai, irmãos)"},
                        {"id": "b", "text": "Casa"},
                        {"id": "c", "text": "Vizinho"},
                        {"id": "d", "text": "Amigo"},
                    ],
                    "correct": "a",
                    "word_id": "it_familia", "target": "familia", "native": "família",
                    "npc_reaction": "Familia. La sangre — los que vinieron prima y los que vienen después.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "¿Tu apellido — es Sangra?",
                    "translation": "Teu sobrenome — é Sangra?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Silêncio. Lucia não responde rápido. Antonio il Contadino olha "
                        "pra ela. Você olha pra ela.\n\n"
                        "Ela acaba decidindo não responder. Mas o silêncio fala."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Ya no uso ese apellido. Hace años.",
                    "translation": "Já não uso esse sobrenome. Faz anni.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia disse 'ya no uso ese apellido'. A palavrinha 'ya' significa:",
                    "options": [
                        {"id": "a", "text": "Já (algo que mudou, agora é assim)"},
                        {"id": "b", "text": "Ainda não"},
                        {"id": "c", "text": "Vou"},
                        {"id": "d", "text": "Sou"},
                    ],
                    "correct": "a",
                    "word_id": "it_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya. Prima lo usaba — hoy no. Esa palabrita marca cambio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Ma el apellido — ¿era Sangra?",
                    "translation": "Mas o sobrenome — era Sangra?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Todavía no te lo confirmo. No es momento.",
                    "translation": "Ainda não te confirmo. Não é momento.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia disse 'todavía no te lo confirmo'. A junção 'todavía no' significa:",
                    "options": [
                        {"id": "a", "text": "Ainda não (talvez depois)"},
                        {"id": "b", "text": "Já não"},
                        {"id": "c", "text": "Nunca"},
                        {"id": "d", "text": "Sempre"},
                    ],
                    "correct": "a",
                    "word_id": "it_ancora_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Es 'todavía' + 'no'. Significa que algo aún no pasa — ma podría pasar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Entiendo. Ma — algún día vas a tener que decirlo. Aquí o en otro lugar.",
                    "translation": "Entendo. Mas — algum dia vai ter que dizer. Aqui ou em outro lugar.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro aponta pra ele mesmo. 'Io sono más viejo que tu — ma ya no sono ___.' Pietro tem 70. Pra falar que ele NÃO é jovem:",
                    "options": [
                        {"id": "a", "text": "giovane"},
                        {"id": "b", "text": "alto"},
                        {"id": "c", "text": "bajo"},
                        {"id": "d", "text": "delgado"},
                    ],
                    "correct": "a",
                    "word_id": "it_giovane", "target": "giovane", "native": "jovem",
                    "npc_reaction": "Jovieni. Ya no. Ma la palabra no cambia con hombre o mujer — siempre 'giovane'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Ma ya entiendes que hay algo grande detrás de todo esto, ¿verdad?",
                    "translation": "Mas você já entende que tem algo grande por trás de tudo isso, né?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Confirmação simples — sim, você já entende isso pelo menos:",
                    "options": [
                        {"id": "a", "text": "Sí, ya entiendo questo"},
                        {"id": "b", "text": "No, todavía no"},
                        {"id": "c", "text": "Vado a entender"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya. Esatto es lo mínimo que necesitas saber por adesso.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Você precisa agradecer Pietro pela coragem de mostrar a marca:",
                    "options": [
                        {"id": "a", "text": "Grazie, Pietro"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Sto male"},
                        {"id": "d", "text": "Sono grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Si necesitan saber más — yo cuento. Ma chi decide cuándo es Lucia.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Saindo da herrería. Antonio il Contadino para você na rua e explica devagar
    # "ya / todavía no". Sem nomear "advérbio". Apenas: palavrinhas que dizem
    # quando algo mudou ou ainda não mudou.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino"],
                "story": (
                    "Vocês 3 (Lucia separada à fronte, andando rápido sozinha) "
                    "saem da herrería. Antonio il Contadino encosta na parede de adobe e "
                    "te chama com a mão.\n\n"
                    "'Jovieni — quiero enseñarte una cosa que oíste mucho ahí dentro.'"
                ),
                "now": "Antonio il Contadino mostra come 'ya' e 'todavía no' funcionam.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "'Ya' y 'todavía no'. Son parole del tiempo. Ma diferentes de 'hoy', 'ayer', 'mañana'.",
                    "translation": "'Ya' e 'todavía no'. São palavras do tempo. Mas diferentes de 'hoy', 'ayer', 'mañana'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ya = já (mudou pra esse estado)",
                    "meaning": "algo aconteceu, mudou de estado, agora é assim",
                    "note": "ya entiendo (entendi e continuo entendendo) · ya no uso (parei de usar)",
                },
                {
                    "kind": "reveal",
                    "phrase": "Todavía no = ainda não (talvez depois)",
                    "meaning": "algo ainda não aconteceu, piu pode acontecer",
                    "note": "todavía no entiendo (não entendo agora — piu vou) · todavía no acepto",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "YA ",       "isKey": True},
                        {"text": "entiendo · ", "isKey": False},
                        {"text": "TODAVÍA NO ", "isKey": True},
                        {"text": "entiendo",   "isKey": False},
                    ],
                    "example": "Ya entiendo el borgo. Todavía no entiendo a Lucia. Ya hablo poco español. Todavía no leo bene.",
                    "translation": "Já entendo o borgo. Ainda não entendo Lucia. Já falo um pouco de italiano. Ainda não leio bem.",
                    "note": "'ya' = cambio que ya pasó · 'todavía no' = cambio que falta",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você já conhece Bianca, Giulia, Pietro, Antonio il Contadino, Chiara, Nico, Lucia. Pra dizer 'já conheço o borgo':",
                    "options": [
                        {"id": "a", "text": "Ya conozco el borgo"},
                        {"id": "b", "text": "Todavía no conozco"},
                        {"id": "c", "text": "Vado a conocer"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya. Esatto es. Conoces — ya no eres extraño.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Mas você ainda não sabe ler a carta da Antonio il Contadino (que vai aparecer logo). Pra dizer 'ainda não leio':",
                    "options": [
                        {"id": "a", "text": "Todavía no leo bene"},
                        {"id": "b", "text": "Ya leo bene"},
                        {"id": "c", "text": "Vado a leer"},
                        {"id": "d", "text": "Sono leer"},
                    ],
                    "correct": "a",
                    "word_id": "it_ancora_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Ma pronto. Esa palabra te dice — espera, hay tiempo aún.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Si alguien te pregunta '¿estás listo?' y todavía no — dices 'todavía no'. Si ya estás — dices 'ya sto'.",
                    "translation": "Se alguém te pergunta 'está pronto?' e ainda não — diz 'todavía no'. Se já está — diz 'ya sto'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino testa: '¿Estás listo para hablar con Lucia sobre todo esto?' Você ainda não tá:",
                    "options": [
                        {"id": "a", "text": "Todavía no"},
                        {"id": "b", "text": "Ya"},
                        {"id": "c", "text": "Vado a"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ancora_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Bene. Topiu tu tiempo — questo es sabiduría.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Caminho de volta. Lucia à fronte — silenciosa. Antonio il Contadino ao seu lado.
    # Conversa baixa. Decisão silenciosa: vão observar mais prima de confrontar.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Lucia"],
                "story": (
                    "Vocês caminham de volta. Lucia vai na fronte — 20 passos "
                    "adiante. Sem olhar pra trás. Antonio il Contadino ao seu lado.\n\n"
                    "'Hijo — vado a hablarte de algo. En voz baja. Que ella no oiga.'"
                ),
                "now": "Decisão silenciosa entre você e Antonio il Contadino sobre o que fazer.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Hoy supimos mucho. Ma todavía no sabemos lo más importante — quién era la familia de Lucia prima.",
                    "translation": "Hoje soubemos muito. Mas ainda não sabemos o mais importante — quem era a família de Lucia prima.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino diz 'ya supimos mucho'. Pra você concordar que SIM, vocês já sabem muito:",
                    "options": [
                        {"id": "a", "text": "Sí, ya sabemos mucho"},
                        {"id": "b", "text": "No, todavía no sabemos"},
                        {"id": "c", "text": "Andiamo a saber"},
                        {"id": "d", "text": "Sono mucho"},
                    ],
                    "correct": "a",
                    "word_id": "it_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya. Ma hace falta más.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Yo quiero que tu no le digas a Lucia que estuvimos hablando solos en el camino.",
                    "translation": "Eu quero que você não fale pra Lucia que estivemos falando sozinhos no caminho.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino disse 'yo quiero que tu no le digas'. Pra você confirmar que NÃO vai contar (querer + verbo):",
                    "options": [
                        {"id": "a", "text": "No quiero decirle nada"},
                        {"id": "b", "text": "Quiero decirle todo"},
                        {"id": "c", "text": "Vado a decirle"},
                        {"id": "d", "text": "Sono decirle"},
                    ],
                    "correct": "a",
                    "word_id": "it_quiero", "target": "quiero decirle", "native": "quero contar",
                    "npc_reaction": "Bene. 'No quiero decirle' — clara la posición. Esatto me tranquiliza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Chiara y Nico — ¿qué hacemos con ellos?¿Les contamos?",
                    "translation": "Chiara e Nico — o que fazemos com eles?Contamos pra eles?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Antonio il Contadino tá te dando o poder de decidir isso. Chiara e "
                        "Nico já sabem o passado de Bianca com o Podesta (F16). "
                        "Agora vocês têm a marca. Eles merecem saber tudo."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Sua decisão — sim, contar pra eles (algo que andiamo fazer):",
                    "options": [
                        {"id": "a", "text": "Sí, andiamo a decirles"},
                        {"id": "b", "text": "No, no quiero"},
                        {"id": "c", "text": "Vado a decirles"},
                        {"id": "d", "text": "Sono decirles"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo a decirles. Esta notte. Cuando Lucia se duerma — los reunimos.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lucia já estava chegando na esquina da rua. Vocês "
                        "apertaram o passo pra alcançá-la. Quando chegaram do "
                        "lado dela, ela estava tranquila — come se a manhã "
                        "tivesse sido normale."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Ya está hecho. Pietro está tranquilo. Antonio il Contadino — grazie por organizar el encuentro.",
                    "translation": "Já está feito. Pietro está tranquilo. Antonio il Contadino — obrigada por organizar o encontro.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Antonio il Contadino responde calmo — 'de nada':",
                    "options": [
                        {"id": "a", "text": "De nada, Lucia"},
                        {"id": "b", "text": "Adiós Lucia"},
                        {"id": "c", "text": "Ho nada"},
                        {"id": "d", "text": "Sono nada"},
                    ],
                    "correct": "a",
                    "word_id": "it_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Andiamo a casa. Quiero descansar.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Noite. Você espera Lucia dormir. Sai com Antonio il Contadino pra falar com Chiara
    # e Nico. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Chiara", "Nico"],
                "story": (
                    "A casa silenciou. Lucia foi pro quarto cedo — disse que "
                    "queria descansar muito. Vocês esperaram uma hora. Quando "
                    "ouviram a respiração dela fundo do outro lado da parede, "
                    "Antonio il Contadino acenou.\n\n"
                    "Saíram baixo pela porta dos fundos. Foram até a casa de "
                    "Chiara — onde Nico já tinha avisado que ia estar."
                ),
                "now": "Reunião secreta dos 4. Você precisa contar tudo.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌙 Casa de Chiara · Noite · Lamparina baixa · Quatro sentados em volta de uma mesa pequena",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Hablen. ¿Qué pasó esta mañana?",
                    "translation": "Falem. O que aconteceu essa manhã?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Você começa — sim, vocês viram a marca:",
                    "options": [
                        {"id": "a", "text": "Sí, vi la marca de Pietro"},
                        {"id": "b", "text": "No vi nada"},
                        {"id": "c", "text": "Vado a verla"},
                        {"id": "d", "text": "Sono marca"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. ¿Y Lucia — qué ha detto?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Pra contar o que Lucia disse (já passou, sobre ela):",
                    "options": [
                        {"id": "a", "text": "Ha detto que conoce esa marca"},
                        {"id": "b", "text": "Dice que conoce"},
                        {"id": "c", "text": "Va a decir"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ha detto", "target": "ha detto", "native": "ele/ela disse",
                    "npc_reaction": "Ha detto. Bene. ¿Y Pietro le preguntó algo más?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Você conta — Pietro perguntou o sobrenome dela. Lucia disse 'todavía no te confirmo'. Para confirmar pra Nico a posição dela:",
                    "options": [
                        {"id": "a", "text": "Todavía no confirma"},
                        {"id": "b", "text": "Ya confirma"},
                        {"id": "c", "text": "Va a confirmar"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ancora_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no. Bene escogió tus parole — questo es exacto.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Tres pistas tenemos ya: lo que Bianca contó del Podesta, lo que mi mujer Lucía senzatió, y adesso la marca de Pietro. Tres puntos en una línea.",
                    "translation": "Três pistas já temos: o que Bianca contou do Podesta, o que minha mulher Lucía sentiu, e agora a marca de Pietro. Três pontos numa linha.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Chiara pergunta: '¿Y qué andiamo a hacer adesso?' Antonio il Contadino responde — andiamo observar. Como Chiara concorda?",
                    "options": [
                        {"id": "a", "text": "Andiamo a observar"},
                        {"id": "b", "text": "Vado a observar"},
                        {"id": "c", "text": "Va a observar"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo a observar. Ma hay algo más — algo que ya no podemos posponer.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Antonio il Contadino respirou fundo. Olhou pra você. Pra Chiara. Pra Nico. Decidiu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Mañana — vado a enseñarles la carta. La que ho guardada hace veinte años. El forestiero ya la necesita.",
                    "translation": "Amanhã — vou mostrar pra vocês a carta. A que tenho guardada faz vinte anni. O forasteiro já precisa dela.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico: 'Una carta tuya, papá?¿De qué carta hablas?' Antonio il Contadino: 'Mañana. Adesso todos a dormir.' Você responde — concorda, vão dormir:",
                    "options": [
                        {"id": "a", "text": "Andiamo a dormir"},
                        {"id": "b", "text": "Vado a dormir"},
                        {"id": "c", "text": "Va a dormir"},
                        {"id": "d", "text": "Sono dormir"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo. Mañana al amanecer — los cuatro. La carta cambia todo.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F18 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🌃 Caminho de volta · Você e Antonio il Contadino · Lucia dormindo profundo",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês voltaram baixo. Entraram pela porta dos fundos. "
                        "Lucia dormindo profundo — você ouviu a respiração dela "
                        "calma na parede.\n\n"
                        "Você deitou. Não dormiu. A palavra 'carta' girava na "
                        "cabeça. Antonio il Contadino — homem que guardou um segredo "
                        "vinte anni — ia abrir um baú amanhã."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────


