import { useState } from "react";
import { ChevronLeft, Star, Trophy } from "lucide-react";

import { useStrings } from "../../contexts/StringsContext";
import { getAdventureColors } from "../../theme/adventureColors";

type Colors = ReturnType<typeof getAdventureColors>;

// ── Section type interfaces ───────────────────────────────────────────────────

interface CotidianoSection {
  type: "cotidiano";
  scene: string;
  narrative: string;
  npc: string;
  npcLine: string;
  npcTranslation: string;
}
interface AquecimentoSection {
  type: "aquecimento";
  narrative: string;
  vocab: Array<{ it: string; pt: string }>;
}
interface EventoPrincipalSection {
  type: "evento-principal";
  narrative: string;
  npc: string;
  npcLine: string;
  npcTranslation: string;
  highlight: { phrase: string; meaning: string };
}
interface DecodificacaoSection {
  type: "decodificacao";
  narrative: string;
  pattern: { formula: string; example: string; translation: string; note: string };
}
interface PraticaSection {
  type: "pratica";
  narrative: string;
  npc: string;
  npcLine: string;
  npcTranslation: string;
  exercise: { phrase: string; answer: string };
}
interface ObstaculoSection {
  type: "obstaculo";
  narrative: string;
  npc: string;
  npcLine: string;
  npcTranslation: string;
  challenge: { question: string; options: Array<{ id: string; text: string }>; correct: string };
}

type PhaseSection =
  | CotidianoSection
  | AquecimentoSection
  | EventoPrincipalSection
  | DecodificacaoSection
  | PraticaSection
  | ObstaculoSection;

// ── Mock sections — Phase 1, Italian T1 ──────────────────────────────────────

const MOCK_SECTIONS: PhaseSection[] = [
  {
    type: "cotidiano",
    npc: "Giovanni il Contadino",
    scene: "Um campo de trigo ao amanhecer. O sol nasce por trás das colinas.",
    narrative:
      "Você acorda sozinho num campo de trigo dourado. Não sabe seu nome, não sabe de onde veio. Uma figura se aproxima.",
    npcLine: "Ehi, straniero! Stai bene?",
    npcTranslation: "Ei, forasteiro! Você está bem?",
  },
  {
    type: "aquecimento",
    narrative: "Giovanni te ensina as primeiras palavras. Leia cada uma em voz alta:",
    vocab: [
      { it: "ciao",       pt: "olá / tchau" },
      { it: "buongiorno", pt: "bom dia" },
      { it: "come stai?", pt: "como vai você?" },
      { it: "bene",       pt: "bem" },
      { it: "grazie",     pt: "obrigado/a" },
    ],
  },
  {
    type: "evento-principal",
    npc: "Giovanni il Contadino",
    narrative: "Giovanni para diante de você. Coloca a mão no peito e fala com orgulho:",
    npcLine: "Mi chiamo Giovanni. E tu, come ti chiami?",
    npcTranslation: "Meu nome é Giovanni. E você, como se chama?",
    highlight: { phrase: "Mi chiamo...", meaning: "Meu nome é..." },
  },
  {
    type: "decodificacao",
    narrative: "Você acabou de aprender o padrão mais importante para se apresentar em italiano:",
    pattern: {
      formula: "Mi chiamo + [nome]",
      example: "Mi chiamo Marco.",
      translation: "Meu nome é Marco.",
      note: "'Chiamarsi' é reflexivo — 'mi' indica que a ação recai sobre você mesmo.",
    },
  },
  {
    type: "pratica",
    npc: "Giovanni il Contadino",
    narrative: "Giovanni aponta para você, curioso:",
    npcLine: "E tu? Come ti chiami?",
    npcTranslation: "E você? Como se chama?",
    exercise: { phrase: "Mi chiamo...", answer: "Meu nome é..." },
  },
  {
    type: "obstaculo",
    npc: "Guarda del Borgo",
    narrative:
      "O portão do vilarejo está fechado. O guarda cruza os braços e te barra a passagem.",
    npcLine: "Come stai, forestiero?",
    npcTranslation: "Como vai, forasteiro?",
    challenge: {
      question: "O que significa 'Come stai'?",
      options: [
        { id: "a", text: "Como se chama?" },
        { id: "b", text: "Como vai você?" },
        { id: "c", text: "Onde está?" },
        { id: "d", text: "O que quer?" },
      ],
      correct: "b",
    },
  },
];

// ── NPC speech bubble ─────────────────────────────────────────────────────────

function NpcSpeech({ npc, line, translation, c }: {
  npc: string;
  line: string;
  translation: string;
  c: Colors;
}) {
  return (
    <div
      className="rounded-2xl p-4"
      style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
    >
      <p className="mb-1.5 text-[10px] font-bold uppercase tracking-widest" style={{ color: c.goldAccent }}>
        {npc}
      </p>
      <p className="text-base font-semibold italic leading-relaxed" style={{ color: c.parchment }}>
        "{line}"
      </p>
      <p className="mt-1.5 text-xs font-medium" style={{ color: c.textOnBg }}>
        {translation}
      </p>
    </div>
  );
}

// ── Props ─────────────────────────────────────────────────────────────────────

export interface AdventureChapterSectionsProps {
  phaseNumber: number;
  langCode: string;
  onBack: () => void;
}

// ── Component — fills its container (parent sets height + bg) ─────────────────

export default function AdventureChapterSections({
  phaseNumber,
  langCode,
  onBack,
}: AdventureChapterSectionsProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, "dark");

  const [sectionIdx,       setSectionIdx]       = useState(0);
  const [practiceRevealed, setPracticeRevealed] = useState(false);
  const [chosenOption,     setChosenOption]      = useState<string | null>(null);
  const [phaseComplete,    setPhaseComplete]     = useState(false);

  const sections = MOCK_SECTIONS;
  const section  = sections[sectionIdx];
  const total    = sections.length;

  function advance() {
    setPracticeRevealed(false);
    setChosenOption(null);
    if (sectionIdx >= total - 1) {
      setPhaseComplete(true);
    } else {
      setSectionIdx((i) => i + 1);
    }
  }

  const typeLabels: Record<PhaseSection["type"], string> = {
    "cotidiano":         s.adventure.sectionTypeCotidiano,
    "aquecimento":       s.adventure.sectionTypeAquecimento,
    "evento-principal":  s.adventure.sectionTypeEventoP,
    "decodificacao":     s.adventure.sectionTypeDecodificacao,
    "pratica":           s.adventure.sectionTypePratica,
    "obstaculo":         s.adventure.sectionTypeObstaculo,
  };

  // ── Phase complete ────────────────────────────────────────────────────────

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

  // ── Can continue? ─────────────────────────────────────────────────────────

  const canContinue =
    section.type === "obstaculo" ? chosenOption === section.challenge.correct :
    section.type === "pratica"   ? practiceRevealed :
    true;

  return (
    <div className="flex h-full flex-col">

      {/* Header */}
      <header className="shrink-0 px-4 pb-2 pt-3">
        <div className="mb-3 flex items-center gap-3">
          <button
            type="button"
            onClick={onBack}
            className="flex items-center gap-1.5 rounded-full px-3 py-2 text-sm font-semibold"
            style={{ background: c.surface, color: c.parchment }}
          >
            <ChevronLeft size={15} />
            {s.adventure.exit}
          </button>
          <p className="text-xs font-bold" style={{ color: c.goldAccent }}>
            {s.adventure.phaseLabel(phaseNumber)} · {s.adventure.sectionLabel(sectionIdx + 1, total)}
          </p>
        </div>
        <div className="flex gap-1.5">
          {sections.map((_, i) => (
            <div
              key={i}
              className="h-1.5 flex-1 rounded-full transition-all duration-300"
              style={{
                background:
                  i < sectionIdx  ? c.nodeCompleted :
                  i === sectionIdx ? c.nodeActive :
                  c.surface,
              }}
            />
          ))}
        </div>
      </header>

      {/* Section type pill */}
      <div className="shrink-0 px-4 py-2">
        <span
          className="rounded-full px-3 py-1 text-[10px] font-bold uppercase tracking-widest"
          style={{ background: c.surfaceMid, color: c.goldAccent }}
        >
          {typeLabels[section.type]}
        </span>
      </div>

      {/* Scrollable content */}
      <div className="flex-1 overflow-y-auto px-4 pb-4 pt-2">

        {section.type === "cotidiano" && (
          <div className="flex flex-col gap-4" style={{ animation: "fadeIn 200ms ease-out both" }}>
            <p className="text-xs italic" style={{ color: c.textFaint }}>{section.scene}</p>
            <p className="text-base font-medium leading-relaxed" style={{ color: c.textOnBg }}>
              {section.narrative}
            </p>
            <NpcSpeech npc={section.npc} line={section.npcLine} translation={section.npcTranslation} c={c} />
          </div>
        )}

        {section.type === "aquecimento" && (
          <div className="flex flex-col gap-4" style={{ animation: "fadeIn 200ms ease-out both" }}>
            <p className="text-base font-medium leading-relaxed" style={{ color: c.textOnBg }}>
              {section.narrative}
            </p>
            <div className="flex flex-col gap-2">
              {section.vocab.map(({ it, pt }) => (
                <div
                  key={it}
                  className="flex items-center justify-between rounded-xl px-4 py-3"
                  style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
                >
                  <span className="text-lg font-bold" style={{ color: c.parchment }}>{it}</span>
                  <span className="text-sm font-medium" style={{ color: c.textOnBg }}>{pt}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {section.type === "evento-principal" && (
          <div className="flex flex-col gap-4" style={{ animation: "fadeIn 200ms ease-out both" }}>
            <p className="text-base font-medium leading-relaxed" style={{ color: c.textOnBg }}>
              {section.narrative}
            </p>
            <NpcSpeech npc={section.npc} line={section.npcLine} translation={section.npcTranslation} c={c} />
            <div
              className="flex items-center justify-between rounded-xl px-4 py-3"
              style={{ background: `${c.seasonBadgeBg}18`, border: `1px solid ${c.seasonBadgeBg}40` }}
            >
              <span className="text-base font-bold italic" style={{ color: c.parchment }}>
                {section.highlight.phrase}
              </span>
              <span className="text-sm font-semibold" style={{ color: c.goldAccent }}>
                {section.highlight.meaning}
              </span>
            </div>
          </div>
        )}

        {section.type === "decodificacao" && (
          <div className="flex flex-col gap-4" style={{ animation: "fadeIn 200ms ease-out both" }}>
            <p className="text-base font-medium leading-relaxed" style={{ color: c.textOnBg }}>
              {section.narrative}
            </p>
            <div
              className="flex flex-col gap-3 rounded-2xl p-4"
              style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
            >
              <div>
                <p className="text-[10px] font-bold uppercase tracking-widest" style={{ color: c.goldAccent }}>
                  Fórmula
                </p>
                <p className="mt-1 text-base font-bold" style={{ color: c.parchment }}>
                  {section.pattern.formula}
                </p>
              </div>
              <div className="rounded-xl px-3 py-2.5" style={{ background: c.surface }}>
                <p className="text-base italic" style={{ color: c.parchment }}>{section.pattern.example}</p>
                <p className="text-sm" style={{ color: c.textOnBg }}>{section.pattern.translation}</p>
              </div>
              <p className="text-xs italic leading-relaxed" style={{ color: c.textFaint }}>
                {section.pattern.note}
              </p>
            </div>
          </div>
        )}

        {section.type === "pratica" && (
          <div className="flex flex-col gap-4" style={{ animation: "fadeIn 200ms ease-out both" }}>
            <p className="text-base font-medium leading-relaxed" style={{ color: c.textOnBg }}>
              {section.narrative}
            </p>
            <NpcSpeech npc={section.npc} line={section.npcLine} translation={section.npcTranslation} c={c} />
            <div
              className="flex flex-col items-center gap-3 rounded-2xl p-5 text-center"
              style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
            >
              <p className="text-2xl font-bold italic" style={{ color: c.parchment }}>
                {section.exercise.phrase}
              </p>
              {practiceRevealed ? (
                <p
                  className="text-base font-semibold"
                  style={{ color: c.goldAccent, animation: "fadeIn 200ms ease-out both" }}
                >
                  {section.exercise.answer}
                </p>
              ) : (
                <button
                  type="button"
                  onClick={() => setPracticeRevealed(true)}
                  className="rounded-xl px-4 py-2 text-sm font-bold"
                  style={{ background: c.surface, color: c.textOnBg }}
                >
                  {s.adventure.practiceReveal}
                </button>
              )}
            </div>
          </div>
        )}

        {section.type === "obstaculo" && (
          <div className="flex flex-col gap-4" style={{ animation: "fadeIn 200ms ease-out both" }}>
            <p className="text-base font-medium leading-relaxed" style={{ color: c.textOnBg }}>
              {section.narrative}
            </p>
            <NpcSpeech npc={section.npc} line={section.npcLine} translation={section.npcTranslation} c={c} />
            <p className="text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
              {s.adventure.obstaclePrompt}
            </p>
            <p className="text-base font-semibold" style={{ color: c.parchment }}>
              {section.challenge.question}
            </p>
            <div className="flex flex-col gap-2">
              {section.challenge.options.map(({ id, text }) => {
                const isChosen  = chosenOption === id;
                const isCorrect = id === section.challenge.correct;

                let bg     = c.surfaceMid;
                let border = c.borderFaint;
                let color  = c.textOnBg;

                if (isChosen && isCorrect)  { bg = "#16a34a30"; border = "#16a34a"; color = "#4ade80"; }
                else if (isChosen)          { bg = "#dc262630"; border = "#dc2626"; color = "#f87171"; }

                return (
                  <button
                    key={id}
                    type="button"
                    onClick={() => setChosenOption(id)}
                    className="w-full rounded-xl px-4 py-3.5 text-left text-sm font-semibold transition active:scale-[0.98]"
                    style={{ background: bg, border: `1px solid ${border}`, color }}
                  >
                    {text}
                  </button>
                );
              })}
            </div>
            {chosenOption !== null && (
              <p
                className="text-sm font-bold"
                style={{
                  color: chosenOption === section.challenge.correct ? "#4ade80" : "#f87171",
                  animation: "fadeIn 180ms ease-out both",
                }}
              >
                {chosenOption === section.challenge.correct
                  ? s.adventure.obstacleCorrect
                  : s.adventure.obstacleWrong}
              </p>
            )}
          </div>
        )}

      </div>

      {/* Continue button */}
      <div className="shrink-0 px-4 pb-6 pt-2">
        <button
          type="button"
          disabled={!canContinue}
          onClick={advance}
          className="flex h-14 w-full items-center justify-center rounded-2xl text-base font-bold transition"
          style={{
            background: canContinue ? c.ctaBg : c.surface,
            color: canContinue ? "#fff" : c.textFaint,
          }}
        >
          {s.actions.continue}
        </button>
      </div>

    </div>
  );
}
