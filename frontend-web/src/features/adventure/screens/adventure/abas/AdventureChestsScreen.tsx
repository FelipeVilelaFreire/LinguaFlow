import { CheckCircle2, Clock3, Gift, PackageOpen, Timer, Unlock } from "lucide-react";
import { useEffect, useMemo, useState } from "react";

import Emoji from "../../../../../components/Emoji";
import { adventureService } from "../../../../../services/adventureService";
import type { ApiUserChest } from "../../../../../types/adventure";
import { getAdventureColors } from "../../../theme/adventureColors";
import type { AdventureThemeMode } from "../../../theme/adventureColors";

interface AdventureChestsScreenProps {
  langCode: string;
  themeMode: AdventureThemeMode;
}

const TIER_LABEL: Record<string, string> = {
  bronze: "Bronze",
  prata: "Prata",
  ouro: "Ouro",
  lendario: "Lendario",
};

const STATUS_LABEL: Record<ApiUserChest["status"], string> = {
  stored: "Guardado",
  opening: "Abrindo",
  ready: "Pronto",
  claimed: "Coletado",
  discarded: "Descartado",
};

export default function AdventureChestsScreen({ langCode, themeMode }: AdventureChestsScreenProps) {
  const c = getAdventureColors(langCode, themeMode);
  const [chests, setChests] = useState<ApiUserChest[]>([]);
  const [loading, setLoading] = useState(true);
  const [busyId, setBusyId] = useState<number | null>(null);
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
      setChests(prev => prev.map(chest => chest.id === id ? updated : chest));
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

  const openingChest = activeChests.find(chest => chest.status === "opening");
  const readyCount = activeChests.filter(chest => chest.is_ready || chest.status === "ready").length;
  const storedCount = activeChests.filter(chest => chest.status === "stored").length;

  if (loading) {
    return (
      <div className="flex h-full items-center justify-center">
        <p className="animate-pulse text-sm font-semibold" style={{ color: c.textOnBg }}>
          Carregando baus...
        </p>
      </div>
    );
  }

  return (
    <div className="px-4 pb-8 pt-5 md:px-8 md:pt-7">
      <div className="mb-5">
        <p className="text-[10px] font-bold uppercase tracking-[0.22em]" style={{ color: c.textFaint }}>
          Recompensas
        </p>
        <h2 className="mt-0.5 text-xl font-bold leading-tight md:text-2xl" style={{ color: c.parchment }}>
          Baus
        </h2>
        <p className="mt-1 text-sm" style={{ color: c.textOnBg }}>
          Guarde baus de fase, abra um por vez e colete itens que fortalecem seus poderes.
        </p>
      </div>

      <div className="mb-5 grid grid-cols-3 gap-2">
        <SummaryPill Icon={PackageOpen} label="Guardados" value={storedCount} c={c} />
        <SummaryPill Icon={Timer} label="Abrindo" value={openingChest ? 1 : 0} c={c} />
        <SummaryPill Icon={CheckCircle2} label="Prontos" value={readyCount} c={c} />
      </div>

      {activeChests.length === 0 ? (
        <div
          className="flex flex-col items-center gap-3 rounded-2xl px-6 py-10 text-center"
          style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
        >
          <Gift size={36} style={{ color: c.textOnBg }} />
          <p className="text-sm font-semibold" style={{ color: c.textOnBg }}>
            Complete fases com bau para guardar recompensas aqui.
          </p>
        </div>
      ) : (
        <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
          {activeChests.map(chest => (
            <ChestCard
              key={chest.id}
              chest={chest}
              now={now}
              c={c}
              busy={busyId === chest.id}
              openingBlocked={Boolean(openingChest && openingChest.id !== chest.id)}
              onStart={() => void startChest(chest.id)}
              onClaim={() => void claimChest(chest.id)}
            />
          ))}
        </div>
      )}

      {recentClaimed.length > 0 && (
        <section className="mt-8">
          <p className="mb-3 text-[10px] font-bold uppercase tracking-[0.22em]" style={{ color: c.textFaint }}>
            Coletados recentes
          </p>
          <div className="grid gap-3 md:grid-cols-2 xl:grid-cols-3">
            {recentClaimed.map(chest => (
              <ClaimedChestCard key={chest.id} chest={chest} c={c} />
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

function ChestCard({ chest, now, c, busy, openingBlocked, onStart, onClaim }: {
  chest: ApiUserChest;
  now: number;
  c: ReturnType<typeof getAdventureColors>;
  busy: boolean;
  openingBlocked: boolean;
  onStart: () => void;
  onClaim: () => void;
}) {
  const unlockAt = chest.unlock_at ? new Date(chest.unlock_at).getTime() : null;
  const startedAt = chest.started_at ? new Date(chest.started_at).getTime() : null;
  const remainingMs = unlockAt ? Math.max(0, unlockAt - now) : 0;
  const isReady = chest.is_ready || chest.status === "ready" || (chest.status === "opening" && remainingMs <= 0);
  const minutes = Math.floor(remainingMs / 60000);
  const seconds = Math.floor((remainingMs % 60000) / 1000);
  const totalMs = unlockAt && startedAt ? Math.max(1, unlockAt - startedAt) : 1;
  const progress = isReady ? 1 : unlockAt && startedAt ? Math.min(1, Math.max(0, (now - startedAt) / totalMs)) : 0;
  const tierLabel = TIER_LABEL[chest.chest_tier] ?? chest.chest_tier;
  const canStart = chest.status === "stored" && !openingBlocked && !busy;

  return (
    <div
      className="rounded-2xl p-4"
      style={{ background: c.surface, border: `1px solid ${c.borderFaint}`, boxShadow: "0 12px 30px rgba(0,0,0,0.16)" }}
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
              Bau {tierLabel}
            </p>
            <span
              className="rounded-full px-2 py-0.5 text-[9px] font-bold uppercase tracking-wider"
              style={{ background: c.surfaceMid, color: isReady ? c.goldAccent : c.textFaint, border: `1px solid ${c.borderFaint}` }}
            >
              {isReady ? "Pronto" : STATUS_LABEL[chest.status]}
            </span>
          </div>
          <p className="text-xs font-semibold" style={{ color: c.textFaint }}>
            Fase {chest.phase_number} · score {chest.phase_score}
          </p>
        </div>
      </div>

      <div className="mt-4 rounded-xl p-3" style={{ background: c.surfaceMid }}>
        <div className="flex items-center gap-2 text-sm font-semibold" style={{ color: c.textOnBg }}>
          {chest.status === "opening" ? <Timer size={16} /> : <Unlock size={16} />}
          {chest.status === "opening"
            ? isReady ? "Pronto para coletar" : `${minutes}:${seconds.toString().padStart(2, "0")}`
            : "Armazenado para abrir depois"}
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
          disabled={!canStart}
          className="mt-4 h-11 w-full rounded-xl text-sm font-bold disabled:cursor-not-allowed disabled:opacity-55"
          style={{ background: c.ctaBg, color: c.ctaText }}
        >
          {openingBlocked ? "Aguarde o bau atual" : busy ? "Iniciando..." : "Iniciar abertura"}
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
          {busy ? "Coletando..." : isReady ? "Coletar recompensa" : "Abrindo"}
        </button>
      )}
    </div>
  );
}

function ClaimedChestCard({ chest, c }: {
  chest: ApiUserChest;
  c: ReturnType<typeof getAdventureColors>;
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
            {item?.name ?? `Bau ${TIER_LABEL[chest.chest_tier] ?? chest.chest_tier}`}
          </p>
          <p className="text-xs font-semibold capitalize" style={{ color: c.textFaint }}>
            {item?.skill ? `${item.skill.emoji} ${item.skill.name}` : chest.rolled_rarity ?? "Recompensa coletada"}
          </p>
        </div>
        <CheckCircle2 size={18} style={{ color: c.goldAccent }} />
      </div>
    </div>
  );
}
