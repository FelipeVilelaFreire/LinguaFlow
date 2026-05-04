import { CheckCircle2, Sparkles } from "lucide-react";

import LessonCard from "../components/learning/LessonCard";
import VideoCard from "../components/learning/VideoCard";
import ProgressBar from "../components/ui/ProgressBar";
import StateMessage from "../components/ui/StateMessage";
import { useStrings } from "../contexts/StringsContext";
import { useTodayStudy } from "../hooks/useTodayStudy";

interface TodayScreenProps {
  onCompleted: () => void;
}

export default function TodayScreen({ onCompleted }: TodayScreenProps) {
  const strings = useStrings();
  const study = useTodayStudy(onCompleted);
  const today = study.today.data;

  if (study.today.loading) return <StateMessage />;
  if (study.today.error || !today || !study.currentPhrase) {
    return (
      <StateMessage
        title={strings.today.noLessonsTitle}
        detail={strings.today.noLessonsDetail}
      />
    );
  }

  if (study.completed) {
    return (
      <section className="rounded-[8px] bg-white p-8 text-center shadow-sm ring-1 ring-slate-200">
        <div className="mx-auto grid h-16 w-16 place-items-center rounded-full bg-white text-emerald-600">
          <CheckCircle2 size={34} />
        </div>
        <p className="mt-5 text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{strings.today.completed}</p>
        <h2 className="mt-2 text-4xl font-semibold text-slate-950">{today.lesson.title}</h2>
        <p className="mx-auto mt-3 max-w-xl font-medium text-slate-600">{strings.today.completedDetail}</p>
      </section>
    );
  }

  return (
    <div className="pb-20 md:pb-0">
      <header className="mb-6 rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
        <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
          <div>
            <p className="inline-flex items-center gap-2 rounded-full px-3 py-1 text-sm font-semibold ring-1" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
              <Sparkles size={16} />
              {strings.today.session}
            </p>
            <h2 className="mt-3 text-3xl font-semibold md:text-5xl">
              {strings.today.titlePrefix} {String(today.day_number).padStart(2, "0")} - {today.lesson.title}
            </h2>
          </div>
          <div className="text-left md:text-right">
            <p className="text-sm font-semibold uppercase text-slate-500">{study.progress}% {strings.layout.completed}</p>
            <p className="font-medium text-slate-500">{today.lesson.scenario.title}</p>
          </div>
        </div>
        <div className="mt-5">
          <ProgressBar value={study.progress} />
        </div>
      </header>

      <div className="grid gap-5 lg:grid-cols-[1fr_320px]">
        <LessonCard
          answer={study.answer}
          checked={study.checked}
          isCorrect={study.isCorrect}
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
          <aside className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
            <p className="text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{strings.today.practice}</p>
            <p className="mt-2 text-2xl font-semibold">{strings.today.practice}</p>
            <p className="mt-2 text-sm font-medium text-slate-600">{strings.today.tryAgain}</p>
          </aside>
        </div>
      </div>
    </div>
  );
}
