"use client";

import { getCharacterImageCandidates } from "@linguaflow/shared-core";
import { useEffect, useMemo, useState } from "react";
import styles from "./CharacterAvatar.module.css";

export function CharacterAvatar({
  slug,
  emoji,
  name,
  langCode = "es",
  size = 48,
  className = "",
}: {
  slug?: string | null;
  emoji?: string | null;
  name: string;
  langCode?: string;
  size?: number;
  className?: string;
}) {
  const [srcIndex, setSrcIndex] = useState(0);
  const imageSources = useMemo(() => getCharacterImageCandidates({ langCode, slug }), [langCode, slug]);

  useEffect(() => {
    setSrcIndex(0);
  }, [langCode, slug]);

  const src = imageSources[srcIndex];

  if (src) {
    return (
      <img
        alt={name}
        className={`${styles.avatar} ${className}`}
        height={size}
        src={src}
        style={{ height: size, width: size }}
        width={size}
        onError={() => setSrcIndex((current) => current + 1)}
      />
    );
  }

  return (
    <span className={`${styles.fallback} ${className}`} style={{ height: size, width: size }}>
      {emoji || name.charAt(0).toUpperCase()}
    </span>
  );
}
