import { useCallback, useMemo, useState } from "react";
import { adventureService } from "../../services/adventureService";
import type { StudySessionExercise } from "../../types/content";

function normalizeAnswer(value: string) {
  return value.trim().toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

export function useStudySessionRunner({
  exercises,
  langCode = "ES",
  onComplete,
}: {
  exercises: StudySessionExercise[];
  langCode?: string;
  onComplete?: () => void;
}) {
  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState<Array<{ id: string; correct: boolean }>>([]);
  const current = exercises[index] ?? null;

  const correctCount = useMemo(() => answers.filter((answer) => answer.correct).length, [answers]);
  const done = index >= exercises.length;

  const submit = useCallback((value: string) => {
    if (!current) return;
    const expected = current.kind === "multiple_choice" ? current.correct : current.answer;
    const correct = normalizeAnswer(value) === normalizeAnswer(expected ?? "");
    setAnswers((items) => [...items, { id: current.word_id, correct }]);
    adventureService.recordWordAnswer({
      word_id: current.word_id,
      correct,
      target: current.target,
      native: current.native,
      lang_code: langCode.toLowerCase(),
    }).catch(() => {});
    setIndex((item) => item + 1);
  }, [current, langCode]);

  const finish = useCallback(() => {
    onComplete?.();
  }, [onComplete]);

  return {
    current,
    index,
    total: exercises.length,
    done,
    correctCount,
    mistakes: answers.length - correctCount,
    submit,
    finish,
  };
}
