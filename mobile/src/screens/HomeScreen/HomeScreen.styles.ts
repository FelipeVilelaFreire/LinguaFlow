import { StyleSheet } from "react-native";
import { COLORS, FONT_SIZE, RADIUS, SPACING } from "@linguaflow/shared-core";

export const styles = StyleSheet.create({
  container: {
    backgroundColor: COLORS.white,
    flex: 1,
    gap: SPACING.lg,
    justifyContent: "center",
    padding: SPACING.lg,
  },
  eyebrow: {
    color: COLORS.primary,
    fontSize: FONT_SIZE.sm,
  },
  title: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE["4xl"],
    lineHeight: 42,
  },
  primaryAction: {
    backgroundColor: COLORS.primary,
    borderRadius: RADIUS.md,
    color: COLORS.white,
    minHeight: 48,
    overflow: "hidden",
    paddingHorizontal: SPACING.lg,
    paddingVertical: SPACING.md,
    textAlign: "center",
  },
});
