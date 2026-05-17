"use client";

import { ROUTES, adventureService, contentService } from "@linguaflow/shared-core";
import type { ApiAdventureChapter, StudyModule, StudySessionData } from "@linguaflow/shared-core";
import { useStudySessionRunner } from "@linguaflow/shared-core/hooks/study";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import styles from "./StudyScreen.module.css";

export function StudyScreen() {
  const [session, setSession] = useState<StudySessionData | null>(null);
  const [chapters, setChapters] = useState<ApiAdventureChapter[]>([]);
  const [modules, setModules] = useState<StudyModule[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [reviewOpen, setReviewOpen] = useState(false);

  useEffect(() => {
    Promise.all([
      adventureService.getStudySession(),
      adventureService.listChapters(),
      contentService.listStudyModules(),
    ])
      .then(([nextSession, nextChapters, nextModules]) => {
        setSession(nextSession);
        setChapters(nextChapters);
        setModules(nextModules);
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

  if (loading) return <State message="Carregando estudo..." />;
  if (error) return <State message="Nao foi possivel carregar o estudo." />;
  if (reviewOpen && session) {
    return <StudyReview exercises={session.exercises} onClose={() => setReviewOpen(false)} />;
  }

  return (
    <main className={styles.page}>
      <header className={styles.header}>
        <p>Estudo guiado</p>
        <h1>Treine o que a aventura esta pedindo agora.</h1>
        <span>{session?.due_count ?? 0} revisoes pendentes</span>
      </header>

      <section className={styles.hero}>
        <div>
          <p>Proxima fase</p>
          <h2>{nextPhase?.phase.title ?? "Comece sua aventura"}</h2>
          <span>{nextPhase ? `${nextPhase.chapter.title} · Fase ${nextPhase.phase.number}` : "Mapa da aventura"}</span>
        </div>
        <div className={styles.actions}>
          <button disabled={!session?.exercises.length} onClick={() => setReviewOpen(true)} type="button">Revisar agora</button>
          <Link href={ROUTES.adventureMap}>Abrir mapa</Link>
        </div>
      </section>

      {currentLesson && (
        <section className={styles.section}>
          <div className={styles.sectionHeader}>
            <div>
              <p>Licao atual</p>
              <h2>{currentLesson.lesson.title}</h2>
              <span>{currentLesson.module.title}</span>
            </div>
            <strong>{currentLesson.lesson.phrase_count}</strong>
          </div>
          <p className={styles.description}>{currentLesson.lesson.description}</p>
        </section>
      )}

      <section className={styles.moduleGrid}>
        {modules.map((module) => (
          <article className={styles.moduleCard} key={module.id}>
            <h2>{module.title}</h2>
            <span>{module.lessons.length} licoes</span>
            <div>
              {module.lessons.slice(0, 5).map((lesson) => (
                <p key={lesson.id}>{lesson.title}</p>
              ))}
            </div>
          </article>
        ))}
      </section>
    </main>
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
        <h1>Revisao concluida</h1>
        <p>{runner.correctCount} acertos · {runner.mistakes} erros</p>
        <button onClick={runner.finish} type="button">Voltar</button>
      </main>
    );
  }

  if (!runner.current) return <State message="Nenhuma revisao pendente." />;

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
          <button onClick={() => { runner.submit(answer); setAnswer(""); }} type="button">Responder</button>
        </div>
      )}
      <button className={styles.secondaryButton} onClick={onClose} type="button">Sair</button>
    </main>
  );
}

function State({ message }: { message: string }) {
  return <main className={styles.page}><p className={styles.state}>{message}</p></main>;
}
