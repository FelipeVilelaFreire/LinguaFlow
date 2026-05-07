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
