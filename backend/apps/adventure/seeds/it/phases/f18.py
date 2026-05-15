"""
Seed das 6 seções da Fase 18 Italiano A1 — "Antonio il Contadino se entera".

Os três giovanes reuniram tudo. Antonio il Contadino ouviu. Decisão pendente:
o que fazer com Lucia agora que existem três pistas concretas
(passado dela com Podesta via Bianca, marca dos Buscadores, sussurro
de Lucía).

Decisão final: continuar observando — sem confrontar. Mas Antonio il Contadino
revela que tem uma carta guardada faz 20 anni. Vai mostrar amanhã.

VOCAB NOVO (3): verdad · mentir · confiar
LINGUAGEM NOVA: poder + verbo (puedo / puedes / puede / podemos)
    Apresentado pelo uso natural — "no puedo decirle, todavía no"

Revisão F1-F17 dominante:
  · ya / todavía no (F17)
  · quiero + verbo (F16)
  · vi/hablé/oí (F12)
  · mi/tu/su (F13)
  · el/la (F14)
  · sono/sto/ho (F8)

NPC principais: Antonio il Contadino · Chiara · Nico · você
Arco emocional: dúvida → reunião → decisão coletiva → tensão crescente
Transição: F19 abre logo após — Antonio il Contadino já indo até o baú.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Manhã cedo. Chiara e Nico chegam à casa de Antonio il Contadino. Lucia saiu
    # cedo — disse que ia ao mercato. Os 4 (Antonio il Contadino + 3 giovanes) na cozinha.
    # 2 novos exer + 2 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌅 Casa de Antonio il Contadino · Manhã cedo · Cozinha\n\n"
                        "Lucia saiu prima do amanhecer — disse que ia ao mercato "
                        "comprar erbe. Chiara e Nico chegaram logo depois. "
                        "Antonio il Contadino preparou café forte. Quatro tigelas humeprima "
                        "na mesa baixa."
                    ),
                },
                {
                    "kind": "skill_check",
                    "skill": "cura",
                    "min_level": 2,
                    "uses_item_tag": "remedio",
                    "success": "Voce improvisa cuidado limpo antes que a dor vire problema maior.",
                    "fallback": "Sem tecnica suficiente, voce faz o basico e aceita ajuda para seguir.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Bene. Prima de que vuelva — andiamo a juntar todo lo que sabemos.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "Empezamos por Bianca, después la marca, después lo de tu mujer.",
                    "pace": "slow",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio il Contadino",
                    "line": "Sí. Ma prima — quiero saber qué creen voi. Senza que yo influya.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Antonio il Contadino quer ouvir vocês primeiro. Chiara olha pra Nico. Nico olha pra você. Você decide começar.",
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
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino cumprimentou vocês — amanhecer cedo:",
                    "options": [
                        {"id": "a", "text": "Benes días, Antonio il Contadino"},
                        {"id": "b", "text": "Buona notte"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Benes días. Hijo — empieza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Lo que tenemos que decidir hoy es importante. Ma la verdad — ¿qué sentimos sobre Lucia?",
                    "translation": "O que temos que decidir hoje é importante. Mas a verdade — o que sentimos sobre Lucia?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino falou 'la verdad'. Significa:",
                    "options": [
                        {"id": "a", "text": "Verdade (o que é real)"},
                        {"id": "b", "text": "Mentira"},
                        {"id": "c", "text": "Pergunta"},
                        {"id": "d", "text": "Resposta"},
                    ],
                    "correct": "a",
                    "word_id": "it_verdad", "target": "verdad", "native": "verdade",
                    "npc_reaction": "Verdad. La cosa que es. Aunque duela.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Chiara responde — 'no es que Lucia mienta. Es que oculta cose.' A palavra 'mentir' significa:",
                    "options": [
                        {"id": "a", "text": "Dizer algo falso"},
                        {"id": "b", "text": "Dizer a verdade"},
                        {"id": "c", "text": "Estar quieto"},
                        {"id": "d", "text": "Sair correndo"},
                    ],
                    "correct": "a",
                    "word_id": "it_mentir", "target": "mentir", "native": "mentir",
                    "npc_reaction": "Mentir. Decir algo falso. Chiara hace bene la distinción — Lucia no miente. Calla.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico: 'La pregunta es — ¿podemos confiar en ella?' A palavra 'confiar' significa:",
                    "options": [
                        {"id": "a", "text": "Acreditar que alguém é seguro"},
                        {"id": "b", "text": "Esconder coisas"},
                        {"id": "c", "text": "Lutar"},
                        {"id": "d", "text": "Sair"},
                    ],
                    "correct": "a",
                    "word_id": "it_confiar", "target": "confiar", "native": "confiar",
                    "npc_reaction": "Confiar. Creer que alguien no te va a hacer daño. Esa palabra siempre se gana — nunca se da.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # Os 3 contam pra Antonio il Contadino as 3 pistas em detalhe. 100% revisão F1-F17.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Chiara", "Nico"],
                "story": (
                    "Antonio il Contadino pegou um pedaço de papel velho e uma pena. "
                    "Quer anotar — pra ter clareza.\n\n"
                    "'Empezamos. Primero — lo de Bianca. Chiara — cuéntalo tu.'"
                ),
                "now": "Cada pista é contada do que já passou. Antonio il Contadino anota.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Bianca nos contó que fue novia del Podesta hace veinticinco años. El padre del Podesta rompió el compromiso.",
                    "translation": "Bianca nos contou que foi noiva do Podesta há vinte e cinco anni. O pai do Podesta quebrou o noivado.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Chiara disse 'Bianca nos contó'. 'Contó' significa que Bianca:",
                    "options": [
                        {"id": "a", "text": "Contou (já passou)"},
                        {"id": "b", "text": "Conta (agora)"},
                        {"id": "c", "text": "Vai contar"},
                        {"id": "d", "text": "Sou contar"},
                    ],
                    "correct": "a",
                    "word_id": "it_conto", "target": "contó", "native": "contou",
                    "npc_reaction": "Contó. Ya pasó. Anotando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Y mi madre — anotte en la cocina — me ha detto que conoce a Lucia de algún sitio. No recuerda de dónde.",
                    "translation": "E minha mãe — ontem à noite na cozinha — me disse que conhece Lucia de algum lugar. Não lembra de onde.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Nico disse 'me ha detto'. Pra você confirmar pra Antonio il Contadino — você ouviu o sussurro também:",
                    "options": [
                        {"id": "a", "text": "Yo también lo oí"},
                        {"id": "b", "text": "Yo oigo"},
                        {"id": "c", "text": "Vado a oír"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oí. Bene. Dos puntos confirmados.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Y ayer — la marca de Pietro. Lucia la reconoció senza disfrazar. Ha detto que su familia tenía relación con esa gente.",
                    "translation": "E ontem — a marca de Pietro. Lucia a reconheceu sem disfarçar. Disse que sua família tinha relação com essa gente.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino resumiu três pistas. Pra você confirmar que entendeu:",
                    "options": [
                        {"id": "a", "text": "Sí, ya entiendo las tres"},
                        {"id": "b", "text": "Todavía no entiendo"},
                        {"id": "c", "text": "Vado a entender"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya entiendes. Bene.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Y hay otra cosa que solo el forestiero y yo sabemos. Lo de la cena con Lucia — ella sabía cose que el forestiero nunca contó.",
                    "translation": "E tem outra coisa que só o forasteiro e eu sabemos. Aquilo do jantar com Lucia — ela sabia coisas que o forasteiro nunca contou.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino: 'Cuatro pistas. ¿Y qué siente cada uno?' Você responde honesto — tem medo:",
                    "options": [
                        {"id": "a", "text": "Ho paura"},
                        {"id": "b", "text": "Sto paura"},
                        {"id": "c", "text": "Sono paura"},
                        {"id": "d", "text": "Vado paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_paura", "target": "ho paura", "native": "tenho medo",
                    "npc_reaction": "Ho paura. Es válido — y necesario.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta — 'Antonio il Contadino — ¿tu la conoces de prima?' Pra Antonio il Contadino ela usa 'tu' formale?Não — informale. Resposta dela:",
                    "options": [
                        {"id": "a", "text": "No, no la conozco de prima"},
                        {"id": "b", "text": "Sí, la conozco"},
                        {"id": "c", "text": "Vado a conocerla"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_no", "target": "no", "native": "não",
                    "npc_reaction": "No. Ma mi mujer sí. Y questo pesa.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Antonio il Contadino apresenta "poder + verbo" pelo uso. "¿Podemos confrontarla?
    # ¿Podemos echarla?¿Puedo confiar?" Cada exercício uma situação. Mistura
    # revisão pesada com nova linguagem.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino", "Chiara", "Nico"],
                "story": (
                    "Antonio il Contadino pousou a pena. Cruzou as mãos. Pensa.\n\n"
                    "'Tenemos cuatro pistas. Ma la pregunta es — ¿podemos "
                    "hacer algo con esto adesso?'"
                ),
                "now": "Discussão tensa. Decisão pendente. Antonio il Contadino orienta.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "¿Podemos confrontarla hoy mismo?",
                    "translation": "Podemos confrontá-la hoje mesmo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino disse 'podemos confrontarla'. A palavra 'podemos' significa:",
                    "options": [
                        {"id": "a", "text": "Nós podemos (se quisermos / temos a opção)"},
                        {"id": "b", "text": "Nós devemos"},
                        {"id": "c", "text": "Nós andiamo"},
                        {"id": "d", "text": "Nós somos"},
                    ],
                    "correct": "a",
                    "word_id": "it_podemos", "target": "podemos", "native": "podemos",
                    "npc_reaction": "Podemos. Significa que tenemos la opción — ma no la obligación.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Yo creo que no podemos. Si la enfrentamos adesso senza pruebas, ella se va a defender — y andiamo a perder lo poco que sabemos.",
                    "translation": "Eu acho que não podemos. Se a enfrentarmos agora sem provas, ela vai se defender — e andiamo perder o pouco que sabemos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara disse 'no podemos'. Pra Nico concordar — ele também acha que não podem:",
                    "options": [
                        {"id": "a", "text": "Hai razón — no podemos"},
                        {"id": "b", "text": "Andiamo a confrontarla"},
                        {"id": "c", "text": "Io vado"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_podemos", "target": "no podemos", "native": "não podemos",
                    "npc_reaction": "No podemos. Por adesso. Bene — pensemos qué sí podemos hacer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Yo puedo seguir observándola. Chiara puede hablar más con Bianca — quizá Bianca sabe algo más.",
                    "translation": "Eu posso seguir observando ela. Chiara pode falar mais com Bianca — talvez Bianca saiba algo mais.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino disse 'yo puedo seguir observándola'. A palavra 'puedo' significa:",
                    "options": [
                        {"id": "a", "text": "Eu posso (tenho a opção)"},
                        {"id": "b", "text": "Tu podes"},
                        {"id": "c", "text": "Ele pode"},
                        {"id": "d", "text": "Nós podemos"},
                    ],
                    "correct": "a",
                    "word_id": "it_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedo. Yo — primera. Cuando hablo de mí mismo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Forestiero — tu puedes seguir cerca de ella. Tu eres chi le importa más. Si te abres un poco, lei va a decirte más.",
                    "translation": "Forasteiro — você pode seguir perto dela. Você é quem mais interessa pra ela. Se você se abrir um pouco, ela vai te dizer mais.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico disse 'tu puedes seguir cerca'. A palavra 'puedes' significa:",
                    "options": [
                        {"id": "a", "text": "Tu podes / você pode"},
                        {"id": "b", "text": "Eu posso"},
                        {"id": "c", "text": "Ela pode"},
                        {"id": "d", "text": "Nós podemos"},
                    ],
                    "correct": "a",
                    "word_id": "it_puedes", "target": "puedes", "native": "podes",
                    "npc_reaction": "Puedes. Tu — segunda. Cuando le hablas a alguien.",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você pensa. Ficar perto de Lucia. Pegar mais informação. "
                        "Mas sem comprometer o grupo. É possível?Você não sabe."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Você concorda — pode tentar. Mas você não quer mentir muito pra ela. Honesto:",
                    "options": [
                        {"id": "a", "text": "Puedo intentarlo, ma todavía no sé bene"},
                        {"id": "b", "text": "Vado a mentir mucho"},
                        {"id": "c", "text": "Sono bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_puedo", "target": "puedo intentarlo", "native": "posso tentar",
                    "npc_reaction": "Bene. Honestidad — questo es lo que vale. Si no puedes — paras. Nadie te obliga.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Bene. Plan — Chiara habla con Bianca. Nico observa por las stradas. Yo me quedo en casa con Lucia cuando vuelva. Y el forestiero — habla con me aparte.",
                    "translation": "Bom. Plano — Chiara fala com Bianca. Nico observa pelas ruas. Eu fico em casa com Lucia quando ela voltar. E o forasteiro — fala comigo separado.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Pra você confirmar pra Antonio il Contadino — você concorda em ficar separado com ele:",
                    "options": [
                        {"id": "a", "text": "Sí, con te"},
                        {"id": "b", "text": "Vado a uscire"},
                        {"id": "c", "text": "Sono aparte"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_si", "target": "sí", "native": "sim",
                    "npc_reaction": "Bene. Prima de que vuelva — quiero enseñarte la carta.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara: '¿Qué carta?' Antonio il Contadino: 'Una que guardo hace veinte años.' Pra você expressar que NÃO sabe o que é ainda:",
                    "options": [
                        {"id": "a", "text": "Todavía no sé qué es"},
                        {"id": "b", "text": "Ya sé qué es"},
                        {"id": "c", "text": "Vado a saber"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ancora_no", "target": "todavía no", "native": "ainda não",
                    "npc_reaction": "Todavía no sabes. Ma pronto. Hoy mismo.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Chiara e Nico saem. Você fica com Antonio il Contadino. Apresentação formale de
    # "poder + verbo" — sem nomear "verbo modal". Apenas: "puedo, puedes,
    # podemos — quando algo é possível ou não".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino"],
                "story": (
                    "Chiara saiu pra falar com Bianca. Nico saiu pelo lado dos "
                    "fundos pra circular pela praça. Sobrou você e Antonio il Contadino "
                    "na cozinha.\n\n"
                    "'Prima de enseñarte la carta — quiero aclararte algo de las "
                    "parole que oíste mucho esta mañana. Puedo, puedes, podemos.'"
                ),
                "now": "Antonio il Contadino explica come 'puedo + verbo' funciona.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "'Poder' es lo que te dice si algo es posible o no. Yo puedo hablar — quiere decir, sono capaz de hablar. Yo no puedo volar — quiere decir, no sono capaz.",
                    "translation": "'Poder' é o que te diz se algo é possível ou não. Yo puedo hablar — quer dizer, sou capaz de falar. Yo no puedo volar — quer dizer, não sou capaz.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Puedo + verbo",
                    "meaning": "O que você é capaz de fazer / tem permissão de fazer",
                    "note": "junta dos parole — puedo hablar, puedo entrar, puedo confiar",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Yo puedo ", "isKey": True},
                        {"text": "hablar · ", "isKey": False},
                        {"text": "Tu puedes ","isKey": True},
                        {"text": "ver · ",    "isKey": False},
                        {"text": "Ella puede ","isKey": True},
                        {"text": "decidir · ", "isKey": False},
                        {"text": "Podemos ",  "isKey": True},
                        {"text": "uscire",     "isKey": False},
                    ],
                    "example": "Yo puedo cuidarte. Tu puedes confiar en mí. Ella puede uscire cuando quiera. Podemos hablar mañana.",
                    "translation": "Eu posso cuidar de você. Tu podes confiar em mim. Ela pode sair quando quiser. Podemos falar amanhã.",
                    "note": "puedo / puedes / puede / podemos — cambia con chi puede.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Pra você dizer que pode tentar ficar perto de Lucia:",
                    "options": [
                        {"id": "a", "text": "Yo puedo intentarlo"},
                        {"id": "b", "text": "Tu puedes intentar"},
                        {"id": "c", "text": "Ella puede"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedo. Cuando hablas de ti mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino: 'Cuéntame sobre ___ familia adesso — la tuya, lo que recuerdes.' Pra falar da SUA família (tua):",
                    "options": [
                        {"id": "a", "text": "tu"},
                        {"id": "b", "text": "mi"},
                        {"id": "c", "text": "su"},
                        {"id": "d", "text": "nuestra"},
                    ],
                    "correct": "a",
                    "word_id": "it_tu", "target": "tu familia", "native": "tua família",
                    "npc_reaction": "Tu familia. Cuando te hablo a ti — lo tuyo es 'tu'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino aponta pra Chiara: 'Guarda a Chiara — es ___' (Chiara tem 18 anni, alta, magra). Pra descrever a altura dela (mulher):",
                    "options": [
                        {"id": "a", "text": "alta"},
                        {"id": "b", "text": "alto"},
                        {"id": "c", "text": "altos"},
                        {"id": "d", "text": "altas"},
                    ],
                    "correct": "a",
                    "word_id": "it_alta", "target": "alta", "native": "alta",
                    "npc_reaction": "Alta. Chiara — mujer, alta. La palabra termina en '-a'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "E pra você descrever a casa de Antonio il Contadino — 'palavra de mulher, uma só':",
                    "options": [
                        {"id": "a", "text": "la casa"},
                        {"id": "b", "text": "el casa"},
                        {"id": "c", "text": "los casa"},
                        {"id": "d", "text": "las casa"},
                    ],
                    "correct": "a",
                    "word_id": "it_la", "target": "la casa", "native": "a casa",
                    "npc_reaction": "La casa. Mi casa — y por estos días, también tuya.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Y la forma negativa — 'no puedo'. 'No puedo decirte todavía' significa que aún no eres capaz, o que aún no hai permiso.",
                    "translation": "E a forma negativa — 'no puedo'. 'No puedo decirte todavía' significa que ainda não és capaz, ou que ainda não tens permissão.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você quer dizer que NÃO pode mentir pra Lucia descaradamente — não é capaz:",
                    "options": [
                        {"id": "a", "text": "No puedo mentirle"},
                        {"id": "b", "text": "Puedo mentirle"},
                        {"id": "c", "text": "Vado a mentir"},
                        {"id": "d", "text": "Sono mentir"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_puedo", "target": "no puedo", "native": "não posso",
                    "npc_reaction": "No puedes. Esatto es honesto con te mismo. Te ayuda a no romperte.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Antonio il Contadino finalmente abre o assunto da carta. Ainda não mostra — só
    # explica come ela chegou nas mãos dele. Conversa íntima. Foco em revisão
    # orgânica + uso de poder/quero/ya/todavía no.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino"],
                "story": (
                    "Antonio il Contadino se levantou da mesa. Foi até o canto da cozinha "
                    "onde fica o baú velho — coberto por um paneo grosso. Não "
                    "abriu ainda. Só pousou a mão nele.\n\n"
                    "'Esta carta llegó a mis manni hace veinte años. Te vado a "
                    "contar cómo.'"
                ),
                "now": "Antonio il Contadino conta a história da carta. Você ouve.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Yo tenía veintiocho años. Trabajaba en el campo de mi padre. Un día llegó un viejo al borgo — viajero, cansado, con una capa rota.",
                    "translation": "Eu tinha vinte e oito anni. Trabalhava no campo do meu pai. Um dia chegou um velho ao borgo — viajante, cansado, com uma capa rota.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino disse 'yo tenía veintiocho'. 'Tenía' significa:",
                    "options": [
                        {"id": "a", "text": "Tinha (idade dele naquele tempo)"},
                        {"id": "b", "text": "Tem (agora)"},
                        {"id": "c", "text": "Vai ter"},
                        {"id": "d", "text": "É"},
                    ],
                    "correct": "a",
                    "word_id": "it_tenia", "target": "tenía", "native": "tinha",
                    "npc_reaction": "Tenía. Como 'ho' del pasado lejano. Yo tenía esa edad cuando pasó esto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "El viejo tenía la marca de los Buscadores — igual que Pietro. Yo entonces no la conocía. Ma la vi.",
                    "translation": "O velho tinha a marca dos Buscadores — igual a Pietro. Eu naquela época não conhecia. Mas vi.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino disse 'no la conocía'. Pra você reagir — você AGORA já conhece a marca (depois de F17):",
                    "options": [
                        {"id": "a", "text": "Ya la conozco yo también"},
                        {"id": "b", "text": "Todavía no la conozco"},
                        {"id": "c", "text": "Vado a conocer"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_ya", "target": "ya", "native": "já",
                    "npc_reaction": "Ya la conoces. Esatto me alegra — vas más rápido que yo a tu edad.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "El viejo se quedó tres días. Me observó. Me preguntó cose — 'puedes guardar silencio?', 'puedes esperar veinte años?'",
                    "translation": "O velho ficou três dias. Me observou. Me perguntou coisas — 'podes guardar silêncio?', 'podes esperar vinte anni?'",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "O velho perguntou 'puedes guardar silencio?'. Pra Antonio il Contadino responder ao velho — sim, ele podia:",
                    "options": [
                        {"id": "a", "text": "Sí, puedo"},
                        {"id": "b", "text": "Tu puedes"},
                        {"id": "c", "text": "Vado a poder"},
                        {"id": "d", "text": "Sono puedo"},
                    ],
                    "correct": "a",
                    "word_id": "it_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Sí, puedo. Dije questo. Y cumplí. Veinte años.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Me dio la carta. Me ha detto: 'Cuando arrivi alguien al borgo con la palabra encendida — abrírsela.' Me marché. Murió a la semana siguiente.",
                    "translation": "Me deu a carta. Me disse: 'Quando chegar alguém ao borgo com a palavra acesa — abrir pra ele.' Foi embora. Morreu na semana seguinte.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Antonio il Contadino disse 'cuando arrivi alguien con la palabra encendida'. Pra você processar — você é quem fez o fogo aparecer na F5. Você confirma:",
                    "options": [
                        {"id": "a", "text": "Sono yo. Ya entiendo"},
                        {"id": "b", "text": "Todavía no sono"},
                        {"id": "c", "text": "Vado a ser"},
                        {"id": "d", "text": "Ho"},
                    ],
                    "correct": "a",
                    "word_id": "it_sono", "target": "sono yo", "native": "sou eu",
                    "npc_reaction": "Sono yo. Esatto es. Eres tu.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Esperé veinte años. Cuando vi el fuoco en el pasillo aquella notte — supe que ya era el momento. Ma quería estar seguro. Adesso — con todo lo que sabemos — ya no ho dudas.",
                    "translation": "Esperei vinte anni. Quando vi o fogo no corredor aquela noite — soube que já era o momento. Mas queria ter certeza. Agora — com tudo que sabemos — já não tenho dúvidas.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Pra você responder firme — você confia em Antonio il Contadino (verbo confiar, com 'en'):",
                    "options": [
                        {"id": "a", "text": "Confío en ti"},
                        {"id": "b", "text": "Confías en ti"},
                        {"id": "c", "text": "Vado a confiar"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_confiar", "target": "confío", "native": "confio",
                    "npc_reaction": "Confías. Bene. Esatto me importa. Andiamo al baúl.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Antonio il Contadino se aproxima do baú. Hesita. Pergunta uma última vez se você
    # está pronto. Gate: errar trava. Closenzag prepara F19 (carta revelada).
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Antonio il Contadino"],
                "story": (
                    "Antonio il Contadino está em pé do lado do baú. A mão sobre a tampa. "
                    "Você sentado na mesa, café frio na fronte. Nenhum dos dois "
                    "falou nos últimos dois minutos.\n\n"
                    "'Prima de abrirlo — quiero preguntarte algo. Y quiero la "
                    "verdad.'"
                ),
                "now": "Decisão final. Você precisa estar pronto.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "📦 Baú velho · Tampa fechada · Antonio il Contadino com a mão sobre ele",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "¿Estás listo para ver una cosa que va a cambiar lo que sabes de ti?",
                    "translation": "Está pronto pra ver uma coisa que vai mudar o que sabe de você?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você precisa decidir. Honesto — tem medo, piu quer ver. Resposta com ya / todavía no e querer:",
                    "options": [
                        {"id": "a", "text": "Ho paura, ma ya quiero verla"},
                        {"id": "b", "text": "Todavía no quiero"},
                        {"id": "c", "text": "Sono listo"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_ya", "target": "ya quiero", "native": "já quero",
                    "npc_reaction": "Bene. Es la respuesta correcta. El paura no se va — ma el querer es más fuerte.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Una pregunta más — ¿puedes guardar lo que andiamo a ver?Aunque Lucia pregunte directamente?",
                    "translation": "Uma pergunta mais — você pode guardar o que andiamo ver?Mesmo se Lucia perguntar diretamente?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Você responde — sim, pode. Junte 'puedo' com 'guardar':",
                    "options": [
                        {"id": "a", "text": "Sí, puedo guardarlo"},
                        {"id": "b", "text": "Sí, tu puedes"},
                        {"id": "c", "text": "Vado a guardar"},
                        {"id": "d", "text": "Sono guardar"},
                    ],
                    "correct": "a",
                    "word_id": "it_puedo", "target": "puedo", "native": "posso",
                    "npc_reaction": "Puedo guardarlo. Bene. Cuando dices 'puedo', te haces responsable.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Última — ¿confías en mí?",
                    "translation": "Última — confia em mim?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio il Contadino",
                    "question": "Resposta firme — sim, confia em Antonio il Contadino:",
                    "options": [
                        {"id": "a", "text": "Sí, confío en ti"},
                        {"id": "b", "text": "No confío"},
                        {"id": "c", "text": "Vado a confiar"},
                        {"id": "d", "text": "Sono confío"},
                    ],
                    "correct": "a",
                    "word_id": "it_confiar", "target": "confío", "native": "confio",
                    "npc_reaction": "Confías. Y yo en ti también. Bene — andiamo.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F19 ────────────────────────
                {
                    "kind": "scene",
                    "text": "📦 Antonio il Contadino levanta a tampa do baú · Dentro: papéis velhos, livros, um envelope selado em cera vermelha",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio il Contadino pegou o envelope. Mostrou pra você. O selo em "
                        "cera tinha o mesmo símbolo da marca de Pietro — o sol "
                        "partido.\n\n"
                        "Você nunca tinha visto. Mas sentiu o peito apertar — "
                        "come quando 'fuoco' saiu na F5. Algo dentro reconheceu."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Mañana — al amanecer — la abrimos juntos. Hoy dormimos. Necesitas la testa clara.",
                    "translation": "Amanhã — ao amanhecer — abrimos juntos. Hoje dormimos. Você precisa da cabeça clara.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Antonio il Contadino fechou o baú. Trancou. Pôs o paneo em cima. "
                        "Lucia não tinha voltado ainda do mercato.\n\n"
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


