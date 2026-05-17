import { useEffect, useMemo, useState } from "react";

import Emoji from "../../../components/Emoji";

interface CharacterAvatarProps {
  slug?: string;
  emoji?: string;
  name: string;
  langCode?: string;
  size?: number;
  fallbackBg?: string;
  className?: string;
}

const SLUG_IMAGE_ALIASES: Record<string, string[]> = {
  rosa_panadera: ["rosa"],
};

// Images live in public/{langCode}/characters/{slug}.png
// Falls back to emoji → first initial when image is absent or fails to load.
export default function CharacterAvatar({
  slug,
  emoji,
  name,
  langCode = "es",
  size = 40,
  fallbackBg = "#4a3728",
  className = "",
}: CharacterAvatarProps) {
  const [srcIndex, setSrcIndex] = useState(0);
  const imageSources = useMemo(() => {
    if (!slug) return [];
    const lang = langCode.toLowerCase();
    const slugs = [slug, ...(SLUG_IMAGE_ALIASES[slug] ?? [])];
    return slugs.flatMap(imageSlug => [
      `/${lang}/characters/${imageSlug}.png`,
      `/${lang}/characters/${imageSlug}.jpg`,
    ]);
  }, [langCode, slug]);

  useEffect(() => {
    setSrcIndex(0);
  }, [langCode, slug]);

  if (imageSources[srcIndex]) {
    return (
      <img
        src={imageSources[srcIndex]}
        alt={name}
        className={`shrink-0 rounded-full object-cover object-top ${className}`}
        style={{ width: size, height: size }}
        onError={() => setSrcIndex(current => current + 1)}
      />
    );
  }

  return (
    <div
      className={`grid shrink-0 place-items-center rounded-full ${className}`}
      style={{ width: size, height: size, background: fallbackBg }}
    >
      {emoji ? (
        <Emoji char={emoji} size={Math.round(size * 0.55)} />
      ) : (
        <span className="font-bold text-white" style={{ fontSize: size * 0.38 }}>
          {name.charAt(0).toUpperCase()}
        </span>
      )}
    </div>
  );
}
