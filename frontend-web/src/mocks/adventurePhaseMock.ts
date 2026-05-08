import type { PhaseSection } from "../types/sections";

// ── Phase 1 — "O Despertar no Borgo" ─────────────────────────────────────────
//
// Vocabulary (with word_id):
//   it_forestiero · it_contadino · it_bene · it_mi_chiamo · it_amico
//   it_ciao · it_buongiorno · it_come_stai · it_grazie · it_straniero
//   it_piacere · it_benvenuto
//
// Grammar: chiamarsi reflexivo (mi/ti/si chiamo/chiami/chiama)
//
// Tier rule: all words start at "bronze" — first exposure in Phase 1.
// Exercises that test a specific word carry word_id + tier.
// Grammar and contextual deduction exercises carry no word_id.
//
// Story arc:
//   S1 — Você chega. Giovanni te aborda na entrada do borgo.
//   S2 — Giovanni te leva a passear. Você pratica com os moradores.
//   S3 — Vocês chegam ao mercado. Você conhece Lucia.
//   S4 — Na praça central, Giovanni explica 'mi chiamo' e o reflexivo.
//   S5 — Você encontra Marco e Sofia. Apresentações na prática.
//   S6 — Portão do centro: o guarda testa tudo que você aprendeu.
//
// 6 sections · 51 exercises:
//   1 narrativa           —  5 ex.
//   2 revisao_srs         — 12 ex.
//   3 pratica_aplicada    — 10 ex.
//   4 gramatica_narrativa —  8 ex.
//   5 reforco             —  6 ex.
//   6 obstaculo           — 10 ex. gated

const PHASE_1_SECTIONS: PhaseSection[] = [

  // ── 1 · NARRATIVA ──────────────────────────────────────────────────────────
  {
    type: "narrativa",
    beats: [
      { kind: "scene",
        text: "🏘️  Entrada do Borgo · Manhã cedo · T1 Ep.1" },
      { kind: "narrative",
        text: "O portão de madeira range atrás de você. Você está dentro do vilarejo.\n\nAs ruas de paralelepípedos se ramificam à sua frente. Crianças correm entre casas de pedra. O cheiro de pão assado se mistura com o de ervas frescas. Vozes por todo lado — rápidas, musicais, completamente incompreensíveis.\n\nVocê não sabe seu nome. Não sabe de onde veio. Sabe apenas que o guarda deixou você entrar — e que agora precisa descobrir onde está." },
      { kind: "narrative",
        text: "Um homem de mãos calejadas e avental manchado de terra te observa de trás de uma banca de legumes. Seu olhar é curioso, não ameaçador. Ele larga uma abóbora e caminha na sua direção." },
      { kind: "npc",    npc: "Giovanni il Contadino", line: "Ehi, forestiero! Sei appena arrivato?" },
      { kind: "player", text: "Você olha para ele sem entender uma única palavra. As sílabas soam bonitas — como uma canção que você quase conhece, mas não." },
      { kind: "npc",    npc: "Giovanni il Contadino", line: "Ah... non capisci l'italiano, vero? Non parli la nostra lingua." },
      { kind: "player", text: "Você balança a cabeça. Giovanni coça a barba, pensativo. Então ri — não com deboche, mas com a simpatia de quem já viu essa cena antes." },
      { kind: "npc",    npc: "Giovanni il Contadino", line: "Va bene, va bene! Io mi chiamo Giovanni. Sono un contadino — capisce? Un farmer." },
      { kind: "npc",    npc: "Giovanni il Contadino", line: "Siediti. Io ti insegno le prime parole. Parola per parola, amico mio." },
      { kind: "narrative",
        text: "Você se senta no banquinho que ele oferece. Em algum lugar nesse vilarejo há respostas para as suas perguntas. Por enquanto — há Giovanni, e as palavras que ele está prestes a te ensinar." },
    ],
    exercises: [
      {
        kind: "multiple_choice",
        word_id: "it_forestiero",
        tier: "bronze",
        question: "Giovanni te chamou de 'forestiero' assim que chegou. Você acabou de entrar vindo de fora. O que essa palavra significa?",
        options: [
          { id: "a", text: "Fazendeiro" },
          { id: "b", text: "Forasteiro" },
          { id: "c", text: "Amigo" },
          { id: "d", text: "Guarda" },
        ],
        correct: "b",
        explanation: "Forestiero = forasteiro. Chegou de fora — o contexto já dizia tudo.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_contadino",
        tier: "bronze",
        question: "Giovanni tem mãos calejadas, avental manchado de terra e uma banca de legumes. Que tipo de pessoa é um 'contadino'?",
        options: [
          { id: "a", text: "Um comerciante de tecidos" },
          { id: "b", text: "Um guarda da cidade" },
          { id: "c", text: "Um fazendeiro" },
          { id: "d", text: "Um curandeiro" },
        ],
        correct: "c",
        explanation: "Contadino = fazendeiro. As mãos, a terra, os legumes — tudo confirma.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_bene",
        tier: "bronze",
        question: "Você não entendeu nada — e Giovanni sorriu, disse 'Va bene, va bene!' e se sentou com você sem julgamento. O que 'bene' provavelmente significa?",
        options: [
          { id: "a", text: "Não, pare" },
          { id: "b", text: "Cuidado" },
          { id: "c", text: "Bem / tudo certo" },
          { id: "d", text: "Vamos embora" },
        ],
        correct: "c",
        explanation: "Bene = bem. 'Va bene' = tudo bem. Ele repetiu duas vezes para te tranquilizar.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_mi_chiamo",
        tier: "bronze",
        question: "Giovanni colocou a mão no peito e disse 'Io mi chiamo Giovanni.' O que ele estava fazendo?",
        options: [
          { id: "a", text: "Perguntando o seu nome" },
          { id: "b", text: "Se apresentando" },
          { id: "c", text: "Pedindo para você ir embora" },
          { id: "d", text: "Chamando alguém ao longe" },
        ],
        correct: "b",
        explanation: "'Mi chiamo' = meu nome é. A mão no peito é universal — você acabou de aprender a frase mais importante.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_amico",
        tier: "bronze",
        question: "Giovanni sorriu e disse 'Parola per parola, amico mio' — sem pressa, sem julgamento. O que 'amico' significa?",
        options: [
          { id: "a", text: "Mestre" },
          { id: "b", text: "Inimigo" },
          { id: "c", text: "Palavra" },
          { id: "d", text: "Amigo" },
        ],
        correct: "d",
        explanation: "Amico = amigo. O sorriso, a paciência, o tom — tudo confirma que ele está do seu lado.",
      },
    ],
  },

  // ── 2 · REVISÃO SRS — aquecimento contextual (primeira fase de T1) ──────────
  // Giovanni te leva a passear pelo borgo. Todas as 12 palavras são testadas no tier atual.
  {
    type: "revisao_srs",
    steps: [
      {
        kind: "narrative",
        text: "Giovanni se levanta e gesticula para você seguir. Caminhando pelas ruas de pedra, ele vai apontando para os moradores que passam — e testando se você lembrou das palavras do início.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Allora — quando incontri qualcuno, cosa dici?",
        translation: "Então — quando você encontra alguém, o que diz?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_ciao",
        tier: "bronze",
        question: "Um vizinho de Giovanni passa e te olha com um sorriso. O que você diz?",
        options: [
          { id: "a", text: "Grazie!" },
          { id: "b", text: "Ciao!" },
          { id: "c", text: "Straniero!" },
          { id: "d", text: "Contadino!" },
        ],
        correct: "b",
        explanation: "Ciao! — saudação informal, serve para olá e tchau. A mais natural ao encontrar alguém.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Bene! E di mattina — come si saluta più formalmente?",
        translation: "Bem! E de manhã — como se cumprimenta de forma mais formal?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_buongiorno",
        tier: "bronze",
        question: "Giovanni aponta para o sol que acabou de subir. Qual é a saudação mais adequada para essa hora?",
        options: [
          { id: "a", text: "Buonanotte!" },
          { id: "b", text: "Buonasera!" },
          { id: "c", text: "Buongiorno!" },
          { id: "d", text: "Arrivederci!" },
        ],
        correct: "c",
        explanation: "Buongiorno = bom dia. 'Buon' (bom) + 'giorno' (dia) — mais formal que ciao.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Perfetto! Ora io ti chiedo: come stai?",
        translation: "Perfeito! Agora eu te pergunto: como vai você?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_come_stai",
        tier: "bronze",
        question: "Giovanni perguntou 'come stai?'. O que ele quer saber?",
        options: [
          { id: "a", text: "Onde você mora" },
          { id: "b", text: "Como vai você" },
          { id: "c", text: "Qual é o seu nome" },
          { id: "d", text: "De onde você veio" },
        ],
        correct: "b",
        explanation: "'Come stai?' = como vai você? A pergunta mais comum depois do ciao.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_bene",
        tier: "bronze",
        question: "Giovanni perguntou 'Come stai?'. Como você responde que está bem?",
        options: [
          { id: "a", text: "Ciao!" },
          { id: "b", text: "Buongiorno!" },
          { id: "c", text: "Bene, grazie!" },
          { id: "d", text: "Non capisco." },
        ],
        correct: "c",
        explanation: "'Bene, grazie!' — bem, obrigado/a! A resposta natural para come stai?",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Bravo! E 'grazie' — sai cosa significa?",
        translation: "Bravo! E 'grazie' — você sabe o que significa?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_grazie",
        tier: "bronze",
        question: "Giovanni usou 'grazie' para te elogiar. O que essa palavra significa?",
        options: [
          { id: "a", text: "Por favor" },
          { id: "b", text: "De nada" },
          { id: "c", text: "Obrigado/a" },
          { id: "d", text: "Com licença" },
        ],
        correct: "c",
        explanation: "Grazie = obrigado/a. Curta, musical e indispensável.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "E tu — come ti chiami? Dimmi!",
        translation: "E você — como se chama? Me diga!",
      },
      {
        kind: "multiple_choice",
        word_id: "it_mi_chiamo",
        tier: "bronze",
        question: "Giovanni quer saber seu nome. Como você responde?",
        options: [
          { id: "a", text: "Bene, grazie!" },
          { id: "b", text: "Ciao, Giovanni!" },
          { id: "c", text: "Mi chiamo [nome]." },
          { id: "d", text: "Sono forestiero." },
        ],
        correct: "c",
        explanation: "'Mi chiamo + nome' — você aprendeu isso no começo. Hora de usar.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Io ti ho chiamato 'forestiero' e anche 'straniero' — sai la differenza?",
        translation: "Eu te chamei de 'forestiero' e também de 'straniero' — você sabe a diferença?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_straniero",
        tier: "bronze",
        question: "Giovanni usou 'forestiero' e 'straniero' para falar de você. O que essas palavras têm em comum?",
        options: [
          { id: "a", text: "São opostos — uma é elogio, outra é ofensa" },
          { id: "b", text: "As duas significam forasteiro/estrangeiro — forestiero é regional" },
          { id: "c", text: "Forestiero = homem, straniero = mulher" },
          { id: "d", text: "Straniero é plural de forestiero" },
        ],
        correct: "b",
        explanation: "Forestiero (regional) e straniero (padrão) têm o mesmo significado — forasteiro/estrangeiro.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "E quando vai embora — come si dice?",
        translation: "E quando vai embora — como se diz?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_ciao",
        tier: "bronze",
        question: "Você precisa se afastar de Giovanni por um momento. O que diz?",
        options: [
          { id: "a", text: "Grazie!" },
          { id: "b", text: "Bene!" },
          { id: "c", text: "Ciao!" },
          { id: "d", text: "Come stai?" },
        ],
        correct: "c",
        explanation: "Ciao! serve tanto para cumprimentar quanto para se despedir — informal e natural.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_buongiorno",
        tier: "bronze",
        question: "Uma senhora idosa sorri para você na rua. Você quer cumprimentá-la. O que diz?",
        options: [
          { id: "a", text: "Ciao!" },
          { id: "b", text: "Buongiorno!" },
          { id: "c", text: "Come stai?" },
          { id: "d", text: "Straniero!" },
        ],
        correct: "b",
        explanation: "Buongiorno! é mais respeitoso que ciao — ideal para adultos que você não conhece.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Sto bene, grazie! — è la risposta completa. Non solo 'bene' — 'sto bene'.",
        translation: "Estou bem, obrigado/a! — é a resposta completa. Não apenas 'bene' — 'sto bene'.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_bene",
        tier: "bronze",
        question: "Giovanni corrigiu: a resposta completa não é só 'bene', é 'sto bene, grazie!' O que 'sto' acrescenta?",
        options: [
          { id: "a", text: "Nada — é apenas uma formalidade" },
          { id: "b", text: "Indica estado: 'eu estou' bem, não só 'bem'" },
          { id: "c", text: "É o plural de bene" },
          { id: "d", text: "É uma forma regional de 'sei'" },
        ],
        correct: "b",
        explanation: "'Sto' vem de 'stare' = estar. 'Sto bene' = eu estou bem — mais completo que só 'bene'.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_ciao",
        tier: "bronze",
        question: "Giovanni acena para um amigo do outro lado da rua. Qual saudação casual ele usa?",
        options: [
          { id: "a", text: "Grazie!" },
          { id: "b", text: "Straniero!" },
          { id: "c", text: "Ciao!" },
          { id: "d", text: "Bene!" },
        ],
        correct: "c",
        explanation: "Ciao! — o cumprimento casual entre amigos. Informal, animado e bidirecional.",
      },
    ],
  },

  // ── 3 · PRÁTICA APLICADA ─────────────────────────────────────────────────────
  // Vocês chegam ao mercado. Giovanni apresenta você a Lucia.
  // 10 exercises — vocabulário revisitado em contexto novo (tier avança naturalmente)
  {
    type: "pratica_aplicada",
    steps: [
      {
        kind: "scene",
        text: "🛒  Mercato del Borgo · Meio da manhã",
      },
      {
        kind: "narrative",
        text: "As ruas estreitas levam a uma praça aberta. Bancas coloridas de pães, tecidos e especiarias lotam o espaço. Giovanni cumprimenta todos os que passam — um aceno aqui, um ciao ali.\n\nEle para na frente de uma banca de ervas aromáticas. Uma mulher de cabelos presos e avental bordado olha para você com curiosidade.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Lucia! Questo è il mio nuovo amico — è forestiero.",
        translation: "Lucia! Este é meu novo amigo — é forasteiro.",
      },
      {
        kind: "npc_speak",
        npc: "Lucia la Mercante",
        line: "Ciao! Come stai?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_bene",
        tier: "bronze",
        question: "Lucia acabou de te cumprimentar e perguntar como vai. O que você responde?",
        options: [
          { id: "a", text: "Grazie, Giovanni!" },
          { id: "b", text: "Bene, grazie!" },
          { id: "c", text: "Come stai, Lucia?" },
          { id: "d", text: "Buonanotte!" },
        ],
        correct: "b",
        explanation: "'Bene, grazie!' — bem, obrigado/a. A resposta natural para come stai?",
      },
      {
        kind: "npc_speak",
        npc: "Lucia la Mercante",
        line: "Benvenuto al borgo! Come ti chiami?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_benvenuto",
        tier: "bronze",
        question: "Lucia disse 'Benvenuto al borgo!' antes de perguntar seu nome. Você já sabe 'bene' — o que 'benvenuto' provavelmente significa?",
        options: [
          { id: "a", text: "Boa tarde" },
          { id: "b", text: "Bem-vindo" },
          { id: "c", text: "Até logo" },
          { id: "d", text: "Com licença" },
        ],
        correct: "b",
        explanation: "Benvenuto = bem-vindo. 'Bene' (bem) + 'venuto' (vindo) — você deduziu a palavra em contexto.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_mi_chiamo",
        tier: "bronze",
        question: "Lucia perguntou 'Come ti chiami?'. O que ela quer saber?",
        options: [
          { id: "a", text: "De onde você veio" },
          { id: "b", text: "Como você está" },
          { id: "c", text: "Qual é o seu nome" },
          { id: "d", text: "Quanto tempo vai ficar" },
        ],
        correct: "c",
        explanation: "'Come ti chiami?' = como você se chama? Ela quer seu nome.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_mi_chiamo",
        tier: "bronze",
        question: "Lucia quer saber seu nome. Como você responde?",
        options: [
          { id: "a", text: "Io sono forestiero." },
          { id: "b", text: "Bene, grazie!" },
          { id: "c", text: "Mi chiamo [nome]." },
          { id: "d", text: "Ciao Lucia!" },
        ],
        correct: "c",
        explanation: "'Mi chiamo + nome' — você aprendeu com Giovanni. Hora de usar com alguém novo.",
      },
      {
        kind: "npc_speak",
        npc: "Lucia la Mercante",
        line: "Piacere! Io mi chiamo Lucia. Sono una mercante.",
        translation: "Prazer! Meu nome é Lucia. Sou uma mercadora.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_piacere",
        tier: "bronze",
        question: "Lucia disse 'Piacere!' ao ser apresentada a você. Em que contexto essa palavra faz sentido?",
        options: [
          { id: "a", text: "Quando você quer ir embora" },
          { id: "b", text: "Quando quer agradecer" },
          { id: "c", text: "Ao conhecer alguém pela primeira vez" },
          { id: "d", text: "Quando não entende algo" },
        ],
        correct: "c",
        explanation: "Piacere = prazer (em conhecê-lo). É o que se diz ao ser apresentado a alguém.",
      },
      {
        kind: "npc_speak",
        npc: "Lucia la Mercante",
        line: "Giovanni è un buon amico, vero?",
        translation: "Giovanni é um bom amigo, não é?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_amico",
        tier: "bronze",
        question: "Lucia usou 'amico' de novo. Você já sabe essa palavra — o que ela disse sobre Giovanni?",
        options: [
          { id: "a", text: "Giovanni é um bom forasteiro" },
          { id: "b", text: "Giovanni é um bom fazendeiro" },
          { id: "c", text: "Giovanni é um bom amigo" },
          { id: "d", text: "Giovanni é um bom guarda" },
        ],
        correct: "c",
        explanation: "Amico = amigo. Você já ouviu com Giovanni — e agora Lucia confirma.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Andiamo! C'è ancora molto da vedere.",
        translation: "Vamos! Ainda tem muito para ver.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_ciao",
        tier: "bronze",
        question: "Você quer se despedir de Lucia antes de partir com Giovanni. O que diz?",
        options: [
          { id: "a", text: "Come stai?" },
          { id: "b", text: "Straniero!" },
          { id: "c", text: "Ciao, Lucia!" },
          { id: "d", text: "Piacere Giovanni!" },
        ],
        correct: "c",
        explanation: "Ciao, Lucia! — despedida informal e calorosa. Ciao funciona para olá E tchau.",
      },
      {
        kind: "npc_speak",
        npc: "Lucia la Mercante",
        line: "Ciao! Buona giornata!",
        translation: "Tchau! Tenha um bom dia!",
      },
      {
        kind: "multiple_choice",
        question: "Lucia disse 'Buona giornata!' ao se despedir. Você já conhece 'buon' e 'giorno' — o que 'buona giornata' significa?",
        options: [
          { id: "a", text: "Até logo, forasteiro" },
          { id: "b", text: "Boa sorte na viagem" },
          { id: "c", text: "Tenha um bom dia" },
          { id: "d", text: "Volte sempre" },
        ],
        correct: "c",
        explanation: "'Buona giornata' = tenha um bom dia. Você deduziu combinando 'buon' + 'giornata'.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_ciao",
        tier: "bronze",
        question: "Depois de conhecer Lucia, Giovanni pergunta se você entendeu. 'Ciao' serve para:",
        options: [
          { id: "a", text: "Apenas cumprimentar ao chegar" },
          { id: "b", text: "Apenas se despedir" },
          { id: "c", text: "Tanto cumprimentar quanto se despedir" },
          { id: "d", text: "Apenas com amigos íntimos" },
        ],
        correct: "c",
        explanation: "Ciao é bidirecional — olá E tchau. Diferente do português onde essas funções têm palavras separadas.",
      },
    ],
  },

  // ── 4 · GRAMÁTICA NARRATIVA ───────────────────────────────────────────────────
  // Na praça central, Giovanni explica 'mi chiamo' e o verbo reflexivo.
  // 8 exercises — foco em gramática (reflexivo), não em vocabulário → sem word_id na maioria
  {
    type: "gramatica_narrativa",
    steps: [
      {
        kind: "scene",
        text: "⛲  Piazza Centrale · Início da tarde",
      },
      {
        kind: "narrative",
        text: "Vocês chegam a uma praça com uma fonte no centro. Giovanni para, se senta numa pedra e te olha com seriedade — mas ainda com aquele sorriso no canto da boca.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Hai imparato 'mi chiamo' — ma sai perché non diciamo 'io sono il mio nome'?",
        translation: "Você aprendeu 'mi chiamo' — mas sabe por que não dizemos 'eu sou o meu nome'?",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "In italiano, 'chiamarsi' è riflessivo. L'azione torna su di te.",
        translation: "Em italiano, 'chiamarsi' é reflexivo. A ação volta para você mesmo.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Io mi chiamo Giovanni. Lei si chiama Lucia. Tu — come ti chiami?",
        translation: "Meu nome é Giovanni. O nome dela é Lucia. E você — como se chama?",
      },
      {
        kind: "multiple_choice",
        question: "Giovanni disse 'Io mi chiamo Giovanni.' O que 'mi' indica nessa frase?",
        options: [
          { id: "a", text: "Que ele está falando de outra pessoa" },
          { id: "b", text: "Que 'io' é desnecessário" },
          { id: "c", text: "Que a ação recai sobre ele mesmo — verbo reflexivo" },
          { id: "d", text: "Que é uma forma irregular" },
        ],
        correct: "c",
        explanation: "'Mi' é o pronome reflexivo da primeira pessoa — 'chiamarsi' volta para o próprio sujeito.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_mi_chiamo",
        tier: "bronze",
        question: "Giovanni quer que você se apresente em italiano. Qual é a estrutura correta?",
        options: [
          { id: "a", text: "Io sono [nome]." },
          { id: "b", text: "Mi chiamo [nome]." },
          { id: "c", text: "Il mio nome è [nome]." },
          { id: "d", text: "Chiamo io [nome]." },
        ],
        correct: "b",
        explanation: "'Mi chiamo + nome' — sem verbo 'ser' ou possessivo. Direto, reflexivo, musical.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "E Lucia — 'lei si chiama Lucia'. 'Si' è la sua forma — come 'mi' è la mia.",
        translation: "E Lucia — 'ela se chama Lucia'. 'Si' é a forma dela — como 'mi' é a minha.",
      },
      {
        kind: "multiple_choice",
        question: "Giovanni disse 'Lei si chiama Lucia.' Como você diria 'Ela se chama Sofia'?",
        options: [
          { id: "a", text: "Lei mi chiama Sofia." },
          { id: "b", text: "Lei chiama Sofia." },
          { id: "c", text: "Lei si chiama Sofia." },
          { id: "d", text: "Sofia si io chiama." },
        ],
        correct: "c",
        explanation: "'Lei si chiama Sofia.' — lei (ela) + si (reflexivo dela) + chiama (chama).",
      },
      {
        kind: "multiple_choice",
        question: "Um menino corre até Giovanni. Ele diz 'Lui si chiama Marco'. O que Giovanni comunicou?",
        options: [
          { id: "a", text: "Ele conhece Marco" },
          { id: "b", text: "O nome dele é Marco" },
          { id: "c", text: "Marco está perdido" },
          { id: "d", text: "Marco é filho de Giovanni" },
        ],
        correct: "b",
        explanation: "'Lui si chiama Marco' = o nome dele é Marco. 'Lui' (ele) + 'si chiama' (se chama).",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "E tu? Come ti chiami? Dimmelo in italiano!",
        translation: "E você? Como se chama? Me diga em italiano!",
      },
      {
        kind: "multiple_choice",
        word_id: "it_mi_chiamo",
        tier: "bronze",
        question: "Giovanni quer que você responda. Qual frase está correta?",
        options: [
          { id: "a", text: "Io sono [nome]." },
          { id: "b", text: "Mi chiamo [nome]." },
          { id: "c", text: "Il nome mio è [nome]." },
          { id: "d", text: "Tu chiami [nome]." },
        ],
        correct: "b",
        explanation: "Mi chiamo + [nome] — sempre essa estrutura para se apresentar.",
      },
      {
        kind: "multiple_choice",
        question: "Giovanni perguntou 'Come ti chiami?'. O que 'ti' indica aqui?",
        options: [
          { id: "a", text: "Que é uma pergunta formal" },
          { id: "b", text: "Que ele está perguntando sobre outra pessoa" },
          { id: "c", text: "Que 'chiamarsi' está na forma 'tu' — reflexivo para você" },
          { id: "d", text: "Que 'ti' substitui 'si' no plural" },
        ],
        correct: "c",
        explanation: "'Ti' é o reflexivo para 'tu' — assim como 'mi' é para 'io' e 'si' é para 'lei/lui'.",
      },
      {
        kind: "multiple_choice",
        question: "Qual dessas frases está errada?",
        options: [
          { id: "a", text: "Io mi chiamo Giovanni." },
          { id: "b", text: "Tu ti chiami Marco." },
          { id: "c", text: "Lui si chiama Marco." },
          { id: "d", text: "Lei mi chiama Lucia." },
        ],
        correct: "d",
        explanation: "'Lei mi chiama Lucia' está errado — 'lei' usa 'si', não 'mi'. Correto: 'Lei si chiama Lucia.'",
      },
      {
        kind: "multiple_choice",
        word_id: "it_mi_chiamo",
        tier: "bronze",
        question: "Como Lucia se apresentaria usando a estrutura correta?",
        options: [
          { id: "a", text: "Io sono Lucia." },
          { id: "b", text: "Mi chiamo Lucia." },
          { id: "c", text: "Chiamo Lucia." },
          { id: "d", text: "Il nome è Lucia." },
        ],
        correct: "b",
        explanation: "'Mi chiamo Lucia.' — sempre Mi chiamo + nome, independente de quem seja.",
      },
    ],
  },

  // ── 5 · REFORÇO ─────────────────────────────────────────────────────────────
  // Você encontra Marco e Sofia nas ruas. Apresentações acontecem.
  // 6 exercises — prática guiada de tudo que aprendeu
  {
    type: "reforco",
    steps: [
      {
        kind: "scene",
        text: "🏘️  Ruas do Borgo · Início da tarde",
      },
      {
        kind: "pattern",
        parts: [
          { text: "Mi chiamo",  isKey: true  },
          { text: " + ",        isKey: false },
          { text: "[seu nome]", isKey: true  },
        ],
        example: "Mi chiamo Marco.",
        translation: "Meu nome é Marco.",
        note: "Em português: verbo ser + possessivo. Em italiano: verbo reflexivo direto. Mais curto, mais musical.",
      },
      {
        kind: "narrative",
        text: "Giovanni para na esquina e cruza os braços com um sorriso. Dois moradores se aproximam. 'Agora você fala sozinho', diz ele com o olhar.",
      },
      {
        kind: "npc_speak",
        npc: "Marco il Fabbro",
        line: "Ciao! Come ti chiami?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_mi_chiamo",
        tier: "bronze",
        question: "Marco perguntou seu nome. O que você diz?",
        options: [
          { id: "a", text: "Bene, grazie!" },
          { id: "b", text: "Ciao, Marco!" },
          { id: "c", text: "Mi chiamo [nome]." },
          { id: "d", text: "Io sono forestiero." },
        ],
        correct: "c",
        explanation: "'Mi chiamo + nome' — você já sabe. Use.",
      },
      {
        kind: "npc_speak",
        npc: "Marco il Fabbro",
        line: "Piacere! Come stai?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_bene",
        tier: "bronze",
        question: "Marco perguntou como você está. O que você responde?",
        options: [
          { id: "a", text: "Straniero!" },
          { id: "b", text: "Bene, grazie!" },
          { id: "c", text: "Mi chiamo [nome]." },
          { id: "d", text: "Buonanotte!" },
        ],
        correct: "b",
        explanation: "'Bene, grazie!' — bem, obrigado/a. A resposta natural para come stai?",
      },
      {
        kind: "npc_speak",
        npc: "Sofia la Maestra",
        line: "Buongiorno! Sei nuovo qui?",
        translation: "Bom dia! Você é novo aqui?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_buongiorno",
        tier: "bronze",
        question: "Sofia te cumprimentou formalmente. Qual é a resposta adequada?",
        options: [
          { id: "a", text: "Ciao ciao!" },
          { id: "b", text: "Buongiorno!" },
          { id: "c", text: "Come stai?" },
          { id: "d", text: "Grazie, arrivederci!" },
        ],
        correct: "b",
        explanation: "Buongiorno! — cumprimento formal de manhã. Certo para alguém que você não conhece ainda.",
      },
      {
        kind: "npc_speak",
        npc: "Sofia la Maestra",
        line: "Mi chiamo Sofia. E tu?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_piacere",
        tier: "bronze",
        question: "Sofia se apresentou e perguntou seu nome. Como você completa a conversa?",
        options: [
          { id: "a", text: "Io sono forestiero." },
          { id: "b", text: "Bene, grazie Sofia!" },
          { id: "c", text: "Mi chiamo [nome]. Piacere!" },
          { id: "d", text: "Come stai?" },
        ],
        correct: "c",
        explanation: "'Mi chiamo + nome. Piacere!' — apresentação + prazer em conhecê-la. Completo.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Bravissimo! E come si chiama la mercante del mercato?",
        translation: "Ótimo! E como se chama a mercante do mercado?",
      },
      {
        kind: "multiple_choice",
        question: "Giovanni pergunta sobre Lucia. Como você diz 'ela se chama Lucia'?",
        options: [
          { id: "a", text: "Lei mi chiama Lucia." },
          { id: "b", text: "Lucia si chiama lei." },
          { id: "c", text: "Lei si chiama Lucia." },
          { id: "d", text: "Lucia chiamo lei." },
        ],
        correct: "c",
        explanation: "'Lei si chiama Lucia.' — lei (ela) + si (reflexivo dela) + chiama (chama).",
      },
    ],
  },

  // ── 6 · OBSTÁCULO ────────────────────────────────────────────────────────────
  // Gate — Guarda do portão central. Errar trava. Tudo que você aprendeu é testado.
  // 10 exercises gated — tier Ouro+ em produção; bronze no mock da fase 1
  {
    type: "obstaculo",
    steps: [
      {
        kind: "scene",
        text: "⚔️  Portão do Centro · Fim da tarde",
      },
      {
        kind: "narrative",
        text: "O caminho para o centro do vilarejo termina num portão de madeira reforçada. Um guarda imponente cruza os braços.\n\nGiovanni para atrás de você e sussurra baixinho:\n\n'Daqui em diante, você fala por conta própria.'",
      },
      {
        kind: "npc_speak",
        npc: "Guarda del Borgo",
        line: "Fermo! Come ti chiami, forestiero?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_mi_chiamo",
        tier: "bronze",
        question: "O guarda quer saber seu nome. Como você responde?",
        options: [
          { id: "a", text: "Io sono forestiero." },
          { id: "b", text: "Bene, grazie!" },
          { id: "c", text: "Mi chiamo [nome]." },
          { id: "d", text: "Non capisco." },
        ],
        correct: "c",
        explanation: "'Mi chiamo + nome' — você aprendeu com Giovanni no primeiro momento. O guarda acena.",
      },
      {
        kind: "npc_speak",
        npc: "Guarda del Borgo",
        line: "Bene. Come stai?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_bene",
        tier: "bronze",
        question: "O guarda perguntou 'come stai?'. Como você responde?",
        options: [
          { id: "a", text: "Mi chiamo [nome]." },
          { id: "b", text: "Ciao, guarda!" },
          { id: "c", text: "Bene, grazie!" },
          { id: "d", text: "Come ti chiami?" },
        ],
        correct: "c",
        explanation: "'Bene, grazie!' — bem, obrigado/a. Natural e respeitoso.",
      },
      {
        kind: "npc_speak",
        npc: "Guarda del Borgo",
        line: "Conosci qualcuno qui al borgo?",
        translation: "Você conhece alguém aqui no borgo?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_amico",
        tier: "bronze",
        question: "O guarda quer saber se você conhece alguém. Como você diz que Giovanni é seu amigo?",
        options: [
          { id: "a", text: "Giovanni è un contadino." },
          { id: "b", text: "Giovanni è il mio amico." },
          { id: "c", text: "Giovanni è forestiero." },
          { id: "d", text: "Giovanni è straniero." },
        ],
        correct: "b",
        explanation: "'Giovanni è il mio amico.' — Giovanni é meu amigo. 'Amico' você aprendeu no primeiro dia.",
      },
      {
        kind: "npc_speak",
        npc: "Guarda del Borgo",
        line: "E la mercante — come si chiama?",
        translation: "E a mercante — como ela se chama?",
      },
      {
        kind: "multiple_choice",
        question: "O guarda pergunta o nome da mercante. Como você diz 'ela se chama Lucia'?",
        options: [
          { id: "a", text: "Lei mi chiama Lucia." },
          { id: "b", text: "Mi chiamo Lucia." },
          { id: "c", text: "Lucia si chiama lei." },
          { id: "d", text: "Lei si chiama Lucia." },
        ],
        correct: "d",
        explanation: "'Lei si chiama Lucia.' — lei (ela) + si (reflexivo dela) + chiama (chama).",
      },
      {
        kind: "npc_speak",
        npc: "Guarda del Borgo",
        line: "Sei forestiero — ma già sai qualcosa. Una domanda: 'buongiorno' si usa...",
        translation: "Você é forasteiro — mas já sabe alguma coisa. Uma pergunta: 'buongiorno' se usa...",
      },
      {
        kind: "multiple_choice",
        word_id: "it_buongiorno",
        tier: "bronze",
        question: "O guarda quer saber quando se usa 'buongiorno'. Quando é correto?",
        options: [
          { id: "a", text: "Qualquer hora do dia" },
          { id: "b", text: "À noite, antes de dormir" },
          { id: "c", text: "De manhã" },
          { id: "d", text: "Apenas ao se despedir" },
        ],
        correct: "c",
        explanation: "Buongiorno = bom dia — de manhã. Buonasera = boa tarde. Buonanotte = boa noite (ao dormir).",
      },
      {
        kind: "npc_speak",
        npc: "Guarda del Borgo",
        line: "Lucia ti ha detto 'piacere' — sai quando si usa?",
        translation: "Lucia te disse 'piacere' — você sabe quando se usa?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_piacere",
        tier: "bronze",
        question: "Lucia usou 'piacere' ao ser apresentada a você. Quando se diz isso?",
        options: [
          { id: "a", text: "Quando você quer ir embora" },
          { id: "b", text: "Ao conhecer alguém pela primeira vez" },
          { id: "c", text: "Para agradecer por algo" },
          { id: "d", text: "Quando não entende o que foi dito" },
        ],
        correct: "b",
        explanation: "Piacere = prazer (em conhecê-lo). Se diz ao ser apresentado a alguém pela primeira vez.",
      },
      {
        kind: "npc_speak",
        npc: "Guarda del Borgo",
        line: "Un'ultima cosa — come si dice 'obrigado' in italiano?",
        translation: "Uma última coisa — como se diz 'obrigado' em italiano?",
      },
      {
        kind: "multiple_choice",
        word_id: "it_grazie",
        tier: "bronze",
        question: "Como se diz 'obrigado/a' em italiano?",
        options: [
          { id: "a", text: "Prego!" },
          { id: "b", text: "Piacere!" },
          { id: "c", text: "Grazie!" },
          { id: "d", text: "Ciao!" },
        ],
        correct: "c",
        explanation: "Grazie = obrigado/a. Simples, musical, indispensável.",
      },
      {
        kind: "npc_speak",
        npc: "Guarda del Borgo",
        line: "Bene! Sei pronto. Puoi passare.",
        translation: "Bem! Você está pronto. Pode passar.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_grazie",
        tier: "bronze",
        question: "Você agradece ao guarda ao cruzar o portão. O que diz?",
        options: [
          { id: "a", text: "Straniero!" },
          { id: "b", text: "Come stai?" },
          { id: "c", text: "Grazie!" },
          { id: "d", text: "Contadino!" },
        ],
        correct: "c",
        explanation: "Grazie! — obrigado. O guarda abre o portão. O centro do borgo está aberto para você.",
      },
      {
        kind: "multiple_choice",
        word_id: "it_ciao",
        tier: "bronze",
        question: "Você se despede do guarda. O que diz?",
        options: [
          { id: "a", text: "Straniero!" },
          { id: "b", text: "Ciao!" },
          { id: "c", text: "Come stai?" },
          { id: "d", text: "Forestiero!" },
        ],
        correct: "b",
        explanation: "Ciao! — despedida informal e calorosa. Você passou. Fase 1 concluída.",
      },
    ],
  },

];

export const PHASES_CONTENT: Record<number, PhaseSection[]> = {
  1: PHASE_1_SECTIONS,
};
