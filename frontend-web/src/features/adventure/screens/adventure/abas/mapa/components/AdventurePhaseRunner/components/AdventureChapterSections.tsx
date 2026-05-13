import { Check, ChevronLeft, Flame, History, Lightbulb, Moon, Sparkles, Sun, Sunset, Volume2 } from "lucide-react";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";

import CharacterAvatar from "../../../../../../../components/CharacterAvatar";
import CharacterProfileModal from "../../../../../../../components/CharacterProfileModal";
import Emoji from "../../../../../../../../../components/Emoji";
import { CHARACTER_AVATARS } from "../../../../../../../constants/characterAvatars";
import { getCharacterProfile } from "../../../../../../../constants/characterProfiles";
import { useStrings } from "../../../../../../../../../contexts/StringsContext";
import { PLAYER_PRONOUN } from "../../../../../../../../../constants/playerPronoun";
import { adventureService } from "../../../../../../../../../services/adventureService";
import { audioService } from "../../../../../../../../../services/audioService";
import { getAdventureColors } from "../../../../../../../theme/adventureColors";
import type { PhaseSection, SectionRecap, SectionStep, VoiceProfile } from "../../../../../../../../../types/sections";

type Colors = ReturnType<typeof getAdventureColors>;

// ── Chat entry — each item accumulated in the scroll ─────────────────────────

type ChatEntry = { id: string } & (
  | { kind: "narrative";      text: string }
  | { kind: "npc";            npc: string; line: string; translation?: string; isNew?: boolean; pace?: string; speech_rate?: number; voice?: VoiceProfile }
  | { kind: "npc_reaction";   npc: string; line: string }
  | { kind: "situation";      context: string; prompt: string }
  | { kind: "player_text";    text: string; label: string }
  | { kind: "player_answer";  text: string; label: string; correct: boolean }
  | { kind: "wrong_hint";     correctText: string }
  | { kind: "pattern";        parts: Array<{ text: string; isKey: boolean }>; example: string; translation: string; note: string }
  | { kind: "reveal";         phrase: string; meaning: string; note?: string }
  | { kind: "vocab_list";     items: Array<{ target: string; native: string }> }
);

type ActiveChoice = {
  question:      string;
  options:       Array<{ id: string; text: string }>;
  correct:       string;
  npc?:          string;
  npc_reaction?: string;
  isGated:       boolean;
  shaking:       boolean;
};

type FloatBadge = { id: string; x: number; bottomPx: number; text: string; isCombo: boolean };
type SelectedCharacter = { name: string; slug?: string; emoji?: string };

function formatSpeedLabel(speed: number): string {
  return `${Number.isInteger(speed) ? speed.toFixed(0) : String(speed)}x`;
}

// ── Normalize section → flat SectionStep[] ───────────────────────────────────

function normalizeSection(section: PhaseSection): SectionStep[] {
  if (section.type !== "narrativa") return section.steps;
  const fromBeats: SectionStep[] = section.beats.map(b => {
    if (b.kind === "npc")    return { ...b, kind: "npc_speak"    as const };
    if (b.kind === "player") return { ...b, kind: "player_react" as const };
    return b;
  });
  return [...fromBeats, ...(section.exercises ?? [])];
}

// ── Scene card — parses "🏘️  Location · Time · Episode" ─────────────────────

function SceneCard({ text, c, onTap }: { text: string; c: Colors; onTap: () => void }) {
  const parts    = text.split(" · ");
  const location = parts[0] ?? text;
  const time     = parts[1];
  const episode  = parts[2];
  return (
    <div
      className="absolute inset-0 z-20 flex flex-col items-center justify-center gap-5 cursor-pointer select-none"
      style={{ background: "rgba(0,0,0,0.93)", animation: "narrativeFadeIn 500ms ease-out both" }}
      onClick={onTap}
    >
      <div className="flex flex-col items-center gap-3 px-8 text-center">
        {episode && (
          <p
            className="text-xs font-bold uppercase tracking-widest"
            style={{ color: c.goldAccent }}
          >
            {episode}
          </p>
        )}
        <p className="text-2xl font-bold leading-snug md:text-3xl" style={{ color: c.parchment }}>
          {location}
        </p>
        {time && (
          <p className="text-sm font-medium md:text-base" style={{ color: c.textOnBg }}>
            {time}
          </p>
        )}
      </div>
      <p
        className="absolute bottom-14 text-xs font-semibold tracking-wide"
        style={{ color: c.textFaint, animation: "tapPulse 1.8s ease-in-out infinite" }}
      >
        toque para continuar  ›
      </p>
    </div>
  );
}

// ── Recap card — "Me relembre onde paramos" overlay opened by header button ──

function RecapCard({ recap, c, langCode, onCharacterOpen, onClose, labels }: {
  recap: SectionRecap;
  c: Colors;
  langCode: string;
  onCharacterOpen: (character: SelectedCharacter) => void;
  onClose: () => void;
  labels: { eyebrow: string; now: string; close: string };
}) {
  return (
    <div
      className="absolute inset-0 z-30 flex flex-col"
      style={{ background: "rgba(0,0,0,0.97)", animation: "narrativeFadeIn 350ms ease-out both" }}
    >
      <div className="flex flex-1 flex-col gap-6 overflow-y-auto px-6 pb-4 pt-14">

        <div className="flex flex-col gap-4" style={{ animation: "narrativeFadeIn 400ms 80ms ease-out both" }}>
          <p className="text-[11px] font-bold uppercase tracking-[0.2em]" style={{ color: c.goldAccent }}>
            ✦ {labels.eyebrow}
          </p>

          {recap.characters && recap.characters.length > 0 && (
            <div className="flex flex-wrap gap-2">
              {recap.characters.map((name) => {
                const avatar = CHARACTER_AVATARS[name];
                return (
                  <div
                    key={name}
                    className="flex items-center gap-2 rounded-full py-1 pl-1 pr-3"
                    style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
                  >
                    <button
                      type="button"
                      className="rounded-full transition active:scale-95"
                      onClick={() => onCharacterOpen({ name, slug: avatar?.slug, emoji: avatar?.emoji })}
                    >
                      <CharacterAvatar
                        slug={avatar?.slug}
                        emoji={avatar?.emoji}
                        name={name}
                        langCode={langCode}
                        size={28}
                        fallbackBg={c.ctaBg}
                      />
                    </button>
                    <span className="text-sm font-semibold" style={{ color: c.parchment }}>
                      {name}
                    </span>
                  </div>
                );
              })}
            </div>
          )}
        </div>

        <div style={{ animation: "narrativeFadeIn 400ms 200ms ease-out both" }}>
          {recap.story.split("\n\n").map((para, i) => (
            <p
              key={i}
              className="text-base leading-[1.8] md:text-[17px]"
              style={{
                color: c.parchment,
                marginBottom: i < recap.story.split("\n\n").length - 1 ? "0.85rem" : 0,
              }}
            >
              {para}
            </p>
          ))}
        </div>

        {recap.now && (
          <div
            className="flex flex-col gap-2 rounded-2xl px-4 py-4"
            style={{
              background: c.surface,
              border: `1px solid ${c.borderFaint}`,
              animation: "narrativeFadeIn 400ms 350ms ease-out both",
            }}
          >
            <p className="text-[10px] font-bold uppercase tracking-widest" style={{ color: c.goldAccent }}>
              {labels.now}
            </p>
            <p className="text-[15px] leading-relaxed md:text-base" style={{ color: c.textOnBg }}>
              {recap.now}
            </p>
          </div>
        )}
      </div>

      <div className="shrink-0 px-4 pb-6 pt-2">
        <button
          type="button"
          onClick={onClose}
          className="w-full rounded-2xl py-4 text-base font-bold transition active:scale-[0.97]"
          style={{ background: c.goldAccent, color: "#1a0800" }}
        >
          {labels.close}
        </button>
      </div>
    </div>
  );
}

// ── Section complete overlay ──────────────────────────────────────────────────

function SectionCompleteOverlay({ sectionNumber, totalSections, c }: {
  sectionNumber: number; totalSections: number; c: Colors;
}) {
  return (
    <div
      className="absolute inset-0 z-30 flex flex-col items-center justify-center gap-6 pointer-events-none"
      style={{ background: "rgba(0,0,0,0.92)", animation: "narrativeFadeIn 350ms ease-out both" }}
    >
      {/* glow pulse behind checkmark */}
      <div className="relative flex items-center justify-center">
        <div
          className="absolute rounded-full"
          style={{
            width: 120, height: 120,
            background: `radial-gradient(circle, ${c.goldAccent}25 0%, transparent 70%)`,
            animation: "progressGlow 1.8s ease-in-out infinite",
          }}
        />
        <div
          className="relative grid h-20 w-20 place-items-center rounded-full"
          style={{
            background: `${c.goldAccent}15`,
            border: `1.5px solid ${c.goldAccent}60`,
            boxShadow: `0 0 32px ${c.goldAccent}30`,
            animation: "successPop 500ms 200ms cubic-bezier(0.16,1,0.3,1) both",
          }}
        >
          <Check size={32} style={{ color: c.goldAccent }} />
        </div>
      </div>
      <div
        className="flex flex-col items-center gap-2 text-center"
        style={{ animation: "narrativeFadeIn 450ms 380ms ease-out both" }}
      >
        <p className="text-xs font-bold uppercase tracking-widest" style={{ color: c.goldAccent }}>
          Seção {sectionNumber} de {totalSections}
        </p>
        <p className="text-2xl font-bold leading-snug md:text-3xl" style={{ color: c.parchment }}>
          Concluída
        </p>
      </div>
    </div>
  );
}

// ── Sub-components ────────────────────────────────────────────────────────────

function NarrativeEntry({ text, c }: { text: string; c: Colors }) {
  return (
    <div className="px-1">
      {text.split("\n\n").map((para, i) => (
        <p
          key={i}
          className="text-base leading-[1.9] md:text-[17px]"
          style={{ color: c.textOnBg, marginBottom: i < text.split("\n\n").length - 1 ? "0.75rem" : 0 }}
        >
          {para}
        </p>
      ))}
    </div>
  );
}

function NpcEntry({ npc, line, translation, isNew, langCode, pace, speechRate, voice, ttsSpeed, onCycleSpeed, onCharacterOpen, c }: {
  npc: string; line: string; translation?: string; isNew?: boolean; langCode: string; pace?: string; speechRate?: number; voice?: VoiceProfile;
  ttsSpeed?: number; onCycleSpeed?: () => void; onCharacterOpen: (character: SelectedCharacter) => void; c: Colors;
}) {
  const avatar = CHARACTER_AVATARS[npc];
  return (
    <div className="flex items-end gap-3" style={{ maxWidth: "88%" }}>
      <button
        type="button"
        className="mb-0.5 rounded-full transition active:scale-95"
        onClick={() => onCharacterOpen({ name: npc, slug: avatar?.slug, emoji: avatar?.emoji })}
      >
        <CharacterAvatar
          slug={avatar?.slug}
          emoji={avatar?.emoji}
          name={npc}
          langCode={langCode}
          size={36}
          fallbackBg={c.ctaBg}
        />
      </button>
      <div className="flex flex-col gap-1">
        {isNew && (
          <span
            className="mb-0.5 w-fit rounded-full px-2 py-0.5 text-[9px] font-bold uppercase tracking-widest"
            style={{ background: `${c.goldAccent}18`, color: c.goldAccent, border: `1px solid ${c.goldAccent}40`, animation: "narrativeFadeIn 400ms ease-out both" }}
          >
            ✦ Novo personagem
          </span>
        )}
        <p className="text-xs font-bold uppercase tracking-wider pl-1" style={{ color: c.goldAccent }}>
          {npc}
        </p>
        <div
          className="rounded-2xl rounded-bl-sm px-4 py-3"
          style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
        >
          <p className="text-base font-semibold italic leading-relaxed md:text-[17px]" style={{ color: c.parchment }}>
            {line}
          </p>
          {translation && (
            <p
              className="mt-2 border-t pt-2 text-[13px] leading-relaxed italic"
              style={{ color: c.textFaint, borderColor: `${c.borderFaint}` }}
            >
              <span className="not-italic mr-1 opacity-50">∿</span>
              {translation}
            </p>
          )}
          <div className="mt-2 flex items-center gap-1.5">
            <button
              type="button"
              onClick={() => audioService.speak(line, langCode, npc, pace, voice, speechRate)}
              className="flex items-center justify-center rounded-full w-7 h-7 transition active:scale-90"
              style={{ background: c.surface, color: c.textFaint }}
            >
              <Volume2 size={12} />
            </button>
            {onCycleSpeed && (
              <button
                type="button"
                onClick={onCycleSpeed}
                className="flex items-center justify-center rounded-full px-2 h-7 text-[11px] font-bold tabular-nums transition active:scale-90"
                style={{
                  background: (ttsSpeed ?? 1) > 1 ? `${c.goldAccent}22` : c.surface,
                  color:      (ttsSpeed ?? 1) > 1 ? c.goldAccent          : c.textFaint,
                  border:     `1px solid ${(ttsSpeed ?? 1) > 1 ? c.goldAccent + "40" : c.borderFaint}`,
                }}
              >
                {formatSpeedLabel(ttsSpeed ?? 1)}
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

function SituationEntry({ context, prompt, c }: { context: string; prompt: string; c: Colors }) {
  return (
    <div
      className="rounded-xl px-4 py-3 mx-1"
      style={{ background: `${c.surface}`, border: `1px solid ${c.borderFaint}` }}
    >
      <p className="mb-1 text-xs font-bold uppercase tracking-wider" style={{ color: c.textFaint }}>
        {context}
      </p>
      <p className="text-[15px] leading-relaxed md:text-base" style={{ color: c.textOnBg }}>
        {prompt}
      </p>
    </div>
  );
}

function PlayerEntry({ text, label, correct, c }: {
  text: string; label: string; correct?: boolean; c: Colors;
}) {
  const isAnswer = correct !== undefined;
  const bg     = isAnswer ? (correct ? "#16a34a22" : "#dc262622") : `${c.nodeActive}15`;
  const border = isAnswer ? (correct ? "#16a34a55" : "#dc262655") : `${c.nodeActive}35`;
  return (
    <div className="flex items-end justify-end gap-2.5">
      <div
        className="rounded-2xl rounded-br-sm px-4 py-3"
        style={{ background: bg, border: `1px solid ${border}`, maxWidth: "80%" }}
      >
        <p className="text-base italic leading-relaxed md:text-[17px]" style={{ color: c.parchment }}>{text}</p>
      </div>
      <div
        className="mb-0.5 grid h-9 w-9 shrink-0 place-items-center rounded-full text-xs font-bold"
        style={{ background: `${c.nodeActive}25`, color: c.parchment }}
      >
        {label}
      </div>
    </div>
  );
}

function WrongHintEntry({ correctText, c }: { correctText: string; c: Colors }) {
  return (
    <div
      className="rounded-xl px-3 py-2 mx-1"
      style={{ background: "#dc262610", border: "1px solid #dc262625" }}
    >
      <p className="text-sm leading-relaxed" style={{ color: "#f87171" }}>
        Forma correta: <strong>{correctText}</strong>
      </p>
    </div>
  );
}

function PatternEntry({ parts, example, translation, note, c }: {
  parts: Array<{ text: string; isKey: boolean }>; example: string; translation: string; note: string; c: Colors;
}) {
  return (
    <div
      className="rounded-2xl p-4"
      style={{ background: c.surfaceMid, border: `1px solid ${c.goldAccent}35` }}
    >
      <p className="mb-3 text-xs font-bold uppercase tracking-widest" style={{ color: c.goldAccent }}>
        ✏️  Gramática
      </p>
      <div className="mb-3 flex flex-wrap items-center gap-2">
        {parts.map((part, i) =>
          part.isKey ? (
            <span
              key={i}
              className="rounded-lg px-2.5 py-1 text-sm font-bold md:text-base"
              style={{ background: `${c.goldAccent}18`, color: c.goldAccent, border: `1px solid ${c.goldAccent}40` }}
            >
              {part.text}
            </span>
          ) : (
            <span key={i} className="text-sm font-semibold md:text-base" style={{ color: c.textFaint }}>
              {part.text}
            </span>
          )
        )}
      </div>
      <div className="mb-3 rounded-xl px-3 py-2.5" style={{ background: c.surface }}>
        <p className="text-base font-bold italic md:text-[17px]" style={{ color: c.parchment }}>{example}</p>
        <p className="mt-0.5 text-sm" style={{ color: c.textOnBg }}>{translation}</p>
      </div>
      <div className="flex items-start gap-1.5 text-sm leading-relaxed" style={{ color: c.textFaint }}>
        <Lightbulb size={14} className="mt-0.5 shrink-0" />
        <span>{note}</span>
      </div>
    </div>
  );
}

// ── Props ─────────────────────────────────────────────────────────────────────

export interface AdventureChapterSectionsProps {
  section: PhaseSection;
  sectionNumber?: number;
  totalSections?: number;
  phaseNumber: number;
  langCode: string;
  sourceLangCode: string;
  firstName?: string;
  onComplete?: (mistakes: number) => void;
  onBack: () => void;
}

// ── Component ─────────────────────────────────────────────────────────────────

export default function AdventureChapterSections({
  section,
  sectionNumber = 1,
  totalSections = 6,
  phaseNumber: _phaseNumber,
  langCode,
  sourceLangCode,
  firstName = "",
  onComplete = () => {},
  onBack,
}: AdventureChapterSectionsProps) {
  const s           = useStrings();
  const c           = getAdventureColors(langCode, "dark");
  const playerLabel = firstName
    ? firstName.charAt(0).toUpperCase()
    : (PLAYER_PRONOUN[sourceLangCode.toUpperCase()] ?? sourceLangCode);

  const allSteps = useMemo(() => normalizeSection(section), [section]);

  const sectionWords = useMemo(() => {
    for (const step of allSteps) {
      if (step.kind === "vocab_list") return step.items;
    }
    return [];
  }, [allSteps]);

  // +1 badge only fires in sections that introduce vocabulary (have a vocab_list step)
  const hasVocabList = useMemo(() => allSteps.some(s => s.kind === "vocab_list"), [allSteps]);

  const [entries,      setEntries]      = useState<ChatEntry[]>([]);
  const [cursor,       setCursor]       = useState(0);
  const [sessionId,    setSessionId]    = useState(0);
  const [phase,        setPhase]        = useState<"auto" | "tap" | "choosing" | "done" | "summary">("auto");
  const [activeChoice, setActiveChoice] = useState<ActiveChoice | null>(null);
  const [sceneCard,    setSceneCard]    = useState<string | null>(null);
  const [currentTime,  setCurrentTime]  = useState<string | null>(null);
  const [currentDay,   setCurrentDay]   = useState<string | null>(null);
  const [recapOpen,    setRecapOpen]    = useState<boolean>(false);
  const [selectedCharacter, setSelectedCharacter] = useState<SelectedCharacter | null>(null);
  const [ttsSpeed,     setTtsSpeed]     = useState(() => audioService.speedMultiplier);
  const selectedProfile = selectedCharacter ? getCharacterProfile(selectedCharacter.name) : null;

  const SPEEDS = [1, 1.25, 1.3, 1.5, 2];
  function cycleSpeed() {
    const currentIndex = SPEEDS.findIndex(speed => Math.abs(speed - ttsSpeed) < 0.001);
    const next = SPEEDS[((currentIndex >= 0 ? currentIndex : 0) + 1) % SPEEDS.length];
    audioService.setSpeed(next);
    setTtsSpeed(next);
  }

  const [floats,       setFloats]       = useState<FloatBadge[]>([]);
  const [summaryData,  setSummaryData]  = useState<{
    xp: number; correct: number; mistakes: number;
    newChars: string[];
    earnedItems: Array<{ emoji: string; name: string; rarity: string }>;
  } | null>(null);
  const [xpDisplay,    setXpDisplay]    = useState(0);

  const mistakesRef    = useRef(0);
  const correctRef     = useRef(0);
  const comboRef       = useRef(0);
  const maxComboRef    = useRef(0);
  const earnedItemsRef = useRef<Array<{ emoji: string; name: string; rarity: string }>>([]);
  const seenWordIds    = useRef<Set<string>>(new Set());
  const metNpcs        = useRef<Set<string>>(new Set());
  const bottomRef      = useRef<HTMLDivElement>(null);
  const rootRef        = useRef<HTMLDivElement>(null);
  const timerRef       = useRef<ReturnType<typeof setTimeout> | null>(null);
  const choicesFootRef = useRef<HTMLDivElement>(null);

  function addFloat(text: string, isCombo: boolean) {
    const id = `float-${Date.now()}-${Math.random()}`;
    const x  = 30 + Math.random() * 40;
    // bottomPx is relative to the component root so the badge appears just above the choices footer
    const rootBottom  = rootRef.current?.getBoundingClientRect().bottom   ?? window.innerHeight;
    const footerTop   = choicesFootRef.current?.getBoundingClientRect().top ?? (rootBottom - 220);
    const bottomPx    = (rootBottom - footerTop) + 10;
    setFloats(prev => [...prev, { id, x, bottomPx, text, isCombo }]);
    setTimeout(() => setFloats(prev => prev.filter(f => f.id !== id)), 3000);
  }

  function clearTimer() {
    if (timerRef.current) clearTimeout(timerRef.current);
  }

  const addEntry = useCallback((entry: ChatEntry) => {
    setEntries(prev => {
      if (prev.some(e => e.id === entry.id)) return prev;
      return [...prev, entry];
    });
  }, []);

  // Reset when section changes
  useEffect(() => {
    clearTimer();
    audioService.stop();
    setEntries([]);
    setCursor(0);
    setPhase("auto");
    setActiveChoice(null);
    setSceneCard(null);
    setCurrentTime(null);
    setCurrentDay(null);
    setRecapOpen(false);
    mistakesRef.current   = 0;
    correctRef.current    = 0;
    comboRef.current      = 0;
    maxComboRef.current   = 0;
    earnedItemsRef.current = [];
    seenWordIds.current   = new Set();
    metNpcs.current      = new Set();
    setFloats([]);
    setSummaryData(null);
    setXpDisplay(0);
    setSessionId(id => id + 1);
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [section]);

  // Scroll to bottom whenever content changes
  useEffect(() => {
    const t = setTimeout(() => {
      bottomRef.current?.scrollIntoView({ behavior: "smooth", block: "end" });
    }, 60);
    return () => clearTimeout(t);
  }, [entries, activeChoice]);

  // Process the step at `cursor`
  useEffect(() => {
    clearTimer();
    const step = allSteps[cursor];
    if (!step) { setPhase("done"); return; }

    const id       = `${sessionId}-${cursor}`;
    const withDelay = (ms: number, fn: () => void) => {
      timerRef.current = setTimeout(fn, ms);
    };

    switch (step.kind) {

      // ── Scene — full-screen cinematic card ───────────────────────────────
      case "scene": {
        setSceneCard(step.text);
        setPhase("tap");
        const parts = step.text.split(" · ");
        if (parts[1]) setCurrentTime(parts[1]);
        if (parts[2]) setCurrentDay(parts[2]);
        break;
      }

      // ── Auto-advance ─────────────────────────────────────────────────────
      case "player_react":
        addEntry({ id, kind: "player_text", text: step.text, label: playerLabel });
        timerRef.current = setTimeout(() => setCursor(n => n + 1), 1100);
        break;

      // ── Tap to continue ───────────────────────────────────────────────────
      case "narrative":
        addEntry({ id, kind: "narrative", text: step.text });
        setPhase("tap");
        break;

      case "npc_speak":
        withDelay(300, () => {
          addEntry({
            id,
            kind: "npc",
            npc: step.npc,
            line: step.line,
            translation: step.translation,
            isNew: step.is_new_npc,
            pace: step.pace,
            speech_rate: step.speech_rate,
            voice: step.voice,
          });
          audioService.speak(step.line, langCode, step.npc, step.pace, step.voice, step.speech_rate);
          setPhase("tap");
        });
        if (step.npc && !metNpcs.current.has(step.npc)) {
          metNpcs.current.add(step.npc);
          adventureService.meetCharacterByName(step.npc).catch(() => {});
        }
        break;

      case "pattern":
        addEntry({ id, kind: "pattern", parts: step.parts, example: step.example, translation: step.translation, note: step.note });
        setPhase("tap");
        break;

      case "reveal":
        addEntry({ id, kind: "reveal", phrase: step.phrase, meaning: step.meaning, note: step.note });
        setPhase("tap");
        break;

      case "vocab_list":
        addEntry({ id, kind: "vocab_list", items: step.items });
        setPhase("tap");
        break;

      // ── Choice ────────────────────────────────────────────────────────────
      case "multiple_choice":
        withDelay(300, () => {
          if (step.npc) {
            addEntry({ id: `${id}-q`, kind: "situation", context: step.npc, prompt: step.question });
          }
          setActiveChoice({
            question:     step.npc ? "" : step.question,
            options:      step.options,
            correct:      step.correct,
            npc:          step.npc,
            npc_reaction: step.npc_reaction,
            isGated:      section.type === "obstaculo",
            shaking:      false,
          });
          setPhase("choosing");
        });
        break;

      default:
        setPhase("tap");
    }

    return clearTimer;
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [cursor, sessionId]);

  // When done, show completion overlay briefly then advance to summary
  useEffect(() => {
    if (phase !== "done") return;
    timerRef.current = setTimeout(() => {
      const totalExercises = allSteps.filter(s =>
        s.kind === "multiple_choice" || s.kind === "fill_blank" || s.kind === "translate"
      ).length;
      const perfect  = mistakesRef.current === 0 && totalExercises > 0;
      const hasCombo = maxComboRef.current >= 3;
      const xpEarned = 10
        + correctRef.current   * 2
        + (perfect  ? 10 : 0)
        + (hasCombo ?  5 : 0);
      setSummaryData({
        xp:          xpEarned,
        correct:     correctRef.current,
        mistakes:    mistakesRef.current,
        newChars:    Array.from(metNpcs.current),
        earnedItems: [...earnedItemsRef.current],
      });
      setPhase("summary");
    }, 1800);
    return clearTimer;
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [phase]);

  useEffect(() => {
    if (phase === "done") audioService.playComplete();
  }, [phase]);

  // Count-up animation for XP on summary screen
  useEffect(() => {
    if (!summaryData) return;
    const target = summaryData.xp;
    let start: number | null = null;
    let raf: number;
    const step = (ts: number) => {
      if (!start) start = ts;
      const pct = Math.min((ts - start) / 800, 1);
      setXpDisplay(Math.floor(pct * target));
      if (pct < 1) raf = requestAnimationFrame(step);
    };
    raf = requestAnimationFrame(step);
    return () => cancelAnimationFrame(raf);
  }, [summaryData]);

  function handleTap() {
    if (phase !== "tap") return;
    audioService.stop();
    setSceneCard(null);
    setPhase("auto");
    setCursor(n => n + 1);
  }

  function handleChoice(chosenId: string) {
    if (!activeChoice || activeChoice.shaking) return;
    const { correct, options, npc, npc_reaction, isGated } = activeChoice;
    const isCorrect   = chosenId === correct;
    const chosenText  = options.find(o => o.id === chosenId)?.text ?? chosenId;
    const correctText = options.find(o => o.id === correct)?.text ?? correct;
    const id          = `${sessionId}-${cursor}`;

    const currentStep = allSteps[cursor];
    const wordId      = currentStep?.kind === "multiple_choice" ? currentStep.word_id : undefined;
    const wordTarget  = currentStep?.kind === "multiple_choice" ? currentStep.target  : undefined;
    const wordNative  = currentStep?.kind === "multiple_choice" ? currentStep.native  : undefined;
    // New word = section introduces vocab (has vocab_list) AND this word_id hasn't been answered correctly yet
    const isNewWord   = hasVocabList && Boolean(wordId) && !seenWordIds.current.has(wordId!);

    if (wordId) {
      adventureService.recordWordAnswer({
        word_id:   wordId,
        correct:   isCorrect,
        target:    wordTarget,
        native:    wordNative,
        lang_code: langCode.toLowerCase(),
      }).then(res => {
        if (res.earned_item) {
          addFloat(res.earned_item.name, false);
          earnedItemsRef.current = [
            ...earnedItemsRef.current.filter(i => i.name !== res.earned_item!.name),
            { emoji: res.earned_item.emoji, name: res.earned_item.name, rarity: res.earned_item.rarity },
          ];
        }
      }).catch(() => {});
    }

    if (isCorrect) {
      correctRef.current += 1;
      if (wordId) seenWordIds.current.add(wordId);
      if (isNewWord) {
        comboRef.current += 1;
        if (comboRef.current > maxComboRef.current) maxComboRef.current = comboRef.current;
        const n = comboRef.current;
        if (n >= 3) addFloat(s.adventure.comboLabel(n), true);
        else        addFloat(s.adventure.plusOne, false);
      }
    } else {
      comboRef.current = 0;
    }

    if (!isCorrect && isGated) {
      mistakesRef.current++;
      audioService.playWrong();
      setActiveChoice(prev => prev ? { ...prev, shaking: true } : null);
      timerRef.current = setTimeout(() => {
        setActiveChoice(prev => prev ? { ...prev, shaking: false } : null);
      }, 550);
      return;
    }

    if (!isCorrect) mistakesRef.current++;

    addEntry({ id: `${id}-ans`, kind: "player_answer", text: chosenText, label: playerLabel, correct: isCorrect });
    setActiveChoice(null);

    if (!isCorrect) {
      audioService.playWrong();
      addEntry({ id: `${id}-hint`, kind: "wrong_hint", correctText });
      timerRef.current = setTimeout(() => setCursor(n => n + 1), 1600);
      return;
    }

    audioService.playCorrect();

    if (npc_reaction && npc) {
      timerRef.current = setTimeout(() => {
        addEntry({ id: `${id}-react`, kind: "npc_reaction", npc, line: npc_reaction });
        timerRef.current = setTimeout(() => setCursor(n => n + 1), 1100);
      }, 400);
    } else {
      timerRef.current = setTimeout(() => setCursor(n => n + 1), 700);
    }
  }

  return (
    <div ref={rootRef} className="relative flex h-full flex-col">

      {/* Floating +1 / combo badges */}
      {floats.length > 0 && (
        <div className="pointer-events-none absolute inset-0 z-20 overflow-hidden">
          {floats.map(badge => (
            <span
              key={badge.id}
              className="absolute font-black"
              style={{
                left:       `${badge.x}%`,
                bottom:     `${badge.bottomPx}px`,
                fontSize:   badge.isCombo ? "1.4rem" : "1.1rem",
                color:      badge.isCombo ? c.goldAccent : "#4ade80",
                textShadow: badge.isCombo
                  ? `0 0 16px ${c.goldAccent}90`
                  : "0 0 12px #4ade8090",
                animation:  "floatUpFade 3s cubic-bezier(0.16,1,0.3,1) both",
              }}
            >
              {badge.text}
            </span>
          ))}
        </div>
      )}

      {/* Recap card — opened by the "Me relembre" header button */}
      {recapOpen && section.recap && (
        <RecapCard
          recap={section.recap}
          c={c}
          langCode={langCode}
          onCharacterOpen={setSelectedCharacter}
          onClose={() => setRecapOpen(false)}
          labels={{
            eyebrow: s.adventure.recapEyebrow,
            now:     s.adventure.recapNowLabel,
            close:   s.adventure.recapClose,
          }}
        />
      )}

      {/* Scene full-screen card */}
      {sceneCard && (
        <SceneCard text={sceneCard} c={c} onTap={handleTap} />
      )}

      {/* Section complete overlay */}
      {phase === "done" && (
        <SectionCompleteOverlay sectionNumber={sectionNumber} totalSections={totalSections} c={c} />
      )}

      {/* Section summary */}
      {phase === "summary" && summaryData && (
        <div
          className="absolute inset-0 z-30 flex flex-col"
          style={{ background: "rgba(0,0,0,0.97)", animation: "narrativeFadeIn 400ms ease-out both" }}
        >
          <div className="flex flex-1 flex-col items-center gap-5 overflow-y-auto px-5 pb-4 pt-12">

            {/* Check icon */}
            <div
              className="grid h-14 w-14 place-items-center rounded-full"
              style={{ background: `${c.goldAccent}15`, border: `1.5px solid ${c.goldAccent}55`, animation: "successPop 500ms ease-out both" }}
            >
              <Check size={22} style={{ color: c.goldAccent }} />
            </div>

            {/* Title */}
            <div className="text-center" style={{ animation: "narrativeFadeIn 450ms 200ms ease-out both" }}>
              <p className="text-xs font-bold uppercase tracking-widest" style={{ color: c.goldAccent }}>
                {s.adventure.sectionLabel(sectionNumber, totalSections)}
              </p>
              <p className="mt-1 text-2xl font-bold" style={{ color: c.parchment }}>Concluída</p>
            </div>

            {/* XP earned */}
            <div
              className="flex flex-col items-center gap-1"
              style={{ animation: "narrativeFadeIn 450ms 350ms ease-out both" }}
            >
              <span
                className="text-5xl font-black tabular-nums leading-none"
                style={{
                  color:      c.goldAccent,
                  textShadow: `0 0 28px ${c.goldAccent}70`,
                  animation:  "successPop 0.5s cubic-bezier(0.16,1,0.3,1) 0.45s both",
                }}
              >
                +{xpDisplay} XP
              </span>
              <div className="mt-1 flex flex-col items-center gap-0.5">
                {summaryData.mistakes === 0 && summaryData.correct > 0 && (
                  <span className="inline-flex items-center gap-1 text-xs font-bold" style={{ color: "#4ade80", animation: "narrativeFadeIn 400ms 750ms ease-out both" }}>
                    <Sparkles size={12} />
                    Sem erros! +10 bônus
                  </span>
                )}
                {maxComboRef.current >= 3 && (
                  <span className="inline-flex items-center gap-1 text-xs font-bold" style={{ color: c.goldAccent, animation: "narrativeFadeIn 400ms 800ms ease-out both" }}>
                    <Flame size={12} />
                    Combo ×{maxComboRef.current}! +5 bônus
                  </span>
                )}
              </div>
            </div>

            {/* Score row */}
            {summaryData.correct + summaryData.mistakes > 0 && (
              <div className="flex w-full gap-3" style={{ animation: "narrativeFadeIn 450ms 500ms ease-out both" }}>
                <div
                  className="flex flex-1 flex-col items-center gap-1 rounded-xl py-3"
                  style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
                >
                  <span className="text-xl font-bold tabular-nums" style={{ color: "#4ade80" }}>{summaryData.correct}</span>
                  <span className="text-[10px] uppercase tracking-wide" style={{ color: c.textFaint }}>acertos</span>
                </div>
                <div
                  className="flex flex-1 flex-col items-center gap-1 rounded-xl py-3"
                  style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
                >
                  <span
                    className="text-xl font-bold tabular-nums"
                    style={{ color: summaryData.mistakes > 0 ? "#f87171" : c.textFaint }}
                  >
                    {summaryData.mistakes}
                  </span>
                  <span className="text-[10px] uppercase tracking-wide" style={{ color: c.textFaint }}>erros</span>
                </div>
              </div>
            )}

            {/* Earned items */}
            {summaryData.earnedItems.length > 0 && (
              <div className="w-full" style={{ animation: "narrativeFadeIn 450ms 560ms ease-out both" }}>
                <p className="mb-3 text-xs font-bold uppercase tracking-wider" style={{ color: c.textFaint }}>
                  Itens encontrados
                </p>
                <div className="flex flex-col gap-2">
                  {summaryData.earnedItems.map((item, i) => (
                    <div
                      key={item.name}
                      className="flex items-center gap-3 rounded-xl px-4 py-3"
                      style={{
                        background: c.surfaceMid,
                        border: `1px solid ${c.goldAccent}30`,
                        animation: `successPop 0.4s cubic-bezier(0.16,1,0.3,1) ${i * 0.1}s both`,
                      }}
                    >
                      <Emoji char={item.emoji} size={28} style={{ flexShrink: 0 }} />
                      <div className="min-w-0 flex-1">
                        <p className="text-sm font-bold" style={{ color: c.parchment }}>{item.name}</p>
                        <p className="text-[10px] font-semibold uppercase tracking-wide" style={{ color: c.goldAccent }}>{item.rarity}</p>
                      </div>
                      <span
                        className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full text-[10px] font-black"
                        style={{ background: c.goldAccent, color: "#1a0800" }}
                      >
                        +1
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* New characters */}
            {summaryData.newChars.length > 0 && (
              <div className="w-full" style={{ animation: "narrativeFadeIn 450ms 580ms ease-out both" }}>
                <p className="mb-3 text-xs font-bold uppercase tracking-wider" style={{ color: c.textFaint }}>
                  Personagens encontrados
                </p>
                <div className="flex gap-4 overflow-x-auto pb-1">
                  {summaryData.newChars.map((name, i) => {
                    const avatar = CHARACTER_AVATARS[name];
                    const shortName = name.split(" ")[0];
                    return (
                      <div
                        key={name}
                        className="flex flex-col items-center gap-2 shrink-0"
                        style={{ animation: `successPop 0.4s cubic-bezier(0.16,1,0.3,1) ${i * 0.1}s both` }}
                      >
                        <button
                          type="button"
                          className="relative"
                          onClick={() => setSelectedCharacter({ name, slug: avatar?.slug, emoji: avatar?.emoji })}
                          style={{
                            borderRadius: "50%",
                            border: `2px solid ${c.goldAccent}60`,
                            boxShadow: `0 0 16px ${c.goldAccent}30`,
                          }}
                        >
                          <CharacterAvatar
                            slug={avatar?.slug}
                            emoji={avatar?.emoji ?? ""}
                            name={name}
                            langCode={langCode}
                            size={60}
                            fallbackBg={`${c.goldAccent}18`}
                          />
                          <span
                            className="absolute -top-1 -right-1 flex h-5 w-5 items-center justify-center rounded-full text-[8px] font-black"
                            style={{ background: c.goldAccent, color: "#1a0800" }}
                          >
                            ✦
                          </span>
                        </button>
                        <span className="text-xs font-bold" style={{ color: c.parchment }}>{shortName}</span>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* Words earned */}
            {sectionWords.length > 0 && (
              <div className="w-full" style={{ animation: "narrativeFadeIn 450ms 640ms ease-out both" }}>
                <p className="mb-3 text-xs font-bold uppercase tracking-wider" style={{ color: c.textFaint }}>
                  Palavras desbloqueadas
                </p>
                <div className="flex flex-col gap-2">
                  {sectionWords.map(({ target, native }, i) => (
                    <div
                      key={target}
                      className="flex items-center gap-3 rounded-xl px-4 py-3"
                      style={{
                        background: c.surfaceMid,
                        border: `1px solid ${c.borderFaint}`,
                        animation: `narrativeFadeIn 0.35s ease-out ${0.65 + i * 0.07}s both`,
                      }}
                    >
                      <span
                        className="flex h-7 w-7 shrink-0 items-center justify-center rounded-lg text-[10px] font-black"
                        style={{ background: `${c.nodeActive}22`, color: c.nodeActive, border: `1px solid ${c.nodeActive}40` }}
                      >
                        +1
                      </span>
                      <span className="flex-1 text-sm font-bold italic" style={{ color: c.parchment }}>{target}</span>
                      <span className="text-right text-xs font-medium" style={{ color: c.textOnBg }}>{native}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          <div className="shrink-0 px-4 pb-6 pt-2">
            <button
              type="button"
              onClick={() => onComplete(mistakesRef.current)}
              className="w-full rounded-2xl py-4 text-base font-bold transition active:scale-[0.97]"
              style={{ background: c.goldAccent, color: "#1a0800" }}
            >
              {s.adventure.continueBtn}
            </button>
          </div>
        </div>
      )}

      {/* Header */}
      <header className="relative shrink-0 flex items-center justify-between px-4 pb-3 pt-3">
        <button
          type="button"
          onClick={onBack}
          className="flex items-center justify-center rounded-full w-9 h-9"
          style={{ background: c.surface, color: c.parchment }}
        >
          <ChevronLeft size={16} />
        </button>

        {currentTime && (
          <div
            className="absolute left-1/2 -translate-x-1/2 flex items-center gap-1.5 rounded-full px-3 py-1.5"
            style={{ background: c.surfaceMid }}
          >
            {/noite|anoitecer/i.test(currentTime)
              ? <Moon   size={11} style={{ color: c.goldAccent }} />
              : /tarde|final/i.test(currentTime)
              ? <Sunset size={11} style={{ color: c.goldAccent }} />
              : <Sun    size={11} style={{ color: c.goldAccent }} />}
            <span className="text-xs font-semibold" style={{ color: c.textOnBg }}>
              {currentDay ? `${currentDay} · ${currentTime}` : currentTime}
            </span>
          </div>
        )}

        <div className="flex items-center gap-2">
          {section.recap && (
            <button
              type="button"
              onClick={() => setRecapOpen(true)}
              className="flex items-center gap-1.5 rounded-full px-3 py-1.5 text-xs font-semibold"
              style={{ background: c.surfaceMid, color: c.parchment, border: `1px solid ${c.borderFaint}` }}
            >
              <History size={12} style={{ color: c.goldAccent }} />
              {s.adventure.recapButton}
            </button>
          )}
          <p className="text-xs font-bold tabular-nums" style={{ color: c.textFaint }}>
            S{sectionNumber}/{totalSections}
          </p>
        </div>
      </header>

      {/* Chat scroll */}
      <div className="adventure-scroll flex-1 overflow-y-auto px-4">
        <div className="flex flex-col gap-5 pb-4 pt-1">

          {entries.map((entry) => (
            <div
              key={entry.id}
              style={{ animation: "narrativeFadeIn 350ms ease-out both" }}
            >
              {entry.kind === "narrative" && (
                <NarrativeEntry text={entry.text} c={c} />
              )}
              {entry.kind === "npc" && (
                <NpcEntry npc={entry.npc} line={entry.line} translation={entry.translation} isNew={entry.isNew} langCode={langCode} pace={entry.pace} speechRate={entry.speech_rate} voice={entry.voice} ttsSpeed={ttsSpeed} onCycleSpeed={cycleSpeed} onCharacterOpen={setSelectedCharacter} c={c} />
              )}
              {entry.kind === "npc_reaction" && (
                <NpcEntry npc={entry.npc} line={entry.line} langCode={langCode} onCharacterOpen={setSelectedCharacter} c={c} />
              )}
              {entry.kind === "situation" && (
                <SituationEntry context={entry.context} prompt={entry.prompt} c={c} />
              )}
              {entry.kind === "player_text" && (
                <PlayerEntry text={entry.text} label={entry.label} c={c} />
              )}
              {entry.kind === "player_answer" && (
                <PlayerEntry text={entry.text} label={entry.label} correct={entry.correct} c={c} />
              )}
              {entry.kind === "wrong_hint" && (
                <WrongHintEntry correctText={entry.correctText} c={c} />
              )}
              {entry.kind === "pattern" && (
                <PatternEntry
                  parts={entry.parts}
                  example={entry.example}
                  translation={entry.translation}
                  note={entry.note}
                  c={c}
                />
              )}
              {entry.kind === "reveal" && (
                <div
                  className="flex flex-col items-center gap-2 rounded-2xl px-6 py-8 text-center"
                  style={{ background: `${c.goldAccent}15`, border: `1px solid ${c.goldAccent}40` }}
                >
                  <p className="text-3xl font-bold italic md:text-4xl" style={{ color: c.parchment }}>{entry.phrase}</p>
                  <button
                    type="button"
                    onClick={() => audioService.speak(entry.phrase, langCode)}
                    className="flex items-center justify-center rounded-full w-8 h-8 transition active:scale-90"
                    style={{ background: `${c.goldAccent}20`, color: c.goldAccent }}
                  >
                    <Volume2 size={14} />
                  </button>
                  <p className="text-lg font-semibold md:text-xl" style={{ color: c.goldAccent }}>{entry.meaning}</p>
                  {entry.note && (
                    <p className="mt-1 text-sm" style={{ color: c.textFaint }}>💡 {entry.note}</p>
                  )}
                </div>
              )}
              {entry.kind === "vocab_list" && (
                <div className="flex flex-col gap-2">
                  {entry.items.map(({ target, native }) => (
                    <div
                      key={target}
                      className="flex items-center gap-3 rounded-xl px-4 py-3"
                      style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
                    >
                      <button
                        type="button"
                        onClick={() => audioService.speak(target, langCode)}
                        className="flex items-center justify-center rounded-full w-7 h-7 shrink-0 transition active:scale-90"
                        style={{ background: c.surface, color: c.textFaint }}
                      >
                        <Volume2 size={12} />
                      </button>
                      <span className="flex-1 text-base font-bold italic md:text-[17px]" style={{ color: c.parchment }}>{target}</span>
                      <span className="text-sm font-medium md:text-base" style={{ color: c.textOnBg }}>{native}</span>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))}

          <div ref={bottomRef} />
        </div>
      </div>

      {/* Footer — fixed Continuar (hidden during choices / scene / done / summary) */}
      {!sceneCard && phase !== "choosing" && phase !== "done" && phase !== "summary" && (
        <div className="shrink-0 px-4 pb-6 pt-2">
          <button
            type="button"
            onClick={phase === "tap" ? handleTap : undefined}
            disabled={phase !== "tap"}
            className="w-full rounded-2xl py-4 text-base font-bold transition active:scale-[0.97] md:text-lg"
            style={{
              background: phase === "tap" ? c.goldAccent : `${c.goldAccent}30`,
              color:      phase === "tap" ? "#1a0800"    : `${c.goldAccent}70`,
              cursor:     phase === "tap" ? "pointer"    : "default",
            }}
          >
            Continuar
          </button>
        </div>
      )}

      {phase === "choosing" && activeChoice && (
        <div
          ref={choicesFootRef}
          className="shrink-0 px-4 pb-6 pt-3"
          style={{
            borderTop: `1px solid ${c.borderFaint}`,
            background: `linear-gradient(to bottom, rgba(0,0,0,0.2), rgba(0,0,0,0.5))`,
          }}
        >
          {activeChoice.question && (
            <p className="mb-3 px-1 text-[15px] leading-snug md:text-base" style={{ color: c.textOnBg }}>
              {activeChoice.question}
            </p>
          )}
          <div
            className="flex flex-col gap-2"
            style={activeChoice.shaking ? { animation: "shake 500ms ease-out both" } : undefined}
          >
            {activeChoice.options.map(({ id, text }) => (
              <button
                key={id}
                type="button"
                onClick={() => handleChoice(id)}
                className="w-full rounded-xl px-4 py-3.5 text-left text-[15px] font-semibold transition active:scale-[0.97] md:text-base"
                style={{
                  background: c.surfaceMid,
                  border: `1px solid ${c.borderFaint}`,
                  color: c.textOnBg,
                }}
              >
                {text}
              </button>
            ))}
          </div>
        </div>
      )}

      <CharacterProfileModal
        open={Boolean(selectedCharacter)}
        character={selectedProfile}
        slug={selectedCharacter?.slug}
        emoji={selectedCharacter?.emoji}
        langCode={langCode}
        closeLabel={s.adventure.recapClose}
        c={c}
        onClose={() => setSelectedCharacter(null)}
      />

    </div>
  );
}

