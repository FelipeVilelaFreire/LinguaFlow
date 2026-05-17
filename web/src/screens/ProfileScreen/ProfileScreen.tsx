"use client";

import { ROUTES, STRINGS, adventureService, authService, contentService } from "@linguaflow/shared-core";
import type { AvailableLanguage, Goal, User } from "@linguaflow/shared-core";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import styles from "./ProfileScreen.module.css";

const WEEKDAYS = [0, 1, 2, 3, 4, 5, 6];
const SESSION_OPTIONS = [15, 30, 45, 60, 90];

export function ProfileScreen() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [goals, setGoals] = useState<Goal[]>([]);
  const [loading, setLoading] = useState(true);
  const [modal, setModal] = useState<"add" | "routine" | "delete" | null>(null);
  const [selectedGoal, setSelectedGoal] = useState<Goal | null>(null);

  useEffect(() => {
    Promise.all([authService.me(), contentService.listGoals()])
      .then(([nextUser, nextGoals]) => {
        setUser(nextUser);
        setGoals(nextGoals);
      })
      .finally(() => setLoading(false));
  }, []);

  async function logout() {
    await authService.logout();
    router.replace(ROUTES.login);
  }

  function upsertGoal(goal: Goal) {
    setGoals((current) => {
      const exists = current.some((item) => item.id === goal.id);
      return exists ? current.map((item) => item.id === goal.id ? goal : item) : [...current, goal];
    });
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

  if (loading) return <State message="Carregando perfil..." />;
  if (!user) return <State message="Perfil indisponivel." />;

  const activeGoal = goals.find((goal) => goal.is_active);

  return (
    <main className={styles.page}>
      <section className={styles.userCard}>
        <div className={styles.avatar}>{user.username.charAt(0).toUpperCase()}</div>
        <div>
          <h1>{user.username}</h1>
          <p>{user.email || "Sem email"}</p>
        </div>
        <button onClick={logout} type="button">Sair</button>
      </section>

      {activeGoal && (
        <section className={styles.card}>
          <p>Curso ativo</p>
          <h2>{activeGoal.target_language?.name ?? activeGoal.target_language?.code}</h2>
          <span>{activeGoal.source_language?.code} {"->"} {activeGoal.target_language?.code} · {activeGoal.target_level}</span>
          <div className={styles.progress}><div style={{ width: `${activeGoal.progress_percent}%` }} /></div>
          <button className={styles.inlineAction} onClick={() => { setSelectedGoal(activeGoal); setModal("routine"); }} type="button">
            Editar rotina
          </button>
        </section>
      )}

      <section className={styles.grid}>
        {goals.map((goal) => (
          <article className={styles.goalCard} key={goal.id}>
            <strong>{goal.target_language?.name ?? goal.target_language?.code}</strong>
            <span>{goal.progress_percent}% concluido</span>
            {!goal.is_active && (
              <button onClick={() => { setSelectedGoal(goal); setModal("delete"); }} type="button">Excluir</button>
            )}
          </article>
        ))}
      </section>

      <button className={styles.addButton} onClick={() => setModal("add")} type="button">Adicionar area</button>
      <Link className={styles.historyLink} href={ROUTES.history}>Ver historico completo</Link>

      {modal === "add" && <AddAreaModal onClose={() => setModal(null)} onCreated={upsertGoal} />}
      {modal === "routine" && selectedGoal && <EditRoutineModal goal={selectedGoal} onClose={() => setModal(null)} onSaved={upsertGoal} />}
      {modal === "delete" && selectedGoal && (
        <ConfirmModal
          title="Excluir area"
          detail={`Excluir ${selectedGoal.target_language?.name ?? selectedGoal.target_language?.code}?`}
          onCancel={() => setModal(null)}
          onConfirm={() => deleteGoal(selectedGoal)}
        />
      )}
    </main>
  );
}

function State({ message }: { message: string }) {
  return <main className={styles.page}><p>{message}</p></main>;
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

  function toggleDay(day: number) {
    setDays((current) => current.includes(day) ? current.filter((item) => item !== day) : [...current, day].sort((a, b) => a - b));
  }

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
    <Modal title="Adicionar area" onClose={onClose}>
      <Section label="Voce quer aprender">
        {languages.map((language) => (
          <button className={`${styles.selectCard} ${target?.code === language.code ? styles.selected : ""}`} key={language.code} onClick={() => setTarget(language)} type="button">
            <strong>{STRINGS.languages[language.code as keyof typeof STRINGS.languages] ?? language.code}</strong>
            <span>{language.chapter_subtitle || language.chapter_title}</span>
          </button>
        ))}
      </Section>
      <RoutineFields days={days} minutes={minutes} onToggleDay={toggleDay} onMinutes={setMinutes} />
      <button className={styles.modalPrimary} disabled={saving || !target || days.length === 0} onClick={submit} type="button">
        {saving ? "Salvando..." : "Adicionar area"}
      </button>
    </Modal>
  );
}

function EditRoutineModal({ goal, onClose, onSaved }: { goal: Goal; onClose: () => void; onSaved: (goal: Goal) => void }) {
  const [days, setDays] = useState(goal.study_weekdays);
  const [minutes, setMinutes] = useState(goal.session_minutes);
  const [saving, setSaving] = useState(false);

  function toggleDay(day: number) {
    setDays((current) => current.includes(day) ? current.filter((item) => item !== day) : [...current, day].sort((a, b) => a - b));
  }

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
    <Modal title="Editar rotina" onClose={onClose}>
      <RoutineFields days={days} minutes={minutes} onToggleDay={toggleDay} onMinutes={setMinutes} />
      <button className={styles.modalPrimary} disabled={saving || days.length === 0} onClick={submit} type="button">
        {saving ? "Salvando..." : "Salvar rotina"}
      </button>
    </Modal>
  );
}

function ConfirmModal({ title, detail, onCancel, onConfirm }: { title: string; detail: string; onCancel: () => void; onConfirm: () => void }) {
  return (
    <Modal title={title} onClose={onCancel}>
      <p className={styles.modalDetail}>{detail}</p>
      <div className={styles.modalActions}>
        <button onClick={onCancel} type="button">Cancelar</button>
        <button className={styles.danger} onClick={onConfirm} type="button">Excluir</button>
      </div>
    </Modal>
  );
}

function RoutineFields({ days, minutes, onToggleDay, onMinutes }: { days: number[]; minutes: number; onToggleDay: (day: number) => void; onMinutes: (minutes: number) => void }) {
  return (
    <>
      <Section label="Dias de estudo">
        <div className={styles.dayGrid}>
          {WEEKDAYS.map((day) => (
            <button className={days.includes(day) ? styles.selected : ""} key={day} onClick={() => onToggleDay(day)} type="button">
              {STRINGS.weekdays.short[day]}
            </button>
          ))}
        </div>
      </Section>
      <Section label="Duracao">
        <div className={styles.pillGrid}>
          {SESSION_OPTIONS.map((option) => (
            <button className={minutes === option ? styles.selected : ""} key={option} onClick={() => onMinutes(option)} type="button">
              {STRINGS.onboarding.minutesShort(option)}
            </button>
          ))}
        </div>
      </Section>
    </>
  );
}

function Section({ label, children }: { label: string; children: React.ReactNode }) {
  return <section className={styles.modalSection}><p>{label}</p>{children}</section>;
}

function Modal({ title, children, onClose }: { title: string; children: React.ReactNode; onClose: () => void }) {
  return (
    <div className={styles.modalBackdrop}>
      <div className={styles.modalPanel}>
        <header>
          <h2>{title}</h2>
          <button onClick={onClose} type="button">Fechar</button>
        </header>
        {children}
      </div>
    </div>
  );
}
