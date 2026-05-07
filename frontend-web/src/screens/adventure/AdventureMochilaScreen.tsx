import { Package } from "lucide-react";
import { useState } from "react";

import { getAdventureColors } from "../../theme/adventureColors";
import type { AdventureThemeMode } from "../../theme/adventureColors";

type Rarity = "comum" | "raro" | "epico";

interface WordCard {
  id: number;
  word: string;
  translation: string;
  category: string;
  rarity: Rarity;
  stars: number;
}

// Placeholder cards — will connect to backend vocab API
const MOCK_CARDS: WordCard[] = [
  { id: 1,  word: "ciao",       translation: "olá",          category: "Saudações",  rarity: "comum", stars: 1 },
  { id: 2,  word: "grazie",     translation: "obrigado",     category: "Saudações",  rarity: "comum", stars: 1 },
  { id: 3,  word: "prego",      translation: "de nada",      category: "Saudações",  rarity: "comum", stars: 1 },
  { id: 4,  word: "amore",      translation: "amor",         category: "Emoções",    rarity: "raro",  stars: 2 },
  { id: 5,  word: "fortezza",   translation: "fortaleza",    category: "Lugares",    rarity: "raro",  stars: 2 },
  { id: 6,  word: "cavaliere",  translation: "cavaleiro",    category: "Personagens",rarity: "raro",  stars: 2 },
  { id: 7,  word: "imperatore", translation: "imperador",    category: "Personagens",rarity: "epico", stars: 3 },
  { id: 8,  word: "colosseo",   translation: "coliseu",      category: "Lugares",    rarity: "epico", stars: 3 },
  { id: 9,  word: "rinascita",  translation: "renascimento", category: "Conceitos",  rarity: "epico", stars: 3 },
  { id: 10, word: "viaggio",    translation: "viagem",       category: "Conceitos",  rarity: "comum", stars: 1 },
  { id: 11, word: "mercato",    translation: "mercado",      category: "Lugares",    rarity: "comum", stars: 1 },
  { id: 12, word: "gondola",    translation: "gôndola",      category: "Lugares",    rarity: "raro",  stars: 2 },
];

const RARITY_CONFIG: Record<Rarity, { darkBg: string; lightBg: string; darkText: string; lightText: string; badge: string; label: string }> = {
  comum: {
    darkBg:   "linear-gradient(135deg, #1e293b 0%, #0f172a 100%)",
    lightBg:  "linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%)",
    darkText: "#f8fafc",
    lightText:"#1e293b",
    badge:    "#475569",
    label:    "Comum",
  },
  raro: {
    darkBg:   "linear-gradient(135deg, #1e3a5f 0%, #0c1a2e 100%)",
    lightBg:  "linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%)",
    darkText: "#f8fafc",
    lightText:"#1e3a8a",
    badge:    "#3b82f6",
    label:    "Raro",
  },
  epico: {
    darkBg:   "linear-gradient(135deg, #3b1f5e 0%, #1a0a2e 100%)",
    lightBg:  "linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%)",
    darkText: "#f8fafc",
    lightText:"#581c87",
    badge:    "#a855f7",
    label:    "Épico",
  },
};

const FILTERS: Array<{ id: Rarity | "todos"; label: string }> = [
  { id: "todos", label: "Todos" },
  { id: "comum", label: "Comum" },
  { id: "raro",  label: "Raro" },
  { id: "epico", label: "Épico" },
];

interface AdventureMochilaScreenProps {
  langCode: string;
  themeMode: AdventureThemeMode;
}

export default function AdventureMochilaScreen({ langCode, themeMode }: AdventureMochilaScreenProps) {
  const c = getAdventureColors(langCode, themeMode);
  const [filter, setFilter] = useState<Rarity | "todos">("todos");

  const cards = filter === "todos" ? MOCK_CARDS : MOCK_CARDS.filter((card) => card.rarity === filter);

  function getRarityStyle(rarity: Rarity) {
    const cfg = RARITY_CONFIG[rarity];
    return {
      bg:    themeMode === "dark" ? cfg.darkBg  : cfg.lightBg,
      text:  themeMode === "dark" ? cfg.darkText : cfg.lightText,
      badge: cfg.badge,
      label: cfg.label,
    };
  }

  return (
    <div className="px-3 pt-4 pb-4">
      {/* Header */}
      <div className="mb-4 px-1">
        <p className="text-[10px] font-bold uppercase tracking-widest" style={{ color: c.goldAccent }}>
          Coleção
        </p>
        <h2 className="mt-0.5 text-2xl font-bold" style={{ color: c.parchment }}>
          Mochila
        </h2>
        <p className="mt-0.5 text-xs font-medium" style={{ color: `${c.parchment}60` }}>
          {MOCK_CARDS.length} cards coletados
        </p>
      </div>

      {/* Filter bar */}
      <div
        className="mb-4 flex gap-1 rounded-xl p-1"
        style={{ background: c.surfaceMid }}
      >
        {FILTERS.map(({ id, label }) => {
          const active = filter === id;
          return (
            <button
              key={id}
              type="button"
              onClick={() => setFilter(id as Rarity | "todos")}
              className="flex-1 rounded-lg py-2 text-xs font-bold uppercase tracking-wider transition"
              style={
                active
                  ? { background: c.ctaBg, color: c.ctaText }
                  : { color: `${c.parchment}55` }
              }
            >
              {label}
            </button>
          );
        })}
      </div>

      {/* Card grid */}
      <div className="grid grid-cols-3 gap-2">
        {cards.map((card) => {
          const style = getRarityStyle(card.rarity);
          return (
            <div
              key={card.id}
              className="flex flex-col rounded-xl p-2.5"
              style={{
                background: style.bg,
                border: `1px solid ${style.badge}30`,
                minHeight: 110,
              }}
            >
              {/* Rarity badge */}
              <span
                className="self-start rounded-full px-2 py-0.5 text-[9px] font-bold uppercase"
                style={{ background: style.badge + "30", color: style.badge }}
              >
                {style.label}
              </span>

              {/* Word */}
              <p
                className="mt-auto text-sm font-bold leading-tight"
                style={{ color: style.text }}
              >
                {card.word}
              </p>
              <p className="text-[10px] font-medium" style={{ color: `${style.text}99` }}>
                {card.translation}
              </p>

              {/* Stars */}
              <div className="mt-1.5 flex gap-0.5">
                {[1, 2, 3].map((s) => (
                  <span
                    key={s}
                    className="text-[10px]"
                    style={{ color: style.badge, opacity: s <= card.stars ? 1 : 0.2 }}
                  >
                    ★
                  </span>
                ))}
              </div>
            </div>
          );
        })}
      </div>

      {/* Empty state */}
      {cards.length === 0 && (
        <div className="flex flex-col items-center justify-center py-16 text-center">
          <Package size={40} style={{ color: `${c.parchment}30` }} />
          <p className="mt-4 text-sm font-semibold" style={{ color: `${c.parchment}50` }}>
            Nenhum card nesta categoria ainda.
          </p>
        </div>
      )}
    </div>
  );
}
