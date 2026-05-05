import { ArrowRight, BookOpen, CalendarDays, CheckCircle2, Flame, Gauge, PlayCircle, Plus, Trophy } from "lucide-react";
import type { ReactNode } from "react";

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
  const strings = useStrings();
  const locale = useLocale();
  const goal = useAsyncData(contentService.getCurrentGoal);

  if (!hasActiveGoal) {
    return (
      <div className="pb-20 md:pb-0">
        <section className="rounded-[8px] bg-white p-6 shadow-sm ring-1 ring-slate-200 md:p-8">
          <div className="grid h-12 w-12 place-items-center rounded-[8px]" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
            <BookOpen size={23} />
          </div>
          <h2 className="mt-4 max-w-2xl text-4xl font-semibold leading-tight text-slate-950">
            {locale === "pt" ? "Nenhuma area de estudo ativa" : "No active study area"}
          </h2>
          <p className="mt-3 max-w-2xl text-lg font-medium leading-8 text-slate-600">
            {locale === "pt" ? "Sua conta esta vazia agora. Crie uma area quando quiser para comecar um plano de idiomas." : "Your account is empty right now. Create an area whenever you want to start a language plan."}
          </p>
          <button type="button" onClick={onCreateArea} className="mt-6 inline-flex h-12 items-center justify-center gap-2 rounded-[8px] px-5 font-semibold text-white shadow-sm transition hover:brightness-95" style={{ background: "var(--area-primary)" }}>
            <Plus size={18} />
            {strings.actions.createArea}
          </button>
        </section>
      </div>
    );
  }

  if (goal.loading) return <StateMessage />;
  if (goal.error || !goal.data) return <StateMessage title={strings.states.empty} detail={strings.states.apiHint} />;

  const remaining = Math.max(goal.data.duration_days - goal.data.completed_lessons, 0);
  const sourceLanguage = getLanguageName(goal.data.source_language?.code, locale);
  const targetLanguage = getLanguageName(goal.data.target_language?.code, locale);
  const targetCode = goal.data.target_language?.code ?? "DE";
  const hasRoutine = Boolean(goal.data.study_weekdays?.length);
  const routine = hasRoutine ? strings.home.routine(formatWeekdays(goal.data.study_weekdays ?? [], locale), goal.data.session_minutes ?? 30) : strings.home.flexibleStudy;
  const nextStudyLabel = hasRoutine
    ? goal.data.is_study_day_today ? strings.home.studyToday : strings.home.nextSession(formatDate(goal.data.next_study_date, locale))
    : strings.home.noFixedSchedule;
  const plannedSessionsPerWeek = goal.data.study_weekdays?.length || 1;
  const plannedWeeks = Math.max(1, Math.ceil(goal.data.duration_days / 7));
  const expectedSessions = plannedSessionsPerWeek * plannedWeeks;
  const pacePercent = Math.min(140, Math.round((goal.data.completed_lessons / Math.max(1, expectedSessions)) * 100));
  const paceLabel = pacePercent >= 100
    ? locale === "pt" ? "No ritmo ou adiantado" : "On pace or ahead"
    : locale === "pt" ? "Ajuste o ritmo esta semana" : "Adjust your pace this week";

  return (
    <div className="pb-20 md:pb-0">
      <section className="grid overflow-hidden rounded-[8px] bg-white shadow-sm ring-1 ring-slate-200 lg:grid-cols-[1fr_360px]">
        <div className="p-6 md:p-8">
          <div className="inline-flex items-center gap-2 rounded-full px-3 py-1 text-sm font-semibold ring-1" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
            <PlayCircle size={16} />
            {strings.home.eyebrow}
          </div>
          <h2 className="mt-4 max-w-2xl text-4xl font-semibold leading-tight text-slate-950 md:text-5xl">
            {strings.home.headline}
          </h2>
          <p className="mt-4 max-w-2xl text-lg font-medium leading-8 text-slate-600">
            {strings.home.subtitle}
          </p>

          <div className="mt-7 grid gap-3 sm:grid-cols-[auto_1fr] sm:items-center">
            <button type="button" onClick={onStartToday} className="inline-flex h-12 items-center justify-center gap-2 rounded-[8px] px-5 font-semibold text-white shadow-sm transition hover:brightness-95" style={{ background: "var(--area-primary)" }}>
              {strings.actions.startToday}
              <ArrowRight size={19} />
            </button>
            <p className="text-sm font-semibold text-slate-500">{strings.home.keepGoing}</p>
          </div>
        </div>

        <aside className="border-t border-slate-200 bg-slate-50 p-6 lg:border-l lg:border-t-0 md:p-8">
          <p className="text-sm font-semibold uppercase text-slate-500">{strings.home.progress}</p>
          <div className="mt-3 flex items-end justify-between gap-4">
            <p className="text-5xl font-semibold text-slate-950">{goal.data.progress_percent}%</p>
            <span className="rounded-[8px] px-3 py-2 text-sm font-bold" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
              {targetCode} {goal.data.target_level}
            </span>
          </div>
          <div className="mt-5">
            <ProgressBar value={goal.data.progress_percent} />
          </div>
          <div className="mt-6 rounded-[8px] bg-white p-4 ring-1 ring-slate-200">
            <p className="text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{strings.home.nextLesson}</p>
            <p className="mt-2 font-semibold text-slate-700">{routine}</p>
            <p className="mt-1 text-sm font-bold" style={{ color: "var(--area-primary)" }}>{nextStudyLabel}</p>
          </div>
        </aside>
      </section>

      <div className="mt-5 grid gap-4 md:grid-cols-3">
        <Stat icon={<Flame />} color="area" value={goal.data.streak_days} label={strings.home.streak} />
        <Stat icon={<BookOpen />} color="bg-sky-100 text-sky-700" value={goal.data.completed_lessons} label={strings.home.lessons} />
        <Stat icon={<CalendarDays />} color="bg-violet-100 text-violet-700" value={remaining} label={strings.home.remaining} />
      </div>

      <section className="mt-5 grid gap-4 lg:grid-cols-[1fr_0.9fr]">
        <div className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
          <div className="grid h-11 w-11 place-items-center rounded-[8px]" style={{ background: "var(--area-accent-soft)", color: "var(--area-primary-dark)" }}>
            <Trophy size={21} />
          </div>
          <h3 className="mt-3 text-2xl font-semibold">{strings.home.recommendedPace}</h3>
          <p className="mt-2 font-semibold text-slate-600">{strings.home.recommendedDetail}</p>
        </div>
        <div className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
          <div className="flex items-start gap-3">
            <div className="grid h-11 w-11 shrink-0 place-items-center rounded-[8px] bg-emerald-50 text-emerald-700">
              <CheckCircle2 size={21} />
            </div>
            <div>
              <p className="text-sm font-semibold uppercase text-slate-500">{strings.home.activeGoal}</p>
              <p className="mt-2 text-2xl font-semibold">
                {strings.home.languagePath(sourceLanguage, targetLanguage, goal.data.target_level)}
              </p>
              <p className="mt-1 text-sm font-bold" style={{ color: "var(--area-primary)" }}>{routine}</p>
            </div>
          </div>
          <p className="mt-2 font-semibold text-slate-600">{strings.home.learned(goal.data.learned_phrases, goal.data.total_phrases)}</p>
        </div>
      </section>

      <section className="mt-5 rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
        <div className="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
          <div>
            <p className="flex items-center gap-2 text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>
              <Gauge size={17} />
              {locale === "pt" ? "Rota da meta" : "Goal route"}
            </p>
            <h3 className="mt-2 text-2xl font-semibold">
              {locale === "pt" ? `Chegar em ${targetLanguage} ${goal.data.target_level} em ${goal.data.duration_days} dias` : `Reach ${targetLanguage} ${goal.data.target_level} in ${goal.data.duration_days} days`}
            </h3>
            <p className="mt-2 font-medium text-slate-500">
              {locale === "pt" ? `${plannedSessionsPerWeek} sessoes por semana, cerca de ${expectedSessions} sessoes planejadas.` : `${plannedSessionsPerWeek} sessions per week, about ${expectedSessions} planned sessions.`}
            </p>
          </div>
          <div className="rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-200 md:min-w-64">
            <div className="flex items-center justify-between gap-3">
              <p className="text-sm font-semibold uppercase text-slate-500">{locale === "pt" ? "Ritmo" : "Pace"}</p>
              <p className="font-bold" style={{ color: pacePercent >= 100 ? "var(--area-primary)" : "#b45309" }}>{paceLabel}</p>
            </div>
            <div className="mt-3 h-2 overflow-hidden rounded-full bg-slate-200">
              <div className="h-full rounded-full transition-all" style={{ width: `${Math.min(100, pacePercent)}%`, background: pacePercent >= 100 ? "var(--area-primary)" : "#f59e0b" }} />
            </div>
            <p className="mt-2 text-sm font-semibold text-slate-500">{Math.min(100, pacePercent)}% {locale === "pt" ? "do ritmo esperado" : "of expected pace"}</p>
          </div>
        </div>
      </section>
    </div>
  );
}

const WEEKDAY_LABELS: Record<"pt" | "en", string[]> = {
  pt: ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"],
  en: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
};

const LANGUAGE_NAMES: Record<"pt" | "en", Record<string, string>> = {
  pt: { PT: "Portugues", EN: "Ingles", DE: "Alemao", ES: "Espanhol" },
  en: { PT: "Portuguese", EN: "English", DE: "German", ES: "Spanish" },
};

function formatWeekdays(days: number[], locale: "pt" | "en") {
  if (days.length === 7) return locale === "pt" ? "Todo dia" : "Every day";
  if (!days.length) return locale === "pt" ? "Sem rotina definida" : "No routine set";
  return days.map((day) => WEEKDAY_LABELS[locale][day]).filter(Boolean).join(", ");
}

function formatDate(value: string | null, locale: "pt" | "en") {
  if (!value) return locale === "pt" ? "sem data definida" : "no date set";
  return new Intl.DateTimeFormat(locale === "pt" ? "pt-BR" : "en-US", { weekday: "long", day: "2-digit", month: "2-digit" }).format(new Date(`${value}T12:00:00`));
}

function getLanguageName(code: string | undefined, locale: "pt" | "en") {
  if (!code) return locale === "pt" ? "Idioma" : "Language";
  return LANGUAGE_NAMES[locale][code] ?? code;
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
