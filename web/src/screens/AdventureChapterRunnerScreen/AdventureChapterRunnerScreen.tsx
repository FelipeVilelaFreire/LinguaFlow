"use client";

import {
  useAdventurePhaseRunner,
  useAdventureSectionRunner,
} from "@linguaflow/shared-core/hooks/adventure";
import type { AdventureChatEntry } from "@linguaflow/shared-core/hooks/adventure";
import { ROUTES as APP_ROUTES } from "@linguaflow/shared-core";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { useState } from "react";
import styles from "./AdventureChapterRunnerScreen.module.css";

export function AdventureChapterRunnerScreen({ phaseId }: { phaseId: number }) {
  const router = useRouter();
  const search = useSearchParams();
  const phaseNumber = Number(search.get("phase") ?? "1");
  const langCode = search.get("lang") ?? "ES";
  const sourceLangCode = search.get("source") ?? "PT";
  const firstName = search.get("name") ?? "";
  const keyWords = (search.get("words") ?? "").split(",").map((word) => word.trim()).filter(Boolean);

  const runner = useAdventurePhaseRunner({
    phaseId,
    phaseNumber,
    keyWords,
    onExit: () => router.push(APP_ROUTES.adventureMap),
  });

  if (runner.loading) return <State message="Carregando fase..." />;
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
  if (!runner.currentSection) return <State message="Fase sem secoes." />;

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
}) {
  const [input, setInput] = useState("");
  const runner = useAdventureSectionRunner(props);

  function submitInput() {
    runner.submitInput(input);
    setInput("");
  }

  return (
    <main className={styles.page}>
      <header className={styles.topbar}>
        <button onClick={props.onBack} type="button">Voltar</button>
        <span>Secao {props.sectionNumber}/{props.totalSections}</span>
      </header>

      {props.section.recap && (
        <section className={styles.recap}>
          <strong>Onde paramos</strong>
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
            <button onClick={submitInput} type="button">Responder</button>
          </div>
        </section>
      )}

      {(runner.phase === "tap" || runner.phase === "readyComplete") && (
        <section className={styles.footer}>
          <button onClick={runner.continueStep} type="button">
            {runner.phase === "readyComplete" ? "Concluir" : "Continuar"}
          </button>
        </section>
      )}

      {runner.phase === "summary" && runner.summary && (
        <section className={styles.summary}>
          <h1>Secao concluida</h1>
          <div className={styles.metrics}>
            <span>{runner.summary.correct} acertos</span>
            <span>{runner.summary.mistakes} erros</span>
            <span>{runner.summary.xp} XP</span>
          </div>
          {runner.summary.words.length > 0 && (
            <div className={styles.words}>
              {runner.summary.words.map((word) => <span key={word.target}>{word.target}</span>)}
            </div>
          )}
          <button onClick={runner.completeSummary} type="button">Continuar</button>
        </section>
      )}
    </main>
  );
}

function ChatEntryView({ entry }: { entry: AdventureChatEntry }) {
  if (entry.kind === "scene") return <article className={styles.scene}>{entry.text}</article>;
  if (entry.kind === "narrative") return <article className={styles.narrative}>{entry.text}</article>;
  if (entry.kind === "npc") {
    return (
      <article className={styles.npc}>
        <strong>{entry.npc}</strong>
        <p>{entry.line}</p>
        {entry.translation && <span>{entry.translation}</span>}
      </article>
    );
  }
  if (entry.kind === "player") return <article className={styles.player}>{entry.text}</article>;
  if (entry.kind === "answer") {
    return (
      <article className={entry.correct ? styles.correct : styles.wrong}>
        <p>{entry.text}</p>
        {!entry.correct && entry.correctText && <span>Correto: {entry.correctText}</span>}
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
}: {
  stage: "trophy" | "words" | "item";
  phaseNumber: number;
  words: string[];
  earnedItem: { emoji: string; name: string; lore: string; rarity: string } | null;
  onNext: () => void;
}) {
  return (
    <main className={styles.complete}>
      {stage === "trophy" && (
        <>
          <p>Fase concluida</p>
          <h1>Fase {phaseNumber}</h1>
        </>
      )}
      {stage === "words" && (
        <>
          <p>Palavras praticadas</p>
          <div className={styles.words}>{words.map((word) => <span key={word}>{word}</span>)}</div>
        </>
      )}
      {stage === "item" && earnedItem && (
        <>
          <p>Item ganho</p>
          <div className={styles.itemEmoji}>{earnedItem.emoji}</div>
          <h1>{earnedItem.name}</h1>
          <span>{earnedItem.rarity}</span>
          <small>{earnedItem.lore}</small>
        </>
      )}
      <button onClick={onNext} type="button">{stage === "item" ? "Para o mapa" : "Continuar"}</button>
    </main>
  );
}

function State({ message }: { message: string }) {
  return (
    <main className={styles.page}>
      <Link href={APP_ROUTES.adventureMap}>Voltar ao mapa</Link>
      <p>{message}</p>
    </main>
  );
}
