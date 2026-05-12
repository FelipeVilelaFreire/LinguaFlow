export interface Language {
  id: number;
  code: string;
  name: string;
}

export interface Scenario {
  id: number;
  slug: string;
  title: string;
  description: string;
  phrase_count: number;
}

export interface StudyLesson {
  id: number;
  slug: string;
  title: string;
  description: string;
  adventure_phase: number | null;
  order: number;
  phrase_count: number;
}

export interface StudyModule {
  id: number;
  title: string;
  lang_code: string;
  order: number;
  lessons: StudyLesson[];
}

export interface Phrase {
  id: number;
  source_language: Language;
  target_language: Language;
  source_text: string;
  target_text: string;
  category: string;
  scenario: number | null;
  scenario_title: string;
  difficulty: string;
}

export interface Lesson {
  id: number;
  title: string;
  day_number: number;
  scenario: Scenario;
  phrases: Phrase[];
  video_title: string;
  video_url: string;
  video_duration: string;
}

export type PracticeItemType = "intro" | "new" | "multiple_choice" | "fill_blank" | "reverse" | "dictation" | "word_order" | "review";

export interface PreviewPhrase {
  source_text: string;
  target_text: string;
  source_code: string;
  target_code: string;
}

export interface PracticeItem {
  id: string;
  type: PracticeItemType;
  prompt: string;
  answer: string;
  helper: string;
  options: string[];
  word_bank: string[];
  preview_phrases?: PreviewPhrase[];
  phrase: Phrase | null;
}

export interface StudyDay {
  id: number;
  day_number: number;
  lesson: Lesson;
  practice_items: PracticeItem[];
  is_active: boolean;
  completed: boolean;
}

export interface Goal {
  id: number;
  source_language?: Language;
  target_language?: Language;
  current_level: string;
  target_level: string;
  duration_days: number;
  total_phrases: number;
  learned_phrases: number;
  completed_lessons: number;
  streak_days: number;
  study_weekdays: number[];
  session_minutes: number;
  is_study_day_today: boolean;
  next_study_date: string | null;
  is_active: boolean;
  progress_percent: number;
}

export interface Favorite {
  id: number;
  phrase: Phrase;
  created_at: string;
}

export interface HistoryLesson {
  id: number;
  lesson_title: string;
  study_day: number;
  completed_at: string;
}

export interface HistoryDay {
  date: string;
  planned: boolean;
  completed: boolean;
  completion_count: number;
  lessons: HistoryLesson[];
}

export interface GoalHistory {
  goal: Goal;
  days: HistoryDay[];
}

export interface HistoryMonth {
  year: number;
  month: number;
  goals: GoalHistory[];
}

// ─── SRS Study Session ────────────────────────────────────────────────────────

export interface StudySessionOption {
  id: string;
  text: string;
}

export interface StudySessionExercise {
  kind: "multiple_choice" | "write_word";
  word_id: string;
  tier: string;
  target: string;
  native: string;
  // multiple_choice fields
  question?: string;
  options?: StudySessionOption[];
  correct?: string;
  // write_word fields
  prompt?: string;
  answer?: string;
  hint?: string;
}

export interface StudySessionData {
  total: number;
  due_count: number;
  exercises: StudySessionExercise[];
}
