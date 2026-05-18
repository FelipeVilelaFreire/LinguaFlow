"use client";

import {
  STRINGS,
  contentService,
  getStudyAreaTheme,
  getStudyAreaThemeVars,
} from "@linguaflow/shared-core";
import type { Goal, GoalHistory, HistoryDay, HistoryMonth } from "@linguaflow/shared-core";
import { ChevronLeft, ChevronRight } from "lucide-react";
import type { CSSProperties } from "react";
import { useEffect, useMemo, useState } from "react";
import styles from "./HistoryScreen.module.css";

const COMPLETED_COLOR = "#16a34a";
const TODAY = new Date().toISOString().split("T")[0];

type ViewMode = "all" | "areas";

export function HistoryScreen() {
  const [cursor, setCursor] = useState(() => {
    const today = new Date();
    return { year: today.getFullYear(), month: today.getMonth() + 1 };
  });
  const [history, setHistory] = useState<HistoryMonth | null>(null);
  const [viewMode, setViewMode] = useState<ViewMode>("all");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    setLoading(true);
    setError(false);
    contentService.getHistory(cursor.year, cursor.month)
      .then(setHistory)
      .catch(() => setError(true))
      .finally(() => setLoading(false));
  }, [cursor]);

  const monthLabel = useMemo(() => {
    return new Intl.DateTimeFormat(undefined, { month: "long", year: "numeric" })
      .format(new Date(cursor.year, cursor.month - 1, 1));
  }, [cursor]);

  const goals = history?.goals ?? [];
  const summary = useMemo(() => getMonthSummary(goals, cursor.year, cursor.month), [goals, cursor.year, cursor.month]);
  const hasHistory = goals.some((entry) => entry.days.some((day) => day.completed || day.planned));

  function moveMonth(delta: number) {
    const next = new Date(cursor.year, cursor.month - 1 + delta, 1);
    setCursor({ year: next.getFullYear(), month: next.getMonth() + 1 });
  }

  if (loading) return <State message={STRINGS.history.loading} />;
  if (error || !history) return <State message={STRINGS.history.unavailableDetail} title={STRINGS.history.unavailableTitle} />;

  return (
    <main className={styles.page}>
      <section className={styles.shell}>
        <header className={styles.header}>
          <div>
            <p className={styles.eyebrow}>{STRINGS.history.title}</p>
            <h1>{STRINGS.history.title}</h1>
            <span>{STRINGS.history.subtitle}</span>
          </div>
          <div className={styles.monthNav}>
            <button aria-label={STRINGS.history.previousMonth} onClick={() => moveMonth(-1)} type="button">
              <ChevronLeft size={18} />
            </button>
            <strong>{monthLabel}</strong>
            <button aria-label={STRINGS.history.nextMonth} onClick={() => moveMonth(1)} type="button">
              <ChevronRight size={18} />
            </button>
          </div>
        </header>

        <section className={styles.stats}>
          <Metric label={STRINGS.history.bestStreak} value={summary.bestStreak} />
          <Metric label={STRINGS.history.days} value={summary.completedDays} />
          <Metric label={STRINGS.history.sessions} value={summary.sessions} />
        </section>

        <div className={styles.segmented}>
          <button className={viewMode === "all" ? styles.activeSegment : ""} onClick={() => setViewMode("all")} type="button">
            {STRINGS.history.all}
          </button>
          <button className={viewMode === "areas" ? styles.activeSegment : ""} onClick={() => setViewMode("areas")} type="button">
            {STRINGS.history.byArea}
          </button>
        </div>

        {!hasHistory ? <EmptyState /> : null}

        {viewMode === "all" ? (
          <HistoryPanel days={mergeGoalDays(goals)} month={cursor.month} title={STRINGS.history.all} year={cursor.year} />
        ) : (
          <section className={styles.panelStack}>
            {goals.map((entry) => (
              <GoalHistoryPanel entry={entry} key={entry.goal.id} month={cursor.month} year={cursor.year} />
            ))}
          </section>
        )}
      </section>
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

function GoalHistoryPanel({ entry, year, month }: { entry: GoalHistory; year: number; month: number }) {
  const theme = getStudyAreaTheme(entry.goal);
  const dayMap = useMemo(() => new Map(entry.days.map((day) => [day.date, day])), [entry.days]);

  return (
    <HistoryPanel
      days={dayMap}
      goal={entry.goal}
      month={month}
      softColor={theme.primarySoft}
      style={getStudyAreaThemeVars(theme) as CSSProperties}
      title={formatGoal(entry.goal)}
      year={year}
    />
  );
}

function HistoryPanel({
  days,
  goal,
  month,
  softColor = "#e2e8f0",
  style,
  title,
  year,
}: {
  days: Map<string, HistoryDay>;
  goal?: Goal;
  month: number;
  softColor?: string;
  style?: CSSProperties;
  title: string;
  year: number;
}) {
  return (
    <section className={styles.panel} style={style}>
      <div className={styles.panelHeader}>
        <h2>{title}</h2>
        {goal?.is_active ? <span>{STRINGS.history.active}</span> : null}
      </div>
      <div className={styles.legend}>
        <Legend color={COMPLETED_COLOR} label={STRINGS.history.completed} />
        <Legend color={softColor} label={STRINGS.history.planned} />
        <Legend color="transparent" label={STRINGS.history.open} border />
      </div>
      <CalendarGrid dayMap={days} month={month} softColor={softColor} year={year} />
    </section>
  );
}

function CalendarGrid({ dayMap, softColor, year, month }: {
  dayMap: Map<string, HistoryDay>;
  softColor: string;
  year: number;
  month: number;
}) {
  const daysInMonth = new Date(year, month, 0).getDate();
  const firstDay = new Date(year, month - 1, 1).getDay();
  const leadingBlanks = (firstDay + 6) % 7;

  return (
    <div className={styles.calendar}>
      {STRINGS.weekdays.short.map((day) => <p key={day}>{day}</p>)}
      {Array.from({ length: leadingBlanks }, (_, index) => <span aria-hidden="true" key={`blank-${index}`} />)}
      {Array.from({ length: daysInMonth }, (_, index) => {
        const dayNum = index + 1;
        const date = `${year}-${String(month).padStart(2, "0")}-${String(dayNum).padStart(2, "0")}`;
        return <HistoryCell data={dayMap.get(date)} date={date} dayNum={dayNum} key={date} softColor={softColor} />;
      })}
    </div>
  );
}

function HistoryCell({ data, date, dayNum, softColor }: {
  data: HistoryDay | undefined;
  date: string;
  dayNum: number;
  softColor: string;
}) {
  const completed = data?.completed ?? false;
  const planned = data?.planned ?? false;
  const count = data?.completion_count ?? 0;
  const classNames = [
    styles.day,
    completed ? styles.completed : "",
    planned && !completed ? styles.planned : "",
    date === TODAY ? styles.today : "",
  ].filter(Boolean).join(" ");

  return (
    <span className={classNames} style={planned && !completed ? { background: softColor } : undefined}>
      <strong>{dayNum}</strong>
      {completed && count > 1 ? <small>{count}x</small> : null}
    </span>
  );
}

function Legend({ color, label, border }: { color: string; label: string; border?: boolean }) {
  return (
    <span>
      <i style={{ background: color, boxShadow: border ? "inset 0 0 0 1.5px #cbd5e1" : undefined }} />
      {label}
    </span>
  );
}

function EmptyState() {
  return (
    <section className={styles.emptyCard}>
      <h2>{STRINGS.history.noHistoryTitle}</h2>
      <p>{STRINGS.history.noHistoryDetail}</p>
    </section>
  );
}

function State({ message, title }: { message: string; title?: string }) {
  return (
    <main className={styles.page}>
      <section className={styles.shell}>
        <div className={styles.emptyCard}>
          {title ? <h2>{title}</h2> : null}
          <p>{message}</p>
        </div>
      </section>
    </main>
  );
}

function getMonthSummary(goals: GoalHistory[], year: number, month: number) {
  const completedDates = new Set<string>();
  let sessions = 0;
  let bestStreak = 0;

  for (const entry of goals) {
    sessions += entry.days.reduce((total, day) => total + day.completion_count, 0);
    const map = new Map(entry.days.map((day) => [day.date, day]));
    bestStreak = Math.max(bestStreak, getBestStreak(map, year, month));
    entry.days.forEach((day) => {
      if (day.completed) completedDates.add(day.date);
    });
  }

  return { bestStreak, completedDays: completedDates.size, sessions };
}

function getBestStreak(dayMap: Map<string, HistoryDay>, year: number, month: number) {
  const daysInMonth = new Date(year, month, 0).getDate();
  let current = 0;
  let best = 0;

  for (let day = 1; day <= daysInMonth; day += 1) {
    const date = `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
    current = dayMap.get(date)?.completed ? current + 1 : 0;
    best = Math.max(best, current);
  }

  return best;
}

function mergeGoalDays(goals: GoalHistory[]) {
  const byDate = new Map<string, HistoryDay>();

  for (const entry of goals) {
    for (const day of entry.days) {
      const existing = byDate.get(day.date);
      if (!existing) {
        byDate.set(day.date, { ...day, lessons: [...day.lessons] });
        continue;
      }
      existing.planned = existing.planned || day.planned;
      existing.completed = existing.completed || day.completed;
      existing.completion_count += day.completion_count;
      existing.lessons = [...existing.lessons, ...day.lessons];
    }
  }

  return byDate;
}

function formatGoal(goal: Goal) {
  const source = STRINGS.languages[goal.source_language?.code as keyof typeof STRINGS.languages] ?? goal.source_language?.code ?? "";
  const target = STRINGS.languages[goal.target_language?.code as keyof typeof STRINGS.languages] ?? goal.target_language?.code ?? "";
  return STRINGS.home.languagePath(source, target, goal.target_level);
}
