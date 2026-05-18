import { Feather } from "@expo/vector-icons";
import { STRINGS, contentService, getStudyAreaTheme } from "@linguaflow/shared-core";
import type { Goal, GoalHistory, HistoryDay, HistoryMonth } from "@linguaflow/shared-core";
import { useEffect, useMemo, useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import { styles } from "./HistoryScreen.styles";

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
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={styles.header}>
        <Text style={styles.eyebrow}>{STRINGS.history.title}</Text>
        <Text style={styles.title}>{STRINGS.history.title}</Text>
        <Text style={styles.subtitle}>{STRINGS.history.subtitle}</Text>
      </View>

      <View style={styles.monthNav}>
        <Pressable accessibilityLabel={STRINGS.history.previousMonth} style={styles.monthButton} onPress={() => moveMonth(-1)}>
          <Feather name="chevron-left" size={18} color="#334155" />
        </Pressable>
        <Text style={styles.monthLabel}>{monthLabel}</Text>
        <Pressable accessibilityLabel={STRINGS.history.nextMonth} style={styles.monthButton} onPress={() => moveMonth(1)}>
          <Feather name="chevron-right" size={18} color="#334155" />
        </Pressable>
      </View>

      <View style={styles.stats}>
        <Metric label={STRINGS.history.bestStreak} value={summary.bestStreak} />
        <Metric label={STRINGS.history.days} value={summary.completedDays} />
        <Metric label={STRINGS.history.sessions} value={summary.sessions} />
      </View>

      <View style={styles.segmented}>
        <Pressable style={[styles.segment, viewMode === "all" ? styles.activeSegment : null]} onPress={() => setViewMode("all")}>
          <Text style={viewMode === "all" ? styles.activeSegmentText : styles.segmentText}>{STRINGS.history.all}</Text>
        </Pressable>
        <Pressable style={[styles.segment, viewMode === "areas" ? styles.activeSegment : null]} onPress={() => setViewMode("areas")}>
          <Text style={viewMode === "areas" ? styles.activeSegmentText : styles.segmentText}>{STRINGS.history.byArea}</Text>
        </Pressable>
      </View>

      {!hasHistory ? <EmptyState /> : null}

      {viewMode === "all" ? (
        <HistoryPanel days={mergeGoalDays(goals)} month={cursor.month} title={STRINGS.history.all} year={cursor.year} />
      ) : (
        goals.map((entry) => <GoalHistoryPanel entry={entry} key={entry.goal.id} month={cursor.month} year={cursor.year} />)
      )}
    </ScrollView>
  );
}

function Metric({ label, value }: { label: string; value: number }) {
  return (
    <View style={styles.metric}>
      <Text style={styles.metricValue}>{value}</Text>
      <Text style={styles.metricLabel}>{label}</Text>
    </View>
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
  title,
  year,
}: {
  days: Map<string, HistoryDay>;
  goal?: Goal;
  month: number;
  softColor?: string;
  title: string;
  year: number;
}) {
  return (
    <View style={styles.panel}>
      <View style={styles.panelHeader}>
        <Text style={styles.panelTitle}>{title}</Text>
        {goal?.is_active ? <Text style={styles.activeBadge}>{STRINGS.history.active}</Text> : null}
      </View>
      <View style={styles.legend}>
        <Legend color={COMPLETED_COLOR} label={STRINGS.history.completed} />
        <Legend color={softColor} label={STRINGS.history.planned} />
        <Legend color="transparent" label={STRINGS.history.open} border />
      </View>
      <CalendarGrid dayMap={days} month={month} softColor={softColor} year={year} />
    </View>
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
    <View style={styles.calendar}>
      {STRINGS.weekdays.short.map((day) => <Text style={styles.weekday} key={day}>{day}</Text>)}
      {Array.from({ length: leadingBlanks }, (_, index) => <View style={styles.day} key={`blank-${index}`} />)}
      {Array.from({ length: daysInMonth }, (_, index) => {
        const dayNum = index + 1;
        const date = `${year}-${String(month).padStart(2, "0")}-${String(dayNum).padStart(2, "0")}`;
        return <HistoryCell data={dayMap.get(date)} date={date} dayNum={dayNum} key={date} softColor={softColor} />;
      })}
    </View>
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

  return (
    <View
      style={[
        styles.day,
        planned && !completed ? { backgroundColor: softColor } : null,
        completed ? styles.completed : null,
        date === TODAY ? styles.today : null,
      ]}
    >
      <Text style={[styles.dayText, completed ? styles.completedText : null]}>{dayNum}</Text>
      {completed && count > 1 ? <Text style={styles.countText}>{count}x</Text> : null}
    </View>
  );
}

function Legend({ color, label, border }: { color: string; label: string; border?: boolean }) {
  return (
    <View style={styles.legendItem}>
      <View style={[styles.legendDot, { backgroundColor: color }, border ? styles.legendBorder : null]} />
      <Text style={styles.legendText}>{label}</Text>
    </View>
  );
}

function EmptyState() {
  return (
    <View style={styles.emptyCard}>
      <Text style={styles.emptyTitle}>{STRINGS.history.noHistoryTitle}</Text>
      <Text style={styles.emptyDetail}>{STRINGS.history.noHistoryDetail}</Text>
    </View>
  );
}

function State({ message, title }: { message: string; title?: string }) {
  return (
    <View style={styles.state}>
      {title ? <Text style={styles.emptyTitle}>{title}</Text> : null}
      <Text style={styles.stateText}>{message}</Text>
    </View>
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
