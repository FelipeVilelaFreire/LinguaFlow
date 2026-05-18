import { Link } from "expo-router";
import { useState } from "react";
import { Pressable, ScrollView, Text, useWindowDimensions, View } from "react-native";
import { getAdventureColors, STRINGS } from "@linguaflow/shared-core";
import type { ApiAdventureChapter, ApiAdventurePhase } from "@linguaflow/shared-core";
import { useAdventureChapters } from "@linguaflow/shared-core/hooks/adventure";
import { AdventurePhaseModal } from "@/src/components/modals";
import type { AdventurePhaseSelection } from "@/src/components/modals";
import { styles } from "./AdventureMapScreen.styles";

const WINDING: Array<{ x: number; y: number }> = [
  { x: 50, y: 70 }, { x: 65, y: 155 }, { x: 78, y: 240 }, { x: 82, y: 325 }, { x: 72, y: 408 },
  { x: 55, y: 493 }, { x: 38, y: 578 }, { x: 24, y: 663 }, { x: 18, y: 748 }, { x: 22, y: 833 },
  { x: 34, y: 918 }, { x: 48, y: 1003 }, { x: 62, y: 1088 }, { x: 76, y: 1173 }, { x: 80, y: 1258 },
  { x: 70, y: 1340 }, { x: 55, y: 1420 }, { x: 40, y: 1500 }, { x: 26, y: 1580 }, { x: 20, y: 1660 },
  { x: 28, y: 1740 }, { x: 40, y: 1820 }, { x: 50, y: 1900 }, { x: 50, y: 1980 }, { x: 50, y: 2050 },
];

const SEASON_HEIGHT = 2120;
const NODE_SIZE = 54;
const BOSS_SIZE = 64;

const TABS: Array<{ href: string; label: string; active?: boolean }> = [
  { href: "/(tabs)/adventure", label: STRINGS.adventure.title },
  { href: "/adventure/map", label: STRINGS.adventure.mapTitle, active: true },
  { href: "/adventure/inventory", label: STRINGS.adventure.inventory },
  { href: "/adventure/chests", label: STRINGS.adventure.chests },
  { href: "/adventure/words", label: STRINGS.adventure.words },
  { href: "/adventure/hero", label: STRINGS.adventure.hero },
  { href: "/adventure/characters", label: STRINGS.adventure.characters },
] as const;

export function AdventureMapScreen() {
  const langCode = "ES";
  const theme = getAdventureColors(langCode, "dark");
  const { chapters, isLoading, error } = useAdventureChapters(langCode);
  const { width } = useWindowDimensions();
  const mapWidth = Math.max(320, width - 28);
  const [selectedPhase, setSelectedPhase] = useState<AdventurePhaseSelection | null>(null);

  if (isLoading) {
    return <State message={STRINGS.adventure.loading} />;
  }

  if (error) {
    return <State message={error} />;
  }

  if (chapters.length === 0) {
    return <State message={STRINGS.adventure.empty} />;
  }

  return (
    <ScrollView style={[styles.container, { backgroundColor: theme.bgFrom }]} contentContainerStyle={styles.content}>
      <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.tabs}>
        {TABS.map((tab) => tab.active ? (
          <Text key={tab.href} style={[styles.tab, styles.activeTab]}>{tab.label}</Text>
        ) : (
          <Link href={tab.href} key={tab.href} style={styles.tab}>{tab.label}</Link>
        ))}
      </ScrollView>

      {chapters.map((chapter, index) => (
        <SeasonMap
          chapter={chapter}
          isUnlocked={index === 0 || chapters[index - 1].phases.every((phase) => phase.is_completed)}
          key={chapter.id}
          mapWidth={mapWidth}
          onSelectPhase={(phase) => setSelectedPhase({ chapter, phase })}
        />
      ))}
      <AdventurePhaseModal selection={selectedPhase} onClose={() => setSelectedPhase(null)} />
    </ScrollView>
  );
}

function SeasonMap({
  chapter,
  isUnlocked,
  mapWidth,
  onSelectPhase,
}: {
  chapter: ApiAdventureChapter;
  isUnlocked: boolean;
  mapWidth: number;
  onSelectPhase: (phase: ApiAdventurePhase) => void;
}) {
  const theme = getAdventureColors(chapter.language_code || "ES", "dark");
  const currentPhase = chapter.progress?.current_phase ?? 1;
  const completed = chapter.phases.filter((phase) => phase.is_completed).length;

  return (
    <View style={styles.season}>
      <View style={styles.seasonHeader}>
        <View style={styles.seasonMeta}>
          <Text style={styles.levelBadge}>{chapter.level}</Text>
          {chapter.subtitle ? <Text style={styles.seasonSubtitle}>{chapter.subtitle}</Text> : null}
        </View>
        <Text style={styles.seasonTitle}>{chapter.title}</Text>
        <Text style={styles.seasonProgress}>
          {isUnlocked ? STRINGS.adventure.phasesCompleted(completed, chapter.phases.length) : STRINGS.adventure.lockedLabel}
        </Text>
      </View>

      <View style={[styles.winding, { height: SEASON_HEIGHT, width: mapWidth }]}>
        <PathLines color={theme.pathColor} width={mapWidth} />
        {chapter.phases.map((phase, phaseIndex) => {
          const position = WINDING[phaseIndex] ?? { x: 50, y: 70 + phaseIndex * 82 };
          const status = getPhaseStatus(phase, currentPhase, isUnlocked);
          return <PhaseNode chapter={chapter} key={phase.id} mapWidth={mapWidth} phase={phase} position={position} status={status} onSelect={() => onSelectPhase(phase)} />;
        })}
      </View>
    </View>
  );
}

function PathLines({ color, width }: { color: string; width: number }) {
  return (
    <>
      {WINDING.slice(0, -1).map((point, index) => {
        const next = WINDING[index + 1];
        const x1 = (point.x / 100) * width;
        const x2 = (next.x / 100) * width;
        const y1 = point.y;
        const y2 = next.y;
        const dx = x2 - x1;
        const dy = y2 - y1;
        const length = Math.sqrt(dx * dx + dy * dy);
        const angle = `${Math.atan2(dy, dx)}rad`;
        return (
          <View
            key={`${point.y}-${next.y}`}
            style={[
              styles.pathLine,
              {
                backgroundColor: color,
                left: x1,
                top: y1,
                transform: [{ rotateZ: angle }],
                width: length,
              },
            ]}
          />
        );
      })}
    </>
  );
}

function PhaseNode({
  chapter,
  mapWidth,
  phase,
  position,
  status,
  onSelect,
}: {
  chapter: ApiAdventureChapter;
  mapWidth: number;
  phase: ApiAdventurePhase;
  position: { x: number; y: number };
  status: "completed" | "current" | "locked";
  onSelect: () => void;
}) {
  const theme = getAdventureColors(chapter.language_code || "ES", "dark");
  const isBoss = phase.is_boss;
  const isReview = phase.phase_type === "review";
  const size = isBoss ? BOSS_SIZE : NODE_SIZE;
  const left = (position.x / 100) * mapWidth - 90;
  const top = position.y - size / 2;
  const nodeContent = (
    <>
      <View
        style={[
          styles.phaseNode,
          { height: size, width: size },
          status === "completed" ? styles.completedNode : null,
          status === "locked" ? styles.lockedNode : null,
          status === "current" ? styles.currentNode : null,
          status === "current" && isBoss ? { backgroundColor: theme.bossColor } : null,
          status === "current" && isReview ? { backgroundColor: theme.goldAccent } : null,
        ]}
      >
        <Text style={styles.nodeGlyph}>{getGlyph(phase, status)}</Text>
      </View>
      <View style={styles.phaseLabel}>
        <Text style={styles.phaseTitle} numberOfLines={2}>{phase.title}</Text>
        <Text style={styles.phaseStatus}>{getStatusLabel(status, phase)}</Text>
      </View>
    </>
  );

  if (status === "locked") {
    return <View style={[styles.phaseWrap, { left, top, width: 180 }]}>{nodeContent}</View>;
  }

  return (
    <Pressable onPress={onSelect} style={[styles.phaseWrap, { left, top, width: 180 }]}>
      {nodeContent}
    </Pressable>
  );
}


function State({ message }: { message: string }) {
  const theme = getAdventureColors("ES", "dark");
  return (
    <View style={[styles.state, { backgroundColor: theme.bgFrom }]}>
      <Text style={[styles.stateText, { color: theme.textOnBg }]}>{message}</Text>
    </View>
  );
}

function getPhaseStatus(phase: ApiAdventurePhase, currentPhase: number, chapterUnlocked: boolean) {
  if (!chapterUnlocked) return "locked";
  if (phase.is_completed) return "completed";
  if (phase.number === currentPhase) return "current";
  return "locked";
}

function getGlyph(phase: ApiAdventurePhase, status: "completed" | "current" | "locked") {
  if (status === "completed") return "âœ“";
  if (status === "locked") return "ðŸ”’";
  if (phase.is_boss) return "â˜ ";
  if (phase.phase_type === "review") return "â†»";
  return String(phase.number);
}

function getStatusLabel(status: "completed" | "current" | "locked", phase: ApiAdventurePhase) {
  if (status === "completed") return STRINGS.adventure.completedLabel;
  if (status === "locked") return STRINGS.adventure.lockedLabel;
  if (phase.is_boss) return STRINGS.adventure.phaseStartBoss;
  if (phase.phase_type === "review") return STRINGS.adventure.phaseStartReview;
  return STRINGS.adventure.sectionLabel((phase.completed_sections ?? 0) + 1, 6);
}
