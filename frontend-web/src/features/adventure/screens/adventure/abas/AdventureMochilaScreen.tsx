import { Backpack, Lock, X } from "lucide-react";
import { motion } from "framer-motion";
import { useEffect, useState } from "react";

import { useStrings } from "../../../../../contexts/StringsContext";
import { adventureService } from "../../../../../services/adventureService";
import { getAdventureColors } from "../../../theme/adventureColors";
import type { AdventureThemeMode } from "../../../theme/adventureColors";
import Emoji from "../../../../../components/Emoji";
import type { ApiAdventureItem, ApiUserInventoryItem, ItemRarity } from "../../../../../types/adventure";

type LockedItem = ApiAdventureItem & { unlock_hint_word_id: string };

interface AdventureMochilaScreenProps {
  langCode: string;
  themeMode: AdventureThemeMode;
  chapterSlug?: string;
}

const RARITY_CONFIG: Record<ItemRarity, { color: string; glow: string; border: string; surface: string }> = {
  comum:    { color: "#94a3b8", glow: "#94a3b820", border: "#94a3b840", surface: "linear-gradient(160deg, rgba(148,163,184,0.16), rgba(255,255,255,0.035))" },
  raro:     { color: "#60a5fa", glow: "#60a5fa24", border: "#60a5fa45", surface: "linear-gradient(160deg, rgba(96,165,250,0.18), rgba(255,255,255,0.04))" },
  epico:    { color: "#c084fc", glow: "#c084fc30", border: "#c084fc55", surface: "linear-gradient(160deg, rgba(192,132,252,0.22), rgba(255,255,255,0.045))" },
  lendario: { color: "#fbbf24", glow: "#fbbf2438", border: "#fbbf2465", surface: "linear-gradient(160deg, rgba(251,191,36,0.22), rgba(255,255,255,0.05))" },
  mitico:   { color: "#22d3ee", glow: "#22d3ee40", border: "#22d3ee70", surface: "linear-gradient(160deg, rgba(34,211,238,0.24), rgba(192,132,252,0.12), rgba(255,255,255,0.045))" },
};

export default function AdventureMochilaScreen({ langCode, themeMode, chapterSlug }: AdventureMochilaScreenProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, themeMode);

  const [inventory, setInventory] = useState<ApiUserInventoryItem[]>([]);
  const [lockedItems, setLockedItems] = useState<LockedItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [expanded, setExpanded] = useState<number | null>(null);

  useEffect(() => {
    if (!chapterSlug) return;
    setLoading(true);
    Promise.all([
      adventureService.listInventory(),
      adventureService.listLockedItems(chapterSlug),
    ])
      .then(([inv, lockedRes]) => { setInventory(inv); setLockedItems(lockedRes.locked); })
      .finally(() => setLoading(false));
  }, [chapterSlug]);

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
          {inventory.map((entry, index) => (
            <ItemCard
              key={entry.item.id}
              item={entry.item}
              isUsed={entry.is_used}
              expanded={expanded === entry.item.id}
              onToggle={() => setExpanded(prev => prev === entry.item.id ? null : entry.item.id)}
              c={c}
              itemUsedLabel={s.adventure.itemUsed}
              rarityLabel={s.adventure.itemRarity[entry.item.rarity]}
              index={index}
            />
          ))}
        </div>
      )}

      {lockedItems.length > 0 && (
        <div className="mt-8">
          <p className="mb-3 text-[10px] font-bold uppercase tracking-[0.22em]" style={{ color: c.textFaint }}>
            {s.adventure.toDiscover}
          </p>
          <div className="grid grid-cols-2 gap-3 md:grid-cols-3 lg:grid-cols-4">
            {lockedItems.map(item => (
              <LockedItemCard
                key={item.id}
                item={item}
                c={c}
                hint={s.adventure.itemLockedHint(item.word_id ?? "")}
              />
            ))}
          </div>
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
            className="relative grid h-20 w-20 shrink-0 place-items-center overflow-hidden rounded-2xl"
            style={{
              background: r.surface,
              border: `2px solid ${r.border}`,
              boxShadow: `0 0 28px ${r.glow}`,
              opacity: entry.is_used ? 0.45 : 1,
            }}
          >
            <span className="absolute inset-x-3 top-2 h-px" style={{ background: `linear-gradient(90deg, transparent, ${r.color}, transparent)` }} />
            <span style={{ filter: `drop-shadow(0 0 12px ${r.color}70)` }}>
              <Emoji char={entry.item.emoji} size={52} />
            </span>
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

function LockedItemCard({ item, c, hint }: {
  item: LockedItem;
  c: ReturnType<typeof getAdventureColors>;
  hint: string;
}) {
  return (
    <div
      className="relative flex min-h-[166px] flex-col items-center gap-2.5 overflow-hidden rounded-2xl px-3 pb-4 pt-4 text-center"
      style={{
        background: `linear-gradient(160deg, ${c.surface}, rgba(255,255,255,0.025))`,
        border: `1px dashed ${c.borderFaint}`,
      }}
    >
      <span className="pointer-events-none absolute inset-0 bg-black/10" />
      <div
        className="relative flex h-16 w-16 items-center justify-center rounded-2xl"
        style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
      >
        <span style={{ opacity: 0.25, filter: "grayscale(1)" }}>
          <Emoji char={item.emoji} size={40} />
        </span>
        <div
          className="absolute -bottom-1 -right-1 flex h-6 w-6 items-center justify-center rounded-full"
          style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
        >
          <Lock size={12} style={{ color: c.textFaint }} />
        </div>
      </div>
      <div className="min-w-0 w-full">
        <p className="truncate text-sm font-bold leading-tight" style={{ color: c.textFaint }}>
          {item.name}
        </p>
        <p className="mt-0.5 text-[10px] leading-tight" style={{ color: c.textFaint }}>
          {hint}
        </p>
      </div>
    </div>
  );
}

function ItemCard({ item, isUsed, expanded, onToggle, c, itemUsedLabel, rarityLabel, index }: {
  item: ApiAdventureItem;
  isUsed: boolean;
  expanded: boolean;
  onToggle: () => void;
  c: ReturnType<typeof getAdventureColors>;
  itemUsedLabel: string;
  rarityLabel: string;
  index: number;
}) {
  const r = RARITY_CONFIG[item.rarity];
  return (
    <motion.button
      type="button"
      onClick={onToggle}
      className="relative flex min-h-[172px] flex-col items-center gap-2.5 overflow-hidden rounded-2xl px-3 pb-4 pt-4 text-center transition hover:-translate-y-0.5 active:scale-[0.97]"
      initial={{ opacity: 0, y: 12, scale: 0.96 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      whileHover={{ y: -3 }}
      whileTap={{ scale: 0.96 }}
      transition={{ duration: 0.28, delay: Math.min(index * 0.035, 0.22), ease: [0.16, 1, 0.3, 1] }}
      style={{
        background: expanded ? r.surface : `linear-gradient(160deg, ${c.surface}, rgba(255,255,255,0.035))`,
        border: `1px solid ${expanded ? r.color + "60" : r.border}`,
        boxShadow: expanded ? `0 18px 44px ${r.glow}` : `0 10px 28px rgba(0,0,0,0.12), inset 0 1px 0 rgba(255,255,255,0.06)`,
        opacity: isUsed ? 0.68 : 1,
      }}
    >
      <span
        className="pointer-events-none absolute inset-x-4 top-0 h-px"
        style={{ background: `linear-gradient(90deg, transparent, ${r.color}, transparent)` }}
      />
      <span
        className="pointer-events-none absolute -right-8 -top-8 h-20 w-20 rounded-full blur-2xl"
        style={{ background: r.glow }}
      />
      <div
        className="relative flex h-16 w-16 items-center justify-center overflow-hidden rounded-2xl"
        style={{
          background: r.surface,
          border: `2px solid ${r.border}`,
          boxShadow: `0 0 24px ${r.glow}`,
        }}
      >
        <span className="absolute inset-x-2 top-2 h-px" style={{ background: `linear-gradient(90deg, transparent, ${r.color}, transparent)` }} />
        <span style={{ filter: `drop-shadow(0 0 10px ${r.color}80)` }}>
          <Emoji char={item.emoji} size={40} />
        </span>
      </div>
      <div className="min-w-0 w-full">
        <p className="truncate text-sm font-bold leading-tight" style={{ color: isUsed ? c.textFaint : c.parchment, textShadow: isUsed ? "none" : "0 1px 8px rgba(0,0,0,0.28)" }}>
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
    </motion.button>
  );
}
