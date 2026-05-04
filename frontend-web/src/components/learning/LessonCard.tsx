import { CheckCircle2, Heart, RotateCcw, Send } from "lucide-react";

import { useStrings } from "../../contexts/StringsContext";
import type { Phrase } from "../../types/content";

interface LessonCardProps {
  answer: string;
  checked: boolean;
  isCorrect: boolean;
  phrase: Phrase;
  phraseIndex: number;
  totalPhrases: number;
  showTranslation: boolean;
  onAnswerChange: (value: string) => void;
  onCheck: () => void;
  onFavorite: () => void;
  onNext: () => void;
  onReveal: () => void;
}

export default function LessonCard({
  answer,
  checked,
  isCorrect,
  phrase,
  phraseIndex,
  totalPhrases,
  showTranslation,
  onAnswerChange,
  onCheck,
  onFavorite,
  onNext,
  onReveal,
}: LessonCardProps) {
  const strings = useStrings();

  return (
    <section className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200 md:p-8">
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>
            {strings.today.lesson} {phraseIndex + 1} / {totalPhrases}
          </p>
          <p className="mt-2 text-sm font-bold text-slate-500">{strings.today.inputPrompt}</p>
          <h2 className="mt-5 min-h-28 text-4xl font-semibold leading-tight md:text-5xl">{phrase.target_text}</h2>
        </div>
        <button type="button" onClick={onFavorite} className="grid h-11 w-11 shrink-0 place-items-center rounded-[8px] bg-rose-50 text-rose-600 ring-1 ring-rose-100 transition hover:bg-rose-100" title={strings.actions.favorite}>
          <Heart size={21} />
        </button>
      </div>

      <button type="button" onClick={onReveal} className="mt-6 inline-flex items-center gap-2 rounded-[8px] bg-slate-950 px-5 py-3 text-sm font-semibold text-white shadow-sm transition hover:bg-slate-800">
        <RotateCcw size={17} />
        {showTranslation ? strings.actions.hideTranslation : strings.actions.showTranslation}
      </button>

      <div className={`mt-5 rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-200 transition-all duration-300 ${showTranslation ? "translate-y-0 opacity-100" : "pointer-events-none -translate-y-2 opacity-0"}`}>
        <p className="text-xs font-semibold uppercase text-slate-500">{phrase.source_language.code}</p>
        <p className="mt-1 text-xl font-semibold">{phrase.source_text}</p>
      </div>

      <div className="mt-6 rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-200">
        <label className="text-sm font-semibold uppercase text-slate-500" htmlFor="answer">
          {strings.today.recallPrompt}
        </label>
        <input
          id="answer"
          value={answer}
          onChange={(event) => onAnswerChange(event.target.value)}
          className="mt-3 h-14 w-full rounded-[8px] border border-slate-200 bg-white px-4 text-lg font-medium outline-none transition focus:ring-4"
        />
      </div>

      {checked ? (
        <div className={`mt-4 flex items-center gap-2 rounded-[8px] px-4 py-3 text-sm font-semibold transition ${isCorrect ? "bg-emerald-50 text-emerald-700 ring-1 ring-emerald-100" : "bg-red-50 text-red-700 ring-1 ring-red-100 animate-[shake_180ms_ease-in-out]"}`}>
          <CheckCircle2 size={18} />
          {isCorrect ? strings.today.correct : strings.today.tryAgain}
        </div>
      ) : null}

      <div className="mt-6 grid gap-3 sm:grid-cols-2">
        <button type="button" onClick={onCheck} className="rounded-[8px] bg-white px-4 py-3 text-sm font-semibold ring-1 ring-slate-200 transition hover:bg-slate-50">
          {strings.actions.check}
        </button>
        <button type="button" onClick={onNext} className="inline-flex items-center justify-center gap-2 rounded-[8px] px-4 py-3 text-sm font-semibold text-white shadow-sm transition hover:brightness-95" style={{ background: "var(--area-primary)" }}>
          {strings.actions.next}
          <Send size={16} />
        </button>
      </div>
    </section>
  );
}
