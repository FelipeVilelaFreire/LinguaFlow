"""
Seed ES A1 T1 · "El Pueblo de San Cristóbal" — todas as 25 fases.

Cria/atualiza: chapter, cenários, frases, personagens, itens e fases 1–25.
As seções de cada fase vivem em seeds separados (seed_es_sections, seed_es_f2_sections, etc.)

Uso: python manage.py seed_es_full
"""
from django.core.management.base import BaseCommand

from apps.adventure.models import (
    AdventureCharacter,
    AdventureChapter,
    AdventureItem,
    AdventurePhase,
    AdventureSkill,
)
from apps.learning.models import Language, Phrase, Scenario

from apps.adventure.seeds.skills import seed_chapter_skills, sync_chapter_item_skills


# ═══════════════════════════════════════════════════════════════════════════════
# CENÁRIOS
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIOS = [
    ("es-social",   "Social",     "Saudações, apresentações e convívio."),
    ("es-lugares",  "Lugares",    "Orientação, direções e pontos do pueblo."),
    ("es-comida",   "Comida",     "Alimentação, pedidos e sabores."),
    ("es-mercado",  "Mercado",    "Compras, preços e negociação."),
    ("es-salud",    "Salud",      "Saúde, corpo e cuidado pessoal."),
    ("es-trabalho", "Trabajo",    "Trabalho, ofícios e rotina."),
    ("es-historia", "Historia",   "Memória, passado e mistério."),
    ("es-desafio",  "Desafío",    "Provas, conflito e decisões."),
]


# ═══════════════════════════════════════════════════════════════════════════════
# FRASES PT → ES
# ═══════════════════════════════════════════════════════════════════════════════

PHRASES: list[tuple[str, str, str]] = [

    # ── es-social ──────────────────────────────────────────────────────────────
    ("Olá",                        "Hola",                   "es-social"),
    ("Bom dia",                    "Buenos días",            "es-social"),
    ("Boa tarde",                  "Buenas tardes",          "es-social"),
    ("Boa noite",                  "Buenas noches",          "es-social"),
    ("Tchau",                      "Adiós",                  "es-social"),
    ("Até logo",                   "Hasta luego",            "es-social"),
    ("Meu nome é",                 "Me llamo",               "es-social"),
    ("Como você se chama?",        "¿Cómo te llamas?",       "es-social"),
    ("Prazer",                     "Mucho gusto",            "es-social"),
    ("Forasteiro",                 "Forastero",              "es-social"),
    ("Fazendeiro",                 "Campesino",              "es-social"),
    ("Bem",                        "Bien",                   "es-social"),
    ("Por favor",                  "Por favor",              "es-social"),
    ("Obrigado",                   "Gracias",                "es-social"),
    ("De nada",                    "De nada",                "es-social"),
    ("Amigo",                      "Amigo",                  "es-social"),
    ("Passo a passo",              "Paso a paso",            "es-social"),
    ("Sente-se",                   "Siéntate",               "es-social"),
    ("Sim",                        "Sí",                     "es-social"),
    ("Não",                        "No",                     "es-social"),

    # ── es-lugares ─────────────────────────────────────────────────────────────
    ("Onde fica?",                 "¿Dónde está?",           "es-lugares"),
    ("À esquerda",                 "A la izquierda",         "es-lugares"),
    ("À direita",                  "A la derecha",           "es-lugares"),
    ("Em frente",                  "Enfrente",               "es-lugares"),
    ("Aqui",                       "Aquí",                   "es-lugares"),
    ("Ali",                        "Allá",                   "es-lugares"),
    ("O mercado",                  "El mercado",             "es-lugares"),
    ("A praça",                    "La plaza",               "es-lugares"),
    ("A pousada",                  "La posada",              "es-lugares"),
    ("A Igreja",                   "La iglesia",             "es-lugares"),
    ("O portão",                   "La puerta",              "es-lugares"),
    ("O poço",                     "El pozo",                "es-lugares"),
    ("A cidade",                   "La ciudad",              "es-lugares"),
    ("O caminho",                  "El camino",              "es-lugares"),
    ("Próximo",                    "Cerca",                  "es-lugares"),

    # ── es-comida ──────────────────────────────────────────────────────────────
    ("Estou com fome",             "Tengo hambre",           "es-comida"),
    ("Estou com sede",             "Tengo sed",              "es-comida"),
    ("Água",                       "Agua",                   "es-comida"),
    ("Pão",                        "Pan",                    "es-comida"),
    ("Tortilha",                   "Tortilla",               "es-comida"),
    ("Feijão",                     "Frijoles",               "es-comida"),
    ("Queijo",                     "Queso",                  "es-comida"),
    ("Fruta",                      "Fruta",                  "es-comida"),
    ("Carne",                      "Carne",                  "es-comida"),
    ("Quero comer",                "Quiero comer",           "es-comida"),
    ("Está bom",                   "Está bueno",             "es-comida"),
    ("Muito gostoso",              "Muy rico",               "es-comida"),
    ("A mesa",                     "La mesa",                "es-comida"),
    ("A taverna",                  "La taberna",             "es-comida"),
    ("Um prato",                   "Un plato",               "es-comida"),

    # ── es-mercado ─────────────────────────────────────────────────────────────
    ("Quanto custa?",              "¿Cuánto cuesta?",        "es-mercado"),
    ("Muito caro",                 "Muy caro",               "es-mercado"),
    ("Barato",                     "Barato",                 "es-mercado"),
    ("Quero comprar",              "Quiero comprar",         "es-mercado"),
    ("Dinheiro",                   "Dinero",                 "es-mercado"),
    ("Moeda",                      "Moneda",                 "es-mercado"),
    ("Tem desconto?",              "¿Hay descuento?",        "es-mercado"),
    ("Vou levar",                  "Me lo llevo",            "es-mercado"),
    ("Vendedor",                   "Vendedor",               "es-mercado"),
    ("Permissão",                  "Permiso",                "es-mercado"),
    ("Documento",                  "Documento",              "es-mercado"),
    ("Passe",                      "Pase",                   "es-mercado"),

    # ── es-salud ───────────────────────────────────────────────────────────────
    ("Estou doente",               "Estoy enfermo",          "es-salud"),
    ("Dói aqui",                   "Me duele aquí",          "es-salud"),
    ("Curandeira",                 "Curandera",              "es-salud"),
    ("Remédio",                    "Medicina",               "es-salud"),
    ("Melhor",                     "Mejor",                  "es-salud"),
    ("Descanse",                   "Descanse",               "es-salud"),
    ("Erva",                       "Hierba",                 "es-salud"),
    ("Mão",                        "Mano",                   "es-salud"),
    ("Cabeça",                     "Cabeza",                 "es-salud"),
    ("Cansado",                    "Cansado",                "es-salud"),

    # ── es-trabalho ────────────────────────────────────────────────────────────
    ("Ferreiro",                   "Herrero",                "es-trabalho"),
    ("Padeira",                    "Panadera",               "es-trabalho"),
    ("Cozinheiro",                 "Cocinero",               "es-trabalho"),
    ("Sentinela",                  "Vigilante",              "es-trabalho"),
    ("Trabalho",                   "Trabajo",                "es-trabalho"),
    ("Trabalho muito",             "Trabajo mucho",          "es-trabalho"),
    ("De onde você vem?",          "¿De dónde vienes?",      "es-trabalho"),
    ("Venho de longe",             "Vengo de lejos",         "es-trabalho"),
    ("Forte",                      "Fuerte",                 "es-trabalho"),
    ("Ferro",                      "Hierro",                 "es-trabalho"),

    # ── es-historia ────────────────────────────────────────────────────────────
    ("Não me lembro",              "No recuerdo",            "es-historia"),
    ("Meu passado",                "Mi pasado",              "es-historia"),
    ("Esqueci",                    "Olvidé",                 "es-historia"),
    ("É verdade",                  "Es verdad",              "es-historia"),
    ("É mentira",                  "Es mentira",             "es-historia"),
    ("Segredo",                    "Secreto",                "es-historia"),
    ("Perigo",                     "Peligro",                "es-historia"),
    ("Cuidado",                    "Cuidado",                "es-historia"),
    ("Conheço",                    "Conozco",                "es-historia"),
    ("Preciso ir",                 "Necesito irme",          "es-historia"),
    ("Ficar",                      "Quedarme",               "es-historia"),
    ("Futuro",                     "Futuro",                 "es-historia"),

    # ── es-desafio ─────────────────────────────────────────────────────────────
    ("Prova",                      "Prueba",                 "es-desafio"),
    ("Mostrar",                    "Demostrar",              "es-desafio"),
    ("Respeito",                   "Respeto",                "es-desafio"),
    ("Honra",                      "Honor",                  "es-desafio"),
    ("Julgamento",                 "Juicio",                 "es-desafio"),
    ("Estrangeiro",                "Extranjero",             "es-desafio"),
    ("Provar que",                 "Demostrar que",          "es-desafio"),
    ("Deixar passar",              "Dejar pasar",            "es-desafio"),
    ("Autoridade",                 "Autoridad",              "es-desafio"),
    ("Bem-vindo",                  "Bienvenido",             "es-desafio"),
]


# ═══════════════════════════════════════════════════════════════════════════════
# FASES
# ═══════════════════════════════════════════════════════════════════════════════

PHASES = [
    {
        "number": 1, "phase_type": "story",
        "title": "O Despertar no Campo",
        "narrative_intro": (
            "Você acorda sozinho num campo de milho dourado. Não sabe seu nome — "
            "não sabe de onde veio. Um homem de sombrero caminha na sua direção.\n\n"
            "'¡Oye, forastero! ¿Estás bien?'"
        ),
        "narrative_outro": (
            "Você aprendeu as primeiras palavras e Don Miguel te acompanhou até a posada do pueblo. "
            "Antes de entrar, ele te dá um tapinha no ombro:\n\n"
            "'Descansa, forastero. Mañana es otro día.'"
        ),
        "key_words": ["hola", "me llamo", "forastero", "campesino", "bien"],
        "scenario_slug": "es-social", "phrase_count": 8,
    },
    {
        "number": 2, "phase_type": "story",
        "title": "El Pueblo Despierta",
        "narrative_intro": (
            "A manhã chega com cheiro de pão. Don Miguel bate na sua porta cedo — "
            "tem mais pueblo pra conhecer.\n\n"
            "'¡Buenos días, forastero! Rosa tiene pan.'"
        ),
        "narrative_outro": (
            "Você se virou sozinho na plaza pela primeira vez. E alguém com chapéu "
            "baixo passou olhando demais.\n\n"
            "'Vamos pra posada. Fica perto de mim.' — Don Miguel"
        ),
        "key_words": ["pan", "agua", "tengo hambre", "tengo sed"],
        "scenario_slug": "es-comida", "phrase_count": 8,
    },
    {
        "number": 3, "phase_type": "story",
        "title": "El Camino de Tierra",
        "narrative_intro": (
            "Don Miguel te leva pra fora dos muros do pueblo pela primeira vez. "
            "Campo aberto, caminho de terra, árboles ao longe.\n\n"
            "'Hay cosas que el pueblo no te enseña.'"
        ),
        "narrative_outro": (
            "O velho Ernesto te entregou uma pedra do río sem explicar por quê. "
            "'Tienes algo en los ojos. Como los que escuchan la tierra.'\n\n"
            "Você ainda estava pensando nisso quando chegaram ao pueblo."
        ),
        "key_words": ["árbol", "piedra", "río", "hay", "no hay"],
        "scenario_slug": "es-lugares", "phrase_count": 8,
    },
    {
        "number": 4, "phase_type": "story",
        "title": "El Mercado",
        "narrative_intro": (
            "Dia de mercado — a plaza inteira vira um labirinto de bancas. "
            "Don Miguel te ensina a contar e a barganhar.\n\n"
            "'Aquí te enganam se você não sabe os números.'"
        ),
        "narrative_outro": (
            "Carmen avisou Don Miguel em voz baixa. Alguém novo no pueblo "
            "fazendo perguntas. Sobre o forasteiro.\n\n"
            "Miguel ficou mais quieto na volta."
        ),
        "key_words": ["naranja", "uno", "dos", "tres", "mucho", "poco"],
        "scenario_slug": "es-mercado", "phrase_count": 8,
    },
    {
        "number": 5, "phase_type": "story",
        "title": "La Primera Chispa",
        "narrative_intro": (
            "Algo está errado no pueblo. Don Miguel muda a rota, fala menos, "
            "fica mais perto. À noite, um barulho no corredor da posada.\n\n"
            "'Fuego. Correr. Miedo.' — as palavras que você vai precisar."
        ),
        "narrative_outro": (
            "A palavra 'fuego' saiu antes de você pensar. E o corredor explodiu em luz.\n\n"
            "El Vigilante fugiu. Don Miguel olhou pras suas mãos por um longo segundo.\n\n"
            "'Entra. Cierra la puerta. Tenemos que hablar.'"
        ),
        "key_words": ["miedo", "fuego", "correr", "corre", "para"],
        "scenario_slug": "es-desafio", "phrase_count": 8,
    },
    {
        "number": 6, "phase_type": "story",
        "title": "Lo que vio Sofía",
        "narrative_intro": (
            "Don Miguel tranca a porta do quarto. Ele te explica em espanhol simples "
            "o que ele acha que aconteceu — não tem palavras pra isso.\n\n"
            "'Voy a buscar a alguien que sabe leer estas cosas.'"
        ),
        "narrative_outro": (
            "Sofía não recuou ao ver a lamparina acender. Riu — uma risada curta, "
            "decidida. 'Vale. Yo voy con vosotros.'\n\n"
            "Pela primeira vez você não está sozinho no que aconteceu."
        ),
        "key_words": ["luz", "chispa", "yo voy", "tú vienes", "lámpara"],
        "scenario_slug": "es-historia", "phrase_count": 8,
    },
    {
        "number": 7, "phase_type": "story",
        "title": "El día normal",
        "narrative_intro": (
            "Sofía aparece na plaza pela manhã como se fossem amigos há anos. "
            "Miguel decide que o forastero precisa aprender a viver como gente daqui.\n\n"
            "'Hoy nada raro. Sólo pueblo.'"
        ),
        "narrative_outro": (
            "À noite a febre começou. Atrás dos olhos, depois na cabeça inteira.\n\n"
            "Sofía: 'Conozco a una. Llega de fuera, pero cura bien.'\n\n"
            "Miguel sai correndo pelas ruas escuras."
        ),
        "key_words": ["hoy", "mañana", "vecino", "tengo años", "me llamo"],
        "scenario_slug": "es-social", "phrase_count": 8,
    },
    {
        "number": 8, "phase_type": "story",
        "title": "La curandera",
        "narrative_intro": (
            "Sofía traz uma mulher de 24 anos com mãos firmes e olhar paciente. "
            "Pousa a mão na sua têmpora — e a expressão dela muda por um segundo.\n\n"
            "'Está bien. Voy a hacer una infusión.'"
        ),
        "narrative_outro": (
            "Don Miguel ofereceu a casa de hóspedes a María até passar tudo. "
            "Ela aceitou. Está dentro do círculo agora.\n\n"
            "Você não sabe que ela soube quem você era no instante em que te tocou."
        ),
        "key_words": ["cabeza", "fiebre", "manos", "estoy enfermo", "mejor"],
        "scenario_slug": "es-salud", "phrase_count": 8,
    },
    {
        "number": 9, "phase_type": "story",
        "title": "Cuatro a la mesa",
        "narrative_intro": (
            "Primeira manhã com María na casa. Café fumegante, pão fresco, "
            "Sofía rindo de alguma coisa. O grupo de 4 começou.\n\n"
            "'Vamos al mercado. Hay que reponer.'"
        ),
        "narrative_outro": (
            "Voltando do mercado, Miguel sussurra: 'Esta mujer me da algo raro. No sé qué.'\n\n"
            "Você não sabe ainda o que olhar — mas vê El Vigilante de longe, observando o grupo. "
            "Quando pisca, ele já foi embora."
        ),
        "key_words": ["comida", "café", "me gusta", "no me gusta", "naranja"],
        "scenario_slug": "es-comida", "phrase_count": 8,
    },
    {
        "number": 10, "phase_type": "story",
        "title": "La sombra del Vigilante",
        "narrative_intro": (
            "Uma rua estreita perto do mercado. El Vigilante bloqueia o caminho.\n\n"
            "'El pase de forastero. Sin pase, sales del pueblo antes del atardecer.'"
        ),
        "narrative_outro": (
            "María sussurrou três frases pra El Vigilante. Ele recuou. Foi embora.\n\n"
            "'Conocidos antiguos.' — ela disse pro grupo, sorrindo.\n\n"
            "Don Miguel à noite: 'El pase sólo lo da el Alcalde. Y eso va a ser un problema.'"
        ),
        "key_words": ["pase", "alcalde", "ven", "para", "mira"],
        "scenario_slug": "es-desafio", "phrase_count": 8,
    },
    {
        "number": 11, "phase_type": "story",
        "title": "El Ayuntamiento",
        "narrative_intro": (
            "Amanhecer. Os quatro chegam ao ayuntamiento — pedra grossa, porta "
            "de ferro. O Alcalde recebe sem se levantar.\n\n"
            "'¿Forastero sin papeles? Vamos a ver.'"
        ),
        "narrative_outro": (
            "O Alcalde não concedeu o pase. 'Vuelvan en tres días — con testigos.'\n\n"
            "Saindo, Don Miguel sussurrou: 'Esto no es sobre el pase. Es sobre saber "
            "quién eres.'"
        ),
        "key_words": ["testigo", "papel", "sello", "voy a", "vamos a"],
        "scenario_slug": "es-desafio", "phrase_count": 8,
    },
    {
        "number": 12, "phase_type": "story",
        "title": "Tres días",
        "narrative_intro": (
            "Vocês têm três dias pra reunir testemunhas. Carmen aceita. "
            "Eduardo o ferreiro também — mas pede algo em troca.\n\n"
            "'Yo te vi en la calle. Yo te oí saludar. Eso digo.'"
        ),
        "narrative_outro": (
            "Voltando da herrería, El Vigilante passa pelo cruzamento e olha demais.\n\n"
            "Miguel: 'Nos sigue desde ayer. Hoy oí sus pasos en el callejón.'"
        ),
        "key_words": ["ayer", "vi", "oí", "hablé", "recuerdo"],
        "scenario_slug": "es-historia", "phrase_count": 8,
    },
    {
        "number": 13, "phase_type": "story",
        "title": "La familia de Miguel",
        "narrative_intro": (
            "Miguel leva o grupo pra casa da mãe dele essa noite — Doña Lucía. "
            "Mesa cheia, irmãs jovens, cheiro de guiso.\n\n"
            "'Mi madre. Mis hermanas. Mi casa también es tuya.'"
        ),
        "narrative_outro": (
            "Doña Lucía olhou pra María por longo tempo antes de dormir.\n\n"
            "'A esa mujer la conozco de algún sitio. No recuerdo de dónde.' — sussurrou "
            "pra Miguel quando o resto já dormia."
        ),
        "key_words": ["madre", "padre", "hermana", "hermano", "mi", "tu", "su"],
        "scenario_slug": "es-social", "phrase_count": 8,
    },
    {
        "number": 14, "phase_type": "review",
        "title": "La cena de María",
        "narrative_intro": (
            "María convidou todos pra jantar na casa de hóspedes. Vela "
            "acesa, pão na mesa, vinho. María observando.\n\n"
            "'Cuéntenme. Todo. Desde el principio.'"
        ),
        "narrative_outro": (
            "Você relatou tudo. María ouvia sem perguntar. No fim, fez uma "
            "única pergunta que ninguém esperava:\n\n"
            "'¿Y la palabra que dijiste — fuego — la sentiste subir desde dónde?'\n\n"
            "Ninguém tinha contado pra ela onde sentiu."
        ),
        "key_words": ["el", "la", "los", "las", "recuerdo"],
        "scenario_slug": "es-historia", "phrase_count": 8,
    },
    {
        "number": 15, "phase_type": "story",
        "title": "El primer testigo",
        "narrative_intro": (
            "Carmen veste a melhor blusa. Vai com vocês ao ayuntamiento. "
            "Sentou na frente do Alcalde como quem já tinha sentado ali antes.\n\n"
            "'Yo testifico. Conozco al forastero.'"
        ),
        "narrative_outro": (
            "O Alcalde aceitou o depoimento — mas pediu mais provas. El "
            "Vigilante observou tudo do fundo da sala.\n\n"
            "Saindo, Carmen sussurrou pra María: 'Ese hombre y yo — tenemos historia.'"
        ),
        "key_words": ["alto", "bajo", "joven", "viejo", "delgado"],
        "scenario_slug": "es-desafio", "phrase_count": 8,
    },
    {
        "number": 16, "phase_type": "story",
        "title": "Lo que Carmen no contó",
        "narrative_intro": (
            "Os três jovens encontram Carmen sozinha na plaza. Sem María. "
            "Ela espera vocês com o bordado nas mãos.\n\n"
            "'Quería contarles algo. Antes que sea tarde.'"
        ),
        "narrative_outro": (
            "Carmen contou. Foi noiva do Alcalde há 25 anos. O pai dele "
            "quebrou o noivado.\n\n"
            "Voltando pra casa — María estava na porta. 'Forastero — "
            "¿dónde estuviste?' Você mentiu pela primeira vez."
        ),
        "key_words": ["amor", "novio", "casarse", "quiero", "antes"],
        "scenario_slug": "es-historia", "phrase_count": 8,
    },
    {
        "number": 17, "phase_type": "story",
        "title": "Eduardo y la marca",
        "narrative_intro": (
            "Don Miguel marca o encontro no pátio da herrería ao fim do dia. "
            "Eduardo, María, Don Miguel e você. Sofía e Miguel ficam de fora.\n\n"
            "Eduardo abre a camisa parcialmente. María olha. Não disfarça."
        ),
        "narrative_outro": (
            "A marca era da irmandade dos Buscadores — gente que rastreava "
            "palabras antigas. Eduardo saiu faz décadas.\n\n"
            "María: 'Mi familia tenía relación con esa gente.' Don Miguel "
            "olhou pra ela diferente. Nada igual depois."
        ),
        "key_words": ["espalda", "marca", "familia", "ya", "todavía"],
        "scenario_slug": "es-historia", "phrase_count": 8,
    },
    {
        "number": 18, "phase_type": "story",
        "title": "Don Miguel se entera",
        "narrative_intro": (
            "Você decide contar a Don Miguel. Sofía conta o que Carmen "
            "disse. Miguel conta o sussurro da mãe.\n\n"
            "Três pistas sobre María — agora juntas pela primeira vez."
        ),
        "narrative_outro": (
            "Don Miguel ouviu tudo. Não falou por um minuto inteiro. "
            "Depois: 'No podemos echarla. Aún no. Pero la observamos.'\n\n"
            "E antes de você dormir: 'Hijo — voy a enseñarte una cosa "
            "que necesitas saber. La carta.'"
        ),
        "key_words": ["verdad", "mentir", "confiar", "puedo", "podemos"],
        "scenario_slug": "es-historia", "phrase_count": 8,
    },
    {
        "number": 19, "phase_type": "review",
        "title": "La carta",
        "narrative_intro": (
            "Don Miguel tira do baú uma carta selada de cera vermelha. O "
            "selo tem o mesmo símbolo da marca de Eduardo.\n\n"
            "'Esta carta llegó a mis manos hace veinte años. Hoy te la enseño.'"
        ),
        "narrative_outro": (
            "Você olhou. Quase tudo ilegível. Mas no centro — uma palavra "
            "ficou clara, escura como tinta fresca.\n\n"
            "'Vuelves.'\n\n"
            "Você sentiu algo no peito. A carta sabe mais sobre você do que "
            "você sabe."
        ),
        "key_words": ["carta", "leer", "palabra", "vuelves"],
        "scenario_slug": "es-historia", "phrase_count": 8,
    },
    {
        "number": 20, "phase_type": "story",
        "title": "La visita inesperada",
        "narrative_intro": (
            "Manhã cheia. Sofía corre pra casa de Don Miguel. 'Hay un hombre "
            "extranjero en la plaza. Pregunta por María — la llama por otro "
            "nombre.'\n\n"
            "Vocês todos se levantam ao mesmo tempo."
        ),
        "narrative_outro": (
            "El Inspector falou com María dez minutos. Trocou um papel. "
            "Apontou pra casa de Don Miguel. Foi embora antes do meio-dia.\n\n"
            "À noite, María voltou calorosa como sempre. 'Hoy fue tranquilo, "
            "¿no?' Ninguém respondeu."
        ),
        "key_words": ["visita", "llegar", "esperar", "tengo que", "hay que"],
        "scenario_slug": "es-desafio", "phrase_count": 8,
    },
    {
        "number": 21, "phase_type": "story",
        "title": "El confronto a María",
        "narrative_intro": (
            "Amanhecer no quarto da casa de hóspedes. María já está sentada "
            "na cadeira esperando. 'Sé por qué viniste.'"
        ),
        "narrative_outro": (
            "María não negou nada. Mas também não revelou o nome verdadeiro. "
            "'Cuando puedan saber, sabrán. Hoy no es el día.'"
        ),
        "key_words": ["cuando", "saber", "decir", "verdad"],
        "scenario_slug": "es-historia", "phrase_count": 8,
    },
    {
        "number": 22, "phase_type": "story",
        "title": "La verdad parcial",
        "narrative_intro": (
            "Carmen veio. Trouxe um envelope velho — guardava há 20 anos pelo "
            "Buscador que entregou a carta a Don Miguel. 'Esto pertenece al "
            "forastero. No a Don Miguel.'"
        ),
        "narrative_outro": (
            "Você abriu. Era um nome — escrito em letra firme. Não 'forastero'. "
            "Um nome. Você sentou no chão sem se mexer por um minuto."
        ),
        "key_words": ["contar", "guardar", "nombre", "pertenece"],
        "scenario_slug": "es-historia", "phrase_count": 8,
    },
    {
        "number": 23, "phase_type": "story",
        "title": "El plan del Alcalde",
        "narrative_intro": (
            "El Inspector volta. Não vem sozinho — três homens de uniforme "
            "atrás. Sofía corre. 'Vienen a por el forastero. Hoy.'\n\n"
            "Don Miguel pega a carta do baú."
        ),
        "narrative_outro": (
            "Os três homens cercaram a casa. María saiu primeiro — falou "
            "com eles dez minutos. Quando voltou, disse: 'Tienen orden de "
            "llevarte al Alcalde. Si los acompañas pacíficamente, no hay sangre.'"
        ),
        "key_words": ["si", "orden", "uniforme", "acompañar"],
        "scenario_slug": "es-desafio", "phrase_count": 8,
    },
    {
        "number": 24, "phase_type": "story",
        "title": "La víspera del juicio",
        "narrative_intro": (
            "Cela do ayuntamiento. Frio. Pedra úmida. Don Miguel suborna o "
            "guarda da noite — uma hora. Sofía, Miguel e María entram com "
            "ele.\n\n"
            "'Mañana es el juicio. Hoy revisamos todo.'"
        ),
        "narrative_outro": (
            "María entregou o frasco com Hierba de María — pra você dormir "
            "antes do dia mais difícil.\n\n"
            "'Bébetelo. Mañana vas a necesitar la cabeza clara.'"
        ),
        "key_words": ["juicio", "cárcel", "soborno", "guarda"],
        "scenario_slug": "es-desafio", "phrase_count": 8,
    },
    {
        "number": 25, "phase_type": "boss",
        "title": "El Jefe del Pueblo",
        "narrative_intro": (
            "Sala de julgamento. Alcalde no centro. Inspector de pé. Três "
            "guardas. O grupo de você, atrás. Carmen na fila do público.\n\n"
            "O Alcalde se levanta — pela primeira vez em todas as suas "
            "aparições. 'Forastero — el juicio empieza ahora.'"
        ),
        "narrative_outro": (
            "Carmen levantou-se do público. Falou três frases que ninguém "
            "esperava — sobre o pai do Alcalde, sobre o noivado quebrado, "
            "sobre a vergonha guardada 25 anos.\n\n"
            "O Alcalde empalideceu. Sentou. Sem voz por meio minuto. Depois "
            "carimbou o pase definitivo — em silêncio.\n\n"
            "Saindo, na sua mão: o **Sello del Pueblo**. E no fundo do "
            "peito, uma segunda palavra da carta se acendeu — *'Hermano.'*"
        ),
        "key_words": ["juicio", "vergüenza", "sello", "hermano"],
        "scenario_slug": "es-desafio", "phrase_count": 10,
    },
]


# ═══════════════════════════════════════════════════════════════════════════════
# PERSONAGENS
# ═══════════════════════════════════════════════════════════════════════════════

CHARACTERS = [
    (
        "don_miguel",
        "Don Miguel el Campesino",
        "Campesino",
        "👨‍🌾",
        "ally",
        True,
        1,
        1,
        "Un campesino mayor de San Cristobal. Habla despacio, observa antes de actuar y guia al forastero con paciencia.",
        "Poco a poco, amigo. La lengua se aprende viviendo.",
    ),
    (
        "miguel",
        "Miguel el Campesino",
        "Campesino",
        "🧑‍🌾",
        "ally",
        True,
        1,
        2,
        "Un joven del pueblo, leal e irreverente. Conoce cada calle, cada favor pendiente y cada atajo de San Cristobal.",
        "Fica perto de mim, forastero. Aqui todo mundo fala rapido.",
    ),
    (
        "rosa_panadera",
        "Rosa la Panadera",
        "Panadera",
        "👩‍🍳",
        "npc",
        False,
        1,
        3,
        "La panadera del pueblo. Calida, rapida y sonriente, aparece con harina en las manos y pan recien hecho.",
        "¡Hola, hola! Bienvenido.",
    ),
    (
        "ernesto",
        "Ernesto",
        "Leñador",
        "🪓",
        "npc",
        False,
        3,
        4,
        "Un lenador viejo y reservado. Habla poco, mira el rio como si guardara secretos y entrega ayuda sin explicar demasiado.",
        "La piedra recuerda mas que nosotros.",
    ),
    (
        "mercader",
        "El Mercader",
        "Mercader",
        "🍊",
        "npc",
        False,
        4,
        5,
        "Un vendedor atento y calculador. Sonrie mientras cuenta monedas, frutas y silencios ajenos en el mercado.",
        "Tres naranjas, dos monedas. Buen trato.",
    ),
    (
        "vigilante",
        "El Vigilante del Mercado",
        "Vigilante",
        "💂",
        "npc",
        False,
        5,
        6,
        "El guardia del mercado. Vigila puertas, pases y movimientos sospechosos con una severidad dificil de ignorar.",
        "El pase o la puerta. No hay otra opción.",
    ),
    (
        "senora_carmen",
        "Señora Carmen",
        "Vecina",
        "👩",
        "npc",
        False,
        4,
        7,
        "Una vecina atenta del pueblo. Conoce a todos, recuerda cada gesto y defiende las pequenas reglas de la convivencia.",
        "La palabra más bonita del español es 'gracias'.",
    ),
    (
        "sofia",
        "Sofía",
        "Compañera",
        "🙋‍♀️",
        "ally",
        False,
        6,
        8,
        "Una aliada curiosa y electrica, lista para unir pistas, personas y palabras que parecen lejanas.",
        "Vale. Yo voy con vosotros.",
    ),
    (
        "maria",
        "María",
        "Curandera",
        "🌿",
        "ally",
        False,
        8,
        9,
        "Una curandera sabia y protectora en la superficie, con una paciencia peligrosa y un plan que avanza en silencio.",
        "Bébete esto si vuelve a subirte la fiebre.",
    ),
    (
        "alcalde",
        "El Alcalde",
        "Alcalde",
        "🎩",
        "boss",
        False,
        11,
        10,
        "El Alcalde de San Cristóbal. Hombre politico que no se levanta para saludar, calculador y celoso de cada papel sellado del pueblo.",
        "El pase no se da. Se gana.",
    ),
    (
        "dona_lucia",
        "Doña Lucía",
        "Madre",
        "👵",
        "npc",
        False,
        13,
        11,
        "La madre de Miguel. Mujer firme y observadora, recuerda caras viejas mejor de lo que admite y guarda el hogar con dos manos.",
        "Mi casa también es tuya, forastero.",
    ),
    (
        "inspector",
        "El Inspector",
        "Inspector",
        "🕴️",
        "npc",
        False,
        20,
        12,
        "Un hombre de fuera, primo del Alcalde. Llega con papeles, hace preguntas y se va antes del mediodía. Conoce a María por otro nombre.",
        "Vengo por orden del distrito. No me dilato.",
    ),
]


# ═══════════════════════════════════════════════════════════════════════════════
# ITENS  (nenhum ainda — sem boss na fase 1)
# ═══════════════════════════════════════════════════════════════════════════════

ITEMS: list = []


# ═══════════════════════════════════════════════════════════════════════════════
# COMMAND
# ═══════════════════════════════════════════════════════════════════════════════

class Command(BaseCommand):
    help = "Seed ES A1 T1 — El Pueblo, fases 1-25"

    def handle(self, *args, **options):
        self.stdout.write("\n📦 Iniciando seed ES A1 T1 — El Pueblo (fases 1-25)\n")

        # ── 1. Idiomas ────────────────────────────────────────────────────────
        pt, _ = Language.objects.get_or_create(code="PT", defaults={"name": "Português", "is_ready": False})
        es, created = Language.objects.get_or_create(code="ES", defaults={"name": "Español", "is_ready": True})
        if not created:
            Language.objects.filter(code="ES").update(is_ready=True)
        self.stdout.write("  ✓ Idiomas: PT, ES")

        # ── 2. Cenários ───────────────────────────────────────────────────────
        scenario_objs: dict[str, Scenario] = {}
        for slug, title, description in SCENARIOS:
            obj, _ = Scenario.objects.get_or_create(
                slug=slug, defaults={"title": title, "description": description}
            )
            scenario_objs[slug] = obj
        self.stdout.write(f"  ✓ Cenários: {len(scenario_objs)} criados/existentes")

        # ── 3. Frases PT→ES ───────────────────────────────────────────────────
        phrase_count = 0
        for source_text, target_text, scenario_slug in PHRASES:
            _, created = Phrase.objects.get_or_create(
                source_language=pt,
                target_language=es,
                source_text=source_text,
                target_text=target_text,
                defaults={"scenario": scenario_objs[scenario_slug], "difficulty": "A1"},
            )
            if created:
                phrase_count += 1
        self.stdout.write(f"  ✓ Frases PT→ES: {phrase_count} novas ({len(PHRASES)} total)")

        # ── 4. Chapter ────────────────────────────────────────────────────────
        chapter, _ = AdventureChapter.objects.update_or_create(
            slug="es-a1-t1",
            defaults={
                "language":           es,
                "level":              "A1",
                "order":              1,
                "title":              "El Pueblo",
                "subtitle":           "T1 · A chegada",
                "background":         "es_pueblo",
                "boss_name":          "El Jefe del Pueblo",
                "boss_intro": (
                    "O senhor do pueblo. Ninguém passa pela Ciudad de la Plata "
                    "sem o seu sello — e ele não dá sellos de graça."
                ),
                "reward_name":        "Sello del Pueblo",
                "reward_description": (
                    "Impresso em cera vermelha. Prova que você sobreviveu ao Pueblo "
                    "e conhece as suas regras."
                ),
            },
        )
        self.stdout.write(f"  ✓ Chapter: {chapter.slug}")

        # ── 5. Fases ──────────────────────────────────────────────────────────
        skill_defs = [
            {"slug": "armas", "name": "Armas", "description": "Combate com ferramentas e armas.", "category": AdventureSkill.CATEGORY_COMBATE, "emoji": "W", "base_power": 12},
            {"slug": "sustento", "name": "Sustento", "description": "Comida e recursos de sobrevivencia.", "category": AdventureSkill.CATEGORY_SOBREVIVENCIA, "emoji": "S", "base_power": 10},
            {"slug": "agua", "name": "Agua", "description": "Agua, sede e resistencia.", "category": AdventureSkill.CATEGORY_SOBREVIVENCIA, "emoji": "A", "base_power": 10},
            {"slug": "cura", "name": "Cura", "description": "Remedios, ervas e protecao do corpo.", "category": AdventureSkill.CATEGORY_SUPORTE, "emoji": "C", "base_power": 14},
            {"slug": "persuasao", "name": "Persuasion", "description": "Moedas, documentos e autoridade social.", "category": AdventureSkill.CATEGORY_SOCIAL, "emoji": "P", "base_power": 12},
            {"slug": "investigacion", "name": "Investigacion", "description": "Pistas, mapas, cartas e memoria.", "category": AdventureSkill.CATEGORY_INVESTIGACAO, "emoji": "I", "base_power": 12},
        ]
        skills = seed_chapter_skills(chapter, skill_defs)

        def sync_item_skills():
            sync_chapter_item_skills(chapter, skills, skill_defs)

        phase_map: dict[int, AdventurePhase] = {}
        for p in PHASES:
            phase_obj, _ = AdventurePhase.objects.update_or_create(
                chapter=chapter,
                number=p["number"],
                defaults={
                    "title":           p["title"],
                    "narrative_intro": p["narrative_intro"],
                    "narrative_outro": p["narrative_outro"],
                    "key_words":       p["key_words"],
                    "scenario_slug":   p["scenario_slug"],
                    "phrase_count":    p["phrase_count"],
                    "phase_type":      p["phase_type"],
                },
            )
            phase_map[p["number"]] = phase_obj
        self.stdout.write(f"  ✓ Fases: {len(PHASES)}")

        # ── 6. Personagens ────────────────────────────────────────────────────
        char_map: dict[str, AdventureCharacter] = {}
        for slug, name, role, emoji, ctype, lang_bridge, first_phase_num, order, description, quote in CHARACTERS:
            char_obj, _ = AdventureCharacter.objects.update_or_create(
                chapter=chapter,
                slug=slug,
                defaults={
                    "name":           name,
                    "role":           role,
                    "emoji":          emoji,
                    "character_type": ctype,
                    "description":    description,
                    "quote":          quote,
                    "lang_bridge":    lang_bridge,
                    "first_phase":    phase_map[first_phase_num],
                    "order":          order,
                },
            )
            char_map[slug] = char_obj
        self.stdout.write(f"  ✓ Personagens: {len(CHARACTERS)}")

        # ── 7. Itens ──────────────────────────────────────────────────────────
        # Mochila Fase 1 = bolsa de viajante de verdade. Itens cotidianos que
        # mapeiam aos momentos da fase. Cada item reforça vocab (pan, manzana,
        # agua) e ancora um beat narrativo. Sem item lendário/épico aqui — esses
        # ficam pra fases avançadas (boss, marcos emocionais).

        # Remove sombrero antigo se existir (foi substituído pelos itens diários)
        AdventureItem.objects.filter(chapter=chapter, slug="sombrero_viejo").delete()

        PHASE1_ITEMS = [
            {
                "slug": "pan_fresco",
                "emoji": "🍞",
                "name": "Pan Fresco",
                "lore": (
                    "Quente, ainda saindo do forno de barro. Uma senhora de avental "
                    "empoeirado te entregou um pedaço quando você passava pela porta "
                    "de adobe dela. 'Para el camino, forastero.' Ela não pediu nada "
                    "em troca — só sorriu e voltou pra dentro."
                ),
                "source_character_slug": None,
                "word_id": "es_pan",
                "item_tag": AdventureItem.TAG_COMIDA,
                "action":   AdventureItem.ACTION_USAR,
                "order": 1,
            },
            {
                "slug": "manzana_del_campo",
                "emoji": "🍎",
                "name": "Manzana del Campo",
                "lore": (
                    "Don Miguel arrancou esta manzana da árvore atrás da casa dele e "
                    "te passou sem cerimônia. Pequena, vermelha, com gosto de fruta "
                    "de verdade. 'El campesino siempre tiene algo en el bolsillo, ¿eh?'"
                ),
                "source_character_slug": "don_miguel",
                "word_id": "es_manzana",
                "item_tag": AdventureItem.TAG_COMIDA,
                "action":   AdventureItem.ACTION_USAR,
                "order": 2,
            },
            {
                "slug": "agua_del_pozo",
                "emoji": "💧",
                "name": "Agua del Pozo",
                "lore": (
                    "Você bebeu da água do poço da plaza central. Fria, com gosto leve "
                    "de pedra molhada. Don Miguel acenou enquanto você bebia: 'El agua "
                    "de este pozo es buena. Aquí no te enfermarás, forastero.'"
                ),
                "source_character_slug": None,
                "word_id": "es_agua",
                "item_tag": AdventureItem.TAG_BEBIDA,
                "action":   AdventureItem.ACTION_USAR,
                "order": 3,
            },
            {
                "slug": "moneda_de_cobre",
                "emoji": "🪙",
                "name": "Moneda de Cobre",
                "lore": (
                    "Don Miguel te entregou esta moeda velha antes de você seguir caminho. "
                    "'Quédatela. Te trae suerte en este pueblo.' Pequena, manchada de "
                    "verde nas bordas, parece ter passado por muitas mãos antes da sua."
                ),
                "source_character_slug": "don_miguel",
                "word_id": "es_forastero",
                "item_tag": AdventureItem.TAG_MONEDA,
                "action":   AdventureItem.ACTION_ENTREGAR,
                "order": 4,
            },
        ]

        created_count = 0
        for item_data in PHASE1_ITEMS:
            source_char_slug = item_data.get("source_character_slug")
            source_char = char_map.get(source_char_slug) if source_char_slug else None
            _, created = AdventureItem.objects.update_or_create(
                chapter=chapter,
                slug=item_data["slug"],
                defaults={
                    "emoji":            item_data["emoji"],
                    "name":             item_data["name"],
                    "lore":             item_data["lore"],
                    "rarity":           AdventureItem.RARITY_COMUM,
                    "action":           item_data.get("action", AdventureItem.ACTION_EXAMINAR),
                    "word_id":          item_data.get("word_id", ""),
                    "item_tag":         item_data.get("item_tag", ""),
                    "source_phase":     phase_map[1],
                    "source_character": source_char,
                    "order":            item_data["order"],
                },
            )
            if created:
                created_count += 1
        self.stdout.write(f"  ✓ Itens: {len(PHASE1_ITEMS)} (cotidiano) — {created_count} novos")

        # ── 7b. Pool de baús (raro/épico/lendário) — não ligados a source_phase ──
        # Estes itens entram via UserItemQueue: cada usuário tem fila embaralhada,
        # entregue 1 por baú aberto. has_chest=True nas fases F5/F10/F15/F20 abre
        # baús comuns; F25 entrega lendário (boss).
        # Pool grande (~46 itens) >> nº de baús (15). Cada usuário só sorteia
        # uma fração — dois jogadores terminam a T1 com mochilas diferentes.
        CHEST_POOL = [
            # ── COMUNS (~19) — caem pra todo mundo, sem filtro de maestria ───
            {"slug": "navaja_simple",     "emoji": "🔪", "name": "Navaja Simple",     "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_ARMA,    "lore": "Pequena, gasta nas dobradiças. Útil pra cortar pão, descascar fruta — ou abrir uma carta selada."},
            {"slug": "vino_de_la_casa",   "emoji": "🍷", "name": "Vino de la Casa",   "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_BEBIDA,  "lore": "Tinto jovem, ácido. A taverna da plaza serve em copos sem marca."},
            {"slug": "tortilla_envuelta", "emoji": "🌯", "name": "Tortilla Envuelta", "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMIDA,  "lore": "Embrulhada num pano sujo. Fria agora, mas enche."},
            {"slug": "queso_curado",      "emoji": "🧀", "name": "Queso Curado",      "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMIDA,  "lore": "Duro, salgado, com cheiro forte. Carmen guarda numa caixa de madeira. Dura semanas."},
            {"slug": "jarra_de_agua",     "emoji": "🏺", "name": "Jarra de Agua",     "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_BEBIDA,  "lore": "Barro cozido, fresca por dentro. A água do poço de San Cristóbal mantém o gosto de pedra molhada."},
            {"slug": "palo_de_caminar",   "emoji": "🦯", "name": "Palo de Caminar",   "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_ARMA,    "lore": "Galho de oliveira lixado liso pelo uso. Serve pra apoiar o passo — ou pra afastar um cão bravo."},
            {"slug": "pan_de_centeno",    "emoji": "🥖", "name": "Pan de Centeno",    "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMIDA,  "lore": "Pão escuro, denso. Rosa faz só às quartas. Aguenta a viagem melhor que o pão branco."},
            {"slug": "moneda_de_hierro",  "emoji": "🪙", "name": "Moneda de Hierro",  "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_MONEDA,  "lore": "Vale pouco — mas vale. Suficiente pra comprar o silêncio de um guarda jovem."},
            {"slug": "vendas_limpias",    "emoji": "🩹", "name": "Vendas Limpias",    "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_REMEDIO, "lore": "Tiras de linho fervidas. María sempre carrega — feridas no pueblo não esperam."},
            {"slug": "cuerda_gastada",    "emoji": "🪢", "name": "Cuerda Gastada",    "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMUM,   "lore": "Três braças de corda de cânhamo. Desfia nas pontas, mas aguenta o peso de um homem."},
            {"slug": "vela_de_sebo",      "emoji": "🕯️", "name": "Vela de Sebo",      "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMUM,   "lore": "Cheira a gordura queimada. Mas no escuro do pueblo à noite, qualquer luz é luz."},
            {"slug": "cuchara_de_palo",   "emoji": "🥄", "name": "Cuchara de Palo",   "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMUM,   "lore": "Talhada à faca por algum campesino entediado. Funciona."},
            {"slug": "sombrero_de_paja",  "emoji": "👒", "name": "Sombrero de Paja",  "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMUM,   "lore": "Aba larga, palha trançada. O sol de San Cristóbal não perdoa quem anda de cabeça nua."},
            {"slug": "manta_remendada",   "emoji": "🧶", "name": "Manta Remendada",   "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMUM,   "lore": "Lã grossa, três remendos de cores diferentes. As noites do pueblo são frias mais cedo do que se espera."},
            {"slug": "sal_en_papel",      "emoji": "🧂", "name": "Sal en Papel",      "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMIDA,  "lore": "Um punhado de sal dobrado num papel encerado. No pueblo, sal ainda é moeda de troca."},
            {"slug": "higos_secos",       "emoji": "🫐", "name": "Higos Secos",       "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMIDA,  "lore": "Doces, pegajosos, num saquinho de pano. Energia rápida pra quem caminha."},
            {"slug": "aguja_e_hilo",      "emoji": "🧵", "name": "Aguja e Hilo",      "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMUM,   "lore": "Agulha de osso, novelo pequeno. Carmen diria: 'quem sabe costurar nunca anda roto.'"},
            {"slug": "pedernal",          "emoji": "🪨", "name": "Pedernal",          "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMUM,   "lore": "Pedra de fazer fogo. Ironia — você faz fogo de outro jeito agora. Mas guarda mesmo assim."},
            {"slug": "fruta_seca",        "emoji": "🍇", "name": "Fruta Seca",        "rarity": AdventureItem.RARITY_COMUM, "tag": AdventureItem.TAG_COMIDA,  "lore": "Uvas passas e damascos secos misturados. Don Miguel diz que é comida de quem anda longe."},

            # ── RAROS (~15) — word-linked só pra quem domina a palavra ──────
            {"slug": "mapa_rasgado",      "emoji": "🗺️", "name": "Mapa Rasgado",      "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_DOCUMENTO,"lore": "Metade. Mostra caminhos pelo norte do pueblo. A outra metade falta — alguém a guarda."},
            {"slug": "carta_sellada",     "emoji": "✉️", "name": "Carta Sellada",     "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_DOCUMENTO,"lore": "Cera vermelha, símbolo de sol partido. Não tua — mas terminou na sua mão."},
            {"slug": "moneda_de_plata",   "emoji": "🪙", "name": "Moneda de Plata",   "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_MONEDA,  "lore": "Pesada. Imagem gasta — um rosto que ninguém do pueblo reconhece."},
            {"slug": "cuchillo_de_caza",  "emoji": "🗡️", "name": "Cuchillo de Caza",  "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_ARMA,    "lore": "Lâmina longa, cabo de osso. Eduardo forjou anos atrás — passou de mão em mão até a sua."},
            {"slug": "frasco_de_tinta",   "emoji": "🖋️", "name": "Frasco de Tinta",   "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_DOCUMENTO,"lore": "Tinta de nogueira. Quem tem tinta pode escrever — e quem escreve, no pueblo, tem poder."},
            {"slug": "brujula_de_laton",  "emoji": "🧭", "name": "Brújula de Latón",  "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_COMUM,   "lore": "Aponta o norte com teimosia. O norte — pra onde Carmen disse que você tem que ir."},
            {"slug": "lente_de_aumento",  "emoji": "🔍", "name": "Lente de Aumento",  "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_DOCUMENTO,"lore": "Vidro polido com moldura de cobre. Faz palavras pequenas ficarem grandes — útil pra cartas que não querem ser lidas."},
            {"slug": "llave_sin_puerta",  "emoji": "🗝️", "name": "Llave sin Puerta",  "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_COMUM,   "lore": "Ferro velho, dentes intactos. Abre alguma porta — em algum lugar. Você ainda não sabe qual."},
            {"slug": "cantimplora_cuero", "emoji": "🫗", "name": "Cantimplora de Cuero","rarity": AdventureItem.RARITY_RARO, "tag": AdventureItem.TAG_BEBIDA,  "lore": "Couro curtido, rolha de madeira. Mantém a água fresca um dia inteiro de caminhada."},
            {"slug": "dado_de_hueso",     "emoji": "🎲", "name": "Dado de Hueso",     "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_COMUM,   "lore": "Marfim amarelado, pontos gastos. Rodrigo apostaria nele sem pensar. Você ainda não conhece Rodrigo."},
            {"slug": "espuela_de_plata",  "emoji": "🐎", "name": "Espuela de Plata",  "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_COMUM,   "lore": "Só uma — a outra se perdeu. Prata de verdade. Quem usava isso montava bem."},
            {"slug": "pluma_de_halcon",   "emoji": "🪶", "name": "Pluma de Halcón",   "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_DOCUMENTO,"lore": "Pena longa, ponta cortada pra escrever. Halcão não é ave de pueblo — veio de fora, como você."},
            {"slug": "frasco_de_aceite",  "emoji": "🛢️", "name": "Frasco de Aceite",  "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_COMUM,   "lore": "Azeite de oliva puro. Acende lamparinas, frita comida, cura couro. No pueblo, vale ouro líquido."},
            {"slug": "cinturon_de_cuero", "emoji": "🔗", "name": "Cinturón de Cuero", "rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_COMUM,   "lore": "Largo, fivela de bronze. Tem um corte fino por dentro — alguém escondia algo aqui."},
            {"slug": "navaja_del_herrero","emoji": "🔪", "name": "Navaja del Herrero","rarity": AdventureItem.RARITY_RARO,  "tag": AdventureItem.TAG_ARMA,    "lore": "Eduardo fez. Aço dobrado sete vezes. Corta o que a navaja simples não corta."},

            # ── ÉPICOS (~10) — word-linked só pra quem domina a palavra ─────
            {"slug": "hierba_de_maria",   "emoji": "🌿", "name": "Hierba de María",   "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_REMEDIO, "lore": "Folhas amargas que María seca no fundo da casa de hóspedes. Tira febre — talvez tire outras coisas também."},
            {"slug": "anillo_viejo",      "emoji": "💍", "name": "Anillo Viejo",      "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_COMUM,   "lore": "Ouro fino, gravação interna ilegível. Encontrado no chão da casa de Don Miguel sob uma tábua solta."},
            {"slug": "medallon_partido",  "emoji": "🥇", "name": "Medallón Partido",  "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_COMUM,   "lore": "Metade de um medalhão de bronze. O corte não é acidente — alguém partiu de propósito, pra que duas pessoas guardassem cada metade."},
            {"slug": "libro_de_hierbas",  "emoji": "📕", "name": "Libro de Hierbas",  "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_DOCUMENTO,"lore": "Caderno de couro com desenhos de plantas e notas numa letra apertada. A última página foi arrancada."},
            {"slug": "daga_ceremonial",   "emoji": "🗡️", "name": "Daga Ceremonial",   "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_ARMA,    "lore": "Lâmina curva, símbolo do sol partido gravado no cabo. A marca dos Buscadores. Não é arma de matar — é arma de jurar."},
            {"slug": "reloj_de_bolsillo", "emoji": "⏱️", "name": "Reloj de Bolsillo", "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_COMUM,   "lore": "Parou às 3h47. Ninguém sabe de que dia. Mas alguém parou de propósito — relógios não escolhem a hora de morrer."},
            {"slug": "mapa_completo",     "emoji": "🗺️", "name": "Mapa Completo",     "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_DOCUMENTO,"lore": "O mapa inteiro do norte — não a metade rasgada. Mostra um caminho marcado a tinta vermelha até um ponto sem nome."},
            {"slug": "frasco_de_veneno",  "emoji": "☠️", "name": "Frasco de Veneno",  "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_REMEDIO, "lore": "Vidro escuro, rótulo em branco. María sabe o que é. María sabe que você o tem. Nenhum dos dois comenta."},
            {"slug": "espejo_de_mano",    "emoji": "🪞", "name": "Espejo de Mano",    "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_COMUM,   "lore": "Prata fosca, moldura entalhada. Você olha — e por um segundo o rosto não parece o seu. Depois parece de novo."},
            {"slug": "amuleto_de_hueso",  "emoji": "🦴", "name": "Amuleto de Hueso",  "rarity": AdventureItem.RARITY_EPICO, "tag": AdventureItem.TAG_COMUM,   "lore": "Osso polido amarrado num cordão. Os Buscadores davam a quem ia 'longe demais'. Pesa mais do que devia."},

            # ── LENDÁRIOS DE POOL (~2) — só caem em baú alto, e raramente ────
            {"slug": "moneda_de_oro_antiguo","emoji": "🏅", "name": "Moneda de Oro Antiguo","rarity": AdventureItem.RARITY_LENDARIO, "tag": AdventureItem.TAG_MONEDA, "lore": "Ouro puro. A imagem é de um pueblo que não existe mais. No verso, em letra antiga: o mesmo sol partido da carta."},
            {"slug": "llave_maestra",     "emoji": "🗝️", "name": "Llave Maestra",     "rarity": AdventureItem.RARITY_LENDARIO, "tag": AdventureItem.TAG_COMUM,  "lore": "Ferro negro, sem ferrugem apesar dos anos. Os Buscadores diziam que abria 'a última porta'. Ninguém explicava qual."},
        ]
        chest_created = 0
        for item_data in CHEST_POOL:
            _, created = AdventureItem.objects.update_or_create(
                chapter=chapter, slug=item_data["slug"],
                defaults={
                    "emoji":    item_data["emoji"],
                    "name":     item_data["name"],
                    "lore":     item_data["lore"],
                    "rarity":   item_data["rarity"],
                    "action":   AdventureItem.ACTION_EXAMINAR,
                    "word_id":  "",
                    "item_tag": item_data["tag"],
                    # Sem source_phase — só entram via baú
                },
            )
            if created:
                chest_created += 1
        self.stdout.write(f"  ✓ Pool de baú: {len(CHEST_POOL)} itens — {chest_created} novos")

        # ── 7c. Versões degradadas (fallback para palavras com erro crônico) ──
        # Quando o jogador erra a palavra 5x+, sistema entrega versão degradada
        # do item — bônus menor, some quando a palavra finalmente vira bronze.
        DEGRADED = [
            {"slug": "mendrugo_seco",       "emoji": "🥖", "name": "Mendrugo Seco",       "of": "pan_fresco",     "lore": "Pão velho, duro. Versão temporária — sai da mochila quando você dominar 'pan'."},
            {"slug": "agua_estancada",      "emoji": "💧", "name": "Agua Estancada",      "of": "agua_del_pozo",  "lore": "Tirada de uma poça que ficou da chuva. Mata a sede mas não satisfaz."},
            {"slug": "manzana_machucada",   "emoji": "🍎", "name": "Manzana Machucada",   "of": "manzana_del_campo", "lore": "Caiu do pé sozinha. Marrom de um lado. Ainda alimenta."},
        ]
        deg_created = 0
        for d in DEGRADED:
            pleno = AdventureItem.objects.filter(chapter=chapter, slug=d["of"]).first()
            if not pleno:
                continue
            _, created = AdventureItem.objects.update_or_create(
                chapter=chapter, slug=d["slug"],
                defaults={
                    "emoji":       d["emoji"],
                    "name":        d["name"],
                    "lore":        d["lore"],
                    "rarity":      AdventureItem.RARITY_COMUM,
                    "action":      AdventureItem.ACTION_USAR,
                    "word_id":     pleno.word_id,
                    "item_tag":    pleno.item_tag,
                    "is_degraded": True,
                    "degrades_to": pleno,
                },
            )
            if created:
                deg_created += 1
        self.stdout.write(f"  ✓ Versões degradadas: {len(DEGRADED)} — {deg_created} novas")

        # ── 7d. Marcar fases com baú (has_chest=True, chest_tier) ────────────
        # Distribuição densa conforme inventory-system.md:
        #   ~8 comuns (a cada 2-3 fases) · ~4 raros (a cada 5-6) · ~3 épicos
        #   (milestones). Lendários do boss vêm via source_phase, não pool.
        CHEST_PHASES = {
            2:  AdventureItem.RARITY_COMUM,
            3:  AdventureItem.RARITY_COMUM,
            6:  AdventureItem.RARITY_COMUM,
            9:  AdventureItem.RARITY_COMUM,
            11: AdventureItem.RARITY_COMUM,
            13: AdventureItem.RARITY_COMUM,
            17: AdventureItem.RARITY_COMUM,
            22: AdventureItem.RARITY_COMUM,
            7:  AdventureItem.RARITY_RARO,
            12: AdventureItem.RARITY_RARO,
            16: AdventureItem.RARITY_RARO,
            20: AdventureItem.RARITY_RARO,
            8:  AdventureItem.RARITY_EPICO,   # milestone — María entra
            14: AdventureItem.RARITY_EPICO,   # milestone — 3ª revisão
            19: AdventureItem.RARITY_EPICO,   # milestone — 4ª revisão, carta
        }
        chest_phases_marked = 0
        for phase_num, tier in CHEST_PHASES.items():
            phase = phase_map.get(phase_num)
            if not phase:
                continue
            phase.has_chest = True
            phase.chest_tier = tier
            phase.save(update_fields=["has_chest", "chest_tier"])
            chest_phases_marked += 1
        self.stdout.write(f"  ✓ Fases com baú: {chest_phases_marked} marcadas")

        # ── 7e. Recompensa de boss F25 (lendário — entregue via source_phase) ─
        if 25 in phase_map:
            boss_phase = phase_map[25]
            BOSS_REWARDS = [
                {
                    "slug": "sello_del_pueblo",
                    "emoji": "🛡️",
                    "name": "Sello del Pueblo",
                    "lore": (
                        "Impresso em cera vermelha no papel do seu pase. Carmen "
                        "fez o Alcalde recuar com três frases. Você ganhou o "
                        "direito de ficar em San Cristóbal — sem prazo, sem "
                        "condição. Provou ao pueblo que sobreviveu às regras dele."
                    ),
                    "rarity":   AdventureItem.RARITY_LENDARIO,
                    "action":   AdventureItem.ACTION_EXAMINAR,
                    "item_tag": AdventureItem.TAG_DOCUMENTO,
                    "word_id":  "es_sello",
                    "order":    25,
                },
                {
                    "slug": "carta_fragmento_2",
                    "emoji": "📜",
                    "name": "Fragmento 2 de la Carta",
                    "lore": (
                        "Depois do juicio, a segunda palavra da carta de Valentina "
                        "ficou legível: *'Hermano.'*\n\n"
                        "Você sabe que tem um irmão mais velho. Não sabe onde. "
                        "Não sabe se está vivo. Mas agora — a palavra existe."
                    ),
                    "rarity":   AdventureItem.RARITY_LENDARIO,
                    "action":   AdventureItem.ACTION_EXAMINAR,
                    "item_tag": AdventureItem.TAG_DOCUMENTO,
                    "word_id":  "es_hermano",
                    "order":    26,
                },
            ]
            for item_data in BOSS_REWARDS:
                AdventureItem.objects.update_or_create(
                    chapter=chapter, slug=item_data["slug"],
                    defaults={
                        "emoji":            item_data["emoji"],
                        "name":             item_data["name"],
                        "lore":             item_data["lore"],
                        "rarity":           item_data["rarity"],
                        "action":           item_data["action"],
                        "word_id":          item_data["word_id"],
                        "item_tag":         item_data["item_tag"],
                        "source_phase":     boss_phase,
                        "order":            item_data["order"],
                    },
                )
            self.stdout.write(f"  ✓ Recompensa boss F25: {len(BOSS_REWARDS)} itens lendários")

        # ─────────────────────────────────────────────────────────────────────
        sync_item_skills()

        self.stdout.write(self.style.SUCCESS(
            "\n✅ Seed ES A1 T1 completo!\n"
            f"   {len(PHASES)} fases · {len(CHARACTERS)} personagens · {len(PHRASES)} frases\n"
        ))
