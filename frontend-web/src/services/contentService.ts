import { apiRequest } from "./api";
import type { Favorite, Goal, HistoryMonth, Phrase, Scenario, StudyDay, StudyModule } from "../types/content";

export const contentService = {
  getCurrentGoal: () => apiRequest<Goal>("/goals/current/"),
  listGoals: () => apiRequest<Goal[]>("/goals/"),
  activateGoal: (goalId: number) => apiRequest<Goal>(`/goals/${goalId}/activate/`, { method: "POST" }),
  deleteGoal: (goalId: number) => apiRequest<{ current_goal: Goal | null }>(`/goals/${goalId}/`, { method: "DELETE" }),
  getToday: () => apiRequest<StudyDay>("/study-days/today/"),
  getHistory: (year: number, month: number) => apiRequest<HistoryMonth>(`/goals/history/?year=${year}&month=${month}`),
  listScenarios: () => apiRequest<Scenario[]>("/scenarios/"),
  listStudyModules: () => apiRequest<StudyModule[]>("/study/modules/"),
  listPhrases: (scenario?: string) => apiRequest<Phrase[]>(scenario ? `/phrases/?scenario=${scenario}` : "/phrases/"),
  listFavorites: () => apiRequest<Favorite[]>("/favorites/"),
  favoritePhrase: (phraseId: number) => apiRequest<Favorite>("/favorites/", { method: "POST", body: JSON.stringify({ phrase_id: phraseId }) }),
  markProgress: (data: { phrase_id: number; correct: boolean; answer: string }) =>
    apiRequest<void>("/progress/mark/", { method: "POST", body: JSON.stringify(data) }),
  createGoal: (data: { source_language: string; target_language: string; current_level?: string; target_level: string; duration_days: number; study_weekdays: number[]; session_minutes: number }) =>
    apiRequest<Goal>("/goals/onboarding/", { method: "POST", body: JSON.stringify(data) }),
  updateGoal: (goalId: number, data: { study_weekdays?: number[]; session_minutes?: number }) =>
    apiRequest<Goal>(`/goals/${goalId}/`, { method: "PATCH", body: JSON.stringify(data) }),
  completeStudyDay: (studyDayId: number) => apiRequest<{ completed: boolean }>(`/study-days/${studyDayId}/complete/`, { method: "POST" }),
  removeFavorite: (favoriteId: number) => apiRequest<void>(`/favorites/${favoriteId}/`, { method: "DELETE" }),
};
