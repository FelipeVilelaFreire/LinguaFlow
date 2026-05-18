import { StyleSheet } from "react-native";
import { COLORS, FONT_SIZE, RADIUS, SPACING, getAdventureColors } from "@linguaflow/shared-core";

const adventureTheme = getAdventureColors("ES", "dark");

export const styles = StyleSheet.create({
  modalHero: {
    alignItems: "center",
    flexDirection: "row",
    gap: SPACING.md,
    paddingRight: 48,
  },
  modalHeroText: {
    flex: 1,
    gap: SPACING.xs,
  },
  modalEmoji: {
    backgroundColor: adventureTheme.goldAccentSoft,
    borderRadius: RADIUS.sm,
    fontSize: 34,
    height: 64,
    overflow: "hidden",
    paddingTop: 11,
    textAlign: "center",
    width: 64,
  },
  modalRole: {
    color: adventureTheme.parchmentSubtext,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  modalTitle: {
    color: adventureTheme.parchmentText,
    fontSize: FONT_SIZE["2xl"],
    fontWeight: "700",
  },
  meta: {
    color: adventureTheme.textFaint,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
    textTransform: "uppercase",
  },
  quote: {
    borderLeftColor: adventureTheme.goldAccent,
    borderLeftWidth: 3,
    color: adventureTheme.parchmentText,
    fontSize: FONT_SIZE.base,
    fontWeight: "700",
    lineHeight: 24,
    paddingLeft: SPACING.md,
  },
  modalDescription: {
    color: adventureTheme.parchmentText,
    fontSize: FONT_SIZE.base,
    lineHeight: 24,
  },
  factGrid: {
    flexDirection: "row",
    gap: SPACING.sm,
  },
  fact: {
    backgroundColor: adventureTheme.goldAccentSoft,
    borderColor: adventureTheme.parchmentBorder,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    flex: 1,
    gap: SPACING.xs,
    padding: SPACING.md,
  },
  factLabel: {
    color: adventureTheme.parchmentSubtext,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
    textTransform: "uppercase",
  },
  factValue: {
    color: adventureTheme.parchmentText,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  modalError: {
    color: COLORS.error,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  actionButton: {
    alignItems: "center",
    backgroundColor: adventureTheme.goldAccent,
    borderRadius: RADIUS.sm,
    justifyContent: "center",
    minHeight: 42,
    paddingHorizontal: SPACING.lg,
  },
  disabledAction: {
    opacity: 0.55,
  },
  actionButtonText: {
    color: adventureTheme.bgTo,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
});
