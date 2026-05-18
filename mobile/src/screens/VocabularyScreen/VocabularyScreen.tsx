import { Feather } from "@expo/vector-icons";
import { STRINGS, contentService } from "@linguaflow/shared-core";
import type { Favorite } from "@linguaflow/shared-core";
import { useEffect, useMemo, useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import { styles } from "./VocabularyScreen.styles";

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

  const scenarios = useMemo(() => getUnique(favorites.map((favorite) => favorite.phrase.scenario_title)), [favorites]);
  const categories = useMemo(() => getUnique(favorites.map((favorite) => favorite.phrase.category)), [favorites]);
  const filtered = filter ? favorites.filter((favorite) => favorite.phrase.scenario_title === filter) : favorites;

  async function removeFavorite(id: number) {
    await contentService.removeFavorite(id);
    setFavorites((current) => current.filter((favorite) => favorite.id !== id));
  }

  if (loading) return <State message={STRINGS.vocabulary.loading} />;
  if (error) return <State message={STRINGS.vocabulary.loadError} />;

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={styles.header}>
        <Text style={styles.eyebrow}>{STRINGS.vocabulary.eyebrow}</Text>
        <Text style={styles.title}>{STRINGS.vocabulary.title}</Text>
        <Text style={styles.subtitle}>{STRINGS.vocabulary.subtitle}</Text>
      </View>

      <View style={styles.summaryRow}>
        <Summary value={favorites.length} label={STRINGS.vocabulary.savedCount(favorites.length)} />
        <Summary value={scenarios.length} label={STRINGS.vocabulary.scenarioCount(scenarios.length)} />
        <Summary value={categories.length} label={STRINGS.vocabulary.categoryCount(categories.length)} />
      </View>

      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.filters}>
        <Pressable style={[styles.filter, filter === null ? styles.selected : null]} onPress={() => setFilter(null)}>
          <Text style={filter === null ? styles.selectedText : styles.filterText}>{STRINGS.vocabulary.filterAll}</Text>
          <Text style={filter === null ? styles.selectedCount : styles.filterCount}>{favorites.length}</Text>
        </Pressable>
        {scenarios.map((scenario) => (
          <Pressable
            style={[styles.filter, filter === scenario ? styles.selected : null]}
            key={scenario}
            onPress={() => setFilter(filter === scenario ? null : scenario)}
          >
            <Text style={filter === scenario ? styles.selectedText : styles.filterText}>{scenario}</Text>
          </Pressable>
        ))}
      </ScrollView>

      {favorites.length === 0 ? <EmptyState /> : null}
      {favorites.length > 0 && filtered.length === 0 ? <Text style={styles.empty}>{STRINGS.vocabulary.filterEmpty}</Text> : null}

      {filtered.map((favorite) => (
        <View style={styles.card} key={favorite.id}>
          <View style={styles.cardTop}>
            <View style={styles.cardIcon}>
              <Feather name="bookmark" size={18} color="#14b8a6" />
            </View>
            <View style={styles.cardCopy}>
              <Text style={styles.cardTitle}>{favorite.phrase.target_text}</Text>
              <Text style={styles.cardDetail}>{favorite.phrase.source_text}</Text>
            </View>
          </View>

          <View style={styles.meta}>
            <Text style={styles.badge}>{favorite.phrase.scenario_title || STRINGS.vocabulary.scenarioFallback}</Text>
            <Text style={styles.badge}>{favorite.phrase.category || STRINGS.vocabulary.categoryFallback}</Text>
            {favorite.phrase.difficulty ? (
              <Text style={styles.badge}>{`${STRINGS.vocabulary.difficultyLabel}: ${favorite.phrase.difficulty}`}</Text>
            ) : null}
          </View>

          <Pressable style={styles.remove} onPress={() => removeFavorite(favorite.id)}>
            <Feather name="trash-2" size={14} color="#dc2626" />
            <Text style={styles.removeText}>{STRINGS.vocabulary.remove}</Text>
          </Pressable>
        </View>
      ))}
    </ScrollView>
  );
}

function Summary({ value, label }: { value: number; label: string }) {
  return (
    <View style={styles.summaryCard}>
      <Text style={styles.summaryValue}>{value}</Text>
      <Text style={styles.summaryLabel}>{label}</Text>
    </View>
  );
}

function EmptyState() {
  return (
    <View style={styles.emptyCard}>
      <View style={styles.emptyIcon}>
        <Feather name="layers" size={24} color="#14b8a6" />
      </View>
      <Text style={styles.emptyTitle}>{STRINGS.vocabulary.emptyTitle}</Text>
      <Text style={styles.emptyDetail}>{STRINGS.vocabulary.emptyDetail}</Text>
    </View>
  );
}

function State({ message }: { message: string }) {
  return (
    <View style={styles.state}>
      <Text style={styles.stateText}>{message}</Text>
    </View>
  );
}

function getUnique(values: Array<string | null | undefined>) {
  return Array.from(new Set(values.filter((value): value is string => Boolean(value))));
}
