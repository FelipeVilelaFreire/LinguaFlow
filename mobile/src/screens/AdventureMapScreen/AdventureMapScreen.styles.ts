import { StyleSheet } from "react-native";
import { COLORS, FONT_SIZE, RADIUS, SPACING } from "@linguaflow/shared-core";

export const styles = StyleSheet.create({
  container: {
    backgroundColor: COLORS.white,
    flex: 1,
  },
  content: {
    gap: SPACING.lg,
    padding: SPACING.lg,
    paddingTop: SPACING["3xl"],
  },
  tabs: {
    gap: SPACING.sm,
    paddingBottom: SPACING.xs,
  },
  tab: {
    backgroundColor: COLORS.gray100,
    borderRadius: RADIUS.sm,
    color: COLORS.gray600,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
    minHeight: 38,
    overflow: "hidden",
    paddingHorizontal: SPACING.md,
    paddingVertical: 9,
  },
  activeTab: {
    backgroundColor: COLORS.primaryLight,
    color: COLORS.primary,
  },
  state: {
    alignItems: "center",
    backgroundColor: COLORS.white,
    flex: 1,
    justifyContent: "center",
    padding: SPACING.lg,
  },
  stateText: {
    color: COLORS.gray600,
    fontSize: FONT_SIZE.base,
  },
  title: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE["3xl"],
  },
  chapter: {
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.xl,
    borderWidth: 1,
    gap: SPACING.md,
    padding: SPACING.lg,
  },
  chapterTitle: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE.xl,
  },
  phase: {
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.md,
    borderWidth: 1,
    gap: SPACING.xs,
    padding: SPACING.md,
  },
  phaseTitle: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE.base,
  },
  phaseSubtitle: {
    color: COLORS.gray600,
    fontSize: FONT_SIZE.sm,
  },
});
