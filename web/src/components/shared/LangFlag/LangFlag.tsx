"use client";

import { getFlagImage, STRINGS, type FlagSize } from "@linguaflow/shared-core";
import styles from "./LangFlag.module.css";

export function LangFlag({ code, size = "md", className = "" }: { code: string; size?: FlagSize; className?: string }) {
  const flag = getFlagImage(code, size);

  return (
    <img
      alt={STRINGS.onboarding.flagAlt(code)}
      className={`${styles.flag} ${className}`}
      height={flag.height}
      src={flag.src}
      srcSet={flag.srcSet}
      style={{
        borderRadius: flag.radius,
        height: flag.height,
        width: flag.width,
      }}
      width={flag.width}
      onError={(event) => {
        event.currentTarget.style.display = "none";
      }}
    />
  );
}
