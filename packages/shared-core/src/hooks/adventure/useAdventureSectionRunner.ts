import { useCallback, useEffect, useMemo, useState } from "react";
import { adventureService } from "../../services/adventureService";
import type { PhaseSection, SectionStep } from "../../types/sections";

export type AdventureChatEntry =
  | { id: string; kind: "scene"; text: string }
  | { id: string; kind: "narrative"; text: string }
  | { id: string; kind: "npc"; npc: string; line: string; translation?: string; isNew?: boolean; audio_url?: string }
  | { id: string; kind: "player"; text: string; label: string }
  | { id: string; kind: "answer"; text: string; label: string; correct: boolean; correctText?: string }
  | { id: string; kind: "pattern"; parts: Array<{ text: string; isKey: boolean }>; example: string; translation: string; note: string }
  | { id: string; kind: "reveal"; phrase: string; meaning: string; note?: string }
  | { id: string; kind: "vocab_list"; items: Array<{ target: string; native: string }> };

export type AdventureRunnerPhase = "tap" | "choosing" | "input" | "readyComplete" | "summary";

export interface ActiveChoice {
  question: string;
  options: Array<{ id: string; text: string }>;
}

export interface ActiveInput {
  prompt: string;
  answer: string;
  kind: "fill_blank" | "translate" | "write_word";
  hint?: string;
}

export interface SectionSummary {
  correct: number;
  mistakes: number;
  xp: number;
  words: Array<{ target: string; native: string }>;
}

function normalizeSection(section: PhaseSection): SectionStep[] {
  if (section.type !== "narrativa") return section.steps;
  const fromBeats: SectionStep[] = section.beats.map((beat) => {
    if (beat.kind === "npc") return { ...beat, kind: "npc_speak" as const };
    if (beat.kind === "player") return { ...beat, kind: "player_react" as const };
    return beat;
  });
  return [...fromBeats, ...(section.exercises ?? [])];
}

function normalizeAnswer(value: string) {
  return value.trim().toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

export function useAdventureSectionRunner({
  section,
  sectionNumber,
  langCode,
  sourceLangCode,
  firstName,
  onComplete,
}: {
  section: PhaseSection;
  sectionNumber: number;
  langCode: string;
  sourceLangCode: string;
  firstName?: string;
  onComplete: (mistakes: number) => void;
}) {
  const steps = useMemo(() => normalizeSection(section), [section]);
  const sectionWords = useMemo(() => {
    const vocab = steps.find((step): step is Extract<SectionStep, { kind: "vocab_list" }> => step.kind === "vocab_list");
    return vocab?.items ?? [];
  }, [steps]);

  const playerLabel = (firstName?.trim()?.charAt(0) || sourceLangCode.charAt(0) || "?").toUpperCase();
  const [entries, setEntries] = useState<AdventureChatEntry[]>([]);
  const [cursor, setCursor] = useState(0);
  const [phase, setPhase] = useState<AdventureRunnerPhase>("tap");
  const [activeChoice, setActiveChoice] = useState<ActiveChoice | null>(null);
  const [activeInput, setActiveInput] = useState<ActiveInput | null>(null);
  const [summary, setSummary] = useState<SectionSummary | null>(null);
  const [correct, setCorrect] = useState(0);
  const [mistakes, setMistakes] = useState(0);

  const addEntry = useCallback((entry: AdventureChatEntry) => {
    setEntries((current) => current.some((item) => item.id === entry.id) ? current : [...current, entry]);
  }, []);

  useEffect(() => {
    setEntries([]);
    setCursor(0);
    setPhase("tap");
    setActiveChoice(null);
    setActiveInput(null);
    setSummary(null);
    setCorrect(0);
    setMistakes(0);
  }, [section]);

  useEffect(() => {
    const step = steps[cursor];
    if (!step) {
      setPhase("readyComplete");
      return;
    }

    const id = `${sectionNumber}-${cursor}`;
    setActiveChoice(null);
    setActiveInput(null);

    if (step.kind === "scene") {
      addEntry({ id, kind: "scene", text: step.text });
      setPhase("tap");
      return;
    }
    if (step.kind === "narrative") {
      addEntry({ id, kind: "narrative", text: step.text });
      setPhase("tap");
      return;
    }
    if (step.kind === "npc_speak") {
      addEntry({ id, kind: "npc", npc: step.npc, line: step.line, translation: step.translation, isNew: step.is_new_npc, audio_url: step.audio_url });
      adventureService.meetCharacterByName(step.npc).catch(() => {});
      setPhase("tap");
      return;
    }
    if (step.kind === "player_react") {
      addEntry({ id, kind: "player", text: step.text, label: playerLabel });
      setPhase("tap");
      return;
    }
    if (step.kind === "pattern") {
      addEntry({ id, kind: "pattern", parts: step.parts, example: step.example, translation: step.translation, note: step.note });
      setPhase("tap");
      return;
    }
    if (step.kind === "reveal") {
      addEntry({ id, kind: "reveal", phrase: step.phrase, meaning: step.meaning, note: step.note });
      setPhase("tap");
      return;
    }
    if (step.kind === "vocab_list") {
      addEntry({ id, kind: "vocab_list", items: step.items });
      setPhase("tap");
      return;
    }
    if (step.kind === "skill_check") {
      addEntry({ id, kind: "narrative", text: step.fallback });
      setPhase("tap");
      return;
    }
    if (step.kind === "item_moment") {
      addEntry({ id: `${id}-situation`, kind: "narrative", text: step.situation });
      addEntry({ id: `${id}-npc`, kind: "npc", npc: step.npc, line: step.npc_line, audio_url: step.npc_line_audio_url });
      setActiveChoice({
        question: `Usar item: ${step.item_tag}?`,
        options: [
          { id: "use", text: "Usar item" },
          { id: "skip", text: "Continuar sem item" },
        ],
      });
      setPhase("choosing");
      return;
    }
    if (step.kind === "multiple_choice") {
      setActiveChoice({ question: step.question, options: step.options });
      setPhase("choosing");
      return;
    }
    if (step.kind === "fill_blank") {
      setActiveInput({ kind: "fill_blank", prompt: step.prompt, answer: step.answer });
      setPhase("input");
      return;
    }
    if (step.kind === "translate") {
      setActiveInput({ kind: "translate", prompt: step.source, answer: step.answer });
      setPhase("input");
      return;
    }
    if (step.kind === "write_word") {
      setActiveInput({ kind: "write_word", prompt: step.prompt, answer: step.answer, hint: step.hint });
      setPhase("input");
    }
  }, [addEntry, cursor, firstName, langCode, playerLabel, sectionNumber, sourceLangCode, steps]);

  const continueStep = useCallback(() => {
    if (phase === "readyComplete") {
      const nextSummary = {
        correct,
        mistakes,
        xp: 10 + correct * 2 + (mistakes === 0 && correct > 0 ? 10 : 0),
        words: sectionWords,
      };
      setSummary(nextSummary);
      setPhase("summary");
      return;
    }
    if (phase !== "tap") return;
    setCursor((current) => current + 1);
  }, [correct, mistakes, phase, sectionWords]);

  const choose = useCallback((choiceId: string) => {
    const step = steps[cursor];
    const id = `${sectionNumber}-${cursor}`;

    if (step?.kind === "item_moment") {
      const used = choiceId === "use";
      if (used) adventureService.useByTag(step.item_tag).catch(() => {});
      addEntry({
        id: `${id}-item-${choiceId}`,
        kind: "narrative",
        text: used ? step.on_use.narrative : step.on_skip.npc_reaction,
      });
      if (used) {
        addEntry({ id: `${id}-item-react`, kind: "npc", npc: step.npc, line: step.on_use.npc_reaction, audio_url: step.on_use.npc_reaction_audio_url });
      }
      setCursor((current) => current + 1);
      setActiveChoice(null);
      setPhase("tap");
      return;
    }

    if (step?.kind !== "multiple_choice") return;
    const isCorrect = choiceId === step.correct;
    const chosenText = step.options.find((option) => option.id === choiceId)?.text ?? choiceId;
    const correctText = step.options.find((option) => option.id === step.correct)?.text ?? step.correct;
    addEntry({ id: `${id}-answer`, kind: "answer", text: chosenText, label: playerLabel, correct: isCorrect, correctText });
    if (isCorrect) setCorrect((value) => value + 1);
    else setMistakes((value) => value + 1);
    if (step.word_id) {
      adventureService.recordWordAnswer({
        word_id: step.word_id,
        correct: isCorrect,
        target: step.target,
        native: step.native,
        lang_code: langCode.toLowerCase(),
      }).catch(() => {});
    }
    setActiveChoice(null);
    setPhase("tap");
    setCursor((current) => current + 1);
  }, [addEntry, cursor, langCode, playerLabel, sectionNumber, steps]);

  const submitInput = useCallback((value: string) => {
    if (!activeInput) return;
    const id = `${sectionNumber}-${cursor}`;
    const isCorrect = normalizeAnswer(value) === normalizeAnswer(activeInput.answer);
    addEntry({
      id: `${id}-input`,
      kind: "answer",
      text: value,
      label: playerLabel,
      correct: isCorrect,
      correctText: activeInput.answer,
    });
    if (isCorrect) setCorrect((current) => current + 1);
    else setMistakes((current) => current + 1);
    setActiveInput(null);
    setPhase("tap");
    setCursor((current) => current + 1);
  }, [activeInput, addEntry, cursor, playerLabel, sectionNumber]);

  const completeSummary = useCallback(() => {
    onComplete(mistakes);
  }, [mistakes, onComplete]);

  return {
    entries,
    phase,
    activeChoice,
    activeInput,
    summary,
    recap: section.recap,
    continueStep,
    choose,
    submitInput,
    completeSummary,
  };
}
