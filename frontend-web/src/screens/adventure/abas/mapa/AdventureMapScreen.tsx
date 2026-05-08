import { BookOpen, CheckCircle2, Lock, Skull, Star, Swords } from "lucide-react";
import { useEffect, useState } from "react";

import { useStrings } from "../../../../contexts/StringsContext";
import { getAdventureColors } from "../../../../theme/adventureColors";
import type { AdventureThemeMode } from "../../../../theme/adventureColors"; // prop type only
import type { AdventureChapter, AdventurePhase } from "../../../../types/adventure";

// ── Winding path positions (x%, y px) — 25 nodes, ~85 px spacing ─────────────
const WINDING: Array<{ x: number; y: number }> = [
  // Row 1 → right
  { x: 50, y: 70  }, { x: 65, y: 155 }, { x: 78, y: 240 }, { x: 82, y: 325 }, { x: 72, y: 408 },
  // Row 2 ← left
  { x: 55, y: 493 }, { x: 38, y: 578 }, { x: 24, y: 663 }, { x: 18, y: 748 }, { x: 22, y: 833 },
  // Row 3 → right
  { x: 34, y: 918 }, { x: 48, y: 1003 }, { x: 62, y: 1088 }, { x: 76, y: 1173 }, { x: 80, y: 1258 },
  // Row 4 ← left
  { x: 70, y: 1340 }, { x: 55, y: 1420 }, { x: 40, y: 1500 }, { x: 26, y: 1580 }, { x: 20, y: 1660 },
  // Boss approach → center
  { x: 28, y: 1740 }, { x: 40, y: 1820 }, { x: 50, y: 1900 }, { x: 50, y: 1980 }, { x: 50, y: 2050 },
];

// SVG bezier path (viewBox "0 0 100 2120") — each segment: C ax,mid bx,mid bx,by
const PATH_D =
  "M50,70 " +
  "C50,112 65,112 65,155 C65,197 78,197 78,240 C78,282 82,282 82,325 C82,366 72,366 72,408 " +
  "C72,450 55,450 55,493 C55,535 38,535 38,578 C38,620 24,620 24,663 C24,705 18,705 18,748 " +
  "C18,790 22,790 22,833 C22,875 34,875 34,918 C34,960 48,960 48,1003 C48,1045 62,1045 62,1088 " +
  "C62,1130 76,1130 76,1173 C76,1215 80,1215 80,1258 C80,1299 70,1299 70,1340 " +
  "C70,1380 55,1380 55,1420 C55,1460 40,1460 40,1500 C40,1540 26,1540 26,1580 C26,1620 20,1620 20,1660 " +
  "C20,1700 28,1700 28,1740 C28,1780 40,1780 40,1820 C40,1860 50,1860 50,1900 " +
  "C50,1940 50,1940 50,1980 C50,2015 50,2015 50,2050";

const SEASON_HEIGHT = 2120;

// ── Decorative SVG silhouettes between seasons (pure CSS, no images) ─────────
function ItalianDivider({ index, color }: { index: number; color: string }) {
  const opacity = "opacity-20";
  if (index === 0) return (
    <svg viewBox="0 0 200 80" className={`w-full ${opacity}`} style={{ fill: "none", stroke: color, strokeWidth: 2.5 }}>
      {/* Roman arch */}
      <path d="M30,78 L30,35 Q100,2 170,35 L170,78" />
      <line x1="20" y1="78" x2="180" y2="78" />
      <line x1="30" y1="55" x2="170" y2="55" strokeWidth={1} strokeDasharray="4,4" />
    </svg>
  );
  if (index === 1) return (
    <svg viewBox="0 0 200 80" className={`w-full ${opacity}`} style={{ fill: color, stroke: "none" }}>
      {/* Cypress grove */}
      <polygon points="50,78 44,12 56,12" />
      <polygon points="100,78 92,5 108,5" />
      <polygon points="150,78 144,14 156,14" />
    </svg>
  );
  if (index === 2) return (
    <svg viewBox="0 0 200 80" className={`w-full ${opacity}`} style={{ fill: "none", stroke: color, strokeWidth: 2.5 }}>
      {/* Amphora */}
      <path d="M85,8 L80,8 Q60,22 65,50 Q68,66 82,74 L118,74 Q132,66 135,50 Q140,22 120,8 Z" />
      <path d="M80,22 Q62,34 65,50" />
      <path d="M120,22 Q138,34 135,50" />
      <line x1="85" y1="8" x2="115" y2="8" />
    </svg>
  );
  // index === 3 — column
  return (
    <svg viewBox="0 0 200 80" className={`w-full ${opacity}`} style={{ fill: color, stroke: "none" }}>
      {/* Roman column */}
      <rect x="82" y="4"  width="36" height="8"  rx="1" />
      <rect x="88" y="12" width="24" height="50" rx="0" />
      <rect x="80" y="62" width="40" height="8"  rx="1" />
      <rect x="84" y="70" width="32" height="6"  rx="1" />
      {/* flute lines */}
      {[94, 99, 104, 109].map(x => (
        <line key={x} x1={x} y1={13} x2={x} y2={61} stroke="rgba(0,0,0,0.35)" strokeWidth={0.8} />
      ))}
    </svg>
  );
}

// ── Section ring SVG — thin circular progress for the current phase node ──────
function SectionRing({
  completed,
  total,
  size,
  strokeWidth = 2,
  c,
}: {
  completed: number;
  total: number;
  size: number;
  strokeWidth?: number;
  c: ReturnType<typeof getAdventureColors>;
}) {
  if (total <= 0) return null;
  const r = size / 2 - strokeWidth / 2 - 1;
  const circumference = 2 * Math.PI * r;
  const dashOffset = circumference * (1 - (completed / total));

  return (
    <svg
      width={size}
      height={size}
      className="pointer-events-none absolute inset-0"
      style={{ transform: "rotate(-90deg)" }}
    >
      <circle
        cx={size / 2}
        cy={size / 2}
        r={r}
        fill="none"
        stroke={c.textFaint}
        strokeWidth={strokeWidth}
      />
      {completed > 0 && (
        <circle
          cx={size / 2}
          cy={size / 2}
          r={r}
          fill="none"
          stroke={c.nodeActive}
          strokeWidth={strokeWidth}
          strokeDasharray={circumference}
          strokeDashoffset={dashOffset}
          strokeLinecap="round"
        />
      )}
    </svg>
  );
}

// ── Phase entry card (bottom-sheet or floating) ───────────────────────────────
function PhaseEntry({
  phase, nodeRect, c, onClose, onStart,
}: {
  phase: AdventurePhase;
  nodeRect: DOMRect | null;
  c: ReturnType<typeof getAdventureColors>;
  onClose: () => void;
  onStart: () => void;
}) {
  const s        = useStrings();
  const isBoss   = phase.is_boss;
  const isReview = phase.phase_type === "review";
  const ctaBg    = isBoss ? c.bossColor : c.ctaBg;
  const cur      = (phase.completed_sections ?? 0) + 1;
  const tot      = phase.section_count ?? 6;
  const label    = isBoss
    ? s.adventure.bossLabel
    : isReview
    ? `${s.adventure.reviewLabel} · ${s.adventure.sectionLabel(cur, tot)}`
    : s.adventure.sectionLabel(cur, tot);
  const ctaLabel = isBoss ? s.adventure.phaseStartBoss
    : isReview ? s.adventure.phaseStartReview
    : s.adventure.phaseStart;

  const inner = (
    <>
      <p className="text-[10px] font-bold uppercase tracking-widest" style={{ color: c.goldAccent }}>{label}</p>
      <p className="mt-1 text-sm font-bold leading-snug" style={{ color: c.parchment }}>{phase.title}</p>
      {phase.npc_name && !isBoss && (
        <p className="mt-0.5 text-[11px]" style={{ color: c.textOnBg }}>{phase.npc_name}</p>
      )}
      <button
        type="button"
        onClick={onStart}
        className="mt-3 flex h-11 w-full items-center justify-center gap-2 rounded-xl text-sm font-bold transition active:scale-[0.98]"
        style={{ background: ctaBg, color: "#fff" }}
      >
        {isBoss ? <Skull size={15} /> : <Swords size={15} />}
        {ctaLabel}
      </button>
    </>
  );

  if (!nodeRect) {
    return (
      <div className="fixed inset-0 z-40" onClick={onClose}>
        <div
          className="absolute inset-x-0 bottom-0 rounded-t-2xl px-5 pb-10 pt-4"
          style={{
            background: `linear-gradient(160deg, ${c.bgMid} 0%, ${c.bgFrom} 100%)`,
            borderTop: `1px solid ${c.parchmentBorder}`,
            boxShadow: "0 -8px 32px rgba(0,0,0,0.25)",
            animation: "sheetSlideUp 220ms ease-out both",
          }}
          onClick={(e) => e.stopPropagation()}
        >
          <div className="mx-auto mb-4 h-1 w-10 rounded-full" style={{ background: c.textFaint }} />
          {inner}
        </div>
      </div>
    );
  }

  const CARD_W    = Math.min(272, window.innerWidth - 32);
  const cx        = nodeRect.left + nodeRect.width / 2;
  const cardLeft  = Math.max(16, Math.min(cx - CARD_W / 2, window.innerWidth - CARD_W - 16));
  const cardTop   = nodeRect.bottom + 12;
  const arrowLeft = Math.max(12, Math.min(cx - cardLeft, CARD_W - 12));

  return (
    <div className="fixed inset-0 z-40" onClick={onClose}>
      <div
        className="absolute"
        style={{ left: cardLeft, top: cardTop, width: CARD_W, animation: "fadeIn 120ms ease-out both" }}
        onClick={(e) => e.stopPropagation()}
      >
        <div
          className="absolute"
          style={{
            top: 0, left: arrowLeft - 8, transform: "translateY(-100%)",
            width: 0, height: 0,
            borderLeft: "8px solid transparent",
            borderRight: "8px solid transparent",
            borderBottom: `8px solid ${c.bgMid}`,
          }}
        />
        <div
          className="rounded-2xl px-4 pt-3.5 pb-4"
          style={{
            background: `linear-gradient(160deg, ${c.bgMid} 0%, ${c.bgFrom} 100%)`,
            border: `1px solid ${c.parchmentBorder}`,
            boxShadow: "0 8px 32px rgba(0,0,0,0.18)",
          }}
        >
          {inner}
        </div>
      </div>
    </div>
  );
}

// ── Season header ─────────────────────────────────────────────────────────────
function SeasonHeader({
  chapter,
  index,
  isUnlocked,
  c,
}: {
  chapter: AdventureChapter;
  index: number;
  isUnlocked: boolean;
  c: ReturnType<typeof getAdventureColors>;
}) {
  const isLocked = !isUnlocked;
  return (
    <div
      className="mx-4 mb-2 mt-6 rounded-xl p-4"
      style={{
        background: isLocked ? c.surfaceMid : `${c.seasonBadgeBg}22`,
        border: `1px solid ${isLocked ? c.borderFaint : c.seasonBadgeBg + "44"}`,
      }}
    >
      <div className="flex items-center justify-between gap-3">
        <div className="flex items-center gap-2">
          <span
            className="rounded-md px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider"
            style={
              isLocked
                ? { background: c.surface, color: c.textFaint }
                : { background: c.seasonBadgeBg, color: c.seasonBadgeText }
            }
          >
            {chapter.level}
          </span>
          <span
            className="text-[10px] font-semibold uppercase tracking-widest"
            style={{ color: isLocked ? c.textFaint : `${c.parchment}60` }}
          >
            A1 · Il Viandante
          </span>
        </div>
        {isLocked && <Lock size={13} style={{ color: c.textFaint }} />}
      </div>
      <p
        className="mt-1 text-base font-semibold leading-tight"
        style={{ color: isLocked ? c.textOnBg : c.parchment }}
      >
        {chapter.title}
      </p>
      {!isLocked && (
        <p className="mt-1 text-xs font-medium" style={{ color: c.textOnBg }}>
          {chapter.phases.filter(p => p.is_completed).length}/{chapter.phases.length} fases concluídas
        </p>
      )}
    </div>
  );
}

// ── Single phase node button ──────────────────────────────────────────────────
function PhaseNode({
  phase,
  pos,
  currentPhaseNumber,
  themeMode,
  c,
  onClick,
}: {
  phase: AdventurePhase;
  pos: { x: number; y: number };
  currentPhaseNumber: number;
  themeMode: AdventureThemeMode;
  c: ReturnType<typeof getAdventureColors>;
  onClick: (rect: DOMRect) => void;
}) {
  const isCompleted = phase.is_completed;
  const isCurrent   = phase.number === currentPhaseNumber && !phase.is_completed;
  const isLocked    = !isCompleted && !isCurrent;
  const isBoss      = phase.is_boss;
  const isReview    = phase.phase_type === "review";
  const isLight     = themeMode === "light";

  const size     = isBoss ? 64 : 54;
  const ringSize = size + 14;

  const bg = isCompleted ? c.nodeCompleted
           : isCurrent && isBoss   ? c.bossColor
           : isCurrent && isReview ? c.goldAccent
           : isCurrent             ? c.nodeActive
           : c.nodeLocked;

  const activeColor = isBoss ? c.bossColor : isReview ? c.goldAccent : c.nodeActive;
  const boxShadow = isCurrent
    ? `0 0 0 3px ${activeColor}, 0 0 28px ${isBoss ? c.bossGlow : c.nodeActiveGlow}`
    : isCompleted
    ? `0 0 0 2px ${c.nodeCompleted}80, 0 4px 12px rgba(0,0,0,0.18)`
    : "0 4px 14px rgba(0,0,0,0.15)";

  const border = isLight
    ? `2px solid ${isCompleted ? c.nodeCompleted : isCurrent ? activeColor : c.pathColor}80`
    : undefined;

  const sectionCount       = phase.section_count ?? 6;
  const completedSections  = phase.completed_sections ?? 0;
  const showRing = isCurrent;

  return (
    <div
      className="absolute"
      style={{
        left: `${pos.x}%`,
        top: pos.y,
        transform: "translate(-50%, -50%)",
        width: ringSize,
        height: ringSize,
        zIndex: isCurrent ? 2 : 1,
        opacity: isLocked ? (isLight ? 0.6 : 0.45) : 1,
        animation: isCurrent ? "adventureBounce 1.4s ease-in-out infinite" : undefined,
      }}
    >
      {/* Section progress ring — current phase only */}
      {showRing && (
        <SectionRing
          completed={completedSections}
          total={sectionCount}
          size={ringSize}
          strokeWidth={2}
          c={c}
        />
      )}

      {/* Phase button */}
      <button
        type="button"
        disabled={isLocked}
        data-current-phase={isCurrent ? "true" : undefined}
        onClick={(e) => onClick((e.currentTarget as HTMLElement).getBoundingClientRect())}
        className="absolute left-1/2 top-1/2 flex items-center justify-center rounded-full font-bold transition"
        style={{
          transform: "translate(-50%, -50%)",
          width: size,
          height: size,
          background: bg,
          boxShadow,
          border,
          cursor: isLocked ? "not-allowed" : "pointer",
          color: isLocked ? c.textOnBg : "#ffffff",
        }}
      >
        {isCompleted ? (
          <CheckCircle2 size={isBoss ? 24 : 20} />
        ) : isLocked ? (
          <Lock size={isBoss ? 22 : 17} />
        ) : isBoss ? (
          <Skull size={22} />
        ) : isReview ? (
          <BookOpen size={17} />
        ) : (
          <span className="text-[15px] font-bold tabular-nums">{phase.number}</span>
        )}
      </button>

      {/* Stars on completed nodes */}
      {isCompleted && !isBoss && (
        <span
          className="absolute flex gap-0.5"
          style={{ bottom: -6, left: "50%", transform: "translateX(-50%)" }}
        >
          {[1, 2, 3].map((s) => (
            <Star
              key={s}
              size={8}
              fill={s <= Math.ceil(((phase.score ?? 0) / (phase.phrase_count || 1)) * 3) ? c.goldAccent : "none"}
              stroke={c.goldAccent}
              strokeWidth={1.5}
            />
          ))}
        </span>
      )}
    </div>
  );
}

// ── Main screen ───────────────────────────────────────────────────────────────
interface AdventureMapScreenProps {
  langCode: string;
  themeMode: AdventureThemeMode;
  chapters: AdventureChapter[];
  onStartChapter: (chapterId: number, phaseTitle: string, phaseNumber: number, chapterLevel: string) => void;
}

export default function AdventureMapScreen({ langCode, themeMode, chapters, onStartChapter }: AdventureMapScreenProps) {
  const s = useStrings();
  const effectiveLangCode = chapters[0]?.language_code ?? langCode;
  const c = getAdventureColors(effectiveLangCode, themeMode);

  const [entry, setEntry] = useState<{ phase: AdventurePhase; chapter: AdventureChapter; nodeRect: DOMRect | null } | null>(null);

  useEffect(() => {
    for (const chapter of chapters) {
      const cur = chapter.progress?.current_phase ?? 1;
      const phase = chapter.phases.find((p) => p.number === cur && !p.is_completed);
      if (phase) {
        const el = document.querySelector("[data-current-phase='true']");
        const nodeRect = el ? (el as HTMLElement).getBoundingClientRect() : null;
        setEntry({ phase, chapter, nodeRect });
        break;
      }
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="relative pb-8">

      {/* Ambient top glow */}
      <div
        className="pointer-events-none absolute left-0 right-0 top-0 h-64"
        style={{ background: `radial-gradient(ellipse at 50% 0%, ${c.ambientGlow}, transparent 70%)` }}
      />

      {/* Season sections */}
      {chapters.map((chapter, ci) => {
        const currentPhaseNumber = chapter.progress?.current_phase ?? 1;
        // A chapter is unlocked if it's the first, or the previous one has all phases done
        const isUnlocked = ci === 0 || chapters[ci - 1].phases.every((p) => p.is_completed);

        return (
          <div key={chapter.id}>
            {/* Season header */}
            <SeasonHeader chapter={chapter} index={ci} isUnlocked={isUnlocked} c={c} />

            {/* Winding map area */}
            <div className="relative mx-0" style={{ height: SEASON_HEIGHT }}>
              {/* Ambient glow */}
              <div
                className="pointer-events-none absolute inset-0"
                style={{
                  background: `radial-gradient(ellipse at 50% 40%, ${c.ambientGlow}, transparent 65%)`,
                }}
              />

              {/* SVG road path */}
              <svg
                width="100%"
                height={SEASON_HEIGHT}
                viewBox={`0 0 100 ${SEASON_HEIGHT}`}
                preserveAspectRatio="none"
                className="absolute inset-0"
                style={{ pointerEvents: "none" }}
              >
                {/* Road base */}
                <path d={PATH_D} fill="none" stroke={c.pathColor} strokeWidth="3.2" opacity="0.25" />
                {/* Road surface */}
                <path d={PATH_D} fill="none" stroke={c.pathColor} strokeWidth="2" opacity="0.5" />
                {/* Center dashes */}
                <path
                  d={PATH_D}
                  fill="none"
                  stroke={c.goldAccent}
                  strokeWidth="0.6"
                  strokeDasharray="5,8"
                  opacity="0.3"
                />
              </svg>

              {/* Phase nodes */}
              {chapter.phases.map((phase, pi) => {
                const pos = WINDING[pi] ?? { x: 50, y: 55 + pi * 62 };
                return (
                  <PhaseNode
                    key={phase.id}
                    phase={phase}
                    pos={pos}
                    currentPhaseNumber={currentPhaseNumber}
                    themeMode={themeMode}
                    c={c}
                    onClick={(rect) => {
                      if (phase.is_completed || phase.number !== currentPhaseNumber) return;
                      setEntry({ phase, chapter, nodeRect: rect });
                    }}
                  />
                );
              })}
            </div>

            {/* Decorative divider between seasons */}
            {ci < chapters.length - 1 && (
              <div className="px-8 py-2">
                <ItalianDivider index={ci} color={c.pathColor} />
              </div>
            )}
          </div>
        );
      })}

      {entry && (
        <PhaseEntry
          phase={entry.phase}
          nodeRect={entry.nodeRect}
          c={c}
          onClose={() => setEntry(null)}
          onStart={() => {
            setEntry(null);
            onStartChapter(entry.phase.id, entry.phase.title, entry.phase.number, entry.chapter.level);
          }}
        />
      )}
    </div>
  );
}
