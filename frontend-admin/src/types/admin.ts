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
