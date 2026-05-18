import { StyleSheet } from "react-native";
import { FONT_SIZE, RADIUS, SPACING, getAdventureColors } from "@linguaflow/shared-core";

const theme = getAdventureColors("ES", "dark");

export const styles = StyleSheet.create({
  backdrop: {
    alignItems: "stretch",
    justifyContent: "flex-end",
    padding: 0,
  },
  panel: {
    borderRadius: 0,
    borderTopLeftRadius: 16,
    borderTopRightRadius: 16,
    gap: SPACING.md,
    padding: SPACING.lg,
    paddingBottom: SPACING["3xl"],
  },
  modalEyebrow: {
    color: theme.parchmentSubtext,
    fontSize: FONT_SIZE.xs,
    fontWeight: "900",
    marginRight: 44,
    textTransform: "uppercase",
  },
  modalTitle: {
    color: theme.parchmentText,
    fontSize: FONT_SIZE["2xl"],
    fontWeight: "900",
    lineHeight: 30,
    marginRight: 44,
  },
  modalFacts: {
    flexDirection: "row",
    gap: SPACING.sm,
  },
  fact: {
    backgroundColor: theme.goldAccentSoft,
    borderColor: theme.parchmentBorder,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    flex: 1,
    gap: 4,
    padding: SPACING.sm,
  },
  factLabel: {
    color: theme.parchmentSubtext,
    fontSize: FONT_SIZE.xs,
    fontWeight: "900",
    textTransform: "uppercase",
  },
  factValue: {
    color: theme.parchmentText,
    fontSize: FONT_SIZE.sm,
    fontWeight: "800",
  },
  keyWords: {
    backgroundColor: theme.goldAccentSoft,
    borderColor: theme.parchmentBorder,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    gap: SPACING.sm,
    padding: SPACING.sm,
  },
  keyWordRow: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 6,
  },
  keyWord: {
    backgroundColor: "rgba(255,255,255,0.55)",
    borderRadius: RADIUS.full,
    color: theme.parchmentText,
    fontSize: FONT_SIZE.xs,
    fontWeight: "800",
    overflow: "hidden",
    paddingHorizontal: SPACING.sm,
    paddingVertical: 4,
  },
  modalAction: {
    backgroundColor: theme.ctaBg,
    borderRadius: RADIUS.sm,
    color: theme.ctaText,
    fontSize: FONT_SIZE.base,
    fontWeight: "900",
    minHeight: 46,
    overflow: "hidden",
    paddingVertical: 13,
    textAlign: "center",
  },
});
