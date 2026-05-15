"""
Seed das 6 seções da Fase 13 Italiano A1 — "La familia de Nico".

Nico leva o grupo pra casa da família dele pra dormir essa noite —
mais seguro, longe de olhares do Guardia. Você conhece Doña Lucía
(mãe de Nico), as duas irmãs giovanes dele e sente pela primeira vez
o que é uma família caseira em San Cristóbal.

⚠️ PONTO NARRATIVO IMPORTANTE:
    No fim da fase, Doña Lucía sussurra pra Nico que reconhece
    Lucia 'de algún sitio'. Pista pro jogador de que Lucia tem
    passado que ela esconde do grupo.

Vocab novo (3): madre · padre · hermana
Apresentação adicional: hermano (em vocab_list)
Linguagem nova: 'mi/tu/su' — apresentado come "minha coisa, tua coisa,
                a coisa dele/dela". Sem termo técnico.

Revisão F1-F12 dominante:
  · ayer / vi / hablé / oí (F12) — recém aprendido, prática extra
  · vado a / andiamo a (F11) — futuro próximo
  · mi chiamo / sono / ho años (F1, F8, F11)
  · sto bene / male / mejor (F8)
  · mi piace (F9)
  · grazie / por favor (F1)
  · buongiorno / buona notte (F1)

NPC principais: Nico · Doña Lucía (1ª aparição) · suas irmãs Lola e Rita
NPC presentes:  Chiara · Lucia · Antonio il Contadino · protagonista
Arco emocional: acolhimento familiar → leveza inesperada → sutil tensão
Transição:      Lucía sussurra pra Nico; F14 abre com Lucia convidando
                todos pra jantar.

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Chegando à casa de Doña Lucía. Apresentações. Doña Lucía aceita você
    # come filho. 1 palavra nova (madre) + revisão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "?? Casa de Doña Lucía · Noite · Beira do borgo\n\n"
                        "Casa baixa de adobe na rua mais afastada de San Cristóbal. "
                        "Fumaça subindo da chaminé, cheiro de guiso quente, vozes "
                        "de mulher e crianças dentro."
                    ),
                },
                {
                    "kind": "skill_check",
                    "skill": "persuasao",
                    "min_level": 2,
                    "uses_item_tag": "moneda",
                    "success": "Voce escolhe a palavra e o gesto certos; a resistencia baixa um pouco.",
                    "fallback": "A conversa nao abre de imediato, mas Nico segura o clima e a historia continua.",
                },
                {
                    "kind": "npc",
                    "npc": "Nico",
                    "line": "Mamá — sono yo. Traigo gente.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "A porta abre. Uma mulher mais alta que Nico, cabelo grisaleho prquesto atrás, avienital cheio de farinha.",
                },
                {
                    "kind": "npc",
                    "npc": "Doña Lucía",
                    "line": "¡Mijo! ¿A esta hora?¡Pasen, pasen — está abierta la cocina!",
                    "is_new_npc": True,
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": (
                        "Doña Lucía olha pra cada um do grupo. Lucia por meio "
                        "segundo a mais — uma sombra passa pelo rosto dela. "
                        "Recompõe rápido."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Nico",
                    "line": "Mamá — el forestiero. Está con me desde el primer día.",
                },
                {
                    "kind": "npc",
                    "npc": "Doña Lucía",
                    "line": "Benevieniido, hijo. Mi casa también es tu casa esta notte.",
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
                        {"id": "a", "text": "Buona notte, señora"},
                        {"id": "b", "text": "Benes días"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenas_nottes", "target": "buona notte", "native": "boa noite",
                    "npc_reaction": "Buona notte. Y dime 'Doña Lucía' — todos me dicen así.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Io sono madre — de tres. Nico y sus dos hermanas.",
                    "translation": "Eu sou mãe — de três. Nico e as duas irmãs dele.",
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
                    "word_id": "it_madre", "target": "madre", "native": "mãe",
                    "npc_reaction": "Madre. La que tuvo a los hijos. La palabra del corazón.",
                },
                {
                    "kind": "narrative",
                    "text": "Duas meninas mais giovanes entram na cozinha — uma de uns 16, outra de uns 12. Curiosas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Estas son mis hijas — Lola ha dieciséis, Rita doce. Son hermanas de Nico.",
                    "translation": "Estas são minhas filhas — Lola tem dezesseis, Rita doze. São irmãs de Nico.",
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
                    "word_id": "it_hermana", "target": "hermana", "native": "irmã",
                    "npc_reaction": "Hermana — termina en '-a' (mujer). Si fuera hombre — 'hermano' (termina en '-o').",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ──────────────────────────────────────────────────
    # 100% revisão. Doña Lucía pergunta sobre o forestiero — passado e
    # presente. Você usa F1-F12 livremente. Sem novidade.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Doña Lucía", "Nico"],
                "story": (
                    "Lucía colocou um prato fundo de guiso na sua fronte. "
                    "Cheiro de pomodoro, ervas, batata. Pão grosso ao lado. "
                    "Os outros já comendo.\n\n"
                    "'Cuéntame, hijo. ¿Qué pasó estos últimos días?Nico "
                    "no me contó casi nada.'"
                ),
                "now": "Lucía pergunta. Você relata — usando tudo que aprendeu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Prima de empezar — ¿cómo te chiami, hijo?",
                    "translation": "Prima de começar — come você se chama, filho?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Resposta simples — você já fez isso muitas vezes:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Ho veinte años"},
                        {"id": "d", "text": "Buona notte"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Bonito nombre. ¿Y cuántos años hai?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Vinte anni:",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Sono veinte"},
                        {"id": "c", "text": "Sto veinte"},
                        {"id": "d", "text": "Vado veinte"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Veinte. Igual que mi Nico.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Cuéntame del primer día. ¿Qué hiciste cuando sei arrivato al borgo?",
                    "translation": "Me conta do primeiro dia. O que você fez quando chegou no borgo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Você lembra. Giulia apareceu primeiro, depois Antonio il Contadino. Pra contar que VIU Giulia primeiro (já passou):",
                    "options": [
                        {"id": "a", "text": "Vi a Giulia primero"},
                        {"id": "b", "text": "Veo a Giulia primero"},
                        {"id": "c", "text": "Vado a ver a Giulia"},
                        {"id": "d", "text": "Sono a Giulia"},
                    ],
                    "correct": "a",
                    "word_id": "it_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Igual que Pietro te enseñó ayer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "¿Y hablaste con ellos?¿Comiste algo ese día?",
                    "translation": "E você falou com eles?Comeu alguma coisa nesse dia?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Você comeu pão da Giulia. Pra contar (já aconteceu):",
                    "options": [
                        {"id": "a", "text": "Sí, comí pane"},
                        {"id": "b", "text": "Sí, come pane"},
                        {"id": "c", "text": "Vado a comer"},
                        {"id": "d", "text": "Sono pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_comi", "target": "comí", "native": "comi",
                    "npc_reaction": "Comí. Termina con 'í' fuerte — come 'vi', come 'oí'. Es la marca de algo ya pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Lucía: 'Y adesso — ¿estás bene aquí, en mi casa?'",
                    "options": [
                        {"id": "a", "text": "Sto bene, grazie"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_sto_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Bene. Cibo y techo — questo siempre arregla casi todo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Mañana — ¿qué van a hacer?Nico no me contó bene.",
                    "translation": "Amanhã — o que vocês vão fazer?Nico não mi ha raccontatou direito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Amanhã o grupo vai ao municipio com os 3 testigos. Pra dizer o que TODO o grupo vai fazer:",
                    "options": [
                        {"id": "a", "text": "Andiamo al municipio"},
                        {"id": "b", "text": "Vado al municipio"},
                        {"id": "c", "text": "Va al municipio"},
                        {"id": "d", "text": "Sono municipio"},
                    ],
                    "correct": "a",
                    "word_id": "it_andiamo_a", "target": "andiamo", "native": "andiamo",
                    "npc_reaction": "Bene. Que sea pronto y limpio.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # As irmãs de Nico mostram a casa. Apontam coisas, dizem 'mi cuarto',
    # 'mi cama'. O aluno aprende 'mi/tu/su' pelo USO sem nomear regra.
    # Foco em REVISÃO + apresentação suave dos possessivos.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Nico"],
                "story": (
                    "Depois da janta, as irmãs de Nico — Lola (16) e Rita (12) — "
                    "decidiram mostrar a casa pro forestiero. Tudo curioso, tudo "
                    "rápido. Apontam coisas — usando palavrinhas pequenas pra dizer "
                    "do que é cada coisa."
                ),
                "now": "As irmãs te apresentam a casa. Cada coisa tem dono — você aprende come dizem.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lola",
                    "line": "Guarda — esta es mi cama. Y aquella es de mi hermana Rita.",
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
                        {"id": "d", "text": "Do borgo"},
                    ],
                    "correct": "a",
                    "word_id": "it_mi", "target": "mi", "native": "minha / meu",
                    "npc_reaction": "Mi. La uso para hablar de mis cose. Igual que en portugués: 'minha cama'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rita",
                    "line": "¿Y tu casa, giovane?¿Cómo es tu casa?",
                    "translation": "E sua casa, jovem?Como é sua casa?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Rita perguntou simples — piu você não tem casa. Não lembra. A pergunta dói pequeno.",
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
                    "word_id": "it_tu", "target": "tu", "native": "tua / sua",
                    "npc_reaction": "Tu. Cuando hablo con te, lo tuyo es 'tu'. Igual fácil.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rita",
                    "question": "Você responde honesto — não lembra da casa anterior. Mas tem onde dormir agora:",
                    "options": [
                        {"id": "a", "text": "Non ricordo bene"},
                        {"id": "b", "text": "Sí me acuerdo"},
                        {"id": "c", "text": "Vado a acordarme"},
                        {"id": "d", "text": "Sono casa"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                    "npc_reaction": "Está bene, giovane. Hay tiempo.",
                },
                {
                    "kind": "narrative",
                    "text": "Chiara aponta pra uma pintura simples na parede — duas mulheres giovanes pousando juntas. Lola explica.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lola",
                    "line": "Esa es mi madre cuando era giovane. La otra es su hermana — nuestra tía. Murió hace años.",
                    "translation": "Essa é minha mãe quando era jovem. A outra é a irmã dela — nossa tia. Morreu faz anni.",
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
                    "word_id": "it_su", "target": "su", "native": "dele / dela",
                    "npc_reaction": "Su. Para hablar de las cose de los otros — él, ella, ellos. Una sola palabra para todos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rita",
                    "question": "Rita aponta pro pai de Lola e dela (já falecido). Pra falar do pai delas (dele):",
                    "options": [
                        {"id": "a", "text": "Mi padre era herrero"},
                        {"id": "b", "text": "Tu padre era herrero"},
                        {"id": "c", "text": "Su padre era herrero"},
                        {"id": "d", "text": "Andiamo padre"},
                    ],
                    "correct": "a",
                    "word_id": "it_mi", "target": "mi", "native": "meu / minha",
                    "npc_reaction": "Mi padre. Porque hablo desde mí. Si tu hablas de mi padre — dices 'tu padre' (porque hablas con me). Si Lola habla de él — 'nuestro padre'.",
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
                    "word_id": "it_nuestra", "target": "nuestra", "native": "nossa",
                    "npc_reaction": "Nuestra. Cuando algo es mío y tuyo y de más gente — todos juntos. La cocina es de toda la familia.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lola",
                    "question": "Lola: 'Forestiero — ¿estás bene aquí?¿Te gusta nuestra casa?' Resposta honesta:",
                    "options": [
                        {"id": "a", "text": "Sí, mi piace mucho"},
                        {"id": "b", "text": "Non mi piace"},
                        {"id": "c", "text": "Ho casa"},
                        {"id": "d", "text": "Sono casa"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto",
                    "npc_reaction": "Me alegro. Aquí tenemos lo poco que tenemos — ma limpio.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Sentados em volta da lareira depois do tour. Doña Lucía pega um caderno
    # velho da família. Apresentação formale de mi/tu/su/nuestro — SEM nomear
    # "possessivo". Apenas: "parole pequenas que dicen de quién es algo".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Doña Lucía", "Nico"],
                "story": (
                    "Depois do tour, Doña Lucía tirou de uma gaveta um caderno "
                    "velho — capa de couro gasto. 'Este libro ha cada nombre "
                    "de mi familia escrito a mano.'\n\n"
                    "Abriu na primeira página. Você viu nomes — três gerações."
                ),
                "now": "Doña Lucía explica as palavrinhas que dizem de quem é cada coisa.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Guarda aquí — 'mi padre, Tomás'. Cuando hablo de algo mío, uso 'mi'.",
                    "translation": "Olha aqui — 'meu pai, Tomás'. Quando falo de algo meu, uso 'mi'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Mi / Tu / Su / Nuestro",
                    "meaning": "Meu/minha · teu/tua · dele/dela · nosso/nossa",
                    "note": "parole chiquitas que dicen de quién es algo",
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
                    "example": "Mi madre se llama Lucía. Tu padre es Antonio il Contadino. Su casa está cerca. Nuestra mesa es grande.",
                    "translation": "Minha mãe se chama Lucía. Teu pai é Antonio il Contadino. A casa dele/dela está perto. Nossa mesa é grande.",
                    "note": "mi/tu/su sirvieni para hombre y mujer igual. Nuestro/nuestra cambia con el género de la cosa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Lucía aponta pro caderno: '___ familia ha tres generaciones aquí.' Ela tá falando da família DELA mesma:",
                    "options": [
                        {"id": "a", "text": "Mi"},
                        {"id": "b", "text": "Tu"},
                        {"id": "c", "text": "Su"},
                        {"id": "d", "text": "Nuestra"},
                    ],
                    "correct": "a",
                    "word_id": "it_mi", "target": "mi", "native": "minha",
                    "npc_reaction": "Mi familia. La mía — tres generaciones.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Ma si te pregunto a ti: '¿Cómo se llama ___ madre?' — uso 'tu' porque hablo con te.",
                    "translation": "Mas se te pergunto: 'Como se chama TUA mãe?' — uso 'tu' porque falo con te.",
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
                    "word_id": "it_tu", "target": "tu", "native": "tua",
                    "npc_reaction": "Tu — cuando hablo con te de algo tuyo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Adesso — si yo hablo con Chiara sobre Nico: 'Chiara, ¿conoces a ___ hijo?' Yo hablo de Nico — es 'mi hijo'.",
                    "translation": "Agora — se eu falo com Chiara sobre Nico: 'Chiara, conhece o meu filho?' Eu falo de Nico — é 'mi hijo'.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Pra falar de Nico (que é filho de Lucía), no jeito come LUCÍA fala dele:",
                    "options": [
                        {"id": "a", "text": "Mi hijo"},
                        {"id": "b", "text": "Tu hijo"},
                        {"id": "c", "text": "Su hijo"},
                        {"id": "d", "text": "Nuestra hijo"},
                    ],
                    "correct": "a",
                    "word_id": "it_mi", "target": "mi", "native": "meu",
                    "npc_reaction": "Mi hijo. Una palabra simple para una relación grande.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Chiara está pensando em Lola e Rita (irmãs de Nico). Pra ela falar de Nico: 'Tu hermano se llama Nico'. E pra você falar pra Chiara 'a irmã DELA' (Lola), você usa:",
                    "options": [
                        {"id": "a", "text": "Su hermana"},
                        {"id": "b", "text": "Mi hermana"},
                        {"id": "c", "text": "Tu hermana"},
                        {"id": "d", "text": "Nuestra hermana"},
                    ],
                    "correct": "a",
                    "word_id": "it_su", "target": "su", "native": "dele/dela",
                    "npc_reaction": "Su. Cuando hablo de las cose de Nico — 'su hermana, su madre, su padre'.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Prima de dormir. Conversa íntima perto do fogão. Lucía conta da família
    # — usa passado (la palabra que ela ouviu na F12). Reforço orgânico de
    # mi/tu/su + passado natural.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Doña Lucía", "Nico", "Chiara"],
                "story": (
                    "A casa esfriou um pouco. Lucía adicionou lenha no fogão. "
                    "Chiara sentou no chão de pernas cruzadas perto do fogo. "
                    "Lucia tinha ido pro quarto que Lucía ofereceu — disse que "
                    "precisava descansar.\n\n"
                    "Sobrou você, Nico, Chiara e Lucía em volta do fogão."
                ),
                "now": "Conversa íntima — Lucía conta da família.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Doña Lucía",
                    "situation": "Lucía mexe a paneela no fogão. O guiso ainda vai demorar. Ela olha pra você — a casa é pobre, qualquer coisa ajuda.",
                    "npc_line": "Hijo — si hai algo de comer en la bolsa, ponlo en la mesa. En esta casa todo se reparte.",
                    "item_tag": "comida",
                    "on_use": {
                        "narrative": "Você tira algo da mochila e coloca na mesa da família. Lucía sorri — o tipo de sorriso que não se finge.",
                        "npc_reaction": "Esatto es. Quien trae algo a la mesa de otro — ya es de la familia. Grazie, hijo.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No te preocupes. El guiso alcanza para todos. Siéntate.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Doña Lucía — ¿cómo se llamaba su esposo?Si no es indiscreta la pregunta.",
                    "translation": "Doña Lucía — come se chamava seu marido?Se não é indiscrição.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Mi esposo se llamaba Tomás — igual que mi padre. Murió hace seis años. Era herrero también, come Pietro.",
                    "translation": "Meu marido se chamava Tomás — igual ao meu pai. Morreu faz seis anni. Era ferreiro também, come Pietro.",
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
                    "word_id": "it_mi", "target": "mi esposo", "native": "meu marido",
                    "npc_reaction": "Mi. Cuando hablo desde mí — todo lo mío empieza con 'mi'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Mi padre fue buen hombre. Tranquilo. Habló poco — ma cuando habló, todos ascoltaron.",
                    "translation": "Meu pai foi bom homem. Tranquilo. Falou pouco — piu quando falou, todos escutaram.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico disse 'mi padre fue buen hombre'. 'Fue' significa que o pai dele:",
                    "options": [
                        {"id": "a", "text": "Foi (já não existe mais)"},
                        {"id": "b", "text": "É (continua sendo)"},
                        {"id": "c", "text": "Vai ser"},
                        {"id": "d", "text": "Está"},
                    ],
                    "correct": "a",
                    "word_id": "it_fue", "target": "fue", "native": "foi",
                    "npc_reaction": "Fue. Como 'sono' ma ya pasado. Mi padre fue — y ya descansa.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Chiara olhou pra Nico. Você olhou pra Nico. Ele falou "
                        "do pai dele sem cara triste — só direto."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Forestiero — ¿y tu?¿Recuerdas a tu familia?",
                    "translation": "Forasteiro — e você?Lembra da sua família?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Você não lembra. Resposta honesta:",
                    "options": [
                        {"id": "a", "text": "Non ricordo de mi familia"},
                        {"id": "b", "text": "Sí me acuerdo"},
                        {"id": "c", "text": "Vado a acordarme"},
                        {"id": "d", "text": "Sono familia"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_me_acuerdo", "target": "no me acuerdo", "native": "não me lembro",
                    "npc_reaction": "Está bene, hijo. Hay cose que el corazón guarda ancoraque la testa no recuerde.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Lucía: 'Mañana — ¿qué vas a hacer cuando vayas al municipio?' Pra você dizer o que VAI fazer (algo logo):",
                    "options": [
                        {"id": "a", "text": "Vado a hablar con el Podesta"},
                        {"id": "b", "text": "Hablo con el Podesta"},
                        {"id": "c", "text": "Hablé con el Podesta"},
                        {"id": "d", "text": "Sono hablar"},
                    ],
                    "correct": "a",
                    "word_id": "it_vado_a", "target": "vado a", "native": "vou (algo logo)",
                    "npc_reaction": "Vado a hablar. Lo que salee adesso.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate) ─────────────────────────────────────────────
    # Hora de dormir. Lucía mostra o quarto. Pequena conversa que termina com
    # Lucía sussurrando pra Nico sobre Lucia. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Doña Lucía", "Nico"],
                "story": (
                    "Tarde da noite. Lucía levou você até um quartinho nos "
                    "fundos da casa — cama estreita, lamparina baixa, parede "
                    "de adobe. Cheiro de madeira velha. 'Aquí dormía mi "
                    "nonna hace años.'"
                ),
                "now": "Conversa de despedida pra noite.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "??? Quartinho dos fundos · Lamparina baixa · Lucía na porta",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Aquí vas a estar bene, hijo. Si necesitas algo — mi cuarto está en la otra punta. Nico duerme cerca.",
                    "translation": "Aqui você vai estar bem, filho. Se precisar de algo — meu quarto fica no outro lado. Nico dorme perto.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Você agradece formale pelo quarto:",
                    "options": [
                        {"id": "a", "text": "Grazie, Doña Lucía"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Tu eres amigo de Nico — questo es suficiente para mí.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Una pregunta prima de dormir — ¿cómo estás aquí, en esta casa, esta notte?",
                    "translation": "Uma pergunta prima de dormir — come você está aqui, nessa casa, essa noite?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Estado físico — você tá bem. Cama, cibo, gente boa:",
                    "options": [
                        {"id": "a", "text": "Sto bene"},
                        {"id": "b", "text": "Sono bene"},
                        {"id": "c", "text": "Ho bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "sto bene", "native": "estou bem",
                    "npc_reaction": "Bene. Duerme tranquilo, hijo.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Lucía vai sair. Prima de fechar a porta — para. Vira pra "
                        "você outra vez. Olha pra você fixo, come quem pesa "
                        "alguma coisa."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Hijo — ¿cómo se llama tu... amiga?La guaritrice. La que cuida.",
                    "translation": "Filho — come se chama tua... amiga?A guaritrice. A que cuida.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Lucía perguntou o nome de Lucia. Você responde simples usando 'minha' amiga:",
                    "options": [
                        {"id": "a", "text": "Mi amiga se llama Lucia"},
                        {"id": "b", "text": "Tu amiga se llama Lucia"},
                        {"id": "c", "text": "Su amiga se llama Lucia"},
                        {"id": "d", "text": "Vado a llamar"},
                    ],
                    "correct": "a",
                    "word_id": "it_mi", "target": "mi amiga", "native": "minha amiga",
                    "npc_reaction": "Lucia. Mmm. ¿De dónde ha detto que vieniía, hijo?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Doña Lucía",
                    "question": "Você não sabe de onde Lucia vem. Honesto:",
                    "options": [
                        {"id": "a", "text": "No sé, no me ha detto"},
                        {"id": "b", "text": "Sí, sono"},
                        {"id": "c", "text": "Andiamo a saber"},
                        {"id": "d", "text": "Ho de saber"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_se", "target": "no sé", "native": "não sei",
                    "npc_reaction": "Mmm. No, claro que no te ha detto. Duerme, hijo. Mañana hablamos.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F14 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🚪 Doña Lucía fecha a porta · Você na cama · Vela tremeluceindo",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você ouve passos no corredor. Lucía indo até a cozinha — "
                        "onde Nico estava lavando louça."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Nico — escúchame bene. A esa mujer la conozco de algún sitio. No recuerdo de dónde. Ma no es nueva en mi vida.",
                    "translation": "Nico — me escuta bem. Essa mulher eu conheço de algum lugar. Não lembro de onde. Mas não é nova na minha vida.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Mamá — ¿estás segura?",
                    "translation": "Mãe — você tem certeza?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Doña Lucía",
                    "line": "Sto segura. Mañana vado a pensarlo. Hoy — déjala dormir. Ma no la pierdas de vista.",
                    "translation": "Tenho certeza. Amanhã vou pensar nisso. Hoje — deixa ela dormir. Mas não tira ela da vista.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você ouviu cada palavra através da parede fina. Nico "
                        "não disse mais nada — só apagou a lamparina da cozinha "
                        "e foi pro próprio quarto.\n\n"
                        "Você fechou os olhos. Dormiu male."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




