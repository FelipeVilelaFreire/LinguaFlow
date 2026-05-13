import { Users } from "lucide-react";
import { useEffect, useState } from "react";

import CharacterAvatar from "../../../components/CharacterAvatar";
import CharacterProfileModal from "../../../components/CharacterProfileModal";
import { getCharacterProfile } from "../../../constants/characterProfiles";
import { useStrings } from "../../../../../contexts/StringsContext";
import { adventureService } from "../../../../../services/adventureService";
import { getAdventureColors } from "../../../theme/adventureColors";
import type { AdventureThemeMode } from "../../../theme/adventureColors";
import type { ApiAdventureCharacter } from "../../../../../types/adventure";

interface AdventurePersonagensScreenProps {
  langCode: string;
  themeMode: AdventureThemeMode;
  chapterSlug?: string;
}

export default function AdventurePersonagensScreen({ langCode, themeMode, chapterSlug }: AdventurePersonagensScreenProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, themeMode);
  const [expanded, setExpanded] = useState<number | null>(null);
  const [characters, setCharacters] = useState<ApiAdventureCharacter[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!chapterSlug) return;
    setLoading(true);
    setError(null);
    adventureService.listCharacters(chapterSlug)
      .then(data => setCharacters(data))
      .catch(() => setError(s.adventure.errorLoading))
      .finally(() => setLoading(false));
  }, [chapterSlug, s.adventure.errorLoading]);

  const met = characters.filter(ch => ch.is_met);
  const expandedChar = characters.find(ch => ch.id === expanded);
  const expandedProfile = expandedChar
    ? {
        ...getCharacterProfile(expandedChar.name),
        name: expandedChar.name,
        role: expandedChar.role,
        description: expandedChar.description || getCharacterProfile(expandedChar.name).description,
        quote: expandedChar.quote,
      }
    : null;

  if (!chapterSlug || loading) {
    return (
      <div className="flex h-full items-center justify-center">
        <p className="animate-pulse text-sm font-semibold" style={{ color: c.textOnBg }}>
          {s.adventure.loading}
        </p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex h-full flex-col items-center justify-center gap-3 px-8 text-center">
        <p className="text-sm font-semibold" style={{ color: c.textOnBg }}>{error}</p>
      </div>
    );
  }

  return (
    <div className="px-4 pb-8 pt-5 md:px-8 md:pt-7">
      <div className="mb-5">
        <p className="text-[10px] font-bold uppercase tracking-[0.22em]" style={{ color: c.textFaint }}>
          {s.adventure.castLabel}
        </p>
        <h2 className="mt-0.5 text-xl font-bold leading-tight md:text-2xl" style={{ color: c.parchment }}>
          {s.adventure.tabPersonagens}
        </h2>
        <p className="mt-1 text-sm" style={{ color: c.textOnBg }}>
          {s.adventure.metCount(met.length)}
        </p>
      </div>

      {met.length > 0 && (
        <div className="grid grid-cols-2 gap-3 md:grid-cols-3 lg:grid-cols-4">
          {met.map(ch => (
            <CharCard
              key={ch.id}
              ch={ch}
              expanded={expanded === ch.id}
              onToggle={() => setExpanded(prev => prev === ch.id ? null : ch.id)}
              c={c}
              langCode={langCode}
              speaksYourLang={s.adventure.speaksYourLang}
            />
          ))}
        </div>
      )}

      {characters.length === 0 && (
        <div
          className="flex flex-col items-center gap-3 rounded-2xl px-6 py-12 text-center"
          style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
        >
          <Users size={40} style={{ color: c.textOnBg }} />
          <p className="text-sm font-semibold" style={{ color: c.textOnBg }}>
            {s.adventure.noCharactersYet}
          </p>
        </div>
      )}

      <CharacterProfileModal
        open={Boolean(expandedChar)}
        character={expandedProfile}
        slug={expandedChar?.slug}
        emoji={expandedChar?.emoji}
        langCode={langCode}
        closeLabel={s.adventure.recapClose}
        c={c}
        onClose={() => setExpanded(null)}
      />
    </div>
  );
}

function CharCard({ ch, expanded, onToggle, c, langCode, speaksYourLang }: {
  ch: ApiAdventureCharacter;
  expanded: boolean;
  onToggle: () => void;
  c: ReturnType<typeof getAdventureColors>;
  langCode: string;
  speaksYourLang: string;
}) {
  return (
    <button
      type="button"
      onClick={onToggle}
      className="flex flex-col items-center gap-2.5 rounded-2xl px-3 pb-4 pt-4 text-center transition active:scale-[0.97]"
      style={{
        background: expanded ? c.surfaceMid : c.surface,
        border: `1px solid ${expanded ? c.nodeActive + "44" : c.borderFaint}`,
        boxShadow: expanded ? `0 0 16px ${c.nodeActiveGlow}30` : "none",
      }}
    >
      <div
        className="relative"
        style={{
          borderRadius: "50%",
          border: `2px solid ${ch.lang_bridge ? c.goldAccent + "70" : c.borderFaint}`,
        }}
      >
        <CharacterAvatar
          slug={ch.slug}
          emoji={ch.emoji}
          name={ch.name}
          langCode={langCode}
          size={64}
          fallbackBg={`${c.goldAccent}22`}
        />
      </div>

      <div className="min-w-0 w-full">
        <p className="truncate text-sm font-bold leading-tight" style={{ color: c.parchment }}>
          {ch.name}
        </p>
        <p className="mt-0.5 truncate text-xs" style={{ color: c.textFaint }}>
          {ch.role}
        </p>
      </div>

      {ch.lang_bridge && (
        <span
          className="rounded-full px-2 py-0.5 text-[9px] font-bold uppercase tracking-wider"
          style={{
            background: `${c.goldAccent}18`,
            color: c.goldAccent,
            border: `1px solid ${c.goldAccent}35`,
          }}
        >
          {speaksYourLang}
        </span>
      )}
    </button>
  );
}
