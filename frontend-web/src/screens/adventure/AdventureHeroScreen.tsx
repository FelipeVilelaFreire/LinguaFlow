import { Lock, Trophy, Zap } from "lucide-react";

import { getAdventureColors } from "../../theme/adventureColors";

// Reward items match the Italian seeds: Sigillo → Mappa → Codice → Pietra → Corona
const ITEMS = [
  { key: "sigillo", name: "Sigillo",  emoji: "📜", season: 1 },
  { key: "mappa",   name: "Mappa",    emoji: "🗺️",  season: 2 },
  { key: "codice",  name: "Codice",   emoji: "📖", season: 3 },
  { key: "pietra",  name: "Pietra",   emoji: "💎", season: 4 },
  { key: "corona",  name: "Corona",   emoji: "👑", season: 5 },
];

// Placeholder stats — will come from backend
const HERO = {
  name:       "Il Viandante",
  title:      "Viaggiatore",
  level:      3,
  xp:         1240,
  xpNext:     2000,
  attributes: [
    { label: "Vocabulário", value: 68 },
    { label: "Gramática",   value: 42 },
    { label: "Fluência",    value: 31 },
  ],
  unlockedSeasons: 1,
  achievements: [
    { icon: "⚔️", label: "Primeira Batalha",  desc: "Completou a fase 1" },
    { icon: "🔥", label: "Em Chamas",         desc: "7 dias seguidos" },
    { icon: "📚", label: "Leitor de Runas",   desc: "50 frases aprendidas" },
  ],
};

interface AdventureHeroScreenProps {
  langCode: string;
}

export default function AdventureHeroScreen({ langCode }: AdventureHeroScreenProps) {
  const c = getAdventureColors(langCode);
  const xpPct = Math.round((HERO.xp / HERO.xpNext) * 100);

  return (
    <div className="px-4 pb-6 pt-4">
      {/* ── Avatar + title ───────────────────────────────────────── */}
      <div className="flex flex-col items-center py-6 text-center">
        <div
          className="grid h-24 w-24 place-items-center rounded-full text-4xl shadow-xl"
          style={{
            background: `linear-gradient(135deg, ${c.nodeActive}, ${c.ctaBg})`,
            boxShadow: `0 0 32px ${c.nodeActiveGlow}`,
          }}
        >
          ⚔️
        </div>
        <p
          className="mt-4 text-2xl font-bold tracking-tight"
          style={{ color: c.parchment }}
        >
          {HERO.name}
        </p>
        <div className="mt-1 flex items-center gap-2">
          <span
            className="rounded-full px-3 py-0.5 text-xs font-bold uppercase tracking-wider"
            style={{ background: c.seasonBadgeBg, color: c.seasonBadgeText }}
          >
            Nível {HERO.level}
          </span>
          <span className="text-xs font-semibold" style={{ color: `${c.parchment}60` }}>
            {HERO.title}
          </span>
        </div>
      </div>

      {/* ── XP bar ───────────────────────────────────────────────── */}
      <div
        className="mb-4 rounded-xl p-4"
        style={{ background: "rgba(0,0,0,0.35)", border: `1px solid ${c.pathColor}25` }}
      >
        <div className="mb-2 flex items-center justify-between">
          <div className="flex items-center gap-1.5">
            <Zap size={13} style={{ color: c.goldAccent }} />
            <span className="text-xs font-bold uppercase tracking-wide" style={{ color: c.goldAccent }}>
              XP
            </span>
          </div>
          <span className="text-xs font-semibold" style={{ color: `${c.parchment}70` }}>
            {HERO.xp.toLocaleString()} / {HERO.xpNext.toLocaleString()}
          </span>
        </div>
        <div className="h-2.5 overflow-hidden rounded-full" style={{ background: "rgba(255,255,255,0.08)" }}>
          <div
            className="h-full rounded-full transition-all"
            style={{
              width: `${xpPct}%`,
              background: `linear-gradient(90deg, ${c.nodeActive}, ${c.goldAccent})`,
              boxShadow: `0 0 8px ${c.nodeActiveGlow}`,
            }}
          />
        </div>
      </div>

      {/* ── Attributes ───────────────────────────────────────────── */}
      <section className="mb-4">
        <p className="mb-2 text-[10px] font-bold uppercase tracking-widest" style={{ color: `${c.parchment}50` }}>
          Atributos
        </p>
        <div
          className="flex flex-col gap-3 rounded-xl p-4"
          style={{ background: "rgba(0,0,0,0.35)", border: `1px solid ${c.pathColor}25` }}
        >
          {HERO.attributes.map(({ label, value }) => (
            <div key={label}>
              <div className="mb-1 flex items-center justify-between">
                <span className="text-xs font-semibold" style={{ color: `${c.parchment}80` }}>{label}</span>
                <span className="text-xs font-bold" style={{ color: c.goldAccent }}>{value}%</span>
              </div>
              <div className="h-2 overflow-hidden rounded-full" style={{ background: "rgba(255,255,255,0.06)" }}>
                <div
                  className="h-full rounded-full"
                  style={{
                    width: `${value}%`,
                    background: c.pathColor,
                    opacity: 0.75,
                  }}
                />
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* ── Collected items (season rewards) ─────────────────────── */}
      <section className="mb-4">
        <p className="mb-2 text-[10px] font-bold uppercase tracking-widest" style={{ color: `${c.parchment}50` }}>
          Itens Coletados
        </p>
        <div className="flex gap-2">
          {ITEMS.map((item) => {
            const unlocked = item.season <= HERO.unlockedSeasons;
            return (
              <div
                key={item.key}
                className="flex flex-1 flex-col items-center gap-1.5 rounded-xl py-3"
                style={{
                  background: unlocked ? `${c.seasonBadgeBg}25` : "rgba(255,255,255,0.04)",
                  border: `1px solid ${unlocked ? c.seasonBadgeBg + "40" : "rgba(255,255,255,0.06)"}`,
                }}
              >
                <span
                  className="text-xl"
                  style={{ filter: unlocked ? "none" : "grayscale(1)", opacity: unlocked ? 1 : 0.25 }}
                >
                  {item.emoji}
                </span>
                <span
                  className="text-[9px] font-bold uppercase tracking-wide"
                  style={{ color: unlocked ? c.goldAccent : `${c.parchment}25` }}
                >
                  {item.name}
                </span>
                {!unlocked && <Lock size={9} style={{ color: `${c.parchment}20` }} />}
              </div>
            );
          })}
        </div>
      </section>

      {/* ── Achievements ─────────────────────────────────────────── */}
      <section>
        <p className="mb-2 text-[10px] font-bold uppercase tracking-widest" style={{ color: `${c.parchment}50` }}>
          Conquistas Recentes
        </p>
        <div className="flex flex-col gap-2">
          {HERO.achievements.map(({ icon, label, desc }) => (
            <div
              key={label}
              className="flex items-center gap-3 rounded-xl p-3"
              style={{ background: "rgba(0,0,0,0.30)", border: `1px solid ${c.pathColor}20` }}
            >
              <span className="text-xl">{icon}</span>
              <div>
                <p className="text-sm font-bold" style={{ color: c.parchment }}>{label}</p>
                <p className="text-xs font-medium" style={{ color: `${c.parchment}55` }}>{desc}</p>
              </div>
              <Trophy size={14} className="ml-auto shrink-0" style={{ color: c.goldAccent }} />
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
