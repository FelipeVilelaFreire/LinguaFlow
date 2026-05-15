"""
Seed das 6 seções da Fase 18 Espanhol A1 — "Don Miguel se entera".

Os três jovens reuniram tudo. Don Miguel ouviu. Decisão pendente:
o que fazer com María agora que existem três pistas concretas
(passado dela com Alcalde via Carmen, marca dos Buscadores, sussurro
de Lucía).

Decisão final: continuar observando — sem confrontar. Mas Don Miguel
revela que tem uma carta guardada faz 20 anos. Vai mostrar amanhã.

VOCAB NOVO (3): verdad · mentir · confiar
LINGUAGEM NOVA: poder + verbo (puedo / puedes / puede / podemos)
    Apresentado pelo uso natural — "no puedo decirle, todavía no"

Revisão F1-F17 dominante:
  · ya / todavía no (F17)
  · quiero + verbo (F16)
  · vi/hablé/oí (F12)
  · mi/tu/su (F13)
  · el/la (F14)
  · soy/estoy/tengo (F8)

NPC principais: Don Miguel · Sofía · Miguel · você
Arco emocional: dúvida → reunião → decisão coletiva → tensão crescente
Transição: F19 abre logo após — Don Miguel já indo até o baú.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f18_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Manhã cedo. Sofía e Miguel chegam à casa de Don Miguel. María saiu
    # cedo — disse que ia ao mercado. Os 4 (Don Miguel + 3 jovens) na cozinha.
    # 2 novos exer + 2 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "cura",
                    "min_level": 2,
                    "uses_item_tag": "remedio",
                    "success": "Voce percebe o cansaco de Don Miguel e evita pressionar antes da verdade aparecer.",
                    "fallback": "Voce pergunta cedo demais, mas Don Miguel respira fundo e continua mesmo assim.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🌅 Casa de Don Miguel · Manhã cedo · Cozinha\n\n"
                        "María saiu antes do amanhecer — disse que ia ao mercado "
                        "comprar hierbas. Sofía e Miguel chegaram logo depois. "
                        "Don Miguel preparou café forte. Quatro tigelas humeantes "
                        "na mesa baixa."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Bueno. Antes de que vuelva — vamos a juntar todo lo que sabemos.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "Empezamos por Carmen, después la marca, después lo de tu mujer.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Sí. Pero antes — quiero saber qué creen ustedes. Sin que yo influya.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Don Miguel quer ouvir vocês primeiro. Sofía olha pra Miguel. Miguel olha pra você. Você decide começar.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "verdad",  "native": "verdade"},
                        {"target": "mentir",  "native": "mentir"},
                        {"target": "confiar", "native": "confiar"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel cumprimentou vocês — amanhecer cedo:",
                    "options": [
                        {"id": "a", "text": "Buenos días, Don Miguel"},
                        {"id": "b", "text": "Buenas noches"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días. Hijo — empieza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Lo que tenemos que decidir hoy es importante. Pero la verdad — ¿qué sentimos sobre María?",
                    "translation": "O que temos que decidir hoje é importante. Mas a verdade — o que sentimos sobre María?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel falou 'la verdad'. Significa:",
                    "options": [
                        {"id": "a", "text": "Verdade (o que é real)"},
                        {"id": "b", "text": "Mentira"},
                        {"id": "c", "text": "Pergunta"},
                        {"id": "d", "text": "Resposta"},
                    ],
                    "correct": "a",
                    "word_id": "es_verdad", "target": "verdad", "native": "verdade",
                    "npc_reaction": "Verdad. La cosa que es. Aunque duela.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Sofía responde — 'no es que María mienta. Es que oculta cosas.' A palavra 'mentir' significa:",
                    "options": [
                        {"id": "a", "text": "Dizer algo falso"},
                        {"id": "b", "text": "Dizer a verdade"},
                        {"id": "c", "text": "Estar quieto"},
                        {"id": "d", "text": "Sair correndo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mentir", "target": "mentir", "native": "mentir",
                    "npc_reaction": "Mentir. Decir algo falso. Sofía hace bien la distinción — María no miente. Calla.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'La pregunta es — ¿podemos confiar en ella?' A palavra 'confiar' significa:",
                    "options": [
                        {"id": "a", "text": "Acreditar que alguém é seguro"},
                        {"id": "b", "text": "Esconder coisas"},
                        {"id": "c", "text": "Lutar"},
                        {"id": "d", "text": "Sair"},
                    ],
                    "correct": "a",
                    "word_id": "es_confiar", "target": "confiar", "native": "confiar",
                    "npc_reaction": "Confiar. Creer que alguien no te va a hacer daño. Esa palabra siempre se gana — nunca se da.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Os 3 contam pra Don Miguel as 3 pistas em detalhe. 100% revisão F1-F17.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Sofía", "Miguel"],
                "story": (
                    "Don Miguel pegou um pedaço de papel velho e uma pena. "
                    "Quer anotar — pra ter clareza.\n\n"
                    "'Empezamos. Primero — lo de Carmen. Sofía — cuéntalo tú.'"
                ),
                "now": "Cada pista é contada do que já passou. Don Miguel anota.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Carmen nos contó que fue novia del Alcalde hace veinticinco años. El padre del Alcalde rompió el compromiso.",
                    "translation": "Carmen nos contou que foi noiva do Alcalde há vinte e cinco anos. O pai do Alcalde quebrou o noivado.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Sofía disse 'Carmen nos contó'. 'Contó' significa que Carmen:",
                    "options": [
                        {"id": "a", "text": "Contou (já passou)"},
                        {"id": "b", "text": "Conta (agora)"},
                        {"id": "c", "text": "Vai contar"},
                        {"id": "d", "text": "Sou contar"},
                    ],
                    "correct": "a",
                    "word_id": "es_conto", "target": "contó", "native": "contou",
                    "npc_reaction": "Contó. Ya pasó. Anotando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y mi madre — anoche en la cocina — me dijo que conoce a María de algún sitio. No recuerda de dónde.",
                    "translation": "E minha mãe — ontem à noite na cozinha — me disse que conhece María de algum lugar. Não lembra de onde.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Miguel disse 'me dijo'. Pra você confirmar pra Don Miguel — você ouviu o sussurro também:",
                    "options": [
                        {"id": "a", "text": "Yo también lo oí"},
                        {"id": "b", "text": "Yo oigo"},
                        {"id": "c", "text": "Voy a oír"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oí. Bueno. Dos puntos confirmados.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y ayer — la marca de Eduardo. María la reconoció sin disfrazar. Dijo que su familia tenía relación con esa gente.",
                    "translation": "E ontem — a marca de Eduardo. María a reconheceu sem disfarçar. Disse que sua família tinha relação com essa gente.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel resumiu três pistas. Pra você confirmar que entendeu:",
                    "options": [
                        {"id": "a", "text": "Sí, ya entiendo las tres"},
                        {"id": "b", "text": "Todavía no entiendo"},
                        {"id": "c", "text": "Voy a entender"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya entiendes. Bueno.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Y hay otra cosa que solo el forastero y yo sabemos. Lo de la cena con María — ella sabía cosas que el forastero nunca contó.",
                    "translation": "E tem outra coisa que só o forasteiro e eu sabemos. Aquilo do jantar com María — ela sabia coisas que o forasteiro nunca contou.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'Cuatro pistas. ¿Y qué siente cada uno?' Você responde honesto — tem medo:",
                    "options": [
                        {"id": "a", "text": "Tengo miedo"},
                        {"id": "b", "text": "Estoy miedo"},
                        {"id": "c", "text": "Soy miedo"},
                        {"id": "d", "text": "Voy miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_miedo", "target": "tengo miedo", "native": "tenho medo",
                    "npc_reaction": "Tengo miedo. Es válido — y necesario.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta — 'Don Miguel — ¿tú la conoces de antes?' Pra Don Miguel ela usa 'tu' formal? Não — informal. Resposta dela:",
                    "options": [
                        {"id": "a", "text": "No, no la conozco de antes"},
                        {"id": "b", "text": "Sí, la conozco"},
                        {"id": "c", "text": "Voy a conocerla"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "não",
                    "npc_reaction": "No. Pero mi mujer sí. Y eso pesa.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Don Miguel apresenta "poder + verbo" pelo uso. "¿Podemos confrontarla?
    # ¿Podemos echarla? ¿Puedo confiar?" Cada exercício uma situação. Mistura
    # revisão pesada com nova linguagem.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Sofía", "Miguel"],
                "story": (
                    "Don Miguel pousou a pena. Cruzou as mãos. Pensa.\n\n"
                    "'Tenemos cuatro pistas. Pero la pregunta es — ¿podemos "
                    "hacer algo con esto ahora?'"
                ),
                "now": "Discussão tensa. Decisão pendente. Don Miguel orienta.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Podemos confrontarla hoy mismo?",
                    "translation": "Podemos confrontá-la hoje mesmo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'podemos confrontarla'. A palavra 'podemos' significa:",
                    "options": [
                        {"id": "a", "text": "Nós podemos (se quisermos / temos a opção)"},
                        {"id": "b", "text": "Nós devemos"},
                        {"id": "c", "text": "Nós vamos"},
                        {"id": "d", "text": "Nós somos"},
                    ],
                    "correct": "a",
                    "word_id": "es_podemos", "target": "podemos", "native": "podemos",
                    "npc_reaction": "Podemos. Significa que tenemos la opción — pero no la obligación.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Yo creo que no podemos. Si la enfrentamos ahora sin pruebas, ella se va a defender — y vamos a perder lo poco que sabemos.",
                    "translation": "Eu acho que não podemos. Se a enfrentarmos agora sem provas, ela vai se defender — e vamos perder o pouco que sabemos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía disse 'no podemos'. Pra Miguel concordar — ele também acha que não podem:",
                    "options": [
                        {"id": "a", "text": "Tienes razón — no podemos"},
                        {"id": "b", "text": "Vamos a confrontarla"},
                        {"id": "c", "text": "Yo voy"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_podemos", "target": "no podemos", "native": "não podemos",
                    "npc_reaction": "No podemos. Por ahora. Bueno — pensemos qué sí podemos hacer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Yo puedo seguir observándola. Sofía puede hablar más con Carmen — quizá Carmen sabe algo más.",
                    "translation": "Eu posso seguir observando ela. Sofía pode falar mais com Carmen — talvez Carmen saiba algo mais.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'yo puedo seguir observándola'. A palavra 'puedo' significa:",
                    "options": [
                        {"id": "a", "text": "Eu posso (tenho a opção)"},
                        {"id": "b", "text": "Tu podes"},
                        {"id": "c", "text": "Ele pode"},
                        {"id": "d", "text": "Nós podemos"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedo. Yo — primera. Cuando hablo de mí mismo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero — tú puedes seguir cerca de ella. Tú eres quien le importa más. Si te abres un poco, ella va a decirte más.",
                    "translation": "Forasteiro — você pode seguir perto dela. Você é quem mais interessa pra ela. Se você se abrir um pouco, ela vai te dizer mais.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel disse 'tú puedes seguir cerca'. A palavra 'puedes' significa:",
                    "options": [
                        {"id": "a", "text": "Tu podes / você pode"},
                        {"id": "b", "text": "Eu posso"},
                        {"id": "c", "text": "Ela pode"},
                        {"id": "d", "text": "Nós podemos"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedes", "target": "puedes", "native": "podes",
                    "npc_reaction": "Puedes. Tú — segunda. Cuando le hablas a alguien.",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você pensa. Ficar perto de María. Pegar mais informação. "
                        "Mas sem comprometer o grupo. É possível? Você não sabe."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Você concorda — pode tentar. Mas você não quer mentir muito pra ela. Honesto:",
                    "options": [
                        {"id": "a", "text": "Puedo intentarlo, pero todavía no sé bien"},
                        {"id": "b", "text": "Voy a mentir mucho"},
                        {"id": "c", "text": "Soy bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo intentarlo", "native": "posso tentar",
                    "npc_reaction": "Bueno. Honestidad — eso es lo que vale. Si no puedes — paras. Nadie te obliga.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Bueno. Plan — Sofía habla con Carmen. Miguel observa por las calles. Yo me quedo en casa con María cuando vuelva. Y el forastero — habla conmigo aparte.",
                    "translation": "Bom. Plano — Sofía fala com Carmen. Miguel observa pelas ruas. Eu fico em casa com María quando ela voltar. E o forasteiro — fala comigo separado.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra você confirmar pra Don Miguel — você concorda em ficar separado com ele:",
                    "options": [
                        {"id": "a", "text": "Sí, contigo"},
                        {"id": "b", "text": "Voy a salir"},
                        {"id": "c", "text": "Soy aparte"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_si", "target": "sí", "native": "sim",
                    "npc_reaction": "Bueno. Antes de que vuelva — quiero enseñarte la carta.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía: '¿Qué carta?' Don Miguel: 'Una que guardo hace veinte años.' Pra você expressar que NÃO sabe o que é ainda:",
                    "options": [
                        {"id": "a", "text": "Todavía no sé qué es"},
                        {"id": "b", "text": "Ya sé qué es"},
                        {"id": "c", "text": "Voy a saber"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_todavia_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no sabes. Pero pronto. Hoy mismo.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Sofía e Miguel saem. Você fica com Don Miguel. Apresentação formal de
    # "poder + verbo" — sem nomear "verbo modal". Apenas: "puedo, puedes,
    # podemos — quando algo é possível ou não".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Sofía saiu pra falar com Carmen. Miguel saiu pelo lado dos "
                    "fundos pra circular pela praça. Sobrou você e Don Miguel "
                    "na cozinha.\n\n"
                    "'Antes de enseñarte la carta — quiero aclararte algo de las "
                    "palabras que oíste mucho esta mañana. Puedo, puedes, podemos.'"
                ),
                "now": "Don Miguel explica como 'puedo + verbo' funciona.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "'Poder' es lo que te dice si algo es posible o no. Yo puedo hablar — quiere decir, soy capaz de hablar. Yo no puedo volar — quiere decir, no soy capaz.",
                    "translation": "'Poder' é o que te diz se algo é possível ou não. Yo puedo hablar — quer dizer, sou capaz de falar. Yo no puedo volar — quer dizer, não sou capaz.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Puedo + verbo",
                    "meaning": "O que você é capaz de fazer / tem permissão de fazer",
                    "note": "junta dos palabras — puedo hablar, puedo entrar, puedo confiar",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo puedo ", "isKey": True},
                        {"text": "hablar · ", "isKey": False},
                        {"text": "Tú puedes ","isKey": True},
                        {"text": "ver · ",    "isKey": False},
                        {"text": "Ella puede ","isKey": True},
                        {"text": "decidir · ", "isKey": False},
                        {"text": "Podemos ",  "isKey": True},
                        {"text": "salir",     "isKey": False},
                    ],
                    "example": "Yo puedo cuidarte. Tú puedes confiar en mí. Ella puede salir cuando quiera. Podemos hablar mañana.",
                    "translation": "Eu posso cuidar de você. Tu podes confiar em mim. Ela pode sair quando quiser. Podemos falar amanhã.",
                    "note": "puedo / puedes / puede / podemos — cambia con quien puede.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra você dizer que pode tentar ficar perto de María:",
                    "options": [
                        {"id": "a", "text": "Yo puedo intentarlo"},
                        {"id": "b", "text": "Tú puedes intentar"},
                        {"id": "c", "text": "Ella puede"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedo. Cuando hablas de ti mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel: 'Cuéntame sobre ___ familia ahora — la tuya, lo que recuerdes.' Pra falar da SUA família (tua):",
                    "options": [
                        {"id": "a", "text": "tu"},
                        {"id": "b", "text": "mi"},
                        {"id": "c", "text": "su"},
                        {"id": "d", "text": "nuestra"},
                    ],
                    "correct": "a",
                    "word_id": "es_tu", "target": "tu familia", "native": "tua família",
                    "npc_reaction": "Tu familia. Cuando te hablo a ti — lo tuyo es 'tu'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel aponta pra Sofía: 'Mira a Sofía — es ___' (Sofía tem 18 anos, alta, magra). Pra descrever a altura dela (mulher):",
                    "options": [
                        {"id": "a", "text": "alta"},
                        {"id": "b", "text": "alto"},
                        {"id": "c", "text": "altos"},
                        {"id": "d", "text": "altas"},
                    ],
                    "correct": "a",
                    "word_id": "es_alta", "target": "alta", "native": "alta",
                    "npc_reaction": "Alta. Sofía — mujer, alta. La palabra termina en '-a'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "E pra você descrever a casa de Don Miguel — 'palavra de mulher, uma só':",
                    "options": [
                        {"id": "a", "text": "la casa"},
                        {"id": "b", "text": "el casa"},
                        {"id": "c", "text": "los casa"},
                        {"id": "d", "text": "las casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_la", "target": "la casa", "native": "a casa",
                    "npc_reaction": "La casa. Mi casa — y por estos días, también tuya.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Y la forma negativa — 'no puedo'. 'No puedo decirte todavía' significa que aún no eres capaz, o que aún no tienes permiso.",
                    "translation": "E a forma negativa — 'no puedo'. 'No puedo decirte todavía' significa que ainda não és capaz, ou que ainda não tens permissão.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você quer dizer que NÃO pode mentir pra María descaradamente — não é capaz:",
                    "options": [
                        {"id": "a", "text": "No puedo mentirle"},
                        {"id": "b", "text": "Puedo mentirle"},
                        {"id": "c", "text": "Voy a mentir"},
                        {"id": "d", "text": "Soy mentir"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_puedo", "target": "no puedo", "native": "não posso",
                    "npc_reaction": "No puedes. Eso es honesto contigo mismo. Te ayuda a no romperte.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Don Miguel finalmente abre o assunto da carta. Ainda não mostra — só
    # explica como ela chegou nas mãos dele. Conversa íntima. Foco em revisão
    # orgânica + uso de poder/quero/ya/todavía no.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel se levantou da mesa. Foi até o canto da cozinha "
                    "onde fica o baú velho — coberto por um pano grosso. Não "
                    "abriu ainda. Só pousou a mão nele.\n\n"
                    "'Esta carta llegó a mis manos hace veinte años. Te voy a "
                    "contar cómo.'"
                ),
                "now": "Don Miguel conta a história da carta. Você ouve.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Yo tenía veintiocho años. Trabajaba en el campo de mi padre. Un día llegó un viejo al pueblo — viajero, cansado, con una capa rota.",
                    "translation": "Eu tinha vinte e oito anos. Trabalhava no campo do meu pai. Um dia chegou um velho ao pueblo — viajante, cansado, com uma capa rota.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'yo tenía veintiocho'. 'Tenía' significa:",
                    "options": [
                        {"id": "a", "text": "Tinha (idade dele naquele tempo)"},
                        {"id": "b", "text": "Tem (agora)"},
                        {"id": "c", "text": "Vai ter"},
                        {"id": "d", "text": "É"},
                    ],
                    "correct": "a",
                    "word_id": "es_tenia", "target": "tenía", "native": "tinha",
                    "npc_reaction": "Tenía. Como 'tengo' del pasado lejano. Yo tenía esa edad cuando pasó esto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "El viejo tenía la marca de los Buscadores — igual que Eduardo. Yo entonces no la conocía. Pero la vi.",
                    "translation": "O velho tinha a marca dos Buscadores — igual a Eduardo. Eu naquela época não conhecia. Mas vi.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'no la conocía'. Pra você reagir — você AGORA já conhece a marca (depois de F17):",
                    "options": [
                        {"id": "a", "text": "Ya la conozco yo también"},
                        {"id": "b", "text": "Todavía no la conozco"},
                        {"id": "c", "text": "Voy a conocer"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya la conoces. Eso me alegra — vas más rápido que yo a tu edad.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "El viejo se quedó tres días. Me observó. Me preguntó cosas — 'puedes guardar silencio?', 'puedes esperar veinte años?'",
                    "translation": "O velho ficou três dias. Me observou. Me perguntou coisas — 'podes guardar silêncio?', 'podes esperar vinte anos?'",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "O velho perguntou 'puedes guardar silencio?'. Pra Don Miguel responder ao velho — sim, ele podia:",
                    "options": [
                        {"id": "a", "text": "Sí, puedo"},
                        {"id": "b", "text": "Tú puedes"},
                        {"id": "c", "text": "Voy a poder"},
                        {"id": "d", "text": "Soy puedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Sí, puedo. Dije eso. Y cumplí. Veinte años.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Me dio la carta. Me dijo: 'Cuando llegue alguien al pueblo con la palabra encendida — abrírsela.' Me marché. Murió a la semana siguiente.",
                    "translation": "Me deu a carta. Me disse: 'Quando chegar alguém ao pueblo com a palavra acesa — abrir pra ele.' Foi embora. Morreu na semana seguinte.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel disse 'cuando llegue alguien con la palabra encendida'. Pra você processar — você é quem fez o fogo aparecer na F5. Você confirma:",
                    "options": [
                        {"id": "a", "text": "Soy yo. Ya entiendo"},
                        {"id": "b", "text": "Todavía no soy"},
                        {"id": "c", "text": "Voy a ser"},
                        {"id": "d", "text": "Tengo"},
                    ],
                    "correct": "a",
                    "word_id": "es_soy", "target": "soy yo", "native": "sou eu",
                    "npc_reaction": "Soy yo. Eso es. Eres tú.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Esperé veinte años. Cuando vi el fuego en el pasillo aquella noche — supe que ya era el momento. Pero quería estar seguro. Ahora — con todo lo que sabemos — ya no tengo dudas.",
                    "translation": "Esperei vinte anos. Quando vi o fogo no corredor aquela noite — soube que já era o momento. Mas queria ter certeza. Agora — com tudo que sabemos — já não tenho dúvidas.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Pra você responder firme — você confia em Don Miguel (verbo confiar, com 'en'):",
                    "options": [
                        {"id": "a", "text": "Confío en ti"},
                        {"id": "b", "text": "Confías en ti"},
                        {"id": "c", "text": "Voy a confiar"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_confiar", "target": "confío", "native": "confio",
                    "npc_reaction": "Confías. Bueno. Eso me importa. Vamos al baúl.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Don Miguel se aproxima do baú. Hesita. Pergunta uma última vez se você
    # está pronto. Gate: errar trava. Closing prepara F19 (carta revelada).
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Don Miguel"],
                "story": (
                    "Don Miguel está em pé do lado do baú. A mão sobre a tampa. "
                    "Você sentado na mesa, café frio na frente. Nenhum dos dois "
                    "falou nos últimos dois minutos.\n\n"
                    "'Antes de abrirlo — quiero preguntarte algo. Y quiero la "
                    "verdad.'"
                ),
                "now": "Decisão final. Você precisa estar pronto.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "📦 Baú velho · Tampa fechada · Don Miguel com a mão sobre ele",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "¿Estás listo para ver una cosa que va a cambiar lo que sabes de ti?",
                    "translation": "Está pronto pra ver uma coisa que vai mudar o que sabe de você?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você precisa decidir. Honesto — tem medo, mas quer ver. Resposta com ya / todavía no e querer:",
                    "options": [
                        {"id": "a", "text": "Tengo miedo, pero ya quiero verla"},
                        {"id": "b", "text": "Todavía no quiero"},
                        {"id": "c", "text": "Soy listo"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_ya", "target": "ya quiero", "native": "já quero",
                    "npc_reaction": "Bueno. Es la respuesta correcta. El miedo no se va — pero el querer es más fuerte.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Una pregunta más — ¿puedes guardar lo que vamos a ver? Aunque María pregunte directamente?",
                    "translation": "Uma pergunta mais — você pode guardar o que vamos ver? Mesmo se María perguntar diretamente?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Você responde — sim, pode. Junte 'puedo' com 'guardar':",
                    "options": [
                        {"id": "a", "text": "Sí, puedo guardarlo"},
                        {"id": "b", "text": "Sí, tú puedes"},
                        {"id": "c", "text": "Voy a guardar"},
                        {"id": "d", "text": "Soy guardar"},
                    ],
                    "correct": "a",
                    "word_id": "es_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedo guardarlo. Bueno. Cuando dices 'puedo', te haces responsable.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Última — ¿confías en mí?",
                    "translation": "Última — confia em mim?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Resposta firme — sim, confia em Don Miguel:",
                    "options": [
                        {"id": "a", "text": "Sí, confío en ti"},
                        {"id": "b", "text": "No confío"},
                        {"id": "c", "text": "Voy a confiar"},
                        {"id": "d", "text": "Soy confío"},
                    ],
                    "correct": "a",
                    "word_id": "es_confiar", "target": "confío", "native": "confio",
                    "npc_reaction": "Confías. Y yo en ti también. Bueno — vamos.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F19 ────────────────────────
                {
                    "kind": "scene",
                    "text": "📦 Don Miguel levanta a tampa do baú · Dentro: papéis velhos, livros, um envelope selado em cera vermelha",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel pegou o envelope. Mostrou pra você. O selo em "
                        "cera tinha o mesmo símbolo da marca de Eduardo — o sol "
                        "partido.\n\n"
                        "Você nunca tinha visto. Mas sentiu o peito apertar — "
                        "como quando 'fuego' saiu na F5. Algo dentro reconheceu."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Mañana — al amanecer — la abrimos juntos. Hoy dormimos. Necesitas la cabeza clara.",
                    "translation": "Amanhã — ao amanhecer — abrimos juntos. Hoje dormimos. Você precisa da cabeça clara.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Don Miguel fechou o baú. Trancou. Pôs o pano em cima. "
                        "María não tinha voltado ainda do mercado.\n\n"
                        "Você foi pro quarto. Deitou de olhos abertos. A imagem do "
                        "envelope com cera vermelha não saía da cabeça.\n\n"
                        "Amanhã."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
