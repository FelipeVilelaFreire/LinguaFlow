import { router } from "expo-router";
import { AntDesign } from "@expo/vector-icons";
import { useEffect, useState } from "react";
import { Image, Pressable, ScrollView, Text, View } from "react-native";
import { STRINGS, adventureService, contentService, getFlagImage } from "@linguaflow/shared-core";
import type { AvailableLanguage } from "@linguaflow/shared-core";
import { styles } from "./OnboardingScreen.styles";

const LOGO = require("../../../assets/lang-plus.svg");

const SOURCE_LANGUAGES = [
  { code: "PT", detailKey: "sourceLanguageDetailPt" as const },
];

const LEVELS = [
  { code: "A1", labelKey: "levelIniciante" as const, detailKey: "levelA1Detail" as const },
];

const WEEKDAYS = [0, 1, 2, 3, 4, 5, 6];
const SESSION_OPTIONS = [15, 30, 45, 60, 90];

export function OnboardingScreen() {
  const [step, setStep] = useState<1 | 2>(1);
  const [sourceLanguage, setSourceLanguage] = useState(SOURCE_LANGUAGES[0]);
  const [targetLanguage, setTargetLanguage] = useState<AvailableLanguage | null>(null);
  const [level, setLevel] = useState(LEVELS[0]);
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
        source_language: sourceLanguage.code,
        target_language: targetLanguage.code,
        target_level: level.code,
        duration_days: 90,
        study_weekdays: studyDays,
        session_minutes: sessionMinutes,
      });
      router.replace("/(tabs)/home");
    } finally {
      setLoading(false);
    }
  }

  const months = estimateMonths(studyDays, sessionMinutes);

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={styles.glow} />
      <View style={styles.shell}>
        <View style={styles.header}>
          <Image source={LOGO} style={styles.logo} resizeMode="contain" accessibilityLabel={STRINGS.app.name} />
          <Text style={styles.progress}>{STRINGS.onboarding.stepProgress(step, 2)}</Text>
        </View>
        <View style={styles.progressBar}>
          <View style={[styles.progressFill, { width: step === 1 ? "50%" : "100%" }]} />
        </View>

        <View style={styles.panel}>
          {step === 1 ? (
            <>
              <View style={styles.heading}>
                <Text style={styles.title}>{STRINGS.onboarding.configureCourseTitle}</Text>
                <Text style={styles.subtitle}>{STRINGS.onboarding.configureCourseSubtitle}</Text>
              </View>

              <View style={styles.section}>
                <Text style={styles.label}>{STRINGS.onboarding.youSpeak}</Text>
                <View style={styles.stack}>
                  {SOURCE_LANGUAGES.map((language) => (
                    <SelectCard
                      key={language.code}
                      code={language.code}
                      title={STRINGS.languages[language.code as keyof typeof STRINGS.languages] ?? language.code}
                      detail={STRINGS.onboarding[language.detailKey]}
                      selected={sourceLanguage.code === language.code}
                      onPress={() => setSourceLanguage(language)}
                    />
                  ))}
                </View>
              </View>

              <View style={styles.section}>
                <Text style={styles.label}>{STRINGS.onboarding.youLearn}</Text>
                <View style={styles.stack}>
                  {languages.map((language) => (
                    <SelectCard
                      key={language.code}
                      code={language.code}
                      title={STRINGS.languages[language.code as keyof typeof STRINGS.languages] ?? language.code}
                      detail={language.chapter_subtitle || language.chapter_title}
                      selected={targetLanguage?.code === language.code}
                      onPress={() => setTargetLanguage(language)}
                    />
                  ))}
                </View>
              </View>

              <View style={styles.section}>
                <Text style={styles.label}>{STRINGS.onboarding.levelLabel}</Text>
                <View style={styles.levelGrid}>
                  {LEVELS.map((item) => (
                    <Pressable
                      key={item.code}
                      style={[styles.levelPill, level.code === item.code ? styles.selected : null]}
                      onPress={() => setLevel(item)}
                    >
                      <Text style={styles.levelCode}>{item.code}</Text>
                      <Text style={[styles.levelLabel, level.code === item.code ? styles.levelSelectedLabel : null]}>{STRINGS.onboarding[item.labelKey]}</Text>
                      <Text style={styles.levelDetail}>{STRINGS.onboarding[item.detailKey]}</Text>
                    </Pressable>
                  ))}
                </View>
              </View>
            </>
          ) : (
            <>
              <View style={styles.heading}>
                <Text style={styles.title}>{STRINGS.onboarding.routineTitle}</Text>
                <Text style={styles.subtitle}>{STRINGS.onboarding.routineSubtitle}</Text>
              </View>
              <View style={styles.section}>
                <Text style={styles.label}>{STRINGS.onboarding.daysLabel}</Text>
                <View style={styles.dayGrid}>
                  {WEEKDAYS.map((day) => {
                    const selected = studyDays.includes(day);
                    return (
                      <Pressable style={[styles.day, selected ? styles.selectedDay : null]} key={day} onPress={() => toggleDay(day)}>
                        <Text style={selected ? styles.selectedDayText : styles.dayText}>{STRINGS.weekdays.short[day]}</Text>
                      </Pressable>
                    );
                  })}
                </View>
                {studyDays.length === 0 ? <Text style={styles.dayError}>{STRINGS.onboarding.chooseDayError}</Text> : null}
              </View>

              <View style={styles.section}>
                <Text style={styles.label}>{STRINGS.onboarding.durationLabel}</Text>
                <View style={styles.sessionGrid}>
                  {SESSION_OPTIONS.map((minutes) => (
                    <Pressable style={[styles.session, sessionMinutes === minutes ? styles.selected : null]} key={minutes} onPress={() => setSessionMinutes(minutes)}>
                      <Text style={sessionMinutes === minutes ? styles.selectedPillText : styles.pillText}>{formatSessionDuration(minutes, "short")}</Text>
                    </Pressable>
                  ))}
                </View>
              </View>

              {months !== null ? (
                <View style={styles.estimate}>
                  <Text style={styles.estimateTitle}>{STRINGS.onboarding.estimateSentence(months)}</Text>
                  <Text style={styles.estimateDetail}>{STRINGS.onboarding.estimatePace(studyDays.length, formatSessionDuration(sessionMinutes, "long"))}</Text>
                </View>
              ) : null}
            </>
          )}
          <View style={styles.footer}>
            {step === 2 ? (
              <Pressable style={styles.back} onPress={() => setStep(1)} accessibilityLabel={STRINGS.actions.back}>
                <AntDesign name="arrowleft" size={18} color="#64748b" />
              </Pressable>
            ) : null}
            <Pressable style={styles.submit} onPress={step === 1 ? () => setStep(2) : finish} disabled={loading || !targetLanguage || (step === 2 && studyDays.length === 0)}>
              <Text style={styles.submitText}>{loading ? STRINGS.app.loading : step === 1 ? STRINGS.onboarding.next : STRINGS.onboarding.start}</Text>
              {!loading ? <AntDesign name="arrowright" size={16} color="#ffffff" /> : null}
            </Pressable>
          </View>
        </View>
      </View>
    </ScrollView>
  );
}

function SelectCard({
  code,
  title,
  detail,
  selected,
  onPress,
}: {
  code: string;
  title: string;
  detail: string;
  selected: boolean;
  onPress: () => void;
}) {
  return (
    <Pressable style={[styles.card, selected ? styles.selected : null]} onPress={onPress}>
      <LangFlag code={code} />
      <View style={styles.cardCopy}>
        <Text style={styles.cardTitle}>{title}</Text>
        <Text style={styles.cardDetail}>{detail}</Text>
      </View>
      {selected ? <AntDesign name="check" size={16} color="#14b8a6" /> : null}
    </Pressable>
  );
}

function LangFlag({ code }: { code: string }) {
  const flag = getFlagImage(code, "sm");
  return <Image source={{ uri: flag.src }} style={styles.flag} accessibilityLabel={STRINGS.onboarding.flagAlt(code)} />;
}

function estimateMonths(days: number[], minutes: number) {
  if (days.length === 0) return null;
  const weeks = 80 / ((days.length * minutes) / 60);
  return Math.max(1, Math.round(weeks / 4.3));
}

function formatSessionDuration(minutes: number, style: "short" | "long") {
  if (minutes === 60) return style === "long" ? STRINGS.onboarding.hourLong : STRINGS.onboarding.hourShort;
  if (minutes === 90) return STRINGS.onboarding.hourAndHalfShort;
  return STRINGS.onboarding.minutesShort(minutes);
}
