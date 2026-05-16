export interface AdminSummary {
  users: number;
  staff_users: number;
  active_goals: number;
  goals: number;
  languages: number;
  scenarios: number;
  lessons: number;
  study_days: number;
  phrases: number;
  completions: number;
  favorites: number;
  progress_entries: number;
}

export interface AdminUser {
  id: number;
  username: string;
  email: string;
  is_staff: boolean;
  is_superuser: boolean;
  is_active: boolean;
  date_joined: string;
  goal_count: number;
  completion_count: number;
}

export interface AdminGoal {
  id: number;
  user: string | null;
  source_language: string;
  target_language: string;
  current_level: string;
  target_level: string;
  duration_days: number;
  session_minutes: number;
  study_weekdays: number[];
  is_active: boolean;
  learned_phrases: number;
  total_phrases: number;
  completed_lessons: number;
  streak_days: number;
}

export interface AdminScenario {
  id: number;
  slug: string;
  title: string;
  phrase_count: number;
  lesson_count: number;
}

export interface AdminContent {
  languages: Array<{ id: number; code: string; name: string }>;
  scenarios: AdminScenario[];
  phrase_counts: Record<string, number>;
  lesson_count: number;
  study_day_count: number;
}

export interface AdminLearningDetail {
  modules: Array<{ id: number; lang_code: string; title: string; order: number; scenario_count: number }>;
  lessons: Array<{ id: number; title: string; day_number: number; scenario: string; module: string; objective: string; phrase_count: number; has_video: boolean }>;
  study_days: Array<{ id: number; day_number: number; lesson: string; scenario: string; is_active: boolean }>;
  phrases: Array<{ id: number; source_language: string; target_language: string; source_text: string; target_text: string; category: string; scenario: string; difficulty: string }>;
}

export interface AdminAdventure {
  chapters: Array<{ id: number; language: string; level: string; order: number; title: string; boss_name: string; phase_count: number; character_count: number; item_count: number }>;
  phases: Array<{ id: number; chapter: string; language: string; number: number; title: string; scenario_slug: string; phrase_count: number; phase_type: string; has_chest: boolean; chest_tier: string; section_count: number }>;
  sections: Array<{ id: number; phase: number; chapter: string; section_number: number; section_type: string; step_count: number }>;
  characters: Array<{ id: number; chapter: string; name: string; role: string; emoji: string; character_type: string; lang_bridge: boolean; first_phase: number | null }>;
  skills: Array<{ id: number; chapter: string; name: string; category: string; emoji: string; base_power: number; item_count: number }>;
  items: Array<{ id: number; chapter: string; name: string; emoji: string; rarity: string; action: string; item_tag: string; skill: string; source_phase: number | null }>;
  user_counts: { chests: number; inventory_items: number; skill_mastery: number; section_progress: number };
}

export interface AdminProgressDetail {
  completions: Array<{ id: number; user: string; study_day: number; lesson: string; goal: string; completed_at: string }>;
  progress_entries: Array<{ id: number; user: string; phrase: string; status: string; correct_count: number; incorrect_count: number; review_due: string | null; updated_at: string }>;
  favorites: Array<{ id: number; user: string; phrase: string; created_at: string }>;
  word_mastery: Array<{ id: number; user: string; word_id: string; target: string; native: string; lang_code: string; tier: string; streak: number; error_count: number; last_seen_at: string | null }>;
  streaks: Array<{ id: number; user: string; current_streak: number; longest_streak: number; last_active_date: string | null }>;
}
