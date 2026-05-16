import { ArrowLeft, ArrowRight, Check } from "lucide-react";
import { useEffect, useState } from "react";

import { useStrings } from "../../../contexts/StringsContext";
import { adventureService } from "../../../services/adventureService";
import { contentService } from "../../../services/contentService";
import type { AvailableLanguage } from "../../../types/adventure";
import type { Goal } from "../../../types/content";

interface OnboardingScreenProps {
  onComplete: (goal: Goal) => void;
}

const SOURCE_LANGUAGES = [
  { code: "PT", detailKey: "sourceLanguageDetailPt" as const },
];

const LEVELS = [
  { code: "A1", labelKey: "levelIniciante" as const, detailKey: "levelA1Detail" as const },
];

const WEEKDAYS = [0, 1, 2, 3, 4, 5, 6];

const SESSION_OPTIONS = [15, 30, 45, 60, 90];

function estimateMonths(days: number[], minutes: number) {
  if (days.length === 0) return null;
  const weeks = 80 / ((days.length * minutes) / 60);
  return Math.max(1, Math.round(weeks / 4.3));
}

function formatSessionDuration(minutes: number, s: ReturnType<typeof useStrings>, style: "short" | "long") {
  if (minutes === 60) return style === "long" ? s.onboarding.hourLong : s.onboarding.hourShort;
  if (minutes === 90) return s.onboarding.hourAndHalfShort;
  return s.onboarding.minutesShort(minutes);
}

export default function OnboardingScreen({ onComplete }: OnboardingScreenProps) {
  const s = useStrings();
  const [step, setStep] = useState<1 | 2>(1);
  const [direction, setDirection] = useState<"forward" | "back">("forward");

  const [sourceLanguage, setSourceLanguage] = useState(SOURCE_LANGUAGES[0]);
  const [targetLanguage, setTargetLanguage] = useState<AvailableLanguage | null>(null);
  const [level, setLevel] = useState(LEVELS[0]);

  const [studyDays, setStudyDays] = useState([0, 2, 4]);
  const [sessionMinutes, setSessionMinutes] = useState(30);
  const [loading, setLoading] = useState(false);

  const [availableTargets, setAvailableTargets] = useState<AvailableLanguage[]>([]);
  const [loadingLanguages, setLoadingLanguages] = useState(true);

  useEffect(() => {
    adventureService.listAvailableLanguages()
      .then((langs) => {
        setAvailableTargets(langs);
        if (langs.length > 0) setTargetLanguage(langs[0]);
      })
      .finally(() => setLoadingLanguages(false));
  }, []);

  function goToStep2() { setDirection("forward"); setStep(2); }
  function goToStep1() { setDirection("back"); setStep(1); }

  function toggleDay(day: number) {
    setStudyDays((curr) =>
      curr.includes(day) ? curr.filter((d) => d !== day) : [...curr, day].sort((a, b) => a - b)
    );
  }

  async function finish() {
    if (studyDays.length === 0 || !targetLanguage) return;
    setLoading(true);
    try {
      const goal = await contentService.createGoal({
        source_language: sourceLanguage.code,
        target_language: targetLanguage.code,
        target_level: level.code,
        duration_days: 90,
        study_weekdays: studyDays,
        session_minutes: sessionMinutes,
      });
      onComplete(goal);
    } finally {
      setLoading(false);
    }
  }

  const months = estimateMonths(studyDays, sessionMinutes);
  const animClass = direction === "forward" ? "onb-step-forward" : "onb-step-back";

  return (
    <main className="flex min-h-dvh flex-col items-center justify-center bg-white px-4 py-10">
      <div aria-hidden className="auth-glow z-0" />
      <div className="relative z-10 flex w-full max-w-[440px] flex-col gap-6">

        <div className="flex flex-col gap-4">
          <div className="flex items-center justify-between">
            <img src="/lang-plus.svg" alt="Lang+" className="h-8 w-auto" />
            <span className="text-xs font-semibold text-slate-400">{s.onboarding.stepProgress(step, 2)}</span>
          </div>
          <div className="onb-progress-bar">
            <div className="onb-progress-fill" style={{ width: step === 1 ? "50%" : "100%" }} />
          </div>
        </div>

        <div
          key={step}
          className={`w-full rounded-2xl border border-slate-200 bg-white p-7 shadow-[0_2px_4px_rgba(0,0,0,0.03),0_8px_24px_rgba(0,0,0,0.06)] ${animClass}`}
        >
          {step === 1 ? (
            <Step1
              s={s}
              sourceLanguage={sourceLanguage}
              targetLanguage={targetLanguage}
              availableTargets={availableTargets}
              loadingLanguages={loadingLanguages}
              level={level}
              onSelectSource={setSourceLanguage}
              onSelectTarget={setTargetLanguage}
              onSelectLevel={setLevel}
            />
          ) : (
            <Step2
              studyDays={studyDays}
              sessionMinutes={sessionMinutes}
              months={months}
              onToggleDay={toggleDay}
              onSelectMinutes={setSessionMinutes}
            />
          )}

          <div className="mt-6 flex gap-3">
            {step === 2 && (
              <button
                type="button"
                onClick={goToStep1}
                className="flex items-center justify-center rounded-xl border border-slate-200 bg-white text-slate-500 transition hover:bg-slate-50"
                style={{ minWidth: "52px", height: "52px" }}
              >
                <ArrowLeft size={18} />
              </button>
            )}
            <button
              type="button"
              onClick={step === 1 ? goToStep2 : finish}
              disabled={loading || (step === 2 && studyDays.length === 0) || (step === 1 && !targetLanguage)}
              className="auth-submit flex-1"
            >
              {loading ? <LoadingDots /> : step === 1
                ? <>{s.onboarding.next} <ArrowRight size={17} strokeWidth={2.5} /></>
                : <>{s.onboarding.start} <ArrowRight size={17} strokeWidth={2.5} /></>
              }
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}

function Step1({
  s, sourceLanguage, targetLanguage, availableTargets, loadingLanguages, level,
  onSelectSource, onSelectTarget, onSelectLevel,
}: {
  s: ReturnType<typeof useStrings>;
  sourceLanguage: typeof SOURCE_LANGUAGES[number];
  targetLanguage: AvailableLanguage | null;
  availableTargets: AvailableLanguage[];
  loadingLanguages: boolean;
  level: typeof LEVELS[number];
  onSelectSource: (l: typeof SOURCE_LANGUAGES[number]) => void;
  onSelectTarget: (l: AvailableLanguage) => void;
  onSelectLevel: (l: typeof LEVELS[number]) => void;
}) {
  return (
    <div className="flex flex-col gap-6">
      <div>
        <h1 className="text-xl font-bold tracking-tight text-slate-950">{s.onboarding.configureCourseTitle}</h1>
        <p className="mt-1 text-sm font-medium text-slate-500">{s.onboarding.configureCourseSubtitle}</p>
      </div>

      <Section label={s.onboarding.youSpeak}>
        <div className="flex flex-col gap-2">
          {SOURCE_LANGUAGES.map((lang) => (
            <button
              key={lang.code}
              type="button"
              onClick={() => onSelectSource(lang)}
              className={`onb-select-card ${sourceLanguage.code === lang.code ? "selected" : ""}`}
            >
              <LangFlag code={lang.code} />
              <div className="flex-1 text-left">
                <p className="text-sm font-bold text-slate-950">{s.languages[lang.code as keyof typeof s.languages] ?? lang.code}</p>
                <p className="text-xs font-medium text-slate-500">{s.onboarding[lang.detailKey]}</p>
              </div>
              {sourceLanguage.code === lang.code && <Check size={16} className="shrink-0 area-text-primary" />}
            </button>
          ))}
        </div>
      </Section>

      <Section label={s.onboarding.youLearn}>
        {loadingLanguages ? (
          <div className="flex items-center gap-2 py-4 text-sm text-slate-400">
            <LoadingDots /> {s.onboarding.loadingLanguages}
          </div>
        ) : (
          <div className="flex flex-col gap-2">
            {availableTargets.map((lang) => (
              <button
                key={lang.code}
                type="button"
                onClick={() => onSelectTarget(lang)}
                className={`onb-select-card ${targetLanguage?.code === lang.code ? "selected" : ""}`}
              >
                <LangFlag code={lang.code} />
                <div className="flex-1 text-left">
                  <p className="text-sm font-bold text-slate-950">{s.languages[lang.code as keyof typeof s.languages] ?? lang.code}</p>
                  <p className="text-xs font-medium text-slate-500">{lang.chapter_subtitle || lang.chapter_title}</p>
                </div>
                {targetLanguage?.code === lang.code && <Check size={16} className="shrink-0 area-text-primary" />}
              </button>
            ))}
          </div>
        )}
      </Section>

      <Section label={s.onboarding.levelLabel}>
        <div className="flex gap-2">
          {LEVELS.map((l) => (
            <button
              key={l.code}
              type="button"
              onClick={() => onSelectLevel(l)}
              className={`onb-pill flex-1 text-center ${level.code === l.code ? "selected" : ""}`}
              style={{ padding: "10px 8px" }}
            >
              <span className="block text-base font-bold">{l.code}</span>
              <span className="block text-[11px] font-semibold opacity-80">{s.onboarding[l.labelKey]}</span>
              <span className="block text-[10px] font-medium opacity-60">{s.onboarding[l.detailKey]}</span>
            </button>
          ))}
        </div>
      </Section>
    </div>
  );
}

function Step2({
  studyDays, sessionMinutes, months, onToggleDay, onSelectMinutes,
}: {
  studyDays: number[];
  sessionMinutes: number;
  months: number | null;
  onToggleDay: (day: number) => void;
  onSelectMinutes: (m: number) => void;
}) {
  const s = useStrings();
  return (
    <div className="flex flex-col gap-6">
      <div>
        <h1 className="text-xl font-bold tracking-tight text-slate-950">{s.onboarding.routineTitle}</h1>
        <p className="mt-1 text-sm font-medium text-slate-500">{s.onboarding.routineSubtitle}</p>
      </div>

      <Section label={s.onboarding.daysLabel}>
        <div className="flex justify-between gap-1">
          {WEEKDAYS.map((day) => (
            <button
              key={day}
              type="button"
              onClick={() => onToggleDay(day)}
              className={`onb-day-pill ${studyDays.includes(day) ? "selected" : ""}`}
            >
              {s.weekdays.short[day]}
            </button>
          ))}
        </div>
        {studyDays.length === 0 && (
          <p className="mt-2 text-xs font-semibold text-red-500">{s.profile.chooseDayError}</p>
        )}
      </Section>

      <Section label={s.onboarding.durationLabel}>
        <div className="flex flex-wrap gap-2">
          {SESSION_OPTIONS.map((opt) => (
            <button
              key={opt}
              type="button"
              onClick={() => onSelectMinutes(opt)}
              className={`onb-pill ${sessionMinutes === opt ? "selected" : ""}`}
            >
              {formatSessionDuration(opt, s, "short")}
            </button>
          ))}
        </div>
      </Section>

      {months !== null && (
        <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
          <p className="text-sm font-semibold text-slate-950">
            {s.onboarding.estimateSentence(months)}
          </p>
          <p className="mt-1 text-xs font-medium text-slate-400">
            {s.onboarding.estimatePace(studyDays.length, formatSessionDuration(sessionMinutes, s, "long"))}
          </p>
        </div>
      )}
    </div>
  );
}

function LangFlag({ code }: { code: string }) {
  const s = useStrings();
  const countryCode = code === "PT" ? "br" : code === "EN" ? "us" : code.toLowerCase();
  return (
    <img
      src={`https://flagcdn.com/w40/${countryCode}.png`}
      srcSet={`https://flagcdn.com/w80/${countryCode}.png 2x`}
      alt={s.onboarding.flagAlt(code)}
      width={26}
      height={17}
      className="shrink-0 rounded object-cover shadow-sm ring-1 ring-black/[0.08]"
    />
  );
}

function Section({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div className="flex flex-col gap-2.5">
      <p className="text-xs font-semibold uppercase tracking-wide text-slate-400">{label}</p>
      {children}
    </div>
  );
}

function LoadingDots() {
  return (
    <span className="flex items-center gap-1.5">
      {[0, 1, 2].map((i) => (
        <span
          key={i}
          className="h-1.5 w-1.5 rounded-full bg-current opacity-70"
          style={{ animation: "loadingDot 1.2s ease-in-out infinite", animationDelay: `${i * 0.2}s` }}
        />
      ))}
    </span>
  );
}
