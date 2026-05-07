from django.core.management.base import BaseCommand

from apps.adventure.models import AdventureChapter, AdventurePhase
from apps.learning.models import Language


# ─── T1 · A1 — Arrivo al Borgo ────────────────────────────────────────────────

PHASES_IT_A1 = [
    {
        "number": 1,
        "title": "Il Risveglio",
        "narrative_intro": (
            "Você acorda ao lado de uma fonte de pedra. "
            "O cheiro de alecrim e pão quente vem das casas próximas. "
            "Uma mulher idosa passa carregando um cesto e te olha com desconfiança. "
            "Você abre a boca para pedir ajuda — e percebe que não sabe como. "
            "As palavras desta língua são estranhas, mas belas. "
            "Para sobreviver aqui, você precisará aprendê-las, começando pelas mais simples."
        ),
        "narrative_outro": (
            "A mulher te deu água e apontou para a taverna no centro do borgo. "
            "Você entendeu as primeiras palavras: 'acqua', 'pane', 'grazie'. "
            "Pequenas como sementes — mas era um começo."
        ),
        "key_words": [
            "Acqua — água",
            "Pane — pão",
            "Grazie — obrigado",
            "Per favore — por favor",
        ],
        "scenario_slug": "restaurant",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 2,
        "title": "Il Borgo",
        "narrative_intro": (
            "O borgo é pequeno, mas cheio de vida. "
            "Um menino corre e aponta entusiasmado para cada lugar: "
            "a piazza, la chiesa, il pozzo, la bottega. "
            "Você percebe que para não se perder — e não parecer suspeito — "
            "precisa aprender a se orientar e a perguntar o caminho."
        ),
        "narrative_outro": (
            "Agora você consegue atravessar o borgo sem se perder. "
            "Algumas pessoas já respondem quando você pergunta direções. "
            "O menino, Piero, virou seu guia informal. "
            "Ele ri dos seus erros — mas com carinho."
        ),
        "key_words": [
            "Dov'è — onde fica",
            "Qui — aqui",
            "A sinistra — à esquerda",
            "A destra — à direita",
        ],
        "scenario_slug": "transport",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 3,
        "title": "La Taverna",
        "narrative_intro": (
            "A taverna de Marco é o coração do borgo. "
            "Barulhenta, quente, cheia de gente que fala rápido e ri alto. "
            "Marco te olha com curiosidade quando você entra: "
            "'Straniero. Da dove vieni?' "
            "Você não entende tudo — mas percebe que ele não é hostil. "
            "Se conseguir conversar com ele, talvez encontre um lugar para dormir esta noite."
        ),
        "narrative_outro": (
            "Marco gargalhou quando você misturou as palavras. "
            "Mas no final, estendeu a mão: 'Mi chiamo Marco. E tu?' "
            "Você inventou um nome. Ele aceitou sem perguntar mais nada. "
            "Você tinha um aliado — e uma cama para dormir."
        ),
        "key_words": [
            "Mi chiamo — meu nome é",
            "Sono — eu sou",
            "Amico — amigo",
            "Aiutare — ajudar",
        ],
        "scenario_slug": "social",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 4,
        "title": "Il Mercato",
        "narrative_intro": (
            "Marco te manda ao mercado pela manhã com uma lista e algumas moedas. "
            "'Semplice', ele diz. Mas no mercado, os vendedores falam rápido "
            "e os preços mudam dependendo de quem está comprando. "
            "Um forasteiro sem habilidade com a língua paga o dobro. "
            "Você precisa aprender a comprar, barganhar e se defender com palavras."
        ),
        "narrative_outro": (
            "Você voltou com tudo da lista — e ainda sobrou uma moeda. "
            "Marco abriu os olhos: 'Hai contrattato con la Signora Bianchi? Impossibile.' "
            "Você sorriu. A língua estava começando a trabalhar a seu favor."
        ),
        "key_words": [
            "Quanto costa — quanto custa",
            "Voglio comprare — quero comprar",
            "È troppo caro — é muito caro",
            "Ho bisogno di — preciso de",
        ],
        "scenario_slug": "market",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 5,
        "title": "La Guardia",
        "narrative_intro": (
            "Dois guardas te param na entrada norte do borgo. "
            "'Chi sei? Da dove vieni? Cosa vuoi qui?' "
            "As perguntas chegam rápidas. Eles não parecem amigáveis. "
            "Você sabe que qualquer resposta confusa pode significar uma noite na prisão local. "
            "É hora de usar tudo que aprendeu para se identificar e explicar sua presença."
        ),
        "narrative_outro": (
            "Os guardas trocaram um olhar e te deixaram passar. "
            "Um deles murmurou: 'Straniero, ma parla bene.' "
            "Não era um elogio generoso — mas era suficiente. "
            "Você aprendeu que a língua também é um escudo."
        ),
        "key_words": [
            "Mi chiamo — me chamo",
            "Vengo da — venho de",
            "Non capisco — não entendo",
            "Puoi ripetere — pode repetir",
        ],
        "scenario_slug": "services",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 6,
        "title": "La Guaritrice",
        "narrative_intro": (
            "Lucia vive no fim da rua mais estreita do borgo, entre ervas secas e frascos coloridos. "
            "Marco te disse: 'Se você está com dor, fala com Lucia. Mas seja preciso — "
            "ela não tem paciência para quem não sabe descrever o que sente.' "
            "Um guerreiro local entrou antes de você, pálido e suando frio. "
            "Lucia te olha: 'Traduza para mim.' "
            "Você precisa aprender as palavras do corpo e da dor."
        ),
        "narrative_outro": (
            "O guerreiro saiu com uma erva e instrução em mãos. "
            "Lucia te olhou com aprovação silenciosa: 'Vai bene.' "
            "Vindo dela, isso equivalia a uma declaração de amizade."
        ),
        "key_words": [
            "Mi fa male — está doendo",
            "Ho la febbre — estou com febre",
            "Non mi sento bene — não me sinto bem",
            "Aiuto — socorro / ajuda",
        ],
        "scenario_slug": "health",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 7,
        "title": "La Festa",
        "narrative_intro": (
            "O borgo acendeu tochas nas ruas. Há música, vinho e risadas. "
            "Piero te puxa pelo braço: 'Vieni! È la festa di San Lorenzo!' "
            "Em festas, as pessoas falam mais, perguntam mais e esperam que você participe. "
            "É o momento perfeito para praticar — e para conhecer alguém que talvez saiba quem você é."
        ),
        "narrative_outro": (
            "Você dançou, comeu, riu dos próprios erros e corrigiu alguns. "
            "Uma senhora idosa te segurou pelo braço no final da noite: "
            "'Tu parli come noi adesso.' Você fala como nós agora. "
            "Você não sabia seu nome — mas sabia que estava começando a pertencer."
        ),
        "key_words": [
            "Come stai — como você está",
            "Bene, grazie — bem, obrigado",
            "Sono felice — estou feliz",
            "Insieme — juntos",
        ],
        "scenario_slug": "social",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 8,
        "title": "Il Lavoro",
        "narrative_intro": (
            "Marco te oferece trabalho na taverna em troca de comida e abrigo. "
            "'Ma devi saper parlare con i clienti', ele avisa. "
            "Os clientes pedem, reclamam, elogiam e mudam de ideia constantemente. "
            "Você precisa aprender a língua do trabalho: servir, confirmar, pedir desculpa, resolver."
        ),
        "narrative_outro": (
            "No final do primeiro dia, Marco jogou uma moeda na sua direção. "
            "'Non male per uno straniero.' Não mau para um estrangeiro. "
            "Era pouco — mas significava que você estava ganhando seu lugar aqui."
        ),
        "key_words": [
            "Subito — agora mesmo",
            "Ho capito — entendi",
            "Mi dispiace — me desculpe",
            "Tutto bene — tudo bem",
        ],
        "scenario_slug": "work",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 9,
        "title": "La Vigilia",
        "narrative_intro": (
            "Marco, Lucia e Piero sentam com você na taverna depois que todos foram embora. "
            "Marco fala devagar, pela primeira vez: ele está preocupado. "
            "Il Podestà, o governador local, quer expulsar forasteiros do borgo. "
            "Amanhã haverá um confronto público. "
            "Eles acreditam que você pode ajudar — mas só se falar bem o suficiente para ser ouvido."
        ),
        "narrative_outro": (
            "Lucia colocou uma vela na janela: 'Per buona fortuna.' Para boa sorte. "
            "Você olhou para eles — três pessoas que te acolheram sem perguntar quem você era. "
            "Amanhã, você falaria por eles."
        ),
        "key_words": [
            "Domani — amanhã",
            "Sono pronto — estou pronto",
            "Insieme ce la facciamo — juntos conseguimos",
            "Non ho paura — não tenho medo",
        ],
        "scenario_slug": "daily-routine",
        "phrase_count": 6,
        "is_boss": False,
    },
    {
        "number": 10,
        "title": "Il Podestà",
        "narrative_intro": (
            "Il Podestà se ergue na piazza central com a voz de quem está acostumado a não ser contrariado. "
            "Ele aponta para você: 'Questo straniero non ha documentos, non ha famiglia, non ha passato.' "
            "A multidão murmura. Marco e Lucia estão ao seu lado. "
            "Mas você percebe algo que o Podestà não esperava: "
            "você aprendeu a língua deles — não por obrigação, mas por escolha. "
            "E isso dá a você o direito de falar. Use cada palavra que aprendeu."
        ),
        "narrative_outro": (
            "O Podestà recuou. A multidão ficou em silêncio por um momento — "
            "e então Marco bateu palmas. Depois Piero. Depois todos. "
            "Il Podestà saiu sem dizer mais nada. "
            "Você ficou de pé na piazza, exausto e livre. "
            "Marco veio até você e colocou algo frio na sua mão: "
            "um sigillo antigo, de prata, com um caminho gravado. "
            "'Era do último viajante que passou por aqui, há muitos anos.' "
            "'Agora é seu.' "
            "O Sigillo del Viandante brilhou fracamente. "
            "Havia mais caminhos pela frente."
        ),
        "key_words": [
            "Io capisco — eu entendo",
            "Sono qui — estou aqui",
            "Ho scelto questa lingua — escolhi essa língua",
            "Ho vinto — venci",
        ],
        "scenario_slug": "social",
        "phrase_count": 10,
        "is_boss": True,
    },
]


# ─── T2 · A2 — I Canali di Venezia ───────────────────────────────────────────

PHASES_IT_A2 = [
    {
        "number": 1,
        "title": "L'Arrivo in Barca",
        "narrative_intro": (
            "A gôndola desliza por um canal estreito ao amanhecer. "
            "A cidade à sua frente é diferente de tudo que você viu no borgo: "
            "palazzi cor-de-rosa e dourado refletidos na água verde. "
            "O gondoleiro Giacomo te olha de soslaio: 'Prima volta a Venezia?' "
            "Você tem o Sigillo del Viandante no bolso — e a língua no coração. "
            "Mas esta cidade fala de um jeito diferente. Mais rápido. Mais musical."
        ),
        "narrative_outro": (
            "Giacomo amarrou a gôndola num cais de pedra e apontou para o mercado. "
            "'Vai lì. Trovi Beatrice. Lei sa tutto.' "
            "Você não entendia tudo — mas entendia o suficiente para ir."
        ),
        "key_words": [
            "Devo andare — devo ir",
            "Quanto tempo — quanto tempo",
            "Ho già — já tenho",
            "Mi può aiutare — pode me ajudar",
        ],
        "scenario_slug": "transport",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 2,
        "title": "Il Mercato del Pesce",
        "narrative_intro": (
            "O mercado de peixe fervilha de vozes e cheiros fortes. "
            "Beatrice, uma mercadora de cabelos pretos e olhos rápidos, "
            "negocia três conversas ao mesmo tempo sem perder o fio de nenhuma. "
            "Ela te vê, reconhece o Sigillo e para tudo: "
            "'Tu sei il viandante. Siediti. Parliamo.' "
            "Mas primeiro, ela quer saber se você sobrevive numa negociação veneziana."
        ),
        "narrative_outro": (
            "Beatrice sorriu — um sorriso raro, você descobrirá. "
            "'Non male. Hai imparato bene nel borgo.' "
            "Ela te contou sobre a cidade, sobre os mercadores e sobre alguém "
            "que estava procurando um viajante com um sigillo antigo."
        ),
        "key_words": [
            "Preferisco — prefiro",
            "È possibile — é possível",
            "Ho già comprato — já comprei",
            "Cosa include — o que inclui",
        ],
        "scenario_slug": "market",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 3,
        "title": "Il Palazzo",
        "narrative_intro": (
            "Beatrice te leva a um palazzo no Grand Canal para um jantar de mercadores. "
            "Aqui, a língua é formal, cuidadosa, cheia de subtexto. "
            "Um erro de vocabulário pode custar um contrato — ou revelar quem você realmente é. "
            "Você não sabe ao certo quem é. Mas sabe que precisa parecer que sabe."
        ),
        "narrative_outro": (
            "Você passou pelo jantar sem revelar nada que não devia. "
            "De volta ao canal, Beatrice disse: "
            "'Você aprendeu a língua do borgonha. Agora aprendeu a língua do palazzo.' "
            "'São a mesma língua,' você respondeu. 'Só o volume muda.' "
            "Ela riu. Era a verdade."
        ),
        "key_words": [
            "Le presento — apresento-lhe",
            "Con piacere — com prazer",
            "Sono d'accordo — concordo",
            "Mi permetta — com sua licença",
        ],
        "scenario_slug": "work",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 4,
        "title": "La Tempesta",
        "narrative_intro": (
            "Uma tempestade chegou pelo Adriático sem aviso. "
            "Giacomo precisava de ajuda nos canais — cordas, sinais, avisos aos outros gondoleiros. "
            "Na escuridão e na chuva, a comunicação rápida e precisa era questão de vida. "
            "Você foi chamado para ajudar a coordenar."
        ),
        "narrative_outro": (
            "A tempestade passou. Nenhuma embarcação afundou. "
            "Giacomo te abraçou com as roupas encharcadas: 'Fratello.' Irmão. "
            "Era a primeira vez que alguém usava aquela palavra com você."
        ),
        "key_words": [
            "Attento — cuidado",
            "Pronto — pronto",
            "Ancora — ainda / âncora",
            "Forza — força / vai em frente",
        ],
        "scenario_slug": "travel",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 5,
        "title": "Il Mercante Oscuro",
        "narrative_intro": (
            "Beatrice te avisou: 'Il Mercante Oscuro compra e vende segredos. "
            "Ele sabe quem você é — ou pensa que sabe. "
            "E quer o Sigillo.' "
            "O encontro aconteceu num armazém de especiarias às margens do canal. "
            "Ele é educado, preciso e perigoso. "
            "Mas você percebeu algo: ele pressupõe que você é fraco na língua. "
            "Essa é sua vantagem."
        ),
        "narrative_outro": (
            "Il Mercante Oscuro saiu de mãos vazias — pela primeira vez em anos, dizem. "
            "Beatrice ficou boquiaberta: 'Como você fez isso?' "
            "'Usei as palavras dele contra ele.' "
            "A Mappa dei Canali caiu no seu bolso como recompensa. "
            "Os caminhos de Venezia agora eram seus."
        ),
        "key_words": [
            "Non è in vendita — não está à venda",
            "Ho capito la situazione — entendi a situação",
            "Questo non mi interessa — isso não me interessa",
            "Ho già deciso — já decidi",
        ],
        "scenario_slug": "social",
        "phrase_count": 10,
        "is_boss": True,
    },
    {
        "number": 6,
        "title": "La Biblioteca",
        "narrative_intro": (
            "Beatrice te levou à biblioteca do palazzo mais antigo de Venezia. "
            "Lá, um bibliotecário silencioso guardava registros de viajantes dos últimos dois séculos. "
            "Talvez houvesse algo sobre você — ou sobre quem você era antes."
        ),
        "narrative_outro": (
            "O bibliotecário encontrou uma entrada com uma descrição familiar. "
            "Mas as páginas seguintes estavam arrancadas. "
            "Alguém havia passado antes de você. "
            "A jornada estava ficando mais complexa."
        ),
        "key_words": [
            "Sto cercando — estou procurando",
            "Ha trovato — encontrou",
            "Da quanto tempo — há quanto tempo",
            "Dove posso trovare — onde posso encontrar",
        ],
        "scenario_slug": "university",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 7,
        "title": "Il Carnevale",
        "narrative_intro": (
            "O Carnaval de Venezia transformou a cidade. Máscaras por todo lado. "
            "Ninguém é quem parece ser — o que, para você, era libertador. "
            "Mas também significava que seus inimigos podiam estar em qualquer lugar. "
            "Você precisava se comunicar na multidão sem revelar sua identidade."
        ),
        "narrative_outro": (
            "Na última hora da noite, você encontrou Giacomo sem máscara. "
            "'Sai chi sei adesso?' Você sabe quem é agora? "
            "Você ainda não sabia o nome — mas sabia o que era. "
            "Um viajante que pertencia à língua que escolheu aprender."
        ),
        "key_words": [
            "Non lo so — não sei",
            "Forse — talvez",
            "Mi sembra — me parece",
            "Posso fidarmi di te — posso confiar em você",
        ],
        "scenario_slug": "social",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 8,
        "title": "La Partenza",
        "narrative_intro": (
            "Era hora de partir para a Toscana. "
            "Beatrice organizou os suprimentos, Giacomo preparou a rota. "
            "Mas você precisava resolver pendências antes de ir: "
            "pagar dívidas, agradecer, despedir-se de quem te ajudou."
        ),
        "narrative_outro": (
            "Giacomo te levou ao cais ao amanhecer. "
            "'A Toscana è diversa,' ele disse. 'Più lenta. Più profonda.' "
            "Você não sabia o que te esperava. "
            "Mas a Mappa dei Canali brilhava no bolso — e havia estradas para percorrer."
        ),
        "key_words": [
            "Devo partire — devo partir",
            "Grazie di tutto — obrigado por tudo",
            "Ci rivedremo — nos veremos novamente",
            "Buon viaggio — boa viagem",
        ],
        "scenario_slug": "travel",
        "phrase_count": 8,
        "is_boss": False,
    },
]


# ─── T3 · B1 — Le Colline della Toscana ──────────────────────────────────────

PHASES_IT_B1 = [
    {
        "number": 1,
        "title": "La Strada dei Cipressi",
        "narrative_intro": (
            "A estrada toscana é longa, silenciosa e bordeada de ciprestes. "
            "Você caminha por horas sem ver ninguém. "
            "Então, no alto de uma colina, aparece um mosteiro antigo. "
            "Fra' Lorenzo, um monge de cabelos brancos, te abre a porta sem perguntar nada. "
            "'Vieni. Hai fame. Si vede.' Você tem fome. Dá para ver. "
            "Aqui, as conversas são longas, filosóficas e sem pressa."
        ),
        "narrative_outro": (
            "Depois do jantar, Fra' Lorenzo te perguntou: 'Cosa stai cercando davvero?' "
            "O que você está realmente procurando? "
            "Você não tinha uma resposta — mas percebeu que era a primeira vez "
            "que alguém fazia a pergunta certa."
        ),
        "key_words": [
            "Sto cercando — estou procurando",
            "Non sono sicuro — não tenho certeza",
            "Mi chiedo se — fico me perguntando se",
            "Dipende da — depende de",
        ],
        "scenario_slug": "daily-routine",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 2,
        "title": "La Biblioteca del Convento",
        "narrative_intro": (
            "O mosteiro tem uma biblioteca com manuscritos de séculos. "
            "Fra' Lorenzo te deixa ali e diz: 'Hai il tempo che ti serve.' "
            "Você tem o tempo que precisar. "
            "Isabella, uma estudiosa de Florença, já está lá quando você chega. "
            "Ela estudava os mesmos documentos que você procurava."
        ),
        "narrative_outro": (
            "Isabella olhou para o Sigillo del Viandante e abriu os olhos. "
            "'Conosco questo sigillo. L'ho visto in un documento del 1347.' "
            "Você não era o primeiro viandante. E talvez não fosse o último."
        ),
        "key_words": [
            "Ho letto che — li que",
            "Secondo me — na minha opinião",
            "È possibile che — é possível que",
            "Mi sembra importante — me parece importante",
        ],
        "scenario_slug": "university",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 3,
        "title": "La Vendemmia",
        "narrative_intro": (
            "Era época de colheita nas vinícolas. "
            "Os contadini precisavam de mais mãos, e você se ofereceu para ajudar. "
            "Trabalhar com as mãos e falar ao mesmo tempo — essa era a prova real de fluência. "
            "Ninguém aqui tem paciência para quem não entende instrução na primeira vez."
        ),
        "narrative_outro": (
            "Ao fim do dia, o vinho novo foi provado em grupo. "
            "Um velho contadino te passou a taça e disse: 'Hai lavorato come uno di noi.' "
            "Você trabalhou como um de nós. "
            "Era mais do que um elogio. Era uma adoção."
        ),
        "key_words": [
            "Come si fa — como se faz",
            "Ho bisogno di aiuto — preciso de ajuda",
            "Lasciami provare — deixa eu tentar",
            "Adesso capisco — agora entendo",
        ],
        "scenario_slug": "work",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 4,
        "title": "Il Villaggio in Collina",
        "narrative_intro": (
            "No topo da colina há um pequeno vilaggio onde todos se conhecem. "
            "Novidades chegam devagar — e um forasteiro é notícia. "
            "O alcaide local quer saber quem você é, de onde veio e para onde vai. "
            "Aqui não há mercadores ou guardas: há vizinhos. "
            "A língua precisa ser íntima, direta e honesta."
        ),
        "narrative_outro": (
            "O alcaide te convidou para jantar com a família. "
            "À mesa, você falou mais do que nos últimos meses combinados. "
            "Errou palavras, foi corrigido com gentileza, e aprendeu que errar "
            "em volta de gente boa é a forma mais rápida de melhorar."
        ),
        "key_words": [
            "Da quanto tempo sei qui — há quanto tempo você está aqui",
            "Ho vissuto a — morei em",
            "Mi piace perché — gosto porque",
            "Preferisco — prefiro",
        ],
        "scenario_slug": "housing",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 5,
        "title": "La Lettera",
        "narrative_intro": (
            "Isabella encontrou uma carta nos arquivos do mosteiro — endereçada a 'il Viandante'. "
            "Escrita em italiano antigo, ela descrevia alguém que havia passado pelo mesmo caminho. "
            "Alguém que havia chegado sem memória, aprendido a língua, "
            "e desaparecido na direção de Napoli. "
            "Você leu cada linha em voz alta, traduzindo enquanto lia."
        ),
        "narrative_outro": (
            "Ao terminar, Fra' Lorenzo disse: 'Chi l'ha scritto sapeva di te.' "
            "Quem escreveu sabia de você. "
            "Você dobrou a carta com cuidado. "
            "Napoli era o próximo passo."
        ),
        "key_words": [
            "Ho capito il significato — entendi o significado",
            "Si riferisce a — se refere a",
            "Questo spiega — isso explica",
            "Devo scoprire — preciso descobrir",
        ],
        "scenario_slug": "university",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 6,
        "title": "La Guarigione",
        "narrative_intro": (
            "Numa aldeia menor, você encontrou um médico local em dificuldades: "
            "um surto de febre e pacientes demais. "
            "Ele precisava de um assistente que soubesse comunicar diagnósticos simples. "
            "Você passou os próximos dias aprendendo vocabulário médico na prática."
        ),
        "narrative_outro": (
            "A febre passou. O médico te pagou com comida e palavras: "
            "'Lei ha una dote rara: sa ascoltare e rispondere nel momento giusto.' "
            "Você tem um dom raro: sabe ouvir e responder no momento certo. "
            "Era talvez a melhor descrição de quem você estava se tornando."
        ),
        "key_words": [
            "Può descrivere — pode descrever",
            "Da quanto tempo — há quanto tempo",
            "Sta migliorando — está melhorando",
            "Ha bisogno di riposo — precisa de descanso",
        ],
        "scenario_slug": "health",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 7,
        "title": "Il Maestro",
        "narrative_intro": (
            "Il Maestro Oscuro mora numa villa isolada entre os ciprestes. "
            "Isabella te avisou: ele compra e vende informação sobre viajantes sem memória. "
            "Ele já soube que você existe. E quer fazer uma troca: "
            "o Sigillo del Viandante em troca de informações sobre seu passado. "
            "A conversa seria em italiano culto, formal e sem margem para ambiguidade. "
            "Você teria uma chance. Use cada nuance que aprendeu."
        ),
        "narrative_outro": (
            "Il Maestro ficou em silêncio por um longo momento depois que você terminou de falar. "
            "Então abriu uma gaveta e tirou um pequeno códice encadernado em couro: "
            "'Prendilo. Ho già quello che cercavo — vederti parlare.' "
            "Pegue. Já tenho o que procurava — te ver falar. "
            "O Codice Antico estava nas suas mãos. "
            "E dentro dele, havia nomes que você reconhecia."
        ),
        "key_words": [
            "Non accetto questa proposta — não aceito essa proposta",
            "Permettemi di spiegare — permita-me explicar",
            "La situazione è complessa — a situação é complexa",
            "Ho le mie ragioni — tenho minhas razões",
        ],
        "scenario_slug": "work",
        "phrase_count": 10,
        "is_boss": True,
    },
    {
        "number": 8,
        "title": "Il Congedo",
        "narrative_intro": (
            "Hora de se despedir da Toscana. "
            "Fra' Lorenzo, Isabella e o velho contadino estavam esperando na estrada. "
            "Eles sabiam que você ia embora — e queriam dizer coisas que importavam."
        ),
        "narrative_outro": (
            "Fra' Lorenzo colocou uma mão no seu ombro: "
            "'Porti la lingua con te come un mantello. Ti proteggerà.' "
            "Leve a língua com você como um manto. Ela vai te proteger. "
            "Napoli estava no horizonte. E dentro do Codice, havia um endereço."
        ),
        "key_words": [
            "Non dimenticherò — não esquecerei",
            "Mi avete insegnato molto — me ensinaram muito",
            "Tornerò — voltarei",
            "Vi porterò sempre nel cuore — sempre os levarei no coração",
        ],
        "scenario_slug": "social",
        "phrase_count": 8,
        "is_boss": False,
    },
]


# ─── T4 · B2 — Il Vesuvio ─────────────────────────────────────────────────────

PHASES_IT_B2 = [
    {
        "number": 1,
        "title": "Napoli dal Mare",
        "narrative_intro": (
            "Napoli aparece do mar como uma cidade que cresceu rápido demais para si mesma. "
            "Barulhenta, caótica, cheia de vida em todas as direções. "
            "O Vesuvio observa tudo de cima com indiferença. "
            "Você desceu do barco com o Codice na mochila e um endereço na cabeça. "
            "Aqui ninguém tem tempo para quem não se expressa com clareza."
        ),
        "narrative_outro": (
            "O porteiro do palazzetto te olhou dos pés à cabeça "
            "e disse: 'Lei parla bene per essere straniero.' "
            "Você fala bem para ser estrangeiro. "
            "Você respondeu: 'Non sono più straniero.' Não sou mais estrangeiro. "
            "Ele levantou uma sobrancelha e te deixou entrar."
        ),
        "key_words": [
            "Ho sentito dire che — ouvi dizer que",
            "Si dice che — dizem que",
            "Stando a quello che so — pelo que sei",
            "È noto che — é sabido que",
        ],
        "scenario_slug": "social",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 2,
        "title": "La Vittoria",
        "narrative_intro": (
            "Vittoria é pescadora, filósofa e a pessoa mais direta que você já encontrou. "
            "Ela leu o endereço no Codice e deu de ombros: "
            "'Conosco quel posto. È pericoloso.' "
            "Mas concordou em te ajudar — com uma condição: "
            "que você prove que é capaz de argumentar, não apenas responder."
        ),
        "narrative_outro": (
            "Vittoria bateu na mesa com aprovação: 'Bene. Sai difendere le tue idee.' "
            "Você sabe defender suas ideias. "
            "Era exatamente o que você precisaria onde estava indo."
        ),
        "key_words": [
            "Sono convinto che — estou convicto de que",
            "Non sono d'accordo perché — discordo porque",
            "Bisogna considerare che — é preciso considerar que",
            "Dal mio punto di vista — do meu ponto de vista",
        ],
        "scenario_slug": "work",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 3,
        "title": "I Quartieri",
        "narrative_intro": (
            "O endereço no Codice levava aos quartieri antichi — "
            "becos onde a memória da cidade é mais densa que o ar. "
            "Para navegar ali sem atrair atenção errada, "
            "você precisava falar como alguém que conhece os costumes locais, "
            "não como um viajante de passagem."
        ),
        "narrative_outro": (
            "Um velho sentado na soleira de uma porta te chamou: "
            "'Aspetta. Ti ho visto prima, su un quadro antico.' "
            "Espera. Te vi antes, num quadro antigo. "
            "Você sentou ao lado dele. Ele começou a contar uma história."
        ),
        "key_words": [
            "Hai mai sentito parlare di — você já ouviu falar de",
            "Secondo la tradizione — segundo a tradição",
            "Mi ricorda — me lembra",
            "È come se — é como se",
        ],
        "scenario_slug": "travel",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 4,
        "title": "Il Documento",
        "narrative_intro": (
            "O quadro que o velho descreveu estava numa cartório municipal. "
            "Para acessá-lo, você precisava navegar burocracia italiana — "
            "a mais complexa, lenta e inesperadamente poética do mundo. "
            "Don Pasquale, o funcionário, falava em subordinativos e condicionais. "
            "Você aprendeu a fazer o mesmo."
        ),
        "narrative_outro": (
            "Don Pasquale finalmente abriu o arquivo. "
            "O quadro mostrava um viajante — com o mesmo Sigillo. "
            "E abaixo, um nome. Um nome que você reconheceu. "
            "Não como memória — como verdade."
        ),
        "key_words": [
            "Avrei bisogno di — eu precisaria de",
            "Sarebbe possibile — seria possível",
            "Nel caso in cui — no caso em que",
            "Se non le dispiace — se não se importar",
        ],
        "scenario_slug": "services",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 5,
        "title": "L'Eruzione",
        "narrative_intro": (
            "O Vesuvio acordou. Não uma erupção — mas tremores suficientes "
            "para esvaziar os bairros mais próximos. "
            "Vittoria organizou a evacuação. Você foi designado para comunicar rotas "
            "às famílias mais idosas que não queriam sair. "
            "Aqui, persuasão era urgência. E urgência precisava de precisão."
        ),
        "narrative_outro": (
            "Todos chegaram ao ponto seguro. Vittoria contou as cabeças duas vezes. "
            "'Nessuno manca.' Não falta ninguém. "
            "Você olhou para o vulcão fumegante e sentiu algo esquisito: gratidão. "
            "Mesmo sem memória, estava construindo um histórico de ações. "
            "Isso também era identidade."
        ),
        "key_words": [
            "È urgente che — é urgente que",
            "Non c'è tempo da perdere — não há tempo a perder",
            "Dobbiamo agire subito — precisamos agir agora",
            "Fidatevi di me — confiem em mim",
        ],
        "scenario_slug": "health",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 6,
        "title": "Il Barone",
        "narrative_intro": (
            "Il Barone controla os portos de Napoli e quase tudo mais. "
            "Ele soube do documento municipal. Soube do quadro. "
            "E mandou um convite — que era, na verdade, uma ordem. "
            "A reunião seria num salão de mármores brancos com guardas nas paredes. "
            "Você iria sozinho. E usaria apenas palavras."
        ),
        "narrative_outro": (
            "Il Barone ficou de pé e te estendeu a mão — não como ameaça, mas como respeito. "
            "'Non sapevo che il Viandante fosse così... eloquente.' "
            "Não sabia que o Viandante fosse tão... eloquente. "
            "A Pietra del Vesuvio, negra e quente, estava na sua mão. "
            "'Roma ti aspetta,' ele disse. Roma te espera."
        ),
        "key_words": [
            "Permettetemi di essere diretto — permita-me ser direto",
            "Non intendo cedere — não pretendo ceder",
            "Questa è la mia posizione — esta é minha posição",
            "Ho tutto il necessario per dimostrare — tenho tudo para provar",
        ],
        "scenario_slug": "social",
        "phrase_count": 10,
        "is_boss": True,
    },
    {
        "number": 7,
        "title": "La Vigilia di Roma",
        "narrative_intro": (
            "Última noite em Napoli. Vittoria preparou uma ceia simples — "
            "pasta, pão, vinho do Vesuvio. "
            "Don Pasquale apareceu com um envelope. "
            "Dentro, uma carta em latim e italiano antigo: instruções para Roma. "
            "E pela primeira vez, um nome assinado embaixo que você reconhecia como seu."
        ),
        "narrative_outro": (
            "Vittoria levantou o copo: 'A chi sei diventato.' "
            "Para quem você se tornou. "
            "Você levantou o copo também. "
            "Roma amanhã. E a resposta para tudo."
        ),
        "key_words": [
            "Sono pronto per — estou pronto para",
            "Ho imparato abbastanza — aprendi o suficiente",
            "Non vedo l'ora di — mal posso esperar para",
            "Sarà difficile ma — será difícil mas",
        ],
        "scenario_slug": "daily-routine",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 8,
        "title": "Verso Roma",
        "narrative_intro": (
            "A estrada para Roma. "
            "Sozinho desta vez — Vittoria ficou em Napoli, Don Pasquale nos seus documentos. "
            "Você tinha o Sigillo, a Mappa, o Codice e a Pietra. "
            "Quatro objetos de quatro cidades. "
            "E pela primeira vez, um senso de direção que não vinha do mapa — vinha de dentro."
        ),
        "narrative_outro": (
            "Roma apareceu no horizonte ao entardecer. "
            "Cúpulas douradas e colunas antigas contra o céu laranja. "
            "Você parou por um momento. Respirou fundo. "
            "E entrou."
        ),
        "key_words": [
            "Dopo tutto questo tempo — depois de todo esse tempo",
            "Finalmente — finalmente",
            "È il momento di — é o momento de",
            "So chi sono — sei quem sou",
        ],
        "scenario_slug": "travel",
        "phrase_count": 8,
        "is_boss": False,
    },
]


# ─── T5 · C1 — La Grande Roma ─────────────────────────────────────────────────

PHASES_IT_C1 = [
    {
        "number": 1,
        "title": "L'Arrivo Eterno",
        "narrative_intro": (
            "Roma não é uma cidade — é uma sobreposição de tempos. "
            "Cada rua carrega três mil anos de conversas. "
            "Você entrou pela Porta del Popolo com quatro objetos no bolso "
            "e um nome na memória — o seu. "
            "Mas saber o nome era só o começo. "
            "Aqui, a língua precisava estar no nível mais alto: "
            "nuançada, precisa, capaz de convencer qualquer interlocutor."
        ),
        "narrative_outro": (
            "Um poeta sentado nos degraus de uma fontana te olhou com atenção. "
            "'Parli italiano come se l'avessi sempre saputo.' "
            "Você fala italiano como se sempre soubesse. "
            "Você sorriu: 'Forse è così.' Talvez seja assim."
        ),
        "key_words": [
            "Non si può fare a meno di — não se pode deixar de",
            "Vale la pena sottolineare — vale a pena sublinhar",
            "Tenendo conto di — levando em conta",
            "A prescindere da — independentemente de",
        ],
        "scenario_slug": "travel",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 2,
        "title": "Il Cardinale",
        "narrative_intro": (
            "O endereço no Codice levava a um palazzo vaticano. "
            "Il Cardinale Orsini te recebeu num jardim de laranjeiras. "
            "Ele sabia sobre o Viandante há anos — e tinha esperado. "
            "'Sapevo che saresti arrivato quando la lingua fosse pronta.' "
            "Sabia que chegaria quando a língua estivesse pronta. "
            "Aqui, as conversas eram longas, filosóficas e sem respostas simples."
        ),
        "narrative_outro": (
            "O Cardinale te deu acesso aos arquivos mais antigos do Vaticano. "
            "'Lì troverai le risposte. Ma preparati: alcune cambieranno tutto.' "
            "Lá você encontrará as respostas. Mas se prepare: algumas mudarão tudo."
        ),
        "key_words": [
            "Nel corso dei secoli — ao longo dos séculos",
            "È opportuno ricordare che — é oportuno lembrar que",
            "Alla luce di ciò — à luz disso",
            "Non si può ignorare il fatto che — não se pode ignorar o fato de que",
        ],
        "scenario_slug": "university",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 3,
        "title": "Gli Archivi",
        "narrative_intro": (
            "Os arquivos vaticanos são infinitos. "
            "Fiamma, uma poetisa que o Cardinale designou como sua guia, "
            "conhecia cada corredor como uma partitura musical. "
            "Nos documentos, você encontrou registros de outros viandantes. "
            "E finalmente, o seu próprio: nome completo, origem, e um evento "
            "que explicava tudo — inclusive por que você havia esquecido."
        ),
        "narrative_outro": (
            "Fiamma te olhou enquanto você lia. "
            "'Come ti senti?' Como você se sente? "
            "Você precisou de um tempo antes de responder. "
            "Era uma pergunta que exigia a língua inteira para ser respondida bem."
        ),
        "key_words": [
            "Stando a quanto ho letto — com base no que li",
            "Questo mi porta a concludere che — isso me leva a concluir que",
            "È evidente che — é evidente que",
            "Si tratta di — trata-se de",
        ],
        "scenario_slug": "university",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 4,
        "title": "La Poesia",
        "narrative_intro": (
            "Fiamma escrevia poesia toda manhã no Foro Romano. "
            "Ela te desafiou: escreva algo em italiano. "
            "Não uma frase. Não uma resposta. Algo criado. "
            "'La lingua vera si vede quando crei, non solo quando rispondi.' "
            "A língua verdadeira aparece quando você cria, não apenas quando responde."
        ),
        "narrative_outro": (
            "Você escreveu três linhas. Fiamma as leu em silêncio. "
            "Depois dobrou o papel e guardou. "
            "'Questo è italiano,' ela disse. 'Non perfetto. Ma italiano.' "
            "Isso é italiano. Não perfeito. Mas italiano."
        ),
        "key_words": [
            "Come direbbe un poeta — como diria um poeta",
            "In senso figurato — em sentido figurado",
            "Per usare le parole di — para usar as palavras de",
            "L'essenza di — a essência de",
        ],
        "scenario_slug": "social",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 5,
        "title": "Il Dibattito",
        "narrative_intro": (
            "O Cardinale organizou um debate público no Campidoglio. "
            "Filósofos, poetas, juristas. "
            "E você — o viandante que aprendeu a língua caminhando. "
            "O tema: 'O que une uma língua ao seu povo?' "
            "Era, claramente, uma pergunta sobre você."
        ),
        "narrative_outro": (
            "Quando você terminou de falar, houve silêncio. "
            "Depois aplausos. "
            "Fiamma te olhou: 'Hai risposto con tutta la tua storia.' "
            "Você respondeu com toda a sua história. "
            "Era verdade. Cada fase, cada cidade, cada palavra aprendida — "
            "estava ali, tecida no argumento."
        ),
        "key_words": [
            "Vorrei argomentare che — gostaria de argumentar que",
            "Contrariamente a quanto si pensa — ao contrário do que se pensa",
            "Ciò detto — dito isso",
            "In definitiva — em definitivo",
        ],
        "scenario_slug": "work",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 6,
        "title": "Il Ritorno della Memoria",
        "narrative_intro": (
            "Nos arquivos, você encontrou o último documento: "
            "uma carta que você mesmo havia escrito — antes de esquecer. "
            "Era em italiano. Porque você havia escolhido a língua muito antes "
            "de acordar ao lado da fonte no borgo. "
            "A memória voltou não como um raio — mas como uma maré."
        ),
        "narrative_outro": (
            "Você saiu dos arquivos com os olhos cheios. "
            "Fiamma estava esperando. "
            "'Hai trovato?' Você encontrou? "
            "'Ho trovato tutto.' Encontrei tudo. "
            "A língua que você aprendeu era a língua que você escolhera para viver. "
            "E agora a vivia de verdade."
        ),
        "key_words": [
            "Ora che so — agora que sei",
            "Tutto ha senso — tudo faz sentido",
            "Era questo che cercavo — era isso que procurava",
            "Finalmente ricordo — finalmente me lembro",
        ],
        "scenario_slug": "daily-routine",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 7,
        "title": "La Vigilia Finale",
        "narrative_intro": (
            "Última noite antes do confronto final. "
            "O Cardinale, Fiamma e um mensageiro de cada cidade que você visitou "
            "estavam reunidos no jardim do palazzo. "
            "Marco do borgo. Beatrice de Venezia. Isabella da Toscana. Vittoria de Napoli. "
            "Todos haviam sido avisados. Todos vieram. "
            "Ninguém sabia exatamente o que viria amanhã. "
            "Mas sabiam que estava chegando."
        ),
        "narrative_outro": (
            "A noite passou em conversas longas. "
            "Você falou com todos, em italiano, sobre tudo que havia aprendido. "
            "E percebeu: a língua era a linha que conectava cada uma dessas histórias. "
            "Amanhã, você a usaria de uma vez por todas."
        ),
        "key_words": [
            "Devo ringraziarvi — devo agradecer a vocês",
            "Senza di voi — sem vocês",
            "Questo momento — este momento",
            "Non finisce qui — não termina aqui",
        ],
        "scenario_slug": "social",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 8,
        "title": "Il Colosseo",
        "narrative_intro": (
            "O encontro foi marcado no Colosseo ao amanhecer. "
            "L'Imperatore — não um governante, mas o guardião do segredo da sua origem — "
            "estava esperando no centro da arena. "
            "Ele acreditava que a memória recuperada te tornaria vulnerável. "
            "Que saber quem você era significava saber o que você temia. "
            "Ele estava errado."
        ),
        "narrative_outro": (
            "L'Imperatore ficou em silêncio por um longo tempo depois do último argumento. "
            "Então fez algo inesperado: inclinou a cabeça. "
            "'Non ho mai incontrato qualcuno che usasse la lingua come un'armatura.' "
            "Nunca encontrei alguém que usasse a língua como uma armadura. "
            "Você respondeu: 'Non è un'armatura. È la mia casa.' "
            "Não é uma armadura. É minha casa. "
            "A Corona dell'Eloquenza caiu dos ombros dele para as suas mãos. "
            "Pesada, dourada, e com inscrições de cada cidade que você atravessou. "
            "A viagem havia terminado. "
            "A língua havia começado."
        ),
        "key_words": [
            "Ho imparato questa lingua per scelta — aprendi esta língua por escolha",
            "Non posso essere sconfitto — não posso ser derrotado",
            "Questa è la mia storia — esta é minha história",
            "Sono il Viandante — sou o Viandante",
        ],
        "scenario_slug": "social",
        "phrase_count": 12,
        "is_boss": True,
    },
    {
        "number": 9,
        "title": "L'Alba",
        "narrative_intro": (
            "Amanhã cedo. O Colosseo vazio de novo. "
            "Você está sentado na pedra antiga com a Corona ao lado. "
            "Fiamma chegou com dois cafès. "
            "'E adesso?' E agora? "
            "Você olhou para Roma acordando ao redor. "
            "E sorriu — porque sabia exatamente o que responder."
        ),
        "narrative_outro": (
            "A cidade começou a se encher de vozes. "
            "Italiano por todo lado — no mercado, nas janelas, nas crianças correndo. "
            "Você entendeu cada palavra. "
            "Não porque havia estudado. "
            "Porque havia vivido."
        ),
        "key_words": [
            "Adesso so — agora sei",
            "Ho tutto quello che mi serve — tenho tudo que preciso",
            "La lingua è mia — a língua é minha",
            "Il viaggio continua — a viagem continua",
        ],
        "scenario_slug": "daily-routine",
        "phrase_count": 8,
        "is_boss": False,
    },
    {
        "number": 10,
        "title": "Il Viandante",
        "narrative_intro": (
            "Você escreveu uma carta. Endereçada ao próximo viandante. "
            "Alguém que um dia acordaria sem memória, em algum lugar de Itália, "
            "e precisaria começar do zero. "
            "Como você havia começado. "
            "A carta começava: 'Caro Viandante, la prima parola che imparerai è acqua. "
            "Non perché hai sete — ma perché è lì che tutto comincia.'"
        ),
        "narrative_outro": (
            "Você deixou a carta dobrada ao lado da fonte no borgo de onde tudo começou. "
            "Deu uma última volta pela piazza. "
            "Marco acenou da taverna. Piero correu para te dar um abraço. "
            "Você disse: 'Ci vediamo presto.' Nos vemos em breve. "
            "E foi embora. "
            "Não sem memória desta vez. "
            "Com ela toda."
        ),
        "key_words": [
            "Grazie per tutto — obrigado por tudo",
            "Ho imparato più di una lingua — aprendi mais do que uma língua",
            "Porto con me — levo comigo",
            "A presto — até logo",
        ],
        "scenario_slug": "social",
        "phrase_count": 8,
        "is_boss": False,
    },
]


# ─── CHAPTERS CONFIG ─────────────────────────────────────────────────────────

CHAPTERS = [
    {
        "slug": "it-a1",
        "level": "A1",
        "order": 1,
        "title": "Arrivo al Borgo",
        "subtitle": "Il Risveglio — O Despertar",
        "background": "italian-village",
        "boss_name": "Il Podestà",
        "boss_intro": (
            "O Podestà se ergue na piazza com a autoridade de quem nunca foi contestado. "
            "Mas você não é mais o forasteiro de algumas semanas atrás. "
            "Cada palavra que aprendeu neste borgo é uma pedra no seu argumento. "
            "Use tudo."
        ),
        "reward_name": "Sigillo del Viandante",
        "reward_description": (
            "Um sigillo de prata com um caminho gravado, pertencente ao último viajante "
            "que passou por este borgo há séculos. Agora é seu. "
            "Concede reconhecimento nos próximos destinos."
        ),
        "phases": PHASES_IT_A1,
    },
    {
        "slug": "it-a2",
        "level": "A2",
        "order": 2,
        "title": "I Canali di Venezia",
        "subtitle": "Il Mercante — O Mercador",
        "background": "italian-canals",
        "boss_name": "Il Mercante Oscuro",
        "boss_intro": (
            "Il Mercante Oscuro quer o Sigillo e acredita que você é fraco na língua. "
            "Mostre que ele está errado. "
            "Cada frase que você aprendeu em Venezia é uma vantagem."
        ),
        "reward_name": "Mappa dei Canali",
        "reward_description": (
            "Um mapa detalhado dos canais de Venezia, "
            "com rotas secretas e pontos de encontro marcados. "
            "Prova que você navegou a cidade — e suas intrigas."
        ),
        "phases": PHASES_IT_A2,
    },
    {
        "slug": "it-b1",
        "level": "B1",
        "order": 3,
        "title": "Le Colline della Toscana",
        "subtitle": "Il Maestro — O Mestre",
        "background": "italian-hills",
        "boss_name": "Il Maestro Oscuro",
        "boss_intro": (
            "Il Maestro quer fazer uma troca: o Sigillo pela sua história. "
            "Mas você aprendeu que a língua não se troca — se domina. "
            "Use a precisão que aprendeu nas colinas toscanas."
        ),
        "reward_name": "Codice Antico",
        "reward_description": (
            "Um códice encadernado em couro com registros de viajantes dos últimos séculos. "
            "Dentro, nomes que você reconhece. "
            "A próxima pista está em Napoli."
        ),
        "phases": PHASES_IT_B1,
    },
    {
        "slug": "it-b2",
        "level": "B2",
        "order": 4,
        "title": "Il Vesuvio",
        "subtitle": "Il Barone — O Barão",
        "background": "italian-volcano",
        "boss_name": "Il Barone",
        "boss_intro": (
            "Il Barone controla os portos e esperava que você chegasse. "
            "Mas você também esperava por ele. "
            "Cada argumento que você desenvolveu em Napoli foi para este momento."
        ),
        "reward_name": "Pietra del Vesuvio",
        "reward_description": (
            "Uma pedra negra e quente das encostas do Vesuvio. "
            "Símbolo de quem sobreviveu à cidade mais intensa da Itália — "
            "e saiu mais forte."
        ),
        "phases": PHASES_IT_B2,
    },
    {
        "slug": "it-c1",
        "level": "C1",
        "order": 5,
        "title": "La Grande Roma",
        "subtitle": "L'Imperatore — O Imperador",
        "background": "italian-rome",
        "boss_name": "L'Imperatore",
        "boss_intro": (
            "L'Imperatore acredita que a memória recuperada é sua fraqueza. "
            "Você sabe que é sua maior força. "
            "Toda a jornada — cada cidade, cada aliado, cada palavra aprendida — "
            "foi preparação para este momento no Colosseo."
        ),
        "reward_name": "Corona dell'Eloquenza",
        "reward_description": (
            "A Corona dell'Eloquenza — com inscrições de cada cidade que você atravessou. "
            "Não é um prêmio pelo que você aprendeu. "
            "É o reconhecimento de quem você se tornou."
        ),
        "phases": PHASES_IT_C1,
    },
]


class Command(BaseCommand):
    help = "Seed Italian adventure chapters and phases (all 5 seasons)."

    def handle(self, *args, **options):
        try:
            it = Language.objects.get(code="IT")
        except Language.DoesNotExist:
            self.stdout.write(self.style.ERROR(
                "Language IT not found. Run seed_content_it first."
            ))
            return

        total_phases_created = 0
        total_phases_updated = 0

        for chapter_data in CHAPTERS:
            phases = chapter_data.pop("phases")

            chapter, created = AdventureChapter.objects.update_or_create(
                slug=chapter_data["slug"],
                defaults={**chapter_data, "language": it},
            )
            action = "Criado" if created else "Atualizado"
            self.stdout.write(f"{action} capítulo: {chapter}")

            for phase_data in phases:
                _, phase_created = AdventurePhase.objects.update_or_create(
                    chapter=chapter,
                    number=phase_data["number"],
                    defaults={k: v for k, v in phase_data.items() if k != "number"},
                )
                if phase_created:
                    total_phases_created += 1
                else:
                    total_phases_updated += 1

            chapter_data["phases"] = phases  # restore for idempotency

        self.stdout.write(
            self.style.SUCCESS(
                f"Italian adventure seed concluído: "
                f"{total_phases_created} fases criadas, "
                f"{total_phases_updated} atualizadas "
                f"em {len(CHAPTERS)} capítulos."
            )
        )
