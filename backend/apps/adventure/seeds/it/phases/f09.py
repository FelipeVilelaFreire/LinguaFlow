"""
Seed das 6 seções da Fase 9 Italiano A1 — "Cuatro a la mesa".

Sem milestone obrigatório — construção do vínculo do grupo de 4.
Necessária pra dar pquesto emocional à traição da T5 (canônico).

Primeira manhã com Lucia na casa. Café fumegante, pão fresco, Chiara rindo.
Lucia conta uma piada e Chiara morre de rir. Nico, ao lado do protagonista,
sussurra: "Esta mujer me da algo raro. No sé qué." — instinto de Nico
sobre Lucia começa aqui (nunca vira acusação até T5).

Lucia leva o grupo ao mercato pra repor mantimentos — usa a saída pra
observar o protagonista falando italiano em contexto real, mensurando
o quanto a língua dele já "pegou". Il Mercante percebe Lucia, troca um
olhar com ela rápido. Pista plantada: outros sabem dela.

Voltando, o protagonista vê de longe La Guardia del Mercato parado na
esquina, observando o grupo. Quando o protagonista repara, ele já foi.

Novos vocab (3): cibo · café · arancia  (revisão de mercato da F4)
Gramática nova: mi piace / no mi piace  (verbos pronominais básicos)
Revisão F1-F8:  números, ¿cuánto cuesta?, mucho/poco, pane, acqua,
                ciao, grazie, sto bene/mejor, ho X años
NPC principais: Os 4 do grupo (protagonista · Nico · Chiara · Lucia)
NPC cameo:      Il Mercante (F4 retorno) · Giulia (cameo) · La Guardia (avistado)
Arco emocional: pertencimento → primeira refeição em família → instinto
                silencioso de Nico ("algo não bate")
Transição:      Guardia avistado de longe → F10 abre com confronto direto

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Primeira manhã com Lucia na casa. Café da manhã com os quatro.
    # Lucia já parece familiar. Chiara rindo. Nico sussurra a primeira
    # desconfiança. Falas sem tradução — imersão.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "☀️ Manhã clara · Mesa da cozinha · Quatro lugares postos\n\n"
                        "Você acorda com cheiro de café. Vozes baixas, paneela "
                        "batendo no fogão. Quando você entra na cozinha, Lucia "
                        "já tá lá — avienital, cabelo prquesto, mãos rápidas. Como "
                        "se sempre tivesse morado ali."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Lucia",
                    "line": "¡Benes días! Hice café fuerte — vas a necesitarlo.",
                    "pace": "normale",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "Forestiero — siéntate. Lucia nos hizo desayuno.",
                },
                {
                    "kind": "narrative",
                    "text": "Chiara senta primeiro, Nico na fronte dela, Lucia na cabeceira. Sobra o lugar do seu lado pra você.",
                },
                {
                    "kind": "npc",
                    "npc": "Nico",
                    "line": "Aquí, forestiero. Te guardé el pane más calda.",
                },
                {
                    "kind": "scene",
                    "text": "??☕ Pão, queijo, café fumegante, uma jarra de água com fatias de laranja. Mesa cheia.",
                },
                {
                    "kind": "npc",
                    "npc": "Lucia",
                    "line": "Chiara — ¿qué hizo Bianca ayer cuando le contaste que me llamaron?",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "Bianca ha detto — '¡Por fin alguien con testa llega al borgo!' Y siguió cosiendo senza levantar la guardada.",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia ri — uma risada genuína, curta, baixa. Chiara morre de rir e quase derruba o café. Nico sorri sem se entregar.",
                },
                {
                    "kind": "npc",
                    "npc": "Nico",
                    "line": "Forestiero — vieni aquí un segundo.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Nico se inclina pro seu lado, conversa baixa enquanto Chiara e Lucia continuam falando alto na outra ponta.",
                },
                {
                    "kind": "npc",
                    "npc": "Nico",
                    "line": "Esta mujer me da algo raro. No sé qué. Ma algo.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": (
                        "Nico não te olha enquanto fala. Bebe o café come se não "
                        "tivesse dito nada. Mas você ouviu."
                    ),
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "cibo",  "native": "cibo"},
                        {"target": "café",    "native": "café"},
                        {"target": "arancia", "native": "laranja"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia põe um prato cheio na sua fronte. Pão, queijo, laranja cortada. 'Esto es...' Como se chama tudo isso junto?",
                    "options": [
                        {"id": "a", "text": "Cibo"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Pane"},
                        {"id": "d", "text": "Lampada"},
                    ],
                    "correct": "a",
                    "word_id": "it_cibo", "target": "cibo", "native": "cibo",
                    "npc_reaction": "Cibo. Lo que el corpo necesita para seguir.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Ela enche sua caneca com o líquido escuro, fumegante e amargo. Você toma um gole. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Café"},
                        {"id": "b", "text": "Acqua"},
                        {"id": "c", "text": "Sal"},
                        {"id": "d", "text": "Pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_caffe", "target": "café", "native": "café",
                    "npc_reaction": "Café. Despierta los muertos. Aquí en el borgo se toma fuerte.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara empurra uma fruta laranja redonda na sua direção. Doce, com cheiro forte. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Naranja"},
                        {"id": "b", "text": "Pane"},
                        {"id": "c", "text": "Café"},
                        {"id": "d", "text": "Fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_arancia", "target": "arancia", "native": "laranja",
                    "npc_reaction": "Naranja. La compramos hoy al mercato. La fresca, no la del día anterior.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico, baixinho, ainda do seu lado: 'Forestiero — ¿cómo estás hoy?' Você responde verdadeiramente — corpo descansado, cabeça limpa:",
                    "options": [
                        {"id": "a", "text": "Sto bene"},
                        {"id": "b", "text": "Sto male"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Andiamo al mercato después del desayuno. Mantente cerca.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ─────────────────────────────────────────────────
    # Saída pra rua. Caminho até o mercato. Revisão pesada de F4 mercato:
    # números, cuánto cuesta, mucho/poco. Chiara testa o protagonista pra
    # ver se ele consegue lidar com o mercato sozinho.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Vocês saíram da casa depois do desayuno. Lucia na fronte — "
                    "ela já parecia conhecer o caminho. Chiara do seu lado, "
                    "Nico atrás. O sol já alto, o borgo cheio.\n\n"
                    "Chiara: 'Mientras llegamos al mercato — repaso. ¿Listo, "
                    "forestiero?'"
                ),
                "now": "Chiara testa seu vocab de mercato enquanto caminham. Rápido.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Si te digo 'una arancia, dos arance' — ¿cómo cuentas hasta cinco?",
                    "translation": "Se eu digo 'uma laranja, duas laranjas' — come você conta até cinco?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta os dedos pra contar: uno, dos, tres... a sequência completa de 1 a 5 é:",
                    "options": [
                        {"id": "a", "text": "uno, dos, tres, cuatro, cinco"},
                        {"id": "b", "text": "uno, dos, tres, cinco, cuatro"},
                        {"id": "c", "text": "uno, dos, dos, tres, cuatro"},
                        {"id": "d", "text": "uno, dos, tres, cuatro, seis"},
                    ],
                    "correct": "a",
                    "word_id": "it_numeros", "target": "uno, dos, tres, cuatro, cinco", "native": "um, dois, três, quatro, cinco",
                    "npc_reaction": "Perfecto. Si pierdes la cuenta — vuelves a empezar. Aquí no se acepta dudar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Y si quieres saber el precio de algo — ¿qué preguntas al vienidedor?",
                    "translation": "E se você quer saber o preço de algo — o que você pergunta ao vienidedor?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você precisa saber quanto custa a laranja. A pergunta certa pro vienidedor é:",
                    "options": [
                        {"id": "a", "text": "¿Cuánto cuesta?"},
                        {"id": "b", "text": "¿Cómo te chiami?"},
                        {"id": "c", "text": "¿Cómo estás?"},
                        {"id": "d", "text": "¿Tu vieni?"},
                    ],
                    "correct": "a",
                    "word_id": "it_cuanto_cuesta", "target": "¿cuánto cuesta?", "native": "quanto custa?",
                    "npc_reaction": "Exacto. Y si el precio te parece alto — ya te enseñé qué hacer.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Y si encuentras algo que cuesta una sola moneda — ¿es 'mucho' o 'poco'?",
                    "translation": "E se você acha algo que custa só uma moeda — é 'muito' ou 'pouco'?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Uma moeda só por uma laranja gorda — preço bom. Como você fala isso?",
                    "options": [
                        {"id": "a", "text": "Poco"},
                        {"id": "b", "text": "Mucho"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Buen precio. Lo llevas senza dudar.",
                },
                {
                    "kind": "narrative",
                    "text": "Vocês entram na praça do mercato. Bancas coloridas, vienidedores gritando, cheiro de fruta no ar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Allá — la banca del Mercante. El de las arance. Lo conoces, ¿verdad?",
                    "translation": "Ali — a banca do Mercante. O das laranjas. Você conhece, né?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Você lembra do Mercante da F4. Como você cumprimenta um vienidedor ao chegar na banca dele de manhã?",
                    "options": [
                        {"id": "a", "text": "¡Benes días!"},
                        {"id": "b", "text": "¡Adiós!"},
                        {"id": "c", "text": "¡Male!"},
                        {"id": "d", "text": "¡Ho paura!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Esatto. Y él va a responder igual. Es lo educado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Vado a esperar acá. Tu entras a la banca. Pide tres arance tu mismo.",
                    "translation": "Vou esperar aqui. Você entra na banca. Pede três laranjas você mesmo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Você vai sozinho. O Mercante olha pra você esperando. Você pede o que quer:",
                    "options": [
                        {"id": "a", "text": "Quiero tres arance, por favor"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Adiós, mercader"},
                        {"id": "d", "text": "Sono forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_quiero", "target": "quiero", "native": "eu quero",
                    "npc_reaction": "Esatto. Pide directo, senza disculparte. Aquí pedir bene es respetarse a sí mismo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Mercante",
                    "line": "Tres arance, giovane. Dos monedas.",
                    "translation": "Três laranjas, jovem. Duas moedas.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Mercante",
                    "question": "Duas moedas por três laranjas. Preço justo. Você diz a palavra que combina com o preço:",
                    "options": [
                        {"id": "a", "text": "Está bene"},
                        {"id": "b", "text": "Muy caro"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Buen trato. Ya hablas come gente de aquí.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # Dentro do mercato. Lucia testando o protagonista subtilmente — quer ver
    # quão rápido o dom dele 'pegou' a língua. Cada exercício é uma situação
    # real do mercato. Mercante percebe Lucia — troca de olhar rápido.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Você pagou as três laranjas. Chiara aprovou de longe com o "
                    "polegar. Nico já tinha conseguido sale de outra banca. "
                    "Lucia — que ficou um pouco atrás — chegou agora, examinando "
                    "frutas em silêncio.\n\n"
                    "Ela observa você mais do que observa os pomodori. Você nota — "
                    "piu não pesa muito."
                ),
                "now": "Prática intensa — situações reais de mercato uma atrás da outra.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Forestiero — ¿puedes pedirme pomodori allá?Cinco, los rojos.",
                    "translation": "Forasteiro — pode pedir pomodori ali pra mim?Cinco, os vermelhos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vienidedora",
                    "question": "Você chega na banca dos pomodori. Uma mulher idosa, mãos enrugadas. Você cumprimenta prima de pedir:",
                    "options": [
                        {"id": "a", "text": "¡Benes días, señora!"},
                        {"id": "b", "text": "¡Adiós!"},
                        {"id": "c", "text": "¡Male!"},
                        {"id": "d", "text": "¡Forestiero!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Benes días, giovane. ¿Qué te llevas hoy?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vienidedora",
                    "question": "A vienidedora espera. Lucia quer cinco pomodori. Como você pede?",
                    "options": [
                        {"id": "a", "text": "Quiero cinco pomodori, por favor"},
                        {"id": "b", "text": "Ho cinco pomodori"},
                        {"id": "c", "text": "Sono cinco"},
                        {"id": "d", "text": "Mañana cinco"},
                    ],
                    "correct": "a",
                    "word_id": "it_quiero", "target": "quiero", "native": "eu quero",
                    "npc_reaction": "Cinco pomodori. Aquí están — los más maduros. Una moneda.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vienidedora",
                    "question": "Uma moeda só por cinco pomodori?Você compara com o preço da laranja. É:",
                    "options": [
                        {"id": "a", "text": "Poco"},
                        {"id": "b", "text": "Mucho"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Mejor"},
                    ],
                    "correct": "a",
                    "word_id": "it_poco", "target": "poco", "native": "pouco",
                    "npc_reaction": "Poco. Hoy hay mucho pomodoro, todos bajaron el precio.",
                },
                {
                    "kind": "narrative",
                    "text": "Você paga, pega os pomodori num paneo dobrado. Volta pra Lucia. Ela aceita com um sorriso pequeno — piu os olhos dela vão pra outra banca enquanto sorri.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "¿Y la testa hoy?¿Te sigue molestando?",
                    "translation": "E a cabeça hoje?Continua incomedando?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Sua cabeça tá leve hoje — diferente da noite da febbre. Você responde com a palavra que aprendeu com ela:",
                    "options": [
                        {"id": "a", "text": "Sto meglio"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Sto male"},
                        {"id": "d", "text": "Ho años"},
                    ],
                    "correct": "a",
                    "word_id": "it_mejor", "target": "mejor", "native": "melhor",
                    "npc_reaction": "Mejor. La testa vuelve a ser tuya con descanso y cibo buena.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Guarda — ahí está el Mercante otra vez. ¿Te acuerdas de él?",
                    "translation": "Olha — ali tá o Mercante de novo. Você lembra dele?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Mercante",
                    "question": "Il Mercante te vê passando. Acena com a cabeça. Você cumprimenta de volta:",
                    "options": [
                        {"id": "a", "text": "¡Ciao!"},
                        {"id": "b", "text": "¡Male!"},
                        {"id": "c", "text": "¡Adiós!"},
                        {"id": "d", "text": "¡Buona notte!"},
                    ],
                    "correct": "a",
                    "word_id": "it_ciao", "target": "ciao", "native": "olá",
                    "npc_reaction": "Ciao, giovane. Veo que andas en buena compañía hoy.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Il Mercante olha pra Lucia. Lucia olha pra Il Mercante. "
                        "Por meio segundo — silêncio entre eles. Depois ela sorri, "
                        "ele continua organizando frutas, e a cena se desfaz come "
                        "se nada tivesse acontecido.\n\n"
                        "Você notou. Não tem come saber ainda o que significa."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Forestiero — andiamo a la fuente. Ho sete después de esta caminata.",
                    "translation": "Forasteiro — andiamo pra fonte. Tô com sede depois dessa caminhada.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara espera você dizer também o que precisa. Você confirma o que sente:",
                    "options": [
                        {"id": "a", "text": "Yo también ho sete"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Sto male"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Andiamo los cuatro. La fuente está cerca.",
                },
                {
                    "kind": "scene",
                    "text": "⛲ A fonte de pedra do centro da piazza. Vocês param pra beber água — Lucia faz copo com as mãos. Nico bebe direto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Forestiero — ¿qué piensas del mercato?¿Te gustó?",
                    "translation": "Forasteiro — o que você acha do mercato?Você gostou?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Você gostou — gente, cheiro, vida. Como você diz isso?",
                    "options": [
                        {"id": "a", "text": "Sí, mi piace"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Sto male"},
                        {"id": "d", "text": "Sono mercato"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto / eu gosto",
                    "npc_reaction": "Bene. A todos nos gusta. Aunque a veces es ruidoso de más.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "¿Y el café que Lucia hizo esta mañana?¿Te gustó también?",
                    "translation": "E o café que Lucia fez essa manhã?Você gostou também?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "O café estava muito forte pro seu gosto — amargo demais. Honesto, você diz:",
                    "options": [
                        {"id": "a", "text": "Non mi piace"},
                        {"id": "b", "text": "Mi piace mucho"},
                        {"id": "c", "text": "Ho café"},
                        {"id": "d", "text": "Sono café"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_me_gusta", "target": "no mi piace", "native": "não gosto",
                    "npc_reaction": "Bene — honesto. Mañana hago menos fuerte. Ma el café del borgo es así, te acostumbras.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia olha pra você esperando. Pergunta direta: 'Y la arancia del Mercante — ¿te gustó?' A laranja era doce, suculenta. Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, mi piace mucho"},
                        {"id": "b", "text": "Non mi piace nada"},
                        {"id": "c", "text": "Ho arancia"},
                        {"id": "d", "text": "Adiós arancia"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto / eu gosto",
                    "npc_reaction": "Bene. La arancia del borgo es la mejor — no acepto otra opinión.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara começa a cantar baixinho uma música do borgo. Você ouve. Não conhece — piu gosta. Você diz:",
                    "options": [
                        {"id": "a", "text": "Mi piace esa canción"},
                        {"id": "b", "text": "Ho canción"},
                        {"id": "c", "text": "Sto canción"},
                        {"id": "d", "text": "Adiós canción"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto / eu gosto",
                    "npc_reaction": "Es vieja, del borgo. Te la enseño otro día completa.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Voltando do mercato, sentados na sombra de uma árvore. Lucia explica
    # 'mi piace' / 'no mi piace' formalemente, agora que o protagonista já
    # usou os dois sem perceber. Pratica simples.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Voltando da fonte vocês sentaram sob uma árvore antiga "
                    "perto da iglesia. Sombra fresca, vienito leve. Pomodori, "
                    "laranjas, sale — tudo na cesta de Nico.\n\n"
                    "Lucia: 'Guarda — ya hai detto 'mi piace' tres veces senza "
                    "darte cuenta. Vado a explicarte cómo funciona.'"
                ),
                "now": "Lucia vai explicar formalemente o que você já tava usando.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "'Mi piace' es raro — no es come 'ho' o 'sto'. Es come decir 'a mí me agrada questo'. La cosa actua sobre ti, no tu sobre la cosa.",
                    "translation": "'Mi piace' é diferente — não é come 'ho' ou 'sto'. É come dizer 'isso me agrada'. A coisa age sobre você, não você sobre a coisa.",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Mi piace + cosa senzagular",
                    "meaning": "Eu gosto disso (lit: 'isso me agrada')",
                    "note": "se for uma coisa só, sempre 'mi piace': mi piace el pane",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Si la cosa es plural — 'arance', muchas — entonces 'mi piacen'. Las arance actuan en plural sobre ti.",
                    "translation": "Se a coisa é plural — 'laranjas', muitas — então 'mi piacen'. As laranjas agem no plural sobre você.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Mi piacen + cose plurales",
                    "meaning": "Eu gosto delas (plural)",
                    "note": "mi piacen las arance, mi piacen los pomodori",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Mi piace",   "isKey": True},
                        {"text": " el café / ", "isKey": False},
                        {"text": "Mi piacen",  "isKey": True},
                        {"text": " las arance", "isKey": False},
                    ],
                    "example": "Mi piace el café. Mi piacen las arance. Non mi piace el café muy fuerte.",
                    "translation": "Eu gosto do café. Eu gosto das laranjas. Não gosto do café muito forte.",
                    "note": "senzagular: mi piace | plural: mi piacen | negar: 'no' prima de tudo",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você gosta do pão de Giulia. Pão é uma coisa só. Como você diz?",
                    "options": [
                        {"id": "a", "text": "Mi piace el pane"},
                        {"id": "b", "text": "Mi piacen el pane"},
                        {"id": "c", "text": "Ho pane"},
                        {"id": "d", "text": "Sono pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto",
                    "npc_reaction": "Esatto. El pane — senzagular — 'mi piace el pane'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Você gosta das laranjas do mercato. Laranjas — várias. Como você diz?",
                    "options": [
                        {"id": "a", "text": "Mi piacen las arance"},
                        {"id": "b", "text": "Mi piace las arance"},
                        {"id": "c", "text": "Ho arance"},
                        {"id": "d", "text": "Sono arance"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gustan", "target": "mi piacen", "native": "gosto (plural)",
                    "npc_reaction": "Las arance — plural — 'mi piacen'. El verbo cambia con la cosa, no con te.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Y si no te gusta algo — sólo añade 'no' al principio. Simple.",
                    "translation": "E se você não gosta de algo — só adiciona 'no' no começo. Simples.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "O café estava forte demais essa manhã pra você. Você não gostou. Como você fala?",
                    "options": [
                        {"id": "a", "text": "Non mi piace el café"},
                        {"id": "b", "text": "Ho no café"},
                        {"id": "c", "text": "Sono no café"},
                        {"id": "d", "text": "Adiós café"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_me_gusta", "target": "no mi piace", "native": "não gosto",
                    "npc_reaction": "Simple. Lucia hace el café muy fuerte. Yo tampoco lo tomo así.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico: 'Forestiero — ¿y a ti, te gustan los pomodori rojos?' Você gosta. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sí, mi piacen"},
                        {"id": "b", "text": "Sí, mi piace"},
                        {"id": "c", "text": "Ho pomodori"},
                        {"id": "d", "text": "Sono pomodoro"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gustan", "target": "mi piacen", "native": "gosto (plural)",
                    "npc_reaction": "Pomodori — plural — 'mi piacen'. Vas a comer bene aquí.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Tarde no pátio da casa de Antonio il Contadino. Conversa informale entre os quatro.
    # Lucia, sutilmente, faz o protagonista falar mais. Chiara conta histórias
    # da avó. Nico observa em silêncio. Poucos exercícios, foco em vida.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "Vocês voltaram pra casa de Antonio il Contadino ao meio-dia. Comeram "
                    "as laranjas no pátio, sentados em torno de uma mesa baixa "
                    "de madeira. Lucia partiu os pomodori em fatias com a navaja "
                    "pequena que ela carrega.\n\n"
                    "Antonio il Contadino saiu pra trabalhar no campo. Sobrou os quatro "
                    "giovanes, sombra da macieira, vienito leve, tarde longa."
                ),
                "now": "Conversa real entre os quatro — vocab orgânico, vida normale.",
            },
            "steps": [
                {
                    "kind": "item_moment",
                    "npc": "Chiara",
                    "situation": "A mesa baixa do pátio tem pomodoro fatiado e laranja — piu Chiara olha pra mochila do forestiero, curiosa.",
                    "npc_line": "Forestiero — ¿hai algo en la bolsa para sumar a la mesa?Una cibo compartida sabe mejor.",
                    "item_tag": "comida",
                    "on_use": {
                        "narrative": "Você tira algo da mochila e põe no centro da mesa baixa. Os quatro dividem — Chiara, Nico, Lucia e você.",
                        "npc_reaction": "¡Esatto! Adesso sí es mesa de verdad. Cuatro personas, una cibo — somos grupo.",
                        "bonus": "relationship_boost",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa — el pomodoro y la arancia alcanzan. Otra vez será.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Mi nonna tenía una receta de pomodori con ququesto, arance y sale. Sonaba raro ma era de lo mejor que comí en mi vida.",
                    "translation": "Minha avó tinha uma receita de pomodori com queijo, laranjas e sale. Soava estranho piu era das melhores coisas que comi na vida.",
                },
                {
                    "kind": "narrative",
                    "text": "Lucia corta uma laranja em quatro pedaços. Coloca sale em um. Estende pra Chiara. Chiara come. Faz cara de surpresa, ri alto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "¡Es questo! ¡Exacto! ¿Cómo lo sabías?",
                    "translation": "É isso! Exato! Como você sabia?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Una receta vieja. La aprendí lejos de aquí. Las parole buenas y las recetas buenas viajan iguales.",
                    "translation": "Uma receita velha. Aprendi longe daqui. As palavras boas e as receitas boas viajam iguais.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia estende um pedaço de laranja com sale pra você. Você prova. Doce, salegado, estranho piu bom. Você diz:",
                    "options": [
                        {"id": "a", "text": "Mi piace"},
                        {"id": "b", "text": "Non mi piace"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_gusta", "target": "mi piace", "native": "gosto",
                    "npc_reaction": "Bene. Sabía que te iba a gustar. Algunos sabores se reconocen ancoraque uno nunca los haya probado.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Forestiero — ¿todavía hai la lampada en el bolsillo?La de mi nonna.",
                    "translation": "Forasteiro — você ainda tem a lamparina no bolso?A da minha avó.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara pergunta sobre a lamparina. Você tira do bolso pra mostrar — quente do sol. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Lampada"},
                        {"id": "b", "text": "Fuoco"},
                        {"id": "c", "text": "Naranja"},
                        {"id": "d", "text": "Pane"},
                    ],
                    "correct": "a",
                    "word_id": "it_lampada", "target": "lampada", "native": "lamparina",
                    "npc_reaction": "Lampada. La cargas senza pensar. Esatto es bene — la palabra ya es tuya.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Nico come em silêncio do lado da macieira. Olha pra "
                        "Lucia de vez em quando — uma fração de segundo. Depois "
                        "volta a olhar pra árvore. Não comenta nada."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Nico — ¿tu no comes la arancia con sale?¿No te gusta?",
                    "translation": "Nico — você não come a laranja com sale?Não gosta?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico olha pra Chiara. Decide responder educado piu honesto: 'Non mi piace mezclar. Naranja con arancia, sale con pomodoro.' Como ele diz que não gosta?",
                    "options": [
                        {"id": "a", "text": "Non mi piace"},
                        {"id": "b", "text": "Mi piace"},
                        {"id": "c", "text": "Ho gusto"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_no_me_gusta", "target": "no mi piace", "native": "não gosto",
                    "npc_reaction": "Cada uno con su receta. Vado a comer mi pane tranquilo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Forestiero — ¿cuántos años ha tu padre?Si te acuerdas.",
                    "translation": "Forasteiro — quantos anni seu pai tem?Se você lembra.",
                },
                {
                    "kind": "player",
                    "text": "Você não lembra do seu pai. Não lembra de ninguém de prima. A pergunta dói um pouco — piu Chiara perguntou sem maledade.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Você responde a verdade — não tem come mentir sobre isso. A palavra do que você é aqui ainda:",
                    "options": [
                        {"id": "a", "text": "Non ricordo, sono forestiero"},
                        {"id": "b", "text": "Ho veinte años"},
                        {"id": "c", "text": "Mi chiamo"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_forestiero", "target": "forestiero", "native": "estrangeiro",
                    "npc_reaction": "Lo siento. No tenía que preguntarte. Olvida.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Silêncio breve. Lucia olha pra Chiara com um aviso silencioso. "
                        "Chiara abaixa a cabeça meio sem graça. Nico — que tinha "
                        "ouvido tudo — olha pra você de lado e diz baixo:"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Tu padre — el que sea — ha un hijo bene. Esatto ya es algo.",
                    "translation": "Seu pai — quem quer que seja — tem um filho bom. Isso já é algo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico acabou de dizer algo que tocou em você. Você responde com a palavra que sempre vale:",
                    "options": [
                        {"id": "a", "text": "Grazie, Nico"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada, hermano. Esatto es lo que pienso.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Voltando pra casa no fim da tarde, vocês passam por uma rua estreita.
    # O protagonista vê de longe La Guardia del Mercato parado, observando.
    # Gate de reação social — você precisa avisar o grupo sem alarmar.
    # Transição direta pra F10 (confronto com Guardia).
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Lucia", "Chiara", "Nico"],
                "story": (
                    "A tarde virou em fim de tarde, fim de tarde em entardecer. "
                    "Vocês recolheram os restos da cibo e saíram pra dar "
                    "uma volta pelo borgo prima do jantar. Lucia queria ver "
                    "alguma loja de tecidos que Bianca tinha mencionado.\n\n"
                    "Caminham por uma rua estreita perto do mercato vazio. "
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
                        "Você anda do lado de Nico. Chiara e Lucia à fronte "
                        "conversando baixo. Sombras compridas no chão de pedra."
                    ),
                },
                {
                    "kind": "scene",
                    "text": "👤 Uma figura na esquina ao fim da rua — parado, observando. Chapéu baixo. Você reconhece — La Guardia del Mercato.",
                },
                {
                    "kind": "player",
                    "text": (
                        "Ele te olha de longe. Você lembra o que ele tentou fazer "
                        "no corredor da locanda. Ele recuou do fogo — piu voltou. "
                        "Aqui. Agora."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Forestiero — ¿qué pasa?¿Estás bene?",
                    "translation": "Forasteiro — o que foi?Você tá bem?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico notou que você parou de andar. Você precisa avisar sem alarmar Chiara e Lucia à fronte. Você diz baixo:",
                    "options": [
                        {"id": "a", "text": "Nico — guarda allá. La Guardia."},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Sto bene"},
                        {"id": "d", "text": "Benes nottes"},
                    ],
                    "correct": "a",
                    "word_id": "it_guarda", "target": "guarda", "native": "olha",
                    "npc_reaction": "Nico sigue tu guardada. Lo ve. Aprieta la mandíbula. Senza levantar la voz: 'Sigue caminando. No te detengas.'",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "??? La Guardia continua parado. Não se mexe. Apenas observa.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "¿Hai paura, forestiero?Es válido. Sé honesto con me.",
                    "translation": "Tá com medo, forasteiro?É válido. Seja honesto comigo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Você sente medo — claro que sente. Não dá pra esconder de Nico. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sí, ho paura"},
                        {"id": "b", "text": "No, sto bene"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "ho paura", "native": "tenho medo",
                    "npc_reaction": "Bene. Yo también. Quien no ha paura aquí es el peligroso — no noi.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": "Lucia, que ia à fronte, para de andar. Como se tivesse sentido — sem ter visto. Vira a cabeça pra atrás.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Nico — ¿qué pasa?¿Por qué se quedaron parados?",
                    "translation": "Nico — o que foi?Por que vocês pararam?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Nico se vira pra Lucia. Aponta com o queixo discreto pra esquina. Você decide responder primeiro — sem alarmar Chiara. Você diz:",
                    "options": [
                        {"id": "a", "text": "Hay un hombre allá"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Benes nottes"},
                    ],
                    "correct": "a",
                    "word_id": "it_hay", "target": "hay", "native": "tem / há",
                    "npc_reaction": "Lucia sigue tu guardada. Ve a La Guardia. Su expresión no cambia — ma pone la mano en el hombro de Chiara.",
                    "gated": True,
                },
                {
                    "kind": "scene",
                    "text": "???→ Quando você olha de novo pra esquina, La Guardia já não está lá. Sumiu sem você ver ele se mover.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Ya se fue. Ma estuvo — los cuatro lo confirmamos.",
                    "translation": "Já foi. Mas esteve — nós quatro confirmamos.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "¿Qué?¿Quién?¡Yo no vi nada!",
                    "translation": "O quê?Quem?Eu não vi nada!",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Lucia",
                    "line": "Después te explicamos. Adesso — a la casa. Pronto.",
                    "translation": "Depois explicamos. Agora — pra casa. Rápido.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Lucia",
                    "question": "Lucia decide que o grupo precisa voltar prima que escureça mais. Pergunta: '¿Tu vieni rápido con me, forestiero?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado"},
                        {"id": "b", "text": "Non ho paura"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Benes nottes"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Andiamo los cuatro juntos. Nadie atrás, nadie adelante. Línea cerrada.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F10 ───────────────────────
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês andam apertados pelas ruas de pedra de volta pra "
                        "casa. Lucia no centro. Chiara à esquerda. Você no meio. "
                        "Nico atrás vigiando atrás.\n\n"
                        "Antonio il Contadino já estava na porta esperando — Bianca tinha "
                        "mandado um recado. 'Hablamos adentro.'"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio il Contadino",
                    "line": "Mañana al amanecer andiamo a tener que hablar con el Podesta. La Guardia ya escaló esto a sus jefes.",
                    "translation": "Amanhã ao amanhecer andiamo ter que falar com o Podesta. La Guardia já levou isso pros chefes dele.",
                    "pace": "slow",
                },
                {
                    "kind": "scene",
                    "text": "🌙 Noite cai · Os quatro mais Antonio il Contadino sentados em volta da mesa · A lamparina baixa · Conversa difícil",
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




