import { Backpack, BookOpen, ChevronLeft, Map, Moon, Shield, Sun, Users } from "lucide-react";
import { useCallback, useEffect, useState } from "react";

import LangFlag from "../../components/ui/LangFlag";
import { useStrings } from "../../contexts/StringsContext";
import { useImmersiveNav } from "../../hooks/useImmersiveNav";
import { useAdventureChapters } from "../../hooks/useAdventureChapters";
import { getAdventureColors } from "../../theme/adventureColors";
import type { AdventureThemeMode } from "../../theme/adventureColors";
import AdventurePhaseRunner from "./abas/mapa/components/AdventurePhaseRunner/AdventurePhaseRunner";
import AdventureHeroScreen from "./abas/AdventureHeroScreen";
import AdventureMapScreen from "./abas/mapa/AdventureMapScreen";
import AdventureMochilaScreen from "./abas/AdventureMochilaScreen";
import AdventurePersonagensScreen from "./abas/AdventurePersonagensScreen";
import AdventureWordsScreen from "./abas/AdventureWordsScreen";
import AdventureOpeningCinematic from "./AdventureOpeningCinematic";
import DevJumpToPhaseModal from "./components/DevJumpToPhaseModal";

export type AdventureTab = "map" | "mochila" | "palavras" | "personagens" | "heroi";

interface AdventureModuleProps {
  langCode: string;
  sourceLangCode: string;
  initialTab: AdventureTab;
  chapterPath: (chapterId: number) => string;
  onBack: () => void;
  onTabChange: (tab: AdventureTab) => void;
}

export default function AdventureModule({
  langCode,
  sourceLangCode,
  initialTab,
  chapterPath,
  onBack,
  onTabChange,
}: AdventureModuleProps) {
  const s = useStrings();
  const [themeMode,   setThemeMode]   = useState<AdventureThemeMode>("dark");
  const [chapterView, setChapterView] = useState<{ phaseNumber: number; phaseId: number; startSectionIdx: number; keyWords: string[] } | null>(null);
  const [openingDone, setOpeningDone] = useState(() =>
    Boolean(localStorage.getItem(`fluenci_opening_${langCode.toLowerCase()}`)),
  );
  const [devModalOpen, setDevModalOpen] = useState(false);

  const { navigateImmersive } = useImmersiveNav();
  const { chapters, isLoading, error, completeSection, refresh, jumpToPhase } =
    useAdventureChapters(langCode);

  // Redirect to map if opening not yet seen and user lands on another tab
  useEffect(() => {
    if (!openingDone && initialTab !== "map") onTabChange("map");
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Re-sync chapters when returning from mobile immersive chapter screen
  useEffect(() => {
    function onPopState() { void refresh(); }
    function onSectionCompleteEvent(e: Event) {
      const { phaseId, newCount } = (e as CustomEvent<{ phaseId: number; newCount: number }>).detail;
      void completeSection(phaseId, newCount);
    }
    window.addEventListener("popstate", onPopState);
    window.addEventListener("talkly:section_complete", onSectionCompleteEvent);
    return () => {
      window.removeEventListener("popstate", onPopState);
      window.removeEventListener("talkly:section_complete", onSectionCompleteEvent);
    };
  }, [refresh, completeSection]);

  // ── Derived values ───────────────────────────────────────────────────────────
  const effectiveLangCode = chapters[0]?.language_code ?? langCode;
  const c                 = getAdventureColors(effectiveLangCode, themeMode);
  const totalPhases       = chapters.reduce((n, ch) => n + ch.phases.length, 0);
  const completedPhases   = chapters.reduce((n, ch) => n + ch.phases.filter(p => p.is_completed).length, 0);
  const progressPct       = totalPhases > 0 ? Math.round((completedPhases / totalPhases) * 100) : 0;
  const langName          = s.languages[effectiveLangCode.toUpperCase() as keyof typeof s.languages] ?? effectiveLangCode;
  const storyTitle        = chapters[0]?.title ?? langName;

  const TABS = [
    { id: "map"         as AdventureTab, label: s.adventure.tabMap,         Icon: Map      },
    { id: "mochila"     as AdventureTab, label: s.adventure.tabBag,         Icon: Backpack },
    { id: "palavras"    as AdventureTab, label: s.adventure.tabWords,       Icon: BookOpen },
    { id: "personagens" as AdventureTab, label: s.adventure.tabPersonagens, Icon: Users    },
    { id: "heroi"       as AdventureTab, label: s.adventure.tabHero,        Icon: Shield   },
  ];

  // ── Handlers ─────────────────────────────────────────────────────────────────
  const handleSectionComplete = useCallback((phaseId: number, newCount: number) => {
    void completeSection(phaseId, newCount);
  }, [completeSection]);

  const handleStartChapter = useCallback((
    chapterId: number,
    phaseTitle: string,
    phaseNumber: number,
    chapterLevel: string,
  ) => {
    const phase = chapters.flatMap(ch => ch.phases).find(p => p.id === chapterId);
    const startSectionIdx = phase?.completed_sections ?? 0;

    if (window.innerWidth >= 768) {
      setChapterView({ phaseNumber, phaseId: chapterId, startSectionIdx, keyWords: phase?.key_words ?? [] });
    } else {
      navigateImmersive(
        chapterPath(chapterId),
        { phaseNumber, langCode: effectiveLangCode, sourceLangCode, chapterId, startSectionIdx },
        {
          title:    phaseTitle,
          subtitle: `${chapterLevel} · ${s.adventure.phaseLabel(phaseNumber)} · ${langName}`,
          langCode: effectiveLangCode,
        },
      );
    }
  }, [chapters, chapterPath, effectiveLangCode, langName, navigateImmersive, s.adventure, sourceLangCode]);

  // ── Content renderer ─────────────────────────────────────────────────────────
  function renderTabContent() {
    if (isLoading) {
      return (
        <div className="flex h-full items-center justify-center">
          <p className="animate-pulse text-sm font-semibold" style={{ color: c.textOnBg }}>
            Carregando aventura...
          </p>
        </div>
      );
    }

    if (error) {
      return (
        <div className="flex h-full flex-col items-center justify-center gap-4 px-8 text-center">
          <p className="text-sm font-semibold" style={{ color: c.textOnBg }}>{error}</p>
          <button
            type="button"
            onClick={() => void refresh()}
            className="rounded-xl px-5 py-2.5 text-sm font-bold transition active:scale-[0.98]"
            style={{ background: c.ctaBg, color: c.ctaText }}
          >
            Tentar novamente
          </button>
        </div>
      );
    }

    if (chapterView) {
      return (
        <AdventurePhaseRunner
          phaseNumber={chapterView.phaseNumber}
          phaseId={chapterView.phaseId}
          keyWords={chapterView.keyWords}
          langCode={effectiveLangCode}
          sourceLangCode={sourceLangCode}
          startSectionIdx={chapterView.startSectionIdx}
          onSectionComplete={(n) => handleSectionComplete(chapterView.phaseId, n)}
          onBack={() => setChapterView(null)}
        />
      );
    }

    if (!openingDone && initialTab === "map") {
      return (
        <AdventureOpeningCinematic
          langCode={effectiveLangCode}
          onComplete={() => {
            localStorage.setItem(`fluenci_opening_${langCode.toLowerCase()}`, "1");
            setOpeningDone(true);
          }}
        />
      );
    }

    const mapProps = {
      langCode: effectiveLangCode,
      themeMode,
      chapters,
      onStartChapter: handleStartChapter,
    };

    return (
      <div
        className="adventure-scroll h-full overflow-y-auto"
        style={{
          "--adv-thumb":       `${c.pathColor}80`,
          "--adv-thumb-hover": `${c.goldAccent}cc`,
          "--adv-track":       c.surface,
          "--adv-glow":        c.nodeActiveGlow,
        } as React.CSSProperties}
      >
        {initialTab === "map"         && <AdventureMapScreen {...mapProps} />}
        {initialTab === "mochila"     && <AdventureMochilaScreen     langCode={effectiveLangCode} themeMode={themeMode} chapterSlug={chapters[0]?.slug} />}
        {initialTab === "palavras"    && <AdventureWordsScreen        langCode={effectiveLangCode} themeMode={themeMode} />}
        {initialTab === "personagens" && <AdventurePersonagensScreen  langCode={effectiveLangCode} themeMode={themeMode} chapterSlug={chapters[0]?.slug} />}
        {initialTab === "heroi"       && <AdventureHeroScreen         langCode={effectiveLangCode} themeMode={themeMode} storyTitle={storyTitle} />}
      </div>
    );
  }

  // ── Render ───────────────────────────────────────────────────────────────────
  return (
    <div
      className="h-dvh overflow-hidden"
      style={{ background: `linear-gradient(180deg, ${c.bgFrom} 0%, ${c.bgMid} 50%, ${c.bgTo} 100%)` }}
    >
      <div className="flex h-full flex-col md:flex-row">

        {/* ── Desktop sidebar ─────────────────────────────────────────────── */}
        <aside
          className="hidden md:flex md:w-80 md:shrink-0 md:flex-col"
          style={{
            background:    `${c.bgFrom}f5`,
            backdropFilter: "blur(20px)",
            borderRight:   `1px solid ${c.pathColor}30`,
          }}
        >
          {/* Back */}
          <div className="px-4 pt-5">
            <button
              type="button"
              onClick={onBack}
              className="flex w-full items-center gap-2 rounded-xl px-3 py-2.5 text-sm font-semibold transition active:scale-[0.98]"
              style={{ background: c.surface, color: c.parchment }}
            >
              <ChevronLeft size={15} />
              {s.adventure.exit}
            </button>
          </div>

          {/* Story header */}
          <div className="mt-5 px-5">
            <div className="flex items-center gap-2.5">
              <LangFlag code={effectiveLangCode} size="sm" />
              <div className="min-w-0">
                <p className="truncate text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
                  A1 · {langName}
                </p>
                <h2 className="truncate text-base font-bold leading-tight" style={{ color: c.parchment }}>
                  {storyTitle}
                </h2>
              </div>
            </div>
          </div>

          {/* Progress bar */}
          <div className="mt-4 px-5">
            <div className="mb-1.5 flex items-center justify-between">
              <p className="text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
                {s.adventure.progress}
              </p>
              <p className="text-xs font-bold tabular-nums" style={{ color: c.goldAccent }}>
                {completedPhases}/{totalPhases}
              </p>
            </div>
            <div className="h-1.5 overflow-hidden rounded-full" style={{ background: c.surface }}>
              <div
                className="h-full rounded-full transition-all duration-700"
                style={{
                  width:      `${progressPct || 2}%`,
                  background: `linear-gradient(90deg, ${c.nodeActive}, ${c.goldAccent})`,
                  boxShadow:  `0 0 6px ${c.nodeActiveGlow}`,
                }}
              />
            </div>
          </div>

          {/* Tab nav */}
          <nav className={`mt-6 space-y-1 px-3 ${(!openingDone && initialTab === "map") || chapterView ? "hidden" : ""}`}>
            {TABS.map(({ id, label, Icon }) => {
              const active = id === initialTab;
              return (
                <button
                  key={id}
                  type="button"
                  onClick={() => onTabChange(id)}
                  className="flex h-11 w-full items-center gap-3 rounded-xl px-3 text-left text-sm font-semibold transition"
                  style={
                    active
                      ? { background: `${c.nodeActive}22`, color: c.nodeActive, boxShadow: `inset 0 0 0 1px ${c.nodeActive}44` }
                      : { color: c.textOnBg }
                  }
                >
                  <Icon size={17} strokeWidth={active ? 2.5 : 1.8} />
                  {label}
                </button>
              );
            })}
          </nav>

          <div className="flex-1" />

          {/* Season overview */}
          <div className="px-4">
            <div className="rounded-xl p-3" style={{ background: c.surface }}>
              <p className="mb-2.5 text-[10px] font-bold uppercase tracking-wider" style={{ color: c.textFaint }}>
                Temporadas
              </p>
              <div className="space-y-2.5">
                {chapters.map((ch, i) => {
                  const done       = ch.phases.filter(p => p.is_completed).length;
                  const isUnlocked = i === 0 || chapters[i - 1].phases.every(p => p.is_completed);
                  const pct        = done > 0 ? Math.round((done / ch.phases.length) * 100) : 0;
                  return (
                    <div key={ch.id} className="flex items-center gap-2">
                      <span
                        className="shrink-0 rounded px-1.5 py-0.5 text-[9px] font-bold"
                        style={
                          isUnlocked
                            ? { background: c.seasonBadgeBg,  color: c.seasonBadgeText }
                            : { background: c.surfaceMid,      color: c.textFaint       }
                        }
                      >
                        {ch.level}
                      </span>
                      <div className="min-w-0 flex-1">
                        <div className="h-1 overflow-hidden rounded-full" style={{ background: c.borderFaint }}>
                          <div
                            className="h-full rounded-full"
                            style={{ width: `${pct}%`, background: isUnlocked ? c.nodeCompleted : c.textFaint }}
                          />
                        </div>
                      </div>
                      <span className="shrink-0 tabular-nums text-[10px]" style={{ color: c.textFaint }}>
                        {done}/{ch.phases.length}
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>

          {/* Theme toggle */}
          <div className="px-4 pb-2 pt-3">
            <button
              type="button"
              onClick={() => setThemeMode(m => m === "dark" ? "light" : "dark")}
              className="flex w-full items-center gap-2.5 rounded-xl px-3 py-2.5 text-sm font-semibold transition"
              style={{ background: c.surface, color: c.parchment }}
            >
              {themeMode === "dark" ? <Sun size={14} /> : <Moon size={14} />}
              <span style={{ color: c.textOnBg }}>
                {themeMode === "dark" ? "Modo dia" : "Modo noite"}
              </span>
            </button>
          </div>

          {/* DEV jump to phase */}
          <div className="px-4 pb-5">
            <button
              type="button"
              onClick={() => setDevModalOpen(true)}
              className="flex w-full items-center justify-center rounded-xl px-3 py-2 text-xs font-semibold transition"
              style={{ background: c.surfaceMid, color: c.textFaint }}
            >
              {s.adventure.devResetLabel}
            </button>
          </div>
        </aside>

        {/* ── Main content column ─────────────────────────────────────────── */}
        <div className="flex flex-1 flex-col overflow-hidden">

          {/* Mobile header — hidden during inline chapter view */}
          <header
            className={`shrink-0 flex items-center gap-3 px-4 py-3 md:hidden ${chapterView ? "hidden" : ""}`}
            style={{
              background:     `${c.bgFrom}e8`,
              backdropFilter: "blur(12px)",
              borderBottom:   `1px solid ${c.pathColor}20`,
            }}
          >
            <button
              type="button"
              onClick={onBack}
              className="flex shrink-0 items-center gap-1.5 rounded-full px-3 py-2 text-sm font-semibold transition"
              style={{ background: c.surface, color: c.parchment }}
            >
              <ChevronLeft size={15} />
              {s.adventure.exit}
            </button>

            <div className="flex flex-1 min-w-0 items-center gap-2">
              <LangFlag code={effectiveLangCode} size="xs" />
              <div className="min-w-0">
                <p className="truncate text-sm font-bold leading-tight" style={{ color: c.parchment }}>
                  {storyTitle}
                </p>
                <p className="text-[10px] font-semibold uppercase tracking-wider leading-tight" style={{ color: c.textFaint }}>
                  A1 · {langName}
                </p>
              </div>
            </div>

            <button
              type="button"
              onClick={() => setThemeMode(m => m === "dark" ? "light" : "dark")}
              className="grid h-8 w-8 shrink-0 place-items-center rounded-full transition"
              style={{ background: c.surface, color: c.parchment }}
            >
              {themeMode === "dark" ? <Sun size={14} /> : <Moon size={14} />}
            </button>

            <div className="shrink-0 rounded-lg px-3 py-1.5 text-right" style={{ background: c.surfaceMid }}>
              <p className="text-[9px] font-bold uppercase tracking-wide" style={{ color: c.goldAccent }}>
                {s.adventure.progress}
              </p>
              <p className="text-sm font-bold" style={{ color: c.parchment }}>
                {completedPhases}<span style={{ color: c.textFaint }}>/{totalPhases}</span>
              </p>
            </div>
          </header>

          {/* Tab content area */}
          <div className="flex-1 overflow-hidden">
            {renderTabContent()}
          </div>

          {/* Mobile bottom nav */}
          <nav
            className={`shrink-0 flex items-center ${(!openingDone && initialTab === "map") || chapterView ? "hidden" : "md:hidden"}`}
            style={{
              background:     `${c.bgFrom}f0`,
              backdropFilter: "blur(14px)",
              borderTop:      `1px solid ${c.borderFaint}`,
              height:         68,
            }}
          >
            {TABS.map(({ id, label, Icon }) => {
              const active = id === initialTab;
              return (
                <button
                  key={id}
                  type="button"
                  onClick={() => onTabChange(id)}
                  className="flex flex-1 flex-col items-center justify-center gap-1 transition"
                  style={{ color: active ? c.nodeActive : c.textFaint }}
                >
                  <div
                    className="flex h-8 w-8 items-center justify-center rounded-full transition"
                    style={active ? { background: `${c.nodeActive}25` } : {}}
                  >
                    <Icon size={20} strokeWidth={active ? 2.5 : 1.8} />
                  </div>
                  <span
                    className="text-[10px] font-bold uppercase tracking-wider"
                    style={active ? { color: c.nodeActive } : {}}
                  >
                    {label}
                  </span>
                </button>
              );
            })}
          </nav>

        </div>
      </div>

      {devModalOpen && chapters[0] && (
        <DevJumpToPhaseModal
          chapterSlug={chapters[0].slug}
          phasesCount={chapters[0].phases.length}
          onClose={() => setDevModalOpen(false)}
          onConfirm={(phaseNumber, sectionNumber) =>
            jumpToPhase(chapters[0].slug, phaseNumber, sectionNumber)
          }
        />
      )}
    </div>
  );
}
