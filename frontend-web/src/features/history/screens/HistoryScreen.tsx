import { ArrowLeft, ChevronLeft, ChevronRight } from "lucide-react";
import { useMemo, useState } from "react";

import StateMessage from "../../../components/ui/StateMessage";
import { useLocale } from "../../../contexts/StringsContext";
import { useAsyncData } from "../../../hooks/useAsyncData";
import { contentService } from "../../../services/contentService";
import { getStudyAreaTheme } from "../../../theme/studyAreaTheme";
import type { Goal, HistoryDay } from "../../../types/content";

const COMPLETED_COLOR = "#16a34a";
const TODAY = new Date().toISOString().split("T")[0];

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
  const history = useAsyncData(
    () => contentService.getHistory(cursor.year, cursor.month),
    [cursor.year, cursor.month]
  );

  const monthLabel = useMemo(() => {
    return new Intl.DateTimeFormat(locale === "pt" ? "pt-BR" : "en-US", {
      month: "long",
      year: "numeric",
    }).format(new Date(cursor.year, cursor.month - 1, 1));
  }, [cursor, locale]);

  function moveMonth(delta: number) {
    const next = new Date(cursor.year, cursor.month - 1 + delta, 1);
    setCursor({ year: next.getFullYear(), month: next.getMonth() + 1 });
  }

  if (history.loading) return (
    <div className="history-shell">
      <StateMessage />
    </div>
  );

  if (history.error || !history.data) return (
    <div className="history-shell">
      <StateMessage
        title={locale === "pt" ? "Historico indisponivel." : "History unavailable."}
        detail={locale === "pt" ? "Confira se o backend esta rodando." : "Check if the backend is running."}
      />
    </div>
  );

  const summary = getMonthSummary(history.data.goals);

  return (
    <div className="history-shell" style={{ animation: "fadeIn 220ms ease-out" }}>

      {/* Top bar */}
      <div className="history-topbar">
        <button type="button" onClick={onBack} className="history-back-btn">
          <ArrowLeft size={18} />
        </button>
        <h1 className="history-title">
          {locale === "pt" ? "Histórico" : "History"}
        </h1>
        <div className="w-9" />
      </div>

      <div className="history-content">

        {/* Month navigation */}
        <div className="history-month-nav">
          <button type="button" onClick={() => moveMonth(-1)} className="history-month-btn">
            <ChevronLeft size={18} />
          </button>
          <span className="history-month-label capitalize">{monthLabel}</span>
          <button type="button" onClick={() => moveMonth(1)} className="history-month-btn">
            <ChevronRight size={18} />
          </button>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-2">
          <StatPill
            value={summary.bestStreak}
            label={locale === "pt" ? "Melhor streak" : "Best streak"}
          />
          <StatPill
            value={summary.completedDays}
            label={locale === "pt" ? "Dias" : "Days"}
          />
          <StatPill
            value={summary.sessions}
            label={locale === "pt" ? "Sessões" : "Sessions"}
          />
        </div>

        {/* View toggle */}
        <div className="grid grid-cols-2 gap-1 rounded-[8px] bg-slate-100 p-1">
          <button
            type="button"
            onClick={() => setViewMode("all")}
            className={`h-10 rounded-[6px] text-sm font-semibold transition ${viewMode === "all" ? "bg-white text-slate-950 shadow-sm" : "text-slate-500"}`}
          >
            {locale === "pt" ? "Tudo" : "All"}
          </button>
          <button
            type="button"
            onClick={() => setViewMode("areas")}
            className={`h-10 rounded-[6px] text-sm font-semibold transition ${viewMode === "areas" ? "bg-white text-slate-950 shadow-sm" : "text-slate-500"}`}
          >
            {locale === "pt" ? "Por área" : "By area"}
          </button>
        </div>

        {/* Calendars */}
        {viewMode === "all" ? (
          <AllHistoryPanel
            goals={history.data.goals}
            locale={locale}
            year={cursor.year}
            month={cursor.month}
          />
        ) : (
          history.data.goals.map((entry) => (
            <GoalHistoryPanel
              key={entry.goal.id}
              goal={entry.goal}
              days={entry.days}
              locale={locale}
              year={cursor.year}
              month={cursor.month}
            />
          ))
        )}

      </div>
    </div>
  );
}

// ── Sub-components ────────────────────────────────────────

function StatPill({ value, label }: { value: number; label: string }) {
  return (
    <div className="card p-3 text-center">
      <p className="display-num text-2xl text-slate-950">{value}</p>
      <p className="mt-0.5 text-[10px] font-semibold uppercase tracking-wide text-slate-400">{label}</p>
    </div>
  );
}

function AllHistoryPanel({ goals, locale, year, month }: {
  goals: Array<{ goal: Goal; days: HistoryDay[] }>;
  locale: "pt" | "en";
  year: number;
  month: number;
}) {
  const dayMap = useMemo(() => mergeGoalDays(goals), [goals]);

  return (
    <section className="card p-4">
      <div className="mb-4 flex flex-wrap gap-3 text-xs font-semibold text-slate-500">
        <Legend color={COMPLETED_COLOR} label={locale === "pt" ? "Concluído" : "Completed"} />
        <Legend color="#e2e8f0" label={locale === "pt" ? "Planejado" : "Planned"} />
        <Legend color="transparent" label={locale === "pt" ? "Livre" : "Open"} border />
      </div>
      <CalendarGrid dayMap={dayMap} softColor="#cbd5e1" locale={locale} year={year} month={month} />
    </section>
  );
}

function GoalHistoryPanel({ goal, days, locale, year, month }: {
  goal: Goal;
  days: HistoryDay[];
  locale: "pt" | "en";
  year: number;
  month: number;
}) {
  const theme = getStudyAreaTheme(goal);
  const dayMap = useMemo(() => new Map(days.map((d) => [d.date, d])), [days]);

  return (
    <section className="card p-4">
      <div className="mb-3 flex items-center justify-between gap-3">
        <p className="text-sm font-bold text-slate-950">{formatGoal(goal, locale)}</p>
        {goal.is_active && (
          <span className="rounded-full px-2.5 py-0.5 text-xs font-semibold" style={{ background: theme.primarySoft, color: theme.primaryDark }}>
            {locale === "pt" ? "Ativa" : "Active"}
          </span>
        )}
      </div>
      <div className="mb-4 flex flex-wrap gap-3 text-xs font-semibold text-slate-500">
        <Legend color={COMPLETED_COLOR} label={locale === "pt" ? "Concluído" : "Completed"} />
        <Legend color={theme.primarySoft} label={locale === "pt" ? "Planejado" : "Planned"} />
        <Legend color="transparent" label={locale === "pt" ? "Livre" : "Open"} border />
      </div>
      <CalendarGrid dayMap={dayMap} softColor={theme.primarySoft} locale={locale} year={year} month={month} />
    </section>
  );
}

// ── Calendar ──────────────────────────────────────────────

function CalendarGrid({ dayMap, softColor, locale, year, month }: {
  dayMap: Map<string, HistoryDay>;
  softColor: string;
  locale: "pt" | "en";
  year: number;
  month: number;
}) {
  const weekdays = locale === "pt"
    ? ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
    : ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

  const daysInMonth = new Date(year, month, 0).getDate();
  const firstDayJs = new Date(year, month - 1, 1).getDay(); // 0=Sun
  const leadingBlanks = (firstDayJs + 6) % 7; // Mon=0

  return (
    <div className="grid grid-cols-7 gap-1">
      {weekdays.map((d) => (
        <p key={d} className="pb-1 text-center text-[10px] font-bold uppercase text-slate-400">{d}</p>
      ))}
      {Array.from({ length: leadingBlanks }, (_, i) => (
        <div key={`blank-${i}`} className="aspect-square" />
      ))}
      {Array.from({ length: daysInMonth }, (_, i) => {
        const day = i + 1;
        const dateStr = `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
        const data = dayMap.get(dateStr);
        return (
          <HistoryCell
            key={dateStr}
            dateStr={dateStr}
            dayNum={day}
            data={data}
            softColor={softColor}
          />
        );
      })}
    </div>
  );
}

function HistoryCell({ dateStr, dayNum, data, softColor }: {
  dateStr: string;
  dayNum: number;
  data: HistoryDay | undefined;
  softColor: string;
}) {
  const isToday = dateStr === TODAY;
  const completed = data?.completed ?? false;
  const planned = data?.planned ?? false;
  const count = data?.completion_count ?? 0;

  let bgStyle: React.CSSProperties | undefined;
  let cellClass = "aspect-square rounded-[8px] flex flex-col items-center justify-center transition-all ";

  if (completed) {
    bgStyle = { background: COMPLETED_COLOR };
    cellClass += "text-white";
  } else if (planned) {
    bgStyle = { background: softColor };
    cellClass += "text-slate-700";
  } else if (isToday) {
    cellClass += "ring-2 text-slate-950 font-bold";
    bgStyle = { boxShadow: "inset 0 0 0 2px var(--area-primary)" };
  } else {
    cellClass += "text-slate-300";
  }

  return (
    <div className={cellClass} style={bgStyle}>
      <p className="text-xs font-semibold leading-none">{dayNum}</p>
      {completed && count > 1 && (
        <p className="mt-0.5 text-[8px] font-bold opacity-75">{count}×</p>
      )}
    </div>
  );
}

function Legend({ color, label, border }: { color: string; label: string; border?: boolean }) {
  return (
    <span className="inline-flex items-center gap-1.5">
      <span
        className="h-2.5 w-2.5 rounded-full"
        style={{
          background: color,
          boxShadow: border ? "inset 0 0 0 1.5px #cbd5e1" : undefined,
        }}
      />
      {label}
    </span>
  );
}

// ── Data helpers ──────────────────────────────────────────

function getBestStreak(dayMap: Map<string, HistoryDay>, year: number, month: number) {
  const daysInMonth = new Date(year, month, 0).getDate();
  let current = 0;
  let best = 0;
  for (let i = 1; i <= daysInMonth; i++) {
    const dateStr = `${year}-${String(month).padStart(2, "0")}-${String(i).padStart(2, "0")}`;
    const d = dayMap.get(dateStr);
    current = d?.completed ? current + 1 : 0;
    best = Math.max(best, current);
  }
  return best;
}

function getMonthSummary(goals: Array<{ days: HistoryDay[] }>) {
  const completedDates = new Set<string>();
  let sessions = 0;
  let bestStreak = 0;
  for (const goal of goals) {
    sessions += goal.days.reduce((t, d) => t + d.completion_count, 0);
    const map = new Map(goal.days.map((d) => [d.date, d]));
    const cursor = new Date();
    const streak = getBestStreak(map, cursor.getFullYear(), cursor.getMonth() + 1);
    bestStreak = Math.max(bestStreak, streak);
    goal.days.forEach((d) => { if (d.completed) completedDates.add(d.date); });
  }
  return { completedDays: completedDates.size, sessions, bestStreak };
}

function mergeGoalDays(goals: Array<{ days: HistoryDay[] }>): Map<string, HistoryDay> {
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
  return byDate;
}

function formatGoal(goal: Goal, locale: "pt" | "en") {
  const names = locale === "pt"
    ? { PT: "Portugues", EN: "Ingles", DE: "Alemao", ES: "Espanhol" }
    : { PT: "Portuguese", EN: "English", DE: "German", ES: "Spanish" };
  const source = names[goal.source_language?.code as keyof typeof names] ?? goal.source_language?.code ?? "";
  const target = names[goal.target_language?.code as keyof typeof names] ?? goal.target_language?.code ?? "";
  return locale === "pt" ? `${source} para ${target} · ${goal.target_level}` : `${source} to ${target} · ${goal.target_level}`;
}
