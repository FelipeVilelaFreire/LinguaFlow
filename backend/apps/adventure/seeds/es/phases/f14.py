"""
Seed das 6 seções da Fase 14 Espanhol A1 — "La cena de María".

⚠️ MILESTONE OBRIGATÓRIO (canônico — story.md):
    F14 = 3ª fase de revisão. A Marta-equivalente (María) está no
    cenário, observando. Precisa que o protagonista fique e fique
    mais forte para o ritual.

María convida todos pra jantar na casa de hóspedes. Pede que cada
um conte o que viveu. Ela escuta. Anota mentalmente. Calibra.

No fim, María faz uma pergunta que mostra que ela sabe coisas que
ninguém contou pra ela. O jogador pega a pista, os personagens
ainda não.

ABORDAGEM PEDAGÓGICA:
    Esta é fase de REVISÃO. Apresenta apenas 1 novidade: como
    el/la/los/las trabalha (palavrinhas que vão na frente).
    Explicado simples como "para palavras de homem (el/los) ou
    de mulher (la/las)". Sem nomear "artigo definido".

Vocab novo (minimal): foco em revisão.
Apresentação adicional: el/la/los/las (já usados sem saber desde F1)

Revisão F1-F13 dominante (~75% dos exercícios):
  · vi/hablé/oí (F12) — relato
  · mi/tu/su (F13) — pertencimento
  · voy a / vamos a (F11) — futuro próximo
  · soy/estoy/tengo (F8)
  · me llamo / tengo X años / gracias
  · me gusta / no me gusta (F9)

NPC principais: María (observadora central) · os 4
Arco emocional: revisão coletiva → leveza enganosa → momento gélido no fim
Transição: F15 abre na manhã seguinte, todos calados.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f14_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Os 4 chegando à casa de hóspedes de María. Convite formal pra jantar.
    # Apresentação suave de el/la/los/las nas próprias frases dos NPCs.
    # 1 exercício novo + 3 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "sustento",
                    "min_level": 2,
                    "uses_item_tag": "comida",
                    "success": "Voce reconhece a comida da mesa e acompanha a revisao sem quebrar o ritual da janta.",
                    "fallback": "Voce erra a ordem dos pratos, mas Lucia ri baixo e deixa a revisao continuar.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🕯️ Casa de hóspedes de María · Noite · Mesa posta\n\n"
                        "María preparou tudo desde a manhã. Vela no centro da "
                        "mesa, pão fresco que ela mesma assou, guisado fumegante, "
                        "uma jarra de vinho leve. Quatro pratos. Um lugar pra "
                        "Don Miguel também — caso quisesse vir."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "Os 4 entram. Don Miguel não veio. Sobrou vocês quatro com María.",
                },
                {
                    "kind": "npc",
                    "npc": "María",
                    "line": "Bienvenidos. Siéntense — todos. Esta noche quiero oír.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Sofía olha pra você por um segundo. Miguel já se "
                        "lembrava do sussurro da mãe. Você sabe que ele sabe — "
                        "e ele sabe que você sabe."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "María",
                    "line": "Vamos a comer primero. Después — cuéntenme. Cada uno. Lo que vivieron estos diez días.",
                    "pace": "slow",
                },
                {
                    "kind": "scene",
                    "text": "🍷 Sopa servida · Vinho leve · Cada um pega o próprio pão",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "el",  "native": "o (pra palavra de homem)"},
                        {"target": "la",  "native": "a (pra palavra de mulher)"},
                        {"target": "los", "native": "os (muitos, homem)"},
                        {"target": "las", "native": "as (muitas, mulher)"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María serve o caldo: 'Esta es ___ sopa de mi abuela.' Você já reparou — antes de 'sopa' sempre vem 'la' (sopa é palavra de mulher):",
                    "options": [
                        {"id": "a", "text": "la"},
                        {"id": "b", "text": "el"},
                        {"id": "c", "text": "los"},
                        {"id": "d", "text": "las"},
                    ],
                    "correct": "a",
                    "word_id": "es_la", "target": "la", "native": "a (pra mulher)",
                    "npc_reaction": "La sopa. Igual que la cocina, la mesa, la noche — todas palavras de mujer.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pede pão. 'Pásame ___ pan, por favor.' Pan é palavra de homem (você já tinha usado 'el pan' várias vezes):",
                    "options": [
                        {"id": "a", "text": "el"},
                        {"id": "b", "text": "la"},
                        {"id": "c", "text": "los"},
                        {"id": "d", "text": "las"},
                    ],
                    "correct": "a",
                    "word_id": "es_el", "target": "el", "native": "o (pra homem)",
                    "npc_reaction": "El pan. Como el campesino, el río, el pueblo — todas de hombre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel olha pra María: 'Estos guisos están bien hechos.' Pra dizer 'os guisos' (palavra de homem, muitos):",
                    "options": [
                        {"id": "a", "text": "los"},
                        {"id": "b", "text": "las"},
                        {"id": "c", "text": "el"},
                        {"id": "d", "text": "la"},
                    ],
                    "correct": "a",
                    "word_id": "es_los", "target": "los", "native": "os (muitos, homem)",
                    "npc_reaction": "Los guisos. 'El' se hace 'los' cuando hay muchos. Igual que 'la' se hace 'las'.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. María pergunta sobre os primeiros dias. Mistura de
    # F1-F13 — pretérito recém aprendido (F12), possessivos (F13), futuro
    # próximo (F11), saudações, identidade.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["María"],
                "story": (
                    "Vocês comeram. Pão sumiu rápido. Vinho leve, não enche a "
                    "cabeça mas relaxa. María sentou — não comeu muito. Esperou.\n\n"
                    "'Bueno. Empezamos. Forastero — empieza tú. Cuéntame del "
                    "primer día. Desde que pisaste el pueblo.'"
                ),
                "now": "María quer cada detalhe. Você relata. Cada pergunta é revisão.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Primero — ¿quién te encontró primero? ¿Quién te habló primero?",
                    "translation": "Primeiro — quem te encontrou primeiro? Quem falou contigo primeiro?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Rosa foi a primeira voz que você ouviu. Pra contar que ELA falou primeiro:",
                    "options": [
                        {"id": "a", "text": "Rosa habló conmigo primero"},
                        {"id": "b", "text": "Rosa habla conmigo primero"},
                        {"id": "c", "text": "Rosa va a hablar"},
                        {"id": "d", "text": "Rosa soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_hablo", "target": "habló", "native": "ela falou",
                    "npc_reaction": "Habló — ella, ya pasó. Rosa siempre encuentra a los forasteros.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Y la palabra primera que aprendiste? ¿Recuerdas cuál fue?",
                    "translation": "E a primeira palavra que você aprendeu? Lembra qual foi?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Pan. Foi a primeira palavra que Rosa repetiu com você. Pra contar que VOCÊ aprendeu:",
                    "options": [
                        {"id": "a", "text": "Aprendí 'pan'"},
                        {"id": "b", "text": "Aprendo 'pan'"},
                        {"id": "c", "text": "Voy a aprender 'pan'"},
                        {"id": "d", "text": "Soy 'pan'"},
                    ],
                    "correct": "a",
                    "word_id": "es_aprendi", "target": "aprendí", "native": "aprendi",
                    "npc_reaction": "Pan. Suficiente para el primer día. La palabra que abrió todas las demás.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Y la familia de Miguel? ¿Cómo te trataron anoche?",
                    "translation": "E a família de Miguel? Como te trataram ontem à noite?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Bem. Pra falar de coisas DELES (família de Miguel, terceira pessoa):",
                    "options": [
                        {"id": "a", "text": "Su casa es cálida"},
                        {"id": "b", "text": "Mi casa es cálida"},
                        {"id": "c", "text": "Tu casa es cálida"},
                        {"id": "d", "text": "Voy casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_su", "target": "su casa", "native": "a casa deles",
                    "npc_reaction": "Su casa. Bien usado — lo que es de ellos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Sofía — ¿y tú? ¿Cuándo viste al forastero por primera vez?",
                    "translation": "Sofía — e você? Quando viu o forasteiro pela primeira vez?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Yo lo vi en el cuarto de Don Miguel — la noche del fuego.",
                    "translation": "Eu vi ele no quarto de Don Miguel — a noite do fogo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Sofía disse 'lo vi'. Pra você confirmar pra María que ouviu o que Sofía falou (ouviu já):",
                    "options": [
                        {"id": "a", "text": "Sí, la oí decir eso"},
                        {"id": "b", "text": "Sí, la oigo"},
                        {"id": "c", "text": "Voy a oír"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oí. Bien usado — ya pasó.",
                },
                {
                    "kind": "narrative",
                    "text": "María olha pra Sofía mais um segundo. Anota mentalmente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Forastero — ¿qué sentiste cuando salió el fuego de tus manos?",
                    "translation": "Forasteiro — o que você sentiu quando o fogo saiu das suas mãos?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você sentiu medo. Pra contar (já aconteceu — TENER no passado é 'tuve'):",
                    "options": [
                        {"id": "a", "text": "Tuve miedo"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Voy a tener miedo"},
                        {"id": "d", "text": "Soy miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_tuve", "target": "tuve miedo", "native": "tive medo",
                    "npc_reaction": "Tuve. Como 'tengo' pero ya pasado. Igual que 'vi' del verbo ver.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Y ahora cuéntame de la cena en casa de Doña Lucía. ¿Te gustó?",
                    "translation": "E agora me conta do jantar na casa de Doña Lucía. Você gostou?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você gostou — comida boa, gente acolhedora. Resposta com 'me gusta':",
                    "options": [
                        {"id": "a", "text": "Sí, me gusta su casa"},
                        {"id": "b", "text": "Sí, me gustan su casa"},
                        {"id": "c", "text": "Sí, voy a gustar"},
                        {"id": "d", "text": "Sí, soy casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Una casa — singular — 'me gusta'. Su madre fue muy amable contigo, ¿no?",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # María continua perguntando. As perguntas começam mais inocentes mas
    # gradualmente focam em detalhes que ela "não deveria saber". Foco em
    # REVISÃO PESADA. Sofía começa a perceber, Miguel também.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "María serviu mais vinho. As perguntas continuam — mas o "
                    "tom mudou um pouco. Ela quer detalhes específicos. Sofía "
                    "começou a responder com mais cuidado. Miguel observa.\n\n"
                    "Você não sabe ainda como reagir."
                ),
                "now": "María faz perguntas precisas. Cada resposta tua precisa ser cuidadosa.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Cuéntame de Eduardo. ¿Por qué pidió que lo lleváramos conmigo cuando vaya a testificar?",
                    "translation": "Me conta sobre Eduardo. Por que ele pediu que a gente levasse ele junto comigo quando ele for testemunhar?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "A pergunta é específica. Eduardo pediu pra ver María — "
                        "mas só Don Miguel e você estavam lá. Como María sabe "
                        "do detalhe específico?"
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você responde simples — sem entregar muito. Pra contar que ele PEDIU isso (ele, já passou):",
                    "options": [
                        {"id": "a", "text": "Pidió ver tu espalda"},
                        {"id": "b", "text": "Pide ver tu espalda"},
                        {"id": "c", "text": "Voy a pedir"},
                        {"id": "d", "text": "Soy espalda"},
                    ],
                    "correct": "a",
                    "word_id": "es_pidio", "target": "pidió", "native": "pediu",
                    "npc_reaction": "Pidió. Mmm. Curioso. ¿Te dijo por qué?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Eduardo não te disse por quê — só que precisava. Negação simples no passado:",
                    "options": [
                        {"id": "a", "text": "No, no me dijo por qué"},
                        {"id": "b", "text": "Sí, me dije"},
                        {"id": "c", "text": "Voy a decir"},
                        {"id": "d", "text": "Soy decir"},
                    ],
                    "correct": "a",
                    "word_id": "es_dijo", "target": "dijo", "native": "ele disse",
                    "npc_reaction": "Bueno. Veré qué quiere cuando llegue el momento.",
                },
                {
                    "kind": "narrative",
                    "text": "Sofía mexe o dedo na borda do copo. Não está bebendo. Olha pra María com uma expressão neutra que custa muito manter.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Y Doña Lucía. ¿Te trató bien anoche?",
                    "translation": "E Doña Lucía. Te tratou bem ontem à noite?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Sim, Lucía tratou bem. Pra responder simples sobre o passado:",
                    "options": [
                        {"id": "a", "text": "Sí, me trató muy bien"},
                        {"id": "b", "text": "Sí, me trata muy bien"},
                        {"id": "c", "text": "Voy a tratarme"},
                        {"id": "d", "text": "Soy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_trato", "target": "trató", "native": "tratou",
                    "npc_reaction": "Bueno. Lucía es de las antiguas. Y siempre supo distinguir a quien recibe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Y habló mucho de mí?",
                    "translation": "E falou muito de mim?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Silêncio breve. Miguel olha pra você. Sofía olha pra você. "
                        "Você é quem mais ouviu o sussurro de Lucía através da parede."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você responde simples — sem entregar nada. Pra dizer que ELA falou pouco (já passou):",
                    "options": [
                        {"id": "a", "text": "No, no habló mucho"},
                        {"id": "b", "text": "Sí, habló todo"},
                        {"id": "c", "text": "Voy a hablar"},
                        {"id": "d", "text": "Soy habló"},
                    ],
                    "correct": "a",
                    "word_id": "es_hablo", "target": "habló", "native": "ela falou",
                    "npc_reaction": "Mmm. Bueno saberlo. Lucía es discreta — siempre lo fue.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "'Siempre lo fue.' — María falou disso como quem conhece "
                        "Lucía há muito tempo. Mas ela disse que chegou ao pueblo "
                        "faz dois meses."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Sofía — y tu abuela. La que hablaba de las palabras 'que despiertan'. ¿Cuándo murió?",
                    "translation": "Sofía — e tua avó. A que falava das palavras 'que despertam'. Quando ela morreu?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Hace siete años. Yo tenía once.",
                    "translation": "Faz sete anos. Eu tinha onze.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Sofía disse 'yo tenía once'. Aqui ela tá falando da idade DELA no passado. Pra confirmar pra ela que você entendeu — quantos anos VOCÊ tem AGORA:",
                    "options": [
                        {"id": "a", "text": "Yo tengo veinte ahora"},
                        {"id": "b", "text": "Yo soy veinte"},
                        {"id": "c", "text": "Voy veinte"},
                        {"id": "d", "text": "Tenía veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo", "native": "tenho",
                    "npc_reaction": "Tengo — ahora. Tenía — antes. Las dos formas son útiles.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Miguel — tu madre tiene buena cocina. ¿Te enseñó ella?",
                    "translation": "Miguel — tua mãe tem cozinha boa. Foi ela que te ensinou?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel responde — sim, foi ela. Pra dizer que ela LHE ENSINOU (passado, ela):",
                    "options": [
                        {"id": "a", "text": "Sí, ella me enseñó"},
                        {"id": "b", "text": "Sí, ella me enseña"},
                        {"id": "c", "text": "Sí, va a enseñarme"},
                        {"id": "d", "text": "Sí, soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_enseno", "target": "enseñó", "native": "ensinou",
                    "npc_reaction": "Eso. Las cosas que aprendí de niño — el guiso, el saludo, cómo callar cuando es necesario.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel disse 'cómo callar cuando es necesario' olhando direto pra María. Foi o mais perto que ele chegou de uma acusação.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Sofía saiu pegar água. María se vira pro forastero. Apresentação suave
    # de el/la/los/las — usando frases concretas. SEM nomear "artigo".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["María"],
                "story": (
                    "Sofía levantou pra pegar água. Miguel saiu pro pátio. "
                    "Sobrou você e María na mesa.\n\n"
                    "'Espera. Antes de que terminen la noche — quiero "
                    "enseñarte algo que tu cabeza ya usa sin saber.'"
                ),
                "now": "María mostra como el/la trabalham. Você já usava.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Dijiste 'el pan' y 'la lámpara' desde el primer día. ¿Sabes por qué uno es 'el' y el otro es 'la'?",
                    "translation": "Você disse 'el pan' e 'la lámpara' desde o primeiro dia. Sabe por que um é 'el' e o outro é 'la'?",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "El (de hombre) · La (de mujer)",
                    "meaning": "Palavrinhas que vão na frente da coisa.",
                    "note": "cada palabra del español es 'de hombre' o 'de mujer'. No hay neutro.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Lo más útil: si la palabra termina en '-o', casi siempre es de hombre. Si termina en '-a', casi siempre de mujer.",
                    "translation": "O mais útil: se a palavra termina em '-o', quase sempre é de homem. Se termina em '-a', quase sempre de mulher.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "EL ",        "isKey": True},
                        {"text": "campesin",   "isKey": False},
                        {"text": "O",          "isKey": True},
                        {"text": " · ",        "isKey": False},
                        {"text": "LA ",        "isKey": True},
                        {"text": "lámpar",     "isKey": False},
                        {"text": "A",          "isKey": True},
                    ],
                    "example": "El campesino tiene una casa. La lámpara da luz. El forastero come pan. La fiebre subió ayer.",
                    "translation": "O camponês tem uma casa. A lamparina dá luz. O forasteiro come pão. A febre subiu ontem.",
                    "note": "termina en -o → 'el' (de hombre) · termina en -a → 'la' (de mujer). Hay excepciones pero pocas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "'Cocina' termina em '-a'. A palavrinha certa pra ir na frente:",
                    "options": [
                        {"id": "a", "text": "la cocina"},
                        {"id": "b", "text": "el cocina"},
                        {"id": "c", "text": "los cocina"},
                        {"id": "d", "text": "las cocina"},
                    ],
                    "correct": "a",
                    "word_id": "es_la", "target": "la", "native": "a (de mulher)",
                    "npc_reaction": "La cocina. De mujer. Igual que la mesa, la silla, la noche.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "'Mercado' termina em '-o'. A palavrinha:",
                    "options": [
                        {"id": "a", "text": "el mercado"},
                        {"id": "b", "text": "la mercado"},
                        {"id": "c", "text": "los mercado"},
                        {"id": "d", "text": "las mercado"},
                    ],
                    "correct": "a",
                    "word_id": "es_el", "target": "el", "native": "o (de homem)",
                    "npc_reaction": "El mercado. De hombre. Igual que el pueblo, el río, el campesino.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Y cuando hay muchos — 'el' se hace 'los', 'la' se hace 'las'. Y la cosa también suma una '-s'.",
                    "translation": "E quando tem muitos — 'el' vira 'los', 'la' vira 'las'. E a coisa também ganha um '-s'.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "el pan → ",   "isKey": False},
                        {"text": "los panes",   "isKey": True},
                        {"text": " · ",         "isKey": False},
                        {"text": "la naranja → ", "isKey": False},
                        {"text": "las naranjas", "isKey": True},
                    ],
                    "example": "Los panes están calientes. Las naranjas son dulces.",
                    "translation": "Os pães estão quentes. As laranjas são doces.",
                    "note": "el → los · la → las — y siempre suma '-s' o '-es' a la palabra.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você vai falar de duas ou mais laranjas (de mulher, muitas):",
                    "options": [
                        {"id": "a", "text": "las naranjas"},
                        {"id": "b", "text": "los naranjas"},
                        {"id": "c", "text": "la naranjas"},
                        {"id": "d", "text": "el naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_las", "target": "las", "native": "as (muitas, mulher)",
                    "npc_reaction": "Las naranjas. De mujer, muchas.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Sofía volta. Miguel volta. Os 4 na mesa. María faz a pergunta final
    # — uma pergunta que mostra que ela sabe coisas que ninguém contou.
    # Foco em revisão + tensão dramática.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "Sofía voltou com mais uma jarra. Miguel voltou do pátio. "
                    "María acendeu uma nova vela. Sobrou pão na mesa, ninguém "
                    "com fome.\n\n"
                    "'Una última cosa antes de que se vayan. Después se duermen.'"
                ),
                "now": "Última pergunta de María. A resposta vai mudar tudo.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Quiero saber una cosa — solamente. ¿Pueden contestarme con honestidad?",
                    "translation": "Quero saber uma coisa — só. Vocês podem me responder com honestidade?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Depende de qué sea.",
                    "translation": "Depende do que for.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "María sorri pequeno. Sem rancor. Sem deboche. Como quem aceita a defesa de Sofía.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Es razonable. Forastero — la palabra que dijiste esa noche. Fuego. ¿La sentiste subir desde dónde?",
                    "translation": "É razoável. Forasteiro — a palavra que você disse aquela noite. Fogo. Você sentiu subir de onde?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você gela. Você sentiu — sim. Mas você NUNCA falou em "
                        "voz alta de onde sentiu. Nem pra Sofía, nem pra Miguel, "
                        "nem pra Don Miguel. NEM PRA MARÍA.\n\n"
                        "Ela está perguntando uma informação que ela não devia ter.\n\n"
                        "Você olha pra Sofía. Sofía olha pra você. Miguel olha "
                        "pros dois. Ninguém respira."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você precisa responder algo — sem entregar tudo. Resposta segura — você não lembra dos detalhes:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo bien"},
                        {"id": "b", "text": "Sí, me acuerdo de todo"},
                        {"id": "c", "text": "Voy a contarte"},
                        {"id": "d", "text": "Soy fuego"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                    "npc_reaction": "Está bien, hijo. Yo entiendo. Es difícil acordarse de algo que la cabeza no quiere recordar.",
                },
                {
                    "kind": "narrative",
                    "text": "María aceitou a resposta. Não insistiu. Mas Sofía agora SABE — e Miguel também — que María sabe coisas que ninguém contou pra ela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "María — ¿cómo sabes que sintió que subió? El forastero nunca dijo esa palabra a nadie.",
                    "translation": "María — como você sabe que ele sentiu subir? O forasteiro nunca disse essa palavra pra ninguém.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Pausa longa. María não responde rápido. Quando responde, é com calma de quem já tinha preparado a resposta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Mi abuela también tenía un don. Cuando alguien le tocaba, ella sabía algunas cosas — sin que se las dijeran. Yo no lo tengo igual de fuerte. Pero algo me llega.",
                    "translation": "Minha avó também tinha um dom. Quando alguém a tocava, ela sabia algumas coisas — sem que falassem. Eu não tenho igual de forte. Mas algo me chega.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María disse 'mi abuela tenía un don'. 'Tenía' significa:",
                    "options": [
                        {"id": "a", "text": "Ela tinha (antes, sempre)"},
                        {"id": "b", "text": "Ela tem (agora)"},
                        {"id": "c", "text": "Vai ter"},
                        {"id": "d", "text": "Ela é"},
                    ],
                    "correct": "a",
                    "word_id": "es_tenia", "target": "tenía", "native": "tinha",
                    "npc_reaction": "Tenía. Como 'tengo' pero ya pasado. Y duró años — no fue solo un momento.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "A explicação serve. Os três jovens aceitam — porque o "
                        "que mais podem fazer? Acusar? Sair? Sofía olha pra "
                        "Miguel. Miguel acena de leve.\n\n"
                        "Mas vocês três sabem que isso não terminou."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Bueno. Es tarde. Mañana al ayuntamiento — temprano. Vayan a descansar.",
                    "translation": "Bom. Já é tarde. Amanhã no ayuntamiento — cedo. Vão descansar.",
                    "pace": "slow",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Saindo da casa de hóspedes. Os 3 jovens caminhando juntos pra casa de
    # Don Miguel — silêncio carregado. Sofía sussurra, Miguel sussurra.
    # Decisão: vão fingir que não notaram. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Sofía", "Miguel"],
                "story": (
                    "Vocês três saíram. María ficou na porta acenando — "
                    "amistosa como sempre. Calorosa. Vocês acenaram de volta. "
                    "Caminharam até o cruzamento sem dizer nada.\n\n"
                    "Quando a casa dela já estava longe — Sofía parou e olhou "
                    "pra Miguel."
                ),
                "now": "Decisão difícil. O que fazer com o que vocês descobriram?",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌃 Rua escura · Os três parados no cruzamento · Don Miguel à frente",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Miguel — ella sabe cosas que nunca le contamos.",
                    "translation": "Miguel — ela sabe coisas que a gente nunca contou pra ela.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Mi madre dijo lo mismo anoche. Que la conocía de algún sitio.",
                    "translation": "Minha mãe disse o mesmo ontem à noite. Que conhecia ela de algum lugar.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta direto se você ouviu o sussurro da Lucía. Confirmando que ouviu:",
                    "options": [
                        {"id": "a", "text": "Sí, oí lo que dijo"},
                        {"id": "b", "text": "Sí, oigo"},
                        {"id": "c", "text": "Voy a oír"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oíste. Bueno. Entonces los tres sabemos lo mismo.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "¿Y qué hacemos? ¿Decírselo a Don Miguel? ¿A Carmen?",
                    "translation": "E o que a gente faz? Falar pro Don Miguel? Pra Carmen?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "No. Todavía no. Si ella se entera que sospechamos — no sé qué hace. Mejor que crea que dormimos como tontos.",
                    "translation": "Não. Ainda não. Se ela descobrir que a gente desconfia — não sei o que ela faz. Melhor que ela acredite que dormimos como tolos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía propõe fingir normalidade. Pra concordar — 'não vamos contar nada':",
                    "options": [
                        {"id": "a", "text": "No le decimos nada"},
                        {"id": "b", "text": "Sí le decimos"},
                        {"id": "c", "text": "Voy a decirle"},
                        {"id": "d", "text": "Soy decir"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "não",
                    "npc_reaction": "No. Eso. Mañana normal — sin caras raras.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Vamos a observar. Eso es lo que vamos a hacer.",
                    "translation": "Vamos observar. Isso é o que vamos fazer.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel propõe um plano de observação. Pra você concordar — 'os três vamos':",
                    "options": [
                        {"id": "a", "text": "Vamos a observar los tres"},
                        {"id": "b", "text": "Voy a observar"},
                        {"id": "c", "text": "Va a observar"},
                        {"id": "d", "text": "Soy observar"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos a", "native": "vamos",
                    "npc_reaction": "Vamos a observar. Los tres juntos. No la perdemos de vista.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês três se olharam — no escuro da rua, sem mais "
                        "palavras. Selaram o acordo com silêncio."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Forastero — ¿estás bien con todo esto? Es mucho.",
                    "translation": "Forasteiro — você tá bem com tudo isso? É muita coisa.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Honestidade dupla — bem mas com sensação:",
                    "options": [
                        {"id": "a", "text": "Estoy bien, pero tengo miedo"},
                        {"id": "b", "text": "Soy bien, soy miedo"},
                        {"id": "c", "text": "Voy bien y voy miedo"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Las dos cosas a la vez — bien y con miedo. Eso es ser humano y honesto.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F15 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🏡 Voltando pra casa de Don Miguel · Noite alta · Silêncio na rua",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês três caminharam pelo resto do caminho sem dizer "
                        "mais nada. María ficou na sua cabeça — a calma dela "
                        "agora soava diferente.\n\n"
                        "Você foi pra cama. Não dormiu logo. A pergunta de María "
                        "girava — 'la sentiste subir desde dónde?'\n\n"
                        "Você lembrou agora. Do peito. Subiu do peito antes de "
                        "sair pelas mãos.\n\n"
                        "E você nunca tinha contado isso pra ninguém."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
