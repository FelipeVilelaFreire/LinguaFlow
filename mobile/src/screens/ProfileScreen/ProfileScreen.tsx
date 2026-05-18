import { AntDesign, Feather } from "@expo/vector-icons";
import { Link, router } from "expo-router";
import { useEffect, useState } from "react";
import { Image, Pressable, ScrollView, Text, View } from "react-native";
import { STRINGS, authService, contentService, getFlagImage } from "@linguaflow/shared-core";
import type { Goal, HistoryMonth, User } from "@linguaflow/shared-core";
import {
  ProfileAddAreaModal,
  ProfileConfirmModal,
  ProfileEditRoutineModal,
} from "@/src/components/modals";
import { styles } from "./ProfileScreen.styles";

export function ProfileScreen() {
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
    router.replace("/login");
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
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <Pressable style={styles.userCard}>
        <Text style={styles.avatar}>{user.username.charAt(0).toUpperCase()}</Text>
        <View style={styles.userText}>
          <Text style={styles.username}>{user.username}</Text>
          <Text style={styles.email}>{user.email || STRINGS.profile.noEmail}</Text>
          <Text style={styles.member}>{STRINGS.profile.memberLabel}</Text>
        </View>
        <AntDesign name="right" size={16} color="#cbd5e1" />
      </Pressable>

      {activeGoal ? (
        <ActiveGoalCard goal={activeGoal} onEdit={() => { setSelectedGoal(activeGoal); setModal("routine"); }} />
      ) : null}

      <WeekPreview activeGoal={activeGoal ?? null} history={history} />

      {inactiveGoals.length > 0 ? (
        <View style={styles.listCard}>
          <Text style={styles.sectionLabel}>{STRINGS.profile.otherAreas}</Text>
          {inactiveGoals.map((goal) => (
            <View style={styles.areaRow} key={goal.id}>
              <LangFlag code={goal.target_language?.code ?? ""} />
              <View style={styles.areaText}>
                <Text style={styles.areaTitle}>{languageName(goal)}</Text>
                <Text style={styles.areaDetail}>{goal.source_language?.code} {"->"} {goal.target_language?.code} Â· {goal.target_level}</Text>
              </View>
              <Pressable style={styles.useButton} onPress={() => activateGoal(goal)}>
                <Text style={styles.useButtonText}>{STRINGS.profile.useArea}</Text>
              </Pressable>
              <Pressable style={styles.trashButton} onPress={() => { setSelectedGoal(goal); setModal("delete"); }}>
                <Feather name="trash-2" size={14} color="#dc2626" />
              </Pressable>
            </View>
          ))}
        </View>
      ) : null}

      <Pressable style={styles.addArea} onPress={() => setModal("add")}>
        <View style={styles.addIcon}><Feather name="plus" size={18} color="#14b8a6" /></View>
        <View style={styles.userText}>
          <Text style={styles.addAreaTitle}>{STRINGS.profile.addArea}</Text>
          <Text style={styles.addAreaDetail}>{STRINGS.profile.addAreaDetail}</Text>
        </View>
        <AntDesign name="right" size={16} color="#cbd5e1" />
      </Pressable>

      <View style={styles.planCard}>
        <Text style={styles.sectionLabel}>{STRINGS.profile.planLabel}</Text>
        <View style={styles.planRow}>
          <View>
            <Text style={styles.planName}>{STRINGS.profile.planName}</Text>
            <Text style={styles.planDetail}>{STRINGS.profile.planDetail}</Text>
          </View>
          <Pressable style={styles.upgradeButton}><Text style={styles.upgradeText}>{STRINGS.profile.upgrade}</Text></Pressable>
        </View>
      </View>

      <Pressable style={styles.signOut} onPress={logout}><Text style={styles.signOutText}>{STRINGS.profile.signOut}</Text></Pressable>

      {modal === "add" ? <ProfileAddAreaModal onClose={() => setModal(null)} onCreated={upsertGoal} /> : null}
      {modal === "routine" && selectedGoal ? <ProfileEditRoutineModal goal={selectedGoal} onClose={() => setModal(null)} onSaved={upsertGoal} /> : null}
      {modal === "delete" && selectedGoal ? (
        <ProfileConfirmModal
          title={STRINGS.profile.deleteAreaTitle}
          detail={STRINGS.profile.deleteAreaBody(languageName(selectedGoal))}
          onCancel={() => setModal(null)}
          onConfirm={() => deleteGoal(selectedGoal)}
        />
      ) : null}
    </ScrollView>
  );
}

function ActiveGoalCard({ goal, onEdit }: { goal: Goal; onEdit: () => void }) {
  return (
    <View style={styles.courseCard}>
      <View style={styles.courseHeader}>
        <LangFlag code={goal.target_language?.code ?? ""} large />
        <View style={styles.courseText}>
          <Text style={styles.cardTitle}>{languageName(goal)}</Text>
          <View style={styles.badgeRow}>
            <Text style={styles.langBadge}>{goal.source_language?.code} {"->"} {goal.target_language?.code}</Text>
            <Text style={styles.levelBadge}>{goal.target_level}</Text>
          </View>
        </View>
      </View>
      <View style={styles.divider} />
      <View style={styles.routineRow}>
        <Feather name="clock" size={14} color="#a1a1aa" />
        <Text style={styles.routineText}>{formatDays(goal.study_weekdays)} Â· {formatMinutes(goal.session_minutes)}</Text>
        <Pressable onPress={onEdit}><Text style={styles.linkText}>{STRINGS.profile.editRoutine}</Text></Pressable>
      </View>
    </View>
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
    <View style={styles.weekCard}>
      <View style={styles.weekHeader}>
        <Text style={styles.sectionLabel}>{STRINGS.profile.weekActivity}</Text>
        <Link href="/history" style={styles.linkText}>{STRINGS.profile.viewHistory}</Link>
      </View>
      <View style={styles.weekGrid}>
        {last7.map((dateString) => {
          const date = new Date(`${dateString}T12:00:00`);
          const weekdayIndex = date.getDay() === 0 ? 6 : date.getDay() - 1;
          const completed = completedDates.has(dateString);
          const planned = routineSet.has(weekdayIndex);
          return (
            <View style={styles.weekDay} key={dateString}>
              <Text style={[styles.weekDate, planned ? styles.plannedDay : null, completed ? styles.completedDay : null]}>{date.getDate()}</Text>
              <Text style={styles.weekLabel}>{STRINGS.weekdays.short[weekdayIndex]}</Text>
            </View>
          );
        })}
      </View>
    </View>
  );
}


function LangFlag({ code, large = false }: { code: string; large?: boolean }) {
  const flag = getFlagImage(code, large ? "xl" : "sm");
  return <Image source={{ uri: flag.src }} style={large ? styles.flagLarge : styles.flag} />;
}

function State({ message }: { message: string }) {
  return <View style={styles.state}><Text style={styles.stateText}>{message}</Text></View>;
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
