import { useState } from "react";

import Emoji from "./Emoji";

interface CharacterAvatarProps {
  slug?: string;
  emoji?: string;
  name: string;
  size?: number;
  fallbackBg?: string;
  className?: string;
}

// Images live in public/characters/{slug}.png
// Falls back to emoji → first initial when image is absent or fails to load.
export default function CharacterAvatar({
  slug,
  emoji,
  name,
  size = 40,
  fallbackBg = "#4a3728",
  className = "",
}: CharacterAvatarProps) {
  const [imgFailed, setImgFailed] = useState(false);

  if (slug && !imgFailed) {
    return (
      <img
        src={`/characters/${slug}.png`}
        alt={name}
        className={`shrink-0 rounded-full object-cover object-top ${className}`}
        style={{ width: size, height: size }}
        onError={() => setImgFailed(true)}
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
