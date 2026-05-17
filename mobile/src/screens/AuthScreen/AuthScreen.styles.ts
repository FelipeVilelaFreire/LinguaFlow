import { StyleSheet } from "react-native";
import { COLORS, FONT_SIZE, RADIUS, SPACING } from "@linguaflow/shared-core";

export const styles = StyleSheet.create({
  container: {
    backgroundColor: COLORS.white,
    flex: 1,
    justifyContent: "center",
    padding: SPACING.lg,
  },
  logo: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE["3xl"],
    fontWeight: "700",
    textAlign: "center",
  },
  subtitle: {
    color: COLORS.gray500,
    fontSize: FONT_SIZE.sm,
    fontWeight: "500",
    marginBottom: SPACING["2xl"],
    marginTop: SPACING.xs,
    textAlign: "center",
  },
  tabs: {
    backgroundColor: COLORS.gray100,
    borderRadius: RADIUS.md,
    flexDirection: "row",
    gap: SPACING.xs,
    marginBottom: SPACING.md,
    padding: SPACING.xs,
  },
  tab: {
    alignItems: "center",
    borderRadius: RADIUS.sm,
    flex: 1,
    paddingVertical: 10,
  },
  activeTab: {
    backgroundColor: COLORS.white,
  },
  tabText: {
    color: COLORS.gray500,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  activeTabText: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  input: {
    borderColor: COLORS.gray200,
    borderRadius: RADIUS.md,
    borderWidth: 1,
    color: COLORS.gray900,
    fontSize: FONT_SIZE.base,
    marginBottom: SPACING.md,
    minHeight: 50,
    paddingHorizontal: SPACING.md,
  },
  error: {
    backgroundColor: "#fef2f2",
    borderColor: "#fecaca",
    borderRadius: RADIUS.md,
    borderWidth: 1,
    color: "#dc2626",
    fontSize: FONT_SIZE.sm,
    fontWeight: "600",
    marginBottom: SPACING.md,
    padding: SPACING.md,
  },
  submit: {
    alignItems: "center",
    backgroundColor: COLORS.primary,
    borderRadius: RADIUS.md,
    minHeight: 50,
    justifyContent: "center",
  },
  submitText: {
    color: COLORS.white,
    fontSize: FONT_SIZE.base,
    fontWeight: "700",
  },
});
