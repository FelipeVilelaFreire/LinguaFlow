import type { Goal } from "../types/content";

export interface StudyAreaColorTokens {
  name: string;
  primary: string;
  primaryDark: string;
  primarySoft: string;
  accent: string;
  accentSoft: string;
  page: string;
  textOnPrimary: string;
}

export interface StudyAreaTheme extends StudyAreaColorTokens {
  code: string;
  label: string;
}

export const STUDY_AREA_COLORS: Record<string, StudyAreaColorTokens> = {
  DE: {
    name: "Alemao",
    primary: "#14b8a6",
    primaryDark: "#0f766e",
    primarySoft: "#f0fdfa",
    accent: "#dc2626",
    accentSoft: "#fef2f2",
    page: "#f8fafc",
    textOnPrimary: "#ffffff",
  },
  IT: {
    name: "Italiano",
    primary: "#c2410c",
    primaryDark: "#9a3412",
    primarySoft: "#fff7ed",
    accent: "#ca8a04",
    accentSoft: "#fefce8",
    page: "#fffbf5",
    textOnPrimary: "#ffffff",
  },
  ES: {
    name: "Espanhol",
    primary: "#b91c1c",
    primaryDark: "#7f1d1d",
    primarySoft: "#fef2f2",
    accent: "#ca8a04",
    accentSoft: "#fefce8",
    page: "#fffbf5",
    textOnPrimary: "#ffffff",
  },
  EN: {
    name: "Ingles",
    primary: "#1e3a8a",
    primaryDark: "#172554",
    primarySoft: "#eff6ff",
    accent: "#dc2626",
    accentSoft: "#fef2f2",
    page: "#f8fafc",
    textOnPrimary: "#ffffff",
  },
  FR: {
    name: "Frances",
    primary: "#1d4ed8",
    primaryDark: "#1e40af",
    primarySoft: "#eff6ff",
    accent: "#ca8a04",
    accentSoft: "#fefce8",
    page: "#f8fafc",
    textOnPrimary: "#ffffff",
  },
  JA: {
    name: "Japones",
    primary: "#be123c",
    primaryDark: "#9f1239",
    primarySoft: "#fff1f2",
    accent: "#0e7490",
    accentSoft: "#ecfeff",
    page: "#fafafa",
    textOnPrimary: "#ffffff",
  },
};

export const FALLBACK_STUDY_AREA_COLORS = STUDY_AREA_COLORS.DE;

export function getStudyAreaTheme(goal: Goal | null | undefined): StudyAreaTheme {
  const code = goal?.target_language?.code?.toUpperCase() ?? "DE";
  const theme = STUDY_AREA_COLORS[code] ?? FALLBACK_STUDY_AREA_COLORS;

  return {
    code,
    label: `${goal?.source_language?.code ?? "PT"} -> ${code} ${goal?.target_level ?? "A1"}`,
    ...theme,
  };
}

export function getStudyAreaThemeVars(theme: StudyAreaTheme): Record<string, string> {
  return {
    "--area-primary": theme.primary,
    "--area-primary-dark": theme.primaryDark,
    "--area-primary-soft": theme.primarySoft,
    "--area-accent": theme.accent,
    "--area-accent-soft": theme.accentSoft,
    "--area-page": theme.page,
    "--area-text-on-primary": theme.textOnPrimary,
  };
}
