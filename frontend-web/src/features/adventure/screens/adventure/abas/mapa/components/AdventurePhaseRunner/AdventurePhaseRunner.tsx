import { Backpack, Flame, Sparkles, Star, Trophy } from "lucide-react";
import confetti from "canvas-confetti";
import { motion } from "framer-motion";
import { useEffect, useState } from "react";

import { useStrings } from "../../../../../../../../contexts/StringsContext";
import type { PhaseSection } from "../../../../../../../../types/sections";
import { adventureService } from "../../../../../../../../services/adventureService";
import { getAdventureColors } from "../../../../../../theme/adventureColors";
import type { EarnedItemData, ItemRarity, StreakData } from "../../../../../../../../types/adventure";
import Emoji from "../../../../../../../../components/Emoji";
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

type CompleteStage = "trophy" | "words" | "chest" | "item";

const RARITY_GLOW: Record<ItemRarity, { color: string; glow: string; border: string }> = {
  comum:    { color: "#94a3b8", glow: "#94a3b840", border: "#94a3b850" },
  raro:     { color: "#60a5fa", glow: "#60a5fa40", border: "#60a5fa50" },
  epico:    { color: "#c084fc", glow: "#c084fc45", border: "#c084fc55" },
  lendario: { color: "#fbbf24", glow: "#fbbf2450", border: "#fbbf2460" },
  mitico:   { color: "#22d3ee", glow: "#22d3ee55", border: "#22d3ee70" },
};

const RARITY_CONFETTI: Record<ItemRarity, { colors: string[]; particleCount: number; spread: number }> = {
  comum:    { colors: ["#94a3b8", "#e2e8f0", "#ffffff"], particleCount: 42, spread: 46 },
  raro:     { colors: ["#60a5fa", "#93c5fd", "#ffffff"], particleCount: 58, spread: 54 },
  epico:    { colors: ["#c084fc", "#f0abfc", "#ffffff"], particleCount: 74, spread: 64 },
  lendario: { colors: ["#fbbf24", "#fde68a", "#ffffff"], particleCount: 92, spread: 72 },
  mitico:   { colors: ["#22d3ee", "#a78bfa", "#f0abfc", "#ffffff"], particleCount: 116, spread: 82 },
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

  useEffect(() => {
    if (stage !== "item" || !earnedItem) return;
    const cfg = RARITY_CONFETTI[earnedItem.rarity];
    const burst = () => {
      confetti({
        particleCount: cfg.particleCount,
        spread: cfg.spread,
        startVelocity: 34,
        gravity: 0.82,
        scalar: 0.9,
        origin: { x: 0.5, y: 0.38 },
        colors: cfg.colors,
      });
      confetti({
        particleCount: Math.floor(cfg.particleCount * 0.45),
        angle: 62,
        spread: 46,
        startVelocity: 42,
        origin: { x: 0.14, y: 0.62 },
        colors: cfg.colors,
      });
      confetti({
        particleCount: Math.floor(cfg.particleCount * 0.45),
        angle: 118,
        spread: 46,
        startVelocity: 42,
        origin: { x: 0.86, y: 0.62 },
        colors: cfg.colors,
      });
    };

    const timer = window.setTimeout(burst, 180);
    return () => window.clearTimeout(timer);
  }, [stage, earnedItem]);

  async function handleSectionComplete(sectionMistakes: number) {
    setTotalMistakes(n => n + sectionMistakes);
    const newCount = sectionIdx + 1;
    onSectionComplete?.(newCount);

    if (sectionIdx >= sections.length - 1) {
      try {
        const result = await adventureService.completePhase(phaseId, Math.max(0, 100 - sectionMistakes * 5));
        let chestEarned: EarnedItemData | null = null;
        try {
          const chestRes = await adventureService.openPhaseChest(phaseId);
          if (chestRes.earned_item) {
            chestEarned = {
              slug:   chestRes.earned_item.slug,
              emoji:  chestRes.earned_item.emoji,
              name:   chestRes.earned_item.name,
              lore:   chestRes.earned_item.lore,
              rarity: chestRes.earned_item.rarity,
              action: chestRes.earned_item.action,
            };
          }
        } catch {
          // phase has_chest=false — silent
        }
        setEarnedItem(chestEarned ?? result.earned_item ?? null);
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
                <Flame
                  size={30}
                  style={{ color: c.goldAccent, animation: "flamePulse 1.5s ease-in-out 1.3s infinite" }}
                />
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
              else if (earnedItem) setStage("chest");
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
            onClick={() => { if (earnedItem) setStage("chest"); else onBack(); }}
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
  if (stage === "chest" && earnedItem) {
    const r = RARITY_GLOW[earnedItem.rarity];
    return (
      <motion.div
        className="relative flex h-full flex-col items-center justify-center overflow-hidden px-6 pb-10 pt-8 text-center"
        initial={{ opacity: 0, scale: 0.98 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.38, ease: [0.16, 1, 0.3, 1] }}
      >
        <div
          className="pointer-events-none absolute inset-0"
          style={{
            background: `
              radial-gradient(ellipse at 50% 34%, ${r.glow}, transparent 56%),
              radial-gradient(ellipse at 50% 105%, rgba(0,0,0,0.45), transparent 48%)
            `,
          }}
        />

        <div className="pointer-events-none absolute inset-0 z-0 overflow-hidden">
          {[0, 1, 2, 3, 4, 5].map((i) => (
            <span
              key={i}
              className="absolute h-1.5 w-1.5 rounded-full"
              style={{
                left: `${22 + i * 11}%`,
                top: `${24 + (i % 3) * 12}%`,
                background: i % 2 === 0 ? r.color : c.goldAccent,
                boxShadow: `0 0 14px ${i % 2 === 0 ? r.color : c.goldAccent}`,
                animation: `chestSpark 1.8s ease-in-out ${i * 130}ms infinite`,
              }}
            />
          ))}
        </div>

        <p
          className="relative z-10 text-[10px] font-bold uppercase tracking-[0.25em]"
          style={{ color: c.goldAccent, animation: "itemLoreIn 0.5s ease-out 0.1s both" }}
        >
          {s.adventure.chestRewardLabel}
        </p>

        <motion.button
          type="button"
          onClick={() => setStage("item")}
          className="relative z-10 mt-7 flex h-44 w-52 items-center justify-center transition active:scale-[0.98]"
          initial={{ opacity: 0, y: 26, scale: 0.86 }}
          animate={{ opacity: 1, y: 0, scale: 1 }}
          whileTap={{ scale: 0.96 }}
          transition={{ duration: 0.72, ease: [0.16, 1, 0.3, 1] }}
        >
          <span className="absolute bottom-4 h-8 w-40 rounded-full bg-black/35 blur-md" />
          <motion.span
            className="absolute left-1/2 top-8 h-24 w-40 -translate-x-1/2 rounded-t-[28px] border"
            initial={{ x: "-50%", rotateX: 0, y: 0, filter: "brightness(1)" }}
            animate={{ x: "-50%", rotateX: -58, y: -16, filter: "brightness(1.28)" }}
            transition={{ duration: 1.05, delay: 0.38, ease: [0.16, 1, 0.3, 1] }}
            style={{
              background: `linear-gradient(180deg, ${c.goldAccent} 0%, #8a3d11 52%, #4a1c08 100%)`,
              borderColor: `${c.goldAccent}80`,
              boxShadow: `0 -18px 36px ${r.glow}`,
              transformOrigin: "50% 100%",
            }}
          />
          <span
            className="absolute bottom-9 left-1/2 h-20 w-48 -translate-x-1/2 rounded-[22px] border"
            style={{
              background: "linear-gradient(180deg, #9a4d18 0%, #6b2d0f 48%, #311004 100%)",
              borderColor: `${c.goldAccent}75`,
              boxShadow: "inset 0 10px 18px rgba(255,255,255,0.12), 0 18px 44px rgba(0,0,0,0.42)",
            }}
          />
          <span
            className="absolute bottom-16 left-1/2 h-12 w-14 -translate-x-1/2 rounded-xl border"
            style={{
              background: `linear-gradient(180deg, ${c.goldAccent}, #7c3b09)`,
              borderColor: `${c.goldAccent}90`,
              boxShadow: `0 0 22px ${c.goldAccent}55`,
            }}
          />
          <motion.span
            className="absolute bottom-20 left-1/2 -translate-x-1/2"
            initial={{ x: "-50%", opacity: 0, y: 22, scale: 0.48, rotate: -8 }}
            animate={{ x: "-50%", opacity: 1, y: -18, scale: 1, rotate: 0 }}
            transition={{ duration: 1.05, delay: 0.5, ease: [0.16, 1, 0.3, 1] }}
          >
            <Emoji char={earnedItem.emoji} size={62} />
          </motion.span>
          <motion.span
            className="absolute right-8 top-8"
            animate={{ scale: [0.9, 1.25, 0.9], rotate: [0, 14, 0], opacity: [0.65, 1, 0.65] }}
            transition={{ duration: 1.4, repeat: Infinity, ease: "easeInOut" }}
          >
            <Sparkles
              size={26}
              style={{ color: r.color, filter: `drop-shadow(0 0 12px ${r.color})` }}
            />
          </motion.span>
        </motion.button>

        <h2
          className="relative z-10 mt-3 text-2xl font-bold leading-tight"
          style={{ color: c.parchment, animation: "itemLoreIn 0.5s ease-out 0.72s both" }}
        >
          {s.adventure.chestFoundTitle}
        </h2>
        <p
          className="relative z-10 mt-2 max-w-xs text-sm font-medium leading-relaxed"
          style={{ color: c.textOnBg, animation: "itemLoreIn 0.5s ease-out 0.82s both" }}
        >
          {s.adventure.chestFoundHint}
        </p>

        <button
          type="button"
          onClick={() => setStage("item")}
          className="relative z-10 mt-8 flex h-14 w-full max-w-xs items-center justify-center rounded-2xl text-base font-bold transition active:scale-[0.97]"
          style={{
            background: c.goldAccent,
            color: "#1a0800",
            boxShadow: `0 4px 28px ${c.goldAccent}45`,
            animation: "itemLoreIn 0.5s ease-out 0.95s both",
          }}
        >
          {s.adventure.chestOpen}
        </button>
      </motion.div>
    );
  }

  if (stage === "item" && earnedItem) {
    const r = RARITY_GLOW[earnedItem.rarity];
    return (
      <motion.div
        className="relative flex h-full flex-col items-center justify-center overflow-hidden px-6 pb-10 pt-8 text-center"
        initial={{ opacity: 0, scale: 0.985 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.38, ease: [0.16, 1, 0.3, 1] }}
      >
        <div
          className="pointer-events-none absolute inset-0"
          style={{ background: `radial-gradient(ellipse at 50% 30%, ${r.glow}, transparent 62%), radial-gradient(ellipse at 50% 100%, rgba(0,0,0,0.38), transparent 45%)` }}
        />

        <p
          className="relative z-10 text-[10px] font-bold uppercase tracking-[0.25em]"
          style={{ color: r.color, animation: "itemLoreIn 0.5s ease-out 0.1s both" }}
        >
          {s.adventure.phaseItemGainedEyebrow}
        </p>

        {/* Emoji burst */}
        <motion.div
          className="relative z-10 mt-5 flex min-h-[164px] w-full max-w-sm items-center justify-center rounded-[28px] px-6 py-7"
          initial={{ opacity: 0, y: 18, scale: 0.94, rotateX: 8 }}
          animate={{ opacity: 1, y: 0, scale: 1, rotateX: 0 }}
          transition={{ duration: 0.62, ease: [0.16, 1, 0.3, 1] }}
          style={{
            background: `linear-gradient(160deg, ${r.glow}, rgba(255,255,255,0.055) 42%, rgba(0,0,0,0.24))`,
            border: `1px solid ${r.border}`,
            boxShadow: `0 24px 80px rgba(0,0,0,0.28), 0 0 54px ${r.glow}`,
          }}
        >
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
            className="relative"
            style={{ animation: "itemRevealBurst 0.65s cubic-bezier(0.16,1,0.3,1) both" }}
          >
            <Emoji char={earnedItem.emoji} size={72} />
          </span>
        </motion.div>

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

        <motion.button
          type="button"
          onClick={onBack}
          className="relative z-10 mt-8 flex h-14 w-full max-w-xs items-center justify-center gap-2 rounded-2xl text-base font-bold transition active:scale-[0.97]"
          whileTap={{ scale: 0.96 }}
          whileHover={{ y: -2 }}
          style={{
            background:  r.color,
            color:       "#fff",
            boxShadow:   `0 4px 28px ${r.glow}`,
            animation:   "itemLoreIn 0.5s ease-out 0.7s both",
          }}
        >
          <Backpack size={18} />
          {s.adventure.phaseToBag}
        </motion.button>
      </motion.div>
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
