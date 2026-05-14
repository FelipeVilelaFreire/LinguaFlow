"""
Seed das 6 seções da Fase 12 Italiano A1 — "Tres días".

Bianca aceitou testemunhar. Pietro aceitou (com a condição estranha
sobre as costas). Falta um terceiro testigo imparcial. Esta fase
apresenta o PASSADO de forma natural — porque pra testemunhar é
preciso contar o que aconteceu prima.

ABORDAGEM PEDAGÓGICA:
    Os NPCs usam o passado naturalmente. O aluno aprende pelo uso —
    "vi", "oí", "hablé" aparecem em situações claras. Sem termo
    técnico. Sem tabela de conjugação. Bianca e Pietro são quem
    usam, e o jogador entende pelo contexto.

Vocab novo (2): ayer · vi
Apresentação adicional: oí · hablé (no vocab_list, sem foco em todos)

Revisão F1-F11 dominante:
  · mi chiamo / sono forestiero (F1, F8, F11)
  · ho veinte años (F7, F11)
  · sto bene (F8, F11)
  · mi piace / no mi piace (F9)
  · andiamo a (F11) — futuro próximo já conhecido
  · grazie / buongiorno (F1)
  · vecino (F7) — Bianca e Pietro são vecinos imparciales

NPC principais: Bianca · Pietro · Chiara · Antonio il Contadino · Lucia
NPC tensão:     La Guardia (vigia o grupo)
Arco emocional: trabalho em equipe → tensão sobre o 3º testigo
Transição:      F13 abre com Nico propondo levar o grupo pra casa
                da mãe dele essa noite.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Manhã do segundo dia. Bianca ensaiando com Chiara. Apresentação suave
    # do passado — Bianca usa "vi", "hablé" em conversa real. 1 exercício
    # novo sobre 'ayer' + revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "☀️ Manhã do segundo dia · Casa de Antonio il Contadino · Cozinha cheia\n\n"
                        "Bianca sentada à mesa com Chiara explicando o protocolo do "
                        "municipio. Nico servindo café pra todos. Lucia na "
                        "paneela do fundo — quieta desde que voltou ontem à noite."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Bianca",
                    "line": "Ya he testificado dos veces prima en mi vida. Sé cómo se hace.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "Cuéntale al forestiero qué van a preguntar. Para que sepa.",
                },
                {
                    "kind": "npc",
                    "npc": "Bianca",
                    "line": "Primero — '¿Cuándo lo conoció?' Y yo digo: 'Lo conocí el segundo día. Hablé con él. Lo vi cumplir saleudos.'",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você ouve as palavras 'hablé' e 'vi' pela primeira vez "
                        "com esse formato. Não é 'hablo' (falo agora) — é 'hablé' "
                        "(falei prima). Algo mudou no fim da palavra."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Bianca",
                    "line": "Es para hablar de cose que ya pasaron. Ayer pasó — entonces hablamos así.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "ayer",  "native": "ontem"},
                        {"target": "vi",    "native": "vi (já aconteceu)"},
                        {"target": "oí",    "native": "ouvi (já aconteceu)"},
                        {"target": "hablé", "native": "falei (já aconteceu)"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca quer falar do dia que já passou — o anterior a hoje. A palavra que ela usa:",
                    "options": [
                        {"id": "a", "text": "Ayer"},
                        {"id": "b", "text": "Hoy"},
                        {"id": "c", "text": "Mañana"},
                        {"id": "d", "text": "Siempre"},
                    ],
                    "correct": "a",
                    "word_id": "it_ayer", "target": "ayer", "native": "ontem",
                    "npc_reaction": "Ayer. El día que ya pasó. Quando hablamos del 'ayer', las palavras cambian un poco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca disse 'lo **vi** cumplir saleudos'. 'Vi' significa que ela:",
                    "options": [
                        {"id": "a", "text": "Viu (algo já aconteceu)"},
                        {"id": "b", "text": "Vê (acontece agora)"},
                        {"id": "c", "text": "Vai ver (amanhã)"},
                        {"id": "d", "text": "Quer ver"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Yo vi — y ya pasó. La 'i' final con acento te dice que es algo del pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara bebe café e olha pra você: 'Forestiero — ¿cómo estás hoy?'",
                    "options": [
                        {"id": "a", "text": "Sto bene, grazie"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Bene. Hoy es día de mucho movimiento — vas a necesitar fuerza.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Bianca ensaiando com o forestiero — testa o que o Podesta
    # pode perguntar. Nenhum exercício de palavra nova. F1-F11 puro.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Bianca", "Chiara"],
                "story": (
                    "Bianca vai testemunhar amanhã. Pra não se contradizer, ela "
                    "quer ensaiar — pede que o forestiero responda as mespiu "
                    "perguntas que o Podesta fez ontem. Ela ouve sem interromper."
                ),
                "now": "Bianca testa. Você responde tudo de novo — com mais firmeza.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Empezamos. '¿Cómo te chiami tu?'",
                    "translation": "Começamos. 'Como você se chama?'",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca quer te ouvir sem hesitar:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Ho veinte años"},
                        {"id": "d", "text": "Andiamo a hablar"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Bene. Senza pausa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "'¿Qué eres tu aquí?'",
                    "translation": "'O que você é aqui?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Identidade — o que você É no borgo:",
                    "options": [
                        {"id": "a", "text": "Sono forestiero"},
                        {"id": "b", "text": "Sto forestiero"},
                        {"id": "c", "text": "Ho forestiero"},
                        {"id": "d", "text": "Vado forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_sono", "target": "sono", "native": "sou",
                    "npc_reaction": "Sono. Esatto eres — y questo queda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "'¿Cómo estás aquí, después de tantos días?'",
                    "translation": "'Como você está aqui, depois de tantos dias?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Como você se sente hoje, neste momento:",
                    "options": [
                        {"id": "a", "text": "Sto bene, grazie"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Vado bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Sto bene. Estado de adesso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Adesso la trampa — '¿Cuántos años hai?'",
                    "translation": "Agora a pegadinha — 'Quantos anni você tem?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Resposta exata. Tenho vinte:",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Sono veinte años"},
                        {"id": "c", "text": "Sto veinte"},
                        {"id": "d", "text": "Mi chiamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Ho. La edad va con 'ho' siempre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Una más: '¿Te gusta el borgo?'",
                    "translation": "Mais uma: 'Você gosta do borgo?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Senzacero. Você gosta:",
                    "options": [
                        {"id": "a", "text": "Sí, mi piace"},
                        {"id": "b", "text": "Sí, sono gusta"},
                        {"id": "c", "text": "Sí, sto gusta"},
                        {"id": "d", "text": "Sí, ho gusta"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto",
                    "npc_reaction": "Mi piace. La cosa que te gusta actua sobre ti — Lucia ya te lo enseñó hace tiempo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Y '¿qué vas a hacer en mi borgo?' — esa también la van a preguntar.",
                    "translation": "E '¿qué vas a hacer en mi borgo?' — essa também vão perguntar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Você precisa dizer o que vai fazer logo — buscar o terceiro testigo:",
                    "options": [
                        {"id": "a", "text": "Vado a buscar al tercer testigo"},
                        {"id": "b", "text": "Sono a buscar"},
                        {"id": "c", "text": "Sto a buscar"},
                        {"id": "d", "text": "Ho a buscar"},
                    ],
                    "correct": "a",
                    "word_id": "it_vado_a", "target": "vado a buscar", "native": "vou buscar",
                    "npc_reaction": "Vado a. Lo que salee adesso. Bene usado.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Visita a Pietro na herrería pra ensaiar o testemunho dele. Pietro
    # conta ONTEM o que viu — usando passado naturalmente. O aluno OUVE
    # passado em contexto e reconhece. Foco em REVISÃO + apresentação suave
    # de 'vi' e 'hablé' usados pelos NPCs.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Pietro", "Antonio il Contadino"],
                "story": (
                    "Foram à herrería. Pietro recebeu, trancou a porta — não "
                    "quer testemunhar com gente passando. Sentou no banco baixo "
                    "e disse: 'Vado a contarte lo que vi. Memorízalo — porque "
                    "es lo que repetiré al Podesta.'"
                ),
                "now": "Pietro conta o que viu. Você reconhece o que ele usou ontem.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Pietro",
                    "situation": "Pietro trabalhou a manhã inteira na fracqua. O fogo do carvão deixa a garganta seca. Ele aponta pra mochila do forestiero.",
                    "npc_line": "Prima de empezar — ¿hai algo de beber?La fracqua seca la garganta come el desierto.",
                    "item_tag": "bebida",
                    "on_use": {
                        "narrative": "Você passa algo de beber pra Pietro. Ele bebe devagar, olhando você por cima do copo.",
                        "npc_reaction": "Grazie, giovane. Quien comparte acqua con un herrero — ese ha mi palabra. Vado a testificar bene.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Hay un balde de acqua en el rincón. Ma grazie por pensar.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Ayer por la mañana yo stavo en mi taller. Salí a las ocho — vi al forestiero en la piazza con Chiara.",
                    "translation": "Ontem de manhã eu estava no meu taller. Saí às oito — vi o forasteiro na piazza com Chiara.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro disse 'vi al forestiero'. Aqui ele tá falando de:",
                    "options": [
                        {"id": "a", "text": "Algo que aconteceu ontem"},
                        {"id": "b", "text": "Algo que acontece todo dia"},
                        {"id": "c", "text": "Algo que ainda vai acontecer"},
                        {"id": "d", "text": "Algo que ele vai fazer"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Yo vi — y se acabó. La 'i' con acento dice que ya pasó.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Hablé con el giovane. Le pregunté si tenía fame. Me respondió que sí.",
                    "translation": "Falei com o jovem. Perguntei se ele tinha fome. Ele respondeu que sim.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro disse 'hablé con te'. Significa que ele:",
                    "options": [
                        {"id": "a", "text": "Falou (já aconteceu)"},
                        {"id": "b", "text": "Fala (todo dia)"},
                        {"id": "c", "text": "Vai falar (amanhã)"},
                        {"id": "d", "text": "Quer falar"},
                    ],
                    "correct": "a",
                    "word_id": "it_hable", "target": "hablé", "native": "falei",
                    "npc_reaction": "Hablé. Yo hablé — ya pasó. Misma idea: lo del 'ayer' lleva 'é' final.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Você lembra do encontro. Pra confirmar pra Pietro que VOCÊ TAMBÉM viu ele:",
                    "options": [
                        {"id": "a", "text": "Yo te vi también"},
                        {"id": "b", "text": "Yo te veo"},
                        {"id": "c", "text": "Vado a verte"},
                        {"id": "d", "text": "Sono ver"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Bene. Yo vi. Tu viste. Igual de simple.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Pietro — adesso dile al forestiero qué le vas a decir al Podesta mañana.",
                    "translation": "Pietro — agora diz pro forasteiro o que você vai dizer pro Podesta amanhã.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Pietro vai testemunhar amanhã. Pra confirmar que ele VAI fazer isso:",
                    "options": [
                        {"id": "a", "text": "Pietro va a testificar"},
                        {"id": "b", "text": "Pietro vado a testificar"},
                        {"id": "c", "text": "Pietro andiamo a testificar"},
                        {"id": "d", "text": "Pietro sono testificar"},
                    ],
                    "correct": "a",
                    "word_id": "it_va_a", "target": "va a", "native": "vai (algo logo)",
                    "npc_reaction": "Va — Pietro, él. Lo que aprendiste con Antonio il Contadino: vado, vas, va.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Vado a decirle: 'Conocí al giovane el segundo día. Hablé con él. Saludó con respeto. No vi nada raro.'",
                    "translation": "Vou dizer pra ele: 'Conheci o jovem no segundo dia. Falei com ele. Cumprimentou com respeito. Não vi nada estranho.'",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Pietro termina dizendo 'no vi nada raro'. Pra negar algo que NÃO aconteceu prima — a palavra 'no' fica:",
                    "options": [
                        {"id": "a", "text": "Prima do verbo (no vi)"},
                        {"id": "b", "text": "Depois do verbo (vi no)"},
                        {"id": "c", "text": "Não existe negação"},
                        {"id": "d", "text": "Só no fim da frase"},
                    ],
                    "correct": "a",
                    "word_id": "it_no", "target": "no", "native": "não",
                    "npc_reaction": "No al principio. Igual que 'no mi piace'. Simple.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino comenta: 'Ayer la piazza stavo llena. La Guardia también te vio.' Você confirma — você sabe que ele viu (já aconteceu):",
                    "options": [
                        {"id": "a", "text": "Sí, él me vio"},
                        {"id": "b", "text": "Sí, él me ve"},
                        {"id": "c", "text": "Sí, él va a verme"},
                        {"id": "d", "text": "Sí, sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_vio", "target": "vio", "native": "viu",
                    "npc_reaction": "Vio. Él vio — ya pasó. Aprendiste rápido: 'yo vi, tu viste, él vio'. La forma cambia con chi hizo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Pietro",
                    "line": "Una pregunta más — ¿tu me viste anteayer?Yo te saleudé y tu me respondiste.",
                    "translation": "Mais uma pergunta — você me viu anteontem?Eu te cumprimentei e você me respondeu.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Pietro",
                    "question": "Sim, você viu Pietro no mercato. Resposta firme:",
                    "options": [
                        {"id": "a", "text": "Sí, te vi"},
                        {"id": "b", "text": "Sí, te veo"},
                        {"id": "c", "text": "Vado a verte"},
                        {"id": "d", "text": "Sono verte"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Te vi. Y yo te vi a ti también — por questo vado a testificar mañana.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Saindo da herrería. Antonio il Contadino para o grupo na piazza e explica devagar
    # come contar algo do passado. SEM nomear "pretérito". Apenas: "as palavras
    # mudam quando você fala de algo que já aconteceu". ~3-4 exercícios.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Chiara"],
                "story": (
                    "Vocês voltam da herrería pela praça. Antonio il Contadino decide parar "
                    "perto do poço — quer que o forestiero entenda o que Pietro "
                    "tava fazendo com as palavras. 'Si lo entiendes adesso, mañana "
                    "en el municipio vas a entender todo lo que digan.'"
                ),
                "now": "Antonio il Contadino explica come falar do que já aconteceu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Pietro ha detto 'hablé', 'vi', 'saleí'. Lo que ya pasó. Las parole cambian al final cuando es 'ayer' y no 'hoy'.",
                    "translation": "Pietro disse 'hablé', 'vi', 'saleí'. O que já passou. As palavras mudam no final quando é 'ayer' e não 'hoy'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Hoy hablo · Ayer hablé",
                    "meaning": "Hoje eu falo · Ontem eu falei",
                    "note": "a palavra termina diferente quando algo já aconteceu",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo habl",  "isKey": False},
                        {"text": "é",        "isKey": True},
                        {"text": " · Yo v",  "isKey": False},
                        {"text": "i",        "isKey": True},
                        {"text": " · Yo o",  "isKey": False},
                        {"text": "í",        "isKey": True},
                    ],
                    "example": "Yo hablé con Bianca. Yo vi al Guardia. Yo oí su voz.",
                    "translation": "Eu falei com Bianca. Eu vi La Guardia. Eu ouvi a voz dele.",
                    "note": "quando ya pasó: la palabra termina con sonido fuerte — é · í",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você falou com Bianca ontem. Pra contar isso pra alguém:",
                    "options": [
                        {"id": "a", "text": "Hablé con Bianca ayer"},
                        {"id": "b", "text": "Hablo con Bianca ayer"},
                        {"id": "c", "text": "Vado a hablar ayer"},
                        {"id": "d", "text": "Sono con Bianca"},
                    ],
                    "correct": "a",
                    "word_id": "it_hable", "target": "hablé", "native": "falei",
                    "npc_reaction": "Hablé. Yo, ya pasado, ya hecho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Y cambia con chi lo hizo — igual que con 'vado/vas/va' cuando algo va a uscire.",
                    "translation": "E muda com quem fez — igual a 'vado/vas/va' quando algo vai sair.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo vi · ", "isKey": True},
                        {"text": "Tu viste · ", "isKey": True},
                        {"text": "Él/Ella vio", "isKey": True},
                    ],
                    "example": "Yo vi a Bianca. Tu viste a Pietro. Lucia vio al Podesta.",
                    "translation": "Eu vi Bianca. Você viu Pietro. Lucia viu Il Podesta.",
                    "note": "es el verbo 'ver' cuando ya pasó. Las terminaciones cambian con la persona.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Pietro viu o forestiero ontem. Pra contar (sobre ELE):",
                    "options": [
                        {"id": "a", "text": "Pietro vio al forestiero"},
                        {"id": "b", "text": "Pietro vi al forestiero"},
                        {"id": "c", "text": "Pietro viste al forestiero"},
                        {"id": "d", "text": "Pietro ve al forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_vio", "target": "vio", "native": "viu (ele/ela)",
                    "npc_reaction": "Vio — él, ella. Como 'va' cuando algo salee, ma del pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara testa: 'Forestiero — ¿tu me viste con Bianca anotte?' Pra você responder que sim, você viu:",
                    "options": [
                        {"id": "a", "text": "Sí, te vi"},
                        {"id": "b", "text": "Sí, te veo"},
                        {"id": "c", "text": "Sí, vado a verte"},
                        {"id": "d", "text": "Sí, sono verte"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Igual que Pietro usó. Lo entendiste rápido.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Tarde. Voltando pra casa. Conversa do grupo. Lucia aparece finalmente
    # — calada. Não quer falar do Podesta. Foco em REVISÃO ORGÂNICA F1-F11.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Nico", "Chiara", "Lucia"],
                "story": (
                    "Vocês voltam pra casa de Antonio il Contadino ao fim da tarde. "
                    "Dois testigos garantidos: Bianca e Pietro. Falta um.\n\n"
                    "Lucia estava esperando na porta. Cabelo prquesto, vestido "
                    "diferente — mais formale. Não disse nada sobre ontem."
                ),
                "now": "Reunião à mesa. Lucia quieta. Você tenta entender.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌅 Casa de Antonio il Contadino · Fim de tarde · Os cinco em volta da mesa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Hoy hablamos con Bianca y con Pietro. Los dos aceptan. Lucia — ¿y tu?¿Qué pasó ayer con el Podesta?",
                    "translation": "Hoje falamos com Bianca e com Pietro. Os dois aceitam. Lucia — e você?O que aconteceu ontem com o Podesta?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Hablé con él. Le conté lo que necesitaba saber. Esatto es todo.",
                    "translation": "Falei com ele. Contei o que ele precisava saber. Isso é tudo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia disse 'hablé con él' — confirmou que falou. Você comenta com Chiara baixinho que ouviu Lucia falar isso:",
                    "options": [
                        {"id": "a", "text": "Sí, la oí decir questo"},
                        {"id": "b", "text": "Sí, la oigo"},
                        {"id": "c", "text": "Vado a oír"},
                        {"id": "d", "text": "Sono oír"},
                    ],
                    "correct": "a",
                    "word_id": "it_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oí. Yo oí — ya pasó. La 'í' con acento, come Pietro te enseñó.",
                },
                {
                    "kind": "narrative",
                    "text": "Chiara olha pra você por um segundo. Nico não levanta os olhos do prato. Lucia continua serena.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Lucia — ¿el Guardia estuvo allí cuando hablaste con él?",
                    "translation": "Lucia — La Guardia estava lá quando você falou com ele?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "No. Solo estuvimos los dos. Yo y él.",
                    "translation": "Não. Só estáandiamo os dois. Eu e ele.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico pergunta pra você: 'Forestiero — ¿cómo estás con todo esto?'",
                    "options": [
                        {"id": "a", "text": "Sto bene, ma ho paura"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Andiamo bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Las dos cose a la vez — estado bene, sensación paura. Esatto es ser humano.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Falta uno más. ¿En quién pensamos?",
                    "translation": "Falta mais um. Em quem pensamos?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara sugere: 'Giulia te vio el primer día'. Você concorda. Chiara sai pra falar com Giulia — pra dizer o que ELA vai fazer (já saindo agora):",
                    "options": [
                        {"id": "a", "text": "Vado a buscar a Giulia"},
                        {"id": "b", "text": "Andiamo a buscar a Giulia"},
                        {"id": "c", "text": "Vas a buscar"},
                        {"id": "d", "text": "Sono buscar"},
                    ],
                    "correct": "a",
                    "word_id": "it_vado_a", "target": "vado a", "native": "vou (algo logo)",
                    "npc_reaction": "Vado a — yo, adesso. Chiara nunca pierde tiempo.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Noite. Vão atrás do terceiro testigo. Giulia — quem viu o
    # forestiero no primeiro dia. Chegam na padaria. Giulia hesita. Tem medo.
    # Gate: errar trava. Closenzag prepara F13.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Chiara", "Nico", "Antonio il Contadino"],
                "story": (
                    "À noite, Chiara: 'Giulia te vio el primer día. "
                    "Si alguien ha memoria exacta de tu llegada, es ella.'\n\n"
                    "Saíram os quatro. Lucia ficou em casa — disse que precisava "
                    "descansar. Vocês andam três quadras até a padaria de Giulia. "
                    "Luce acesa lá dentro — está fechando o forno."
                ),
                "now": "Convienicer Giulia. Errar trava — palavras certas, situação real.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌙 Padaria de Giulia · Noite · Forno apagado · Luce baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "¡Hijos! ¿A esta hora?¿Pasó algo?",
                    "translation": "Filhos! A essa hora?Aconteceu alguma coisa?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia abriu a porta preocupada. Sol já se pôs. Você cumprimenta calmo:",
                    "options": [
                        {"id": "a", "text": "Buona notte, Giulia"},
                        {"id": "b", "text": "Benes días"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenas_nottes", "target": "buona notte", "native": "boa noite",
                    "npc_reaction": "Buona notte, hijo. Entren — la notte está fría.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Giulia — necesitamos algo. Il Podesta pide testigos del forestiero. Tu lo viste el primer día.",
                    "translation": "Giulia — a gente precisa de algo. O Podesta pede testigos do forasteiro. Você viu ele no primeiro dia.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "...Il Podesta. Mmm.",
                    "translation": "...O Podesta. Mmm.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Giulia olha pra porta da fronte — fechada, piu ela checa de "
                        "novo. Tem medo. Você consegue ver."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Yo te vi ese día, giovane. Llegaste perdido. Yo te ofrecí pane — y al día siguiente te lo di gratis.",
                    "translation": "Eu te vi naquele dia, jovem. Você chegou perdido. Eu te ofereci pão — e no dia seguinte te dei de graça.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia lembra de tudo. Pra confirmar que VOCÊ TAMBÉM lembra dela te dando pão (você viu Giulia):",
                    "options": [
                        {"id": "a", "text": "Sí, te vi"},
                        {"id": "b", "text": "Sí, te veo"},
                        {"id": "c", "text": "Vado a verte"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Te vi. Sí — y yo te vi a ti. Esatto ya es suficiente.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Giulia — ¿vas a testificar mañana o pasado mañana?",
                    "translation": "Giulia — você vai testemunhar amanhã ou depois de amanhã?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Giulia olha pro chão. Pra Antonio il Contadino. Pra Chiara. Pra você. "
                        "Pensa. Pensa muito tempo."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Vado a hacerlo. Ma quiero ir el primero día — prima que el Guardia se entere. Mañana mismo.",
                    "translation": "Vou fazer. Mas quero ir no primeiro dia — prima do Guardia saber. Amanhã mesmo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia aceitou com coragem. Você agradece formale:",
                    "options": [
                        {"id": "a", "text": "Grazie, Giulia"},
                        {"id": "b", "text": "Adiós Giulia"},
                        {"id": "c", "text": "Sto male"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada, giovane. Lo hago por Antonio il Contadino — y porque te vi llegar perdido. Esatto pesa.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino propõe ao grupo o que VAMOS fazer amanhã cedo (todos juntos):",
                    "options": [
                        {"id": "a", "text": "Andiamo al municipio mañana"},
                        {"id": "b", "text": "Vado al municipio mañana"},
                        {"id": "c", "text": "Va al municipio"},
                        {"id": "d", "text": "Sono municipio"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo — los siete. Tres testigos, los cuatro nuestros. Mañana al amanecer.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F13 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🌃 Saindo da padaria · Rua escura · Os quatro caminhando",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Tres testigos. Mañana al municipio. Ma esta notte — mejor que durmamos en casa de mi madre. Más lejos, más seguro.",
                    "translation": "Três testigos. Amanhã no municipio. Mas essa noite — melhor dormir na casa da minha mãe. Mais longe, mais seguro.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio il Contadino concorda com a cabeça. Chiara corre na fronte "
                        "pra avisar Lucia. Você caminha com Nico pelo lado mais "
                        "escuro da rua.\n\n"
                        "'Mañana vas a conocer a mi madre. Y a mis hermanas.'"
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




