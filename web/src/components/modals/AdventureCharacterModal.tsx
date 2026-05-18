"use client";

import { getCharacterAvatar, STRINGS } from "@linguaflow/shared-core";
import type { ApiAdventureCharacter } from "@linguaflow/shared-core";
import { CharacterAvatar } from "@/src/components/shared";
import { BaseModal } from "./BaseModal";
import styles from "./AdventureModal.module.css";

export function AdventureCharacterModal({
  character,
  onClose,
}: {
  character: ApiAdventureCharacter;
  onClose: () => void;
}) {
  return (
    <BaseModal closeLabel={STRINGS.actions.close} onClose={onClose} panelClassName={styles.panel}>
      <div className={styles.hero}>
        <CharacterAvatar
          emoji={character.emoji}
          langCode="ES"
          name={character.name}
          size={72}
          slug={character.slug || getCharacterAvatar(character.name)?.slug}
        />
        <div>
          <p>{character.role}</p>
          <h2 className={styles.title}>{character.name}</h2>
          <small>{character.character_type} - {character.is_met ? STRINGS.adventure.met : STRINGS.adventure.undiscovered}</small>
        </div>
      </div>
      {character.quote ? <blockquote className={styles.quote}>{character.quote}</blockquote> : null}
      <p className={styles.description}>{character.description}</p>
      <dl className={styles.facts}>
        <div>
          <dt>{STRINGS.adventure.languageBridge}</dt>
          <dd>{character.lang_bridge ? STRINGS.adventure.yes : STRINGS.adventure.no}</dd>
        </div>
        <div>
          <dt>{STRINGS.adventure.narrativeOrder}</dt>
          <dd>{character.order}</dd>
        </div>
      </dl>
    </BaseModal>
  );
}

