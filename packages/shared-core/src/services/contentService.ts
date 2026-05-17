import { api } from "../lib/apiClient";
import type {
  Favorite,
  Goal,
  HistoryMonth,
  Phrase,
  Scenario,
  StudyDay,
  StudyModule,
} from "../types/content";

export const contentService = {
  getCurrentGoal: () => api().request<Goal>("/goals/current/"),
  listGoals: () => api().request<Goal[]>("/goals/"),
  activateGoal: (goalId: number) => api().request<Goal>(`/goals/${goalId}/activate/`, { method: "POST" }),
  deleteGoal: (goalId: number) => api().request<{ current_goal: Goal | null }>(`/goals/${goalId}/`, { method: "DELETE" }),
  getToday: () => api().request<StudyDay>("/study-days/today/"),
  getHistory: (year: number, month: number) => api().request<HistoryMonth>(`/goals/history/?year=${year}&month=${month}`),
  listScenarios: () => api().request<Scenario[]>("/scenarios/"),
  listStudyModules: () => api().request<StudyModule[]>("/study/modules/"),
  listPhrases: (scenario?: string) => api().request<Phrase[]>(scenario ? `/phrases/?scenario=${scenario}` : "/phrases/"),
  listFavorites: () => api().request<Favorite[]>("/favorites/"),
  favoritePhrase: (phraseId: number) => api().request<Favorite>("/favorites/", {
    method: "POST",
    body: JSON.stringify({ phrase_id: phraseId }),
  }),
  markProgress: (data: { phrase_id: number; correct: boolean; answer: string }) =>
    api().request<void>("/progress/mark/", { method: "POST", body: JSON.stringify(data) }),
  createGoal: (data: {
    source_language: string;
    target_language: string;
    current_level?: string;
    target_level: string;
    duration_days: number;
    study_weekdays: number[];
    session_minutes: number;
  }) => api().request<Goal>("/goals/onboarding/", { method: "POST", body: JSON.stringify(data) }),
  updateGoal: (goalId: number, data: { study_weekdays?: number[]; session_minutes?: number }) =>
    api().request<Goal>(`/goals/${goalId}/`, { method: "PATCH", body: JSON.stringify(data) }),
  completeStudyDay: (studyDayId: number) =>
    api().request<{ completed: boolean }>(`/study-days/${studyDayId}/complete/`, { method: "POST" }),
  removeFavorite: (favoriteId: number) =>
    api().request<void>(`/favorites/${favoriteId}/`, { method: "DELETE" }),
};
