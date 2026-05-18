import { Link } from "expo-router";
import { useEffect, useMemo, useState } from "react";
import { Pressable, ScrollView, Text, TextInput, View } from "react-native";
import { STRINGS, adventureService, contentService } from "@linguaflow/shared-core";
import type { ApiAdventureChapter, StudyModule, StudySessionData } from "@linguaflow/shared-core";
import { useStudySessionRunner } from "@linguaflow/shared-core/hooks/study";
import { styles } from "./StudyScreen.styles";

export function StudyScreen() {
  const [session, setSession] = useState<StudySessionData | null>(null);
  const [chapters, setChapters] = useState<ApiAdventureChapter[]>([]);
  const [modules, setModules] = useState<StudyModule[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [reviewOpen, setReviewOpen] = useState(false);

  useEffect(() => {
    Promise.all([
      adventureService.getStudySession(),
      adventureService.listChapters(),
      contentService.listStudyModules(),
    ])
      .then(([nextSession, nextChapters, nextModules]) => {
        setSession(nextSession);
        setChapters(nextChapters);
        setModules(nextModules);
      })
      .catch(() => setError(true))
      .finally(() => setLoading(false));
  }, []);

  const nextPhase = useMemo(() => {
    for (const chapter of chapters) {
      const phase = chapter.phases.find((item) => !item.is_completed);
      if (phase) return { chapter, phase };
    }
    return null;
  }, [chapters]);

  const currentLesson = useMemo(() => {
    const phaseNumber = nextPhase?.phase.number ?? null;
    for (const module of modules) {
      const lesson = phaseNumber
        ? module.lessons.find((item) => item.adventure_phase === phaseNumber)
        : module.lessons[0];
      if (lesson) return { module, lesson };
    }
    return null;
  }, [modules, nextPhase]);

  if (loading) return <State message={STRINGS.states.loadingStudy} />;
  if (error) return <State message={STRINGS.states.studyLoadError} />;
  if (reviewOpen && session) return <StudyReview exercises={session.exercises} onClose={() => setReviewOpen(false)} />;

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <Text style={styles.eyebrow}>{STRINGS.study.title}</Text>
      <Text style={styles.title}>{STRINGS.study.headline}</Text>
      <Text style={styles.subtitle}>{STRINGS.study.pendingReviews(session?.due_count ?? 0)}</Text>

      <View style={styles.hero}>
        <Text style={styles.cardLabel}>{STRINGS.study.nextPhase}</Text>
        <Text style={styles.cardTitle}>{nextPhase?.phase.title ?? STRINGS.study.startAdventureTitle}</Text>
        <Text style={styles.cardDetail}>
          {nextPhase ? `${nextPhase.chapter.title} - ${STRINGS.adventure.phaseLabel(nextPhase.phase.number)}` : STRINGS.study.adventureMap}
        </Text>
        <Pressable style={[styles.actionButton, !session?.exercises.length ? styles.disabled : null]} disabled={!session?.exercises.length} onPress={() => setReviewOpen(true)}>
          <Text style={styles.actionText}>{STRINGS.study.reviewBtn}</Text>
        </Pressable>
        <Link href="/(tabs)/adventure" style={styles.action}>{STRINGS.study.continueAdventureBtn}</Link>
      </View>

      {currentLesson ? (
        <View style={styles.card}>
          <Text style={styles.cardLabel}>{STRINGS.study.currentLesson}</Text>
          <Text style={styles.cardTitle}>{currentLesson.lesson.title}</Text>
          <Text style={styles.cardDetail}>{currentLesson.module.title}</Text>
          <Text style={styles.description}>{currentLesson.lesson.description}</Text>
        </View>
      ) : null}

      {modules.map((module) => (
        <View style={styles.card} key={module.id}>
          <Text style={styles.cardTitle}>{module.title}</Text>
          <Text style={styles.cardDetail}>{STRINGS.study.moduleLessons(module.lessons.length)}</Text>
          {module.lessons.slice(0, 4).map((lesson) => (
            <Text style={styles.lesson} key={lesson.id}>{lesson.title}</Text>
          ))}
        </View>
      ))}
    </ScrollView>
  );
}

function StudyReview({
  exercises,
  onClose,
}: {
  exercises: StudySessionData["exercises"];
  onClose: () => void;
}) {
  const [answer, setAnswer] = useState("");
  const runner = useStudySessionRunner({ exercises, onComplete: onClose });

  if (runner.done) {
    return (
      <View style={styles.reviewPage}>
        <Text style={styles.title}>{STRINGS.study.sessionComplete}</Text>
        <Text style={styles.subtitle}>{STRINGS.study.sessionScore(runner.correctCount, runner.mistakes)}</Text>
        <Pressable style={styles.actionButton} onPress={runner.finish}><Text style={styles.actionText}>{STRINGS.actions.back}</Text></Pressable>
      </View>
    );
  }

  if (!runner.current) return <State message={STRINGS.states.emptyReview} />;

  return (
    <View style={styles.reviewPage}>
      <Text style={styles.subtitle}>{runner.index + 1}/{runner.total}</Text>
      <Text style={styles.title}>{runner.current.kind === "multiple_choice" ? runner.current.question : runner.current.prompt}</Text>
      <Text style={styles.subtitle}>{runner.current.native}</Text>
      {runner.current.kind === "multiple_choice" && runner.current.options ? (
        <View style={styles.reviewOptions}>
          {runner.current.options.map((option) => (
            <Pressable style={styles.optionButton} key={option.id} onPress={() => runner.submit(option.id)}>
              <Text style={styles.optionText}>{option.text}</Text>
            </Pressable>
          ))}
        </View>
      ) : (
        <View style={styles.reviewInput}>
          <TextInput style={styles.input} value={answer} onChangeText={setAnswer} autoCapitalize="none" />
          <Pressable style={styles.smallButton} onPress={() => { runner.submit(answer); setAnswer(""); }}>
            <Text style={styles.actionText}>{STRINGS.study.answer}</Text>
          </Pressable>
        </View>
      )}
      <Pressable style={styles.secondaryButton} onPress={onClose}><Text style={styles.secondaryText}>{STRINGS.study.exit}</Text></Pressable>
    </View>
  );
}

function State({ message }: { message: string }) {
  return (
    <View style={styles.state}>
      <Text style={styles.stateText}>{message}</Text>
    </View>
  );
}
