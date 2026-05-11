import { Award, Flame, Swords, Zap } from "lucide-react";

import { useStrings } from "../../../contexts/StringsContext";
import { getAdventureColors } from "../../../theme/adventureColors";
import type { AdventureThemeMode } from "../../../theme/adventureColors";

const JOURNEY_ITEMS = [
  { key: "t1", emoji: "📜", seasonBadge: "T1" },
  { key: "t2", emoji: "🗺️",  seasonBadge: "T2" },
  { key: "t3", emoji: "📖", seasonBadge: "T3" },
  { key: "t4", emoji: "💎", seasonBadge: "T4" },
  { key: "t5", emoji: "👑", seasonBadge: "T5" },
];

const ATTRIBUTES = [
  { label: "Vocabulário" },
  { label: "Gramática"   },
  { label: "Fluência"    },
];

interface AdventureHeroScreenProps {
  langCode:    string;
  themeMode:   AdventureThemeMode;
  storyTitle?: string;
}

export default function AdventureHeroScreen({ langCode, themeMode, storyTitle }: AdventureHeroScreenProps) {
  const s    = useStrings();
  const c    = getAdventureColors(langCode, themeMode);
  const langName = s.languages[langCode.toUpperCase() as keyof typeof s.languages] ?? langCode;

  return (
    <div className="px-4 pb-10 pt-6">

      {/* ── Avatar + identity ───────────────────────────────────────── */}
      <div className="mb-6 flex flex-col items-center text-center">
        <div
          className="relative grid h-24 w-24 place-items-center rounded-full shadow-lg"
          style={{ background: `linear-gradient(135deg, ${c.nodeActive}, ${c.ctaBg})` }}
        >
          <span className="text-3xl font-bold" style={{ color: "#fff" }}>F</span>
          <span
            className="absolute -bottom-1 -right-1 flex h-6 w-6 items-center justify-center rounded-full text-[10px] font-bold"
            style={{ background: c.goldAccent, color: c.seasonBadgeText }}
          >
            1
          </span>
        </div>

        <p className="mt-4 text-[10px] font-bold uppercase tracking-[0.2em]" style={{ color: c.goldAccent }}>
          {storyTitle ?? langName}
        </p>
        <h2 className="mt-1 text-xl font-bold" style={{ color: c.parchment }}>
          Forasteiro
        </h2>
        <p className="mt-0.5 text-xs" style={{ color: c.textFaint }}>{langName} · Nível 1</p>

        {/* Stats row */}
        <div
          className="mt-4 flex w-full divide-x rounded-xl overflow-hidden"
          style={{ background: c.surfaceMid, borderColor: c.borderFaint }}
        >
          {[
            { Icon: Swords, label: "Fases",     value: "0"  },
            { Icon: Zap,    label: "XP",        value: "0"  },
            { Icon: Flame,  label: "Sequência", value: "0d" },
          ].map(({ Icon, label, value }) => (
            <div key={label} className="flex flex-1 flex-col items-center gap-0.5 py-3">
              <span className="text-base font-bold" style={{ color: c.parchment }}>{value}</span>
              <div className="flex items-center gap-1">
                <Icon size={10} style={{ color: c.textFaint }} />
                <span className="text-[9px] uppercase tracking-wide" style={{ color: c.textFaint }}>{label}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* ── Body ───────────────────────────────────────────────────── */}
      <div>

        {/* XP progress */}
        <div
          className="mb-5 rounded-2xl p-4"
          style={{ background: c.surfaceMid, border: `1px solid ${c.pathColor}25` }}
        >
          <div className="mb-2.5 flex items-center justify-between">
            <div className="flex items-center gap-1.5">
              <Zap size={12} style={{ color: c.goldAccent }} />
              <span className="text-xs font-bold uppercase tracking-wide" style={{ color: c.goldAccent }}>
                XP · Nível 1
              </span>
            </div>
            <span className="text-xs font-semibold tabular-nums" style={{ color: c.textFaint }}>0 / 1 000</span>
          </div>
          <div className="h-2 overflow-hidden rounded-full" style={{ background: c.surface }}>
            <div
              className="h-full w-0 rounded-full"
              style={{ background: `linear-gradient(90deg, ${c.nodeActive}, ${c.goldAccent})` }}
            />
          </div>
        </div>

        {/* Attributes */}
        <section className="mb-5">
          <p className="mb-2 text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
            Atributos
          </p>
          <div
            className="overflow-hidden rounded-2xl"
            style={{ border: `1px solid ${c.borderFaint}` }}
          >
            {ATTRIBUTES.map(({ label }, i) => (
              <div
                key={label}
                className="px-4 py-3"
                style={{
                  background: c.surfaceMid,
                  borderBottom: i < ATTRIBUTES.length - 1 ? `1px solid ${c.borderFaint}` : undefined,
                }}
              >
                <div className="mb-1.5 flex items-center justify-between">
                  <span className="text-xs font-semibold" style={{ color: c.textOnBg }}>{label}</span>
                  <span className="text-xs font-bold tabular-nums" style={{ color: c.textFaint }}>0%</span>
                </div>
                <div className="h-1.5 overflow-hidden rounded-full" style={{ background: c.surface }}>
                  <div className="h-full w-0 rounded-full" style={{ background: c.pathColor }} />
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Journey items */}
        <section className="mb-5">
          <p className="mb-2 text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
            Itens da Jornada
          </p>
          <div className="grid grid-cols-5 gap-2">
            {JOURNEY_ITEMS.map((item) => (
              <div
                key={item.key}
                className="flex flex-col items-center gap-1.5 rounded-xl pb-3 pt-3.5"
                style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
              >
                <span className="text-2xl leading-none" style={{ filter: "grayscale(1)", opacity: 0.22 }}>
                  {item.emoji}
                </span>
                <span
                  className="rounded px-1.5 py-0.5 text-[8px] font-bold uppercase tracking-wide"
                  style={{ background: c.surfaceMid, color: c.textFaint }}
                >
                  {item.seasonBadge}
                </span>
              </div>
            ))}
          </div>
          <p className="mt-2 text-center text-[10px]" style={{ color: c.textFaint }}>
            Derrote o boss de cada temporada para desbloquear
          </p>
        </section>

        {/* Achievements */}
        <section>
          <p className="mb-2 text-[10px] font-bold uppercase tracking-widest" style={{ color: c.textFaint }}>
            Conquistas
          </p>
          <div
            className="flex flex-col items-center gap-2 rounded-2xl py-10 text-center"
            style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
          >
            <Award size={32} style={{ color: c.textFaint }} />
            <p className="text-sm font-semibold" style={{ color: c.textFaint }}>Nenhuma conquista ainda</p>
            <p className="text-xs" style={{ color: c.textFaint }}>Complete fases para desbloquear</p>
          </div>
        </section>

      </div>
    </div>
  );
}
