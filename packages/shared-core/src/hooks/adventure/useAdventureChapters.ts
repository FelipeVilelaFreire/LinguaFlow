import { useCallback, useEffect, useState } from "react";
import { storage } from "../../lib/storage";
import { adventureService } from "../../services/adventureService";
import type { AdventureChapter, ApiAdventureChapter } from "../../types/adventure";

const SECTION_COUNT = 6;

function sectionKey(langCode: string) {
  return `talkly_${langCode.toLowerCase()}_sections`;
}

async function loadSectionMap(langCode: string): Promise<Record<string, number>> {
  try {
    return JSON.parse(await storage().getItem(sectionKey(langCode)) ?? "{}") as Record<string, number>;
  } catch {
    return {};
  }
}

async function writeSectionMap(langCode: string, map: Record<string, number>) {
  await storage().setItem(sectionKey(langCode), JSON.stringify(map));
}

async function clearSectionMap(langCode: string) {
  await storage().removeItem(sectionKey(langCode));
}

async function hydrate(apiChapters: ApiAdventureChapter[], langCode: string): Promise<AdventureChapter[]> {
  const sectionMap = await loadSectionMap(langCode);
  return apiChapters.map((chapter) => ({
    ...chapter,
    phases: chapter.phases.map((phase) => {
      const completedSections = phase.is_completed
        ? SECTION_COUNT
        : Math.max(sectionMap[String(phase.id)] ?? 0, phase.completed_sections ?? 0);

      return {
        ...phase,
        section_count: SECTION_COUNT,
        completed_sections: completedSections,
        phase_type: phase.phase_type,
        npc_name: phase.npc_name ?? "",
        vocab_gate: undefined,
      };
    }),
  }));
}

export interface UseAdventureChaptersResult {
  chapters: AdventureChapter[];
  isLoading: boolean;
  error: string | null;
  completeSection: (phaseId: number, newCount: number) => Promise<void>;
  refresh: () => Promise<void>;
  resetProgress: () => Promise<void>;
  jumpToPhase: (chapterSlug: string, phaseNumber: number, sectionNumber: number) => Promise<void>;
}

export function useAdventureChapters(langCode: string): UseAdventureChaptersResult {
  const [chapters, setChapters] = useState<AdventureChapter[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchChapters = useCallback(async () => {
    setError(null);
    try {
      const data = await adventureService.listChapters();
      setChapters(await hydrate(data, langCode));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Erro ao carregar aventura.");
    }
  }, [langCode]);

  useEffect(() => {
    setIsLoading(true);
    fetchChapters().finally(() => setIsLoading(false));
  }, [fetchChapters]);

  const refresh = useCallback(() => fetchChapters(), [fetchChapters]);

  const completeSection = useCallback(async (phaseId: number, newCount: number) => {
    const map = await loadSectionMap(langCode);
    map[String(phaseId)] = newCount;
    await writeSectionMap(langCode, map);

    adventureService.updateSectionProgress(phaseId, newCount).catch(() => {});

    const isPhaseComplete = newCount >= SECTION_COUNT;
    setChapters((prev) => prev.map((chapter) => ({
      ...chapter,
      phases: chapter.phases.map((phase) => phase.id !== phaseId ? phase : {
        ...phase,
        completed_sections: newCount,
        is_completed: isPhaseComplete,
      }),
    })));

    if (isPhaseComplete) {
      try {
        await adventureService.completePhase(phaseId, 100);
        await fetchChapters();
      } catch {
        // Optimistic state remains usable; backend will be reconciled on refresh.
      }
    }
  }, [langCode, fetchChapters]);

  const resetProgress = useCallback(async () => {
    await clearSectionMap(langCode);
    await fetchChapters();
  }, [langCode, fetchChapters]);

  const jumpToPhase = useCallback(async (chapterSlug: string, phaseNumber: number, sectionNumber: number) => {
    await adventureService.devJumpToPhase(chapterSlug, phaseNumber, sectionNumber);

    const data = await adventureService.listChapters();
    const targetChapter = data.find((chapter) => chapter.slug === chapterSlug);
    const targetPhase = targetChapter?.phases.find((phase) => phase.number === phaseNumber);

    const newMap: Record<string, number> = {};
    if (targetPhase && sectionNumber > 1) {
      newMap[String(targetPhase.id)] = sectionNumber - 1;
    }
    await writeSectionMap(langCode, newMap);
    setChapters(await hydrate(data, langCode));
  }, [langCode]);

  return { chapters, isLoading, error, completeSection, refresh, resetProgress, jumpToPhase };
}
