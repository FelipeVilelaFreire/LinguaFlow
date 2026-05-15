"""
Seed das 6 seções da Fase 7 Italiano A1 — "El día normale".

Fase de respiração — falsa normaleidade. Depois da noite do dom (F5) e da
entrada da Chiara (F6), o grupo decide passar um dia inteiro come se nada
tivesse acontecido. Chiara aparece na piazza come amiga de anni. Nico
leva o grupo a Bianca pra aprender a 'viver come gente daqui'. Bianca
ensenzaa perguntar idade.

No final da fase: febre. Chiara sussurra sobre a 'dor de cabeça da primeira
vez'. O dom tem custo físico. Nico sai à noite buscar uma guaritrice.

Novos vocab (3): hoy · mañana · vecino
Gramática nova:  tener + idade  (ho veinte años)
Revisão F1-F6:   saudações, ¿cómo estás?, mi chiamo, grazie, luce, io vado
NPC principais:  Chiara (no grupo agora) · Nico · Bianca (reaparece)
Cameo:           Giulia (acena)
Arco emocional:  alívio engannio → primeira pontada de fadiga
Transição:       febre → Nico sai pela rua escura buscar Lucia (F8)

Pré-requisito: python manage.py seed_it
Uso:           python manage.py seed_it_sections [--reset]
"""

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Manhã na piazza. Chiara aparece come se nada tivesse acontecido — alegre,
    # rápida, falando alto. O grupo decide gastar o dia em coisas pequenas.
    # Cameo de Giulia na padaria. Imersão — falas dos NPCs sem tradução.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": (
                        "🌅 Piazza central · Manhã clara · Dia depois\n\n"
                        "O sol já está alto. Cheiro de pão da padaria de Giulia, "
                        "vozes de mulheres no mercato, criança correndo atrás "
                        "de um cão. San Cristóbal acordou inteiro."
                    ),
                },
                {
                    "kind": "skill_check",
                    "skill": "persuasao",
                    "min_level": 1,
                    "uses_item_tag": "moneda",
                    "success": "Voce escolhe a palavra e o gesto certos; a resistencia baixa um pouco.",
                    "fallback": "A conversa nao abre de imediato, mas Nico segura o clima e a historia continua.",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "¡Forestiero! ¡Aquí estás! ¿Dormiste algo?",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": (
                        "Chiara aparece da esquina come se vocês fossem amigos há "
                        "anni. Nenhuma menção da noite anterior. Nenhum pquesto na cara."
                    ),
                },
                {
                    "kind": "npc",
                    "npc": "Nico",
                    "line": "Benes días. Hoy nada raro, ¿eh?Sólo borgo.",
                    "pace": "normale",
                },
                {
                    "kind": "narrative",
                    "text": "Nico chega devagar. Olhos cansados de quem não dormiu direito — piu sorriso firme.",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "Hai que aprender a vivir aquí come gente normale. Hoy te enseño.",
                },
                {
                    "kind": "scene",
                    "text": "?? Giulia na porta da padaria, farinha nas mãos, acena ao ver vocês.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "¡Benes días, hijos! ¡El pane está calda!",
                },
                {
                    "kind": "player",
                    "text": "Giulia estende três pães pequenos pra Chiara. Não cobra. Chiara sorri e devolve um aceno.",
                },
                {
                    "kind": "npc",
                    "npc": "Chiara",
                    "line": "¡Grazie, Giulia! Que tengas un buen día.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "hoy",     "native": "hoje"},
                        {"target": "mañana",  "native": "amanhã / manhã"},
                        {"target": "vecino",  "native": "vizinho"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara estende um pão pra você dizendo 'Cómete esto. Aún senza almuerzo, ¿no?'. Você diz:",
                    "options": [
                        {"id": "a", "text": "Grazie"},
                        {"id": "b", "text": "Adiós"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada, forestiero. Hoy comemos juntos.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pro sol. 'Es...' — Qual palavra ela usa pra dizer 'hoje'?",
                    "options": [
                        {"id": "a", "text": "Hoy"},
                        {"id": "b", "text": "Mañana"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_hoy", "target": "hoy", "native": "hoje",
                    "npc_reaction": "Hoy. El día que estamos viviendo adesso mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Um senhor da casa ao lado passa de bicicleta e acena. Nico: 'Es nuestro...' — quem é esse senhor pra Nico?",
                    "options": [
                        {"id": "a", "text": "Vecino"},
                        {"id": "b", "text": "Forestiero"},
                        {"id": "c", "text": "Campesenzao"},
                        {"id": "d", "text": "Padre"},
                    ],
                    "correct": "a",
                    "word_id": "it_vecino", "target": "vecino", "native": "vizinho",
                    "npc_reaction": "Vecino. Vive en la casa de al lado. Lo conozco desde niño.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara diz 'Bianca está cosiendo en la piazza. ¿Andiamo a verla?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado"},
                        {"id": "b", "text": "No ho fame"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Benes nottes"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Vale. Andiamo los tres.",
                },
            ],
        },
    },

    # ── Seção 2: Revisão SRS ─────────────────────────────────────────────────
    # Caminhada pela piazza. Vizinhos cumprimentam. Revisão de saudações,
    # nome, estado físico — F1 vocab em múltiplas situações reais. Chiara e
    # Nico se revezam testando.
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Chiara", "Nico"],
                "story": (
                    "Vocês caminham pra Bianca. Pelo caminho, Chiara decide testar "
                    "se 'el borgo conoce al forestiero ya o no'. Aponta pessoas, "
                    "espera que você cumprimente cada uma."
                ),
                "now": "Pratique cumprimentos vivos — uma rua cheia de vizinhos.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Guarda — son las nueve. Aún es mañana. ¿Cómo saleudas?",
                    "translation": "Olha — são nove horas. Ainda é manhã. Como você cumprimenta?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Uma vizinha de Chiara passa carregando uma cesta. Sol da manhã, dia novo. Você diz:",
                    "options": [
                        {"id": "a", "text": "¡Benes días!"},
                        {"id": "b", "text": "¡Buon pomeriggio!"},
                        {"id": "c", "text": "¡Buona notte!"},
                        {"id": "d", "text": "¡Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buongiorno", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Bene. Lei va a recordar tu cara.",
                },
                {
                    "kind": "narrative",
                    "text": "A vizinha sorri pra você e responde com a mesma saudação. Continua o caminho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Adesso ese señor — el del sombrero — te va a preguntar tu nombre. Te aviso.",
                    "translation": "Agora aquele senhor — o do chapéu — vai te perguntar seu nome. Te aviso.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Vecino",
                    "line": "Benes días, giovane. ¿Cómo te chiami?Eres nuevo aquí, ¿no?",
                    "translation": "Bom dia, jovem. Como você se chama?Você é novo aqui, né?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecino",
                    "question": "O senhor para na sua fronte, olhando educado. Quer saber seu nome. Você responde:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Bene, grazie"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto. Io sono Pietro. Ho la herrería al fondo de la strada.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecino",
                    "question": "Pietro se apresentou: 'Io sono Pietro.' Para descrever a profissão dele que ele mencionou — ferreiro — você completa: 'Pietro ___ herrero.'",
                    "options": [
                        {"id": "a", "text": "es"},
                        {"id": "b", "text": "ha"},
                        {"id": "c", "text": "está"},
                        {"id": "d", "text": "vado"},
                    ],
                    "correct": "a",
                    "word_id": "it_es", "target": "es", "native": "é (de SER, ele/ela)",
                    "npc_reaction": "Pietro es herrero. 'Es' es 'sono' cuando hablamos de otra persona. Sono yo, eres tu, es él.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Adesso él te va a preguntar si te gusta el borgo. ¿Cómo le respondes?",
                    "translation": "Agora ele vai te perguntar come você está. Como você responde?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Vecino",
                    "question": "'¿Y cómo estás hoy, giovane?¿El borgo te trata bene?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho sete"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene. Si necesitas algo de hierro o herramienta — ya sabes dónde sto.",
                },
                {
                    "kind": "narrative",
                    "text": "Pietro o ferreiro acena e segue. Nico ri baixinho: 'Te lo dije.'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Andiamo por el otro lado de la piazza. Más vecinos para conocer.",
                    "translation": "Andiamo pelo outro lado da piazza. Mais vizinhos pra conhecer.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Uma criança passa correndo, para de repente, te olha e ri. Você cumprimenta de volta:",
                    "options": [
                        {"id": "a", "text": "¡Ciao!"},
                        {"id": "b", "text": "¡Adiós!"},
                        {"id": "c", "text": "¡Male!"},
                        {"id": "d", "text": "¡Forestiero!"},
                    ],
                    "correct": "a",
                    "word_id": "it_ciao", "target": "ciao", "native": "olá",
                    "npc_reaction": "Ciao. Simple. La niña ya te aceptó.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Y si alguien te da algo en este borgo — ¿qué dices siempre?",
                    "translation": "E se alguém te dá algo nesse borgo — o que você fala sempre?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara te dá metade do pão que sobrou da Giulia. Quente ainda. Você diz:",
                    "options": [
                        {"id": "a", "text": "Grazie"},
                        {"id": "b", "text": "Ciao"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada, forestiero. Tu harías lo mismo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pro outro lado da piazza: 'Bianca está allá, sentada en su banco.' Você caminha pra lá. Chiara pergunta: '¿Tu vieni con me?' Você:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Male"},
                        {"id": "d", "text": "Ho sete"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Andiamo juntos. Bianca va a estar feliz de verte de nuevo.",
                },
            ],
        },
    },

    # ── Seção 3: Prática Aplicada ──────────────────────────────────────────────
    # No banco da Bianca. Bianca pergunta sobre o forestiero. Chiara e Nico
    # respondem por ele às vezes, piu o protagonista também fala. Rapid-fire.
    {
        "section_number": 3,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Chiara", "Nico"],
                "story": (
                    "Bianca tá no banco de pedra com o bordado, come sempre. Ergue "
                    "os óculos pequenos do nariz ao ver vocês três chegando.\n\n"
                    "'¡Ciao, hijos! ¡Y tu — el forestiero! ¿Cómo estás hoy?'"
                ),
                "now": "Bianca vai fazer várias perguntas — você responde sem hesitar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "¡Ciao, giovane! ¿Cómo estás hoy?Te ves más asentado que ayer.",
                    "translation": "Olá, jovem! Como você está hoje?Tá com cara mais firme que ontem.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Você dormiu pouco, piu comeu pão da Giulia e tá na sombra da piazza. Bianca quer uma resposta direta:",
                    "options": [
                        {"id": "a", "text": "Bene, grazie"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Me alegro. Siéntate aquí, déjame verte.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Ya sé tu nombre — Chiara me lo ha detto. Ma quiero oírlo de tu boca.",
                    "translation": "Já sei seu nome — Chiara me falou. Mas quero ouvir da sua boca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca larga o bordado e te olha de fronte. Quer ouvir seu nome dito por você.",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Sono forestiero"},
                        {"id": "c", "text": "Bene, grazie"},
                        {"id": "d", "text": "Ho sete"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_chiamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto, hijo. Ya eres parte de la piazza.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "¿Y de dónde vieni, giovane?¿Es lejos?",
                    "translation": "E de onde você vem, jovem?É longe?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Você não lembra de onde vem — é a verdade. Mas Bianca sabe que você é de fora. Você responde:",
                    "options": [
                        {"id": "a", "text": "Sono forestiero"},
                        {"id": "b", "text": "Sono campesenzao"},
                        {"id": "c", "text": "Sono vecino"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_forestiero", "target": "forestiero", "native": "estrangeiro",
                    "npc_reaction": "Forestiero. Aquí los recibimos, hijo. Si te quedas, dejas de ser forestiero pronto.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Chiara senta no chão de pernas cruzadas perto do banco. "
                        "Nico apoia no muro atrás. Bianca volta ao bordado, "
                        "piu continua falando."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Chiara, ¿le diste pane hoy?",
                    "translation": "Chiara, você deu pão pra ele hoje?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara olha pra você esperando que você responda por ela. Você diz pra Bianca:",
                    "options": [
                        {"id": "a", "text": "Sí, grazie"},
                        {"id": "b", "text": "No, male"},
                        {"id": "c", "text": "Adiós Bianca"},
                        {"id": "d", "text": "Forestiero"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Bene. Aquí no se anda con fame.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "¿Hai sed, hijo?Hay acqua del pozo fresca.",
                    "translation": "Você tá com sede, filho?Tem água do poço fresca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Sol já a pino, garganta seca de tanto falar. Bianca te oferece água. Você responde honestamente:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Sto male"},
                        {"id": "d", "text": "Benes nottes"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Vete al pozo, hijo. Allá la sacas tu mismo.",
                },
                {
                    "kind": "narrative",
                    "text": "Você vai até o poço de pedra no centro da piazza, tira água com a corda. Volta com a cantil cheia. Bianca acena aprovando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Bene. Y adesso — ¿ya conoces a algún vecino más?",
                    "translation": "Bom. E agora — você já conhece algum vizinho mais?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Você conheceu Pietro o ferreiro na rua. Pra Bianca você diz: 'Sí, Pietro es mi...'",
                    "options": [
                        {"id": "a", "text": "Vecino"},
                        {"id": "b", "text": "Forestiero"},
                        {"id": "c", "text": "Campesenzao"},
                        {"id": "d", "text": "Padre"},
                    ],
                    "correct": "a",
                    "word_id": "it_vecino", "target": "vecino", "native": "vizinho",
                    "npc_reaction": "Pietro. Buen hombre. Habla poco, trabaja mucho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Chiara me ha detto algo extraño anotte. Que viste un fuoco que no era de hogar. ¿Es verdad?",
                    "translation": "Chiara me disse uma coisa estranha ontem à noite. Que você viu um fogo que não era de fogueira. É verdade?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca sabe parte. Você não pode mentir piu também não pode contar tudo. Sobre o que aconteceu, o que você sentiu primeiro foi:",
                    "options": [
                        {"id": "a", "text": "Paura"},
                        {"id": "b", "text": "Fame"},
                        {"id": "c", "text": "Sed"},
                        {"id": "d", "text": "Luce"},
                    ],
                    "correct": "a",
                    "word_id": "it_paura", "target": "paura", "native": "medo",
                    "npc_reaction": "Paura. Lo entiendo. Chiara te ayuda a no sentirlo solo. Esatto es bene.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca aponta pra lamparina de aceite que Chiara te deu — você levou ao bolso. 'Esa lampada da...' Que palavra completa?",
                    "options": [
                        {"id": "a", "text": "Luce"},
                        {"id": "b", "text": "Fuoco"},
                        {"id": "c", "text": "Pane"},
                        {"id": "d", "text": "Acqua"},
                    ],
                    "correct": "a",
                    "word_id": "it_luce", "target": "luce", "native": "luce",
                    "npc_reaction": "Luce. Pequeña, segura. Las que más cuidan son las que menos asustan.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "¿Y tu vas a quedarte hoy con Chiara y Nico?",
                    "translation": "E você vai ficar hoje com Chiara e Nico?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Chiara levanta a cabeça esperando sua resposta. Nico sorri. Você diz:",
                    "options": [
                        {"id": "a", "text": "Sí, io vado con ellos"},
                        {"id": "b", "text": "Ho paura"},
                        {"id": "c", "text": "Adiós Bianca"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_io_vado", "target": "io vado", "native": "eu vou",
                    "npc_reaction": "Bene. Los tres juntos. Esatto mi piace verlo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pra você: '¿Y mañana — qué hacemos?' Como você diz 'amanhã' em italiano pra continuar a conversa?",
                    "options": [
                        {"id": "a", "text": "Mañana"},
                        {"id": "b", "text": "Hoy"},
                        {"id": "c", "text": "Vecino"},
                        {"id": "d", "text": "Bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_domani", "target": "mañana", "native": "amanhã",
                    "npc_reaction": "Mañana. El día que viene después de hoy. La misma palabra que 'manhã' del portugués.",
                },
            ],
        },
    },

    # ── Seção 4: Gramática Narrativa ──────────────────────────────────────────
    # Bianca ensenzaa perguntar idade. Tener + años — extensão direta de
    # 'ho fame' que o protagonista já conhece. Chiara e Nico
    # exemplificam falando as próprias idades.
    {
        "section_number": 4,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Bianca", "Chiara", "Nico"],
                "story": (
                    "Bianca quer saber tudo. Bordando devagar, ela faz perguntas "
                    "come quem comenta o clima — piu cada pergunta é precisa.\n\n"
                    "Os três sentaram em volta dela. Chiara no chão de pernas "
                    "cruzadas. Nico apoiado no muro. Você no banco do lado."
                ),
                "now": "Bianca vai te ensenzaar a falar idade — e quer saber a sua.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Ya sabes 'ho fame' y 'ho sete'. Hay otro 'ho' importante: 'ho X años'.",
                    "translation": "Você já sabe 'ho fame' e 'ho sete'. Tem outro 'ho' importante: 'ho X años' (tenho X anni).",
                    "pace": "slow",
                },
                {
                    "kind": "reveal",
                    "phrase": "Ho X años",
                    "meaning": "Eu tenho X anni",
                    "note": "mesmo padrão de 'ho fame' — o que você 'tem' aqui é a idade",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Yo ho dieciocho años. Jovieni todavía.",
                    "translation": "Eu tenho dezoito anni. Jovem ainda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Y yo ho veinte. Igual que tu, ¿no, forestiero?",
                    "translation": "E eu tenho vinte. Igual a você, né, forasteiro?",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Ho",   "isKey": True},
                        {"text": " + ",     "isKey": False},
                        {"text": "veinte",  "isKey": True},
                        {"text": " ",       "isKey": False},
                        {"text": "años",    "isKey": True},
                    ],
                    "example": "— ¿Cuántos años hai?— Ho veinte años.",
                    "translation": "— Quantos anni você tem?— Tenho vinte anni.",
                    "note": "número + 'años' depois de 'ho'. Sempre.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca tira os óculos do nariz pra te olhar de fronte. '¿Y tu?¿Cuántos años hai?' Você responde:",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Sono forestiero"},
                        {"id": "d", "text": "Mi chiamo veinte"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Veinte. La edad en que un hombre todavía cree que sabe todo. Espera, hijo. Espera.",
                },
                {
                    "kind": "narrative",
                    "text": "Chiara ri da resposta da Bianca. Nico ri também, baixo. Você não entende exatamente — piu ri junto.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "¿Y adesso pregunta tu a Nico — '¿cuántos años hai?'.",
                    "translation": "E agora pergunta você pro Nico — 'quantos anni você tem?'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Você se vira pra Nico e quer saber a idade dele. A pergunta começa com:",
                    "options": [
                        {"id": "a", "text": "¿Cuántos años hai?"},
                        {"id": "b", "text": "¿Cómo te chiami?"},
                        {"id": "c", "text": "¿Dónde estás?"},
                        {"id": "d", "text": "¿Tu vieni?"},
                    ],
                    "correct": "a",
                    "word_id": "it_quanti_anni", "target": "¿cuántos años hai?", "native": "quantos anni você tem?",
                    "npc_reaction": "Ho veinte, forestiero. Como tu. Por questo conectamos rápido.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Y la respuesta — recuerda — siempre 'ho X años'.",
                    "translation": "E a resposta — lembra — sempre 'ho X años'.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara repete pra fixar: 'Si alguien te pregunta cuántos años hai, tu dices:'",
                    "options": [
                        {"id": "a", "text": "Ho veinte años"},
                        {"id": "b", "text": "Sono veinte"},
                        {"id": "c", "text": "Mi veinte años"},
                        {"id": "d", "text": "Veinte ho años"},
                    ],
                    "correct": "a",
                    "word_id": "it_ho_anni", "target": "ho veinte años", "native": "tenho vinte anni",
                    "npc_reaction": "Esatto. Memoriza ese 'ho'. Vas a usarlo mucho.",
                },
            ],
        },
    },

    # ── Seção 5: Reforço ──────────────────────────────────────────────────────
    # Tarde caindo. Voltando pra casa de Antonio il Contadino. Chiara sussurra sobre a
    # primeira vez da avó dela — 'duele la testa'. Primeira pista de que o
    # dom tem custo físico. Conversa íntima — poucos exercícios, foco em
    # desenvolver lore e personagem.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Chiara", "Nico", "Bianca"],
                "story": (
                    "Vocês ficaram com Bianca até o sol começar a baixar. A tarde "
                    "passou em conversa — vizinhos parando pra cumprimentar, "
                    "Chiara testando você de leve, Nico rindo às vezes do que "
                    "você falava errado.\n\n"
                    "Quando a sombra do banco virou metade da piazza, Bianca "
                    "guardou o bordado. 'Vayan, hijos. Mañana otro día.'"
                ),
                "now": "Voltando pra locanda — Chiara caminha do seu lado, vira a voz baixa.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌇 Rua estreita, luce alaranjada batendo nas paredes de adobe. Nico uns passos à fronte.",
                },
                {
                    "kind": "item_moment",
                    "npc": "Chiara",
                    "situation": "O calor da tarde ainda pesa. Chiara passa a mão na testa, garganta seca de tanto falar o dia inteiro.",
                    "npc_line": "Forestiero — ¿hai algo de beber?Hablé todo el día y la garganta me arde.",
                    "item_tag": "bebida",
                    "on_use": {
                        "narrative": "Você tira algo de beber da mochila e estende pra Chiara. Ela bebe um gole longo, devolve, respira.",
                        "npc_reaction": "Grazie. Adesso sí — puedo seguir hablando senza sonar a cuervo.",
                        "bonus": "extra_dialogue",
                    },
                    "on_skip": {
                        "npc_reaction": "No importa. Hay una fuente cerca de casa de Antonio il Contadino. Acquanto.",
                    },
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Forestiero — ¿no te duele la testa?La primera vez a mi nonna le dolió por días, dicen.",
                    "translation": "Forasteiro — sua cabeça não está doendo?A primeira vez da minha avó doeu por dias, dizem.",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você parou. Uma pontada atrás dos olhos que você tinha ignorado todo o dia. Como se ela tivesse acabado de nomeá-la.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Mi nonna decía que era el corpo aprendiendo a cargar la palabra. Como un músculo nuevo.",
                    "translation": "Minha avó dizia que era o corpo aprendendo a carregar a palavra. Como um músculo novo.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pra sua testa, esperando uma resposta honesta. Você sente a dor — pequena, piu real:",
                    "options": [
                        {"id": "a", "text": "Male"},
                        {"id": "b", "text": "Bene"},
                        {"id": "c", "text": "Adiós"},
                        {"id": "d", "text": "Ho fame"},
                    ],
                    "correct": "a",
                    "word_id": "it_male", "target": "male", "native": "male",
                    "npc_reaction": "Male. Lo pensé. Mi nonna parlava de questo — todavía me acuerdo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês continuam caminhando. Nico olha pra trás de vez "
                        "em quando, sem perguntar. Sabe que tem coisa sendo dita "
                        "que não precisa entrar nela ainda."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Ella dormía mucho la primera semana. Comía menos. Parlava poco. Después se le pasaba.",
                    "translation": "Ela dormia muito a primeira semana. Comia menos. Falava pouco. Depois passava.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara aponta pro bolso onde você guarda a lamparina dela. 'Si hai paura de notte, enciéndela. La luce cura más que las parole.' Sobre a lamparina, o que ela faz?",
                    "options": [
                        {"id": "a", "text": "Da luce"},
                        {"id": "b", "text": "Ha paura"},
                        {"id": "c", "text": "Ha fame"},
                        {"id": "d", "text": "Es vecino"},
                    ],
                    "correct": "a",
                    "word_id": "it_luce", "target": "luce", "native": "luce",
                    "npc_reaction": "Esatto. Si te despiertas con paura — la enciendes. Funciona.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Hoy descansas. Mañana — andiamo a ver cómo estás. ¿Vale?",
                    "translation": "Hoje você descansa. Amanhã — a gente vê come você tá. Beleza?",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Chiara espera sua resposta. Vocês param na porta da casa de Antonio il Contadino. Você diz:",
                    "options": [
                        {"id": "a", "text": "Grazie, Chiara"},
                        {"id": "b", "text": "Adiós Bianca"},
                        {"id": "c", "text": "Ho paura"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Para esto sto yo en esto con te, ¿no?",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Entra, forestiero. Come algo. Después duermes.",
                    "translation": "Entra, forasteiro. Come alguma coisa. Depois dorme.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Sua cabeça pesa mais agora. A pontada virou uma pressão. Você responde a Nico honestamente sobre come está:",
                    "options": [
                        {"id": "a", "text": "Male, la testa"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ho fame"},
                        {"id": "d", "text": "Benes días"},
                    ],
                    "correct": "a",
                    "word_id": "it_male", "target": "male", "native": "male",
                    "npc_reaction": "La testa. Chiara me había avisado. Andiamo — descansa.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo ────────────────────────────────────────────────────
    # Noite. Febre subindo. Chiara e Nico cuidando. O protagonista precisa
    # responder mesmo com a cabeça queimando. Chiara decide: vai buscar uma
    # guaritrice que ela conhece — Lucia. Transição direta pra F8.
    # Gate: errar trava. Mas situação extrema, exercícios curtos.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Chiara", "Nico"],
                "story": (
                    "Você entrou na casa, comeu metade do pão que sobrou, deitou "
                    "no quarto. Chiara não foi embora — ficou na salea com Nico. "
                    "Acertaram entre eles em voz baixa que não te deixariam só.\n\n"
                    "A febre começou ao escurecer. Atrás dos olhos primeiro. "
                    "Depois cabeça inteira. Chiara bateu na sua porta."
                ),
                "now": "Você precisa responder mesmo doente. Chiara precisa decidir o que fazer.",
            },
            "steps": [
                {
                    "kind": "scene",
                    "text": "🌙 Noite · Quarto · Lamparina baixa\n\nVocê deitado, suando frio. Chiara senta na beira da cama. Nico encostado no batente da porta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Forestiero — ¿cómo estás?Necesito que me digas.",
                    "translation": "Forasteiro — come você tá?Preciso que você me fale.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Cabeça queimando, corpo pesado, garganta seca. Você diz a verdade — não dá pra esconder:",
                    "options": [
                        {"id": "a", "text": "Male"},
                        {"id": "b", "text": "Bene"},
                        {"id": "c", "text": "Benes días"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_male", "target": "male", "native": "male",
                    "npc_reaction": "Male. Lo veo. Hai febbre — la fronte calda.",
                    "gated": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "¿Hai sed?¿Quieres acqua?",
                    "translation": "Tá com sede?Quer água?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Sua boca seca come pedra. Chiara já estende a cantil. Você diz:",
                    "options": [
                        {"id": "a", "text": "Ho sete"},
                        {"id": "b", "text": "Ho fame"},
                        {"id": "c", "text": "Sto bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_sed", "target": "ho sete", "native": "tenho sede",
                    "npc_reaction": "Sed. Toma — bebe despacio.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Chiara levanta. Vai até Nico na porta, fala baixo: 'Esto no "
                        "es sólo cansancio. Es lo que decía mi nonna. Hay que "
                        "cercarla.'"
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Nico — conozco a una. Llega de fuera, ma cura bene. Ve a cercarla.",
                    "translation": "Nico — conheço uma. Vem de fora, piu cura bem. Vai buscar ela.",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "¿Quién?",
                    "translation": "Quem?",
                    "pace": "urgent",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Una guaritrice. Lucia. Llegó al borgo hace dos meses. Pregúntale a Bianca — sabe dónde está.",
                    "translation": "Uma guaritrice. Lucia. Chegou ao borgo faz dois meses. Pergunta pra Bianca — ela sabe onde tá.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico já vestiu o casaco. Aperta seu ombro prima de sair. 'Resisti, forestiero. Torno pronto.' Você responde com o que consegue:",
                    "options": [
                        {"id": "a", "text": "Grazie"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ciao"},
                        {"id": "d", "text": "Ho paura"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "De nada. Ve a dormir un poco — yo torno con ella.",
                    "gated": True,
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Nico sai correndo. Passos rápidos na rua, depois silêncio. "
                        "Chiara senta de novo na beira da cama. Coloca a mão fria na "
                        "sua testa quente."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Mi nonna decía que después de la primera, viene la febbre. Y después la febbre se va. Resisti hasta mañana.",
                    "translation": "Minha avó dizia que depois da primeira, vem a febre. E depois a febre passa. Aguenta até amanhã.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Chiara",
                    "question": "Sua cabeça pesa, os olhos fecham. Você quer perguntar o nome da guaritrice que vem. A pergunta é:",
                    "options": [
                        {"id": "a", "text": "¿Cómo se llama?"},
                        {"id": "b", "text": "¿Cómo estás?"},
                        {"id": "c", "text": "¿Tu vieni?"},
                        {"id": "d", "text": "¿Ho sete?"},
                    ],
                    "correct": "a",
                    "word_id": "it_come_se_llama", "target": "¿cómo se llama?", "native": "come se chama?",
                    "npc_reaction": "Se llama Lucia. Vas a conocerla pronto, forestiero.",
                    "gated": True,
                },
                # ── Closenzag beats — transição pra F8 ────────────────────────
                {
                    "kind": "scene",
                    "text": "🕯️ Quarto escuro · A febre subindo · Chiara velando",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Chiara",
                    "line": "Duerme, forestiero. Cuando despiertes ella ya estará aquí.",
                    "translation": "Dorme, forasteiro. Quando você acordar ela já vai estar aqui.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você fecha os olhos. A última coisa que ouve prima de "
                        "dormir é o paneo molhado da Chiara na sua testa.\n\n"
                        "Lá fora — passos correndo na rua escura. Nico batendo "
                        "na porta de Bianca pra perguntar onde encontrar uma "
                        "mulher chamada Lucia."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────




