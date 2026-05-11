import { ArrowRight, Check } from "lucide-react";
import { useEffect, useState } from "react";

import { useStrings } from "../../contexts/StringsContext";
import { adventureService } from "../../services/adventureService";
import { contentService } from "../../services/contentService";
import type { AvailableLanguage } from "../../types/adventure";
import type { Goal } from "../../types/content";
import BottomModal from "./BottomModal";
import LangFlag from "./LangFlag";

interface AddAreaModalProps {
  onClose: () => void;
  onCreated: (goal: Goal) => void;
}

const SOURCE_LANGUAGES = [
  { code: "PT", labelKey: "PT" as const, detail: "Explicações em português" },
];

const LEVELS = [
  { code: "A1", labelKey: "levelIniciante" as const },
];

const WEEKDAYS = [0, 1, 2, 3, 4, 5, 6];
const SESSION_OPTIONS = [15, 30, 45, 60, 90];

function estimateMonths(days: number[], minutes: number) {
  if (days.length === 0) return null;
  const weeks = 80 / ((days.length * minutes) / 60);
  return Math.max(1, Math.round(weeks / 4.3));
}

function formatMinutes(min: number) {
  if (min === 60) return "1h";
  if (min === 90) return "1h30";
  return `${min} min`;
}

export default function AddAreaModal({ onClose, onCreated }: AddAreaModalProps) {
  const s = useStrings();

  const [source, setSource] = useState(SOURCE_LANGUAGES[0]);
  const [target, setTarget] = useState<AvailableLanguage | null>(null);
  const [level, setLevel] = useState(LEVELS[0]);
  const [days, setDays] = useState([0, 2, 4]);
  const [minutes, setMinutes] = useState(30);
  const [loading, setLoading] = useState(false);
  const [availableTargets, setAvailableTargets] = useState<AvailableLanguage[]>([]);
  const [loadingLanguages, setLoadingLanguages] = useState(true);

  useEffect(() => {
    adventureService.listAvailableLanguages()
      .then((langs) => {
        setAvailableTargets(langs);
        if (langs.length > 0) setTarget(langs[0]);
      })
      .finally(() => setLoadingLanguages(false));
  }, []);

  const months = estimateMonths(days, minutes);

  function toggleDay(d: number) {
    setDays((curr) =>
      curr.includes(d) ? curr.filter((x) => x !== d) : [...curr, d].sort((a, b) => a - b)
    );
  }

  async function submit() {
    if (days.length === 0 || !target) return;
    setLoading(true);
    try {
      const goal = await contentService.createGoal({
        source_language: source.code,
        target_language: target.code,
        target_level: level.code,
        duration_days: 90,
        study_weekdays: days,
        session_minutes: minutes,
      });
      onCreated(goal);
      onClose();
    } finally {
      setLoading(false);
    }
  }

  const footer = (
    <button
      type="button"
      onClick={submit}
      disabled={loading || days.length === 0 || !target}
      className="auth-submit"
    >
      {loading ? <LoadingDots /> : <>{s.onboarding.addAreaCta} <ArrowRight size={17} strokeWidth={2.5} /></>}
    </button>
  );

  return (
    <BottomModal title={s.onboarding.addAreaTitle} onClose={onClose} footer={footer}>
      <div className="flex flex-col gap-6">

        {/* Idioma de origem */}
        <ModalSection label={s.onboarding.youSpeak}>
          <div className="flex flex-col gap-2">
            {SOURCE_LANGUAGES.map((lang) => (
              <LangCard
                key={lang.code}
                code={lang.code}
                name={s.languages[lang.labelKey]}
                detail={lang.detail}
                selected={source.code === lang.code}
                onClick={() => setSource(lang)}
              />
            ))}
          </div>
        </ModalSection>

        {/* Idioma de destino */}
        <ModalSection label={s.onboarding.youLearn}>
          {loadingLanguages ? (
            <div className="flex items-center gap-2 py-4 text-sm text-slate-400">
              <LoadingDots /> Carregando...
            </div>
          ) : (
            <div className="flex flex-col gap-2">
              {availableTargets.map((lang) => (
                <LangCard
                  key={lang.code}
                  code={lang.code}
                  name={s.languages[lang.code as keyof typeof s.languages] ?? lang.code}
                  detail={lang.chapter_subtitle || lang.chapter_title}
                  selected={target?.code === lang.code}
                  onClick={() => setTarget(lang)}
                />
              ))}
            </div>
          )}
        </ModalSection>

        {/* Nível inicial */}
        <ModalSection label={s.onboarding.levelLabel}>
          <div className="flex gap-2">
            {LEVELS.map((l) => (
              <button
                key={l.code}
                type="button"
                onClick={() => setLevel(l)}
                className={`onb-pill flex-1 py-2.5 text-center ${level.code === l.code ? "selected" : ""}`}
              >
                <span className="block text-sm font-bold">{l.code}</span>
                <span className="block text-[11px] font-medium text-slate-500">
                  {s.onboarding[l.labelKey as keyof typeof s.onboarding] as string ?? ""}
                </span>
              </button>
            ))}
          </div>
        </ModalSection>

        <div className="h-px bg-slate-100" />

        {/* Dias de estudo */}
        <ModalSection label={s.onboarding.daysLabel}>
          <div className="flex justify-between">
            {WEEKDAYS.map((d) => (
              <button
                key={d}
                type="button"
                onClick={() => toggleDay(d)}
                className={`onb-day-pill ${days.includes(d) ? "selected" : ""}`}
              >
                {s.weekdays.short[d]}
              </button>
            ))}
          </div>
          {days.length === 0 && (
            <p className="mt-2 text-xs font-semibold text-red-500">{s.profile.chooseDayError}</p>
          )}
        </ModalSection>

        {/* Duração */}
        <ModalSection label={s.onboarding.durationLabel}>
          <div className="flex flex-wrap gap-2">
            {SESSION_OPTIONS.map((opt) => (
              <button
                key={opt}
                type="button"
                onClick={() => setMinutes(opt)}
                className={`onb-pill ${minutes === opt ? "selected" : ""}`}
              >
                {formatMinutes(opt)}
              </button>
            ))}
          </div>
        </ModalSection>

        {/* Estimativa */}
        {months !== null && (
          <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
            <p className="text-sm font-semibold text-slate-950">{s.onboarding.estimateMonths(months)}</p>
            <p className="mt-1 text-xs font-medium text-slate-400">
              {s.onboarding.estimateDetail(days.length, formatMinutes(minutes))}
            </p>
          </div>
        )}

      </div>
    </BottomModal>
  );
}

function ModalSection({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div className="flex flex-col gap-2.5">
      <p className="text-xs font-semibold uppercase tracking-wide text-slate-400">{label}</p>
      {children}
    </div>
  );
}

function LangCard({ code, name, detail, selected, onClick }: {
  code: string;
  name: string;
  detail: string;
  selected: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={`onb-select-card ${selected ? "selected" : ""}`}
    >
      <LangFlag code={code} size="sm" className="shrink-0" />
      <div className="flex-1 text-left">
        <p className="text-sm font-bold text-slate-950">{name}</p>
        <p className="text-xs font-medium text-slate-500">{detail}</p>
      </div>
      {selected && <Check size={16} className="shrink-0 area-text-primary" />}
    </button>
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
