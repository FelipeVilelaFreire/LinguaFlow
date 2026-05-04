import { ArrowRight, BookOpen, CalendarDays, Flame, Trophy } from "lucide-react";
import type { ReactNode } from "react";

import ProgressBar from "../components/ui/ProgressBar";
import StateMessage from "../components/ui/StateMessage";
import { useStrings } from "../contexts/StringsContext";
import { useAsyncData } from "../hooks/useAsyncData";
import { contentService } from "../services/contentService";

interface HomeScreenProps {
  onStartToday: () => void;
}

export default function HomeScreen({ onStartToday }: HomeScreenProps) {
  const strings = useStrings();
  const goal = useAsyncData(contentService.getCurrentGoal);

  if (goal.loading) return <StateMessage />;
  if (goal.error || !goal.data) return <StateMessage title={strings.states.empty} detail={strings.states.apiHint} />;

  const remaining = Math.max(goal.data.duration_days - goal.data.completed_lessons, 0);

  return (
    <div className="pb-20 md:pb-0">
      <section className="relative overflow-hidden rounded-[8px] bg-white p-6 shadow-sm ring-1 ring-slate-200 md:p-8">
        <div className="absolute right-6 top-6 hidden rounded-[8px] px-5 py-3 text-2xl font-semibold ring-1 md:block" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
          {goal.data.target_language?.code ?? "DE"} {goal.data.target_level}
        </div>
        <p className="text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{strings.home.eyebrow}</p>
        <h2 className="mt-2 max-w-2xl text-4xl font-semibold leading-tight text-slate-950 md:text-5xl">
          {strings.home.headline}
        </h2>
        <p className="mt-4 max-w-xl text-lg font-medium text-slate-600">
          {strings.home.subtitle}
        </p>
        <button type="button" onClick={onStartToday} className="mt-7 inline-flex h-12 items-center gap-2 rounded-[8px] px-5 font-semibold text-white shadow-sm transition hover:brightness-95" style={{ background: "var(--area-primary)" }}>
          {strings.actions.startToday}
          <ArrowRight size={19} />
        </button>
      </section>

      <section className="mt-6 rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
        <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
          <div>
            <p className="text-sm font-semibold uppercase text-slate-500">{strings.home.progress}</p>
            <p className="mt-1 text-4xl font-semibold">{goal.data.progress_percent}%</p>
          </div>
          <div className="w-full md:max-w-lg">
            <ProgressBar value={goal.data.progress_percent} />
          </div>
        </div>
      </section>

      <div className="mt-5 grid gap-4 md:grid-cols-3">
        <Stat icon={<Flame />} color="area" value={goal.data.streak_days} label={strings.home.streak} />
        <Stat icon={<BookOpen />} color="bg-sky-100 text-sky-700" value={goal.data.completed_lessons} label={strings.home.lessons} />
        <Stat icon={<CalendarDays />} color="bg-violet-100 text-violet-700" value={remaining} label={strings.home.remaining} />
      </div>

      <section className="mt-5 grid gap-4 lg:grid-cols-[1fr_0.9fr]">
        <div className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
          <Trophy />
          <h3 className="mt-3 text-2xl font-semibold">{strings.home.recommendedPace}</h3>
          <p className="mt-2 font-semibold text-slate-600">{strings.home.recommendedDetail}</p>
        </div>
        <div className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
          <p className="text-sm font-semibold uppercase text-slate-500">{strings.home.activeGoal}</p>
          <p className="mt-2 text-2xl font-semibold">
            {`${goal.data.source_language?.code ?? "PT"} -> ${goal.data.target_language?.code ?? "DE"} em ${goal.data.duration_days} dias`}
          </p>
          <p className="mt-2 font-semibold text-slate-600">{strings.home.learned(goal.data.learned_phrases, goal.data.total_phrases)}</p>
        </div>
      </section>
    </div>
  );
}

function Stat({ icon, color, value, label }: { icon: ReactNode; color: string; value: number; label: string }) {
  return (
    <div className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
      <div className={`grid h-11 w-11 place-items-center rounded-[8px] ${color === "area" ? "" : color}`} style={color === "area" ? { background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" } : undefined}>{icon}</div>
      <p className="mt-4 text-3xl font-semibold">{value}</p>
      <p className="mt-1 text-sm font-bold text-slate-500">{label}</p>
    </div>
  );
}
