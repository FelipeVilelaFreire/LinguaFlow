import { useState } from "react";
import { Pressable, Text, View } from "react-native";
import { STRINGS, adventureService } from "@linguaflow/shared-core";
import type { ApiAdventureCharacter, ApiUserChest, ApiUserInventoryItem } from "@linguaflow/shared-core";
import { BaseModal } from "./BaseModal";
import { styles } from "./AdventureCollectionModals.styles";

export type LearnedWord = { word_id: string; target: string; native: string; tier: string };
export type AdventureCollectionDetail =
  | { type: "inventory"; item: ApiUserInventoryItem }
  | { type: "chest"; chest: ApiUserChest }
  | { type: "word"; word: LearnedWord };

type DetailModalProps = {
  detail: AdventureCollectionDetail | null;
  onClose: () => void;
  onRefresh: () => Promise<void>;
};

export function AdventureCollectionDetailModal({ detail, onClose, onRefresh }: DetailModalProps) {
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

  if (!detail) {
    return null;
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
    <BaseModal visible={Boolean(detail)} onClose={onClose}>
      <View style={styles.modalHero}>
        <Text style={styles.modalEmoji}>{icon}</Text>
        <View style={styles.modalHeroText}>
          <Text style={styles.modalRole}>{STRINGS.adventure.details}</Text>
          <Text style={styles.modalTitle}>{title}</Text>
          <Text style={styles.meta}>{isInventory ? detail.item.item.rarity : isChest ? detail.chest.status : detail.word.tier}</Text>
        </View>
      </View>
      <Text style={styles.modalDescription}>{description}</Text>
      <View style={styles.factGrid}>
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
      </View>
      {error ? <Text style={styles.modalError}>{error}</Text> : null}
      {isInventory ? (
        <Pressable disabled={busy || detail.item.is_used} style={[styles.actionButton, detail.item.is_used ? styles.disabledAction : null]} onPress={() => runAction(() => adventureService.useInventoryItem(detail.item.id))}>
          <Text style={styles.actionButtonText}>{detail.item.is_used ? STRINGS.adventure.itemAlreadyUsed : STRINGS.adventure.useItem}</Text>
        </Pressable>
      ) : null}
      {isChest ? (
        <Pressable disabled={busy || detail.chest.status === "claimed"} style={[styles.actionButton, detail.chest.status === "claimed" ? styles.disabledAction : null]} onPress={() => runAction(() => detail.chest.is_ready ? adventureService.claimChest(detail.chest.id) : adventureService.startChest(detail.chest.id))}>
          <Text style={styles.actionButtonText}>{detail.chest.status === "claimed" ? STRINGS.adventure.chestAlreadyClaimed : detail.chest.is_ready ? STRINGS.adventure.claimChest : STRINGS.adventure.startChest}</Text>
        </Pressable>
      ) : null}
    </BaseModal>
  );
}

export function AdventureCharacterModal({ character, onClose }: { character: ApiAdventureCharacter | null; onClose: () => void }) {
  if (!character) {
    return null;
  }

  return (
    <BaseModal visible={Boolean(character)} onClose={onClose}>
      <View style={styles.modalHero}>
        <Text style={styles.modalEmoji}>{character.emoji}</Text>
        <View style={styles.modalHeroText}>
          <Text style={styles.modalRole}>{character.role}</Text>
          <Text style={styles.modalTitle}>{character.name}</Text>
          <Text style={styles.meta}>{character.character_type} - {character.is_met ? STRINGS.adventure.met : STRINGS.adventure.undiscovered}</Text>
        </View>
      </View>
      {character.quote ? <Text style={styles.quote}>{character.quote}</Text> : null}
      <Text style={styles.modalDescription}>{character.description}</Text>
      <View style={styles.factGrid}>
        <Fact label={STRINGS.adventure.languageBridge} value={character.lang_bridge ? STRINGS.adventure.yes : STRINGS.adventure.no} />
        <Fact label={STRINGS.adventure.narrativeOrder} value={character.order} />
      </View>
    </BaseModal>
  );
}

function Fact({ label, value }: { label: string; value: string | number }) {
  return (
    <View style={styles.fact}>
      <Text style={styles.factLabel}>{label}</Text>
      <Text style={styles.factValue}>{value}</Text>
    </View>
  );
}
