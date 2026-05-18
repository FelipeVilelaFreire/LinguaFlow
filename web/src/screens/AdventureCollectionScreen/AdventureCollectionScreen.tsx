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
import { CharacterAvatar } from "@/src/components/CharacterAvatar";
import { LangFlag } from "@/src/components/LangFlag";
import styles from "./AdventureCollectionScreen.module.css";

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

const TABS: Array<{ kind: CollectionKind | "map"; href: string; label: string }> = [
  { kind: "map", href: ROUTES.adventureMap, label: "Mapa" },
  { kind: "inventory", href: ROUTES.adventureMochila, label: "Mochila" },
  { kind: "chests", href: ROUTES.adventureBaus, label: "Baus" },
  { kind: "words", href: ROUTES.adventurePalavras, label: "Palavras" },
  { kind: "hero", href: ROUTES.adventureHeroi, label: "Heroi" },
  { kind: "characters", href: ROUTES.adventurePersonagens, label: "Personagens" },
];

const TITLES: Record<CollectionKind, { eyebrow: string; title: string; subtitle: string }> = {
  inventory: {
    eyebrow: "Inventario",
    title: "Mochila",
    subtitle: "Itens que voce ganhou na historia aparecem aqui.",
  },
  chests: {
    eyebrow: "Recompensas",
    title: "Baus",
    subtitle: "Baus guardados, abrindo ou prontos para coletar.",
  },
  words: {
    eyebrow: "Vocabulario",
    title: "Palavras",
    subtitle: "Palavras desbloqueadas pela aventura.",
  },
  hero: {
    eyebrow: "Progresso",
    title: "Heroi",
    subtitle: "Nivel, XP, sequencia e atributos da jornada.",
  },
  characters: {
    eyebrow: "Elenco",
    title: "Personagens",
    subtitle: "Aliados, NPCs e figuras importantes que voce encontrou.",
  },
};

export function AdventureCollectionScreen({ kind }: { kind: CollectionKind }) {
  const langCode = "ES";
  const themeStyle = getAdventureThemeVars(getAdventureColors(langCode, "dark")) as CSSProperties;
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
        if (!cancelled) setError("Nao foi possivel carregar esta area da aventura.");
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
    <main className={styles.page} style={themeStyle}>
      <nav className={styles.tabs} aria-label="Aventura">
        {TABS.map((tab) => (
          <Link
            key={tab.kind}
            className={tab.kind === kind ? styles.activeTab : ""}
            href={tab.href}
          >
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

      {loading && <StateMessage message="Carregando..." />}
      {error && <StateMessage message={error} />}
      {!loading && !error && renderCollection(kind, data, setSelectedCharacter, langCode)}
      {selectedCharacter ? (
        <CharacterModal character={selectedCharacter} onClose={() => setSelectedCharacter(null)} />
      ) : null}
    </main>
  );
}

async function loadCollection(kind: CollectionKind): Promise<CollectionState> {
  if (kind === "inventory") {
    const inventory = await adventureService.listInventory();
    return { ...EMPTY_STATE, inventory };
  }
  if (kind === "chests") {
    const chests = await adventureService.listChests();
    return { ...EMPTY_STATE, chests };
  }
  if (kind === "words") {
    const words = await adventureService.listLearnedWords("ES");
    return { ...EMPTY_STATE, words };
  }
  if (kind === "hero") {
    const hero = await adventureService.getHeroStats();
    return { ...EMPTY_STATE, hero };
  }
  const characters = await adventureService.listCharacters("es-a1-t1");
  return { ...EMPTY_STATE, characters };
}

function renderCollection(
  kind: CollectionKind,
  data: CollectionState,
  onCharacterSelect: (character: ApiAdventureCharacter) => void,
  langCode: string,
) {
  if (kind === "inventory") {
    if (data.inventory.length === 0) return <StateMessage message="Sua mochila esta vazia. Complete fases para coletar itens." />;
    return (
      <section className={styles.grid}>
        {data.inventory.map((entry) => (
          <article className={styles.itemCard} key={entry.id}>
            <span className={styles.emoji}>{entry.item.emoji}</span>
            <div>
              <h2>{entry.item.name}</h2>
              <p>{entry.item.lore}</p>
              <small>{entry.item.rarity} · {entry.is_used ? "usado" : "disponivel"}</small>
            </div>
          </article>
        ))}
      </section>
    );
  }

  if (kind === "chests") {
    if (data.chests.length === 0) return <StateMessage message="Complete fases com bau para guardar recompensas aqui." />;
    return (
      <section className={styles.grid}>
        {data.chests.map((chest) => (
          <article className={styles.itemCard} key={chest.id}>
            <span className={styles.emoji}>▣</span>
            <div>
              <h2>Bau {chest.chest_tier}</h2>
              <p>Fase {chest.phase_number} · score {chest.phase_score}</p>
              <small>{chest.status}{chest.is_ready ? " · pronto" : ""}</small>
            </div>
          </article>
        ))}
      </section>
    );
  }

  if (kind === "words") {
    if (data.words.length === 0) return <StateMessage message="Complete a primeira secao para ver as palavras aqui." />;
    return (
      <section className={styles.wordList}>
        {data.words.map((word) => (
          <article className={styles.wordRow} key={word.word_id}>
            <strong>{word.target}</strong>
            <span>{word.native}</span>
            <small>{word.tier}</small>
          </article>
        ))}
      </section>
    );
  }

  if (kind === "hero") {
    if (!data.hero) return <StateMessage message="Dados do heroi indisponiveis." />;
    return (
      <section className={styles.heroGrid}>
        <Metric label="Nivel" value={String(data.hero.level)} />
        <Metric label="XP" value={String(data.hero.xp)} />
        <Metric label="Fases" value={String(data.hero.phases_completed)} />
        <Metric label="Sequencia" value={String(data.hero.current_streak)} />
        <Metric label="Vocabulario" value={String(data.hero.attributes.vocabulario)} />
        <Metric label="Gramatica" value={String(data.hero.attributes.gramatica)} />
        <Metric label="Fluencia" value={String(data.hero.attributes.fluencia)} />
      </section>
    );
  }

  if (data.characters.length === 0) return <StateMessage message="Os personagens aparecerao conforme voce avanca." />;
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
            <small>{character.role} · {character.is_met ? STRINGS.adventure.met : STRINGS.adventure.undiscovered}</small>
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

function CharacterModal({
  character,
  onClose,
}: {
  character: ApiAdventureCharacter;
  onClose: () => void;
}) {
  return (
    <div className={styles.modalBackdrop} role="presentation" onClick={onClose}>
      <section
        aria-modal="true"
        className={styles.modalPanel}
        role="dialog"
        onClick={(event) => event.stopPropagation()}
      >
        <button className={styles.closeButton} type="button" onClick={onClose} aria-label="Fechar">
          ×
        </button>
        <div className={styles.modalHero}>
          <CharacterAvatar
            emoji={character.emoji}
            langCode="ES"
            name={character.name}
            size={72}
            slug={character.slug || getCharacterAvatar(character.name)?.slug}
          />
          <div>
            <p>{character.role}</p>
            <h2>{character.name}</h2>
            <small>{character.character_type} · {character.is_met ? STRINGS.adventure.met : STRINGS.adventure.undiscovered}</small>
          </div>
        </div>
        {character.quote ? <blockquote>{character.quote}</blockquote> : null}
        <p className={styles.modalDescription}>{character.description}</p>
        <dl className={styles.modalFacts}>
          <div>
            <dt>{STRINGS.adventure.languageBridge}</dt>
            <dd>{character.lang_bridge ? STRINGS.adventure.yes : STRINGS.adventure.no}</dd>
          </div>
          <div>
            <dt>{STRINGS.adventure.narrativeOrder}</dt>
            <dd>{character.order}</dd>
          </div>
        </dl>
      </section>
    </div>
  );
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
  return `Nv ${data.hero.level}`;
}
