"""
Seed das 6 seÃ§Ãµes da Fase 9 Espanhol A1 â€” "Cuatro a la mesa".

Sem milestone obrigatÃ³rio â€” construÃ§Ã£o do vÃ­nculo do grupo de 4.
NecessÃ¡ria pra dar peso emocional Ã  traiÃ§Ã£o da T5 (canÃ´nico).

Primeira manhÃ£ com MarÃ­a na casa. CafÃ© fumegante, pÃ£o fresco, SofÃ­a rindo.
MarÃ­a conta uma piada e SofÃ­a morre de rir. Miguel, ao lado do protagonista,
sussurra: "Esta mujer me da algo raro. No sÃ© quÃ©." â€” instinto de Miguel
sobre MarÃ­a comeÃ§a aqui (nunca vira acusaÃ§Ã£o atÃ© T5).

MarÃ­a leva o grupo ao mercado pra repor mantimentos â€” usa a saÃ­da pra
observar o protagonista falando espanhol em contexto real, mensurando
o quanto a lÃ­ngua dele jÃ¡ "pegou". El Mercader percebe MarÃ­a, troca um
olhar com ela rÃ¡pido. Pista plantada: outros sabem dela.

Voltando, o protagonista vÃª de longe El Vigilante del Mercado parado na
esquina, observando o grupo. Quando o protagonista repara, ele jÃ¡ foi.

Novos vocab (3): comida Â· cafÃ© Â· naranja  (revisÃ£o de mercado da F4)
GramÃ¡tica nova: me gusta / no me gusta  (verbos pronominais bÃ¡sicos)
RevisÃ£o F1-F8:  nÃºmeros, Â¿cuÃ¡nto cuesta?, mucho/poco, pan, agua,
                hola, gracias, estoy bien/mejor, tengo X aÃ±os
NPC principais: Os 4 do grupo (protagonista Â· Miguel Â· SofÃ­a Â· MarÃ­a)
NPC cameo:      El Mercader (F4 retorno) Â· Rosa (cameo) Â· El Vigilante (avistado)
Arco emocional: pertencimento â†’ primeira refeiÃ§Ã£o em famÃ­lia â†’ instinto
                silencioso de Miguel ("algo nÃ£o bate")
TransiÃ§Ã£o:      Vigilante avistado de longe â†’ F10 abre com confronto direto

PrÃ©-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f9_sections [--reset]
"""

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Primeira manhÃ£ com MarÃ­a na casa. CafÃ© da manhÃ£ com os quatro.
    # MarÃ­a jÃ¡ parece familiar. SofÃ­a rindo. Miguel sussurra a primeira
    # desconfianÃ§a. Falas sem traduÃ§Ã£o â€” imersÃ£o.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "â˜€ï¸ ManhÃ£ clara Â· Mesa da cozinha Â· Quatro lugares postos\n\n"
                        "VocÃª acorda com cheiro de cafÃ©. Vozes baixas, panela "
                        "batendo no fogÃ£o. Quando vocÃª entra na cozinha, MarÃ­a "
                        "jÃ¡ tÃ¡ lÃ¡ â€” avental, cabelo preso, mÃ£os rÃ¡pidas. Como "
                        "se sempre tivesse morado ali."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "MarÃ­a",
                    "line": "Â¡Buenos dÃ­as! Hice cafÃ© fuerte â€” vas a necesitarlo.",
                    "pace": "normal",
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” siÃ©ntate. MarÃ­a nos hizo desayuno.",
                },
                {
                    "kind": "narrative",
                    "text": "SofÃ­a senta primeiro, Miguel na frente dela, MarÃ­a na cabeceira. Sobra o lugar do seu lado pra vocÃª.",
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "AquÃ­, forastero. Te guardÃ© el pan mÃ¡s caliente.",
                },
                {
                    "kind": "scene",
                    "text": "ðŸžâ˜• PÃ£o, queijo, cafÃ© fumegante, uma jarra de Ã¡gua com fatias de laranja. Mesa cheia.",
                },
                {
                    "kind": "npc",
                    "npc": "MarÃ­a",
                    "line": "SofÃ­a â€” Â¿quÃ© hizo Carmen ayer cuando le contaste que me llamaron?",
                },
                {
                    "kind": "npc",
                    "npc": "SofÃ­a",
                    "line": "Carmen dijo â€” 'Â¡Por fin alguien con cabeza llega al pueblo!' Y siguiÃ³ cosiendo sin levantar la mirada.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a ri â€” uma risada genuÃ­na, curta, baixa. SofÃ­a morre de rir e quase derruba o cafÃ©. Miguel sorri sem se entregar.",
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Forastero â€” ven aquÃ­ un segundo.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Miguel se inclina pro seu lado, conversa baixa enquanto SofÃ­a e MarÃ­a continuam falando alto na outra ponta.",
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Esta mujer me da algo raro. No sÃ© quÃ©. Pero algo.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Miguel nÃ£o te olha enquanto fala. Bebe o cafÃ© como se nÃ£o "
                        "tivesse dito nada. Mas vocÃª ouviu."
                    ),
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "comida",  "native": "comida"},
                        {"target": "cafÃ©",    "native": "cafÃ©"},
                        {"target": "naranja", "native": "laranja"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a pÃµe um prato cheio na sua frente. PÃ£o, queijo, laranja cortada. 'Esto es...' Como se chama tudo isso junto?",
                    "options": [
                        {"id": "a", "text": "Comida"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "LÃ¡mpara"},
                    ],
                    "correct": "a",
                    "word_id": "es_comida", "target": "comida", "native": "comida",
                    "npc_reaction": "Comida. Lo que el cuerpo necesita para seguir.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Ela enche sua caneca com o lÃ­quido escuro, fumegante e amargo. VocÃª toma um gole. Como se chama?",
                    "options": [
                        {"id": "a", "text": "CafÃ©"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_cafe", "target": "cafÃ©", "native": "cafÃ©",
                    "npc_reaction": "CafÃ©. Despierta los muertos. AquÃ­ en el pueblo se toma fuerte.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a empurra uma fruta laranja redonda na sua direÃ§Ã£o. Doce, com cheiro forte. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Naranja"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "CafÃ©"},
                        {"id": "d", "text": "Hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_naranja", "target": "naranja", "native": "laranja",
                    "npc_reaction": "Naranja. La compramos hoy al mercado. La fresca, no la del dÃ­a anterior.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel, baixinho, ainda do seu lado: 'Forastero â€” Â¿cÃ³mo estÃ¡s hoy?' VocÃª responde verdadeiramente â€” corpo descansado, cabeÃ§a limpa:",
                    "options": [
                        {"id": "a", "text": "Estoy bien"},
                        {"id": "b", "text": "Estoy mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Vamos al mercado despuÃ©s del desayuno. Mantente cerca.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: RevisÃ£o SRS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # SaÃ­da pra rua. Caminho atÃ© o mercado. RevisÃ£o pesada de F4 mercado:
    # nÃºmeros, cuÃ¡nto cuesta, mucho/poco. SofÃ­a testa o protagonista pra
    # ver se ele consegue lidar com o mercado sozinho.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "VocÃªs saÃ­ram da casa depois do desayuno. MarÃ­a na frente â€” "
                    "ela jÃ¡ parecia conhecer o caminho. SofÃ­a do seu lado, "
                    "Miguel atrÃ¡s. O sol jÃ¡ alto, o pueblo cheio.\n\n"
                    "SofÃ­a: 'Mientras llegamos al mercado â€” repaso. Â¿Listo, "
                    "forastero?'"
                ),
                "now": "SofÃ­a testa seu vocab de mercado enquanto caminham. RÃ¡pido.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Si te digo 'una naranja, dos naranjas' â€” Â¿cÃ³mo cuentas hasta cinco?",
                    "translation": "Se eu digo 'uma laranja, duas laranjas' â€” como vocÃª conta atÃ© cinco?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a aponta os dedos pra contar: uno, dos, tres... a sequÃªncia completa de 1 a 5 Ã©:",
                    "options": [
                        {"id": "a", "text": "uno, dos, tres, cuatro, cinco"},
                        {"id": "b", "text": "uno, dos, tres, cinco, cuatro"},
                        {"id": "c", "text": "uno, dos, dos, tres, cuatro"},
                        {"id": "d", "text": "uno, dos, tres, cuatro, seis"},
                    ],
                    "correct": "a",
                    "word_id": "es_numeros", "target": "uno, dos, tres, cuatro, cinco", "native": "um, dois, trÃªs, quatro, cinco",
                    "npc_reaction": "Perfecto. Si pierdes la cuenta â€” vuelves a empezar. AquÃ­ no se acepta dudar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Y si quieres saber el precio de algo â€” Â¿quÃ© preguntas al vendedor?",
                    "translation": "E se vocÃª quer saber o preÃ§o de algo â€” o que vocÃª pergunta ao vendedor?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª precisa saber quanto custa a laranja. A pergunta certa pro vendedor Ã©:",
                    "options": [
                        {"id": "a", "text": "Â¿CuÃ¡nto cuesta?"},
                        {"id": "b", "text": "Â¿CÃ³mo te llamas?"},
                        {"id": "c", "text": "Â¿CÃ³mo estÃ¡s?"},
                        {"id": "d", "text": "Â¿TÃº vienes?"},
                    ],
                    "correct": "a",
                    "word_id": "es_cuanto_cuesta", "target": "Â¿cuÃ¡nto cuesta?", "native": "quanto custa?",
                    "npc_reaction": "Exacto. Y si el precio te parece alto â€” ya te enseÃ±Ã© quÃ© hacer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y si encuentras algo que cuesta una sola moneda â€” Â¿es 'mucho' o 'poco'?",
                    "translation": "E se vocÃª acha algo que custa sÃ³ uma moeda â€” Ã© 'muito' ou 'pouco'?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Uma moeda sÃ³ por uma laranja gorda â€” preÃ§o bom. Como vocÃª fala isso?",
                    "options": [
                        {"id": "a", "text": "Poco"},
                        {"id": "b", "text": "Mucho"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Buen precio. Lo llevas sin dudar.",
                },
                {
                    "kind": "narrative",
                    "text": "VocÃªs entram na praÃ§a do mercado. Bancas coloridas, vendedores gritando, cheiro de fruta no ar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "AllÃ¡ â€” la banca del Mercader. El de las naranjas. Lo conoces, Â¿verdad?",
                    "translation": "Ali â€” a banca do Mercader. O das laranjas. VocÃª conhece, nÃ©?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "VocÃª lembra do Mercader da F4. Como vocÃª cumprimenta um vendedor ao chegar na banca dele de manhÃ£?",
                    "options": [
                        {"id": "a", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "b", "text": "Â¡AdiÃ³s!"},
                        {"id": "c", "text": "Â¡Mal!"},
                        {"id": "d", "text": "Â¡Tengo miedo!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Eso. Y Ã©l va a responder igual. Es lo educado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Voy a esperar acÃ¡. TÃº entras a la banca. Pide tres naranjas tÃº mismo.",
                    "translation": "Vou esperar aqui. VocÃª entra na banca. Pede trÃªs laranjas vocÃª mesmo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "VocÃª vai sozinho. O Mercader olha pra vocÃª esperando. VocÃª pede o que quer:",
                    "options": [
                        {"id": "a", "text": "Quiero tres naranjas, por favor"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s, mercader"},
                        {"id": "d", "text": "Soy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero", "native": "eu quero",
                    "npc_reaction": "Eso. Pide directo, sin disculparte. AquÃ­ pedir bien es respetarse a sÃ­ mismo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Mercader",
                    "line": "Tres naranjas, joven. Dos monedas.",
                    "translation": "TrÃªs laranjas, jovem. Duas moedas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Mercader",
                    "question": "Duas moedas por trÃªs laranjas. PreÃ§o justo. VocÃª diz a palavra que combina com o preÃ§o:",
                    "options": [
                        {"id": "a", "text": "EstÃ¡ bien"},
                        {"id": "b", "text": "Muy caro"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Buen trato. Ya hablas como gente de aquÃ­.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: PrÃ¡tica Aplicada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Dentro do mercado. MarÃ­a testando o protagonista subtilmente â€” quer ver
    # quÃ£o rÃ¡pido o dom dele 'pegou' a lÃ­ngua. Cada exercÃ­cio Ã© uma situaÃ§Ã£o
    # real do mercado. Mercader percebe MarÃ­a â€” troca de olhar rÃ¡pido.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "VocÃª pagou as trÃªs laranjas. SofÃ­a aprovou de longe com o "
                    "polegar. Miguel jÃ¡ tinha conseguido sal de outra banca. "
                    "MarÃ­a â€” que ficou um pouco atrÃ¡s â€” chegou agora, examinando "
                    "frutas em silÃªncio.\n\n"
                    "Ela observa vocÃª mais do que observa os tomates. VocÃª nota â€” "
                    "mas nÃ£o pesa muito."
                ),
                "now": "PrÃ¡tica intensa â€” situaÃ§Ãµes reais de mercado uma atrÃ¡s da outra.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Forastero â€” Â¿puedes pedirme tomates allÃ¡? Cinco, los rojos.",
                    "translation": "Forasteiro â€” pode pedir tomates ali pra mim? Cinco, os vermelhos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vendedora",
                    "question": "VocÃª chega na banca dos tomates. Uma mulher idosa, mÃ£os enrugadas. VocÃª cumprimenta antes de pedir:",
                    "options": [
                        {"id": "a", "text": "Â¡Buenos dÃ­as, seÃ±ora!"},
                        {"id": "b", "text": "Â¡AdiÃ³s!"},
                        {"id": "c", "text": "Â¡Mal!"},
                        {"id": "d", "text": "Â¡Forastero!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as, joven. Â¿QuÃ© te llevas hoy?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vendedora",
                    "question": "A vendedora espera. MarÃ­a quer cinco tomates. Como vocÃª pede?",
                    "options": [
                        {"id": "a", "text": "Quiero cinco tomates, por favor"},
                        {"id": "b", "text": "Tengo cinco tomates"},
                        {"id": "c", "text": "Soy cinco"},
                        {"id": "d", "text": "MaÃ±ana cinco"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero", "native": "eu quero",
                    "npc_reaction": "Cinco tomates. AquÃ­ estÃ¡n â€” los mÃ¡s maduros. Una moneda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vendedora",
                    "question": "Uma moeda sÃ³ por cinco tomates? VocÃª compara com o preÃ§o da laranja. Ã‰:",
                    "options": [
                        {"id": "a", "text": "Poco"},
                        {"id": "b", "text": "Mucho"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Mejor"},
                    ],
                    "correct": "a",
                    "word_id": "es_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Hoy hay mucho tomate, todos bajaron el precio.",
                },
                {
                    "kind": "narrative",
                    "text": "VocÃª paga, pega os tomates num pano dobrado. Volta pra MarÃ­a. Ela aceita com um sorriso pequeno â€” mas os olhos dela vÃ£o pra outra banca enquanto sorri.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Â¿Y la cabeza hoy? Â¿Te sigue molestando?",
                    "translation": "E a cabeÃ§a hoje? Continua incomodando?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Sua cabeÃ§a tÃ¡ leve hoje â€” diferente da noite da fiebre. VocÃª responde com a palavra que aprendeu com ela:",
                    "options": [
                        {"id": "a", "text": "Estoy mejor"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Tengo aÃ±os"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. La cabeza vuelve a ser tuya con descanso y comida buena.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Mira â€” ahÃ­ estÃ¡ el Mercader otra vez. Â¿Te acuerdas de Ã©l?",
                    "translation": "Olha â€” ali tÃ¡ o Mercader de novo. VocÃª lembra dele?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Mercader",
                    "question": "El Mercader te vÃª passando. Acena com a cabeÃ§a. VocÃª cumprimenta de volta:",
                    "options": [
                        {"id": "a", "text": "Â¡Hola!"},
                        {"id": "b", "text": "Â¡Mal!"},
                        {"id": "c", "text": "Â¡AdiÃ³s!"},
                        {"id": "d", "text": "Â¡Buenas noches!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olÃ¡",
                    "npc_reaction": "Hola, joven. Veo que andas en buena compaÃ±Ã­a hoy.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "El Mercader olha pra MarÃ­a. MarÃ­a olha pra El Mercader. "
                        "Por meio segundo â€” silÃªncio entre eles. Depois ela sorri, "
                        "ele continua organizando frutas, e a cena se desfaz como "
                        "se nada tivesse acontecido.\n\n"
                        "VocÃª notou. NÃ£o tem como saber ainda o que significa."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” vamos a la fuente. Tengo sed despuÃ©s de esta caminata.",
                    "translation": "Forasteiro â€” vamos pra fonte. TÃ´ com sede depois dessa caminhada.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a espera vocÃª dizer tambÃ©m o que precisa. VocÃª confirma o que sente:",
                    "options": [
                        {"id": "a", "text": "Yo tambiÃ©n tengo sed"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Vamos los cuatro. La fuente estÃ¡ cerca.",
                },
                {
                    "kind": "scene",
                    "text": "â›² A fonte de pedra do centro da plaza. VocÃªs param pra beber Ã¡gua â€” MarÃ­a faz copo com as mÃ£os. Miguel bebe direto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero â€” Â¿quÃ© piensas del mercado? Â¿Te gustÃ³?",
                    "translation": "Forasteiro â€” o que vocÃª acha do mercado? VocÃª gostou?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "VocÃª gostou â€” gente, cheiro, vida. Como vocÃª diz isso?",
                    "options": [
                        {"id": "a", "text": "SÃ­, me gusta"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Soy mercado"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto / eu gosto",
                    "npc_reaction": "Bueno. A todos nos gusta. Aunque a veces es ruidoso de mÃ¡s.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Â¿Y el cafÃ© que MarÃ­a hizo esta maÃ±ana? Â¿Te gustÃ³ tambiÃ©n?",
                    "translation": "E o cafÃ© que MarÃ­a fez essa manhÃ£? VocÃª gostou tambÃ©m?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "O cafÃ© estava muito forte pro seu gosto â€” amargo demais. Honesto, vocÃª diz:",
                    "options": [
                        {"id": "a", "text": "No me gusta"},
                        {"id": "b", "text": "Me gusta mucho"},
                        {"id": "c", "text": "Tengo cafÃ©"},
                        {"id": "d", "text": "Soy cafÃ©"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_gusta", "target": "no me gusta", "native": "nÃ£o gosto",
                    "npc_reaction": "Bueno â€” honesto. MaÃ±ana hago menos fuerte. Pero el cafÃ© del pueblo es asÃ­, te acostumbras.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a olha pra vocÃª esperando. Pergunta direta: 'Y la naranja del Mercader â€” Â¿te gustÃ³?' A laranja era doce, suculenta. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me gusta mucho"},
                        {"id": "b", "text": "No me gusta nada"},
                        {"id": "c", "text": "Tengo naranja"},
                        {"id": "d", "text": "AdiÃ³s naranja"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto / eu gosto",
                    "npc_reaction": "Bueno. La naranja del pueblo es la mejor â€” no acepto otra opiniÃ³n.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a comeÃ§a a cantar baixinho uma mÃºsica do pueblo. VocÃª ouve. NÃ£o conhece â€” mas gosta. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Me gusta esa canciÃ³n"},
                        {"id": "b", "text": "Tengo canciÃ³n"},
                        {"id": "c", "text": "Estoy canciÃ³n"},
                        {"id": "d", "text": "AdiÃ³s canciÃ³n"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto / eu gosto",
                    "npc_reaction": "Es vieja, del pueblo. Te la enseÃ±o otro dÃ­a completa.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Voltando do mercado, sentados na sombra de uma Ã¡rvore. MarÃ­a explica
    # 'me gusta' / 'no me gusta' formalmente, agora que o protagonista jÃ¡
    # usou os dois sem perceber. Pratica simples.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "Voltando da fonte vocÃªs sentaram sob uma Ã¡rvore antiga "
                    "perto da iglesia. Sombra fresca, vento leve. Tomates, "
                    "laranjas, sal â€” tudo na cesta de Miguel.\n\n"
                    "MarÃ­a: 'Mira â€” ya dijiste 'me gusta' tres veces sin "
                    "darte cuenta. Voy a explicarte cÃ³mo funciona.'"
                ),
                "now": "MarÃ­a vai explicar formalmente o que vocÃª jÃ¡ tava usando.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "'Me gusta' es raro â€” no es como 'tengo' o 'estoy'. Es como decir 'a mÃ­ me agrada eso'. La cosa actÃºa sobre ti, no tÃº sobre la cosa.",
                    "translation": "'Me gusta' Ã© diferente â€” nÃ£o Ã© como 'tengo' ou 'estoy'. Ã‰ como dizer 'isso me agrada'. A coisa age sobre vocÃª, nÃ£o vocÃª sobre a coisa.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Me gusta + cosa singular",
                    "meaning": "Eu gosto disso (lit: 'isso me agrada')",
                    "note": "se for uma coisa sÃ³, sempre 'me gusta': me gusta el pan",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Si la cosa es plural â€” 'naranjas', muchas â€” entonces 'me gustan'. Las naranjas actÃºan en plural sobre ti.",
                    "translation": "Se a coisa Ã© plural â€” 'laranjas', muitas â€” entÃ£o 'me gustan'. As laranjas agem no plural sobre vocÃª.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Me gustan + cosas plurales",
                    "meaning": "Eu gosto delas (plural)",
                    "note": "me gustan las naranjas, me gustan los tomates",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Me gusta",   "isKey": True},
                        {"text": " el cafÃ© / ", "isKey": False},
                        {"text": "Me gustan",  "isKey": True},
                        {"text": " las naranjas", "isKey": False},
                    ],
                    "example": "Me gusta el cafÃ©. Me gustan las naranjas. No me gusta el cafÃ© muy fuerte.",
                    "translation": "Eu gosto do cafÃ©. Eu gosto das laranjas. NÃ£o gosto do cafÃ© muito forte.",
                    "note": "singular: me gusta | plural: me gustan | negar: 'no' antes de tudo",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª gosta do pÃ£o de Rosa. PÃ£o Ã© uma coisa sÃ³. Como vocÃª diz?",
                    "options": [
                        {"id": "a", "text": "Me gusta el pan"},
                        {"id": "b", "text": "Me gustan el pan"},
                        {"id": "c", "text": "Tengo pan"},
                        {"id": "d", "text": "Soy pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Eso. El pan â€” singular â€” 'me gusta el pan'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "VocÃª gosta das laranjas do mercado. Laranjas â€” vÃ¡rias. Como vocÃª diz?",
                    "options": [
                        {"id": "a", "text": "Me gustan las naranjas"},
                        {"id": "b", "text": "Me gusta las naranjas"},
                        {"id": "c", "text": "Tengo naranjas"},
                        {"id": "d", "text": "Soy naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gustan", "target": "me gustan", "native": "gosto (plural)",
                    "npc_reaction": "Las naranjas â€” plural â€” 'me gustan'. El verbo cambia con la cosa, no contigo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Y si no te gusta algo â€” sÃ³lo aÃ±ade 'no' al principio. Simple.",
                    "translation": "E se vocÃª nÃ£o gosta de algo â€” sÃ³ adiciona 'no' no comeÃ§o. Simples.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "O cafÃ© estava forte demais essa manhÃ£ pra vocÃª. VocÃª nÃ£o gostou. Como vocÃª fala?",
                    "options": [
                        {"id": "a", "text": "No me gusta el cafÃ©"},
                        {"id": "b", "text": "Tengo no cafÃ©"},
                        {"id": "c", "text": "Soy no cafÃ©"},
                        {"id": "d", "text": "AdiÃ³s cafÃ©"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_gusta", "target": "no me gusta", "native": "nÃ£o gosto",
                    "npc_reaction": "Simple. MarÃ­a hace el cafÃ© muy fuerte. Yo tampoco lo tomo asÃ­.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'Forastero â€” Â¿y a ti, te gustan los tomates rojos?' VocÃª gosta. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "SÃ­, me gustan"},
                        {"id": "b", "text": "SÃ­, me gusta"},
                        {"id": "c", "text": "Tengo tomates"},
                        {"id": "d", "text": "Soy tomate"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gustan", "target": "me gustan", "native": "gosto (plural)",
                    "npc_reaction": "Tomates â€” plural â€” 'me gustan'. Vas a comer bien aquÃ­.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ReforÃ§o â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Tarde no pÃ¡tio da casa de Don Miguel. Conversa informal entre os quatro.
    # MarÃ­a, sutilmente, faz o protagonista falar mais. SofÃ­a conta histÃ³rias
    # da avÃ³. Miguel observa em silÃªncio. Poucos exercÃ­cios, foco em vida.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "VocÃªs voltaram pra casa de Don Miguel ao meio-dia. Comeram "
                    "as laranjas no pÃ¡tio, sentados em torno de uma mesa baixa "
                    "de madeira. MarÃ­a partiu os tomates em fatias com a navaja "
                    "pequena que ela carrega.\n\n"
                    "Don Miguel saiu pra trabalhar no campo. Sobrou os quatro "
                    "jovens, sombra da macieira, vento leve, tarde longa."
                ),
                "now": "Conversa real entre os quatro â€” vocab orgÃ¢nico, vida normal.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "SofÃ­a",
                    "situation": "A mesa baixa do pÃ¡tio tem tomate fatiado e laranja â€” mas SofÃ­a olha pra mochila do forastero, curiosa.",
                    "npc_line": "Forastero â€” Â¿tienes algo en la bolsa para sumar a la mesa? Una comida compartida sabe mejor.",
                    "item_tag": "comida",
                    "on_use": {
                        "narrative": "VocÃª tira algo da mochila e pÃµe no centro da mesa baixa. Os quatro dividem â€” SofÃ­a, Miguel, MarÃ­a e vocÃª.",
                        "npc_reaction": "Â¡Eso! Ahora sÃ­ es mesa de verdad. Cuatro personas, una comida â€” somos grupo.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa â€” el tomate y la naranja alcanzan. Otra vez serÃ¡.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Mi abuela tenÃ­a una receta de tomates con queso, naranjas y sal. Sonaba raro pero era de lo mejor que comÃ­ en mi vida.",
                    "translation": "Minha avÃ³ tinha uma receita de tomates com queijo, laranjas e sal. Soava estranho mas era das melhores coisas que comi na vida.",
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a corta uma laranja em quatro pedaÃ§os. Coloca sal em um. Estende pra SofÃ­a. SofÃ­a come. Faz cara de surpresa, ri alto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Â¡Es eso! Â¡Exacto! Â¿CÃ³mo lo sabÃ­as?",
                    "translation": "Ã‰ isso! Exato! Como vocÃª sabia?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Una receta vieja. La aprendÃ­ lejos de aquÃ­. Las palabras buenas y las recetas buenas viajan iguales.",
                    "translation": "Uma receita velha. Aprendi longe daqui. As palavras boas e as receitas boas viajam iguais.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a estende um pedaÃ§o de laranja com sal pra vocÃª. VocÃª prova. Doce, salgado, estranho mas bom. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Me gusta"},
                        {"id": "b", "text": "No me gusta"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Bueno. SabÃ­a que te iba a gustar. Algunos sabores se reconocen aunque uno nunca los haya probado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” Â¿todavÃ­a tienes la lÃ¡mpara en el bolsillo? La de mi abuela.",
                    "translation": "Forasteiro â€” vocÃª ainda tem a lamparina no bolso? A da minha avÃ³.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "SofÃ­a pergunta sobre a lamparina. VocÃª tira do bolso pra mostrar â€” quente do sol. Como se chama?",
                    "options": [
                        {"id": "a", "text": "LÃ¡mpara"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Naranja"},
                        {"id": "d", "text": "Pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_lampara", "target": "lÃ¡mpara", "native": "lamparina",
                    "npc_reaction": "LÃ¡mpara. La cargas sin pensar. Eso es bueno â€” la palabra ya es tuya.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Miguel come em silÃªncio do lado da macieira. Olha pra "
                        "MarÃ­a de vez em quando â€” uma fraÃ§Ã£o de segundo. Depois "
                        "volta a olhar pra Ã¡rvore. NÃ£o comenta nada."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Miguel â€” Â¿tÃº no comes la naranja con sal? Â¿No te gusta?",
                    "translation": "Miguel â€” vocÃª nÃ£o come a laranja com sal? NÃ£o gosta?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel olha pra SofÃ­a. Decide responder educado mas honesto: 'No me gusta mezclar. Naranja con naranja, sal con tomate.' Como ele diz que nÃ£o gosta?",
                    "options": [
                        {"id": "a", "text": "No me gusta"},
                        {"id": "b", "text": "Me gusta"},
                        {"id": "c", "text": "Tengo gusto"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_gusta", "target": "no me gusta", "native": "nÃ£o gosto",
                    "npc_reaction": "Cada uno con su receta. Voy a comer mi pan tranquilo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Forastero â€” Â¿cuÃ¡ntos aÃ±os tiene tu padre? Si te acuerdas.",
                    "translation": "Forasteiro â€” quantos anos seu pai tem? Se vocÃª lembra.",
                },
                {
                    "kind": "player",
                    "text": "VocÃª nÃ£o lembra do seu pai. NÃ£o lembra de ninguÃ©m de antes. A pergunta dÃ³i um pouco â€” mas SofÃ­a perguntou sem maldade.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "SofÃ­a",
                    "question": "VocÃª responde a verdade â€” nÃ£o tem como mentir sobre isso. A palavra do que vocÃª Ã© aqui ainda:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo, soy forastero"},
                        {"id": "b", "text": "Tengo veinte aÃ±os"},
                        {"id": "c", "text": "Me llamo"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Lo siento. No tenÃ­a que preguntarte. Olvida.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "SilÃªncio breve. MarÃ­a olha pra SofÃ­a com um aviso silencioso. "
                        "SofÃ­a abaixa a cabeÃ§a meio sem graÃ§a. Miguel â€” que tinha "
                        "ouvido tudo â€” olha pra vocÃª de lado e diz baixo:"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Tu padre â€” el que sea â€” tiene un hijo bueno. Eso ya es algo.",
                    "translation": "Seu pai â€” quem quer que seja â€” tem um filho bom. Isso jÃ¡ Ã© algo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel acabou de dizer algo que tocou em vocÃª. VocÃª responde com a palavra que sempre vale:",
                    "options": [
                        {"id": "a", "text": "Gracias, Miguel"},
                        {"id": "b", "text": "AdiÃ³s"},
                        {"id": "c", "text": "Mal"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, hermano. Eso es lo que pienso.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Voltando pra casa no fim da tarde, vocÃªs passam por uma rua estreita.
    # O protagonista vÃª de longe El Vigilante del Mercado parado, observando.
    # Gate de reaÃ§Ã£o social â€” vocÃª precisa avisar o grupo sem alarmar.
    # TransiÃ§Ã£o direta pra F10 (confronto com Vigilante).
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["MarÃ­a", "SofÃ­a", "Miguel"],
                "story": (
                    "A tarde virou em fim de tarde, fim de tarde em entardecer. "
                    "VocÃªs recolheram os restos da comida e saÃ­ram pra dar "
                    "uma volta pelo pueblo antes do jantar. MarÃ­a queria ver "
                    "alguma loja de tecidos que Carmen tinha mencionado.\n\n"
                    "Caminham por uma rua estreita perto do mercado vazio. "
                    "Vai escurecendo aos poucos."
                ),
                "now": "VocÃª precisa reagir certo a uma situaÃ§Ã£o que sÃ³ vocÃª percebeu.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ† Rua estreita Â· Final de tarde Â· VocÃªs quatro andando juntos",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª anda do lado de Miguel. SofÃ­a e MarÃ­a Ã  frente "
                        "conversando baixo. Sombras compridas no chÃ£o de pedra."
                    ),
                },
                {
                    "kind": "scene",
                    "text": "ðŸ‘¤ Uma figura na esquina ao fim da rua â€” parado, observando. ChapÃ©u baixo. VocÃª reconhece â€” El Vigilante del Mercado.",
                },
                {
                    "kind": "player",
                    "text": (
                        "Ele te olha de longe. VocÃª lembra o que ele tentou fazer "
                        "no corredor da posada. Ele recuou do fogo â€” mas voltou. "
                        "Aqui. Agora."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero â€” Â¿quÃ© pasa? Â¿EstÃ¡s bien?",
                    "translation": "Forasteiro â€” o que foi? VocÃª tÃ¡ bem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel notou que vocÃª parou de andar. VocÃª precisa avisar sem alarmar SofÃ­a e MarÃ­a Ã  frente. VocÃª diz baixo:",
                    "options": [
                        {"id": "a", "text": "Miguel â€” mira allÃ¡. El Vigilante."},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_mira", "target": "mira", "native": "olha",
                    "npc_reaction": "Miguel sigue tu mirada. Lo ve. Aprieta la mandÃ­bula. Sin levantar la voz: 'Sigue caminando. No te detengas.'",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸ‘ï¸ El Vigilante continua parado. NÃ£o se mexe. Apenas observa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Â¿Tienes miedo, forastero? Es vÃ¡lido. SÃ© honesto conmigo.",
                    "translation": "TÃ¡ com medo, forasteiro? Ã‰ vÃ¡lido. Seja honesto comigo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "VocÃª sente medo â€” claro que sente. NÃ£o dÃ¡ pra esconder de Miguel. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "SÃ­, tengo miedo"},
                        {"id": "b", "text": "No, estoy bien"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "tengo miedo", "native": "tenho medo",
                    "npc_reaction": "Bueno. Yo tambiÃ©n. Quien no tiene miedo aquÃ­ es el peligroso â€” no nosotros.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "MarÃ­a, que ia Ã  frente, para de andar. Como se tivesse sentido â€” sem ter visto. Vira a cabeÃ§a pra atrÃ¡s.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Miguel â€” Â¿quÃ© pasa? Â¿Por quÃ© se quedaron parados?",
                    "translation": "Miguel â€” o que foi? Por que vocÃªs pararam?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "Miguel se vira pra MarÃ­a. Aponta com o queixo discreto pra esquina. VocÃª decide responder primeiro â€” sem alarmar SofÃ­a. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Hay un hombre allÃ¡"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_hay", "target": "hay", "native": "tem / hÃ¡",
                    "npc_reaction": "MarÃ­a sigue tu mirada. Ve a El Vigilante. Su expresiÃ³n no cambia â€” pero pone la mano en el hombro de SofÃ­a.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "ðŸ‘ï¸â†’ Quando vocÃª olha de novo pra esquina, El Vigilante jÃ¡ nÃ£o estÃ¡ lÃ¡. Sumiu sem vocÃª ver ele se mover.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "Ya se fue. Pero estuvo â€” los cuatro lo confirmamos.",
                    "translation": "JÃ¡ foi. Mas esteve â€” nÃ³s quatro confirmamos.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "SofÃ­a",
                    "line": "Â¿QuÃ©? Â¿QuiÃ©n? Â¡Yo no vi nada!",
                    "translation": "O quÃª? Quem? Eu nÃ£o vi nada!",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "MarÃ­a",
                    "line": "DespuÃ©s te explicamos. Ahora â€” a la casa. Pronto.",
                    "translation": "Depois explicamos. Agora â€” pra casa. RÃ¡pido.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "MarÃ­a",
                    "question": "MarÃ­a decide que o grupo precisa voltar antes que escureÃ§a mais. Pergunta: 'Â¿TÃº vienes rÃ¡pido conmigo, forastero?' VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "SÃ­, yo voy"},
                        {"id": "b", "text": "No tengo miedo"},
                        {"id": "c", "text": "AdiÃ³s"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vamos los cuatro juntos. Nadie atrÃ¡s, nadie adelante. LÃ­nea cerrada.",
                    "gated": True,
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra F10 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs andam apertados pelas ruas de pedra de volta pra "
                        "casa. MarÃ­a no centro. SofÃ­a Ã  esquerda. VocÃª no meio. "
                        "Miguel atrÃ¡s vigiando atrÃ¡s.\n\n"
                        "Don Miguel jÃ¡ estava na porta esperando â€” Carmen tinha "
                        "mandado um recado. 'Hablamos adentro.'"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "MaÃ±ana al amanecer vamos a tener que hablar con el Alcalde. El Vigilante ya escalÃ³ esto a sus jefes.",
                    "translation": "AmanhÃ£ ao amanhecer vamos ter que falar com o Alcalde. El Vigilante jÃ¡ levou isso pros chefes dele.",
                    "pace": "slow",
                },
                {
                    "kind": "scene",
                    "text": "ðŸŒ™ Noite cai Â· Os quatro mais Don Miguel sentados em volta da mesa Â· A lamparina baixa Â· Conversa difÃ­cil",
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
