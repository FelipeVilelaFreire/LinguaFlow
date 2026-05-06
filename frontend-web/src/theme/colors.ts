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

export const STUDY_AREA_COLORS: Record<string, StudyAreaColorTokens> = {
  DE: {
    name: "Alemao",
    primary: "#14b8a6",
    primaryDark: "#0f766e",
    primarySoft: "#f0fdfa",
    accent: "#dc2626",
    accentSoft: "#fef2f2",
    page: "#f8fafc",
    textOnPrimary: "#0f172a",
  },
  ES: {
    name: "Espanhol",
    primary: "#111827",
    primaryDark: "#030712",
    primarySoft: "#f1f5f9",
    accent: "#facc15",
    accentSoft: "#fefce8",
    page: "#f8fafc",
    textOnPrimary: "#ffffff",
  },
  EN: {
    name: "Ingles",
    primary: "#1e3a8a",
    primaryDark: "#172554",
    primarySoft: "#f1f5f9",
    accent: "#dc2626",
    accentSoft: "#fef2f2",
    page: "#f8fafc",
    textOnPrimary: "#ffffff",
  },
};

export const FALLBACK_STUDY_AREA_COLORS = STUDY_AREA_COLORS.DE;
