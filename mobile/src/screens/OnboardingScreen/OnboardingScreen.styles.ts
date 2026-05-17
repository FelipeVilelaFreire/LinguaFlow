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
  progress: {
    color: COLORS.gray400,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
    textAlign: "right",
  },
  title: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE["3xl"],
    fontWeight: "700",
  },
  subtitle: {
    color: COLORS.gray500,
    fontSize: FONT_SIZE.sm,
    fontWeight: "500",
  },
  label: {
    color: COLORS.gray400,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
    marginTop: SPACING.sm,
    textTransform: "uppercase",
  },
  card: {
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    gap: SPACING.xs,
    padding: SPACING.md,
  },
  selected: {
    backgroundColor: COLORS.primaryLight,
    borderColor: COLORS.primary,
  },
  cardTitle: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE.base,
    fontWeight: "700",
  },
  cardDetail: {
    color: COLORS.gray500,
    fontSize: FONT_SIZE.sm,
    fontWeight: "500",
  },
  dayGrid: {
    flexDirection: "row",
    gap: SPACING.xs,
  },
  day: {
    alignItems: "center",
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    flex: 1,
    minHeight: 42,
    justifyContent: "center",
  },
  dayText: {
    color: COLORS.gray600,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
  },
  selectedText: {
    color: COLORS.primary,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
  },
  sessionGrid: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: SPACING.sm,
  },
  session: {
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    paddingHorizontal: SPACING.md,
    paddingVertical: 10,
  },
  footer: {
    flexDirection: "row",
    gap: SPACING.sm,
    marginTop: SPACING.lg,
  },
  back: {
    alignItems: "center",
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    justifyContent: "center",
    paddingHorizontal: SPACING.md,
  },
  backText: {
    color: COLORS.gray600,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  submit: {
    alignItems: "center",
    backgroundColor: COLORS.primary,
    borderRadius: RADIUS.sm,
    flex: 1,
    justifyContent: "center",
    minHeight: 50,
  },
  submitText: {
    color: COLORS.white,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
});
