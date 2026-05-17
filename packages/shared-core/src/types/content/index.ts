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
  question?: string;
  options?: StudySessionOption[];
  correct?: string;
  prompt?: string;
  answer?: string;
  hint?: string;
}

export interface StudySessionData {
  total: number;
  due_count: number;
  exercises: StudySessionExercise[];
}
