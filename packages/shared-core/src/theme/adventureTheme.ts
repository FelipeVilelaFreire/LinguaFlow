export type AdventureThemeMode = "dark" | "light";

export interface AdventureColorTokens {
  surface: string;
  surfaceMid: string;
  textOnBg: string;
  textFaint: string;
  borderFaint: string;
  bgFrom: string;
  bgMid: string;
  bgTo: string;
  ambientGlow: string;
  pathColor: string;
  pathGlow: string;
  nodeActive: string;
  nodeActiveGlow: string;
  nodeCompleted: string;
  nodeLocked: string;
  bossColor: string;
  bossGlow: string;
  seasonBadgeBg: string;
  seasonBadgeText: string;
  parchment: string;
  parchmentBorder: string;
  parchmentText: string;
  parchmentSubtext: string;
  goldAccent: string;
  goldAccentSoft: string;
  ctaBg: string;
  ctaText: string;
  ctaHover: string;
}

const DARK_NEUTRAL = {
  surface: "rgba(255,255,255,0.08)",
  surfaceMid: "rgba(0,0,0,0.35)",
  textOnBg: "rgba(255,255,255,0.70)",
  textFaint: "rgba(255,255,255,0.52)",
  borderFaint: "rgba(255,255,255,0.06)",
};

const LIGHT_NEUTRAL = {
  surface: "rgba(0,0,0,0.07)",
  surfaceMid: "rgba(0,0,0,0.12)",
  textOnBg: "rgba(0,0,0,0.65)",
  textFaint: "rgba(0,0,0,0.50)",
  borderFaint: "rgba(0,0,0,0.14)",
};

export const ADVENTURE_COLORS: Record<string, { dark: AdventureColorTokens; light: AdventureColorTokens }> = {
  IT: {
    dark: {
      ...DARK_NEUTRAL,
      bgFrom: "#3d1400", bgMid: "#5c2000", bgTo: "#3d1400",
      ambientGlow: "rgba(180,83,9,0.18)",
      pathColor: "#b45309", pathGlow: "rgba(180,83,9,0.35)",
      nodeActive: "#d97706", nodeActiveGlow: "rgba(217,119,6,0.50)",
      nodeCompleted: "#059669", nodeLocked: "#292524",
      bossColor: "#7c2d12", bossGlow: "rgba(124,45,18,0.55)",
      seasonBadgeBg: "#b45309", seasonBadgeText: "#faf7f2",
      parchment: "#faf3e0", parchmentBorder: "rgba(180,83,9,0.25)",
      parchmentText: "#1c1412", parchmentSubtext: "#78350f",
      goldAccent: "#f59e0b", goldAccentSoft: "rgba(245,158,11,0.15)",
      ctaBg: "#d97706", ctaText: "#ffffff", ctaHover: "#b45309",
    },
    light: {
      ...LIGHT_NEUTRAL,
      bgFrom: "#f8efd5", bgMid: "#f0dba8", bgTo: "#f8efd5",
      ambientGlow: "rgba(180,83,9,0.12)",
      pathColor: "#92400e", pathGlow: "rgba(146,64,14,0.28)",
      nodeActive: "#b45309", nodeActiveGlow: "rgba(180,83,9,0.42)",
      nodeCompleted: "#047857", nodeLocked: "#cdb07a",
      bossColor: "#7c2d12", bossGlow: "rgba(124,45,18,0.35)",
      seasonBadgeBg: "#92400e", seasonBadgeText: "#fdf8f0",
      parchment: "#3d1400", parchmentBorder: "rgba(146,64,14,0.28)",
      parchmentText: "#1c1412", parchmentSubtext: "#78350f",
      goldAccent: "#a05018", goldAccentSoft: "rgba(146,64,14,0.12)",
      ctaBg: "#b45309", ctaText: "#ffffff", ctaHover: "#92400e",
    },
  },
  DE: {
    dark: {
      ...DARK_NEUTRAL,
      bgFrom: "#0a1f1d", bgMid: "#122e2b", bgTo: "#0a1f1d",
      ambientGlow: "rgba(20,184,166,0.16)",
      pathColor: "#0f766e", pathGlow: "rgba(15,118,110,0.35)",
      nodeActive: "#14b8a6", nodeActiveGlow: "rgba(20,184,166,0.50)",
      nodeCompleted: "#059669", nodeLocked: "#0f2421",
      bossColor: "#dc2626", bossGlow: "rgba(220,38,38,0.50)",
      seasonBadgeBg: "#0f766e", seasonBadgeText: "#f0fdfa",
      parchment: "#f0fdfa", parchmentBorder: "rgba(15,118,110,0.25)",
      parchmentText: "#0f172a", parchmentSubtext: "#0f766e",
      goldAccent: "#f59e0b", goldAccentSoft: "rgba(245,158,11,0.15)",
      ctaBg: "#14b8a6", ctaText: "#ffffff", ctaHover: "#0f766e",
    },
    light: {
      ...LIGHT_NEUTRAL,
      bgFrom: "#f0fdfa", bgMid: "#ccfbf1", bgTo: "#f0fdfa",
      ambientGlow: "rgba(20,184,166,0.08)",
      pathColor: "#0f766e", pathGlow: "rgba(15,118,110,0.20)",
      nodeActive: "#0d9488", nodeActiveGlow: "rgba(13,148,136,0.35)",
      nodeCompleted: "#059669", nodeLocked: "#a8d4d0",
      bossColor: "#dc2626", bossGlow: "rgba(220,38,38,0.30)",
      seasonBadgeBg: "#0f766e", seasonBadgeText: "#f0fdfa",
      parchment: "#0a1f1d", parchmentBorder: "rgba(15,118,110,0.20)",
      parchmentText: "#0f172a", parchmentSubtext: "#0f766e",
      goldAccent: "#d97706", goldAccentSoft: "rgba(217,119,6,0.12)",
      ctaBg: "#0d9488", ctaText: "#ffffff", ctaHover: "#0f766e",
    },
  },
  EN: {
    dark: {
      ...DARK_NEUTRAL,
      bgFrom: "#0c1730", bgMid: "#152545", bgTo: "#0c1730",
      ambientGlow: "rgba(30,58,138,0.20)",
      pathColor: "#1e40af", pathGlow: "rgba(30,64,175,0.35)",
      nodeActive: "#3b82f6", nodeActiveGlow: "rgba(59,130,246,0.50)",
      nodeCompleted: "#059669", nodeLocked: "#0f172a",
      bossColor: "#991b1b", bossGlow: "rgba(153,27,27,0.55)",
      seasonBadgeBg: "#1e3a8a", seasonBadgeText: "#eff6ff",
      parchment: "#f0f4ff", parchmentBorder: "rgba(30,58,138,0.20)",
      parchmentText: "#0f172a", parchmentSubtext: "#1e40af",
      goldAccent: "#ca8a04", goldAccentSoft: "rgba(202,138,4,0.15)",
      ctaBg: "#1e3a8a", ctaText: "#ffffff", ctaHover: "#172554",
    },
    light: {
      ...LIGHT_NEUTRAL,
      bgFrom: "#eff6ff", bgMid: "#dbeafe", bgTo: "#eff6ff",
      ambientGlow: "rgba(30,58,138,0.06)",
      pathColor: "#1e40af", pathGlow: "rgba(30,64,175,0.20)",
      nodeActive: "#2563eb", nodeActiveGlow: "rgba(37,99,235,0.35)",
      nodeCompleted: "#059669", nodeLocked: "#bfcfef",
      bossColor: "#991b1b", bossGlow: "rgba(153,27,27,0.30)",
      seasonBadgeBg: "#1e3a8a", seasonBadgeText: "#eff6ff",
      parchment: "#0c1730", parchmentBorder: "rgba(30,58,138,0.15)",
      parchmentText: "#0f172a", parchmentSubtext: "#1e40af",
      goldAccent: "#ca8a04", goldAccentSoft: "rgba(202,138,4,0.12)",
      ctaBg: "#1e40af", ctaText: "#ffffff", ctaHover: "#1e3a8a",
    },
  },
  ES: {
    dark: {
      ...DARK_NEUTRAL,
      bgFrom: "#3d0f00", bgMid: "#5c1a00", bgTo: "#3d0f00",
      ambientGlow: "rgba(185,28,28,0.18)",
      pathColor: "#b91c1c", pathGlow: "rgba(185,28,28,0.35)",
      nodeActive: "#dc2626", nodeActiveGlow: "rgba(220,38,38,0.50)",
      nodeCompleted: "#059669", nodeLocked: "#1c0808",
      bossColor: "#78350f", bossGlow: "rgba(120,53,15,0.55)",
      seasonBadgeBg: "#b91c1c", seasonBadgeText: "#fef2f2",
      parchment: "#fffbeb", parchmentBorder: "rgba(185,28,28,0.20)",
      parchmentText: "#1c0505", parchmentSubtext: "#7f1d1d",
      goldAccent: "#ca8a04", goldAccentSoft: "rgba(202,138,4,0.15)",
      ctaBg: "#b91c1c", ctaText: "#ffffff", ctaHover: "#7f1d1d",
    },
    light: {
      ...LIGHT_NEUTRAL,
      bgFrom: "#fffbeb", bgMid: "#fef3c7", bgTo: "#fffbeb",
      ambientGlow: "rgba(185,28,28,0.07)",
      pathColor: "#b91c1c", pathGlow: "rgba(185,28,28,0.20)",
      nodeActive: "#dc2626", nodeActiveGlow: "rgba(220,38,38,0.35)",
      nodeCompleted: "#059669", nodeLocked: "#f0c8c8",
      bossColor: "#78350f", bossGlow: "rgba(120,53,15,0.30)",
      seasonBadgeBg: "#b91c1c", seasonBadgeText: "#fef2f2",
      parchment: "#3d0f00", parchmentBorder: "rgba(185,28,28,0.15)",
      parchmentText: "#1c0505", parchmentSubtext: "#7f1d1d",
      goldAccent: "#ca8a04", goldAccentSoft: "rgba(202,138,4,0.12)",
      ctaBg: "#b91c1c", ctaText: "#ffffff", ctaHover: "#7f1d1d",
    },
  },
  FR: {
    dark: {
      ...DARK_NEUTRAL,
      bgFrom: "#0a1228", bgMid: "#10193d", bgTo: "#0a1228",
      ambientGlow: "rgba(29,78,216,0.18)",
      pathColor: "#1d4ed8", pathGlow: "rgba(29,78,216,0.35)",
      nodeActive: "#3b82f6", nodeActiveGlow: "rgba(59,130,246,0.50)",
      nodeCompleted: "#059669", nodeLocked: "#0a0f20",
      bossColor: "#ca8a04", bossGlow: "rgba(202,138,4,0.50)",
      seasonBadgeBg: "#1d4ed8", seasonBadgeText: "#eff6ff",
      parchment: "#f5f3ff", parchmentBorder: "rgba(29,78,216,0.18)",
      parchmentText: "#0f0a20", parchmentSubtext: "#1e40af",
      goldAccent: "#ca8a04", goldAccentSoft: "rgba(202,138,4,0.15)",
      ctaBg: "#1d4ed8", ctaText: "#ffffff", ctaHover: "#1e40af",
    },
    light: {
      ...LIGHT_NEUTRAL,
      bgFrom: "#eff6ff", bgMid: "#e0ecff", bgTo: "#eff6ff",
      ambientGlow: "rgba(29,78,216,0.06)",
      pathColor: "#1d4ed8", pathGlow: "rgba(29,78,216,0.20)",
      nodeActive: "#2563eb", nodeActiveGlow: "rgba(37,99,235,0.35)",
      nodeCompleted: "#059669", nodeLocked: "#b8cef0",
      bossColor: "#ca8a04", bossGlow: "rgba(202,138,4,0.30)",
      seasonBadgeBg: "#1d4ed8", seasonBadgeText: "#eff6ff",
      parchment: "#0a1228", parchmentBorder: "rgba(29,78,216,0.15)",
      parchmentText: "#0f0a20", parchmentSubtext: "#1e40af",
      goldAccent: "#ca8a04", goldAccentSoft: "rgba(202,138,4,0.12)",
      ctaBg: "#1d4ed8", ctaText: "#ffffff", ctaHover: "#1e40af",
    },
  },
  JA: {
    dark: {
      ...DARK_NEUTRAL,
      bgFrom: "#1a0a0a", bgMid: "#251212", bgTo: "#1a0a0a",
      ambientGlow: "rgba(190,18,60,0.16)",
      pathColor: "#9f1239", pathGlow: "rgba(159,18,57,0.35)",
      nodeActive: "#be123c", nodeActiveGlow: "rgba(190,18,60,0.50)",
      nodeCompleted: "#059669", nodeLocked: "#140a0a",
      bossColor: "#0e7490", bossGlow: "rgba(14,116,144,0.50)",
      seasonBadgeBg: "#be123c", seasonBadgeText: "#fff1f2",
      parchment: "#fdf4ff", parchmentBorder: "rgba(190,18,60,0.18)",
      parchmentText: "#0f0a0a", parchmentSubtext: "#9f1239",
      goldAccent: "#f472b6", goldAccentSoft: "rgba(244,114,182,0.15)",
      ctaBg: "#be123c", ctaText: "#ffffff", ctaHover: "#9f1239",
    },
    light: {
      ...LIGHT_NEUTRAL,
      bgFrom: "#fff1f2", bgMid: "#ffe4e6", bgTo: "#fff1f2",
      ambientGlow: "rgba(190,18,60,0.07)",
      pathColor: "#9f1239", pathGlow: "rgba(159,18,57,0.20)",
      nodeActive: "#be123c", nodeActiveGlow: "rgba(190,18,60,0.35)",
      nodeCompleted: "#059669", nodeLocked: "#f0c0c8",
      bossColor: "#0e7490", bossGlow: "rgba(14,116,144,0.30)",
      seasonBadgeBg: "#be123c", seasonBadgeText: "#fff1f2",
      parchment: "#1a0a0a", parchmentBorder: "rgba(190,18,60,0.15)",
      parchmentText: "#0f0a0a", parchmentSubtext: "#9f1239",
      goldAccent: "#f472b6", goldAccentSoft: "rgba(244,114,182,0.12)",
      ctaBg: "#be123c", ctaText: "#ffffff", ctaHover: "#9f1239",
    },
  },
};

export function getAdventureColors(langCode: string, mode: AdventureThemeMode = "dark"): AdventureColorTokens {
  return ADVENTURE_COLORS[langCode.toUpperCase()]?.[mode] ?? ADVENTURE_COLORS.ES[mode];
}

export function getAdventureThemeVars(tokens: AdventureColorTokens): Record<string, string> {
  return {
    "--adventure-surface": tokens.surface,
    "--adventure-surface-mid": tokens.surfaceMid,
    "--adventure-text-on-bg": tokens.textOnBg,
    "--adventure-text-faint": tokens.textFaint,
    "--adventure-border-faint": tokens.borderFaint,
    "--adventure-bg-from": tokens.bgFrom,
    "--adventure-bg-mid": tokens.bgMid,
    "--adventure-bg-to": tokens.bgTo,
    "--adventure-ambient-glow": tokens.ambientGlow,
    "--adventure-path": tokens.pathColor,
    "--adventure-path-glow": tokens.pathGlow,
    "--adventure-node-active": tokens.nodeActive,
    "--adventure-node-active-glow": tokens.nodeActiveGlow,
    "--adventure-node-completed": tokens.nodeCompleted,
    "--adventure-node-locked": tokens.nodeLocked,
    "--adventure-boss": tokens.bossColor,
    "--adventure-boss-glow": tokens.bossGlow,
    "--adventure-season-bg": tokens.seasonBadgeBg,
    "--adventure-season-text": tokens.seasonBadgeText,
    "--adventure-parchment": tokens.parchment,
    "--adventure-parchment-border": tokens.parchmentBorder,
    "--adventure-parchment-text": tokens.parchmentText,
    "--adventure-parchment-subtext": tokens.parchmentSubtext,
    "--adventure-gold": tokens.goldAccent,
    "--adventure-gold-soft": tokens.goldAccentSoft,
    "--adventure-cta-bg": tokens.ctaBg,
    "--adventure-cta-text": tokens.ctaText,
    "--adventure-cta-hover": tokens.ctaHover,
  };
}
