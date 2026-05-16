import { CheckCircle2, Clock3, Gift, PackageOpen, Timer, Unlock } from "lucide-react";
import { useEffect, useMemo, useState } from "react";

import Emoji from "../../../../../components/Emoji";
import { useStrings } from "../../../../../contexts/StringsContext";
import { adventureService } from "../../../../../services/adventureService";
import type { ApiUserChest } from "../../../../../types/adventure";
import { getAdventureColors } from "../../../theme/adventureColors";
import type { AdventureThemeMode } from "../../../theme/adventureColors";

interface AdventureChestsScreenProps {
  langCode: string;
  themeMode: AdventureThemeMode;
}

const OPENING_SLOTS = 2;

export default function AdventureChestsScreen({ langCode, themeMode }: AdventureChestsScreenProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, themeMode);
  const [chests, setChests] = useState<ApiUserChest[]>([]);
  const [loading, setLoading] = useState(true);
  const [busyId, setBusyId] = useState<number | null>(null);
  const [movingChestId, setMovingChestId] = useState<number | null>(null);
  const [now, setNow] = useState(() => Date.now());

  useEffect(() => {
    void refresh();
    const timer = window.setInterval(() => setNow(Date.now()), 1000);
    return () => window.clearInterval(timer);
  }, []);

  async function refresh() {
    setLoading(true);
    try {
      setChests(await adventureService.listChests());
    } finally {
      setLoading(false);
    }
  }

  async function startChest(id: number) {
    setBusyId(id);
    try {
      const updated = await adventureService.startChest(id);
      setMovingChestId(id);
      setChests(prev => prev.map(chest => chest.id === id ? updated : chest));
      window.setTimeout(() => setMovingChestId(current => current === id ? null : current), 720);
    } finally {
      setBusyId(null);
    }
  }

  async function claimChest(id: number) {
    setBusyId(id);
    try {
      const updated = await adventureService.claimChest(id);
      setChests(prev => prev.map(chest => chest.id === id ? updated : chest));
    } finally {
      setBusyId(null);
    }
  }

  const activeChests = useMemo(
    () => chests.filter(chest => chest.status !== "claimed" && chest.status !== "discarded"),
    [chests],
  );

  const recentClaimed = useMemo(
    () => chests
      .filter(chest => chest.status === "claimed")
      .sort((a, b) => new Date(b.claimed_at ?? b.created_at).getTime() - new Date(a.claimed_at ?? a.created_at).getTime())
      .slice(0, 6),
    [chests],
  );

  const slotChests = useMemo(
    () => activeChests
      .filter(chest => chest.status === "opening" || chest.status === "ready")
      .sort((a, b) => new Date(a.unlock_at ?? a.started_at ?? a.created_at).getTime() - new Date(b.unlock_at ?? b.started_at ?? b.created_at).getTime()),
    [activeChests],
  );

  const storedChests = useMemo(
    () => activeChests
      .filter(chest => chest.status === "stored")
      .sort((a, b) => new Date(b.created_at).getTime() - new Date(a.created_at).getTime()),
    [activeChests],
  );

  const readyCount = slotChests.filter(chest => chest.is_ready || chest.status === "ready").length;
  const storedCount = storedChests.length;
  const hasFreeSlot = slotChests.length < OPENING_SLOTS;

  if (loading) {
    return (
      <div className="flex h-full items-center justify-center">
        <p className="animate-pulse text-sm font-semibold" style={{ color: c.textOnBg }}>
          {s.adventure.chestsLoading}
        </p>
      </div>
    );
  }

  return (
    <div className="px-4 pb-8 pt-5 md:px-8 md:pt-7">
      <div className="mb-5">
        <p className="text-[10px] font-bold uppercase tracking-[0.22em]" style={{ color: c.textFaint }}>
          {s.adventure.chestsEyebrow}
        </p>
        <h2 className="mt-0.5 text-xl font-bold leading-tight md:text-2xl" style={{ color: c.parchment }}>
          {s.adventure.chestsTitle}
        </h2>
        <p className="mt-1 text-sm" style={{ color: c.textOnBg }}>
          {s.adventure.chestsSubtitle}
        </p>
      </div>

      <div className="mb-5 grid grid-cols-3 gap-2">
        <SummaryPill Icon={PackageOpen} label={s.adventure.chestsStored} value={storedCount} c={c} />
        <SummaryPill Icon={Timer} label={s.adventure.chestsOpening} value={slotChests.length} c={c} />
        <SummaryPill Icon={CheckCircle2} label={s.adventure.chestsReadyPlural} value={readyCount} c={c} />
      </div>

      {activeChests.length === 0 ? (
        <div
          className="flex flex-col items-center gap-3 rounded-2xl px-6 py-10 text-center"
          style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
        >
          <Gift size={36} style={{ color: c.textOnBg }} />
          <p className="text-sm font-semibold" style={{ color: c.textOnBg }}>
            {s.adventure.chestsEmpty}
          </p>
        </div>
      ) : (
        <div className="space-y-6">
          <section>
            <div className="mb-3 flex items-end justify-between gap-3">
              <div>
                <p className="text-sm font-bold" style={{ color: c.parchment }}>
                  {s.adventure.chestsSlotsTitle}
                </p>
                <p className="mt-0.5 text-xs" style={{ color: c.textFaint }}>
                  {s.adventure.chestsSlotsHint}
                </p>
              </div>
              <span className="shrink-0 rounded-full px-3 py-1 text-xs font-bold tabular-nums" style={{ background: c.surfaceMid, color: c.textOnBg, border: `1px solid ${c.borderFaint}` }}>
                {slotChests.length}/{OPENING_SLOTS}
              </span>
            </div>
            <div className="grid gap-3 md:grid-cols-2">
              {Array.from({ length: OPENING_SLOTS }, (_, index) => {
                const chest = slotChests[index] ?? null;
                return (
                  <OpeningSlot
                    key={chest?.id ?? `empty-${index}`}
                    slotNumber={index + 1}
                    chest={chest}
                    now={now}
                    c={c}
                    strings={s}
                    busy={chest ? busyId === chest.id : false}
                    isArriving={chest?.id === movingChestId}
                    onClaim={chest ? () => void claimChest(chest.id) : undefined}
                  />
                );
              })}
            </div>
          </section>

          <section>
            <div className="mb-3 flex items-center justify-between gap-3">
              <p className="text-sm font-bold" style={{ color: c.parchment }}>
                {s.adventure.chestsStoredTitle}
              </p>
              {!hasFreeSlot && storedChests.length > 0 && (
                <span className="rounded-full px-3 py-1 text-[10px] font-bold uppercase tracking-wide" style={{ background: c.surfaceMid, color: c.textFaint, border: `1px solid ${c.borderFaint}` }}>
                  {s.adventure.chestsSlotsFull}
                </span>
              )}
            </div>
            {storedChests.length === 0 ? (
              <div className="rounded-2xl px-4 py-6 text-center" style={{ background: c.surface, border: `1px dashed ${c.borderFaint}` }}>
                <p className="text-sm font-semibold" style={{ color: c.textOnBg }}>
                  {s.adventure.chestSlotEmptyHint}
                </p>
              </div>
            ) : (
              <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
                {storedChests.map(chest => (
                  <ChestCard
                    key={chest.id}
                    chest={chest}
                    now={now}
                    c={c}
                    strings={s}
                    busy={busyId === chest.id}
                    variant="stored"
                    canStart={hasFreeSlot}
                    onStart={() => void startChest(chest.id)}
                  />
                ))}
              </div>
            )}
          </section>
        </div>
      )}

      {recentClaimed.length > 0 && (
        <section className="mt-8">
          <p className="mb-3 text-[10px] font-bold uppercase tracking-[0.22em]" style={{ color: c.textFaint }}>
            {s.adventure.chestsRecentClaimed}
          </p>
          <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
            {recentClaimed.map(chest => (
              <ClaimedChestCard key={chest.id} chest={chest} c={c} strings={s} />
            ))}
          </div>
        </section>
      )}
    </div>
  );
}

function SummaryPill({ Icon, label, value, c }: {
  Icon: typeof Gift;
  label: string;
  value: number;
  c: ReturnType<typeof getAdventureColors>;
}) {
  return (
    <div
      className="min-w-0 rounded-xl px-3 py-3"
      style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
    >
      <div className="flex items-center gap-2">
        <Icon size={14} style={{ color: c.goldAccent }} />
        <span className="truncate text-[10px] font-bold uppercase tracking-wide" style={{ color: c.textFaint }}>
          {label}
        </span>
      </div>
      <p className="mt-1 text-lg font-bold tabular-nums" style={{ color: c.parchment }}>
        {value}
      </p>
    </div>
  );
}

function OpeningSlot({ slotNumber, chest, now, c, strings, busy, isArriving, onClaim }: {
  slotNumber: number;
  chest: ApiUserChest | null;
  now: number;
  c: ReturnType<typeof getAdventureColors>;
  strings: ReturnType<typeof useStrings>;
  busy: boolean;
  isArriving: boolean;
  onClaim?: () => void;
}) {
  if (!chest) {
    return (
      <div
        className="grid min-h-[238px] place-items-center rounded-2xl border border-dashed p-4 text-center"
        style={{ background: c.surface, borderColor: c.borderFaint }}
      >
        <div>
          <div
            className="mx-auto grid h-14 w-14 place-items-center rounded-2xl"
            style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
          >
            <Unlock size={24} style={{ color: c.textFaint }} />
          </div>
          <p className="mt-3 text-sm font-bold" style={{ color: c.parchment }}>
            {strings.adventure.chestSlotLabel(slotNumber)}
          </p>
          <p className="mt-1 text-xs font-semibold" style={{ color: c.textFaint }}>
            {strings.adventure.chestSlotEmpty}
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className={isArriving ? "chest-slot-arrive" : undefined}>
      <ChestCard
        chest={chest}
        now={now}
        c={c}
        strings={strings}
        busy={busy}
        variant="slot"
        onClaim={onClaim}
      />
    </div>
  );
}

function ChestCard({ chest, now, c, strings, busy, variant, canStart = false, onStart, onClaim }: {
  chest: ApiUserChest;
  now: number;
  c: ReturnType<typeof getAdventureColors>;
  strings: ReturnType<typeof useStrings>;
  busy: boolean;
  variant: "slot" | "stored";
  canStart?: boolean;
  onStart?: () => void;
  onClaim?: () => void;
}) {
  const unlockAt = chest.unlock_at ? new Date(chest.unlock_at).getTime() : null;
  const startedAt = chest.started_at ? new Date(chest.started_at).getTime() : null;
  const remainingMs = unlockAt ? Math.max(0, unlockAt - now) : 0;
  const isReady = chest.is_ready || chest.status === "ready" || (chest.status === "opening" && remainingMs <= 0);
  const minutes = Math.floor(remainingMs / 60000);
  const seconds = Math.floor((remainingMs % 60000) / 1000);
  const totalMs = unlockAt && startedAt ? Math.max(1, unlockAt - startedAt) : 1;
  const progress = isReady ? 1 : unlockAt && startedAt ? Math.min(1, Math.max(0, (now - startedAt) / totalMs)) : 0;
  const tierLabel = getTierLabel(chest.chest_tier, strings);
  const canStartChest = chest.status === "stored" && canStart && !busy;
  const isSlotCard = variant === "slot";

  return (
    <div
      className="rounded-2xl p-4"
      style={{
        background: isSlotCard ? c.surfaceMid : c.surface,
        border: `1px solid ${isSlotCard ? `${c.goldAccent}55` : c.borderFaint}`,
        boxShadow: isSlotCard ? "0 16px 34px rgba(0,0,0,0.2)" : "0 12px 30px rgba(0,0,0,0.16)",
      }}
    >
      <div className="flex items-start gap-3">
        <div
          className="grid h-14 w-14 shrink-0 place-items-center rounded-2xl"
          style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
        >
          <Gift size={28} style={{ color: c.goldAccent }} />
        </div>
        <div className="min-w-0 flex-1">
          <div className="flex items-start justify-between gap-2">
            <p className="text-base font-bold" style={{ color: c.parchment }}>
              {strings.adventure.chestName(tierLabel)}
            </p>
            <span
              className="rounded-full px-2 py-0.5 text-[9px] font-bold uppercase tracking-wider"
              style={{ background: c.surfaceMid, color: isReady ? c.goldAccent : c.textFaint, border: `1px solid ${c.borderFaint}` }}
            >
              {isReady ? strings.adventure.chestStatusReady : getStatusLabel(chest.status, strings)}
            </span>
          </div>
          <p className="text-xs font-semibold" style={{ color: c.textFaint }}>
            {strings.adventure.chestPhaseScore(chest.phase_number, chest.phase_score)}
          </p>
        </div>
      </div>

      <div className="mt-4 rounded-xl p-3" style={{ background: c.surfaceMid }}>
        <div className="flex items-center gap-2 text-sm font-semibold" style={{ color: c.textOnBg }}>
          {chest.status === "opening" ? <Timer size={16} /> : <Unlock size={16} />}
          {chest.status === "opening"
            ? isReady ? strings.adventure.chestReadyToClaim : `${minutes}:${seconds.toString().padStart(2, "0")}`
            : strings.adventure.chestStoredForLater}
        </div>
        {chest.status === "opening" && (
          <div className="mt-3 h-2 overflow-hidden rounded-full" style={{ background: c.surface }}>
            <div
              className="h-full rounded-full transition-[width] duration-500"
              style={{ width: `${progress * 100}%`, background: `linear-gradient(90deg, ${c.nodeActive}, ${c.goldAccent})` }}
            />
          </div>
        )}
      </div>

      {chest.status === "stored" && (
        <button
          type="button"
          onClick={onStart}
          disabled={!canStartChest}
          className="mt-4 h-11 w-full rounded-xl text-sm font-bold disabled:cursor-not-allowed disabled:opacity-55"
          style={{ background: c.ctaBg, color: c.ctaText }}
        >
          {!canStart ? strings.adventure.chestsSlotsFull : busy ? strings.adventure.chestStarting : strings.adventure.chestStartOpening}
        </button>
      )}
      {(chest.status === "opening" || chest.status === "ready") && (
        <button
          type="button"
          onClick={onClaim}
          disabled={!isReady || busy}
          className="mt-4 h-11 w-full rounded-xl text-sm font-bold disabled:cursor-not-allowed disabled:opacity-55"
          style={{ background: c.goldAccent, color: "#1a0800" }}
        >
          {busy ? strings.adventure.chestClaiming : isReady ? strings.adventure.chestClaimReward : strings.adventure.chestsOpening}
        </button>
      )}
    </div>
  );
}

function ClaimedChestCard({ chest, c, strings }: {
  chest: ApiUserChest;
  c: ReturnType<typeof getAdventureColors>;
  strings: ReturnType<typeof useStrings>;
}) {
  const item = chest.earned_item;

  return (
    <div
      className="rounded-2xl p-4"
      style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
    >
      <div className="flex items-center gap-3">
        <div
          className="grid h-12 w-12 shrink-0 place-items-center rounded-xl"
          style={{ background: c.surfaceMid, border: `1px solid ${c.borderFaint}` }}
        >
          {item ? <Emoji char={item.emoji} size={32} /> : <Clock3 size={22} style={{ color: c.textFaint }} />}
        </div>
        <div className="min-w-0 flex-1">
          <p className="truncate text-sm font-bold" style={{ color: c.parchment }}>
            {item?.name ?? strings.adventure.chestName(getTierLabel(chest.chest_tier, strings))}
          </p>
          <p className="text-xs font-semibold capitalize" style={{ color: c.textFaint }}>
            {item?.skill ? `${item.skill.emoji} ${item.skill.name}` : chest.rolled_rarity ?? strings.adventure.chestFallbackReward}
          </p>
        </div>
        <CheckCircle2 size={18} style={{ color: c.goldAccent }} />
      </div>
    </div>
  );
}

function getTierLabel(tier: string, strings: ReturnType<typeof useStrings>) {
  const labels: Record<string, string> = {
    bronze: strings.adventure.chestTierBronze,
    prata: strings.adventure.chestTierPrata,
    ouro: strings.adventure.chestTierOuro,
    lendario: strings.adventure.chestTierLendario,
  };
  return labels[tier] ?? tier;
}

function getStatusLabel(status: ApiUserChest["status"], strings: ReturnType<typeof useStrings>) {
  const labels: Record<ApiUserChest["status"], string> = {
    stored: strings.adventure.chestStatusStored,
    opening: strings.adventure.chestStatusOpening,
    ready: strings.adventure.chestStatusReady,
    claimed: strings.adventure.chestStatusClaimed,
    discarded: strings.adventure.chestStatusDiscarded,
  };
  return labels[status];
}
