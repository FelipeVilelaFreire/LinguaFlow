import { BookOpen, RotateCcw, Sword } from "lucide-react";
import { useEffect, useState } from "react";

import { useStrings } from "../../../contexts/StringsContext";
import { adventureService } from "../../../services/adventureService";
import { contentService } from "../../../services/contentService";
import type { ApiAdventureChapter } from "../../../types/adventure";
import type { Phrase, StudyLesson, StudyModule, StudySessionData } from "../../../types/content";
import type { AppRoute } from "../../../types/navigation";
import GuidedLessonRunner from "./GuidedLessonRunner";
import ScenariosScreen from "./ScenariosScreen";
import StudySessionScreen from "./StudySessionScreen";

interface StudyScreenProps {
  onCompleted: () => void;
  onNavigate: (route: AppRoute) => void;
}

export default function StudyScreen({ onCompleted: _onCompleted, onNavigate }: StudyScreenProps) {
  const s = useStrings();
  const [tab, setTab]                         = useState<"guided" | "scenarios">("guided");
  const [showSession, setShowSession]         = useState(false);
  const [showGuidedStudy, setShowGuidedStudy] = useState(false);
  const [session, setSession]                 = useState<StudySessionData | null>(null);
  const [chapters, setChapters]               = useState<ApiAdventureChapter[]>([]);
  const [modules, setModules]                 = useState<StudyModule[]>([]);
  const [loading, setLoading]                 = useState(true);
  const [currentLessonPhrases, setCurrentLessonPhrases]               = useState<Phrase[]>([]);
  const [currentLessonPhrasesLoading, setCurrentLessonPhrasesLoading] = useState(false);

  useEffect(() => {
    Promise.all([
      adventureService.getStudySession(),
      adventureService.listChapters(),
      contentService.listStudyModules(),
    ])
      .then(([sess, chs, mods]) => { setSession(sess); setChapters(chs); setModules(mods); })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  function refreshSession() {
    adventureService.getStudySession().then(setSession).catch(() => {});
  }

  // Current adventure phase = first incomplete phase across all chapters
  let currentAdventurePhase: number | null = null;
  let nextPhase: { name: string; phase: number; chapterTitle: string } | null = null;
  for (const ch of chapters) {
    const incomplete = ch.phases.find((p) => !p.is_completed);
    if (incomplete) {
      currentAdventurePhase = incomplete.number;
      nextPhase = { name: incomplete.title, phase: incomplete.number, chapterTitle: ch.title };
      break;
    }
  }

  // Current lesson = module lesson matching current adventure phase (fallback: first lesson)
  let currentLesson: StudyLesson | null = null;
  for (const mod of modules) {
    const match = currentAdventurePhase !== null
      ? mod.lessons.find((l) => l.adventure_phase === currentAdventurePhase)
      : null;
    if (match) { currentLesson = match; break; }
  }
  if (!currentLesson && modules.length > 0 && modules[0].lessons.length > 0) {
    currentLesson = modules[0].lessons[0];
  }

  const currentLessonSlug = currentLesson?.slug ?? null;

  useEffect(() => {
    if (!currentLessonSlug) { setCurrentLessonPhrases([]); return; }
    setCurrentLessonPhrasesLoading(true);
    contentService.listPhrases(currentLessonSlug)
      .then(setCurrentLessonPhrases)
      .catch(() => setCurrentLessonPhrases([]))
      .finally(() => setCurrentLessonPhrasesLoading(false));
  }, [currentLessonSlug]);

  const dueCount = session?.due_count ?? 0;
  const canStudy = !loading && !currentLessonPhrasesLoading && currentLessonPhrases.length >= 2;

  // ── SRS review session ──────────────────────────────────────────────────────
  if (showSession && session && session.exercises.length > 0) {
    return (
      <StudySessionScreen
        exercises={session.exercises}
        onBack={() => setShowSession(false)}
        onComplete={() => { setShowSession(false); refreshSession(); }}
      />
    );
  }

  // ── Guided lesson ───────────────────────────────────────────────────────────
  if (showGuidedStudy && currentLesson) {
    return (
      <GuidedLessonRunner
        lesson={currentLesson}
        phrases={currentLessonPhrases}
        onBack={() => setShowGuidedStudy(false)}
        onComplete={() => setShowGuidedStudy(false)}
      />
    );
  }

  // ── Main tabs ───────────────────────────────────────────────────────────────
  return (
    <div>
      {/* Tabs */}
      <div className="mb-4 grid grid-cols-2 gap-1 rounded-[8px] bg-slate-100 p-1">
        <button
          type="button"
          onClick={() => setTab("guided")}
          className={`h-10 rounded-[6px] text-sm font-semibold transition ${tab === "guided" ? "bg-white text-slate-950 shadow-sm" : "text-slate-500 hover:text-slate-700"}`}
        >
          {s.today.tabSession}
        </button>
        <button
          type="button"
          onClick={() => setTab("scenarios")}
          className={`h-10 rounded-[6px] text-sm font-semibold transition ${tab === "scenarios" ? "bg-white text-slate-950 shadow-sm" : "text-slate-500 hover:text-slate-700"}`}
        >
          {s.today.tabModules}
        </button>
      </div>

      {tab === "guided" ? (
        <div className="flex flex-col gap-4" style={{ animation: "fadeIn 260ms ease-out" }}>

          {/* Hero — adventure context */}
          <div className="study-hero-card" onClick={() => onNavigate("adventure-map")}>
            <div className="study-hero-bg" />
            <div className="relative z-10 flex flex-col gap-4 p-5">
              <div>
                <p className="study-hero-label">{s.study.continueAdventureHint}</p>
                <p className="study-hero-title">
                  {nextPhase ? nextPhase.name : s.study.startAdventureTitle}
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
              <div className="grid grid-cols-2 gap-2">
                <button
                  type="button"
                  className="study-hero-btn-secondary"
                  onClick={(e) => { e.stopPropagation(); onNavigate("adventure-map"); }}
                >
                  <Sword size={15} strokeWidth={2} />
                  {s.study.continueAdventureBtn}
                </button>
                <button
                  type="button"
                  className="study-hero-btn"
                  onClick={(e) => { e.stopPropagation(); if (canStudy) setShowGuidedStudy(true); }}
                  disabled={!canStudy}
                >
                  {s.study.studyNowBtn}
                  <BookOpen size={15} strokeWidth={2.5} />
                </button>
              </div>
            </div>
          </div>

          {/* Current lesson card */}
          {!loading && currentLesson && (
            <div className="card overflow-hidden">
              <div className="flex items-center justify-between gap-3 border-b border-slate-100 px-4 py-3">
                <div className="min-w-0">
                  <p className="text-xs font-semibold uppercase tracking-wide area-text-primary">
                    {s.study.lessonTitle}
                  </p>
                  <p className="mt-0.5 truncate text-sm font-semibold text-slate-950">
                    {currentLesson.title}
                  </p>
                </div>
                {currentLesson.phrase_count > 0 && (
                  <span className="shrink-0 text-xs font-medium text-slate-400">
                    {s.study.phrasesCount(currentLesson.phrase_count)}
                  </span>
                )}
              </div>

              {/* Phrase previews */}
              {currentLessonPhrasesLoading ? (
                <div className="px-4 py-3">
                  <p className="text-sm text-slate-400">{s.states.loading}</p>
                </div>
              ) : (
                <div className="divide-y divide-slate-50">
                  {currentLessonPhrases.slice(0, 5).map((phrase) => (
                    <div key={phrase.id} className="flex items-center justify-between gap-3 px-4 py-2.5">
                      <p className="text-sm font-semibold text-slate-950">{phrase.target_text}</p>
                      <p className="shrink-0 text-xs font-medium text-slate-400">{phrase.source_text}</p>
                    </div>
                  ))}
                  {currentLessonPhrases.length > 5 && (
                    <p className="px-4 py-2 text-xs font-medium text-slate-400">
                      +{currentLessonPhrases.length - 5} {s.study.phrasesCount(currentLessonPhrases.length - 5).split(" ")[1]}
                    </p>
                  )}
                </div>
              )}

              {canStudy && (
                <div className="border-t border-slate-100 px-4 py-3">
                  <button
                    type="button"
                    onClick={() => setShowGuidedStudy(true)}
                    className="area-btn flex h-10 w-full items-center justify-center gap-2 rounded-[8px] px-4 text-sm font-semibold transition"
                  >
                    {s.study.studyPhrasesBtn(currentLessonPhrases.length)}
                    <BookOpen size={14} strokeWidth={2.5} />
                  </button>
                </div>
              )}
            </div>
          )}

          {/* SRS review card */}
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
                  ) : session !== null && session.total === 0 ? (
                    <p className="mt-0.5 text-sm font-semibold text-slate-400">{s.study.noWordsDetail}</p>
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

        </div>
      ) : (
        <div style={{ animation: "fadeIn 260ms ease-out" }}>
          <ScenariosScreen hideHeader />
        </div>
      )}
    </div>
  );
}
