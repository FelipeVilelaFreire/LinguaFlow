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
  eyebrow: {
    color: COLORS.primary,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
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
  filters: {
    gap: SPACING.sm,
  },
  filter: {
    backgroundColor: COLORS.gray100,
    borderRadius: RADIUS.sm,
    paddingHorizontal: SPACING.md,
    paddingVertical: 9,
  },
  selected: {
    backgroundColor: COLORS.primaryLight,
  },
  filterText: {
    color: COLORS.gray600,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  selectedText: {
    color: COLORS.primary,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  card: {
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    gap: SPACING.xs,
    padding: SPACING.md,
  },
  cardTitle: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE.lg,
    fontWeight: "700",
  },
  cardDetail: {
    color: COLORS.gray500,
    fontSize: FONT_SIZE.sm,
    fontWeight: "500",
  },
  badge: {
    alignSelf: "flex-start",
    backgroundColor: COLORS.primaryLight,
    borderRadius: RADIUS.full,
    color: COLORS.primary,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
    marginTop: SPACING.xs,
    overflow: "hidden",
    paddingHorizontal: SPACING.sm,
    paddingVertical: 3,
  },
  remove: {
    alignSelf: "flex-start",
    borderColor: "#fecaca",
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    marginTop: SPACING.sm,
    paddingHorizontal: SPACING.md,
    paddingVertical: 8,
  },
  removeText: {
    color: "#dc2626",
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  empty: {
    color: COLORS.gray500,
    fontSize: FONT_SIZE.sm,
    fontWeight: "600",
    paddingVertical: SPACING["3xl"],
    textAlign: "center",
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
});
