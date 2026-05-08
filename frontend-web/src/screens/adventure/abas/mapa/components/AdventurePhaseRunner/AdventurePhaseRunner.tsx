import { Star, Trophy } from "lucide-react";
import { useState } from "react";

import { PHASES_CONTENT } from "../../../../../../mocks/adventurePhaseMock";
import { useStrings } from "../../../../../../contexts/StringsContext";
import { getAdventureColors } from "../../../../../../theme/adventureColors";
import AdventureChapterSections from "./components/AdventureChapterSections";

// ── Props ─────────────────────────────────────────────────────────────────────

interface AdventurePhaseRunnerProps {
  phaseNumber: number;
  langCode: string;
  sourceLangCode: string;
  startSectionIdx?: number;
  onSectionComplete?: (newCount: number) => void;
  onBack: () => void;
}

// ── Component ─────────────────────────────────────────────────────────────────

export default function AdventurePhaseRunner({
  phaseNumber,
  langCode,
  sourceLangCode,
  startSectionIdx = 0,
  onSectionComplete,
  onBack,
}: AdventurePhaseRunnerProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, "dark");

  // Fallback to phase 1 content until all phases are authored
  const sections = PHASES_CONTENT[phaseNumber] ?? PHASES_CONTENT[1];

  const [sectionIdx]    = useState(() => Math.min(startSectionIdx, sections.length - 1));
  const [phaseComplete, setPhaseComplete] = useState(startSectionIdx >= sections.length);
  const [totalMistakes, setTotalMistakes] = useState(0);

  function handleSectionComplete(sectionMistakes: number) {
    setTotalMistakes(n => n + sectionMistakes);
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
          <p className="mt-4 text-sm font-semibold" style={{ color: totalMistakes === 0 ? "#4ade80" : c.textOnBg }}>
            {s.adventure.phaseMistakesSummary(totalMistakes)}
          </p>
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
      sourceLangCode={sourceLangCode}
      onComplete={handleSectionComplete}
      onBack={onBack}
    />
  );
}
