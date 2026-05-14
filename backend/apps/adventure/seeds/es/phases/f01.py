"""
Seed das 6 seÃ§Ãµes da Fase 1 Espanhol A1 â€” Miguel el Campesino.

PrÃ©-requisito: python manage.py seed_es_full (cria chapter + fase)
Uso:           python manage.py seed_es_sections [--reset]

âš ï¸  PadrÃ£o obrigatÃ³rio: chat conversacional do comeÃ§o ao fim.
Toda multiple_choice carrega 'npc' (situaÃ§Ã£o) + 'npc_reaction' (reaÃ§Ã£o ao acerto).
Miguel Ã© o fio condutor â€” nunca exercÃ­cio solto, nunca pergunta seca.

LÃ­ngua por personagem:
  Don Miguel  â†’ sÃ³ espanhol â€” chama o filho quando nÃ£o consegue comunicar
  Miguel      â†’ portuguÃªs quebrado + exclamaÃ§Ãµes em espanhol (guia/ponte)
  Rosa        â†’ sÃ³ espanhol (imersÃ£o â€” player aprende pelo contexto)
  Carmen      â†’ sÃ³ espanhol (imersÃ£o â€” player aprende pelo contexto)
"""



# â”€â”€â”€ ConteÃºdo das seÃ§Ãµes â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

SECTIONS = [

    # â”€â”€ SeÃ§Ã£o 1: Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Pura imersÃ£o â€” o player entra no pueblo e nÃ£o entende nada. Rosa tenta
    # vender pÃ£o, confusÃ£o com as moedas. Don Miguel intervÃ©m, chama o filho.
    # Falas 100% em espanhol, sem traduÃ§Ã£o â€” o player nÃ£o entende, e isso Ã©
    # intencional. Vocab aparece sÃ³ no vocab_list e exercÃ­cios de reconhecimento.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": "ðŸŒ…  San CristÃ³bal del Pueblo Â· ManhÃ£ Â· Dia 1",
                },
                {
                    "kind": "narrative",
                    "text": "VocÃª atravessa o portÃ£o de adobe. Ruas de pedra, sol novo. Vozes por todo lado â€” vocÃª nÃ£o entende nada.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Â¡SeÃ±or! Â¡SeÃ±or, espere! Â¿Quiere pan? Â¡Pan fresco, reciÃ©n salido del horno!",
                    "is_new_npc": True,
                },
                {
                    "kind": "player",
                    "text": "Uma mulher de avental empoeirado bloqueia o caminho. Estende um pÃ£o quente. Diz alguma coisa â€” vocÃª nÃ£o entende.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Â¡Veinte pesos, seÃ±or! Â¡El mejor pan del pueblo, se lo juro!",
                },
                {
                    "kind": "player",
                    "text": "VocÃª tira moedas do bolso â€” as suas. As erradas.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "Â¿QuÃ© es esto? Â¡Estas no son monedas de aquÃ­!",
                },
                {
                    "kind": "narrative",
                    "text": "Uma voz grave, do outro lado da rua.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¡Rosa, espera! Este es forastero â€” no habla espaÃ±ol.",
                    "is_new_npc": True,
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Um homem mais velho. ChapÃ©u de palha largo, braÃ§os cruzados. Examina vocÃª como quem avalia uma situaÃ§Ã£o.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¿Habla usted espaÃ±ol? Â¿No?",
                },
                {
                    "kind": "player",
                    "text": "VocÃª balanÃ§a a cabeÃ§a. NÃ£o.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Mmm.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Ele olha pra rua. Pensa. Depois abre a boca e grita:",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "Â¡MIGUEL! Â¡MIJO, VEN AQUÃ! Â¡HAY UN FORASTERO!",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "A voz ressoa pela rua inteira. Rosa ri e guarda o pÃ£o.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "forastero", "native": "estrangeiro / forasteiro"},
                        {"target": "pan",       "native": "pÃ£o"},
                        {"target": "espaÃ±ol",   "native": "espanhol (a lÃ­ngua)"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel te chamou de algo ao te ver na rua. O que vocÃª Ã© aqui no pueblo?",
                    "options": [
                        {"id": "a", "text": "Forastero"},
                        {"id": "b", "text": "Campesino"},
                        {"id": "c", "text": "SeÃ±or"},
                        {"id": "d", "text": "Amigo"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero. Quem vem de fora. Por enquanto.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa te estendeu algo e disse 'Â¡pan fresco!'. O que Ã© pan?",
                    "options": [
                        {"id": "a", "text": "PÃ£o"},
                        {"id": "b", "text": "Ãgua"},
                        {"id": "c", "text": "Moeda"},
                        {"id": "d", "text": "ChapÃ©u"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pÃ£o",
                    "npc_reaction": "Â¡Pan! SÃ­, seÃ±or. El mejor del pueblo.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 2: Aquecimento contextual (primeira fase da temporada) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Miguel chega correndo â€” Don Miguel vai embora, Miguel conecta via portuguÃªs
    # (aprendeu com o avÃ´, que era forasteiro). Apresenta hola, me llamo,
    # buenos dÃ­as. Rosa reaparece como callback da S1 â€” dessa vez dÃ¡ o pÃ£o.
    # Miguel faz a ponte em portuguÃªs quebrado (Ãºnica lÃ­ngua compartilhada).
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Rosa"],
                "story": (
                    "VocÃª chegou ao pueblo de San CristÃ³bal de manhÃ£ cedo. "
                    "Rosa tentou te vender pÃ£o â€” vocÃª ofereceu as moedas erradas. "
                    "Don Miguel apareceu, te chamou de 'forastero', tentou espanhol â€” nÃ£o funcionou.\n\n"
                    "AÃ­ ele gritou pra rua inteira: 'Â¡MIGUEL!'"
                ),
                "now": "AlguÃ©m vem correndo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Passos. RÃ¡pidos. VÃªm de longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Â¡PapÃ¡! Â¡AquÃ­ estoy! â€” oi?",
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
                    "npc": "Don Miguel",
                    "line": "Este forastero no habla espaÃ±ol. MuÃ©strale el pueblo, mijo.",
                    "translation": "Esse forasteiro nÃ£o fala espanhol. Mostra o pueblo pra ele, filho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
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
                    "npc": "Don Miguel",
                    "line": "Â¡Bueno! Â¡Mijo, cuÃ­dalo! Â¡Forastero â€” bienvenido a San CristÃ³bal!",
                    "translation": "Bom! Filho, cuida dele! Forasteiro â€” bem-vindo a San CristÃ³bal!",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel vai embora com passos largos. Rosa observa da porta e sorri.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Hola. Me llamo Miguel. Campesino â€” trabalho na terra.",
                    "translation": "OlÃ¡. Meu nome Ã© Miguel.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Meu avÃ´ era forastero tambÃ©m â€” por isso sei um pouco da sua lÃ­ngua. De manhÃ£: 'buenos dÃ­as'. De tarde: 'buenas tardes'.",
                    "translation": "buenos dÃ­as = bom dia | buenas tardes = boa tarde",
                },
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "hola",          "native": "olÃ¡"},
                        {"target": "me llamo",      "native": "meu nome Ã©"},
                        {"target": "buenos dÃ­as",   "native": "bom dia"},
                        {"target": "buenas tardes", "native": "boa tarde"},
                        {"target": "gracias",       "native": "obrigado/a"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel acabou de se apresentar: 'Me llamo Miguel.' Agora Ã© sua vez. VocÃª diz:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Hola, gracias"},
                        {"id": "c", "text": "Buenos dÃ­as"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Â¡Eso! Agora ele sabe quem vocÃª Ã©.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Sol de manhÃ£ cedo. Miguel te olha esperando. Como vocÃª cumprimenta?",
                    "options": [
                        {"id": "a", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "b", "text": "Â¡Buenas tardes!"},
                        {"id": "c", "text": "Â¡Buenas noches!"},
                        {"id": "d", "text": "Â¡Hola!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Buenos dÃ­as â€” atÃ© o meio-dia.",
                },
                {
                    "kind": "narrative",
                    "text": "VocÃªs dobram uma rua. Rosa na porta da padaria â€” reconhece vocÃª.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "Â¡Ah! Â¡El forastero de antes! Toma â€” Â¡sin monedas esta vez!",
                    "translation": "O forasteiro de antes! Toma â€” sem pagar desta vez!",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Fala 'gracias' pra ela.",
                    "translation": "gracias = obrigado/a",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa te dÃ¡ o pÃ£o de graÃ§a. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Â¡Gracias!"},
                        {"id": "b", "text": "Â¡Hola!"},
                        {"id": "c", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "d", "text": "Â¡Mal!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, hijo. Vuelve cuando quieras.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 3: GramÃ¡tica Narrativa â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Miguel senta com o player num murinho e ensina as estruturas de forma direta,
    # como amigo explicando â€” nÃ£o como professor. Intercala beats com exercÃ­cios.
    # Ensina: Â¿cÃ³mo te llamas? / me llamo + Â¿cÃ³mo estÃ¡s? / bien o mal.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Miguel"],
                "story": (
                    "Miguel passou a tarde te fazendo repetir as saudaÃ§Ãµes que ele "
                    "tinha soltado na rua: 'Â¡Hola!', 'Buenos dÃ­as', 'Buenas tardes'. "
                    "Quando vocÃª acertou 'Gracias' com Rosa e ela respondeu 'De nada', "
                    "ele bateu palma uma vez sÃ³. Satisfeito.\n\n"
                    "AÃ­ ele puxou vocÃª pra um murinho na sombra de uma parede de adobe. "
                    "'Tem mais umas coisas que vocÃª precisa saber.'"
                ),
                "now": "Miguel vai te ensinar a pedir nomes e responder como vocÃª estÃ¡.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Miguel se apoia no murinho e te olha de frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Primero: Â¿cÃ³mo te llamas?",
                    "translation": "Primeiro: como vocÃª se chama?",
                },
                {
                    "kind": "reveal",
                    "phrase": "Â¿CÃ³mo te llamas?",
                    "meaning": "Como vocÃª se chama?",
                    "note": "Pergunta padrÃ£o pra pedir o nome de alguÃ©m",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y la respuesta: 'Me llamo' â€” y dices tu nombre.",
                    "translation": "E a resposta: 'Me llamo' â€” e vocÃª diz seu nome.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Me llamo ___",
                    "meaning": "Meu nome Ã© ___",
                    "note": "Use seu prÃ³prio nome: 'Me llamo [nome]'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel aponta pra vocÃª: 'Â¿CÃ³mo te llamas?' Como vocÃª responde?",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy llamo [seu nome]"},
                        {"id": "c", "text": "TÃº llamas [seu nome]"},
                        {"id": "d", "text": "Hola Miguel"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Â¡Mucho gusto, amigo!",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Ahora otra: 'Â¿CÃ³mo estÃ¡s?'",
                    "translation": "Agora outra: 'como vocÃª estÃ¡?'",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "Â¿CÃ³mo estÃ¡s?", "isKey": False},
                        {"text": " â†’ ",          "isKey": False},
                        {"text": "Bien",          "isKey": True},
                        {"text": " / ",           "isKey": False},
                        {"text": "Mal",           "isKey": True},
                    ],
                    "example": "â€” Â¿CÃ³mo estÃ¡s? â€” Bien, gracias.",
                    "translation": "â€” Como vocÃª estÃ¡? â€” Bem, obrigado.",
                    "note": "Bien = bem | Mal = mal",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "O sol tÃ¡ bom, o pÃ£o da Rosa ainda quente no seu bolso. Miguel: 'Â¿CÃ³mo estÃ¡s?'",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Â¡Bien! Ã‰ isso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Pero si no estÃ¡s bien, dilo. No finjas.",
                    "translation": "Mas se vocÃª nÃ£o estÃ¡ bem, fala. NÃ£o finge.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Seus pÃ©s doem, suas pÃ¡lpebras pesam. Faz dias que vocÃª caminha sem parar. Miguel: 'Â¿CÃ³mo estÃ¡s?'",
                    "options": [
                        {"id": "a", "text": "Mal"},
                        {"id": "b", "text": "Bien"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_mal", "target": "mal", "native": "mal",
                    "npc_reaction": "Entendo, forastero. Descansa aqui.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "VocÃª quer saber o nome de alguÃ©m. Pergunta:",
                    "options": [
                        {"id": "a", "text": "Â¿CÃ³mo te llamas?"},
                        {"id": "b", "text": "Â¿CÃ³mo estÃ¡s?"},
                        {"id": "c", "text": "Â¿DÃ³nde estÃ¡s?"},
                        {"id": "d", "text": "Â¿Y tÃº?"},
                    ],
                    "correct": "a",
                    "word_id": "es_como_te_llamas", "target": "Â¿cÃ³mo te llamas?", "native": "como vocÃª se chama?",
                    "npc_reaction": "Isso. E olha pro peito do outro enquanto pergunta.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel tira uma manzana do bolso e te passa sem cerimÃ´nia. 'Del Ã¡rbol detrÃ¡s de mi casa.'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Â¿Sabes cÃ³mo se llama esto? Manzana. Del campo.",
                    "translation": "manzana = maÃ§Ã£",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel te entregou uma fruta do campo. Como se chama?",
                    "options": [
                        {"id": "a", "text": "Manzana"},
                        {"id": "b", "text": "Pan"},
                        {"id": "c", "text": "Agua"},
                        {"id": "d", "text": "Moneda"},
                    ],
                    "correct": "a",
                    "word_id": "es_manzana", "target": "manzana", "native": "maÃ§Ã£",
                    "npc_reaction": "Manzana. Roja, del Ã¡rbol. Gratis.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel cruza os braÃ§os, satisfeito. 'Â¿CÃ³mo estÃ¡s?'",
                    "options": [
                        {"id": "a", "text": "Bien, Â¿y tÃº?"},
                        {"id": "b", "text": "Mal, gracias"},
                        {"id": "c", "text": "Hola, Miguel"},
                        {"id": "d", "text": "De nada"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Â¡Excelente! E o 'Â¿y tÃº?' no final â€” isso Ã© o que separa.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 4: Encontro com Carmen â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Miguel leva o player pra plaza e apresenta doÃ±a Carmen â€” vizinha antiga,
    # conhece todo o pueblo. Narrativa-heavy. Carmen fala sÃ³ espanhol.
    # adiÃ³s Ã© apresentado por Miguel antes de Carmen testar.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Miguel"],
                "story": (
                    "Miguel ficou te testando atÃ© as palavras saÃ­rem sem hesitar. "
                    "SaudaÃ§Ãµes, perguntas, respostas â€” vocÃª foi acertando uma a uma.\n\n"
                    "Quando ele cruzou os braÃ§os satisfeito vocÃª soube que tinha "
                    "passado por algo. 'Bueno, forastero. Tem alguÃ©m que quero que "
                    "vocÃª conheÃ§a.'"
                ),
                "now": "Miguel vai te apresentar alguÃ©m importante do pueblo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs entram na plaza central. Sombra de Ã¡rvores antigas, "
                        "fonte de pedra no meio. Uma mulher mais velha sentada num "
                        "banco, costurando com agulha fina."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Mira â€” esa es doÃ±a Carmen. Conoce a todos en el pueblo. Si quieres saber algo, ella te dice.",
                    "translation": "Olha â€” essa Ã© doÃ±a Carmen. Conhece todo mundo no pueblo. Se quiser saber algo, ela conta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Ah â€” e se for embora de alguÃ©m, fala 'adiÃ³s'. Aprende antes de chegar nela.",
                    "translation": "adiÃ³s = tchau / adeus",
                },
                {
                    "kind": "narrative",
                    "text": "Carmen levanta os olhos do bordado. Sorri pra Miguel, depois pra vocÃª.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Â¡Hola, Miguel! Â¿Y este forastero?",
                    "translation": "OlÃ¡, Miguel! E esse forasteiro?",
                    "is_new_npc": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Mi forastero. Lo estoy enseÃ±ando. Ya sabe saludar.",
                    "translation": "Meu forasteiro. TÃ´ ensinando ele. JÃ¡ sabe cumprimentar.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Carmen tira os Ã³culos pequenos do nariz e te examina de cima "
                        "a baixo. Gesto materno, sem maldade."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "AcÃ©rcate, hijo. DÃ©jame verte mejor.",
                    "translation": "Chega mais perto, filho. Deixa eu te ver melhor.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen aponta o banco do lado dela: 'Â¿Y tÃº, hijo? Â¿CÃ³mo te llamas?'",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Soy forastero"},
                        {"id": "d", "text": "Hola Carmen"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Mucho gusto. Yo soy Carmen. Llevo toda mi vida en este pueblo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃª se senta no banco de pedra ao lado dela. As mÃ£os de "
                        "Carmen voltam ao bordado â€” Ã¡geis, apesar dos anos."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Â¿Quieres agua del pozo? AquÃ­ el agua es buena, forastero.",
                    "translation": "agua = Ã¡gua",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen aponta pro poÃ§o da plaza e oferece algo fresco. O que Ã© 'agua'?",
                    "options": [
                        {"id": "a", "text": "Ãgua"},
                        {"id": "b", "text": "PÃ£o"},
                        {"id": "c", "text": "MaÃ§Ã£"},
                        {"id": "d", "text": "Moeda"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "Ã¡gua",
                    "npc_reaction": "El agua del pozo. La mejor del pueblo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Dime una cosa â€” Â¿cÃ³mo estÃ¡s hoy? El primer dÃ­a siempre es duro.",
                    "translation": "Me diz uma coisa â€” como vocÃª estÃ¡ hoje? O primeiro dia sempre Ã© duro.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "O sol da tarde te aquece, o pÃ£o da Rosa ainda morno no bolso. VocÃª responde:",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Me alegro. AquÃ­ siempre se estÃ¡ bien si el cuerpo aguanta y la gente saluda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Â¿Y sabes despedirte tambiÃ©n, forastero?",
                    "translation": "E vocÃª sabe se despedir tambÃ©m, forasteiro?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen te olha esperando. VocÃª precisa dizer tchau em espanhol.",
                    "options": [
                        {"id": "a", "text": "AdiÃ³s"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Gracias"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_adios", "target": "adiÃ³s", "native": "tchau / adeus",
                    "npc_reaction": "Bien. Aunque espero que no tan pronto, hijo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Ahora â€” pregÃºntale a Miguel cÃ³mo estÃ¡.",
                    "translation": "Agora â€” pergunta pro Miguel como ele tÃ¡.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Carmen aponta pra Miguel. Ã‰ a sua vez de perguntar.",
                    "options": [
                        {"id": "a", "text": "Â¿CÃ³mo estÃ¡s?"},
                        {"id": "b", "text": "Â¿CÃ³mo te llamas?"},
                        {"id": "c", "text": "Â¿Y tÃº?"},
                        {"id": "d", "text": "Â¿AdiÃ³s?"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bien. Como siempre que tengo a alguien queriendo aprender.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel observa de pÃ©, satisfeito. Carmen continua costurando.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 5: ConvivÃªncia com Carmen â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Carmen ensina sobre o ritmo social do pueblo enquanto costura.
    # Poucos exercÃ­cios â€” foco em desenvolver o personagem e contextualizar
    # o vocab em sabedoria local. buenas noches apresentado antes de ser testado.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Miguel", "Carmen"],
                "story": (
                    "Miguel te apresentou a doÃ±a Carmen na plaza. Uma mulher mais "
                    "velha, costurando num banco de pedra, com olhar calmo de quem "
                    "viu tudo.\n\n"
                    "VocÃª se apresentou, disse que estava bem. Carmen sorriu â€” 'aqui "
                    "sempre se estÃ¡ bem se o corpo aguanta e a gente cumprimenta'. "
                    "Agora ela quer te contar como o pueblo funciona."
                ),
                "now": "Carmen vai te ensinar o ritmo social â€” quando cumprimentar como, e por quÃª.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "AquÃ­ en el pueblo, somos pocos. Pero todos nos conocemos.",
                    "translation": "Aqui no pueblo, somos poucos. Mas todos nos conhecemos.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel acena com a cabeÃ§a concordando, mas deixa Carmen falar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Si saludas a alguien, te recordarÃ¡. Si dices 'gracias', te invitarÃ¡. Es asÃ­.",
                    "translation": "Se vocÃª cumprimenta alguÃ©m, vÃ£o lembrar. Se diz 'gracias', vÃ£o te convidar. Ã‰ assim.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "La palabra mÃ¡s bonita del espaÃ±ol es 'gracias'. No la olvides nunca.",
                    "translation": "A palavra mais bonita do espanhol Ã© 'gracias'. NÃ£o esqueÃ§a nunca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen aponta pra Miguel: 'Cuando Ã©l te dÃ© algo â€” pan, agua, una palabra â€” Â¿quÃ© dices?'",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Bien"},
                        {"id": "d", "text": "AdiÃ³s"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Eso. Y si te lo dicen a ti...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Miguel te entrega a manzana que estava no bolso dele. VocÃª diz 'gracias'. Como ele responde?",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Ese es el ciclo, hijo. Saludo, palabra, respuesta. AsÃ­ vivimos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Y cuando el sol se pone y llega la noche, decimos 'buenas noches'.",
                    "translation": "E quando o sol se pÃµe e chega a noite, dizemos 'buenas noches' â€” boa noite.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "O sol sumiu. VocÃª encontra alguÃ©m na rua Ã  noite. Como cumprimenta?",
                    "options": [
                        {"id": "a", "text": "Buenas noches"},
                        {"id": "b", "text": "Buenos dÃ­as"},
                        {"id": "c", "text": "Buenas tardes"},
                        {"id": "d", "text": "Hola noche"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                    "npc_reaction": "AsÃ­. Cada hora tiene su saludo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Una Ãºltima cosa, forastero â€” Â¿cÃ³mo te llamas?",
                    "translation": "Uma Ãºltima coisa, forasteiro â€” como vocÃª se chama?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen te olha com um sorriso. Ela quer ouvir vocÃª dizer seu nome.",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Hola Carmen"},
                        {"id": "d", "text": "Soy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Eso. Nunca olvides tu nombre cuando alguien te lo pida.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Carmen volta ao bordado. O sol comeÃ§ou a baixar mais â€” "
                        "sombras compridas no chÃ£o de pedra."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Vuelve maÃ±ana si quieres. Siempre estoy aquÃ­ â€” en este banco, con la aguja en la mano.",
                    "translation": "Volta amanhÃ£ se quiser. Sempre estou aqui â€” neste banco, com a agulha na mÃ£o.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Vamos, forastero. Tem uma Ãºltima coisa antes de vocÃª descansar.",
                    "translation": "Vamos. Tem uma Ãºltima coisa antes de vocÃª descansar.",
                },
            ],
        },
    },

    # â”€â”€ SeÃ§Ã£o 6: ObstÃ¡culo (gate final â€” gated) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Miguel vira examinador. Cada exercÃ­cio Ã© um desafio dele direto.
    # Errar trava (frontend aplica isGated). Closing beats fazem a transiÃ§Ã£o
    # pra la posada â€” onde a Fase 2 comeÃ§a.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Miguel"],
                "story": (
                    "Miguel encaixou tudo numa sequÃªncia e fez vocÃª repetir atÃ© "
                    "sair natural: 'Â¡Hola! Â¿CÃ³mo estÃ¡s?' â€” pausa â€” resposta â€” "
                    "'Â¿Y tÃº, cÃ³mo te llamas?'\n\n"
                    "Na terceira vez ele nÃ£o corrigiu nada. SÃ³ tirou o chapÃ©u por "
                    "um segundo â€” gesto sÃ©rio. 'Bueno. JÃ¡ pode falar com qualquer um.'\n\n"
                    "AÃ­ o sorriso saiu do rosto. 'Agora vamos ver de verdade.'"
                ),
                "now": "Teste final. Errar trava â€” vocÃª precisa acertar pra passar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Ya basta de explicaciones. Si te equivocas, repites. Sin atajos.",
                    "translation": "Chega de explicaÃ§Ãµes. Se errar, repete. Sem atalho.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "'Es la maÃ±ana. Llego a tu lado. Â¿QuÃ© dices?'",
                    "options": [
                        {"id": "a", "text": "Â¡Buenos dÃ­as!"},
                        {"id": "b", "text": "Â¡Buenas tardes!"},
                        {"id": "c", "text": "Â¡Buenas noches!"},
                        {"id": "d", "text": "Â¡Hola noche!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos dÃ­as", "native": "bom dia",
                    "npc_reaction": "Â¡Eso! Pasa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "'Te di un pedazo de pan. Responde.'",
                    "options": [
                        {"id": "a", "text": "Â¡Gracias!"},
                        {"id": "b", "text": "Â¡Hola!"},
                        {"id": "c", "text": "Â¡Bien!"},
                        {"id": "d", "text": "Â¡AdiÃ³s!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Sigue.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "'Dijiste gracias. Â¿QuÃ© te respondo yo?'",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Â¡Eso! Ã‰ o ciclo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "'Yo te pregunto cÃ³mo te llamas. Tu respuesta empieza con...'",
                    "options": [
                        {"id": "a", "text": "Me llamo"},
                        {"id": "b", "text": "Soy llamo"},
                        {"id": "c", "text": "Mi llama"},
                        {"id": "d", "text": "Te llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome Ã©",
                    "npc_reaction": "Â¡Eso!",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "'Â¿CÃ³mo estÃ¡s? EstÃ¡s bien.'",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Bien.",
                },
                # â”€â”€ Closing beats â€” transiÃ§Ã£o pra la posada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
                {
                    "kind": "narrative",
                    "text": (
                        "Miguel ajeita o chapÃ©u. O sol jÃ¡ tÃ¡ baixo, sombras compridas "
                        "no chÃ£o de terra. Ele te dÃ¡ um tapinha no ombro."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Ya hiciste mucho por hoy. Ven, vamos a la posada.",
                    "translation": "JÃ¡ fez bastante por hoje. Vem, vamos pra posada.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Descansa. MaÃ±ana hay mÃ¡s pueblo para conocer.",
                    "translation": "Descansa. AmanhÃ£ tem mais pueblo pra conhecer.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "VocÃªs caminham pelas ruas de pedra. Primeiras luzes nas janelas. "
                        "Miguel te aponta uma casa de dois andares no canto da plaza â€” "
                        "la posada. Onde vocÃª vai dormir essa noite."
                    ),
                },
            ],
        },
    },
]


# â”€â”€â”€ Command â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
