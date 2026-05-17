import { BookOpen, Brain, CheckCircle2, Circle, ClipboardCheck, Lock, Play, RotateCcw, Sparkles, Sword, Target } from "lucide-react";
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
  const lessonStatusByPhase = new Map<number, "completed" | "current" | "locked" | "open">();
  for (const ch of chapters) {
    const current = ch.progress?.current_phase ?? 1;
    for (const phase of ch.phases) {
      lessonStatusByPhase.set(
        phase.number,
        phase.is_completed ? "completed" : phase.number === current ? "current" : "locked",
      );
    }
  }

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

          <AdvancedStudyTrail
            modules={modules}
            currentLessonSlug={currentLesson?.slug ?? null}
            lessonStatusByPhase={lessonStatusByPhase}
            onStartLesson={(lesson) => {
              if (lesson.slug === currentLesson?.slug && canStudy) setShowGuidedStudy(true);
            }}
          />

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

function AdvancedStudyTrail({
  modules,
  currentLessonSlug,
  lessonStatusByPhase,
  onStartLesson,
}: {
  modules: StudyModule[];
  currentLessonSlug: string | null;
  lessonStatusByPhase: Map<number, "completed" | "current" | "locked" | "open">;
  onStartLesson: (lesson: StudyLesson) => void;
}) {
  const s = useStrings();
  const enrichedModules = modules.map((module) => ({
    ...module,
    lessons: module.lessons.map((lesson) => ({
      lesson,
      status: getStudyLessonStatus(lesson, currentLessonSlug, lessonStatusByPhase),
    })),
  }));
  const lessons = enrichedModules.flatMap((module) => module.lessons);

  if (lessons.length === 0) return null;

  const completed = lessons.filter((item) => item.status === "completed").length;
  const progress = Math.round((completed / lessons.length) * 100);

  return (
    <section className="card overflow-hidden">
      <div className="border-b border-slate-100 px-4 py-4">
        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wide area-text-primary">
              {s.study.studyPathEyebrow}
            </p>
            <h2 className="mt-1 text-xl font-semibold text-slate-950">{s.study.studyPathTitle}</h2>
            <p className="mt-1 text-sm font-medium leading-6 text-slate-500">{s.study.studyPathDetail}</p>
          </div>
          <span className="shrink-0 rounded-full px-3 py-1 text-xs font-bold" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
            {progress}%
          </span>
        </div>
        <div className="mt-4 h-2 overflow-hidden rounded-full bg-slate-100">
          <div className="h-full rounded-full transition-all duration-500" style={{ width: `${progress}%`, background: "var(--area-primary)" }} />
        </div>
      </div>

      <div className="grid gap-5 px-4 py-5">
        {enrichedModules.map((module) => {
          const moduleDone = module.lessons.filter((item) => item.status === "completed").length;
          const moduleTotal = module.lessons.length;
          return (
            <section key={module.id} className="relative">
              <div className="mb-3 flex items-center justify-between gap-3">
                <div className="min-w-0">
                  <p className="text-[11px] font-bold uppercase tracking-wide text-slate-400">
                    {s.study.moduleLabel(module.order)}
                  </p>
                  <h3 className="truncate text-base font-semibold text-slate-950">{module.title}</h3>
                </div>
                <span className="shrink-0 rounded-full bg-slate-100 px-2.5 py-1 text-xs font-bold text-slate-500">
                  {moduleDone}/{moduleTotal}
                </span>
              </div>

              <div className="relative grid gap-3">
                <div className="absolute bottom-7 left-6 top-7 w-0.5 bg-slate-100" />
                {module.lessons.map(({ lesson, status }, index) => (
                  <AdvancedStudyTrailLesson
                    key={lesson.id}
                    lesson={lesson}
                    status={status}
                    index={index + 1}
                    onStart={() => onStartLesson(lesson)}
                  />
                ))}
              </div>
            </section>
          );
        })}
      </div>
    </section>
  );
}

function AdvancedStudyTrailLesson({
  lesson,
  status,
  index,
  onStart,
}: {
  lesson: StudyLesson;
  status: "completed" | "current" | "locked" | "open";
  index: number;
  onStart: () => void;
}) {
  const s = useStrings();
  const isCurrent = status === "current";
  const isLocked = status === "locked" || status === "open";

  return (
    <article
      className={`relative rounded-[8px] border p-3 transition ${
        isCurrent
          ? "border-[var(--area-primary)] bg-[var(--area-primary-soft)] shadow-sm"
          : status === "completed"
            ? "border-emerald-100 bg-emerald-50/40"
            : "border-slate-100 bg-white"
      } ${status === "locked" ? "opacity-60" : ""}`}
    >
      <div className="grid grid-cols-[48px_1fr_auto] items-start gap-3">
        <StudyTrailNode status={status} index={index} />
        <div className="min-w-0">
          <div className="flex flex-wrap items-center gap-2">
            <h4 className="min-w-0 max-w-full truncate text-sm font-semibold text-slate-950">{lesson.title}</h4>
            {lesson.adventure_phase ? (
              <span className="shrink-0 rounded-full bg-white px-2 py-0.5 text-[10px] font-bold text-slate-500 ring-1 ring-slate-200">
                {s.study.lessonPhaseRef(lesson.adventure_phase)}
              </span>
            ) : null}
          </div>
          <p className="mt-1 line-clamp-2 text-xs font-medium leading-5 text-slate-500">
            {lesson.description || s.study.studyLessonFallback}
          </p>
        </div>
        {status === "completed" ? (
          <CheckCircle2 size={18} className="area-text-primary" />
        ) : isLocked ? (
          <Lock size={16} className="text-slate-400" />
        ) : null}
      </div>

      <div className="ml-[60px] mt-3 grid grid-cols-2 gap-2 sm:grid-cols-4">
        {STUDY_STEP_PREVIEW.map((step, stepIndex) => {
          const Icon = step.Icon;
          const done = status === "completed" || (isCurrent && stepIndex === 0);
          return (
            <div
              key={step.labelKey}
              className={`flex min-h-12 items-center gap-2 rounded-[8px] px-2.5 py-2 text-xs font-semibold ring-1 ${
                done
                  ? "bg-white text-slate-800 ring-[var(--area-primary)]/30"
                  : "bg-slate-50 text-slate-500 ring-slate-100"
              }`}
            >
              <Icon size={14} className={done ? "area-text-primary" : "text-slate-400"} />
              <span className="min-w-0 truncate">{s.study[step.labelKey]}</span>
            </div>
          );
        })}
      </div>

      {isCurrent ? (
        <div className="ml-[60px] mt-3">
          <button
            type="button"
            onClick={onStart}
            className="area-btn flex h-11 w-full items-center justify-center gap-2 rounded-[8px] px-4 text-sm font-semibold transition sm:w-auto"
          >
            <Play size={15} fill="currentColor" />
            {s.study.studyNowBtn}
          </button>
        </div>
      ) : isLocked ? (
        <p className="ml-[60px] mt-3 text-xs font-semibold text-slate-400">{s.study.studyLockedHint}</p>
      ) : null}
    </article>
  );
}

const STUDY_STEP_PREVIEW = [
  { labelKey: "studyStepExplain" as const, Icon: Sparkles },
  { labelKey: "studyStepUnderstand" as const, Icon: Brain },
  { labelKey: "studyStepPractice" as const, Icon: Target },
  { labelKey: "studyStepReview" as const, Icon: ClipboardCheck },
];

function StudyTrail({
  modules,
  currentLessonSlug,
  lessonStatusByPhase,
  onStartLesson,
}: {
  modules: StudyModule[];
  currentLessonSlug: string | null;
  lessonStatusByPhase: Map<number, "completed" | "current" | "locked" | "open">;
  onStartLesson: (lesson: StudyLesson) => void;
}) {
  const s = useStrings();
  const lessons = modules.flatMap((module) =>
    module.lessons.map((lesson) => ({
      module,
      lesson,
      status: getStudyLessonStatus(lesson, currentLessonSlug, lessonStatusByPhase),
    })),
  );

  if (lessons.length === 0) return null;

  const completed = lessons.filter((item) => item.status === "completed").length;
  const progress = Math.round((completed / lessons.length) * 100);

  return (
    <section className="card overflow-hidden">
      <div className="border-b border-slate-100 px-4 py-4">
        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="text-xs font-semibold uppercase tracking-wide area-text-primary">
              {s.study.studyPathEyebrow}
            </p>
            <h2 className="mt-1 text-xl font-semibold text-slate-950">{s.study.studyPathTitle}</h2>
            <p className="mt-1 text-sm font-medium leading-6 text-slate-500">{s.study.studyPathDetail}</p>
          </div>
          <span className="shrink-0 rounded-full px-3 py-1 text-xs font-bold" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
            {progress}%
          </span>
        </div>
        <div className="mt-4 h-2 overflow-hidden rounded-full bg-slate-100">
          <div className="h-full rounded-full transition-all duration-500" style={{ width: `${progress}%`, background: "var(--area-primary)" }} />
        </div>
      </div>

      <div className="relative px-4 py-5">
        <div className="absolute bottom-8 left-10 top-8 w-0.5 bg-slate-100" />
        <div className="grid gap-3">
          {lessons.map(({ module, lesson, status }, index) => (
            <button
              key={lesson.id}
              type="button"
              disabled={status === "locked" || status === "open"}
              onClick={() => onStartLesson(lesson)}
              className={`relative grid grid-cols-[48px_1fr_auto] items-center gap-3 rounded-[8px] p-2.5 text-left transition ${
                status === "current"
                  ? "bg-[var(--area-primary-soft)] ring-1 ring-[var(--area-primary)]"
                  : status === "locked"
                    ? "opacity-55"
                    : "hover:bg-slate-50"
              }`}
            >
              <StudyTrailNode status={status} index={index + 1} />
              <div className="min-w-0">
                <div className="flex items-center gap-2">
                  <p className="truncate text-sm font-semibold text-slate-950">{lesson.title}</p>
                  {lesson.adventure_phase ? (
                    <span className="hidden shrink-0 rounded-full bg-white px-2 py-0.5 text-[10px] font-bold text-slate-500 ring-1 ring-slate-200 sm:inline">
                      {s.study.lessonPhaseRef(lesson.adventure_phase)}
                    </span>
                  ) : null}
                </div>
                <p className="mt-0.5 truncate text-xs font-medium text-slate-500">
                  {s.study.moduleLabel(module.order)} · {s.study.phrasesCount(lesson.phrase_count)}
                </p>
              </div>
              <StudyTrailAction status={status} />
            </button>
          ))}
        </div>
      </div>
    </section>
  );
}

function getStudyLessonStatus(
  lesson: StudyLesson,
  currentLessonSlug: string | null,
  lessonStatusByPhase: Map<number, "completed" | "current" | "locked" | "open">,
) {
  if (lesson.slug === currentLessonSlug) return "current";
  if (lesson.adventure_phase === null) return "open";
  return lessonStatusByPhase.get(lesson.adventure_phase) ?? "open";
}

function StudyTrailNode({ status, index }: { status: "completed" | "current" | "locked" | "open"; index: number }) {
  const baseClass = "relative z-10 grid h-11 w-11 place-items-center rounded-full text-sm font-bold shadow-sm ring-4 ring-white";

  if (status === "completed") {
    return (
      <span className={baseClass} style={{ background: "var(--area-primary)", color: "var(--area-text-on-primary)" }}>
        <CheckCircle2 size={20} />
      </span>
    );
  }

  if (status === "current") {
    return (
      <span className={`${baseClass} animate-[adventureBounce_1.4s_ease-in-out_infinite]`} style={{ background: "var(--area-primary)", color: "var(--area-text-on-primary)" }}>
        <Play size={17} fill="currentColor" />
      </span>
    );
  }

  if (status === "locked") {
    return (
      <span className={`${baseClass} bg-slate-200 text-slate-400`}>
        <Lock size={16} />
      </span>
    );
  }

  return (
    <span className={`${baseClass} bg-white text-slate-400 ring-slate-100`}>
      <Circle size={18} />
      <span className="sr-only">{index}</span>
    </span>
  );
}

function StudyTrailAction({ status }: { status: "completed" | "current" | "locked" | "open" }) {
  const s = useStrings();
  if (status === "current") {
    return (
      <span className="hidden rounded-[8px] px-3 py-2 text-xs font-bold text-white sm:inline-flex" style={{ background: "var(--area-primary)" }}>
        {s.study.studyNowBtn}
      </span>
    );
  }
  if (status === "completed") {
    return <span className="hidden text-xs font-bold area-text-primary sm:inline">{s.layout.completed}</span>;
  }
  if (status === "locked") {
    return <Lock size={15} className="text-slate-400" />;
  }
  return null;
}
