"use client";

import {
  ROUTES,
  STRINGS,
  adventureService,
  contentService,
  getStudyAreaTheme,
  getStudyAreaThemeVars,
} from "@linguaflow/shared-core";
import type {
  ApiAdventureChapter,
  Goal,
  Phrase,
  StudyLesson,
  StudyModule,
  StudySessionData,
} from "@linguaflow/shared-core";
import { useStudySessionRunner } from "@linguaflow/shared-core/hooks/study";
import { BookOpen, CheckCircle2, Circle, Lock, Play, RotateCcw, Sparkles, Sword } from "lucide-react";
import Link from "next/link";
import type { CSSProperties } from "react";
import { useEffect, useMemo, useState } from "react";
import { AdventureTransitionLink } from "@/src/components/features/adventure";
import styles from "./StudyScreen.module.css";

type StudyTab = "guided" | "modules";

export function StudyScreen() {
  const [session, setSession] = useState<StudySessionData | null>(null);
  const [chapters, setChapters] = useState<ApiAdventureChapter[]>([]);
  const [modules, setModules] = useState<StudyModule[]>([]);
  const [goal, setGoal] = useState<Goal | null>(null);
  const [phrases, setPhrases] = useState<Phrase[]>([]);
  const [tab, setTab] = useState<StudyTab>("guided");
  const [loading, setLoading] = useState(true);
  const [phrasesLoading, setPhrasesLoading] = useState(false);
  const [error, setError] = useState(false);
  const [reviewOpen, setReviewOpen] = useState(false);
  const [lessonOpen, setLessonOpen] = useState(false);

  useEffect(() => {
    Promise.all([
      adventureService.getStudySession(),
      adventureService.listChapters(),
      contentService.listStudyModules(),
      contentService.getCurrentGoal().catch(() => null),
    ])
      .then(([nextSession, nextChapters, nextModules, nextGoal]) => {
        setSession(nextSession);
        setChapters(nextChapters);
        setModules(nextModules);
        setGoal(nextGoal);
      })
      .catch(() => setError(true))
      .finally(() => setLoading(false));
  }, []);

  const nextPhase = useMemo(() => {
    for (const chapter of chapters) {
      const phase = chapter.phases.find((item) => !item.is_completed);
      if (phase) return { chapter, phase };
    }
    return null;
  }, [chapters]);

  const currentLesson = useMemo(() => {
    const phaseNumber = nextPhase?.phase.number ?? null;
    for (const module of modules) {
      const lesson = phaseNumber
        ? module.lessons.find((item) => item.adventure_phase === phaseNumber)
        : module.lessons[0];
      if (lesson) return { module, lesson };
    }
    return null;
  }, [modules, nextPhase]);

  useEffect(() => {
    if (!currentLesson?.lesson.slug) {
      setPhrases([]);
      return;
    }

    setPhrasesLoading(true);
    contentService
      .listPhrases(currentLesson.lesson.slug)
      .then(setPhrases)
      .catch(() => setPhrases([]))
      .finally(() => setPhrasesLoading(false));
  }, [currentLesson?.lesson.slug]);

  const theme = getStudyAreaTheme(goal);
  const themeVars = getStudyAreaThemeVars(theme) as CSSProperties;
  const dueCount = session?.due_count ?? 0;
  const hasReview = Boolean(session?.exercises.length);

  if (loading) return <State message={STRINGS.states.loadingStudy} />;
  if (error) return <State message={STRINGS.states.studyLoadError} />;
  if (reviewOpen && session) {
    return <StudyReview exercises={session.exercises} onClose={() => setReviewOpen(false)} />;
  }
  if (lessonOpen && currentLesson && phrases.length > 0) {
    return <PhraseLessonRunner lesson={currentLesson.lesson} phrases={phrases} onClose={() => setLessonOpen(false)} />;
  }

  return (
    <main className={styles.page} style={themeVars}>
      <div className={styles.inner}>
        <header className={styles.header}>
          <div>
            <p>{STRINGS.study.title}</p>
            <h1>{STRINGS.study.headline}</h1>
          </div>
          <span>{STRINGS.study.pendingReviews(dueCount)}</span>
        </header>

        <div className={styles.tabs}>
          <button className={tab === "guided" ? styles.activeTab : styles.tab} onClick={() => setTab("guided")} type="button">
            <Sparkles size={16} />
            {STRINGS.today.tabSession}
          </button>
          <button className={tab === "modules" ? styles.activeTab : styles.tab} onClick={() => setTab("modules")} type="button">
            <BookOpen size={16} />
            {STRINGS.today.tabModules}
          </button>
        </div>

        {tab === "guided" ? (
          <div className={styles.content}>
            <section className={styles.hero}>
              <div className={styles.heroCopy}>
                <div className={styles.iconBubble}>
                  <Sword size={22} />
                </div>
                <p>{STRINGS.study.nextPhase}</p>
                <h2>{nextPhase?.phase.title ?? STRINGS.study.startAdventureTitle}</h2>
                <span>
                  {nextPhase
                    ? `${nextPhase.chapter.title} - ${STRINGS.adventure.phaseLabel(nextPhase.phase.number)}`
                    : STRINGS.study.adventureMap}
                </span>
                <small>{STRINGS.study.continueAdventureHint}</small>
              </div>
              <div className={styles.heroActions}>
                <AdventureTransitionLink className={styles.primaryAction} href={ROUTES.adventureMap}>
                  <Play size={16} />
                  {STRINGS.study.continueAdventureBtn}
                </AdventureTransitionLink>
                <button className={styles.secondaryAction} disabled={phrasesLoading || phrases.length === 0} onClick={() => setLessonOpen(true)} type="button">
                  {STRINGS.study.studyNowBtn}
                </button>
              </div>
            </section>

            {currentLesson ? (
            <CurrentLessonCard currentLesson={currentLesson} phrases={phrases} phrasesLoading={phrasesLoading} onStart={() => setLessonOpen(true)} />
            ) : null}

            <ReviewCard dueCount={dueCount} disabled={!hasReview} onReview={() => setReviewOpen(true)} />
            <StudyTrail modules={modules} currentLessonId={currentLesson?.lesson.id ?? null} currentPhase={nextPhase?.phase.number ?? null} />
          </div>
        ) : (
          <StudyTrail modules={modules} currentLessonId={currentLesson?.lesson.id ?? null} currentPhase={nextPhase?.phase.number ?? null} expanded />
        )}
      </div>
    </main>
  );
}

function CurrentLessonCard({
  currentLesson,
  phrases,
  phrasesLoading,
  onStart,
}: {
  currentLesson: { module: StudyModule; lesson: StudyLesson };
  phrases: Phrase[];
  phrasesLoading: boolean;
  onStart: () => void;
}) {
  const phraseCount = phrases.length || currentLesson.lesson.phrase_count;

  return (
    <section className={styles.card}>
      <div className={styles.cardHeader}>
        <div>
          <p>{STRINGS.study.currentLesson}</p>
          <h2>{currentLesson.lesson.title || STRINGS.study.lessonFallback}</h2>
          <span>{currentLesson.module.title}</span>
        </div>
        <strong>{STRINGS.study.phrasesCount(phraseCount)}</strong>
      </div>
      <p className={styles.description}>{currentLesson.lesson.description}</p>
      <div className={styles.phraseList}>
        {phrases.slice(0, 4).map((phrase) => (
          <div className={styles.phraseRow} key={phrase.id}>
            <span>{phrase.source_text}</span>
            <strong>{phrase.target_text}</strong>
          </div>
        ))}
        {!phrasesLoading && phrases.length === 0 ? <p className={styles.emptyDetail}>{STRINGS.study.noWordsDetail}</p> : null}
      </div>
      <button className={styles.lessonButton} disabled={phrasesLoading || phrases.length === 0} onClick={onStart} type="button">
        {STRINGS.study.studyPhrasesBtn(phraseCount)}
      </button>
    </section>
  );
}

function PhraseLessonRunner({ lesson, phrases, onClose }: { lesson: StudyLesson; phrases: Phrase[]; onClose: () => void }) {
  const [index, setIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const phrase = phrases[index];
  const last = index + 1 >= phrases.length;

  function advance() {
    if (!revealed) {
      setRevealed(true);
      return;
    }
    if (last) {
      onClose();
      return;
    }
    setIndex((item) => item + 1);
    setRevealed(false);
  }

  return (
    <main className={styles.reviewPage}>
      <span>{STRINGS.study.lessonSessionTitle}</span>
      <h1>{lesson.title || STRINGS.study.lessonFallback}</h1>
      <p>{STRINGS.study.phraseProgress(index + 1, phrases.length)}</p>
      <section className={styles.lessonRunnerCard}>
        <small>{STRINGS.study.sourcePhrase}</small>
        <strong>{phrase.source_text}</strong>
        {revealed ? (
          <>
            <small>{STRINGS.study.targetPhrase}</small>
            <em>{phrase.target_text}</em>
          </>
        ) : null}
      </section>
      <button onClick={advance} type="button">
        {!revealed ? STRINGS.study.showTranslation : last ? STRINGS.study.finishLesson : STRINGS.study.nextPhrase}
      </button>
      <button className={styles.secondaryButton} onClick={onClose} type="button">{STRINGS.study.exit}</button>
    </main>
  );
}

function ReviewCard({ dueCount, disabled, onReview }: { dueCount: number; disabled: boolean; onReview: () => void }) {
  return (
    <section className={styles.reviewCard}>
      <div className={styles.reviewIcon}>
        <RotateCcw size={18} />
      </div>
      <div>
        <p>{STRINGS.study.reviewNowTitle}</p>
        <h2>{STRINGS.study.reviewNowWords(dueCount)}</h2>
        <span>{STRINGS.study.reviewNowSubtitle}</span>
      </div>
      <button disabled={disabled} onClick={onReview} type="button">
        {STRINGS.study.reviewBtn}
      </button>
    </section>
  );
}

function StudyTrail({
  modules,
  currentLessonId,
  currentPhase,
  expanded = false,
}: {
  modules: StudyModule[];
  currentLessonId: number | null;
  currentPhase: number | null;
  expanded?: boolean;
}) {
  return (
    <section className={styles.trail}>
      <div className={styles.trailHeader}>
        <p>{STRINGS.study.pathEyebrow}</p>
        <h2>{STRINGS.study.pathTitle}</h2>
        <span>{STRINGS.study.pathDetail}</span>
      </div>
      <div className={styles.moduleList}>
        {modules.map((module) => (
          <article className={styles.moduleCard} key={module.id}>
            <div className={styles.moduleHeader}>
              <span>{STRINGS.study.moduleLabel(module.order)}</span>
              <strong>{module.title}</strong>
              <small>{STRINGS.study.moduleLessons(module.lessons.length)}</small>
            </div>
            <div className={styles.lessonList}>
              {(expanded ? module.lessons : module.lessons.slice(0, 5)).map((lesson) => (
                <LessonRow currentLessonId={currentLessonId} currentPhase={currentPhase} key={lesson.id} lesson={lesson} />
              ))}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}

function LessonRow({
  lesson,
  currentLessonId,
  currentPhase,
}: {
  lesson: StudyLesson;
  currentLessonId: number | null;
  currentPhase: number | null;
}) {
  const isCurrent = lesson.id === currentLessonId;
  const isCompleted = Boolean(currentPhase && lesson.adventure_phase && lesson.adventure_phase < currentPhase);
  const isLocked = Boolean(currentPhase && lesson.adventure_phase && lesson.adventure_phase > currentPhase);
  const status = isCurrent ? STRINGS.study.current : isCompleted ? STRINGS.study.completed : isLocked ? STRINGS.study.locked : STRINGS.study.unlocked;

  return (
    <div className={`${styles.lessonRow} ${isCurrent ? styles.currentLesson : ""}`}>
      <span className={styles.lessonIcon}>
        {isCompleted ? <CheckCircle2 size={16} /> : isLocked ? <Lock size={16} /> : <Circle size={16} />}
      </span>
      <div>
        <strong>{lesson.title}</strong>
        <small>
          {lesson.adventure_phase ? STRINGS.study.phaseLabel(lesson.adventure_phase) : STRINGS.study.lessonFallback} - {status}
        </small>
      </div>
      <em>{STRINGS.study.phrasesCount(lesson.phrase_count)}</em>
    </div>
  );
}

function StudyReview({
  exercises,
  onClose,
}: {
  exercises: NonNullable<StudySessionData["exercises"]>;
  onClose: () => void;
}) {
  const [answer, setAnswer] = useState("");
  const runner = useStudySessionRunner({ exercises, onComplete: onClose });

  if (runner.done) {
    return (
      <main className={styles.reviewPage}>
        <h1>{STRINGS.study.sessionComplete}</h1>
        <p>{STRINGS.study.sessionScore(runner.correctCount, runner.mistakes)}</p>
        <button onClick={runner.finish} type="button">{STRINGS.actions.back}</button>
      </main>
    );
  }

  if (!runner.current) return <State message={STRINGS.states.emptyReview} />;

  return (
    <main className={styles.reviewPage}>
      <span>{runner.index + 1}/{runner.total}</span>
      <h1>{runner.current.kind === "multiple_choice" ? runner.current.question : runner.current.prompt}</h1>
      <p>{runner.current.native}</p>
      {runner.current.kind === "multiple_choice" && runner.current.options ? (
        <div className={styles.reviewOptions}>
          {runner.current.options.map((option) => (
            <button key={option.id} onClick={() => runner.submit(option.id)} type="button">{option.text}</button>
          ))}
        </div>
      ) : (
        <div className={styles.reviewInput}>
          <input value={answer} onChange={(event) => setAnswer(event.target.value)} onKeyDown={(event) => {
            if (event.key === "Enter") {
              runner.submit(answer);
              setAnswer("");
            }
          }} />
          <button onClick={() => { runner.submit(answer); setAnswer(""); }} type="button">{STRINGS.study.answer}</button>
        </div>
      )}
      <button className={styles.secondaryButton} onClick={onClose} type="button">{STRINGS.study.exit}</button>
    </main>
  );
}

function State({ message }: { message: string }) {
  return <main className={styles.page}><p className={styles.state}>{message}</p></main>;
}

