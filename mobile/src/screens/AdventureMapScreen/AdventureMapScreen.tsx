import { useEffect, useState } from "react";
import { ScrollView, Text, View } from "react-native";
import { adventureService, type ApiAdventureChapter, STRINGS } from "@linguaflow/shared-core";
import { styles } from "./AdventureMapScreen.styles";

export function AdventureMapScreen() {
  const [chapters, setChapters] = useState<ApiAdventureChapter[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    adventureService.listChapters()
      .then(setChapters)
      .catch((err: unknown) => setError(err instanceof Error ? err.message : STRINGS.errors.generic))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <View style={styles.state}>
        <Text style={styles.stateText}>{STRINGS.adventure.loading}</Text>
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.state}>
        <Text style={styles.stateText}>{error}</Text>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <Text style={styles.title}>{STRINGS.adventure.mapTitle}</Text>
      {chapters.map((chapter) => (
        <View key={chapter.id} style={styles.chapter}>
          <Text style={styles.chapterTitle}>{chapter.title}</Text>
          {chapter.phases.map((phase) => (
            <View key={phase.id} style={styles.phase}>
              <Text style={styles.phaseTitle}>{STRINGS.adventure.phaseLabel(phase.number)}</Text>
              <Text style={styles.phaseSubtitle}>{phase.title}</Text>
            </View>
          ))}
        </View>
      ))}
    </ScrollView>
  );
}
