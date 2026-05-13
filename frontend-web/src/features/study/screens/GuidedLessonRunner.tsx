import { ArrowLeft, BookOpen, Check, X } from "lucide-react";
import { useMemo, useState } from "react";

import { useStrings } from "../../../contexts/StringsContext";
import { adventureService } from "../../../services/adventureService";
import type { Phrase, StudyLesson } from "../../../types/content";

// ── Types ──────────────────────────────────────────────────────────────────────

type Option = { id: string; text: string; correct: boolean };

type Step =
  | { kind: "intro" }
  | { kind: "learn";    phrase: Phrase; learnIdx: number }
  | { kind: "check";    phrase: Phrase; options: Option[] }
  | { kind: "bridge";   learnedCount: number }
  | { kind: "practice"; phrase: Phrase; options: Option[] }
  | { kind: "done" };

// ── Helpers ────────────────────────────────────────────────────────────────────

function shuffleArr<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function buildOptions(phrase: Phrase, allPhrases: Phrase[]): Option[] {
  const distractors = shuffleArr(allPhrases.filter((p) => p.id !== phrase.id))
    .slice(0, 3)
    .map((p) => ({ id: "", text: p.target_text, correct: false as boolean }));

  const raw = shuffleArr([
    { id: "", text: phrase.target_text, correct: true as boolean },
    ...distractors,
  ]);

  return raw.map((opt, i) => ({ ...opt, id: String.fromCharCode(97 + i) }));
}

function buildSteps(phrases: Phrase[]): Step[] {
  if (phrases.length === 0) return [{ kind: "done" }];

  const steps: Step[] = [{ kind: "intro" }];

  phrases.forEach((phrase, i) => {
    steps.push({ kind: "learn", phrase, learnIdx: i });
    // Start checks from the 3rd word so we always have 3+ distractors for good options
    if (i >= 2) {
      steps.push({ kind: "check", phrase, options: buildOptions(phrase, phrases) });
    }
  });

  if (phrases.length >= 2) {
    steps.push({ kind: "bridge", learnedCount: phrases.length });
    shuffleArr(phrases).forEach((phrase) => {
      steps.push({ kind: "practice", phrase, options: buildOptions(phrase, phrases) });
    });
  }

  steps.push({ kind: "done" });
  return steps;
}

// ── Component ──────────────────────────────────────────────────────────────────

interface GuidedLessonRunnerProps {
  lesson: StudyLesson;
  phrases: Phrase[];
  onBack: () => void;
  onComplete: () => void;
}

export default function GuidedLessonRunner({ lesson, phrases, onBack, onComplete }: GuidedLessonRunnerProps) {
  const s = useStrings();

  // Steps are computed once on mount — shuffling is stable for this session
  const steps = useMemo(() => buildSteps(phrases), [phrases]);

  const [stepIdx, setStepIdx]               = useState(0);
  const [selected, setSelected]             = useState<string | null>(null);
  const [revealed, setRevealed]             = useState(false);
  const [practiceScore, setPracticeScore]   = useState(0);
  const practiceTotal = steps.filter((st) => st.kind === "practice").length;

  const step     = steps[stepIdx];
  const progress = steps.length > 1 ? stepIdx / (steps.length - 1) : 1;

  function advance() {
    setSelected(null);
    setRevealed(false);
    if (stepIdx + 1 >= steps.length) {
      onComplete();
    } else {
      setStepIdx((n) => n + 1);
    }
  }

  function handleSelect(opt: Option) {
    if (revealed) return;
    setSelected(opt.id);
    setRevealed(true);
    if (step.kind === "practice" || step.kind === "check") {
      if (step.kind === "practice" && opt.correct) setPracticeScore((n) => n + 1);
      // Feed every word answer into the SRS system (both check and practice rounds)
      adventureService.recordWordAnswer({
        word_id:   `${step.phrase.target_language.code.toLowerCase()}_${step.phrase.id}`,
        correct:   opt.correct,
        target:    step.phrase.target_text,
        native:    step.phrase.source_text,
        lang_code: step.phrase.target_language.code.toLowerCase(),
      }).catch(() => {});
    }
  }

  // Shared header: back button + lesson title + progress bar
  const header = (
    <div className="flex items-center gap-3">
      <button
        type="button"
        onClick={onBack}
        className="flex h-9 w-9 shrink-0 items-center justify-center rounded-[8px] border border-slate-200 text-slate-500 hover:bg-slate-50 transition"
      >
        <ArrowLeft size={16} />
      </button>
      <div className="flex-1">
        <p className="text-sm font-semibold text-slate-950">{lesson.title}</p>
        <div className="mt-1.5 h-1.5 w-full overflow-hidden rounded-full bg-slate-100">
          <div
            className="h-full rounded-full transition-all duration-500 area-btn"
            style={{ width: `${progress * 100}%` }}
          />
        </div>
      </div>
    </div>
  );

  // ── Intro ──────────────────────────────────────────────────────────────────

  if (step.kind === "intro") {
    return (
      <div className="flex flex-col gap-6" style={{ animation: "fadeIn 260ms ease-out" }}>
        {header}
        <div className="flex flex-col items-center gap-4 py-10 text-center">
          <div className="area-bg-soft flex h-16 w-16 items-center justify-center rounded-2xl">
            <BookOpen size={28} className="area-text-primary" />
          </div>
          <div>
            <p className="text-xl font-bold text-slate-950">{lesson.title}</p>
            <p className="mt-1 text-sm font-medium text-slate-500">
              {s.study.phrasesCount(phrases.length)}
            </p>
          </div>
          <p className="max-w-xs text-sm font-medium text-slate-400">
            {s.study.guidedIntroDetail}
          </p>
        </div>
        <button
          type="button"
          onClick={advance}
          className="area-btn h-14 rounded-[8px] font-semibold shadow-sm transition"
        >
          {s.actions.continue}
        </button>
      </div>
    );
  }

  // ── Learn ──────────────────────────────────────────────────────────────────

  if (step.kind === "learn") {
    return (
      <div
        key={stepIdx}
        className="flex flex-col gap-5"
        style={{ animation: "studyCardIn 260ms ease-out" }}
      >
        {header}

        <div className="flex items-center justify-between">
          <p className="text-xs font-semibold uppercase tracking-wide area-text-primary">
            {s.study.guidedNewWord}
          </p>
          <p className="text-xs font-medium text-slate-400">
            {s.study.guidedWordOf(step.learnIdx + 1, phrases.length)}
          </p>
        </div>

        <div className="card flex flex-col items-center gap-4 p-8 text-center">
          <p
            className="text-4xl font-bold leading-tight area-text-primary"
            style={{ fontFeatureSettings: '"kern"' }}
          >
            {step.phrase.target_text}
          </p>
          <div className="h-px w-10 bg-slate-200" />
          <p className="text-lg font-semibold text-slate-500">{step.phrase.source_text}</p>
        </div>

        <button
          type="button"
          onClick={advance}
          className="area-btn h-14 rounded-[8px] font-semibold shadow-sm transition"
        >
          {s.study.guidedUnderstood}
        </button>
      </div>
    );
  }

  // ── Check / Practice ───────────────────────────────────────────────────────

  if (step.kind === "check" || step.kind === "practice") {
    const selectedOpt = step.options.find((o) => o.id === selected);
    const correctOpt  = step.options.find((o) => o.correct);
    const isRight     = selectedOpt?.correct ?? false;

    return (
      <div
        key={stepIdx}
        className="flex flex-col gap-5"
        style={{ animation: "studyCardIn 260ms ease-out" }}
      >
        {header}

        <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-[0_2px_4px_rgba(0,0,0,0.03),0_8px_24px_rgba(0,0,0,0.06)]">
          <div className="flex flex-col gap-4">
            <p className="text-base font-semibold text-slate-950">
              {s.study.guidedCheckQuestion(step.phrase.source_text)}
            </p>

            <div className="flex flex-col gap-2">
              {step.options.map((opt) => {
                const isSelected = opt.id === selected;
                let cls =
                  "flex w-full items-center gap-3 rounded-xl border px-4 py-3.5 text-sm font-semibold transition text-left";
                if (!revealed) {
                  cls += " border-slate-200 bg-white hover:bg-slate-50 text-slate-950";
                } else if (opt.correct) {
                  cls += " border-emerald-300 bg-emerald-50 text-emerald-800";
                } else if (isSelected) {
                  cls += " border-red-300 bg-red-50 text-red-700";
                } else {
                  cls += " border-slate-100 bg-slate-50 text-slate-400";
                }
                return (
                  <button
                    key={opt.id}
                    type="button"
                    onClick={() => handleSelect(opt)}
                    className={cls}
                  >
                    {revealed && opt.correct && (
                      <Check size={15} className="shrink-0 text-emerald-600" />
                    )}
                    {revealed && isSelected && !opt.correct && (
                      <X size={15} className="shrink-0 text-red-500" />
                    )}
                    {!revealed && (
                      <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full border border-slate-300 text-xs font-bold text-slate-500">
                        {opt.id.toUpperCase()}
                      </span>
                    )}
                    {opt.text}
                  </button>
                );
              })}
            </div>

            {revealed && (
              <p className={`text-sm font-semibold ${isRight ? "text-emerald-700" : "text-red-600"}`}>
                {isRight
                  ? s.study.correctLabel
                  : `${s.study.wrongLabel} — ${correctOpt?.text ?? ""}`}
              </p>
            )}
          </div>
        </div>

        {revealed && (
          <button
            type="button"
            onClick={advance}
            className="area-btn h-14 rounded-[8px] font-semibold shadow-sm transition"
          >
            {s.actions.continue}
          </button>
        )}
      </div>
    );
  }

  // ── Bridge ─────────────────────────────────────────────────────────────────

  if (step.kind === "bridge") {
    return (
      <div className="flex flex-col gap-6" style={{ animation: "fadeIn 260ms ease-out" }}>
        {header}
        <div className="flex flex-col items-center gap-4 py-10 text-center">
          <div className="area-bg-soft flex h-16 w-16 items-center justify-center rounded-2xl">
            <Check size={28} className="area-text-primary" />
          </div>
          <div>
            <p className="text-xl font-bold text-slate-950">{s.study.guidedPracticeTitle}</p>
            <p className="mt-1 text-sm font-medium text-slate-400">
              {s.study.guidedPracticeDetail(step.learnedCount)}
            </p>
          </div>
        </div>
        <button
          type="button"
          onClick={advance}
          className="area-btn h-14 rounded-[8px] font-semibold shadow-sm transition"
        >
          {s.study.guidedPracticeStart}
        </button>
      </div>
    );
  }

  // ── Done ───────────────────────────────────────────────────────────────────

  if (step.kind === "done") {
    const pct = practiceTotal > 0 ? Math.round((practiceScore / practiceTotal) * 100) : 100;
    return (
      <div
        className="flex min-h-[calc(100dvh-3.5rem)] flex-col items-center justify-center gap-6 p-6"
        style={{ animation: "celebrationRise 400ms ease-out" }}
      >
        <div className="area-bg-soft flex h-16 w-16 items-center justify-center rounded-full">
          <Check size={28} className="area-text-primary" />
        </div>
        <div className="text-center">
          <p className="text-xl font-bold text-slate-950">{s.study.sessionComplete}</p>
          {practiceTotal > 0 && (
            <>
              <p className="mt-1 text-lg font-semibold area-text-primary">
                {s.study.sessionScore(practiceScore, practiceTotal)}
              </p>
              <p className="mt-0.5 text-sm font-medium text-slate-400">
                {s.study.sessionScoreDetail(pct)}
              </p>
            </>
          )}
        </div>
        <button type="button" onClick={onComplete} className="auth-submit w-full max-w-xs">
          {s.actions.back}
        </button>
      </div>
    );
  }

  return null;
}
