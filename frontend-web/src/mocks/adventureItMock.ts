import type { AdventureChapter, PhaseType } from "../types/adventure";

/**
 * Mock data — Italian adventure "Il Viandante" — 25 phases per season.
 * T1 = 3 fases concluídas (fase 4 = atual), T2–T5 = bloqueadas.
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
    8, false, true, 7, "Giovanni il Contadino"),

  phase(102, 2, "A Entrada no Vilarejo",
    "O Borgo Antico se ergue diante de você: pedras antigas, o cheiro de pão fresco, crianças correndo. A dona de uma taverna se aproxima. 'Cerchi qualcosa?' Você precisa dizer que procura ajuda.",
    "A taverna abriu suas portas para você. Pela primeira vez, alguém te chama pelo nome que você mesmo inventou.",
    ["aiuto", "per favore", "dove", "taverna", "mangiare"],
    8, false, true, 6, "Ostessa Carmela"),

  phase(103, 3, "A Primeira Refeição",
    "Fome. Muita fome. O taberneiro mostra o cardápio rabiscado num pedaço de couro. Ele pergunta: 'Cosa vuoi mangiare?' Você precisa pedir algo — qualquer coisa.",
    "O pão com azeite e azeitonas chegou. Nunca uma refeição simples pareceu tão importante.",
    ["pane", "acqua", "vino", "formaggio", "buono"],
    8, false, true, 8, "Oste Stefano"),

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

const T2_TITLES = [
  "A Chegada pelo Canal", "O Mercado de Rialto", "A Guilda dos Vidraceiros",
  "O Baile das Máscaras", "A Biblioteca Secreta", "Revisão · Chegada a Venezia",
  "O Espião Florentino", "A Gondola Noturna", "O Palácio dos Doges",
  "A Trança de Vidro", "O Canal dos Assassinos", "Revisão · A Cidade das Águas",
  "A Festa dei Santi", "A Jovem Pintora", "O Nobre Endividado",
  "A Carta Cifrada", "O Fogo no Arsenal", "Revisão · Intrigas em Venezia",
  "A Testemunha Muda", "O Mercador Árabe", "A Traição do Gondoleiro",
  "Revisão · O Conflito Final", "O Julgamento no Palácio",
  "A Fuga pelos Telhados", "Il Leone Alato — Boss",
];

const T2_PHASES: AdventureChapter["phases"] = Array.from({ length: 25 }, (_, i) => {
  const title = T2_TITLES[i];
  const isBoss = i === 24;
  const isReview = title.startsWith("Revisão");
  const type: PhaseType = isBoss ? "boss" : isReview ? "review" : "story";
  return phase(
    200 + i + 1, i + 1, title,
    "Uma nova fase aguarda em Venezia...",
    "Mais um passo na jornada.",
    [], isBoss ? 15 : isReview ? 8 : 10, isBoss, false, null,
    "", type, "it-t2",
  );
});

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
    progress: { current_phase: 4, reward_unlocked: false, started_at: "2025-01-01", completed_at: null },
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
