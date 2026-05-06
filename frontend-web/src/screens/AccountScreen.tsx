import {
  BookOpen,
  ChevronRight,
  Clock,
  Flame,
  Globe,
  Key,
  LogOut,
  Mail,
  Plus,
  Sparkles,
  Trash2,
} from "lucide-react";
import { useState } from "react";

import { useStrings } from "../contexts/StringsContext";
import AddAreaModal from "../components/ui/AddAreaModal";
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
}

const FLAGS: Record<string, string> = { DE: "🇩🇪", ES: "🇪🇸", EN: "🇺🇸", PT: "🇧🇷" };

function userInitial(username: string) {
  return username.charAt(0).toUpperCase();
}

function formatMinutes(min: number) {
  if (min === 60) return "1h";
  if (min === 90) return "1h30";
  return `${min} min`;
}

export default function AccountScreen({ user, goals, onCreateGoal, onUpdateGoal, onDeleteGoal, onLogout, onSwitchGoal, onViewHistory }: AccountScreenProps) {
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

        {/* User card */}
        <section className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
          <div className="flex items-center gap-4">
            <div className="profile-avatar">{userInitial(user.username)}</div>
            <div>
              <p className="text-lg font-bold text-slate-950">{user.username}</p>
              <p className="text-sm font-medium text-slate-500">{user.email || s.profile.noEmail}</p>
              <p className="mt-0.5 text-xs text-slate-400">{s.profile.memberLabel}</p>
            </div>
          </div>
        </section>

        {/* Stats */}
        {activeGoal && (
          <section className="grid grid-cols-3 gap-px overflow-hidden rounded-xl border border-slate-200 bg-slate-200">
            <StatCell icon={<Flame size={16} />} iconClass="bg-orange-50 text-orange-500" value={String(activeGoal.streak_days)} label={s.profile.statStreak} />
            <StatCell icon={<BookOpen size={16} />} iconClass="bg-blue-50 text-blue-500" value={String(activeGoal.completed_lessons)} label={s.profile.statPhrases} />
            <StatCell icon={<Sparkles size={16} />} iconClass="area-bg-soft" value={activeGoal.target_level} label={s.profile.statLevel} valueClass="area-text-primary" />
          </section>
        )}

        {/* Meu curso */}
        {activeGoal && (
          <section className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2 text-sm font-bold text-slate-950">
                <span className="area-bg-soft flex h-[22px] w-[22px] items-center justify-center rounded-full">
                  <Globe size={13} />
                </span>
                {FLAGS[targetCode]} {targetName}
              </div>
              <span className="area-bg-soft rounded-full px-2.5 py-0.5 text-xs font-semibold">
                {sourceCode} → {targetCode}
              </span>
            </div>

            <div className="mt-3 h-1.5 overflow-hidden rounded-full bg-slate-100">
              <div className="h-full rounded-full transition-all duration-500" style={{ width: `${activeGoal.progress_percent}%`, background: "var(--area-primary)" }} />
            </div>
            <div className="mt-1.5 flex justify-between text-xs">
              <span className="text-slate-500">{s.profile.progressLabel(activeGoal.target_level, activeGoal.progress_percent)}</span>
              <span className="area-text-primary font-semibold">{activeGoal.progress_percent}%</span>
            </div>

            <div className="my-4 h-px bg-slate-100" />

            <div className="flex items-center gap-2">
              <Clock size={14} className="text-slate-400" />
              <span className="flex-1 text-sm font-medium text-slate-600">
                {formatDays(activeGoal.study_weekdays)} · {formatMinutes(activeGoal.session_minutes)}
              </span>
              <button type="button" onClick={() => setShowEditRoutine(true)} className="area-text-primary text-sm font-semibold">
                {s.profile.editRoutine}
              </button>
            </div>
          </section>
        )}

        {/* Atividade da semana */}
        <WeekPreview onViewAll={onViewHistory} />

        {/* Outras áreas */}
        {inactiveGoals.length > 0 && (
          <section className="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
            <p className="px-5 pt-4 pb-2 text-xs font-semibold uppercase tracking-wider text-slate-400">{s.profile.otherAreas}</p>
            {inactiveGoals.map((goal, i) => {
              const tc = goal.target_language?.code ?? "";
              const sc = goal.source_language?.code ?? "";
              const name = s.languages[tc as keyof typeof s.languages] ?? tc;
              return (
                <div key={goal.id} className={`flex items-center gap-3 px-5 py-3.5 ${i > 0 ? "border-t border-slate-100" : ""}`}>
                  <span className="text-xl">{FLAGS[tc] ?? "🌐"}</span>
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

        {/* Conta */}
        <section className="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
          <p className="px-5 pt-4 pb-2 text-xs font-semibold uppercase tracking-wider text-slate-400">{s.profile.accountSection}</p>
          <AccountRow icon={<Mail size={16} className="text-slate-400" />} text={user.email || s.profile.noEmail} />
          <AccountRow icon={<Key size={16} className="text-slate-400" />} text={s.profile.changePassword} chev />
          <AccountRow icon={<LogOut size={16} className="text-red-500" />} text={s.profile.signOut} danger onClick={onLogout} />
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

function WeekPreview({ onViewAll }: { onViewAll: () => void }) {
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

  const dayMap = new Map<string, HistoryDay>();
  if (history.data) {
    for (const goal of history.data.goals) {
      for (const day of goal.days) {
        const ex = dayMap.get(day.date);
        if (!ex) {
          dayMap.set(day.date, { ...day });
        } else {
          ex.completed = ex.completed || day.completed;
          ex.planned = ex.planned || day.planned;
          ex.completion_count += day.completion_count;
        }
      }
    }
  }

  return (
    <section className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
      <div className="flex items-center justify-between">
        <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">{s.profile.weekActivity}</p>
        <button type="button" onClick={onViewAll} className="text-xs font-semibold area-text-primary">
          {s.profile.viewHistory}
        </button>
      </div>

      <div className="mt-3 grid grid-cols-7 gap-1">
        {last7.map((dateStr) => {
          const day = dayMap.get(dateStr);
          const d = new Date(`${dateStr}T12:00:00`);
          const jsDay = d.getDay();
          const weekdayIdx = jsDay === 0 ? 6 : jsDay - 1;
          return (
            <div key={dateStr} className="flex flex-col items-center gap-1">
              <div
                className={`flex h-9 w-full items-center justify-center rounded-lg text-xs font-bold transition ${
                  day?.completed ? "text-white" : day?.planned ? "bg-slate-100 text-slate-600" : "bg-slate-50 text-slate-300"
                }`}
                style={day?.completed ? { background: "var(--area-primary)" } : undefined}
              >
                {d.getDate()}
              </div>
              <p className="text-[9px] font-semibold uppercase text-slate-400">{s.weekdays.short[weekdayIdx]}</p>
            </div>
          );
        })}
      </div>
    </section>
  );
}

// ── Sub-components ────────────────────────────────────────

function StatCell({ icon, iconClass, value, label, valueClass = "text-slate-950" }: {
  icon: React.ReactNode; iconClass: string; value: string; label: string; valueClass?: string;
}) {
  return (
    <div className="flex flex-col items-center gap-1.5 bg-white px-2 py-4">
      <div className={`flex h-8 w-8 items-center justify-center rounded-full ${iconClass}`}>{icon}</div>
      <p className={`text-xl font-bold ${valueClass}`}>{value}</p>
      <p className="text-center text-[11px] font-semibold uppercase tracking-wide text-slate-400">{label}</p>
    </div>
  );
}

function AccountRow({ icon, text, chev, danger, onClick }: {
  icon: React.ReactNode; text: string; chev?: boolean; danger?: boolean; onClick?: () => void;
}) {
  return (
    <button type="button" onClick={onClick} className="flex w-full items-center gap-3 border-t border-slate-100 px-5 py-3.5 text-left transition first:border-t-0 hover:bg-slate-50">
      {icon}
      <span className={`flex-1 text-sm ${danger ? "font-semibold text-red-500" : "font-medium text-slate-700"}`}>{text}</span>
      {chev && <ChevronRight size={14} className="text-slate-300" />}
    </button>
  );
}
