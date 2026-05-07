import { ChevronLeft } from "lucide-react";
import { useState } from "react";

import { useStrings } from "../../contexts/StringsContext";
import { getAdventureColors } from "../../theme/adventureColors";

interface Scene {
  eyebrow: string;
  paragraphs: string[];
  npcLabel?: string;
  npcLine?: string;
  playerReply?: string;
  replyEcho?: string;
}

const SCENES: Scene[] = [
  {
    eyebrow: "Il Viandante · T1 · Cena I",
    paragraphs: [
      "Você não sabe seu nome. Não sabe de onde veio.",
      "Quando seus olhos se abrem, o que você vê é um céu mediterrâneo — azul profundo, sem uma nuvem — e o cheiro de terra quente de um verão italiano.",
      "Você está deitado num campo de trigo dourado. Ao longe, as torres de um vilarejo medieval recortam o horizonte.",
      "No bolso, um envelope lacrado. Estampado na cera vermelha, duas palavras: Non ancora.",
    ],
  },
  {
    eyebrow: "Il Viandante · T1 · Cena II",
    paragraphs: [
      "Você tenta abrir o envelope. A cera não cede. Seja o que for que está dentro — não é para agora.",
      "Você olha para as torres ao longe. Alguém naquele vilarejo pode saber quem você é.",
      "Para sobreviver. Para perguntar. Para entender o que ouvir — você vai precisar aprender a falar italiano.",
      "Você se levanta e começa a caminhar.",
    ],
  },
  {
    eyebrow: "Il Viandante · T1 · Cena III",
    paragraphs: [
      "O portão de pedra do vilarejo está fechado. Um guarda cruza os braços e te barra a passagem.",
      "Você vasculha a memória. O idioma é estranho — mas uma única palavra emerge.",
    ],
    npcLabel: "Guarda",
    npcLine: "Ciao, forestiero.",
    playerReply: "Ciao.",
    replyEcho: "O portão se abre.",
  },
];

interface AdventureOpeningCinematicProps {
  langCode: string;
  onComplete: () => void;
}

export default function AdventureOpeningCinematic({
  langCode,
  onComplete,
}: AdventureOpeningCinematicProps) {
  const s = useStrings();
  const c = getAdventureColors(langCode, "dark");
  const [sceneIdx, setSceneIdx] = useState(0);

  const scene   = SCENES[sceneIdx];
  const isLast  = sceneIdx === SCENES.length - 1;

  function advance() {
    if (isLast) {
      onComplete();
    } else {
      setSceneIdx((i) => i + 1);
    }
  }

  return (
    <div className="flex h-full flex-col">

      {/* Header with back button */}
      <header className="shrink-0 flex items-center justify-between px-4 pb-2 pt-3">
        {sceneIdx > 0 ? (
          <button
            type="button"
            onClick={() => setSceneIdx((i) => i - 1)}
            className="flex items-center gap-1.5 rounded-full px-3 py-2 text-sm font-semibold"
            style={{ background: c.surface, color: c.parchment }}
          >
            <ChevronLeft size={15} />
            {s.actions.back}
          </button>
        ) : (
          <div className="h-9 w-20" />
        )}
        <p className="text-xs font-bold tabular-nums" style={{ color: c.textFaint }}>
          {sceneIdx + 1} / {SCENES.length}
        </p>
      </header>

      {/* Scrollable narrative */}
      <div className="flex-1 overflow-y-auto px-5 pb-4 pt-4">
        <div
          key={sceneIdx}
          className="flex flex-col gap-6"
          style={{ animation: "narrativeFadeIn 600ms ease-out both" }}
        >
          {/* Eyebrow */}
          <div className="flex items-center gap-3">
            <div className="h-px flex-1 rounded" style={{ background: `${c.goldAccent}35` }} />
            <span
              className="shrink-0 text-[9px] font-bold uppercase tracking-[0.25em]"
              style={{ color: `${c.goldAccent}80` }}
            >
              {scene.eyebrow}
            </span>
            <div className="h-px flex-1 rounded" style={{ background: `${c.goldAccent}35` }} />
          </div>

          {/* Paragraphs */}
          <div className="flex flex-col gap-5">
            {scene.paragraphs.map((para, i) => (
              <p
                key={i}
                className="text-base font-medium leading-8"
                style={{
                  color: c.textOnBg,
                  animation: `narrativeFadeIn ${300 + i * 250}ms ease-out both`,
                }}
              >
                {para}
              </p>
            ))}
          </div>

          {/* NPC speech */}
          {scene.npcLine && (
            <div
              className="rounded-2xl p-4"
              style={{
                background: c.surfaceMid,
                border: `1px solid ${c.borderFaint}`,
                animation: "narrativeFadeIn 1400ms ease-out both",
              }}
            >
              {scene.npcLabel && (
                <p
                  className="mb-1.5 text-[10px] font-bold uppercase tracking-widest"
                  style={{ color: c.goldAccent }}
                >
                  {scene.npcLabel}
                </p>
              )}
              <p
                className="text-lg font-semibold italic leading-relaxed"
                style={{ color: c.parchment }}
              >
                "{scene.npcLine}"
              </p>
            </div>
          )}

          {/* Player reply + gate echo */}
          {scene.playerReply && (
            <div
              className="flex flex-col items-center gap-3 rounded-2xl p-5 text-center"
              style={{
                background: `${c.seasonBadgeBg}18`,
                border: `1px solid ${c.seasonBadgeBg}40`,
                animation: "narrativeFadeIn 1800ms ease-out both",
              }}
            >
              <p className="text-2xl font-bold italic" style={{ color: c.parchment }}>
                "{scene.playerReply}"
              </p>
              {scene.replyEcho && (
                <p className="text-sm font-semibold" style={{ color: c.goldAccent }}>
                  {s.adventure.openingGateOpens}
                </p>
              )}
            </div>
          )}

          {/* Bottom ornament — only on last scene */}
          {isLast && (
            <div className="flex justify-center pt-2" style={{ animation: "narrativeFadeIn 2200ms ease-out both" }}>
              <svg viewBox="0 0 80 20" width={80} height={20} style={{ opacity: 0.25 }}>
                <path d="M5,10 Q20,2 40,10 Q60,18 75,10" fill="none" stroke={c.goldAccent} strokeWidth="1.5" />
                <circle cx="40" cy="10" r="3" fill={c.goldAccent} />
              </svg>
            </div>
          )}
        </div>
      </div>

      {/* Scene dots */}
      <div className="shrink-0 flex items-center justify-center gap-2 pb-3 pt-1">
        {SCENES.map((_, i) => (
          <div
            key={i}
            className="rounded-full transition-all duration-300"
            style={{
              width:  i === sceneIdx ? 18 : 6,
              height: 6,
              background: i <= sceneIdx ? c.nodeActive : c.surface,
            }}
          />
        ))}
      </div>

      {/* CTA */}
      <div className="shrink-0 px-4 pb-6 pt-1">
        <button
          type="button"
          onClick={advance}
          className="flex h-14 w-full items-center justify-center rounded-2xl text-base font-bold transition active:scale-[0.98]"
          style={{ background: c.ctaBg, color: "#fff" }}
        >
          {isLast ? s.adventure.openingEnterVillage : s.actions.continue}
        </button>
      </div>

    </div>
  );
}
