import { useCallback, useEffect, useState } from "react";

import { adventureService } from "../services/adventureService";
import type { AdventureChapter, ApiAdventureChapter } from "../types/adventure";

// ─── Local section-progress persistence ───────────────────────────────────────
// The backend tracks phase-level completion (is_completed).
// Section-level progress (0–6) within an in-progress phase is kept locally
// and merged with the API response on every fetch.

const SECTION_COUNT = 6;

function sectionKey(langCode: string) {
  return `talkly_${langCode.toLowerCase()}_sections`;
}

function loadSectionMap(langCode: string): Record<string, number> {
  try {
    return JSON.parse(localStorage.getItem(sectionKey(langCode)) ?? "{}");
  } catch {
    return {};
  }
}

function writeSectionMap(langCode: string, map: Record<string, number>) {
  localStorage.setItem(sectionKey(langCode), JSON.stringify(map));
}

function clearSectionMap(langCode: string) {
  localStorage.removeItem(sectionKey(langCode));
}

// ─── Hydration — merges API chapters with local section progress ──────────────

function hydrate(apiChapters: ApiAdventureChapter[], langCode: string): AdventureChapter[] {
  const sectionMap = loadSectionMap(langCode);
  return apiChapters.map(ch => ({
    ...ch,
    phases: ch.phases.map(p => {
      const completedSections = p.is_completed
        ? SECTION_COUNT
        : Math.max(sectionMap[String(p.id)] ?? 0, p.completed_sections ?? 0);
      return {
        ...p,
        section_count:      SECTION_COUNT,
        completed_sections: completedSections,
        phase_type:         p.phase_type,
        npc_name:           "",
        vocab_gate:         undefined,
      };
    }),
  }));
}

// ─── Hook ─────────────────────────────────────────────────────────────────────

export interface UseAdventureChaptersResult {
  chapters:        AdventureChapter[];
  isLoading:       boolean;
  error:           string | null;
  /** Call when a section inside a phase finishes. Syncs backend when phase fully done. */
  completeSection: (phaseId: number, newCount: number) => Promise<void>;
  /** Re-fetch from API (used on popstate / focus return). */
  refresh:         () => Promise<void>;
  /** Clear local section progress + re-fetch (DEV reset). */
  resetProgress:   () => Promise<void>;
  /** Jump to "phase X, section Y": wipes chapter progress and pre-unlocks everything that came before. */
  jumpToPhase:     (chapterSlug: string, phaseNumber: number, sectionNumber: number) => Promise<void>;
}

export function useAdventureChapters(langCode: string): UseAdventureChaptersResult {
  const [chapters, setChapters] = useState<AdventureChapter[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError]         = useState<string | null>(null);

  // ── Core fetch ──────────────────────────────────────────────────────────────
  const fetchChapters = useCallback(async () => {
    setError(null);
    try {
      const data = await adventureService.listChapters();
      setChapters(hydrate(data, langCode));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Erro ao carregar aventura.");
    }
  }, [langCode]);

  useEffect(() => {
    setIsLoading(true);
    fetchChapters().finally(() => setIsLoading(false));
  }, [fetchChapters]);

  // ── Public refresh (popstate) ───────────────────────────────────────────────
  const refresh = useCallback(() => fetchChapters(), [fetchChapters]);

  // ── Section completion ──────────────────────────────────────────────────────
  const completeSection = useCallback(async (phaseId: number, newCount: number) => {
    // 1. Persist locally
    const map = loadSectionMap(langCode);
    map[String(phaseId)] = newCount;
    writeSectionMap(langCode, map);

    // Sync to backend non-blocking (best-effort; local state is authoritative)
    adventureService.updateSectionProgress(phaseId, newCount).catch(() => {});

    const isPhaseComplete = newCount >= SECTION_COUNT;

    // 2. Optimistic UI update
    setChapters(prev => prev.map(ch => ({
      ...ch,
      phases: ch.phases.map(p => p.id !== phaseId ? p : {
        ...p,
        completed_sections: newCount,
        is_completed:       isPhaseComplete,
      }),
    })));

    // 3. Notify backend when phase fully done, then confirm from API
    if (isPhaseComplete) {
      try {
        await adventureService.completePhase(phaseId, 100);
        await fetchChapters();
      } catch {
        // Non-blocking — optimistic update already applied
      }
    }
  }, [langCode, fetchChapters]);

  // ── DEV reset ───────────────────────────────────────────────────────────────
  const resetProgress = useCallback(async () => {
    clearSectionMap(langCode);
    await fetchChapters();
  }, [langCode, fetchChapters]);

  // ── DEV jump to phase (backend wipes chapter + pre-unlocks everything before) ──
  // After the server wipes/repopulates, we also mirror "Y-1 sections done on the
  // target phase" into the local section map so the map ring is correct without
  // waiting for the next completion.
  const jumpToPhase = useCallback(async (chapterSlug: string, phaseNumber: number, sectionNumber: number) => {
    await adventureService.devJumpToPhase(chapterSlug, phaseNumber, sectionNumber);

    const data         = await adventureService.listChapters();
    const targetChapter = data.find(c => c.slug === chapterSlug);
    const targetPhase   = targetChapter?.phases.find(p => p.number === phaseNumber);

    const newMap: Record<string, number> = {};
    if (targetPhase && sectionNumber > 1) {
      newMap[String(targetPhase.id)] = sectionNumber - 1;
    }
    writeSectionMap(langCode, newMap);

    setChapters(hydrate(data, langCode));
  }, [langCode]);

  return { chapters, isLoading, error, completeSection, refresh, resetProgress, jumpToPhase };
}
