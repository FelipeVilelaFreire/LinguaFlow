import { useEffect, useMemo, useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import { contentService } from "@linguaflow/shared-core";
import type { Favorite } from "@linguaflow/shared-core";
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

  const scenarios = useMemo(
    () => Array.from(new Set(favorites.map((favorite) => favorite.phrase.scenario_title).filter(Boolean))),
    [favorites],
  );
  const filtered = filter ? favorites.filter((favorite) => favorite.phrase.scenario_title === filter) : favorites;

  async function removeFavorite(id: number) {
    await contentService.removeFavorite(id);
    setFavorites((current) => current.filter((favorite) => favorite.id !== id));
  }

  if (loading) return <State message="Carregando vocabulario..." />;
  if (error) return <State message="Nao foi possivel carregar o vocabulario." />;

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <Text style={styles.eyebrow}>Vocabulario</Text>
      <Text style={styles.title}>Frases salvas</Text>
      <Text style={styles.subtitle}>Revise o que voce marcou como importante.</Text>

      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.filters}>
        <Pressable style={[styles.filter, filter === null ? styles.selected : null]} onPress={() => setFilter(null)}>
          <Text style={filter === null ? styles.selectedText : styles.filterText}>Tudo {favorites.length}</Text>
        </Pressable>
        {scenarios.map((scenario) => (
          <Pressable style={[styles.filter, filter === scenario ? styles.selected : null]} key={scenario} onPress={() => setFilter(scenario)}>
            <Text style={filter === scenario ? styles.selectedText : styles.filterText}>{scenario}</Text>
          </Pressable>
        ))}
      </ScrollView>

      {filtered.length === 0 ? <Text style={styles.empty}>Nenhuma frase salva ainda.</Text> : null}
      {filtered.map((favorite) => (
        <View style={styles.card} key={favorite.id}>
          <Text style={styles.cardTitle}>{favorite.phrase.target_text}</Text>
          <Text style={styles.cardDetail}>{favorite.phrase.source_text}</Text>
          {favorite.phrase.scenario_title ? <Text style={styles.badge}>{favorite.phrase.scenario_title}</Text> : null}
          <Pressable style={styles.remove} onPress={() => removeFavorite(favorite.id)}>
            <Text style={styles.removeText}>Remover</Text>
          </Pressable>
        </View>
      ))}
    </ScrollView>
  );
}

function State({ message }: { message: string }) {
  return (
    <View style={styles.state}>
      <Text style={styles.stateText}>{message}</Text>
    </View>
  );
}
