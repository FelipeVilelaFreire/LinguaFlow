import { router, useLocalSearchParams } from "expo-router";
import { useState } from "react";
import { Pressable, ScrollView, Text, TextInput, View } from "react-native";
import {
  useAdventurePhaseRunner,
  useAdventureSectionRunner,
} from "@linguaflow/shared-core/hooks/adventure";
import type { AdventureChatEntry } from "@linguaflow/shared-core/hooks/adventure";
import { STRINGS, type PhaseSection } from "@linguaflow/shared-core";
import { styles } from "./AdventureChapterRunnerScreen.styles";

export function AdventureChapterRunnerScreen({ phaseId }: { phaseId: number }) {
  const params = useLocalSearchParams<{ phase?: string; lang?: string; source?: string; name?: string; words?: string }>();
  const phaseNumber = Number(params.phase ?? "1");
  const langCode = params.lang ?? "ES";
  const sourceLangCode = params.source ?? "PT";
  const firstName = params.name ?? "";
  const keyWords = (params.words ?? "").split(",").map((word) => word.trim()).filter(Boolean);

  const runner = useAdventurePhaseRunner({
    phaseId,
    phaseNumber,
    keyWords,
    onExit: () => router.replace("/adventure/map"),
  });

  if (runner.loading) return <State message={STRINGS.adventure.phaseLoading} />;
  if (runner.error) return <State message={runner.error} />;
  if (runner.stage) {
    return (
      <CompletionStage
        stage={runner.stage}
        phaseNumber={runner.phaseNumber}
        words={runner.wordsToShow}
        earnedItem={runner.earnedItem}
        onNext={runner.nextStage}
      />
    );
  }
  if (!runner.currentSection) return <State message={STRINGS.adventure.phaseEmptySections} />;

  return (
    <SectionRunner
      section={runner.currentSection}
      sectionNumber={runner.sectionIndex + 1}
      totalSections={runner.sections.length}
      langCode={langCode}
      sourceLangCode={sourceLangCode}
      firstName={firstName}
      onBack={() => router.replace("/adventure/map")}
      onComplete={runner.completeSection}
    />
  );
}

function SectionRunner({
  section,
  sectionNumber,
  totalSections,
  langCode,
  sourceLangCode,
  firstName,
  onBack,
  onComplete,
}: {
  section: PhaseSection;
  sectionNumber: number;
  totalSections: number;
  langCode: string;
  sourceLangCode: string;
  firstName: string;
  onBack: () => void;
  onComplete: (mistakes: number) => void;
}) {
  const [input, setInput] = useState("");
  const runner = useAdventureSectionRunner({ section, sectionNumber, langCode, sourceLangCode, firstName, onComplete });

  function submitInput() {
    runner.submitInput(input);
    setInput("");
  }

  return (
    <View style={styles.container}>
      <View style={styles.topbar}>
        <Pressable style={styles.backButton} onPress={onBack}><Text style={styles.backText}>{STRINGS.actions.back}</Text></Pressable>
        <Text style={styles.sectionLabel}>{STRINGS.adventure.sectionLabel(sectionNumber, totalSections)}</Text>
      </View>

      <ScrollView style={styles.chat} contentContainerStyle={styles.chatContent}>
        {section.recap ? (
          <View style={styles.recap}>
            <Text style={styles.recapTitle}>{STRINGS.adventure.recapTitle}</Text>
            <Text style={styles.recapText}>{section.recap.story}</Text>
            {section.recap.now ? <Text style={styles.recapNow}>{section.recap.now}</Text> : null}
          </View>
        ) : null}
        {runner.entries.map((entry) => <ChatEntryView entry={entry} key={entry.id} />)}
        {runner.phase === "summary" && runner.summary ? (
          <View style={styles.summary}>
            <Text style={styles.completeTitle}>{STRINGS.adventure.completeSection}</Text>
            <Text style={styles.meta}>{STRINGS.adventure.correctCount(runner.summary.correct)} · {STRINGS.adventure.mistakesCount(runner.summary.mistakes)} · {runner.summary.xp} XP</Text>
            <Pressable style={styles.primaryButton} onPress={runner.completeSummary}><Text style={styles.primaryText}>{STRINGS.actions.continue}</Text></Pressable>
          </View>
        ) : null}
      </ScrollView>

      {runner.phase === "choosing" && runner.activeChoice ? (
        <View style={styles.footer}>
          {runner.activeChoice.question ? <Text style={styles.footerPrompt}>{runner.activeChoice.question}</Text> : null}
          {runner.activeChoice.options.map((option) => (
            <Pressable style={styles.choice} key={option.id} onPress={() => runner.choose(option.id)}>
              <Text style={styles.choiceText}>{option.text}</Text>
            </Pressable>
          ))}
        </View>
      ) : null}

      {runner.phase === "input" && runner.activeInput ? (
        <View style={styles.footer}>
          <Text style={styles.footerPrompt}>{runner.activeInput.prompt}</Text>
          <View style={styles.inputRow}>
            <TextInput style={styles.input} value={input} onChangeText={setInput} autoCapitalize="none" />
            <Pressable style={styles.inputButton} onPress={submitInput}><Text style={styles.primaryText}>OK</Text></Pressable>
          </View>
        </View>
      ) : null}

      {(runner.phase === "tap" || runner.phase === "readyComplete") ? (
        <View style={styles.footer}>
          <Pressable style={styles.primaryButton} onPress={runner.continueStep}>
            <Text style={styles.primaryText}>{runner.phase === "readyComplete" ? STRINGS.adventure.finish : STRINGS.actions.continue}</Text>
          </Pressable>
        </View>
      ) : null}
    </View>
  );
}

function ChatEntryView({ entry }: { entry: AdventureChatEntry }) {
  if (entry.kind === "scene") return <Text style={styles.scene}>{entry.text}</Text>;
  if (entry.kind === "narrative") return <Text style={styles.narrative}>{entry.text}</Text>;
  if (entry.kind === "npc") {
    return (
      <View style={styles.npc}>
        <Text style={styles.npcName}>{entry.npc}</Text>
        <Text style={styles.npcLine}>{entry.line}</Text>
        {entry.translation ? <Text style={styles.translation}>{entry.translation}</Text> : null}
      </View>
    );
  }
  if (entry.kind === "player") return <Text style={styles.player}>{entry.text}</Text>;
  if (entry.kind === "answer") {
    return (
      <View style={entry.correct ? styles.correct : styles.wrong}>
        <Text style={styles.answerText}>{entry.text}</Text>
        {!entry.correct && entry.correctText ? <Text style={styles.translation}>{STRINGS.adventure.answerCorrect(entry.correctText)}</Text> : null}
      </View>
    );
  }
  if (entry.kind === "pattern") {
    return (
      <View style={styles.narrativeBox}>
        <Text style={styles.npcLine}>{entry.example}</Text>
        <Text style={styles.translation}>{entry.translation}</Text>
        <Text style={styles.translation}>{entry.note}</Text>
      </View>
    );
  }
  if (entry.kind === "reveal") return <View style={styles.narrativeBox}><Text style={styles.reveal}>{entry.phrase}</Text><Text style={styles.translation}>{entry.meaning}</Text></View>;
  return <View style={styles.narrativeBox}>{entry.items.map((item) => <Text style={styles.vocab} key={item.target}>{item.target} · {item.native}</Text>)}</View>;
}

function CompletionStage({
  stage,
  phaseNumber,
  words,
  earnedItem,
  onNext,
}: {
  stage: "trophy" | "words" | "item";
  phaseNumber: number;
  words: string[];
  earnedItem: { emoji: string; name: string; lore: string; rarity: string } | null;
  onNext: () => void;
}) {
  return (
    <View style={styles.complete}>
      {stage === "trophy" ? (
        <>
          <View style={styles.trophyBadge}><Text style={styles.trophyIcon}>🏆</Text></View>
          <Text style={styles.meta}>{STRINGS.adventure.phaseCompleted}</Text>
          <Text style={styles.completeTitle}>{STRINGS.adventure.phaseLabel(phaseNumber)}</Text>
          <Text style={styles.starRow}>★ ★ ★</Text>
        </>
      ) : null}
      {stage === "words" ? <><Text style={styles.meta}>{STRINGS.adventure.practicedWords}</Text>{words.map((word) => <Text style={styles.wordChip} key={word}>{word}</Text>)}</> : null}
      {stage === "item" && earnedItem ? (
        <>
          <View style={styles.chestReveal}>
            <Text style={styles.chestSparkLeft}>✦</Text>
            <Text style={styles.chestLid}>▔▔▔</Text>
            <Text style={styles.chestBox}>▰</Text>
            <Text style={styles.itemEmoji}>{earnedItem.emoji}</Text>
            <Text style={styles.chestSparkRight}>✦</Text>
          </View>
          <Text style={styles.meta}>{STRINGS.adventure.earnedItem}</Text>
          <Text style={styles.completeTitle}>{earnedItem.name}</Text>
          <Text style={styles.meta}>{earnedItem.rarity}</Text>
          <Text style={styles.translation}>{earnedItem.lore}</Text>
        </>
      ) : null}
      <Pressable style={styles.primaryButton} onPress={onNext}><Text style={styles.primaryText}>{stage === "item" ? STRINGS.adventure.backToMap : STRINGS.actions.continue}</Text></Pressable>
    </View>
  );
}

function State({ message }: { message: string }) {
  return (
    <View style={styles.complete}>
      <Text style={styles.translation}>{message}</Text>
    </View>
  );
}
