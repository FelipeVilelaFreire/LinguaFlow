import { useCallback, useEffect, useState } from "react";
import { adventureService } from "../../services/adventureService";
import type { EarnedItemData } from "../../types/adventure";
import type { PhaseSection } from "../../types/sections";

export type PhaseCompletionStage = null | "trophy" | "words" | "item";

export function useAdventurePhaseRunner({
  phaseId,
  phaseNumber,
  keyWords = [],
  startSectionIndex = 0,
  onExit,
}: {
  phaseId: number;
  phaseNumber: number;
  keyWords?: string[];
  startSectionIndex?: number;
  onExit: () => void;
}) {
  const [sections, setSections] = useState<PhaseSection[]>([]);
  const [sectionIndex, setSectionIndex] = useState(startSectionIndex);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [totalMistakes, setTotalMistakes] = useState(0);
  const [stage, setStage] = useState<PhaseCompletionStage>(null);
  const [earnedItem, setEarnedItem] = useState<EarnedItemData | null>(null);
  const [serverWords, setServerWords] = useState<string[]>([]);

  useEffect(() => {
    setLoading(true);
    setError(null);
    setStage(null);
    setSectionIndex(startSectionIndex);
    setTotalMistakes(0);
    setEarnedItem(null);
    setServerWords([]);

    adventureService.getSections(phaseId)
      .then(setSections)
      .catch(() => setError("Nao foi possivel carregar a fase."))
      .finally(() => setLoading(false));
  }, [phaseId, startSectionIndex]);

  const completeSection = useCallback(async (mistakes: number) => {
    setTotalMistakes((current) => current + mistakes);
    const nextCount = sectionIndex + 1;
    adventureService.updateSectionProgress(phaseId, nextCount).catch(() => {});

    if (sectionIndex < sections.length - 1) {
      setSectionIndex((current) => current + 1);
      return;
    }

    try {
      const result = await adventureService.completePhase(phaseId, Math.max(0, 100 - mistakes * 5));
      setServerWords(result.key_words ?? []);
      let nextItem = result.earned_item ?? null;
      try {
        const chest = await adventureService.openPhaseChest(phaseId);
        if (chest.earned_item) {
          nextItem = {
            slug: chest.earned_item.slug,
            emoji: chest.earned_item.emoji,
            name: chest.earned_item.name,
            lore: chest.earned_item.lore,
            rarity: chest.earned_item.rarity,
            action: chest.earned_item.action,
          };
        }
      } catch {
        // Some phases do not have a chest.
      }
      setEarnedItem(nextItem);
    } catch {
      // Keep the local completion flow available even if the reward call fails.
    }
    setStage("trophy");
  }, [phaseId, sectionIndex, sections.length]);

  const wordsToShow = serverWords.length > 0 ? serverWords : keyWords;

  const nextStage = useCallback(() => {
    if (stage === "trophy") {
      if (wordsToShow.length > 0) setStage("words");
      else if (earnedItem) setStage("item");
      else onExit();
      return;
    }
    if (stage === "words") {
      if (earnedItem) setStage("item");
      else onExit();
      return;
    }
    if (stage === "item") onExit();
  }, [earnedItem, onExit, stage, wordsToShow.length]);

  return {
    phaseNumber,
    sections,
    sectionIndex,
    currentSection: sections[sectionIndex] ?? null,
    loading,
    error,
    totalMistakes,
    stage,
    earnedItem,
    wordsToShow,
    completeSection,
    nextStage,
  };
}
