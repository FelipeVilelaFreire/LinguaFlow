import { CheckCircle2, Heart, MousePointerClick, RotateCcw, Send } from "lucide-react";
import type { CSSProperties } from "react";

import { useStrings } from "../../contexts/StringsContext";
import type { Phrase, PracticeItem } from "../../types/content";

interface LessonCardProps {
  answer: string;
  checked: boolean;
  feedback: { quality: "correct" | "close" | "wrong"; missingWords: string[]; expected: string };
  isCorrect: boolean;
  item: PracticeItem | null;
  phrase: Phrase | null;
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
  feedback,
  isCorrect,
  item,
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
  const canContinue = checked && feedback.quality !== "wrong";
  const primaryAction = canContinue ? strings.actions.next : strings.actions.check;
  const exercise = item ?? {
    type: "new",
    prompt: phrase?.target_text ?? "",
    answer: phrase?.source_text ?? "",
    helper: strings.today.inputPrompt,
    options: [],
    word_bank: [],
  };
  const labels = getPracticeLabels(exercise.type, strings.today.inputPrompt);
  const isIntro = exercise.type === "intro";
  const usesChoice = exercise.type === "multiple_choice";
  const usesWordOrder = exercise.type === "word_order";

  if (isIntro) {
    return (
      <section className="relative">
        <div className="absolute inset-x-4 -bottom-3 top-5 rounded-[8px] bg-white/60 ring-1 ring-slate-200" style={{ animation: "stackLift 360ms ease-out both" }} />
        <div className="relative rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200 md:p-7" style={{ animation: "studyCardIn 320ms ease-out both" }}>
          <p className="inline-flex rounded-full px-3 py-1 text-sm font-semibold ring-1" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
            Aula do dia
          </p>
          <h2 className="mt-4 text-3xl font-semibold leading-tight text-slate-950 md:text-5xl">{exercise.prompt}</h2>
          <p className="mt-3 max-w-2xl font-medium leading-7 text-slate-600">
            Primeiro veja o contexto e as frases principais. Depois a pratica vai cobrar exatamente esse conteudo e revisoes anteriores.
          </p>

          <div className="mt-6 grid gap-3">
            {(exercise.preview_phrases ?? []).map((preview, index) => (
              <div key={`${preview.target_text}-${index}`} className="rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-200">
                <p className="text-xs font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{preview.target_code}</p>
                <p className="mt-1 text-xl font-semibold text-slate-950">{preview.target_text}</p>
                <p className="mt-2 text-sm font-semibold uppercase text-slate-500">{preview.source_code}</p>
                <p className="mt-1 font-medium text-slate-600">{preview.source_text}</p>
              </div>
            ))}
          </div>

          <button type="button" onClick={onNext} className="mt-6 inline-flex w-full items-center justify-center gap-2 rounded-[8px] px-4 py-3 text-sm font-semibold text-white shadow-sm transition hover:brightness-95" style={{ background: "var(--area-primary)" }}>
            Comecar pratica
            <Send size={16} />
          </button>
        </div>
      </section>
    );
  }

  return (
    <section className="relative">
      <div className="absolute inset-x-4 -bottom-3 top-5 rounded-[8px] bg-white/60 ring-1 ring-slate-200" style={{ animation: "stackLift 360ms ease-out both" }} />
      <div className="absolute inset-x-8 -bottom-6 top-10 rounded-[8px] bg-white/40 ring-1 ring-slate-200" style={{ animation: "stackLift 420ms ease-out both" }} />
      <div className="relative rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200 md:p-7" style={{ animation: checked && feedback.quality !== "wrong" ? "lessonBounce 360ms ease-out both" : "studyCardIn 320ms ease-out both" }}>
      <div className="flex items-start justify-between gap-4">
        <div>
          <p className="inline-flex rounded-full px-3 py-1 text-sm font-semibold ring-1" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
            {labels.title} {phraseIndex + 1} / {totalPhrases}
          </p>
          <p className="mt-4 max-w-2xl text-sm font-bold leading-6 text-slate-500">{labels.detail}</p>
          <h2 className="mt-5 min-h-24 text-4xl font-semibold leading-tight text-slate-950 md:text-5xl">{exercise.prompt}</h2>
        </div>
        <button type="button" onClick={onFavorite} className="grid h-11 w-11 shrink-0 place-items-center rounded-[8px] bg-rose-50 text-rose-600 ring-1 ring-rose-100 transition hover:bg-rose-100" title={strings.actions.favorite}>
          <Heart size={21} />
        </button>
      </div>

      <button type="button" onClick={onReveal} className="mt-6 inline-flex items-center gap-2 rounded-[8px] bg-slate-950 px-5 py-3 text-sm font-semibold text-white shadow-sm transition hover:bg-slate-800">
        <RotateCcw size={17} />
        {showTranslation ? strings.actions.hideTranslation : strings.actions.showTranslation}
      </button>

      <div className={`mt-5 rounded-[8px] border-l-4 bg-slate-50 p-4 ring-1 ring-slate-200 transition-all duration-300 ${showTranslation ? "translate-y-0 opacity-100" : "pointer-events-none -translate-y-2 opacity-0"}`} style={{ borderColor: "var(--area-primary)" }}>
        <p className="text-xs font-semibold uppercase text-slate-500">{phrase?.source_language.code}</p>
        <p className="mt-1 text-xl font-semibold">{exercise.answer}</p>
      </div>

      {usesChoice ? (
        <div className="mt-6 grid gap-3">
          <p className="text-sm font-semibold uppercase text-slate-500">{labels.input}</p>
          {exercise.options.map((option) => (
            <button
              key={option}
              type="button"
              onClick={() => onAnswerChange(option)}
              className={`flex min-h-12 items-center gap-3 rounded-[8px] px-4 py-3 text-left font-semibold ring-1 transition ${answer === option ? "text-white shadow-sm" : "bg-slate-50 ring-slate-200 hover:bg-white"}`}
              style={answer === option ? { animation: "optionTap 180ms ease-out both", background: "var(--area-primary)", borderColor: "var(--area-primary)" } : undefined}
            >
              <MousePointerClick size={17} />
              {option}
            </button>
          ))}
        </div>
      ) : usesWordOrder ? (
        <div className="mt-6 rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-200">
          <p className="text-sm font-semibold uppercase text-slate-500">{labels.input}</p>
          <div className="mt-3 min-h-14 rounded-[8px] bg-white p-3 text-lg font-semibold ring-1 ring-slate-200">
            {answer || " "}
          </div>
          <div className="mt-3 flex flex-wrap gap-2">
            {exercise.word_bank.map((word, index) => (
              <button key={`${word}-${index}`} type="button" onClick={() => onAnswerChange(answer ? `${answer} ${word}` : word)} className="rounded-[8px] bg-white px-3 py-2 text-sm font-semibold ring-1 ring-slate-200 transition hover:bg-slate-100">
                {word}
              </button>
            ))}
            <button type="button" onClick={() => onAnswerChange("")} className="rounded-[8px] bg-slate-950 px-3 py-2 text-sm font-semibold text-white">
              Limpar
            </button>
          </div>
        </div>
      ) : (
        <div className="mt-6 rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-200">
          <label className="text-sm font-semibold uppercase text-slate-500" htmlFor="answer">
            {labels.input}
          </label>
          <input
            id="answer"
            value={answer}
            onChange={(event) => onAnswerChange(event.target.value)}
            className="mt-3 h-14 w-full rounded-[8px] border border-slate-200 bg-white px-4 text-lg font-medium outline-none transition focus:border-transparent focus:ring-4"
            style={{ "--tw-ring-color": "var(--area-primary-soft)" } as CSSProperties}
          />
        </div>
      )}

      {checked ? (
        <div className={`mt-4 rounded-[8px] px-4 py-3 text-sm font-semibold transition ${feedback.quality === "correct" ? "bg-emerald-50 text-emerald-700 ring-1 ring-emerald-100" : feedback.quality === "close" ? "bg-amber-50 text-amber-700 ring-1 ring-amber-100" : "bg-red-50 text-red-700 ring-1 ring-red-100 animate-[shake_180ms_ease-in-out]"}`} style={feedback.quality !== "wrong" ? { animation: "successPop 260ms ease-out both" } : undefined}>
          <div className="flex items-center gap-2">
            <CheckCircle2 size={18} />
            {feedback.quality === "correct" ? strings.today.correct : feedback.quality === "close" ? "Quase certo" : strings.today.tryAgain}
          </div>
          {feedback.quality !== "correct" ? (
            <div className="mt-2 text-sm font-medium">
              <p>Resposta ideal: <span className="font-bold">{feedback.expected}</span></p>
              {feedback.missingWords.length ? <p className="mt-1">Faltou revisar: {feedback.missingWords.join(", ")}</p> : null}
            </div>
          ) : null}
        </div>
      ) : null}

      <div className="mt-6 grid gap-3 sm:grid-cols-[1fr_auto]">
        <button type="button" onClick={canContinue ? onNext : onCheck} className="inline-flex items-center justify-center gap-2 rounded-[8px] px-4 py-3 text-sm font-semibold text-white shadow-sm transition hover:brightness-95" style={{ background: "var(--area-primary)" }}>
          {primaryAction}
          <Send size={16} />
        </button>
        <button type="button" onClick={onNext} className="rounded-[8px] bg-white px-4 py-3 text-sm font-semibold ring-1 ring-slate-200 transition hover:bg-slate-50">
          {strings.actions.skip}
        </button>
      </div>
      </div>
    </section>
  );
}

function getPracticeLabels(type: PracticeItem["type"], fallback: string) {
  if (type === "multiple_choice") {
    return {
      title: "Escolha",
      detail: "Toque na alternativa correta para a frase.",
      input: "Escolha a resposta correta:",
    };
  }
  if (type === "intro") {
    return {
      title: "Aquecimento",
      detail: "Veja o contexto antes de praticar.",
      input: "Comece quando estiver pronto:",
    };
  }
  if (type === "fill_blank") {
    return {
      title: "Lacuna",
      detail: "Complete a palavra que falta na frase.",
      input: "Digite a palavra faltando:",
    };
  }
  if (type === "word_order") {
    return {
      title: "Montar frase",
      detail: "Toque nas palavras para montar a frase no idioma alvo.",
      input: "Monte a frase:",
    };
  }
  if (type === "reverse") {
    return {
      title: "Traducao",
      detail: "Leia no idioma base e escreva no idioma alvo.",
      input: "Escreva a resposta:",
    };
  }
  if (type === "dictation") {
    return {
      title: "Memoria",
      detail: "Use o sentido da frase para reconstruir a frase no idioma alvo.",
      input: "Digite no idioma alvo:",
    };
  }
  if (type === "review") {
    return {
      title: "Revisao",
      detail: "Reforce uma frase antiga antes de avancar.",
      input: "Escreva o significado:",
    };
  }
  return {
    title: "Frase nova",
    detail: fallback,
    input: "Escreva o significado:",
  };
}
