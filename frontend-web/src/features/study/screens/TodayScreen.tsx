import { CalendarCheck2, CheckCircle2, Flame, Lightbulb, Sparkles, Trophy } from "lucide-react";

import LessonCard from "../components/learning/LessonCard";
import VideoCard from "../components/learning/VideoCard";
import ProgressBar from "../../../components/ui/ProgressBar";
import StateMessage from "../../../components/ui/StateMessage";
import { useStrings } from "../../../contexts/StringsContext";
import { useTodayStudy } from "../../../hooks/useTodayStudy";

interface TodayScreenProps {
  onCompleted: () => void;
}

export default function TodayScreen({ onCompleted }: TodayScreenProps) {
  const strings = useStrings();
  const study = useTodayStudy(onCompleted);
  const today = study.today.data;

  if (study.today.loading) return <StateMessage />;
  if (study.today.error || !today || !study.currentItem) {
    return (
      <StateMessage
        title={strings.today.noLessonsTitle}
        detail={strings.today.noLessonsDetail}
      />
    );
  }

  if (study.completed) {
    return (
      <section className="card relative overflow-hidden p-6 text-center md:p-8">
        <div className="pointer-events-none absolute inset-x-0 top-0 flex justify-center gap-5">
          {[0, 1, 2, 3, 4, 5].map((item) => (
            <span
              key={item}
              className="h-2.5 w-2.5 rounded-[3px] opacity-0"
              style={{
                animation: `confettiFall 1100ms ease-out ${item * 90}ms both`,
                background: item % 2 === 0 ? "var(--area-primary)" : "var(--area-accent)",
              }}
            />
          ))}
        </div>

        <div className="mx-auto grid h-20 w-20 place-items-center rounded-[8px] text-white shadow-sm" style={{ animation: "successPop 420ms ease-out both, progressGlow 1600ms ease-in-out 320ms 2", background: "var(--area-primary)" }}>
          <Trophy size={38} />
        </div>
        <p className="mt-5 text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{strings.today.completed}</p>
        <h2 className="mt-2 text-4xl font-semibold text-slate-950 md:text-5xl">Sessao finalizada</h2>
        <p className="mx-auto mt-3 max-w-xl font-medium leading-7 text-slate-600">{strings.today.completedDetail}</p>

        <div className="mx-auto mt-6 grid max-w-3xl grid-cols-3 gap-2 md:mt-7 md:gap-3">
          <CompletionStat icon={<CheckCircle2 size={20} />} label="Exercicios" value={study.phrases.length} />
          <CompletionStat icon={<CalendarCheck2 size={20} />} label="Dia" value={today.day_number} />
          <CompletionStat icon={<Flame size={20} />} label="Progresso" value={100} suffix="%" />
        </div>

        <div className="mx-auto mt-7 max-w-xl rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-200">
          <p className="text-sm font-semibold uppercase text-slate-500">{today.lesson.scenario.title}</p>
          <p className="mt-1 text-xl font-semibold text-slate-950">{today.lesson.title}</p>
        </div>
      </section>
    );
  }

  return (
    <div className="pb-4 md:pb-0">
      <header className="card mb-4 p-4 md:mb-6 md:p-6">
        <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
          <div>
            <p className="inline-flex items-center gap-2 rounded-full px-3 py-1 text-sm font-semibold ring-1" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
              <Sparkles size={16} />
              {study.stage.title}
            </p>
            <h2 className="mt-3 text-2xl font-semibold leading-tight md:text-5xl">
              {strings.today.titlePrefix} {String(today.day_number).padStart(2, "0")} - {today.lesson.title}
            </h2>
            <p className="mt-2 max-w-2xl font-medium text-slate-500">{study.stage.detail}</p>
          </div>
          <div className="rounded-[8px] bg-slate-50 p-3 text-left ring-1 ring-slate-200 md:min-w-56 md:p-4 md:text-right">
            <p className="text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{study.progress}% {strings.layout.completed}</p>
            <p className="font-medium text-slate-500">{today.lesson.scenario.title}</p>
          </div>
        </div>
        <div className="mt-5">
          <ProgressBar value={study.progress} />
        </div>
      </header>

      <div className="grid gap-4 lg:grid-cols-[1fr_320px] lg:gap-5">
        <LessonCard
          key={study.currentItem?.id ?? study.phraseIndex}
          answer={study.answer}
          checked={study.checked}
          feedback={study.feedback}
          isCorrect={study.isCorrect}
          item={study.currentItem}
          phrase={study.currentPhrase}
          phraseIndex={study.phraseIndex}
          totalPhrases={study.phrases.length}
          showTranslation={study.showTranslation}
          onAnswerChange={study.setAnswer}
          onCheck={study.checkAnswer}
          onFavorite={study.favoriteCurrentPhrase}
          onNext={study.nextPhrase}
          onReveal={study.revealTranslation}
        />
        <div className="grid content-start gap-4">
          <VideoCard title={today.lesson.video_title} duration={today.lesson.video_duration} url={today.lesson.video_url} />
          <aside className="card p-5">
            <div className="grid h-11 w-11 place-items-center rounded-[8px]" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
              <Lightbulb size={20} />
            </div>
            <p className="mt-2 text-2xl font-semibold">{strings.today.practice}</p>
            <p className="mt-2 text-sm font-medium leading-6 text-slate-600">{strings.today.inputPrompt}</p>
          </aside>
        </div>
      </div>
    </div>
  );
}

function CompletionStat({ icon, label, value, suffix = "" }: { icon: React.ReactNode; label: string; value: number; suffix?: string }) {
  return (
    <div className="min-w-0 rounded-[8px] bg-slate-50 p-3 text-left ring-1 ring-slate-200 md:p-4" style={{ animation: "celebrationRise 420ms ease-out both" }}>
      <div className="grid h-9 w-9 place-items-center rounded-[8px] md:h-10 md:w-10" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
        {icon}
      </div>
      <p className="mt-3 text-2xl font-semibold text-slate-950 md:text-3xl">{value}{suffix}</p>
      <p className="break-words text-[11px] font-bold leading-tight text-slate-500 md:text-sm">{label}</p>
    </div>
  );
}
