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

export interface StudyDay {
  id: number;
  day_number: number;
  lesson: Lesson;
  is_active: boolean;
  completed: boolean;
}

export interface Goal {
  id: number;
  source_language?: Language;
  target_language?: Language;
  target_level: string;
  duration_days: number;
  total_phrases: number;
  learned_phrases: number;
  completed_lessons: number;
  streak_days: number;
  is_active: boolean;
  progress_percent: number;
}

export interface Favorite {
  id: number;
  phrase: Phrase;
  created_at: string;
}
