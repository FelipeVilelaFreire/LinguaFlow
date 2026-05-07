import type { AdventureChapter, PhaseType } from "../types/adventure";

/**
 * Mock data — Italian adventure "Il Viandante" — 25 phases per season.
 * T1 = fase 1 = atual (nenhuma fase concluída), T2–T5 = bloqueadas.
 * To switch to real API: remove import in AdventureMapScreen and restore adventureService.listChapters().
 */

function phase(
  id: number,
  number: number,
  title: string,
  intro: string,
  outro: string,
  keywords: string[],
  phraseCount: number,
  isBoss: boolean,
  isCompleted: boolean,
  score: number | null,
  npcName: string = "",
  phaseType: PhaseType = "story",
  chSlug: string = "it-t1",
  completedSections?: number,
): AdventureChapter["phases"][number] {
  return {
    id,
    number,
    title,
    narrative_intro: intro,
    narrative_outro: outro,
    key_words: keywords,
    scenario_slug: `${chSlug}-f${number}`,
    phrase_count: phraseCount,
    section_count: 6,
    completed_sections: completedSections ?? (isCompleted ? 6 : 0),
    phase_type: phaseType,
    npc_name: npcName,
    is_boss: isBoss,
    is_completed: isCompleted,
    score,
  };
}

// ── T1 · A1 — Arrivo al Borgo (25 fases) ─────────────────────────────────────

const T1_PHASES: AdventureChapter["phases"] = [
  phase(101, 1, "O Despertar no Campo",
    "Você acorda sozinho num campo de trigo dourado. Não sabe seu nome, não sabe de onde veio. Uma voz ao longe grita: 'Ehi, straniero! Stai bene?' Você precisa responder.",
    "Você aprendeu as primeiras palavras. O camponês sorri e aponta para o vilarejo ao longe.",
    ["ciao", "buongiorno", "come stai", "bene", "grazie"],
    8, false, false, null, "Giovanni il Contadino"),

  phase(102, 2, "A Entrada no Vilarejo",
    "O Borgo Antico se ergue diante de você: pedras antigas, o cheiro de pão fresco, crianças correndo. A dona de uma taverna se aproxima. 'Cerchi qualcosa?' Você precisa dizer que procura ajuda.",
    "A taverna abriu suas portas para você. Pela primeira vez, alguém te chama pelo nome que você mesmo inventou.",
    ["aiuto", "per favore", "dove", "taverna", "mangiare"],
    8, false, false, null, "Ostessa Carmela"),

  phase(103, 3, "A Primeira Refeição",
    "Fome. Muita fome. O taberneiro mostra o cardápio rabiscado num pedaço de couro. Ele pergunta: 'Cosa vuoi mangiare?' Você precisa pedir algo — qualquer coisa.",
    "O pão com azeite e azeitonas chegou. Nunca uma refeição simples pareceu tão importante.",
    ["pane", "acqua", "vino", "formaggio", "buono"],
    8, false, false, null, "Oste Stefano"),

  phase(104, 4, "O Ferreiro Fala",
    "Na praça central, o ferreiro Marcello marreta com força num pedaço de ferro em brasa. Ele para ao te ver e fala devagar: 'Da dove vieni, amico?' De onde você vem? Essa é a pergunta que você não consegue responder — ainda.",
    "Marcello ri e diz que não importa de onde você veio. O que importa é que está aqui agora.",
    ["da dove", "venire", "nome", "straniero", "amico"],
    10, false, false, null, "Marcello il Fabbro"),

  phase(105, 5, "A Criança Perdida",
    "Uma criança chora perto do poço. Perdeu o gato — 'Il mio gatto è sparito!' — e ninguém está ajudando. Você é o único que se aproxima.",
    "O gato foi encontrado num celeiro de feno. A criança te deu uma moeda velha com a cara de um imperador romano.",
    ["cercare", "trovare", "gatto", "aiutare", "piccolo"],
    10, false, false, null, "Bambina Lucia"),

  phase(106, 6, "O Mercado da Manhã",
    "Ao amanhecer, o mercado toma vida. Vendedores gritam os preços, mulheres bargam por tecidos, um velho conta histórias de guerra. Você precisa comprar mantimentos para a jornada.",
    "Com pão, queijo e um cantil d'água, você se sente mais preparado para o que vem.",
    ["quanto costa", "comprare", "soldi", "mercato", "frutta"],
    10, false, false, null, "Mercante Rinaldo"),

  phase(107, 7, "A Noite na Taverna",
    "À noite, bêbados cantam baladas antigas na taverna. Um homem misterioso no canto te observa há horas. Quando você se aproxima, ele sussurra: 'So chi sei.' Eu sei quem você é.",
    "O homem misterioso partiu antes que você pudesse fazer mais perguntas. Deixou apenas um bilhete com três palavras: 'Vai per Roma.'",
    ["notte", "uomo", "segreto", "sapere", "andare"],
    10, false, false, null, "Uomo Misterioso"),

  phase(108, 8, "A Estrada do Norte",
    "Uma caravana de mercadores parte amanhã para Venezia. O chefe da caravana, Berto, aceita viajantes — mas só se conseguirem se comunicar. 'Parli italiano?' ele pergunta com desconfiança.",
    "Berto apertou sua mão com força. 'Benvenuto nella carovana.' Você vai para Venezia.",
    ["viaggio", "partire", "domani", "insieme", "carovana"],
    10, false, false, null, "Berto il Carovaniere"),

  phase(109, 9, "Segredos do Borgo",
    "Antes de partir, a taverneira te chama em particular. Ela conhecia alguém com sua descrição — anos atrás. Mostra uma medalha com um brasão que você não reconhece, mas seu coração acelera ao ver.",
    "A medalha está no seu bolso agora. Alguma coisa no seu passado está conectada a este lugar.",
    ["memoria", "passato", "conoscere", "storia", "mistero"],
    10, false, false, null, "Ostessa Carmela"),

  phase(110, 10, "O Poço da Praça",
    "O portador d'água Pietro transporta baldes pesados desde o amanhecer. Ele conta cada balde em voz alta — 'uno, due, tre' — e ri ao perceber que você está ouvindo. 'Vuoi imparare a contare?' Quer aprender a contar?",
    "Você chegou até 'venti'. Pietro te presenteou com um cântaro de água fresca e uma lição sobre o tempo que nunca para.",
    ["uno", "due", "tre", "contare", "numero"],
    10, false, false, null, "Pietro il Portatore"),

  phase(111, 11, "A Lavadeira e o Rio",
    "Sofia lava roupa às margens do ribeiro, cantando enquanto estende tecidos coloridos. 'Che bel colore, questo rosso!' Você se aproxima e ela começa a nomear cada cor.",
    "Sofia te ensinou oito cores. 'Adesso il mondo è più colorato per te,' ela disse sorrindo.",
    ["colore", "rosso", "bianco", "nero", "azzurro"],
    10, false, false, null, "Sofia la Lavandaia"),

  phase(112, 12, "A Tempestade",
    "Nuvens negras chegam rápido. 'Pioggia!' grita alguém. O mercado entra em colapso enquanto todos correm para cobrir as mercadorias. Um velho para ao seu lado e olha o céu: 'Brutto tempo. Che freddo.'",
    "A chuva passou tão rápido quanto veio. O velho te disse seu nome: Nonno Aldo. E que o tempo em italiano sempre muda.",
    ["pioggia", "vento", "freddo", "caldo", "cielo"],
    10, false, false, null, "Nonno Aldo"),

  phase(113, 13, "O Florentino",
    "Marco di Firenze chegou ontem. Ele fala italiano rápido demais — você mal entende. Mas ele percebe e desacelera: 'Capisce?' Você precisa responder honestamente e pedir que repita devagar.",
    "Marco ri. 'Non importa — continua a provare.' Ele deixou um bilhete com frases de Firenze.",
    ["capire", "parlare", "lentamente", "ripetere", "provare"],
    10, false, false, null, "Marco di Firenze"),

  phase(114, 14, "A Acusação",
    "O mercante Rinaldo bloqueia seu caminho na praça. 'Non hai pagato!' Você não pagou! Uma acusação falsa — ou não? Você precisa se defender com as palavras que tem.",
    "O borgomastro resolveu a disputa. Rinaldo foi embora resmungando. Palavras podem ser tão poderosas quanto espadas.",
    ["pagare", "denaro", "sbaglio", "scusa", "vero"],
    10, false, false, null, "Mercante Rinaldo"),

  phase(115, 15, "Vozes na Madrugada",
    "Você não consegue dormir. Pelas frestas do quarto, ouve fragmentos de conversa — as vozes de todos que conheceu no Borgo. Giovanni. Carmela. Marcello. Sofia. É como se o vilarejo inteiro estivesse te testando.",
    "Ao amanhecer, você percebe que guardou mais do que imaginava. O Borgo já é seu.",
    ["ripassare", "ricordare", "tutto", "imparato", "bene"],
    12, false, false, null, "", "review"),

  phase(116, 16, "O Monge",
    "Fra' Lorenzo te convida para o scriptorium do mosteiro. Manuscritos antigos cobrem as mesas. Ele aponta para letras: 'Questa si legge così.' Você está aprendendo a soletrar.",
    "Fra' Lorenzo te disse um segredo: uma das letras no manuscrito mais antigo parece seu nome — numa língua que ele não reconhece.",
    ["leggere", "scrivere", "libro", "lettera", "parola"],
    10, false, false, null, "Fra' Lorenzo"),

  phase(117, 17, "A Guarda da Porta",
    "Para sair do Borgo, você precisa passar pela guarda. Guardia Enzo cruza a lança: 'Dove vai? Da solo?' Para onde vai? Sozinho? Você precisa explicar sua rota e motivo.",
    "Enzo ergueu a lança e acenou. 'Buon viaggio, straniero.' A estrada está aberta — por enquanto.",
    ["destra", "sinistra", "dritto", "uscire", "passare"],
    10, false, false, null, "Guardia Enzo"),

  phase(118, 18, "A Filha do Senhor",
    "Uma nota dobrada cai da janela do castelo. Letra fina: 'Ti stanno osservando. Stai attento.' Estão te observando. Tome cuidado. Assina: Fiamma.",
    "Você levantou os olhos — ela já havia sumido. Mas a nota ficou. Alguém dentro do castello sabe quem você é.",
    ["pericolo", "attento", "segreto", "guardare", "nascondersi"],
    10, false, false, null, "Fiamma"),

  phase(119, 19, "O Cavalo Doente",
    "O cavalo de Berto não se levanta esta manhã. 'Il cavallo è malato!' Berto está desesperado — sem o cavalo, a caravana não parte. Você precisa ajudar a encontrar o curandeiro.",
    "O curandeiro chegou e o cavalo melhorou até o anoitecer. Berto te deve um favor. Um favor importante.",
    ["malato", "medico", "guarire", "presto", "aiuto"],
    10, false, false, null, "Berto il Carovaniere"),

  phase(120, 20, "A Noite dos Addii",
    "A última noite no Borgo. Giovanni, Carmela, Marcello, Sofia, Fra' Lorenzo — todos aparecem na taverna, cada um com suas palavras. Uma festa de despedida que você não esperava.",
    "Cada pessoa falou na sua língua. Você entendeu tudo. Isso significou mais do que qualquer medalha.",
    ["addio", "arrivederci", "grazie", "insieme", "ricordare"],
    12, false, false, null, "Tutti", "review"),

  phase(121, 21, "Revisão · Primeiras Palavras",
    "O SRS do Borgo aciona os fragmentos mais antigos da sua memória. Ciao. Buongiorno. Come stai. As primeiras palavras que aprendeu — precisam ser reforçadas antes da partida.",
    "Memória consolidada. Essas palavras agora são reflexos — não precisam mais de esforço.",
    ["ciao", "buongiorno", "come stai", "grazie", "prego"],
    8, false, false, null, "", "review"),

  phase(122, 22, "Revisão · Vida no Borgo",
    "Comida, cores, números, tempo — tudo que aprendeu observando a vida do vilarejo. O revisor implacável do Borgo não deixa nada passar.",
    "Aprovado. Você sabe sobreviver num vilarejo medieval italiano.",
    ["pane", "colore", "numero", "pioggia", "mercato"],
    8, false, false, null, "", "review"),

  phase(123, 23, "Revisão · Encontros e Conflitos",
    "Marcello, Rinaldo, Fiamma, Fra' Lorenzo — cada encontro deixou vocabulário. O revisor reacende cada memória em sequência rápida.",
    "Aprovado. Cada pessoa que você conheceu virou uma palavra que não vai mais esquecer.",
    ["amico", "pericolo", "pagare", "leggere", "destra"],
    8, false, false, null, "", "review"),

  phase(124, 24, "A Noite antes da Batalha",
    "Berto te encontra atrás da taverna. Ele fala baixo: 'Il Condottiero vem amanhã. Se quiser partir, ele vai te parar.' Ele te ensina as palavras que um guerreiro precisa saber.",
    "Você praticou até o amanhecer. Berto disse: 'Sei pronto.' Você está pronto.",
    ["forza", "coraggio", "combattere", "pronto", "vittoria"],
    12, false, false, null, "Berto il Carovaniere"),

  phase(125, 25, "Il Condottiero — Boss",
    "O executor do Borgomastro bloqueia a saída com a armadura reluzente. 'Nessuno lascia il Borgo senza permesso.' Ele vai testar cada palavra que você aprendeu — da saudação mais simples até as palavras de batalha.",
    "Il Condottiero recuou lentamente, o capacete inclinado em respeito. 'Vai per Venezia, straniero.' A estrada está aberta.",
    ["combattere", "vincere", "andare via", "libertà", "potere"],
    15, true, false, null, "Il Condottiero", "boss"),
];

// ── T2 · A2 — Venezia dei Mercanti (25 fases) ────────────────────────────────

const T2_PHASES: AdventureChapter["phases"] = [
  phase(201, 1, "A Chegada pelo Canal",
    "Uma gondola desliza silenciosa pelo Canal Grande ao entardecer. O gondoleiro Matteo canta baixinho enquanto você observa palácios refletidos na água escura. 'Benvenuto a Venezia, straniero,' ele diz sem olhar. 'Questa città ha occhi dappertutto.' Esta cidade tem olhos em todo lugar.",
    "Matteo te deixou no cais de Rialto sem cobrar nada. Isso te preocupou mais do que se tivesse cobrado demais.",
    ["canale", "gondola", "palazzo", "benvenuto", "straniero"],
    10, false, false, null, "Gondoliere Matteo"),

  phase(202, 2, "O Mercado de Rialto",
    "O Mercato di Rialto é um caos glorioso. Especiarias do Oriente, tecidos de Firenze, peixes ainda vivos nos balcões. Messer Alvise grita os preços e ri do seu italiano hesitante. 'Cosa vuoi comprare, forestiero? Parla più forte!'",
    "Você saiu com pão, queijo e a certeza de que Alvise cobrou o dobro. Mas ele te ensinou mais italiano do que cobrou em moedas.",
    ["mercato", "spezie", "comprare", "prezzo", "forestiero"],
    10, false, false, null, "Messer Alvise"),

  phase(203, 3, "A Guilda dos Vidraceiros",
    "A ilha de Murano cheira a areia derretida e fogo. Maestro Giacomo sopra vidro incandescente com maestria incomparável. Ele para e empurra o tubo para você: 'Soffia — ma piano, piano.' Sopre — mas devagar, devagar. É um teste ou um convite?",
    "'I difetti la rendono unica,' Giacomo disse guardando a esfera imperfeita que você criou. Os defeitos a tornam única. Ele a colocou numa prateleira de honra.",
    ["vetro", "fuoco", "soffiare", "artigiano", "isola"],
    10, false, false, null, "Maestro Giacomo"),

  phase(204, 4, "O Baile das Máscaras",
    "Uma máscara dourada em forma de sol cobre seu rosto. A Contessa Isabella se inclina e sussurra: 'Qui tutti hanno un segreto. Anche tu.' Todos têm um segredo aqui — você também. Para dançar neste baile é preciso falar de aparências, verdades e mentiras.",
    "A Contessa desapareceu antes que você pudesse agradecê-la. Mas há um bilhete na sua manga: 'Fidati di Matteo. Non ti abbandonerà.' Confie em Matteo.",
    ["maschera", "ballo", "segreto", "nascondersi", "fidarsi"],
    10, false, false, null, "Contessa Isabella"),

  phase(205, 5, "A Biblioteca Secreta",
    "Uma porta oculta atrás de um tapiz leva à biblioteca privada do Doge. Fra' Benedetto cataloga manuscritos com mãos cuidadosas. Ele te olha por cima dos óculos: 'Lei sa leggere il latino? O almeno l'italiano antico?' Você sabe ler latim? Ou ao menos italiano antigo?",
    "Fra' Benedetto não respondeu nada sobre o brasão. Mas marcou uma página com uma pena antes de sair — e isso não foi por acidente.",
    ["biblioteca", "manoscritto", "leggere", "antico", "pagina"],
    10, false, false, null, "Fra' Benedetto"),

  phase(206, 6, "Revisão · Chegada a Venezia",
    "O sussurro dos canais traz de volta cada momento. Gondola. Mercato. Murano. Il ballo. La biblioteca. As palavras se sobrepõem como reflexos na água verde do canal.",
    "Venezia já está em você. Mas as palavras importantes precisam ser fixadas antes que a maré as carregue.",
    ["canale", "maschera", "vetro", "mercato", "segreto"],
    8, false, false, null, "", "review"),

  phase(207, 7, "O Espião Florentino",
    "Ele te segue desde Rialto — você percebeu há dois dias mas ficou calado. Agora Lorenzo il Sottile senta à sua mesa e sorri: 'Sei meglio di quanto pensassi.' Você é melhor do que eu pensava. Um espião ou um aliado? Você precisa descobrir sem revelar o que sabe.",
    "Lorenzo revelou apenas que serve 'interessi fiorentini'. E que o Sigillo del Borgo que você carrega vale muito mais do que imagina.",
    ["spia", "seguire", "scoprire", "fiducia", "pericoloso"],
    10, false, false, null, "Lorenzo il Sottile"),

  phase(208, 8, "A Gondola Noturna",
    "Às duas da madrugada, Dario aparece no seu cais. 'Ho qualcosa da mostrarti. Vieni.' Tenho algo para te mostrar. Uma gondola sem luz desce por um canal tão estreito que as paredes quase se tocam. Você sente que pode ser uma armadilha — mas sente também que não tem escolha.",
    "Dario te mostrou um depósito secreto embaixo de um palácio. Caixas com o mesmo brasão da sua medalha. Alguém está procurando algo — ou alguém.",
    ["notte", "buio", "nascosto", "mostrare", "paura"],
    10, false, false, null, "Gondoliere Dario"),

  phase(209, 9, "O Palácio dos Doges",
    "O Palazzo Ducale resplandece ao sol da manhã. O Capitão Marco cruza a lança na entrada: 'Il Doge non riceve stranieri senza presentazione formale.' O Doge não recebe estranhos sem apresentação formal. Você precisa convencê-lo ou encontrar outra entrada.",
    "Marco te deixou passar pela entrada dos escribas. 'Dieci minuti,' ele disse. Dez minutos. Você aproveitou cada segundo.",
    ["palazzo", "guardia", "permesso", "entrare", "formale"],
    10, false, false, null, "Capitano Marco"),

  phase(210, 10, "A Trança de Vidro",
    "Chiara fabrica colares de vidro para a Contessa, cantando enquanto trabalha. Cada cor tem um nome e uma superstição veneziana. Ela te empurra um colar e pergunta: 'Dimmi — che colore è questo?' Diga-me — que cor é esta?",
    "'Azzurro come il Canal Grande,' você respondeu. Chiara sorriu: 'Esatto.' Ela embrulhou o colar azul para você levar.",
    ["collana", "colore", "azzurro", "regalo", "chiaro"],
    10, false, false, null, "Chiara la Muranesa"),

  phase(211, 11, "O Canal dos Assassinos",
    "Vincenzo te encontra nervoso à beira do Rio degli Assassini. 'Stanotte han trovato un corpo nel canale.' Esta noite encontraram um corpo. O morto carregava um documento com seu nome. Você precisa descobrir quem matou — antes de ser o próximo.",
    "O assassino fugiu pelos telhados. Mas Vincenzo confirmou: o documento era falso. Alguém está construindo uma história sobre você.",
    ["pericolo", "morto", "canale", "scappare", "documento"],
    10, false, false, null, "Sbirro Vincenzo"),

  phase(212, 12, "Revisão · A Cidade das Águas",
    "Os canais espelham tudo que você viveu: o espião, o assassino, a gondola noturna, o palácio. Venezia não perdoa quem esquece.",
    "Memória consolidada. Venezia registrou tudo — e você também.",
    ["spia", "guardia", "notte", "palazzo", "canale"],
    8, false, false, null, "", "review"),

  phase(213, 13, "A Festa dei Santi",
    "A cidade inteira parou para a Festa dei Santi. Incenso, procissões, velas. O velho Piero te puxa para a fila e vai sussurrando os nomes de cada santo que passa. 'Sai pregare in italiano?' Você sabe rezar em italiano?",
    "Você aprendeu mais palavras de tempo e calendário naquela procissão do que em duas semanas. Piero sorriu: 'La fede insegna molto.'",
    ["festa", "santo", "chiesa", "pregare", "candela"],
    10, false, false, null, "Nonno Piero"),

  phase(214, 14, "A Jovem Pintora",
    "Lena pinta em cima de uma ponte, ignorando todos ao redor. Sua tela mostra o Canal Grande — mas com um detalhe que não existe na realidade: um homem com o rosto coberto. 'È lei,' ela diz sem olhar. 'Non so chi sia — qualcuno mi ha chiesto di dipingere questo.' Não sei quem é — mas alguém me pediu.",
    "O nome de quem encomendou estava raspado. Mas Lena lembrou um detalhe: ele falava italiano com sotaque romano.",
    ["dipingere", "quadro", "artista", "misterioso", "ritratto"],
    10, false, false, null, "Lena la Pittrice"),

  phase(215, 15, "O Nobre Endividado",
    "Giovanni Dandolo perdeu tudo no jogo — palácio, reputação e família. Ele te aborda no cais com olhos vermelhos: 'Ho bisogno di un favore urgente.' Preciso de um favor urgente. Em troca de informações sobre o brasão, ele quer ajuda para recuperar uma caixa roubada.",
    "A caixa estava vazia. Mas Dandolo, como prometido, te disse onde o brasão foi visto pela última vez: nos arquivos secretos do Arsenal.",
    ["nobile", "debito", "favore", "promessa", "archivio"],
    10, false, false, null, "Nobile Dandolo"),

  phase(216, 16, "A Carta Cifrada",
    "Fra' Benedetto aparece na sua janela de madrugada, apavorado. Ele te entrega uma carta com símbolos estranhos: 'Non riesco a decifrare questo — ma tu sì, ne sono certo.' Não consigo decifrar — mas você consegue, tenho certeza. A carta mistura italiano com latim e parece falar sobre você.",
    "A carta dizia que 'Il Viandante' é o nome de uma missão — não de uma pessoa. Missão de quê, ainda não está claro.",
    ["lettera", "codice", "decifrare", "missione", "cifra"],
    10, false, false, null, "Fra' Benedetto"),

  phase(217, 17, "O Fogo no Arsenal",
    "O Arsenal de Venezia — a maior fábrica de navios do mundo — está em chamas. Mastro Calafato grita ordens desesperadas: 'Aiuto! Portate secchi d'acqua! Veloce, veloce!' Você é o único livre para agir.",
    "O fogo foi controlado. Calafato apertou sua mão com força: 'Hai rischiato la vita per noi.' Dentro do Arsenal queimado: o mesmo brasão, gravado num barco inacabado.",
    ["fuoco", "arsenale", "aiuto", "rischio", "secchio"],
    10, false, false, null, "Mastro Calafato"),

  phase(218, 18, "Revisão · Intrigas em Venezia",
    "Fra' Benedetto. Dandolo. Lena. O fogo. A carta cifrada. Os fios começam a se conectar — mas o revisor de Venezia não vai deixar você avançar sem fixar cada nó.",
    "Os fios viraram uma rede. Você está no centro dela — queira ou não.",
    ["spia", "lettera", "missione", "fuoco", "nobile"],
    8, false, false, null, "", "review"),

  phase(219, 19, "A Testemunha Muda",
    "Crippa não fala — nunca falou. Mas comunica com gestos precisos e um caderninho rabiscado. Ele viu quem ateou fogo ao Arsenal. Para entender o que Crippa viu, você precisa aprender a se comunicar além das palavras.",
    "O desenho de Crippa mostrava um homem de capuz — com um detalhe: luvas brancas. O sinal da Contessa Isabella.",
    ["silenzio", "gesto", "testimone", "disegno", "capire"],
    10, false, false, null, "Crippa il Muto"),

  phase(220, 20, "O Mercador Árabe",
    "Karim chegou do Egito com especiarias e informações. Ele fala italiano com sotaque denso e ri da sua pronúncia. 'Siamo tutti stranieri qui, amico.' Todos somos estrangeiros aqui. Ele tem informações sobre o brasão — mas quer praticar italiano primeiro.",
    "'Vai a Roma, amico,' Karim disse por fim. 'La risposta è lì.' A resposta está em Roma. Ele pagou a conta sem que você pedisse.",
    ["straniero", "mercante", "spezie", "risposta", "lontano"],
    10, false, false, null, "Karim al-Rashid"),

  phase(221, 21, "A Traição do Gondoleiro",
    "Dario te encontra perto do Arsenal — mas desta vez com guardas da Contessa atrás dele. 'Mi dispiace tanto, amico.' Me desculpe muito. Ele te vendeu. As palavras que você precisa agora são de fuga, defesa e sobrevivência.",
    "Você escapou pelos canais secundários. Dario desapareceu. A Contessa quer o Sigillo del Borgo — e agora tem seu rastro.",
    ["tradimento", "scappare", "guardia", "prigione", "libertà"],
    10, false, false, null, "Gondoliere Dario"),

  phase(222, 22, "Revisão · O Conflito Final",
    "Traição. Fuga pelo canal escuro. Cada palavra que você aprendeu em Venezia foi testada esta noite. O revisor final não tem misericórdia.",
    "Você passou. Mas o teste real vem agora.",
    ["tradimento", "libertà", "segreto", "scappare", "missione"],
    8, false, false, null, "", "review"),

  phase(223, 23, "O Julgamento no Palácio",
    "Você foi capturado. O julgamento é rápido — Venezia não perde tempo com estrangeiros. O Avvocato Sebastiano sussurra: 'Ho bisogno che lei dica esattamente quello che le dico.' Preciso que diga exatamente o que eu disser. Um julgamento num idioma que você aprendeu mês a mês — é o teste supremo.",
    "O Doge ouviu. Não te libertou completamente — concedeu 'libertà condizionata.' Liberdade condicional. Suficiente para fugir.",
    ["tribunale", "giustizia", "difesa", "giudice", "innocente"],
    10, false, false, null, "Avvocato Sebastiano"),

  phase(224, 24, "A Fuga pelos Telhados",
    "Matteo estava esperando no telhado — ele sabia desde o começo. 'Ti ho aspettato,' disse sorrindo. Os telhados de Venezia formam uma cidade acima da cidade, e você precisa cruzá-la inteira sem ser visto. Cada passo errado é uma queda nos canais.",
    "A gondola esperava no canal externo. Matteo remou sem dizer nada. Quando o sol surgiu, Venezia estava atrás de você. À frente: a Toscana.",
    ["tetto", "correre", "nascondersi", "libertà", "partire"],
    10, false, false, null, "Gondoliere Matteo"),

  phase(225, 25, "Il Leone Alato — Boss",
    "A estátua do Leão Alado de São Marcos não é uma estátua — esta noite os olhos se movem. 'Nessuno lascia Venezia senza rispondere delle sue azioni.' Ninguém sai sem responder por suas ações. Cada frase que você aprendeu aqui será testada. O Leão conhece tudo que aconteceu.",
    "'Hai parlato la nostra lingua. Sei libero.' Você falou nossa língua. Está livre. Nos seus bolsos agora: a Mappa di Venezia, com os canais secretos para a Toscana.",
    ["leone", "alato", "onore", "libertà", "venezia"],
    15, true, false, null, "Il Leone Alato", "boss"),
];

// ── T3 · B1 — La Toscana dei Medici (25 fases) ───────────────────────────────

const T3_TITLES = [
  "As Colinas de Cipresso", "A Villa dos Médici", "O Ateliê do Pintor",
  "A Conspiração", "O Torneio de Poesia", "Revisão · Chegada à Toscana",
  "O Veneno no Vinho", "A Alquimista de Siena", "O Trovador Cego",
  "O Jardim Secreto", "A Carta de Lorenzo", "Revisão · Arte e Poder",
  "O Mercenário Alemão", "A Jovem Freira", "O Palácio Abandonado",
  "A Acusação de Bruxaria", "A Fuga para Siena", "Revisão · Os Médici",
  "O Castelo de Pedra", "A Traição", "O Duelo de Palavras",
  "Revisão · A Grande Decisão", "O Tribunal de Florença",
  "O Último Aliado", "Il Magnifico — Boss",
];

const T3_PHASES: AdventureChapter["phases"] = Array.from({ length: 25 }, (_, i) => {
  const title = T3_TITLES[i];
  const isBoss = i === 24;
  const isReview = title.startsWith("Revisão");
  const type: PhaseType = isBoss ? "boss" : isReview ? "review" : "story";
  return phase(
    300 + i + 1, i + 1, title,
    "Os campos dourados da Toscana escondem intrigas entre nobres e artistas...",
    "A jornada continua.",
    [], isBoss ? 15 : isReview ? 8 : 10, isBoss, false, null,
    "", type, "it-t3",
  );
});

// ── T4 · B2 — Napoli e il Vesuvio (25 fases) ─────────────────────────────────

const T4_TITLES = [
  "O Porto Vulcânico", "O Mercato di Spaccanapoli", "A Camorra e o Segredo",
  "O Vilarejo nas Cinzas", "A Pesca Noturna", "Revisão · Chegada a Napoli",
  "Os Catacumbas de San Gennaro", "O Rei sem Coroa", "A Dançarina de Tarantella",
  "O Bairro Espanhol", "O Presepe Vivo", "Revisão · A Cidade Viva",
  "A Erupção Menor", "O Capitão do Porto", "A Criança da Via Toledo",
  "O Monge do Duomo", "O Último Barco", "Revisão · Perigos e Promessas",
  "A Noite de San Gennaro", "O Criminoso Arrependido", "A Decisão Final",
  "Revisão · Napoli Eterna", "A Subida ao Vesúvio",
  "A Cratera", "Il Vesuvio — Boss",
];

const T4_PHASES: AdventureChapter["phases"] = Array.from({ length: 25 }, (_, i) => {
  const title = T4_TITLES[i];
  const isBoss = i === 24;
  const isReview = title.startsWith("Revisão");
  const type: PhaseType = isBoss ? "boss" : isReview ? "review" : "story";
  return phase(
    400 + i + 1, i + 1, title,
    "Nápoles pulsa com vida, perigo e o calor do vulcão adormecido...",
    "A jornada continua.",
    [], isBoss ? 15 : isReview ? 8 : 10, isBoss, false, null,
    "", type, "it-t4",
  );
});

// ── T5 · C1 — Roma Aeterna (25 fases) ────────────────────────────────────────

const T5_TITLES = [
  "A Entrada pela Via Appia", "O Colosseo ao Amanhecer", "O Senado e a Sombra",
  "As Catacumbas", "O Arquivo Secreto", "Revisão · Chegada a Roma",
  "A Verdade sobre Il Viandante", "O Gladiador Aposentado", "A Sibila do Palatino",
  "O Embaixador Veneziano", "A Conspiração dos Senadores", "Revisão · Poder e Memória",
  "Os Jardins de Nero", "A Guardiã do Fórum", "O Manuscrito Perdido",
  "O Interrogatório", "A Fuga pelo Subterrâneo", "Revisão · Identidade",
  "O Confronto no Capitólio", "O Guardião Eterno", "A Verdade Revelada",
  "Revisão · A Grande Prova", "Il Ritorno",
  "A Coroação", "L'Imperatore — Boss Final",
];

const T5_PHASES: AdventureChapter["phases"] = Array.from({ length: 25 }, (_, i) => {
  const title = T5_TITLES[i];
  const isBoss = i === 24;
  const isReview = title.startsWith("Revisão");
  const type: PhaseType = isBoss ? "boss" : isReview ? "review" : "story";
  return phase(
    500 + i + 1, i + 1, title,
    "Roma. A cidade eterna. Aqui sua identidade será revelada — ou destruída para sempre...",
    "A jornada continua.",
    [], isBoss ? 15 : isReview ? 8 : 10, isBoss, false, null,
    "", type, "it-t5",
  );
});

// ── Export ─────────────────────────────────────────────────────────────────────

export const ADVENTURE_IT_MOCK: AdventureChapter[] = [
  {
    id: 1,
    slug: "it-a1-borgo",
    language_code: "IT",
    level: "T1",
    order: 1,
    title: "Arrivo al Borgo",
    subtitle: "Um viajante sem memória chega a um vilarejo medieval italiano",
    background: "medieval_village",
    boss_name: "Il Condottiero",
    boss_intro: "O executor do Borgomastro nunca deixa ninguém partir sem permissão.",
    reward_name: "Sigillo del Borgo",
    reward_description: "O selo antigo que prova que você sobreviveu ao Borgo Antico. Abre portas em Venezia.",
    phases: T1_PHASES,
    progress: { current_phase: 1, reward_unlocked: false, started_at: "2025-01-01", completed_at: null },
  },
  {
    id: 2,
    slug: "it-a2-venezia",
    language_code: "IT",
    level: "T2",
    order: 2,
    title: "Venezia dei Mercanti",
    subtitle: "Entre canais e máscaras, os segredos da sua identidade emergem",
    background: "venice",
    boss_name: "Il Leone Alato",
    boss_intro: "O guardião de Venezia não perdoa traidores — nem viajantes sem documentos.",
    reward_name: "Mappa di Venezia",
    reward_description: "Um mapa detalhado dos canais secretos. Indispensável para atravessar a Toscana.",
    phases: T2_PHASES,
    progress: null,
  },
  {
    id: 3,
    slug: "it-b1-toscana",
    language_code: "IT",
    level: "T3",
    order: 3,
    title: "La Toscana dei Medici",
    subtitle: "Arte, poder e veneno na corte dos Médici",
    background: "tuscany",
    boss_name: "Il Magnifico",
    boss_intro: "Lorenzo de' Medici é generoso com amigos e implacável com inimigos.",
    reward_name: "Codice dei Medici",
    reward_description: "Um manuscrito cifrado com segredos das famílias nobres da Itália.",
    phases: T3_PHASES,
    progress: null,
  },
  {
    id: 4,
    slug: "it-b2-napoli",
    language_code: "IT",
    level: "T4",
    order: 4,
    title: "Napoli e il Vesuvio",
    subtitle: "A cidade mais viva da Itália guarda a maior ameaça",
    background: "naples",
    boss_name: "Il Vesuvio",
    boss_intro: "Não é um homem. É a montanha de fogo que acorda quando o idioma é desrespeitado.",
    reward_name: "Pietra del Fuoco",
    reward_description: "Um fragmento de lava solidificada do Vesúvio. Dizem que protege quem a carrega.",
    phases: T4_PHASES,
    progress: null,
  },
  {
    id: 5,
    slug: "it-c1-roma",
    language_code: "IT",
    level: "T5",
    order: 5,
    title: "Roma Aeterna",
    subtitle: "A verdade sobre Il Viandante está enterrada nas ruínas de Roma",
    background: "rome",
    boss_name: "L'Imperatore",
    boss_intro: "O último guardião da verdade. Ele sabe quem você é. Você precisa provar que merece saber também.",
    reward_name: "Corona di Alloro",
    reward_description: "A coroa de louros do verdadeiro viajante. Quem a usa domina o italiano como um romano.",
    phases: T5_PHASES,
    progress: null,
  },
];
