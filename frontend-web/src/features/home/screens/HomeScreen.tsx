import { ArrowRight, BookOpen, CalendarDays, Flame, Plus, Sparkles, Sword } from "lucide-react";

import LangFlag from "../../../components/ui/LangFlag";
import ProgressBar from "../../../components/ui/ProgressBar";
import StateMessage from "../../../components/ui/StateMessage";
import { useLocale, useStrings } from "../../../contexts/StringsContext";
import { useAsyncData } from "../../../hooks/useAsyncData";
import { contentService } from "../../../services/contentService";

interface HomeScreenProps {
  hasActiveGoal: boolean;
  onContinueAdventure: () => void;
  onCreateArea: () => void;
  onStartToday: () => void;
}

export default function HomeScreen({ hasActiveGoal, onContinueAdventure, onCreateArea, onStartToday }: HomeScreenProps) {
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
        <button type="button" onClick={onCreateArea} className="area-btn mt-7 inline-flex h-12 items-center gap-2 rounded-[10px] px-6 font-semibold transition">
          <Plus size={18} />
          {s.actions.createArea}
        </button>
      </div>
    );
  }

  if (goal.loading) return <StateMessage />;
  if (goal.error || !goal.data) return <StateMessage title={s.states.empty} detail={s.states.apiHint} />;

  const g = goal.data;
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

  const routine = hasRoutine ? s.home.routine(weekdayStr, g.session_minutes ?? 30) : s.home.flexibleStudy;

  const nextStudyLabel = hasRoutine
    ? g.is_study_day_today ? s.home.studyToday : s.home.nextSession(formatDate(g.next_study_date, locale))
    : s.home.noFixedSchedule;

  return (
    <div className="flex flex-col gap-3 pb-4 md:pb-0" style={{ animation: "fadeIn 260ms ease-out" }}>

      {/* Começar o dia */}
      {g.is_study_day_today && (
        <div className="home-study-banner">
          <div>
            <p className="text-[11px] font-bold uppercase tracking-widest opacity-75">{s.home.studyToday}</p>
            <p className="mt-0.5 text-base font-bold">{s.home.studyDaySubtitle(targetName, formatMinutes(g.session_minutes ?? 30))}</p>
          </div>
          <button type="button" onClick={onStartToday} className="home-study-banner-btn">
            {s.home.startDay}
            <ArrowRight size={15} />
          </button>
        </div>
      )}

      {/* Hero */}
      <section
        className="card p-5 transition-all"
        style={g.is_study_day_today ? { boxShadow: "0 0 0 1.5px var(--area-primary), 0 2px 12px rgba(15,23,42,0.08)" } : undefined}
      >
        <div className="flex items-center justify-between gap-3">
          <span className="area-bg-soft rounded-full px-3 py-1 text-[11px] font-bold uppercase tracking-wider">
            {targetCode} · {g.current_level} → {g.target_level}
          </span>
          <span className="display-num area-text-primary text-xl">{g.progress_percent}%</span>
        </div>

        <div className="mt-4 flex items-center gap-3">
          <LangFlag code={targetCode} size="md" />
          <h2 className="text-3xl font-bold leading-tight text-slate-950">{targetName}</h2>
        </div>
        <p className="mt-1 text-sm font-medium text-slate-400">{s.home.languagePath(sourceName, targetName, g.target_level)}</p>

        <p className="mt-2 flex items-center gap-1.5 text-xs font-semibold text-slate-400">
          <Sword size={12} className="shrink-0" />
          {s.home.adventurePosition(
            g.current_level,
            s.adventureSeries[g.current_level as keyof typeof s.adventureSeries] ?? g.current_level,
            2, 3
          )}
        </p>

        <div className="mt-4">
          <ProgressBar value={g.progress_percent} />
          <p className="mt-2 text-xs font-semibold text-slate-400">
            {g.learned_phrases.toLocaleString()} / {g.total_phrases.toLocaleString()} {s.home.phrasesLabel}
          </p>
        </div>

        {!g.is_study_day_today && (
          <button type="button" onClick={onContinueAdventure} className="area-btn mt-4 flex h-12 w-full items-center justify-center gap-2 rounded-[10px] font-semibold transition active:scale-[0.99]">
            {s.home.continueAdventure}
            <ArrowRight size={18} />
          </button>
        )}
      </section>

      {/* Stats */}
      <div className="grid grid-cols-3 gap-px overflow-hidden rounded-[12px] bg-slate-100">
        <StatCell value={g.streak_days} label={s.home.statStreak} icon={<Flame size={13} className="text-orange-400" />} />
        <StatCell value={g.learned_phrases} label={s.home.statWords} icon={<BookOpen size={13} className="text-sky-500" />} />
        <StatCell value={g.target_level} label={s.home.statLevel} icon={<Sparkles size={13} />} highlight />
      </div>

      {/* Próxima sessão */}
      {!g.is_study_day_today && (
        <section className="card p-4">
          <div className="flex items-center gap-2">
            <CalendarDays size={14} className="shrink-0 text-slate-400" />
            <p className="text-[10px] font-bold uppercase tracking-widest text-slate-400">{s.home.nextSessionTitle}</p>
          </div>
          <p className="mt-2 text-sm font-bold area-text-primary">{nextStudyLabel}</p>
          <p className="mt-0.5 text-xs font-medium text-slate-400">{routine}</p>
        </section>
      )}

    </div>
  );
}

function StatCell({ value, label, icon, highlight }: { value: number | string; label: string; icon: React.ReactNode; highlight?: boolean }) {
  return (
    <div className="bg-white px-3 py-4">
      <div className="flex items-center gap-1.5">
        <p className={`display-num text-2xl leading-none ${highlight ? "area-text-primary" : "text-slate-950"}`}>{value}</p>
        {icon}
      </div>
      <p className="mt-1.5 text-[11px] font-bold leading-tight text-slate-500">{label}</p>
    </div>
  );
}

function formatDate(value: string | null, locale: "pt" | "en") {
  if (!value) return "";
  return new Intl.DateTimeFormat(locale === "pt" ? "pt-BR" : "en-US", { weekday: "long", day: "2-digit", month: "2-digit" }).format(new Date(`${value}T12:00:00`));
}

function formatMinutes(min: number) {
  if (min === 60) return "1h";
  if (min === 90) return "1h30";
  return `${min} min`;
}
