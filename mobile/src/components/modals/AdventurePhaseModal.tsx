import { Link } from "expo-router";
import { Text, View } from "react-native";
import { STRINGS } from "@linguaflow/shared-core";
import type { ApiAdventureChapter, ApiAdventurePhase } from "@linguaflow/shared-core";
import { BaseModal } from "./BaseModal";
import { styles } from "./AdventurePhaseModal.styles";

export type AdventurePhaseSelection = {
  chapter: ApiAdventureChapter;
  phase: ApiAdventurePhase;
};

export function AdventurePhaseModal({ selection, onClose }: { selection: AdventurePhaseSelection | null; onClose: () => void }) {
  if (!selection) {
    return null;
  }

  const { chapter, phase } = selection;
  const href = `/adventure/chapter/${phase.id}?phase=${phase.number}&lang=${chapter.language_code}&words=${encodeURIComponent(phase.key_words.join(","))}` as never;
  const startLabel = phase.is_boss
    ? STRINGS.adventure.phaseStartBoss
    : phase.phase_type === "review"
      ? STRINGS.adventure.phaseStartReview
      : STRINGS.adventure.phaseStart;

  return (
    <BaseModal animationType="slide" visible={Boolean(selection)} onClose={onClose} contentStyle={styles.backdrop} panelStyle={styles.panel}>
      <Text style={styles.modalEyebrow}>{chapter.level} - {STRINGS.adventure.phaseLabel(phase.number)}</Text>
      <Text style={styles.modalTitle}>{phase.title}</Text>
      <View style={styles.modalFacts}>
        <View style={styles.fact}>
          <Text style={styles.factLabel}>{STRINGS.adventure.phaseType}</Text>
          <Text style={styles.factValue}>{phase.phase_type}</Text>
        </View>
        <View style={styles.fact}>
          <Text style={styles.factLabel}>{STRINGS.adventure.sectionLabel((phase.completed_sections ?? 0) + 1, 6)}</Text>
          <Text style={styles.factValue}>{phase.is_completed ? STRINGS.adventure.completedLabel : STRINGS.adventure.currentLabel}</Text>
        </View>
      </View>
      {phase.npc_name ? (
        <View style={styles.fact}>
          <Text style={styles.factLabel}>{STRINGS.adventure.npc}</Text>
          <Text style={styles.factValue}>{phase.npc_name}</Text>
        </View>
      ) : null}
      {phase.key_words.length > 0 ? (
        <View style={styles.keyWords}>
          <Text style={styles.factLabel}>{STRINGS.adventure.keyWords}</Text>
          <View style={styles.keyWordRow}>
            {phase.key_words.map((word) => <Text style={styles.keyWord} key={word}>{word}</Text>)}
          </View>
        </View>
      ) : null}
      <Link href={href} style={styles.modalAction}>
        {startLabel}
      </Link>
    </BaseModal>
  );
}
