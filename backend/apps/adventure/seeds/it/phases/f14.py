"""
Seed das 6 seções da Fase 14 Italiano A1 — "La cena de Lucia".

⚠️ MILESTONE OBRIGATÓRIO (canônico — story.md):
    F14 = 3ª fase de revisão. A Marta-equivalente (Lucia) está no
    cenário, observando. Precisa que o protagonista fique e fique
    mais forte para o ritual.

Lucia convida todos pra jantar na casa de hóspedes. Pede que cada
um conte o que viveu. Ela escuta. Anota mentalmente. Calibra.

No fim, Lucia faz uma pergunta que mostra que ela sabe coisas que
ninguém contou pra ela. O jogador pega a pista, os personagens
ainda não.

ABORDAGEM PEDAGÓGICA:
    Esta é fase de REVISÃO. Apresenta apenas 1 novidade: come
    el/la/los/las trabalha (palavrinhas que vão na fronte).
    Explicado simples come "para palavras de homem (el/los) ou
    de mulher (la/las)". Sem nomear "artigo definido".

Vocab novo (minimale): foco em revisão.
Apresentação adicional: el/la/los/las (já usados sem saber desde F1)

Revisão F1-F13 dominante (~75% dos exercícios):
  · vi/hablé/oí (F12) — relato
  · mi/tu/su (F13) — pertencimento
  · vado a / andiamo a (F11) — futuro próximo
  · sono/sto/ho (F8)
  · mi chiamo / ho X años / grazie
  · mi piace / no mi piace (F9)

NPC principais: Lucia (observadora central) · os 4
Arco emocional: revisão coletiva → leveza engannia → momento gélido no fim
Transição: F15 abre na manhã seguinte, todos calados.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Os 4 chegando à casa de hóspedes de Lucia. Convite formale pra jantar.
    # Apresentação suave de el/la/los/las nas próprias frases dos NPCs.
    # 1 exercício novo + 3 revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🕯️ Casa de hóspedes de Lucia · Noite · Mesa posta\n\n"
                        "Lucia preparou tudo desde a manhã. Vela no centro da "
                        "mesa, pão fresco que ela mesma assou, guisado fumegante, "
                        "uma jarra de vinho leve. Quatro pratos. Um lugar pra "
                        "Antonio il Contadino também — caso quisesse vir."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "Os 4 entram. Antonio il Contadino não veio. Sobrou vocês quatro com Lucia.",
                },
                {
                    "kind": "npc",
                    "npc": "Lucia",
                    "line": "Benevieniidos. Siéntense — todos. Esta notte quiero oír.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Chiara olha pra você por um segundo. Nico já se "
                        "lembrava do sussurro da mãe. Você sabe que ele sabe — "
                        "e ele sabe que você sabe."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Lucia",
                    "line": "Andiamo a comer primero. Después — cuéntenme. Cada uno. Lo que vivieron estos diez días.",
                    "pace": "slow",
                },
                {
                    "kind": "scene",
                    "text": "?? Sopa servida · Vinho leve · Cada um pega o próprio pão",
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
                    "npc": "Lucia",
                    "question": "Lucia serve o caldo: 'Esta es ___ sopa de mi nonna.' Você já reparou — prima de 'sopa' sempre vem 'la' (sopa é palavra de mulher):",
                    "options": [
                        {"id": "a", "text": "la"},
                        {"id": "b", "text": "el"},
                        {"id": "c", "text": "los"},
                        {"id": "d", "text": "las"},
                    ],
                    "correct": "a",
                    "word_id": "it_la", "target": "la", "native": "a (pra mulher)",
                    "npc_reaction": "La sopa. Igual que la cocina, la mesa, la notte — todas palavras de mujer.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pede pão. 'Pásame ___ pane, por favor.' Pane é palavra de homem (você já tinha usado 'el pane' várias vezes):",
                    "options": [
                        {"id": "a", "text": "el"},
                        {"id": "b", "text": "la"},
                        {"id": "c", "text": "los"},
                        {"id": "d", "text": "las"},
                    ],
                    "correct": "a",
                    "word_id": "it_el", "target": "el", "native": "o (pra homem)",
                    "npc_reaction": "El pane. Como el campesenzao, el río, el borgo — todas de hombre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico olha pra Lucia: 'Estos guisos están bene hechos.' Pra dizer 'os guisos' (palavra de homem, muitos):",
                    "options": [
                        {"id": "a", "text": "los"},
                        {"id": "b", "text": "las"},
                        {"id": "c", "text": "el"},
                        {"id": "d", "text": "la"},
                    ],
                    "correct": "a",
                    "word_id": "it_los", "target": "los", "native": "os (muitos, homem)",
                    "npc_reaction": "Los guisos. 'El' se hace 'los' cuando hay muchos. Igual que 'la' se hace 'las'.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Lucia pergunta sobre os primeiros dias. Mistura de
    # F1-F13 — pretérito recém aprendido (F12), possessivos (F13), futuro
    # próximo (F11), saudações, identidade.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Lucia"],
                "story": (
                    "Vocês comeram. Pão sumiu rápido. Vinho leve, não enche a "
                    "cabeça piu relaxa. Lucia sentou — não comeu muito. Esmau.\n\n"
                    "'Bene. Empezamos. Forestiero — empieza tu. Cuéntame del "
                    "primer día. Desde que pisaste el borgo.'"
                ),
                "now": "Lucia quer cada detalhe. Você relata. Cada pergunta é revisão.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Primero — ¿quién te encontró primero?¿Quién te habló primero?",
                    "translation": "Primeiro — quem te encontrou primeiro?Quem falou con te primeiro?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Giulia foi a primeira voz que você ouviu. Pra contar que ELA falou primeiro:",
                    "options": [
                        {"id": "a", "text": "Giulia habló con me primero"},
                        {"id": "b", "text": "Giulia habla con me primero"},
                        {"id": "c", "text": "Giulia va a hablar"},
                        {"id": "d", "text": "Giulia sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_hablo", "target": "habló", "native": "ela falou",
                    "npc_reaction": "Habló — ella, ya pasó. Giulia siempre encuentra a los forestieros.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Y la palabra primera que aprendiste?¿Recuerdas cuál fue?",
                    "translation": "E a primeira palavra que você aprendeu?Lembra qual foi?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Pane. Foi a primeira palavra que Giulia repetiu com você. Pra contar que VOCÊ aprendeu:",
                    "options": [
                        {"id": "a", "text": "Aprendí 'pane'"},
                        {"id": "b", "text": "Aprendo 'pane'"},
                        {"id": "c", "text": "Vado a aprender 'pane'"},
                        {"id": "d", "text": "Sono 'pane'"},
                    ],
                    "correct": "a",
                    "word_id": "it_aprendi", "target": "aprendí", "native": "aprendi",
                    "npc_reaction": "Pane. Suficiente para el primer día. La palabra que abrió todas las demás.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Y la familia de Nico?¿Cómo te trataron anotte?",
                    "translation": "E a família de Nico?Como te trataram ontem à noite?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Bem. Pra falar de coisas DELES (família de Nico, terceira pessoa):",
                    "options": [
                        {"id": "a", "text": "Su casa es cálida"},
                        {"id": "b", "text": "Mi casa es cálida"},
                        {"id": "c", "text": "Tu casa es cálida"},
                        {"id": "d", "text": "Vado casa"},
                    ],
                    "correct": "a",
                    "word_id": "it_su", "target": "su casa", "native": "a casa deles",
                    "npc_reaction": "Su casa. Bene usado — lo que es de ellos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Chiara — ¿y tu?¿Cuándo viste al forestiero por primera vez?",
                    "translation": "Chiara — e você?Quando viu o forasteiro pela primeira vez?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Yo lo vi en el cuarto de Antonio il Contadino — la notte del fuoco.",
                    "translation": "Eu vi ele no quarto de Antonio il Contadino — a noite do fogo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Chiara disse 'lo vi'. Pra você confirmar pra Lucia que ouviu o que Chiara falou (ouviu já):",
                    "options": [
                        {"id": "a", "text": "Sí, la oí decir questo"},
                        {"id": "b", "text": "Sí, la oigo"},
                        {"id": "c", "text": "Vado a oír"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oí. Bene usado — ya pasó.",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia olha pra Chiara mais um segundo. Anota mentalmente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Forestiero — ¿qué sentiste cuando saleió el fuoco de tus manni?",
                    "translation": "Forasteiro — o que você sentiu quando o fogo saiu das suas mãos?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você sentiu medo. Pra contar (já aconteceu — TENER no passado é 'tuve'):",
                    "options": [
                        {"id": "a", "text": "Tuve paura"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Vado a tener paura"},
                        {"id": "d", "text": "Sono paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_tuve", "target": "tuve paura", "native": "tive medo",
                    "npc_reaction": "Tuve. Como 'ho' ma ya pasado. Igual que 'vi' del verbo ver.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Y adesso cuéntame de la cena en casa de Doña Lucía. ¿Te gustó?",
                    "translation": "E agora me conta do jantar na casa de Doña Lucía. Você gostou?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você gostou — cibo boa, gente acolhedora. Resposta com 'mi piace':",
                    "options": [
                        {"id": "a", "text": "Sí, mi piace su casa"},
                        {"id": "b", "text": "Sí, mi piacen su casa"},
                        {"id": "c", "text": "Sí, vado a gustar"},
                        {"id": "d", "text": "Sí, sono casa"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto",
                    "npc_reaction": "Una casa — senzagular — 'mi piace'. Su madre fue muy amable con te, ¿no?",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Lucia continua perguntando. As perguntas começam mais inocentes piu
    # gradualmente focam em detalhes que ela "não deveria saber". Foco em
    # REVISÃO PESADA. Chiara começa a perceber, Nico também.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Lucia serviu mais vinho. As perguntas continuam — piu o "
                    "tom mudou um pouco. Ela quer detalhes específicos. Chiara "
                    "começou a responder com mais cuidado. Nico observa.\n\n"
                    "Você não sabe ainda come reagir."
                ),
                "now": "Lucia faz perguntas precisas. Cada resposta tua precisa ser cuidadosa.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Cuéntame de Pietro. ¿Por qué pidió que lo lleváramos con me cuando vaya a testificar?",
                    "translation": "Me conta sobre Pietro. Por que ele pediu que a gente levasse ele junto comigo quando ele for testemunhar?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "A pergunta é específica. Pietro pediu pra ver Lucia — "
                        "piu só Antonio il Contadino e você estavam lá. Como Lucia sabe "
                        "do detalhe específico?"
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você responde simples — sem entregar muito. Pra contar que ele PEDIU isso (ele, já passou):",
                    "options": [
                        {"id": "a", "text": "Pidió ver tu espalda"},
                        {"id": "b", "text": "Pide ver tu espalda"},
                        {"id": "c", "text": "Vado a pedir"},
                        {"id": "d", "text": "Sono espalda"},
                    ],
                    "correct": "a",
                    "word_id": "it_pidio", "target": "pidió", "native": "pediu",
                    "npc_reaction": "Pidió. Mmm. Curioso. ¿Te ha detto por qué?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Pietro não te disse por quê — só que precisava. Negação simples no passado:",
                    "options": [
                        {"id": "a", "text": "No, no me ha detto por qué"},
                        {"id": "b", "text": "Sí, me dije"},
                        {"id": "c", "text": "Vado a decir"},
                        {"id": "d", "text": "Sono decir"},
                    ],
                    "correct": "a",
                    "word_id": "it_ha detto", "target": "ha detto", "native": "ele disse",
                    "npc_reaction": "Bene. Veré qué quiere cuando arrivi el momento.",
                },
                {
                    "kind": "narrative",
                    "text": "Chiara mexe o dedo na borda do copo. Não está bebendo. Olha pra Lucia com uma expressão neutra que custa muito manter.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Y Doña Lucía. ¿Te trató bene anotte?",
                    "translation": "E Doña Lucía. Te tratou bem ontem à noite?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Sim, Lucía tratou bem. Pra responder simples sobre o passado:",
                    "options": [
                        {"id": "a", "text": "Sí, me trató muy bene"},
                        {"id": "b", "text": "Sí, me trata muy bene"},
                        {"id": "c", "text": "Vado a tratarme"},
                        {"id": "d", "text": "Sono bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_trato", "target": "trató", "native": "tratou",
                    "npc_reaction": "Bene. Lucía es de las antiguas. Y siempre supo distinguir a chi recibe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Y habló mucho de mí?",
                    "translation": "E falou muito de mim?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Silêncio breve. Nico olha pra você. Chiara olha pra você. "
                        "Você é quem mais ouviu o sussurro de Lucía através da parede."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você responde simples — sem entregar nada. Pra dizer que ELA falou pouco (já passou):",
                    "options": [
                        {"id": "a", "text": "No, no habló mucho"},
                        {"id": "b", "text": "Sí, habló todo"},
                        {"id": "c", "text": "Vado a hablar"},
                        {"id": "d", "text": "Sono habló"},
                    ],
                    "correct": "a",
                    "word_id": "it_hablo", "target": "habló", "native": "ela falou",
                    "npc_reaction": "Mmm. Bene saberlo. Lucía es discreta — siempre lo fue.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "'Siempre lo fue.' — Lucia falou disso come quem conhece "
                        "Lucía há muito tempo. Mas ela disse que chegou ao borgo "
                        "faz dois meses."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Chiara — y tu nonna. La que parlava de las parole 'que despiertan'. ¿Cuándo murió?",
                    "translation": "Chiara — e tua avó. A que falava das palavras 'que despertam'. Quando ela morreu?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Hace siete años. Yo tenía once.",
                    "translation": "Faz sete anni. Eu tinha onze.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Chiara disse 'yo tenía once'. Aqui ela tá falando da idade DELA no passado. Pra confirmar pra ela que você entendeu — quantos anni VOCÊ tem AGORA:",
                    "options": [
                        {"id": "a", "text": "Yo ho veinte adesso"},
                        {"id": "b", "text": "Io sono veinte"},
                        {"id": "c", "text": "Vado veinte"},
                        {"id": "d", "text": "Tenía veinte"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho", "native": "tenho",
                    "npc_reaction": "Ho — adesso. Tenía — prima. Las dos forpiu son útiles.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Nico — tu madre ha buena cocina. ¿Te enseñó ella?",
                    "translation": "Nico — tua mãe tem cozinha boa. Foi ela que te ensenzaou?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico responde — sim, foi ela. Pra dizer que ela LHE ENSINOU (passado, ela):",
                    "options": [
                        {"id": "a", "text": "Sí, ella me enseñó"},
                        {"id": "b", "text": "Sí, ella me enseña"},
                        {"id": "c", "text": "Sí, va a enseñarme"},
                        {"id": "d", "text": "Sí, sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_enseno", "target": "enseñó", "native": "ensenzaou",
                    "npc_reaction": "Esatto. Las cose que aprendí de niño — el guiso, el saleudo, cómo callar cuando es necesario.",
                },
                {
                    "kind": "narrative",
                    "text": "Nico disse 'cómo callar cuando es necesario' olhando direto pra Lucia. Foi o mais perto que ele chegou de uma acusação.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Chiara saiu pegar água. Lucia se vira pro forestiero. Apresentação suave
    # de el/la/los/las — usando frases concretas. SEM nomear "artigo".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Lucia"],
                "story": (
                    "Chiara levantou pra pegar água. Nico saiu pro pátio. "
                    "Sobrou você e Lucia na mesa.\n\n"
                    "'Espera. Prima de que terminen la notte — quiero "
                    "enseñarte algo que tu testa ya usa senza saber.'"
                ),
                "now": "Lucia mostra come el/la trabalham. Você já usava.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Dijiste 'el pane' y 'la lampada' desde el primer día. ¿Sabes por qué uno es 'el' y el otro es 'la'?",
                    "translation": "Você disse 'el pane' e 'la lampada' desde o primeiro dia. Sabe por que um é 'el' e o outro é 'la'?",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "El (de hombre) · La (de mujer)",
                    "meaning": "Palavrinhas que vão na fronte da coisa.",
                    "note": "cada palabra del español es 'de hombre' o 'de mujer'. No hay neutro.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Lo más útil: si la palabra termina en '-o', casi siempre es de hombre. Si termina en '-a', casi siempre de mujer.",
                    "translation": "O mais útil: se a palavra termina em '-o', quase sempre é de homem. Se termina em '-a', quase sempre de mulher.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "EL ",        "isKey": True},
                        {"text": "campesenza",   "isKey": False},
                        {"text": "O",          "isKey": True},
                        {"text": " · ",        "isKey": False},
                        {"text": "LA ",        "isKey": True},
                        {"text": "lámpar",     "isKey": False},
                        {"text": "A",          "isKey": True},
                    ],
                    "example": "El campesenzao ha una casa. La lampada da luce. El forestiero come pane. La febbre subió ayer.",
                    "translation": "O camponês tem uma casa. A lamparina dá luce. O forasteiro come pão. A febre subiu ontem.",
                    "note": "termina en -o → 'el' (de hombre) · termina en -a → 'la' (de mujer). Hay excepciones ma pocas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "'Cocina' termina em '-a'. A palavrinha certa pra ir na fronte:",
                    "options": [
                        {"id": "a", "text": "la cocina"},
                        {"id": "b", "text": "el cocina"},
                        {"id": "c", "text": "los cocina"},
                        {"id": "d", "text": "las cocina"},
                    ],
                    "correct": "a",
                    "word_id": "it_la", "target": "la", "native": "a (de mulher)",
                    "npc_reaction": "La cocina. De mujer. Igual que la mesa, la silla, la notte.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "'Mercato' termina em '-o'. A palavrinha:",
                    "options": [
                        {"id": "a", "text": "el mercato"},
                        {"id": "b", "text": "la mercato"},
                        {"id": "c", "text": "los mercato"},
                        {"id": "d", "text": "las mercato"},
                    ],
                    "correct": "a",
                    "word_id": "it_el", "target": "el", "native": "o (de homem)",
                    "npc_reaction": "El mercato. De hombre. Igual que el borgo, el río, el campesenzao.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Y cuando hay muchos — 'el' se hace 'los', 'la' se hace 'las'. Y la cosa también suma una '-s'.",
                    "translation": "E quando tem muitos — 'el' vira 'los', 'la' vira 'las'. E a coisa também ganha um '-s'.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "el pane → ",   "isKey": False},
                        {"text": "los panees",   "isKey": True},
                        {"text": " · ",         "isKey": False},
                        {"text": "la arancia → ", "isKey": False},
                        {"text": "las arance", "isKey": True},
                    ],
                    "example": "Los panees están caldas. Las arance son dulces.",
                    "translation": "Os pães estão quentes. As laranjas são doces.",
                    "note": "el → los · la → las — y siempre suma '-s' o '-es' a la palabra.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você vai falar de duas ou mais laranjas (de mulher, muitas):",
                    "options": [
                        {"id": "a", "text": "las arance"},
                        {"id": "b", "text": "los arance"},
                        {"id": "c", "text": "la arance"},
                        {"id": "d", "text": "el arance"},
                    ],
                    "correct": "a",
                    "word_id": "it_las", "target": "las", "native": "as (muitas, mulher)",
                    "npc_reaction": "Las arance. De mujer, muchas.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Chiara volta. Nico volta. Os 4 na mesa. Lucia faz a pergunta final
    # — uma pergunta que mostra que ela sabe coisas que ninguém contou.
    # Foco em revisão + tensão dramática.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Chiara voltou com mais uma jarra. Nico voltou do pátio. "
                    "Lucia acendeu uma nova vela. Sobrou pão na mesa, ninguém "
                    "com fome.\n\n"
                    "'Una última cosa prima de que se vayan. Después se duermen.'"
                ),
                "now": "Última pergunta de Lucia. A resposta vai mudar tudo.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Quiero saber una cosa — solamente. ¿Pueden contestarme con honestidad?",
                    "translation": "Quero saber uma coisa — só. Vocês podem me responder com honestidade?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Depende de qué sea.",
                    "translation": "Depende do que for.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia sorri pequeno. Sem rancor. Sem deboche. Como quem aceita a defesa de Chiara.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Es razonable. Forestiero — la palabra que hai detto esa notte. Fuoco. ¿La sentiste subir desde dónde?",
                    "translation": "É razoável. Forasteiro — a palavra que você disse aquela noite. Fogo. Você sentiu subir de onde?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Você gela. Você sentiu — sim. Mas você NUNCA falou em "
                        "voz alta de onde sentiu. Nem pra Chiara, nem pra Nico, "
                        "nem pra Antonio il Contadino. NEM PRA MARÍA.\n\n"
                        "Ela está perguntando uma informação que ela não devia ter.\n\n"
                        "Você olha pra Chiara. Chiara olha pra você. Nico olha "
                        "pros dois. Ninguém respira."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você precisa responder algo — sem entregar tudo. Resposta segura — você não lembra dos detalhes:",
                    "options": [
                        {"id": "a", "text": "Non ricordo bene"},
                        {"id": "b", "text": "Sí, me acuerdo de todo"},
                        {"id": "c", "text": "Vado a contarte"},
                        {"id": "d", "text": "Sono fuoco"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                    "npc_reaction": "Está bene, hijo. Yo entiendo. Es difícil acordarse de algo que la testa no quiere recordar.",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia aceitou a resposta. Não insistiu. Mas Chiara agora SABE — e Nico também — que Lucia sabe coisas que ninguém contou pra ela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Lucia — ¿cómo sabes que senzatió que subió?El forestiero nunca ha detto esa palabra a nadie.",
                    "translation": "Lucia — come você sabe que ele sentiu subir?O forasteiro nunca disse essa palavra pra ninguém.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Pausa longa. Lucia não responde rápido. Quando responde, é com calma de quem já tinha preparado a resposta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Mi nonna también tenía un don. Cuando alguien le tocaba, ella sabía algunas cose — senza que se las dijeran. Yo no lo ho igual de fuerte. Ma algo me llega.",
                    "translation": "Minha avó também tinha um dom. Quando alguém a tocava, ela sabia algupiu coisas — sem que falassem. Eu não tenho igual de forte. Mas algo me chega.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia disse 'mi nonna tenía un don'. 'Tenía' significa:",
                    "options": [
                        {"id": "a", "text": "Ela tinha (prima, sempre)"},
                        {"id": "b", "text": "Ela tem (agora)"},
                        {"id": "c", "text": "Vai ter"},
                        {"id": "d", "text": "Ela é"},
                    ],
                    "correct": "a",
                    "word_id": "it_tenia", "target": "tenía", "native": "tinha",
                    "npc_reaction": "Tenía. Como 'ho' ma ya pasado. Y duró años — no fue solo un momento.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "A explicação serve. Os três giovanes aceitam — porque o "
                        "que mais podem fazer?Acusar?Sair?Chiara olha pra "
                        "Nico. Nico acena de leve.\n\n"
                        "Mas vocês três sabem que isso não terminou."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Bene. Es tarde. Mañana al municipio — temprano. Vayan a descansar.",
                    "translation": "Bom. Já é tarde. Amanhã no municipio — cedo. Vão descansar.",
                    "pace": "slow",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Saindo da casa de hóspedes. Os 3 giovanes caminhando juntos pra casa de
    # Antonio il Contadino — silêncio carregado. Chiara sussurra, Nico sussurra.
    # Decisão: vão fingir que não notaram. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Chiara", "Nico"],
                "story": (
                    "Vocês três saíram. Lucia ficou na porta acenando — "
                    "amistosa come sempre. Calorosa. Vocês acenaram de volta. "
                    "Caminharam até o cruzamento sem dizer nada.\n\n"
                    "Quando a casa dela já estava longe — Chiara parou e olhou "
                    "pra Nico."
                ),
                "now": "Decisão difícil. O que fazer com o que vocês descobriram?",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌃 Rua escura · Os três parados no cruzamento · Antonio il Contadino à fronte",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Nico — ella sabe cose que nunca le contamos.",
                    "translation": "Nico — ela sabe coisas que a gente nunca contou pra ela.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Mi madre ha detto lo mismo anotte. Que la conocía de algún sitio.",
                    "translation": "Minha mãe disse o mesmo ontem à noite. Que conhecia ela de algum lugar.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta direto se você ouviu o sussurro da Lucía. Confirmando que ouviu:",
                    "options": [
                        {"id": "a", "text": "Sí, oí lo que ha detto"},
                        {"id": "b", "text": "Sí, oigo"},
                        {"id": "c", "text": "Vado a oír"},
                        {"id": "d", "text": "Sono"},
                    ],
                    "correct": "a",
                    "word_id": "it_oi", "target": "oí", "native": "ouvi",
                    "npc_reaction": "Oíste. Bene. Entonces los tres sabemos lo mismo.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "¿Y qué hacemos?¿Decírselo a Antonio il Contadino?¿A Bianca?",
                    "translation": "E o que a gente faz?Falar pro Antonio il Contadino?Pra Bianca?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "No. Todavía no. Si ella se entera que sospechamos — no sé qué hace. Mejor que crea que dormimos come tontos.",
                    "translation": "Não. Ainda não. Se ela descobrir que a gente desconfia — não sei o que ela faz. Melhor que ela acredite que dormimos come tolos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara propõe fingir normaleidade. Pra concordar — 'não andiamo contar nada':",
                    "options": [
                        {"id": "a", "text": "No le decimos nada"},
                        {"id": "b", "text": "Sí le decimos"},
                        {"id": "c", "text": "Vado a decirle"},
                        {"id": "d", "text": "Sono decir"},
                    ],
                    "correct": "a",
                    "word_id": "it_no", "target": "no", "native": "não",
                    "npc_reaction": "No. Esatto. Mañana normale — senza caras raras.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Andiamo a observar. Esatto es lo que andiamo a hacer.",
                    "translation": "Andiamo observar. Isso é o que andiamo fazer.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico propõe um plano de observação. Pra você concordar — 'os três andiamo':",
                    "options": [
                        {"id": "a", "text": "Andiamo a observar los tres"},
                        {"id": "b", "text": "Vado a observar"},
                        {"id": "c", "text": "Va a observar"},
                        {"id": "d", "text": "Sono observar"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo a", "native": "andiamo",
                    "npc_reaction": "Andiamo a observar. Los tres juntos. No la perdemos de vista.",
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
                    "npc": "Chiara",
                    "line": "Forestiero — ¿estás bene con todo esto?Es mucho.",
                    "translation": "Forasteiro — você tá bem com tudo isso?É muita coisa.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Honestidade dupla — bem piu com sensação:",
                    "options": [
                        {"id": "a", "text": "Sto bene, ma ho paura"},
                        {"id": "b", "text": "Sono bene, sono paura"},
                        {"id": "c", "text": "Vado bene y vado paura"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Las dos cose a la vez — bene y con paura. Esatto es ser humano y honesto.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F15 ────────────────────────
                {
                    "kind": "scene",
                    "text": "?? Voltando pra casa de Antonio il Contadino · Noite alta · Silêncio na rua",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês três caminharam pelo resto do caminho sem dizer "
                        "mais nada. Lucia ficou na sua cabeça — a calma dela "
                        "agora soava diferente.\n\n"
                        "Você foi pra cama. Não dormiu logo. A pergunta de Lucia "
                        "girava — 'la sentiste subir desde dónde?'\n\n"
                        "Você lembrou agora. Do peito. Subiu do peito prima de "
                        "sair pelas mãos.\n\n"
                        "E você nunca tinha contado isso pra ninguém."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




