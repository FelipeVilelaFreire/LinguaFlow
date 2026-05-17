"use client";

import { contentService } from "@linguaflow/shared-core";
import type { Favorite } from "@linguaflow/shared-core";
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

  const scenarios = useMemo(
    () => Array.from(new Set(favorites.map((favorite) => favorite.phrase.scenario_title).filter(Boolean))),
    [favorites],
  );
  const filtered = filter ? favorites.filter((favorite) => favorite.phrase.scenario_title === filter) : favorites;

  async function removeFavorite(id: number) {
    await contentService.removeFavorite(id);
    setFavorites((current) => current.filter((favorite) => favorite.id !== id));
  }

  if (loading) return <State message="Carregando vocabulario..." />;
  if (error) return <State message="Nao foi possivel carregar o vocabulario." />;

  return (
    <main className={styles.page}>
      <header className={styles.header}>
        <p>Vocabulario</p>
        <h1>Frases salvas</h1>
        <span>Revise o que voce marcou como importante.</span>
      </header>

      <nav className={styles.filters}>
        <button className={filter === null ? styles.selected : ""} onClick={() => setFilter(null)} type="button">
          Tudo <span>{favorites.length}</span>
        </button>
        {scenarios.map((scenario) => (
          <button className={filter === scenario ? styles.selected : ""} key={scenario} onClick={() => setFilter(scenario)} type="button">
            {scenario}
          </button>
        ))}
      </nav>

      {filtered.length === 0 ? <p className={styles.empty}>Nenhuma frase salva ainda.</p> : (
        <section className={styles.list}>
          {filtered.map((favorite) => (
            <article className={styles.card} key={favorite.id}>
              <div>
                <h2>{favorite.phrase.target_text}</h2>
                <p>{favorite.phrase.source_text}</p>
                {favorite.phrase.scenario_title && <span>{favorite.phrase.scenario_title}</span>}
              </div>
              <button onClick={() => removeFavorite(favorite.id)} type="button">Remover</button>
            </article>
          ))}
        </section>
      )}
    </main>
  );
}

function State({ message }: { message: string }) {
  return <main className={styles.page}><p className={styles.empty}>{message}</p></main>;
}
