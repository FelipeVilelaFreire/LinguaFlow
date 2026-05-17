import { ArrowLeft, Loader2, Play, RotateCcw, Volume2 } from "lucide-react";
import { useEffect, useMemo, useState } from "react";

import CharacterAvatar from "../../components/CharacterAvatar";
import { adventureService } from "../../../../services/adventureService";
import { audioService } from "../../../../services/audioService";
import { getAdventureColors } from "../../theme/adventureColors";
import type { ApiAdventureCharacter } from "../../../../types/adventure";

const DEFAULT_SAMPLE =
  "¡Buenos días! Soy una voz de prueba para la aventura. Necesito sonar natural, con emoción, calma y ritmo de personaje, no como una voz robótica del navegador.";

interface AdventureVoiceDevScreenProps {
  langCode: string;
  chapterSlug?: string;
  onBack: () => void;
}

export default function AdventureVoiceDevScreen({ langCode, chapterSlug, onBack }: AdventureVoiceDevScreenProps) {
  const c = getAdventureColors(langCode, "dark");
  const [characters, setCharacters] = useState<ApiAdventureCharacter[]>([]);
  const [models, setModels] = useState<Array<{ id: string; name: string; label?: string; path: string; length_scale?: number | null }>>([]);
  const [sampleText, setSampleText] = useState(DEFAULT_SAMPLE);
  const [loading, setLoading] = useState(true);
  const [playingId, setPlayingId] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!chapterSlug) return;
    setLoading(true);
    adventureService.listCharacters(chapterSlug)
      .then(setCharacters)
      .catch(() => setError("Nao foi possivel carregar personagens."))
      .finally(() => setLoading(false));
    adventureService.devVoiceOptions()
      .then(res => setModels(res.models))
      .catch(() => {});
  }, [chapterSlug]);

  const visibleCharacters = useMemo(
    () => characters.filter(ch => ch.is_met || import.meta.env.DEV),
    [characters],
  );

  async function playSample(ch: ApiAdventureCharacter, modelPath?: string, lengthScale?: number | null) {
    setPlayingId(ch.id);
    setError(null);
    try {
      const res = await adventureService.devVoiceSample({
        npc: ch.name,
        lang: langCode,
        text: sampleText,
        model_path: modelPath,
        length_scale: lengthScale,
      });
      audioService.speakOrPlay(res.audio_url, res.text, langCode, ch.name);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Falha ao gerar audio.");
    } finally {
      setPlayingId(null);
    }
  }

  return (
    <main
      className="min-h-screen px-4 py-5 md:px-8 md:py-7"
      style={{
        background: `radial-gradient(circle at 20% 0%, ${c.ambientGlow}, transparent 34%), linear-gradient(135deg, ${c.bgFrom}, ${c.bgMid} 48%, ${c.bgTo})`,
      }}
    >
      <div className="mx-auto max-w-6xl">
        <div className="mb-5 flex items-start justify-between gap-3">
          <div>
            <p className="text-[10px] font-bold uppercase tracking-[0.22em]" style={{ color: c.textFaint }}>
              DEV · voice lab
            </p>
            <h1 className="mt-1 text-2xl font-black md:text-3xl" style={{ color: c.parchment }}>
              Teste de vozes dos personagens
            </h1>
          </div>
          <button
            type="button"
            onClick={onBack}
            className="inline-flex h-10 items-center gap-2 rounded-full px-4 text-sm font-bold transition active:scale-95"
            style={{ background: c.surface, border: `1px solid ${c.borderFaint}`, color: c.parchment }}
          >
            <ArrowLeft size={16} />
            Voltar
          </button>
        </div>

        <section
          className="mb-5 rounded-2xl p-4"
          style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
        >
          <div className="mb-3 flex items-center justify-between gap-3">
            <div className="flex items-center gap-2">
              <Volume2 size={18} style={{ color: c.goldAccent }} />
              <p className="text-sm font-bold" style={{ color: c.parchment }}>Frase de teste</p>
            </div>
            <button
              type="button"
              onClick={() => setSampleText(DEFAULT_SAMPLE)}
              className="inline-flex items-center gap-1.5 rounded-full px-3 py-1.5 text-xs font-bold"
              style={{ background: c.surfaceMid, color: c.textOnBg, border: `1px solid ${c.borderFaint}` }}
            >
              <RotateCcw size={13} />
              Reset
            </button>
          </div>
          <textarea
            value={sampleText}
            onChange={e => setSampleText(e.target.value)}
            rows={4}
            className="w-full resize-none rounded-xl px-3 py-3 text-sm font-semibold outline-none"
            style={{ background: "rgba(0,0,0,0.28)", color: c.parchment, border: `1px solid ${c.borderFaint}` }}
          />
        </section>

        {error && (
          <p className="mb-4 rounded-xl px-4 py-3 text-sm font-bold" style={{ background: "#7f1d1d66", color: "#fecaca" }}>
            {error}
          </p>
        )}

        {loading ? (
          <div className="grid min-h-[40vh] place-items-center">
            <Loader2 className="animate-spin" style={{ color: c.goldAccent }} />
          </div>
        ) : (
          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-3">
            {visibleCharacters.map(ch => (
              <article
                key={ch.id}
                className="rounded-2xl p-4"
                style={{ background: c.surface, border: `1px solid ${c.borderFaint}` }}
              >
                <div className="flex items-center gap-3">
                  <CharacterAvatar
                    slug={ch.slug}
                    emoji={ch.emoji}
                    name={ch.name}
                    langCode={langCode}
                    size={58}
                    fallbackBg={`${c.goldAccent}22`}
                  />
                  <div className="min-w-0 flex-1">
                    <h2 className="truncate text-base font-black" style={{ color: c.parchment }}>{ch.name}</h2>
                    <p className="truncate text-xs font-semibold" style={{ color: c.textFaint }}>{ch.role}</p>
                  </div>
                </div>
                <p className="mt-3 line-clamp-3 min-h-[3.75rem] text-sm leading-relaxed" style={{ color: c.textOnBg }}>
                  {ch.description || ch.quote || "Sem descricao."}
                </p>
                <button
                  type="button"
                  onClick={() => playSample(ch)}
                  disabled={playingId === ch.id || !sampleText.trim()}
                  className="mt-4 inline-flex h-10 w-full items-center justify-center gap-2 rounded-xl text-sm font-black transition active:scale-[0.98] disabled:opacity-60"
                  style={{ background: c.ctaBg, color: c.ctaText }}
                >
                  {playingId === ch.id ? <Loader2 size={16} className="animate-spin" /> : <Play size={16} />}
                  Ouvir voz atual
                </button>
                {models.length > 0 && (
                  <div className="mt-3 grid grid-cols-2 gap-2">
                    {models.map(model => (
                      <button
                        key={model.path}
                        type="button"
                        onClick={() => playSample(ch, model.path, model.length_scale)}
                        disabled={playingId === ch.id || !sampleText.trim()}
                        className="min-h-9 rounded-lg px-2 text-[11px] font-black transition active:scale-[0.98] disabled:opacity-60"
                        title={model.path}
                        style={{
                          background: c.surfaceMid,
                          color: c.textOnBg,
                          border: `1px solid ${c.borderFaint}`,
                        }}
                      >
                        {model.label ?? model.name}
                      </button>
                    ))}
                  </div>
                )}
              </article>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
