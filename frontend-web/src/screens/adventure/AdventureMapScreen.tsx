import { BookOpen, CheckCircle2, ChevronLeft, Lock, Skull, Star, Swords, X } from "lucide-react";
import { useState } from "react";

import LangFlag from "../../components/ui/LangFlag";
import { ADVENTURE_IT_MOCK } from "../../mocks/adventureItMock";
import { getAdventureColors } from "../../theme/adventureColors";
import type { AdventureChapter, AdventurePhase } from "../../types/adventure";

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
        background: isLocked ? "rgba(0,0,0,0.35)" : `${c.seasonBadgeBg}22`,
        border: `1px solid ${isLocked ? "rgba(255,255,255,0.06)" : c.seasonBadgeBg + "44"}`,
      }}
    >
      <div className="flex items-center justify-between gap-3">
        <div className="flex items-center gap-2">
          <span
            className="rounded-md px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider"
            style={
              isLocked
                ? { background: "rgba(255,255,255,0.08)", color: "rgba(255,255,255,0.3)" }
                : { background: c.seasonBadgeBg, color: c.seasonBadgeText }
            }
          >
            {chapter.level}
          </span>
          <span
            className="text-[10px] font-semibold uppercase tracking-widest"
            style={{ color: isLocked ? "rgba(255,255,255,0.18)" : `${c.parchment}60` }}
          >
            A1 · Il Viandante
          </span>
        </div>
        {isLocked && <Lock size={13} style={{ color: "rgba(255,255,255,0.2)" }} />}
      </div>
      <p
        className="mt-1 text-base font-semibold leading-tight"
        style={{ color: isLocked ? "rgba(255,255,255,0.25)" : c.parchment }}
      >
        {chapter.title}
      </p>
      {!isLocked && (
        <p className="mt-1 text-xs font-medium" style={{ color: c.parchmentSubtext }}>
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
  c,
  onClick,
}: {
  phase: AdventurePhase;
  pos: { x: number; y: number };
  currentPhaseNumber: number;
  c: ReturnType<typeof getAdventureColors>;
  onClick: () => void;
}) {
  const isCompleted = phase.is_completed;
  const isCurrent   = phase.number === currentPhaseNumber && !phase.is_completed;
  const isLocked    = !isCompleted && !isCurrent;
  const isBoss      = phase.is_boss;
  const isReview    = phase.phase_type === "review";

  const size   = isBoss ? 64 : 54;
  const bg     = isCompleted ? c.nodeCompleted
               : isCurrent && isBoss   ? c.bossColor
               : isCurrent && isReview ? c.goldAccent
               : isCurrent             ? c.nodeActive
               : isLocked && isBoss    ? "#2a0d0d"
               : isLocked && isReview  ? "#1a1200"
               : c.nodeLocked;

  const activeColor = isBoss ? c.bossColor : isReview ? c.goldAccent : c.nodeActive;
  const boxShadow = isCurrent
    ? `0 0 0 3px ${activeColor}, 0 0 28px ${isBoss ? c.bossGlow : c.nodeActiveGlow}`
    : isCompleted
    ? `0 0 0 2px ${c.nodeCompleted}80, 0 4px 12px rgba(0,0,0,0.5)`
    : "0 4px 14px rgba(0,0,0,0.55)";

  return (
    <button
      type="button"
      disabled={isLocked}
      onClick={onClick}
      className="absolute flex items-center justify-center rounded-full font-bold text-white transition"
      style={{
        left: `${pos.x}%`,
        top: pos.y,
        transform: "translate(-50%, -50%)",
        width: size,
        height: size,
        background: bg,
        boxShadow,
        animation: isCurrent ? "adventureBounce 1.4s ease-in-out infinite" : undefined,
        zIndex: isCurrent ? 2 : 1,
        opacity: isLocked ? 0.45 : 1,
        cursor: isLocked ? "not-allowed" : "pointer",
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

      {/* Stars on completed nodes */}
      {isCompleted && !isBoss && (
        <span className="absolute -bottom-5 flex gap-0.5">
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
    </button>
  );
}

// ── Phase bottom sheet ────────────────────────────────────────────────────────
function PhaseSheet({
  phase,
  chapter,
  c,
  onClose,
  onStart,
}: {
  phase: AdventurePhase;
  chapter: AdventureChapter;
  c: ReturnType<typeof getAdventureColors>;
  onClose: () => void;
  onStart: () => void;
}) {
  return (
    <div
      className="fixed inset-0 z-40 flex items-end"
      style={{ background: "rgba(0,0,0,0.70)" }}
      onClick={onClose}
    >
      <div
        className="w-full rounded-t-2xl p-5 pb-8"
        style={{
          background: `linear-gradient(180deg, ${c.bgMid} 0%, ${c.bgFrom} 100%)`,
          border: `1px solid ${c.pathColor}30`,
          borderBottom: "none",
          animation: "sheetSlideUp 220ms ease-out both",
          maxHeight: "80vh",
          overflowY: "auto",
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="mb-4 flex items-start justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <p
                className="text-xs font-bold uppercase tracking-wide"
                style={{
                  color: phase.is_boss ? c.bossColor
                       : phase.phase_type === "review" ? c.goldAccent
                       : c.goldAccent,
                }}
              >
                {phase.is_boss ? "⚔️ Fase Boss"
                : phase.phase_type === "review" ? "📚 Revisão"
                : `Fase ${phase.number} · ${chapter.level}`}
              </p>
              {phase.npc_name && phase.phase_type === "story" && (
                <span className="text-[11px] font-medium" style={{ color: `${c.parchment}55` }}>
                  com {phase.npc_name}
                </span>
              )}
            </div>
            <h3 className="mt-1 text-xl font-semibold" style={{ color: c.parchment }}>
              {phase.title}
            </h3>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="grid h-9 w-9 shrink-0 place-items-center rounded-full transition"
            style={{ background: "rgba(255,255,255,0.08)", color: c.parchment }}
          >
            <X size={17} />
          </button>
        </div>

        {/* Narrative snippet */}
        <div
          className="rounded-xl p-4"
          style={{ background: c.parchment + "14", border: `1px solid ${c.parchmentBorder}` }}
        >
          <p className="text-sm font-medium leading-6" style={{ color: `${c.parchment}CC` }}>
            {phase.narrative_intro}
          </p>
        </div>

        {/* Keywords */}
        {phase.key_words?.length ? (
          <div className="mt-3 flex flex-wrap gap-1.5">
            {phase.key_words.map((kw) => (
              <span
                key={kw}
                className="rounded-full px-3 py-1 text-[11px] font-semibold"
                style={{ background: c.goldAccentSoft, color: c.goldAccent }}
              >
                {kw}
              </span>
            ))}
          </div>
        ) : null}

        {/* Meta */}
        <p className="mt-3 text-xs font-semibold" style={{ color: `${c.parchment}50` }}>
          {phase.phrase_count} frases
          {phase.is_completed && phase.score !== null
            ? ` · Concluída · ${phase.score} pts`
            : phase.is_completed
            ? " · Concluída"
            : ""}
        </p>

        {/* CTA */}
        <button
          type="button"
          onClick={onStart}
          className="mt-5 flex w-full items-center justify-center gap-2 rounded-xl px-5 py-4 text-base font-semibold transition active:scale-[0.98]"
          style={{
            background: phase.is_completed
              ? "rgba(255,255,255,0.12)"
              : phase.is_boss
              ? c.bossColor
              : c.ctaBg,
            color: c.ctaText,
          }}
        >
          {phase.is_completed ? (
            <><Star size={18} /> Jogar novamente</>
          ) : phase.is_boss ? (
            <><Skull size={18} /> Enfrentar o Chefe</>
          ) : (
            <><Swords size={18} /> Iniciar Fase</>
          )}
        </button>
      </div>
    </div>
  );
}

// ── Main screen ───────────────────────────────────────────────────────────────
interface AdventureMapScreenProps {
  langCode: string;
  onBack: () => void;
  onStartChapter: (chapterId: number) => void;
}

export default function AdventureMapScreen({ langCode, onBack, onStartChapter }: AdventureMapScreenProps) {
  // TODO: replace mock with real API — adventureService.listChapters()
  // When using mock, derive language from the mock data itself (not from the active goal)
  const chapters = ADVENTURE_IT_MOCK;
  const effectiveLangCode = chapters[0]?.language_code ?? langCode;
  const c = getAdventureColors(effectiveLangCode);
  const [selectedPhase, setSelectedPhase] = useState<{ phase: AdventurePhase; chapter: AdventureChapter } | null>(null);

  return (
    <div className="relative pb-8">
      {/* Fixed top header */}
      <div
        className="sticky top-0 z-20 flex items-center gap-3 px-4 py-3"
        style={{
          background: `${c.bgFrom}e8`,
          backdropFilter: "blur(12px)",
          borderBottom: `1px solid ${c.pathColor}20`,
        }}
      >
        <button
          type="button"
          onClick={onBack}
          className="flex shrink-0 items-center gap-1.5 rounded-full px-3 py-2 text-sm font-semibold transition"
          style={{ background: "rgba(255,255,255,0.08)", color: c.parchment }}
        >
          <ChevronLeft size={15} />
          Sair
        </button>
        <div className="flex flex-1 min-w-0 items-center gap-2">
          <LangFlag code={effectiveLangCode} size="xs" />
          <div className="min-w-0">
            <p className="truncate text-sm font-bold leading-tight" style={{ color: c.parchment }}>Il Viandante</p>
            <p className="text-[10px] font-semibold uppercase tracking-wider leading-tight" style={{ color: `${c.parchment}55` }}>A1 · Italiano</p>
          </div>
        </div>
        <div
          className="shrink-0 rounded-lg px-3 py-1.5 text-right"
          style={{ background: "rgba(0,0,0,0.35)" }}
        >
          <p className="text-[9px] font-bold uppercase tracking-wide" style={{ color: c.goldAccent }}>Progresso</p>
          <p className="text-sm font-bold" style={{ color: c.parchment }}>
            {chapters.reduce((s, ch) => s + ch.phases.filter(p => p.is_completed).length, 0)}
            <span style={{ color: `${c.parchment}50` }}>/{chapters.reduce((s, ch) => s + ch.phases.length, 0)}</span>
          </p>
        </div>
      </div>

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
                    c={c}
                    onClick={() => {
                      if (!phase.is_completed && phase.number !== currentPhaseNumber) return;
                      setSelectedPhase({ phase, chapter });
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

      {/* Phase bottom sheet */}
      {selectedPhase && (
        <PhaseSheet
          phase={selectedPhase.phase}
          chapter={selectedPhase.chapter}
          c={c}
          onClose={() => setSelectedPhase(null)}
          onStart={() => {
            setSelectedPhase(null);
            onStartChapter(selectedPhase.chapter.id);
          }}
        />
      )}
    </div>
  );
}
