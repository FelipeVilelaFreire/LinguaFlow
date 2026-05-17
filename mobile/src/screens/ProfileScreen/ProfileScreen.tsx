import { Link, router } from "expo-router";
import { useEffect, useState } from "react";
import { Modal, Pressable, ScrollView, Text, View } from "react-native";
import { STRINGS, adventureService, authService, contentService } from "@linguaflow/shared-core";
import type { AvailableLanguage, Goal, User } from "@linguaflow/shared-core";
import { styles } from "./ProfileScreen.styles";

const WEEKDAYS = [0, 1, 2, 3, 4, 5, 6];
const SESSION_OPTIONS = [15, 30, 45, 60, 90];

export function ProfileScreen() {
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
    router.replace("/(tabs)/home");
  }

  function upsertGoal(goal: Goal) {
    setGoals((current) => {
      const exists = current.some((item) => item.id === goal.id);
      return exists ? current.map((item) => item.id === goal.id ? goal : item) : [...current, goal];
    });
  }

  async function deleteGoal(goal: Goal) {
    const result = await contentService.deleteGoal(goal.id);
    setGoals((current) => current.filter((item) => item.id !== goal.id));
    if (result.current_goal) upsertGoal(result.current_goal);
    setModal(null);
    setSelectedGoal(null);
  }

  if (loading) {
    return (
      <View style={styles.state}>
        <Text style={styles.stateText}>Carregando perfil...</Text>
      </View>
    );
  }

  if (!user) {
    return (
      <View style={styles.state}>
        <Text style={styles.stateText}>Perfil indisponivel.</Text>
      </View>
    );
  }

  const activeGoal = goals.find((goal) => goal.is_active);

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={styles.userCard}>
        <Text style={styles.avatar}>{user.username.charAt(0).toUpperCase()}</Text>
        <View style={styles.userText}>
          <Text style={styles.username}>{user.username}</Text>
          <Text style={styles.email}>{user.email || "Sem email"}</Text>
        </View>
        <Pressable style={styles.logout} onPress={logout}>
          <Text style={styles.logoutText}>Sair</Text>
        </Pressable>
      </View>

      {activeGoal ? (
        <View style={styles.card}>
          <Text style={styles.label}>Curso ativo</Text>
          <Text style={styles.cardTitle}>{activeGoal.target_language?.name ?? activeGoal.target_language?.code}</Text>
          <Text style={styles.cardDetail}>{activeGoal.source_language?.code} {"->"} {activeGoal.target_language?.code} · {activeGoal.target_level}</Text>
          <View style={styles.progress}><View style={[styles.progressFill, { width: `${activeGoal.progress_percent}%` }]} /></View>
          <Pressable style={styles.secondaryAction} onPress={() => { setSelectedGoal(activeGoal); setModal("routine"); }}>
            <Text style={styles.secondaryActionText}>Editar rotina</Text>
          </Pressable>
        </View>
      ) : null}

      {goals.map((goal) => (
        <View style={styles.goalCard} key={goal.id}>
          <Text style={styles.goalTitle}>{goal.target_language?.name ?? goal.target_language?.code}</Text>
          <Text style={styles.cardDetail}>{goal.progress_percent}% concluido</Text>
          {!goal.is_active ? (
            <Pressable style={styles.dangerOutline} onPress={() => { setSelectedGoal(goal); setModal("delete"); }}>
              <Text style={styles.dangerText}>Excluir</Text>
            </Pressable>
          ) : null}
        </View>
      ))}

      <Pressable style={styles.addArea} onPress={() => setModal("add")}>
        <Text style={styles.addAreaText}>Adicionar area</Text>
      </Pressable>
      <Link href="/history" style={styles.historyLink}>Ver historico completo</Link>

      {modal === "add" ? <AddAreaModal onClose={() => setModal(null)} onCreated={upsertGoal} /> : null}
      {modal === "routine" && selectedGoal ? <EditRoutineModal goal={selectedGoal} onClose={() => setModal(null)} onSaved={upsertGoal} /> : null}
      {modal === "delete" && selectedGoal ? (
        <ConfirmModal
          title="Excluir area"
          detail={`Excluir ${selectedGoal.target_language?.name ?? selectedGoal.target_language?.code}?`}
          onCancel={() => setModal(null)}
          onConfirm={() => deleteGoal(selectedGoal)}
        />
      ) : null}
    </ScrollView>
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
    <ModalShell title="Adicionar area" onClose={onClose}>
      <Text style={styles.modalLabel}>Voce quer aprender</Text>
      {languages.map((language) => (
        <Pressable style={[styles.modalCard, target?.code === language.code ? styles.modalSelected : null]} key={language.code} onPress={() => setTarget(language)}>
          <Text style={styles.modalCardTitle}>{STRINGS.languages[language.code as keyof typeof STRINGS.languages] ?? language.code}</Text>
          <Text style={styles.modalCardDetail}>{language.chapter_subtitle || language.chapter_title}</Text>
        </Pressable>
      ))}
      <RoutineFields days={days} minutes={minutes} onToggleDay={toggleDay} onMinutes={setMinutes} />
      <Pressable style={[styles.modalPrimary, saving || !target || days.length === 0 ? styles.disabled : null]} disabled={saving || !target || days.length === 0} onPress={submit}>
        <Text style={styles.modalPrimaryText}>{saving ? "Salvando..." : "Adicionar area"}</Text>
      </Pressable>
    </ModalShell>
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
    <ModalShell title="Editar rotina" onClose={onClose}>
      <RoutineFields days={days} minutes={minutes} onToggleDay={toggleDay} onMinutes={setMinutes} />
      <Pressable style={[styles.modalPrimary, saving || days.length === 0 ? styles.disabled : null]} disabled={saving || days.length === 0} onPress={submit}>
        <Text style={styles.modalPrimaryText}>{saving ? "Salvando..." : "Salvar rotina"}</Text>
      </Pressable>
    </ModalShell>
  );
}

function ConfirmModal({ title, detail, onCancel, onConfirm }: { title: string; detail: string; onCancel: () => void; onConfirm: () => void }) {
  return (
    <ModalShell title={title} onClose={onCancel}>
      <Text style={styles.modalCardDetail}>{detail}</Text>
      <View style={styles.confirmRow}>
        <Pressable style={styles.cancelButton} onPress={onCancel}><Text style={styles.cancelText}>Cancelar</Text></Pressable>
        <Pressable style={styles.dangerButton} onPress={onConfirm}><Text style={styles.dangerButtonText}>Excluir</Text></Pressable>
      </View>
    </ModalShell>
  );
}

function RoutineFields({ days, minutes, onToggleDay, onMinutes }: { days: number[]; minutes: number; onToggleDay: (day: number) => void; onMinutes: (minutes: number) => void }) {
  return (
    <>
      <Text style={styles.modalLabel}>Dias de estudo</Text>
      <View style={styles.modalDayGrid}>
        {WEEKDAYS.map((day) => (
          <Pressable style={[styles.modalDay, days.includes(day) ? styles.modalSelected : null]} key={day} onPress={() => onToggleDay(day)}>
            <Text style={days.includes(day) ? styles.modalSelectedText : styles.modalDayText}>{STRINGS.weekdays.short[day]}</Text>
          </Pressable>
        ))}
      </View>
      <Text style={styles.modalLabel}>Duracao</Text>
      <View style={styles.modalPillGrid}>
        {SESSION_OPTIONS.map((option) => (
          <Pressable style={[styles.modalPill, minutes === option ? styles.modalSelected : null]} key={option} onPress={() => onMinutes(option)}>
            <Text style={minutes === option ? styles.modalSelectedText : styles.modalDayText}>{STRINGS.onboarding.minutesShort(option)}</Text>
          </Pressable>
        ))}
      </View>
    </>
  );
}

function ModalShell({ title, children, onClose }: { title: string; children: React.ReactNode; onClose: () => void }) {
  return (
    <Modal transparent animationType="slide" onRequestClose={onClose}>
      <View style={styles.modalBackdrop}>
        <View style={styles.modalPanel}>
          <View style={styles.modalHeader}>
            <Text style={styles.modalTitle}>{title}</Text>
            <Pressable style={styles.modalClose} onPress={onClose}><Text style={styles.modalCloseText}>Fechar</Text></Pressable>
          </View>
          <ScrollView contentContainerStyle={styles.modalContent}>{children}</ScrollView>
        </View>
      </View>
    </Modal>
  );
}
