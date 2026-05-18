import { Link } from "expo-router";
import { useEffect, useMemo, useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import { STRINGS, adventureService } from "@linguaflow/shared-core";
import type {
  ApiAdventureCharacter,
  ApiUserChest,
  ApiUserInventoryItem,
  HeroStats,
} from "@linguaflow/shared-core";
import {
  AdventureCharacterModal,
  AdventureCollectionDetailModal,
} from "@/src/components/modals";
import type {
  AdventureCollectionDetail,
  LearnedWord,
} from "@/src/components/modals";
import { styles } from "./AdventureCollectionScreen.styles";

type CollectionKind = "inventory" | "chests" | "words" | "hero" | "characters";

interface CollectionState {
  inventory: ApiUserInventoryItem[];
  chests: ApiUserChest[];
  words: LearnedWord[];
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

const TABS: Array<{ href: string; kind: CollectionKind | "hub" | "map"; label: string }> = [
  { href: "/(tabs)/adventure", kind: "hub", label: STRINGS.adventure.title },
  { href: "/adventure/map", kind: "map", label: STRINGS.adventure.mapTitle },
  { href: "/adventure/inventory", kind: "inventory", label: STRINGS.adventure.inventory },
  { href: "/adventure/chests", kind: "chests", label: STRINGS.adventure.chests },
  { href: "/adventure/words", kind: "words", label: STRINGS.adventure.words },
  { href: "/adventure/hero", kind: "hero", label: STRINGS.adventure.hero },
  { href: "/adventure/characters", kind: "characters", label: STRINGS.adventure.characters },
];

const TITLES: Record<CollectionKind, { eyebrow: string; title: string; subtitle: string }> = {
  inventory: { eyebrow: STRINGS.adventure.inventoryEyebrow, title: STRINGS.adventure.inventory, subtitle: STRINGS.adventure.inventorySubtitle },
  chests: { eyebrow: STRINGS.adventure.chestsEyebrow, title: STRINGS.adventure.chests, subtitle: STRINGS.adventure.chestsSubtitle },
  words: { eyebrow: STRINGS.adventure.wordsEyebrow, title: STRINGS.adventure.words, subtitle: STRINGS.adventure.wordsSubtitle },
  hero: { eyebrow: STRINGS.adventure.heroEyebrow, title: STRINGS.adventure.hero, subtitle: STRINGS.adventure.heroSubtitle },
  characters: { eyebrow: STRINGS.adventure.charactersEyebrow, title: STRINGS.adventure.characters, subtitle: STRINGS.adventure.charactersSubtitle },
};

export function AdventureCollectionScreen({ kind }: { kind: CollectionKind }) {
  const [data, setData] = useState<CollectionState>(EMPTY_STATE);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedCharacter, setSelectedCharacter] = useState<ApiAdventureCharacter | null>(null);
  const [selectedDetail, setSelectedDetail] = useState<AdventureCollectionDetail | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);

    loadCollection(kind)
      .then((nextData) => {
        if (!cancelled) setData(nextData);
      })
      .catch(() => {
        if (!cancelled) setError(STRINGS.adventure.collectionLoadError);
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });

    return () => {
      cancelled = true;
    };
  }, [kind]);

  async function refreshCollection() {
    setData(await loadCollection(kind));
  }

  const title = TITLES[kind];
  const count = useMemo(() => getCount(kind, data), [kind, data]);

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.tabs}>
        {TABS.map((tab) => (
          <Link key={tab.href} href={tab.href} style={[styles.tab, tab.kind === kind ? styles.activeTab : null]}>
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

      {loading ? <StateMessage message={STRINGS.adventure.loading} /> : null}
      {error ? <StateMessage message={error} /> : null}
      {!loading && !error ? renderCollection(kind, data, setSelectedCharacter, setSelectedDetail) : null}
      <AdventureCharacterModal character={selectedCharacter} onClose={() => setSelectedCharacter(null)} />
      <AdventureCollectionDetailModal detail={selectedDetail} onClose={() => setSelectedDetail(null)} onRefresh={refreshCollection} />
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
  onDetailSelect: (detail: AdventureCollectionDetail) => void,
) {
  if (kind === "inventory") {
    if (data.inventory.length === 0) return <StateMessage message={STRINGS.adventure.inventoryEmpty} />;
    return data.inventory.map((entry) => (
      <ItemCard
        key={entry.id}
        emoji={entry.item.emoji}
        title={entry.item.name}
        detail={entry.item.lore}
        meta={`${entry.item.rarity} - ${entry.is_used ? STRINGS.adventure.used : STRINGS.adventure.available}`}
        onPress={() => onDetailSelect({ type: "inventory", item: entry })}
      />
    ));
  }

  if (kind === "chests") {
    if (data.chests.length === 0) return <StateMessage message={STRINGS.adventure.chestsEmpty} />;
    return <ChestBoard chests={data.chests} onDetailSelect={onDetailSelect} />;
  }

  if (kind === "words") {
    if (data.words.length === 0) return <StateMessage message={STRINGS.adventure.wordsEmpty} />;
    return data.words.map((word) => (
      <Pressable key={word.word_id} style={({ pressed }) => [styles.wordRow, styles.pressableCard, pressed ? styles.pressedCard : null]} onPress={() => onDetailSelect({ type: "word", word })}>
        <Text style={styles.wordTarget}>{word.target}</Text>
        <Text style={styles.wordNative}>{word.native}</Text>
        <Text style={styles.meta}>{word.tier}</Text>
      </Pressable>
    ));
  }

  if (kind === "hero") {
    if (!data.hero) return <StateMessage message={STRINGS.adventure.heroEmpty} />;
    return (
      <View style={styles.metricGrid}>
        <Metric label={STRINGS.adventure.heroLevel} value={String(data.hero.level)} />
        <Metric label={STRINGS.adventure.heroXp} value={String(data.hero.xp)} />
        <Metric label={STRINGS.adventure.heroPhases} value={String(data.hero.phases_completed)} />
        <Metric label={STRINGS.adventure.heroStreak} value={String(data.hero.current_streak)} />
        <Metric label={STRINGS.adventure.heroVocabulary} value={String(data.hero.attributes.vocabulario)} />
        <Metric label={STRINGS.adventure.heroGrammar} value={String(data.hero.attributes.gramatica)} />
        <Metric label={STRINGS.adventure.heroFluency} value={String(data.hero.attributes.fluencia)} />
      </View>
    );
  }

  if (data.characters.length === 0) return <StateMessage message={STRINGS.adventure.charactersEmpty} />;
  return data.characters.map((character) => (
    <ItemCard
      key={character.id}
      emoji={character.emoji}
      title={character.name}
      detail={character.description}
      meta={`${character.role} - ${character.is_met ? STRINGS.adventure.met : STRINGS.adventure.undiscovered}`}
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

  return <View style={styles.card}>{content}</View>;
}

function ChestBoard({ chests, onDetailSelect }: { chests: ApiUserChest[]; onDetailSelect: (detail: AdventureCollectionDetail) => void }) {
  const activeChests = chests.filter((chest) => chest.status !== "claimed" && chest.status !== "discarded");
  const slotChests = activeChests.filter((chest) => chest.status === "opening" || chest.status === "ready").slice(0, 2);
  const storedChests = activeChests.filter((chest) => chest.status === "stored");
  const claimedChests = chests.filter((chest) => chest.status === "claimed").slice(0, 6);
  const readyCount = slotChests.filter((chest) => chest.is_ready || chest.status === "ready").length;

  return (
    <View style={styles.chestBoard}>
      <View style={styles.chestSummary}>
        <Metric label={STRINGS.adventure.chestsStoredMetric} value={String(storedChests.length)} />
        <Metric label={STRINGS.adventure.chestsOpeningMetric} value={String(slotChests.length)} />
        <Metric label={STRINGS.adventure.chestsReadyMetric} value={String(readyCount)} />
      </View>
      <SectionHeader title={STRINGS.adventure.chestsSlotsTitle} meta={`${slotChests.length}/2`} />
      {[0, 1].map((slot) => {
        const chest = slotChests[slot];
        if (!chest) {
          return (
            <View key={slot} style={styles.emptyChestSlot}>
              <Text style={styles.emptyChestIcon}>â–¡</Text>
              <Text style={styles.meta}>{STRINGS.adventure.chestSlotEmpty}</Text>
            </View>
          );
        }
        return <ChestCard chest={chest} key={chest.id} onPress={() => onDetailSelect({ type: "chest", chest })} />;
      })}
      {storedChests.length > 0 ? (
        <>
          <SectionHeader title={STRINGS.adventure.chestsStoredTitle} meta={slotChests.length >= 2 ? STRINGS.adventure.chestsSlotsFull : ""} />
          {storedChests.map((chest) => <ChestCard chest={chest} key={chest.id} onPress={() => onDetailSelect({ type: "chest", chest })} />)}
        </>
      ) : null}
      {claimedChests.length > 0 ? (
        <>
          <SectionHeader title={STRINGS.adventure.chestAlreadyClaimed} meta="" />
          {claimedChests.map((chest) => <ChestCard chest={chest} key={chest.id} onPress={() => onDetailSelect({ type: "chest", chest })} />)}
        </>
      ) : null}
    </View>
  );
}

function SectionHeader({ title, meta }: { title: string; meta: string }) {
  return (
    <View style={styles.chestSectionHeader}>
      <Text style={styles.chestSectionTitle}>{title}</Text>
      {meta ? <Text style={styles.chestSectionMeta}>{meta}</Text> : null}
    </View>
  );
}

function ChestCard({ chest, onPress }: { chest: ApiUserChest; onPress: () => void }) {
  const ready = chest.is_ready || chest.status === "ready";
  return (
    <Pressable style={({ pressed }) => [styles.card, styles.pressableCard, styles.chestCard, pressed ? styles.pressedCard : null]} onPress={onPress}>
      <Text style={styles.emoji}>â–¡</Text>
      <View style={styles.cardText}>
        <Text style={styles.cardTitle}>{STRINGS.adventure.chestTitle(chest.chest_tier)}</Text>
        <Text style={styles.cardDetail}>{STRINGS.adventure.phaseScore(chest.phase_number, chest.phase_score)}</Text>
        <Text style={styles.meta}>{ready ? STRINGS.adventure.chestReadyToClaim : chest.status === "opening" ? getChestRemaining(chest) : STRINGS.adventure.chestStoredForLater}</Text>
        {chest.status === "opening" ? <View style={styles.chestProgress}><View style={[styles.chestProgressFill, { width: `${getChestProgress(chest)}%` }]} /></View> : null}
      </View>
    </Pressable>
  );
}

function getChestRemaining(chest: ApiUserChest) {
  if (!chest.unlock_at) return STRINGS.adventure.chestsOpeningMetric;
  const remainingMs = Math.max(0, new Date(chest.unlock_at).getTime() - Date.now());
  const minutes = Math.floor(remainingMs / 60000);
  const seconds = Math.floor((remainingMs % 60000) / 1000);
  return `${minutes}:${seconds.toString().padStart(2, "0")}`;
}

function getChestProgress(chest: ApiUserChest) {
  if (!chest.started_at || !chest.unlock_at) return 0;
  const startedAt = new Date(chest.started_at).getTime();
  const unlockAt = new Date(chest.unlock_at).getTime();
  return Math.min(100, Math.max(0, ((Date.now() - startedAt) / Math.max(1, unlockAt - startedAt)) * 100));
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <View style={styles.metric}>
      <Text style={styles.metricLabel}>{label}</Text>
      <Text style={styles.metricValue}>{value}</Text>
    </View>
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
  return `${STRINGS.adventure.heroLevel} ${data.hero.level}`;
}
