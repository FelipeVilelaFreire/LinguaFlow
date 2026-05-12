import { Star, Trophy } from "lucide-react";
import { useEffect, useState } from "react";

import { useStrings } from "../../../../../../contexts/StringsContext";
import type { PhaseSection } from "../../../../../../types/sections";
import { adventureService } from "../../../../../../services/adventureService";
import { getAdventureColors } from "../../../../../../theme/adventureColors";
import type { EarnedItemData, ItemRarity, StreakData } from "../../../../../../types/adventure";
import AdventureChapterSections from "./components/AdventureChapterSections";

interface AdventurePhaseRunnerProps {
  phaseNumber:        number;
  phaseId:            number;
  keyWords?:          string[];
  langCode:           string;
  sourceLangCode:     string;
  firstName?:         string;
  startSectionIdx?:   number;
  onSectionComplete?: (newCount: number) => void;
  onBack:             () => void;
}

type CompleteStage = "trophy" | "words" | "item";

const RARITY_GLOW: Record<ItemRarity, { color: string; glow: string; border: string }> = {
  comum:    { color: "#94a3b8", glow: "#94a3b840", border: "#94a3b850" },
  raro:     { color: "#60a5fa", glow: "#60a5fa40", border: "#60a5fa50" },
  epico:    { color: "#c084fc", glow: "#c084fc45", border: "#c084fc55" },
  lendario: { color: "#fbbf24", glow: "#fbbf2450", border: "#fbbf2460" },
};

export default function AdventurePhaseRunner({
  phaseNumber,
  phaseId,
  keyWords = [],
  langCode,
  sourceLangCode,
  firstName = "",
  startSectionIdx = 0,
  onSectionComplete,
  onBack,
}: AdventurePhaseRunnerProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, "dark");

  const [sections, setSections]           = useState<PhaseSection[]>([]);
  const [sectionsLoading, setSectionsLoading] = useState(true);
  const sectionIdx = sections.length > 0 ? Math.min(startSectionIdx, sections.length - 1) : 0;
  const [totalMistakes, setTotalMistakes] = useState(0);
  const [stage,         setStage]         = useState<CompleteStage | null>(null);
  const [earnedItem,    setEarnedItem]    = useState<EarnedItemData | null>(null);
  const [serverWords,   setServerWords]   = useState<string[]>([]);
  const [streakData,    setStreakData]    = useState<StreakData | null>(null);

  useEffect(() => {
    setSectionsLoading(true);
    adventureService.getSections(phaseId)
      .then(setSections)
      .catch(() => setSections([]))
      .finally(() => setSectionsLoading(false));
  }, [phaseId]);

  async function handleSectionComplete(sectionMistakes: number) {
    setTotalMistakes(n => n + sectionMistakes);
    const newCount = sectionIdx + 1;
    onSectionComplete?.(newCount);

    if (sectionIdx >= sections.length - 1) {
      try {
        const result = await adventureService.completePhase(phaseId, Math.max(0, 100 - sectionMistakes * 5));
        setEarnedItem(result.earned_item ?? null);
        setServerWords(result.key_words ?? []);
        setStreakData(result.streak ?? null);
      } catch {
        // non-blocking
      }
      setStage("trophy");
    } else {
      onBack();
    }
  }

  const wordsToShow = serverWords.length > 0 ? serverWords : keyWords;

  // ── Trophy ────────────────────────────────────────────────────────────────────
  if (stage === "trophy") {
    return (
      <div
        className="relative flex h-full flex-col items-center justify-center overflow-hidden p-6 text-center"
        style={{ animation: "phaseCompleteIn 0.45s cubic-bezier(0.16,1,0.3,1) both" }}
      >
        <div
          className="pointer-events-none absolute inset-0"
          style={{ background: `radial-gradient(ellipse at 50% 20%, ${c.nodeActiveGlow}cc, transparent 65%)` }}
        />
        <div className="relative z-10 flex flex-col items-center">
          <div
            className="grid h-24 w-24 place-items-center rounded-full shadow-2xl"
            style={{
              background: `linear-gradient(135deg, ${c.nodeActive}, ${c.ctaBg})`,
              boxShadow:  `0 0 48px ${c.nodeActiveGlow}`,
              animation:  "successPop 420ms ease-out both",
            }}
          >
            <Trophy size={40} color="#fff" />
          </div>

          <p className="mt-5 text-[10px] font-bold uppercase tracking-widest" style={{ color: c.goldAccent }}>
            {s.adventure.phaseComplete}
          </p>
          <p className="mt-1 text-3xl font-bold" style={{ color: c.parchment }}>
            {s.adventure.phaseLabel(phaseNumber)}
          </p>

          <div className="mt-4 flex gap-3">
            {[1, 2, 3].map((i) => (
              <Star
                key={i}
                size={32}
                fill={c.goldAccent}
                stroke={c.goldAccent}
                style={{ animation: `successPop ${200 + i * 140}ms ease-out both` }}
              />
            ))}
          </div>

          <p className="mt-3 text-sm font-semibold" style={{ color: totalMistakes === 0 ? "#4ade80" : c.textOnBg }}>
            {s.adventure.phaseMistakesSummary(totalMistakes)}
          </p>

          {streakData?.updated_today && (
            <div
              className="mt-6 flex flex-col items-center gap-1"
              style={{ animation: "streakReveal 0.5s ease-out 1.1s both" }}
            >
              <div className="flex items-center gap-2">
                <span
                  className="text-3xl leading-none"
                  style={{ display: "inline-block", animation: "flamePulse 1.5s ease-in-out 1.3s infinite" }}
                >
                  🔥
                </span>
                <span
                  className="text-4xl font-black tabular-nums leading-none"
                  style={{ color: c.goldAccent, animation: "streakNumberPop 0.6s cubic-bezier(0.16,1,0.3,1) 1.3s both" }}
                >
                  {streakData.current}
                </span>
              </div>
              <p
                className="text-sm font-bold"
                style={{ color: c.textOnBg, animation: "streakReveal 0.5s ease-out 1.5s both" }}
              >
                {s.adventure.streakToday(streakData.current)}
              </p>
            </div>
          )}

          <button
            type="button"
            onClick={() => {
              if (wordsToShow.length > 0) setStage("words");
              else if (earnedItem) setStage("item");
              else onBack();
            }}
            className="mt-8 flex h-14 w-full max-w-xs items-center justify-center rounded-2xl text-base font-bold transition active:scale-[0.97]"
            style={{ background: c.ctaBg, color: "#fff", boxShadow: `0 4px 20px ${c.nodeActiveGlow}60` }}
          >
            {wordsToShow.length > 0 || earnedItem ? s.adventure.phaseSeeSummary : s.adventure.backToMap}
          </button>
        </div>
      </div>
    );
  }

  // ── Words ─────────────────────────────────────────────────────────────────────
  if (stage === "words" && wordsToShow.length > 0) {
    return (
      <div
        className="flex h-full flex-col overflow-y-auto px-5 pb-10 pt-8"
        style={{ animation: "phaseCompleteIn 0.38s cubic-bezier(0.16,1,0.3,1) both" }}
      >
        <p className="text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
          {s.adventure.phaseWordsSummaryEyebrow}
        </p>
        <h2 className="mt-1 text-2xl font-bold" style={{ color: c.parchment }}>
          {s.adventure.phaseWordsSummaryTitle}
        </h2>
        <p className="mt-1 text-sm" style={{ color: c.textOnBg }}>
          {s.adventure.phaseWordsSummaryCount(wordsToShow.length)}
        </p>

        <div className="mt-6 flex flex-wrap gap-2">
          {wordsToShow.map((word, i) => (
            <span
              key={word}
              className="rounded-xl px-3.5 py-2 text-sm font-bold"
              style={{
                background: `${c.nodeActive}22`,
                color:      c.nodeActive,
                border:     `1px solid ${c.nodeActive}44`,
                animation:  `wordChipIn 0.35s cubic-bezier(0.16,1,0.3,1) ${i * 55}ms both`,
              }}
            >
              {word}
            </span>
          ))}
        </div>

        <div className="mt-auto pt-8">
          <button
            type="button"
            onClick={() => { if (earnedItem) setStage("item"); else onBack(); }}
            className="flex h-14 w-full items-center justify-center rounded-2xl text-base font-bold transition active:scale-[0.97]"
            style={{ background: c.ctaBg, color: "#fff", boxShadow: `0 4px 20px ${c.nodeActiveGlow}60` }}
          >
            {earnedItem ? s.adventure.phaseSeeItem : s.adventure.backToMap}
          </button>
        </div>
      </div>
    );
  }

  // ── Item reveal ───────────────────────────────────────────────────────────────
  if (stage === "item" && earnedItem) {
    const r = RARITY_GLOW[earnedItem.rarity];
    return (
      <div
        className="relative flex h-full flex-col items-center justify-center overflow-hidden px-6 pb-10 pt-8 text-center"
        style={{ animation: "phaseCompleteIn 0.38s cubic-bezier(0.16,1,0.3,1) both" }}
      >
        <div
          className="pointer-events-none absolute inset-0"
          style={{ background: `radial-gradient(ellipse at 50% 30%, ${r.glow}, transparent 62%)` }}
        />

        <p
          className="relative z-10 text-[10px] font-bold uppercase tracking-[0.25em]"
          style={{ color: r.color, animation: "itemLoreIn 0.5s ease-out 0.1s both" }}
        >
          {s.adventure.phaseItemGainedEyebrow}
        </p>

        {/* Emoji burst */}
        <div className="relative z-10 mt-5 flex items-center justify-center">
          <div
            className="absolute rounded-full"
            style={{
              width: 120, height: 120,
              border: `2px solid ${r.color}`,
              animation: "itemRevealRing 1.8s ease-out infinite",
            }}
          />
          <div
            className="absolute rounded-full"
            style={{
              width: 96, height: 96,
              background: r.glow,
              animation: "itemRevealGlow 2.4s ease-in-out infinite",
            }}
          />
          <span
            className="relative text-7xl"
            style={{ animation: "itemRevealBurst 0.65s cubic-bezier(0.16,1,0.3,1) both" }}
          >
            {earnedItem.emoji}
          </span>
        </div>

        <h2
          className="relative z-10 mt-6 text-2xl font-bold leading-tight"
          style={{ color: c.parchment, animation: "itemLoreIn 0.5s ease-out 0.3s both" }}
        >
          {earnedItem.name}
        </h2>

        <span
          className="relative z-10 mt-2 rounded-full px-3 py-1 text-[11px] font-bold uppercase tracking-wider"
          style={{
            background: `${r.color}18`,
            color: r.color,
            border: `1px solid ${r.border}`,
            animation: "itemLoreIn 0.5s ease-out 0.4s both",
          }}
        >
          {s.adventure.itemRarity[earnedItem.rarity]}
        </span>

        <p
          className="relative z-10 mt-4 max-w-sm text-sm font-medium leading-relaxed"
          style={{ color: c.textOnBg, animation: "itemLoreIn 0.5s ease-out 0.55s both" }}
        >
          {earnedItem.lore}
        </p>

        <button
          type="button"
          onClick={onBack}
          className="relative z-10 mt-8 flex h-14 w-full max-w-xs items-center justify-center rounded-2xl text-base font-bold transition active:scale-[0.97]"
          style={{
            background:  r.color,
            color:       "#fff",
            boxShadow:   `0 4px 28px ${r.glow}`,
            animation:   "itemLoreIn 0.5s ease-out 0.7s both",
          }}
        >
          {s.adventure.phaseToBag} 🎒
        </button>
      </div>
    );
  }

  // ── Loading / empty guards ───────────────────────────────────────────────────
  if (sectionsLoading) {
    return (
      <div className="flex h-full items-center justify-center">
        <p className="animate-pulse text-sm font-semibold" style={{ color: c.textOnBg }}>
          {s.adventure.loading}
        </p>
      </div>
    );
  }

  if (sections.length === 0 || !sections[sectionIdx]) {
    return null;
  }

  // ── Active section ────────────────────────────────────────────────────────────
  return (
    <AdventureChapterSections
      section={sections[sectionIdx]}
      sectionNumber={sectionIdx + 1}
      totalSections={sections.length}
      phaseNumber={phaseNumber}
      langCode={langCode}
      sourceLangCode={sourceLangCode}
      firstName={firstName}
      onComplete={handleSectionComplete}
      onBack={onBack}
    />
  );
}
