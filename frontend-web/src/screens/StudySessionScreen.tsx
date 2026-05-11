import { ArrowLeft, Check, X } from "lucide-react";
import { useRef, useState } from "react";

import { useStrings } from "../contexts/StringsContext";
import { adventureService } from "../services/adventureService";
import type { StudySessionExercise } from "../types/content";

interface StudySessionScreenProps {
  exercises: StudySessionExercise[];
  onBack: () => void;
  onComplete: () => void;
}

export default function StudySessionScreen({ exercises, onBack, onComplete }: StudySessionScreenProps) {
  const s = useStrings();
  const [idx, setIdx] = useState(0);
  const [selected, setSelected] = useState<string | null>(null);
  const [revealed, setRevealed] = useState(false);
  const [written, setWritten] = useState("");
  const [writeCorrect, setWriteCorrect] = useState<boolean | null>(null);
  const [score, setScore] = useState(0);
  const [done, setDone] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  const exercise = exercises[idx];
  const total    = exercises.length;

  function handleSelect(optId: string) {
    if (revealed) return;
    const correct = optId === exercise.correct;
    setSelected(optId);
    setRevealed(true);
    if (correct) setScore((n) => n + 1);
    adventureService.recordWordAnswer({
      word_id:    exercise.word_id,
      correct,
      target:     exercise.target,
      native:     exercise.native,
      lang_code:  exercise.word_id.split("_")[0],
    }).catch(() => {});
  }

  function handleWrite(e: React.FormEvent) {
    e.preventDefault();
    if (writeCorrect !== null) return;
    const correct = written.trim().toLowerCase() === (exercise.answer ?? "").toLowerCase();
    setWriteCorrect(correct);
    setRevealed(true);
    if (correct) setScore((n) => n + 1);
    adventureService.recordWordAnswer({
      word_id:    exercise.word_id,
      correct,
      target:     exercise.target,
      native:     exercise.native,
      lang_code:  exercise.word_id.split("_")[0],
    }).catch(() => {});
  }

  function advance() {
    if (idx + 1 >= total) {
      setDone(true);
    } else {
      setIdx((n) => n + 1);
      setSelected(null);
      setRevealed(false);
      setWritten("");
      setWriteCorrect(null);
    }
  }

  if (done) {
    const pct = Math.round((score / total) * 100);
    return (
      <div className="flex min-h-[calc(100dvh-3.5rem)] flex-col items-center justify-center gap-6 p-6"
           style={{ animation: "fadeIn 300ms ease-out" }}>
        <div className="flex h-16 w-16 items-center justify-center rounded-full area-bg-soft">
          <Check size={28} className="area-text-primary" />
        </div>
        <div className="text-center">
          <p className="text-xl font-bold text-slate-950">{s.study.sessionComplete}</p>
          <p className="mt-1 text-lg font-semibold area-text-primary">
            {s.study.sessionScore(score, total)}
          </p>
          <p className="mt-0.5 text-sm font-medium text-slate-400">
            {s.study.sessionScoreDetail(pct)}
          </p>
        </div>
        <button type="button" onClick={onComplete} className="auth-submit w-full max-w-xs">
          {s.actions.back}
        </button>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-5" style={{ animation: "fadeIn 240ms ease-out" }}>

      {/* Header */}
      <div className="flex items-center gap-3">
        <button type="button" onClick={onBack}
          className="flex h-9 w-9 items-center justify-center rounded-[8px] border border-slate-200 text-slate-500 hover:bg-slate-50 transition">
          <ArrowLeft size={16} />
        </button>
        <div className="flex-1">
          <div className="flex items-center justify-between">
            <p className="text-sm font-semibold text-slate-950">{s.study.sessionTitle}</p>
            <p className="text-xs font-semibold text-slate-400">
              {s.study.sessionProgress(idx + 1, total)}
            </p>
          </div>
          <div className="mt-1.5 h-1.5 w-full overflow-hidden rounded-full bg-slate-100">
            <div className="h-full rounded-full transition-all duration-300 area-btn"
                 style={{ width: `${((idx + 1) / total) * 100}%` }} />
          </div>
        </div>
      </div>

      {/* Exercise card */}
      <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-[0_2px_4px_rgba(0,0,0,0.03),0_8px_24px_rgba(0,0,0,0.06)]"
           key={idx} style={{ animation: "studyCardIn 260ms ease-out" }}>

        {exercise.kind === "multiple_choice" && (
          <MultipleChoice
            exercise={exercise}
            selected={selected}
            revealed={revealed}
            onSelect={handleSelect}
          />
        )}

        {exercise.kind === "write_word" && (
          <WriteWord
            exercise={exercise}
            written={written}
            isCorrect={writeCorrect}
            revealed={revealed}
            inputRef={inputRef}
            onWritten={setWritten}
            onSubmit={handleWrite}
            placeholder={s.study.writePlaceholder}
            hintLabel={s.study.hintLabel}
          />
        )}

        {revealed && (
          <button type="button" onClick={advance}
            className="auth-submit mt-5 w-full">
            {s.actions.continue}
          </button>
        )}
      </div>

    </div>
  );
}

function MultipleChoice({ exercise, selected, revealed, onSelect }: {
  exercise: StudySessionExercise;
  selected: string | null;
  revealed: boolean;
  onSelect: (id: string) => void;
}) {
  const s = useStrings();
  return (
    <div className="flex flex-col gap-4">
      <p className="text-base font-semibold text-slate-950">{exercise.question}</p>

      <div className="flex flex-col gap-2">
        {(exercise.options ?? []).map((opt) => {
          const isCorrect  = opt.id === exercise.correct;
          const isSelected = opt.id === selected;
          let cls = "flex items-center gap-3 rounded-xl border px-4 py-3 text-sm font-semibold transition text-left w-full";
          if (!revealed) {
            cls += " border-slate-200 bg-white hover:bg-slate-50 text-slate-950";
          } else if (isCorrect) {
            cls += " border-emerald-300 bg-emerald-50 text-emerald-800";
          } else if (isSelected) {
            cls += " border-red-300 bg-red-50 text-red-700";
          } else {
            cls += " border-slate-100 bg-slate-50 text-slate-400";
          }
          return (
            <button key={opt.id} type="button" onClick={() => onSelect(opt.id)} className={cls}>
              {revealed && isCorrect && <Check size={15} className="shrink-0 text-emerald-600" />}
              {revealed && isSelected && !isCorrect && <X size={15} className="shrink-0 text-red-500" />}
              {!revealed && <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full border border-slate-300 text-xs font-bold text-slate-500">{opt.id.toUpperCase()}</span>}
              {opt.text}
            </button>
          );
        })}
      </div>

      {revealed && (
        <p className={`text-sm font-semibold ${selected === exercise.correct ? "text-emerald-700" : "text-red-600"}`}>
          {selected === exercise.correct
            ? s.study.correctLabel
            : `${s.study.wrongLabel} — ${(exercise.options ?? []).find((o) => o.id === exercise.correct)?.text ?? ""}`}
        </p>
      )}
    </div>
  );
}

function WriteWord({ exercise, written, isCorrect, revealed, inputRef, onWritten, onSubmit, placeholder, hintLabel }: {
  exercise: StudySessionExercise;
  written: string;
  isCorrect: boolean | null;
  revealed: boolean;
  inputRef: React.RefObject<HTMLInputElement>;
  onWritten: (v: string) => void;
  onSubmit: (e: React.FormEvent) => void;
  placeholder: string;
  hintLabel: string;
}) {
  const s = useStrings();
  return (
    <form onSubmit={onSubmit} className="flex flex-col gap-4">
      <p className="text-base font-semibold text-slate-950">{exercise.prompt}</p>

      {exercise.hint && !revealed && (
        <p className="text-xs font-medium text-slate-400">
          {hintLabel}: <span className="font-mono tracking-widest">{exercise.hint}</span>
        </p>
      )}

      <input
        ref={inputRef}
        type="text"
        value={written}
        onChange={(e) => onWritten(e.target.value)}
        disabled={revealed}
        placeholder={placeholder}
        className={`area-input w-full ${
          isCorrect === true  ? "border-emerald-400 bg-emerald-50" :
          isCorrect === false ? "border-red-400 bg-red-50" : ""
        }`}
        autoFocus
      />

      {revealed && (
        <p className={`text-sm font-semibold ${isCorrect ? "text-emerald-700" : "text-red-600"}`}>
          {isCorrect ? s.study.correctLabel : `${s.study.wrongLabel} — ${exercise.answer}`}
        </p>
      )}

      {!revealed && (
        <button type="submit" className="auth-submit">
          {s.actions.check}
        </button>
      )}
    </form>
  );
}
