"""
Seed das 6 seções da Fase 9 Espanhol A1 — "Cuatro a la mesa".

Sem milestone obrigatório — construção do vínculo do grupo de 4.
Necessária pra dar peso emocional à traição da T5 (canônico).

Primeira manhã com María na casa. Café fumegante, pão fresco, Sofía rindo.
María conta uma piada e Sofía morre de rir. Miguel, ao lado do protagonista,
sussurra: "Esta mujer me da algo raro. No sé qué." — instinto de Miguel
sobre María começa aqui (nunca vira acusação até T5).

María leva o grupo ao mercado pra repor mantimentos — usa a saída pra
observar o protagonista falando espanhol em contexto real, mensurando
o quanto a língua dele já "pegou". El Mercader percebe María, troca um
olhar com ela rápido. Pista plantada: outros sabem dela.

Voltando, o protagonista vê de longe El Vigilante del Mercado parado na
esquina, observando o grupo. Quando o protagonista repara, ele já foi.

Novos vocab (3): comida · café · naranja  (revisão de mercado da F4)
Gramática nova: me gusta / no me gusta  (verbos pronominais básicos)
Revisão F1-F8:  números, ¿cuánto cuesta?, mucho/poco, pan, agua,
                hola, gracias, estoy bien/mejor, tengo X años
NPC principais: Os 4 do grupo (protagonista · Miguel · Sofía · María)
NPC cameo:      El Mercader (F4 retorno) · Rosa (cameo) · El Vigilante (avistado)
Arco emocional: pertencimento → primeira refeição em família → instinto
                silencioso de Miguel ("algo não bate")
Transição:      Vigilante avistado de longe → F10 abre com confronto direto

Pré-requisito: python manage.py seed_es_full
Uso:           python manage.py seed_es_f9_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Primeira manhã com María na casa. Café da manhã com os quatro.
    # María já parece familiar. Sofía rindo. Miguel sussurra a primeira
    # desconfiança. Falas sem tradução — imersão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "skill_check",
                    "skill": "sustento",
                    "min_level": 1,
                    "uses_item_tag": "comida",
                    "success": "Voce entende a ordem da mesa e evita ofender quem serviu a comida.",
                    "fallback": "Voce hesita diante da mesa, mas Miguel traduz o gesto e todos continuam.",
                },
                {
                    "kind": "scene",
                    "text": (
                        "☀️ Manhã clara · Mesa da cozinha · Quatro lugares postos\n\n"
                        "Você acorda com cheiro de café. Vozes baixas, panela "
                        "batendo no fogão. Quando você entra na cozinha, María "
                        "já tá lá — avental, cabelo preso, mãos rápidas. Como "
                        "se sempre tivesse morado ali."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "María",
                    "line": "¡Buenos días! Hice café fuerte — vas a necesitarlo.",
                    "pace": "normal",
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "Forastero — siéntate. María nos hizo desayuno.",
                },
                {
                    "kind": "narrative",
                    "text": "Sofía senta primeiro, Miguel na frente dela, María na cabeceira. Sobra o lugar do seu lado pra você.",
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Aquí, forastero. Te guardé el pan más caliente.",
                },
                {
                    "kind": "scene",
                    "text": "🍞☕ Pão, queijo, café fumegante, uma jarra de água com fatias de laranja. Mesa cheia.",
                },
                {
                    "kind": "npc",
                    "npc": "María",
                    "line": "Sofía — ¿qué hizo Carmen ayer cuando le contaste que me llamaron?",
                },
                {
                    "kind": "npc",
                    "npc": "Sofía",
                    "line": "Carmen dijo — '¡Por fin alguien con cabeza llega al pueblo!' Y siguió cosiendo sin levantar la mirada.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "María ri — uma risada genuína, curta, baixa. Sofía morre de rir e quase derruba o café. Miguel sorri sem se entregar.",
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Forastero — ven aquí un segundo.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Miguel se inclina pro seu lado, conversa baixa enquanto Sofía e María continuam falando alto na outra ponta.",
                },
                {
                    "kind": "npc",
                    "npc": "Miguel",
                    "line": "Esta mujer me da algo raro. No sé qué. Pero algo.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Miguel não te olha enquanto fala. Bebe o café como se não "
                        "tivesse dito nada. Mas você ouviu."
                    ),
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "comida",  "native": "comida"},
                        {"target": "café",    "native": "café"},
                        {"target": "naranja", "native": "laranja"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María põe um prato cheio na sua frente. Pão, queijo, laranja cortada. 'Esto es...' Como se chama tudo isso junto?",
                    "options": [
                        {"id": "a", "text": "Comida"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Pan"},
                        {"id": "d", "text": "Lámpara"},
                    ],
                    "correct": "a",
                    "word_id": "es_comida", "target": "comida", "native": "comida",
                    "npc_reaction": "Comida. Lo que el cuerpo necesita para seguir.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Ela enche sua caneca com o líquido escuro, fumegante e amargo. Você toma um gole. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Café"},
                        {"id": "b", "text": "Agua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_cafe", "target": "café", "native": "café",
                    "npc_reaction": "Café. Despierta los muertos. Aquí en el pueblo se toma fuerte.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía empurra uma fruta laranja redonda na sua direção. Doce, com cheiro forte. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Naranja"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "Café"},
                        {"id": "d", "text": "Hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_naranja", "target": "naranja", "native": "laranja",
                    "npc_reaction": "Naranja. La compramos hoy al mercado. La fresca, no la del día anterior.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel, baixinho, ainda do seu lado: 'Forastero — ¿cómo estás hoy?' Você responde verdadeiramente — corpo descansado, cabeça limpa:",
                    "options": [
                        {"id": "a", "text": "Estoy bien"},
                        {"id": "b", "text": "Estoy mal"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bueno. Vamos al mercado después del desayuno. Mantente cerca.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ─────────────────────────────────────────────────
    # Saída pra rua. Caminho até o mercado. Revisão pesada de F4 mercado:
    # números, cuánto cuesta, mucho/poco. Sofía testa o protagonista pra
    # ver se ele consegue lidar com o mercado sozinho.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "Vocês saíram da casa depois do desayuno. María na frente — "
                    "ela já parecia conhecer o caminho. Sofía do seu lado, "
                    "Miguel atrás. O sol já alto, o pueblo cheio.\n\n"
                    "Sofía: 'Mientras llegamos al mercado — repaso. ¿Listo, "
                    "forastero?'"
                ),
                "now": "Sofía testa seu vocab de mercado enquanto caminham. Rápido.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Si te digo 'una naranja, dos naranjas' — ¿cómo cuentas hasta cinco?",
                    "translation": "Se eu digo 'uma laranja, duas laranjas' — como você conta até cinco?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía aponta os dedos pra contar: uno, dos, tres... a sequência completa de 1 a 5 é:",
                    "options": [
                        {"id": "a", "text": "uno, dos, tres, cuatro, cinco"},
                        {"id": "b", "text": "uno, dos, tres, cinco, cuatro"},
                        {"id": "c", "text": "uno, dos, dos, tres, cuatro"},
                        {"id": "d", "text": "uno, dos, tres, cuatro, seis"},
                    ],
                    "correct": "a",
                    "word_id": "es_numeros", "target": "uno, dos, tres, cuatro, cinco", "native": "um, dois, três, quatro, cinco",
                    "npc_reaction": "Perfecto. Si pierdes la cuenta — vuelves a empezar. Aquí no se acepta dudar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Y si quieres saber el precio de algo — ¿qué preguntas al vendedor?",
                    "translation": "E se você quer saber o preço de algo — o que você pergunta ao vendedor?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você precisa saber quanto custa a laranja. A pergunta certa pro vendedor é:",
                    "options": [
                        {"id": "a", "text": "¿Cuánto cuesta?"},
                        {"id": "b", "text": "¿Cómo te llamas?"},
                        {"id": "c", "text": "¿Cómo estás?"},
                        {"id": "d", "text": "¿Tú vienes?"},
                    ],
                    "correct": "a",
                    "word_id": "es_cuanto_cuesta", "target": "¿cuánto cuesta?", "native": "quanto custa?",
                    "npc_reaction": "Exacto. Y si el precio te parece alto — ya te enseñé qué hacer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y si encuentras algo que cuesta una sola moneda — ¿es 'mucho' o 'poco'?",
                    "translation": "E se você acha algo que custa só uma moeda — é 'muito' ou 'pouco'?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Uma moeda só por uma laranja gorda — preço bom. Como você fala isso?",
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
                    "text": "Vocês entram na praça do mercado. Bancas coloridas, vendedores gritando, cheiro de fruta no ar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Allá — la banca del Mercader. El de las naranjas. Lo conoces, ¿verdad?",
                    "translation": "Ali — a banca do Mercader. O das laranjas. Você conhece, né?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Você lembra do Mercader da F4. Como você cumprimenta um vendedor ao chegar na banca dele de manhã?",
                    "options": [
                        {"id": "a", "text": "¡Buenos días!"},
                        {"id": "b", "text": "¡Adiós!"},
                        {"id": "c", "text": "¡Mal!"},
                        {"id": "d", "text": "¡Tengo miedo!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Eso. Y él va a responder igual. Es lo educado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Voy a esperar acá. Tú entras a la banca. Pide tres naranjas tú mismo.",
                    "translation": "Vou esperar aqui. Você entra na banca. Pede três laranjas você mesmo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Você vai sozinho. O Mercader olha pra você esperando. Você pede o que quer:",
                    "options": [
                        {"id": "a", "text": "Quiero tres naranjas, por favor"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Adiós, mercader"},
                        {"id": "d", "text": "Soy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero", "native": "eu quero",
                    "npc_reaction": "Eso. Pide directo, sin disculparte. Aquí pedir bien es respetarse a sí mismo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Mercader",
                    "line": "Tres naranjas, joven. Dos monedas.",
                    "translation": "Três laranjas, jovem. Duas moedas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Mercader",
                    "question": "Duas moedas por três laranjas. Preço justo. Você diz a palavra que combina com o preço:",
                    "options": [
                        {"id": "a", "text": "Está bien"},
                        {"id": "b", "text": "Muy caro"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Buen trato. Ya hablas como gente de aquí.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Dentro do mercado. María testando o protagonista subtilmente — quer ver
    # quão rápido o dom dele 'pegou' a língua. Cada exercício é uma situação
    # real do mercado. Mercader percebe María — troca de olhar rápido.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "Você pagou as três laranjas. Sofía aprovou de longe com o "
                    "polegar. Miguel já tinha conseguido sal de outra banca. "
                    "María — que ficou um pouco atrás — chegou agora, examinando "
                    "frutas em silêncio.\n\n"
                    "Ela observa você mais do que observa os tomates. Você nota — "
                    "mas não pesa muito."
                ),
                "now": "Prática intensa — situações reais de mercado uma atrás da outra.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Forastero — ¿puedes pedirme tomates allá? Cinco, los rojos.",
                    "translation": "Forasteiro — pode pedir tomates ali pra mim? Cinco, os vermelhos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vendedora",
                    "question": "Você chega na banca dos tomates. Uma mulher idosa, mãos enrugadas. Você cumprimenta antes de pedir:",
                    "options": [
                        {"id": "a", "text": "¡Buenos días, señora!"},
                        {"id": "b", "text": "¡Adiós!"},
                        {"id": "c", "text": "¡Mal!"},
                        {"id": "d", "text": "¡Forastero!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días, joven. ¿Qué te llevas hoy?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vendedora",
                    "question": "A vendedora espera. María quer cinco tomates. Como você pede?",
                    "options": [
                        {"id": "a", "text": "Quiero cinco tomates, por favor"},
                        {"id": "b", "text": "Tengo cinco tomates"},
                        {"id": "c", "text": "Soy cinco"},
                        {"id": "d", "text": "Mañana cinco"},
                    ],
                    "correct": "a",
                    "word_id": "es_quiero", "target": "quiero", "native": "eu quero",
                    "npc_reaction": "Cinco tomates. Aquí están — los más maduros. Una moneda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vendedora",
                    "question": "Uma moeda só por cinco tomates? Você compara com o preço da laranja. É:",
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
                    "text": "Você paga, pega os tomates num pano dobrado. Volta pra María. Ela aceita com um sorriso pequeno — mas os olhos dela vão pra outra banca enquanto sorri.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "¿Y la cabeza hoy? ¿Te sigue molestando?",
                    "translation": "E a cabeça hoje? Continua incomodando?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Sua cabeça tá leve hoje — diferente da noite da fiebre. Você responde com a palavra que aprendeu com ela:",
                    "options": [
                        {"id": "a", "text": "Estoy mejor"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Tengo años"},
                    ],
                    "correct": "a",
                    "word_id": "es_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. La cabeza vuelve a ser tuya con descanso y comida buena.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Mira — ahí está el Mercader otra vez. ¿Te acuerdas de él?",
                    "translation": "Olha — ali tá o Mercader de novo. Você lembra dele?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Mercader",
                    "question": "El Mercader te vê passando. Acena com a cabeça. Você cumprimenta de volta:",
                    "options": [
                        {"id": "a", "text": "¡Hola!"},
                        {"id": "b", "text": "¡Mal!"},
                        {"id": "c", "text": "¡Adiós!"},
                        {"id": "d", "text": "¡Buenas noches!"},
                    ],
                    "correct": "a",
                    "word_id": "es_hola", "target": "hola", "native": "olá",
                    "npc_reaction": "Hola, joven. Veo que andas en buena compañía hoy.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "El Mercader olha pra María. María olha pra El Mercader. "
                        "Por meio segundo — silêncio entre eles. Depois ela sorri, "
                        "ele continua organizando frutas, e a cena se desfaz como "
                        "se nada tivesse acontecido.\n\n"
                        "Você notou. Não tem como saber ainda o que significa."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Forastero — vamos a la fuente. Tengo sed después de esta caminata.",
                    "translation": "Forasteiro — vamos pra fonte. Tô com sede depois dessa caminhada.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía espera você dizer também o que precisa. Você confirma o que sente:",
                    "options": [
                        {"id": "a", "text": "Yo también tengo sed"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_sed", "target": "tengo sed", "native": "tenho sede",
                    "npc_reaction": "Vamos los cuatro. La fuente está cerca.",
                },
                {
                    "kind": "scene",
                    "text": "⛲ A fonte de pedra do centro da plaza. Vocês param pra beber água — María faz copo com as mãos. Miguel bebe direto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero — ¿qué piensas del mercado? ¿Te gustó?",
                    "translation": "Forasteiro — o que você acha do mercado? Você gostou?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Você gostou — gente, cheiro, vida. Como você diz isso?",
                    "options": [
                        {"id": "a", "text": "Sí, me gusta"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy mal"},
                        {"id": "d", "text": "Soy mercado"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto / eu gosto",
                    "npc_reaction": "Bueno. A todos nos gusta. Aunque a veces es ruidoso de más.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "¿Y el café que María hizo esta mañana? ¿Te gustó también?",
                    "translation": "E o café que María fez essa manhã? Você gostou também?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "O café estava muito forte pro seu gosto — amargo demais. Honesto, você diz:",
                    "options": [
                        {"id": "a", "text": "No me gusta"},
                        {"id": "b", "text": "Me gusta mucho"},
                        {"id": "c", "text": "Tengo café"},
                        {"id": "d", "text": "Soy café"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_gusta", "target": "no me gusta", "native": "não gosto",
                    "npc_reaction": "Bueno — honesto. Mañana hago menos fuerte. Pero el café del pueblo es así, te acostumbras.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María olha pra você esperando. Pergunta direta: 'Y la naranja del Mercader — ¿te gustó?' A laranja era doce, suculenta. Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, me gusta mucho"},
                        {"id": "b", "text": "No me gusta nada"},
                        {"id": "c", "text": "Tengo naranja"},
                        {"id": "d", "text": "Adiós naranja"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto / eu gosto",
                    "npc_reaction": "Bueno. La naranja del pueblo es la mejor — no acepto otra opinión.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía começa a cantar baixinho uma música do pueblo. Você ouve. Não conhece — mas gosta. Você diz:",
                    "options": [
                        {"id": "a", "text": "Me gusta esa canción"},
                        {"id": "b", "text": "Tengo canción"},
                        {"id": "c", "text": "Estoy canción"},
                        {"id": "d", "text": "Adiós canción"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto / eu gosto",
                    "npc_reaction": "Es vieja, del pueblo. Te la enseño otro día completa.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Voltando do mercado, sentados na sombra de uma árvore. María explica
    # 'me gusta' / 'no me gusta' formalmente, agora que o protagonista já
    # usou os dois sem perceber. Pratica simples.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "Voltando da fonte vocês sentaram sob uma árvore antiga "
                    "perto da iglesia. Sombra fresca, vento leve. Tomates, "
                    "laranjas, sal — tudo na cesta de Miguel.\n\n"
                    "María: 'Mira — ya dijiste 'me gusta' tres veces sin "
                    "darte cuenta. Voy a explicarte cómo funciona.'"
                ),
                "now": "María vai explicar formalmente o que você já tava usando.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "'Me gusta' es raro — no es como 'tengo' o 'estoy'. Es como decir 'a mí me agrada eso'. La cosa actúa sobre ti, no tú sobre la cosa.",
                    "translation": "'Me gusta' é diferente — não é como 'tengo' ou 'estoy'. É como dizer 'isso me agrada'. A coisa age sobre você, não você sobre a coisa.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Me gusta + cosa singular",
                    "meaning": "Eu gosto disso (lit: 'isso me agrada')",
                    "note": "se for uma coisa só, sempre 'me gusta': me gusta el pan",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Si la cosa es plural — 'naranjas', muchas — entonces 'me gustan'. Las naranjas actúan en plural sobre ti.",
                    "translation": "Se a coisa é plural — 'laranjas', muitas — então 'me gustan'. As laranjas agem no plural sobre você.",
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
                        {"text": " el café / ", "isKey": False},
                        {"text": "Me gustan",  "isKey": True},
                        {"text": " las naranjas", "isKey": False},
                    ],
                    "example": "Me gusta el café. Me gustan las naranjas. No me gusta el café muy fuerte.",
                    "translation": "Eu gosto do café. Eu gosto das laranjas. Não gosto do café muito forte.",
                    "note": "singular: me gusta | plural: me gustan | negar: 'no' antes de tudo",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você gosta do pão de Rosa. Pão é uma coisa só. Como você diz?",
                    "options": [
                        {"id": "a", "text": "Me gusta el pan"},
                        {"id": "b", "text": "Me gustan el pan"},
                        {"id": "c", "text": "Tengo pan"},
                        {"id": "d", "text": "Soy pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Eso. El pan — singular — 'me gusta el pan'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Você gosta das laranjas do mercado. Laranjas — várias. Como você diz?",
                    "options": [
                        {"id": "a", "text": "Me gustan las naranjas"},
                        {"id": "b", "text": "Me gusta las naranjas"},
                        {"id": "c", "text": "Tengo naranjas"},
                        {"id": "d", "text": "Soy naranjas"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gustan", "target": "me gustan", "native": "gosto (plural)",
                    "npc_reaction": "Las naranjas — plural — 'me gustan'. El verbo cambia con la cosa, no contigo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Y si no te gusta algo — sólo añade 'no' al principio. Simple.",
                    "translation": "E se você não gosta de algo — só adiciona 'no' no começo. Simples.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "O café estava forte demais essa manhã pra você. Você não gostou. Como você fala?",
                    "options": [
                        {"id": "a", "text": "No me gusta el café"},
                        {"id": "b", "text": "Tengo no café"},
                        {"id": "c", "text": "Soy no café"},
                        {"id": "d", "text": "Adiós café"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_gusta", "target": "no me gusta", "native": "não gosto",
                    "npc_reaction": "Simple. María hace el café muy fuerte. Yo tampoco lo tomo así.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel: 'Forastero — ¿y a ti, te gustan los tomates rojos?' Você gosta. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sí, me gustan"},
                        {"id": "b", "text": "Sí, me gusta"},
                        {"id": "c", "text": "Tengo tomates"},
                        {"id": "d", "text": "Soy tomate"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gustan", "target": "me gustan", "native": "gosto (plural)",
                    "npc_reaction": "Tomates — plural — 'me gustan'. Vas a comer bien aquí.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Tarde no pátio da casa de Don Miguel. Conversa informal entre os quatro.
    # María, sutilmente, faz o protagonista falar mais. Sofía conta histórias
    # da avó. Miguel observa em silêncio. Poucos exercícios, foco em vida.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "Vocês voltaram pra casa de Don Miguel ao meio-dia. Comeram "
                    "as laranjas no pátio, sentados em torno de uma mesa baixa "
                    "de madeira. María partiu os tomates em fatias com a navaja "
                    "pequena que ela carrega.\n\n"
                    "Don Miguel saiu pra trabalhar no campo. Sobrou os quatro "
                    "jovens, sombra da macieira, vento leve, tarde longa."
                ),
                "now": "Conversa real entre os quatro — vocab orgânico, vida normal.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Sofía",
                    "situation": "A mesa baixa do pátio tem tomate fatiado e laranja — mas Sofía olha pra mochila do forastero, curiosa.",
                    "npc_line": "Forastero — ¿tienes algo en la bolsa para sumar a la mesa? Una comida compartida sabe mejor.",
                    "item_tag": "comida",
                    "on_use": {
                        "narrative": "Você tira algo da mochila e põe no centro da mesa baixa. Os quatro dividem — Sofía, Miguel, María e você.",
                        "npc_reaction": "¡Eso! Ahora sí es mesa de verdad. Cuatro personas, una comida — somos grupo.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa — el tomate y la naranja alcanzan. Otra vez será.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Mi abuela tenía una receta de tomates con queso, naranjas y sal. Sonaba raro pero era de lo mejor que comí en mi vida.",
                    "translation": "Minha avó tinha uma receita de tomates com queijo, laranjas e sal. Soava estranho mas era das melhores coisas que comi na vida.",
                },
                {
                    "kind": "narrative",
                    "text": "María corta uma laranja em quatro pedaços. Coloca sal em um. Estende pra Sofía. Sofía come. Faz cara de surpresa, ri alto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "¡Es eso! ¡Exacto! ¿Cómo lo sabías?",
                    "translation": "É isso! Exato! Como você sabia?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Una receta vieja. La aprendí lejos de aquí. Las palabras buenas y las recetas buenas viajan iguales.",
                    "translation": "Uma receita velha. Aprendi longe daqui. As palavras boas e as receitas boas viajam iguais.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María estende um pedaço de laranja com sal pra você. Você prova. Doce, salgado, estranho mas bom. Você diz:",
                    "options": [
                        {"id": "a", "text": "Me gusta"},
                        {"id": "b", "text": "No me gusta"},
                        {"id": "c", "text": "Tengo miedo"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_gusta", "target": "me gusta", "native": "gosto",
                    "npc_reaction": "Bueno. Sabía que te iba a gustar. Algunos sabores se reconocen aunque uno nunca los haya probado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Forastero — ¿todavía tienes la lámpara en el bolsillo? La de mi abuela.",
                    "translation": "Forasteiro — você ainda tem a lamparina no bolso? A da minha avó.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Sofía pergunta sobre a lamparina. Você tira do bolso pra mostrar — quente do sol. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Lámpara"},
                        {"id": "b", "text": "Fuego"},
                        {"id": "c", "text": "Naranja"},
                        {"id": "d", "text": "Pan"},
                    ],
                    "correct": "a",
                    "word_id": "es_lampara", "target": "lámpara", "native": "lamparina",
                    "npc_reaction": "Lámpara. La cargas sin pensar. Eso es bueno — la palabra ya es tuya.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Miguel come em silêncio do lado da macieira. Olha pra "
                        "María de vez em quando — uma fração de segundo. Depois "
                        "volta a olhar pra árvore. Não comenta nada."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Miguel — ¿tú no comes la naranja con sal? ¿No te gusta?",
                    "translation": "Miguel — você não come a laranja com sal? Não gosta?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel olha pra Sofía. Decide responder educado mas honesto: 'No me gusta mezclar. Naranja con naranja, sal con tomate.' Como ele diz que não gosta?",
                    "options": [
                        {"id": "a", "text": "No me gusta"},
                        {"id": "b", "text": "Me gusta"},
                        {"id": "c", "text": "Tengo gusto"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_no_me_gusta", "target": "no me gusta", "native": "não gosto",
                    "npc_reaction": "Cada uno con su receta. Voy a comer mi pan tranquilo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "Forastero — ¿cuántos años tiene tu padre? Si te acuerdas.",
                    "translation": "Forasteiro — quantos anos seu pai tem? Se você lembra.",
                },
                {
                    "kind": "player",
                    "text": "Você não lembra do seu pai. Não lembra de ninguém de antes. A pergunta dói um pouco — mas Sofía perguntou sem maldade.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Sofía",
                    "question": "Você responde a verdade — não tem como mentir sobre isso. A palavra do que você é aqui ainda:",
                    "options": [
                        {"id": "a", "text": "No me acuerdo, soy forastero"},
                        {"id": "b", "text": "Tengo veinte años"},
                        {"id": "c", "text": "Me llamo"},
                        {"id": "d", "text": "Tengo miedo"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Lo siento. No tenía que preguntarte. Olvida.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Silêncio breve. María olha pra Sofía com um aviso silencioso. "
                        "Sofía abaixa a cabeça meio sem graça. Miguel — que tinha "
                        "ouvido tudo — olha pra você de lado e diz baixo:"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Tu padre — el que sea — tiene un hijo bueno. Eso ya es algo.",
                    "translation": "Seu pai — quem quer que seja — tem um filho bom. Isso já é algo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel acabou de dizer algo que tocou em você. Você responde com a palavra que sempre vale:",
                    "options": [
                        {"id": "a", "text": "Gracias, Miguel"},
                        {"id": "b", "text": "Adiós"},
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

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Voltando pra casa no fim da tarde, vocês passam por uma rua estreita.
    # O protagonista vê de longe El Vigilante del Mercado parado, observando.
    # Gate de reação social — você precisa avisar o grupo sem alarmar.
    # Transição direta pra F10 (confronto com Vigilante).
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["María", "Sofía", "Miguel"],
                "story": (
                    "A tarde virou em fim de tarde, fim de tarde em entardecer. "
                    "Vocês recolheram os restos da comida e saíram pra dar "
                    "uma volta pelo pueblo antes do jantar. María queria ver "
                    "alguma loja de tecidos que Carmen tinha mencionado.\n\n"
                    "Caminham por uma rua estreita perto do mercado vazio. "
                    "Vai escurecendo aos poucos."
                ),
                "now": "Você precisa reagir certo a uma situação que só você percebeu.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌆 Rua estreita · Final de tarde · Vocês quatro andando juntos",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você anda do lado de Miguel. Sofía e María à frente "
                        "conversando baixo. Sombras compridas no chão de pedra."
                    ),
                },
                {
                    "kind": "scene",
                    "text": "👤 Uma figura na esquina ao fim da rua — parado, observando. Chapéu baixo. Você reconhece — El Vigilante del Mercado.",
                },
                {
                    "kind": "player",
                    "text": (
                        "Ele te olha de longe. Você lembra o que ele tentou fazer "
                        "no corredor da posada. Ele recuou do fogo — mas voltou. "
                        "Aqui. Agora."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Forastero — ¿qué pasa? ¿Estás bien?",
                    "translation": "Forasteiro — o que foi? Você tá bem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel notou que você parou de andar. Você precisa avisar sem alarmar Sofía e María à frente. Você diz baixo:",
                    "options": [
                        {"id": "a", "text": "Miguel — mira allá. El Vigilante."},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Estoy bien"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_mira", "target": "mira", "native": "olha",
                    "npc_reaction": "Miguel sigue tu mirada. Lo ve. Aprieta la mandíbula. Sin levantar la voz: 'Sigue caminando. No te detengas.'",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "👁️ El Vigilante continua parado. Não se mexe. Apenas observa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "¿Tienes miedo, forastero? Es válido. Sé honesto conmigo.",
                    "translation": "Tá com medo, forasteiro? É válido. Seja honesto comigo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Você sente medo — claro que sente. Não dá pra esconder de Miguel. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sí, tengo miedo"},
                        {"id": "b", "text": "No, estoy bien"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Tengo hambre"},
                    ],
                    "correct": "a",
                    "word_id": "es_miedo", "target": "tengo miedo", "native": "tenho medo",
                    "npc_reaction": "Bueno. Yo también. Quien no tiene miedo aquí es el peligroso — no nosotros.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "María, que ia à frente, para de andar. Como se tivesse sentido — sem ter visto. Vira a cabeça pra atrás.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Miguel — ¿qué pasa? ¿Por qué se quedaron parados?",
                    "translation": "Miguel — o que foi? Por que vocês pararam?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "Miguel se vira pra María. Aponta com o queixo discreto pra esquina. Você decide responder primeiro — sem alarmar Sofía. Você diz:",
                    "options": [
                        {"id": "a", "text": "Hay un hombre allá"},
                        {"id": "b", "text": "Tengo miedo"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_hay", "target": "hay", "native": "tem / há",
                    "npc_reaction": "María sigue tu mirada. Ve a El Vigilante. Su expresión no cambia — pero pone la mano en el hombro de Sofía.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "👁️→ Quando você olha de novo pra esquina, El Vigilante já não está lá. Sumiu sem você ver ele se mover.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Ya se fue. Pero estuvo — los cuatro lo confirmamos.",
                    "translation": "Já foi. Mas esteve — nós quatro confirmamos.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Sofía",
                    "line": "¿Qué? ¿Quién? ¡Yo no vi nada!",
                    "translation": "O quê? Quem? Eu não vi nada!",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "María",
                    "line": "Después te explicamos. Ahora — a la casa. Pronto.",
                    "translation": "Depois explicamos. Agora — pra casa. Rápido.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "María",
                    "question": "María decide que o grupo precisa voltar antes que escureça mais. Pergunta: '¿Tú vienes rápido conmigo, forastero?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, yo voy"},
                        {"id": "b", "text": "No tengo miedo"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Buenos noches"},
                    ],
                    "correct": "a",
                    "word_id": "es_yo_voy", "target": "yo voy", "native": "eu vou",
                    "npc_reaction": "Vamos los cuatro juntos. Nadie atrás, nadie adelante. Línea cerrada.",
                    "gated": True,
                },
                # ── Closing beats — transição pra F10 ───────────────────────
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês andam apertados pelas ruas de pedra de volta pra "
                        "casa. María no centro. Sofía à esquerda. Você no meio. "
                        "Miguel atrás vigiando atrás.\n\n"
                        "Don Miguel já estava na porta esperando — Carmen tinha "
                        "mandado um recado. 'Hablamos adentro.'"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Don Miguel",
                    "line": "Mañana al amanecer vamos a tener que hablar con el Alcalde. El Vigilante ya escaló esto a sus jefes.",
                    "translation": "Amanhã ao amanhecer vamos ter que falar com o Alcalde. El Vigilante já levou isso pros chefes dele.",
                    "pace": "slow",
                },
                {
                    "kind": "scene",
                    "text": "🌙 Noite cai · Os quatro mais Don Miguel sentados em volta da mesa · A lamparina baixa · Conversa difícil",
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
