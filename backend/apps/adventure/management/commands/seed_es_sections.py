"""
Seed das 6 seções da Fase 1 Espanhol A1 — Miguel el Campesino.

Pré-requisito: python manage.py seed_es_full (cria chapter + fase)
Uso:           python manage.py seed_es_sections [--reset]

⚠️  Padrão obrigatório: chat conversacional do começo ao fim.
Toda multiple_choice carrega 'npc' (situação) + 'npc_reaction' (reação ao acerto).
Miguel é o fio condutor — nunca exercício solto, nunca pergunta seca.

Língua por personagem:
  Don Miguel  → só espanhol — chama o filho quando não consegue comunicar
  Miguel      → português quebrado + exclamações em espanhol (guia/ponte)
  Rosa        → só espanhol (imersão — player aprende pelo contexto)
  Carmen      → só espanhol (imersão — player aprende pelo contexto)
"""
from django.core.management.base import BaseCommand, CommandError

from apps.adventure.models import AdventureChapter, AdventurePhase, PhaseSection
from apps.adventure.management.commands.seed_voice import hydrate_section_content


# ─── Conteúdo das seções ──────────────────────────────────────────────────────

SECTIONS = [

    # ── Seção 1: Narrativa ────────────────────────────────────────────────────
    # Pura imersão — o player entra no pueblo e não entende nada. Rosa tenta
    # vender pão, confusão com as moedas. Don Miguel intervém, chama o filho.
    # Falas 100% em espanhol, sem tradução — o player não entende, e isso é
    # intencional. Vocab aparece só no vocab_list e exercícios de reconhecimento.
    {
        "section_number": 1,
        "section_type": "narrativa",
        "content": {
            "beats": [
                {
                    "kind": "scene",
                    "text": "🌅  San Cristóbal del Pueblo · Manhã · Dia 1",
                },
                {
                    "kind": "narrative",
                    "text": "Você atravessa o portão de adobe. Ruas de pedra, sol novo. Vozes por todo lado — você não entende nada.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "¡Señor! ¡Señor, espere! ¿Quiere pan? ¡Pan fresco, recién salido del horno!",
                    "is_new_npc": True,
                },
                {
                    "kind": "player",
                    "text": "Uma mulher de avental empoeirado bloqueia o caminho. Estende um pão quente. Diz alguma coisa — você não entende.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "¡Veinte pesos, señor! ¡El mejor pan del pueblo, se lo juro!",
                },
                {
                    "kind": "player",
                    "text": "Você tira moedas do bolso — as suas. As erradas.",
                },
                {
                    "kind": "npc",
                    "npc": "Rosa",
                    "line": "¿Qué es esto? ¡Estas no son monedas de aquí!",
                },
                {
                    "kind": "narrative",
                    "text": "Uma voz grave, do outro lado da rua.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¡Rosa, espera! Este es forastero — no habla español.",
                    "is_new_npc": True,
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "Um homem mais velho. Chapéu de palha largo, braços cruzados. Examina você como quem avalia uma situação.",
                },
                {
                    "kind": "npc",
                    "npc": "Don Miguel",
                    "line": "¿Habla usted español? ¿No?",
                },
                {
                    "kind": "player",
                    "text": "Você balança a cabeça. Não.",
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
                    "line": "¡MIGUEL! ¡MIJO, VEN AQUÍ! ¡HAY UN FORASTERO!",
                    "pace": "urgent",
                },
                {
                    "kind": "player",
                    "text": "A voz ressoa pela rua inteira. Rosa ri e guarda o pão.",
                },
            ],
            "exercises": [
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "forastero", "native": "estrangeiro / forasteiro"},
                        {"target": "pan",       "native": "pão"},
                        {"target": "español",   "native": "espanhol (a língua)"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Don Miguel",
                    "question": "Don Miguel te chamou de algo ao te ver na rua. O que você é aqui no pueblo?",
                    "options": [
                        {"id": "a", "text": "Forastero"},
                        {"id": "b", "text": "Campesino"},
                        {"id": "c", "text": "Señor"},
                        {"id": "d", "text": "Amigo"},
                    ],
                    "correct": "a",
                    "word_id": "es_forastero", "target": "forastero", "native": "estrangeiro",
                    "npc_reaction": "Forastero. Quem vem de fora. Por enquanto.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Rosa",
                    "question": "Rosa te estendeu algo e disse '¡pan fresco!'. O que é pan?",
                    "options": [
                        {"id": "a", "text": "Pão"},
                        {"id": "b", "text": "Água"},
                        {"id": "c", "text": "Moeda"},
                        {"id": "d", "text": "Chapéu"},
                    ],
                    "correct": "a",
                    "word_id": "es_pan", "target": "pan", "native": "pão",
                    "npc_reaction": "¡Pan! Sí, señor. El mejor del pueblo.",
                },
            ],
        },
    },

    # ── Seção 2: Aquecimento contextual (primeira fase da temporada) ───────────
    # Miguel chega correndo — Don Miguel vai embora, Miguel conecta via português
    # (aprendeu com o avô, que era forasteiro). Apresenta hola, me llamo,
    # buenos días. Rosa reaparece como callback da S1 — dessa vez dá o pão.
    # Miguel faz a ponte em português quebrado (única língua compartilhada).
    {
        "section_number": 2,
        "section_type": "revisao_srs",
        "content": {
            "recap": {
                "characters": ["Don Miguel", "Rosa"],
                "story": (
                    "Você chegou ao pueblo de San Cristóbal de manhã cedo. "
                    "Rosa tentou te vender pão — você ofereceu as moedas erradas. "
                    "Don Miguel apareceu, te chamou de 'forastero', tentou espanhol — não funcionou.\n\n"
                    "Aí ele gritou pra rua inteira: '¡MIGUEL!'"
                ),
                "now": "Alguém vem correndo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Passos. Rápidos. Vêm de longe.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "¡Papá! ¡Aquí estoy! — oi?",
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
                    "npc": "Don Miguel",
                    "line": "Este forastero no habla español. Muéstrale el pueblo, mijo.",
                    "translation": "Esse forasteiro não fala espanhol. Mostra o pueblo pra ele, filho.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
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
                    "npc": "Don Miguel",
                    "line": "¡Bueno! ¡Mijo, cuídalo! ¡Forastero — bienvenido a San Cristóbal!",
                    "translation": "Bom! Filho, cuida dele! Forasteiro — bem-vindo a San Cristóbal!",
                    "pace": "urgent",
                },
                {
                    "kind": "narrative",
                    "text": "Don Miguel vai embora com passos largos. Rosa observa da porta e sorri.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Hola. Me llamo Miguel. Campesino — trabalho na terra.",
                    "translation": "Olá. Meu nome é Miguel.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Meu avô era forastero também — por isso sei um pouco da sua língua. De manhã: 'buenos días'. De tarde: 'buenas tardes'.",
                    "translation": "buenos días = bom dia | buenas tardes = boa tarde",
                },
                {
                    "kind": "vocab_list",
                    "items": [
                        {"target": "hola",          "native": "olá"},
                        {"target": "me llamo",      "native": "meu nome é"},
                        {"target": "buenos días",   "native": "bom dia"},
                        {"target": "buenas tardes", "native": "boa tarde"},
                        {"target": "gracias",       "native": "obrigado/a"},
                    ],
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel acabou de se apresentar: 'Me llamo Miguel.' Agora é sua vez. Você diz:",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Hola, gracias"},
                        {"id": "c", "text": "Buenos días"},
                        {"id": "d", "text": "Forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "¡Eso! Agora ele sabe quem você é.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Sol de manhã cedo. Miguel te olha esperando. Como você cumprimenta?",
                    "options": [
                        {"id": "a", "text": "¡Buenos días!"},
                        {"id": "b", "text": "¡Buenas tardes!"},
                        {"id": "c", "text": "¡Buenas noches!"},
                        {"id": "d", "text": "¡Hola!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "Buenos días — até o meio-dia.",
                },
                {
                    "kind": "narrative",
                    "text": "Vocês dobram uma rua. Rosa na porta da padaria — reconhece você.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Rosa",
                    "line": "¡Ah! ¡El forastero de antes! Toma — ¡sin monedas esta vez!",
                    "translation": "O forasteiro de antes! Toma — sem pagar desta vez!",
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
                    "question": "Rosa te dá o pão de graça. Você responde:",
                    "options": [
                        {"id": "a", "text": "¡Gracias!"},
                        {"id": "b", "text": "¡Hola!"},
                        {"id": "c", "text": "¡Buenos días!"},
                        {"id": "d", "text": "¡Mal!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "De nada, hijo. Vuelve cuando quieras.",
                },
            ],
        },
    },

    # ── Seção 3: Gramática Narrativa ───────────────────────────────────────────
    # Miguel senta com o player num murinho e ensina as estruturas de forma direta,
    # como amigo explicando — não como professor. Intercala beats com exercícios.
    # Ensina: ¿cómo te llamas? / me llamo + ¿cómo estás? / bien o mal.
    {
        "section_number": 3,
        "section_type": "gramatica_narrativa",
        "content": {
            "recap": {
                "characters": ["Miguel"],
                "story": (
                    "Miguel passou a tarde te fazendo repetir as saudações que ele "
                    "tinha soltado na rua: '¡Hola!', 'Buenos días', 'Buenas tardes'. "
                    "Quando você acertou 'Gracias' com Rosa e ela respondeu 'De nada', "
                    "ele bateu palma uma vez só. Satisfeito.\n\n"
                    "Aí ele puxou você pra um murinho na sombra de uma parede de adobe. "
                    "'Tem mais umas coisas que você precisa saber.'"
                ),
                "now": "Miguel vai te ensinar a pedir nomes e responder como você está.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": "Miguel se apoia no murinho e te olha de frente.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Primero: ¿cómo te llamas?",
                    "translation": "Primeiro: como você se chama?",
                },
                {
                    "kind": "reveal",
                    "phrase": "¿Cómo te llamas?",
                    "meaning": "Como você se chama?",
                    "note": "Pergunta padrão pra pedir o nome de alguém",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Y la respuesta: 'Me llamo' — y dices tu nombre.",
                    "translation": "E a resposta: 'Me llamo' — e você diz seu nome.",
                },
                {
                    "kind": "reveal",
                    "phrase": "Me llamo ___",
                    "meaning": "Meu nome é ___",
                    "note": "Use seu próprio nome: 'Me llamo [nome]'",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel aponta pra você: '¿Cómo te llamas?' Como você responde?",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Soy llamo [seu nome]"},
                        {"id": "c", "text": "Tú llamas [seu nome]"},
                        {"id": "d", "text": "Hola Miguel"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "¡Mucho gusto, amigo!",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Ahora otra: '¿Cómo estás?'",
                    "translation": "Agora outra: 'como você está?'",
                },
                {
                    "kind": "pattern",
                    "parts": [
                        {"text": "¿Cómo estás?", "isKey": False},
                        {"text": " → ",          "isKey": False},
                        {"text": "Bien",          "isKey": True},
                        {"text": " / ",           "isKey": False},
                        {"text": "Mal",           "isKey": True},
                    ],
                    "example": "— ¿Cómo estás? — Bien, gracias.",
                    "translation": "— Como você está? — Bem, obrigado.",
                    "note": "Bien = bem | Mal = mal",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "O sol tá bom, o pão da Rosa ainda quente no seu bolso. Miguel: '¿Cómo estás?'",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "¡Bien! É isso.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Pero si no estás bien, dilo. No finjas.",
                    "translation": "Mas se você não está bem, fala. Não finge.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Seus pés doem, suas pálpebras pesam. Faz dias que você caminha sem parar. Miguel: '¿Cómo estás?'",
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
                    "question": "Você quer saber o nome de alguém. Pergunta:",
                    "options": [
                        {"id": "a", "text": "¿Cómo te llamas?"},
                        {"id": "b", "text": "¿Cómo estás?"},
                        {"id": "c", "text": "¿Dónde estás?"},
                        {"id": "d", "text": "¿Y tú?"},
                    ],
                    "correct": "a",
                    "word_id": "es_como_te_llamas", "target": "¿cómo te llamas?", "native": "como você se chama?",
                    "npc_reaction": "Isso. E olha pro peito do outro enquanto pergunta.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel tira uma manzana do bolso e te passa sem cerimônia. 'Del árbol detrás de mi casa.'",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "¿Sabes cómo se llama esto? Manzana. Del campo.",
                    "translation": "manzana = maçã",
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
                    "word_id": "es_manzana", "target": "manzana", "native": "maçã",
                    "npc_reaction": "Manzana. Roja, del árbol. Gratis.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Miguel cruza os braços, satisfeito. '¿Cómo estás?'",
                    "options": [
                        {"id": "a", "text": "Bien, ¿y tú?"},
                        {"id": "b", "text": "Mal, gracias"},
                        {"id": "c", "text": "Hola, Miguel"},
                        {"id": "d", "text": "De nada"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "¡Excelente! E o '¿y tú?' no final — isso é o que separa.",
                },
            ],
        },
    },

    # ── Seção 4: Encontro com Carmen ──────────────────────────────────────────
    # Miguel leva o player pra plaza e apresenta doña Carmen — vizinha antiga,
    # conhece todo o pueblo. Narrativa-heavy. Carmen fala só espanhol.
    # adiós é apresentado por Miguel antes de Carmen testar.
    {
        "section_number": 4,
        "section_type": "pratica_aplicada",
        "content": {
            "recap": {
                "characters": ["Miguel"],
                "story": (
                    "Miguel ficou te testando até as palavras saírem sem hesitar. "
                    "Saudações, perguntas, respostas — você foi acertando uma a uma.\n\n"
                    "Quando ele cruzou os braços satisfeito você soube que tinha "
                    "passado por algo. 'Bueno, forastero. Tem alguém que quero que "
                    "você conheça.'"
                ),
                "now": "Miguel vai te apresentar alguém importante do pueblo.",
            },
            "steps": [
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês entram na plaza central. Sombra de árvores antigas, "
                        "fonte de pedra no meio. Uma mulher mais velha sentada num "
                        "banco, costurando com agulha fina."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Mira — esa es doña Carmen. Conoce a todos en el pueblo. Si quieres saber algo, ella te dice.",
                    "translation": "Olha — essa é doña Carmen. Conhece todo mundo no pueblo. Se quiser saber algo, ela conta.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Ah — e se for embora de alguém, fala 'adiós'. Aprende antes de chegar nela.",
                    "translation": "adiós = tchau / adeus",
                },
                {
                    "kind": "narrative",
                    "text": "Carmen levanta os olhos do bordado. Sorri pra Miguel, depois pra você.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¡Hola, Miguel! ¿Y este forastero?",
                    "translation": "Olá, Miguel! E esse forasteiro?",
                    "is_new_npc": True,
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Mi forastero. Lo estoy enseñando. Ya sabe saludar.",
                    "translation": "Meu forasteiro. Tô ensinando ele. Já sabe cumprimentar.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Carmen tira os óculos pequenos do nariz e te examina de cima "
                        "a baixo. Gesto materno, sem maldade."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Acércate, hijo. Déjame verte mejor.",
                    "translation": "Chega mais perto, filho. Deixa eu te ver melhor.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen aponta o banco do lado dela: '¿Y tú, hijo? ¿Cómo te llamas?'",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Soy forastero"},
                        {"id": "d", "text": "Hola Carmen"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Mucho gusto. Yo soy Carmen. Llevo toda mi vida en este pueblo.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Você se senta no banco de pedra ao lado dela. As mãos de "
                        "Carmen voltam ao bordado — ágeis, apesar dos anos."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¿Quieres agua del pozo? Aquí el agua es buena, forastero.",
                    "translation": "agua = água",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen aponta pro poço da plaza e oferece algo fresco. O que é 'agua'?",
                    "options": [
                        {"id": "a", "text": "Água"},
                        {"id": "b", "text": "Pão"},
                        {"id": "c", "text": "Maçã"},
                        {"id": "d", "text": "Moeda"},
                    ],
                    "correct": "a",
                    "word_id": "es_agua", "target": "agua", "native": "água",
                    "npc_reaction": "El agua del pozo. La mejor del pueblo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Dime una cosa — ¿cómo estás hoy? El primer día siempre es duro.",
                    "translation": "Me diz uma coisa — como você está hoje? O primeiro dia sempre é duro.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "O sol da tarde te aquece, o pão da Rosa ainda morno no bolso. Você responde:",
                    "options": [
                        {"id": "a", "text": "Bien"},
                        {"id": "b", "text": "Mal"},
                        {"id": "c", "text": "Hola"},
                        {"id": "d", "text": "Gracias"},
                    ],
                    "correct": "a",
                    "word_id": "es_bien", "target": "bien", "native": "bem",
                    "npc_reaction": "Me alegro. Aquí siempre se está bien si el cuerpo aguanta y la gente saluda.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "¿Y sabes despedirte también, forastero?",
                    "translation": "E você sabe se despedir também, forasteiro?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen te olha esperando. Você precisa dizer tchau em espanhol.",
                    "options": [
                        {"id": "a", "text": "Adiós"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Gracias"},
                        {"id": "d", "text": "Bien"},
                    ],
                    "correct": "a",
                    "word_id": "es_adios", "target": "adiós", "native": "tchau / adeus",
                    "npc_reaction": "Bien. Aunque espero que no tan pronto, hijo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Ahora — pregúntale a Miguel cómo está.",
                    "translation": "Agora — pergunta pro Miguel como ele tá.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "Carmen aponta pra Miguel. É a sua vez de perguntar.",
                    "options": [
                        {"id": "a", "text": "¿Cómo estás?"},
                        {"id": "b", "text": "¿Cómo te llamas?"},
                        {"id": "c", "text": "¿Y tú?"},
                        {"id": "d", "text": "¿Adiós?"},
                    ],
                    "correct": "a",
                    "npc_reaction": "Bien. Como siempre que tengo a alguien queriendo aprender.",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel observa de pé, satisfeito. Carmen continua costurando.",
                },
            ],
        },
    },

    # ── Seção 5: Convivência com Carmen ────────────────────────────────────────
    # Carmen ensina sobre o ritmo social do pueblo enquanto costura.
    # Poucos exercícios — foco em desenvolver o personagem e contextualizar
    # o vocab em sabedoria local. buenas noches apresentado antes de ser testado.
    {
        "section_number": 5,
        "section_type": "reforco",
        "content": {
            "recap": {
                "characters": ["Miguel", "Carmen"],
                "story": (
                    "Miguel te apresentou a doña Carmen na plaza. Uma mulher mais "
                    "velha, costurando num banco de pedra, com olhar calmo de quem "
                    "viu tudo.\n\n"
                    "Você se apresentou, disse que estava bem. Carmen sorriu — 'aqui "
                    "sempre se está bem se o corpo aguanta e a gente cumprimenta'. "
                    "Agora ela quer te contar como o pueblo funciona."
                ),
                "now": "Carmen vai te ensinar o ritmo social — quando cumprimentar como, e por quê.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Aquí en el pueblo, somos pocos. Pero todos nos conocemos.",
                    "translation": "Aqui no pueblo, somos poucos. Mas todos nos conhecemos.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": "Miguel acena com a cabeça concordando, mas deixa Carmen falar.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Si saludas a alguien, te recordará. Si dices 'gracias', te invitará. Es así.",
                    "translation": "Se você cumprimenta alguém, vão lembrar. Se diz 'gracias', vão te convidar. É assim.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "La palabra más bonita del español es 'gracias'. No la olvides nunca.",
                    "translation": "A palavra mais bonita do espanhol é 'gracias'. Não esqueça nunca.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen aponta pra Miguel: 'Cuando él te dé algo — pan, agua, una palabra — ¿qué dices?'",
                    "options": [
                        {"id": "a", "text": "Gracias"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Bien"},
                        {"id": "d", "text": "Adiós"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Eso. Y si te lo dicen a ti...",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Miguel te entrega a manzana que estava no bolso dele. Você diz 'gracias'. Como ele responde?",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "Ese es el ciclo, hijo. Saludo, palabra, respuesta. Así vivimos.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Y cuando el sol se pone y llega la noche, decimos 'buenas noches'.",
                    "translation": "E quando o sol se põe e chega a noite, dizemos 'buenas noches' — boa noite.",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "O sol sumiu. Você encontra alguém na rua à noite. Como cumprimenta?",
                    "options": [
                        {"id": "a", "text": "Buenas noches"},
                        {"id": "b", "text": "Buenos días"},
                        {"id": "c", "text": "Buenas tardes"},
                        {"id": "d", "text": "Hola noche"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenas_noches", "target": "buenas noches", "native": "boa noite",
                    "npc_reaction": "Así. Cada hora tiene su saludo.",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Una última cosa, forastero — ¿cómo te llamas?",
                    "translation": "Uma última coisa, forasteiro — como você se chama?",
                    "pace": "slow",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Carmen",
                    "question": "Carmen te olha com um sorriso. Ela quer ouvir você dizer seu nome.",
                    "options": [
                        {"id": "a", "text": "Me llamo [seu nome]"},
                        {"id": "b", "text": "Bien, gracias"},
                        {"id": "c", "text": "Hola Carmen"},
                        {"id": "d", "text": "Soy forastero"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "Eso. Nunca olvides tu nombre cuando alguien te lo pida.",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Carmen volta ao bordado. O sol começou a baixar mais — "
                        "sombras compridas no chão de pedra."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Carmen",
                    "line": "Vuelve mañana si quieres. Siempre estoy aquí — en este banco, con la aguja en la mano.",
                    "translation": "Volta amanhã se quiser. Sempre estou aqui — neste banco, com a agulha na mão.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Vamos, forastero. Tem uma última coisa antes de você descansar.",
                    "translation": "Vamos. Tem uma última coisa antes de você descansar.",
                },
            ],
        },
    },

    # ── Seção 6: Obstáculo (gate final — gated) ────────────────────────────────
    # Miguel vira examinador. Cada exercício é um desafio dele direto.
    # Errar trava (frontend aplica isGated). Closing beats fazem a transição
    # pra la posada — onde a Fase 2 começa.
    {
        "section_number": 6,
        "section_type": "obstaculo",
        "content": {
            "recap": {
                "characters": ["Miguel"],
                "story": (
                    "Miguel encaixou tudo numa sequência e fez você repetir até "
                    "sair natural: '¡Hola! ¿Cómo estás?' — pausa — resposta — "
                    "'¿Y tú, cómo te llamas?'\n\n"
                    "Na terceira vez ele não corrigiu nada. Só tirou o chapéu por "
                    "um segundo — gesto sério. 'Bueno. Já pode falar com qualquer um.'\n\n"
                    "Aí o sorriso saiu do rosto. 'Agora vamos ver de verdade.'"
                ),
                "now": "Teste final. Errar trava — você precisa acertar pra passar.",
            },
            "steps": [
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Ya basta de explicaciones. Si te equivocas, repites. Sin atajos.",
                    "translation": "Chega de explicações. Se errar, repete. Sem atalho.",
                    "pace": "urgent",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "'Es la mañana. Llego a tu lado. ¿Qué dices?'",
                    "options": [
                        {"id": "a", "text": "¡Buenos días!"},
                        {"id": "b", "text": "¡Buenas tardes!"},
                        {"id": "c", "text": "¡Buenas noches!"},
                        {"id": "d", "text": "¡Hola noche!"},
                    ],
                    "correct": "a",
                    "word_id": "es_buenos_dias", "target": "buenos días", "native": "bom dia",
                    "npc_reaction": "¡Eso! Pasa.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "'Te di un pedazo de pan. Responde.'",
                    "options": [
                        {"id": "a", "text": "¡Gracias!"},
                        {"id": "b", "text": "¡Hola!"},
                        {"id": "c", "text": "¡Bien!"},
                        {"id": "d", "text": "¡Adiós!"},
                    ],
                    "correct": "a",
                    "word_id": "es_gracias", "target": "gracias", "native": "obrigado/a",
                    "npc_reaction": "Sigue.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "'Dijiste gracias. ¿Qué te respondo yo?'",
                    "options": [
                        {"id": "a", "text": "De nada"},
                        {"id": "b", "text": "Hola"},
                        {"id": "c", "text": "Bien"},
                        {"id": "d", "text": "Mal"},
                    ],
                    "correct": "a",
                    "word_id": "es_de_nada", "target": "de nada", "native": "de nada",
                    "npc_reaction": "¡Eso! É o ciclo.",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "'Yo te pregunto cómo te llamas. Tu respuesta empieza con...'",
                    "options": [
                        {"id": "a", "text": "Me llamo"},
                        {"id": "b", "text": "Soy llamo"},
                        {"id": "c", "text": "Mi llama"},
                        {"id": "d", "text": "Te llamo"},
                    ],
                    "correct": "a",
                    "word_id": "es_me_llamo", "target": "me llamo", "native": "meu nome é",
                    "npc_reaction": "¡Eso!",
                },
                {
                    "kind": "multiple_choice",
                    "npc": "Miguel",
                    "question": "'¿Cómo estás? Estás bien.'",
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
                # ── Closing beats — transição pra la posada ──────────────────
                {
                    "kind": "narrative",
                    "text": (
                        "Miguel ajeita o chapéu. O sol já tá baixo, sombras compridas "
                        "no chão de terra. Ele te dá um tapinha no ombro."
                    ),
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Ya hiciste mucho por hoy. Ven, vamos a la posada.",
                    "translation": "Já fez bastante por hoje. Vem, vamos pra posada.",
                    "pace": "slow",
                },
                {
                    "kind": "npc_speak",
                    "npc": "Miguel",
                    "line": "Descansa. Mañana hay más pueblo para conocer.",
                    "translation": "Descansa. Amanhã tem mais pueblo pra conhecer.",
                    "pace": "slow",
                },
                {
                    "kind": "narrative",
                    "text": (
                        "Vocês caminham pelas ruas de pedra. Primeiras luzes nas janelas. "
                        "Miguel te aponta uma casa de dois andares no canto da plaza — "
                        "la posada. Onde você vai dormir essa noite."
                    ),
                },
            ],
        },
    },
]


# ─── Command ──────────────────────────────────────────────────────────────────

class Command(BaseCommand):
    help = "Seed das 6 seções da Fase 1 Espanhol A1 (requer seed_es_full antes)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Apaga e recria as seções (default: pula se já existem)",
        )

    def handle(self, *args, **options):
        self.stdout.write("\n📦 Seeding seções — ES A1 T1 Fase 1\n")

        try:
            chapter = AdventureChapter.objects.get(slug="es-a1-t1")
        except AdventureChapter.DoesNotExist:
            raise CommandError(
                "Chapter 'es-a1-t1' não encontrado. Rode 'seed_es_full' primeiro."
            )

        try:
            phase = AdventurePhase.objects.get(chapter=chapter, number=1)
        except AdventurePhase.DoesNotExist:
            raise CommandError(
                "Fase 1 do chapter 'es-a1-t1' não encontrada. Rode 'seed_es_full' primeiro."
            )

        existing = PhaseSection.objects.filter(phase=phase).count()
        if existing and not options["reset"]:
            self.stdout.write(
                self.style.WARNING(
                    f"  Fase 1 já tem {existing} seções. Use --reset para recriar."
                )
            )
            return

        if options["reset"]:
            deleted, _ = PhaseSection.objects.filter(phase=phase).delete()
            self.stdout.write(f"  ↻ {deleted} seções apagadas")

        created_count = 0
        for sec in SECTIONS:
            PhaseSection.objects.create(
                phase=phase,
                section_number=sec["section_number"],
                section_type=sec["section_type"],
                content=hydrate_section_content(sec["content"]),
            )
            self.stdout.write(
                f"  ✓ Seção {sec['section_number']}: {sec['section_type']}"
            )
            created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"\n✅ {created_count} seções criadas para Fase 1 · ES A1 T1\n"
            "   Endpoint: GET /api/adventure/phases/{phase_id}/sections/\n"
        ))
