import { ArrowRight, Check, ChevronDown, Clock, Flag, X } from "lucide-react";
import { useState } from "react";

import { contentService } from "../services/contentService";
import { useStrings } from "../contexts/StringsContext";
import type { Goal } from "../types/content";

interface OnboardingScreenProps {
  onComplete: (goal: Goal) => void;
}

const SOURCE_LANGUAGES = [
  { code: "PT", label: "Portugues", detail: "Explicacoes, traducoes e apoio em portugues." },
  { code: "EN", label: "Ingles", detail: "Use ingles como idioma base do estudo." },
];

const TARGET_LANGUAGES = [
  { code: "DE", label: "Alemao", detail: "Frases praticas para viagem, rotina e estudos." },
  { code: "ES", label: "Espanhol", detail: "Comunicacao cotidiana para contextos reais." },
];

const AVAILABLE_COURSES = [
  { source: "PT", target: "DE" },
  { source: "PT", target: "ES" },
  { source: "EN", target: "DE" },
];

const LEVELS = [
  { code: "A1", label: "A1", detail: "Comecando do basico." },
  { code: "A2", label: "A2", detail: "Frases simples com mais autonomia." },
  { code: "B1", label: "B1", detail: "Conversas e situacoes mais completas." },
];

const WEEKDAYS = [
  { value: 0, short: "Seg", label: "Segunda" },
  { value: 1, short: "Ter", label: "Terca" },
  { value: 2, short: "Qua", label: "Quarta" },
  { value: 3, short: "Qui", label: "Quinta" },
  { value: 4, short: "Sex", label: "Sexta" },
  { value: 5, short: "Sab", label: "Sabado" },
  { value: 6, short: "Dom", label: "Domingo" },
];

const SESSION_OPTIONS = [15, 30, 45, 60, 90];

export default function OnboardingScreen({ onComplete }: OnboardingScreenProps) {
  const strings = useStrings();
  const [sourceLanguage, setSourceLanguage] = useState(SOURCE_LANGUAGES[0]);
  const [targetLanguage, setTargetLanguage] = useState(TARGET_LANGUAGES[0]);
  const [targetLevel, setTargetLevel] = useState(LEVELS[0]);
  const [routineMode, setRoutineMode] = useState<"planned" | "flexible">("planned");
  const [studyWeekdays, setStudyWeekdays] = useState(WEEKDAYS.map((day) => day.value));
  const [sessionMinutes, setSessionMinutes] = useState(60);
  const [modal, setModal] = useState<"source" | "target" | null>(null);
  const [loading, setLoading] = useState(false);

  async function start() {
    if (routineMode === "planned" && studyWeekdays.length === 0) return;
    setLoading(true);
    const goal = await contentService.createGoal({
      source_language: sourceLanguage.code,
      target_language: targetLanguage.code,
      target_level: targetLevel.code,
      duration_days: 90,
      study_weekdays: routineMode === "planned" ? studyWeekdays : [],
      session_minutes: sessionMinutes,
    });
    onComplete(goal);
  }

  function toggleWeekday(day: number) {
    setStudyWeekdays((current) => {
      if (current.includes(day)) return current.filter((item) => item !== day);
      return [...current, day].sort((a, b) => a - b);
    });
  }

  return (
    <main className="min-h-screen bg-slate-50 px-5 py-8 text-slate-950">
      <section className="mx-auto max-w-4xl">
        <div className="rounded-[8px] bg-white p-6 shadow-sm ring-1 ring-slate-200">
          <div className="flex items-center gap-4">
            <div className="grid h-14 w-14 place-items-center rounded-[8px] bg-emerald-50 text-emerald-700 ring-1 ring-emerald-100">
              <Flag />
            </div>
            <div>
              <p className="text-sm font-semibold uppercase text-emerald-700">{strings.onboarding.eyebrow}</p>
              <h1 className="text-3xl font-semibold">{strings.onboarding.title}</h1>
            </div>
          </div>

          <div className="mt-8 grid gap-4 md:grid-cols-3">
            <Choice title={strings.onboarding.source} value={sourceLanguage.label} detail={sourceLanguage.detail} onClick={() => setModal("source")} />
            <Choice title={strings.onboarding.target} value={`${targetLanguage.label} ${targetLevel.label}`} detail={targetLanguage.detail} onClick={() => setModal("target")} />
            <Choice title={strings.onboarding.session} value={routineMode === "planned" ? `${sessionMinutes} min` : "Estudo avulso"} detail={routineMode === "planned" ? formatWeekdays(studyWeekdays) : "Sem dias fixos por enquanto"} />
          </div>

          <div className="mt-8 rounded-[8px] bg-slate-50 p-5 ring-1 ring-slate-200">
            <div className="flex items-start gap-3">
              <div className="grid h-11 w-11 place-items-center rounded-[8px] bg-emerald-50 text-emerald-700 ring-1 ring-emerald-100">
                <Clock size={20} />
              </div>
              <div>
                <p className="text-sm font-semibold uppercase text-slate-500">Sua rotina de estudo</p>
                <h2 className="mt-1 text-2xl font-semibold">Quando voce quer estudar?</h2>
                <p className="mt-1 font-medium text-slate-500">O plano usa essa rotina para organizar suas sessoes e manter o estudo realista.</p>
              </div>
            </div>

            <div className="mt-5 grid gap-3 sm:grid-cols-2">
              <button type="button" onClick={() => setRoutineMode("planned")} className={`rounded-[8px] p-4 text-left ring-1 transition ${routineMode === "planned" ? "bg-emerald-600 text-white ring-emerald-600" : "bg-white ring-slate-200 hover:bg-slate-50"}`}>
                <p className="font-semibold">Criar rotina</p>
                <p className={`mt-1 text-sm font-medium ${routineMode === "planned" ? "text-emerald-50" : "text-slate-500"}`}>Escolher dias e tempo fixo para estudar.</p>
              </button>
              <button type="button" onClick={() => setRoutineMode("flexible")} className={`rounded-[8px] p-4 text-left ring-1 transition ${routineMode === "flexible" ? "bg-emerald-600 text-white ring-emerald-600" : "bg-white ring-slate-200 hover:bg-slate-50"}`}>
                <p className="font-semibold">Estudar avulso</p>
                <p className={`mt-1 text-sm font-medium ${routineMode === "flexible" ? "text-emerald-50" : "text-slate-500"}`}>Entrar quando quiser, sem agenda definida.</p>
              </button>
            </div>

            {routineMode === "planned" ? (
              <>
            <div className="mt-5">
              <p className="text-sm font-semibold uppercase text-slate-500">Dias da semana</p>
              <div className="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-4 md:grid-cols-7">
                {WEEKDAYS.map((day) => {
                  const selected = studyWeekdays.includes(day.value);
                  return (
                    <button key={day.value} type="button" onClick={() => toggleWeekday(day.value)} className={`h-14 rounded-[8px] px-3 text-sm font-semibold ring-1 transition ${selected ? "bg-emerald-600 text-white ring-emerald-600" : "bg-white text-slate-600 ring-slate-200 hover:bg-slate-50"}`}>
                      {day.short}
                    </button>
                  );
                })}
              </div>
            </div>

            <div className="mt-5">
              <p className="text-sm font-semibold uppercase text-slate-500">Tempo por sessao</p>
              <div className="mt-3 flex flex-wrap gap-3">
                {SESSION_OPTIONS.map((item) => (
                  <button key={item} type="button" onClick={() => setSessionMinutes(item)} className={`rounded-[8px] px-5 py-3 font-semibold ring-1 transition ${sessionMinutes === item ? "bg-emerald-600 text-white ring-emerald-600" : "bg-white ring-slate-200 hover:bg-slate-50"}`}>
                    {item === 60 ? "1 hora" : `${item} min`}
                  </button>
                ))}
              </div>
            </div>
              </>
            ) : (
              <div className="mt-5 rounded-[8px] bg-white p-4 ring-1 ring-slate-200">
                <p className="font-semibold text-slate-900">Sem rotina fixa por agora</p>
                <p className="mt-1 text-sm font-medium text-slate-500">Voce ainda pode iniciar uma sessao pela Home quando quiser. Depois da para criar uma rotina no perfil.</p>
              </div>
            )}
          </div>

          <button type="button" onClick={start} disabled={loading || (routineMode === "planned" && studyWeekdays.length === 0)} className="mt-7 flex h-14 w-full items-center justify-center gap-2 rounded-[8px] bg-emerald-600 font-semibold text-white shadow-sm transition hover:bg-emerald-700 disabled:opacity-60">
            {loading ? strings.actions.creating : strings.onboarding.start}
            <ArrowRight size={18} />
          </button>
        </div>
      </section>

      {modal ? (
        <LanguageModal
          mode={modal}
          sourceLanguage={sourceLanguage}
          targetLanguage={targetLanguage}
          targetLevel={targetLevel}
          onClose={() => setModal(null)}
          onSelectSource={(language) => {
            setSourceLanguage(language);
            const nextTargets = getAvailableTargets(language.code);
            if (!nextTargets.some((target) => target.code === targetLanguage.code)) {
              setTargetLanguage(nextTargets[0]);
            }
            setModal(null);
          }}
          onSelectTarget={(language) => setTargetLanguage(language)}
          onSelectLevel={(level) => setTargetLevel(level)}
          onConfirmTarget={() => setModal(null)}
        />
      ) : null}
    </main>
  );
}

function formatWeekdays(days: number[]) {
  if (days.length === 7) return "Todo dia";
  if (days.length === 0) return "Escolha pelo menos um dia";
  return WEEKDAYS.filter((day) => days.includes(day.value)).map((day) => day.short).join(", ");
}

function Choice({ title, value, detail, onClick }: { title: string; value: string; detail: string; onClick?: () => void }) {
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

function LanguageModal({
  mode,
  sourceLanguage,
  targetLanguage,
  targetLevel,
  onClose,
  onSelectSource,
  onSelectTarget,
  onSelectLevel,
  onConfirmTarget,
}: {
  mode: "source" | "target";
  sourceLanguage: typeof SOURCE_LANGUAGES[number];
  targetLanguage: typeof TARGET_LANGUAGES[number];
  targetLevel: typeof LEVELS[number];
  onClose: () => void;
  onSelectSource: (language: typeof SOURCE_LANGUAGES[number]) => void;
  onSelectTarget: (language: typeof TARGET_LANGUAGES[number]) => void;
  onSelectLevel: (level: typeof LEVELS[number]) => void;
  onConfirmTarget: () => void;
}) {
  const isSource = mode === "source";
  const availableTargets = getAvailableTargets(sourceLanguage.code);

  return (
    <div className="fixed inset-0 z-40 grid place-items-center bg-slate-950/40 px-4 backdrop-blur-sm">
      <section className="w-full max-w-2xl rounded-[8px] bg-white p-5 shadow-xl ring-1 ring-slate-200">
        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="text-sm font-semibold uppercase text-emerald-700">{isSource ? "Idioma de origem" : "Idioma de destino"}</p>
            <h2 className="mt-1 text-3xl font-semibold">{isSource ? "Qual idioma voce entende melhor?" : "Qual idioma voce quer aprender?"}</h2>
            <p className="mt-2 max-w-xl font-medium text-slate-500">
              {isSource ? "Esse idioma sera usado para explicacoes e traducoes." : "Escolha o idioma principal e o nivel inicial do curso."}
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
                className={`rounded-[8px] p-4 text-left ring-1 transition ${selected ? "bg-emerald-50 text-emerald-950 ring-emerald-200" : "bg-white ring-slate-200 hover:bg-slate-50"}`}
              >
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <p className="text-xl font-semibold">{language.label}</p>
                    <p className="mt-1 text-sm font-medium text-slate-500">{language.detail}</p>
                  </div>
                  {selected ? <Check className="text-emerald-600" size={20} /> : null}
                </div>
              </button>
            );
          })}
        </div>

        {!isSource ? (
          <>
            <div className="mt-6 border-t border-slate-200 pt-5">
              <p className="text-sm font-semibold uppercase text-slate-500">Nivel inicial</p>
              <div className="mt-3 grid gap-3 sm:grid-cols-3">
                {LEVELS.map((level) => {
                  const selected = level.code === targetLevel.code;
                  return (
                    <button key={level.code} type="button" onClick={() => onSelectLevel(level)} className={`rounded-[8px] p-4 text-left ring-1 transition ${selected ? "bg-emerald-600 text-white ring-emerald-600" : "bg-white ring-slate-200 hover:bg-slate-50"}`}>
                      <p className="text-xl font-semibold">{level.label}</p>
                      <p className={`mt-1 text-sm font-medium ${selected ? "text-emerald-50" : "text-slate-500"}`}>{level.detail}</p>
                    </button>
                  );
                })}
              </div>
            </div>

            <button type="button" onClick={onConfirmTarget} className="mt-6 h-12 w-full rounded-[8px] bg-emerald-600 px-5 font-semibold text-white transition hover:bg-emerald-700">
              Confirmar destino
            </button>
          </>
        ) : null}
      </section>
    </div>
  );
}

function getAvailableTargets(sourceCode: string) {
  const targetCodes = AVAILABLE_COURSES.filter((course) => course.source === sourceCode).map((course) => course.target);
  return TARGET_LANGUAGES.filter((language) => targetCodes.includes(language.code));
}
