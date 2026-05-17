import { useEffect, useMemo, useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import { contentService } from "@linguaflow/shared-core";
import type { HistoryMonth } from "@linguaflow/shared-core";
import { styles } from "./HistoryScreen.styles";

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
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <Text style={styles.title}>Historico</Text>
      <View style={styles.monthNav}>
        <Pressable style={styles.monthButton} onPress={() => moveMonth(-1)}><Text style={styles.monthButtonText}>Anterior</Text></Pressable>
        <Text style={styles.monthLabel}>{monthLabel}</Text>
        <Pressable style={styles.monthButton} onPress={() => moveMonth(1)}><Text style={styles.monthButtonText}>Proximo</Text></Pressable>
      </View>

      {loading ? <Text style={styles.state}>Carregando...</Text> : (
        <>
          <View style={styles.stats}>
            <Metric label="Dias" value={completed} />
            <Metric label="Sessoes" value={sessions} />
            <Metric label="Areas" value={history?.goals.length ?? 0} />
          </View>
          {history?.goals.map((entry) => (
            <View style={styles.goal} key={entry.goal.id}>
              <Text style={styles.goalTitle}>{entry.goal.target_language?.name ?? entry.goal.target_language?.code}</Text>
              <View style={styles.days}>
                {entry.days.map((day) => (
                  <Text style={[styles.day, day.planned ? styles.planned : null, day.completed ? styles.completed : null]} key={day.date}>
                    {new Date(`${day.date}T00:00:00`).getDate()}
                  </Text>
                ))}
              </View>
            </View>
          ))}
        </>
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
