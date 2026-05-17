export type WordTier = "bronze" | "prata" | "ouro" | "diamante" | "esmeralda";
export type VoiceGender = "male" | "female" | "neutral";

export interface VoiceProfile {
  lang?: string;
  gender?: VoiceGender;
  pitch?: number;
  rate?: number;
  voiceName?: string;
}

export interface SkillCheckStep {
  kind: "skill_check";
  skill: string;
  min_level: number;
  success: string;
  fallback: string;
  uses_item_tag?: string;
  reward_hint?: string;
}

export type NarrativaBeat =
  | { kind: "scene"; text: string }
  | { kind: "narrative"; text: string }
  | { kind: "npc"; npc: string; line: string; translation?: string; pace?: "slow" | "normal" | "urgent"; speech_rate?: number; voice?: VoiceProfile; audio_url?: string }
  | { kind: "player"; text: string }
  | SkillCheckStep;

export type ItemBonusKind =
  | "skip_exercise"
  | "extra_dialogue"
  | "relationship_boost"
  | "reduce_gated";

export interface ItemMomentStep {
  kind: "item_moment";
  npc: string;
  situation: string;
  npc_line: string;
  npc_line_audio_url?: string;
  item_tag: string;
  on_use: {
    narrative: string;
    npc_reaction: string;
    npc_reaction_audio_url?: string;
    bonus: ItemBonusKind;
  };
  on_skip: {
    npc_reaction: string;
  };
}

export type SectionStep =
  | { kind: "narrative"; text: string }
  | { kind: "scene"; text: string }
  | { kind: "npc_speak"; npc: string; line: string; translation?: string; is_new_npc?: boolean; pace?: "slow" | "normal" | "urgent"; speech_rate?: number; voice?: VoiceProfile; audio_url?: string }
  | { kind: "player_react"; text: string }
  | { kind: "reveal"; phrase: string; meaning: string; note?: string }
  | { kind: "pattern"; parts: Array<{ text: string; isKey: boolean }>; example: string; translation: string; note: string }
  | { kind: "vocab_list"; items: Array<{ target: string; native: string }> }
  | { kind: "multiple_choice"; question: string; options: Array<{ id: string; text: string }>; correct: string; explanation?: string; word_id?: string; target?: string; native?: string; tier?: WordTier; npc?: string; npc_reaction?: string; npc_reaction_audio_url?: string }
  | { kind: "fill_blank"; prompt: string; answer: string }
  | { kind: "translate"; source: string; answer: string }
  | { kind: "write_word"; prompt: string; word_id: string; answer: string; tier: Extract<WordTier, "diamante" | "esmeralda">; hint?: string }
  | SkillCheckStep
  | ItemMomentStep;

export interface SectionRecap {
  story: string;
  now?: string;
  characters?: string[];
}

interface BaseSection {
  recap?: SectionRecap;
}

export interface NarrativaSection extends BaseSection {
  type: "narrativa";
  beats: NarrativaBeat[];
  exercises?: SectionStep[];
}

export interface RevisaoSrsSection extends BaseSection {
  type: "revisao_srs";
  steps: SectionStep[];
}

export interface PraticaAplicadaSection extends BaseSection {
  type: "pratica_aplicada";
  steps: SectionStep[];
}

export interface GramaticaNarrativaSection extends BaseSection {
  type: "gramatica_narrativa";
  steps: SectionStep[];
}

export interface ReforcoSection extends BaseSection {
  type: "reforco";
  steps: SectionStep[];
}

export interface ObstaculoSection extends BaseSection {
  type: "obstaculo";
  steps: SectionStep[];
}

export type PhaseSection =
  | NarrativaSection
  | RevisaoSrsSection
  | PraticaAplicadaSection
  | GramaticaNarrativaSection
  | ReforcoSection
  | ObstaculoSection;
