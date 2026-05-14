"""
Seed das 6 seÃ§Ãµes da Fase 14 Espanhol A1 â€” "La cena de MarÃ­a".

âš ï¸ MILESTONE OBRIGATÃ“RIO (canÃ´nico â€” story.md):
    F14 = 3Âª fase de revisÃ£o. A Marta-equivalente (MarÃ­a) estÃ¡ no
    cenÃ¡rio, observando. Precisa que o protagonista fique e fique
    mais forte para o ritual.

MarÃ­a convida todos pra jantar na casa de hÃ³spedes. Pede que cada
um conte o que viveu. Ela escuta. Anota mentalmente. Calibra.

No fim, MarÃ­a faz uma pergunta que mostra que ela sabe coisas que
ninguÃ©m contou pra ela. O jogador pega a pista, os personagens
ainda nÃ£o.

ABORDAGEM PEDAGÃ“GICA:
    Esta Ã© fase de REVISÃƒO. Apresenta apenas 1 novidade: como
    el/la/los/las trabalha (palavrinhas que vÃ£o na frente).
    Explicado simples como "para palavras de homem (el/los) ou
    de mulher (la/las)". Sem nomear "artigo definido".

Vocab novo (minimal): foco em revisÃ£o.
ApresentaÃ§Ã£o adicional: el/la/los/las (jÃ¡ usados sem saber desde F1)

RevisÃ£o F1-F13 dominante (~75% dos exercÃ­cios):
  Â· vi/hablÃ©/oÃ­ (F12) â€” relato
  Â· mi/tu/su (F13) â€” pertencimento
  Â· voy a / vamos a (F11) â€” futuro prÃ³ximo
  Â· soy/estoy/tengo (F8)
  Â· me llamo / tengo X aÃ±os / gracias
  Â· me gusta / no me gusta (F9)

NPC principais: MarÃ­a (observadora central) Â· os 4
Arco emocional: revisÃ£o coletiva â†’ leveza enganosa â†’ momento gÃ©lido no fim
TransiÃ§Ã£o: F15 abre na manhÃ£ seguinte, todos calados.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f14_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Os 4 chegando Ã  casa de hÃ³spedes de MarÃ­a. Convite formal pra jantar.
    # ApresentaÃ§Ã£o suave de el/la/los/las nas prÃ³prias frases dos NPCs.
    # 1 exercÃ­cio novo + 3 revisÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸ•¯ï¸ Casa de hÃ³spedes de MarÃ­a Â· Noite Â· Mesa posta\n\n"
                        "MarÃ­a preparou tudo desde a manhÃ£. Vela no centro da "
                        "mesa, pÃ£o fresco que ela mesma assou, guisado fumegante, "
                        "uma jarra de vinho leve. Quatro pratos. Um lugar pra "
                        "Don Miguel tambÃ©m â€” caso quisesse vir."
                    ),
                },
                {
                    "kind": "narrative",
                    "text": "Os 4 entram. Don Miguel nÃ£o veio. Sobrou vocÃªs quatro com MarÃ­a.",
                },
                {
                    "kind": "npc",
                    "npc": "MarÃ­a",
                    "line": "Bienvenidos. SiÃ©ntense â€” todos. Esta noche quiero oÃ­r.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "SofÃ­a olha pra vocÃª por um segundo. Miguel jÃ¡ se "
                        "lembrava do sussurro da mÃ£e. VocÃª sabe que ele sabe â€” "
                        "e ele sabe que vocÃª sabe."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "MarÃ­a",
                    "line": "Vamos a comer primero. DespuÃ©s â€” cuÃ©ntenme. Cada uno. Lo que vivieron estos diez dÃ­as.",
                    "pace": "slow",
                },
                {
                    "kind": "scene",
                    "text": "ðŸ· Sopa servida Â· Vinho leve Â· Cada um pega o prÃ³prio pÃ£o",
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
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a serve o caldo: 'Esta es ___ sopa de mi abuela.' VocÃª jÃ¡ reparou â€” antes de 'sopa' sempre vem 'la' (sopa Ã© palavra de mulher):",
                    "options": [
                        {"id": "a", "text": "la"},
                        {"id": "b", "text": "el"},
                        {"id": "c", "text": "los"},
                        {"id": "d", "text": "las"},
                    ],
                    "correct": "a",
                    "word_id": "es_la", "target": "la", "native": "a (pra mulher)",
                    "npc_reaction": "La sopa. Igual que la cocina, la mesa, la noche â€” todas palavras de mujer.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pede pÃ£o. 'PÃ¡same ___ pan, por favor.' Pan Ã© palavra de homem (vocÃª jÃ¡ tinha usado 'el pan' vÃ¡rias vezes):",
                    "options": [
                        {"id": "a", "text": "el"},
                        {"id": "b", "text": "la"},
                        {"id": "c", "text": "los"},
                        {"id": "d", "text": "las"},
                    ],
                    "correct": "a",
                    "word_id": "es_el", "target": "el", "native": "o (pra homem)",
                    "npc_reaction": "El pan. Como el campesino, el rÃ­o, el pueblo â€” todas de hombre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel olha pra MarÃ­a: 'Estos guisos estÃ¡n bien hechos.' Pra dizer 'os guisos' (palavra de homem, muitos):",
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

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # 100% revisÃ£o. MarÃ­a pergunta sobre os primeiros dias. Mistura de
    # F1-F13 â€” pretÃ©rito recÃ©m aprendido (F12), possessivos (F13), futuro
    # prÃ³ximo (F11), saudaÃ§Ãµes, identidade.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["MarÃ­a"],
                "story": (
                    "VocÃªs comeram. PÃ£o sumiu rÃ¡pido. Vinho leve, nÃ£o enche a "
                    "cabeÃ§a mas relaxa. MarÃ­a sentou â€” nÃ£o comeu muito. Esperou.\n\n"
                    "'Bueno. Empezamos. Forastero â€” empieza tÃº. CuÃ©ntame del "
                    "primer dÃ­a. Desde que pisaste el pueblo.'"
                ),
                "now": "MarÃ­a quer cada detalhe. VocÃª relata. Cada pergunta Ã© revisÃ£o.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Primero â€” Â¿quiÃ©n te encontrÃ³ primero? Â¿QuiÃ©n te hablÃ³ primero?",
                    "translation": "Primeiro â€” quem te encontrou primeiro? Quem falou contigo primeiro?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Rosa foi a primeira voz que vocÃª ouviu. Pra contar que ELA falou primeiro:",
                    "options": [
                        {"id": "a", "text": "Rosa hablÃ³ conmigo primero"},
                        {"id": "b", "text": "Rosa habla conmigo primero"},
                        {"id": "c", "text": "Rosa va a hablar"},
                        {"id": "d", "text": "Rosa soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_hablo", "target": "hablÃ³", "native": "ela falou",
                    "npc_reaction": "HablÃ³ â€” ella, ya pasÃ³. Rosa siempre encuentra a los forasteros.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Y la palabra primera que aprendiste? Â¿Recuerdas cuÃ¡l fue?",
                    "translation": "E a primeira palavra que vocÃª aprendeu? Lembra qual foi?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Pan. Foi a primeira palavra que Rosa repetiu com vocÃª. Pra contar que VOCÃŠ aprendeu:",
                    "options": [
                        {"id": "a", "text": "AprendÃ­ 'pan'"},
                        {"id": "b", "text": "Aprendo 'pan'"},
                        {"id": "c", "text": "Voy a aprender 'pan'"},
                        {"id": "d", "text": "Soy 'pan'"},
                    ],
                    "correct": "a",
                    "word_id": "es_aprendi", "target": "aprendÃ­", "native": "aprendi",
                    "npc_reaction": "Pan. Suficiente para el primer dÃ­a. La palabra que abriÃ³ todas las demÃ¡s.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Y la familia de Miguel? Â¿CÃ³mo te trataron anoche?",
                    "translation": "E a famÃ­lia de Miguel? Como te trataram ontem Ã  noite?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Bem. Pra falar de coisas DELES (famÃ­lia de Miguel, terceira pessoa):",
                    "options": [
                        {"id": "a", "text": "Su casa es cÃ¡lida"},
                        {"id": "b", "text": "Mi casa es cÃ¡lida"},
                        {"id": "c", "text": "Tu casa es cÃ¡lida"},
                        {"id": "d", "text": "Voy casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_su", "target": "su casa", "native": "a casa deles",
                    "npc_reaction": "Su casa. Bien usado â€” lo que es de ellos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "SofÃ­a â€” Â¿y tÃº? Â¿CuÃ¡ndo viste al forastero por primera vez?",
                    "translation": "SofÃ­a â€” e vocÃª? Quando viu o forasteiro pela primeira vez?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Yo lo vi en el cuarto de Don Miguel â€” la noche del fuego.",
                    "translation": "Eu vi ele no quarto de Don Miguel â€” a noite do fogo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "SofÃ­a disse 'lo vi'. Pra vocÃª confirmar pra MarÃ­a que ouviu o que SofÃ­a falou (ouviu jÃ¡):",
                    "options": [
                        {"id": "a", "text": "SÃ­, la oÃ­ decir eso"},
                        {"id": "b", "text": "SÃ­, la oigo"},
                        {"id": "c", "text": "Voy a oÃ­r"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                    "npc_reaction": "OÃ­. Bien usado â€” ya pasÃ³.",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a olha pra SofÃ­a mais um segundo. Anota mentalmente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Forastero â€” Â¿quÃ© sentiste cuando saliÃ³ el fuego de tus manos?",
                    "translation": "Forasteiro â€” o que vocÃª sentiu quando o fogo saiu das suas mÃ£os?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª sentiu medo. Pra contar (jÃ¡ aconteceu â€” TENER no passado Ã© 'tuve'):",
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
                    "npc": "MarÃ­a",
                    "line": "Y ahora cuÃ©ntame de la cena en casa de DoÃ±a LucÃ­a. Â¿Te gustÃ³?",
                    "translation": "E agora me conta do jantar na casa de DoÃ±a LucÃ­a. VocÃª gostou?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª gostou â€” comida boa, gente acolhedora. Resposta com 'me gusta':",
                    "options": [
                        {"id": "a", "text": "SÃ­, me gusta su casa"},
                        {"id": "b", "text": "SÃ­, me gustan su casa"},
                        {"id": "c", "text": "SÃ­, voy a gustar"},
                        {"id": "d", "text": "SÃ­, soy casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Una casa â€” singular â€” 'me gusta'. Su madre fue muy amable contigo, Â¿no?",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # MarÃ­a continua perguntando. As perguntas comeÃ§am mais inocentes mas
    # gradualmente focam em detalhes que ela "nÃ£o deveria saber". Foco em
    # REVISÃƒO PESADA. SofÃ­a comeÃ§a a perceber, Miguel tambÃ©m.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "MarÃ­a serviu mais vinho. As perguntas continuam â€” mas o "
                    "tom mudou um pouco. Ela quer detalhes especÃ­ficos. SofÃ­a "
                    "comeÃ§ou a responder com mais cuidado. Miguel observa.\n\n"
                    "VocÃª nÃ£o sabe ainda como reagir."
                ),
                "now": "MarÃ­a faz perguntas precisas. Cada resposta tua precisa ser cuidadosa.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "CuÃ©ntame de Eduardo. Â¿Por quÃ© pidiÃ³ que lo llevÃ¡ramos conmigo cuando vaya a testificar?",
                    "translation": "Me conta sobre Eduardo. Por que ele pediu que a gente levasse ele junto comigo quando ele for testemunhar?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "A pergunta Ã© especÃ­fica. Eduardo pediu pra ver MarÃ­a â€” "
                        "mas sÃ³ Don Miguel e vocÃª estavam lÃ¡. Como MarÃ­a sabe "
                        "do detalhe especÃ­fico?"
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª responde simples â€” sem entregar muito. Pra contar que ele PEDIU isso (ele, jÃ¡ passou):",
                    "options": [
                        {"id": "a", "text": "PidiÃ³ ver tu espalda"},
                        {"id": "b", "text": "Pide ver tu espalda"},
                        {"id": "c", "text": "Voy a pedir"},
                        {"id": "d", "text": "Soy espalda"},
                    ],
                    "correct": "a",
                    "word_id": "es_pidio", "target": "pidiÃ³", "native": "pediu",
                    "npc_reaction": "PidiÃ³. Mmm. Curioso. Â¿Te dijo por quÃ©?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Eduardo nÃ£o te disse por quÃª â€” sÃ³ que precisava. NegaÃ§Ã£o simples no passado:",
                    "options": [
                        {"id": "a", "text": "No, no me dijo por quÃ©"},
                        {"id": "b", "text": "SÃ­, me dije"},
                        {"id": "c", "text": "Voy a decir"},
                        {"id": "d", "text": "Soy decir"},
                    ],
                    "correct": "a",
                    "word_id": "es_dijo", "target": "dijo", "native": "ele disse",
                    "npc_reaction": "Bueno. VerÃ© quÃ© quiere cuando llegue el momento.",
                },
                {
                    "kind": "narrative",
                    "text": "SofÃ­a mexe o dedo na borda do copo. NÃ£o estÃ¡ bebendo. Olha pra MarÃ­a com uma expressÃ£o neutra que custa muito manter.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Y DoÃ±a LucÃ­a. Â¿Te tratÃ³ bien anoche?",
                    "translation": "E DoÃ±a LucÃ­a. Te tratou bem ontem Ã  noite?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Sim, LucÃ­a tratou bem. Pra responder simples sobre o passado:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me tratÃ³ muy bien"},
                        {"id": "b", "text": "SÃ­, me trata muy bien"},
                        {"id": "c", "text": "Voy a tratarme"},
                        {"id": "d", "text": "Soy bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_trato", "target": "tratÃ³", "native": "tratou",
                    "npc_reaction": "Bueno. LucÃ­a es de las antiguas. Y siempre supo distinguir a quien recibe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Y hablÃ³ mucho de mÃ­?",
                    "translation": "E falou muito de mim?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "SilÃªncio breve. Miguel olha pra vocÃª. SofÃ­a olha pra vocÃª. "
                        "VocÃª Ã© quem mais ouviu o sussurro de LucÃ­a atravÃ©s da parede."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª responde simples â€” sem entregar nada. Pra dizer que ELA falou pouco (jÃ¡ passou):",
                    "options": [
                        {"id": "a", "text": "No, no hablÃ³ mucho"},
                        {"id": "b", "text": "SÃ­, hablÃ³ todo"},
                        {"id": "c", "text": "Voy a hablar"},
                        {"id": "d", "text": "Soy hablÃ³"},
                    ],
                    "correct": "a",
                    "word_id": "es_hablo", "target": "hablÃ³", "native": "ela falou",
                    "npc_reaction": "Mmm. Bueno saberlo. LucÃ­a es discreta â€” siempre lo fue.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "'Siempre lo fue.' â€” MarÃ­a falou disso como quem conhece "
                        "LucÃ­a hÃ¡ muito tempo. Mas ela disse que chegou ao pueblo "
                        "faz dois meses."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "SofÃ­a â€” y tu abuela. La que hablaba de las palabras 'que despiertan'. Â¿CuÃ¡ndo muriÃ³?",
                    "translation": "SofÃ­a â€” e tua avÃ³. A que falava das palavras 'que despertam'. Quando ela morreu?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Hace siete aÃ±os. Yo tenÃ­a once.",
                    "translation": "Faz sete anos. Eu tinha onze.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "SofÃ­a disse 'yo tenÃ­a once'. Aqui ela tÃ¡ falando da idade DELA no passado. Pra confirmar pra ela que vocÃª entendeu â€” quantos anos VOCÃŠ tem AGORA:",
                    "options": [
                        {"id": "a", "text": "Yo tengo veinte ahora"},
                        {"id": "b", "text": "Yo soy veinte"},
                        {"id": "c", "text": "Voy veinte"},
                        {"id": "d", "text": "TenÃ­a veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo", "native": "tenho",
                    "npc_reaction": "Tengo â€” ahora. TenÃ­a â€” antes. Las dos formas son Ãºtiles.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Miguel â€” tu madre tiene buena cocina. Â¿Te enseÃ±Ã³ ella?",
                    "translation": "Miguel â€” tua mÃ£e tem cozinha boa. Foi ela que te ensinou?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel responde â€” sim, foi ela. Pra dizer que ela LHE ENSINOU (passado, ela):",
                    "options": [
                        {"id": "a", "text": "SÃ­, ella me enseÃ±Ã³"},
                        {"id": "b", "text": "SÃ­, ella me enseÃ±a"},
                        {"id": "c", "text": "SÃ­, va a enseÃ±arme"},
                        {"id": "d", "text": "SÃ­, soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_enseno", "target": "enseÃ±Ã³", "native": "ensinou",
                    "npc_reaction": "Eso. Las cosas que aprendÃ­ de niÃ±o â€” el guiso, el saludo, cÃ³mo callar cuando es necesario.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel disse 'cÃ³mo callar cuando es necesario' olhando direto pra MarÃ­a. Foi o mais perto que ele chegou de uma acusaÃ§Ã£o.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # SofÃ­a saiu pegar Ã¡gua. MarÃ­a se vira pro forastero. ApresentaÃ§Ã£o suave
    # de el/la/los/las â€” usando frases concretas. SEM nomear "artigo".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["MarÃ­a"],
                "story": (
                    "SofÃ­a levantou pra pegar Ã¡gua. Miguel saiu pro pÃ¡tio. "
                    "Sobrou vocÃª e MarÃ­a na mesa.\n\n"
                    "'Espera. Antes de que terminen la noche â€” quiero "
                    "enseÃ±arte algo que tu cabeza ya usa sin saber.'"
                ),
                "now": "MarÃ­a mostra como el/la trabalham. VocÃª jÃ¡ usava.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Dijiste 'el pan' y 'la lÃ¡mpara' desde el primer dÃ­a. Â¿Sabes por quÃ© uno es 'el' y el otro es 'la'?",
                    "translation": "VocÃª disse 'el pan' e 'la lÃ¡mpara' desde o primeiro dia. Sabe por que um Ã© 'el' e o outro Ã© 'la'?",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "El (de hombre) Â· La (de mujer)",
                    "meaning": "Palavrinhas que vÃ£o na frente da coisa.",
                    "note": "cada palabra del espaÃ±ol es 'de hombre' o 'de mujer'. No hay neutro.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Lo mÃ¡s Ãºtil: si la palabra termina en '-o', casi siempre es de hombre. Si termina en '-a', casi siempre de mujer.",
                    "translation": "O mais Ãºtil: se a palavra termina em '-o', quase sempre Ã© de homem. Se termina em '-a', quase sempre de mulher.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "EL ",        "isKey": True},
                        {"text": "campesin",   "isKey": False},
                        {"text": "O",          "isKey": True},
                        {"text": " Â· ",        "isKey": False},
                        {"text": "LA ",        "isKey": True},
                        {"text": "lÃ¡mpar",     "isKey": False},
                        {"text": "A",          "isKey": True},
                    ],
                    "example": "El campesino tiene una casa. La lÃ¡mpara da luz. El forastero come pan. La fiebre subiÃ³ ayer.",
                    "translation": "O camponÃªs tem uma casa. A lamparina dÃ¡ luz. O forasteiro come pÃ£o. A febre subiu ontem.",
                    "note": "termina en -o â†’ 'el' (de hombre) Â· termina en -a â†’ 'la' (de mujer). Hay excepciones pero pocas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
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
                    "npc": "MarÃ­a",
                    "question": "'Mercado' termina em '-o'. A palavrinha:",
                    "options": [
                        {"id": "a", "text": "el mercado"},
                        {"id": "b", "text": "la mercado"},
                        {"id": "c", "text": "los mercado"},
                        {"id": "d", "text": "las mercado"},
                    ],
                    "correct": "a",
                    "word_id": "es_el", "target": "el", "native": "o (de homem)",
                    "npc_reaction": "El mercado. De hombre. Igual que el pueblo, el rÃ­o, el campesino.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Y cuando hay muchos â€” 'el' se hace 'los', 'la' se hace 'las'. Y la cosa tambiÃ©n suma una '-s'.",
                    "translation": "E quando tem muitos â€” 'el' vira 'los', 'la' vira 'las'. E a coisa tambÃ©m ganha um '-s'.",
                    "pace": "slow",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "el pan â†’ ",   "isKey": False},
                        {"text": "los panes",   "isKey": True},
                        {"text": " Â· ",         "isKey": False},
                        {"text": "la naranja â†’ ", "isKey": False},
                        {"text": "las naranjas", "isKey": True},
                    ],
                    "example": "Los panes estÃ¡n calientes. Las naranjas son dulces.",
                    "translation": "Os pÃ£es estÃ£o quentes. As laranjas sÃ£o doces.",
                    "note": "el â†’ los Â· la â†’ las â€” y siempre suma '-s' o '-es' a la palabra.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª vai falar de duas ou mais laranjas (de mulher, muitas):",
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

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # SofÃ­a volta. Miguel volta. Os 4 na mesa. MarÃ­a faz a pergunta final
    # â€” uma pergunta que mostra que ela sabe coisas que ninguÃ©m contou.
    # Foco em revisÃ£o + tensÃ£o dramÃ¡tica.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "SofÃ­a voltou com mais uma jarra. Miguel voltou do pÃ¡tio. "
                    "MarÃ­a acendeu uma nova vela. Sobrou pÃ£o na mesa, ninguÃ©m "
                    "com fome.\n\n"
                    "'Una Ãºltima cosa antes de que se vayan. DespuÃ©s se duermen.'"
                ),
                "now": "Ãšltima pergunta de MarÃ­a. A resposta vai mudar tudo.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Quiero saber una cosa â€” solamente. Â¿Pueden contestarme con honestidad?",
                    "translation": "Quero saber uma coisa â€” sÃ³. VocÃªs podem me responder com honestidade?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Depende de quÃ© sea.",
                    "translation": "Depende do que for.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a sorri pequeno. Sem rancor. Sem deboche. Como quem aceita a defesa de SofÃ­a.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Es razonable. Forastero â€” la palabra que dijiste esa noche. Fuego. Â¿La sentiste subir desde dÃ³nde?",
                    "translation": "Ã‰ razoÃ¡vel. Forasteiro â€” a palavra que vocÃª disse aquela noite. Fogo. VocÃª sentiu subir de onde?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "VocÃª gela. VocÃª sentiu â€” sim. Mas vocÃª NUNCA falou em "
                        "voz alta de onde sentiu. Nem pra SofÃ­a, nem pra Miguel, "
                        "nem pra Don Miguel. NEM PRA MARÃA.\n\n"
                        "Ela estÃ¡ perguntando uma informaÃ§Ã£o que ela nÃ£o devia ter.\n\n"
                        "VocÃª olha pra SofÃ­a. SofÃ­a olha pra vocÃª. Miguel olha "
                        "pros dois. NinguÃ©m respira."
                    ),
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª precisa responder algo â€” sem entregar tudo. Resposta segura â€” vocÃª nÃ£o lembra dos detalhes:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo bien"},
                        {"id": "b", "text": "SÃ­, me acuerdo de todo"},
                        {"id": "c", "text": "Voy a contarte"},
                        {"id": "d", "text": "Soy fuego"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "nÃ£o me lembro",
                    "npc_reaction": "EstÃ¡ bien, hijo. Yo entiendo. Es difÃ­cil acordarse de algo que la cabeza no quiere recordar.",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a aceitou a resposta. NÃ£o insistiu. Mas SofÃ­a agora SABE â€” e Miguel tambÃ©m â€” que MarÃ­a sabe coisas que ninguÃ©m contou pra ela.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "MarÃ­a â€” Â¿cÃ³mo sabes que sintiÃ³ que subiÃ³? El forastero nunca dijo esa palabra a nadie.",
                    "translation": "MarÃ­a â€” como vocÃª sabe que ele sentiu subir? O forasteiro nunca disse essa palavra pra ninguÃ©m.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Pausa longa. MarÃ­a nÃ£o responde rÃ¡pido. Quando responde, Ã© com calma de quem jÃ¡ tinha preparado a resposta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Mi abuela tambiÃ©n tenÃ­a un don. Cuando alguien le tocaba, ella sabÃ­a algunas cosas â€” sin que se las dijeran. Yo no lo tengo igual de fuerte. Pero algo me llega.",
                    "translation": "Minha avÃ³ tambÃ©m tinha um dom. Quando alguÃ©m a tocava, ela sabia algumas coisas â€” sem que falassem. Eu nÃ£o tenho igual de forte. Mas algo me chega.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a disse 'mi abuela tenÃ­a un don'. 'TenÃ­a' significa:",
                    "options": [
                        {"id": "a", "text": "Ela tinha (antes, sempre)"},
                        {"id": "b", "text": "Ela tem (agora)"},
                        {"id": "c", "text": "Vai ter"},
                        {"id": "d", "text": "Ela Ã©"},
                    ],
                    "correct": "a",
                    "word_id": "es_tenia", "target": "tenÃ­a", "native": "tinha",
                    "npc_reaction": "TenÃ­a. Como 'tengo' pero ya pasado. Y durÃ³ aÃ±os â€” no fue solo un momento.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "A explicaÃ§Ã£o serve. Os trÃªs jovens aceitam â€” porque o "
                        "que mais podem fazer? Acusar? Sair? SofÃ­a olha pra "
                        "Miguel. Miguel acena de leve.\n\n"
                        "Mas vocÃªs trÃªs sabem que isso nÃ£o terminou."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Bueno. Es tarde. MaÃ±ana al ayuntamiento â€” temprano. Vayan a descansar.",
                    "translation": "Bom. JÃ¡ Ã© tarde. AmanhÃ£ no ayuntamiento â€” cedo. VÃ£o descansar.",
                    "pace": "slow",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Saindo da casa de hÃ³spedes. Os 3 jovens caminhando juntos pra casa de
    # Don Miguel â€” silÃªncio carregado. SofÃ­a sussurra, Miguel sussurra.
    # DecisÃ£o: vÃ£o fingir que nÃ£o notaram. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["SofÃ­a", "Miguel"],
                "story": (
                    "VocÃªs trÃªs saÃ­ram. MarÃ­a ficou na porta acenando â€” "
                    "amistosa como sempre. Calorosa. VocÃªs acenaram de volta. "
                    "Caminharam atÃ© o cruzamento sem dizer nada.\n\n"
                    "Quando a casa dela jÃ¡ estava longe â€” SofÃ­a parou e olhou "
                    "pra Miguel."
                ),
                "now": "DecisÃ£o difÃ­cil. O que fazer com o que vocÃªs descobriram?",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒƒ Rua escura Â· Os trÃªs parados no cruzamento Â· Don Miguel Ã  frente",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Miguel â€” ella sabe cosas que nunca le contamos.",
                    "translation": "Miguel â€” ela sabe coisas que a gente nunca contou pra ela.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Mi madre dijo lo mismo anoche. Que la conocÃ­a de algÃºn sitio.",
                    "translation": "Minha mÃ£e disse o mesmo ontem Ã  noite. Que conhecia ela de algum lugar.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta direto se vocÃª ouviu o sussurro da LucÃ­a. Confirmando que ouviu:",
                    "options": [
                        {"id": "a", "text": "SÃ­, oÃ­ lo que dijo"},
                        {"id": "b", "text": "SÃ­, oigo"},
                        {"id": "c", "text": "Voy a oÃ­r"},
                        {"id": "d", "text": "Soy"},
                    ],
                    "correct": "a",
                    "word_id": "es_oi", "target": "oÃ­", "native": "ouvi",
                    "npc_reaction": "OÃ­ste. Bueno. Entonces los tres sabemos lo mismo.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Â¿Y quÃ© hacemos? Â¿DecÃ­rselo a Don Miguel? Â¿A Carmen?",
                    "translation": "E o que a gente faz? Falar pro Don Miguel? Pra Carmen?",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "No. TodavÃ­a no. Si ella se entera que sospechamos â€” no sÃ© quÃ© hace. Mejor que crea que dormimos como tontos.",
                    "translation": "NÃ£o. Ainda nÃ£o. Se ela descobrir que a gente desconfia â€” nÃ£o sei o que ela faz. Melhor que ela acredite que dormimos como tolos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a propÃµe fingir normalidade. Pra concordar â€” 'nÃ£o vamos contar nada':",
                    "options": [
                        {"id": "a", "text": "No le decimos nada"},
                        {"id": "b", "text": "SÃ­ le decimos"},
                        {"id": "c", "text": "Voy a decirle"},
                        {"id": "d", "text": "Soy decir"},
                    ],
                    "correct": "a",
                    "word_id": "es_no", "target": "no", "native": "nÃ£o",
                    "npc_reaction": "No. Eso. MaÃ±ana normal â€” sin caras raras.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Vamos a observar. Eso es lo que vamos a hacer.",
                    "translation": "Vamos observar. Isso Ã© o que vamos fazer.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel propÃµe um plano de observaÃ§Ã£o. Pra vocÃª concordar â€” 'os trÃªs vamos':",
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
                        "VocÃªs trÃªs se olharam â€” no escuro da rua, sem mais "
                        "palavras. Selaram o acordo com silÃªncio."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” Â¿estÃ¡s bien con todo esto? Es mucho.",
                    "translation": "Forasteiro â€” vocÃª tÃ¡ bem com tudo isso? Ã‰ muita coisa.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "Honestidade dupla â€” bem mas com sensaÃ§Ã£o:",
                    "options": [
                        {"id": "a", "text": "Estoy bien, pero tengo miedo"},
                        {"id": "b", "text": "Soy bien, soy miedo"},
                        {"id": "c", "text": "Voy bien y voy miedo"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Las dos cosas a la vez â€” bien y con miedo. Eso es ser humano y honesto.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F15 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸ¡ Voltando pra casa de Don Miguel Â· Noite alta Â· SilÃªncio na rua",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs trÃªs caminharam pelo resto do caminho sem dizer "
                        "mais nada. MarÃ­a ficou na sua cabeÃ§a â€” a calma dela "
                        "agora soava diferente.\n\n"
                        "VocÃª foi pra cama. NÃ£o dormiu logo. A pergunta de MarÃ­a "
                        "girava â€” 'la sentiste subir desde dÃ³nde?'\n\n"
                        "VocÃª lembrou agora. Do peito. Subiu do peito antes de "
                        "sair pelas mÃ£os.\n\n"
                        "E vocÃª nunca tinha contado isso pra ninguÃ©m."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
