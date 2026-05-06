import { ArrowRight } from "lucide-react";
import { useState } from "react";

import { useStrings } from "../../contexts/StringsContext";
import { contentService } from "../../services/contentService";
import type { Goal } from "../../types/content";
import BottomModal from "./BottomModal";

interface EditRoutineModalProps {
  goal: Goal;
  onClose: () => void;
  onSaved: (goal: Goal) => void;
}

const WEEKDAYS = [0, 1, 2, 3, 4, 5, 6];
const SESSION_OPTIONS = [15, 30, 45, 60, 90];

function formatMinutes(min: number) {
  if (min === 60) return "1h";
  if (min === 90) return "1h30";
  return `${min} min`;
}

export default function EditRoutineModal({ goal, onClose, onSaved }: EditRoutineModalProps) {
  const s = useStrings();
  const [days, setDays] = useState(goal.study_weekdays);
  const [minutes, setMinutes] = useState(goal.session_minutes);
  const [loading, setLoading] = useState(false);

  function toggleDay(d: number) {
    setDays((curr) =>
      curr.includes(d) ? curr.filter((x) => x !== d) : [...curr, d].sort((a, b) => a - b)
    );
  }

  async function submit() {
    if (days.length === 0) return;
    setLoading(true);
    try {
      const updated = await contentService.updateGoal(goal.id, {
        study_weekdays: days,
        session_minutes: minutes,
      });
      onSaved(updated);
      onClose();
    } finally {
      setLoading(false);
    }
  }

  return (
    <BottomModal title={s.profile.editRoutineTitle} onClose={onClose}>
      <div className="flex flex-col gap-6">

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

        <button
          type="button"
          onClick={submit}
          disabled={loading || days.length === 0}
          className="auth-submit"
        >
          {loading ? (
            <LoadingDots />
          ) : (
            <>{s.profile.saveRoutine} <ArrowRight size={17} strokeWidth={2.5} /></>
          )}
        </button>
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
