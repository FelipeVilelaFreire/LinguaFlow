"use client";

import { useEffect, useState } from "react";
import { adventureService, type ApiAdventureChapter, STRINGS } from "@linguaflow/shared-core";
import { AppBoot } from "@/src/components/AppBoot";
import styles from "./AdventureMapScreen.module.css";

function AdventureMapContent() {
  const [chapters, setChapters] = useState<ApiAdventureChapter[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    adventureService.listChapters()
      .then(setChapters)
      .catch((err: unknown) => setError(err instanceof Error ? err.message : STRINGS.errors.generic))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p className={styles.state}>{STRINGS.adventure.loading}</p>;
  if (error) return <p className={styles.state}>{error}</p>;
  if (chapters.length === 0) return <p className={styles.state}>{STRINGS.adventure.empty}</p>;

  return (
    <main className={styles.page}>
      <h1 className={styles.title}>{STRINGS.adventure.mapTitle}</h1>
      <div className={styles.chapterList}>
        {chapters.map((chapter) => (
          <section className={styles.chapter} key={chapter.id}>
            <h2 className={styles.chapterTitle}>{chapter.title}</h2>
            <div className={styles.phaseList}>
              {chapter.phases.map((phase) => (
                <article className={styles.phaseCard} key={phase.id}>
                  <strong>{STRINGS.adventure.phaseLabel(phase.number)}</strong>
                  <span>{phase.title}</span>
                </article>
              ))}
            </div>
          </section>
        ))}
      </div>
    </main>
  );
}

export function AdventureMapScreen() {
  return (
    <AppBoot>
      <AdventureMapContent />
    </AppBoot>
  );
}
