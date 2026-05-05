import { Check, CheckCircle2, ChevronDown, Clock, GraduationCap, LogOut, Plus, Trash2, UserCircle, X } from "lucide-react";
import { useState } from "react";

import ProgressBar from "../components/ui/ProgressBar";
import WarningModal from "../components/ui/WarningModal";
import { useLocale, useStrings } from "../contexts/StringsContext";
import { contentService } from "../services/contentService";
import type { User } from "../services/authService";
import { getStudyAreaTheme } from "../theme/studyAreaTheme";
import type { Goal } from "../types/content";

interface AccountScreenProps {
  user: User;
  goals: Goal[];
  onCreateGoal: (goal: Goal) => void;
  onDeleteGoal: (goal: Goal) => void;
  onLogout: () => void;
  onSwitchGoal: (goal: Goal) => void;
}

const SOURCE_LANGUAGES = [
  { code: "PT", label: "Portugues", labelEn: "Portuguese", detail: "Explicacoes, traducoes e apoio em portugues.", detailEn: "Explanations, translations, and support in Portuguese." },
  { code: "EN", label: "Ingles", labelEn: "English", detail: "Use ingles como idioma base do estudo.", detailEn: "Use English as the base language for study." },
];

const TARGET_LANGUAGES = [
  { code: "DE", label: "Alemao", labelEn: "German", detail: "Frases praticas para viagem, rotina e estudos.", detailEn: "Practical phrases for travel, routine, and study." },
  { code: "ES", label: "Espanhol", labelEn: "Spanish", detail: "Comunicacao cotidiana para contextos reais.", detailEn: "Everyday communication for real contexts." },
];

const AVAILABLE_COURSES = [
  { source: "PT", target: "DE" },
  { source: "PT", target: "ES" },
  { source: "EN", target: "DE" },
];

const CURRENT_LEVELS = [
  { code: "NONE", rank: 0, label: "Estou comecando agora", labelEn: "I am starting now", detail: "Sem base ainda ou quer revisar desde o zero.", detailEn: "No base yet, or wants to review from zero." },
  { code: "A1", rank: 1, label: "Ja me considero A1", labelEn: "I consider myself A1", detail: "Ja entende apresentacoes, pedidos simples e frases basicas.", detailEn: "Already understands introductions, simple requests, and basic phrases." },
  { code: "A2", rank: 2, label: "Ja me considero A2", labelEn: "I consider myself A2", detail: "Ja resolve situacoes simples e quer conversar melhor.", detailEn: "Already handles simple situations and wants better conversations." },
];

const GOAL_LEVELS = [
  { code: "A1", rank: 1, label: "Chegar no A1", labelEn: "Reach A1", detail: "Base para situacoes simples.", detailEn: "Foundation for simple situations." },
  { code: "A2", rank: 2, label: "Chegar no A2", labelEn: "Reach A2", detail: "Mais autonomia na rotina.", detailEn: "More autonomy in daily life." },
  { code: "B1", rank: 3, label: "Chegar no B1", labelEn: "Reach B1", detail: "Conversas e problemas reais.", detailEn: "Real conversations and problems." },
];

const WEEKDAYS = [
  { value: 0, short: "Seg", shortEn: "Mon" },
  { value: 1, short: "Ter", shortEn: "Tue" },
  { value: 2, short: "Qua", shortEn: "Wed" },
  { value: 3, short: "Qui", shortEn: "Thu" },
  { value: 4, short: "Sex", shortEn: "Fri" },
  { value: 5, short: "Sab", shortEn: "Sat" },
  { value: 6, short: "Dom", shortEn: "Sun" },
];

const SESSION_OPTIONS = [15, 30, 45, 60, 90];

export default function AccountScreen({ user, goals, onCreateGoal, onDeleteGoal, onLogout, onSwitchGoal }: AccountScreenProps) {
  const strings = useStrings();
  const locale = useLocale();
  const [sourceLanguage, setSourceLanguage] = useState(SOURCE_LANGUAGES[0]);
  const [targetLanguage, setTargetLanguage] = useState(TARGET_LANGUAGES[0]);
  const [currentLevel, setCurrentLevel] = useState(CURRENT_LEVELS[0]);
  const [targetLevel, setTargetLevel] = useState(GOAL_LEVELS[1]);
  const [durationDays, setDurationDays] = useState(90);
  const [routineMode, setRoutineMode] = useState<"planned" | "flexible">("planned");
  const [studyWeekdays, setStudyWeekdays] = useState(WEEKDAYS.map((day) => day.value));
  const [sessionMinutes, setSessionMinutes] = useState(60);
  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);
  const [languageModal, setLanguageModal] = useState<"source" | "target" | null>(null);
  const [goalToDelete, setGoalToDelete] = useState<Goal | null>(null);
  const [creating, setCreating] = useState(false);

  async function createGoal() {
    if (routineMode === "planned" && studyWeekdays.length === 0) return;
    if (durationDays < 7 || durationDays > 365) return;
    setCreating(true);
    try {
      const goal = await contentService.createGoal({
        source_language: sourceLanguage.code,
        target_language: targetLanguage.code,
        current_level: currentLevel.code,
        target_level: targetLevel.code,
        duration_days: durationDays,
        study_weekdays: routineMode === "planned" ? studyWeekdays : [],
        session_minutes: sessionMinutes,
      });
      onCreateGoal(goal);
      setIsCreateModalOpen(false);
    } finally {
      setCreating(false);
    }
  }

  function toggleWeekday(day: number) {
    setStudyWeekdays((current) => {
      if (current.includes(day)) return current.filter((item) => item !== day);
      return [...current, day].sort((a, b) => a - b);
    });
  }

  return (
    <div className="pb-20 md:pb-0">
      <section className="rounded-[8px] bg-white p-6 shadow-sm ring-1 ring-slate-200">
        <p className="flex items-center gap-2 text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>
          <UserCircle size={18} />
          {strings.profile.eyebrow}
        </p>
        <h2 className="mt-2 text-4xl font-semibold">{strings.profile.title}</h2>
        <p className="mt-2 max-w-xl font-medium text-slate-600">
          {strings.profile.subtitle}
        </p>
      </section>

      <section className="mt-6 grid gap-4 lg:grid-cols-[0.85fr_1.15fr]">
        <div className="space-y-4">
          <div className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
            <div className="flex items-center gap-4">
              <div className="grid h-14 w-14 place-items-center rounded-full ring-1" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
                <UserCircle size={30} />
              </div>
              <div>
                <p className="text-xl font-semibold">{user.username}</p>
                <p className="text-sm font-medium text-slate-500">{user.email || strings.profile.noEmail}</p>
              </div>
            </div>

            <button type="button" onClick={onLogout} className="mt-6 inline-flex h-12 items-center gap-2 rounded-[8px] bg-slate-950 px-5 font-semibold text-white transition hover:bg-slate-800">
              <LogOut size={18} />
              {strings.actions.logout}
            </button>
          </div>

          <div className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
            <div className="grid h-11 w-11 place-items-center rounded-[8px]" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
              <GraduationCap size={21} />
            </div>
            <h3 className="mt-3 text-xl font-semibold">{strings.profile.newArea}</h3>
            <p className="mt-2 text-sm font-medium leading-6 text-slate-500">
              {locale === "pt" ? "Crie uma nova area com idioma, nivel e duracao propria." : "Create a new area with its own language, level, and duration."}
            </p>
            <button type="button" onClick={() => setIsCreateModalOpen(true)} className="mt-4 inline-flex h-12 w-full items-center justify-center gap-2 rounded-[8px] px-5 font-semibold text-white shadow-sm transition hover:brightness-95" style={{ background: "var(--area-primary)" }}>
              <Plus size={18} />
              {strings.actions.createArea}
            </button>
          </div>
        </div>

        <div className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
          <h3 className="text-xl font-semibold">{strings.profile.yourAreas}</h3>
          <div className="mt-4 grid gap-3">
            {!goals.length ? (
              <div className="rounded-[8px] border border-dashed border-slate-300 bg-slate-50 p-5 text-center">
                <p className="font-semibold">{locale === "pt" ? "Nenhuma area criada" : "No areas yet"}</p>
                <p className="mt-1 text-sm font-medium text-slate-500">{locale === "pt" ? "Crie uma nova area para iniciar um plano de estudo." : "Create a new area to start a study plan."}</p>
              </div>
            ) : null}
            {goals.map((goal) => (
              <AreaRow key={goal.id} goal={goal} onDelete={() => setGoalToDelete(goal)} onSwitch={() => onSwitchGoal(goal)} />
            ))}
          </div>
        </div>
      </section>

      {isCreateModalOpen ? (
        <div className="fixed inset-0 z-40 grid place-items-center bg-slate-950/40 px-4 backdrop-blur-sm">
          <section className="max-h-[92vh] w-full max-w-4xl overflow-y-auto rounded-[8px] bg-white p-5 shadow-xl ring-1 ring-slate-200">
            <div className="flex items-start justify-between gap-4">
              <div>
                <p className="text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{strings.profile.newArea}</p>
                <h2 className="mt-1 text-3xl font-semibold">{locale === "pt" ? "Monte sua nova area" : "Build your new area"}</h2>
                <p className="mt-2 max-w-xl font-medium text-slate-500">
                  {locale === "pt" ? "Escolha origem, destino, nivel, duracao e rotina como no onboarding." : "Choose source, target, level, duration, and routine like onboarding."}
                </p>
              </div>
              <button type="button" onClick={() => setIsCreateModalOpen(false)} className="grid h-10 w-10 shrink-0 place-items-center rounded-[8px] text-slate-500 transition hover:bg-slate-100">
                <X size={19} />
              </button>
            </div>

            <div className="mt-6 grid gap-4 md:grid-cols-3">
              <ChoiceCard title={locale === "pt" ? "Origem" : "Source"} value={getLanguageLabel(sourceLanguage, locale)} detail={getLanguageDetail(sourceLanguage, locale)} onClick={() => setLanguageModal("source")} />
              <ChoiceCard title={locale === "pt" ? "Destino e meta" : "Target and goal"} value={`${getLanguageLabel(targetLanguage, locale)} ${targetLevel.code}`} detail={`${locale === "pt" ? currentLevel.label : currentLevel.labelEn} -> ${locale === "pt" ? targetLevel.label : targetLevel.labelEn}`} onClick={() => setLanguageModal("target")} />
              <ChoiceCard title={locale === "pt" ? "Sessao" : "Session"} value={routineMode === "planned" ? formatSession(sessionMinutes, locale) : locale === "pt" ? "Estudo avulso" : "Flexible study"} detail={routineMode === "planned" ? formatWeekdays(studyWeekdays, locale) : locale === "pt" ? "Sem dias fixos por enquanto" : "No fixed days for now"} />
            </div>

            <div className="mt-6 rounded-[8px] bg-slate-50 p-5 ring-1 ring-slate-200">
              <div className="flex items-start gap-3">
                <div className="grid h-11 w-11 place-items-center rounded-[8px]" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" }}>
                  <Clock size={20} />
                </div>
                <div>
                  <p className="text-sm font-semibold uppercase text-slate-500">{locale === "pt" ? "Plano de estudo" : "Study plan"}</p>
                  <h3 className="mt-1 text-2xl font-semibold">{locale === "pt" ? "Quando e por quanto tempo?" : "When and for how long?"}</h3>
                  <p className="mt-1 font-medium text-slate-500">{locale === "pt" ? "Essa rotina organiza o calendario, historico e sessoes dessa area." : "This routine organizes the calendar, history, and sessions for this area."}</p>
                </div>
              </div>

              <div className="mt-5 grid gap-3 sm:grid-cols-2">
                <button type="button" onClick={() => setRoutineMode("planned")} className={`rounded-[8px] p-4 text-left ring-1 transition ${routineMode === "planned" ? "text-white shadow-sm" : "bg-white ring-slate-200 hover:bg-slate-50"}`} style={routineMode === "planned" ? { background: "var(--area-primary)", borderColor: "var(--area-primary)" } : undefined}>
                  <p className="font-semibold">{locale === "pt" ? "Criar rotina" : "Create routine"}</p>
                  <p className={`mt-1 text-sm font-medium ${routineMode === "planned" ? "text-white/85" : "text-slate-500"}`}>{locale === "pt" ? "Escolher dias e tempo fixo para estudar." : "Choose fixed days and time to study."}</p>
                </button>
                <button type="button" onClick={() => setRoutineMode("flexible")} className={`rounded-[8px] p-4 text-left ring-1 transition ${routineMode === "flexible" ? "text-white shadow-sm" : "bg-white ring-slate-200 hover:bg-slate-50"}`} style={routineMode === "flexible" ? { background: "var(--area-primary)", borderColor: "var(--area-primary)" } : undefined}>
                  <p className="font-semibold">{locale === "pt" ? "Estudar avulso" : "Flexible study"}</p>
                  <p className={`mt-1 text-sm font-medium ${routineMode === "flexible" ? "text-white/85" : "text-slate-500"}`}>{locale === "pt" ? "Entrar quando quiser, sem agenda definida." : "Study whenever you want, without a fixed schedule."}</p>
                </button>
              </div>

              {routineMode === "planned" ? (
                <>
                  <div className="mt-5">
                    <p className="text-sm font-semibold uppercase text-slate-500">{locale === "pt" ? "Dias da semana" : "Weekdays"}</p>
                    <div className="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-4 md:grid-cols-7">
                      {WEEKDAYS.map((day) => {
                        const selected = studyWeekdays.includes(day.value);
                        return (
                          <button key={day.value} type="button" onClick={() => toggleWeekday(day.value)} className={`h-14 rounded-[8px] px-3 text-sm font-semibold ring-1 transition ${selected ? "text-white" : "bg-white text-slate-600 ring-slate-200 hover:bg-slate-50"}`} style={selected ? { background: "var(--area-primary)", borderColor: "var(--area-primary)" } : undefined}>
                            {locale === "pt" ? day.short : day.shortEn}
                          </button>
                        );
                      })}
                    </div>
                  </div>

                  <div className="mt-5">
                    <p className="text-sm font-semibold uppercase text-slate-500">{locale === "pt" ? "Tempo por sessao" : "Time per session"}</p>
                    <div className="mt-3 flex flex-wrap gap-3">
                      {SESSION_OPTIONS.map((item) => (
                        <button key={item} type="button" onClick={() => setSessionMinutes(item)} className={`rounded-[8px] px-5 py-3 font-semibold ring-1 transition ${sessionMinutes === item ? "text-white" : "bg-white ring-slate-200 hover:bg-slate-50"}`} style={sessionMinutes === item ? { background: "var(--area-primary)", borderColor: "var(--area-primary)" } : undefined}>
                          {formatSession(item, locale)}
                        </button>
                      ))}
                    </div>
                  </div>
                </>
              ) : null}

              <div className="mt-5 border-t border-slate-200 pt-5">
                <p className="text-sm font-semibold uppercase text-slate-500">{locale === "pt" ? "Duracao da meta" : "Goal duration"}</p>
                <div className="mt-3 flex flex-wrap gap-3">
                  {[30, 60, 90].map((item) => (
                    <button key={item} type="button" onClick={() => setDurationDays(item)} className={`rounded-[8px] px-5 py-3 font-semibold ring-1 transition ${durationDays === item ? "text-white" : "bg-white ring-slate-200 hover:bg-slate-50"}`} style={durationDays === item ? { background: "var(--area-primary)", borderColor: "var(--area-primary)" } : undefined}>
                      {locale === "pt" ? `${item} dias` : `${item} days`}
                    </button>
                  ))}
                </div>
                <label className="mt-4 block max-w-xs">
                  <span className="text-sm font-semibold text-slate-500">{locale === "pt" ? "Ou personalize" : "Or customize"}</span>
                  <input
                    type="number"
                    min={7}
                    max={365}
                    value={durationDays}
                    onChange={(event) => setDurationDays(Number(event.target.value))}
                    className="mt-2 h-12 w-full rounded-[8px] border border-slate-200 bg-white px-4 font-semibold outline-none transition focus:border-slate-400"
                  />
                </label>
                <p className="mt-2 text-sm font-medium text-slate-500">{locale === "pt" ? "Use qualquer prazo entre 7 e 365 dias." : "Use any timeline from 7 to 365 days."}</p>
              </div>
            </div>

            <button type="button" onClick={createGoal} disabled={creating || (routineMode === "planned" && studyWeekdays.length === 0) || durationDays < 7 || durationDays > 365} className="mt-6 h-12 w-full rounded-[8px] px-5 font-semibold text-white transition hover:brightness-95 disabled:opacity-60" style={{ background: "var(--area-primary)" }}>
              {creating ? strings.actions.creating : strings.actions.createArea}
            </button>
          </section>

          {languageModal ? (
            <LanguagePickerModal
              mode={languageModal}
              locale={locale}
              sourceLanguage={sourceLanguage}
              targetLanguage={targetLanguage}
              currentLevel={currentLevel}
              targetLevel={targetLevel}
              onClose={() => setLanguageModal(null)}
              onSelectSource={(language) => {
                setSourceLanguage(language);
                const nextTargets = getAvailableTargets(language.code);
                if (!nextTargets.some((target) => target.code === targetLanguage.code)) {
                  setTargetLanguage(nextTargets[0]);
                }
                setLanguageModal(null);
              }}
              onSelectTarget={(language) => setTargetLanguage(language)}
              onSelectCurrentLevel={(level) => {
                setCurrentLevel(level);
                setTargetLevel(normalizeTargetLevel(level, targetLevel));
              }}
              onSelectTargetLevel={(level) => setTargetLevel(level)}
              onConfirmTarget={() => setLanguageModal(null)}
            />
          ) : null}
        </div>
      ) : null}

      {goalToDelete ? (
        <WarningModal
          title={locale === "pt" ? "Excluir area?" : "Delete area?"}
          detail={`${goalToDelete.source_language?.code ?? ""} -> ${goalToDelete.target_language?.code ?? ""} ${goalToDelete.target_level}: ${
            goals.length <= 1
              ? locale === "pt"
                ? "essa e sua ultima area. Depois de excluir, sua conta ficara sem area ativa."
                : "this is your last area. After deleting it, your account will have no active area."
              : locale === "pt"
                ? "essa area sera removida do seu perfil."
                : "this area will be removed from your profile."
          }`}
          cancelLabel={locale === "pt" ? "Cancelar" : "Cancel"}
          confirmLabel={strings.actions.delete}
          onCancel={() => setGoalToDelete(null)}
          onConfirm={() => {
            onDeleteGoal(goalToDelete);
            setGoalToDelete(null);
          }}
        />
      ) : null}
    </div>
  );
}

const LANGUAGE_NAMES: Record<"pt" | "en", Record<string, string>> = {
  pt: { PT: "Portugues", EN: "Ingles", DE: "Alemao", ES: "Espanhol" },
  en: { PT: "Portuguese", EN: "English", DE: "German", ES: "Spanish" },
};

function getLanguageName(code: string, locale: "pt" | "en") {
  return LANGUAGE_NAMES[locale][code] ?? code;
}

function getLanguageLabel(language: { label: string; labelEn: string }, locale: "pt" | "en") {
  return locale === "pt" ? language.label : language.labelEn;
}

function getLanguageDetail(language: { detail: string; detailEn: string }, locale: "pt" | "en") {
  return locale === "pt" ? language.detail : language.detailEn;
}

function formatWeekdays(days: number[], locale: "pt" | "en") {
  if (days.length === 7) return locale === "pt" ? "Todo dia" : "Every day";
  if (days.length === 0) return locale === "pt" ? "Escolha pelo menos um dia" : "Choose at least one day";
  return WEEKDAYS.filter((day) => days.includes(day.value)).map((day) => locale === "pt" ? day.short : day.shortEn).join(", ");
}

function formatSession(minutes: number, locale: "pt" | "en") {
  if (minutes === 60) return locale === "pt" ? "1 hora" : "1 hour";
  return `${minutes} min`;
}

function getAvailableTargets(sourceCode: string) {
  const targetCodes = AVAILABLE_COURSES.filter((course) => course.source === sourceCode).map((course) => course.target);
  return TARGET_LANGUAGES.filter((language) => targetCodes.includes(language.code));
}

function minimumGoalRank(currentLevel: typeof CURRENT_LEVELS[number]) {
  return currentLevel.rank + 1;
}

function normalizeTargetLevel(currentLevel: typeof CURRENT_LEVELS[number], targetLevel: typeof GOAL_LEVELS[number]) {
  const minimumRank = minimumGoalRank(currentLevel);
  if (targetLevel.rank >= minimumRank) return targetLevel;
  return GOAL_LEVELS.find((level) => level.rank >= minimumRank) ?? GOAL_LEVELS[GOAL_LEVELS.length - 1];
}

function ChoiceCard({ title, value, detail, onClick }: { title: string; value: string; detail: string; onClick?: () => void }) {
  const content = (
    <>
      <div className="flex items-start justify-between gap-3">
        <Check className="text-emerald-500" />
        {onClick ? <ChevronDown className="text-slate-400" size={18} /> : null}
      </div>
      <p className="mt-4 text-sm font-semibold uppercase text-slate-500">{title}</p>
      <p className="text-xl font-semibold">{value}</p>
      <p className="mt-1 text-sm font-medium text-slate-500">{detail}</p>
    </>
  );

  if (onClick) {
    return (
      <button type="button" onClick={onClick} className="rounded-[8px] bg-white p-4 text-left ring-1 ring-slate-200 transition hover:bg-slate-50">
        {content}
      </button>
    );
  }

  return <div className="rounded-[8px] bg-white p-4 text-left ring-1 ring-slate-200">{content}</div>;
}

function LanguagePickerModal({
  mode,
  locale,
  sourceLanguage,
  targetLanguage,
  currentLevel,
  targetLevel,
  onClose,
  onSelectSource,
  onSelectTarget,
  onSelectCurrentLevel,
  onSelectTargetLevel,
  onConfirmTarget,
}: {
  mode: "source" | "target";
  locale: "pt" | "en";
  sourceLanguage: typeof SOURCE_LANGUAGES[number];
  targetLanguage: typeof TARGET_LANGUAGES[number];
  currentLevel: typeof CURRENT_LEVELS[number];
  targetLevel: typeof GOAL_LEVELS[number];
  onClose: () => void;
  onSelectSource: (language: typeof SOURCE_LANGUAGES[number]) => void;
  onSelectTarget: (language: typeof TARGET_LANGUAGES[number]) => void;
  onSelectCurrentLevel: (level: typeof CURRENT_LEVELS[number]) => void;
  onSelectTargetLevel: (level: typeof GOAL_LEVELS[number]) => void;
  onConfirmTarget: () => void;
}) {
  const isSource = mode === "source";
  const availableTargets = getAvailableTargets(sourceLanguage.code);
  const minimumRank = minimumGoalRank(currentLevel);

  return (
    <div className="fixed inset-0 z-50 grid place-items-center bg-slate-950/40 px-4 backdrop-blur-sm">
      <section className="w-full max-w-2xl rounded-[8px] bg-white p-5 shadow-xl ring-1 ring-slate-200">
        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{isSource ? locale === "pt" ? "Idioma de origem" : "Source language" : locale === "pt" ? "Destino e meta" : "Target and goal"}</p>
            <h2 className="mt-1 text-3xl font-semibold">{isSource ? locale === "pt" ? "Qual idioma voce entende melhor?" : "Which language do you understand best?" : locale === "pt" ? "O que voce quer aprender?" : "What do you want to learn?"}</h2>
            <p className="mt-2 max-w-xl font-medium text-slate-500">
              {isSource ? locale === "pt" ? "Esse idioma sera usado para explicacoes e traducoes." : "This language will be used for explanations and translations." : locale === "pt" ? "Escolha o idioma, seu nivel atual e a meta que quer alcancar." : "Choose the language, your current level, and the goal you want to reach."}
            </p>
          </div>
          <button type="button" onClick={onClose} className="grid h-10 w-10 shrink-0 place-items-center rounded-[8px] text-slate-500 transition hover:bg-slate-100">
            <X size={19} />
          </button>
        </div>

        <div className="mt-6 grid gap-3 sm:grid-cols-2">
          {(isSource ? SOURCE_LANGUAGES : availableTargets).map((language) => {
            const selected = isSource ? language.code === sourceLanguage.code : language.code === targetLanguage.code;
            return (
              <button
                key={language.code}
                type="button"
                onClick={() => isSource ? onSelectSource(language as typeof SOURCE_LANGUAGES[number]) : onSelectTarget(language as typeof TARGET_LANGUAGES[number])}
                className={`rounded-[8px] p-4 text-left ring-1 transition ${selected ? "text-slate-950" : "bg-white ring-slate-200 hover:bg-slate-50"}`}
                style={selected ? { background: "var(--area-primary-soft)", boxShadow: "inset 0 0 0 1px var(--area-primary)" } : undefined}
              >
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <p className="text-xl font-semibold">{getLanguageLabel(language, locale)}</p>
                    <p className="mt-1 text-sm font-medium text-slate-500">{getLanguageDetail(language, locale)}</p>
                  </div>
                  {selected ? <Check style={{ color: "var(--area-primary)" }} size={20} /> : null}
                </div>
              </button>
            );
          })}
        </div>

        {!isSource ? (
          <>
            <div className="mt-6 border-t border-slate-200 pt-5">
              <p className="text-sm font-semibold uppercase text-slate-500">{locale === "pt" ? "Hoje eu me considero" : "Today I consider myself"}</p>
              <div className="mt-3 grid gap-3 sm:grid-cols-3">
                {CURRENT_LEVELS.map((level) => {
                  const selected = level.code === currentLevel.code;
                  return (
                    <button key={level.code} type="button" onClick={() => onSelectCurrentLevel(level)} className={`rounded-[8px] p-4 text-left ring-1 transition ${selected ? "text-white" : "bg-white ring-slate-200 hover:bg-slate-50"}`} style={selected ? { background: "var(--area-primary)", borderColor: "var(--area-primary)" } : undefined}>
                      <p className="text-lg font-semibold">{locale === "pt" ? level.label : level.labelEn}</p>
                      <p className={`mt-1 text-sm font-medium ${selected ? "text-white/80" : "text-slate-500"}`}>{locale === "pt" ? level.detail : level.detailEn}</p>
                    </button>
                  );
                })}
              </div>
            </div>

            <div className="mt-6 border-t border-slate-200 pt-5">
              <p className="text-sm font-semibold uppercase text-slate-500">{locale === "pt" ? "Minha meta" : "My goal"}</p>
              <div className="mt-3 grid gap-3 sm:grid-cols-3">
                {GOAL_LEVELS.map((level) => {
                  const selected = level.code === targetLevel.code;
                  const disabled = level.rank < minimumRank;
                  return (
                    <button key={level.code} type="button" disabled={disabled} onClick={() => onSelectTargetLevel(level)} className={`rounded-[8px] p-4 text-left ring-1 transition disabled:cursor-not-allowed disabled:opacity-45 ${selected ? "text-white" : "bg-white ring-slate-200 hover:bg-slate-50"}`} style={selected ? { background: "var(--area-primary)", borderColor: "var(--area-primary)" } : undefined}>
                      <p className="text-xl font-semibold">{level.code}</p>
                      <p className={`mt-1 text-sm font-bold ${selected ? "text-white/90" : "text-slate-700"}`}>{locale === "pt" ? level.label : level.labelEn}</p>
                      <p className={`mt-1 text-sm font-medium ${selected ? "text-white/80" : "text-slate-500"}`}>{disabled ? locale === "pt" ? "Abaixo do seu nivel atual." : "Below your current level." : locale === "pt" ? level.detail : level.detailEn}</p>
                    </button>
                  );
                })}
              </div>
            </div>

            <button type="button" onClick={onConfirmTarget} className="mt-6 h-12 w-full rounded-[8px] px-5 font-semibold text-white transition hover:brightness-95" style={{ background: "var(--area-primary)" }}>
              {locale === "pt" ? "Confirmar destino" : "Confirm target"}
            </button>
          </>
        ) : null}
      </section>
    </div>
  );
}

function AreaRow({ goal, onDelete, onSwitch }: { goal: Goal; onDelete: () => void; onSwitch: () => void }) {
  const strings = useStrings();
  const theme = getStudyAreaTheme(goal);

  return (
    <article className="rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-200">
      <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
        <div className="min-w-0 flex-1">
          <div className="flex items-center gap-2">
            <h4 className="text-lg font-semibold">{theme.label}</h4>
            {goal.is_active ? (
              <span className="inline-flex items-center gap-1 rounded-full px-2 py-1 text-xs font-semibold" style={{ background: theme.primarySoft, color: theme.primaryDark }}>
                <CheckCircle2 size={13} />
                {strings.profile.active}
              </span>
            ) : null}
          </div>
          <p className="mt-1 text-sm font-medium text-slate-500">{strings.profile.completeLessons(goal.completed_lessons)} | {strings.profile.streak(goal.streak_days)}</p>
          <div className="mt-3 max-w-md">
            <ProgressBar value={goal.progress_percent} />
          </div>
        </div>
        <div className="flex gap-2">
          {!goal.is_active ? (
            <button type="button" onClick={onSwitch} className="h-10 rounded-[8px] px-3 text-sm font-semibold text-white" style={{ background: theme.primary }}>
              {strings.actions.use}
            </button>
          ) : null}
          <button type="button" onClick={onDelete} className="inline-flex h-10 items-center gap-2 rounded-[8px] bg-white px-3 text-sm font-semibold text-red-700 ring-1 ring-red-100 transition hover:bg-red-50">
            <Trash2 size={15} />
            {strings.actions.delete}
          </button>
        </div>
      </div>
    </article>
  );
}
