import { StyleSheet } from "react-native";
import { FONT_SIZE, RADIUS, SPACING, getAdventureColors } from "@linguaflow/shared-core";

const adventureTheme = getAdventureColors("ES", "dark");

export const styles = StyleSheet.create({
  backdrop: {
    alignItems: "center",
    backgroundColor: adventureTheme.surfaceMid,
    flex: 1,
    justifyContent: "center",
    padding: SPACING.lg,
  },
  panel: {
    backgroundColor: adventureTheme.parchment,
    borderColor: adventureTheme.parchmentBorder,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    gap: SPACING.md,
    padding: SPACING.lg,
    width: "100%",
  },
  closeButton: {
    alignItems: "center",
    backgroundColor: adventureTheme.goldAccentSoft,
    borderColor: adventureTheme.parchmentBorder,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    height: 34,
    justifyContent: "center",
    position: "absolute",
    right: SPACING.md,
    top: SPACING.md,
    width: 34,
    zIndex: 2,
  },
  closeButtonText: {
    color: adventureTheme.parchmentText,
    fontSize: FONT_SIZE.xl,
    fontWeight: "700",
    lineHeight: 24,
  },
});
