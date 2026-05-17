import { api } from "../lib/apiClient";
import type { Phrase, StudySessionData } from "../types/content";
import type { PhaseSection } from "../types/sections";
import type {
  ApiAdventureChapter,
  ApiAdventureCharacter,
  ApiAdventureItem,
  ApiUserChest,
  ApiUserInventoryItem,
  ApiUserSkillMastery,
  AvailableLanguage,
  EarnedItemData,
  HeroStats,
  StreakData,
} from "../types/adventure";

export const adventureService = {
  listAvailableLanguages: () =>
    api().request<AvailableLanguage[]>("/adventure/chapters/languages/"),

  getChapter: (slug: string) =>
    api().request<ApiAdventureChapter>(`/adventure/chapters/${slug}/`),

  listChapters: () =>
    api().request<ApiAdventureChapter[]>("/adventure/chapters/"),

  listCharacters: (chapterSlug?: string) =>
    api().request<ApiAdventureCharacter[]>(
      `/adventure/characters/${chapterSlug ? `?chapter=${chapterSlug}` : ""}`,
    ),

  listItems: (chapterSlug?: string) =>
    api().request<ApiAdventureItem[]>(
      `/adventure/items/${chapterSlug ? `?chapter=${chapterSlug}` : ""}`,
    ),

  listSkillMastery: () =>
    api().request<ApiUserSkillMastery[]>("/adventure/skills/mastery/"),

  listChests: () =>
    api().request<ApiUserChest[]>("/adventure/chests/"),

  startChest: (chestId: number) =>
    api().request<ApiUserChest>(`/adventure/chests/${chestId}/start/`, { method: "POST" }),

  claimChest: (chestId: number) =>
    api().request<ApiUserChest>(`/adventure/chests/${chestId}/claim/`, { method: "POST" }),

  listInventory: () =>
    api().request<ApiUserInventoryItem[]>("/adventure/inventory/"),

  useInventoryItem: (itemId: number) =>
    api().request<ApiUserInventoryItem>(`/adventure/inventory/${itemId}/use/`, { method: "POST" }),

  getPhrasesForPhase: (phaseId: number) =>
    api().request<Phrase[]>(`/adventure/phases/${phaseId}/phrases/`),

  getSections: (phaseId: number) =>
    api().request<PhaseSection[]>(`/adventure/phases/${phaseId}/sections/`),

  getStudySession: () =>
    api().request<StudySessionData>("/adventure/vocabulary/study-session/"),

  listLearnedWords: (langCode?: string) =>
    api().request<{ word_id: string; target: string; native: string; tier: string }[]>(
      `/adventure/vocabulary/${langCode ? `?lang=${langCode}` : ""}`,
    ),

  recordWordAnswer: (payload: {
    word_id: string;
    correct: boolean;
    target?: string;
    native?: string;
    lang_code?: string;
  }) =>
    api().request<{
      word_id: string;
      target: string;
      native: string;
      tier: string;
      streak: number;
      promoted: boolean;
      created: boolean;
      earned_item: { slug: string; emoji: string; name: string; lore: string; rarity: string; action: string } | null;
    }>("/adventure/vocabulary/record/", {
      method: "POST",
      body: JSON.stringify(payload),
    }),

  meetCharacterByName: (name: string) =>
    api().request<{ character_id: number; slug: string; name: string; created: boolean }>(
      "/adventure/characters/meet-by-name/",
      { method: "POST", body: JSON.stringify({ name }) },
    ),

  devJumpToPhase: (chapterSlug: string, phaseNumber: number, sectionNumber: number) =>
    api().request<{
      chapter: string;
      current_phase: number;
      current_section: number;
      completed_phases: number;
      met_characters: number;
      words_unlocked: number;
      items_unlocked: number;
    }>("/adventure/dev/jump-to-phase/", {
      method: "POST",
      body: JSON.stringify({
        chapter_slug: chapterSlug,
        phase_number: phaseNumber,
        section_number: sectionNumber,
      }),
    }),

  devVoiceSample: (payload: { npc: string; lang?: string; text?: string; model_path?: string; length_scale?: number | null }) =>
    api().request<{ npc: string; text: string; audio_url: string }>(
      "/adventure/dev/voice-sample/",
      { method: "POST", body: JSON.stringify(payload) },
    ),

  devVoiceOptions: () =>
    api().request<{ models: Array<{ id: string; name: string; label?: string; path: string; length_scale?: number | null }> }>(
      "/adventure/dev/voice-options/",
    ),

  updateSectionProgress: (phaseId: number, completedSections: number) =>
    api().request<{ phase_id: number; completed_sections: number }>(
      `/adventure/phases/${phaseId}/section-progress/`,
      { method: "POST", body: JSON.stringify({ completed_sections: completedSections }) },
    ),

  getHeroStats: () =>
    api().request<HeroStats>("/adventure/chapters/hero-stats/"),

  completePhase: (phaseId: number, score: number) =>
    api().request<{
      score: number;
      phase_number: number;
      is_boss: boolean;
      reward_unlocked: boolean;
      current_phase: number;
      chapter_completed: boolean;
      earned_item: EarnedItemData | null;
      earned_items: EarnedItemData[];
      earned_chest: ApiUserChest | null;
      key_words: string[];
      streak: StreakData;
    }>(`/adventure/phases/${phaseId}/complete/`, {
      method: "POST",
      body: JSON.stringify({ score }),
    }),

  listInventoryByTag: (tag: string) =>
    api().request<{ tag: string; items: ApiUserInventoryItem[] }>(
      `/adventure/inventory/by-tag/?tag=${encodeURIComponent(tag)}`,
    ),

  listLockedItems: (chapterSlug?: string) =>
    api().request<{ locked: Array<ApiAdventureItem & { unlock_hint_word_id: string }> }>(
      `/adventure/inventory/locked/${chapterSlug ? `?chapter=${chapterSlug}` : ""}`,
    ),

  useByTag: (tag: string) =>
    api().request<{
      used_item: ApiAdventureItem;
      is_degraded: boolean;
      consumed: boolean;
    }>("/adventure/inventory/use-by-tag/", {
      method: "POST",
      body: JSON.stringify({ tag }),
    }),

  openPhaseChest: (phaseId: number) =>
    api().request<{
      from_chest: true;
      chest_tier: string;
      rolled_rarity: string | null;
      phase_score?: number;
      earned_item: ApiAdventureItem | null;
      stored_chest?: ApiUserChest;
    }>(`/adventure/phases/${phaseId}/open-chest/`, { method: "POST" }),
};
