import { StyleSheet } from "react-native";
import { COLORS, FONT_SIZE, SPACING } from "@linguaflow/shared-core";

export const styles = StyleSheet.create({
  container: {
    backgroundColor: COLORS.white,
    flex: 1,
    justifyContent: "center",
    padding: SPACING.lg,
  },
  title: {
    color: COLORS.gray900,
    fontSize: FONT_SIZE["3xl"],
  },
});
