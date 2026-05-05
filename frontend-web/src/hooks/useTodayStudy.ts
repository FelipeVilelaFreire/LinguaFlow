import { useMemo, useState } from "react";

import { contentService } from "../services/contentService";
import type { Phrase, PracticeItem } from "../types/content";
import { useAsyncData } from "./useAsyncData";

export function useTodayStudy(onCompleted?: () => void) {
  const today = useAsyncData(contentService.getToday);
  const [phraseIndex, setPhraseIndex] = useState(0);
  const [showTranslation, setShowTranslation] = useState(false);
  const [answer, setAnswer] = useState("");
  const [checked, setChecked] = useState(false);
  const [completed, setCompleted] = useState(false);

  const practiceItems = today.data?.practice_items?.length ? today.data.practice_items : phraseItems(today.data?.lesson.phrases ?? []);
  const currentItem = practiceItems[phraseIndex] ?? null;
  const currentPhrase = currentItem?.phrase ?? null;
  const progress = practiceItems.length === 0 ? 0 : Math.round(((phraseIndex + (completed ? 1 : 0)) / practiceItems.length) * 100);
  const feedback = useMemo(() => getAnswerFeedback(answer, currentItem), [answer, currentItem]);
  const isCorrect = feedback.quality === "correct";
  const stage = useMemo(() => getSessionStage(practiceItems, phraseIndex), [practiceItems, phraseIndex]);

  function revealTranslation() {
    setShowTranslation((current) => !current);
  }

  async function checkAnswer() {
    if (currentItem?.type === "intro") {
      setChecked(true);
      return;
    }
    setChecked(true);
    if (currentItem?.phrase) {
      await contentService.markProgress({
        phrase_id: currentItem.phrase.id,
        correct: feedback.quality !== "wrong",
        answer,
      }).catch(() => null);
    }
  }

  async function favoriteCurrentPhrase() {
    if (!currentPhrase) return;
    await contentService.favoritePhrase(currentPhrase.id).catch(() => null);
  }

  async function nextPhrase() {
    if (phraseIndex >= practiceItems.length - 1) {
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
    phrases: practiceItems,
    practiceItems,
    currentItem,
    currentPhrase,
    phraseIndex,
    showTranslation,
    answer,
    checked,
    completed,
    progress,
    isCorrect,
    feedback,
    stage,
    setAnswer,
    revealTranslation,
    checkAnswer,
    nextPhrase,
    favoriteCurrentPhrase,
  };
}

function phraseItems(phrases: Phrase[]): PracticeItem[] {
  return phrases.map((phrase, index) => ({
    id: `new-${phrase.id}-${index}`,
    type: "new",
    prompt: phrase.target_text,
    answer: phrase.source_text,
    helper: "Understand the target phrase.",
    options: [],
    word_bank: [],
    preview_phrases: [],
    phrase,
  }));
}

function normalize(value: string): string {
  return value.trim().toLowerCase().replace(/[.,!?¿¡]/g, "").replace(/\s+/g, " ");
}

function getAnswerFeedback(answer: string, item: PracticeItem | null): { quality: "correct" | "close" | "wrong"; missingWords: string[]; expected: string } {
  if (!item || answer.trim().length < 3) return { quality: "wrong", missingWords: [], expected: item?.answer ?? "" };
  if (item.type === "intro") return { quality: "correct", missingWords: [], expected: "" };
  const normalizedAnswer = normalize(answer);
  const normalizedTarget = normalize(item.answer);
  if (normalizedAnswer === normalizedTarget || normalizedTarget.includes(normalizedAnswer) || normalizedAnswer.includes(normalizedTarget)) {
    return { quality: "correct", missingWords: [], expected: item.answer };
  }
  const answerWords = new Set(normalizedAnswer.split(" ").filter(Boolean));
  const targetWords = normalizedTarget.split(" ").filter(Boolean);
  const missingWords = targetWords.filter((word) => !answerWords.has(word));
  const matched = targetWords.length - missingWords.length;
  const ratio = targetWords.length ? matched / targetWords.length : 0;
  return { quality: ratio >= 0.55 ? "close" : "wrong", missingWords: missingWords.slice(0, 5), expected: item.answer };
}

function getSessionStage(items: PracticeItem[], index: number) {
  const current = items[index];
  if (!current) return { title: "Aquecimento", detail: "Prepare sua memoria para a sessao." };
  if (current.type === "intro") return { title: "Aquecimento", detail: "Entenda o contexto antes de praticar." };
  if (current.type === "review") return { title: "Revisao espacada", detail: "Recupere frases antigas antes que elas esfriem." };
  const progress = items.length ? index / items.length : 0;
  if (progress < 0.2) return { title: "Aquecimento", detail: "Reconheca as primeiras frases do contexto." };
  if (current.type === "multiple_choice") return { title: "Escolha rapida", detail: "Ganhe velocidade reconhecendo a resposta certa." };
  if (current.type === "fill_blank") return { title: "Completar lacuna", detail: "Foque na palavra-chave da frase." };
  if (current.type === "word_order") return { title: "Montar frase", detail: "Construa a ordem correta das palavras." };
  if (current.type === "new") return { title: "Frases novas", detail: "Entenda o sentido antes de revelar a resposta." };
  if (current.type === "reverse") return { title: "Pratica ativa", detail: "Construa a frase no idioma alvo." };
  if (current.type === "dictation") return { title: "Mini teste", detail: "Reconstrua a frase de memoria." };
  return { title: "Pratica guiada", detail: "Continue ate fechar a sessao." };
}
