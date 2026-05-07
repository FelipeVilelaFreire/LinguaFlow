/**
 * Adventure mode color tokens per language.
 * These are distinct from STUDY_AREA_COLORS — they define the immersive,
 * dark RPG atmosphere of the adventure module, not the light app UI.
 *
 * Each language gets a cultural identity:
 *   IT → Roman/Renaissance  (terracotta, parchment, wine)
 *   DE → Germanic/Medieval  (forest teal, amber, iron)
 *   EN → British/Imperial   (royal navy, gold, crimson)
 *   ES → Iberian/Flamenco   (deep red, saffron, dark amber)
 *   FR → Parisian/Royal     (midnight blue, fleur gold, ivory)
 *   JA → Edo/Samurai        (ink black, crimson, sakura)
 */

export interface AdventureColorTokens {
  // Dark immersive background
  bgFrom: string;
  bgMid: string;
  bgTo: string;
  ambientGlow: string;       // radial overlay color (rgba)

  // Winding road / path
  pathColor: string;
  pathGlow: string;          // rgba for path shadow

  // Phase nodes
  nodeActive: string;        // current phase — fill
  nodeActiveGlow: string;    // rgba for pulse ring glow
  nodeCompleted: string;     // done phases
  nodeLocked: string;        // not yet unlocked

  // Boss node (season finale)
  bossColor: string;
  bossGlow: string;          // rgba

  // Season header badge
  seasonBadgeBg: string;
  seasonBadgeText: string;

  // Light parchment surface (narrative text panels)
  parchment: string;
  parchmentBorder: string;
  parchmentText: string;
  parchmentSubtext: string;

  // Accent highlights (XP, stars, labels)
  goldAccent: string;
  goldAccentSoft: string;    // rgba

  // CTAs inside the adventure module
  ctaBg: string;
  ctaText: string;
  ctaHover: string;
}

export const ADVENTURE_COLORS: Record<string, AdventureColorTokens> = {

  // ── Italian: Roman ruins, warm parchment, terracotta ────────────────────
  IT: {
    bgFrom:           "#1a0800",
    bgMid:            "#2d1200",
    bgTo:             "#1a0a00",
    ambientGlow:      "rgba(180,83,9,0.12)",

    pathColor:        "#b45309",
    pathGlow:         "rgba(180,83,9,0.35)",

    nodeActive:       "#d97706",
    nodeActiveGlow:   "rgba(217,119,6,0.50)",
    nodeCompleted:    "#059669",
    nodeLocked:       "#292524",

    bossColor:        "#7c2d12",
    bossGlow:         "rgba(124,45,18,0.55)",

    seasonBadgeBg:    "#b45309",
    seasonBadgeText:  "#faf7f2",

    parchment:        "#faf3e0",
    parchmentBorder:  "rgba(180,83,9,0.25)",
    parchmentText:    "#1c1412",
    parchmentSubtext: "#78350f",

    goldAccent:       "#f59e0b",
    goldAccentSoft:   "rgba(245,158,11,0.15)",

    ctaBg:            "#d97706",
    ctaText:          "#ffffff",
    ctaHover:         "#b45309",
  },

  // ── German: dark forest, teal steel, amber torchlight ───────────────────
  DE: {
    bgFrom:           "#040d0c",
    bgMid:            "#0a1a18",
    bgTo:             "#040d0c",
    ambientGlow:      "rgba(20,184,166,0.10)",

    pathColor:        "#0f766e",
    pathGlow:         "rgba(15,118,110,0.35)",

    nodeActive:       "#14b8a6",
    nodeActiveGlow:   "rgba(20,184,166,0.50)",
    nodeCompleted:    "#059669",
    nodeLocked:       "#0f2421",

    bossColor:        "#dc2626",
    bossGlow:         "rgba(220,38,38,0.50)",

    seasonBadgeBg:    "#0f766e",
    seasonBadgeText:  "#f0fdfa",

    parchment:        "#f0fdfa",
    parchmentBorder:  "rgba(15,118,110,0.25)",
    parchmentText:    "#0f172a",
    parchmentSubtext: "#0f766e",

    goldAccent:       "#f59e0b",
    goldAccentSoft:   "rgba(245,158,11,0.15)",

    ctaBg:            "#14b8a6",
    ctaText:          "#0f172a",
    ctaHover:         "#0f766e",
  },

  // ── English: royal navy, gold crowns, crimson ───────────────────────────
  EN: {
    bgFrom:           "#050b1a",
    bgMid:            "#0c1635",
    bgTo:             "#050b1a",
    ambientGlow:      "rgba(30,58,138,0.14)",

    pathColor:        "#1e40af",
    pathGlow:         "rgba(30,64,175,0.35)",

    nodeActive:       "#3b82f6",
    nodeActiveGlow:   "rgba(59,130,246,0.50)",
    nodeCompleted:    "#059669",
    nodeLocked:       "#0f172a",

    bossColor:        "#991b1b",
    bossGlow:         "rgba(153,27,27,0.55)",

    seasonBadgeBg:    "#1e3a8a",
    seasonBadgeText:  "#eff6ff",

    parchment:        "#f0f4ff",
    parchmentBorder:  "rgba(30,58,138,0.20)",
    parchmentText:    "#0f172a",
    parchmentSubtext: "#1e40af",

    goldAccent:       "#ca8a04",
    goldAccentSoft:   "rgba(202,138,4,0.15)",

    ctaBg:            "#1e3a8a",
    ctaText:          "#ffffff",
    ctaHover:         "#172554",
  },

  // ── Spanish: Iberian passion, deep red, saffron gold ────────────────────
  ES: {
    bgFrom:           "#1c0500",
    bgMid:            "#2d0a00",
    bgTo:             "#1c0500",
    ambientGlow:      "rgba(185,28,28,0.12)",

    pathColor:        "#b91c1c",
    pathGlow:         "rgba(185,28,28,0.35)",

    nodeActive:       "#dc2626",
    nodeActiveGlow:   "rgba(220,38,38,0.50)",
    nodeCompleted:    "#059669",
    nodeLocked:       "#1c0808",

    bossColor:        "#78350f",
    bossGlow:         "rgba(120,53,15,0.55)",

    seasonBadgeBg:    "#b91c1c",
    seasonBadgeText:  "#fef2f2",

    parchment:        "#fffbeb",
    parchmentBorder:  "rgba(185,28,28,0.20)",
    parchmentText:    "#1c0505",
    parchmentSubtext: "#7f1d1d",

    goldAccent:       "#ca8a04",
    goldAccentSoft:   "rgba(202,138,4,0.15)",

    ctaBg:            "#b91c1c",
    ctaText:          "#ffffff",
    ctaHover:         "#7f1d1d",
  },

  // ── French: Parisian midnight, fleur-de-lis blue, ivory ─────────────────
  FR: {
    bgFrom:           "#040816",
    bgMid:            "#080f2a",
    bgTo:             "#040816",
    ambientGlow:      "rgba(29,78,216,0.12)",

    pathColor:        "#1d4ed8",
    pathGlow:         "rgba(29,78,216,0.35)",

    nodeActive:       "#3b82f6",
    nodeActiveGlow:   "rgba(59,130,246,0.50)",
    nodeCompleted:    "#059669",
    nodeLocked:       "#0a0f20",

    bossColor:        "#ca8a04",
    bossGlow:         "rgba(202,138,4,0.50)",

    seasonBadgeBg:    "#1d4ed8",
    seasonBadgeText:  "#eff6ff",

    parchment:        "#f5f3ff",
    parchmentBorder:  "rgba(29,78,216,0.18)",
    parchmentText:    "#0f0a20",
    parchmentSubtext: "#1e40af",

    goldAccent:       "#ca8a04",
    goldAccentSoft:   "rgba(202,138,4,0.15)",

    ctaBg:            "#1d4ed8",
    ctaText:          "#ffffff",
    ctaHover:         "#1e40af",
  },

  // ── Japanese: Edo ink, crimson torii, sakura ─────────────────────────────
  JA: {
    bgFrom:           "#0a0505",
    bgMid:            "#12080a",
    bgTo:             "#0a0505",
    ambientGlow:      "rgba(190,18,60,0.10)",

    pathColor:        "#9f1239",
    pathGlow:         "rgba(159,18,57,0.35)",

    nodeActive:       "#be123c",
    nodeActiveGlow:   "rgba(190,18,60,0.50)",
    nodeCompleted:    "#059669",
    nodeLocked:       "#140a0a",

    bossColor:        "#0e7490",
    bossGlow:         "rgba(14,116,144,0.50)",

    seasonBadgeBg:    "#be123c",
    seasonBadgeText:  "#fff1f2",

    parchment:        "#fdf4ff",
    parchmentBorder:  "rgba(190,18,60,0.18)",
    parchmentText:    "#0f0a0a",
    parchmentSubtext: "#9f1239",

    goldAccent:       "#f472b6",
    goldAccentSoft:   "rgba(244,114,182,0.15)",

    ctaBg:            "#be123c",
    ctaText:          "#ffffff",
    ctaHover:         "#9f1239",
  },
};

export const FALLBACK_ADVENTURE_COLORS = ADVENTURE_COLORS.IT;

export function getAdventureColors(langCode: string): AdventureColorTokens {
  return ADVENTURE_COLORS[langCode.toUpperCase()] ?? FALLBACK_ADVENTURE_COLORS;
}
