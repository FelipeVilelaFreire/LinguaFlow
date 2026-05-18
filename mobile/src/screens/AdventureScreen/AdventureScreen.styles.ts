import { StyleSheet } from "react-native";
import { getAdventureColors } from "@linguaflow/shared-core";

const theme = getAdventureColors("ES", "dark");

export const styles = StyleSheet.create({
  container: {
    backgroundColor: theme.bgFrom,
    flex: 1,
  },
  content: {
    gap: 18,
    padding: 20,
    paddingTop: 56,
  },
  hero: {
    gap: 14,
    minHeight: 360,
    justifyContent: "center",
  },
  eyebrow: {
    color: theme.goldAccent,
    fontSize: 12,
    fontWeight: "800",
    textTransform: "uppercase",
  },
  title: {
    color: theme.parchment,
    fontSize: 48,
    fontWeight: "900",
    lineHeight: 48,
  },
  subtitle: {
    color: theme.textOnBg,
    fontSize: 16,
    fontWeight: "600",
    lineHeight: 24,
  },
  primaryAction: {
    alignItems: "center",
    alignSelf: "flex-start",
    backgroundColor: theme.ctaBg,
    borderRadius: 8,
    flexDirection: "row",
    gap: 9,
    minHeight: 48,
    paddingHorizontal: 18,
  },
  primaryText: {
    color: theme.ctaText,
    fontSize: 15,
    fontWeight: "800",
  },
  shortcuts: {
    gap: 10,
    paddingBottom: 28,
  },
  shortcut: {
    alignItems: "center",
    backgroundColor: theme.surface,
    borderColor: theme.borderFaint,
    borderRadius: 8,
    borderWidth: 1,
    flexDirection: "row",
    gap: 10,
    minHeight: 56,
    paddingHorizontal: 14,
  },
  highlightShortcut: {
    backgroundColor: theme.goldAccentSoft,
    borderColor: theme.goldAccent,
  },
  shortcutText: {
    color: theme.textOnBg,
    fontSize: 15,
    fontWeight: "800",
  },
  highlightShortcutText: {
    color: theme.parchment,
    fontSize: 15,
    fontWeight: "800",
  },
});
