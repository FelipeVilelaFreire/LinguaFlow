"use client";

import { STRINGS, adventureService } from "@linguaflow/shared-core";
import type { ApiUserChest, ApiUserInventoryItem } from "@linguaflow/shared-core";
import { useState } from "react";
import { BaseModal } from "./BaseModal";
import styles from "./AdventureModal.module.css";

export type LearnedWord = { word_id: string; target: string; native: string; tier: string };
export type AdventureCollectionDetail =
  | { type: "inventory"; item: ApiUserInventoryItem }
  | { type: "chest"; chest: ApiUserChest }
  | { type: "word"; word: LearnedWord };

export function AdventureCollectionDetailModal({
  detail,
  onClose,
  onRefresh,
}: {
  detail: AdventureCollectionDetail;
  onClose: () => void;
  onRefresh: () => Promise<void>;
}) {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function runAction(action: () => Promise<unknown>) {
    setBusy(true);
    setError(null);
    try {
      await action();
      await onRefresh();
      onClose();
    } catch {
      setError(STRINGS.adventure.actionError);
    } finally {
      setBusy(false);
    }
  }

  const isInventory = detail.type === "inventory";
  const isChest = detail.type === "chest";
  const isWord = detail.type === "word";
  const title = isInventory
    ? detail.item.item.name
    : isChest
      ? STRINGS.adventure.chestTitle(detail.chest.chest_tier)
      : detail.word.target;
  const icon = isInventory ? detail.item.item.emoji : isChest ? "□" : "Aa";
  const description = isInventory
    ? detail.item.item.lore
    : isChest
      ? detail.chest.earned_item?.lore ?? STRINGS.adventure.chestEmptyReward
      : detail.word.native;

  return (
    <BaseModal closeLabel={STRINGS.actions.close} onClose={onClose} panelClassName={styles.panel}>
      <div className={styles.hero}>
        <span className={styles.icon}>{icon}</span>
        <div>
          <p>{STRINGS.adventure.details}</p>
          <h2 className={styles.title}>{title}</h2>
          <small>{isInventory ? detail.item.item.rarity : isChest ? detail.chest.status : detail.word.tier}</small>
        </div>
      </div>
      <p className={styles.description}>{description}</p>
      <dl className={styles.facts}>
        {isInventory ? (
          <>
            <Fact label={STRINGS.adventure.itemAction} value={detail.item.item.action} />
            <Fact label={STRINGS.adventure.itemSource} value={detail.item.item.source_character_name ?? STRINGS.adventure.phaseLabel(detail.item.item.source_phase_number ?? 0)} />
          </>
        ) : null}
        {isChest ? (
          <>
            <Fact label={STRINGS.adventure.chestStatus} value={detail.chest.status} />
            <Fact label={STRINGS.adventure.chestReward} value={detail.chest.earned_item?.name ?? STRINGS.adventure.chestEmptyReward} />
          </>
        ) : null}
        {isWord ? (
          <>
            <Fact label={STRINGS.adventure.wordNative} value={detail.word.native} />
            <Fact label={STRINGS.adventure.wordTier} value={detail.word.tier} />
          </>
        ) : null}
      </dl>
      {error ? <p className={styles.error}>{error}</p> : null}
      {isInventory ? (
        <button className={styles.action} disabled={busy || detail.item.is_used} onClick={() => runAction(() => adventureService.useInventoryItem(detail.item.id))} type="button">
          {detail.item.is_used ? STRINGS.adventure.itemAlreadyUsed : STRINGS.adventure.useItem}
        </button>
      ) : null}
      {isChest ? (
        <button
          className={styles.action}
          disabled={busy || detail.chest.status === "claimed"}
          onClick={() => runAction(() => detail.chest.is_ready ? adventureService.claimChest(detail.chest.id) : adventureService.startChest(detail.chest.id))}
          type="button"
        >
          {detail.chest.status === "claimed" ? STRINGS.adventure.chestAlreadyClaimed : detail.chest.is_ready ? STRINGS.adventure.claimChest : STRINGS.adventure.startChest}
        </button>
      ) : null}
    </BaseModal>
  );
}

function Fact({ label, value }: { label: string; value: string | number }) {
  return (
    <div>
      <dt>{label}</dt>
      <dd>{value}</dd>
    </div>
  );
}
