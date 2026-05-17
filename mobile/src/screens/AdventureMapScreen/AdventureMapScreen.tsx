import { ScrollView, Text, View } from "react-native";
import { Link } from "expo-router";
import { STRINGS } from "@linguaflow/shared-core";
import { useAdventureChapters } from "@linguaflow/shared-core/hooks/adventure";
import { styles } from "./AdventureMapScreen.styles";

export function AdventureMapScreen() {
  const { chapters, isLoading, error } = useAdventureChapters("ES");

  if (isLoading) {
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
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.tabs}>
        <Text style={[styles.tab, styles.activeTab]}>Mapa</Text>
        <Link href="/adventure/inventory" style={styles.tab}>Mochila</Link>
        <Link href="/adventure/chests" style={styles.tab}>Baus</Link>
        <Link href="/adventure/words" style={styles.tab}>Palavras</Link>
        <Link href="/adventure/hero" style={styles.tab}>Heroi</Link>
        <Link href="/adventure/characters" style={styles.tab}>Personagens</Link>
      </ScrollView>
      <Text style={styles.title}>{STRINGS.adventure.mapTitle}</Text>
      {chapters.map((chapter) => (
        <View key={chapter.id} style={styles.chapter}>
          <Text style={styles.chapterTitle}>{chapter.title}</Text>
          {chapter.phases.map((phase) => (
            <Link
              href={`/adventure/chapter/${phase.id}?phase=${phase.number}&lang=${chapter.language_code}&words=${encodeURIComponent(phase.key_words.join(","))}` as never}
              key={phase.id}
              style={styles.phase}
            >
              <Text style={styles.phaseTitle}>{STRINGS.adventure.phaseLabel(phase.number)}</Text>
              <Text style={styles.phaseSubtitle}>{phase.title}</Text>
            </Link>
          ))}
        </View>
      ))}
    </ScrollView>
  );
}
