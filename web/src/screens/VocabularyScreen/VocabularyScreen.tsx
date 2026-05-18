"use client";

import { STRINGS, contentService } from "@linguaflow/shared-core";
import type { Favorite } from "@linguaflow/shared-core";
import { BookMarked, Layers3, Trash2 } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import styles from "./VocabularyScreen.module.css";

export function VocabularyScreen() {
  const [favorites, setFavorites] = useState<Favorite[]>([]);
  const [filter, setFilter] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    contentService.listFavorites()
      .then(setFavorites)
      .catch(() => setError(true))
      .finally(() => setLoading(false));
  }, []);

  const scenarios = useMemo(() => getUnique(favorites.map((favorite) => favorite.phrase.scenario_title)), [favorites]);
  const categories = useMemo(() => getUnique(favorites.map((favorite) => favorite.phrase.category)), [favorites]);
  const filtered = filter ? favorites.filter((favorite) => favorite.phrase.scenario_title === filter) : favorites;

  async function removeFavorite(id: number) {
    await contentService.removeFavorite(id);
    setFavorites((current) => current.filter((favorite) => favorite.id !== id));
  }

  if (loading) return <State message={STRINGS.vocabulary.loading} />;
  if (error) return <State message={STRINGS.vocabulary.loadError} />;

  return (
    <main className={styles.page}>
      <section className={styles.shell}>
        <header className={styles.header}>
          <div>
            <p className={styles.eyebrow}>{STRINGS.vocabulary.eyebrow}</p>
            <h1>{STRINGS.vocabulary.title}</h1>
            <span>{STRINGS.vocabulary.subtitle}</span>
          </div>
          <div className={styles.summaryGrid} aria-label={STRINGS.vocabulary.title}>
            <Summary label={STRINGS.vocabulary.savedCount(favorites.length)} value={favorites.length} />
            <Summary label={STRINGS.vocabulary.scenarioCount(scenarios.length)} value={scenarios.length} />
            <Summary label={STRINGS.vocabulary.categoryCount(categories.length)} value={categories.length} />
          </div>
        </header>

        <nav className={styles.filters} aria-label={STRINGS.vocabulary.eyebrow}>
          <button className={filter === null ? styles.selected : ""} onClick={() => setFilter(null)} type="button">
            {STRINGS.vocabulary.filterAll}
            <span>{favorites.length}</span>
          </button>
          {scenarios.map((scenario) => (
            <button
              className={filter === scenario ? styles.selected : ""}
              key={scenario}
              onClick={() => setFilter(filter === scenario ? null : scenario)}
              type="button"
            >
              {scenario}
            </button>
          ))}
        </nav>

        {favorites.length === 0 ? <EmptyState /> : null}

        {favorites.length > 0 && filtered.length === 0 ? (
          <p className={styles.emptyLine}>{STRINGS.vocabulary.filterEmpty}</p>
        ) : null}

        {filtered.length > 0 ? (
          <section className={styles.list}>
            {filtered.map((favorite) => (
              <article className={styles.card} key={favorite.id}>
                <div className={styles.cardIcon}>
                  <BookMarked size={18} />
                </div>
                <div className={styles.cardBody}>
                  <h2>{favorite.phrase.target_text}</h2>
                  <p>{favorite.phrase.source_text}</p>
                  <div className={styles.meta}>
                    <span>{favorite.phrase.scenario_title || STRINGS.vocabulary.scenarioFallback}</span>
                    <span>{favorite.phrase.category || STRINGS.vocabulary.categoryFallback}</span>
                    {favorite.phrase.difficulty ? (
                      <span>{`${STRINGS.vocabulary.difficultyLabel}: ${favorite.phrase.difficulty}`}</span>
                    ) : null}
                  </div>
                </div>
                <button className={styles.remove} onClick={() => removeFavorite(favorite.id)} type="button">
                  <Trash2 size={15} />
                  <span>{STRINGS.vocabulary.remove}</span>
                </button>
              </article>
            ))}
          </section>
        ) : null}
      </section>
    </main>
  );
}

function Summary({ label, value }: { label: string; value: number }) {
  return (
    <div className={styles.summaryCard}>
      <strong>{value}</strong>
      <span>{label}</span>
    </div>
  );
}

function EmptyState() {
  return (
    <section className={styles.emptyCard}>
      <div>
        <Layers3 size={24} />
      </div>
      <h2>{STRINGS.vocabulary.emptyTitle}</h2>
      <p>{STRINGS.vocabulary.emptyDetail}</p>
    </section>
  );
}

function State({ message }: { message: string }) {
  return (
    <main className={styles.page}>
      <section className={styles.shell}>
        <p className={styles.emptyLine}>{message}</p>
      </section>
    </main>
  );
}

function getUnique(values: Array<string | null | undefined>) {
  return Array.from(new Set(values.filter((value): value is string => Boolean(value))));
}
