import { BookOpen, Lock, RotateCcw, Sword } from "lucide-react";
import { useEffect, useState } from "react";

import { useStrings } from "../contexts/StringsContext";
import { adventureService } from "../services/adventureService";
import type { ApiAdventureChapter } from "../types/adventure";
import type { StudySessionData } from "../types/content";
import type { AppRoute } from "../types/navigation";
import ScenariosScreen from "./ScenariosScreen";
import StudySessionScreen from "./StudySessionScreen";

interface StudyScreenProps {
  onCompleted: () => void;
  onNavigate: (route: AppRoute) => void;
}

export default function StudyScreen({ onCompleted: _onCompleted, onNavigate }: StudyScreenProps) {
  const s = useStrings();
  const [tab, setTab]               = useState<"session" | "scenarios">("session");
  const [showSession, setShowSession] = useState(false);
  const [session, setSession]       = useState<StudySessionData | null>(null);
  const [chapters, setChapters]     = useState<ApiAdventureChapter[]>([]);
  const [loading, setLoading]       = useState(true);

  useEffect(() => {
    Promise.all([
      adventureService.getStudySession(),
      adventureService.listChapters(),
    ])
      .then(([sess, chs]) => { setSession(sess); setChapters(chs); })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  function refreshSession() {
    adventureService.getStudySession().then(setSession).catch(() => {});
  }

  // Next phase to continue (first incomplete phase across all chapters)
  let nextPhase: { name: string; phase: number; chapterTitle: string } | null = null;
  for (const ch of chapters) {
    const incomplete = ch.phases.find((p) => !p.is_completed);
    if (incomplete) {
      nextPhase = { name: incomplete.title, phase: incomplete.number, chapterTitle: ch.title };
      break;
    }
  }

  // Seasons = chapters, with real progress
  const seasons = chapters.map((ch, i) => ({
    id:     i + 1,
    name:   ch.title,
    done:   ch.phases.filter((p) => p.is_completed).length,
    total:  ch.phases.length,
    locked: i > 0 && !chapters[i - 1].phases.every((p) => p.is_completed),
  }));

  const dueCount = session?.due_count ?? 0;

  if (showSession && session && session.exercises.length > 0) {
    return (
      <StudySessionScreen
        exercises={session.exercises}
        onBack={() => setShowSession(false)}
        onComplete={() => { setShowSession(false); refreshSession(); }}
      />
    );
  }

  return (
    <div>
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
                <div className="min-w-0 flex-1">
                  <p className="study-hero-label">{s.study.continueAdventureHint}</p>
                  <p className="study-hero-title">
                    {nextPhase ? nextPhase.name : s.study.continueAdventureHint}
                  </p>
                  {nextPhase && (
                    <div className="mt-2 flex items-center gap-1.5">
                      <Sword size={12} className="study-hero-meta-icon" />
                      <p className="study-hero-meta">
                        {nextPhase.chapterTitle} · {s.adventure.phaseLabel(nextPhase.phase)}
                      </p>
                    </div>
                  )}
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
                  onClick={(e) => {
                    e.stopPropagation();
                    if (dueCount > 0) setShowSession(true);
                  }}
                  disabled={dueCount === 0}
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
                  {loading ? (
                    <p className="mt-0.5 text-sm font-semibold text-slate-400">{s.states.loading}</p>
                  ) : dueCount === 0 ? (
                    <p className="mt-0.5 text-sm font-semibold text-slate-400">{s.study.sessionEmpty}</p>
                  ) : (
                    <p className="mt-0.5 text-sm font-semibold text-slate-950">
                      {s.study.reviewNowWords(dueCount)} {s.study.reviewNowSubtitle}
                    </p>
                  )}
                </div>
              </div>
              <button
                type="button"
                onClick={() => dueCount > 0 && setShowSession(true)}
                disabled={loading || dueCount === 0}
                className="area-btn h-10 shrink-0 rounded-[8px] px-4 text-sm font-semibold transition disabled:opacity-40"
              >
                {s.study.reviewBtn}
              </button>
            </div>
          </div>

          {/* Temporadas */}
          {(loading || seasons.length > 0) && (
            <section>
              <p className="mb-2 text-xs font-semibold uppercase text-slate-400">{s.study.seasonsTitle}</p>
              {loading ? (
                <div className="card p-4 text-sm text-slate-400">{s.states.loading}</div>
              ) : (
                <div className="card divide-y divide-slate-100">
                  {seasons.map((season) => (
                    <div key={season.id} className={`flex items-center gap-3 px-4 py-3.5 ${season.locked ? "opacity-40" : ""}`}>
                      {season.locked
                        ? <Lock size={13} className="shrink-0 text-slate-400" />
                        : <span className="w-[13px] shrink-0 text-center text-xs font-bold tabular-nums area-text-primary">{season.id}</span>
                      }
                      <div className="min-w-0 flex-1">
                        <div className="flex items-center justify-between gap-2">
                          <p className={`truncate text-sm font-semibold ${season.locked ? "text-slate-400" : "text-slate-950"}`}>
                            {season.name}
                          </p>
                          <p className="shrink-0 text-xs font-semibold tabular-nums text-slate-400">
                            {season.locked ? "—" : `${season.done}/${season.total}`}
                          </p>
                        </div>
                        {!season.locked && (
                          <div className="study-season-bar mt-1.5">
                            <div className="study-season-fill" style={{ width: `${season.total > 0 ? (season.done / season.total) * 100 : 0}%` }} />
                          </div>
                        )}
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </section>
          )}

          {/* Empty state — no words yet */}
          {!loading && session?.total === 0 && (
            <div className="rounded-xl border border-slate-100 bg-slate-50 p-5 text-center">
              <p className="text-sm font-semibold text-slate-950">{s.study.noWordsTitle}</p>
              <p className="mt-1 text-xs font-medium text-slate-400">{s.study.noWordsDetail}</p>
            </div>
          )}

        </div>
      )}
    </div>
  );
}
