import { useEffect, useState } from "react";
import { BookOpen, Search } from "lucide-react";

import { useStrings } from "../../../contexts/StringsContext";
import { adventureService } from "../../../services/adventureService";
import { getAdventureColors } from "../../../theme/adventureColors";
import type { AdventureThemeMode } from "../../../theme/adventureColors";

type WordTier = "bronze" | "prata" | "ouro" | "diamante" | "esmeralda";

interface LearnedWord {
  target: string;
  native: string;
  word_id: string;
  tier: WordTier;
}

const TIER_CONFIG: Record<WordTier, { label: string; dot: string }> = {
  bronze:    { label: "Bronze",    dot: "#cd7f32" },
  prata:     { label: "Prata",     dot: "#a8a9ad" },
  ouro:      { label: "Ouro",      dot: "#f59e0b" },
  diamante:  { label: "Diamante",  dot: "#38bdf8" },
  esmeralda: { label: "Esmeralda", dot: "#34d399" },
};

interface AdventureWordsScreenProps {
  langCode: string;
  themeMode: AdventureThemeMode;
}

export default function AdventureWordsScreen({ langCode, themeMode }: AdventureWordsScreenProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, themeMode);
  const [allWords, setAllWords] = useState<LearnedWord[]>([]);
  const [loading, setLoading]   = useState(true);
  const [query, setQuery]       = useState("");

  useEffect(() => {
    adventureService.listLearnedWords(langCode)
      .then(data => setAllWords(data.filter(w => w.native) as LearnedWord[]))
      .catch(() => setAllWords([]))
      .finally(() => setLoading(false));
  }, [langCode]);

  const words = query.trim()
    ? allWords.filter(w =>
        w.target.toLowerCase().includes(query.toLowerCase()) ||
        w.native.toLowerCase().includes(query.toLowerCase())
      )
    : allWords;

  return (
    <div className="px-4 pb-8 pt-5 md:px-8 md:pt-7">

      <div className="mb-5">
        <p className="text-[10px] font-bold uppercase tracking-[0.22em]" style={{ color: c.textFaint }}>
          {s.adventure.vocabularyLabel}
        </p>
        <h2 className="mt-0.5 text-xl font-bold leading-tight md:text-2xl" style={{ color: c.parchment }}>
          {s.adventure.wordsLearned}
        </h2>
        <p className="mt-1 text-sm" style={{ color: c.textOnBg }}>
          {loading ? s.adventure.loading : s.adventure.wordCount(allWords.length)}
        </p>
      </div>

      {allWords.length > 0 && (
        <div
          className="mb-5 flex items-center gap-2.5 rounded-xl px-3.5 py-2.5"
          style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
        >
          <Search size={15} style={{ color: c.textFaint, flexShrink: 0 }} />
          <input
            type="text"
            value={query}
            onChange={e => setQuery(e.target.value)}
            placeholder={s.adventure.searchPlaceholder}
            className="flex-1 bg-transparent text-sm outline-none placeholder:opacity-40"
            style={{ color: c.parchment }}
          />
          {query && (
            <button
              type="button"
              onClick={() => setQuery("")}
              className="text-[11px] font-bold"
              style={{ color: c.textFaint }}
            >
              ✕
            </button>
          )}
        </div>
      )}

      {loading ? (
        <div
          className="flex flex-col items-center gap-3 rounded-2xl px-6 py-12 text-center"
          style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
        >
          <p className="animate-pulse text-sm font-semibold" style={{ color: c.textOnBg }}>
            {s.adventure.loading}
          </p>
        </div>
      ) : allWords.length === 0 ? (
        <div
          className="flex flex-col items-center gap-3 rounded-2xl px-6 py-12 text-center"
          style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
        >
          <BookOpen size={40} style={{ color: c.textOnBg }} />
          <p className="text-sm font-semibold" style={{ color: c.textOnBg }}>
            {s.adventure.noWordsYet}
          </p>
        </div>
      ) : words.length === 0 ? (
        <div
          className="flex flex-col items-center gap-3 rounded-2xl px-6 py-12 text-center"
          style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
        >
          <Search size={40} style={{ color: c.textOnBg }} />
          <p className="text-sm font-semibold" style={{ color: c.textOnBg }}>
            {s.adventure.noWordsSearch(query)}
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-2 gap-3 md:grid-cols-3 lg:grid-cols-4">
          {words.map((word) => {
            const tier    = TIER_CONFIG[word.tier] ?? TIER_CONFIG.bronze;
            const dashIdx = word.native.indexOf(" — ");
            const mainMeaning = dashIdx >= 0 ? word.native.slice(0, dashIdx) : word.native;
            const hint        = dashIdx >= 0 ? word.native.slice(dashIdx + 3) : null;

            return (
              <div
                key={word.word_id}
                className="flex flex-col items-center gap-2 rounded-2xl px-3 pb-4 pt-5 text-center"
                style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
              >
                <div
                  className="h-2 w-2 rounded-full"
                  style={{ background: tier.dot, boxShadow: `0 0 8px ${tier.dot}80` }}
                />
                <p className="text-xl font-bold italic leading-tight" style={{ color: c.parchment }}>
                  {word.target}
                </p>
                <p className="text-[13px] font-semibold leading-snug" style={{ color: c.textOnBg }}>
                  {mainMeaning}
                </p>
                {hint && (
                  <p className="text-[10px] leading-snug" style={{ color: c.textFaint }}>
                    {hint}
                  </p>
                )}
                <span
                  className="mt-auto pt-1 rounded-full px-2 py-0.5 text-[9px] font-bold uppercase tracking-wider"
                  style={{
                    background: `${tier.dot}18`,
                    color: tier.dot,
                    border: `1px solid ${tier.dot}35`,
                  }}
                >
                  {tier.label}
                </span>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
