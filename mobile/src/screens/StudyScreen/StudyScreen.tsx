import { Link } from "expo-router";
import { useEffect, useMemo, useState } from "react";
import { Pressable, ScrollView, Text, TextInput, View } from "react-native";
import { adventureService, contentService } from "@linguaflow/shared-core";
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

  if (loading) return <State message="Carregando estudo..." />;
  if (error) return <State message="Nao foi possivel carregar o estudo." />;
  if (reviewOpen && session) return <StudyReview exercises={session.exercises} onClose={() => setReviewOpen(false)} />;

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <Text style={styles.eyebrow}>Estudo guiado</Text>
      <Text style={styles.title}>Treine o que a aventura pede agora.</Text>
      <Text style={styles.subtitle}>{session?.due_count ?? 0} revisoes pendentes</Text>

      <View style={styles.hero}>
        <Text style={styles.cardLabel}>Proxima fase</Text>
        <Text style={styles.cardTitle}>{nextPhase?.phase.title ?? "Comece sua aventura"}</Text>
        <Text style={styles.cardDetail}>{nextPhase ? `${nextPhase.chapter.title} · Fase ${nextPhase.phase.number}` : "Mapa da aventura"}</Text>
        <Pressable style={[styles.actionButton, !session?.exercises.length ? styles.disabled : null]} disabled={!session?.exercises.length} onPress={() => setReviewOpen(true)}>
          <Text style={styles.actionText}>Revisar agora</Text>
        </Pressable>
        <Link href="/(tabs)/adventure" style={styles.action}>Abrir mapa</Link>
      </View>

      {currentLesson ? (
        <View style={styles.card}>
          <Text style={styles.cardLabel}>Licao atual</Text>
          <Text style={styles.cardTitle}>{currentLesson.lesson.title}</Text>
          <Text style={styles.cardDetail}>{currentLesson.module.title}</Text>
          <Text style={styles.description}>{currentLesson.lesson.description}</Text>
        </View>
      ) : null}

      {modules.map((module) => (
        <View style={styles.card} key={module.id}>
          <Text style={styles.cardTitle}>{module.title}</Text>
          <Text style={styles.cardDetail}>{module.lessons.length} licoes</Text>
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
        <Text style={styles.title}>Revisao concluida</Text>
        <Text style={styles.subtitle}>{runner.correctCount} acertos · {runner.mistakes} erros</Text>
        <Pressable style={styles.actionButton} onPress={runner.finish}><Text style={styles.actionText}>Voltar</Text></Pressable>
      </View>
    );
  }

  if (!runner.current) return <State message="Nenhuma revisao pendente." />;

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
            <Text style={styles.actionText}>OK</Text>
          </Pressable>
        </View>
      )}
      <Pressable style={styles.secondaryButton} onPress={onClose}><Text style={styles.secondaryText}>Sair</Text></Pressable>
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
