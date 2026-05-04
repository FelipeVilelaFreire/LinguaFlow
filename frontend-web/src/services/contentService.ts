import { apiRequest } from "./api";
import { addMockFavorite, getMockFavorites, mockPhrases, mockScenarios, removeMockFavorite } from "../data/mockContent";
import type { Favorite, Goal, Phrase, Scenario, StudyDay } from "../types/content";

export const contentService = {
  getCurrentGoal: () => apiRequest<Goal>("/goals/current/"),
  listGoals: () => apiRequest<Goal[]>("/goals/"),
  activateGoal: (goalId: number) => apiRequest<Goal>(`/goals/${goalId}/activate/`, { method: "POST" }),
  deleteGoal: (goalId: number) => apiRequest<{ current_goal: Goal | null }>(`/goals/${goalId}/`, { method: "DELETE" }),
  getToday: () => apiRequest<StudyDay>("/study-days/today/"),
  listScenarios: () => withFallback<Scenario[]>(() => apiRequest<Scenario[]>("/scenarios/"), mockScenarios),
  listPhrases: (scenario?: string) =>
    withFallback<Phrase[]>(
      () => apiRequest<Phrase[]>(scenario ? `/phrases/?scenario=${scenario}` : "/phrases/"),
      scenario ? mockPhrases.filter((phrase) => phrase.scenario === mockScenarios.find((item) => item.slug === scenario)?.id) : mockPhrases,
    ),
  listFavorites: () => withFallback<Favorite[]>(() => apiRequest<Favorite[]>("/favorites/"), getMockFavorites()),
  favoritePhrase: (phraseId: number) => withFallback<Favorite>(() => apiRequest<Favorite>("/favorites/", { method: "POST", body: JSON.stringify({ phrase_id: phraseId }) }), addMockFavorite(phraseId)),
  createGoal: (data: { source_language: string; target_language: string; target_level: string; duration_days: number }) =>
    apiRequest<Goal>("/goals/onboarding/", { method: "POST", body: JSON.stringify(data) }),
  completeStudyDay: (studyDayId: number) => apiRequest<{ completed: boolean }>(`/study-days/${studyDayId}/complete/`, { method: "POST" }),
  removeFavorite: async (favoriteId: number) => {
    try {
      await apiRequest<void>(`/favorites/${favoriteId}/`, { method: "DELETE" });
    } catch {
      removeMockFavorite(favoriteId);
    }
  },
};

async function withFallback<T>(request: () => Promise<T>, fallback: T): Promise<T> {
  try {
    return await request();
  } catch {
    return fallback;
  }
}
