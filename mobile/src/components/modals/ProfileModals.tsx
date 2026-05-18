import { useEffect, useState } from "react";
import type { ReactNode } from "react";
import { Image, Modal, Pressable, ScrollView, Text, View } from "react-native";
import { STRINGS, adventureService, contentService, getFlagImage } from "@linguaflow/shared-core";
import type { AvailableLanguage, Goal } from "@linguaflow/shared-core";
import { styles } from "./ProfileModals.styles";

const WEEKDAYS = [0, 1, 2, 3, 4, 5, 6];
const SESSION_OPTIONS = [15, 30, 45, 60, 90];

export function ProfileAddAreaModal({ onClose, onCreated }: { onClose: () => void; onCreated: (goal: Goal) => void }) {
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
    <ProfileModalShell title={STRINGS.profile.addAreaTitle} onClose={onClose}>
      <Text style={styles.modalLabel}>{STRINGS.profile.learnTarget}</Text>
      {languages.map((language) => (
        <Pressable style={[styles.modalCard, target?.code === language.code ? styles.modalSelected : null]} key={language.code} onPress={() => setTarget(language)}>
          <LangFlag code={language.code} />
          <View style={styles.areaText}>
            <Text style={styles.modalCardTitle}>{STRINGS.languages[language.code as keyof typeof STRINGS.languages] ?? language.code}</Text>
            <Text style={styles.modalCardDetail}>{language.chapter_subtitle || language.chapter_title}</Text>
          </View>
        </Pressable>
      ))}
      <RoutineFields days={days} minutes={minutes} onToggleDay={(day) => setDays(toggleDay(days, day))} onMinutes={setMinutes} />
      <Pressable style={[styles.modalPrimary, saving || !target || days.length === 0 ? styles.disabled : null]} disabled={saving || !target || days.length === 0} onPress={submit}>
        <Text style={styles.modalPrimaryText}>{saving ? STRINGS.profile.saving : STRINGS.profile.addArea}</Text>
      </Pressable>
    </ProfileModalShell>
  );
}

export function ProfileEditRoutineModal({ goal, onClose, onSaved }: { goal: Goal; onClose: () => void; onSaved: (goal: Goal) => void }) {
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
    <ProfileModalShell title={STRINGS.profile.editRoutineTitle} onClose={onClose}>
      <RoutineFields days={days} minutes={minutes} onToggleDay={(day) => setDays(toggleDay(days, day))} onMinutes={setMinutes} />
      {days.length === 0 ? <Text style={styles.dayError}>{STRINGS.profile.chooseDayError}</Text> : null}
      <Pressable style={[styles.modalPrimary, saving || days.length === 0 ? styles.disabled : null]} disabled={saving || days.length === 0} onPress={submit}>
        <Text style={styles.modalPrimaryText}>{saving ? STRINGS.profile.saving : STRINGS.profile.saveRoutine}</Text>
      </Pressable>
    </ProfileModalShell>
  );
}

export function ProfileConfirmModal({ title, detail, onCancel, onConfirm }: { title: string; detail: string; onCancel: () => void; onConfirm: () => void }) {
  return (
    <ProfileModalShell title={title} onClose={onCancel}>
      <Text style={styles.modalCardDetail}>{detail}</Text>
      <View style={styles.confirmRow}>
        <Pressable style={styles.cancelButton} onPress={onCancel}><Text style={styles.cancelText}>{STRINGS.profile.cancelAction}</Text></Pressable>
        <Pressable style={styles.dangerButton} onPress={onConfirm}><Text style={styles.dangerButtonText}>{STRINGS.actions.delete}</Text></Pressable>
      </View>
    </ProfileModalShell>
  );
}

function RoutineFields({ days, minutes, onToggleDay, onMinutes }: { days: number[]; minutes: number; onToggleDay: (day: number) => void; onMinutes: (minutes: number) => void }) {
  return (
    <>
      <Text style={styles.modalLabel}>{STRINGS.profile.studyDays}</Text>
      <View style={styles.modalDayGrid}>
        {WEEKDAYS.map((day) => (
          <Pressable style={[styles.modalDay, days.includes(day) ? styles.modalDaySelected : null]} key={day} onPress={() => onToggleDay(day)}>
            <Text style={days.includes(day) ? styles.modalDaySelectedText : styles.modalDayText}>{STRINGS.weekdays.short[day]}</Text>
          </Pressable>
        ))}
      </View>
      <Text style={styles.modalLabel}>{STRINGS.profile.duration}</Text>
      <View style={styles.modalPillGrid}>
        {SESSION_OPTIONS.map((option) => (
          <Pressable style={[styles.modalPill, minutes === option ? styles.modalSelected : null]} key={option} onPress={() => onMinutes(option)}>
            <Text style={minutes === option ? styles.modalSelectedText : styles.modalDayText}>{formatMinutes(option)}</Text>
          </Pressable>
        ))}
      </View>
    </>
  );
}

function ProfileModalShell({ title, children, onClose }: { title: string; children: ReactNode; onClose: () => void }) {
  return (
    <Modal transparent animationType="slide" onRequestClose={onClose}>
      <View style={styles.modalBackdrop}>
        <View style={styles.modalPanel}>
          <View style={styles.modalHeader}>
            <Text style={styles.modalTitle}>{title}</Text>
            <Pressable style={styles.modalClose} onPress={onClose}><Text style={styles.modalCloseText}>{STRINGS.profile.close}</Text></Pressable>
          </View>
          <ScrollView contentContainerStyle={styles.modalContent}>{children}</ScrollView>
        </View>
      </View>
    </Modal>
  );
}

function LangFlag({ code }: { code: string }) {
  const flag = getFlagImage(code, "sm");
  return <Image source={{ uri: flag.src }} style={styles.flag} />;
}

function toggleDay(current: number[], day: number) {
  return current.includes(day) ? current.filter((item) => item !== day) : [...current, day].sort((a, b) => a - b);
}

function formatMinutes(minutes: number) {
  if (minutes === 60) return STRINGS.onboarding.hourShort;
  if (minutes === 90) return STRINGS.onboarding.hourAndHalfShort;
  return STRINGS.onboarding.minutesShort(minutes);
}
