import { ArrowLeft, CalendarDays, ChevronLeft, ChevronRight } from "lucide-react";
import { useMemo, useState } from "react";

import StateMessage from "../components/ui/StateMessage";
import { useLocale } from "../contexts/StringsContext";
import { useAsyncData } from "../hooks/useAsyncData";
import { contentService } from "../services/contentService";
import { getStudyAreaTheme } from "../theme/studyAreaTheme";
import type { Goal, HistoryDay } from "../types/content";

const COMPLETED_COLOR = "#16a34a";

interface HistoryScreenProps {
  onBack: () => void;
}

export default function HistoryScreen({ onBack }: HistoryScreenProps) {
  const locale = useLocale();
  const [viewMode, setViewMode] = useState<"all" | "areas">("all");
  const [cursor, setCursor] = useState(() => {
    const today = new Date();
    return { year: today.getFullYear(), month: today.getMonth() + 1 };
  });
  const history = useAsyncData(() => contentService.getHistory(cursor.year, cursor.month), [cursor.year, cursor.month]);

  const monthLabel = useMemo(() => {
    return new Intl.DateTimeFormat(locale === "pt" ? "pt-BR" : "en-US", { month: "long", year: "numeric" }).format(new Date(cursor.year, cursor.month - 1, 1));
  }, [cursor, locale]);

  function moveMonth(delta: number) {
    const next = new Date(cursor.year, cursor.month - 1 + delta, 1);
    setCursor({ year: next.getFullYear(), month: next.getMonth() + 1 });
  }

  if (history.loading) return <StateMessage />;
  if (history.error || !history.data) {
    return <StateMessage title={locale === "pt" ? "Historico indisponivel." : "History unavailable."} detail={locale === "pt" ? "Confira se o backend esta rodando." : "Check if the backend is running."} />;
  }

  const summary = getMonthSummary(history.data.goals);

  return (
    <div className="pb-4 md:pb-0">

      {/* Back */}
      <button type="button" onClick={onBack} className="mb-4 flex items-center gap-2 text-sm font-semibold text-slate-500 transition hover:text-slate-800">
        <ArrowLeft size={16} />
        {locale === "pt" ? "Voltar ao perfil" : "Back to profile"}
      </button>

      <section className="rounded-[8px] bg-white p-4 shadow-sm ring-1 ring-slate-200 md:p-6">
        <p className="flex items-center gap-2 text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>
          <CalendarDays size={18} />
          {locale === "pt" ? "Agenda mensal" : "Monthly calendar"}
        </p>
        <div className="mt-3 flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
          <div>
            <div className="flex flex-wrap items-center gap-2">
              <h2 className="text-2xl font-semibold capitalize leading-tight md:text-4xl">{monthLabel}</h2>
              <button type="button" onClick={() => setCursor({ year: new Date().getFullYear(), month: new Date().getMonth() + 1 })} className="h-9 rounded-[8px] bg-slate-50 px-3 text-xs font-semibold ring-1 ring-slate-200 transition hover:bg-slate-100 md:h-10 md:text-sm">
                {locale === "pt" ? "Mes atual" : "Current month"}
              </button>
            </div>
            <p className="mt-2 max-w-2xl font-medium text-slate-600">
              {locale === "pt" ? "Veja seus dias planejados e concluidos por area de estudo." : "Review planned and completed days by study area."}
            </p>
          </div>
          <div className="flex flex-wrap gap-2">
            <button type="button" onClick={() => moveMonth(-1)} className="grid h-11 w-11 place-items-center rounded-[8px] bg-white ring-1 ring-slate-200 transition hover:bg-slate-50">
              <ChevronLeft size={19} />
            </button>
            <button type="button" onClick={() => moveMonth(1)} className="grid h-11 w-11 place-items-center rounded-[8px] bg-white ring-1 ring-slate-200 transition hover:bg-slate-50">
              <ChevronRight size={19} />
            </button>
          </div>
        </div>

        <div className="mt-4 grid grid-cols-3 gap-2 md:mt-5 md:gap-3">
          <CompactStat label={locale === "pt" ? "Maior streak" : "Best streak"} value={summary.bestStreak} />
          <CompactStat label={locale === "pt" ? "Dias estudados" : "Study days"} value={summary.completedDays} />
          <CompactStat label={locale === "pt" ? "Sessoes" : "Sessions"} value={summary.sessions} />
        </div>
      </section>

      <div className="mt-5 rounded-[8px] bg-white p-2 shadow-sm ring-1 ring-slate-200">
        <div className="grid grid-cols-2 gap-2">
          <button type="button" onClick={() => setViewMode("all")} className={`h-11 rounded-[8px] text-sm font-semibold transition ${viewMode === "all" ? "text-white" : "text-slate-600 hover:bg-slate-50"}`} style={viewMode === "all" ? { background: "var(--area-primary)" } : undefined}>
            {locale === "pt" ? "Tudo" : "All"}
          </button>
          <button type="button" onClick={() => setViewMode("areas")} className={`h-11 rounded-[8px] text-sm font-semibold transition ${viewMode === "areas" ? "text-white" : "text-slate-600 hover:bg-slate-50"}`} style={viewMode === "areas" ? { background: "var(--area-primary)" } : undefined}>
            {locale === "pt" ? "Por area" : "By area"}
          </button>
        </div>
      </div>

      <div className="mt-4 grid gap-4 md:mt-5 md:gap-5">
        {viewMode === "all" ? (
          <AllHistoryPanel goals={history.data.goals} locale={locale} />
        ) : (
          history.data.goals.map((entry) => (
            <GoalHistoryPanel key={entry.goal.id} goal={entry.goal} days={entry.days} locale={locale} />
          ))
        )}
      </div>
    </div>
  );
}

function AllHistoryPanel({ goals, locale }: { goals: Array<{ goal: Goal; days: HistoryDay[] }>; locale: "pt" | "en" }) {
  const days = mergeGoalDays(goals);
  const completedDays = days.filter((day) => day.completed).length;
  const plannedDays = days.filter((day) => day.planned).length;
  const bestStreak = getBestStreak(days);

  return (
    <section className="rounded-[8px] bg-white p-4 shadow-sm ring-1 ring-slate-200 md:p-5">
      <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
        <div>
          <p className="text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{locale === "pt" ? "Todas as areas" : "All areas"}</p>
          <h3 className="mt-1 text-2xl font-semibold">{locale === "pt" ? "Agenda geral" : "Overall calendar"}</h3>
          <p className="mt-1 text-sm font-bold text-slate-500">
            {locale === "pt" ? `${completedDays} dias concluidos | ${plannedDays} dias planejados` : `${completedDays} completed days | ${plannedDays} planned days`}
          </p>
        </div>
        <span className="rounded-full px-3 py-1 text-sm font-semibold" style={{ background: "#dcfce7", color: "#166534" }}>
          {locale === "pt" ? `${bestStreak} dias de streak` : `${bestStreak} day streak`}
        </span>
      </div>

      <div className="mt-5 flex flex-wrap gap-3 text-sm font-semibold text-slate-500">
        <Legend color={COMPLETED_COLOR} label={locale === "pt" ? "Concluido" : "Completed"} />
        <Legend color="#e2e8f0" label={locale === "pt" ? "Planejado" : "Planned"} textColor="text-slate-600" />
        <Legend color="#ffffff" label={locale === "pt" ? "Livre" : "Open"} textColor="text-slate-600" />
      </div>

      <div className="mt-5 grid grid-cols-7 gap-1.5 md:gap-2">
        {getWeekdays(locale).map((day) => (
          <p key={day} className="text-center text-xs font-bold uppercase text-slate-400">{day}</p>
        ))}
        {getLeadingBlanks(days).map((item) => (
          <div key={`blank-${item}`} className="aspect-square rounded-[8px]" />
        ))}
        {days.map((day) => (
          <HistoryCell key={day.date} day={day} locale={locale} softColor="#e2e8f0" />
        ))}
      </div>
    </section>
  );
}

function GoalHistoryPanel({ goal, days, locale }: { goal: Goal; days: HistoryDay[]; locale: "pt" | "en" }) {
  const theme = getStudyAreaTheme(goal);
  const completedDays = days.filter((day) => day.completed).length;
  const plannedDays = days.filter((day) => day.planned).length;
  const bestStreak = getBestStreak(days);

  return (
    <section className="rounded-[8px] bg-white p-4 shadow-sm ring-1 ring-slate-200 md:p-5">
      <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
        <div>
          <p className="text-sm font-semibold uppercase" style={{ color: theme.primary }}>{locale === "pt" ? "Area" : "Area"}</p>
          <h3 className="mt-1 text-2xl font-semibold">{formatGoal(goal, locale)}</h3>
          <p className="mt-1 text-sm font-bold text-slate-500">
            {locale === "pt" ? `${completedDays} dias concluidos | ${plannedDays} dias planejados` : `${completedDays} completed days | ${plannedDays} planned days`}
          </p>
        </div>
        <div className="flex flex-wrap gap-2">
          <span className="rounded-full px-3 py-1 text-sm font-semibold" style={{ background: "#dcfce7", color: "#166534" }}>
            {locale === "pt" ? `${bestStreak} dias de streak` : `${bestStreak} day streak`}
          </span>
          {goal.is_active ? (
            <span className="rounded-full px-3 py-1 text-sm font-semibold" style={{ background: theme.primarySoft, color: theme.primaryDark }}>
              {locale === "pt" ? "Ativa" : "Active"}
            </span>
          ) : null}
        </div>
      </div>

      <div className="mt-5 flex flex-wrap gap-3 text-sm font-semibold text-slate-500">
        <Legend color={COMPLETED_COLOR} label={locale === "pt" ? "Concluido" : "Completed"} />
        <Legend color={theme.primarySoft} label={locale === "pt" ? "Planejado" : "Planned"} textColor="text-slate-600" />
        <Legend color="#ffffff" label={locale === "pt" ? "Livre" : "Open"} textColor="text-slate-600" />
      </div>

      <div className="mt-5 grid grid-cols-7 gap-1.5 md:gap-2">
        {getWeekdays(locale).map((day) => (
          <p key={day} className="text-center text-xs font-bold uppercase text-slate-400">{day}</p>
        ))}
        {getLeadingBlanks(days).map((item) => (
          <div key={`blank-${item}`} className="aspect-square rounded-[8px]" />
        ))}
        {days.map((day) => (
          <HistoryCell key={day.date} day={day} locale={locale} softColor={theme.primarySoft} />
        ))}
      </div>
    </section>
  );
}

function CompactStat({ label, value }: { label: string; value: number }) {
  return (
    <div className="min-w-0 rounded-[8px] bg-slate-50 p-2.5 ring-1 ring-slate-200 md:p-3">
      <p className="break-words text-[10px] font-semibold uppercase leading-tight text-slate-500 md:text-xs">{label}</p>
      <p className="mt-1 text-xl font-semibold text-slate-950 md:text-2xl">{value}</p>
    </div>
  );
}

function Legend({ color, label, textColor = "text-slate-500" }: { color: string; label: string; textColor?: string }) {
  return (
    <span className={`inline-flex items-center gap-2 ${textColor}`}>
      <span className="h-3 w-3 rounded-full ring-1 ring-slate-200" style={{ background: color }} />
      {label}
    </span>
  );
}

function HistoryCell({ day, locale, softColor }: { day: HistoryDay; locale: "pt" | "en"; softColor: string }) {
  const date = new Date(`${day.date}T12:00:00`);
  const title = day.lessons.length
    ? day.lessons.map((lesson) => `${lesson.lesson_title} (${locale === "pt" ? "Dia" : "Day"} ${lesson.study_day})`).join("\n")
    : day.planned ? (locale === "pt" ? "Dia planejado" : "Planned day") : "";

  return (
    <div
      title={title}
      className={`aspect-square rounded-[8px] p-1.5 ring-1 transition md:p-2 ${day.completed ? "text-white shadow-sm" : day.planned ? "bg-slate-50 text-slate-700 ring-slate-200" : "bg-white text-slate-400 ring-slate-100"}`}
      style={day.completed ? { background: COMPLETED_COLOR, borderColor: COMPLETED_COLOR } : day.planned ? { background: softColor } : undefined}
    >
      <p className="text-xs font-semibold md:text-sm">{date.getDate()}</p>
      {day.completion_count ? <p className="mt-1 text-xs font-bold">{day.completion_count}x</p> : null}
    </div>
  );
}

function getLeadingBlanks(days: HistoryDay[]) {
  if (!days.length) return [];
  const first = new Date(`${days[0].date}T12:00:00`);
  const mondayFirstIndex = (first.getDay() + 6) % 7;
  return Array.from({ length: mondayFirstIndex }, (_, index) => index);
}

function getBestStreak(days: HistoryDay[]) {
  let current = 0;
  let best = 0;
  for (const day of days) {
    if (day.completed) {
      current += 1;
      best = Math.max(best, current);
    } else {
      current = 0;
    }
  }
  return best;
}

function getMonthSummary(goals: Array<{ days: HistoryDay[] }>) {
  const completedDateKeys = new Set<string>();
  let sessions = 0;
  let bestStreak = 0;
  for (const goal of goals) {
    sessions += goal.days.reduce((total, day) => total + day.completion_count, 0);
    bestStreak = Math.max(bestStreak, getBestStreak(goal.days));
    goal.days.forEach((day) => {
      if (day.completed) completedDateKeys.add(day.date);
    });
  }
  return { completedDays: completedDateKeys.size, sessions, bestStreak };
}

function mergeGoalDays(goals: Array<{ days: HistoryDay[] }>): HistoryDay[] {
  const byDate = new Map<string, HistoryDay>();
  for (const goal of goals) {
    for (const day of goal.days) {
      const existing = byDate.get(day.date);
      if (!existing) {
        byDate.set(day.date, { ...day, lessons: [...day.lessons] });
        continue;
      }
      existing.planned = existing.planned || day.planned;
      existing.completed = existing.completed || day.completed;
      existing.completion_count += day.completion_count;
      existing.lessons = [...existing.lessons, ...day.lessons];
    }
  }
  return Array.from(byDate.values()).sort((a, b) => a.date.localeCompare(b.date));
}

function getWeekdays(locale: "pt" | "en") {
  return locale === "pt" ? ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"] : ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
}

function formatGoal(goal: Goal, locale: "pt" | "en") {
  const names = locale === "pt"
    ? { PT: "Portugues", EN: "Ingles", DE: "Alemao", ES: "Espanhol" }
    : { PT: "Portuguese", EN: "English", DE: "German", ES: "Spanish" };
  const source = names[goal.source_language?.code as keyof typeof names] ?? goal.source_language?.code ?? "";
  const target = names[goal.target_language?.code as keyof typeof names] ?? goal.target_language?.code ?? "";
  return locale === "pt" ? `${source} para ${target} - ${goal.target_level}` : `${source} to ${target} - ${goal.target_level}`;
}
