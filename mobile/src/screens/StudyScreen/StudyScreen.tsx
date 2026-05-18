import { Feather } from "@expo/vector-icons";
import { useEffect, useMemo, useState } from "react";
import { Pressable, ScrollView, Text, TextInput, View } from "react-native";
import { STRINGS, adventureService, contentService } from "@linguaflow/shared-core";
import type { ApiAdventureChapter, Phrase, StudyLesson, StudyModule, StudySessionData } from "@linguaflow/shared-core";
import { useStudySessionRunner } from "@linguaflow/shared-core/hooks/study";
import { AdventureTransitionButton } from "@/src/components/features/adventure";
import { styles } from "./StudyScreen.styles";

type StudyTab = "guided" | "modules";

export function StudyScreen() {
  const [session, setSession] = useState<StudySessionData | null>(null);
  const [chapters, setChapters] = useState<ApiAdventureChapter[]>([]);
  const [modules, setModules] = useState<StudyModule[]>([]);
  const [phrases, setPhrases] = useState<Phrase[]>([]);
  const [tab, setTab] = useState<StudyTab>("guided");
  const [loading, setLoading] = useState(true);
  const [phrasesLoading, setPhrasesLoading] = useState(false);
  const [error, setError] = useState(false);
  const [reviewOpen, setReviewOpen] = useState(false);
  const [lessonOpen, setLessonOpen] = useState(false);

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
      const lesson = phaseNumber ? module.lessons.find((item) => item.adventure_phase === phaseNumber) : module.lessons[0];
      if (lesson) return { module, lesson };
    }
    return null;
  }, [modules, nextPhase]);

  useEffect(() => {
    if (!currentLesson?.lesson.slug) {
      setPhrases([]);
      return;
    }
    setPhrasesLoading(true);
    contentService.listPhrases(currentLesson.lesson.slug)
      .then(setPhrases)
      .catch(() => setPhrases([]))
      .finally(() => setPhrasesLoading(false));
  }, [currentLesson?.lesson.slug]);

  if (loading) return <State message={STRINGS.states.loadingStudy} />;
  if (error) return <State message={STRINGS.states.studyLoadError} />;
  if (reviewOpen && session) return <StudyReview exercises={session.exercises} onClose={() => setReviewOpen(false)} />;
  if (lessonOpen && currentLesson && phrases.length > 0) return <PhraseLessonRunner lesson={currentLesson.lesson} phrases={phrases} onClose={() => setLessonOpen(false)} />;

  const dueCount = session?.due_count ?? 0;

  return (
    <ScrollView style={styles.container} contentContainerStyle={styles.content}>
      <View style={styles.header}>
        <View>
          <Text style={styles.eyebrow}>{STRINGS.study.title}</Text>
          <Text style={styles.title}>{STRINGS.study.headline}</Text>
        </View>
        <Text style={styles.reviewPill}>{STRINGS.study.pendingReviews(dueCount)}</Text>
      </View>

      <View style={styles.tabs}>
        <Pressable style={tab === "guided" ? styles.activeTab : styles.tab} onPress={() => setTab("guided")}>
          <Text style={tab === "guided" ? styles.activeTabText : styles.tabText}>{STRINGS.today.tabSession}</Text>
        </Pressable>
        <Pressable style={tab === "modules" ? styles.activeTab : styles.tab} onPress={() => setTab("modules")}>
          <Text style={tab === "modules" ? styles.activeTabText : styles.tabText}>{STRINGS.today.tabModules}</Text>
        </Pressable>
      </View>

      {tab === "guided" ? (
        <>
          <View style={styles.hero}>
            <View style={styles.iconBubble}><Feather name="map" size={22} color="#ffffff" /></View>
            <Text style={styles.cardLabel}>{STRINGS.study.nextPhase}</Text>
            <Text style={styles.cardTitle}>{nextPhase?.phase.title ?? STRINGS.study.startAdventureTitle}</Text>
            <Text style={styles.cardDetail}>
              {nextPhase ? `${nextPhase.chapter.title} - ${STRINGS.adventure.phaseLabel(nextPhase.phase.number)}` : STRINGS.study.adventureMap}
            </Text>
            <Text style={styles.description}>{STRINGS.study.continueAdventureHint}</Text>
            <View style={styles.heroActions}>
              <AdventureTransitionButton href="/adventure/map" style={styles.action}>
                <Text style={styles.actionText}>{STRINGS.study.continueAdventureBtn}</Text>
              </AdventureTransitionButton>
              <Pressable style={[styles.secondaryAction, phrasesLoading || phrases.length === 0 ? styles.disabled : null]} disabled={phrasesLoading || phrases.length === 0} onPress={() => setLessonOpen(true)}>
                <Text style={styles.secondaryActionText}>{STRINGS.study.studyNowBtn}</Text>
              </Pressable>
            </View>
          </View>

          {currentLesson ? (
            <CurrentLessonCard currentLesson={currentLesson} phrases={phrases} phrasesLoading={phrasesLoading} onStart={() => setLessonOpen(true)} />
          ) : null}

          <ReviewCard dueCount={dueCount} disabled={!session?.exercises.length} onReview={() => setReviewOpen(true)} />
          <StudyTrail modules={modules} currentLessonId={currentLesson?.lesson.id ?? null} currentPhase={nextPhase?.phase.number ?? null} />
        </>
      ) : (
        <StudyTrail modules={modules} currentLessonId={currentLesson?.lesson.id ?? null} currentPhase={nextPhase?.phase.number ?? null} expanded />
      )}
    </ScrollView>
  );
}

function CurrentLessonCard({ currentLesson, phrases, phrasesLoading, onStart }: { currentLesson: { module: StudyModule; lesson: StudyLesson }; phrases: Phrase[]; phrasesLoading: boolean; onStart: () => void }) {
  const phraseCount = phrases.length || currentLesson.lesson.phrase_count;
  return (
    <View style={styles.card}>
      <View style={styles.cardHeader}>
        <View style={styles.cardHeaderText}>
          <Text style={styles.cardLabel}>{STRINGS.study.currentLesson}</Text>
          <Text style={styles.cardTitle}>{currentLesson.lesson.title || STRINGS.study.lessonFallback}</Text>
          <Text style={styles.cardDetail}>{currentLesson.module.title}</Text>
        </View>
        <Text style={styles.countPill}>{STRINGS.study.phrasesCount(phraseCount)}</Text>
      </View>
      <Text style={styles.description}>{currentLesson.lesson.description}</Text>
      {phrases.slice(0, 4).map((phrase) => (
        <View style={styles.phraseRow} key={phrase.id}>
          <Text style={styles.phraseSource}>{phrase.source_text}</Text>
          <Text style={styles.phraseTarget}>{phrase.target_text}</Text>
        </View>
      ))}
      {!phrasesLoading && phrases.length === 0 ? <Text style={styles.emptyDetail}>{STRINGS.study.noWordsDetail}</Text> : null}
      <Pressable style={[styles.actionButton, phrasesLoading || phrases.length === 0 ? styles.disabled : null]} disabled={phrasesLoading || phrases.length === 0} onPress={onStart}>
        <Text style={styles.actionText}>{STRINGS.study.studyPhrasesBtn(phraseCount)}</Text>
      </Pressable>
    </View>
  );
}

function ReviewCard({ dueCount, disabled, onReview }: { dueCount: number; disabled: boolean; onReview: () => void }) {
  return (
    <View style={styles.reviewCard}>
      <View style={styles.reviewIcon}><Feather name="rotate-ccw" size={18} color="#14b8a6" /></View>
      <View style={styles.cardHeaderText}>
        <Text style={styles.cardLabel}>{STRINGS.study.reviewNowTitle}</Text>
        <Text style={styles.cardTitle}>{STRINGS.study.reviewNowWords(dueCount)}</Text>
        <Text style={styles.cardDetail}>{STRINGS.study.reviewNowSubtitle}</Text>
      </View>
      <Pressable style={[styles.actionButton, disabled ? styles.disabled : null]} disabled={disabled} onPress={onReview}>
        <Text style={styles.actionText}>{STRINGS.study.reviewBtn}</Text>
      </Pressable>
    </View>
  );
}

function StudyTrail({ modules, currentLessonId, currentPhase, expanded = false }: { modules: StudyModule[]; currentLessonId: number | null; currentPhase: number | null; expanded?: boolean }) {
  return (
    <View style={styles.trail}>
      <Text style={styles.cardLabel}>{STRINGS.study.pathEyebrow}</Text>
      <Text style={styles.cardTitle}>{STRINGS.study.pathTitle}</Text>
      <Text style={styles.cardDetail}>{STRINGS.study.pathDetail}</Text>
      {modules.map((module) => (
        <View style={styles.moduleCard} key={module.id}>
          <View style={styles.moduleHeader}>
            <Text style={styles.moduleLabel}>{STRINGS.study.moduleLabel(module.order)}</Text>
            <Text style={styles.moduleTitle}>{module.title}</Text>
            <Text style={styles.cardDetail}>{STRINGS.study.moduleLessons(module.lessons.length)}</Text>
          </View>
          {(expanded ? module.lessons : module.lessons.slice(0, 5)).map((lesson) => (
            <LessonRow currentLessonId={currentLessonId} currentPhase={currentPhase} key={lesson.id} lesson={lesson} />
          ))}
        </View>
      ))}
    </View>
  );
}

function LessonRow({ lesson, currentLessonId, currentPhase }: { lesson: StudyLesson; currentLessonId: number | null; currentPhase: number | null }) {
  const current = lesson.id === currentLessonId;
  const completed = Boolean(currentPhase && lesson.adventure_phase && lesson.adventure_phase < currentPhase);
  const locked = Boolean(currentPhase && lesson.adventure_phase && lesson.adventure_phase > currentPhase);
  const status = current ? STRINGS.study.current : completed ? STRINGS.study.completed : locked ? STRINGS.study.locked : STRINGS.study.unlocked;
  return (
    <View style={[styles.lessonRow, current ? styles.currentLesson : null]}>
      <Text style={styles.lessonIcon}>{completed ? "✓" : locked ? "•" : "○"}</Text>
      <View style={styles.cardHeaderText}>
        <Text style={styles.lessonTitle}>{lesson.title}</Text>
        <Text style={styles.cardDetail}>{lesson.adventure_phase ? STRINGS.study.phaseLabel(lesson.adventure_phase) : STRINGS.study.lessonFallback} - {status}</Text>
      </View>
      <Text style={styles.lessonCount}>{STRINGS.study.phrasesCount(lesson.phrase_count)}</Text>
    </View>
  );
}

function PhraseLessonRunner({ lesson, phrases, onClose }: { lesson: StudyLesson; phrases: Phrase[]; onClose: () => void }) {
  const [index, setIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const phrase = phrases[index];
  const last = index + 1 >= phrases.length;

  function advance() {
    if (!revealed) {
      setRevealed(true);
      return;
    }
    if (last) {
      onClose();
      return;
    }
    setIndex((item) => item + 1);
    setRevealed(false);
  }

  return (
    <View style={styles.reviewPage}>
      <Text style={styles.eyebrow}>{STRINGS.study.lessonSessionTitle}</Text>
      <Text style={styles.title}>{lesson.title || STRINGS.study.lessonFallback}</Text>
      <Text style={styles.subtitle}>{STRINGS.study.phraseProgress(index + 1, phrases.length)}</Text>
      <View style={styles.lessonRunnerCard}>
        <Text style={styles.cardLabel}>{STRINGS.study.sourcePhrase}</Text>
        <Text style={styles.runnerPhrase}>{phrase.source_text}</Text>
        {revealed ? (
          <>
            <Text style={styles.cardLabel}>{STRINGS.study.targetPhrase}</Text>
            <Text style={styles.runnerTarget}>{phrase.target_text}</Text>
          </>
        ) : null}
      </View>
      <Pressable style={styles.actionButton} onPress={advance}>
        <Text style={styles.actionText}>{!revealed ? STRINGS.study.showTranslation : last ? STRINGS.study.finishLesson : STRINGS.study.nextPhrase}</Text>
      </Pressable>
      <Pressable style={styles.secondaryButton} onPress={onClose}><Text style={styles.secondaryText}>{STRINGS.study.exit}</Text></Pressable>
    </View>
  );
}

function StudyReview({ exercises, onClose }: { exercises: StudySessionData["exercises"]; onClose: () => void }) {
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
  return <View style={styles.state}><Text style={styles.stateText}>{message}</Text></View>;
}

