import { StyleSheet } from "react-native";
import { COLORS, FONT_SIZE, RADIUS, SPACING } from "@linguaflow/shared-core";

export const styles = StyleSheet.create({
  container: {
    backgroundColor: COLORS.white,
    flex: 1,
  },
  content: {
    gap: SPACING.md,
    padding: SPACING.lg,
    paddingTop: SPACING["3xl"],
  },
  title: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE["3xl"],
    fontWeight: "700",
  },
  monthNav: {
    alignItems: "center",
    flexDirection: "row",
    gap: SPACING.sm,
    justifyContent: "space-between",
  },
  monthButton: {
    backgroundColor: COLORS.gray100,
    borderRadius: RADIUS.sm,
    paddingHorizontal: SPACING.md,
    paddingVertical: 9,
  },
  monthButtonText: {
    color: COLORS.gray700,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  monthLabel: {
    color: COLORS.gray600,
    flex: 1,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
    textAlign: "center",
    textTransform: "capitalize",
  },
  stats: {
    flexDirection: "row",
    gap: SPACING.sm,
  },
  metric: {
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    flex: 1,
    padding: SPACING.md,
  },
  metricValue: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE["2xl"],
    fontWeight: "700",
  },
  metricLabel: {
    color: COLORS.gray500,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
  },
  goal: {
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    gap: SPACING.md,
    padding: SPACING.md,
  },
  goalTitle: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE.lg,
    fontWeight: "700",
  },
  days: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 6,
  },
  day: {
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.xs,
    borderWidth: 1,
    color: COLORS.gray500,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
    height: 32,
    overflow: "hidden",
    paddingTop: 7,
    textAlign: "center",
    width: 32,
  },
  planned: {
    backgroundColor: COLORS.primaryLight,
    color: COLORS.primary,
  },
  completed: {
    backgroundColor: COLORS.success,
    borderColor: COLORS.success,
    color: COLORS.white,
  },
  state: {
    color: COLORS.gray500,
    fontSize: FONT_SIZE.sm,
    fontWeight: "600",
    paddingVertical: SPACING["3xl"],
    textAlign: "center",
  },
});
