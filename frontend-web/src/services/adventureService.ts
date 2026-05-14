import { apiRequest } from "./api";
import type { ApiAdventureChapter, ApiAdventureCharacter, ApiAdventureItem, ApiUserInventoryItem, AvailableLanguage, EarnedItemData, HeroStats, StreakData } from "../types/adventure";
import type { Phrase, StudySessionData } from "../types/content";
import type { PhaseSection } from "../types/sections";

export const adventureService = {
  listAvailableLanguages: () =>
    apiRequest<AvailableLanguage[]>("/adventure/chapters/languages/"),

  getChapter: (slug: string) =>
    apiRequest<ApiAdventureChapter>(`/adventure/chapters/${slug}/`),

  listChapters: () =>
    apiRequest<ApiAdventureChapter[]>("/adventure/chapters/"),

  listCharacters: (chapterSlug?: string) =>
    apiRequest<ApiAdventureCharacter[]>(
      `/adventure/characters/${chapterSlug ? `?chapter=${chapterSlug}` : ""}`,
    ),

  listItems: (chapterSlug?: string) =>
    apiRequest<ApiAdventureItem[]>(
      `/adventure/items/${chapterSlug ? `?chapter=${chapterSlug}` : ""}`,
    ),

  listInventory: () =>
    apiRequest<ApiUserInventoryItem[]>("/adventure/inventory/"),

  useInventoryItem: (itemId: number) =>
    apiRequest<ApiUserInventoryItem>(`/adventure/inventory/${itemId}/use/`, { method: "POST" }),

  getPhrasesForPhase: (phaseId: number) =>
    apiRequest<Phrase[]>(`/adventure/phases/${phaseId}/phrases/`),

  getSections: (phaseId: number) =>
    apiRequest<PhaseSection[]>(`/adventure/phases/${phaseId}/sections/`),

  getStudySession: () =>
    apiRequest<StudySessionData>("/adventure/vocabulary/study-session/"),

  listLearnedWords: (langCode?: string) =>
    apiRequest<{ word_id: string; target: string; native: string; tier: string }[]>(
      `/adventure/vocabulary/${langCode ? `?lang=${langCode}` : ""}`,
    ),

  recordWordAnswer: (payload: {
    word_id:    string;
    correct:    boolean;
    target?:    string;
    native?:    string;
    lang_code?: string;
  }) =>
    apiRequest<{
      word_id:    string;
      target:     string;
      native:     string;
      tier:       string;
      streak:     number;
      promoted:   boolean;
      created:    boolean;
      earned_item: { slug: string; emoji: string; name: string; lore: string; rarity: string; action: string } | null;
    }>(
      "/adventure/vocabulary/record/",
      { method: "POST", body: JSON.stringify(payload) },
    ),

  meetCharacterByName: (name: string) =>
    apiRequest<{ character_id: number; slug: string; name: string; created: boolean }>(
      "/adventure/characters/meet-by-name/",
      { method: "POST", body: JSON.stringify({ name }) },
    ),

  devJumpToPhase: (chapterSlug: string, phaseNumber: number, sectionNumber: number) =>
    apiRequest<{
      chapter:          string;
      current_phase:    number;
      current_section:  number;
      completed_phases: number;
      met_characters:   number;
      words_unlocked:   number;
      items_unlocked:   number;
    }>("/adventure/dev/jump-to-phase/", {
      method: "POST",
      body: JSON.stringify({
        chapter_slug:   chapterSlug,
        phase_number:   phaseNumber,
        section_number: sectionNumber,
      }),
    }),

  updateSectionProgress: (phaseId: number, completedSections: number) =>
    apiRequest<{ phase_id: number; completed_sections: number }>(
      `/adventure/phases/${phaseId}/section-progress/`,
      { method: "POST", body: JSON.stringify({ completed_sections: completedSections }) },
    ),

  getHeroStats: () =>
    apiRequest<HeroStats>("/adventure/chapters/hero-stats/"),

  completePhase: (phaseId: number, score: number) =>
    apiRequest<{
      score: number;
      phase_number: number;
      is_boss: boolean;
      reward_unlocked: boolean;
      current_phase: number;
      chapter_completed: boolean;
      earned_item:  EarnedItemData | null;
      earned_items: EarnedItemData[];
      key_words:    string[];
      streak:       StreakData;
    }>(`/adventure/phases/${phaseId}/complete/`, {
      method: "POST",
      body: JSON.stringify({ score }),
    }),

  // ── Item dynamics (item_moment + chest) ────────────────────────────────────

  listInventoryByTag: (tag: string) =>
    apiRequest<{ tag: string; items: ApiUserInventoryItem[] }>(
      `/adventure/inventory/by-tag/?tag=${encodeURIComponent(tag)}`,
    ),

  listLockedItems: (chapterSlug?: string) =>
    apiRequest<{ locked: Array<ApiAdventureItem & { unlock_hint_word_id: string }> }>(
      `/adventure/inventory/locked/${chapterSlug ? `?chapter=${chapterSlug}` : ""}`,
    ),

  useByTag: (tag: string) =>
    apiRequest<{
      used_item:   ApiAdventureItem;
      is_degraded: boolean;
      consumed:    boolean;
    }>("/adventure/inventory/use-by-tag/", {
      method: "POST",
      body:   JSON.stringify({ tag }),
    }),

  openPhaseChest: (phaseId: number) =>
    apiRequest<{
      from_chest:    true;
      chest_tier:    string;
      rolled_rarity: string | null;
      phase_score?:  number;
      earned_item:   ApiAdventureItem | null;
    }>(`/adventure/phases/${phaseId}/open-chest/`, { method: "POST" }),
};
