import type { WordTier } from "../sections";

export interface AvailableLanguage {
  code: string;
  chapter_title: string;
  chapter_subtitle: string;
}

export type PhaseType = "story" | "review" | "boss";

export interface AdventureProgress {
  current_phase: number;
  reward_unlocked: boolean;
  started_at: string;
  completed_at: string | null;
}

export interface ApiAdventurePhase {
  id: number;
  number: number;
  title: string;
  narrative_intro: string;
  narrative_outro: string;
  key_words: string[];
  scenario_slug: string;
  phrase_count: number;
  phase_type: PhaseType;
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

export interface AdventurePhase extends ApiAdventurePhase {
  section_count: number;
  completed_sections: number;
  phase_type: PhaseType;
  npc_name: string;
  vocab_gate?: string[];
}

export interface AdventureChapter extends Omit<ApiAdventureChapter, "phases"> {
  phases: AdventurePhase[];
}

export interface ApiAdventureCharacter {
  id: number;
  slug: string;
  name: string;
  role: string;
  emoji: string;
  character_type: "main" | "ally" | "boss" | "npc";
  description: string;
  quote: string;
  lang_bridge: boolean;
  order: number;
  is_met: boolean;
}

export type ItemRarity = "comum" | "raro" | "epico" | "lendario" | "mitico";
export type ItemAction = "examinar" | "entregar" | "usar" | "equipar";
export type ItemTag = "comida" | "bebida" | "arma" | "documento" | "moneda" | "remedio" | "comum" | "";

export interface ApiAdventureSkill {
  id: number;
  slug: string;
  name: string;
  description: string;
  category: "combate" | "sobrevivencia" | "social" | "investigacao" | "suporte";
  emoji: string;
  base_power: number;
  order: number;
}

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
  skill?: ApiAdventureSkill | null;
  is_degraded?: boolean;
}

export interface ApiUserInventoryItem {
  id: number;
  item: ApiAdventureItem;
  earned_at: string;
  is_used: boolean;
  used_at: string | null;
}

export interface ApiUserChest {
  id: number;
  phase_number: number;
  chapter_slug: string;
  chest_tier: ItemRarity;
  phase_score: number;
  status: "stored" | "opening" | "ready" | "claimed" | "discarded";
  rolled_rarity: ItemRarity | "";
  earned_item: ApiAdventureItem | null;
  created_at: string;
  started_at: string | null;
  unlock_at: string | null;
  claimed_at: string | null;
  is_ready: boolean;
}

export interface ApiUserSkillMastery {
  id: number;
  skill: ApiAdventureSkill;
  xp: number;
  level: number;
  uses_count: number;
  last_used_at: string | null;
}

export interface StreakData {
  current: number;
  longest: number;
  updated_today: boolean;
}

export interface EarnedItemData {
  slug?: string;
  emoji: string;
  name: string;
  lore: string;
  rarity: ItemRarity;
  action: ItemAction;
}

export interface HeroStats {
  phases_completed: number;
  xp: number;
  level: number;
  xp_current_level: number;
  xp_next_level: number | null;
  current_streak: number;
  longest_streak: number;
  total_words: number;
  words_by_tier: Record<"bronze" | "prata" | "ouro" | "diamante" | "esmeralda", number>;
  attributes: {
    vocabulario: number;
    gramatica: number;
    fluencia: number;
  };
  skills?: ApiUserSkillMastery[];
  achievements: Array<{
    key: string;
    emoji: string;
    label: string;
    desc: string;
  }>;
}

export interface ApiWordMastery {
  word_id: string;
  tier: WordTier;
  streak: number;
  last_seen_at: string | null;
}
