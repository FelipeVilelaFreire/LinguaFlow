import { Link } from "expo-router";
import { useEffect, useMemo, useState } from "react";
import { Image, ScrollView, Text, View } from "react-native";
import {
  STRINGS,
  contentService,
  getFlagImage,
  getStudyAreaTheme,
} from "@linguaflow/shared-core";
import type { Goal } from "@linguaflow/shared-core";
import { AdventureTransitionButton } from "@/src/components/features/adventure";
import { styles } from "./HomeScreen.styles";

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

  if (loading) {
    return (
      <View style={styles.state}>
        <Text style={styles.stateTitle}>{STRINGS.app.loading}</Text>
        <Text style={styles.stateDetail}>{STRINGS.app.subtitle}</Text>
      </View>
    );
  }

  if (error || !goal) {
    return (
      <View style={styles.state}>
        <Text style={styles.stateTitle}>{STRINGS.home.noActiveArea}</Text>
        <Text style={styles.stateDetail}>{STRINGS.home.noActiveAreaDetail}</Text>
      </View>
    );
  }

  const targetCode = goal.target_language?.code ?? theme.code;
  const sourceCode = goal.source_language?.code ?? "PT";
  const targetName = STRINGS.languages[targetCode as keyof typeof STRINGS.languages] ?? targetCode;
  const sourceName = STRINGS.languages[sourceCode as keyof typeof STRINGS.languages] ?? sourceCode;
  const flag = getFlagImage(targetCode, "md");
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
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={styles.heroCard}>
        <View style={styles.heroTop}>
          <Text style={styles.levelPill}>{STRINGS.home.levelBadge(targetCode, goal.current_level, goal.target_level)}</Text>
          <Text style={styles.percent}>{goal.progress_percent}%</Text>
        </View>

        <View style={styles.languageRow}>
          <Image source={{ uri: flag.src }} style={styles.flag} />
          <Text style={styles.languageTitle}>{targetName}</Text>
        </View>
        <Text style={styles.languagePath}>{STRINGS.home.languagePath(sourceName, targetName, goal.target_level)}</Text>
        <Text style={styles.progressMeta}>
          {STRINGS.home.adventurePosition(
            goal.current_level,
            STRINGS.adventureSeries[goal.current_level as keyof typeof STRINGS.adventureSeries] ?? goal.current_level,
            2,
            3,
          )}
        </Text>

        <View style={styles.progressTrack}>
          <View style={[styles.progressFill, { width: `${Math.max(0, Math.min(100, goal.progress_percent))}%` }]} />
        </View>
        <Text style={styles.phrases}>{goal.learned_phrases.toLocaleString()} / {goal.total_phrases.toLocaleString()} {STRINGS.home.phrasesLabel}</Text>

        <AdventureTransitionButton href="/adventure/map" style={styles.primaryAction}>
          <Text style={styles.primaryActionText}>{STRINGS.home.continueAdventure}</Text>
        </AdventureTransitionButton>
      </View>

      <View style={styles.statsGrid}>
        <StatCell label={STRINGS.home.statStreak} value={goal.streak_days} />
        <StatCell label={STRINGS.home.statWords} value={goal.learned_phrases} />
        <StatCell accent label={STRINGS.home.statLevel} value={goal.target_level} />
      </View>

      <View style={styles.routineCard}>
        <Text style={styles.routineLabel}>{STRINGS.home.nextSessionTitle}</Text>
        <Text style={styles.routineTitle}>{nextStudyLabel}</Text>
        <Text style={styles.routineDetail}>{routine}</Text>
      </View>
    </ScrollView>
  );
}

function StatCell({ value, label, accent }: { value: number | string; label: string; accent?: boolean }) {
  return (
    <View style={styles.statCard}>
      <Text style={accent ? styles.statValueAccent : styles.statValue}>{value}</Text>
      <Text style={styles.statLabel}>{label}</Text>
    </View>
  );
}

function formatDate(value: string) {
  return new Intl.DateTimeFormat("pt-BR", { weekday: "long", day: "2-digit", month: "2-digit" }).format(new Date(`${value}T12:00:00`));
}

