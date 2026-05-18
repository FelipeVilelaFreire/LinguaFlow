"use client";

import {
  ROUTES,
  STRINGS,
  contentService,
  getStudyAreaTheme,
  getStudyAreaThemeVars,
} from "@linguaflow/shared-core";
import type { Goal } from "@linguaflow/shared-core";
import { ArrowRight, BookOpen, CalendarDays, Flame, Plus, Sparkles, Sword } from "lucide-react";
import Link from "next/link";
import type { CSSProperties, ReactNode } from "react";
import { useEffect, useMemo, useState } from "react";
import { AdventureTransitionLink } from "@/src/components/features/adventure";
import { LangFlag } from "@/src/components/shared";
import styles from "./HomeScreen.module.css";

export function HomeScreen() {
  const [goal, setGoal] = useState<Goal | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    let cancelled = false;
    contentService.getCurrentGoal()
      .then((nextGoal) => {
        if (!cancelled) setGoal(nextGoal);
      })
      .catch(() => {
        if (!cancelled) setError(true);
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });

    return () => {
      cancelled = true;
    };
  }, []);

  const theme = useMemo(() => getStudyAreaTheme(goal), [goal]);
  const themeVars = getStudyAreaThemeVars(theme) as CSSProperties;

  if (loading) {
    return (
      <main className={styles.page} style={themeVars}>
        <StateCard title={STRINGS.app.loading} detail={STRINGS.app.subtitle} />
      </main>
    );
  }

  if (error || !goal) {
    return (
      <main className={styles.page} style={themeVars}>
        <section className={styles.emptyState}>
          <div className={styles.emptyIcon}><BookOpen size={26} /></div>
          <h1>{STRINGS.home.noActiveArea}</h1>
          <p>{STRINGS.home.noActiveAreaDetail}</p>
          <Link className={styles.primaryAction} href={ROUTES.account}>
            <Plus size={18} />
            {STRINGS.actions.createArea}
          </Link>
        </section>
      </main>
    );
  }

  const targetCode = goal.target_language?.code ?? theme.code;
  const sourceCode = goal.source_language?.code ?? "PT";
  const targetName = STRINGS.languages[targetCode as keyof typeof STRINGS.languages] ?? targetCode;
  const sourceName = STRINGS.languages[sourceCode as keyof typeof STRINGS.languages] ?? sourceCode;
  const hasRoutine = goal.study_weekdays.length > 0;
  const weekdayText = goal.study_weekdays.length === 7
    ? STRINGS.home.allDays
    : goal.study_weekdays.length === 0
      ? STRINGS.home.noRoutine
      : goal.study_weekdays.map((day) => STRINGS.weekdays.short[day]).join(", ");
  const routine = hasRoutine ? STRINGS.home.routine(weekdayText, goal.session_minutes) : STRINGS.home.flexibleStudy;
  const nextStudyLabel = hasRoutine
    ? goal.next_study_date ? STRINGS.home.nextSession(formatDate(goal.next_study_date)) : STRINGS.home.noFixedSchedule
    : STRINGS.home.noFixedSchedule;

  return (
    <main className={styles.page} style={themeVars}>
      <section className={styles.heroCard}>
        <div className={styles.heroTop}>
          <span className={styles.levelPill}>{STRINGS.home.levelBadge(targetCode, goal.current_level, goal.target_level)}</span>
          <strong>{goal.progress_percent}%</strong>
        </div>

        <div className={styles.languageRow}>
          <LangFlag code={targetCode} size="md" />
          <h1>{targetName}</h1>
        </div>
        <p className={styles.languagePath}>{STRINGS.home.languagePath(sourceName, targetName, goal.target_level)}</p>

        <p className={styles.progressMeta}>
          <Sword size={12} />
          {STRINGS.home.adventurePosition(
            goal.current_level,
            STRINGS.adventureSeries[goal.current_level as keyof typeof STRINGS.adventureSeries] ?? goal.current_level,
            2,
            3,
          )}
        </p>

        <div className={styles.progressBlock}>
          <div className={styles.progressTrack}>
            <span style={{ width: `${Math.max(0, Math.min(100, goal.progress_percent))}%` }} />
          </div>
          <p>{goal.learned_phrases.toLocaleString()} / {goal.total_phrases.toLocaleString()} {STRINGS.home.phrasesLabel}</p>
        </div>

        <div className={styles.heroActions}>
          <AdventureTransitionLink className={styles.primaryAction} href={ROUTES.adventureMap}>
            {STRINGS.home.continueAdventure}
            <ArrowRight size={18} />
          </AdventureTransitionLink>
        </div>
      </section>

      <section className={styles.statsGrid}>
        <StatCard icon={<Flame className={styles.flameIcon} size={13} />} label={STRINGS.home.statStreak} value={goal.streak_days} />
        <StatCard icon={<BookOpen className={styles.bookIcon} size={13} />} label={STRINGS.home.statWords} value={goal.learned_phrases} />
        <StatCard icon={<Sparkles size={13} />} label={STRINGS.home.statLevel} value={goal.target_level} accent />
      </section>

      <section className={styles.routineCard}>
        <span><CalendarDays size={14} /> {STRINGS.home.nextSessionTitle}</span>
        <strong>{nextStudyLabel}</strong>
        <p>{routine}</p>
      </section>
    </main>
  );
}

function StateCard({ title, detail }: { title: string; detail: string }) {
  return (
    <section className={styles.emptyState}>
      <div className={styles.emptyIcon}><BookOpen size={26} /></div>
      <h1>{title}</h1>
      <p>{detail}</p>
    </section>
  );
}

function StatCard({
  icon,
  label,
  value,
  accent,
}: {
  icon: ReactNode;
  label: string;
  value: number | string;
  accent?: boolean;
}) {
  return (
    <article className={styles.statCard}>
      <div>
        <strong className={accent ? styles.accentValue : ""}>{value}</strong>
        <span>{icon}</span>
      </div>
      <p>{label}</p>
    </article>
  );
}

function formatDate(value: string) {
  return new Intl.DateTimeFormat("pt-BR", { weekday: "long", day: "2-digit", month: "2-digit" }).format(new Date(`${value}T12:00:00`));
}


