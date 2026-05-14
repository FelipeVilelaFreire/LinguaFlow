"""
Seed das 6 seções da Fase 1 Italiano A1 — Nico.

Pré-requisito: python manage.py seed_it (cria chapter + fase)
Uso:           python manage.py seed_it_sections [--reset]

⚠️  Padrão obrigatório: chat conversacional do começo ao fim.
Toda multiple_choice carrega 'npc' (situação) + 'npc_reaction' (reação ao acerto).
Nico é o fio condutor — nunca exercício solto, nunca pergunta seca.

Língua por personagem:
  Antonio  → só italiano — chama o filho quando não consegue comunicar
  Nico      → português quebrado + exclamações em italiano (guia/ponte)
  Giulia        → só italiano (imersão — player aprende pelo contexto)
  Bianca      → só italiano (imersão — player aprende pelo contexto)
"""



# ─── Conteúdo das seções ──────────────────────────────────────────────────────

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Pura imersão — o player entra no borgo e não entende nada. Giulia tenta
    # vender pão, confusão com as moedas. Antonio intervém, chama o filho.
    # Falas 100% em italiano, sem tradução — o player não entende, e isso é
    # intencional. Vocab aparece só no vocab_list e exercícios de reconhecimento.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": "🌅  Il Borgo di Santa Chiara · Manhã · Dia 1",
                },
                {
                    "kind": "narrative",
                    "text": "Você atravessa o portão de pedra clara. Ruas de pedra, sol novo. Vozes por todo lado — você não entende nada.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Signore! Signore, aspetti! Vuole pane?Pane fresco, appena uscito dal forno!",
                    "is_new_npc": True,
                },
                {
                    "kind": "player",
                    "text": "Uma mulher de avental empoeirado bloqueia o caminho. Estende um pão quente. Diz alguma coisa — você não entende.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Venti lire, signore! Il miglior pane del borgo, lo giuro!",
                },
                {
                    "kind": "player",
                    "text": "Você tira moedas do bolso — as suas. As erradas.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Che cos e questo?Queste non sono monete di qui!",
                },
                {
                    "kind": "narrative",
                    "text": "Uma voz grave, do outro lado da rua.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Giulia, aspetta! E uno straniero - non parla italiano.",
                    "is_new_npc": True,
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Um homem mais velho. Chapéu de palha largo, braços cruzados. Examina você como quem avalia uma situação.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Parla italiano?No?",
                },
                {
                    "kind": "player",
                    "text": "Você balança a cabeça. Não.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Mmm.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Ele olha pra rua. Pensa. Depois abre a boca e grita:",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "NICO! RAGAZZO, VIENI QUI! C E UNO STRANIERO!",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "A voz ressoa pela rua inteira. Giulia ri e guarda o pão.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "straniero", "native": "estrangeiro / straniero"},
                        {"target": "pane",       "native": "pão"},
                        {"target": "italiano",   "native": "italiano (a língua)"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio te chamou de algo ao te ver na rua. O que você é aqui no borgo?",
                    "options": [
                        {"id": "a", "text": "Straniero"},
                        {"id": "b", "text": "Contadino"},
                        {"id": "c", "text": "Signore"},
                        {"id": "d", "text": "Amico"},
                    ],
                    "correct": "a",
                    "word_id": "it_straniero", "target": "straniero", "native": "estrangeiro",
                    "npc_reaction": "Straniero. Quem vem de fora. Por enquanto.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia te estendeu algo e disse 'pane fresco!'. O que é pane?",
                    "options": [
                        {"id": "a", "text": "Pão"},
                        {"id": "b", "text": "Água"},
                        {"id": "c", "text": "Moeda"},
                        {"id": "d", "text": "Chapéu"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pão",
                    "npc_reaction": "Pane! Si, signore. Il migliore del borgo.",
                },
            ],
        },
    },

    # ── Seção 2: Aquecimento contextual (primeira fase da temporada) ───────────
    # Nico chega corrindo — Antonio vai embora, Nico conecta via português
    # (aprendeu com o avô, que era straniero). Apresenta ciao, mi chiamo,
    # buongiorno. Giulia reaparece como callback da S1 — dessa vez d? o pão.
    # Nico faz a ponte em português quebrado (única língua compartilhada).
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio", "Giulia"],
                "story": (
                    "Você chegou ao borgo de Santa Chiara de manhã cedo. "
                    "Giulia tentou te vender pão — você ofereceu as moedas erradas. "
                    "Antonio apareceu, te chamou de 'straniero', tentou italiano — não funcionou.\n\n"
                    "Aí ele gritou pra rua inteira: 'NICO!'"
                ),
                "now": "Alguém vem corrindo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Passos. R?pidos. Vêm de longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Pap?! Aquí estoy! — oi?",
                    "translation": "Pai! Tô aqui! — oi?",
                    "is_new_npc": True,
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Um cara da sua idade. Mesmo chapéu de palha do pai. Para na sua frente, ofegando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Questo straniero non parla italiano. Mostragli il borgo, ragazzo.",
                    "translation": "Esse straniero não fala italiano. Mostra o borgo pra ele, filho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Uh... você... fala português?",
                    "translation": "(português quebrado)",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "Você para.\n\nSotaque pesado. Mas na sua língua.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Bueno! Ragazzo, cuídalo! Straniero — benevenido a Santa Chiara!",
                    "translation": "Bom! Filho, cuida dele! Forasteiro — bem-vindo a Santa Chiara!",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio vai embora com passos largos. Giulia observa da porta e sorri.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Ciao. Mi chiamo Nico. Contadino — trabalho na terra.",
                    "translation": "Ol?. Meu nome é Nico.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Meu avô era straniero também — por isso sei um pouco da sua língua. De manhã: 'buongiorno'. De tarde: 'buonasera'.",
                    "translation": "buongiorno = bom dia | buonasera = boa tarde",
                },
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "ciao",          "native": "ol?"},
                        {"target": "mi chiamo",      "native": "meu nome é"},
                        {"target": "buongiorno",   "native": "bom dia"},
                        {"target": "buonasera", "native": "boa tarde"},
                        {"target": "grazie",       "native": "obrigado/a"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico acabou de se apresentar: 'Mi chiamo Nico.' Agora é sua vez. Você diz:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Ciao, grazie"},
                        {"id": "c", "text": "Buongiorno"},
                        {"id": "d", "text": "Straniero"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Eso! Agora ele sabe quem você é.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Sol de manhã cedo. Nico te olha esperando. Como você cumprimenta?",
                    "options": [
                        {"id": "a", "text": "Buongiorno!"},
                        {"id": "b", "text": "Buonasera!"},
                        {"id": "c", "text": "Buonanotte!"},
                        {"id": "d", "text": "Ciao!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Buongiorno — até o meio-dia.",
                },
                {
                    "kind": "narrative",
                    "text": "Vocês dobram uma rua. Giulia na porta da padaria — reconhece você.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Ah! El straniero de antes! Toma — sin monete esta vez!",
                    "translation": "O straniero de antes! Toma — sem pagar desta vez!",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Fala 'grazie' pra ela.",
                    "translation": "grazie = obrigado/a",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Giulia",
                    "question": "Giulia te d? o pão de graça. Você responde:",
                    "options": [
                        {"id": "a", "text": "Grazie!"},
                        {"id": "b", "text": "Ciao!"},
                        {"id": "c", "text": "Buongiorno!"},
                        {"id": "d", "text": "Male!"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Prego, figlio. Torna quando vuoi.",
                },
            ],
        },
    },

    # ── Seção 3: Gram?tica Narrativa ───────────────────────────────────────────
    # Nico senta com o player num murinho e ensina as estruturas de forma direta,
    # como amico explicando — não como professor. Intercala beats com exercícios.
    # Ensina: come ti chiami?/ mi chiamo + come stai?/ bene o male.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Nico"],
                "story": (
                    "Nico passou a tarde te fazendo repetir as saudações que ele "
                    "tinha soltado na rua: 'Ciao!', 'Buongiorno', 'Buonasera'. "
                    "Quando você acertou 'Grazie' com Giulia e ela respondeu 'Prego', "
                    "ele bateu palma uma vez só. Satisfeito.\n\n"
                    "Aí ele puxou você pra um murinho na sombra de uma parede de pedra clara. "
                    "'Tem mais umas coisas que você precisa saber.'"
                ),
                "now": "Nico vai te ensinar a pedir nomes e responder como você est?.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Nico se apoia no murinho e te olha de frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Primero: come ti chiami?",
                    "translation": "Primeiro: como você se chama?",
                },
                {
                    "kind": "reveal",
                    "phrase": "Come ti chiami?",
                    "meaning": "Como você se chama?",
                    "note": "Pergunta padrão pra pedir o nome de alguém",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "E la risposta: 'Mi chiamo' — e dici il tuo nome.",
                    "translation": "E a resposta: 'Mi chiamo' — e você diz seu nome.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Mi chiamo ___",
                    "meaning": "Meu nome é ___",
                    "note": "Use seu próprio nome: 'Mi chiamo [nome]'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico aponta pra você: 'Come ti chiami?' Como você responde?",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Soy llamo [seu nome]"},
                        {"id": "c", "text": "Tú llamas [seu nome]"},
                        {"id": "d", "text": "Ciao Nico"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Piacere, amico!",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Ora otra: 'Come stai?'",
                    "translation": "Agora outra: 'como você est??'",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Come stai?", "isKey": False},
                        {"text": " → ",          "isKey": False},
                        {"text": "Bene",          "isKey": True},
                        {"text": " / ",           "isKey": False},
                        {"text": "Male",           "isKey": True},
                    ],
                    "example": "— Come stai?— Bene, grazie.",
                    "translation": "— Como você est??— Bem, obrigado.",
                    "note": "Bene = bem | Male = male",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "O sol t? bom, o pão da Giulia ainda quente no seu bolso. Nico: 'Come stai?'",
                    "options": [
                        {"id": "a", "text": "Bene"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ciao"},
                        {"id": "d", "text": "Grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene! É isso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Pero si no stai bene, dilo. No finjas.",
                    "translation": "Mas se você não est? bem, fala. Não finge.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Seus pés doem, suas p?lpebras pesam. Faz dias que você caminha sem parar. Nico: 'Come stai?'",
                    "options": [
                        {"id": "a", "text": "Male"},
                        {"id": "b", "text": "Bene"},
                        {"id": "c", "text": "Ciao"},
                        {"id": "d", "text": "Grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_male", "target": "male", "native": "male",
                    "npc_reaction": "Entendo, straniero. Riposa qui.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Você quer saber o nome de alguém. Pergunta:",
                    "options": [
                        {"id": "a", "text": "Come ti chiami?"},
                        {"id": "b", "text": "Come stai?"},
                        {"id": "c", "text": "Dónde est?s?"},
                        {"id": "d", "text": "Y tú?"},
                    ],
                    "correct": "a",
                    "word_id": "it_como_te_llamas", "target": "come ti chiami?", "native": "como você se chama?",
                    "npc_reaction": "Isso. E olha pro peito do outro enquanto pergunta.",
                },
                {
                    "kind": "narrative",
                    "text": "Nico tira uma manzana do bolso e te passa sem cerimônia. 'Del ?rbol detr?s de mi casa.'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Sabes cómo se llama esto?Manzana. Dil campo.",
                    "translation": "manzana = maçã",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico te entregou uma fruta do campo. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Manzana"},
                        {"id": "b", "text": "Pane"},
                        {"id": "c", "text": "Acqua"},
                        {"id": "d", "text": "Moneta"},
                    ],
                    "correct": "a",
                    "word_id": "it_manzana", "target": "manzana", "native": "maçã",
                    "npc_reaction": "Manzana. Roja, del ?rbol. Gratis.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico cruza os braços, satisfeito. 'Come stai?'",
                    "options": [
                        {"id": "a", "text": "Bene, y tú?"},
                        {"id": "b", "text": "Male, grazie"},
                        {"id": "c", "text": "Ciao, Nico"},
                        {"id": "d", "text": "Prego"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Excelente! E o 'y tú?' no final — isso é o que separa.",
                },
            ],
        },
    },

    # ── Seção 4: Encontro com Bianca ──────────────────────────────────────────
    # Nico leva o player pra piazza e apresenta doña Bianca — vizinha antiga,
    # conhece todo o borgo. Narrativa-heavy. Bianca fala só italiano.
    # adiós é apresentado por Nico antes de Bianca testar.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Nico"],
                "story": (
                    "Nico ficou te testando até as palavras saírem sem hesitar. "
                    "Saudações, perguntas, respostas — você foi acertando uma a uma.\n\n"
                    "Quando ele cruzou os braços satisfeito você soube que tinha "
                    "passado por algo. 'Bueno, straniero. Tem alguém que quero que "
                    "você conheça.'"
                ),
                "now": "Nico vai te apresentar alguém importante do borgo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês entram na piazza central. Sombra de ?rvores antigas, "
                        "fonte de pedra no meio. Uma mulher mais velha sentada num "
                        "banco, costurando com agulha fina."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Guarda — esa es doña Bianca. Conoce a todos nel borgo. Si vuoi saber algo, ella te dice.",
                    "translation": "Olha — essa é doña Bianca. Conhece todo mundo no borgo. Se quiser saber algo, ela conta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Ah — e se for embora de alguém, fala 'adiós'. Aprende antes de chegar nela.",
                    "translation": "adiós = tchau / adeus",
                },
                {
                    "kind": "narrative",
                    "text": "Bianca levanta os olhos do bordado. Sorri pra Nico, depois pra você.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Ciao, Nico! Y este straniero?",
                    "translation": "Ol?, Nico! E esse straniero?",
                    "is_new_npc": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Mi straniero. Lo estoy enseñando. Sa gia saludar.",
                    "translation": "Meu straniero. Tô ensinando ele. J? sabe cumprimentar.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Bianca tira os óculos pequenos do nariz e te examina de cima "
                        "a baixo. Gesto materno, sem maledade."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Avvicinati, figlio. Lasciami vederti meglio.",
                    "translation": "Chega mais perto, filho. Deixa eu te ver melhor.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca aponta o banco do lado dela: 'Y tú, figlio?Come ti chiami?'",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Soy straniero"},
                        {"id": "d", "text": "Ciao Bianca"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Piacere. Io sono Bianca. Llevo toda mi vida en este borgo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você se senta no banco de pedra ao lado dela. As mãos de "
                        "Bianca voltam ao bordado — ?geis, apesar dos anos."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Vuoi acqua del pozo?Aquí el acqua es buena, straniero.",
                    "translation": "acqua = ?gua",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca aponta pro poço da piazza e oferece algo fresco. O que é 'acqua'?",
                    "options": [
                        {"id": "a", "text": "Água"},
                        {"id": "b", "text": "Pão"},
                        {"id": "c", "text": "Maçã"},
                        {"id": "d", "text": "Moeda"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "?gua",
                    "npc_reaction": "L acqua del pozzo. La migliore del borgo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Dimmi una cosa — come stai oggi?Il primo giorno e sempre duro.",
                    "translation": "Me diz uma coisa — como você est? hoje?O primeiro dia sempre é duro.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "O sol da tarde te aquece, o pão da Giulia ainda morno no bolso. Você responde:",
                    "options": [
                        {"id": "a", "text": "Bene"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ciao"},
                        {"id": "d", "text": "Grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Me alegro. Aquí siempre se est? bene si el cuerpo acquanta y la gente saluda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Y sabes despedirte también, straniero?",
                    "translation": "E você sabe se despedir também, straniero?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca te olha esperando. Você precisa dizer tchau em italiano.",
                    "options": [
                        {"id": "a", "text": "Adiós"},
                        {"id": "b", "text": "Ciao"},
                        {"id": "c", "text": "Grazie"},
                        {"id": "d", "text": "Bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_adios", "target": "adiós", "native": "tchau / adeus",
                    "npc_reaction": "Bene. Aunque esma que no tan pronto, figlio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Ora — pregúntale a Nico cómo est?.",
                    "translation": "Agora — pergunta pro Nico como ele t?.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Bianca aponta pra Nico. É a sua vez de perguntar.",
                    "options": [
                        {"id": "a", "text": "Come stai?"},
                        {"id": "b", "text": "Come ti chiami?"},
                        {"id": "c", "text": "Y tú?"},
                        {"id": "d", "text": "Adiós?"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bene. Como siempre que ho a alguien queriendo aprender.",
                },
                {
                    "kind": "narrative",
                    "text": "Nico observa de pé, satisfeito. Bianca continua costurando.",
                },
            ],
        },
    },

    # ── Seção 5: Convivência com Bianca ────────────────────────────────────────
    # Bianca ensina sobre o ritmo social do borgo enquanto costura.
    # Poucos exercícios — foco em desenvolver o personagem e contextualizar
    # o vocab em sabedoria local. buonanotte apresentado antes de ser testado.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Nico", "Bianca"],
                "story": (
                    "Nico te apresentou a doña Bianca na piazza. Uma mulher mais "
                    "velha, costurando num banco de pedra, com olhar calmo de quem "
                    "viu tudo.\n\n"
                    "Você se apresentou, disse que estava bem. Bianca sorriu — 'aqui "
                    "sempre se est? bem se o corpo acquanta e a gente cumprimenta'. "
                    "Agora ela quer te contar como o borgo funciona."
                ),
                "now": "Bianca vai te ensinar o ritmo social — quando cumprimentar como, e por quê.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Aquí nel borgo, somos pocos. Pero todos nos conocemos.",
                    "translation": "Aqui no borgo, somos poucos. Mas todos nos conhecemos.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Nico acena com a cabeça concordando, mas deixa Bianca falar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Se saluti qualcuno, si ricordera di te. Se dici 'grazie', ti invitera. Funziona cosi.",
                    "translation": "Se você cumprimenta alguém, vão lembrar. Se diz 'grazie', vão te convidar. É assim.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "La parola piu bella dell italiano e 'grazie'. Non dimenticarla mai.",
                    "translation": "A palavra mais bonita do italiano é 'grazie'. Não esqueça nunca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca aponta pra Nico: 'Cuando él te dé algo — pane, acqua, una palabra — che dici?'",
                    "options": [
                        {"id": "a", "text": "Grazie"},
                        {"id": "b", "text": "Ciao"},
                        {"id": "c", "text": "Bene"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Eso. Y si te lo dicen a ti...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Nico te entrega a manzana que estava no bolso dele. Você diz 'grazie'. Como ele responde?",
                    "options": [
                        {"id": "a", "text": "Prego"},
                        {"id": "b", "text": "Ciao"},
                        {"id": "c", "text": "Bene"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_de_nada", "target": "prego", "native": "prego",
                    "npc_reaction": "Ese es el ciclo, figlio. Saludo, palabra, respuesta. Así vivimos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Y cuando el sol se pone y llega la noche, decimos 'buonanotte'.",
                    "translation": "E quando o sol se põe e chega a noite, dizemos 'buonanotte' — boa noite.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "O sol sumiu. Você encontra alguém na rua à noite. Como cumprimenta?",
                    "options": [
                        {"id": "a", "text": "Buonanotte"},
                        {"id": "b", "text": "Buongiorno"},
                        {"id": "c", "text": "Buonasera"},
                        {"id": "d", "text": "Ciao noche"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenas_noches", "target": "buonanotte", "native": "boa noite",
                    "npc_reaction": "Así. Cada hora tiene su saludo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Una última cosa, straniero — come ti chiami?",
                    "translation": "Uma última coisa, straniero — como você se chama?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca te olha com um sorriso. Ela quer ouvir você dizer seu nome.",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ciao Bianca"},
                        {"id": "d", "text": "Soy straniero"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Eso. Nunca olvides tu nombre cuando alguien te lo pida.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Bianca volta ao bordado. O sol começou a baixar mais — "
                        "sombras compridas no chão de pedra."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Torna domani se vuoi. Sono sempre qui, su questa panca, con l ago in mano.",
                    "translation": "Volta amanhã se quiser. Sempre estou aqui — neste banco, com a agulha na mão.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Andiamo, straniero. Tem uma última coisa antes de você descansar.",
                    "translation": "Vamos. Tem uma última coisa antes de você descansar.",
                },
            ],
        },
    },

    # ── Seção 6: Obst?culo (gate final — gated) ────────────────────────────────
    # Nico vira examinador. Cada exercício é um desafio dele direto.
    # Errar trava (frontend aplica isGated). Closing beats fazem a transição
    # pra la locanda — onde a Fase 2 começa.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Nico"],
                "story": (
                    "Nico encaixou tudo numa sequência e fez você repetir até "
                    "sair natural: 'Ciao! Come stai?' — pausa — resposta — "
                    "'Y tú, come ti chiami?'\n\n"
                    "Na terceira vez ele não corrigiu nada. Só tirou o chapéu por "
                    "um segundo — gesto sério. 'Bueno. J? pode falar com qualquer um.'\n\n"
                    "Aí o sorriso saiu do rosto. 'Agora vamos ver de verdade.'"
                ),
                "now": "Teste final. Errar trava — você precisa acertar pra passar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Ya basta de explicaciones. Si te equivocas, repites. Sin atajos.",
                    "translation": "Chega de explicações. Se errar, repete. Sem atalho.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "'Es la domani. Llego a tu lado. Che dici?'",
                    "options": [
                        {"id": "a", "text": "Buongiorno!"},
                        {"id": "b", "text": "Buonasera!"},
                        {"id": "c", "text": "Buonanotte!"},
                        {"id": "d", "text": "Ciao noche!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Eso! Pasa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "'Te di un pedazo de pane. Responde.'",
                    "options": [
                        {"id": "a", "text": "Grazie!"},
                        {"id": "b", "text": "Ciao!"},
                        {"id": "c", "text": "Bene!"},
                        {"id": "d", "text": "Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Sigue.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "'Hai detto grazie. Qué ti rispondo yo?'",
                    "options": [
                        {"id": "a", "text": "Prego"},
                        {"id": "b", "text": "Ciao"},
                        {"id": "c", "text": "Bene"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_de_nada", "target": "prego", "native": "prego",
                    "npc_reaction": "Eso! É o ciclo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "'Yo te pregunto come ti chiami. Tu respuesta empieza con...'",
                    "options": [
                        {"id": "a", "text": "Mi chiamo"},
                        {"id": "b", "text": "Soy llamo"},
                        {"id": "c", "text": "Mi llama"},
                        {"id": "d", "text": "Te llamo"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome é",
                    "npc_reaction": "Eso!",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "'Come stai?Stai bene.'",
                    "options": [
                        {"id": "a", "text": "Bene"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ciao"},
                        {"id": "d", "text": "Grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene.",
                },
                # ── Closing beats — transição pra la locanda ──────────────────
                {
                    "kind": "narrative",
                    "text": (
                        "Nico ajeita o chapéu. O sol j? t? baixo, sombras compridas "
                        "no chão de terra. Ele te d? um tapinha no ombro."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Hai fatto molto por hoy. Ven, vamos a la locanda.",
                    "translation": "J? fez bastante por hoje. Vem, vamos pra locanda.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Riposa. Domani c e altro borgo da conoscere.",
                    "translation": "Descansa. Amanhã tem mais borgo pra conhecer.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês caminham pelas ruas de pedra. Primeiras luzes nas janelas. "
                        "Nico te aponta uma casa de dois andares no canto da piazza — "
                        "la locanda. Onde você vai dormir essa noite."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────
