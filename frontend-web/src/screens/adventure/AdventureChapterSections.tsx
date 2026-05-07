import { ChevronLeft } from "lucide-react";
import { useEffect, useRef, useState } from "react";

import { useStrings } from "../../contexts/StringsContext";
import { getAdventureColors } from "../../theme/adventureColors";

type Colors = ReturnType<typeof getAdventureColors>;

// ── Beat types — Cotidiano only ────────────────────────────────────────────────

export type CotidianoBeat =
  | { kind: "scene";     text: string }
  | { kind: "narrative"; text: string }
  | { kind: "npc";       npc: string; line: string; translation?: string }
  | { kind: "player";    text: string };

// ── Step types — all step-based sections ──────────────────────────────────────

export type SectionStep =
  | { kind: "narrative";       text: string }
  | { kind: "scene";           text: string }
  | { kind: "npc_speak";       npc: string; line: string; translation?: string }
  | { kind: "player_react";    text: string }
  | { kind: "reveal";          phrase: string; meaning: string; note?: string }
  | { kind: "pattern";         parts: Array<{ text: string; isKey: boolean }>; example: string; translation: string; note: string }
  | { kind: "vocab_list";      items: Array<{ target: string; native: string }> }
  | { kind: "multiple_choice"; question: string; options: Array<{ id: string; text: string }>; correct: string; explanation?: string }
  | { kind: "fill_blank";      prompt: string; answer: string }
  | { kind: "translate";       source: string; answer: string };

// ── Section types (backend architecture — not shown to player) ─────────────────

export interface CotidianoSection   { type: "cotidiano";   beats: CotidianoBeat[]; exercises?: SectionStep[] }
export interface VocabularioSection { type: "vocabulario"; steps: SectionStep[] }
export interface PraticaSection     { type: "pratica";     steps: SectionStep[] }
export interface DialogoSection     { type: "dialogo";     steps: SectionStep[] }
export interface GramaticaSection   { type: "gramatica";   steps: SectionStep[] }
export interface ObstaculoSection   { type: "obstaculo";   steps: SectionStep[] }

export type PhaseSection =
  | CotidianoSection
  | VocabularioSection
  | PraticaSection
  | DialogoSection
  | GramaticaSection
  | ObstaculoSection;

// ── Sub-components ─────────────────────────────────────────────────────────────

function SceneBar({ text, c }: { text: string; c: Colors }) {
  return (
    <div
      className="flex items-center gap-2 rounded-xl px-3 py-2.5"
      style={{ background: c.surface, border: `1px solid ${c.borderFaint}`, animation: "narrativeFadeIn 300ms ease-out both" }}
    >
      <p className="text-xs font-medium italic" style={{ color: c.textFaint }}>{text}</p>
    </div>
  );
}

function NpcBubble({ npc, line, translation, c }: {
  npc: string; line: string; translation?: string; c: Colors;
}) {
  const initial = npc.charAt(0).toUpperCase();
  return (
    <div className="flex items-start gap-3" style={{ animation: "narrativeFadeIn 300ms ease-out both" }}>
      <div
        className="mt-0.5 grid h-9 w-9 shrink-0 place-items-center rounded-full text-sm font-bold"
        style={{ background: c.ctaBg, color: "#fff" }}
      >{initial}</div>
      <div className="flex min-w-0 flex-col gap-1">
        <p className="text-[10px] font-bold uppercase tracking-wider" style={{ color: c.goldAccent }}>{npc}</p>
        <div className="rounded-2xl rounded-tl-sm px-4 py-3" style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}>
          <p className="text-base font-semibold italic leading-relaxed" style={{ color: c.parchment }}>"{line}"</p>
          {translation && (
            <p className="mt-1.5 text-xs font-medium" style={{ color: c.textOnBg }}>{translation}</p>
          )}
        </div>
      </div>
    </div>
  );
}

function PlayerBubble({ text, c }: { text: string; c: Colors }) {
  return (
    <div className="flex items-end justify-end gap-2.5" style={{ animation: "narrativeFadeIn 300ms ease-out both" }}>
      <div
        className="rounded-2xl rounded-br-sm px-4 py-3"
        style={{ background: `${c.nodeActive}22`, border: `1px solid ${c.nodeActive}50`, maxWidth: "78%" }}
      >
        <p className="text-base italic leading-relaxed" style={{ color: c.parchment }}>{text}</p>
      </div>
      <div
        className="mb-0.5 grid h-8 w-8 shrink-0 place-items-center rounded-full text-xs font-bold"
        style={{ background: `${c.nodeActive}40`, color: c.parchment }}
      >Eu</div>
    </div>
  );
}

// ── Props & fallback ───────────────────────────────────────────────────────────

const FALLBACK_SECTION: PhaseSection = {
  type: "cotidiano",
  beats: [
    { kind: "scene", text: "Borgo · Manhã" },
    { kind: "npc", npc: "Giovanni", line: "Ciao, forestiero!", translation: "Olá, forasteiro!" },
  ],
  exercises: [],
};

export interface AdventureChapterSectionsProps {
  section?: PhaseSection;
  sectionNumber?: number;
  totalSections?: number;
  phaseNumber: number;
  langCode: string;
  onComplete?: () => void;
  onBack: () => void;
}

// ── Component ─────────────────────────────────────────────────────────────────

export default function AdventureChapterSections({
  section = FALLBACK_SECTION,
  sectionNumber = 1,
  totalSections = 6,
  phaseNumber,
  langCode,
  onComplete = () => {},
  onBack,
}: AdventureChapterSectionsProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, "dark");

  const [beatIdx,        setBeatIdx]        = useState(0);
  const [inExercises,    setInExercises]    = useState(false);
  const [exerciseIdx,    setExerciseIdx]    = useState(0);

  const [stepIdx,   setStepIdx]   = useState(0);
  const [answer,    setAnswer]    = useState<string | null>(null);
  const [revealed,  setRevealed]  = useState(false);

  const contentRef = useRef<HTMLDivElement>(null);

  function nextDialogueOrLast(beats: CotidianoBeat[], from: number): number {
    for (let i = from; i < beats.length; i++) {
      if (beats[i].kind === "npc" || beats[i].kind === "player") return i;
    }
    return beats.length - 1;
  }

  // Returns the last scene/narrative beat before the first npc/player beat.
  // This lets the opening context appear automatically; first tap reveals the NPC.
  function lastContextBeat(beats: CotidianoBeat[]): number {
    for (let i = 0; i < beats.length; i++) {
      if (beats[i].kind === "npc" || beats[i].kind === "player") return Math.max(0, i - 1);
    }
    return beats.length - 1;
  }

  useEffect(() => {
    if (section.type === "cotidiano") {
      setBeatIdx(lastContextBeat(section.beats));
      setInExercises(false);
      setExerciseIdx(0);
    } else {
      setStepIdx(0);
    }
    setAnswer(null);
    setRevealed(false);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [section]);

  useEffect(() => {
    if (section.type === "cotidiano" && !inExercises && contentRef.current) {
      contentRef.current.scrollTo({ top: contentRef.current.scrollHeight, behavior: "smooth" });
    }
  }, [beatIdx, inExercises, section.type]);

  const isCotidiano  = section.type === "cotidiano";
  const cotExercises = isCotidiano ? (section.exercises ?? []) : [];

  // Unified "active step" — cotidiano exercise phase OR section steps
  const hasSteps    = "steps" in section;
  const steps       = hasSteps ? section.steps : [];
  const activeStep: SectionStep | null = isCotidiano
    ? (inExercises ? (cotExercises[exerciseIdx] ?? null) : null)
    : (steps[stepIdx] ?? null);
  const activeStepCount: number | null = isCotidiano
    ? (inExercises ? cotExercises.length : null)
    : steps.length;
  const activeStepIdx = isCotidiano ? exerciseIdx : stepIdx;

  const canContinue = (() => {
    if (isCotidiano && !inExercises) return true;
    if (!activeStep) return true;
    if (activeStep.kind === "fill_blank" || activeStep.kind === "translate") return revealed;
    if (activeStep.kind === "multiple_choice") {
      return section.type === "obstaculo" ? answer === activeStep.correct : answer !== null;
    }
    return true;
  })();

  function advance() {
    if (isCotidiano) {
      if (inExercises) {
        if (exerciseIdx >= cotExercises.length - 1) { onComplete(); return; }
        setExerciseIdx(i => i + 1);
        setAnswer(null);
        setRevealed(false);
        return;
      }
      if (beatIdx >= section.beats.length - 1) {
        if (cotExercises.length > 0) { setInExercises(true); setAnswer(null); setRevealed(false); return; }
        onComplete();
        return;
      }
      setBeatIdx(nextDialogueOrLast(section.beats, beatIdx + 1));
      return;
    }
    if (stepIdx >= steps.length - 1) { onComplete(); return; }
    setStepIdx(i => i + 1);
    setAnswer(null);
    setRevealed(false);
  }

  // ── Shared multiple-choice renderer ─────────────────────────────────────────

  function renderChoice(opts: {
    question: string;
    options: Array<{ id: string; text: string }>;
    correct: string;
    explanation?: string;
    currentAnswer: string | null;
    onPick: (id: string) => void;
    gated: boolean;
    animKey: string;
  }) {
    const { question, options, correct, explanation, currentAnswer, onPick, gated, animKey } = opts;
    const isCorrect = currentAnswer === correct;
    return (
      <div key={animKey} className="flex flex-col gap-4" style={{ animation: "fadeIn 250ms ease-out both" }}>
        <p className="px-1 text-base font-semibold leading-snug" style={{ color: c.parchment }}>{question}</p>
        <div className="flex flex-col gap-2">
          {options.map(({ id, text }) => {
            const chosen  = currentAnswer === id;
            const isRight = id === correct;
            let bg = c.surfaceMid, border = c.borderFaint, color = c.textOnBg;
            if (chosen  && isRight)  { bg = "#16a34a22"; border = "#16a34a80"; color = "#4ade80"; }
            if (chosen  && !isRight) { bg = "#dc262622"; border = "#dc262680"; color = "#f87171"; }
            if (!chosen && currentAnswer && isRight) { bg = "#16a34a22"; border = "#16a34a80"; color = "#4ade80"; }
            return (
              <button
                key={id}
                type="button"
                onClick={() => { if (gated ? currentAnswer !== correct : !currentAnswer) onPick(id); }}
                className="w-full rounded-xl px-4 py-3.5 text-left text-sm font-semibold transition active:scale-[0.98]"
                style={{ background: bg, border: `1px solid ${border}`, color }}
              >{text}</button>
            );
          })}
        </div>
        {currentAnswer && (
          <p
            className="px-1 text-sm font-semibold"
            style={{ color: isCorrect ? "#4ade80" : "#f87171", animation: "fadeIn 180ms ease-out both" }}
          >
            {isCorrect
              ? (explanation ?? s.adventure.obstacleCorrect)
              : s.adventure.obstacleWrong}
          </p>
        )}
      </div>
    );
  }

  return (
    <div className="flex h-full flex-col">

      {/* Header */}
      <header className="shrink-0 px-4 pb-2 pt-3">
        <div className="mb-3 flex items-center gap-3">
          <button
            type="button"
            onClick={onBack}
            className="flex items-center gap-1.5 rounded-full px-3 py-2 text-sm font-semibold"
            style={{ background: c.surface, color: c.parchment }}
          >
            <ChevronLeft size={15} />
            {s.adventure.exit}
          </button>
          <div className="flex flex-col gap-0.5">
            <p className="text-xs font-bold" style={{ color: c.goldAccent }}>
              {s.adventure.phaseLabel(phaseNumber)} · {s.adventure.sectionLabel(sectionNumber, totalSections)}
            </p>
            {activeStepCount != null && (
              <p className="text-[10px] font-semibold" style={{ color: c.textFaint }}>
                {activeStepIdx + 1} / {activeStepCount}
              </p>
            )}
          </div>
        </div>

        {/* Section progress */}
        <div className="flex gap-1.5">
          {Array.from({ length: totalSections }, (_, i) => (
            <div
              key={i}
              className="h-1.5 flex-1 rounded-full transition-all duration-300"
              style={{
                background:
                  i < sectionNumber - 1  ? c.nodeCompleted :
                  i === sectionNumber - 1 ? c.nodeActive :
                  c.surface,
              }}
            />
          ))}
        </div>

        {/* Step progress within section */}
        {activeStepCount != null && (
          <div className="mt-1.5 flex gap-1">
            {Array.from({ length: activeStepCount }, (_, i) => (
              <div
                key={i}
                className="h-1 flex-1 rounded-full transition-all duration-300"
                style={{
                  background:
                    i < activeStepIdx  ? c.nodeCompleted :
                    i === activeStepIdx ? c.goldAccent :
                    c.surface,
                }}
              />
            ))}
          </div>
        )}
      </header>

      {/* Content */}
      <div ref={contentRef} className="flex-1 overflow-y-auto px-4 pb-4 pt-3">

        {/* ── Cotidiano — accumulated chat (beat phase only) ────────────────── */}
        {isCotidiano && !inExercises && (
          <div className="flex flex-col gap-4">
            {section.beats.slice(0, beatIdx + 1).map((beat, i) => {
              const delay = `${i * 160}ms`;
              if (beat.kind === "scene") return (
                <div key={i} style={{ animationDelay: delay }}><SceneBar text={beat.text} c={c} /></div>
              );
              if (beat.kind === "narrative") return (
                <div
                  key={i}
                  className="flex flex-col gap-3 px-1"
                  style={{ animation: "narrativeFadeIn 350ms ease-out both", animationDelay: delay }}
                >
                  {beat.text.split("\n\n").map((para, j) => (
                    <p key={j} className="text-base leading-relaxed" style={{ color: c.textOnBg }}>{para}</p>
                  ))}
                </div>
              );
              if (beat.kind === "npc") return (
                <NpcBubble key={i} npc={beat.npc} line={beat.line} translation={beat.translation} c={c} />
              );
              if (beat.kind === "player") return <PlayerBubble key={i} text={beat.text} c={c} />;
              return null;
            })}
          </div>
        )}

        {/* ── Active step — exercises (cotidiano phase 2) OR section steps ─── */}
        {activeStep && (() => {
          const step = activeStep;
          const key  = `${sectionNumber}-${activeStepIdx}`;

          if (step.kind === "scene") return <SceneBar key={key} text={step.text} c={c} />;

          if (step.kind === "narrative") return (
            <div key={key} className="flex flex-col gap-3 px-1" style={{ animation: "fadeIn 250ms ease-out both" }}>
              {step.text.split("\n\n").map((para, j) => (
                <p key={j} className="text-base leading-relaxed" style={{ color: c.textOnBg }}>{para}</p>
              ))}
            </div>
          );

          if (step.kind === "npc_speak") return (
            <NpcBubble key={key} npc={step.npc} line={step.line} translation={step.translation} c={c} />
          );

          if (step.kind === "player_react") return (
            <PlayerBubble key={key} text={step.text} c={c} />
          );

          if (step.kind === "reveal") return (
            <div key={key} className="flex flex-col gap-4" style={{ animation: "fadeIn 250ms ease-out both" }}>
              <div
                className="flex flex-col items-center gap-3 rounded-2xl px-6 py-10 text-center"
                style={{ background: `${c.goldAccent}18`, border: `1px solid ${c.goldAccent}45` }}
              >
                <p className="text-3xl font-bold italic" style={{ color: c.parchment }}>{step.phrase}</p>
                <p className="text-lg font-semibold" style={{ color: c.goldAccent }}>{step.meaning}</p>
              </div>
              {step.note && (
                <p className="px-2 text-xs italic leading-relaxed" style={{ color: c.textFaint }}>💡 {step.note}</p>
              )}
            </div>
          );

          if (step.kind === "pattern") return (
            <div key={key} className="flex flex-col gap-4" style={{ animation: "fadeIn 250ms ease-out both" }}>
              <div className="flex flex-col gap-4 rounded-2xl p-4" style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}>
                <div>
                  <p className="mb-2.5 text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
                    {s.adventure.patternFormula}
                  </p>
                  <div className="flex flex-wrap items-center gap-2">
                    {step.parts.map((part, i) =>
                      part.isKey ? (
                        <span key={i} className="rounded-lg px-3 py-1.5 text-sm font-bold"
                          style={{ background: `${c.goldAccent}20`, color: c.goldAccent, border: `1px solid ${c.goldAccent}45` }}
                        >{part.text}</span>
                      ) : (
                        <span key={i} className="text-sm font-semibold" style={{ color: c.textFaint }}>{part.text}</span>
                      )
                    )}
                  </div>
                </div>
                <div className="rounded-xl px-4 py-3" style={{ background: c.surface }}>
                  <p className="text-base font-bold italic" style={{ color: c.parchment }}>{step.example}</p>
                  <p className="mt-0.5 text-sm font-medium" style={{ color: c.textOnBg }}>{step.translation}</p>
                </div>
                <p className="text-xs italic leading-relaxed" style={{ color: c.textFaint }}>💡 {step.note}</p>
              </div>
            </div>
          );

          if (step.kind === "vocab_list") return (
            <div key={key} className="flex flex-col gap-2" style={{ animation: "fadeIn 250ms ease-out both" }}>
              {step.items.map(({ target, native }, i) => (
                <div
                  key={target}
                  className="flex items-center justify-between rounded-xl px-4 py-3"
                  style={{
                    background: c.surfaceMid,
                    border: `1px solid ${c.borderFaint}`,
                    animation: `narrativeFadeIn 250ms ease-out ${i * 70}ms both`,
                  }}
                >
                  <span className="text-base font-bold italic" style={{ color: c.parchment }}>{target}</span>
                  <span className="text-sm font-medium" style={{ color: c.textOnBg }}>{native}</span>
                </div>
              ))}
            </div>
          );

          if (step.kind === "multiple_choice") return renderChoice({
            question:      step.question,
            options:       step.options,
            correct:       step.correct,
            explanation:   step.explanation,
            currentAnswer: answer,
            onPick:        (id) => { if (!answer || (section.type === "obstaculo" && answer !== step.correct)) setAnswer(id); },
            gated:         section.type === "obstaculo",
            animKey:       key,
          });

          if (step.kind === "fill_blank") return (
            <div key={key} className="flex flex-col gap-4" style={{ animation: "fadeIn 250ms ease-out both" }}>
              <div
                className="flex flex-col items-center gap-5 rounded-2xl px-5 py-10 text-center"
                style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
              >
                <p className="text-2xl font-bold italic" style={{ color: c.parchment }}>{step.prompt}</p>
                {revealed ? (
                  <p className="text-sm font-semibold leading-relaxed"
                    style={{ color: c.goldAccent, animation: "fadeIn 200ms ease-out both" }}
                  >{step.answer}</p>
                ) : (
                  <button type="button" onClick={() => setRevealed(true)}
                    className="rounded-xl px-5 py-2.5 text-sm font-bold transition active:scale-[0.98]"
                    style={{ background: c.surface, color: c.textOnBg, border: `1px solid ${c.borderFaint}` }}
                  >{s.adventure.practiceReveal}</button>
                )}
              </div>
            </div>
          );

          if (step.kind === "translate") return (
            <div key={key} className="flex flex-col gap-4" style={{ animation: "fadeIn 250ms ease-out both" }}>
              <div
                className="flex flex-col items-center gap-5 rounded-2xl px-5 py-10 text-center"
                style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
              >
                <p className="text-[10px] font-bold uppercase tracking-wider" style={{ color: c.textFaint }}>
                  {s.adventure.translatePrompt}
                </p>
                <p className="text-xl font-semibold" style={{ color: c.parchment }}>{step.source}</p>
                {revealed ? (
                  <p className="text-base font-bold italic"
                    style={{ color: c.goldAccent, animation: "fadeIn 200ms ease-out both" }}
                  >{step.answer}</p>
                ) : (
                  <button type="button" onClick={() => setRevealed(true)}
                    className="rounded-xl px-5 py-2.5 text-sm font-bold transition active:scale-[0.98]"
                    style={{ background: c.surface, color: c.textOnBg, border: `1px solid ${c.borderFaint}` }}
                  >{s.adventure.practiceReveal}</button>
                )}
              </div>
            </div>
          );

          return null;
        })()}

      </div>

      {/* Continue button */}
      <div className="shrink-0 px-4 pb-6 pt-2">
        <button
          type="button"
          disabled={!canContinue}
          onClick={advance}
          className="flex h-14 w-full items-center justify-center rounded-2xl text-base font-bold transition"
          style={{ background: canContinue ? c.ctaBg : c.surface, color: canContinue ? "#fff" : c.textFaint }}
        >
          {s.actions.continue}
        </button>
      </div>

    </div>
  );
}
