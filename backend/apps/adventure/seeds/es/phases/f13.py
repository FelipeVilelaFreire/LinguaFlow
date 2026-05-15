"""
Seed das 6 seções da Fase 13 Espanhol A1 — "La familia de Miguel".

Miguel leva o grupo pra casa da família dele pra dormir essa noite —
mais seguro, longe de olhares do Vigilante. Você conhece Doña Lucía
(mãe de Miguel), as duas irmãs jovens dele e sente pela primeira vez
o que é uma família caseira em San Cristóbal.

⚠️ PONTO NARRATIVO IMPORTANTE:
    No fim da fase, Doña Lucía sussurra pra Miguel que reconhece
    María 'de algún sitio'. Pista pro jogador de que María tem
    passado que ela esconde do grupo.

Vocab novo (3): madre · padre · hermana
Apresentação adicional: hermano (em vocab_list)
Linguagem nova: 'mi/tu/su' — apresentado como "minha coisa, tua coisa,
                a coisa dele/dela". Sem termo técnico.

Revisão F1-F12 dominante:
  · ayer / vi / hablé / oí (F12) — recém aprendido, prática extra
  · voy a / vamos a (F11) — futuro próximo
  · me llamo / soy / tengo años (F1, F8, F11)
  · estoy bien / mal / mejor (F8)
  · me gusta (F9)
  · gracias / por favor (F1)
  · buenos días / buenas noches (F1)

NPC principais: Miguel · Doña Lucía (1ª aparição) · suas irmãs Lola e Rita
NPC presentes:  Sofía · María · Don Miguel · protagonista
Arco emocional: acolhimento familiar → leveza inesperada → sutil tensão
Transição:      Lucía sussurra pra Miguel; F14 abre com María convidando
                todos pra jantar.

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f13_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Chegando à casa de Doña Lucía. Apresentações. Doña Lucía aceita você
    # como filho. 1 palavra nova (madre) + revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "persuasao",
                    "min_level": 2,
                    "uses_item_tag": "moneda",
                    "success": "Voce escolhe palavras cuidadosas e a familia de Miguel baixa a guarda.",
                    "fallback": "A conversa fica dura por um momento, mas Miguel segura o clima e apresenta voce.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "🏡 Casa de Doña Lucía · Noite · Beira do pueblo\n\n"
                        "Casa baixa de adobe na rua mais afastada de San Cristóbal. "
                        "Fumaça subindo da chaminé, cheiro de guiso quente, vozes "
                        "de mulher e crianças dentro."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Mamá — soy yo. Traigo gente.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "A porta abre. Uma mulher mais alta que Miguel, cabelo grisalho preso atrás, avental cheio de farinha.",
                },
                {
                    "kind": "npc",
                    "npc": "Doña Lucía",
                    "line": "¡Mijo! ¿A esta hora? ¡Pasen, pasen — está abierta la cocina!",
                    "is_new_npc": True,
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": (
                        "Doña Lucía olha pra cada um do grupo. María por meio "
                        "segundo a mais — uma sombra passa pelo rosto dela. "
                        "Recompõe rápido."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Mamá — el forastero. Está conmigo desde el primer día.",
                },
                {
                    "kind": "npc",
                    "npc": "Doña Lucía",
                    "line": "Bienvenido, hijo. Mi casa también es tu casa esta noche.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "madre",   "native": "mãe"},
                        {"target": "padre",   "native": "pai"},
                        {"target": "hermana", "native": "irmã"},
                        {"target": "hermano", "native": "irmão"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Sol já se pôs. Doña Lucía te recebe. Você cumprimenta com respeito:",
                    "options": [
                        {"id": "a", "text": "Buenas noches, señora"},
                        {"id": "b", "text": "Buenos días"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                    "npc_reaction": "Buenas noches. Y dime 'Doña Lucía' — todos me dicen así.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Yo soy madre — de tres. Miguel y sus dos hermanas.",
                    "translation": "Eu sou mãe — de três. Miguel e as duas irmãs dele.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Doña Lucía falou 'madre'. A palavra significa:",
                    "options": [
                        {"id": "a", "text": "Mãe"},
                        {"id": "b", "text": "Irmã"},
                        {"id": "c", "text": "Filha"},
                        {"id": "d", "text": "Vizinha"},
                    ],
                    "correct": "a",
                    "word_id": "es_madre", "target": "madre", "native": "mãe",
                    "npc_reaction": "Madre. La que tuvo a los hijos. La palabra del corazón.",
                },
                {
                    "kind": "narrative",
                    "text": "Duas meninas mais jovens entram na cozinha — uma de uns 16, outra de uns 12. Curiosas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Estas son mis hijas — Lola tiene dieciséis, Rita doce. Son hermanas de Miguel.",
                    "translation": "Estas são minhas filhas — Lola tem dezesseis, Rita doze. São irmãs de Miguel.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Lola e Rita são meninas. A palavra pra menina da mesma família é:",
                    "options": [
                        {"id": "a", "text": "Hermana"},
                        {"id": "b", "text": "Hermano"},
                        {"id": "c", "text": "Madre"},
                        {"id": "d", "text": "Padre"},
                    ],
                    "correct": "a",
                    "word_id": "es_hermana", "target": "hermana", "native": "irmã",
                    "npc_reaction": "Hermana — termina en '-a' (mujer). Si fuera hombre — 'hermano' (termina en '-o').",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Doña Lucía pergunta sobre o forastero — passado e
    # presente. Você usa F1-F12 livremente. Sem novidade.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Doña Lucía", "Miguel"],
                "story": (
                    "Lucía colocou um prato fundo de guiso na sua frente. "
                    "Cheiro de tomate, ervas, batata. Pão grosso ao lado. "
                    "Os outros já comendo.\n\n"
                    "'Cuéntame, hijo. ¿Qué pasó estos últimos días? Miguel "
                    "no me contó casi nada.'"
                ),
                "now": "Lucía pergunta. Você relata — usando tudo que aprendeu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Antes de empezar — ¿cómo te llamas, hijo?",
                    "translation": "Antes de começar — como você se chama, filho?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Resposta simples — você já fez isso muitas vezes:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo veinte años"},
                        {"id": "d", "text": "Buenas noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Bonito nombre. ¿Y cuántos años tienes?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Vinte anos:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte años"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Estoy veinte"},
                        {"id": "d", "text": "Voy veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte años", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Igual que mi Miguel.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Cuéntame del primer día. ¿Qué hiciste cuando llegaste al pueblo?",
                    "translation": "Me conta do primeiro dia. O que você fez quando chegou no pueblo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Você lembra. Rosa apareceu primeiro, depois Don Miguel. Pra contar que VIU Rosa primeiro (já passou):",
                    "options": [
                        {"id": "a", "text": "Vi a Rosa primero"},
                        {"id": "b", "text": "Veo a Rosa primero"},
                        {"id": "c", "text": "Voy a ver a Rosa"},
                        {"id": "d", "text": "Soy a Rosa"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Igual que Eduardo te enseñó ayer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "¿Y hablaste con ellos? ¿Comiste algo ese día?",
                    "translation": "E você falou com eles? Comeu alguma coisa nesse dia?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Você comeu pão da Rosa. Pra contar (já aconteceu):",
                    "options": [
                        {"id": "a", "text": "Sí, comí pan"},
                        {"id": "b", "text": "Sí, como pan"},
                        {"id": "c", "text": "Voy a comer"},
                        {"id": "d", "text": "Soy pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_comi", "target": "comí", "native": "comi",
                    "npc_reaction": "Comí. Termina con 'í' fuerte — como 'vi', como 'oí'. Es la marca de algo ya pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Lucía: 'Y ahora — ¿estás bien aquí, en mi casa?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Comida y techo — eso siempre arregla casi todo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Mañana — ¿qué van a hacer? Miguel no me contó bien.",
                    "translation": "Amanhã — o que vocês vão fazer? Miguel não me contou direito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Amanhã o grupo vai ao ayuntamiento com os 3 testigos. Pra dizer o que TODO o grupo vai fazer:",
                    "options": [
                        {"id": "a", "text": "Vamos al ayuntamiento"},
                        {"id": "b", "text": "Voy al ayuntamiento"},
                        {"id": "c", "text": "Va al ayuntamiento"},
                        {"id": "d", "text": "Soy ayuntamiento"},
                    ],
                    "correct": "a",
                    "word_id": "es_vamos_a", "target": "vamos", "native": "vamos",
                    "npc_reaction": "Bueno. Que sea pronto y limpio.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # As irmãs de Miguel mostram a casa. Apontam coisas, dizem 'mi cuarto',
    # 'mi cama'. O aluno aprende 'mi/tu/su' pelo USO sem nomear regra.
    # Foco em REVISÃO + apresentação suave dos possessivos.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Miguel"],
                "story": (
                    "Depois da janta, as irmãs de Miguel — Lola (16) e Rita (12) — "
                    "decidiram mostrar a casa pro forastero. Tudo curioso, tudo "
                    "rápido. Apontam coisas — usando palavrinhas pequenas pra dizer "
                    "do que é cada coisa."
                ),
                "now": "As irmãs te apresentam a casa. Cada coisa tem dono — você aprende como dizem.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lola",
                    "line": "Mira — esta es mi cama. Y aquella es de mi hermana Rita.",
                    "translation": "Olha — essa é minha cama. E aquela é da minha irmã Rita.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lola",
                    "question": "Lola disse 'mi cama' apontando pra cama dela. A palavrinha 'mi' significa:",
                    "options": [
                        {"id": "a", "text": "Da Lola (minha, dela mesma falando)"},
                        {"id": "b", "text": "De outra pessoa"},
                        {"id": "c", "text": "De ninguém"},
                        {"id": "d", "text": "Do pueblo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi", "native": "minha / meu",
                    "npc_reaction": "Mi. La uso para hablar de mis cosas. Igual que en portugués: 'minha cama'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rita",
                    "line": "¿Y tu casa, joven? ¿Cómo es tu casa?",
                    "translation": "E sua casa, jovem? Como é sua casa?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Rita perguntou simples — mas você não tem casa. Não lembra. A pergunta dói pequeno.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rita",
                    "question": "Rita perguntou usando 'tu casa'. A palavrinha 'tu' significa:",
                    "options": [
                        {"id": "a", "text": "Tua / sua (de quem ela está falando)"},
                        {"id": "b", "text": "Minha"},
                        {"id": "c", "text": "Dele/dela"},
                        {"id": "d", "text": "Nossa"},
                    ],
                    "correct": "a",
                    "word_id": "es_tu", "target": "tu", "native": "tua / sua",
                    "npc_reaction": "Tu. Cuando hablo contigo, lo tuyo es 'tu'. Igual fácil.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rita",
                    "question": "Você responde honesto — não lembra da casa anterior. Mas tem onde dormir agora:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo bien"},
                        {"id": "b", "text": "Sí me acuerdo"},
                        {"id": "c", "text": "Voy a acordarme"},
                        {"id": "d", "text": "Soy casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                    "npc_reaction": "Está bien, joven. Hay tiempo.",
                },
                {
                    "kind": "narrative",
                    "text": "Sofía aponta pra uma pintura simples na parede — duas mulheres jovens pousando juntas. Lola explica.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lola",
                    "line": "Esa es mi madre cuando era joven. La otra es su hermana — nuestra tía. Murió hace años.",
                    "translation": "Essa é minha mãe quando era jovem. A outra é a irmã dela — nossa tia. Morreu faz anos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lola",
                    "question": "Lola disse 'su hermana' — falando de uma terceira pessoa (sua mãe, Doña Lucía). A palavrinha 'su' significa:",
                    "options": [
                        {"id": "a", "text": "Dele / dela / deles (de outra pessoa)"},
                        {"id": "b", "text": "Minha"},
                        {"id": "c", "text": "Tua"},
                        {"id": "d", "text": "Nossa"},
                    ],
                    "correct": "a",
                    "word_id": "es_su", "target": "su", "native": "dele / dela",
                    "npc_reaction": "Su. Para hablar de las cosas de los otros — él, ella, ellos. Una sola palabra para todos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rita",
                    "question": "Rita aponta pro pai de Lola e dela (já falecido). Pra falar do pai delas (dele):",
                    "options": [
                        {"id": "a", "text": "Mi padre era herrero"},
                        {"id": "b", "text": "Tu padre era herrero"},
                        {"id": "c", "text": "Su padre era herrero"},
                        {"id": "d", "text": "Vamos padre"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi", "native": "meu / minha",
                    "npc_reaction": "Mi padre. Porque hablo desde mí. Si tú hablas de mi padre — dices 'tu padre' (porque hablas conmigo). Si Lola habla de él — 'nuestro padre'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lola",
                    "line": "Y nuestra cocina es la pequeña ahí abajo. Allí come toda la familia.",
                    "translation": "E nossa cozinha é a pequena ali embaixo. Ali come a família toda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lola",
                    "question": "Lola disse 'nuestra cocina'. A palavrinha 'nuestra' significa:",
                    "options": [
                        {"id": "a", "text": "Nossa (de mim e de outra pessoa juntas)"},
                        {"id": "b", "text": "Minha sozinha"},
                        {"id": "c", "text": "Tua"},
                        {"id": "d", "text": "Dele"},
                    ],
                    "correct": "a",
                    "word_id": "es_nuestra", "target": "nuestra", "native": "nossa",
                    "npc_reaction": "Nuestra. Cuando algo es mío y tuyo y de más gente — todos juntos. La cocina es de toda la familia.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lola",
                    "question": "Lola: 'Forastero — ¿estás bien aquí? ¿Te gusta nuestra casa?' Resposta honesta:",
                    "options": [
                        {"id": "a", "text": "Sí, me gusta mucho"},
                        {"id": "b", "text": "No me gusta"},
                        {"id": "c", "text": "Tengo casa"},
                        {"id": "d", "text": "Soy casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Me alegro. Aquí tenemos lo poco que tenemos — pero limpio.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Sentados em volta da lareira depois do tour. Doña Lucía pega um caderno
    # velho da família. Apresentação formal de mi/tu/su/nuestro — SEM nomear
    # "possessivo". Apenas: "palabras pequenas que dicen de quién es algo".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Doña Lucía", "Miguel"],
                "story": (
                    "Depois do tour, Doña Lucía tirou de uma gaveta um caderno "
                    "velho — capa de couro gasto. 'Este libro tiene cada nombre "
                    "de mi familia escrito a mano.'\n\n"
                    "Abriu na primeira página. Você viu nomes — três gerações."
                ),
                "now": "Doña Lucía explica as palavrinhas que dizem de quem é cada coisa.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Mira aquí — 'mi padre, Tomás'. Cuando hablo de algo mío, uso 'mi'.",
                    "translation": "Olha aqui — 'meu pai, Tomás'. Quando falo de algo meu, uso 'mi'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Mi / Tu / Su / Nuestro",
                    "meaning": "Meu/minha · teu/tua · dele/dela · nosso/nossa",
                    "note": "palabras chiquitas que dicen de quién es algo",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Mi madre",  "isKey": True},
                        {"text": " · ",       "isKey": False},
                        {"text": "Tu padre",  "isKey": True},
                        {"text": " · ",       "isKey": False},
                        {"text": "Su casa",   "isKey": True},
                        {"text": " · ",       "isKey": False},
                        {"text": "Nuestra mesa", "isKey": True},
                    ],
                    "example": "Mi madre se llama Lucía. Tu padre es Don Miguel. Su casa está cerca. Nuestra mesa es grande.",
                    "translation": "Minha mãe se chama Lucía. Teu pai é Don Miguel. A casa dele/dela está perto. Nossa mesa é grande.",
                    "note": "mi/tu/su sirven para hombre y mujer igual. Nuestro/nuestra cambia con el género de la cosa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Lucía aponta pro caderno: '___ familia tiene tres generaciones aquí.' Ela tá falando da família DELA mesma:",
                    "options": [
                        {"id": "a", "text": "Mi"},
                        {"id": "b", "text": "Tu"},
                        {"id": "c", "text": "Su"},
                        {"id": "d", "text": "Nuestra"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi", "native": "minha",
                    "npc_reaction": "Mi familia. La mía — tres generaciones.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Pero si te pregunto a ti: '¿Cómo se llama ___ madre?' — uso 'tu' porque hablo contigo.",
                    "translation": "Mas se te pergunto: 'Como se chama TUA mãe?' — uso 'tu' porque falo contigo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Pra perguntar sobre a TUA mãe (sua, falando com você):",
                    "options": [
                        {"id": "a", "text": "Tu madre"},
                        {"id": "b", "text": "Mi madre"},
                        {"id": "c", "text": "Su madre"},
                        {"id": "d", "text": "Nuestra madre"},
                    ],
                    "correct": "a",
                    "word_id": "es_tu", "target": "tu", "native": "tua",
                    "npc_reaction": "Tu — cuando hablo contigo de algo tuyo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Ahora — si yo hablo con Sofía sobre Miguel: 'Sofía, ¿conoces a ___ hijo?' Yo hablo de Miguel — es 'mi hijo'.",
                    "translation": "Agora — se eu falo com Sofía sobre Miguel: 'Sofía, conhece o meu filho?' Eu falo de Miguel — é 'mi hijo'.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Pra falar de Miguel (que é filho de Lucía), no jeito como LUCÍA fala dele:",
                    "options": [
                        {"id": "a", "text": "Mi hijo"},
                        {"id": "b", "text": "Tu hijo"},
                        {"id": "c", "text": "Su hijo"},
                        {"id": "d", "text": "Nuestra hijo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi", "native": "meu",
                    "npc_reaction": "Mi hijo. Una palabra simple para una relación grande.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Sofía está pensando em Lola e Rita (irmãs de Miguel). Pra ela falar de Miguel: 'Tu hermano se llama Miguel'. E pra você falar pra Sofía 'a irmã DELA' (Lola), você usa:",
                    "options": [
                        {"id": "a", "text": "Su hermana"},
                        {"id": "b", "text": "Mi hermana"},
                        {"id": "c", "text": "Tu hermana"},
                        {"id": "d", "text": "Nuestra hermana"},
                    ],
                    "correct": "a",
                    "word_id": "es_su", "target": "su", "native": "dele/dela",
                    "npc_reaction": "Su. Cuando hablo de las cosas de Miguel — 'su hermana, su madre, su padre'.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Antes de dormir. Conversa íntima perto do fogão. Lucía conta da família
    # — usa passado (la palabra que ela ouviu na F12). Reforço orgânico de
    # mi/tu/su + passado natural.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Doña Lucía", "Miguel", "Sofía"],
                "story": (
                    "A casa esfriou um pouco. Lucía adicionou lenha no fogão. "
                    "Sofía sentou no chão de pernas cruzadas perto do fogo. "
                    "María tinha ido pro quarto que Lucía ofereceu — disse que "
                    "precisava descansar.\n\n"
                    "Sobrou você, Miguel, Sofía e Lucía em volta do fogão."
                ),
                "now": "Conversa íntima — Lucía conta da família.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Doña Lucía",
                    "situation": "Lucía mexe a panela no fogão. O guiso ainda vai demorar. Ela olha pra você — a casa é pobre, qualquer coisa ajuda.",
                    "npc_line": "Hijo — si tienes algo de comer en la bolsa, ponlo en la mesa. En esta casa todo se reparte.",
                    "item_tag": "comida",
                    "on_use": {
                        "narrative": "Você tira algo da mochila e coloca na mesa da família. Lucía sorri — o tipo de sorriso que não se finge.",
                        "npc_reaction": "Eso es. Quien trae algo a la mesa de otro — ya es de la familia. Gracias, hijo.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No te preocupes. El guiso alcanza para todos. Siéntate.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Doña Lucía — ¿cómo se llamaba su esposo? Si no es indiscreta la pregunta.",
                    "translation": "Doña Lucía — como se chamava seu marido? Se não é indiscrição.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Mi esposo se llamaba Tomás — igual que mi padre. Murió hace seis años. Era herrero también, como Eduardo.",
                    "translation": "Meu marido se chamava Tomás — igual ao meu pai. Morreu faz seis anos. Era ferreiro também, como Eduardo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Lucía disse 'mi esposo'. Ela tá falando:",
                    "options": [
                        {"id": "a", "text": "Do marido DELA (dela mesma)"},
                        {"id": "b", "text": "Do marido de outra pessoa"},
                        {"id": "c", "text": "Do filho dela"},
                        {"id": "d", "text": "Do irmão dela"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi esposo", "native": "meu marido",
                    "npc_reaction": "Mi. Cuando hablo desde mí — todo lo mío empieza con 'mi'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Mi padre fue buen hombre. Tranquilo. Habló poco — pero cuando habló, todos escucharon.",
                    "translation": "Meu pai foi bom homem. Tranquilo. Falou pouco — mas quando falou, todos escutaram.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel disse 'mi padre fue buen hombre'. 'Fue' significa que o pai dele:",
                    "options": [
                        {"id": "a", "text": "Foi (já não existe mais)"},
                        {"id": "b", "text": "É (continua sendo)"},
                        {"id": "c", "text": "Vai ser"},
                        {"id": "d", "text": "Está"},
                    ],
                    "correct": "a",
                    "word_id": "es_fue", "target": "fue", "native": "foi",
                    "npc_reaction": "Fue. Como 'soy' pero ya pasado. Mi padre fue — y ya descansa.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Sofía olhou pra Miguel. Você olhou pra Miguel. Ele falou "
                        "do pai dele sem cara triste — só direto."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Forastero — ¿y tú? ¿Recuerdas a tu familia?",
                    "translation": "Forasteiro — e você? Lembra da sua família?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Você não lembra. Resposta honesta:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo de mi familia"},
                        {"id": "b", "text": "Sí me acuerdo"},
                        {"id": "c", "text": "Voy a acordarme"},
                        {"id": "d", "text": "Soy familia"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                    "npc_reaction": "Está bien, hijo. Hay cosas que el corazón guarda aunque la cabeza no recuerde.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Lucía: 'Mañana — ¿qué vas a hacer cuando vayas al ayuntamiento?' Pra você dizer o que VAI fazer (algo logo):",
                    "options": [
                        {"id": "a", "text": "Voy a hablar con el Alcalde"},
                        {"id": "b", "text": "Hablo con el Alcalde"},
                        {"id": "c", "text": "Hablé con el Alcalde"},
                        {"id": "d", "text": "Soy hablar"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a", "native": "vou (algo logo)",
                    "npc_reaction": "Voy a hablar. Lo que sale ahora.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Hora de dormir. Lucía mostra o quarto. Pequena conversa que termina com
    # Lucía sussurrando pra Miguel sobre María. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Doña Lucía", "Miguel"],
                "story": (
                    "Tarde da noite. Lucía levou você até um quartinho nos "
                    "fundos da casa — cama estreita, lamparina baixa, parede "
                    "de adobe. Cheiro de madeira velha. 'Aquí dormía mi "
                    "abuela hace años.'"
                ),
                "now": "Conversa de despedida pra noite.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🛏️ Quartinho dos fundos · Lamparina baixa · Lucía na porta",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Aquí vas a estar bien, hijo. Si necesitas algo — mi cuarto está en la otra punta. Miguel duerme cerca.",
                    "translation": "Aqui você vai estar bem, filho. Se precisar de algo — meu quarto fica no outro lado. Miguel dorme perto.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Você agradece formal pelo quarto:",
                    "options": [
                        {"id": "a", "text": "Gracias, Doña Lucía"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. Tú eres amigo de Miguel — eso es suficiente para mí.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Una pregunta antes de dormir — ¿cómo estás aquí, en esta casa, esta noche?",
                    "translation": "Uma pergunta antes de dormir — como você está aqui, nessa casa, essa noite?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Estado físico — você tá bem. Cama, comida, gente boa:",
                    "options": [
                        {"id": "a", "text": "Estoy bien"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Duerme tranquilo, hijo.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lucía vai sair. Antes de fechar a porta — para. Vira pra "
                        "você outra vez. Olha pra você fixo, como quem pesa "
                        "alguma coisa."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Hijo — ¿cómo se llama tu... amiga? La curandera. La que cuida.",
                    "translation": "Filho — como se chama tua... amiga? A curandera. A que cuida.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Lucía perguntou o nome de María. Você responde simples usando 'minha' amiga:",
                    "options": [
                        {"id": "a", "text": "Mi amiga se llama María"},
                        {"id": "b", "text": "Tu amiga se llama María"},
                        {"id": "c", "text": "Su amiga se llama María"},
                        {"id": "d", "text": "Voy a llamar"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi amiga", "native": "minha amiga",
                    "npc_reaction": "María. Mmm. ¿De dónde dijo que venía, hijo?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Você não sabe de onde María vem. Honesto:",
                    "options": [
                        {"id": "a", "text": "No sé, no me dijo"},
                        {"id": "b", "text": "Sí, soy"},
                        {"id": "c", "text": "Vamos a saber"},
                        {"id": "d", "text": "Tengo de saber"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_se", "target": "no sé", "native": "não sei",
                    "npc_reaction": "Mmm. No, claro que no te dijo. Duerme, hijo. Mañana hablamos.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F14 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🚪 Doña Lucía fecha a porta · Você na cama · Vela tremeluzindo",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você ouve passos no corredor. Lucía indo até a cozinha — "
                        "onde Miguel estava lavando louça."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Miguel — escúchame bien. A esa mujer la conozco de algún sitio. No recuerdo de dónde. Pero no es nueva en mi vida.",
                    "translation": "Miguel — me escuta bem. Essa mulher eu conheço de algum lugar. Não lembro de onde. Mas não é nova na minha vida.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Mamá — ¿estás segura?",
                    "translation": "Mãe — você tem certeza?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Estoy segura. Mañana voy a pensarlo. Hoy — déjala dormir. Pero no la pierdas de vista.",
                    "translation": "Tenho certeza. Amanhã vou pensar nisso. Hoje — deixa ela dormir. Mas não tira ela da vista.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você ouviu cada palavra através da parede fina. Miguel "
                        "não disse mais nada — só apagou a lamparina da cozinha "
                        "e foi pro próprio quarto.\n\n"
                        "Você fechou os olhos. Dormiu mal."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
