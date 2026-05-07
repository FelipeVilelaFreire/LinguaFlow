import { ArrowRight, BookOpen, Lock, RotateCcw, Sword } from "lucide-react";
import { useState } from "react";

import { useStrings } from "../contexts/StringsContext";
import type { AppRoute } from "../types/navigation";
import ScenariosScreen from "./ScenariosScreen";

interface StudyScreenProps {
  onCompleted: () => void;
  onNavigate: (route: AppRoute) => void;
}

const REVIEW_COUNT = 12;

const NEXT_PHASE = {
  name: "Saudações e apresentações",
  season: 1,
  phase: 3,
  seasonName: "Chegada ao Vilarejo",
  estimatedMin: 15,
};

const SEASONS = [
  { id: 1, name: "Chegada ao Vilarejo",     done: 8,  total: 10, locked: false },
  { id: 2, name: "A Guilda dos Mercadores", done: 3,  total: 10, locked: false },
  { id: 3, name: "A Floresta das Runas",    done: 0,  total: 10, locked: true  },
  { id: 4, name: "A Fortaleza do Norte",    done: 0,  total: 10, locked: true  },
  { id: 5, name: "O Boss Final",            done: 0,  total: 10, locked: true  },
];

export default function StudyScreen({ onCompleted: _onCompleted, onNavigate }: StudyScreenProps) {
  const s = useStrings();
  const [tab, setTab] = useState<"session" | "scenarios">("session");

  return (
    <div>
      {/* Tab switcher */}
      <div className="mb-4 grid grid-cols-2 gap-1 rounded-[8px] bg-slate-100 p-1">
        <button
          type="button"
          onClick={() => setTab("session")}
          className={`h-10 rounded-[6px] text-sm font-semibold transition ${tab === "session" ? "bg-white text-slate-950 shadow-sm" : "text-slate-500 hover:text-slate-700"}`}
        >
          {s.today.tabSession}
        </button>
        <button
          type="button"
          onClick={() => setTab("scenarios")}
          className={`h-10 rounded-[6px] text-sm font-semibold transition ${tab === "scenarios" ? "bg-white text-slate-950 shadow-sm" : "text-slate-500 hover:text-slate-700"}`}
        >
          {s.today.tabScenarios}
        </button>
      </div>

      {tab === "scenarios" ? <ScenariosScreen /> : (
        <div className="flex flex-col gap-4" style={{ animation: "fadeIn 260ms ease-out" }}>

          {/* Hero — Continuar aventura */}
          <div className="study-hero-card" onClick={() => onNavigate("adventure")}>
            <div className="study-hero-bg" />
            <div className="relative z-10 flex flex-col gap-4 p-5">
              <div className="flex items-start justify-between gap-3">
                <div className="flex-1 min-w-0">
                  <p className="study-hero-label">{s.study.continueAdventureHint}</p>
                  <p className="study-hero-title">{NEXT_PHASE.name}</p>
                  <div className="mt-2 flex items-center gap-1.5">
                    <Sword size={12} className="study-hero-meta-icon" />
                    <p className="study-hero-meta">T{NEXT_PHASE.season} · Fase {NEXT_PHASE.phase} · {NEXT_PHASE.seasonName}</p>
                  </div>
                </div>
                <div className="study-hero-time shrink-0">
                  ~{NEXT_PHASE.estimatedMin} min
                </div>
              </div>
              <div className="grid grid-cols-2 gap-2">
                <button
                  type="button"
                  className="study-hero-btn-secondary"
                  onClick={(e) => { e.stopPropagation(); onNavigate("adventure"); }}
                >
                  <Sword size={15} strokeWidth={2} />
                  {s.study.continueAdventureBtn}
                </button>
                <button
                  type="button"
                  className="study-hero-btn"
                  onClick={(e) => { e.stopPropagation(); }}
                >
                  {s.study.studyNowBtn}
                  <BookOpen size={15} strokeWidth={2.5} />
                </button>
              </div>
            </div>
          </div>

          {/* Revisar agora */}
          <div className="card p-4">
            <div className="flex items-center justify-between gap-4">
              <div className="flex items-center gap-3">
                <div className="area-bg-soft flex h-10 w-10 shrink-0 items-center justify-center rounded-[8px]">
                  <RotateCcw size={16} className="area-text-primary" />
                </div>
                <div>
                  <p className="text-xs font-semibold uppercase text-slate-400">{s.study.reviewNowTitle}</p>
                  <p className="mt-0.5 text-sm font-semibold text-slate-950">
                    {REVIEW_COUNT} {s.study.reviewNowSubtitle}
                  </p>
                </div>
              </div>
              <button type="button" className="area-btn rounded-[8px] h-10 px-4 text-sm font-semibold shrink-0 transition">
                {s.study.reviewBtn}
              </button>
            </div>
          </div>

          {/* Temporadas */}
          <section>
            <p className="mb-2 text-xs font-semibold uppercase text-slate-400">{s.study.seasonsTitle}</p>
            <div className="card divide-y divide-slate-100">
              {SEASONS.map((season) => (
                <div key={season.id} className={`flex items-center gap-3 px-4 py-3.5 ${season.locked ? "opacity-40" : ""}`}>
                  {season.locked
                    ? <Lock size={13} className="shrink-0 text-slate-400" />
                    : <span className="w-[13px] shrink-0 text-center text-xs font-bold tabular-nums area-text-primary">{season.id}</span>
                  }
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between gap-2">
                      <p className={`text-sm font-semibold truncate ${season.locked ? "text-slate-400" : "text-slate-950"}`}>
                        {season.name}
                      </p>
                      <p className="text-xs font-semibold text-slate-400 shrink-0 tabular-nums">
                        {season.locked ? "—" : `${season.done}/${season.total}`}
                      </p>
                    </div>
                    {!season.locked && (
                      <div className="study-season-bar mt-1.5">
                        <div className="study-season-fill" style={{ width: `${(season.done / season.total) * 100}%` }} />
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </section>

        </div>
      )}
    </div>
  );
}
