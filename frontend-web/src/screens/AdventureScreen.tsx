import { ArrowRight, BookOpen, Lock, Skull, Swords } from "lucide-react";

import LangFlag from "../components/ui/LangFlag";
import { useImmersiveNav } from "../hooks/useImmersiveNav";
import { ROUTES } from "../constants/routes";
import { ADVENTURE_IT_MOCK } from "../mocks/adventureItMock";
import { getAdventureColors } from "../theme/adventureColors";

const CHAPTERS = ADVENTURE_IT_MOCK;
const LANG     = CHAPTERS[0].language_code;
const c        = getAdventureColors(LANG);

const totalPhases     = CHAPTERS.reduce((s, ch) => s + ch.phases.length, 0);
const completedPhases = CHAPTERS.reduce((s, ch) => s + ch.phases.filter(p => p.is_completed).length, 0);
const progressPct     = Math.round((completedPhases / totalPhases) * 100);

const activeChapter = CHAPTERS.find(ch => ch.progress && !ch.phases.every(p => p.is_completed)) ?? CHAPTERS[0];
const activePhase   = activeChapter.phases.find(p => !p.is_completed) ?? activeChapter.phases[0];

const TITLE_PT: Record<string, string> = {
  "it-a1-borgo":   "Chegada ao Vilarejo",
  "it-a2-venezia": "Veneza dos Mercantes",
  "it-b1-toscana": "A Toscana dos Médici",
  "it-b2-napoli":  "Nápoles e o Vesúvio",
  "it-c1-roma":    "Roma Eterna",
};

export default function AdventureScreen() {
  const { navigateImmersive } = useImmersiveNav();

  function enter() {
    navigateImmersive(
      ROUTES.adventureMap,
      {},
      { title: activeChapter.title, subtitle: `${activeChapter.level} · Entrando no mundo`, langCode: LANG },
    );
  }

  return (
    // h-[calc(100dvh-3.5rem)] = preenche exatamente do topo do main até o fundo da tela
    // -mx-3 -mt-3 = quebra o padding do <main>
    <div
      className="-mx-3 -mt-3 h-[calc(100dvh-3.5rem)] flex flex-col overflow-hidden"
      style={{ background: `linear-gradient(180deg, ${c.bgFrom} 0%, ${c.bgMid} 60%, ${c.bgTo} 100%)` }}
    >
      {/* Glows decorativos */}
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <div className="absolute" style={{ top: "-8%", left: "30%", width: 380, height: 280, background: `radial-gradient(ellipse, ${c.ambientGlow}, transparent 70%)` }} />
        <div className="absolute" style={{ bottom: "20%", right: "-5%", width: 220, height: 220, background: `radial-gradient(circle, ${c.pathGlow}, transparent 70%)` }} />
      </div>

      {/* ── Área de conteúdo scrollável (flex-1 + min-h-0 para o overflow funcionar) */}
      <div className="relative z-10 flex-1 min-h-0 overflow-y-auto px-5 pt-5 pb-2">

        {/* Badge de idioma */}
        <div className="flex items-center gap-2">
          <LangFlag code={LANG} size="sm" />
          <span
            className="rounded-full px-3 py-1 text-[10px] font-bold uppercase tracking-widest"
            style={{ background: `${c.seasonBadgeBg}28`, color: c.goldAccent, border: `1px solid ${c.seasonBadgeBg}38` }}
          >
            A1 · Italiano
          </span>
        </div>

        {/* Título hero */}
        <div className="mt-4">
          <p className="text-[10px] font-bold uppercase tracking-[0.2em]" style={{ color: `${c.parchment}45` }}>
            A história de
          </p>
          <h1
            className="mt-1 text-5xl font-bold leading-none tracking-tight"
            style={{ color: c.parchment, textShadow: `0 2px 20px ${c.pathGlow}` }}
          >
            Il Viandante
          </h1>
          <p className="mt-2.5 text-sm font-medium leading-relaxed" style={{ color: `${c.parchment}70` }}>
            Um viajante sem memória acorda na Itália medieval. A única forma de descobrir quem é — aprender o idioma que esqueceu.
          </p>
        </div>

        {/* Barra de progresso global */}
        <div className="mt-5">
          <div className="mb-1.5 flex items-center justify-between">
            <span className="text-[10px] font-bold uppercase tracking-widest" style={{ color: `${c.parchment}45` }}>
              Progresso
            </span>
            <span className="text-xs font-bold tabular-nums" style={{ color: c.goldAccent }}>
              {completedPhases}/{totalPhases}
            </span>
          </div>
          <div className="h-1.5 overflow-hidden rounded-full" style={{ background: "rgba(255,255,255,0.07)" }}>
            <div
              className="h-full rounded-full"
              style={{
                width: `${progressPct || 2}%`,
                background: `linear-gradient(90deg, ${c.nodeActive}, ${c.goldAccent})`,
                boxShadow: `0 0 8px ${c.nodeActiveGlow}`,
              }}
            />
          </div>
        </div>

        {/* Lista de temporadas */}
        <div className="mt-4 flex flex-col gap-1.5">
          {CHAPTERS.map((ch, i) => {
            const done      = ch.phases.filter(p => p.is_completed).length;
            const isUnlocked = i === 0 || CHAPTERS[i - 1].phases.every(p => p.is_completed);
            const isCurrent  = ch.id === activeChapter.id;

            const Tag = isUnlocked ? "button" : "div";
            return (
              <Tag
                key={ch.id}
                type={isUnlocked ? "button" : undefined}
                onClick={isUnlocked ? enter : undefined}
                className={`flex w-full items-center gap-3 rounded-xl px-3 py-2.5 text-left transition ${isUnlocked ? "active:scale-[0.98] hover:brightness-110" : ""}`}
                style={{
                  background: isCurrent
                    ? `${c.seasonBadgeBg}20`
                    : isUnlocked
                    ? "rgba(255,255,255,0.04)"
                    : "rgba(0,0,0,0.18)",
                  border: `1px solid ${isCurrent ? c.seasonBadgeBg + "40" : "rgba(255,255,255,0.05)"}`,
                }}
              >
                {/* Badge de nível */}
                <span
                  className="shrink-0 rounded-md px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider"
                  style={
                    isUnlocked
                      ? { background: c.seasonBadgeBg, color: c.seasonBadgeText }
                      : { background: "rgba(255,255,255,0.05)", color: "rgba(255,255,255,0.18)" }
                  }
                >
                  {ch.level}
                </span>

                {/* Nome + tradução + dots */}
                <div className="min-w-0 flex-1">
                  <p
                    className="truncate text-sm font-semibold leading-tight"
                    style={{ color: isUnlocked ? c.parchment : `${c.parchment}25` }}
                  >
                    {ch.title}
                  </p>
                  {isUnlocked && TITLE_PT[ch.slug] && (
                    <p className="truncate text-[11px] font-medium" style={{ color: `${c.parchment}50` }}>
                      {TITLE_PT[ch.slug]}
                    </p>
                  )}
                  {isUnlocked && (
                    <div className="mt-1 flex gap-[2px]">
                      {ch.phases.map((p, pi) => (
                        <div
                          key={pi}
                          className="h-[3px] w-[6px] rounded-full"
                          style={{
                            background: p.is_completed
                              ? c.nodeCompleted
                              : pi === done && isCurrent
                              ? c.nodeActive
                              : p.phase_type === "review"
                              ? "rgba(217,119,6,0.20)"
                              : "rgba(255,255,255,0.10)",
                          }}
                        />
                      ))}
                    </div>
                  )}
                </div>

                {/* Estado direito */}
                {!isUnlocked ? (
                  <Lock size={12} style={{ color: "rgba(255,255,255,0.13)", flexShrink: 0 }} />
                ) : done === ch.phases.length ? (
                  <span className="shrink-0 text-[11px] font-bold" style={{ color: c.nodeCompleted }}>✓</span>
                ) : (
                  <span className="shrink-0 text-[10px] font-bold tabular-nums" style={{ color: isCurrent ? c.goldAccent : `${c.parchment}35` }}>
                    {done}/{ch.phases.length}
                  </span>
                )}
              </Tag>
            );
          })}
        </div>

        {/* Fase atual */}
        <div
          className="mt-3 flex items-center gap-3 rounded-xl px-3.5 py-3"
          style={{
            background: `${activePhase.is_boss ? c.bossColor : c.nodeActive}15`,
            border: `1px solid ${activePhase.is_boss ? c.bossColor : c.nodeActive}30`,
          }}
        >
          <div
            className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full"
            style={{ background: activePhase.is_boss ? c.bossColor : activePhase.phase_type === "review" ? c.goldAccent : c.nodeActive }}
          >
            {activePhase.is_boss ? <Skull size={13} color={c.ctaText} />
            : activePhase.phase_type === "review" ? <BookOpen size={13} color={c.ctaText} />
            : <Swords size={13} color={c.ctaText} />}
          </div>
          <div className="min-w-0">
            <p className="text-[10px] font-bold uppercase tracking-wide" style={{ color: c.goldAccent }}>
              {activePhase.is_boss ? `⚔️ Boss · ${activeChapter.level}` : activePhase.phase_type === "review" ? `📚 Revisão · ${activeChapter.level}` : `Próxima fase · ${activeChapter.level}`}
            </p>
            <p className="truncate text-sm font-semibold leading-tight" style={{ color: c.parchment }}>
              {activePhase.title}
            </p>
            {activePhase.npc_name && activePhase.phase_type === "story" && (
              <p className="truncate text-[11px] font-medium" style={{ color: `${c.parchment}50` }}>
                com {activePhase.npc_name}
              </p>
            )}
          </div>
        </div>

      </div>

      {/* ── CTA — preso ao fundo, pb-20 (5rem) sobe acima do bottom nav (5rem) */}
      <div
        className="relative z-10 shrink-0 px-5 pb-24 pt-3"
        style={{ background: `linear-gradient(0deg, ${c.bgTo}f8 0%, transparent 100%)` }}
      >
        <button
          type="button"
          onClick={enter}
          className="flex w-full items-center justify-center gap-2.5 rounded-xl px-6 py-4 text-base font-bold shadow-xl transition active:scale-[0.98]"
          style={{
            background: `linear-gradient(135deg, ${c.ctaBg}, ${c.nodeActive})`,
            color: c.ctaText,
            boxShadow: `0 4px 20px ${c.nodeActiveGlow}`,
          }}
        >
          {completedPhases > 0 ? "Continuar Aventura" : "Iniciar Aventura"}
          <ArrowRight size={18} strokeWidth={2.5} />
        </button>
      </div>

    </div>
  );
}
