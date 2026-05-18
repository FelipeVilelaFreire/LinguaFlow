"use client";

import { getAdventureColors, getAdventureThemeVars, getCharacterAvatar, ROUTES, STRINGS, adventureService } from "@linguaflow/shared-core";
import type {
  ApiAdventureCharacter,
  ApiUserChest,
  ApiUserInventoryItem,
  HeroStats,
} from "@linguaflow/shared-core";
import Link from "next/link";
import type { CSSProperties } from "react";
import { useEffect, useMemo, useState } from "react";
import { CharacterAvatar } from "@/src/components/shared";
import { LangFlag } from "@/src/components/shared";
import {
  AdventureCharacterModal,
  AdventureCollectionDetailModal,
  type AdventureCollectionDetail,
  type LearnedWord,
} from "@/src/components/modals";
import styles from "./AdventureCollectionScreen.module.css";

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

const TABS: Array<{ kind: CollectionKind | "hub" | "map"; href: string; label: string }> = [
  { kind: "hub", href: ROUTES.adventure, label: STRINGS.adventure.title },
  { kind: "map", href: ROUTES.adventureMap, label: STRINGS.adventure.mapTitle },
  { kind: "inventory", href: ROUTES.adventureMochila, label: STRINGS.adventure.inventory },
  { kind: "chests", href: ROUTES.adventureBaus, label: STRINGS.adventure.chests },
  { kind: "words", href: ROUTES.adventurePalavras, label: STRINGS.adventure.words },
  { kind: "hero", href: ROUTES.adventureHeroi, label: STRINGS.adventure.hero },
  { kind: "characters", href: ROUTES.adventurePersonagens, label: STRINGS.adventure.characters },
];

const TITLES: Record<CollectionKind, { eyebrow: string; title: string; subtitle: string }> = {
  inventory: {
    eyebrow: STRINGS.adventure.inventoryEyebrow,
    title: STRINGS.adventure.inventory,
    subtitle: STRINGS.adventure.inventorySubtitle,
  },
  chests: {
    eyebrow: STRINGS.adventure.chestsEyebrow,
    title: STRINGS.adventure.chests,
    subtitle: STRINGS.adventure.chestsSubtitle,
  },
  words: {
    eyebrow: STRINGS.adventure.wordsEyebrow,
    title: STRINGS.adventure.words,
    subtitle: STRINGS.adventure.wordsSubtitle,
  },
  hero: {
    eyebrow: STRINGS.adventure.heroEyebrow,
    title: STRINGS.adventure.hero,
    subtitle: STRINGS.adventure.heroSubtitle,
  },
  characters: {
    eyebrow: STRINGS.adventure.charactersEyebrow,
    title: STRINGS.adventure.characters,
    subtitle: STRINGS.adventure.charactersSubtitle,
  },
};

export function AdventureCollectionScreen({ kind }: { kind: CollectionKind }) {
  const langCode = "ES";
  const themeStyle = getAdventureThemeVars(getAdventureColors(langCode, "dark")) as CSSProperties;
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
    <main className={styles.page} style={themeStyle}>
      <nav className={styles.tabs} aria-label={STRINGS.adventure.title}>
        {TABS.map((tab) => (
          <Link key={tab.href} className={tab.kind === kind ? styles.activeTab : ""} href={tab.href}>
            {tab.label}
          </Link>
        ))}
      </nav>

      <header className={styles.header}>
        <div>
          <p><LangFlag code={langCode} size="xs" /> {title.eyebrow}</p>
          <h1>{title.title}</h1>
          <span>{title.subtitle}</span>
        </div>
        <strong>{count}</strong>
      </header>

      {loading ? <StateMessage message={STRINGS.adventure.loading} /> : null}
      {error ? <StateMessage message={error} /> : null}
      {!loading && !error ? renderCollection(kind, data, setSelectedCharacter, setSelectedDetail, langCode) : null}
      {selectedCharacter ? <AdventureCharacterModal character={selectedCharacter} onClose={() => setSelectedCharacter(null)} /> : null}
      {selectedDetail ? (
        <AdventureCollectionDetailModal detail={selectedDetail} onClose={() => setSelectedDetail(null)} onRefresh={refreshCollection} />
      ) : null}
    </main>
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
  langCode: string,
) {
  if (kind === "inventory") {
    if (data.inventory.length === 0) return <StateMessage message={STRINGS.adventure.inventoryEmpty} />;
    return (
      <section className={styles.grid}>
        {data.inventory.map((entry) => (
          <button
            className={`${styles.itemCard} ${styles.clickableCard}`}
            key={entry.id}
            onClick={() => onDetailSelect({ type: "inventory", item: entry })}
            type="button"
          >
            <span className={styles.emoji}>{entry.item.emoji}</span>
            <div>
              <h2>{entry.item.name}</h2>
              <p>{entry.item.lore}</p>
              <small>{entry.item.rarity} - {entry.is_used ? STRINGS.adventure.used : STRINGS.adventure.available}</small>
            </div>
          </button>
        ))}
      </section>
    );
  }

  if (kind === "chests") {
    if (data.chests.length === 0) return <StateMessage message={STRINGS.adventure.chestsEmpty} />;
    return <ChestBoard chests={data.chests} onDetailSelect={onDetailSelect} />;
  }

  if (kind === "words") {
    if (data.words.length === 0) return <StateMessage message={STRINGS.adventure.wordsEmpty} />;
    return (
      <section className={styles.wordList}>
        {data.words.map((word) => (
          <button className={`${styles.wordRow} ${styles.clickableRow}`} key={word.word_id} onClick={() => onDetailSelect({ type: "word", word })} type="button">
            <strong>{word.target}</strong>
            <span>{word.native}</span>
            <small>{word.tier}</small>
          </button>
        ))}
      </section>
    );
  }

  if (kind === "hero") {
    if (!data.hero) return <StateMessage message={STRINGS.adventure.heroEmpty} />;
    return (
      <section className={styles.heroGrid}>
        <Metric label={STRINGS.adventure.heroLevel} value={String(data.hero.level)} />
        <Metric label={STRINGS.adventure.heroXp} value={String(data.hero.xp)} />
        <Metric label={STRINGS.adventure.heroPhases} value={String(data.hero.phases_completed)} />
        <Metric label={STRINGS.adventure.heroStreak} value={String(data.hero.current_streak)} />
        <Metric label={STRINGS.adventure.heroVocabulary} value={String(data.hero.attributes.vocabulario)} />
        <Metric label={STRINGS.adventure.heroGrammar} value={String(data.hero.attributes.gramatica)} />
        <Metric label={STRINGS.adventure.heroFluency} value={String(data.hero.attributes.fluencia)} />
      </section>
    );
  }

  if (data.characters.length === 0) return <StateMessage message={STRINGS.adventure.charactersEmpty} />;
  return (
    <section className={styles.grid}>
      {data.characters.map((character) => (
        <button
          type="button"
          className={`${styles.itemCard} ${styles.clickableCard}`}
          key={character.id}
          onClick={() => onCharacterSelect(character)}
        >
          <CharacterAvatar
            emoji={character.emoji}
            langCode={langCode}
            name={character.name}
            size={48}
            slug={character.slug || getCharacterAvatar(character.name)?.slug}
          />
          <div>
            <h2>{character.name}</h2>
            <p>{character.description}</p>
            <small>{character.role} - {character.is_met ? STRINGS.adventure.met : STRINGS.adventure.undiscovered}</small>
          </div>
        </button>
      ))}
    </section>
  );
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <article className={styles.metric}>
      <span>{label}</span>
      <strong>{value}</strong>
    </article>
  );
}

function ChestBoard({ chests, onDetailSelect }: { chests: ApiUserChest[]; onDetailSelect: (detail: AdventureCollectionDetail) => void }) {
  const activeChests = chests.filter((chest) => chest.status !== "claimed" && chest.status !== "discarded");
  const slotChests = activeChests.filter((chest) => chest.status === "opening" || chest.status === "ready").slice(0, 2);
  const storedChests = activeChests.filter((chest) => chest.status === "stored");
  const claimedChests = chests.filter((chest) => chest.status === "claimed").slice(0, 6);
  const readyCount = slotChests.filter((chest) => chest.is_ready || chest.status === "ready").length;

  return (
    <section className={styles.chestBoard}>
      <div className={styles.chestSummary}>
        <Metric label={STRINGS.adventure.chestsStoredMetric} value={String(storedChests.length)} />
        <Metric label={STRINGS.adventure.chestsOpeningMetric} value={String(slotChests.length)} />
        <Metric label={STRINGS.adventure.chestsReadyMetric} value={String(readyCount)} />
      </div>

      <div className={styles.chestSectionHeader}>
        <h2>{STRINGS.adventure.chestsSlotsTitle}</h2>
        <span>{slotChests.length}/2</span>
      </div>
      <div className={styles.grid}>
        {[0, 1].map((slot) => {
          const chest = slotChests[slot];
          if (!chest) {
            return (
              <article className={styles.emptyChestSlot} key={slot}>
                <span>□</span>
                <strong>{STRINGS.adventure.chestSlotEmpty}</strong>
              </article>
            );
          }
          return <ChestCard chest={chest} key={chest.id} onPress={() => onDetailSelect({ type: "chest", chest })} />;
        })}
      </div>

      {storedChests.length > 0 ? (
        <>
          <div className={styles.chestSectionHeader}>
            <h2>{STRINGS.adventure.chestsStoredTitle}</h2>
            {slotChests.length >= 2 ? <span>{STRINGS.adventure.chestsSlotsFull}</span> : null}
          </div>
          <section className={styles.grid}>
            {storedChests.map((chest) => <ChestCard chest={chest} key={chest.id} onPress={() => onDetailSelect({ type: "chest", chest })} />)}
          </section>
        </>
      ) : null}

      {claimedChests.length > 0 ? (
        <>
          <div className={styles.chestSectionHeader}>
            <h2>{STRINGS.adventure.chestAlreadyClaimed}</h2>
          </div>
          <section className={styles.grid}>
            {claimedChests.map((chest) => <ChestCard chest={chest} key={chest.id} onPress={() => onDetailSelect({ type: "chest", chest })} />)}
          </section>
        </>
      ) : null}
    </section>
  );
}

function ChestCard({ chest, onPress }: { chest: ApiUserChest; onPress: () => void }) {
  const remaining = getChestRemaining(chest);
  const ready = chest.is_ready || chest.status === "ready";

  return (
    <button className={`${styles.itemCard} ${styles.clickableCard} ${styles.chestCard}`} onClick={onPress} type="button">
      <span className={styles.emoji}>□</span>
      <div>
        <h2>{STRINGS.adventure.chestTitle(chest.chest_tier)}</h2>
        <p>{STRINGS.adventure.phaseScore(chest.phase_number, chest.phase_score)}</p>
        <small>{ready ? STRINGS.adventure.chestReadyToClaim : chest.status === "opening" ? remaining : STRINGS.adventure.chestStoredForLater}</small>
        {chest.status === "opening" ? <span className={styles.chestProgress}><i style={{ width: `${getChestProgress(chest)}%` }} /></span> : null}
      </div>
    </button>
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

function StateMessage({ message }: { message: string }) {
  return <p className={styles.state}>{message}</p>;
}

function getCount(kind: CollectionKind, data: CollectionState) {
  if (kind === "inventory") return String(data.inventory.length);
  if (kind === "chests") return String(data.chests.length);
  if (kind === "words") return String(data.words.length);
  if (kind === "characters") return String(data.characters.filter((character) => character.is_met).length);
  if (!data.hero) return "0";
  return `${STRINGS.adventure.heroLevel} ${data.hero.level}`;
}




