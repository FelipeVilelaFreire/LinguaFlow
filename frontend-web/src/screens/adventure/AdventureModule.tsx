import { Backpack, ChevronLeft, Map, Moon, Shield, Sun } from "lucide-react";
import { useEffect, useState } from "react";

import LangFlag from "../../components/ui/LangFlag";
import { useStrings } from "../../contexts/StringsContext";
import { useImmersiveNav } from "../../hooks/useImmersiveNav";
import { ADVENTURE_IT_MOCK } from "../../mocks/adventureItMock";
import { getAdventureColors } from "../../theme/adventureColors";
import type { AdventureThemeMode } from "../../theme/adventureColors";
import AdventureChapterSections from "./AdventureChapterSections";
import AdventureHeroScreen from "./AdventureHeroScreen";
import AdventureMapScreen from "./AdventureMapScreen";
import AdventureMochilaScreen from "./AdventureMochilaScreen";
import AdventureOpeningCinematic from "./AdventureOpeningCinematic";

export type AdventureTab = "map" | "mochila" | "heroi";

interface AdventureModuleProps {
  langCode: string;
  initialTab: AdventureTab;
  chapterPath: (chapterId: number) => string;
  onBack: () => void;
  onTabChange: (tab: AdventureTab) => void;
}

export default function AdventureModule({
  langCode,
  initialTab,
  chapterPath,
  onBack,
  onTabChange,
}: AdventureModuleProps) {
  const s = useStrings();
  const [themeMode,   setThemeMode]   = useState<AdventureThemeMode>("dark");
  const [chapterView, setChapterView] = useState<{ phaseNumber: number } | null>(null);
  const [openingDone, setOpeningDone] = useState(() => Boolean(localStorage.getItem("talkly_opening_it")));
  const { navigateImmersive } = useImmersiveNav();

  // Redirect to map if opening not yet seen and user lands on mochila/heroi directly
  useEffect(() => {
    if (!openingDone && initialTab !== "map") {
      onTabChange("map");
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const chapters          = ADVENTURE_IT_MOCK;
  const effectiveLangCode = chapters[0]?.language_code ?? langCode;
  const c                 = getAdventureColors(effectiveLangCode, themeMode);
  const totalPhases       = chapters.reduce((n, ch) => n + ch.phases.length, 0);
  const completedPhases   = chapters.reduce((n, ch) => n + ch.phases.filter(p => p.is_completed).length, 0);
  const progressPct       = totalPhases > 0 ? Math.round((completedPhases / totalPhases) * 100) : 0;
  const langName          = s.languages[effectiveLangCode.toUpperCase() as keyof typeof s.languages] ?? effectiveLangCode;

  const TABS = [
    { id: "map"     as AdventureTab, label: s.adventure.tabMap,  Icon: Map     },
    { id: "mochila" as AdventureTab, label: s.adventure.tabBag,  Icon: Backpack },
    { id: "heroi"   as AdventureTab, label: s.adventure.tabHero, Icon: Shield  },
  ];

  const contentProps = {
    langCode: effectiveLangCode,
    themeMode,
    onStartChapter: (chapterId: number, phaseTitle: string, phaseNumber: number, chapterLevel: string) => {
      if (window.innerWidth >= 768) {
        setChapterView({ phaseNumber });
      } else {
        navigateImmersive(chapterPath(chapterId), { phaseNumber, langCode: effectiveLangCode }, {
          title: phaseTitle,
          subtitle: `${chapterLevel} · ${s.adventure.phaseLabel(phaseNumber)} · ${langName}`,
          langCode: effectiveLangCode,
        });
      }
    },
  };

  return (
    <div
      className="h-dvh overflow-hidden"
      style={{ background: `linear-gradient(180deg, ${c.bgFrom} 0%, ${c.bgMid} 50%, ${c.bgTo} 100%)` }}
    >
      <div className="flex h-full flex-col md:flex-row">

        {/* ── Desktop sidebar (hidden on mobile) ─────────────────────────── */}
        <aside
          className="hidden md:flex md:w-80 md:shrink-0 md:flex-col"
          style={{
            background: `${c.bgFrom}f5`,
            backdropFilter: "blur(20px)",
            borderRight: `1px solid ${c.pathColor}30`,
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

          {/* Story info */}
          <div className="mt-5 px-5">
            <div className="flex items-center gap-2.5">
              <LangFlag code={effectiveLangCode} size="sm" />
              <div className="min-w-0">
                <p className="truncate text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
                  A1 · {langName}
                </p>
                <h2 className="truncate text-base font-bold leading-tight" style={{ color: c.parchment }}>
                  Il Viandante
                </h2>
              </div>
            </div>
          </div>

          {/* Progress */}
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
                  width: `${progressPct || 2}%`,
                  background: `linear-gradient(90deg, ${c.nodeActive}, ${c.goldAccent})`,
                  boxShadow: `0 0 6px ${c.nodeActiveGlow}`,
                }}
              />
            </div>
          </div>

          {/* Tab navigation */}
          <nav className="mt-6 space-y-1 px-3">
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

          {/* Spacer */}
          <div className="flex-1" />

          {/* Season mini-overview */}
          <div className="px-4">
            <div className="rounded-xl p-3" style={{ background: c.surface }}>
              <p className="mb-2.5 text-[10px] font-bold uppercase tracking-wider" style={{ color: c.textFaint }}>
                Temporadas
              </p>
              <div className="space-y-2.5">
                {chapters.map((ch, i) => {
                  const done      = ch.phases.filter(p => p.is_completed).length;
                  const isUnlocked = i === 0 || chapters[i - 1].phases.every(p => p.is_completed);
                  const pct       = done > 0 ? Math.round((done / ch.phases.length) * 100) : 0;
                  return (
                    <div key={ch.id} className="flex items-center gap-2">
                      <span
                        className="shrink-0 rounded px-1.5 py-0.5 text-[9px] font-bold"
                        style={
                          isUnlocked
                            ? { background: c.seasonBadgeBg, color: c.seasonBadgeText }
                            : { background: c.surfaceMid, color: c.textFaint }
                        }
                      >
                        {ch.level}
                      </span>
                      <div className="min-w-0 flex-1">
                        <div className="h-1 overflow-hidden rounded-full" style={{ background: c.borderFaint }}>
                          <div
                            className="h-full rounded-full"
                            style={{
                              width: `${pct}%`,
                              background: isUnlocked ? c.nodeCompleted : c.textFaint,
                            }}
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
          <div className="px-4 pb-5 pt-3">
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
        </aside>

        {/* ── Main content column ─────────────────────────────────────────── */}
        <div className="flex flex-1 flex-col overflow-hidden">

          {/* Mobile header (hidden on desktop) */}
          <header
            className="shrink-0 flex items-center gap-3 px-4 py-3 md:hidden"
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
              style={{ background: c.surface, color: c.parchment }}
            >
              <ChevronLeft size={15} />
              {s.adventure.exit}
            </button>
            <div className="flex flex-1 min-w-0 items-center gap-2">
              <LangFlag code={effectiveLangCode} size="xs" />
              <div className="min-w-0">
                <p className="truncate text-sm font-bold leading-tight" style={{ color: c.parchment }}>
                  Il Viandante
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

          {/* Tab content / inline chapter / opening cinematic */}
          <div className="flex-1 overflow-hidden">
            {chapterView ? (
              <AdventureChapterSections
                phaseNumber={chapterView.phaseNumber}
                langCode={effectiveLangCode}
                onBack={() => setChapterView(null)}
              />
            ) : !openingDone && initialTab === "map" ? (
              <AdventureOpeningCinematic
                langCode={effectiveLangCode}
                onComplete={() => {
                  localStorage.setItem("talkly_opening_it", "1");
                  setOpeningDone(true);
                }}
              />
            ) : (
              <div className="h-full overflow-y-auto">
                {initialTab === "map" && (
                  <AdventureMapScreen {...contentProps} />
                )}
                {initialTab === "mochila" && (
                  <AdventureMochilaScreen langCode={effectiveLangCode} themeMode={themeMode} />
                )}
                {initialTab === "heroi" && (
                  <AdventureHeroScreen langCode={effectiveLangCode} themeMode={themeMode} />
                )}
              </div>
            )}
          </div>

          {/* Mobile bottom nav (hidden on desktop and during opening cinematic) */}
          <nav
            className={`shrink-0 flex items-center ${(!openingDone && initialTab === "map") ? "hidden" : "md:hidden"}`}
            style={{
              background: `${c.bgFrom}f0`,
              backdropFilter: "blur(14px)",
              borderTop: `1px solid ${c.borderFaint}`,
              height: 68,
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
    </div>
  );
}
