"use client";

import { contentService } from "@linguaflow/shared-core";
import type { HistoryMonth } from "@linguaflow/shared-core";
import { useEffect, useMemo, useState } from "react";
import styles from "./HistoryScreen.module.css";

export function HistoryScreen() {
  const [cursor, setCursor] = useState(() => {
    const today = new Date();
    return { year: today.getFullYear(), month: today.getMonth() + 1 };
  });
  const [history, setHistory] = useState<HistoryMonth | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);
    contentService.getHistory(cursor.year, cursor.month)
      .then(setHistory)
      .finally(() => setLoading(false));
  }, [cursor]);

  const monthLabel = useMemo(() => {
    return new Intl.DateTimeFormat("pt-BR", { month: "long", year: "numeric" })
      .format(new Date(cursor.year, cursor.month - 1, 1));
  }, [cursor]);

  function moveMonth(delta: number) {
    const next = new Date(cursor.year, cursor.month - 1 + delta, 1);
    setCursor({ year: next.getFullYear(), month: next.getMonth() + 1 });
  }

  const days = history?.goals.flatMap((goal) => goal.days) ?? [];
  const completed = days.filter((day) => day.completed).length;
  const sessions = days.reduce((total, day) => total + day.completion_count, 0);

  return (
    <main className={styles.page}>
      <header className={styles.header}>
        <h1>Historico</h1>
        <div>
          <button onClick={() => moveMonth(-1)} type="button">Anterior</button>
          <span>{monthLabel}</span>
          <button onClick={() => moveMonth(1)} type="button">Proximo</button>
        </div>
      </header>

      {loading ? <p className={styles.state}>Carregando...</p> : (
        <>
          <section className={styles.stats}>
            <Metric label="Dias" value={completed} />
            <Metric label="Sessoes" value={sessions} />
            <Metric label="Areas" value={history?.goals.length ?? 0} />
          </section>
          <section className={styles.goals}>
            {history?.goals.map((entry) => (
              <article className={styles.goal} key={entry.goal.id}>
                <h2>{entry.goal.target_language?.name ?? entry.goal.target_language?.code}</h2>
                <div className={styles.days}>
                  {entry.days.map((day) => (
                    <span className={day.completed ? styles.completed : day.planned ? styles.planned : ""} key={day.date}>
                      {new Date(`${day.date}T00:00:00`).getDate()}
                    </span>
                  ))}
                </div>
              </article>
            ))}
          </section>
        </>
      )}
    </main>
  );
}

function Metric({ label, value }: { label: string; value: number }) {
  return (
    <article className={styles.metric}>
      <strong>{value}</strong>
      <span>{label}</span>
    </article>
  );
}
