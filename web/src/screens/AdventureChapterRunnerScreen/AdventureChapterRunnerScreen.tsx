"use client";

import {
  useAdventurePhaseRunner,
  useAdventureSectionRunner,
} from "@linguaflow/shared-core/hooks/adventure";
import type { AdventureChatEntry } from "@linguaflow/shared-core/hooks/adventure";
import { getAdventureColors, getAdventureThemeVars, getCharacterAvatar, ROUTES as APP_ROUTES, STRINGS } from "@linguaflow/shared-core";
import { Gift, Star, Trophy, Volume2, VolumeX } from "lucide-react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import type { CSSProperties } from "react";
import { useEffect, useState } from "react";
import { CharacterAvatar } from "@/src/components/shared";
import { audioService } from "@/src/lib/audioService";
import styles from "./AdventureChapterRunnerScreen.module.css";

export function AdventureChapterRunnerScreen({ phaseId }: { phaseId: number }) {
  const router = useRouter();
  const search = useSearchParams();
  const phaseNumber = Number(search.get("phase") ?? "1");
  const langCode = search.get("lang") ?? "ES";
  const sourceLangCode = search.get("source") ?? "PT";
  const firstName = search.get("name") ?? "";
  const keyWords = (search.get("words") ?? "").split(",").map((word) => word.trim()).filter(Boolean);
  const themeStyle = getAdventureThemeVars(getAdventureColors(langCode, "dark")) as CSSProperties;

  const runner = useAdventurePhaseRunner({
    phaseId,
    phaseNumber,
    keyWords,
    onExit: () => router.push(APP_ROUTES.adventureMap),
  });

  if (runner.loading) return <State message={STRINGS.adventure.phaseLoading} style={themeStyle} />;
  if (runner.error) return <State message={runner.error} />;
  if (runner.stage) {
    return (
      <CompletionStage
        stage={runner.stage}
        phaseNumber={runner.phaseNumber}
        words={runner.wordsToShow}
        earnedItem={runner.earnedItem}
        onNext={runner.nextStage}
        style={themeStyle}
      />
    );
  }
  if (!runner.currentSection) return <State message={STRINGS.adventure.phaseEmptySections} style={themeStyle} />;

  return (
    <SectionRunner
      section={runner.currentSection}
      sectionNumber={runner.sectionIndex + 1}
      totalSections={runner.sections.length}
      langCode={langCode}
      sourceLangCode={sourceLangCode}
      firstName={firstName}
      onBack={() => router.push(APP_ROUTES.adventureMap)}
      onComplete={runner.completeSection}
      style={themeStyle}
    />
  );
}

function SectionRunner(props: {
  section: Parameters<typeof useAdventureSectionRunner>[0]["section"];
  sectionNumber: number;
  totalSections: number;
  langCode: string;
  sourceLangCode: string;
  firstName: string;
  onBack: () => void;
  onComplete: (mistakes: number) => void;
  style: CSSProperties;
}) {
  const [input, setInput] = useState("");
  const [muted, setMuted] = useState(() => audioService.muted);
  const runner = useAdventureSectionRunner(props);

  function submitInput() {
    runner.submitInput(input);
    setInput("");
  }

  return (
    <main className={styles.page} style={props.style}>
      <header className={styles.topbar}>
        <button onClick={props.onBack} type="button">{STRINGS.actions.back}</button>
        <span>{STRINGS.adventure.sectionProgress(props.sectionNumber, props.totalSections)}</span>
        <button
          className={styles.audioButton}
          onClick={() => {
            audioService.setMuted(!muted);
            setMuted(audioService.muted);
          }}
          type="button"
        >
          {muted ? <VolumeX size={16} /> : <Volume2 size={16} />}
        </button>
      </header>

      {props.section.recap && (
        <section className={styles.recap}>
          <strong>{STRINGS.adventure.recapTitle}</strong>
          <p>{props.section.recap.story}</p>
          {props.section.recap.now && <span>{props.section.recap.now}</span>}
        </section>
      )}

      <section className={styles.chat}>
        {runner.entries.map((entry) => <ChatEntryView entry={entry} key={entry.id} />)}
      </section>

      {runner.phase === "choosing" && runner.activeChoice && (
        <section className={styles.footer}>
          {runner.activeChoice.question && <p>{runner.activeChoice.question}</p>}
          <div className={styles.choiceGrid}>
            {runner.activeChoice.options.map((option) => (
              <button key={option.id} onClick={() => runner.choose(option.id)} type="button">{option.text}</button>
            ))}
          </div>
        </section>
      )}

      {runner.phase === "input" && runner.activeInput && (
        <section className={styles.footer}>
          <p>{runner.activeInput.prompt}</p>
          {runner.activeInput.hint && <small>{runner.activeInput.hint}</small>}
          <div className={styles.inputRow}>
            <input value={input} onChange={(event) => setInput(event.target.value)} onKeyDown={(event) => event.key === "Enter" && submitInput()} />
            <button onClick={submitInput} type="button">{STRINGS.adventure.answer}</button>
          </div>
        </section>
      )}

      {(runner.phase === "tap" || runner.phase === "readyComplete") && (
        <section className={styles.footer}>
          <button onClick={runner.continueStep} type="button">
            {runner.phase === "readyComplete" ? STRINGS.adventure.finish : STRINGS.actions.continue}
          </button>
        </section>
      )}

      {runner.phase === "summary" && runner.summary && (
        <section className={styles.summary}>
          <h1>{STRINGS.adventure.completeSection}</h1>
          <div className={styles.metrics}>
            <span>{STRINGS.adventure.correctCount(runner.summary.correct)}</span>
            <span>{STRINGS.adventure.mistakesCount(runner.summary.mistakes)}</span>
            <span>{runner.summary.xp} XP</span>
          </div>
          {runner.summary.words.length > 0 && (
            <div className={styles.words}>
              {runner.summary.words.map((word) => <span key={word.target}>{word.target}</span>)}
            </div>
          )}
          <button onClick={runner.completeSummary} type="button">{STRINGS.actions.continue}</button>
        </section>
      )}
    </main>
  );
}

function ChatEntryView({ entry }: { entry: AdventureChatEntry }) {
  useEffect(() => {
    if (entry.kind === "npc") audioService.speakOrPlay(entry.audio_url, entry.line, "ES", entry.npc, entry.pace, entry.voice, entry.speech_rate);
    if (entry.kind === "answer") {
      if (entry.correct) audioService.playCorrect();
      else audioService.playWrong();
    }
  }, [entry]);

  if (entry.kind === "scene") return <article className={styles.scene}>{entry.text}</article>;
  if (entry.kind === "narrative") return <article className={styles.narrative}>{entry.text}</article>;
  if (entry.kind === "npc") {
    const avatar = getCharacterAvatar(entry.npc);
    return (
      <article className={styles.npc}>
        <button
          className={styles.avatarButton}
          onClick={() => audioService.speakOrPlay(entry.audio_url, entry.line, "ES", entry.npc, entry.pace, entry.voice, entry.speech_rate)}
          type="button"
          aria-label={entry.npc}
        >
          <CharacterAvatar emoji="" langCode="ES" name={entry.npc} size={42} slug={avatar?.slug} />
        </button>
        <div>
          <strong>{entry.npc}</strong>
          <p>{entry.line}</p>
          {entry.translation && <span>{entry.translation}</span>}
        </div>
      </article>
    );
  }
  if (entry.kind === "player") return <article className={styles.player}>{entry.text}</article>;
  if (entry.kind === "answer") {
    return (
      <article className={entry.correct ? styles.correct : styles.wrong}>
        <p>{entry.text}</p>
        {!entry.correct && entry.correctText && <span>{STRINGS.adventure.answerCorrect(entry.correctText)}</span>}
      </article>
    );
  }
  if (entry.kind === "pattern") {
    return (
      <article className={styles.pattern}>
        <p>{entry.parts.map((part) => <strong key={`${part.text}-${part.isKey}`}>{part.text}</strong>)}</p>
        <span>{entry.example} · {entry.translation}</span>
        <small>{entry.note}</small>
      </article>
    );
  }
  if (entry.kind === "reveal") return <article className={styles.reveal}><strong>{entry.phrase}</strong><span>{entry.meaning}</span></article>;
  return <article className={styles.vocab}>{entry.items.map((item) => <span key={item.target}>{item.target} · {item.native}</span>)}</article>;
}

function CompletionStage({
  stage,
  phaseNumber,
  words,
  earnedItem,
  onNext,
  style,
}: {
  stage: "trophy" | "words" | "item";
  phaseNumber: number;
  words: string[];
  earnedItem: { emoji: string; name: string; lore: string; rarity: string } | null;
  onNext: () => void;
  style: CSSProperties;
}) {
  useEffect(() => {
    if (stage === "trophy" || stage === "item") audioService.playComplete();
  }, [stage]);

  return (
    <main className={`${styles.complete} ${styles[`complete-${stage}`]}`} style={style}>
      {stage === "trophy" && (
        <>
          <div className={styles.trophyBadge}><Trophy size={42} /></div>
          <p>{STRINGS.adventure.phaseCompleted}</p>
          <h1>{STRINGS.adventure.phaseLabel(phaseNumber)}</h1>
          <div className={styles.stars}>
            {[1, 2, 3].map((star) => <Star fill="currentColor" key={star} size={30} />)}
          </div>
        </>
      )}
      {stage === "words" && (
        <>
          <p>{STRINGS.adventure.practicedWords}</p>
          <div className={styles.words}>{words.map((word) => <span key={word}>{word}</span>)}</div>
        </>
      )}
      {stage === "item" && earnedItem && (
        <>
          <div className={styles.chestReveal}>
            <div className={styles.chestLid} />
            <div className={styles.chestBox}><Gift size={34} /></div>
            <div className={styles.chestTreasure}>{earnedItem.emoji}</div>
            <span className={styles.sparkOne}>✦</span>
            <span className={styles.sparkTwo}>✦</span>
          </div>
          <p>{STRINGS.adventure.earnedItem}</p>
          <h1>{earnedItem.name}</h1>
          <span>{earnedItem.rarity}</span>
          <small>{earnedItem.lore}</small>
        </>
      )}
      <button onClick={onNext} type="button">{stage === "item" ? STRINGS.adventure.backToMap : STRINGS.actions.continue}</button>
    </main>
  );
}

function State({ message, style }: { message: string; style?: CSSProperties }) {
  return (
    <main className={styles.page} style={style}>
      <Link href={APP_ROUTES.adventureMap}>{STRINGS.adventure.backToMap}</Link>
      <p>{message}</p>
    </main>
  );
}

