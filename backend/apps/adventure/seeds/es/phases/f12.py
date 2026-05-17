"""
Seed das 6 seções da Fase 12 Espanhol A1 — "Tres días".

Carmen aceitou testemunhar. Eduardo aceitou (com a condição estranha
sobre as costas). Falta um terceiro testigo imparcial. Esta fase
apresenta o PASSADO de forma natural — porque pra testemunhar é
preciso contar o que aconteceu antes.

ABORDAGEM PEDAGÓGICA:
    Os NPCs usam o passado naturalmente. O aluno aprende pelo uso —
    "vi", "oí", "hablé" aparecem em situações claras. Sem termo
    técnico. Sem tabela de conjugação. Carmen e Eduardo são quem
    usam, e o jogador entende pelo contexto.

Vocab novo (2): ayer · vi
Apresentação adicional: oí · hablé (no vocab_list, sem foco em todos)

Revisão F1-F11 dominante:
  · me llamo / soy forastero (F1, F8, F11)
  · tengo veinte años (F7, F11)
  · estoy bien (F8, F11)
  · me gusta / no me gusta (F9)
  · vamos a (F11) — futuro próximo já conhecido
  · gracias / buenos días (F1)
  · vecino (F7) — Carmen e Eduardo são vecinos imparciales

NPC principais: Carmen · Eduardo · Sofía · Don Miguel · María
NPC tensão:     El Vigilante (vigia o grupo)
Arco emocional: trabalho em equipe → tensão sobre o 3º testigo
Transição:      F13 abre com Miguel propondo levar o grupo pra casa
                da mãe dele essa noite.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f12_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Manhã do segundo dia. Carmen ensaiando com Sofía. Apresentação suave
    # do passado — Carmen usa "vi", "hablé" em conversa real. 1 exercício
    # novo sobre 'ayer' + revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "agua",
                    "min_level": 1,
                    "uses_item_tag": "bebida",
                    "success": "Voce administra a sede nos tres dias e chega com memoria menos embaralhada.",
                    "fallback": "A sede pesa na cabeca, mas o grupo reduz o passo e chega junto.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "☀️ Manhã do segundo dia · Casa de Don Miguel · Cozinha cheia\n\n"
                        "Carmen sentada à mesa com Sofía explicando o protocolo do "
                        "ayuntamiento. Miguel servindo café pra todos. María na "
                        "panela do fundo — quieta desde que voltou ontem à noite."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Ya he testificado dos veces antes en mi vida. Sé cómo se hace.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "Cuéntale al forastero qué van a preguntar. Para que sepa.",
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Primero — '¿Cuándo lo conoció?' Y yo digo: 'Lo conocí el segundo día. Hablé con él. Lo vi cumplir saludos.'",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você ouve as palavras 'hablé' e 'vi' pela primeira vez "
                        "com esse formato. Não é 'hablo' (falo agora) — é 'hablé' "
                        "(falei antes). Algo mudou no fim da palavra."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Carmen",
                    "line": "Es para hablar de cosas que ya pasaron. Ayer pasó — entonces hablamos así.",
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
                    "npc": "Carmen",
                    "question": "Carmen quer falar do dia que já passou — o anterior a hoje. A palavra que ela usa:",
                    "options": [
                        {"id": "a", "text": "Ayer"},
                        {"id": "b", "text": "Hoy"},
                        {"id": "c", "text": "Mañana"},
                        {"id": "d", "text": "Siempre"},
                    ],
                    "correct": "a",
                    "word_id": "es_ayer", "target": "ayer", "native": "ontem",
                    "npc_reaction": "Ayer. El día que ya pasó. Cuando hablamos del 'ayer', las palabras cambian un poco.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen disse 'lo **vi** cumplir saludos'. 'Vi' significa que ela:",
                    "options": [
                        {"id": "a", "text": "Viu (algo já aconteceu)"},
                        {"id": "b", "text": "Vê (acontece agora)"},
                        {"id": "c", "text": "Vai ver (amanhã)"},
                        {"id": "d", "text": "Quer ver"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Yo vi — y ya pasó. La 'i' final con acento te dice que es algo del pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía bebe café e olha pra você: 'Forastero — ¿cómo estás hoy?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Hoy es día de mucho movimiento — vas a necesitar fuerza.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Carmen ensaiando com o forastero — testa o que o Alcalde
    # pode perguntar. Nenhum exercício de palavra nova. F1-F11 puro.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Carmen", "Sofía"],
                "story": (
                    "Carmen vai testemunhar amanhã. Pra não se contradizer, ela "
                    "quer ensaiar — pede que o forastero responda as mesmas "
                    "perguntas que o Alcalde fez ontem. Ela ouve sem interromper."
                ),
                "now": "Carmen testa. Você responde tudo de novo — com mais firmeza.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Empezamos. '¿Cómo te llamas tú?'",
                    "translation": "Começamos. 'Como você se chama?'",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen quer te ouvir sem hesitar:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo veinte años"},
                        {"id": "d", "text": "Vamos a hablar"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Bien. Sin pausa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "'¿Qué eres tú aquí?'",
                    "translation": "'O que você é aqui?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Identidade — o que você É no pueblo:",
                    "options": [
                        {"id": "a", "text": "Soy forastero"},
                        {"id": "b", "text": "Estoy forastero"},
                        {"id": "c", "text": "Tengo forastero"},
                        {"id": "d", "text": "Voy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_soy", "target": "soy", "native": "sou",
                    "npc_reaction": "Soy. Eso eres — y eso queda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "'¿Cómo estás aquí, después de tantos días?'",
                    "translation": "'Como você está aqui, depois de tantos dias?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Como você se sente hoje, neste momento:",
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
                    "line": "Ahora la trampa — '¿Cuántos años tienes?'",
                    "translation": "Agora a pegadinha — 'Quantos anos você tem?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Resposta exata. Tenho vinte:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Soy veinte años"},
                        {"id": "c", "text": "Estoy veinte"},
                        {"id": "d", "text": "Me llamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Tengo. La edad va con 'tengo' siempre.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Una más: '¿Te gusta el pueblo?'",
                    "translation": "Mais uma: 'Você gosta do pueblo?'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Sincero. Você gosta:",
                    "options": [
                        {"id": "a", "text": "Sí, me gusta"},
                        {"id": "b", "text": "Sí, soy gusta"},
                        {"id": "c", "text": "Sí, estoy gusta"},
                        {"id": "d", "text": "Sí, tengo gusta"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Me gusta. La cosa que te gusta actúa sobre ti — María ya te lo enseñó hace tiempo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Y '¿qué vas a hacer en mi pueblo?' — esa también la van a preguntar.",
                    "translation": "E '¿qué vas a hacer en mi pueblo?' — essa também vão perguntar.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Você precisa dizer o que vai fazer logo — buscar o terceiro testigo:",
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

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Visita a Eduardo na herrería pra ensaiar o testemunho dele. Eduardo
    # conta ONTEM o que viu — usando passado naturalmente. O aluno OUVE
    # passado em contexto e reconhece. Foco em REVISÃO + apresentação suave
    # de 'vi' e 'hablé' usados pelos NPCs.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Eduardo", "Don Miguel"],
                "story": (
                    "Foram à herrería. Eduardo recebeu, trancou a porta — não "
                    "quer testemunhar com gente passando. Sentou no banco baixo "
                    "e disse: 'Voy a contarte lo que vi. Memorízalo — porque "
                    "es lo que repetiré al Alcalde.'"
                ),
                "now": "Eduardo conta o que viu. Você reconhece o que ele usou ontem.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Eduardo",
                    "situation": "Eduardo trabalhou a manhã inteira na fragua. O fogo do carvão deixa a garganta seca. Ele aponta pra mochila do forastero.",
                    "npc_line": "Antes de empezar — ¿tienes algo de beber? La fragua seca la garganta como el desierto.",
                    "item_tag": "bebida",
                    "on_use": {
                        "narrative": "Você passa algo de beber pra Eduardo. Ele bebe devagar, olhando você por cima do copo.",
                        "npc_reaction": "Gracias, joven. Quien comparte agua con un herrero — ese tiene mi palabra. Voy a testificar bien.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Hay un balde de agua en el rincón. Pero gracias por pensar.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Ayer por la mañana yo estaba en mi taller. Salí a las ocho — vi al forastero en la plaza con Sofía.",
                    "translation": "Ontem de manhã eu estava no meu taller. Saí às oito — vi o forasteiro na plaza com Sofía.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo disse 'vi al forastero'. Aqui ele tá falando de:",
                    "options": [
                        {"id": "a", "text": "Algo que aconteceu ontem"},
                        {"id": "b", "text": "Algo que acontece todo dia"},
                        {"id": "c", "text": "Algo que ainda vai acontecer"},
                        {"id": "d", "text": "Algo que ele vai fazer"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Yo vi — y se acabó. La 'i' con acento dice que ya pasó.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Hablé con el joven. Le pregunté si tenía hambre. Me respondió que sí.",
                    "translation": "Falei com o jovem. Perguntei se ele tinha fome. Ele respondeu que sim.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo disse 'hablé contigo'. Significa que ele:",
                    "options": [
                        {"id": "a", "text": "Falou (já aconteceu)"},
                        {"id": "b", "text": "Fala (todo dia)"},
                        {"id": "c", "text": "Vai falar (amanhã)"},
                        {"id": "d", "text": "Quer falar"},
                    ],
                    "correct": "a",
                    "word_id": "es_hable", "target": "hablé", "native": "falei",
                    "npc_reaction": "Hablé. Yo hablé — ya pasó. Misma idea: lo del 'ayer' lleva 'é' final.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Você lembra do encontro. Pra confirmar pra Eduardo que VOCÊ TAMBÉM viu ele:",
                    "options": [
                        {"id": "a", "text": "Yo te vi también"},
                        {"id": "b", "text": "Yo te veo"},
                        {"id": "c", "text": "Voy a verte"},
                        {"id": "d", "text": "Soy ver"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Bien. Yo vi. Tú viste. Igual de simple.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Eduardo — ahora dile al forastero qué le vas a decir al Alcalde mañana.",
                    "translation": "Eduardo — agora diz pro forasteiro o que você vai dizer pro Alcalde amanhã.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Eduardo vai testemunhar amanhã. Pra confirmar que ele VAI fazer isso:",
                    "options": [
                        {"id": "a", "text": "Eduardo va a testificar"},
                        {"id": "b", "text": "Eduardo voy a testificar"},
                        {"id": "c", "text": "Eduardo vamos a testificar"},
                        {"id": "d", "text": "Eduardo soy testificar"},
                    ],
                    "correct": "a",
                    "word_id": "es_va_a", "target": "va a", "native": "vai (algo logo)",
                    "npc_reaction": "Va — Eduardo, él. Lo que aprendiste con Don Miguel: voy, vas, va.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Voy a decirle: 'Conocí al joven el segundo día. Hablé con él. Saludó con respeto. No vi nada raro.'",
                    "translation": "Vou dizer pra ele: 'Conheci o jovem no segundo dia. Falei com ele. Cumprimentou com respeito. Não vi nada estranho.'",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Eduardo termina dizendo 'no vi nada raro'. Pra negar algo que NÃO aconteceu antes — a palavra 'no' fica:",
                    "options": [
                        {"id": "a", "text": "Antes do verbo (no vi)"},
                        {"id": "b", "text": "Depois do verbo (vi no)"},
                        {"id": "c", "text": "Não existe negação"},
                        {"id": "d", "text": "Só no fim da frase"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "não",
                    "npc_reaction": "No al principio. Igual que 'no me gusta'. Simple.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel comenta: 'Ayer la plaza estaba llena. El Vigilante también te vio.' Você confirma — você sabe que ele viu (já aconteceu):",
                    "options": [
                        {"id": "a", "text": "Sí, él me vio"},
                        {"id": "b", "text": "Sí, él me ve"},
                        {"id": "c", "text": "Sí, él va a verme"},
                        {"id": "d", "text": "Sí, soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vio", "target": "vio", "native": "viu",
                    "npc_reaction": "Vio. Él vio — ya pasó. Aprendiste rápido: 'yo vi, tú viste, él vio'. La forma cambia con quien hizo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Eduardo",
                    "line": "Una pregunta más — ¿tú me viste anteayer? Yo te saludé y tú me respondiste.",
                    "translation": "Mais uma pergunta — você me viu anteontem? Eu te cumprimentei e você me respondeu.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Eduardo",
                    "question": "Sim, você viu Eduardo no mercado. Resposta firme:",
                    "options": [
                        {"id": "a", "text": "Sí, te vi"},
                        {"id": "b", "text": "Sí, te veo"},
                        {"id": "c", "text": "Voy a verte"},
                        {"id": "d", "text": "Soy verte"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Te vi. Y yo te vi a ti también — por eso voy a testificar mañana.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Saindo da herrería. Don Miguel para o grupo na plaza e explica devagar
    # como contar algo do passado. SEM nomear "pretérito". Apenas: "as palavras
    # mudam quando você fala de algo que já aconteceu". ~3-4 exercícios.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Sofía"],
                "story": (
                    "Vocês voltam da herrería pela praça. Don Miguel decide parar "
                    "perto do poço — quer que o forastero entenda o que Eduardo "
                    "tava fazendo com as palavras. 'Si lo entiendes ahora, mañana "
                    "en el ayuntamiento vas a entender todo lo que digan.'"
                ),
                "now": "Don Miguel explica como falar do que já aconteceu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Eduardo dijo 'hablé', 'vi', 'salí'. Lo que ya pasó. Las palabras cambian al final cuando es 'ayer' y no 'hoy'.",
                    "translation": "Eduardo disse 'hablé', 'vi', 'salí'. O que já passou. As palavras mudam no final quando é 'ayer' e não 'hoy'.",
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
                    "example": "Yo hablé con Carmen. Yo vi al Vigilante. Yo oí su voz.",
                    "translation": "Eu falei com Carmen. Eu vi El Vigilante. Eu ouvi a voz dele.",
                    "note": "quando ya pasó: la palabra termina con sonido fuerte — é · í",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você falou com Carmen ontem. Pra contar isso pra alguém:",
                    "options": [
                        {"id": "a", "text": "Hablé con Carmen ayer"},
                        {"id": "b", "text": "Hablo con Carmen ayer"},
                        {"id": "c", "text": "Voy a hablar ayer"},
                        {"id": "d", "text": "Soy con Carmen"},
                    ],
                    "correct": "a",
                    "word_id": "es_hable", "target": "hablé", "native": "falei",
                    "npc_reaction": "Hablé. Yo, ya pasado, ya hecho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y cambia con quien lo hizo — igual que con 'voy/vas/va' cuando algo va a salir.",
                    "translation": "E muda com quem fez — igual a 'voy/vas/va' quando algo vai sair.",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo vi · ", "isKey": True},
                        {"text": "Tú viste · ", "isKey": True},
                        {"text": "Él/Ella vio", "isKey": True},
                    ],
                    "example": "Yo vi a Carmen. Tú viste a Eduardo. María vio al Alcalde.",
                    "translation": "Eu vi Carmen. Você viu Eduardo. María viu El Alcalde.",
                    "note": "es el verbo 'ver' cuando ya pasó. Las terminaciones cambian con la persona.",
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
                    "npc_reaction": "Vio — él, ella. Como 'va' cuando algo sale, pero del pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía testa: 'Forastero — ¿tú me viste con Carmen anoche?' Pra você responder que sim, você viu:",
                    "options": [
                        {"id": "a", "text": "Sí, te vi"},
                        {"id": "b", "text": "Sí, te veo"},
                        {"id": "c", "text": "Sí, voy a verte"},
                        {"id": "d", "text": "Sí, soy verte"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Igual que Eduardo usó. Lo entendiste rápido.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Tarde. Voltando pra casa. Conversa do grupo. María aparece finalmente
    # — calada. Não quer falar do Alcalde. Foco em REVISÃO ORGÂNICA F1-F11.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Miguel", "Sofía", "María"],
                "story": (
                    "Vocês voltam pra casa de Don Miguel ao fim da tarde. "
                    "Dois testigos garantidos: Carmen e Eduardo. Falta um.\n\n"
                    "María estava esperando na porta. Cabelo preso, vestido "
                    "diferente — mais formal. Não disse nada sobre ontem."
                ),
                "now": "Reunião à mesa. María quieta. Você tenta entender.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌅 Casa de Don Miguel · Fim de tarde · Os cinco em volta da mesa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Hoy hablamos con Carmen y con Eduardo. Los dos aceptan. María — ¿y tú? ¿Qué pasó ayer con el Alcalde?",
                    "translation": "Hoje falamos com Carmen e com Eduardo. Os dois aceitam. María — e você? O que aconteceu ontem com o Alcalde?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Hablé con él. Le conté lo que necesitaba saber. Eso es todo.",
                    "translation": "Falei com ele. Contei o que ele precisava saber. Isso é tudo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María disse 'hablé con él' — confirmou que falou. Você comenta com Sofía baixinho que ouviu María falar isso:",
                    "options": [
                        {"id": "a", "text": "Sí, la oí decir eso"},
                        {"id": "b", "text": "Sí, la oigo"},
                        {"id": "c", "text": "Voy a oír"},
                        {"id": "d", "text": "Soy oír"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oí. Yo oí — ya pasó. La 'í' con acento, como Eduardo te enseñó.",
                },
                {
                    "kind": "narrative",
                    "text": "Sofía olha pra você por um segundo. Miguel não levanta os olhos do prato. María continua serena.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "María — ¿el Vigilante estuvo allí cuando hablaste con él?",
                    "translation": "María — El Vigilante estava lá quando você falou com ele?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "No. Solo estuvimos los dos. Yo y él.",
                    "translation": "Não. Só estávamos os dois. Eu e ele.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel pergunta pra você: 'Forastero — ¿cómo estás con todo esto?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien, pero tengo miedo"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Vamos bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Las dos cosas a la vez — estado bien, sensación miedo. Eso es ser humano.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Falta uno más. ¿En quién pensamos?",
                    "translation": "Falta mais um. Em quem pensamos?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía sugere: 'Rosa te vio el primer día'. Você concorda. Sofía sai pra falar com Rosa — pra dizer o que ELA vai fazer (já saindo agora):",
                    "options": [
                        {"id": "a", "text": "Voy a buscar a Rosa"},
                        {"id": "b", "text": "Vamos a buscar a Rosa"},
                        {"id": "c", "text": "Vas a buscar"},
                        {"id": "d", "text": "Soy buscar"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a", "native": "vou (algo logo)",
                    "npc_reaction": "Voy a — yo, ahora. Sofía nunca pierde tiempo.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Noite. Vão atrás do terceiro testigo. Rosa la Panadera — quem viu o
    # forastero no primeiro dia. Chegam na padaria. Rosa hesita. Tem medo.
    # Gate: errar trava. Closing prepara F13.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Sofía", "Miguel", "Don Miguel"],
                "story": (
                    "À noite, Sofía: 'Rosa la Panadera te vio el primer día. "
                    "Si alguien tiene memoria exacta de tu llegada, es ella.'\n\n"
                    "Saíram os quatro. María ficou em casa — disse que precisava "
                    "descansar. Vocês andam três quadras até a padaria de Rosa. "
                    "Luz acesa lá dentro — está fechando o forno."
                ),
                "now": "Convencer Rosa. Errar trava — palavras certas, situação real.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌙 Padaria de Rosa · Noite · Forno apagado · Luz baixa",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "¡Hijos! ¿A esta hora? ¿Pasó algo?",
                    "translation": "Filhos! A essa hora? Aconteceu alguma coisa?",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa abriu a porta preocupada. Sol já se pôs. Você cumprimenta calmo:",
                    "options": [
                        {"id": "a", "text": "Buenas noches, Rosa"},
                        {"id": "b", "text": "Buenos días"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                    "npc_reaction": "Buenas noches, hijo. Entren — la noche está fría.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Rosa — necesitamos algo. El Alcalde pide testigos del forastero. Tú lo viste el primer día.",
                    "translation": "Rosa — a gente precisa de algo. O Alcalde pede testigos do forasteiro. Você viu ele no primeiro dia.",
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
                        "Rosa olha pra porta da frente — fechada, mas ela checa de "
                        "novo. Tem medo. Você consegue ver."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Yo te vi ese día, joven. Llegaste perdido. Yo te ofrecí pan — y al día siguiente te lo di gratis.",
                    "translation": "Eu te vi naquele dia, jovem. Você chegou perdido. Eu te ofereci pão — e no dia seguinte te dei de graça.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa lembra de tudo. Pra confirmar que VOCÊ TAMBÉM lembra dela te dando pão (você viu Rosa):",
                    "options": [
                        {"id": "a", "text": "Sí, te vi"},
                        {"id": "b", "text": "Sí, te veo"},
                        {"id": "c", "text": "Voy a verte"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Te vi. Sí — y yo te vi a ti. Eso ya es suficiente.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Rosa — ¿vas a testificar mañana o pasado mañana?",
                    "translation": "Rosa — você vai testemunhar amanhã ou depois de amanhã?",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Rosa olha pro chão. Pra Don Miguel. Pra Sofía. Pra você. "
                        "Pensa. Pensa muito tempo."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Voy a hacerlo. Pero quiero ir el primero día — antes que el Vigilante se entere. Mañana mismo.",
                    "translation": "Vou fazer. Mas quero ir no primeiro dia — antes do Vigilante saber. Amanhã mesmo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa aceitou com coragem. Você agradece formal:",
                    "options": [
                        {"id": "a", "text": "Gracias, Rosa"},
                        {"id": "b", "text": "Adiós Rosa"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, joven. Lo hago por Don Miguel — y porque te vi llegar perdido. Eso pesa.",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel propõe ao grupo o que VAMOS fazer amanhã cedo (todos juntos):",
                    "options": [
                        {"id": "a", "text": "Vamos al ayuntamiento mañana"},
                        {"id": "b", "text": "Voy al ayuntamiento mañana"},
                        {"id": "c", "text": "Va al ayuntamiento"},
                        {"id": "d", "text": "Soy ayuntamiento"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos — los siete. Tres testigos, los cuatro nuestros. Mañana al amanecer.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F13 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🌃 Saindo da padaria · Rua escura · Os quatro caminhando",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Tres testigos. Mañana al ayuntamiento. Pero esta noche — mejor que durmamos en casa de mi madre. Más lejos, más seguro.",
                    "translation": "Três testigos. Amanhã no ayuntamiento. Mas essa noite — melhor dormir na casa da minha mãe. Mais longe, mais seguro.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel concorda com a cabeça. Sofía corre na frente "
                        "pra avisar María. Você caminha com Miguel pelo lado mais "
                        "escuro da rua.\n\n"
                        "'Mañana vas a conocer a mi madre. Y a mis hermanas.'"
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
