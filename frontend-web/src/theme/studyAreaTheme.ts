import type { CSSProperties } from "react";

import { FALLBACK_STUDY_AREA_COLORS, STUDY_AREA_COLORS } from "./colors";
import type { Goal } from "../types/content";

export interface StudyAreaTheme {
  code: string;
  name: string;
  label: string;
  primary: string;
  primaryDark: string;
  primarySoft: string;
  accent: string;
  accentSoft: string;
  page: string;
  textOnPrimary: string;
}

export function getStudyAreaTheme(goal: Goal | null): StudyAreaTheme {
  const code = goal?.target_language?.code ?? "DE";
  const theme = STUDY_AREA_COLORS[code] ?? FALLBACK_STUDY_AREA_COLORS;
  return {
    code,
    label: `${goal?.source_language?.code ?? "PT"} -> ${code} ${goal?.target_level ?? "A1"}`,
    ...theme,
  };
}

export function getStudyAreaThemeStyle(theme: StudyAreaTheme): CSSProperties {
  return {
    "--area-primary": theme.primary,
    "--area-primary-dark": theme.primaryDark,
    "--area-primary-soft": theme.primarySoft,
    "--area-accent": theme.accent,
    "--area-accent-soft": theme.accentSoft,
    "--area-page": theme.page,
    "--area-text-on-primary": theme.textOnPrimary,
  } as CSSProperties;
}
