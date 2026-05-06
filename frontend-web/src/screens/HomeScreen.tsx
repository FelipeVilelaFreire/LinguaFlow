import { ArrowRight, BookOpen, CalendarDays, Flame, Plus } from "lucide-react";

import ProgressBar from "../components/ui/ProgressBar";
import StateMessage from "../components/ui/StateMessage";
import { useLocale, useStrings } from "../contexts/StringsContext";
import { useAsyncData } from "../hooks/useAsyncData";
import { contentService } from "../services/contentService";

interface HomeScreenProps {
  hasActiveGoal: boolean;
  onCreateArea: () => void;
  onStartToday: () => void;
}

export default function HomeScreen({ hasActiveGoal, onCreateArea, onStartToday }: HomeScreenProps) {
  const s = useStrings();
  const locale = useLocale();
  const goal = useAsyncData(contentService.getCurrentGoal);

  if (!hasActiveGoal) {
    return (
      <div className="flex min-h-[60vh] flex-col items-center justify-center px-4 pb-20 text-center md:pb-0">
        <div className="grid h-16 w-16 place-items-center rounded-full text-white" style={{ background: "var(--area-primary)" }}>
          <BookOpen size={26} />
        </div>
        <h2 className="mt-6 text-2xl font-bold text-slate-950">{s.home.noActiveArea}</h2>
        <p className="mt-3 max-w-xs text-sm font-medium leading-6 text-slate-500">{s.home.noActiveAreaDetail}</p>
        <button
          type="button"
          onClick={onCreateArea}
          className="mt-7 inline-flex h-12 items-center gap-2 rounded-xl px-6 font-semibold text-white transition hover:brightness-95"
          style={{ background: "var(--area-primary)" }}
        >
          <Plus size={18} />
          {s.actions.createArea}
        </button>
      </div>
    );
  }

  if (goal.loading) return <StateMessage />;
  if (goal.error || !goal.data) return <StateMessage title={s.states.empty} detail={s.states.apiHint} />;

  const g = goal.data;
  const remaining = Math.max(g.duration_days - g.completed_lessons, 0);
  const targetCode = g.target_language?.code ?? "DE";
  const sourceCode = g.source_language?.code ?? "PT";
  const targetName = s.languages[targetCode as keyof typeof s.languages] ?? targetCode;
  const sourceName = s.languages[sourceCode as keyof typeof s.languages] ?? sourceCode;
  const hasRoutine = Boolean(g.study_weekdays?.length);

  const weekdayStr = g.study_weekdays?.length === 7
    ? s.profile.allDays
    : g.study_weekdays?.length === 0
      ? s.home.noRoutine
      : (g.study_weekdays ?? []).map((d) => s.weekdays.short[d]).join(", ");

  const routine = hasRoutine
    ? s.home.routine(weekdayStr, g.session_minutes ?? 30)
    : s.home.flexibleStudy;

  const nextStudyLabel = hasRoutine
    ? g.is_study_day_today
      ? s.home.studyToday
      : s.home.nextSession(formatDate(g.next_study_date, locale))
    : s.home.noFixedSchedule;

  return (
    <div className="pb-4 md:pb-0">

      {/* Hero */}
      <section className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
        <div className="flex items-center justify-between gap-3">
          <span className="rounded-full px-3 py-1 text-[11px] font-bold uppercase tracking-wider area-bg-soft">
            {targetCode} · {g.current_level} → {g.target_level}
          </span>
          <span className="text-xl font-bold tabular-nums area-text-primary">
            {g.progress_percent}%
          </span>
        </div>

        <h2 className="mt-4 text-3xl font-bold leading-tight text-slate-950">{targetName}</h2>
        <p className="mt-1 text-sm font-medium text-slate-400">
          {s.home.languagePath(sourceName, targetName, g.target_level)}
        </p>

        <div className="mt-5">
          <ProgressBar value={g.progress_percent} />
          <p className="mt-2 text-xs font-semibold text-slate-400">
            {g.learned_phrases.toLocaleString()} / {g.total_phrases.toLocaleString()} {s.home.phrasesLabel}
          </p>
        </div>

        <button
          type="button"
          onClick={onStartToday}
          className="mt-5 flex h-12 w-full items-center justify-center gap-2 rounded-xl font-semibold text-white transition hover:brightness-95 active:scale-[0.99]"
          style={{ background: "var(--area-primary)" }}
        >
          {s.actions.startToday}
          <ArrowRight size={18} />
        </button>
      </section>

      {/* Stats */}
      <div className="mt-3 grid grid-cols-3 gap-px overflow-hidden rounded-xl border border-slate-200 bg-slate-200">
        <StatCell value={g.streak_days} label={s.home.streak} icon={<Flame size={13} className="area-text-primary" />} />
        <StatCell value={g.completed_lessons} label={s.home.lessons} icon={<BookOpen size={13} className="text-sky-500" />} />
        <StatCell value={remaining} label={s.home.remaining} icon={<CalendarDays size={13} className="text-violet-500" />} />
      </div>

      {/* Agenda + Meta */}
      <div className="mt-3 divide-y divide-slate-100 overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
        <div className="px-4 py-4">
          <p className="text-[10px] font-bold uppercase tracking-widest text-slate-400">{s.home.nextLesson}</p>
          <p className="mt-1.5 text-sm font-semibold text-slate-800">{routine}</p>
          <p className="mt-0.5 text-sm font-bold area-text-primary">{nextStudyLabel}</p>
        </div>
        <div className="px-4 py-4">
          <p className="text-[10px] font-bold uppercase tracking-widest text-slate-400">{s.home.goalLabel}</p>
          <p className="mt-1.5 text-sm font-semibold text-slate-800">
            {s.home.languagePath(sourceName, targetName, g.target_level)}
          </p>
          <p className="mt-0.5 text-sm font-medium text-slate-400">
            {g.duration_days} {s.home.daysLabel} · {remaining} {s.home.remaining}
          </p>
        </div>
      </div>

    </div>
  );
}

function StatCell({ value, label, icon }: { value: number; label: string; icon: React.ReactNode }) {
  return (
    <div className="bg-white px-3 py-4">
      <p className="text-2xl font-bold tabular-nums text-slate-950">{value}</p>
      <div className="mt-1.5 flex items-center gap-1.5">
        {icon}
        <p className="text-[11px] font-bold leading-tight text-slate-500">{label}</p>
      </div>
    </div>
  );
}

function formatDate(value: string | null, locale: "pt" | "en") {
  if (!value) return "";
  return new Intl.DateTimeFormat(locale === "pt" ? "pt-BR" : "en-US", {
    weekday: "long",
    day: "2-digit",
    month: "2-digit",
  }).format(new Date(`${value}T12:00:00`));
}
