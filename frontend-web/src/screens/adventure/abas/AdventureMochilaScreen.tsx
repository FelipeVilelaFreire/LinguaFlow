import { Backpack, X } from "lucide-react";
import { useEffect, useState } from "react";

import { useStrings } from "../../../contexts/StringsContext";
import { adventureService } from "../../../services/adventureService";
import { getAdventureColors } from "../../../theme/adventureColors";
import type { AdventureThemeMode } from "../../../theme/adventureColors";
import Emoji from "../../../components/Emoji";
import type { ApiAdventureItem, ApiUserInventoryItem, ItemRarity } from "../../../types/adventure";

interface AdventureMochilaScreenProps {
  langCode: string;
  themeMode: AdventureThemeMode;
  chapterSlug?: string;
}

const RARITY_CONFIG: Record<ItemRarity, { color: string; glow: string; border: string }> = {
  comum:    { color: "#94a3b8", glow: "#94a3b820", border: "#94a3b830" },
  raro:     { color: "#60a5fa", glow: "#60a5fa20", border: "#60a5fa35" },
  epico:    { color: "#c084fc", glow: "#c084fc25", border: "#c084fc40" },
  lendario: { color: "#fbbf24", glow: "#fbbf2430", border: "#fbbf2450" },
};

export default function AdventureMochilaScreen({ langCode, themeMode, chapterSlug }: AdventureMochilaScreenProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, themeMode);

  const [inventory, setInventory] = useState<ApiUserInventoryItem[]>([]);
  const [chapterItems, setChapterItems] = useState<ApiAdventureItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [expanded, setExpanded] = useState<number | null>(null);

  useEffect(() => {
    if (!chapterSlug) return;
    setLoading(true);
    Promise.all([
      adventureService.listInventory(),
      adventureService.listItems(chapterSlug),
    ])
      .then(([inv, items]) => { setInventory(inv); setChapterItems(items); })
      .finally(() => setLoading(false));
  }, [chapterSlug]);

  const earnedItemIds = new Set(inventory.map(i => i.item.id));
  const locked = chapterItems.filter(i => !earnedItemIds.has(i.id));
  const expandedEntry = inventory.find(e => e.item.id === expanded);

  async function handleUseItem(itemId: number) {
    try {
      const updated = await adventureService.useInventoryItem(itemId);
      setInventory(prev => prev.map(e => e.item.id === itemId ? updated : e));
    } catch {
      // non-blocking
    }
    setExpanded(null);
  }

  function actionLabel(action: string): string {
    const map: Record<string, string> = {
      examinar: s.adventure.actionExaminar,
      entregar: s.adventure.actionEntregar,
      usar:     s.adventure.actionUsar,
      equipar:  s.adventure.actionEquipar,
    };
    return map[action] ?? action;
  }

  if (!chapterSlug || loading) {
    return (
      <div className="flex h-full items-center justify-center">
        <p className="animate-pulse text-sm font-semibold" style={{ color: c.textOnBg }}>
          {s.adventure.inventoryLoading}
        </p>
      </div>
    );
  }

  return (
    <div className="px-4 pb-8 pt-5 md:px-8 md:pt-7">

      <div className="mb-5">
        <p className="text-[10px] font-bold uppercase tracking-[0.22em]" style={{ color: c.textFaint }}>
          {s.adventure.inventoryLabel}
        </p>
        <h2 className="mt-0.5 text-xl font-bold leading-tight md:text-2xl" style={{ color: c.parchment }}>
          {s.adventure.tabBag}
        </h2>
        <p className="mt-1 text-sm" style={{ color: c.textOnBg }}>
          {s.adventure.itemsCollected(inventory.length)}
        </p>
      </div>

      {inventory.length === 0 ? (
        <div
          className="flex flex-col items-center gap-3 rounded-2xl px-6 py-10 text-center"
          style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
        >
          <Backpack size={36} style={{ color: c.textOnBg }} />
          <p className="text-sm font-semibold" style={{ color: c.textOnBg }}>
            {s.adventure.bagEmpty}
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-2 gap-3 md:grid-cols-3 lg:grid-cols-4">
          {inventory.map(entry => (
            <ItemCard
              key={entry.item.id}
              item={entry.item}
              isUsed={entry.is_used}
              expanded={expanded === entry.item.id}
              onToggle={() => setExpanded(prev => prev === entry.item.id ? null : entry.item.id)}
              c={c}
              itemUsedLabel={s.adventure.itemUsed}
              rarityLabel={s.adventure.itemRarity[entry.item.rarity]}
            />
          ))}
        </div>
      )}


      {expandedEntry && (
        <ItemDetailOverlay
          entry={expandedEntry}
          c={c}
          onClose={() => setExpanded(null)}
          onUse={() => void handleUseItem(expandedEntry.item.id)}
          actionLabel={actionLabel(expandedEntry.item.action)}
          itemUsedLabel={s.adventure.itemUsed}
          rarityLabel={s.adventure.itemRarity[expandedEntry.item.rarity]}
        />
      )}

    </div>
  );
}

function ItemDetailOverlay({ entry, c, onClose, onUse, actionLabel, itemUsedLabel, rarityLabel }: {
  entry: ApiUserInventoryItem;
  c: ReturnType<typeof getAdventureColors>;
  onClose: () => void;
  onUse: () => void;
  actionLabel: string;
  itemUsedLabel: string;
  rarityLabel: string;
}) {
  const r          = RARITY_CONFIG[entry.item.rarity];
  const paragraphs = (entry.item.lore || "").split("\n\n").filter(Boolean);

  return (
    <div
      className="fixed inset-0 z-50 flex flex-col"
      style={{ background: "rgba(0,0,0,0.95)", animation: "narrativeFadeIn 300ms ease-out both" }}
      onClick={onClose}
    >
      <div
        className="flex flex-1 flex-col overflow-hidden md:m-auto md:h-auto md:max-h-[85vh] md:w-full md:max-w-lg md:rounded-3xl"
        style={{
          background: c.surfaceMid,
          border: `1px solid ${r.border}`,
          boxShadow: `0 16px 48px ${r.glow}`,
        }}
        onClick={e => e.stopPropagation()}
      >
        <div className="relative flex shrink-0 items-start gap-4 px-6 pb-4 pt-6">
          <div
            className="grid h-20 w-20 shrink-0 place-items-center rounded-2xl"
            style={{ background: r.glow, border: `2px solid ${r.border}`, opacity: entry.is_used ? 0.45 : 1 }}
          >
            <Emoji char={entry.item.emoji} size={52} />
          </div>
          <div className="min-w-0 flex-1 pt-1">
            <p className="text-lg font-bold leading-tight md:text-xl" style={{ color: c.parchment }}>
              {entry.item.name}
            </p>
            <div className="mt-2 flex items-center gap-2">
              <span
                className="rounded-full px-2 py-0.5 text-[9px] font-bold uppercase tracking-wider"
                style={{ background: `${r.color}15`, color: r.color, border: `1px solid ${r.border}` }}
              >
                {rarityLabel}
              </span>
              {entry.is_used && (
                <span className="text-[10px] font-semibold uppercase tracking-wider" style={{ color: c.textFaint }}>
                  {itemUsedLabel}
                </span>
              )}
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full"
            style={{ background: c.surface, color: c.parchment }}
          >
            <X size={16} />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto px-6 pb-6">
          {paragraphs.map((para, i) => (
            <p
              key={i}
              className="text-[15px] leading-[1.7] md:text-base"
              style={{
                color: c.textOnBg,
                marginBottom: i < paragraphs.length - 1 ? "0.9rem" : 0,
              }}
            >
              {para}
            </p>
          ))}
        </div>

        {entry.item.action === "usar" && !entry.is_used && (
          <div className="shrink-0 px-6 pb-6">
            <button
              type="button"
              onClick={onUse}
              className="w-full rounded-2xl py-3.5 text-base font-bold transition active:scale-[0.97]"
              style={{
                background: r.color,
                color: "#0a0a0a",
              }}
            >
              {actionLabel}
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

function ItemCard({ item, isUsed, expanded, onToggle, c, itemUsedLabel, rarityLabel }: {
  item: ApiAdventureItem;
  isUsed: boolean;
  expanded: boolean;
  onToggle: () => void;
  c: ReturnType<typeof getAdventureColors>;
  itemUsedLabel: string;
  rarityLabel: string;
}) {
  const r = RARITY_CONFIG[item.rarity];
  return (
    <button
      type="button"
      onClick={onToggle}
      className="flex flex-col items-center gap-2.5 rounded-2xl px-3 pb-4 pt-4 text-center transition active:scale-[0.97]"
      style={{
        background: expanded ? c.surfaceMid : c.surface,
        border: `1px solid ${expanded ? r.color + "60" : r.border}`,
        boxShadow: expanded ? `0 0 16px ${r.glow}` : "none",
      }}
    >
      <div
        className="flex h-16 w-16 items-center justify-center rounded-full"
        style={{
          background: r.glow,
          border: `2px solid ${r.border}`,
          opacity: isUsed ? 0.5 : 1,
        }}
      >
        <Emoji char={item.emoji} size={40} />
      </div>
      <div className="min-w-0 w-full">
        <p className="truncate text-sm font-bold leading-tight" style={{ color: isUsed ? c.textFaint : c.parchment }}>
          {item.name}
        </p>
      </div>
      <span
        className="rounded-full px-2 py-0.5 text-[9px] font-bold uppercase tracking-wider"
        style={
          isUsed
            ? { background: c.surface, color: c.textFaint, border: `1px solid ${c.borderFaint}` }
            : { background: `${r.color}15`, color: r.color, border: `1px solid ${r.border}` }
        }
      >
        {isUsed ? itemUsedLabel : rarityLabel}
      </span>
    </button>
  );
}
