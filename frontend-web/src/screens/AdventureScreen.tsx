import { ArrowRight, BookOpen, Lock, Skull, Swords } from "lucide-react";
import { useEffect, useState } from "react";

import LangFlag from "../components/ui/LangFlag";
import { useStrings } from "../contexts/StringsContext";
import { useImmersiveNav } from "../hooks/useImmersiveNav";
import { ROUTES } from "../constants/routes";
import { adventureService } from "../services/adventureService";
import { getAdventureColors } from "../theme/adventureColors";
import type { ApiAdventureChapter } from "../types/adventure";

interface AdventureScreenProps {
  langCode?: string;
}

export default function AdventureScreen({ langCode = "ES" }: AdventureScreenProps) {
  const s = useStrings();
  const { navigateImmersive } = useImmersiveNav();
  const [chapters, setChapters] = useState<ApiAdventureChapter[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    adventureService.listChapters()
      .then(all => setChapters(all.filter(ch => ch.language_code.toLowerCase() === langCode.toLowerCase())))
      .catch(() => setError(s.adventure.errorLoading))
      .finally(() => setLoading(false));
  }, [langCode]);

  if (loading) {
    return (
      <div
        className="-mx-3 -mt-3 overflow-hidden h-[calc(100dvh-3.5rem)] md:mx-0 md:mt-0 md:h-dvh flex items-center justify-center"
        style={{ background: "#1a0a00" }}
      >
        <p className="animate-pulse text-sm font-semibold" style={{ color: "rgba(255,255,255,0.40)" }}>
          {s.adventure.loading}
        </p>
      </div>
    );
  }

  if (error || chapters.length === 0) {
    return (
      <div
        className="-mx-3 -mt-3 overflow-hidden h-[calc(100dvh-3.5rem)] md:mx-0 md:mt-0 md:h-dvh flex flex-col items-center justify-center gap-3 px-8 text-center"
        style={{ background: "#1a0a00" }}
      >
        <p className="text-sm font-semibold" style={{ color: "rgba(255,255,255,0.40)" }}>
          {error ?? s.adventure.errorLoading}
        </p>
      </div>
    );
  }

  const LANG = chapters[0].language_code;
  const c    = getAdventureColors(LANG);

  const totalPhases     = chapters.reduce((s, ch) => s + ch.phases.length, 0);
  const completedPhases = chapters.reduce((s, ch) => s + ch.phases.filter(p => p.is_completed).length, 0);
  const progressPct     = Math.round((completedPhases / Math.max(totalPhases, 1)) * 100);

  const activeChapter = chapters.find(ch => ch.progress && !ch.phases.every(p => p.is_completed)) ?? chapters[0];
  const activePhase   = activeChapter.phases.find(p => !p.is_completed) ?? activeChapter.phases[0];

  function enter() {
    navigateImmersive(
      ROUTES.adventureMap,
      {},
      { title: activeChapter.title, subtitle: `${activeChapter.level} · Entrando no mundo`, langCode: LANG },
    );
  }

  return (
    <div
      className="-mx-3 -mt-3 overflow-hidden h-[calc(100dvh-3.5rem)] md:mx-0 md:mt-0 md:h-dvh"
      style={{ background: `linear-gradient(180deg, ${c.bgFrom} 0%, ${c.bgMid} 60%, ${c.bgTo} 100%)` }}
    >
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div className="absolute" style={{ top: "-5%", left: "20%", width: 700, height: 400, background: `radial-gradient(ellipse, ${c.ambientGlow}, transparent 70%)` }} />
        <div className="absolute" style={{ bottom: "10%", right: "-5%", width: 400, height: 400, background: `radial-gradient(circle, ${c.pathGlow}, transparent 70%)` }} />
      </div>

      <div className="relative z-10 flex h-full flex-col md:flex-row">

        {/* ── Painel hero ────────────────────────────────────────────── */}
        <div
          className="flex shrink-0 flex-col px-6 pt-6 pb-4 md:w-[340px] md:border-r md:px-8 md:py-10 md:pb-8"
          style={{ borderColor: `${c.pathColor}22` }}
        >
          <div className="flex items-center gap-2">
            <LangFlag code={LANG} size="sm" />
            <span
              className="rounded-full px-3 py-1 text-[10px] font-bold uppercase tracking-widest"
              style={{ background: `${c.seasonBadgeBg}28`, color: c.goldAccent, border: `1px solid ${c.seasonBadgeBg}38` }}
            >
              {chapters[0]?.level}
            </span>
          </div>

          <div className="mt-3">
            <p className="text-[10px] font-bold uppercase tracking-[0.2em]" style={{ color: `${c.parchment}40` }}>
              {s.adventure.adventureLabel}
            </p>
            <h1
              className="mt-0.5 text-4xl font-bold leading-none tracking-tight md:text-5xl"
              style={{ color: c.parchment, textShadow: `0 2px 24px ${c.pathGlow}` }}
            >
              {activeChapter.title}
            </h1>
          </div>

          <div className="mt-4">
            <div className="mb-1.5 flex items-center justify-between">
              <span className="text-[10px] font-bold uppercase tracking-widest" style={{ color: `${c.parchment}40` }}>
                {s.adventure.progress}
              </span>
              <span className="text-xs font-bold tabular-nums" style={{ color: c.goldAccent }}>
                {completedPhases}/{totalPhases}
              </span>
            </div>
            <div className="h-1.5 overflow-hidden rounded-full" style={{ background: "rgba(255,255,255,0.08)" }}>
              <div
                className="h-full rounded-full"
                style={{
                  width: `${progressPct || 2}%`,
                  background: `linear-gradient(90deg, ${c.nodeActive}, ${c.goldAccent})`,
                  boxShadow: `0 0 8px ${c.nodeActiveGlow}`,
                }}
              />
            </div>
          </div>

          <div className="hidden flex-1 md:block" />

          {activePhase && (
            <div
              className="mt-4 flex items-center gap-3 rounded-xl px-3.5 py-3"
              style={{
                background: `${activePhase.is_boss ? c.bossColor : c.nodeActive}15`,
                border: `1px solid ${activePhase.is_boss ? c.bossColor : c.nodeActive}30`,
              }}
            >
              <div
                className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full"
                style={{ background: activePhase.is_boss ? c.bossColor : activePhase.phase_type === "review" ? c.goldAccent : c.nodeActive }}
              >
                {activePhase.is_boss ? <Skull size={13} color={c.ctaText} />
                  : activePhase.phase_type === "review" ? <BookOpen size={13} color={c.ctaText} />
                  : <Swords size={13} color={c.ctaText} />}
              </div>
              <div className="min-w-0">
                <p className="text-[10px] font-bold uppercase tracking-wide" style={{ color: c.goldAccent }}>
                  {activePhase.is_boss
                    ? `${s.adventure.bossLabel} · ${activeChapter.level}`
                    : activePhase.phase_type === "review"
                    ? `${s.adventure.reviewLabel} · ${activeChapter.level}`
                    : `${s.adventure.nextPhase} · ${activeChapter.level}`}
                </p>
                <p className="truncate text-sm font-semibold leading-tight" style={{ color: c.parchment }}>
                  {activePhase.title}
                </p>
                {activePhase.npc_name && activePhase.phase_type === "story" && (
                  <p className="truncate text-[11px]" style={{ color: `${c.parchment}50` }}>
                    {s.adventure.withNpc(activePhase.npc_name)}
                  </p>
                )}
              </div>
            </div>
          )}

          <button
            type="button"
            onClick={enter}
            className="mt-3 flex w-full items-center justify-center gap-2.5 rounded-xl px-6 py-3.5 text-base font-bold shadow-xl transition active:scale-[0.98]"
            style={{
              background: `linear-gradient(135deg, ${c.ctaBg}, ${c.nodeActive})`,
              color: c.ctaText,
              boxShadow: `0 4px 20px ${c.nodeActiveGlow}`,
            }}
          >
            {completedPhases > 0 ? s.adventure.continueAdventure : s.adventure.beginAdventure}
            <ArrowRight size={18} strokeWidth={2.5} />
          </button>
        </div>

        {/* ── Lista de temporadas ───────────────────────────────────── */}
        <div className="flex-1 overflow-y-auto px-6 pb-6 md:px-10 md:py-10">
          <p
            className="mb-3 pt-5 text-[10px] font-bold uppercase tracking-widest md:pt-0"
            style={{ color: `${c.parchment}40` }}
          >
            {s.adventure.seasonsLabel}
          </p>

          <div className="flex flex-col">
            {chapters.map((ch, i) => {
              const done       = ch.phases.filter(p => p.is_completed).length;
              const isUnlocked = i === 0 || chapters[i - 1].phases.every(p => p.is_completed);
              const isCurrent  = ch.id === activeChapter.id;

              const Tag = isUnlocked ? "button" : "div";
              return (
                <Tag
                  key={ch.id}
                  type={isUnlocked ? "button" : undefined}
                  onClick={isUnlocked ? enter : undefined}
                  className={`relative flex w-full items-center gap-4 py-4 text-left transition ${isUnlocked ? "hover:brightness-110 active:scale-[0.99]" : ""}`}
                  style={{ borderBottom: `1px solid ${c.borderFaint}` }}
                >
                  {isCurrent && (
                    <div
                      className="absolute left-0 top-3 bottom-3 w-0.5 rounded-full"
                      style={{ background: c.nodeActive }}
                    />
                  )}

                  <span
                    className="shrink-0 rounded-lg px-2.5 py-1 text-[11px] font-bold uppercase tracking-wider"
                    style={
                      isUnlocked
                        ? { background: c.seasonBadgeBg, color: c.seasonBadgeText }
                        : { background: "rgba(255,255,255,0.05)", color: "rgba(255,255,255,0.18)" }
                    }
                  >
                    {ch.level}
                  </span>

                  <div className="min-w-0 flex-1">
                    <p
                      className="truncate text-sm font-semibold leading-tight md:text-base"
                      style={{ color: isUnlocked ? c.parchment : `${c.parchment}25` }}
                    >
                      {ch.title}
                    </p>
                    {isUnlocked && (
                      <div className="mt-2 flex flex-wrap gap-[2px]">
                        {ch.phases.map((p, pi) => (
                          <div
                            key={pi}
                            className="h-1 w-2.5 rounded-full"
                            style={{
                              background: p.is_completed
                                ? c.nodeCompleted
                                : pi === done && isCurrent
                                ? c.nodeActive
                                : p.phase_type === "review"
                                ? "rgba(217,119,6,0.20)"
                                : "rgba(255,255,255,0.10)",
                            }}
                          />
                        ))}
                      </div>
                    )}
                  </div>

                  {!isUnlocked ? (
                    <Lock size={13} style={{ color: "rgba(255,255,255,0.15)", flexShrink: 0 }} />
                  ) : done === ch.phases.length ? (
                    <span className="shrink-0 text-sm font-bold" style={{ color: c.nodeCompleted }}>✓</span>
                  ) : (
                    <span className="shrink-0 text-xs font-bold tabular-nums" style={{ color: isCurrent ? c.goldAccent : `${c.parchment}35` }}>
                      {done}/{ch.phases.length}
                    </span>
                  )}
                </Tag>
              );
            })}
          </div>
        </div>

      </div>
    </div>
  );
}
