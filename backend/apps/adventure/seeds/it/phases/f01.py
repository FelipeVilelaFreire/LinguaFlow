"""
Seed das 6 seÃ§Ãµes da Fase 1 Italiano A1 â€” Nico.

PrÃ©-requisito: python manage.py seed_it (cria chapter + fase)
Uso:           python manage.py seed_it_sections [--reset]

âš ï¸  PadrÃ£o obrigatÃ³rio: chat conversacional do comeÃ§o ao fim.
Toda multiple_choice carrega 'npc' (situaÃ§Ã£o) + 'npc_reaction' (reaÃ§Ã£o ao acerto).
Nico Ã© o fio condutor â€” nunca exercÃ­cio solto, nunca pergunta seca.

LÃ­ngua por personagem:
  Antonio  â†’ sÃ³ italiano â€” chama o filho quando nÃ£o consegue comunicar
  Nico      â†’ portuguÃªs quebrado + exclamaÃ§Ãµes em italiano (guia/ponte)
  Giulia        â†’ sÃ³ italiano (imersÃ£o â€” player aprende pelo contexto)
  Bianca      â†’ sÃ³ italiano (imersÃ£o â€” player aprende pelo contexto)
"""



# â”€â”€â”€ ConteÃºdo das seÃ§Ãµes â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Pura imersÃ£o â€” o player entra no borgo e nÃ£o entende nada. Giulia tenta
    # vender pÃ£o, confusÃ£o com as moedas. Antonio intervÃ©m, chama o filho.
    # Falas 100% em italiano, sem traduÃ§Ã£o â€” o player nÃ£o entende, e isso Ã©
    # intencional. Vocab aparece sÃ³ no vocab_list e exercÃ­cios de reconhecimento.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ…  Il Borgo di Santa Chiara · ManhÃ£ · Dia 1",
                },
                {
                    "kind": "narrative",
                    "text": "VocÃª atravessa o portÃ£o de pedra clara. Ruas de pedra, sol novo. Vozes por todo lado â€” vocÃª nÃ£o entende nada.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Signore! Signore, aspetti! Vuole pane? Pane fresco, appena uscito dal forno!",
                    "is_new_npc": True,
                },
                {
                    "kind": "player",
                    "text": "Uma mulher de avental empoeirado bloqueia o caminho. Estende um pÃ£o quente. Diz alguma coisa â€” vocÃª nÃ£o entende.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Venti lire, signore! Il miglior pane del borgo, lo giuro!",
                },
                {
                    "kind": "player",
                    "text": "VocÃª tira moedas do bolso â€” as suas. As erradas.",
                },
                {
                    "kind": "npc",
                    "npc": "Giulia",
                    "line": "Che cos e questo? Queste non sono monete di qui!",
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
                    "text": "Um homem mais velho. ChapÃ©u de palha largo, braÃ§os cruzados. Examina vocÃª como quem avalia uma situaÃ§Ã£o.",
                },
                {
                    "kind": "npc",
                    "npc": "Antonio",
                    "line": "Parla italiano? No?",
                },
                {
                    "kind": "player",
                    "text": "VocÃª balanÃ§a a cabeÃ§a. NÃ£o.",
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
                    "text": "A voz ressoa pela rua inteira. Giulia ri e guarda o pÃ£o.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "straniero", "native": "estrangeiro / straniero"},
                        {"target": "pane",       "native": "pÃ£o"},
                        {"target": "italiano",   "native": "italiano (a lÃ­ngua)"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Antonio",
                    "question": "Antonio te chamou de algo ao te ver na rua. O que vocÃª Ã© aqui no borgo?",
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
                    "question": "Giulia te estendeu algo e disse 'pane fresco!'. O que Ã© pane?",
                    "options": [
                        {"id": "a", "text": "PÃ£o"},
                        {"id": "b", "text": "Ãgua"},
                        {"id": "c", "text": "Moeda"},
                        {"id": "d", "text": "ChapÃ©u"},
                    ],
                    "correct": "a",
                    "word_id": "it_pane", "target": "pane", "native": "pÃ£o",
                    "npc_reaction": "Pane! Si, signore. Il migliore del borgo.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: Aquecimento contextual (primeira fase da temporada) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Nico chega corrindo â€” Antonio vai embora, Nico conecta via portuguÃªs
    # (aprendeu com o avÃ´, que era straniero). Apresenta ciao, mi chiamo,
    # buongiorno. Giulia reaparece como callback da S1 â€” dessa vez dÃ o pÃ£o.
    # Nico faz a ponte em portuguÃªs quebrado (Ãºnica lÃ­ngua compartilhada).
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Antonio", "Giulia"],
                "story": (
                    "VocÃª chegou ao borgo de Santa Chiara de manhÃ£ cedo. "
                    "Giulia tentou te vender pÃ£o â€” vocÃª ofereceu as moedas erradas. "
                    "Antonio apareceu, te chamou de 'straniero', tentou italiano â€” nÃ£o funcionou.\n\n"
                    "Aí ele gritou pra rua inteira: 'NICO!'"
                ),
                "now": "AlguÃ©m vem corrindo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Passos. RÃpidue. VÃªm de longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "PapÃ! AquÃ­ estoy! â€” oi?",
                    "translation": "Pai! TÃ´ aqui! â€” oi?",
                    "is_new_npc": True,
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Um cara da sua idade. Mesmo chapÃ©u de palha do pai. Para na sua frente, ofegando.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Questo straniero non parla italiano. Mostragli il borgo, ragazzo.",
                    "translation": "Esse straniero nÃ£o fala italiano. Mostra o borgo pra ele, filho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Uh... vocÃª... fala portuguÃªs?",
                    "translation": "(portuguÃªs quebrado)",
                    "pace": "slow",
                },
                {
                    "kind": "player",
                    "text": "VocÃª para.\n\nSotaque pesado. Mas na sua lÃ­ngua.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Antonio",
                    "line": "Bueno! Ragazzo, cuÃ­dalo! Straniero â€” benevenido a Santa Chiara!",
                    "translation": "Bom! Filho, cuida dele! Forasteiro â€” bem-vindo a Santa Chiara!",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Antonio vai embora com passos largos. Giulia observa da porta e sorri.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Ciao. Mi chiamo Nico. Contadino â€” trabalho na terra.",
                    "translation": "OlÃ. Meu nome Ã© Nico.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Meu avÃ´ era straniero tambÃ©m â€” por isso sei um pouco da sua lÃ­ngua. De manhÃ£: 'buongiorno'. De tarde: 'buonasera'.",
                    "translation": "buongiorno = bom dia | buonasera = boa tarde",
                },
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "ciao",          "native": "olÃ"},
                        {"target": "mi chiamo",      "native": "meu nome Ã©"},
                        {"target": "buongiorno",   "native": "bom dia"},
                        {"target": "buonasera", "native": "boa tarde"},
                        {"target": "grazie",       "native": "obrigado/a"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico acabou de se apresentar: 'Mi chiamo Nico.' Agora Ã© sua vez. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Ciao, grazie"},
                        {"id": "c", "text": "Buongiorno"},
                        {"id": "d", "text": "Straniero"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "Eso! Agora ele sabe quem vocÃª Ã©.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Sol de manhÃ£ cedo. Nico te olha esperando. Como vocÃª cumprimenta?",
                    "options": [
                        {"id": "a", "text": "Buongiorno!"},
                        {"id": "b", "text": "Buonasera!"},
                        {"id": "c", "text": "Buonanotte!"},
                        {"id": "d", "text": "Ciao!"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenos_dias", "target": "buongiorno", "native": "bom dia",
                    "npc_reaction": "Buongiorno â€” atÃ© o meio-dia.",
                },
                {
                    "kind": "narrative",
                    "text": "VocÃªs dobram uma rua. Giulia na porta da padaria â€” reconhece vocÃª.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Giulia",
                    "line": "Ah! El straniero de antes! Toma â€” sin monete esta vez!",
                    "translation": "O straniero de antes! Toma â€” sem pagar desta vez!",
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
                    "question": "Giulia te dÃ o pÃ£o de graÃ§a. VocÃª responde:",
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

    # â”€â”€ SeÃ§Ã£o 3: GramÃtica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Nico senta com o player num murinho e ensina as estruturas de forma direta,
    # como amico explicando â€” nÃ£o como professor. Intercala beats com exercÃ­cios.
    # Ensina: come ti chiami? / mi chiamo + come stai? / bene o male.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Nico"],
                "story": (
                    "Nico passou a tarde te fazendo repetir as saudaÃ§Ãµes que ele "
                    "tinha soltado na rua: 'Ciao!', 'Buongiorno', 'Buonasera'. "
                    "Quando vocÃª acertou 'Grazie' com Giulia e ela respondeu 'Prego', "
                    "ele bateu palma uma vez sÃ³. Satisfeito.\n\n"
                    "Aí ele puxou vocÃª pra um murinho na sombra de uma parede de pedra clara. "
                    "'Tem mais umas coisas que vocÃª precisa saber.'"
                ),
                "now": "Nico vai te ensinar a pedir nomes e responder como vocÃª estÃ.",
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
                    "translation": "Primeiro: como vocÃª se chama?",
                },
                {
                    "kind": "reveal",
                    "phrase": "Come ti chiami?",
                    "meaning": "Como vocÃª se chama?",
                    "note": "Pergunta padrÃ£o pra pedir o nome de alguÃ©m",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "E la risposta: 'Mi chiamo' â€” e dici il tuo nome.",
                    "translation": "E a resposta: 'Mi chiamo' â€” e vocÃª diz seu nome.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Mi chiamo ___",
                    "meaning": "Meu nome Ã© ___",
                    "note": "Use seu prÃ³prio nome: 'Mi chiamo [nome]'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico aponta pra vocÃª: 'Come ti chiami?' Como vocÃª responde?",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Soy llamo [seu nome]"},
                        {"id": "c", "text": "TÃº llamas [seu nome]"},
                        {"id": "d", "text": "Ciao Nico"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "Piacere, amico!",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Ora otra: 'Come stai?'",
                    "translation": "Agora outra: 'como vocÃª estÃ?'",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Come stai?", "isKey": False},
                        {"text": " â†’ ",          "isKey": False},
                        {"text": "Bene",          "isKey": True},
                        {"text": " / ",           "isKey": False},
                        {"text": "Male",           "isKey": True},
                    ],
                    "example": "â€” Come stai? â€” Bene, grazie.",
                    "translation": "â€” Como vocÃª estÃ? â€” Bem, obrigado.",
                    "note": "Bene = bem | Male = male",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "O sol tÃ bom, o pÃ£o da Giulia ainda quente no seu bolso. Nico: 'Come stai?'",
                    "options": [
                        {"id": "a", "text": "Bene"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ciao"},
                        {"id": "d", "text": "Grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Bene! Ã‰ isso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Pero si no stai bene, dilo. No finjas.",
                    "translation": "Mas se vocÃª nÃ£o estÃ bem, fala. NÃ£o finge.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Seus pÃ©s doem, suas pÃlpebras pesam. Faz dias que vocÃª caminha sem parar. Nico: 'Come stai?'",
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
                    "question": "VocÃª quer saber o nome de alguÃ©m. Pergunta:",
                    "options": [
                        {"id": "a", "text": "Come ti chiami?"},
                        {"id": "b", "text": "Come stai?"},
                        {"id": "c", "text": "DÃ³nde estÃs?"},
                        {"id": "d", "text": "Y tÃº?"},
                    ],
                    "correct": "a",
                    "word_id": "it_como_te_llamas", "target": "come ti chiami?", "native": "como vocÃª se chama?",
                    "npc_reaction": "Isso. E olha pro peito do outro enquanto pergunta.",
                },
                {
                    "kind": "narrative",
                    "text": "Nico tira uma manzana do bolso e te passa sem cerimÃ´nia. 'Del Ãrbol detrÃs de mi casa.'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Sabes cÃ³mo se llama esto? Manzana. Dil campo.",
                    "translation": "manzana = maÃ§Ã£",
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
                    "word_id": "it_manzana", "target": "manzana", "native": "maÃ§Ã£",
                    "npc_reaction": "Manzana. Roja, del Ãrbol. Gratis.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Nico cruza os braÃ§os, satisfeito. 'Come stai?'",
                    "options": [
                        {"id": "a", "text": "Bene, y tÃº?"},
                        {"id": "b", "text": "Male, grazie"},
                        {"id": "c", "text": "Ciao, Nico"},
                        {"id": "d", "text": "Prego"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Excelente! E o 'y tÃº?' no final â€” isso Ã© o que separa.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: Encontro com Bianca â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Nico leva o player pra piazza e apresenta doÃ±a Bianca â€” vizinha antiga,
    # conhece todo o borgo. Narrativa-heavy. Bianca fala sÃ³ italiano.
    # adiÃ³s Ã© apresentado por Nico antes de Bianca testar.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Nico"],
                "story": (
                    "Nico ficou te testando atÃ© as palavras saÃ­rem sem hesitar. "
                    "SaudaÃ§Ãµes, perguntas, respostas â€” vocÃª foi acertando uma a uma.\n\n"
                    "Quando ele cruzou os braÃ§os satisfeito vocÃª soube que tinha "
                    "passado por algo. 'Bueno, straniero. Tem alguÃ©m que quero que "
                    "vocÃª conheÃ§a.'"
                ),
                "now": "Nico vai te apresentar alguÃ©m importante do borgo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs entram na piazza central. Sombra de Ãrvores antigas, "
                        "fonte de pedra no meio. Uma mulher mais velha sentada num "
                        "banco, costurando com agulha fina."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Guarda â€” esa es doÃ±a Bianca. Conoce a todos nel borgo. Si vuoi saber algo, ella te dice.",
                    "translation": "Olha â€” essa Ã© doÃ±a Bianca. Conhece todo mundo no borgo. Se quiser saber algo, ela conta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Ah â€” e se for embora de alguÃ©m, fala 'adiÃ³s'. Aprende antes de chegar nela.",
                    "translation": "adiÃ³s = tchau / adeus",
                },
                {
                    "kind": "narrative",
                    "text": "Bianca levanta os olhos do bordado. Sorri pra Nico, depois pra vocÃª.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Ciao, Nico! Y este straniero?",
                    "translation": "OlÃ, Nico! E esse straniero?",
                    "is_new_npc": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Mi straniero. Lo estoy enseÃ±ando. Sa gia saludar.",
                    "translation": "Meu straniero. TÃ´ ensinando ele. JÃ sabe cumprimentar.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Bianca tira os Ã³culos pequenos do nariz e te examina de cima "
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
                    "question": "Bianca aponta o banco do lado dela: 'Y tÃº, figlio? Come ti chiami?'",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Soy straniero"},
                        {"id": "d", "text": "Ciao Bianca"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "Piacere. Io sono Bianca. Llevo toda mi vida en este borgo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª se senta no banco de pedra ao lado dela. As mÃ£os de "
                        "Bianca voltam ao bordado â€” Ãgeis, apesar dos anos."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Vuoi acqua del pozo? AquÃ­ el acqua es buena, straniero.",
                    "translation": "acqua = Ãgua",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca aponta pro poÃ§o da piazza e oferece algo fresco. O que Ã© 'acqua'?",
                    "options": [
                        {"id": "a", "text": "Ãgua"},
                        {"id": "b", "text": "PÃ£o"},
                        {"id": "c", "text": "MaÃ§Ã£"},
                        {"id": "d", "text": "Moeda"},
                    ],
                    "correct": "a",
                    "word_id": "it_acqua", "target": "acqua", "native": "Ãgua",
                    "npc_reaction": "L acqua del pozzo. La migliore del borgo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Dimmi una cosa â€” come stai oggi? Il primo giorno e sempre duro.",
                    "translation": "Me diz uma coisa â€” como vocÃª estÃ hoje? O primeiro dia sempre Ã© duro.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "O sol da tarde te aquece, o pÃ£o da Giulia ainda morno no bolso. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Bene"},
                        {"id": "b", "text": "Male"},
                        {"id": "c", "text": "Ciao"},
                        {"id": "d", "text": "Grazie"},
                    ],
                    "correct": "a",
                    "word_id": "it_bene", "target": "bene", "native": "bem",
                    "npc_reaction": "Me alegro. AquÃ­ siempre se estÃ bene si el cuerpo acquanta y la gente saluda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Y sabes despedirte tambiÃ©n, straniero?",
                    "translation": "E vocÃª sabe se despedir tambÃ©m, straniero?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca te olha esperando. VocÃª precisa dizer tchau em italiano.",
                    "options": [
                        {"id": "a", "text": "AdiÃ³s"},
                        {"id": "b", "text": "Ciao"},
                        {"id": "c", "text": "Grazie"},
                        {"id": "d", "text": "Bene"},
                    ],
                    "correct": "a",
                    "word_id": "it_adios", "target": "adiÃ³s", "native": "tchau / adeus",
                    "npc_reaction": "Bene. Aunque esma que no tan pronto, figlio.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Ora â€” pregÃºntale a Nico cÃ³mo estÃ.",
                    "translation": "Agora â€” pergunta pro Nico como ele tÃ.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "Bianca aponta pra Nico. Ã‰ a sua vez de perguntar.",
                    "options": [
                        {"id": "a", "text": "Come stai?"},
                        {"id": "b", "text": "Come ti chiami?"},
                        {"id": "c", "text": "Y tÃº?"},
                        {"id": "d", "text": "AdiÃ³s?"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bene. Como siempre que ho a alguien queriendo aprender.",
                },
                {
                    "kind": "narrative",
                    "text": "Nico observa de pÃ©, satisfeito. Bianca continua costurando.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ConvivÃªncia com Bianca â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Bianca ensina sobre o ritmo social do borgo enquanto costura.
    # Poucos exercÃ­cios â€” foco em desenvolver o personagem e contextualizar
    # o vocab em sabedoria local. buonanotte apresentado antes de ser testado.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Nico", "Bianca"],
                "story": (
                    "Nico te apresentou a doÃ±a Bianca na piazza. Uma mulher mais "
                    "velha, costurando num banco de pedra, com olhar calmo de quem "
                    "viu tudo.\n\n"
                    "VocÃª se apresentou, disse que estava bem. Bianca sorriu â€” 'aqui "
                    "sempre se estÃ bem se o corpo acquanta e a gente cumprimenta'. "
                    "Agora ela quer te contar como o borgo funciona."
                ),
                "now": "Bianca vai te ensinar o ritmo social â€” quando cumprimentar como, e por quÃª.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "AquÃ­ nel borgo, somos pocos. Pero todos nos conocemos.",
                    "translation": "Aqui no borgo, somos poucos. Mas todos nos conhecemos.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Nico acena com a cabeÃ§a concordando, mas deixa Bianca falar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Se saluti qualcuno, si ricordera di te. Se dici 'grazie', ti invitera. Funziona cosi.",
                    "translation": "Se vocÃª cumprimenta alguÃ©m, vÃ£o lembrar. Se diz 'grazie', vÃ£o te convidar. Ã‰ assim.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "La parola piu bella dell italiano e 'grazie'. Non dimenticarla mai.",
                    "translation": "A palavra mais bonita do italiano Ã© 'grazie'. NÃ£o esqueÃ§a nunca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca aponta pra Nico: 'Cuando Ã©l te dÃ© algo â€” pane, acqua, una palabra â€” che dici?'",
                    "options": [
                        {"id": "a", "text": "Grazie"},
                        {"id": "b", "text": "Ciao"},
                        {"id": "c", "text": "Bene"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Eso. Y si te lo dicen a ti...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Nico te entrega a manzana que estava no bolso dele. VocÃª diz 'grazie'. Como ele responde?",
                    "options": [
                        {"id": "a", "text": "Prego"},
                        {"id": "b", "text": "Ciao"},
                        {"id": "c", "text": "Bene"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_de_nada", "target": "prego", "native": "prego",
                    "npc_reaction": "Ese es el ciclo, figlio. Saludo, palabra, respuesta. AsÃ­ vivimos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Y cuando el sol se pone y llega la noche, decimos 'buonanotte'.",
                    "translation": "E quando o sol se pÃµe e chega a noite, dizemos 'buonanotte' â€” boa noite.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "O sol sumiu. VocÃª encontra alguÃ©m na rua Ã  noite. Como cumprimenta?",
                    "options": [
                        {"id": "a", "text": "Buonanotte"},
                        {"id": "b", "text": "Buongiorno"},
                        {"id": "c", "text": "Buonasera"},
                        {"id": "d", "text": "Ciao noche"},
                    ],
                    "correct": "a",
                    "word_id": "it_buenas_noches", "target": "buonanotte", "native": "boa noite",
                    "npc_reaction": "AsÃ­. Cada hora tiene su saludo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Una Ãºltima cosa, straniero â€” come ti chiami?",
                    "translation": "Uma Ãºltima coisa, straniero â€” como vocÃª se chama?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Bianca",
                    "question": "Bianca te olha com um sorriso. Ela quer ouvir vocÃª dizer seu nome.",
                    "options": [
                        {"id": "a", "text": "Mi chiamo [seu nome]"},
                        {"id": "b", "text": "Bene, grazie"},
                        {"id": "c", "text": "Ciao Bianca"},
                        {"id": "d", "text": "Soy straniero"},
                    ],
                    "correct": "a",
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "Eso. Nunca olvides tu nombre cuando alguien te lo pida.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Bianca volta ao bordado. O sol comeÃ§ou a baixar mais â€” "
                        "sombras compridas no chÃ£o de pedra."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Bianca",
                    "line": "Torna domani se vuoi. Sono sempre qui, su questa panca, con l ago in mano.",
                    "translation": "Volta amanhÃ£ se quiser. Sempre estou aqui â€” neste banco, com a agulha na mÃ£o.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Andiamo, straniero. Tem uma Ãºltima coisa antes de vocÃª descansar.",
                    "translation": "Vamos. Tem uma Ãºltima coisa antes de vocÃª descansar.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃculo (gate final â€” gated) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Nico vira examinador. Cada exercÃ­cio Ã© um desafio dele direto.
    # Errar trava (frontend aplica isGated). Closing beats fazem a transiÃ§Ã£o
    # pra la locanda â€” onde a Fase 2 comeÃ§a.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Nico"],
                "story": (
                    "Nico encaixou tudo numa sequÃªncia e fez vocÃª repetir atÃ© "
                    "sair natural: 'Ciao! Come stai?' â€” pausa â€” resposta â€” "
                    "'Y tÃº, come ti chiami?'\n\n"
                    "Na terceira vez ele nÃ£o corrigiu nada. SÃ³ tirou o chapÃ©u por "
                    "um segundo â€” gesto sÃ©rio. 'Bueno. JÃ pode falar com qualquer um.'\n\n"
                    "Aí o sorriso saiu do rosto. 'Agora vamos ver de verdade.'"
                ),
                "now": "Teste final. Errar trava â€” vocÃª precisa acertar pra passar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Ya basta de explicaciones. Si te equivocas, repites. Sin atajos.",
                    "translation": "Chega de explicaÃ§Ãµes. Se errar, repete. Sem atalho.",
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
                        {"id": "d", "text": "AdiÃ³s!"},
                    ],
                    "correct": "a",
                    "word_id": "it_grazie", "target": "grazie", "native": "obrigado/a",
                    "npc_reaction": "Sigue.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "'Hai detto grazie. QuÃ© ti rispondo yo?'",
                    "options": [
                        {"id": "a", "text": "Prego"},
                        {"id": "b", "text": "Ciao"},
                        {"id": "c", "text": "Bene"},
                        {"id": "d", "text": "Male"},
                    ],
                    "correct": "a",
                    "word_id": "it_de_nada", "target": "prego", "native": "prego",
                    "npc_reaction": "Eso! Ã‰ o ciclo.",
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
                    "word_id": "it_me_llamo", "target": "mi chiamo", "native": "meu nome Ã©",
                    "npc_reaction": "Eso!",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Nico",
                    "question": "'Come stai? Stai bene.'",
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
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra la locanda â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "narrative",
                    "text": (
                        "Nico ajeita o chapÃ©u. O sol jÃ tÃ baixo, sombras compridas "
                        "no chÃ£o de terra. Ele te dÃ um tapinha no ombro."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Hai fatto molto por hoy. Ven, vamos a la locanda.",
                    "translation": "JÃ fez bastante por hoje. Vem, vamos pra locanda.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Nico",
                    "line": "Riposa. Domani c e altro borgo da conoscere.",
                    "translation": "Descansa. AmanhÃ£ tem mais borgo pra conhecer.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs caminham pelas ruas de pedra. Primeiras luzes nas janelas. "
                        "Nico te aponta uma casa de dois andares no canto da piazza â€” "
                        "la locanda. Onde vocÃª vai dormir essa noite."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
