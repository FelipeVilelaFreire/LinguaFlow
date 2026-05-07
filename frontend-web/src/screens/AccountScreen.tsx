import {
  ChevronRight,
  Clock,
  Plus,
  Trash2,
} from "lucide-react";
import { useState } from "react";

import { useStrings } from "../contexts/StringsContext";
import AddAreaModal from "../components/ui/AddAreaModal";
import LangFlag from "../components/ui/LangFlag";
import EditRoutineModal from "../components/ui/EditRoutineModal";
import WarningModal from "../components/ui/WarningModal";
import { useAsyncData } from "../hooks/useAsyncData";
import { contentService } from "../services/contentService";
import type { User } from "../services/authService";
import type { Goal, HistoryDay } from "../types/content";

interface AccountScreenProps {
  user: User;
  goals: Goal[];
  onCreateGoal: (goal: Goal) => void;
  onUpdateGoal: (goal: Goal) => void;
  onDeleteGoal: (goal: Goal) => void;
  onLogout: () => void;
  onSwitchGoal: (goal: Goal) => void;
  onViewHistory: () => void;
  onEditProfile: () => void;
}


function userInitial(username: string) {
  return username.charAt(0).toUpperCase();
}

function formatMinutes(min: number) {
  if (min === 60) return "1h";
  if (min === 90) return "1h30";
  return `${min} min`;
}

export default function AccountScreen({ user, goals, onCreateGoal, onUpdateGoal, onDeleteGoal, onLogout: _onLogout, onSwitchGoal, onViewHistory, onEditProfile }: AccountScreenProps) {
  const s = useStrings();
  const [goalToDelete, setGoalToDelete] = useState<Goal | null>(null);
  const [showAddArea, setShowAddArea] = useState(false);
  const [showEditRoutine, setShowEditRoutine] = useState(false);

  const activeGoal = goals.find((g) => g.is_active);
  const inactiveGoals = goals.filter((g) => !g.is_active);
  const targetCode = activeGoal?.target_language?.code ?? "";
  const sourceCode = activeGoal?.source_language?.code ?? "";
  const targetName = s.languages[targetCode as keyof typeof s.languages] ?? targetCode;

  function formatDays(days: number[]) {
    if (days.length === 0) return s.profile.casualStudy;
    if (days.length === 7) return s.profile.allDays;
    return days.map((d) => s.weekdays.short[d]).join(", ");
  }

  return (
    <div className="pb-4">
      <div className="flex flex-col gap-3">

        {/* User card — tappable → Edit profile */}
        <button type="button" onClick={onEditProfile} className="card w-full p-5 text-left transition hover:bg-slate-50 active:scale-[0.99]">
          <div className="flex items-center gap-4">
            <div className="profile-avatar">{userInitial(user.username)}</div>
            <div className="flex-1 min-w-0">
              <p className="text-lg font-bold text-slate-950">{user.username}</p>
              <p className="text-sm font-medium text-slate-500">{user.email || s.profile.noEmail}</p>
              <p className="mt-0.5 text-xs text-slate-400">{s.profile.memberLabel}</p>
            </div>
            <ChevronRight size={16} className="shrink-0 text-slate-300" />
          </div>
        </button>

        {/* Meu curso */}
        {activeGoal && (
          <section className="card p-5">
            <div className="flex items-start gap-4">
              <LangFlag code={targetCode} size="xl" className="shrink-0 mt-0.5" />
              <div className="flex-1 min-w-0">
                <p className="text-xl font-bold text-slate-950 leading-tight">{targetName}</p>
                <div className="mt-1 flex items-center gap-2 flex-wrap">
                  <span className="area-bg-soft rounded-full px-2.5 py-0.5 text-xs font-semibold area-text-primary">
                    {sourceCode} → {targetCode}
                  </span>
                  <span className="text-xs font-semibold text-slate-400">{activeGoal.target_level}</span>
                </div>
              </div>
            </div>

            <div className="my-4 h-px bg-slate-100" />

            <div className="flex items-center gap-2">
              <Clock size={14} className="shrink-0 text-slate-400" />
              <span className="flex-1 text-sm font-medium text-slate-600">
                {formatDays(activeGoal.study_weekdays)} · {formatMinutes(activeGoal.session_minutes)}
              </span>
              <button type="button" onClick={() => setShowEditRoutine(true)} className="area-text-primary text-sm font-semibold shrink-0">
                {s.profile.editRoutine}
              </button>
            </div>
          </section>
        )}

        {/* Atividade da semana */}
        <WeekPreview onViewAll={onViewHistory} activeGoal={activeGoal ?? null} />

        {/* Outras áreas */}
        {inactiveGoals.length > 0 && (
          <section className="card-overflow">
            <p className="px-5 pt-4 pb-2 text-xs font-semibold uppercase tracking-wider text-slate-400">{s.profile.otherAreas}</p>
            {inactiveGoals.map((goal, i) => {
              const tc = goal.target_language?.code ?? "";
              const sc = goal.source_language?.code ?? "";
              const name = s.languages[tc as keyof typeof s.languages] ?? tc;
              return (
                <div key={goal.id} className={`flex items-center gap-3 px-5 py-3.5 ${i > 0 ? "border-t border-slate-100" : ""}`}>
                  <LangFlag code={tc} size="sm" className="shrink-0" />
                  <div className="flex-1">
                    <p className="text-sm font-semibold text-slate-950">{name}</p>
                    <p className="text-xs text-slate-400">{sc} → {tc} · {goal.target_level}</p>
                  </div>
                  <button type="button" onClick={() => onSwitchGoal(goal)} className="auth-submit rounded-lg px-3" style={{ height: "32px", width: "auto", fontSize: "12px" }}>
                    {s.actions.use}
                  </button>
                  <button type="button" onClick={() => setGoalToDelete(goal)} className="flex h-8 w-8 items-center justify-center rounded-lg border border-red-100 bg-white text-red-500 transition hover:bg-red-50">
                    <Trash2 size={14} />
                  </button>
                </div>
              );
            })}
          </section>
        )}

        {/* Adicionar área */}
        <button type="button" onClick={() => setShowAddArea(true)} className="profile-add-area">
          <div className="profile-add-icon"><Plus size={18} /></div>
          <div className="flex-1">
            <p className="text-sm font-bold text-slate-950">{s.profile.addArea}</p>
            <p className="mt-0.5 text-xs text-slate-500">{s.profile.addAreaDetail}</p>
          </div>
          <ChevronRight size={16} className="text-slate-300" />
        </button>

        {/* Plano */}
        <section className="card p-5">
          <p className="text-xs font-semibold uppercase tracking-widest text-slate-400">{s.profile.planLabel}</p>
          <div className="mt-2 flex items-center justify-between gap-3">
            <div>
              <p className="font-bold text-slate-950">{s.profile.planName}</p>
              <p className="mt-0.5 text-sm font-medium text-slate-500">{s.profile.planDetail}</p>
            </div>
            <button type="button" className="area-bg-soft rounded-[8px] px-3 py-2 text-xs font-bold area-text-primary transition">
              Upgrade
            </button>
          </div>
        </section>

      </div>

      {showAddArea && (
        <AddAreaModal
          onClose={() => setShowAddArea(false)}
          onCreated={(goal) => { onCreateGoal(goal); setShowAddArea(false); }}
        />
      )}

      {showEditRoutine && activeGoal && (
        <EditRoutineModal
          goal={activeGoal}
          onClose={() => setShowEditRoutine(false)}
          onSaved={(updated) => { onUpdateGoal(updated); setShowEditRoutine(false); }}
        />
      )}

      {goalToDelete && (
        <WarningModal
          title={s.profile.deleteAreaTitle}
          detail={s.profile.deleteAreaBody(s.languages[goalToDelete.target_language?.code as keyof typeof s.languages] ?? goalToDelete.target_language?.code ?? "")}
          cancelLabel={s.profile.cancelAction}
          confirmLabel={s.actions.delete}
          onCancel={() => setGoalToDelete(null)}
          onConfirm={() => { onDeleteGoal(goalToDelete); setGoalToDelete(null); }}
        />
      )}
    </div>
  );
}

// ── WeekPreview ───────────────────────────────────────────

function WeekPreview({ onViewAll, activeGoal }: { onViewAll: () => void; activeGoal: Goal | null }) {
  const s = useStrings();
  const today = new Date();
  const history = useAsyncData(
    () => contentService.getHistory(today.getFullYear(), today.getMonth() + 1),
    [today.getFullYear(), today.getMonth() + 1]
  );

  const last7 = Array.from({ length: 7 }, (_, i) => {
    const d = new Date(today);
    d.setDate(today.getDate() - 6 + i);
    return d.toISOString().split("T")[0];
  });

  // Build completion map from API
  const completedDates = new Set<string>();
  if (history.data) {
    for (const goal of history.data.goals) {
      for (const day of goal.days) {
        if (day.completed) completedDates.add(day.date);
      }
    }
  }

  // Routine days come directly from study_weekdays (Mon=0 … Sun=6)
  const routineSet = new Set(activeGoal?.study_weekdays ?? []);
  const hasRoutine = routineSet.size > 0;

  return (
    <section className="card p-5">
      <div className="flex items-center justify-between">
        <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">{s.profile.weekActivity}</p>
        <button type="button" onClick={onViewAll} className="text-xs font-semibold area-text-primary">
          {s.profile.viewHistory}
        </button>
      </div>

      <div className="mt-3 grid grid-cols-7 gap-1">
        {last7.map((dateStr) => {
          const d = new Date(`${dateStr}T12:00:00`);
          const jsDay = d.getDay();
          const weekdayIdx = jsDay === 0 ? 6 : jsDay - 1;
          const isCompleted = completedDates.has(dateStr);
          const isRoutine = hasRoutine && routineSet.has(weekdayIdx);

          return (
            <div key={dateStr} className="flex flex-col items-center gap-1">
              <div
                className={`flex h-9 w-full items-center justify-center rounded-lg text-xs font-bold transition ${
                  isCompleted
                    ? "text-white"
                    : isRoutine
                      ? "bg-slate-100 text-slate-600 ring-1 ring-slate-200"
                      : "text-slate-300"
                }`}
                style={isCompleted ? { background: "var(--area-primary)" } : undefined}
              >
                {d.getDate()}
              </div>
              <p className={`text-[9px] font-semibold uppercase ${isRoutine || isCompleted ? "text-slate-400" : "text-slate-300"}`}>
                {s.weekdays.short[weekdayIdx]}
              </p>
            </div>
          );
        })}
      </div>
    </section>
  );
}

