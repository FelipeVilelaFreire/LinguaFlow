import { apiRequest } from "./api";
import type { AdventureChapter } from "../types/adventure";
import type { Phrase } from "../types/content";

export const adventureService = {
  getChapter: (slug: string) =>
    apiRequest<AdventureChapter>(`/adventure/chapters/${slug}/`),

  listChapters: () =>
    apiRequest<AdventureChapter[]>("/adventure/chapters/"),

  getPhrasesForPhase: (phaseId: number) =>
    apiRequest<Phrase[]>(`/adventure/phases/${phaseId}/phrases/`),

  completePhase: (phaseId: number, score: number) =>
    apiRequest<{
      score: number;
      phase_number: number;
      is_boss: boolean;
      reward_unlocked: boolean;
      current_phase: number;
      chapter_completed: boolean;
    }>(`/adventure/phases/${phaseId}/complete/`, {
      method: "POST",
      body: JSON.stringify({ score }),
    }),
};
