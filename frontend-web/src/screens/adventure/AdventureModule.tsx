import { Backpack, Map, Shield } from "lucide-react";

import { getAdventureColors } from "../../theme/adventureColors";
import AdventureHeroScreen from "./AdventureHeroScreen";
import AdventureMapScreen from "./AdventureMapScreen";
import AdventureMochilaScreen from "./AdventureMochilaScreen";

export type AdventureTab = "map" | "mochila" | "heroi";

interface AdventureModuleProps {
  langCode: string;
  initialTab: AdventureTab;
  onBack: () => void;
  onTabChange: (tab: AdventureTab) => void;
  onStartChapter: (chapterId: number) => void;
}

const TABS: Array<{ id: AdventureTab; label: string; Icon: typeof Map }> = [
  { id: "map",     label: "Mapa",    Icon: Map },
  { id: "mochila", label: "Mochila", Icon: Backpack },
  { id: "heroi",   label: "Herói",   Icon: Shield },
];

export default function AdventureModule({
  langCode,
  initialTab,
  onBack,
  onTabChange,
  onStartChapter,
}: AdventureModuleProps) {
  const c = getAdventureColors(langCode);

  return (
    <div
      className="flex min-h-dvh flex-col"
      style={{ background: `linear-gradient(180deg, ${c.bgFrom} 0%, ${c.bgMid} 50%, ${c.bgTo} 100%)` }}
    >
      {/* Content area — scrollable, takes remaining height above bottom nav */}
      <div className="flex-1 overflow-y-auto" style={{ paddingBottom: 72 }}>
        {initialTab === "map" && (
          <AdventureMapScreen
            langCode={langCode}
            onBack={onBack}
            onStartChapter={onStartChapter}
          />
        )}
        {initialTab === "mochila" && <AdventureMochilaScreen langCode={langCode} />}
        {initialTab === "heroi"   && <AdventureHeroScreen   langCode={langCode} />}
      </div>

      {/* Bottom nav — 3 tabs, Italian-themed */}
      <nav
        className="fixed inset-x-0 bottom-0 z-50 flex items-center"
        style={{
          background: `${c.bgFrom}f2`,
          backdropFilter: "blur(12px)",
          borderTop: `1px solid ${c.pathColor}40`,
          height: 68,
        }}
      >
        {TABS.map(({ id, label, Icon }) => {
          const active = id === initialTab;
          return (
            <button
              key={id}
              type="button"
              onClick={() => onTabChange(id)}
              className="flex flex-1 flex-col items-center justify-center gap-1 transition"
              style={{ color: active ? c.nodeActive : `${c.parchment}55` }}
            >
              <div
                className="flex h-8 w-8 items-center justify-center rounded-full transition"
                style={active ? { background: `${c.nodeActive}20` } : {}}
              >
                <Icon size={20} strokeWidth={active ? 2.5 : 1.8} />
              </div>
              <span className="text-[10px] font-bold uppercase tracking-wider">{label}</span>
            </button>
          );
        })}
      </nav>
    </div>
  );
}
