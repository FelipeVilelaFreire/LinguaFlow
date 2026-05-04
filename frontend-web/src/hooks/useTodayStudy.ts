import { useMemo, useState } from "react";

import { contentService } from "../services/contentService";
import type { Phrase } from "../types/content";
import { useAsyncData } from "./useAsyncData";

export function useTodayStudy(onCompleted?: () => void) {
  const today = useAsyncData(contentService.getToday);
  const [phraseIndex, setPhraseIndex] = useState(0);
  const [showTranslation, setShowTranslation] = useState(false);
  const [answer, setAnswer] = useState("");
  const [checked, setChecked] = useState(false);
  const [completed, setCompleted] = useState(false);

  const phrases = today.data?.lesson.phrases ?? [];
  const currentPhrase = phrases[phraseIndex] ?? null;
  const progress = phrases.length === 0 ? 0 : Math.round(((phraseIndex + (completed ? 1 : 0)) / phrases.length) * 100);
  const isCorrect = useMemo(() => isCloseAnswer(answer, currentPhrase), [answer, currentPhrase]);

  function revealTranslation() {
    setShowTranslation((current) => !current);
  }

  function checkAnswer() {
    setChecked(true);
  }

  async function favoriteCurrentPhrase() {
    if (!currentPhrase) return;
    await contentService.favoritePhrase(currentPhrase.id);
  }

  async function nextPhrase() {
    if (phraseIndex >= phrases.length - 1) {
      setCompleted(true);
      if (today.data) {
        await contentService.completeStudyDay(today.data.id).catch(() => null);
        onCompleted?.();
      }
      return;
    }
    setPhraseIndex((current) => current + 1);
    setShowTranslation(false);
    setAnswer("");
    setChecked(false);
  }

  return {
    today,
    phrases,
    currentPhrase,
    phraseIndex,
    showTranslation,
    answer,
    checked,
    completed,
    progress,
    isCorrect,
    setAnswer,
    revealTranslation,
    checkAnswer,
    nextPhrase,
    favoriteCurrentPhrase,
  };
}

function normalize(value: string): string {
  return value.trim().toLowerCase().replace(/[.,!?]/g, "");
}

function isCloseAnswer(answer: string, phrase: Phrase | null): boolean {
  if (!phrase || answer.trim().length < 3) return false;
  const normalizedAnswer = normalize(answer);
  const normalizedTarget = normalize(phrase.target_text);
  return normalizedTarget.includes(normalizedAnswer) || normalizedAnswer.includes(normalizedTarget.slice(0, Math.min(8, normalizedTarget.length)));
}
