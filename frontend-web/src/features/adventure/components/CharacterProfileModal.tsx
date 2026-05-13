import { X } from "lucide-react";
import { useEffect } from "react";

import type { CharacterProfile } from "../constants/characterProfiles";
import type { getAdventureColors } from "../theme/adventureColors";
import CharacterAvatar from "./CharacterAvatar";

type AdventureColors = ReturnType<typeof getAdventureColors>;

interface CharacterProfileModalProps {
  open: boolean;
  character: CharacterProfile | null;
  slug?: string;
  emoji?: string;
  langCode: string;
  closeLabel: string;
  c: AdventureColors;
  onClose: () => void;
}

export default function CharacterProfileModal({
  open,
  character,
  slug,
  emoji,
  langCode,
  closeLabel,
  c,
  onClose,
}: CharacterProfileModalProps) {
  useEffect(() => {
    if (!open) return;
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") onClose();
    };
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [onClose, open]);

  if (!open || !character) return null;

  return (
    <div
      className="fixed inset-0 z-[90] flex items-end justify-center px-3 pb-3 pt-16 md:items-center md:p-6"
      style={{ background: "rgba(0,0,0,0.62)", backdropFilter: "blur(8px)" }}
      role="dialog"
      aria-modal="true"
      aria-labelledby="character-profile-title"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-sm overflow-hidden rounded-2xl md:max-w-md"
        style={{
          background: c.surfaceMid,
          border: `1px solid ${c.borderFaint}`,
          boxShadow: `0 24px 72px ${c.nodeActiveGlow}30`,
          animation: "sheetSlideUp 180ms ease-out both",
        }}
        onClick={event => event.stopPropagation()}
      >
        <div
          className="absolute inset-x-0 top-0 h-24"
          style={{
            background: `linear-gradient(135deg, ${c.goldAccent}33, transparent 68%)`,
          }}
        />

        <button
          type="button"
          aria-label={closeLabel}
          onClick={onClose}
          className="absolute right-3 top-3 z-10 grid h-10 w-10 place-items-center rounded-full transition active:scale-95"
          style={{ background: c.surface, border: `1px solid ${c.borderFaint}`, color: c.parchment }}
        >
          <X size={18} />
        </button>

        <div className="relative flex flex-col items-center px-5 pb-5 pt-7 text-center">
          <div
            className="rounded-full p-1"
            style={{
              border: `2px solid ${c.goldAccent}70`,
              boxShadow: `0 0 22px ${c.goldAccent}24`,
            }}
          >
            <CharacterAvatar
              slug={slug}
              emoji={emoji}
              name={character.name}
              langCode={langCode}
              size={92}
              fallbackBg={`${c.goldAccent}22`}
            />
          </div>

          <h3 id="character-profile-title" className="mt-4 text-xl font-black leading-tight" style={{ color: c.parchment }}>
            {character.name}
          </h3>

          {character.role && (
            <p className="mt-1 text-xs font-bold uppercase tracking-[0.18em]" style={{ color: c.goldAccent }}>
              {character.role}
            </p>
          )}

          <p className="mt-4 text-sm font-medium leading-relaxed" style={{ color: c.textOnBg }}>
            {character.description}
          </p>

          {character.quote && (
            <p
              className="mt-4 w-full rounded-xl px-4 py-3 text-sm font-semibold italic leading-relaxed"
              style={{ background: c.surface, border: `1px solid ${c.borderFaint}`, color: c.parchment }}
            >
              "{character.quote}"
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
