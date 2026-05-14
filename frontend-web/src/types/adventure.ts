// ─── Available languages (from /adventure/chapters/languages/) ───────────────

export interface AvailableLanguage {
  code: string;
  chapter_title: string;
  chapter_subtitle: string;
}

// ─── API shapes (what the backend actually serializes) ────────────────────────
// These lack frontend-only fields (section_count, completed_sections, etc.)
// that are hydrated locally in useAdventureChapters.

export interface ApiAdventurePhase {
  id: number;
  number: number;
  title: string;
  narrative_intro: string;
  narrative_outro: string;
  key_words: string[];
  scenario_slug: string;
  phrase_count: number;
  phase_type: "story" | "review" | "boss";
  npc_name?: string;
  is_boss: boolean;
  is_completed: boolean;
  score: number | null;
  completed_sections: number;
}

export interface ApiAdventureChapter {
  id: number;
  slug: string;
  language_code: string;
  level: string;
  order: number;
  title: string;
  subtitle: string;
  background: string;
  boss_name: string;
  boss_intro: string;
  reward_name: string;
  reward_description: string;
  phases: ApiAdventurePhase[];
  progress: AdventureProgress | null;
}

// ─── Frontend-hydrated shapes ──────────────────────────────────────────────────

export interface AdventureProgress {
  current_phase: number;
  reward_unlocked: boolean;
  started_at: string;
  completed_at: string | null;
}

export type PhaseType = "story" | "review" | "boss";

export interface AdventurePhase {
  id: number;
  number: number;
  title: string;
  narrative_intro: string;
  narrative_outro: string;
  key_words: string[];
  scenario_slug: string;
  phrase_count: number;
  section_count: number;       // always 6
  completed_sections: number;  // 0–6, how many sections are done
  phase_type: PhaseType;
  npc_name: string;
  vocab_gate?: string[];    // Metroidvania: words required to unlock
  is_boss: boolean;
  is_completed: boolean;
  score: number | null;
}

export interface AdventureChapter {
  id: number;
  slug: string;
  language_code: string;
  level: string;
  order: number;
  title: string;
  subtitle: string;
  background: string;
  boss_name: string;
  boss_intro: string;
  reward_name: string;
  reward_description: string;
  phases: AdventurePhase[];
  progress: AdventureProgress | null;
}

// ─── Characters ──────────────────────────────────────────────────────────────

export interface ApiAdventureCharacter {
  id: number;
  slug: string;
  name: string;
  role: string;           // in target language
  emoji: string;
  character_type: "main" | "ally" | "boss" | "npc";
  description: string;
  quote: string;
  lang_bridge: boolean;
  order: number;
  is_met: boolean;        // server-computed per authenticated user
}

// ─── Items / Inventory ────────────────────────────────────────────────────────

export type ItemRarity = "comum" | "raro" | "epico" | "lendario" | "mitico";
export type ItemAction = "examinar" | "entregar" | "usar" | "equipar";
export type ItemTag    = "comida" | "bebida" | "arma" | "documento" | "moneda" | "remedio" | "comum" | "";

export interface ApiAdventureItem {
  id: number;
  slug: string;
  emoji: string;
  name: string;
  lore: string;
  rarity: ItemRarity;
  action: ItemAction;
  order: number;
  source_phase_number: number | null;
  source_character_name: string | null;
  word_id?: string;
  item_tag?: ItemTag;
  is_degraded?: boolean;
}

export interface ApiUserInventoryItem {
  id: number;
  item: ApiAdventureItem;
  earned_at: string;
  is_used: boolean;
  used_at: string | null;
}

export interface StreakData {
  current:       number;
  longest:       number;
  updated_today: boolean;
}

export interface EarnedItemData {
  slug?:  string;
  emoji:  string;
  name:   string;
  lore:   string;
  rarity: ItemRarity;
  action: ItemAction;
}

// ─── Hero stats ───────────────────────────────────────────────────────────────

export interface HeroStats {
  phases_completed: number;
  xp:               number;
  level:            number;
  xp_current_level: number;
  xp_next_level:    number | null;
  current_streak:   number;
  longest_streak:   number;
  total_words:      number;
  words_by_tier: {
    bronze:    number;
    prata:     number;
    ouro:      number;
    diamante:  number;
    esmeralda: number;
  };
  attributes: {
    vocabulario: number;
    gramatica:   number;
    fluencia:    number;
  };
  achievements: Array<{
    key:   string;
    emoji: string;
    label: string;
    desc:  string;
  }>;
}

// ─── Word mastery ─────────────────────────────────────────────────────────────

export type WordTier = "bronze" | "prata" | "ouro" | "diamante" | "esmeralda";

export interface ApiWordMastery {
  word_id: string;
  tier: WordTier;
  streak: number;
  last_seen_at: string | null;
}
