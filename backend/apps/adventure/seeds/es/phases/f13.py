"""
Seed das 6 seÃ§Ãµes da Fase 13 Espanhol A1 â€” "La familia de Miguel".

Miguel leva o grupo pra casa da famÃ­lia dele pra dormir essa noite â€”
mais seguro, longe de olhares do Vigilante. VocÃª conhece DoÃ±a LucÃ­a
(mÃ£e de Miguel), as duas irmÃ£s jovens dele e sente pela primeira vez
o que Ã© uma famÃ­lia caseira em San CristÃ³bal.

âš ï¸ PONTO NARRATIVO IMPORTANTE:
    No fim da fase, DoÃ±a LucÃ­a sussurra pra Miguel que reconhece
    MarÃ­a 'de algÃºn sitio'. Pista pro jogador de que MarÃ­a tem
    passado que ela esconde do grupo.

Vocab novo (3): madre Â· padre Â· hermana
ApresentaÃ§Ã£o adicional: hermano (em vocab_list)
Linguagem nova: 'mi/tu/su' â€” apresentado como "minha coisa, tua coisa,
                a coisa dele/dela". Sem termo tÃ©cnico.

RevisÃ£o F1-F12 dominante:
  Â· ayer / vi / hablÃ© / oÃ­ (F12) â€” recÃ©m aprendido, prÃ¡tica extra
  Â· voy a / vamos a (F11) â€” futuro prÃ³ximo
  Â· me llamo / soy / tengo aÃ±os (F1, F8, F11)
  Â· estoy bien / mal / mejor (F8)
  Â· me gusta (F9)
  Â· gracias / por favor (F1)
  Â· buenos dÃ­as / buenas noches (F1)

NPC principais: Miguel Â· DoÃ±a LucÃ­a (1Âª apariÃ§Ã£o) Â· suas irmÃ£s Lola e Rita
NPC presentes:  SofÃ­a Â· MarÃ­a Â· Don Miguel Â· protagonista
Arco emocional: acolhimento familiar â†’ leveza inesperada â†’ sutil tensÃ£o
TransiÃ§Ã£o:      LucÃ­a sussurra pra Miguel; F14 abre com MarÃ­a convidando
                todos pra jantar.

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f13_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Chegando Ã  casa de DoÃ±a LucÃ­a. ApresentaÃ§Ãµes. DoÃ±a LucÃ­a aceita vocÃª
    # como filho. 1 palavra nova (madre) + revisÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "ðŸ¡ Casa de DoÃ±a LucÃ­a Â· Noite Â· Beira do pueblo\n\n"
                        "Casa baixa de adobe na rua mais afastada de San CristÃ³bal. "
                        "FumaÃ§a subindo da chaminÃ©, cheiro de guiso quente, vozes "
                        "de mulher e crianÃ§as dentro."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "MamÃ¡ â€” soy yo. Traigo gente.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "A porta abre. Uma mulher mais alta que Miguel, cabelo grisalho preso atrÃ¡s, avental cheio de farinha.",
                },
                {
                    "kind": "npc",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Â¡Mijo! Â¿A esta hora? Â¡Pasen, pasen â€” estÃ¡ abierta la cocina!",
                    "is_new_npc": True,
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": (
                        "DoÃ±a LucÃ­a olha pra cada um do grupo. MarÃ­a por meio "
                        "segundo a mais â€” uma sombra passa pelo rosto dela. "
                        "RecompÃµe rÃ¡pido."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "MamÃ¡ â€” el forastero. EstÃ¡ conmigo desde el primer dÃ­a.",
                },
                {
                    "kind": "npc",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Bienvenido, hijo. Mi casa tambiÃ©n es tu casa esta noche.",
                    "pace": "slow",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "madre",   "native": "mÃ£e"},
                        {"target": "padre",   "native": "pai"},
                        {"target": "hermana", "native": "irmÃ£"},
                        {"target": "hermano", "native": "irmÃ£o"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "Sol jÃ¡ se pÃ´s. DoÃ±a LucÃ­a te recebe. VocÃª cumprimenta com respeito:",
                    "options": [
                        {"id": "a", "text": "Buenas noches, seÃ±ora"},
                        {"id": "b", "text": "Buenos dÃ­as"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                    "npc_reaction": "Buenas noches. Y dime 'DoÃ±a LucÃ­a' â€” todos me dicen asÃ­.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Yo soy madre â€” de tres. Miguel y sus dos hermanas.",
                    "translation": "Eu sou mÃ£e â€” de trÃªs. Miguel e as duas irmÃ£s dele.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "DoÃ±a LucÃ­a falou 'madre'. A palavra significa:",
                    "options": [
                        {"id": "a", "text": "MÃ£e"},
                        {"id": "b", "text": "IrmÃ£"},
                        {"id": "c", "text": "Filha"},
                        {"id": "d", "text": "Vizinha"},
                    ],
                    "correct": "a",
                    "word_id": "es_madre", "target": "madre", "native": "mÃ£e",
                    "npc_reaction": "Madre. La que tuvo a los hijos. La palabra del corazÃ³n.",
                },
                {
                    "kind": "narrative",
                    "text": "Duas meninas mais jovens entram na cozinha â€” uma de uns 16, outra de uns 12. Curiosas.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Estas son mis hijas â€” Lola tiene diecisÃ©is, Rita doce. Son hermanas de Miguel.",
                    "translation": "Estas sÃ£o minhas filhas â€” Lola tem dezesseis, Rita doze. SÃ£o irmÃ£s de Miguel.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "Lola e Rita sÃ£o meninas. A palavra pra menina da mesma famÃ­lia Ã©:",
                    "options": [
                        {"id": "a", "text": "Hermana"},
                        {"id": "b", "text": "Hermano"},
                        {"id": "c", "text": "Madre"},
                        {"id": "d", "text": "Padre"},
                    ],
                    "correct": "a",
                    "word_id": "es_hermana", "target": "hermana", "native": "irmÃ£",
                    "npc_reaction": "Hermana â€” termina en '-a' (mujer). Si fuera hombre â€” 'hermano' (termina en '-o').",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # 100% revisÃ£o. DoÃ±a LucÃ­a pergunta sobre o forastero â€” passado e
    # presente. VocÃª usa F1-F12 livremente. Sem novidade.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["DoÃ±a LucÃ­a", "Miguel"],
                "story": (
                    "LucÃ­a colocou um prato fundo de guiso na sua frente. "
                    "Cheiro de tomate, ervas, batata. PÃ£o grosso ao lado. "
                    "Os outros jÃ¡ comendo.\n\n"
                    "'CuÃ©ntame, hijo. Â¿QuÃ© pasÃ³ estos Ãºltimos dÃ­as? Miguel "
                    "no me contÃ³ casi nada.'"
                ),
                "now": "LucÃ­a pergunta. VocÃª relata â€” usando tudo que aprendeu.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Antes de empezar â€” Â¿cÃ³mo te llamas, hijo?",
                    "translation": "Antes de comeÃ§ar â€” como vocÃª se chama, filho?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "Resposta simples â€” vocÃª jÃ¡ fez isso muitas vezes:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy forastero"},
                        {"id": "c", "text": "Tengo veinte aÃ±os"},
                        {"id": "d", "text": "Buenas noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Bonito nombre. Â¿Y cuÃ¡ntos aÃ±os tienes?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "Vinte anos:",
                    "options": [
                        {"id": "a", "text": "Tengo veinte aÃ±os"},
                        {"id": "b", "text": "Soy veinte"},
                        {"id": "c", "text": "Estoy veinte"},
                        {"id": "d", "text": "Voy veinte"},
                    ],
                    "correct": "a",
                    "word_id": "es_tengo_anos", "target": "tengo veinte aÃ±os", "native": "tenho vinte anos",
                    "npc_reaction": "Veinte. Igual que mi Miguel.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "CuÃ©ntame del primer dÃ­a. Â¿QuÃ© hiciste cuando llegaste al pueblo?",
                    "translation": "Me conta do primeiro dia. O que vocÃª fez quando chegou no pueblo?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "VocÃª lembra. Rosa apareceu primeiro, depois Don Miguel. Pra contar que VIU Rosa primeiro (jÃ¡ passou):",
                    "options": [
                        {"id": "a", "text": "Vi a Rosa primero"},
                        {"id": "b", "text": "Veo a Rosa primero"},
                        {"id": "c", "text": "Voy a ver a Rosa"},
                        {"id": "d", "text": "Soy a Rosa"},
                    ],
                    "correct": "a",
                    "word_id": "es_vi", "target": "vi", "native": "vi",
                    "npc_reaction": "Vi. Igual que Eduardo te enseÃ±Ã³ ayer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Â¿Y hablaste con ellos? Â¿Comiste algo ese dÃ­a?",
                    "translation": "E vocÃª falou com eles? Comeu alguma coisa nesse dia?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "VocÃª comeu pÃ£o da Rosa. Pra contar (jÃ¡ aconteceu):",
                    "options": [
                        {"id": "a", "text": "SÃ­, comÃ­ pan"},
                        {"id": "b", "text": "SÃ­, como pan"},
                        {"id": "c", "text": "Voy a comer"},
                        {"id": "d", "text": "Soy pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_comi", "target": "comÃ­", "native": "comi",
                    "npc_reaction": "ComÃ­. Termina con 'Ã­' fuerte â€” como 'vi', como 'oÃ­'. Es la marca de algo ya pasado.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "LucÃ­a: 'Y ahora â€” Â¿estÃ¡s bien aquÃ­, en mi casa?'",
                    "options": [
                        {"id": "a", "text": "Estoy bien, gracias"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_estoy_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Comida y techo â€” eso siempre arregla casi todo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "MaÃ±ana â€” Â¿quÃ© van a hacer? Miguel no me contÃ³ bien.",
                    "translation": "AmanhÃ£ â€” o que vocÃªs vÃ£o fazer? Miguel nÃ£o me contou direito.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "AmanhÃ£ o grupo vai ao ayuntamiento com os 3 testigos. Pra dizer o que TODO o grupo vai fazer:",
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

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # As irmÃ£s de Miguel mostram a casa. Apontam coisas, dizem 'mi cuarto',
    # 'mi cama'. O aluno aprende 'mi/tu/su' pelo USO sem nomear regra.
    # Foco em REVISÃƒO + apresentaÃ§Ã£o suave dos possessivos.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Miguel"],
                "story": (
                    "Depois da janta, as irmÃ£s de Miguel â€” Lola (16) e Rita (12) â€” "
                    "decidiram mostrar a casa pro forastero. Tudo curioso, tudo "
                    "rÃ¡pido. Apontam coisas â€” usando palavrinhas pequenas pra dizer "
                    "do que Ã© cada coisa."
                ),
                "now": "As irmÃ£s te apresentam a casa. Cada coisa tem dono â€” vocÃª aprende como dizem.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lola",
                    "line": "Mira â€” esta es mi cama. Y aquella es de mi hermana Rita.",
                    "translation": "Olha â€” essa Ã© minha cama. E aquela Ã© da minha irmÃ£ Rita.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lola",
                    "question": "Lola disse 'mi cama' apontando pra cama dela. A palavrinha 'mi' significa:",
                    "options": [
                        {"id": "a", "text": "Da Lola (minha, dela mesma falando)"},
                        {"id": "b", "text": "De outra pessoa"},
                        {"id": "c", "text": "De ninguÃ©m"},
                        {"id": "d", "text": "Do pueblo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi", "native": "minha / meu",
                    "npc_reaction": "Mi. La uso para hablar de mis cosas. Igual que en portuguÃ©s: 'minha cama'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rita",
                    "line": "Â¿Y tu casa, joven? Â¿CÃ³mo es tu casa?",
                    "translation": "E sua casa, jovem? Como Ã© sua casa?",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Rita perguntou simples â€” mas vocÃª nÃ£o tem casa. NÃ£o lembra. A pergunta dÃ³i pequeno.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rita",
                    "question": "Rita perguntou usando 'tu casa'. A palavrinha 'tu' significa:",
                    "options": [
                        {"id": "a", "text": "Tua / sua (de quem ela estÃ¡ falando)"},
                        {"id": "b", "text": "Minha"},
                        {"id": "c", "text": "Dele/dela"},
                        {"id": "d", "text": "Nossa"},
                    ],
                    "correct": "a",
                    "word_id": "es_tu", "target": "tu", "native": "tua / sua",
                    "npc_reaction": "Tu. Cuando hablo contigo, lo tuyo es 'tu'. Igual fÃ¡cil.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rita",
                    "question": "VocÃª responde honesto â€” nÃ£o lembra da casa anterior. Mas tem onde dormir agora:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo bien"},
                        {"id": "b", "text": "SÃ­ me acuerdo"},
                        {"id": "c", "text": "Voy a acordarme"},
                        {"id": "d", "text": "Soy casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "nÃ£o me lembro",
                    "npc_reaction": "EstÃ¡ bien, joven. Hay tiempo.",
                },
                {
                    "kind": "narrative",
                    "text": "SofÃ­a aponta pra uma pintura simples na parede â€” duas mulheres jovens pousando juntas. Lola explica.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lola",
                    "line": "Esa es mi madre cuando era joven. La otra es su hermana â€” nuestra tÃ­a. MuriÃ³ hace aÃ±os.",
                    "translation": "Essa Ã© minha mÃ£e quando era jovem. A outra Ã© a irmÃ£ dela â€” nossa tia. Morreu faz anos.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lola",
                    "question": "Lola disse 'su hermana' â€” falando de uma terceira pessoa (sua mÃ£e, DoÃ±a LucÃ­a). A palavrinha 'su' significa:",
                    "options": [
                        {"id": "a", "text": "Dele / dela / deles (de outra pessoa)"},
                        {"id": "b", "text": "Minha"},
                        {"id": "c", "text": "Tua"},
                        {"id": "d", "text": "Nossa"},
                    ],
                    "correct": "a",
                    "word_id": "es_su", "target": "su", "native": "dele / dela",
                    "npc_reaction": "Su. Para hablar de las cosas de los otros â€” Ã©l, ella, ellos. Una sola palabra para todos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rita",
                    "question": "Rita aponta pro pai de Lola e dela (jÃ¡ falecido). Pra falar do pai delas (dele):",
                    "options": [
                        {"id": "a", "text": "Mi padre era herrero"},
                        {"id": "b", "text": "Tu padre era herrero"},
                        {"id": "c", "text": "Su padre era herrero"},
                        {"id": "d", "text": "Vamos padre"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi", "native": "meu / minha",
                    "npc_reaction": "Mi padre. Porque hablo desde mÃ­. Si tÃº hablas de mi padre â€” dices 'tu padre' (porque hablas conmigo). Si Lola habla de Ã©l â€” 'nuestro padre'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lola",
                    "line": "Y nuestra cocina es la pequeÃ±a ahÃ­ abajo. AllÃ­ come toda la familia.",
                    "translation": "E nossa cozinha Ã© a pequena ali embaixo. Ali come a famÃ­lia toda.",
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
                    "npc_reaction": "Nuestra. Cuando algo es mÃ­o y tuyo y de mÃ¡s gente â€” todos juntos. La cocina es de toda la familia.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lola",
                    "question": "Lola: 'Forastero â€” Â¿estÃ¡s bien aquÃ­? Â¿Te gusta nuestra casa?' Resposta honesta:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me gusta mucho"},
                        {"id": "b", "text": "No me gusta"},
                        {"id": "c", "text": "Tengo casa"},
                        {"id": "d", "text": "Soy casa"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Me alegro. AquÃ­ tenemos lo poco que tenemos â€” pero limpio.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Sentados em volta da lareira depois do tour. DoÃ±a LucÃ­a pega um caderno
    # velho da famÃ­lia. ApresentaÃ§Ã£o formal de mi/tu/su/nuestro â€” SEM nomear
    # "possessivo". Apenas: "palabras pequenas que dicen de quiÃ©n es algo".
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["DoÃ±a LucÃ­a", "Miguel"],
                "story": (
                    "Depois do tour, DoÃ±a LucÃ­a tirou de uma gaveta um caderno "
                    "velho â€” capa de couro gasto. 'Este libro tiene cada nombre "
                    "de mi familia escrito a mano.'\n\n"
                    "Abriu na primeira pÃ¡gina. VocÃª viu nomes â€” trÃªs geraÃ§Ãµes."
                ),
                "now": "DoÃ±a LucÃ­a explica as palavrinhas que dizem de quem Ã© cada coisa.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Mira aquÃ­ â€” 'mi padre, TomÃ¡s'. Cuando hablo de algo mÃ­o, uso 'mi'.",
                    "translation": "Olha aqui â€” 'meu pai, TomÃ¡s'. Quando falo de algo meu, uso 'mi'.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Mi / Tu / Su / Nuestro",
                    "meaning": "Meu/minha Â· teu/tua Â· dele/dela Â· nosso/nossa",
                    "note": "palabras chiquitas que dicen de quiÃ©n es algo",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Mi madre",  "isKey": True},
                        {"text": " Â· ",       "isKey": False},
                        {"text": "Tu padre",  "isKey": True},
                        {"text": " Â· ",       "isKey": False},
                        {"text": "Su casa",   "isKey": True},
                        {"text": " Â· ",       "isKey": False},
                        {"text": "Nuestra mesa", "isKey": True},
                    ],
                    "example": "Mi madre se llama LucÃ­a. Tu padre es Don Miguel. Su casa estÃ¡ cerca. Nuestra mesa es grande.",
                    "translation": "Minha mÃ£e se chama LucÃ­a. Teu pai Ã© Don Miguel. A casa dele/dela estÃ¡ perto. Nossa mesa Ã© grande.",
                    "note": "mi/tu/su sirven para hombre y mujer igual. Nuestro/nuestra cambia con el gÃ©nero de la cosa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "LucÃ­a aponta pro caderno: '___ familia tiene tres generaciones aquÃ­.' Ela tÃ¡ falando da famÃ­lia DELA mesma:",
                    "options": [
                        {"id": "a", "text": "Mi"},
                        {"id": "b", "text": "Tu"},
                        {"id": "c", "text": "Su"},
                        {"id": "d", "text": "Nuestra"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi", "native": "minha",
                    "npc_reaction": "Mi familia. La mÃ­a â€” tres generaciones.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Pero si te pregunto a ti: 'Â¿CÃ³mo se llama ___ madre?' â€” uso 'tu' porque hablo contigo.",
                    "translation": "Mas se te pergunto: 'Como se chama TUA mÃ£e?' â€” uso 'tu' porque falo contigo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "Pra perguntar sobre a TUA mÃ£e (sua, falando com vocÃª):",
                    "options": [
                        {"id": "a", "text": "Tu madre"},
                        {"id": "b", "text": "Mi madre"},
                        {"id": "c", "text": "Su madre"},
                        {"id": "d", "text": "Nuestra madre"},
                    ],
                    "correct": "a",
                    "word_id": "es_tu", "target": "tu", "native": "tua",
                    "npc_reaction": "Tu â€” cuando hablo contigo de algo tuyo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Ahora â€” si yo hablo con SofÃ­a sobre Miguel: 'SofÃ­a, Â¿conoces a ___ hijo?' Yo hablo de Miguel â€” es 'mi hijo'.",
                    "translation": "Agora â€” se eu falo com SofÃ­a sobre Miguel: 'SofÃ­a, conhece o meu filho?' Eu falo de Miguel â€” Ã© 'mi hijo'.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "Pra falar de Miguel (que Ã© filho de LucÃ­a), no jeito como LUCÃA fala dele:",
                    "options": [
                        {"id": "a", "text": "Mi hijo"},
                        {"id": "b", "text": "Tu hijo"},
                        {"id": "c", "text": "Su hijo"},
                        {"id": "d", "text": "Nuestra hijo"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi", "native": "meu",
                    "npc_reaction": "Mi hijo. Una palabra simple para una relaciÃ³n grande.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "SofÃ­a estÃ¡ pensando em Lola e Rita (irmÃ£s de Miguel). Pra ela falar de Miguel: 'Tu hermano se llama Miguel'. E pra vocÃª falar pra SofÃ­a 'a irmÃ£ DELA' (Lola), vocÃª usa:",
                    "options": [
                        {"id": "a", "text": "Su hermana"},
                        {"id": "b", "text": "Mi hermana"},
                        {"id": "c", "text": "Tu hermana"},
                        {"id": "d", "text": "Nuestra hermana"},
                    ],
                    "correct": "a",
                    "word_id": "es_su", "target": "su", "native": "dele/dela",
                    "npc_reaction": "Su. Cuando hablo de las cosas de Miguel â€” 'su hermana, su madre, su padre'.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Antes de dormir. Conversa Ã­ntima perto do fogÃ£o. LucÃ­a conta da famÃ­lia
    # â€” usa passado (la palabra que ela ouviu na F12). ReforÃ§o orgÃ¢nico de
    # mi/tu/su + passado natural.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["DoÃ±a LucÃ­a", "Miguel", "SofÃ­a"],
                "story": (
                    "A casa esfriou um pouco. LucÃ­a adicionou lenha no fogÃ£o. "
                    "SofÃ­a sentou no chÃ£o de pernas cruzadas perto do fogo. "
                    "MarÃ­a tinha ido pro quarto que LucÃ­a ofereceu â€” disse que "
                    "precisava descansar.\n\n"
                    "Sobrou vocÃª, Miguel, SofÃ­a e LucÃ­a em volta do fogÃ£o."
                ),
                "now": "Conversa Ã­ntima â€” LucÃ­a conta da famÃ­lia.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "DoÃ±a LucÃ­a",
                    "situation": "LucÃ­a mexe a panela no fogÃ£o. O guiso ainda vai demorar. Ela olha pra vocÃª â€” a casa Ã© pobre, qualquer coisa ajuda.",
                    "npc_line": "Hijo â€” si tienes algo de comer en la bolsa, ponlo en la mesa. En esta casa todo se reparte.",
                    "item_tag": "comida",
                    "on_use": {
                        "narrative": "VocÃª tira algo da mochila e coloca na mesa da famÃ­lia. LucÃ­a sorri â€” o tipo de sorriso que nÃ£o se finge.",
                        "npc_reaction": "Eso es. Quien trae algo a la mesa de otro â€” ya es de la familia. Gracias, hijo.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No te preocupes. El guiso alcanza para todos. SiÃ©ntate.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "DoÃ±a LucÃ­a â€” Â¿cÃ³mo se llamaba su esposo? Si no es indiscreta la pregunta.",
                    "translation": "DoÃ±a LucÃ­a â€” como se chamava seu marido? Se nÃ£o Ã© indiscriÃ§Ã£o.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Mi esposo se llamaba TomÃ¡s â€” igual que mi padre. MuriÃ³ hace seis aÃ±os. Era herrero tambiÃ©n, como Eduardo.",
                    "translation": "Meu marido se chamava TomÃ¡s â€” igual ao meu pai. Morreu faz seis anos. Era ferreiro tambÃ©m, como Eduardo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "LucÃ­a disse 'mi esposo'. Ela tÃ¡ falando:",
                    "options": [
                        {"id": "a", "text": "Do marido DELA (dela mesma)"},
                        {"id": "b", "text": "Do marido de outra pessoa"},
                        {"id": "c", "text": "Do filho dela"},
                        {"id": "d", "text": "Do irmÃ£o dela"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi esposo", "native": "meu marido",
                    "npc_reaction": "Mi. Cuando hablo desde mÃ­ â€” todo lo mÃ­o empieza con 'mi'.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Mi padre fue buen hombre. Tranquilo. HablÃ³ poco â€” pero cuando hablÃ³, todos escucharon.",
                    "translation": "Meu pai foi bom homem. Tranquilo. Falou pouco â€” mas quando falou, todos escutaram.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel disse 'mi padre fue buen hombre'. 'Fue' significa que o pai dele:",
                    "options": [
                        {"id": "a", "text": "Foi (jÃ¡ nÃ£o existe mais)"},
                        {"id": "b", "text": "Ã‰ (continua sendo)"},
                        {"id": "c", "text": "Vai ser"},
                        {"id": "d", "text": "EstÃ¡"},
                    ],
                    "correct": "a",
                    "word_id": "es_fue", "target": "fue", "native": "foi",
                    "npc_reaction": "Fue. Como 'soy' pero ya pasado. Mi padre fue â€” y ya descansa.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "SofÃ­a olhou pra Miguel. VocÃª olhou pra Miguel. Ele falou "
                        "do pai dele sem cara triste â€” sÃ³ direto."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Forastero â€” Â¿y tÃº? Â¿Recuerdas a tu familia?",
                    "translation": "Forasteiro â€” e vocÃª? Lembra da sua famÃ­lia?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "VocÃª nÃ£o lembra. Resposta honesta:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo de mi familia"},
                        {"id": "b", "text": "SÃ­ me acuerdo"},
                        {"id": "c", "text": "Voy a acordarme"},
                        {"id": "d", "text": "Soy familia"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_acuerdo", "target": "no me acuerdo", "native": "nÃ£o me lembro",
                    "npc_reaction": "EstÃ¡ bien, hijo. Hay cosas que el corazÃ³n guarda aunque la cabeza no recuerde.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "LucÃ­a: 'MaÃ±ana â€” Â¿quÃ© vas a hacer cuando vayas al ayuntamiento?' Pra vocÃª dizer o que VAI fazer (algo logo):",
                    "options": [
                        {"id": "a", "text": "Voy a hablar con el Alcalde"},
                        {"id": "b", "text": "Hablo con el Alcalde"},
                        {"id": "c", "text": "HablÃ© con el Alcalde"},
                        {"id": "d", "text": "Soy hablar"},
                    ],
                    "correct": "a",
                    "word_id": "es_voy_a", "target": "voy a", "native": "vou (algo logo)",
                    "npc_reaction": "Voy a hablar. Lo que sale ahora.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Hora de dormir. LucÃ­a mostra o quarto. Pequena conversa que termina com
    # LucÃ­a sussurrando pra Miguel sobre MarÃ­a. Gate: errar trava.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["DoÃ±a LucÃ­a", "Miguel"],
                "story": (
                    "Tarde da noite. LucÃ­a levou vocÃª atÃ© um quartinho nos "
                    "fundos da casa â€” cama estreita, lamparina baixa, parede "
                    "de adobe. Cheiro de madeira velha. 'AquÃ­ dormÃ­a mi "
                    "abuela hace aÃ±os.'"
                ),
                "now": "Conversa de despedida pra noite.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸ›ï¸ Quartinho dos fundos Â· Lamparina baixa Â· LucÃ­a na porta",
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "AquÃ­ vas a estar bien, hijo. Si necesitas algo â€” mi cuarto estÃ¡ en la otra punta. Miguel duerme cerca.",
                    "translation": "Aqui vocÃª vai estar bem, filho. Se precisar de algo â€” meu quarto fica no outro lado. Miguel dorme perto.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "VocÃª agradece formal pelo quarto:",
                    "options": [
                        {"id": "a", "text": "Gracias, DoÃ±a LucÃ­a"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada. TÃº eres amigo de Miguel â€” eso es suficiente para mÃ­.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Una pregunta antes de dormir â€” Â¿cÃ³mo estÃ¡s aquÃ­, en esta casa, esta noche?",
                    "translation": "Uma pergunta antes de dormir â€” como vocÃª estÃ¡ aqui, nessa casa, essa noite?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "Estado fÃ­sico â€” vocÃª tÃ¡ bem. Cama, comida, gente boa:",
                    "options": [
                        {"id": "a", "text": "Estoy bien"},
                        {"id": "b", "text": "Soy bien"},
                        {"id": "c", "text": "Tengo bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "estoy bien", "native": "estou bem",
                    "npc_reaction": "Bueno. Duerme tranquilo, hijo.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "LucÃ­a vai sair. Antes de fechar a porta â€” para. Vira pra "
                        "vocÃª outra vez. Olha pra vocÃª fixo, como quem pesa "
                        "alguma coisa."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Hijo â€” Â¿cÃ³mo se llama tu... amiga? La curandera. La que cuida.",
                    "translation": "Filho â€” como se chama tua... amiga? A curandera. A que cuida.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "LucÃ­a perguntou o nome de MarÃ­a. VocÃª responde simples usando 'minha' amiga:",
                    "options": [
                        {"id": "a", "text": "Mi amiga se llama MarÃ­a"},
                        {"id": "b", "text": "Tu amiga se llama MarÃ­a"},
                        {"id": "c", "text": "Su amiga se llama MarÃ­a"},
                        {"id": "d", "text": "Voy a llamar"},
                    ],
                    "correct": "a",
                    "word_id": "es_mi", "target": "mi amiga", "native": "minha amiga",
                    "npc_reaction": "MarÃ­a. Mmm. Â¿De dÃ³nde dijo que venÃ­a, hijo?",
                    "gated": True,
                },
                {
                    "kind": "multiple_choice",
                    "npc": "DoÃ±a LucÃ­a",
                    "question": "VocÃª nÃ£o sabe de onde MarÃ­a vem. Honesto:",
                    "options": [
                        {"id": "a", "text": "No sÃ©, no me dijo"},
                        {"id": "b", "text": "SÃ­, soy"},
                        {"id": "c", "text": "Vamos a saber"},
                        {"id": "d", "text": "Tengo de saber"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_se", "target": "no sÃ©", "native": "nÃ£o sei",
                    "npc_reaction": "Mmm. No, claro que no te dijo. Duerme, hijo. MaÃ±ana hablamos.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F14 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "scene",
                    "text": "ðŸšª DoÃ±a LucÃ­a fecha a porta Â· VocÃª na cama Â· Vela tremeluzindo",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª ouve passos no corredor. LucÃ­a indo atÃ© a cozinha â€” "
                        "onde Miguel estava lavando louÃ§a."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Miguel â€” escÃºchame bien. A esa mujer la conozco de algÃºn sitio. No recuerdo de dÃ³nde. Pero no es nueva en mi vida.",
                    "translation": "Miguel â€” me escuta bem. Essa mulher eu conheÃ§o de algum lugar. NÃ£o lembro de onde. Mas nÃ£o Ã© nova na minha vida.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "MamÃ¡ â€” Â¿estÃ¡s segura?",
                    "translation": "MÃ£e â€” vocÃª tem certeza?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "DoÃ±a LucÃ­a",
                    "line": "Estoy segura. MaÃ±ana voy a pensarlo. Hoy â€” dÃ©jala dormir. Pero no la pierdas de vista.",
                    "translation": "Tenho certeza. AmanhÃ£ vou pensar nisso. Hoje â€” deixa ela dormir. Mas nÃ£o tira ela da vista.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª ouviu cada palavra atravÃ©s da parede fina. Miguel "
                        "nÃ£o disse mais nada â€” sÃ³ apagou a lamparina da cozinha "
                        "e foi pro prÃ³prio quarto.\n\n"
                        "VocÃª fechou os olhos. Dormiu mal."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
