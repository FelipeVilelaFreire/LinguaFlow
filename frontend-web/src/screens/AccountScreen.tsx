import { CheckCircle2, LogOut, Plus, Trash2, UserCircle } from "lucide-react";
import { useState } from "react";

import ProgressBar from "../components/ui/ProgressBar";
import { useStrings } from "../contexts/StringsContext";
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

const TARGET_LANGUAGES = [
  { code: "DE", label: "Alemao" },
  { code: "ES", label: "Espanhol" },
  { code: "EN", label: "Ingles" },
];

export default function AccountScreen({ user, goals, onCreateGoal, onDeleteGoal, onLogout, onSwitchGoal }: AccountScreenProps) {
  const strings = useStrings();
  const [targetLanguage, setTargetLanguage] = useState("DE");
  const [durationDays, setDurationDays] = useState(30);
  const [creating, setCreating] = useState(false);

  async function createGoal() {
    setCreating(true);
    try {
      const goal = await contentService.createGoal({
        source_language: "PT",
        target_language: targetLanguage,
        target_level: "A1",
        duration_days: durationDays,
      });
      onCreateGoal(goal);
    } finally {
      setCreating(false);
    }
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
            <h3 className="text-xl font-semibold">{strings.profile.newArea}</h3>
            <div className="mt-4 grid gap-3">
              <select value={targetLanguage} onChange={(event) => setTargetLanguage(event.target.value)} className="h-12 rounded-[8px] border border-slate-200 bg-white px-3 font-medium outline-none">
                {TARGET_LANGUAGES.map((item) => (
                  <option key={item.code} value={item.code}>{`PT -> ${item.label}`}</option>
                ))}
              </select>
              <select value={durationDays} onChange={(event) => setDurationDays(Number(event.target.value))} className="h-12 rounded-[8px] border border-slate-200 bg-white px-3 font-medium outline-none">
                <option value={30}>30 dias</option>
                <option value={60}>60 dias</option>
                <option value={90}>90 dias</option>
              </select>
              <button type="button" onClick={createGoal} disabled={creating} className="inline-flex h-12 items-center justify-center gap-2 rounded-[8px] px-5 font-semibold text-white shadow-sm transition hover:brightness-95 disabled:opacity-60" style={{ background: "var(--area-primary)" }}>
                <Plus size={18} />
                {creating ? strings.actions.creating : strings.actions.createArea}
              </button>
            </div>
          </div>
        </div>

        <div className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
          <h3 className="text-xl font-semibold">{strings.profile.yourAreas}</h3>
          <div className="mt-4 grid gap-3">
            {goals.map((goal) => (
              <AreaRow key={goal.id} goal={goal} onDelete={() => onDeleteGoal(goal)} onSwitch={() => onSwitchGoal(goal)} />
            ))}
          </div>
        </div>
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
