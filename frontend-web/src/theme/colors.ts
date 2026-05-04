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
    primary: "#111827",
    primaryDark: "#030712",
    primarySoft: "#fef3c7",
    accent: "#dc2626",
    accentSoft: "#fee2e2",
    page: "#f8fafc",
    textOnPrimary: "#ffffff",
  },
  ES: {
    name: "Espanhol",
    primary: "#dc2626",
    primaryDark: "#991b1b",
    primarySoft: "#fee2e2",
    accent: "#facc15",
    accentSoft: "#fef9c3",
    page: "#fff7ed",
    textOnPrimary: "#ffffff",
  },
  EN: {
    name: "Ingles",
    primary: "#2563eb",
    primaryDark: "#1e3a8a",
    primarySoft: "#dbeafe",
    accent: "#dc2626",
    accentSoft: "#fee2e2",
    page: "#f8fafc",
    textOnPrimary: "#ffffff",
  },
};

export const FALLBACK_STUDY_AREA_COLORS = STUDY_AREA_COLORS.DE;
