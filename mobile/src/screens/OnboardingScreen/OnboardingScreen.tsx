import { router } from "expo-router";
import { useEffect, useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import { STRINGS, adventureService, contentService } from "@linguaflow/shared-core";
import type { AvailableLanguage } from "@linguaflow/shared-core";
import { styles } from "./OnboardingScreen.styles";

const WEEKDAYS = [0, 1, 2, 3, 4, 5, 6];
const SESSION_OPTIONS = [15, 30, 45, 60, 90];

export function OnboardingScreen() {
  const [step, setStep] = useState<1 | 2>(1);
  const [targetLanguage, setTargetLanguage] = useState<AvailableLanguage | null>(null);
  const [languages, setLanguages] = useState<AvailableLanguage[]>([]);
  const [studyDays, setStudyDays] = useState([0, 2, 4]);
  const [sessionMinutes, setSessionMinutes] = useState(30);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    adventureService.listAvailableLanguages().then((nextLanguages) => {
      setLanguages(nextLanguages);
      if (nextLanguages[0]) setTargetLanguage(nextLanguages[0]);
    });
  }, []);

  function toggleDay(day: number) {
    setStudyDays((current) => current.includes(day) ? current.filter((item) => item !== day) : [...current, day].sort((a, b) => a - b));
  }

  async function finish() {
    if (!targetLanguage || studyDays.length === 0) return;
    setLoading(true);
    try {
      await contentService.createGoal({
        source_language: "PT",
        target_language: targetLanguage.code,
        target_level: "A1",
        duration_days: 90,
        study_weekdays: studyDays,
        session_minutes: sessionMinutes,
      });
      router.replace("/(tabs)/home");
    } finally {
      setLoading(false);
    }
  }

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <Text style={styles.progress}>{STRINGS.onboarding.stepProgress(step, 2)}</Text>
      {step === 1 ? (
        <>
          <Text style={styles.title}>{STRINGS.onboarding.configureCourseTitle}</Text>
          <Text style={styles.subtitle}>{STRINGS.onboarding.configureCourseSubtitle}</Text>
          <Text style={styles.label}>{STRINGS.onboarding.youSpeak}</Text>
          <View style={styles.card}><Text style={styles.cardTitle}>Portugues</Text><Text style={styles.cardDetail}>{STRINGS.onboarding.sourceLanguageDetailPt}</Text></View>
          <Text style={styles.label}>{STRINGS.onboarding.youLearn}</Text>
          {languages.map((language) => (
            <Pressable style={[styles.card, targetLanguage?.code === language.code ? styles.selected : null]} key={language.code} onPress={() => setTargetLanguage(language)}>
              <Text style={styles.cardTitle}>{STRINGS.languages[language.code as keyof typeof STRINGS.languages] ?? language.code}</Text>
              <Text style={styles.cardDetail}>{language.chapter_subtitle || language.chapter_title}</Text>
            </Pressable>
          ))}
        </>
      ) : (
        <>
          <Text style={styles.title}>{STRINGS.onboarding.routineTitle}</Text>
          <Text style={styles.subtitle}>{STRINGS.onboarding.routineSubtitle}</Text>
          <Text style={styles.label}>{STRINGS.onboarding.daysLabel}</Text>
          <View style={styles.dayGrid}>
            {WEEKDAYS.map((day) => (
              <Pressable style={[styles.day, studyDays.includes(day) ? styles.selected : null]} key={day} onPress={() => toggleDay(day)}>
                <Text style={studyDays.includes(day) ? styles.selectedText : styles.dayText}>{STRINGS.weekdays.short[day]}</Text>
              </Pressable>
            ))}
          </View>
          <Text style={styles.label}>{STRINGS.onboarding.durationLabel}</Text>
          <View style={styles.sessionGrid}>
            {SESSION_OPTIONS.map((minutes) => (
              <Pressable style={[styles.session, sessionMinutes === minutes ? styles.selected : null]} key={minutes} onPress={() => setSessionMinutes(minutes)}>
                <Text style={sessionMinutes === minutes ? styles.selectedText : styles.dayText}>{STRINGS.onboarding.minutesShort(minutes)}</Text>
              </Pressable>
            ))}
          </View>
        </>
      )}
      <View style={styles.footer}>
        {step === 2 ? <Pressable style={styles.back} onPress={() => setStep(1)}><Text style={styles.backText}>Voltar</Text></Pressable> : null}
        <Pressable style={styles.submit} onPress={step === 1 ? () => setStep(2) : finish} disabled={loading || !targetLanguage}>
          <Text style={styles.submitText}>{loading ? "Carregando..." : step === 1 ? STRINGS.onboarding.next : STRINGS.onboarding.start}</Text>
        </Pressable>
      </View>
    </ScrollView>
  );
}
