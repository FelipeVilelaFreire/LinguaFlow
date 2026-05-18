"use client";

import { ROUTES, STRINGS, adventureService, authService, contentService } from "@linguaflow/shared-core";
import type { AvailableLanguage, Goal, HistoryMonth, User } from "@linguaflow/shared-core";
import { CalendarDays, ChevronRight, Clock, Plus, Trash2 } from "lucide-react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { LangFlag } from "@/src/components/shared";
import styles from "./ProfileScreen.module.css";

const WEEKDAYS = [0, 1, 2, 3, 4, 5, 6];
const SESSION_OPTIONS = [15, 30, 45, 60, 90];

export function ProfileScreen() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [goals, setGoals] = useState<Goal[]>([]);
  const [history, setHistory] = useState<HistoryMonth | null>(null);
  const [loading, setLoading] = useState(true);
  const [modal, setModal] = useState<"add" | "routine" | "delete" | null>(null);
  const [selectedGoal, setSelectedGoal] = useState<Goal | null>(null);

  useEffect(() => {
    const today = new Date();
    Promise.all([
      authService.me(),
      contentService.listGoals(),
      contentService.getHistory(today.getFullYear(), today.getMonth() + 1).catch(() => null),
    ])
      .then(([nextUser, nextGoals, nextHistory]) => {
        setUser(nextUser);
        setGoals(nextGoals);
        setHistory(nextHistory);
      })
      .finally(() => setLoading(false));
  }, []);

  async function logout() {
    await authService.logout();
    router.replace(ROUTES.login);
  }

  function upsertGoal(goal: Goal) {
    setGoals((current) => {
      const normalized = goal.is_active ? current.map((item) => ({ ...item, is_active: item.id === goal.id })) : current;
      return normalized.some((item) => item.id === goal.id)
        ? normalized.map((item) => item.id === goal.id ? goal : item)
        : [...normalized, goal];
    });
  }

  async function activateGoal(goal: Goal) {
    const updated = await contentService.activateGoal(goal.id);
    upsertGoal(updated);
  }

  async function deleteGoal(goal: Goal) {
    const result = await contentService.deleteGoal(goal.id);
    setGoals((current) => current.filter((item) => item.id !== goal.id).map((item) => ({
      ...item,
      is_active: result.current_goal?.id === item.id ? true : item.is_active,
    })));
    if (result.current_goal) upsertGoal(result.current_goal);
    setModal(null);
    setSelectedGoal(null);
  }

  if (loading) return <State message={STRINGS.profile.loading} />;
  if (!user) return <State message={STRINGS.profile.unavailable} />;

  const activeGoal = goals.find((goal) => goal.is_active);
  const inactiveGoals = goals.filter((goal) => !goal.is_active);

  return (
    <main className={styles.page}>
      <button className={styles.userCard} type="button">
        <div className={styles.avatar}>{user.username.charAt(0).toUpperCase()}</div>
        <div className={styles.userText}>
          <h1>{user.username}</h1>
          <p>{user.email || STRINGS.profile.noEmail}</p>
          <span>{STRINGS.profile.memberLabel}</span>
        </div>
        <ChevronRight size={16} />
      </button>

      {activeGoal ? (
        <ActiveGoalCard goal={activeGoal} onEdit={() => { setSelectedGoal(activeGoal); setModal("routine"); }} />
      ) : null}

      <WeekPreview activeGoal={activeGoal ?? null} history={history} />

      {inactiveGoals.length > 0 ? (
        <section className={styles.listCard}>
          <p className={styles.sectionLabel}>{STRINGS.profile.otherAreas}</p>
          {inactiveGoals.map((goal) => (
            <div className={styles.areaRow} key={goal.id}>
              <LangFlag code={goal.target_language?.code ?? ""} size="sm" />
              <div>
                <strong>{languageName(goal)}</strong>
                <span>{goal.source_language?.code} {"->"} {goal.target_language?.code} · {goal.target_level}</span>
              </div>
              <button className={styles.useButton} onClick={() => activateGoal(goal)} type="button">{STRINGS.profile.useArea}</button>
              <button className={styles.trashButton} onClick={() => { setSelectedGoal(goal); setModal("delete"); }} type="button" aria-label={STRINGS.actions.delete}>
                <Trash2 size={14} />
              </button>
            </div>
          ))}
        </section>
      ) : null}

      <button className={styles.addArea} onClick={() => setModal("add")} type="button">
        <span><Plus size={18} /></span>
        <div>
          <strong>{STRINGS.profile.addArea}</strong>
          <p>{STRINGS.profile.addAreaDetail}</p>
        </div>
        <ChevronRight size={16} />
      </button>

      <section className={styles.planCard}>
        <p>{STRINGS.profile.planLabel}</p>
        <div>
          <span>
            <strong>{STRINGS.profile.planName}</strong>
            <small>{STRINGS.profile.planDetail}</small>
          </span>
          <button type="button">{STRINGS.profile.upgrade}</button>
        </div>
      </section>

      <button className={styles.signOut} onClick={logout} type="button">{STRINGS.profile.signOut}</button>

      {modal === "add" && <AddAreaModal onClose={() => setModal(null)} onCreated={upsertGoal} />}
      {modal === "routine" && selectedGoal && <EditRoutineModal goal={selectedGoal} onClose={() => setModal(null)} onSaved={upsertGoal} />}
      {modal === "delete" && selectedGoal && (
        <ConfirmModal
          title={STRINGS.profile.deleteAreaTitle}
          detail={STRINGS.profile.deleteAreaBody(languageName(selectedGoal))}
          onCancel={() => setModal(null)}
          onConfirm={() => deleteGoal(selectedGoal)}
        />
      )}
    </main>
  );
}

function ActiveGoalCard({ goal, onEdit }: { goal: Goal; onEdit: () => void }) {
  return (
    <section className={styles.courseCard}>
      <div className={styles.courseHeader}>
        <LangFlag code={goal.target_language?.code ?? ""} size="xl" />
        <div>
          <h2>{languageName(goal)}</h2>
          <span>{goal.source_language?.code} {"->"} {goal.target_language?.code}</span>
          <small>{goal.target_level}</small>
        </div>
      </div>
      <div className={styles.divider} />
      <div className={styles.routineRow}>
        <Clock size={14} />
        <span>{formatDays(goal.study_weekdays)} · {formatMinutes(goal.session_minutes)}</span>
        <button onClick={onEdit} type="button">{STRINGS.profile.editRoutine}</button>
      </div>
    </section>
  );
}

function WeekPreview({ activeGoal, history }: { activeGoal: Goal | null; history: HistoryMonth | null }) {
  const today = new Date();
  const completedDates = new Set<string>();
  history?.goals.forEach((goal) => goal.days.forEach((day) => {
    if (day.completed) completedDates.add(day.date);
  }));
  const routineSet = new Set(activeGoal?.study_weekdays ?? []);
  const last7 = Array.from({ length: 7 }, (_, index) => {
    const date = new Date(today);
    date.setDate(today.getDate() - 6 + index);
    return date.toISOString().split("T")[0];
  });

  return (
    <section className={styles.weekCard}>
      <div className={styles.weekHeader}>
        <p>{STRINGS.profile.weekActivity}</p>
        <Link href={ROUTES.history}>{STRINGS.profile.viewHistory}</Link>
      </div>
      <div className={styles.weekGrid}>
        {last7.map((dateString) => {
          const date = new Date(`${dateString}T12:00:00`);
          const weekdayIndex = date.getDay() === 0 ? 6 : date.getDay() - 1;
          const completed = completedDates.has(dateString);
          const planned = routineSet.has(weekdayIndex);
          return (
            <div className={styles.weekDay} key={dateString}>
              <span className={completed ? styles.completedDay : planned ? styles.plannedDay : ""}>{date.getDate()}</span>
              <small>{STRINGS.weekdays.short[weekdayIndex]}</small>
            </div>
          );
        })}
      </div>
    </section>
  );
}

function AddAreaModal({ onClose, onCreated }: { onClose: () => void; onCreated: (goal: Goal) => void }) {
  const [languages, setLanguages] = useState<AvailableLanguage[]>([]);
  const [target, setTarget] = useState<AvailableLanguage | null>(null);
  const [days, setDays] = useState([0, 2, 4]);
  const [minutes, setMinutes] = useState(30);
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    adventureService.listAvailableLanguages().then((items) => {
      setLanguages(items);
      if (items[0]) setTarget(items[0]);
    });
  }, []);

  async function submit() {
    if (!target || days.length === 0) return;
    setSaving(true);
    try {
      const goal = await contentService.createGoal({
        source_language: "PT",
        target_language: target.code,
        target_level: "A1",
        duration_days: 90,
        study_weekdays: days,
        session_minutes: minutes,
      });
      onCreated(goal);
      onClose();
    } finally {
      setSaving(false);
    }
  }

  return (
    <Modal title={STRINGS.profile.addAreaTitle} onClose={onClose}>
      <Section label={STRINGS.profile.learnTarget}>
        {languages.map((language) => (
          <button className={`${styles.selectCard} ${target?.code === language.code ? styles.selected : ""}`} key={language.code} onClick={() => setTarget(language)} type="button">
            <LangFlag code={language.code} size="sm" />
            <span><strong>{STRINGS.languages[language.code as keyof typeof STRINGS.languages] ?? language.code}</strong><small>{language.chapter_subtitle || language.chapter_title}</small></span>
          </button>
        ))}
      </Section>
      <RoutineFields days={days} minutes={minutes} onToggleDay={(day) => setDays(toggleDay(days, day))} onMinutes={setMinutes} />
      <button className={styles.modalPrimary} disabled={saving || !target || days.length === 0} onClick={submit} type="button">
        {saving ? STRINGS.profile.saving : STRINGS.profile.addArea}
      </button>
    </Modal>
  );
}

function EditRoutineModal({ goal, onClose, onSaved }: { goal: Goal; onClose: () => void; onSaved: (goal: Goal) => void }) {
  const [days, setDays] = useState(goal.study_weekdays);
  const [minutes, setMinutes] = useState(goal.session_minutes);
  const [saving, setSaving] = useState(false);

  async function submit() {
    if (days.length === 0) return;
    setSaving(true);
    try {
      const updated = await contentService.updateGoal(goal.id, { study_weekdays: days, session_minutes: minutes });
      onSaved(updated);
      onClose();
    } finally {
      setSaving(false);
    }
  }

  return (
    <Modal title={STRINGS.profile.editRoutineTitle} onClose={onClose}>
      <RoutineFields days={days} minutes={minutes} onToggleDay={(day) => setDays(toggleDay(days, day))} onMinutes={setMinutes} />
      {days.length === 0 ? <p className={styles.errorText}>{STRINGS.profile.chooseDayError}</p> : null}
      <button className={styles.modalPrimary} disabled={saving || days.length === 0} onClick={submit} type="button">
        {saving ? STRINGS.profile.saving : STRINGS.profile.saveRoutine}
      </button>
    </Modal>
  );
}

function ConfirmModal({ title, detail, onCancel, onConfirm }: { title: string; detail: string; onCancel: () => void; onConfirm: () => void }) {
  return (
    <Modal title={title} onClose={onCancel}>
      <p className={styles.modalDetail}>{detail}</p>
      <div className={styles.modalActions}>
        <button onClick={onCancel} type="button">{STRINGS.profile.cancelAction}</button>
        <button className={styles.danger} onClick={onConfirm} type="button">{STRINGS.actions.delete}</button>
      </div>
    </Modal>
  );
}

function RoutineFields({ days, minutes, onToggleDay, onMinutes }: { days: number[]; minutes: number; onToggleDay: (day: number) => void; onMinutes: (minutes: number) => void }) {
  return (
    <>
      <Section label={STRINGS.profile.studyDays}>
        <div className={styles.dayGrid}>
          {WEEKDAYS.map((day) => (
            <button className={days.includes(day) ? styles.selectedDay : ""} key={day} onClick={() => onToggleDay(day)} type="button">
              {STRINGS.weekdays.short[day]}
            </button>
          ))}
        </div>
      </Section>
      <Section label={STRINGS.profile.duration}>
        <div className={styles.pillGrid}>
          {SESSION_OPTIONS.map((option) => (
            <button className={minutes === option ? styles.selected : ""} key={option} onClick={() => onMinutes(option)} type="button">
              {formatMinutes(option)}
            </button>
          ))}
        </div>
      </Section>
    </>
  );
}

function Modal({ title, children, onClose }: { title: string; children: React.ReactNode; onClose: () => void }) {
  return (
    <div className={styles.modalBackdrop}>
      <div className={styles.modalPanel}>
        <header>
          <h2>{title}</h2>
          <button onClick={onClose} type="button">{STRINGS.profile.close}</button>
        </header>
        {children}
      </div>
    </div>
  );
}

function Section({ label, children }: { label: string; children: React.ReactNode }) {
  return <section className={styles.modalSection}><p>{label}</p>{children}</section>;
}

function State({ message }: { message: string }) {
  return <main className={styles.page}><p>{message}</p></main>;
}

function toggleDay(current: number[], day: number) {
  return current.includes(day) ? current.filter((item) => item !== day) : [...current, day].sort((a, b) => a - b);
}

function languageName(goal: Goal) {
  const code = goal.target_language?.code ?? "";
  return STRINGS.languages[code as keyof typeof STRINGS.languages] ?? goal.target_language?.name ?? code;
}

function formatDays(days: number[]) {
  if (days.length === 0) return STRINGS.profile.casualStudy;
  if (days.length === 7) return STRINGS.profile.allDays;
  return days.map((day) => STRINGS.weekdays.short[day]).join(", ");
}

function formatMinutes(minutes: number) {
  if (minutes === 60) return STRINGS.onboarding.hourShort;
  if (minutes === 90) return STRINGS.onboarding.hourAndHalfShort;
  return STRINGS.onboarding.minutesShort(minutes);
}

