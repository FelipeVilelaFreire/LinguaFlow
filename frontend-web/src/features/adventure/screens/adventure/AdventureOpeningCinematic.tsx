import { ChevronLeft } from "lucide-react";
import { useState } from "react";

import { useStrings } from "../../../../contexts/StringsContext";
import { getAdventureColors } from "../../theme/adventureColors";

interface Scene {
  eyebrow: string;
  paragraphs: string[];
  npcLabel?: string;
  npcLine?: string;
  preReply?: string;
  playerReply?: string;
  replyEcho?: string;
}

const SCENES_BY_LANG: Record<string, Scene[]> = {
  ES: [
    {
      eyebrow: "El Caminante · T1 · Cena I",
      paragraphs: [
        "Você não sabe seu nome. Não sabe de onde veio.",
        "Quando seus olhos se abrem, o que você vê é um céu de outubro — azul profundo, sem uma nuvem — e o cheiro de terra quente de um verão mexicano.",
        "Você está deitado num campo de milho dourado. Ao longe, as torres de adobe de um pueblo colonial recortam o horizonte.",
        "No bolso, um envelope lacrado. Estampado na cera vermelha, duas palavras: Todavía no.",
      ],
    },
    {
      eyebrow: "El Caminante · T1 · Cena II",
      paragraphs: [
        "Você tenta abrir o envelope. A cera não cede. Seja o que for que está dentro — não é para agora.",
        "Você olha para as torres ao longe. Alguém naquele pueblo pode saber quem você é.",
        "Para sobreviver. Para perguntar. Para entender o que ouvir — você vai precisar aprender a falar espanhol.",
        "Você se levanta e começa a caminhar.",
      ],
    },
    {
      eyebrow: "El Caminante · T1 · Cena III",
      paragraphs: [
        "O caminho de terra seca leva você direto ao pueblo. Cada passo levanta uma nuvem de poeira dourada.",
        "As paredes de adobe crescem diante de você. O cheiro de tortilhas e fumaça. Vozes por todo lado — rápidas, calorosas, completamente incompreensíveis.",
        "Você chega ao portão. Dois batentes de madeira escura, entreabertos. A luz do fim da tarde atravessa a fresta.",
        "Um campesino de chapéu largo aparece do outro lado. Te olha de cima a baixo. Espera.",
        "Você vasculha o que sobrou da memória. O idioma é estranho — mas uma única palavra emerge.",
      ],
      npcLabel: "Don Miguel",
      npcLine: "¡Oye, forastero! ¿Estás bien?",
      preReply: "Ele falou. Você não entendeu nada. E ainda assim, uma única palavra surgiu do fundo de algum lugar.",
      playerReply: "Hola.",
      replyEcho: "O campesino sorri e abre passagem.",
    },
  ],
};

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

  const SCENES = SCENES_BY_LANG[langCode.toUpperCase()] ?? SCENES_BY_LANG.ES;
  const [sceneIdx, setSceneIdx] = useState(0);

  const scene  = SCENES[sceneIdx];
  const isLast = sceneIdx === SCENES.length - 1;

  function advance() {
    if (isLast) {
      onComplete();
    } else {
      setSceneIdx((i) => i + 1);
    }
  }

  return (
    <div className="flex h-full flex-col">

      {/* Header */}
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
      <div className="flex-1 overflow-y-auto px-6 pb-4 pt-6 md:px-10">
        <div
          key={sceneIdx}
          className="mx-auto flex max-w-lg flex-col items-center gap-8 text-center"
          style={{ animation: "narrativeFadeIn 600ms ease-out both" }}
        >
          {/* Eyebrow */}
          <div className="flex w-full items-center gap-3">
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
          <div className="flex flex-col gap-6">
            {scene.paragraphs.map((para, i) => (
              <p
                key={i}
                className="text-lg font-medium leading-9 md:text-xl md:leading-10"
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
              className="w-full rounded-2xl p-5"
              style={{
                background: c.surfaceMid,
                border: `1px solid ${c.borderFaint}`,
                animation: "narrativeFadeIn 1400ms ease-out both",
              }}
            >
              {scene.npcLabel && (
                <p
                  className="mb-2 text-[10px] font-bold uppercase tracking-widest"
                  style={{ color: c.goldAccent }}
                >
                  {scene.npcLabel}
                </p>
              )}
              <p
                className="text-xl font-semibold italic leading-relaxed md:text-2xl"
                style={{ color: c.parchment }}
              >
                "{scene.npcLine}"
              </p>
            </div>
          )}

          {/* Bridge between NPC and player reply */}
          {scene.preReply && (
            <p
              className="text-lg font-medium leading-9 md:text-xl md:leading-10"
              style={{
                color: c.textOnBg,
                animation: "narrativeFadeIn 1600ms ease-out both",
              }}
            >
              {scene.preReply}
            </p>
          )}

          {/* Player reply */}
          {scene.playerReply && (
            <div
              className="flex w-full flex-col items-center gap-3 rounded-2xl p-6"
              style={{
                background: `${c.seasonBadgeBg}18`,
                border: `1px solid ${c.seasonBadgeBg}40`,
                animation: "narrativeFadeIn 1800ms ease-out both",
              }}
            >
              <p className="text-2xl font-bold italic md:text-3xl" style={{ color: c.parchment }}>
                "{scene.playerReply}"
              </p>
              {scene.replyEcho && (
                <p className="text-sm font-semibold" style={{ color: c.goldAccent }}>
                  {scene.replyEcho}
                </p>
              )}
            </div>
          )}

          {/* Bottom ornament — last scene only */}
          {isLast && (
            <div className="pt-2" style={{ animation: "narrativeFadeIn 2200ms ease-out both" }}>
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
