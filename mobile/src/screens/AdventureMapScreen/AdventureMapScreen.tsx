import { ScrollView, Text, View } from "react-native";
import { Link } from "expo-router";
import { getAdventureColors, STRINGS } from "@linguaflow/shared-core";
import { useAdventureChapters } from "@linguaflow/shared-core/hooks/adventure";
import { styles } from "./AdventureMapScreen.styles";

export function AdventureMapScreen() {
  const langCode = "ES";
  const theme = getAdventureColors(langCode, "dark");
  const { chapters, isLoading, error } = useAdventureChapters(langCode);

  if (isLoading) {
    return (
      <View style={[styles.state, { backgroundColor: theme.bgFrom }]}>
        <Text style={[styles.stateText, { color: theme.textOnBg }]}>{STRINGS.adventure.loading}</Text>
      </View>
    );
  }

  if (error) {
    return (
      <View style={[styles.state, { backgroundColor: theme.bgFrom }]}>
        <Text style={[styles.stateText, { color: theme.textOnBg }]}>{error}</Text>
      </View>
    );
  }

  return (
    <ScrollView style={[styles.container, { backgroundColor: theme.bgFrom }]} contentContainerStyle={styles.content}>
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.tabs}>
        <Text style={[styles.tab, { backgroundColor: theme.goldAccentSoft, color: theme.parchment }]}>Mapa</Text>
        <Link href="/adventure/inventory" style={[styles.tab, { backgroundColor: theme.surface, color: theme.textOnBg }]}>Mochila</Link>
        <Link href="/adventure/chests" style={[styles.tab, { backgroundColor: theme.surface, color: theme.textOnBg }]}>Baus</Link>
        <Link href="/adventure/words" style={[styles.tab, { backgroundColor: theme.surface, color: theme.textOnBg }]}>Palavras</Link>
        <Link href="/adventure/hero" style={[styles.tab, { backgroundColor: theme.surface, color: theme.textOnBg }]}>Heroi</Link>
        <Link href="/adventure/characters" style={[styles.tab, { backgroundColor: theme.surface, color: theme.textOnBg }]}>Personagens</Link>
      </ScrollView>
      <Text style={[styles.title, { color: theme.parchment }]}>{STRINGS.adventure.mapTitle}</Text>
      {chapters.map((chapter) => (
        <View key={chapter.id} style={[styles.chapter, { backgroundColor: theme.surface, borderColor: theme.borderFaint }]}>
          <Text style={[styles.chapterTitle, { color: theme.parchment }]}>{chapter.title}</Text>
          {chapter.phases.map((phase) => (
            <Link
              href={`/adventure/chapter/${phase.id}?phase=${phase.number}&lang=${chapter.language_code}&words=${encodeURIComponent(phase.key_words.join(","))}` as never}
              key={phase.id}
              style={[styles.phase, { backgroundColor: theme.surface, borderColor: theme.borderFaint }]}
            >
              <Text style={[styles.phaseTitle, { color: theme.parchment }]}>{STRINGS.adventure.phaseLabel(phase.number)}</Text>
              <Text style={[styles.phaseSubtitle, { color: theme.textOnBg }]}>{phase.title}</Text>
            </Link>
          ))}
        </View>
      ))}
    </ScrollView>
  );
}
