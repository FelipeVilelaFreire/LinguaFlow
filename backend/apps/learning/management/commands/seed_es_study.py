from django.core.management.base import BaseCommand

from apps.adventure.seeds.es.chapter import PHASES
from apps.learning.models import Language, Lesson, Phrase, Scenario, StudyDay, StudyModule

LEGACY_STUDY_SCENARIO_SLUGS = [
    "es-saudacoes",
    "es-natureza",
    "es-emocoes",
    "es-pessoas",
    "es-tempo",
]

LEGACY_STUDY_MODULE_TITLES = [
    "O Mundo Natural",
    "Dentro de Você",
    "Pessoas e Tempo",
    "Pueblo e Mercado",
    "Mistério e Decisão",
]

MODULES = [
    {
        "lang_code": "ES",
        "title": "Primeiros Passos",
        "order": 1,
        "scenarios": [
            {
                "slug": "es-social",
                "title": "Social",
                "description": "Saudações, apresentações, família e convívio no pueblo.",
                "adventure_phase": 1,
                "order": 1,
                "phrases": [
                    ("Olá", "Hola"),
                    ("Bom dia", "Buenos días"),
                    ("Boa tarde", "Buenas tardes"),
                    ("Boa noite", "Buenas noches"),
                    ("Qual é o seu nome?", "¿Cómo te llamas?"),
                    ("Meu nome é...", "Me llamo..."),
                    ("Por favor", "Por favor"),
                    ("Obrigado", "Gracias"),
                    ("Até logo", "Hasta luego"),
                    ("Tchau", "Adiós"),
                    ("Prazer", "Mucho gusto"),
                    ("Sente-se", "Siéntate"),
                    ("Meu irmão", "Mi hermano"),
                    ("Minha irmã", "Mi hermana"),
                    ("O povo", "El pueblo"),
                ],
            },
            {
                "slug": "es-comida",
                "title": "Comida e bebida",
                "description": "Alimentos, bebidas e situações à mesa.",
                "adventure_phase": 2,
                "order": 2,
                "phrases": [
                    ("O pão", "El pan"),
                    ("A água", "El agua"),
                    ("A maçã", "La manzana"),
                    ("O vinho", "El vino"),
                    ("O leite", "La leche"),
                    ("Estou com fome", "Tengo hambre"),
                    ("Estou com sede", "Tengo sed"),
                    ("Tem algo para comer?", "¿Tiene algo de comer?"),
                    ("Quero comer", "Quiero comer"),
                    ("A comida está boa", "La comida está buena"),
                    ("Um pouco mais", "Un poco más"),
                    ("Mais nada, obrigado", "Nada más, gracias"),
                    ("Quanto custa?", "¿Cuánto cuesta?"),
                    ("É muito caro", "Es muy caro"),
                    ("A conta, por favor", "La cuenta, por favor"),
                ],
            },
        ],
    },
    {
        "lang_code": "ES",
        "title": "Orientação e Mercado",
        "order": 2,
        "scenarios": [
            {
                "slug": "es-lugares",
                "title": "Lugares",
                "description": "Orientação, direções, pontos do pueblo e caminho pelo campo.",
                "adventure_phase": 3,
                "order": 3,
                "phrases": [
                    ("O caminho", "El camino"),
                    ("A praça", "La plaza"),
                    ("A pousada", "La posada"),
                    ("A igreja", "La iglesia"),
                    ("A porta", "La puerta"),
                    ("O poço", "El pozo"),
                    ("Onde fica?", "¿Dónde está?"),
                    ("Por aqui", "Por aquí"),
                    ("À esquerda", "A la izquierda"),
                    ("À direita", "A la derecha"),
                    ("Em frente", "Enfrente"),
                    ("Aqui", "Aquí"),
                    ("Ali", "Allá"),
                    ("Perto", "Cerca"),
                    ("Longe", "Lejos"),
                ],
            },
            {
                "slug": "es-mercado",
                "title": "Mercado e números",
                "description": "Comprar, vender e os primeiros números.",
                "adventure_phase": 4,
                "order": 4,
                "phrases": [
                    ("Um", "Uno"),
                    ("Dois", "Dos"),
                    ("Três", "Tres"),
                    ("Quatro", "Cuatro"),
                    ("Cinco", "Cinco"),
                    ("Muito", "Mucho"),
                    ("Pouco", "Poco"),
                    ("O preço", "El precio"),
                    ("A moeda", "La moneda"),
                    ("O mercado", "El mercado"),
                    ("Comprar", "Comprar"),
                    ("Vender", "Vender"),
                    ("Caro", "Caro"),
                    ("Barato", "Barato"),
                    ("O troco", "El cambio"),
                ],
            },
        ],
    },
    {
        "lang_code": "ES",
        "title": "Cuidado e Ofícios",
        "order": 3,
        "scenarios": [
            {
                "slug": "es-salud",
                "title": "Salud",
                "description": "Saúde, corpo, sintomas e cuidado pessoal.",
                "adventure_phase": 8,
                "order": 5,
                "phrases": [
                    ("Estou doente", "Estoy enfermo"),
                    ("Dói aqui", "Me duele aquí"),
                    ("A cabeça", "La cabeza"),
                    ("A mão", "La mano"),
                    ("As mãos", "Las manos"),
                    ("A febre", "La fiebre"),
                    ("O remédio", "La medicina"),
                    ("A erva", "La hierba"),
                    ("A curandeira", "La curandera"),
                    ("Estou melhor", "Estoy mejor"),
                    ("Descanse", "Descanse"),
                    ("Estou cansado", "Estoy cansado"),
                    ("Respire", "Respire"),
                    ("Beba água", "Beba agua"),
                    ("Preciso de ajuda", "Necesito ayuda"),
                ],
            },
            {
                "slug": "es-trabalho",
                "title": "Trabajo",
                "description": "Ofícios, rotina, esforço e tarefas do pueblo.",
                "adventure_phase": 7,
                "order": 6,
                "phrases": [
                    ("O trabalho", "El trabajo"),
                    ("Trabalho muito", "Trabajo mucho"),
                    ("O ferreiro", "El herrero"),
                    ("A padeira", "La panadera"),
                    ("O cozinheiro", "El cocinero"),
                    ("A sentinela", "El vigilante"),
                    ("O fazendeiro", "El campesino"),
                    ("O ferro", "El hierro"),
                    ("A ferramenta", "La herramienta"),
                    ("A rotina", "La rutina"),
                    ("De onde você vem?", "¿De dónde vienes?"),
                    ("Venho de longe", "Vengo de lejos"),
                    ("Eu vou trabalhar", "Voy a trabajar"),
                    ("Vamos ao mercado", "Vamos al mercado"),
                    ("Preciso ir", "Necesito irme"),
                ],
            },
        ],
    },
    {
        "lang_code": "ES",
        "title": "Memória e Segredos",
        "order": 4,
        "scenarios": [
            {
                "slug": "es-historia",
                "title": "Historia",
                "description": "Memória, passado, segredos e revelações.",
                "adventure_phase": 6,
                "order": 7,
                "phrases": [
                    ("Não me lembro", "No recuerdo"),
                    ("Eu me lembro", "Recuerdo"),
                    ("Meu passado", "Mi pasado"),
                    ("Esqueci", "Olvidé"),
                    ("É verdade", "Es verdad"),
                    ("É mentira", "Es mentira"),
                    ("O segredo", "El secreto"),
                    ("O perigo", "El peligro"),
                    ("Cuidado", "Cuidado"),
                    ("Eu conheço", "Conozco"),
                    ("A carta", "La carta"),
                    ("A palavra", "La palabra"),
                    ("Ler", "Leer"),
                    ("O futuro", "El futuro"),
                    ("Pertence a você", "Te pertenece"),
                ],
            },
        ],
    },
    {
        "lang_code": "ES",
        "title": "Julgamento e Desafio",
        "order": 5,
        "scenarios": [
            {
                "slug": "es-desafio",
                "title": "Desafío",
                "description": "Provas, conflito, autoridade e decisões sob pressão.",
                "adventure_phase": 5,
                "order": 8,
                "phrases": [
                    ("O medo", "El miedo"),
                    ("O fogo", "El fuego"),
                    ("Corra", "Corre"),
                    ("Pare", "Para"),
                    ("Venha", "Ven"),
                    ("Olhe", "Mira"),
                    ("A prova", "La prueba"),
                    ("Mostrar", "Demostrar"),
                    ("O respeito", "El respeto"),
                    ("A honra", "El honor"),
                    ("O julgamento", "El juicio"),
                    ("A autoridade", "La autoridad"),
                    ("O passe", "El pase"),
                    ("O prefeito", "El alcalde"),
                    ("Bem-vindo", "Bienvenido"),
                ],
            },
        ],
    },
]

STUDY_CATEGORY_BY_SCENARIO = {
    scenario["slug"]: scenario["title"]
    for module in MODULES
    for scenario in module["scenarios"]
}

PHASE_STUDY_CONTENT = {
    1: {
        "objective": "Cumprimentar, dizer seu nome e responder em espanhol simples.",
        "explanation": "Esta aula transforma a chegada ao campo em linguagem de sobrevivência social. Foque em reconhecer saudações, usar me llamo para se apresentar e responder com frases curtas sem tentar montar estruturas longas demais.",
        "exercise_notes": ["Leia a frase em espanhol antes de revelar a tradução.", "Escreva a resposta de memória usando a pontuação espanhola quando aparecer.", "No final, tente dizer em voz alta: Hola, me llamo..."],
    },
    2: {
        "objective": "Pedir comida e bebida usando fome, sede e cortesia básica.",
        "explanation": "A aventura apresenta pão, água e a rotina da manhã. No estudo, isso vira prática de pedidos: substantivos com artigo, necessidades com tengo e frases educadas para comprar ou pedir algo à mesa.",
        "exercise_notes": ["Separe mentalmente artigo e substantivo: el pan, el agua.", "Use tengo para necessidades: tengo hambre, tengo sed.", "Nos exercícios reversos, escreva a frase inteira, não só a palavra principal."],
    },
    3: {
        "objective": "Localizar lugares e entender direções básicas no pueblo.",
        "explanation": "O caminho de terra introduz orientação espacial. A aula treina onde fica, aqui, ali, perto, longe e direções, para que a exploração da aventura tenha vocabulário utilizável fora da narrativa.",
        "exercise_notes": ["Associe izquierda/derecha com esquerda/direita antes de responder.", "Pratique ¿Dónde está? como bloco fixo.", "Monte frases curtas com lugar + direção: la plaza, a la derecha."],
    },
    4: {
        "objective": "Contar, perguntar preço e entender compras simples.",
        "explanation": "No mercado, números e negociação aparecem juntos. O foco é reconhecer quantidades pequenas, preço, moeda, caro/barato e ações de compra sem sair do nível A1.",
        "exercise_notes": ["Revise números de uno a cinco antes das escolhas.", "Compare caro e barato em voz alta.", "Quando a pergunta tiver quanto custa, responda com a forma completa ¿Cuánto cuesta?."],
    },
    5: {
        "objective": "Reagir a perigo com comandos curtos e vocabulário emocional.",
        "explanation": "A primeira tensão da história pede linguagem rápida: medo, fogo, correr, parar, olhar. A prática usa frases imperativas e palavras de reação para criar reflexo em situações urgentes.",
        "exercise_notes": ["Trate ven, mira, corre e para como comandos prontos.", "Não traduza palavra por palavra quando a frase for um comando.", "Repita fuego e miedo em voz alta para fixar pronúncia."],
    },
    6: {
        "objective": "Falar de memória, luz e descoberta com frases simples.",
        "explanation": "Sofía entra na história e o mistério começa a ganhar nome. A aula usa vocabulário de história para treinar lembrar, esquecer, conhecer e reconhecer sinais importantes.",
        "exercise_notes": ["Compare recuerdo com no recuerdo.", "Use conozco para 'eu conheço'.", "Nas lacunas, observe se a resposta pede verbo ou substantivo."],
    },
    7: {
        "objective": "Falar do dia normal, vizinhos e rotina social.",
        "explanation": "Depois do evento estranho, o estudo volta ao cotidiano. A aula reforça convívio, pessoas do pueblo e frases úteis para uma conversa curta de rotina.",
        "exercise_notes": ["Revise hoy, me llamo e pueblo como palavras de base.", "Use frases curtas antes de tentar variações.", "Na tradução reversa, preserve mi/tu quando aparecer."],
    },
    8: {
        "objective": "Descrever sintomas e pedir cuidado básico.",
        "explanation": "A curandeira traz o campo de saúde. Você pratica cabeça, mãos, febre, remédio e pedidos de ajuda, com foco em frases de necessidade e estado físico.",
        "exercise_notes": ["Memorize me duele aquí como bloco.", "Associe la cabeza e la mano com partes do corpo.", "Nos exercícios de escrita, atenção a estoy enfermo e estoy mejor."],
    },
    9: {
        "objective": "Falar sobre comida em grupo e preferências simples.",
        "explanation": "A mesa com quatro pessoas amplia o vocabulário de comida. O estudo reforça pedidos e preferências para transformar itens de aventura em frases utilizáveis.",
        "exercise_notes": ["Compare tengo hambre com quiero comer.", "Use me gusta/no me gusta em voz alta se aparecer na revisão.", "Pratique substantivos com artigo: la comida, el café."],
    },
    10: {
        "objective": "Entender autoridade, passe e comandos diretos.",
        "explanation": "El Vigilante muda o tom da história. A aula trabalha vocabulário de controle e movimento: passe, alcalde, venha, pare, olhe, além de frases curtas de pressão.",
        "exercise_notes": ["Responda comandos como frases completas quando o exercício pedir.", "Conecte el pase e el alcalde ao contexto da aventura.", "Revise ven, mira e para antes da ditado."],
    },
    11: {
        "objective": "Usar futuro imediato com voy a e vamos a.",
        "explanation": "No ayuntamiento, a aventura começa a exigir plano e autorização. O estudo introduz o futuro imediato de forma prática: vou fazer, vamos fazer, preciso ir.",
        "exercise_notes": ["Leia voy a como 'vou'.", "Leia vamos a como 'vamos'.", "Monte respostas com sujeito + voy/vamos + a + ação."],
    },
    12: {
        "objective": "Contar o que viu, ouviu e lembrou.",
        "explanation": "Três dias colocam o passado simples na superfície, mas o estudo mantém o nível controlado. Você pratica ontem, vi, ouvi, falei e lembro como blocos úteis.",
        "exercise_notes": ["Use ayer para ancorar passado.", "Compare vi, oí e hablé pelo sentido.", "Na revisão, aceite a frase como bloco antes de analisar gramática."],
    },
    13: {
        "objective": "Nomear família e usar possessivos básicos.",
        "explanation": "A família de Miguel conecta vínculo e identidade. A aula foca madre, padre, hermano, hermana e possessivos mi, tu, su para falar de relações.",
        "exercise_notes": ["Associe mi com meu/minha, tu com teu/tua, su com dele/dela.", "Pratique el hermano e la hermana com artigo.", "Monte frases curtas: mi madre, tu padre."],
    },
    14: {
        "objective": "Revisar artigos e vocabulário de memória.",
        "explanation": "A cena da janta funciona como revisão. O estudo reforça el, la, los, las e palavras de história para melhorar precisão antes das fases mais longas.",
        "exercise_notes": ["Antes de responder, identifique se a palavra é singular ou plural.", "Observe se o artigo é masculino ou feminino.", "Use a revisão para corrigir confusões antigas."],
    },
    15: {
        "objective": "Descrever pessoas com adjetivos simples.",
        "explanation": "O primeiro testemunho exige descrição. Você pratica alto, baixo, jovem, velho e outros traços básicos para reconhecer personagens e falar deles.",
        "exercise_notes": ["Leia o adjetivo junto com a pessoa descrita.", "Compare alto/bajo e joven/viejo.", "Na escrita, mantenha a ordem espanhola que o exercício mostra."],
    },
    16: {
        "objective": "Falar de desejo, amor e decisões pessoais.",
        "explanation": "Carmen adiciona passado emocional à história. O estudo trabalha querer, antes, amor, noivo e casar, sempre com frases simples e úteis.",
        "exercise_notes": ["Use quiero como bloco para 'eu quero'.", "Não confunda antes com después.", "Responda com a frase inteira quando houver verbo."],
    },
    17: {
        "objective": "Falar de marca, corpo e pertencimento familiar.",
        "explanation": "Eduardo traz pistas físicas e familiares. A aula conecta corpo, marca e família com advérbios úteis como ya e todavía.",
        "exercise_notes": ["Compare ya com 'já' e todavía com 'ainda'.", "Revise familia, hermano e espalda.", "Observe se o exercício pede palavra isolada ou frase."],
    },
    18: {
        "objective": "Expressar verdade, mentira e confiança.",
        "explanation": "Quando Don Miguel descobre mais, a linguagem fica moral: verdade, mentir, confiar, posso, podemos. O foco é dizer posição com frases curtas.",
        "exercise_notes": ["Compare puedo e podemos.", "Pratique es verdad e es mentira como blocos.", "Use confiar como palavra-chave de sentido, não só tradução."],
    },
    19: {
        "objective": "Ler pistas escritas e revisar vocabulário de história.",
        "explanation": "A carta junta memória, leitura e mistério. O estudo reforça carta, palavra, ler e voltar, preparando o usuário para entender pistas narrativas.",
        "exercise_notes": ["Leia la carta e la palabra com artigo.", "Revise leer como ação principal.", "Nos exercícios de ordem, monte a frase antes de clicar em verificar."],
    },
    20: {
        "objective": "Falar de visita, chegada e obrigação.",
        "explanation": "A visita inesperada puxa estruturas de necessidade. Você pratica llegar, esperar, tengo que e hay que para falar do que precisa acontecer.",
        "exercise_notes": ["Compare tengo que com hay que.", "Use llegar para chegada e esperar para espera.", "Na tradução, mantenha que quando fizer parte da expressão."],
    },
    21: {
        "objective": "Perguntar quando alguém soube ou disse a verdade.",
        "explanation": "O confronto com María usa perguntas e verbos de informação. A aula treina quando, saber, dizer e verdade em frases diretas.",
        "exercise_notes": ["Use cuándo para perguntas de tempo.", "Compare saber e decir pelo sentido.", "Responda sem acrescentar palavras que não estão no exercício."],
    },
    22: {
        "objective": "Falar sobre contar, guardar e pertencer.",
        "explanation": "A verdade parcial exige linguagem de segredo. O estudo trabalha contar, guardar, nome e pertencer, mantendo o foco em frases curtas com valor narrativo.",
        "exercise_notes": ["Associe guardar com manter/proteger informação.", "Leia te pertenece como bloco.", "Revise nombre quando aparecer em frases de identidade."],
    },
    23: {
        "objective": "Entender plano, ordem e acompanhamento.",
        "explanation": "O plano do alcalde leva o vocabulário para autoridade formal. Você pratica si, orden, uniforme e acompañar como base para entender imposição e condição.",
        "exercise_notes": ["Não confunda si com sí: contexto decide.", "Use orden como substantivo de autoridade.", "Pratique acompañar como ação de seguir junto."],
    },
    24: {
        "objective": "Preparar vocabulário de julgamento e risco.",
        "explanation": "A véspera do juicio reúne cárcel, soborno, guarda e julgamento. A aula prepara o usuário para a fase final com palavras de conflito institucional.",
        "exercise_notes": ["Revise juicio antes de começar.", "Associe cárcel com prisão e guarda com autoridade.", "Nas lacunas, confira acentos antes de avançar."],
    },
    25: {
        "objective": "Consolidar a temporada com julgamento, selo e família.",
        "explanation": "A fase final fecha o primeiro arco. O estudo mistura desafio e história para revisar juicio, vergüenza, sello e hermano, conectando vitória narrativa com domínio linguístico.",
        "exercise_notes": ["Trate esta aula como revisão de boss: vá mais devagar.", "Use as traduções reveladas para corrigir escrita.", "Depois de terminar, refaça mentalmente as palavras-chave da temporada."],
    },
}


class Command(BaseCommand):
    help = "Seed study modules, scenarios and phrases for ES A1"

    def handle(self, *args, **options):
        try:
            pt = Language.objects.get(code="PT")
            es = Language.objects.get(code="ES")
        except Language.DoesNotExist as exc:
            self.stderr.write(f"Language not found: {exc}. Run seed_languages first.")
            return

        total_phrases = 0

        for mod_data in MODULES:
            mod_dupes = StudyModule.objects.filter(
                lang_code=mod_data["lang_code"],
                title=mod_data["title"],
            )
            if mod_dupes.count() > 1:
                mod_dupes.exclude(pk=mod_dupes.first().pk).delete()
            module, created = StudyModule.objects.update_or_create(
                lang_code=mod_data["lang_code"],
                title=mod_data["title"],
                defaults={"order": mod_data["order"]},
            )
            action = "created" if created else "updated"
            self.stdout.write(f"  Module {action}: {module}")

            for sc_data in mod_data["scenarios"]:
                scenario, _ = Scenario.objects.update_or_create(
                    slug=sc_data["slug"],
                    defaults={
                        "title":           sc_data["title"],
                        "description":     sc_data["description"],
                        "module":          module,
                        "adventure_phase": sc_data["adventure_phase"],
                        "order":           sc_data["order"],
                    },
                )
                self.stdout.write(f"    Scenario: {scenario.title}")

                for source_text, target_text in sc_data["phrases"]:
                    dupes = Phrase.objects.filter(
                        source_language=pt,
                        target_language=es,
                        source_text=source_text,
                    )
                    if dupes.count() > 1:
                        dupes.exclude(pk=dupes.first().pk).delete()
                    Phrase.objects.update_or_create(
                        source_language=pt,
                        target_language=es,
                        source_text=source_text,
                        defaults={
                            "target_text": target_text,
                            "difficulty":  "A1",
                            "scenario":    scenario,
                            "category":    sc_data["title"],
                        },
                    )
                    total_phrases += 1

        stale_deleted, _ = Scenario.objects.filter(slug__in=LEGACY_STUDY_SCENARIO_SLUGS).delete()
        if stale_deleted:
            self.stdout.write(f"  Removed legacy study scenarios: {stale_deleted}")

        stale_modules_deleted, _ = StudyModule.objects.filter(
            lang_code="ES",
            title__in=LEGACY_STUDY_MODULE_TITLES,
        ).delete()
        if stale_modules_deleted:
            self.stdout.write(f"  Removed legacy study modules: {stale_modules_deleted}")

        canonical_titles = []
        fallback_phrases = list(
            Phrase.objects.filter(
                source_language=pt,
                target_language=es,
                difficulty="A1",
            )
            .select_related("scenario")
            .order_by("id")[:12]
        )

        StudyDay.objects.filter(
            is_active=True,
            lesson__phrases__source_language=pt,
            lesson__phrases__target_language=es,
            lesson__phrases__difficulty="A1",
        ).exclude(lesson__title__startswith="ES A1 T1 Dia ").update(is_active=False)

        created_days = 0
        for phase in PHASES:
            day_number = phase["number"]
            title = f"ES A1 T1 Dia {day_number:02d}: {phase['title']}"
            canonical_titles.append(title)
            lesson_content = PHASE_STUDY_CONTENT[day_number]
            scenario = Scenario.objects.get(slug=phase["scenario_slug"])
            study_category = STUDY_CATEGORY_BY_SCENARIO.get(phase["scenario_slug"])
            phase_phrases = list(
                Phrase.objects.filter(
                    source_language=pt,
                    target_language=es,
                    difficulty="A1",
                    scenario=scenario,
                    category=study_category,
                ).order_by("id")[:12]
            )
            if len(phase_phrases) < 8:
                seen = {phrase.id for phrase in phase_phrases}
                scenario_fallback = list(
                    Phrase.objects.filter(
                        source_language=pt,
                        target_language=es,
                        difficulty="A1",
                        scenario=scenario,
                    ).exclude(id__in=seen).order_by("id")[:12]
                )
                phase_phrases.extend(scenario_fallback)
                seen = {phrase.id for phrase in phase_phrases}
                phase_phrases.extend([phrase for phrase in fallback_phrases if phrase.id not in seen])
            phase_phrases = phase_phrases[:12]

            duplicates = Lesson.objects.filter(title=title).order_by("id")
            if duplicates.count() > 1:
                duplicates.exclude(pk=duplicates.first().pk).delete()

            lesson, _ = Lesson.objects.update_or_create(
                title=title,
                defaults={
                    "day_number": day_number,
                    "scenario": scenario,
                    "objective": lesson_content["objective"],
                    "explanation": lesson_content["explanation"],
                    "exercise_notes": lesson_content["exercise_notes"],
                    "video_title": f"ES A1 T1 - {phase['title']}",
                    "video_url": "",
                    "video_duration": "10 min",
                },
            )
            lesson.phrases.set(phase_phrases)

            day_dupes = StudyDay.objects.filter(day_number=day_number, lesson=lesson).order_by("id")
            if day_dupes.count() > 1:
                day_dupes.exclude(pk=day_dupes.first().pk).delete()

            _, created = StudyDay.objects.update_or_create(
                day_number=day_number,
                lesson=lesson,
                defaults={"is_active": True},
            )
            created_days += 1 if created else 0

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {len(MODULES)} modules, 8 scenarios, {total_phrases} phrases, "
            f"25 canonical study days seeded for ES A1 T1 ({created_days} new)."
        ))
