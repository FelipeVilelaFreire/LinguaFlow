import { StyleSheet } from "react-native";
import { FONT_SIZE, RADIUS, SPACING, getAdventureColors } from "@linguaflow/shared-core";

const adventureTheme = getAdventureColors("ES", "dark");

export const styles = StyleSheet.create({
  container: {
    backgroundColor: adventureTheme.bgFrom,
    flex: 1,
  },
  content: {
    gap: SPACING.md,
    padding: SPACING.lg,
    paddingTop: SPACING["3xl"],
  },
  tabs: {
    gap: SPACING.sm,
    paddingBottom: SPACING.xs,
  },
  tab: {
    backgroundColor: adventureTheme.surface,
    borderRadius: RADIUS.sm,
    color: adventureTheme.textOnBg,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
    minHeight: 38,
    overflow: "hidden",
    paddingHorizontal: SPACING.md,
    paddingVertical: 9,
  },
  activeTab: {
    backgroundColor: adventureTheme.goldAccentSoft,
    color: adventureTheme.parchment,
  },
  header: {
    alignItems: "flex-end",
    flexDirection: "row",
    gap: SPACING.md,
    justifyContent: "space-between",
    marginBottom: SPACING.md,
  },
  headerText: {
    flex: 1,
  },
  eyebrow: {
    color: adventureTheme.goldAccent,
    fontSize: FONT_SIZE.sm,
    fontWeight: "700",
  },
  title: {
    color: adventureTheme.parchment,
    fontSize: FONT_SIZE["3xl"],
    fontWeight: "700",
  },
  subtitle: {
    color: adventureTheme.textOnBg,
    fontSize: FONT_SIZE.sm,
    fontWeight: "500",
    marginTop: SPACING.xs,
  },
  count: {
    color: adventureTheme.goldAccent,
    fontSize: FONT_SIZE["2xl"],
    fontWeight: "700",
  },
  card: {
    alignItems: "flex-start",
    backgroundColor: adventureTheme.surface,
    borderColor: adventureTheme.borderFaint,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    flexDirection: "row",
    gap: SPACING.md,
    padding: SPACING.md,
  },
  pressableCard: {
    backgroundColor: adventureTheme.surface,
  },
  pressedCard: {
    borderColor: adventureTheme.goldAccent,
    transform: [{ translateY: 1 }],
  },
  emoji: {
    backgroundColor: adventureTheme.goldAccentSoft,
    borderRadius: RADIUS.sm,
    fontSize: 24,
    height: 42,
    overflow: "hidden",
    paddingTop: 7,
    textAlign: "center",
    width: 42,
  },
  cardText: {
    flex: 1,
    gap: SPACING.xs,
  },
  cardTitle: {
    color: adventureTheme.parchment,
    fontSize: FONT_SIZE.base,
    fontWeight: "700",
  },
  cardDetail: {
    color: adventureTheme.textOnBg,
    fontSize: FONT_SIZE.sm,
  },
  meta: {
    color: adventureTheme.textFaint,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
    textTransform: "uppercase",
  },
  wordRow: {
    backgroundColor: adventureTheme.surface,
    borderColor: adventureTheme.borderFaint,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    gap: SPACING.xs,
    padding: SPACING.md,
  },
  wordTarget: {
    color: adventureTheme.parchment,
    fontSize: FONT_SIZE.base,
    fontWeight: "700",
  },
  wordNative: {
    color: adventureTheme.textOnBg,
    fontSize: FONT_SIZE.sm,
  },
  metricGrid: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: SPACING.md,
  },
  metric: {
    backgroundColor: adventureTheme.surface,
    borderColor: adventureTheme.borderFaint,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    flexBasis: "47%",
    flexGrow: 1,
    gap: SPACING.xs,
    padding: SPACING.md,
  },
  metricLabel: {
    color: adventureTheme.textOnBg,
    fontSize: FONT_SIZE.sm,
    fontWeight: "600",
  },
  metricValue: {
    color: adventureTheme.parchment,
    fontSize: FONT_SIZE["2xl"],
    fontWeight: "700",
  },
  chestBoard: {
    gap: SPACING.md,
  },
  chestSummary: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: SPACING.sm,
  },
  chestSectionHeader: {
    alignItems: "center",
    flexDirection: "row",
    justifyContent: "space-between",
    marginTop: SPACING.sm,
  },
  chestSectionTitle: {
    color: adventureTheme.parchment,
    fontSize: FONT_SIZE.base,
    fontWeight: "700",
  },
  chestSectionMeta: {
    backgroundColor: adventureTheme.surfaceMid,
    borderColor: adventureTheme.borderFaint,
    borderRadius: RADIUS.full,
    borderWidth: 1,
    color: adventureTheme.textOnBg,
    fontSize: FONT_SIZE.xs,
    fontWeight: "700",
    overflow: "hidden",
    paddingHorizontal: SPACING.sm,
    paddingVertical: 4,
  },
  emptyChestSlot: {
    alignItems: "center",
    backgroundColor: adventureTheme.surface,
    borderColor: adventureTheme.borderFaint,
    borderRadius: RADIUS.sm,
    borderStyle: "dashed",
    borderWidth: 1,
    gap: SPACING.xs,
    justifyContent: "center",
    minHeight: 118,
    padding: SPACING.md,
  },
  emptyChestIcon: {
    color: adventureTheme.goldAccent,
    fontSize: 34,
  },
  chestCard: {
    borderColor: adventureTheme.goldAccentSoft,
  },
  chestProgress: {
    backgroundColor: adventureTheme.surfaceMid,
    borderRadius: RADIUS.full,
    height: 7,
    marginTop: SPACING.xs,
    overflow: "hidden",
    width: "100%",
  },
  chestProgressFill: {
    backgroundColor: adventureTheme.goldAccent,
    borderRadius: RADIUS.full,
    height: "100%",
  },
  state: {
    color: adventureTheme.textOnBg,
    fontSize: FONT_SIZE.base,
    fontWeight: "600",
    paddingVertical: SPACING["3xl"],
    textAlign: "center",
  },
});
