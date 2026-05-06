from django.core.management.base import BaseCommand

from apps.adventure.models import AdventureChapter, AdventurePhase
from apps.learning.models import Language


PHASES_DE_A1 = [
    {
        "number": 1,
        "title": "O Despertar",
        "narrative_intro": (
            "Você abre os olhos. A floresta está escura e o cheiro de fumaça paira no ar. "
            "Sua cabeça dói e você não se lembra de nada — nem do seu nome. "
            "Uma luz fraca vem de longe: uma aldeia. Você se arrasta até lá com dificuldade. "
            "Na entrada, um ancião de cabelos brancos te olha com desconfiança. "
            "Ele fala algo que você não entende. "
            "Você está com fome e com sede. Para sobreviver esta noite, "
            "precisa aprender as primeiras palavras desta língua estranha."
        ),
        "narrative_outro": (
            "O ancião te deu água e um pedaço de pão duro. "
            "Ele ainda desconfia, mas te deixou entrar e dormir perto da fogueira. "
            "Você aprendeu as primeiras palavras desta língua. "
            "Ainda há muito pela frente — mas a jornada começou."
        ),
        "key_words": [
            "Wasser — água",
            "Brot — pão",
            "Bitte — por favor",
            "Danke — obrigado",
        ],
        "scenario_slug": "restaurant",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 2,
        "title": "A Aldeia",
        "narrative_intro": (
            "De manhã cedo, você explora a aldeia. As ruelas são estreitas, cheias de gente ocupada. "
            "Um menino curioso te puxa pela manga e aponta para diferentes lugares: "
            "a taverna, o poço, o celeiro, o portão norte. "
            "Você percebe que para se mover com segurança, precisa aprender a se orientar "
            "e a perguntar o caminho nesta língua que ainda soa estranha."
        ),
        "narrative_outro": (
            "Agora você consegue se mover pela aldeia sem se perder. "
            "Algumas pessoas já acenam quando te veem passar. "
            "Você é um forasteiro — mas um forasteiro que está tentando. "
            "Isso conta muito aqui."
        ),
        "key_words": [
            "Wo ist — onde fica",
            "Hier — aqui",
            "Links — esquerda",
            "Rechts — direita",
        ],
        "scenario_slug": "transport",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 3,
        "title": "Primeiro Aliado",
        "narrative_intro": (
            "No fim da rua principal, uma forja brilha com fogo intenso. "
            "Um ferreiro enorme bate em metal incandescente com golpes precisos. "
            "Ele é o único na aldeia que não te olha com medo — apenas curiosidade. "
            "Se você conseguir conversar com ele, talvez encontre seu primeiro aliado verdadeiro. "
            "Mas primeiro precisa aprender a se apresentar e a falar com as pessoas."
        ),
        "narrative_outro": (
            "O ferreiro gargalhou quando você errou as palavras — um riso honesto, sem crueldade. "
            "No final, ele apertou sua mão com força. "
            "'Kael', você disse, inventando um nome. 'Bjorn', ele respondeu. "
            "Você tem um aliado. E, pela primeira vez desde que acordou, não está sozinho."
        ),
        "key_words": [
            "Ich bin — eu sou",
            "Mein Name — meu nome",
            "Freund — amigo",
            "Helfen — ajudar",
        ],
        "scenario_slug": "social",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 4,
        "title": "Sombra no Horizonte",
        "narrative_intro": (
            "Mercadores chegam à aldeia com notícias ruins: um clã inimigo avança pelo norte, "
            "queimando tudo pelo caminho. A aldeia precisa se abastecer rápido. "
            "Bjorn te leva ao mercado e diz: 'Você fala melhor com estranhos do que eu. Negocie.' "
            "Para garantir a sobrevivência da aldeia, precisa aprender a comprar, vender e barganhar."
        ),
        "narrative_outro": (
            "Você conseguiu os suprimentos por um preço justo. "
            "Os vendedores do mercado já te reconhecem pelo nome. "
            "Bjorn olhou surpreso: 'Você aprende rápido.' "
            "Você entendeu cada palavra. Algo estava mudando."
        ),
        "key_words": [
            "Kaufen — comprar",
            "Wie viel kostet — quanto custa",
            "Ich brauche — eu preciso",
            "Das ist alles — é tudo",
        ],
        "scenario_slug": "market",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 5,
        "title": "O Conselho",
        "narrative_intro": (
            "Os anciãos da aldeia se reúnem em conselho de guerra. "
            "Bjorn insistiu para que você participasse — ele acredita que você tem informações "
            "sobre o clã inimigo, mesmo que não se lembre de nada. "
            "No conselho, todos falam rápido e com seriedade. "
            "Você precisa entender os argumentos e se fazer entender. "
            "Esta é sua chance de provar que merece estar aqui."
        ),
        "narrative_outro": (
            "O conselho ouviu você. Não confiaram totalmente — ninguém confia num estranho de cara. "
            "Mas um dos anciãos se levantou e disse: 'Este forasteiro fala nossa língua. "
            "Isso significa que ele escolheu ficar.' "
            "Você estava começando a pertencer."
        ),
        "key_words": [
            "Verstehen — entender",
            "Wichtig — importante",
            "Zusammen — juntos",
            "Ich habe eine Frage — tenho uma pergunta",
        ],
        "scenario_slug": "work",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 6,
        "title": "A Cura",
        "narrative_intro": (
            "Um guerreiro voltou da patrulha gravemente ferido — uma flecha no ombro e febre alta. "
            "Sigrid, a curandeira da aldeia, precisa saber exatamente o que ele sente "
            "para preparar o remédio certo. O guerreiro mal consegue falar. "
            "Você é chamado para ajudar a comunicar. "
            "Aprender a falar sobre dor, sintomas e cuidado pode salvar uma vida esta noite."
        ),
        "narrative_outro": (
            "O guerreiro sobreviveu. A febre baixou ao amanhecer. "
            "Sigrid te olhou com respeito: 'Você tem o dom das palavras, forasteiro.' "
            "Na aldeia, a notícia se espalhou rapidamente. "
            "Kael não era mais apenas o estranho — era o que fala com todos."
        ),
        "key_words": [
            "Schmerz — dor",
            "Hilfe — socorro / ajuda",
            "Ich fühle mich nicht gut — não me sinto bem",
            "Besser — melhor",
        ],
        "scenario_slug": "health",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 7,
        "title": "A Marcha",
        "narrative_intro": (
            "A aldeia decidiu ir ao encontro do inimigo antes que ele chegue. "
            "A marcha começa ao amanhecer, com guerreiros, suprimentos e famílias inteiras. "
            "Pelo caminho, você precisa comunicar rotas, distâncias e alertas de perigo. "
            "Os guerreiros confiam em você para guiar a comunicação. "
            "Cada palavra errada pode custar vidas — e cada palavra certa pode salvar."
        ),
        "narrative_outro": (
            "A tropa chegou ao ponto de encontro sem baixas. "
            "Os guerreiros te batem nas costas com força. 'Kael conhece o caminho', dizem. "
            "Você não se lembra do seu passado — "
            "mas estava construindo algo novo aqui, palavra por palavra."
        ),
        "key_words": [
            "Der Weg — o caminho",
            "Weit — longe",
            "Schnell — rápido",
            "Gefahr — perigo",
        ],
        "scenario_slug": "travel",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 8,
        "title": "Na Forja",
        "narrative_intro": (
            "Na véspera da batalha, Bjorn te leva de volta à forja. "
            "Ele aquece o metal em silêncio por um tempo e então fala: "
            "'Vou forjar uma arma para você. Mas as runas que darão força a ela "
            "precisam ser pronunciadas por quem as entende.' "
            "Ele te olha firme: 'Prove que você aprendeu nossa língua de verdade.' "
            "Este é o teste final antes do confronto."
        ),
        "narrative_outro": (
            "A arma está pronta. As runas brilham fracamente no metal ainda quente. "
            "Bjorn a coloca nas suas mãos com cuidado: "
            "'Agora você é um de nós, Kael.' "
            "Você sentiu algo se encaixar — não só a língua, mas quem você estava se tornando."
        ),
        "key_words": [
            "Stark — forte",
            "Mut — coragem",
            "Kämpfen — lutar",
            "Sieg — vitória",
        ],
        "scenario_slug": "technology",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 9,
        "title": "Véspera",
        "narrative_intro": (
            "A última noite antes da batalha. A aldeia acende fogueiras grandes. "
            "As famílias se reúnem. Velhos contam histórias antigas. "
            "Crianças dormem nos braços dos pais. "
            "Você se senta com Bjorn e Sigrid e simplesmente conversa — "
            "sobre a aldeia, sobre o que veio antes, sobre o que virá amanhã. "
            "Esta noite, a língua não é uma ferramenta. É conexão."
        ),
        "narrative_outro": (
            "A fogueira queima baixo. Bjorn já dorme. "
            "Sigrid te olha com calma e diz: "
            "'Você chegou sem memória e sem palavras. Agora tem as duas.' "
            "Você sorriu. Amanhã é a batalha. "
            "Mas esta noite, pela primeira vez, você estava em casa."
        ),
        "key_words": [
            "Familie — família",
            "Zuhause — lar / em casa",
            "Morgen — amanhã",
            "Bereit — pronto",
        ],
        "scenario_slug": "daily-routine",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 10,
        "title": "O Confronto",
        "narrative_intro": (
            "O Guardião do clã inimigo se ergue diante de você no campo aberto. "
            "Ele é enorme, com olhos frios e uma voz que ecoa como trovão. "
            "Mas você percebe algo que os outros não viram: "
            "ele desafia com palavras antes de atacar. "
            "Ele acredita que ninguém fora do clã dele conhece a língua. "
            "Esta batalha não é de espadas — é de domínio. "
            "Cada palavra que você aprendeu é uma arma. Use tudo."
        ),
        "narrative_outro": (
            "O Guardião recua, pela primeira vez em anos. "
            "Ele nunca havia enfrentado alguém que conhecesse a língua tão bem — "
            "um forasteiro que a aprendeu não por obrigação, mas por escolha. "
            "'Quem é você?', ele pergunta em voz baixa. "
            "Uma memória surge — rápida, fragmentada, mas real. "
            "Você sorri: 'Sou Kael. E este idioma agora é meu.' "
            "O clã inimigo se retira. A aldeia está salva. "
            "E no bolso, você encontra o Runenschild — "
            "o Escudo das Runas que o Guardião carregava. "
            "Ele será sua vantagem no próximo capítulo."
        ),
        "key_words": [
            "Ich verstehe — eu entendo",
            "Ich bin bereit — estou pronto",
            "Wir kämpfen zusammen — lutamos juntos",
            "Ich habe gewonnen — eu venci",
        ],
        "scenario_slug": "social",
        "phrase_count": 10,
        "is_boss": True,
    },
]


class Command(BaseCommand):
    help = "Seed adventure chapters and phases for German A1."

    def handle(self, *args, **options):
        try:
            de = Language.objects.get(code="DE")
        except Language.DoesNotExist:
            self.stdout.write(self.style.ERROR("Language DE not found. Run seed_content first."))
            return

        chapter, created = AdventureChapter.objects.update_or_create(
            slug="de-a1",
            defaults={
                "language": de,
                "level": "A1",
                "order": 1,
                "title": "Vila dos Germânicos",
                "subtitle": "Das Erwachen — O Despertar",
                "background": "medieval-village",
                "boss_name": "O Guardião",
                "boss_intro": (
                    "Um guerreiro colossal bloqueia o caminho. "
                    "Ele ri ao ver um forasteiro — mas você não é mais um forasteiro. "
                    "Prove que domina a língua e derrote-o com as palavras que aprendeu."
                ),
                "reward_name": "Runenschild",
                "reward_description": (
                    "O Escudo das Runas, arrancado das mãos do Guardião derrotado. "
                    "Carrega marcas de batalhas antigas e concede vantagem nos desafios do próximo capítulo."
                ),
            },
        )

        action = "Criado" if created else "Atualizado"
        self.stdout.write(f"{action} capítulo: {chapter}")

        phases_created = 0
        phases_updated = 0

        for phase_data in PHASES_DE_A1:
            _, phase_created = AdventurePhase.objects.update_or_create(
                chapter=chapter,
                number=phase_data["number"],
                defaults={k: v for k, v in phase_data.items() if k != "number"},
            )
            if phase_created:
                phases_created += 1
            else:
                phases_updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Adventure seed concluido: {phases_created} fases criadas, {phases_updated} atualizadas."
            )
        )
