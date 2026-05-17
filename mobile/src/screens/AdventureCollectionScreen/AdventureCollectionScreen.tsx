import { Link } from "expo-router";
import { useEffect, useMemo, useState } from "react";
import { Modal, Pressable, ScrollView, Text, View } from "react-native";
import { STRINGS, adventureService } from "@linguaflow/shared-core";
import type {
  ApiAdventureCharacter,
  ApiUserChest,
  ApiUserInventoryItem,
  HeroStats,
} from "@linguaflow/shared-core";
import { styles } from "./AdventureCollectionScreen.styles";

type CollectionKind = "inventory" | "chests" | "words" | "hero" | "characters";

interface CollectionState {
  inventory: ApiUserInventoryItem[];
  chests: ApiUserChest[];
  words: Array<{ word_id: string; target: string; native: string; tier: string }>;
  hero: HeroStats | null;
  characters: ApiAdventureCharacter[];
}

const EMPTY_STATE: CollectionState = {
  inventory: [],
  chests: [],
  words: [],
  hero: null,
  characters: [],
};

const TABS: Array<{ href: "/(tabs)/adventure" | "/adventure/inventory" | "/adventure/chests" | "/adventure/words" | "/adventure/hero" | "/adventure/characters"; kind: CollectionKind | "map"; label: string }> = [
  { href: "/(tabs)/adventure", kind: "map", label: "Mapa" },
  { href: "/adventure/inventory", kind: "inventory", label: "Mochila" },
  { href: "/adventure/chests", kind: "chests", label: "Baus" },
  { href: "/adventure/words", kind: "words", label: "Palavras" },
  { href: "/adventure/hero", kind: "hero", label: "Heroi" },
  { href: "/adventure/characters", kind: "characters", label: "Personagens" },
];

const TITLES: Record<CollectionKind, { eyebrow: string; title: string; subtitle: string }> = {
  inventory: { eyebrow: "Inventario", title: "Mochila", subtitle: "Itens ganhos na historia." },
  chests: { eyebrow: "Recompensas", title: "Baus", subtitle: "Baus guardados e prontos." },
  words: { eyebrow: "Vocabulario", title: "Palavras", subtitle: "Palavras desbloqueadas." },
  hero: { eyebrow: "Progresso", title: "Heroi", subtitle: "Nivel, XP e atributos." },
  characters: { eyebrow: "Elenco", title: "Personagens", subtitle: "Figuras encontradas na aventura." },
};

export function AdventureCollectionScreen({ kind }: { kind: CollectionKind }) {
  const [data, setData] = useState<CollectionState>(EMPTY_STATE);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedCharacter, setSelectedCharacter] = useState<ApiAdventureCharacter | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);

    loadCollection(kind)
      .then((nextData) => {
        if (!cancelled) setData(nextData);
      })
      .catch(() => {
        if (!cancelled) setError("Nao foi possivel carregar esta area.");
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });

    return () => {
      cancelled = true;
    };
  }, [kind]);

  const title = TITLES[kind];
  const count = useMemo(() => getCount(kind, data), [kind, data]);

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.tabs}>
        {TABS.map((tab) => (
          <Link key={tab.kind} href={tab.href} style={[styles.tab, tab.kind === kind ? styles.activeTab : null]}>
            {tab.label}
          </Link>
        ))}
      </ScrollView>

      <View style={styles.header}>
        <View style={styles.headerText}>
          <Text style={styles.eyebrow}>{title.eyebrow}</Text>
          <Text style={styles.title}>{title.title}</Text>
          <Text style={styles.subtitle}>{title.subtitle}</Text>
        </View>
        <Text style={styles.count}>{count}</Text>
      </View>

      {loading ? <StateMessage message="Carregando..." /> : null}
      {error ? <StateMessage message={error} /> : null}
      {!loading && !error ? renderCollection(kind, data, setSelectedCharacter) : null}
      <CharacterModal character={selectedCharacter} onClose={() => setSelectedCharacter(null)} />
    </ScrollView>
  );
}

async function loadCollection(kind: CollectionKind): Promise<CollectionState> {
  if (kind === "inventory") return { ...EMPTY_STATE, inventory: await adventureService.listInventory() };
  if (kind === "chests") return { ...EMPTY_STATE, chests: await adventureService.listChests() };
  if (kind === "words") return { ...EMPTY_STATE, words: await adventureService.listLearnedWords("ES") };
  if (kind === "hero") return { ...EMPTY_STATE, hero: await adventureService.getHeroStats() };
  return { ...EMPTY_STATE, characters: await adventureService.listCharacters("es-a1-t1") };
}

function renderCollection(
  kind: CollectionKind,
  data: CollectionState,
  onCharacterSelect: (character: ApiAdventureCharacter) => void,
) {
  if (kind === "inventory") {
    if (data.inventory.length === 0) return <StateMessage message="Sua mochila esta vazia." />;
    return data.inventory.map((entry) => (
      <ItemCard
        key={entry.id}
        emoji={entry.item.emoji}
        title={entry.item.name}
        detail={entry.item.lore}
        meta={`${entry.item.rarity} · ${entry.is_used ? "usado" : "disponivel"}`}
      />
    ));
  }

  if (kind === "chests") {
    if (data.chests.length === 0) return <StateMessage message="Complete fases com bau para guardar recompensas aqui." />;
    return data.chests.map((chest) => (
      <ItemCard
        key={chest.id}
        emoji="▣"
        title={`Bau ${chest.chest_tier}`}
        detail={`Fase ${chest.phase_number} · score ${chest.phase_score}`}
        meta={`${chest.status}${chest.is_ready ? " · pronto" : ""}`}
      />
    ));
  }

  if (kind === "words") {
    if (data.words.length === 0) return <StateMessage message="Complete a primeira secao para ver palavras aqui." />;
    return data.words.map((word) => (
      <View key={word.word_id} style={styles.wordRow}>
        <Text style={styles.wordTarget}>{word.target}</Text>
        <Text style={styles.wordNative}>{word.native}</Text>
        <Text style={styles.meta}>{word.tier}</Text>
      </View>
    ));
  }

  if (kind === "hero") {
    if (!data.hero) return <StateMessage message="Dados do heroi indisponiveis." />;
    return (
      <View style={styles.metricGrid}>
        <Metric label="Nivel" value={String(data.hero.level)} />
        <Metric label="XP" value={String(data.hero.xp)} />
        <Metric label="Fases" value={String(data.hero.phases_completed)} />
        <Metric label="Sequencia" value={String(data.hero.current_streak)} />
        <Metric label="Vocabulario" value={String(data.hero.attributes.vocabulario)} />
        <Metric label="Gramatica" value={String(data.hero.attributes.gramatica)} />
        <Metric label="Fluencia" value={String(data.hero.attributes.fluencia)} />
      </View>
    );
  }

  if (data.characters.length === 0) return <StateMessage message="Os personagens aparecerao conforme voce avanca." />;
  return data.characters.map((character) => (
    <ItemCard
      key={character.id}
      emoji={character.emoji}
      title={character.name}
      detail={character.description}
      meta={`${character.role} · ${character.is_met ? STRINGS.adventure.met : STRINGS.adventure.undiscovered}`}
      onPress={() => onCharacterSelect(character)}
    />
  ));
}

function ItemCard({
  emoji,
  title,
  detail,
  meta,
  onPress,
}: {
  emoji: string;
  title: string;
  detail: string;
  meta: string;
  onPress?: () => void;
}) {
  const content = (
    <>
      <Text style={styles.emoji}>{emoji}</Text>
      <View style={styles.cardText}>
        <Text style={styles.cardTitle}>{title}</Text>
        <Text style={styles.cardDetail}>{detail}</Text>
        <Text style={styles.meta}>{meta}</Text>
      </View>
    </>
  );

  if (onPress) {
    return (
      <Pressable style={({ pressed }) => [styles.card, styles.pressableCard, pressed ? styles.pressedCard : null]} onPress={onPress}>
        {content}
      </Pressable>
    );
  }

  return (
    <View style={styles.card}>
      {content}
    </View>
  );
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <View style={styles.metric}>
      <Text style={styles.metricLabel}>{label}</Text>
      <Text style={styles.metricValue}>{value}</Text>
    </View>
  );
}

function CharacterModal({
  character,
  onClose,
}: {
  character: ApiAdventureCharacter | null;
  onClose: () => void;
}) {
  return (
    <Modal animationType="fade" transparent visible={Boolean(character)} onRequestClose={onClose}>
      <Pressable style={styles.modalBackdrop} onPress={onClose}>
        {character ? (
          <Pressable style={styles.modalPanel} onPress={(event) => event.stopPropagation()}>
            <Pressable style={styles.closeButton} onPress={onClose}>
              <Text style={styles.closeButtonText}>×</Text>
            </Pressable>
            <View style={styles.modalHero}>
              <Text style={styles.modalEmoji}>{character.emoji}</Text>
              <View style={styles.modalHeroText}>
                <Text style={styles.modalRole}>{character.role}</Text>
                <Text style={styles.modalTitle}>{character.name}</Text>
                <Text style={styles.meta}>{character.character_type} · {character.is_met ? STRINGS.adventure.met : STRINGS.adventure.undiscovered}</Text>
              </View>
            </View>
            {character.quote ? <Text style={styles.quote}>{character.quote}</Text> : null}
            <Text style={styles.modalDescription}>{character.description}</Text>
            <View style={styles.factGrid}>
              <View style={styles.fact}>
                <Text style={styles.factLabel}>{STRINGS.adventure.languageBridge}</Text>
                <Text style={styles.factValue}>{character.lang_bridge ? STRINGS.adventure.yes : STRINGS.adventure.no}</Text>
              </View>
              <View style={styles.fact}>
                <Text style={styles.factLabel}>{STRINGS.adventure.narrativeOrder}</Text>
                <Text style={styles.factValue}>{character.order}</Text>
              </View>
            </View>
          </Pressable>
        ) : null}
      </Pressable>
    </Modal>
  );
}

function StateMessage({ message }: { message: string }) {
  return <Text style={styles.state}>{message}</Text>;
}

function getCount(kind: CollectionKind, data: CollectionState) {
  if (kind === "inventory") return String(data.inventory.length);
  if (kind === "chests") return String(data.chests.length);
  if (kind === "words") return String(data.words.length);
  if (kind === "characters") return String(data.characters.filter((character) => character.is_met).length);
  if (!data.hero) return "0";
  return `Nv ${data.hero.level}`;
}
