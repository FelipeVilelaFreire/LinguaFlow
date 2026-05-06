import { useEffect, useMemo, useState } from "react";
import { CheckCircle2, ChevronLeft, Lock, Send, Shield, Skull, Star, Swords, Trophy, X } from "lucide-react";

import LessonCard from "../components/learning/LessonCard";
import ProgressBar from "../components/ui/ProgressBar";
import StateMessage from "../components/ui/StateMessage";
import { adventureService } from "../services/adventureService";
import type { AdventureChapter, AdventurePhase } from "../types/adventure";
import type { Phrase, PracticeItem } from "../types/content";

type ChapterView = "loading" | "map" | "narrative" | "exercise" | "phase-complete" | "chapter-complete";

const NODE_POS = [
  { x: 18, y: 5 },
  { x: 55, y: 13 },
  { x: 80, y: 23 },
  { x: 62, y: 34 },
  { x: 24, y: 43 },
  { x: 12, y: 53 },
  { x: 46, y: 62 },
  { x: 75, y: 71 },
  { x: 48, y: 81 },
  { x: 48, y: 91 },
];

function toItems(phrases: Phrase[]): PracticeItem[] {
  return phrases.map((p, i) => ({
    id: `adv-${p.id}-${i}`,
    type: "new" as const,
    prompt: p.target_text,
    answer: p.source_text,
    helper: "Tradução",
    options: [],
    word_bank: [],
    preview_phrases: [],
    phrase: p,
  }));
}

function normalize(s: string) {
  return s.trim().toLowerCase().replace(/[.,!?¿¡]/g, "").replace(/\s+/g, " ");
}

function getFeedback(answer: string, item: PracticeItem | null) {
  if (!item || !answer.trim()) {
    return { quality: "wrong" as const, missingWords: [] as string[], expected: item?.answer ?? "" };
  }
  const na = normalize(answer);
  const nt = normalize(item.answer);
  if (na === nt || nt.includes(na) || na.includes(nt)) {
    return { quality: "correct" as const, missingWords: [], expected: item.answer };
  }
  const aWords = new Set(na.split(" ").filter(Boolean));
  const tWords = nt.split(" ").filter(Boolean);
  const missing = tWords.filter((w) => !aWords.has(w));
  const ratio = tWords.length ? (tWords.length - missing.length) / tWords.length : 0;
  return {
    quality: ratio >= 0.55 ? ("close" as const) : ("wrong" as const),
    missingWords: missing.slice(0, 5),
    expected: item.answer,
  };
}

interface AdventureChapterScreenProps {
  chapterId: number;
  onBack: () => void;
}

export default function AdventureChapterScreen({ chapterId, onBack }: AdventureChapterScreenProps) {
  const [view, setView] = useState<ChapterView>("loading");
  const [chapter, setChapter] = useState<AdventureChapter | null>(() => {
    const s = window.history.state?.chapter as AdventureChapter | undefined;
    return s && s.id === chapterId ? s : null;
  });
  const [selectedPhase, setSelectedPhase] = useState<AdventurePhase | null>(null);
  const [activePhase, setActivePhase] = useState<AdventurePhase | null>(null);
  const [phrases, setPhrases] = useState<Phrase[]>([]);
  const [phraseIndex, setPhraseIndex] = useState(0);
  const [answer, setAnswer] = useState("");
  const [checked, setChecked] = useState(false);
  const [showTranslation, setShowTranslation] = useState(false);
  const [score, setScore] = useState(0);
  const [phaseResult, setPhaseResult] = useState<{ chapter_completed: boolean; reward_unlocked: boolean } | null>(null);

  useEffect(() => {
    if (chapter) {
      setView("map");
      return;
    }
    adventureService.listChapters().then((chapters) => {
      const found = chapters.find((c) => c.id === chapterId) ?? null;
      setChapter(found);
      setView(found ? "map" : "loading");
    }).catch(() => setView("loading"));
  }, []);

  async function reloadChapter() {
    const chapters = await adventureService.listChapters();
    const updated = chapters.find((c) => c.id === chapterId);
    if (updated) setChapter(updated);
  }

  const currentPhaseNumber = chapter?.progress?.current_phase ?? 1;
  const items = useMemo(() => toItems(phrases), [phrases]);
  const currentItem = items[phraseIndex] ?? null;
  const currentPhrase = currentItem?.phrase ?? null;
  const feedback = useMemo(() => getFeedback(answer, currentItem), [answer, currentItem]);
  const progress = items.length === 0 ? 0 : Math.round((phraseIndex / items.length) * 100);

  async function openPhase(phase: AdventurePhase) {
    setSelectedPhase(null);
    setActivePhase(phase);
    setPhraseIndex(0);
    setAnswer("");
    setChecked(false);
    setScore(0);
    setPhaseResult(null);
    try {
      const loaded = await adventureService.getPhrasesForPhase(phase.id);
      setPhrases(loaded);
    } catch {
      setPhrases([]);
    }
    setView("narrative");
  }

  async function nextPhrase() {
    const earned = checked && feedback.quality !== "wrong";
    const newScore = earned ? score + 1 : score;
    setScore(newScore);

    if (phraseIndex >= items.length - 1) {
      if (activePhase) {
        try {
          const res = await adventureService.completePhase(activePhase.id, newScore);
          setPhaseResult({ chapter_completed: res.chapter_completed, reward_unlocked: res.reward_unlocked });
          await reloadChapter();
          if (res.chapter_completed) {
            setView("chapter-complete");
            return;
          }
        } catch {
          setPhaseResult({ chapter_completed: false, reward_unlocked: false });
        }
      }
      setView("phase-complete");
      return;
    }

    setPhraseIndex((i) => i + 1);
    setAnswer("");
    setChecked(false);
    setShowTranslation(false);
  }

  // ── Loading ──────────────────────────────────────────────────────────────
  if (view === "loading" || !chapter) {
    return (
      <div className="min-h-dvh" style={{ background: "#0a0200" }}>
        <BackButton onBack={onBack} />
        <div className="grid min-h-dvh place-items-center">
          <StateMessage />
        </div>
      </div>
    );
  }

  // ── Map ──────────────────────────────────────────────────────────────────
  if (view === "map") {
    const completedCount = chapter.phases.filter((p) => p.is_completed).length;

    return (
      <div
        className="relative min-h-dvh overflow-hidden"
        style={{
          background: "linear-gradient(180deg, #0a0200 0%, #1a0800 35%, #0f0400 65%, #1a0a00 100%)",
          animation: "immersiveReveal 350ms ease-out both",
        }}
      >
        {/* Atmospheric glows */}
        <div className="pointer-events-none absolute inset-0">
          <div
            className="absolute"
            style={{
              top: "12%", left: "25%", width: 240, height: 240,
              background: "radial-gradient(circle, rgba(217,119,6,0.07), transparent 70%)",
              borderRadius: "50%",
            }}
          />
          <div
            className="absolute"
            style={{
              top: "58%", right: "10%", width: 180, height: 180,
              background: "radial-gradient(circle, rgba(217,119,6,0.05), transparent 70%)",
              borderRadius: "50%",
            }}
          />
        </div>

        {/* Connecting path */}
        <svg
          className="absolute inset-0"
          viewBox="0 0 100 100"
          preserveAspectRatio="none"
          style={{ width: "100%", height: "100%", pointerEvents: "none" }}
        >
          <polyline
            points="18,5 55,13 80,23 62,34 24,43 12,53 46,62 75,71 48,81 48,91"
            fill="none"
            stroke="#d97706"
            strokeWidth="0.65"
            strokeDasharray="3,2.5"
            opacity="0.3"
          />
        </svg>

        {/* Phase nodes */}
        {chapter.phases.map((phase, i) => {
          const pos = NODE_POS[i] ?? { x: 50, y: 50 };
          const isCompleted = phase.is_completed;
          const isCurrent = phase.number === currentPhaseNumber && !phase.is_completed;
          const isLocked = !isCompleted && !isCurrent;
          const isBoss = phase.is_boss;

          let bg = "#1f2937";
          if (isCompleted) bg = "#059669";
          else if (isCurrent && isBoss) bg = "#991b1b";
          else if (isCurrent) bg = "#d97706";
          else if (!isCurrent && isBoss) bg = "#3b1212";

          const size = isBoss ? 62 : 54;

          return (
            <button
              key={phase.id}
              type="button"
              disabled={isLocked}
              onClick={() => !isLocked && setSelectedPhase(phase)}
              className={`absolute flex items-center justify-center rounded-full font-bold text-white transition ${
                isLocked ? "cursor-not-allowed opacity-50" : "cursor-pointer hover:brightness-110 active:scale-95"
              }`}
              style={{
                left: `${pos.x}%`,
                top: `${pos.y}%`,
                transform: "translate(-50%, -50%)",
                width: size,
                height: size,
                background: bg,
                boxShadow: isCurrent
                  ? `0 0 0 3px ${isBoss ? "#ef4444" : "#f59e0b"}, 0 0 24px ${isBoss ? "rgba(239,68,68,0.45)" : "rgba(245,158,11,0.45)"}`
                  : isCompleted
                    ? "0 0 0 2px #059669, 0 4px 12px rgba(0,0,0,0.5)"
                    : "0 4px 14px rgba(0,0,0,0.55)",
                animation: isCurrent ? "adventureBounce 1.4s ease-in-out infinite" : undefined,
                zIndex: isCurrent ? 2 : 1,
              }}
              title={isLocked ? "Fase bloqueada" : phase.title}
            >
              {isCompleted ? (
                <CheckCircle2 size={isBoss ? 23 : 20} />
              ) : isLocked ? (
                <Lock size={isBoss ? 21 : 17} />
              ) : isBoss ? (
                <Skull size={22} />
              ) : (
                <span className="text-[15px] font-bold">{phase.number}</span>
              )}
            </button>
          );
        })}

        {/* Header */}
        <div className="pointer-events-none absolute inset-x-0 top-0 px-4 pt-4">
          <div className="flex items-start justify-between">
            <div className="ml-24">
              <p className="text-[9px] font-bold uppercase tracking-widest text-amber-400">{chapter.level}</p>
              <h2 className="text-sm font-semibold leading-tight text-white">{chapter.title}</h2>
            </div>
            <div className="rounded-[8px] bg-black/50 px-3 py-2 text-right backdrop-blur-sm">
              <p className="text-[9px] font-bold uppercase text-amber-400">Progresso</p>
              <p className="text-sm font-semibold text-white">
                {completedCount}
                <span className="text-amber-400/60">/{chapter.phases.length}</span>
              </p>
            </div>
          </div>
        </div>

        <BackButton onBack={onBack} />

        {/* Phase bottom sheet */}
        {selectedPhase ? (
          <div
            className="fixed inset-0 z-40 flex items-end"
            style={{ background: "rgba(0,0,0,0.65)" }}
            onClick={() => setSelectedPhase(null)}
          >
            <div
              className="w-full rounded-t-2xl bg-slate-900 p-5 pb-safe-bottom md:pb-8"
              style={{ animation: "sheetSlideUp 220ms ease-out both", maxHeight: "80vh", overflowY: "auto" }}
              onClick={(e) => e.stopPropagation()}
            >
              <div className="mb-4 flex items-start justify-between gap-4">
                <div>
                  <p className={`text-xs font-bold uppercase tracking-wide ${selectedPhase.is_boss ? "text-red-400" : "text-amber-400"}`}>
                    {selectedPhase.is_boss ? "⚔️ Fase Boss" : `Fase ${selectedPhase.number}`}
                  </p>
                  <h3 className="mt-1 text-xl font-semibold text-white">{selectedPhase.title}</h3>
                </div>
                <button
                  type="button"
                  onClick={() => setSelectedPhase(null)}
                  className="grid h-9 w-9 shrink-0 place-items-center rounded-full bg-white/10 text-white transition hover:bg-white/20"
                >
                  <X size={17} />
                </button>
              </div>

              <p className="text-sm font-medium leading-6 text-slate-300">{selectedPhase.narrative_intro}</p>

              {selectedPhase.key_words?.length ? (
                <div className="mt-4 flex flex-wrap gap-2">
                  {selectedPhase.key_words.map((kw) => (
                    <span key={kw} className="rounded-full bg-amber-900/40 px-3 py-1 text-xs font-semibold text-amber-300 ring-1 ring-amber-900/60">
                      {kw}
                    </span>
                  ))}
                </div>
              ) : null}

              <div className="mt-4 flex items-center gap-3 text-xs font-semibold text-slate-500">
                <span>{selectedPhase.phrase_count} frases</span>
                {selectedPhase.is_completed && selectedPhase.score !== null ? (
                  <span className="text-emerald-400">· Concluída · {selectedPhase.score} pts</span>
                ) : selectedPhase.is_completed ? (
                  <span className="text-emerald-400">· Concluída</span>
                ) : null}
              </div>

              <button
                type="button"
                onClick={() => openPhase(selectedPhase)}
                className="mt-5 flex w-full items-center justify-center gap-2 rounded-[8px] px-5 py-4 text-base font-semibold text-white transition active:scale-[0.98]"
                style={{ background: selectedPhase.is_completed ? "#334155" : selectedPhase.is_boss ? "#991b1b" : "#d97706" }}
              >
                {selectedPhase.is_completed ? (
                  <><Star size={18} /> Jogar novamente</>
                ) : selectedPhase.is_boss ? (
                  <><Skull size={18} /> Enfrentar o Chefe</>
                ) : (
                  <><Swords size={18} /> Iniciar Fase</>
                )}
              </button>
            </div>
          </div>
        ) : null}
      </div>
    );
  }

  // ── Narrative ────────────────────────────────────────────────────────────
  if (view === "narrative" && activePhase) {
    return (
      <div
        className="relative min-h-dvh overflow-hidden flex flex-col justify-end p-6 pb-12 md:p-10"
        style={{ background: "linear-gradient(180deg, #0a0200 0%, #1a0800 100%)" }}
      >
        <div
          className="pointer-events-none absolute inset-0"
          style={{ background: "radial-gradient(ellipse at 50% 35%, rgba(217,119,6,0.1), transparent 65%)" }}
        />
        <BackButton onBack={() => setView("map")} label="Mapa" />
        <div className="relative z-10">
          <p className={`text-[10px] font-bold uppercase tracking-widest ${activePhase.is_boss ? "text-red-400" : "text-amber-400"}`}>
            {activePhase.is_boss ? "BOSS FINAL" : `Fase ${activePhase.number}`}
          </p>
          <h2 className="mt-2 text-3xl font-semibold leading-tight text-white md:text-4xl">{activePhase.title}</h2>

          <div className="mt-6 rounded-[8px] border border-amber-900/35 bg-amber-950/25 p-5">
            <p
              className="text-base font-medium leading-7 text-amber-100/85"
              style={{ animation: "narrativeFadeIn 700ms ease-out both" }}
            >
              {activePhase.narrative_intro}
            </p>
          </div>

          {activePhase.key_words?.length ? (
            <div className="mt-4 flex flex-wrap gap-2">
              {activePhase.key_words.map((kw) => (
                <span key={kw} className="rounded-full bg-amber-900/30 px-3 py-1 text-xs font-bold text-amber-300">
                  {kw}
                </span>
              ))}
            </div>
          ) : null}

          <button
            type="button"
            onClick={() => setView("exercise")}
            className="mt-8 flex w-full items-center justify-center gap-2 rounded-[8px] px-6 py-4 text-base font-semibold text-white shadow-lg transition hover:brightness-110 active:scale-[0.98]"
            style={{ background: activePhase.is_boss ? "#991b1b" : "#d97706" }}
          >
            <Swords size={18} />
            {activePhase.is_boss ? "Enfrentar o Chefe" : "Entrar na Batalha"}
          </button>
        </div>
      </div>
    );
  }

  // ── Exercise ─────────────────────────────────────────────────────────────
  if (view === "exercise" && activePhase) {
    if (!items.length) {
      return (
        <div className="min-h-dvh" style={{ background: "#0a0200" }}>
          <BackButton onBack={() => setView("map")} label="Mapa" />
          <div className="grid min-h-dvh place-items-center">
            <StateMessage title="Sem frases nesta fase" detail="As frases ainda não foram carregadas. Tente novamente." />
          </div>
        </div>
      );
    }

    return (
      <div className="min-h-dvh bg-slate-50 px-3 pt-4 pb-8">
        <header className="mb-4 flex items-center gap-3">
          <button
            type="button"
            onClick={() => setView("map")}
            className="flex items-center gap-1.5 rounded-[8px] bg-slate-100 px-3 py-2 text-sm font-semibold text-slate-700 transition hover:bg-slate-200"
          >
            <ChevronLeft size={16} />
            Mapa
          </button>
          <div className="min-w-0 flex-1">
            <p className={`text-[10px] font-bold uppercase ${activePhase.is_boss ? "text-red-600" : "text-amber-600"}`}>
              {activePhase.is_boss ? "Boss" : `Fase ${activePhase.number}`}
            </p>
            <p className="truncate text-sm font-semibold text-slate-950">{activePhase.title}</p>
          </div>
          <p className="shrink-0 text-xs font-semibold text-slate-500">
            {phraseIndex + 1}/{items.length}
          </p>
        </header>

        <div className="mb-4">
          <ProgressBar value={progress} />
        </div>

        <LessonCard
          key={currentItem?.id ?? phraseIndex}
          answer={answer}
          checked={checked}
          feedback={feedback}
          isCorrect={feedback.quality === "correct"}
          item={currentItem}
          phrase={currentPhrase}
          phraseIndex={phraseIndex}
          totalPhrases={items.length}
          showTranslation={showTranslation}
          onAnswerChange={setAnswer}
          onCheck={() => setChecked(true)}
          onFavorite={() => {}}
          onNext={nextPhrase}
          onReveal={() => setShowTranslation((t) => !t)}
        />
      </div>
    );
  }

  // ── Phase Complete ────────────────────────────────────────────────────────
  if (view === "phase-complete" && activePhase) {
    const accuracy = items.length > 0 ? Math.round((score / items.length) * 100) : 0;

    return (
      <div
        className="relative min-h-dvh overflow-hidden p-6 pb-12 text-center flex flex-col justify-center md:p-10"
        style={{ background: "linear-gradient(180deg, #0a0200, #1a0800)" }}
      >
        <div
          className="pointer-events-none absolute inset-0"
          style={{ background: "radial-gradient(ellipse at 50% 0%, rgba(217,119,6,0.22), transparent 55%)" }}
        />
        <div className="relative z-10">
          <div
            className="mx-auto grid h-20 w-20 place-items-center rounded-full bg-amber-500 text-white shadow-xl"
            style={{ animation: "successPop 420ms ease-out both" }}
          >
            <Trophy size={34} />
          </div>

          <p className="mt-5 text-[10px] font-bold uppercase tracking-widest text-amber-400">Fase Concluída</p>
          <h2 className="mt-2 text-3xl font-semibold text-white">{activePhase.title}</h2>

          <div className="mx-auto mt-6 grid max-w-xs grid-cols-2 gap-3">
            <div className="rounded-[8px] bg-white/10 p-4 ring-1 ring-white/10">
              <p className="text-3xl font-semibold text-white">{score}</p>
              <p className="mt-1 text-[10px] font-bold uppercase text-amber-400">Pontos</p>
            </div>
            <div className="rounded-[8px] bg-white/10 p-4 ring-1 ring-white/10">
              <p className="text-3xl font-semibold text-white">{accuracy}%</p>
              <p className="mt-1 text-[10px] font-bold uppercase text-amber-400">Precisão</p>
            </div>
          </div>

          <div className="mx-auto mt-6 max-w-sm rounded-[8px] border border-amber-900/35 bg-amber-950/25 p-4 text-left">
            <p className="text-sm font-medium leading-6 text-amber-100/80">{activePhase.narrative_outro}</p>
          </div>

          <button
            type="button"
            onClick={() => setView("map")}
            className="mt-6 flex w-full items-center justify-center gap-2 rounded-[8px] bg-amber-500 px-6 py-4 text-base font-semibold text-white transition hover:bg-amber-400 active:scale-[0.98]"
          >
            <Send size={16} />
            Voltar ao Mapa
          </button>
        </div>
      </div>
    );
  }

  // ── Chapter Complete ──────────────────────────────────────────────────────
  if (view === "chapter-complete") {
    return (
      <div
        className="relative min-h-dvh overflow-hidden p-6 pb-12 text-center flex flex-col justify-center md:p-10"
        style={{ background: "linear-gradient(135deg, #1c0800, #3d1a00, #1c0800)" }}
      >
        <div
          className="pointer-events-none absolute inset-0"
          style={{ background: "radial-gradient(ellipse at 50% 15%, rgba(217,119,6,0.3), transparent 55%)" }}
        />
        <div className="relative z-10">
          <div
            className="mx-auto grid h-24 w-24 place-items-center rounded-full text-white shadow-2xl"
            style={{
              background: "linear-gradient(135deg, #92400e, #d97706)",
              animation: "progressGlow 2s ease-in-out infinite, successPop 500ms ease-out both",
            }}
          >
            <Shield size={40} />
          </div>

          <p className="mt-6 text-[10px] font-bold uppercase tracking-widest text-amber-400">Capítulo Concluído!</p>
          <h2 className="mt-2 text-4xl font-semibold text-white">{chapter.title}</h2>

          <div className="mx-auto mt-8 max-w-sm rounded-[8px] border border-amber-700/40 bg-amber-900/25 p-5">
            <p className="text-[10px] font-bold uppercase tracking-wide text-amber-400">Recompensa Desbloqueada</p>
            <p className="mt-3 text-2xl font-semibold text-amber-200">{chapter.reward_name}</p>
            <p className="mt-2 text-sm font-medium leading-6 text-amber-200/65">{chapter.reward_description}</p>
          </div>

          <button
            type="button"
            onClick={() => setView("map")}
            className="mt-7 flex w-full items-center justify-center gap-2 rounded-[8px] bg-amber-500 px-6 py-4 text-base font-semibold text-white transition hover:bg-amber-400 active:scale-[0.98]"
          >
            <Star size={18} />
            Ver Mapa
          </button>

          <button
            type="button"
            onClick={onBack}
            className="mt-3 flex w-full items-center justify-center gap-2 rounded-[8px] bg-white/10 px-6 py-3 text-sm font-semibold text-amber-200/70 transition hover:bg-white/15"
          >
            Voltar à Aventura
          </button>
        </div>
      </div>
    );
  }

  return null;
}

function BackButton({ onBack, label = "Sair" }: { onBack: () => void; label?: string }) {
  return (
    <button
      type="button"
      onClick={onBack}
      className="fixed top-4 left-4 z-30 flex items-center gap-1.5 rounded-full bg-black/40 px-4 py-2.5 text-sm font-semibold text-white backdrop-blur-sm transition hover:bg-black/60 active:scale-95"
    >
      <ChevronLeft size={16} />
      {label}
    </button>
  );
}
