"use client";

import { ROUTES, STRINGS } from "@linguaflow/shared-core";
import { useAdventureChapters } from "@linguaflow/shared-core/hooks/adventure";
import Link from "next/link";
import styles from "./AdventureMapScreen.module.css";

export function AdventureMapScreen() {
  const { chapters, isLoading, error } = useAdventureChapters("ES");

  if (isLoading) return <p className={styles.state}>{STRINGS.adventure.loading}</p>;
  if (error) return <p className={styles.state}>{error}</p>;
  if (chapters.length === 0) return <p className={styles.state}>{STRINGS.adventure.empty}</p>;

  return (
    <main className={styles.page}>
      <nav className={styles.tabs} aria-label="Aventura">
        <span>Mapa</span>
        <Link href={ROUTES.adventureMochila}>Mochila</Link>
        <Link href={ROUTES.adventureBaus}>Baus</Link>
        <Link href={ROUTES.adventurePalavras}>Palavras</Link>
        <Link href={ROUTES.adventureHeroi}>Heroi</Link>
        <Link href={ROUTES.adventurePersonagens}>Personagens</Link>
      </nav>
      <h1 className={styles.title}>{STRINGS.adventure.mapTitle}</h1>
      <div className={styles.chapterList}>
        {chapters.map((chapter) => (
          <section className={styles.chapter} key={chapter.id}>
            <h2 className={styles.chapterTitle}>{chapter.title}</h2>
            <div className={styles.phaseList}>
              {chapter.phases.map((phase) => (
                <Link
                  className={styles.phaseCard}
                  href={`/aventura/capitulo/${phase.id}?phase=${phase.number}&lang=${chapter.language_code}&words=${encodeURIComponent(phase.key_words.join(","))}`}
                  key={phase.id}
                >
                  <strong>{STRINGS.adventure.phaseLabel(phase.number)}</strong>
                  <span>{phase.title}</span>
                </Link>
              ))}
            </div>
          </section>
        ))}
      </div>
    </main>
  );
}
