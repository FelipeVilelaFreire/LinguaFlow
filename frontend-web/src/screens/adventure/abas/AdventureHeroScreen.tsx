import { type LucideIcon, Award, BookOpen, Crown, Flame, Gem, Map, Scroll, Swords, Zap } from "lucide-react";
import { useEffect, useRef, useState } from "react";

import Emoji from "../../../components/Emoji";

import { adventureService } from "../../../services/adventureService";
import { getAdventureColors } from "../../../theme/adventureColors";
import type { AdventureThemeMode } from "../../../theme/adventureColors";
import type { HeroStats } from "../../../types/adventure";
import { useStrings } from "../../../contexts/StringsContext";

const JOURNEY_ITEMS: Array<{ key: string; Icon: LucideIcon; seasonBadge: string }> = [
  { key: "t1", Icon: Scroll,   seasonBadge: "T1" },
  { key: "t2", Icon: Map,      seasonBadge: "T2" },
  { key: "t3", Icon: BookOpen, seasonBadge: "T3" },
  { key: "t4", Icon: Gem,      seasonBadge: "T4" },
  { key: "t5", Icon: Crown,    seasonBadge: "T5" },
];

const LEVEL_LABELS = ["", "Aprendiz", "Viajante", "Explorador", "Veterano", "Mestre", "Lendário"];

const ATTRIBUTE_DEFS: Array<{ key: keyof HeroStats["attributes"]; label: string }> = [
  { key: "vocabulario", label: "Vocabulário" },
  { key: "gramatica",   label: "Gramática"   },
  { key: "fluencia",    label: "Fluência"     },
];

interface AdventureHeroScreenProps {
  langCode:    string;
  themeMode:   AdventureThemeMode;
  storyTitle?: string;
  firstName?:  string;
}

function useCountUp(target: number, duration = 900) {
  const [value, setValue] = useState(0);
  useEffect(() => {
    if (target === 0) { setValue(0); return; }
    let start: number | null = null;
    const step = (ts: number) => {
      if (!start) start = ts;
      const pct = Math.min((ts - start) / duration, 1);
      setValue(Math.floor(pct * target));
      if (pct < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }, [target, duration]);
  return value;
}

export default function AdventureHeroScreen({
  langCode,
  themeMode,
  storyTitle,
  firstName = "",
}: AdventureHeroScreenProps) {
  const s    = useStrings();
  const c    = getAdventureColors(langCode, themeMode);
  const langName = s.languages[langCode.toUpperCase() as keyof typeof s.languages] ?? langCode;

  const [stats, setStats]     = useState<HeroStats | null>(null);
  const [mounted, setMounted] = useState(false);
  const barRefs = useRef<(HTMLDivElement | null)[]>([]);

  useEffect(() => {
    adventureService.getHeroStats()
      .then(setStats)
      .catch(() => {/* non-blocking */});
  }, []);

  useEffect(() => {
    const id = setTimeout(() => setMounted(true), 50);
    return () => clearTimeout(id);
  }, []);

  const displayXP      = useCountUp(stats?.xp ?? 0);
  const displayPhases  = useCountUp(stats?.phases_completed ?? 0);
  const displayStreak  = useCountUp(stats?.current_streak ?? 0);

  const level          = stats?.level ?? 1;
  const xp             = stats?.xp ?? 0;
  const xpCurrent      = stats?.xp_current_level ?? 0;
  const xpNext         = stats?.xp_next_level ?? null;
  const xpProgress     = xpNext ? Math.min((xp - xpCurrent) / (xpNext - xpCurrent), 1) : 1;

  const unlockedSeasons = stats
    ? Math.min(Math.floor(stats.phases_completed / 25), 5)
    : 0;

  return (
    <div className="px-4 pb-10 pt-6">

      {/* ── Avatar + identity ──────────────────────────────────────────── */}
      <div
        className="mb-6 flex flex-col items-center text-center"
        style={{ animation: "narrativeFadeIn 0.5s ease-out both" }}
      >
        <div
          className="relative grid h-24 w-24 place-items-center rounded-full shadow-lg"
          style={{
            background:  `linear-gradient(135deg, ${c.nodeActive}, ${c.ctaBg})`,
            boxShadow:   `0 0 32px ${c.nodeActiveGlow}60`,
            animation:   "successPop 0.45s cubic-bezier(0.16,1,0.3,1) 0.1s both",
          }}
        >
          <span className="text-3xl font-bold" style={{ color: "#fff" }}>
            {(firstName || "F").charAt(0).toUpperCase()}
          </span>
          <span
            className="absolute -bottom-1 -right-1 flex h-7 w-7 items-center justify-center rounded-full text-[11px] font-bold"
            style={{
              background: c.goldAccent,
              color:      c.seasonBadgeText,
              boxShadow:  `0 2px 8px ${c.goldAccent}60`,
            }}
          >
            {level}
          </span>
        </div>

        <p className="mt-4 text-[10px] font-bold uppercase tracking-[0.2em]" style={{ color: c.goldAccent }}>
          {storyTitle ?? langName}
        </p>
        <h2 className="mt-1 text-xl font-bold" style={{ color: c.parchment }}>
          {firstName || "Forasteiro"}
        </h2>
        <p className="mt-0.5 text-xs" style={{ color: c.textFaint }}>
          {langName} · {LEVEL_LABELS[level] ?? `Nível ${level}`}
        </p>

        {/* Stats row */}
        <div
          className="mt-4 flex w-full divide-x overflow-hidden rounded-xl"
          style={{ background: c.surfaceMid, borderColor: c.borderFaint }}
        >
          {[
            { Icon: Swords, label: "Fases",     value: String(displayPhases) },
            { Icon: Zap,    label: "XP",        value: String(displayXP)     },
            { Icon: Flame,  label: "Sequência", value: `${displayStreak}d`   },
          ].map(({ Icon, label, value }) => (
            <div key={label} className="flex flex-1 flex-col items-center gap-0.5 py-3">
              <span className="text-base font-bold tabular-nums" style={{ color: c.parchment }}>{value}</span>
              <div className="flex items-center gap-1">
                <Icon size={10} style={{ color: c.textFaint }} />
                <span className="text-[9px] uppercase tracking-wide" style={{ color: c.textFaint }}>{label}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* ── Body ────────────────────────────────────────────────────────── */}
      <div>

        {/* XP progress bar */}
        <div
          className="mb-5 rounded-2xl p-4"
          style={{
            background: c.surfaceMid,
            border:     `1px solid ${c.pathColor}25`,
            animation:  "narrativeFadeIn 0.5s ease-out 0.15s both",
          }}
        >
          <div className="mb-2.5 flex items-center justify-between">
            <div className="flex items-center gap-1.5">
              <Zap size={12} style={{ color: c.goldAccent }} />
              <span className="text-xs font-bold uppercase tracking-wide" style={{ color: c.goldAccent }}>
                XP · {LEVEL_LABELS[level] ?? `Nível ${level}`}
              </span>
            </div>
            <span className="text-xs font-semibold tabular-nums" style={{ color: c.textFaint }}>
              {xp - xpCurrent} / {xpNext !== null ? xpNext - xpCurrent : "∞"}
            </span>
          </div>
          <div className="h-2 overflow-hidden rounded-full" style={{ background: c.surface }}>
            <div
              className="h-full rounded-full"
              style={{
                width:      `${mounted ? xpProgress * 100 : 0}%`,
                background: `linear-gradient(90deg, ${c.nodeActive}, ${c.goldAccent})`,
                transition: "width 1.1s cubic-bezier(0.16,1,0.3,1) 0.3s",
                boxShadow:  `0 0 8px ${c.goldAccent}80`,
              }}
            />
          </div>
          {xpNext !== null && (
            <p className="mt-1.5 text-[10px]" style={{ color: c.textFaint }}>
              {xpNext - xp} XP para {LEVEL_LABELS[level + 1] ?? `Nível ${level + 1}`}
            </p>
          )}
        </div>

        {/* Attributes */}
        <section
          className="mb-5"
          style={{ animation: "narrativeFadeIn 0.5s ease-out 0.25s both" }}
        >
          <p className="mb-2 text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
            Atributos
          </p>
          <div className="overflow-hidden rounded-2xl" style={{ border: `1px solid ${c.borderFaint}` }}>
            {ATTRIBUTE_DEFS.map(({ key, label }, i) => {
              const pct = stats?.attributes[key] ?? 0;
              return (
                <div
                  key={key}
                  className="px-4 py-3"
                  style={{
                    background:   c.surfaceMid,
                    borderBottom: i < ATTRIBUTE_DEFS.length - 1 ? `1px solid ${c.borderFaint}` : undefined,
                  }}
                >
                  <div className="mb-1.5 flex items-center justify-between">
                    <span className="text-xs font-semibold" style={{ color: c.textOnBg }}>{label}</span>
                    <span className="text-xs font-bold tabular-nums" style={{ color: c.textFaint }}>{pct}%</span>
                  </div>
                  <div className="h-1.5 overflow-hidden rounded-full" style={{ background: c.surface }}>
                    <div
                      ref={el => { barRefs.current[i] = el; }}
                      className="h-full rounded-full"
                      style={{
                        width:      `${mounted ? pct : 0}%`,
                        background: c.pathColor,
                        transition: `width 1s cubic-bezier(0.16,1,0.3,1) ${0.45 + i * 0.12}s`,
                      }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </section>

        {/* Journey items */}
        <section
          className="mb-5"
          style={{ animation: "narrativeFadeIn 0.5s ease-out 0.35s both" }}
        >
          <p className="mb-2 text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
            Itens da Jornada
          </p>
          <div className="grid grid-cols-5 gap-2">
            {JOURNEY_ITEMS.map((item, i) => {
              const unlocked = i < unlockedSeasons;
              return (
                <div
                  key={item.key}
                  className="flex flex-col items-center gap-1.5 rounded-xl pb-3 pt-3.5"
                  style={{
                    background: unlocked ? `${c.nodeActive}18` : c.surface,
                    border:     `1px solid ${unlocked ? c.nodeActive + "44" : c.borderFaint}`,
                    transition: `all 0.35s ease ${i * 0.07}s`,
                  }}
                >
                  <item.Icon
                    size={22}
                    style={{ color: unlocked ? c.nodeActive : c.textFaint, opacity: unlocked ? 1 : 0.22 }}
                  />
                  <span
                    className="rounded px-1.5 py-0.5 text-[8px] font-bold uppercase tracking-wide"
                    style={{
                      background: unlocked ? `${c.nodeActive}22` : c.surfaceMid,
                      color:      unlocked ? c.nodeActive         : c.textFaint,
                    }}
                  >
                    {item.seasonBadge}
                  </span>
                </div>
              );
            })}
          </div>
          <p className="mt-2 text-center text-[10px]" style={{ color: c.textFaint }}>
            Derrote o boss de cada temporada para desbloquear
          </p>
        </section>

        {/* Achievements */}
        <section style={{ animation: "narrativeFadeIn 0.5s ease-out 0.45s both" }}>
          <p className="mb-2 text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
            Conquistas
          </p>
          {stats?.achievements.length ? (
            <div
              className="overflow-hidden rounded-2xl"
              style={{ border: `1px solid ${c.borderFaint}` }}
            >
              {stats.achievements.map((ach, i) => (
                <div
                  key={ach.key}
                  className="flex items-center gap-3 px-4 py-3"
                  style={{
                    background:   c.surfaceMid,
                    borderBottom: i < stats.achievements.length - 1 ? `1px solid ${c.borderFaint}` : undefined,
                    animation:    `successPop 0.35s ease-out ${i * 0.08}s both`,
                  }}
                >
                  <Emoji char={ach.emoji} size={28} style={{ flexShrink: 0 }} />
                  <div className="min-w-0 flex-1">
                    <p className="text-xs font-bold" style={{ color: c.parchment }}>{ach.label}</p>
                    <p className="text-[10px]" style={{ color: c.textFaint }}>{ach.desc}</p>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div
              className="flex flex-col items-center gap-2 rounded-2xl py-10 text-center"
              style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
            >
              <Award size={32} style={{ color: c.textFaint }} />
              <p className="text-sm font-semibold" style={{ color: c.textFaint }}>Nenhuma conquista ainda</p>
              <p className="text-xs" style={{ color: c.textFaint }}>Complete fases para desbloquear</p>
            </div>
          )}
        </section>

      </div>
    </div>
  );
}
