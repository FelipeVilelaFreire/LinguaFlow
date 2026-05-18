import { StyleSheet } from "react-native";
import { COLORS, FONT_SIZE, RADIUS, SPACING, getAdventureColors } from "@linguaflow/shared-core";

const theme = getAdventureColors("ES", "dark");

export const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  content: {
    gap: SPACING.md,
    padding: 14,
    paddingTop: SPACING["3xl"],
  },
  tabs: {
    gap: SPACING.sm,
    paddingBottom: SPACING.xs,
  },
  tab: {
    backgroundColor: theme.surface,
    borderColor: theme.borderFaint,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    color: theme.textOnBg,
    fontSize: FONT_SIZE.sm,
    fontWeight: "800",
    minHeight: 38,
    overflow: "hidden",
    paddingHorizontal: SPACING.md,
    paddingVertical: 9,
  },
  activeTab: {
    backgroundColor: theme.goldAccentSoft,
    borderColor: theme.goldAccent,
    color: theme.parchment,
  },
  state: {
    alignItems: "center",
    flex: 1,
    justifyContent: "center",
    padding: SPACING.lg,
  },
  stateText: {
    fontSize: FONT_SIZE.base,
    fontWeight: "700",
    textAlign: "center",
  },
  season: {
    gap: SPACING.sm,
  },
  seasonHeader: {
    backgroundColor: "rgba(185,28,28,0.2)",
    borderColor: "rgba(185,28,28,0.42)",
    borderRadius: RADIUS.md,
    borderWidth: 1,
    gap: 6,
    marginHorizontal: 4,
    padding: SPACING.md,
  },
  seasonMeta: {
    alignItems: "center",
    flexDirection: "row",
    gap: SPACING.sm,
  },
  levelBadge: {
    backgroundColor: theme.seasonBadgeBg,
    borderRadius: RADIUS.xs,
    color: theme.seasonBadgeText,
    fontSize: FONT_SIZE.xs,
    fontWeight: "900",
    overflow: "hidden",
    paddingHorizontal: 8,
    paddingVertical: 3,
  },
  seasonSubtitle: {
    color: theme.textOnBg,
    flex: 1,
    fontSize: FONT_SIZE.xs,
    fontWeight: "800",
    textTransform: "uppercase",
  },
  seasonTitle: {
    color: theme.parchment,
    fontSize: FONT_SIZE.xl,
    fontWeight: "900",
    lineHeight: 26,
  },
  seasonProgress: {
    color: theme.textOnBg,
    fontSize: FONT_SIZE.xs,
    fontWeight: "800",
  },
  winding: {
    position: "relative",
  },
  pathLine: {
    height: 4,
    opacity: 0.38,
    position: "absolute",
    transformOrigin: "0px 2px",
  },
  phaseWrap: {
    alignItems: "center",
    position: "absolute",
  },
  phaseNode: {
    alignItems: "center",
    backgroundColor: theme.nodeActive,
    borderColor: theme.nodeActive,
    borderRadius: RADIUS.full,
    borderWidth: 3,
    justifyContent: "center",
    shadowColor: theme.nodeActive,
    shadowOpacity: 0.45,
    shadowRadius: 14,
  },
  currentNode: {
    backgroundColor: theme.nodeActive,
  },
  completedNode: {
    backgroundColor: theme.nodeCompleted,
    borderColor: "rgba(5,150,105,0.6)",
  },
  lockedNode: {
    backgroundColor: theme.nodeLocked,
    borderColor: theme.borderFaint,
    opacity: 0.58,
  },
  nodeGlyph: {
    color: COLORS.white,
    fontSize: 18,
    fontWeight: "900",
  },
  phaseLabel: {
    backgroundColor: theme.surface,
    borderColor: theme.borderFaint,
    borderRadius: RADIUS.sm,
    borderWidth: 1,
    gap: 3,
    marginTop: 8,
    maxWidth: 150,
    paddingHorizontal: 8,
    paddingVertical: 7,
  },
  phaseTitle: {
    color: theme.parchment,
    fontSize: FONT_SIZE.xs,
    fontWeight: "900",
    lineHeight: 15,
    textAlign: "center",
  },
  phaseStatus: {
    color: theme.textOnBg,
    fontSize: 10,
    fontWeight: "800",
    textAlign: "center",
  },
});
