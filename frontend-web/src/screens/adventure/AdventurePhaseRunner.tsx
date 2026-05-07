import { Star, Trophy } from "lucide-react";
import { useState } from "react";

import { useStrings } from "../../contexts/StringsContext";
import { getAdventureColors } from "../../theme/adventureColors";
import AdventureChapterSections from "./AdventureChapterSections";
import type { PhaseSection } from "./AdventureChapterSections";

// ── Phase 1 — "O Despertar no Borgo" ─────────────────────────────────────────
//
// Teaching objective: basic greetings + self-introduction
// Vocabulary: ciao, buongiorno, come stai?, bene, grazie, straniero, mi chiamo
// Grammar: chiamarsi reflexivo (Mi chiamo + [nome])
//
// Section order:
//   1 cotidiano   — narrative + checkpoint (hear vocabulary in context)
//   2 vocabulario — vocab list + 2 exercises (absorb and recognize)
//   3 pratica     — 5 exercises (vocabulary only, grammar not yet taught)
//   4 dialogo     — NPC teaches grammar via story (mi chiamo revealed)
//   5 gramatica   — pattern card + examples + 1 test (grammar understood)
//   6 obstaculo   — gate: must use vocab + grammar correctly to pass

const PHASE_1_SECTIONS: PhaseSection[] = [

  // ── 1 · NARRATIVA ────────────────────────────────────────────────────────────
  // Imersão pura + 4 exercícios de reconhecimento do vocab ouvido na história
  {
    type: "cotidiano",
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
      { kind: "player", text: "Você balança a cabeça negativamente. Giovanni coça a barba, pensativo. Então ri — não com deboche, mas com a simpatia de quem já viu essa cena antes." },
      { kind: "npc",    npc: "Giovanni il Contadino", line: "Va bene, va bene! Io mi chiamo Giovanni. Sono un contadino — capisce? Un farmer." },
      { kind: "npc",    npc: "Giovanni il Contadino", line: "Siediti. Io ti insegno le prime parole. Parola per parola, amico mio." },
      { kind: "narrative",
        text: "Você se senta no banquinho que ele oferece. Em algum lugar nesse vilarejo há respostas para as suas perguntas. Por enquanto — há Giovanni, e as palavras que ele está prestes a te ensinar." },
    ],
    exercises: [
      {
        kind: "multiple_choice",
        question: "Giovanni chamou você de 'forestiero' ao chegar. O que essa palavra significa?",
        options: [
          { id: "a", text: "Fazendeiro — alguém que trabalha na terra" },
          { id: "b", text: "Forasteiro — alguém de fora do lugar" },
          { id: "c", text: "Amigo — alguém querido" },
          { id: "d", text: "Guarda — alguém que protege" },
        ],
        correct: "b",
        explanation: "Forestiero = forasteiro. Você ouviu no contexto certo — ele te chamou assim ao te ver chegar.",
      },
      {
        kind: "multiple_choice",
        question: "Giovanni disse 'Sono un contadino — capisce? Un farmer.' O que é um contadino?",
        options: [
          { id: "a", text: "Um comerciante de tecidos" },
          { id: "b", text: "Um guerreiro da guarda" },
          { id: "c", text: "Um fazendeiro" },
          { id: "d", text: "Um curandeiro do vilarejo" },
        ],
        correct: "c",
        explanation: "Contadino = fazendeiro. Giovanni até traduziu com 'un farmer' para garantir que você entendesse.",
      },
      {
        kind: "multiple_choice",
        question: "Giovanni colocou a mão no peito e disse 'Io mi chiamo Giovanni.' O que ele estava fazendo?",
        options: [
          { id: "a", text: "Perguntando o seu nome" },
          { id: "b", text: "Se apresentando — dizendo o próprio nome" },
          { id: "c", text: "Pedindo para você ir embora" },
          { id: "d", text: "Chamando alguém de longe" },
        ],
        correct: "b",
        explanation: "'Mi chiamo' = meu nome é. Esse é o gesto universal de apresentação — mão no peito, nome.",
      },
      {
        kind: "multiple_choice",
        question: "No final, Giovanni disse 'Parola per parola, amico mio.' O que significa 'amico'?",
        options: [
          { id: "a", text: "Palavra" },
          { id: "b", text: "Inimigo" },
          { id: "c", text: "Mestre" },
          { id: "d", text: "Amigo" },
        ],
        correct: "d",
        explanation: "Amico = amigo. Giovanni usou para mostrar que não há ameaça — ele está do seu lado.",
      },
    ],
  },

  // ── 2 · VOCABULÁRIO ──────────────────────────────────────────────────────────
  {
    type: "vocabulario",
    steps: [
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Prima di andare avanti — ricordiamo le parole di base.",
        translation: "Antes de continuarmos — vamos lembrar as palavras básicas.",
      },
      {
        kind: "vocab_list",
        items: [
          { target: "ciao",       native: "olá / tchau" },
          { target: "buongiorno", native: "bom dia" },
          { target: "come stai?", native: "como vai você?" },
          { target: "bene",       native: "bem" },
          { target: "grazie",     native: "obrigado/a" },
          { target: "straniero",  native: "forasteiro" },
        ],
      },
      {
        kind: "multiple_choice",
        question: "Giovanni chega sorrindo com a mão aberta. O que ele está dizendo?",
        options: [
          { id: "a", text: "Ciao! — Olá!" },
          { id: "b", text: "Arrivederci! — Até logo!" },
          { id: "c", text: "Prego! — De nada!" },
          { id: "d", text: "Per favore — Por favor" },
        ],
        correct: "a",
        explanation: "Ciao é a saudação mais usada — serve tanto para olá quanto para tchau.",
      },
      {
        kind: "multiple_choice",
        question: "Giovanni inclina a cabeça com expectativa. O que ele perguntou?",
        options: [
          { id: "a", text: "Come ti chiami?" },
          { id: "b", text: "Come stai?" },
          { id: "c", text: "Dove sei?" },
          { id: "d", text: "Che ora è?" },
        ],
        correct: "b",
        explanation: "'Come stai?' — Como vai você? A pergunta mais natural sobre o estado de alguém.",
      },
      {
        kind: "reveal",
        phrase: "Sto bene, grazie!",
        meaning: "Estou bem, obrigado/a!",
        note: "A resposta completa para 'come stai?' — você vai ouvir e usar muito.",
      },
    ],
  },

  // ── 3 · PRÁTICA (vocabulário) ─────────────────────────────────────────────────
  // Only exercises. Grammar (mi chiamo) not yet taught — tested in sections 4–5.
  {
    type: "pratica",
    steps: [
      {
        kind: "multiple_choice",
        question: "'Ciao' significa:",
        options: [
          { id: "a", text: "Bom dia" },
          { id: "b", text: "Olá / tchau" },
          { id: "c", text: "Obrigado/a" },
          { id: "d", text: "Por favor" },
        ],
        correct: "b",
        explanation: "Ciao é informal e serve para cumprimentar e despedir.",
      },
      {
        kind: "fill_blank",
        prompt: "Sto _____, grazie!",
        answer: "bene  →  Sto bene, grazie! — Estou bem, obrigado/a!",
      },
      {
        kind: "multiple_choice",
        question: "Giovanni pergunta 'Come stai?' Como você responde que está bem?",
        options: [
          { id: "a", text: "Arrivederci!" },
          { id: "b", text: "Per favore!" },
          { id: "c", text: "Bene, grazie!" },
          { id: "d", text: "Buonasera!" },
        ],
        correct: "c",
        explanation: "'Bene, grazie!' — Bem, obrigado/a! Resposta natural para come stai?",
      },
      {
        kind: "translate",
        source: "Como vai você?",
        answer: "Come stai?",
      },
      {
        kind: "multiple_choice",
        question: "Como se chama um forasteiro em italiano?",
        options: [
          { id: "a", text: "Contadino" },
          { id: "b", text: "Guarda" },
          { id: "c", text: "Straniero" },
          { id: "d", text: "Amico" },
        ],
        correct: "c",
        explanation: "Straniero = forasteiro. Giovanni usou essa palavra para chamar você no Cotidiano.",
      },
    ],
  },

  // ── 4 · DIÁLOGO ──────────────────────────────────────────────────────────────
  {
    type: "dialogo",
    steps: [
      {
        kind: "narrative",
        text: "Giovanni se levanta da pedra. Com um sorriso largo, ele coloca a mão no peito — chegou a hora de trocarem nomes.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Io mi chiamo Giovanni. Sono un contadino.",
        // No translation — player watches, tries to catch the meaning
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Mi chiamo Giovanni.",
        translation: "Meu nome é Giovanni.",
      },
      {
        kind: "reveal",
        phrase: "Mi chiamo...",
        meaning: "Meu nome é...",
        note: "'Chiamarsi' é um verbo reflexivo. 'Mi' indica que a ação recai sobre você mesmo — sem 'ser' no meio, ao contrário do português.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "E tu, come ti chiami?",
        translation: "E você, como se chama?",
      },
    ],
  },

  // ── 5 · GRAMÁTICA ────────────────────────────────────────────────────────────
  {
    type: "gramatica",
    steps: [
      {
        kind: "pattern",
        parts: [
          { text: "Mi chiamo",  isKey: true  },
          { text: " + ",        isKey: false },
          { text: "[seu nome]", isKey: true  },
        ],
        example: "Mi chiamo Marco.",
        translation: "Meu nome é Marco.",
        note: "Diferente do português, não há verbo 'ser' no meio. O verbo 'chiamarsi' já carrega esse significado.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Lei si chiama Lucia. Lui si chiama Marco.",
        translation: "Ela se chama Lucia. Ele se chama Marco.",
      },
      {
        kind: "narrative",
        text: "Em português: 'Meu nome é' = verbo ser + possessivo.\nEm italiano: 'Mi chiamo' = verbo reflexivo.\n\nMais direto, mais musical — e impossível de esquecer.",
      },
      {
        kind: "npc_speak",
        npc: "Giovanni il Contadino",
        line: "Capisce? Mi chiamo Giovanni. E tu?",
        translation: "Entendeu? Meu nome é Giovanni. E você?",
      },
      {
        kind: "multiple_choice",
        question: "Como se diz 'Meu nome é Sofia' em italiano?",
        options: [
          { id: "a", text: "Io sono Sofia." },
          { id: "b", text: "Mi chiamo Sofia." },
          { id: "c", text: "Il mio nome Sofia." },
          { id: "d", text: "Chiamo Sofia io." },
        ],
        correct: "b",
        explanation: "'Mi chiamo + nome' — a estrutura correta para se apresentar em italiano.",
      },
    ],
  },

  // ── 6 · OBSTÁCULO ────────────────────────────────────────────────────────────
  // Gated gate — wrong answer stays locked until correct one is chosen.
  {
    type: "obstaculo",
    steps: [
      {
        kind: "scene",
        text: "⚔️  Portão do Borgo · Fim da manhã",
      },
      {
        kind: "narrative",
        text: "O caminho para o centro do vilarejo termina num portão de madeira reforçada. Um guarda imponente cruza os braços. Giovanni observa de longe com um aceno discreto. Agora você está sozinho.",
      },
      {
        kind: "npc_speak",
        npc: "Guarda del Borgo",
        line: "Fermo! Come stai, forestiero?",
        // No translation — this is the gate challenge
      },
      {
        kind: "multiple_choice",
        question: "O que o guarda perguntou?",
        options: [
          { id: "a", text: "Come ti chiami? — Como se chama?" },
          { id: "b", text: "Come stai? — Como vai você?" },
          { id: "c", text: "Dove sei? — Onde você está?" },
          { id: "d", text: "Chi sei tu? — Quem é você?" },
        ],
        correct: "b",
        explanation: "'Come stai?' — Como vai você? Você reconheceu a pergunta.",
      },
      {
        kind: "multiple_choice",
        question: "O guarda espera uma resposta. O que dizer para passar?",
        options: [
          { id: "a", text: "Non capisco. — Não entendo." },
          { id: "b", text: "Come stai? — Como vai você?" },
          { id: "c", text: "Bene, grazie! Mi chiamo... — Bem, obrigado! Meu nome é..." },
          { id: "d", text: "Ciao ciao! — Tchau tchau!" },
        ],
        correct: "c",
        explanation: "Você respondeu E se apresentou usando tudo que aprendeu. O portão está aberto.",
      },
    ],
  },

];

// ── Props ─────────────────────────────────────────────────────────────────────

interface AdventurePhaseRunnerProps {
  phaseNumber: number;
  langCode: string;
  startSectionIdx?: number;
  onSectionComplete?: (newCount: number) => void;
  onBack: () => void;
}

// ── Component ─────────────────────────────────────────────────────────────────

export default function AdventurePhaseRunner({
  phaseNumber,
  langCode,
  startSectionIdx = 0,
  onSectionComplete,
  onBack,
}: AdventurePhaseRunnerProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, "dark");

  const sections = PHASE_1_SECTIONS;

  const [sectionIdx]    = useState(() => Math.min(startSectionIdx, sections.length - 1));
  const [phaseComplete, setPhaseComplete] = useState(startSectionIdx >= sections.length);

  function handleSectionComplete() {
    const newCount = sectionIdx + 1;
    onSectionComplete?.(newCount);
    if (sectionIdx >= sections.length - 1) {
      setPhaseComplete(true);
    } else {
      onBack();
    }
  }

  if (phaseComplete) {
    return (
      <div className="relative flex h-full flex-col items-center justify-center overflow-hidden p-6 text-center">
        <div
          className="pointer-events-none absolute inset-0"
          style={{ background: `radial-gradient(ellipse at 50% 25%, ${c.nodeActiveGlow}, transparent 60%)` }}
        />
        <div className="relative z-10 flex flex-col items-center">
          <div
            className="grid h-24 w-24 place-items-center rounded-full shadow-2xl"
            style={{
              background: `linear-gradient(135deg, ${c.nodeActive}, ${c.ctaBg})`,
              boxShadow: `0 0 40px ${c.nodeActiveGlow}`,
              animation: "successPop 420ms ease-out both",
            }}
          >
            <Trophy size={40} color="#fff" />
          </div>
          <p className="mt-5 text-[10px] font-bold uppercase tracking-widest" style={{ color: c.goldAccent }}>
            {s.adventure.phaseComplete}
          </p>
          <p className="mt-2 text-3xl font-bold" style={{ color: c.parchment }}>
            {s.adventure.phaseLabel(phaseNumber)}
          </p>
          <div className="mt-5 flex gap-3">
            {[1, 2, 3].map((i) => (
              <Star
                key={i}
                size={34}
                fill={c.goldAccent}
                stroke={c.goldAccent}
                style={{ animation: `successPop ${200 + i * 150}ms ease-out both` }}
              />
            ))}
          </div>
          <button
            type="button"
            onClick={onBack}
            className="mt-10 flex h-14 w-full max-w-xs items-center justify-center rounded-2xl text-base font-bold"
            style={{ background: c.ctaBg, color: "#fff" }}
          >
            {s.adventure.backToMap}
          </button>
        </div>
      </div>
    );
  }

  return (
    <AdventureChapterSections
      section={sections[sectionIdx]}
      sectionNumber={sectionIdx + 1}
      totalSections={sections.length}
      phaseNumber={phaseNumber}
      langCode={langCode}
      onComplete={handleSectionComplete}
      onBack={onBack}
    />
  );
}
