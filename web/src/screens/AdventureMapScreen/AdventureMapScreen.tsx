"use client";

import { getAdventureColors, getAdventureThemeVars, ROUTES, STRINGS } from "@linguaflow/shared-core";
import { useAdventureChapters } from "@linguaflow/shared-core/hooks/adventure";
import Link from "next/link";
import type { CSSProperties } from "react";
import { LangFlag } from "@/src/components/LangFlag";
import styles from "./AdventureMapScreen.module.css";

export function AdventureMapScreen() {
  const langCode = "ES";
  const { chapters, isLoading, error } = useAdventureChapters(langCode);
  const themeStyle = getAdventureThemeVars(getAdventureColors(langCode, "dark")) as CSSProperties;

  if (isLoading) return <p className={styles.state}>{STRINGS.adventure.loading}</p>;
  if (error) return <p className={styles.state}>{error}</p>;
  if (chapters.length === 0) return <p className={styles.state}>{STRINGS.adventure.empty}</p>;

  return (
    <main className={styles.page} style={themeStyle}>
      <nav className={styles.tabs} aria-label="Aventura">
        <span><LangFlag code={langCode} size="xs" /> Mapa</span>
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
            <div className={styles.chapterHeader}>
              <LangFlag code={chapter.language_code || langCode} size="sm" />
              <h2 className={styles.chapterTitle}>{chapter.title}</h2>
            </div>
            <div className={styles.phaseList}>
              {chapter.phases.map((phase, index) => (
                <Link
                  className={styles.phaseCard}
                  href={`/aventura/capitulo/${phase.id}?phase=${phase.number}&lang=${chapter.language_code}&words=${encodeURIComponent(phase.key_words.join(","))}`}
                  key={phase.id}
                >
                  <span className={styles.phaseNode}>{index + 1}</span>
                  <span className={styles.phaseCopy}>
                    <strong>{STRINGS.adventure.phaseLabel(phase.number)}</strong>
                    <span>{phase.title}</span>
                  </span>
                </Link>
              ))}
            </div>
          </section>
        ))}
      </div>
    </main>
  );
}
