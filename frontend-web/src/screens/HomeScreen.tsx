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
  const strings = useStrings();
  const locale = useLocale();
  const goal = useAsyncData(contentService.getCurrentGoal);

  // ── No goal ──────────────────────────────────────────────────────────────
  if (!hasActiveGoal) {
    return (
      <div className="flex min-h-[60vh] flex-col items-center justify-center px-4 pb-20 text-center md:pb-0">
        <div
          className="grid h-16 w-16 place-items-center rounded-full text-white"
          style={{ background: "var(--area-primary)" }}
        >
          <BookOpen size={26} />
        </div>
        <h2 className="mt-6 text-2xl font-semibold text-slate-950">
          {locale === "pt" ? "Nenhuma área ativa" : "No active area"}
        </h2>
        <p className="mt-3 max-w-xs text-base font-medium leading-7 text-slate-500">
          {locale === "pt"
            ? "Crie uma área de estudo para começar seu plano de idiomas."
            : "Create a study area to start your language plan."}
        </p>
        <button
          type="button"
          onClick={onCreateArea}
          className="mt-7 inline-flex h-12 items-center gap-2 rounded-[8px] px-6 font-semibold text-white transition hover:brightness-95"
          style={{ background: "var(--area-primary)" }}
        >
          <Plus size={18} />
          {strings.actions.createArea}
        </button>
      </div>
    );
  }

  if (goal.loading) return <StateMessage />;
  if (goal.error || !goal.data) return <StateMessage title={strings.states.empty} detail={strings.states.apiHint} />;

  const g = goal.data;
  const remaining = Math.max(g.duration_days - g.completed_lessons, 0);
  const targetLanguage = getLanguageName(g.target_language?.code, locale);
  const sourceLanguage = getLanguageName(g.source_language?.code, locale);
  const targetCode = g.target_language?.code ?? "DE";
  const hasRoutine = Boolean(g.study_weekdays?.length);
  const routine = hasRoutine
    ? strings.home.routine(formatWeekdays(g.study_weekdays ?? [], locale), g.session_minutes ?? 30)
    : strings.home.flexibleStudy;
  const nextStudyLabel = hasRoutine
    ? g.is_study_day_today
      ? strings.home.studyToday
      : strings.home.nextSession(formatDate(g.next_study_date, locale))
    : strings.home.noFixedSchedule;

  return (
    <div className="pb-4 md:pb-0">

      {/* ── Hero ─────────────────────────────────────────────────────────── */}
      <section className="rounded-[8px] bg-white p-5 ring-1 ring-slate-200 md:p-7">
        <div className="flex items-center justify-between gap-3">
          <span
            className="rounded-full px-3 py-1 text-[11px] font-bold uppercase tracking-wider"
            style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}
          >
            {targetCode} · {g.current_level} → {g.target_level}
          </span>
          <span className="text-xl font-bold tabular-nums" style={{ color: "var(--area-primary)" }}>
            {g.progress_percent}%
          </span>
        </div>

        <h2 className="mt-4 text-3xl font-semibold leading-tight text-slate-950 md:text-4xl">
          {targetLanguage}
        </h2>
        <p className="mt-1 text-sm font-medium text-slate-400">
          {sourceLanguage} → {targetLanguage} · {g.target_level}
        </p>

        <div className="mt-5">
          <ProgressBar value={g.progress_percent} />
          <p className="mt-2 text-xs font-semibold text-slate-400">
            {g.learned_phrases.toLocaleString()} / {g.total_phrases.toLocaleString()}{" "}
            {locale === "pt" ? "frases" : "phrases"}
          </p>
        </div>

        <button
          type="button"
          onClick={onStartToday}
          className="mt-5 flex h-12 w-full items-center justify-center gap-2 rounded-[8px] font-semibold text-white transition hover:brightness-95 active:scale-[0.99]"
          style={{ background: "var(--area-primary)" }}
        >
          {strings.actions.startToday}
          <ArrowRight size={18} />
        </button>
      </section>

      {/* ── Stats ────────────────────────────────────────────────────────── */}
      <div className="mt-3 grid grid-cols-3 overflow-hidden rounded-[8px] bg-slate-200" style={{ gap: 1 }}>
        <StatCell
          value={g.streak_days}
          label={strings.home.streak}
          icon={<Flame size={13} style={{ color: "var(--area-primary)" }} />}
        />
        <StatCell
          value={g.completed_lessons}
          label={strings.home.lessons}
          icon={<BookOpen size={13} className="text-sky-500" />}
        />
        <StatCell
          value={remaining}
          label={strings.home.remaining}
          icon={<CalendarDays size={13} className="text-violet-500" />}
        />
      </div>

      {/* ── Schedule + Goal ──────────────────────────────────────────────── */}
      <div className="mt-3 overflow-hidden rounded-[8px] bg-white ring-1 ring-slate-200 divide-y divide-slate-100">
        <div className="px-4 py-4 md:px-5">
          <p className="text-[10px] font-bold uppercase tracking-widest text-slate-400">
            {strings.home.nextLesson}
          </p>
          <p className="mt-1.5 text-sm font-semibold text-slate-800">{routine}</p>
          <p
            className="mt-0.5 text-sm font-bold"
            style={{ color: "var(--area-primary)" }}
          >
            {nextStudyLabel}
          </p>
        </div>

        <div className="px-4 py-4 md:px-5">
          <p className="text-[10px] font-bold uppercase tracking-widest text-slate-400">
            {locale === "pt" ? "Meta" : "Goal"}
          </p>
          <p className="mt-1.5 text-sm font-semibold text-slate-800">
            {strings.home.languagePath(sourceLanguage, targetLanguage, g.target_level)}
          </p>
          <p className="mt-0.5 text-sm font-medium text-slate-400">
            {g.duration_days} {locale === "pt" ? "dias" : "days"} ·{" "}
            {remaining} {locale === "pt" ? "restantes" : "remaining"}
          </p>
        </div>
      </div>

    </div>
  );
}

function StatCell({ value, label, icon }: { value: number; label: string; icon: React.ReactNode }) {
  return (
    <div className="bg-white px-3 py-4 md:px-5">
      <p className="text-2xl font-semibold tabular-nums text-slate-950 md:text-3xl">{value}</p>
      <div className="mt-1.5 flex items-center gap-1.5">
        {icon}
        <p className="text-[11px] font-bold leading-tight text-slate-500">{label}</p>
      </div>
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
  return new Intl.DateTimeFormat(locale === "pt" ? "pt-BR" : "en-US", {
    weekday: "long",
    day: "2-digit",
    month: "2-digit",
  }).format(new Date(`${value}T12:00:00`));
}

function getLanguageName(code: string | undefined, locale: "pt" | "en") {
  if (!code) return locale === "pt" ? "Idioma" : "Language";
  return LANGUAGE_NAMES[locale][code] ?? code;
}
