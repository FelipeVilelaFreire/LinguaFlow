"use client";

import type { ApiAdventureChapter, ApiAdventurePhase } from "@linguaflow/shared-core";
import { STRINGS } from "@linguaflow/shared-core";
import { Swords } from "lucide-react";
import Link from "next/link";
import { BaseModal } from "./BaseModal";
import styles from "./AdventureModal.module.css";

export function AdventurePhaseModal({
  chapter,
  phase,
  onClose,
}: {
  chapter: ApiAdventureChapter;
  phase: ApiAdventurePhase;
  onClose: () => void;
}) {
  const href = `/aventura/capitulo/${phase.id}?phase=${phase.number}&lang=${chapter.language_code}&words=${encodeURIComponent(phase.key_words.join(","))}`;
  const startLabel = phase.is_boss
    ? STRINGS.adventure.phaseStartBoss
    : phase.phase_type === "review"
      ? STRINGS.adventure.phaseStartReview
      : STRINGS.adventure.phaseStart;

  return (
    <BaseModal closeLabel={STRINGS.actions.close} onClose={onClose} panelClassName={styles.panel}>
      <p className={styles.eyebrow}>{chapter.level} - {STRINGS.adventure.phaseLabel(phase.number)}</p>
      <h2 className={styles.title}>{phase.title}</h2>
      <div className={styles.facts}>
        <span><strong>{STRINGS.adventure.phaseType}</strong>{phase.phase_type}</span>
        <span><strong>{STRINGS.adventure.sectionLabel((phase.completed_sections ?? 0) + 1, 6)}</strong>{phase.is_completed ? STRINGS.adventure.completedLabel : STRINGS.adventure.currentLabel}</span>
        {phase.npc_name ? <span><strong>{STRINGS.adventure.npc}</strong>{phase.npc_name}</span> : null}
      </div>
      {phase.key_words.length > 0 ? (
        <div className={styles.keyWords}>
          <strong>{STRINGS.adventure.keyWords}</strong>
          <div>{phase.key_words.map((word) => <span key={word}>{word}</span>)}</div>
        </div>
      ) : null}
      <Link className={styles.action} href={href}>
        <Swords size={16} />
        {startLabel}
      </Link>
    </BaseModal>
  );
}
