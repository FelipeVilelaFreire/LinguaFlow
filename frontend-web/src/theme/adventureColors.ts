/**
 * Adventure mode color tokens per language × theme mode.
 * Two modes: "dark" (RPG night default) and "light" (daytime/storybook).
 * Future: drive mode from phase.time_of_day ("dawn"|"day"|"dusk"|"night").
 *
 * Cultural identities:
 *   IT → Roman/Renaissance  (terracotta, parchment, wine)
 *   DE → Germanic/Medieval  (forest teal, amber, iron)
 *   EN → British/Imperial   (royal navy, gold, crimson)
 *   ES → Iberian/Flamenco   (deep red, saffron, dark amber)
 *   FR → Parisian/Royal     (midnight blue, fleur gold, ivory)
 *   JA → Edo/Samurai        (ink black, crimson, sakura)
 */

export type AdventureThemeMode = "dark" | "light";

export interface AdventureColorTokens {
  // Mode-aware neutral overlays (replaces hardcoded rgba in components)
  surface: string;       // subtle tinted surface — "rgba(255,255,255,0.08)" dark / "rgba(0,0,0,0.04)" light
  surfaceMid: string;    // medium overlay — "rgba(0,0,0,0.35)" dark / "rgba(0,0,0,0.06)" light
  textOnBg: string;      // readable body text on bg — "rgba(255,255,255,0.70)" / "rgba(0,0,0,0.60)"
  textFaint: string;     // muted/locked text — "rgba(255,255,255,0.18)" / "rgba(0,0,0,0.28)"
  borderFaint: string;   // barely-visible border — "rgba(255,255,255,0.06)" / "rgba(0,0,0,0.08)"

  // Background gradient
  bgFrom: string;
  bgMid: string;
  bgTo: string;
  ambientGlow: string;

  // Winding road
  pathColor: string;
  pathGlow: string;

  // Phase nodes
  nodeActive: string;
  nodeActiveGlow: string;
  nodeCompleted: string;
  nodeLocked: string;

  // Boss node
  bossColor: string;
  bossGlow: string;

  // Season header badge
  seasonBadgeBg: string;
  seasonBadgeText: string;

  // Parchment panels (narrative text, PhaseSheet)
  parchment: string;
  parchmentBorder: string;
  parchmentText: string;
  parchmentSubtext: string;

  // Accents (XP, stars, keywords)
  goldAccent: string;
  goldAccentSoft: string;

  // CTAs
  ctaBg: string;
  ctaText: string;
  ctaHover: string;
}

// ─── Shared neutral tokens ─────────────────────────────────────────────────────
const DARK_NEUTRAL = {
  surface:      "rgba(255,255,255,0.08)",
  surfaceMid:   "rgba(0,0,0,0.35)",
  textOnBg:     "rgba(255,255,255,0.70)",
  textFaint:    "rgba(255,255,255,0.18)",
  borderFaint:  "rgba(255,255,255,0.06)",
};
const LIGHT_NEUTRAL = {
  surface:      "rgba(0,0,0,0.07)",
  surfaceMid:   "rgba(0,0,0,0.12)",
  textOnBg:     "rgba(0,0,0,0.65)",
  textFaint:    "rgba(0,0,0,0.38)",
  borderFaint:  "rgba(0,0,0,0.14)",
};

// ─── Language palettes ─────────────────────────────────────────────────────────
export const ADVENTURE_COLORS: Record<string, { dark: AdventureColorTokens; light: AdventureColorTokens }> = {

  // ── Italian ──────────────────────────────────────────────────────────────────
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
      bgFrom: "#fdf8f0", bgMid: "#f5e9cf", bgTo: "#fdf8f0",
      ambientGlow: "rgba(180,83,9,0.07)",
      pathColor: "#b45309", pathGlow: "rgba(180,83,9,0.20)",
      nodeActive: "#d97706", nodeActiveGlow: "rgba(217,119,6,0.35)",
      nodeCompleted: "#059669", nodeLocked: "#d9c8a8",
      bossColor: "#7c2d12", bossGlow: "rgba(124,45,18,0.30)",
      seasonBadgeBg: "#b45309", seasonBadgeText: "#faf7f2",
      parchment: "#3d1400", parchmentBorder: "rgba(180,83,9,0.18)",
      parchmentText: "#1c1412", parchmentSubtext: "#78350f",
      goldAccent: "#d97706", goldAccentSoft: "rgba(217,119,6,0.12)",
      ctaBg: "#d97706", ctaText: "#ffffff", ctaHover: "#b45309",
    },
  },

  // ── German ───────────────────────────────────────────────────────────────────
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

  // ── English ───────────────────────────────────────────────────────────────────
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

  // ── Spanish ───────────────────────────────────────────────────────────────────
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

  // ── French ────────────────────────────────────────────────────────────────────
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

  // ── Japanese ──────────────────────────────────────────────────────────────────
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

export function getAdventureColors(
  langCode: string,
  mode: AdventureThemeMode = "dark",
): AdventureColorTokens {
  return ADVENTURE_COLORS[langCode.toUpperCase()]?.[mode] ?? ADVENTURE_COLORS.IT[mode];
}
