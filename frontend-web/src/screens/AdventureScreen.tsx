import { useEffect, useState } from "react";
import { Skull, Swords } from "lucide-react";

import StateMessage from "../components/ui/StateMessage";
import { useAsyncData } from "../hooks/useAsyncData";
import { useImmersiveNav } from "../hooks/useImmersiveNav";
import { ADVENTURE_CHAPTER_BASE } from "../constants/routes";
import { adventureService } from "../services/adventureService";
import type { AdventureChapter } from "../types/adventure";

type AdventureView = "loading" | "empty" | "chapter-intro";

export default function AdventureScreen() {
  const chaptersData = useAsyncData(adventureService.listChapters);
  const [view, setView] = useState<AdventureView>("loading");
  const [chapter, setChapter] = useState<AdventureChapter | null>(null);
  const { navigateImmersive } = useImmersiveNav();

  useEffect(() => {
    if (chaptersData.loading) return;
    if (!chaptersData.data?.length) {
      setView("empty");
      return;
    }
    setChapter(chaptersData.data[0]);
    setView((v) => (v === "loading" ? "chapter-intro" : v));
  }, [chaptersData.loading, chaptersData.data]);

  function enterChapter() {
    if (!chapter) return;
    navigateImmersive(
      `${ADVENTURE_CHAPTER_BASE}/${chapter.id}`,
      { chapter },
      { title: chapter.title, subtitle: `${chapter.level} · Entrando no mundo` },
    );
  }

  if (view === "loading") return <StateMessage />;

  if (view === "empty" || !chapter) {
    return (
      <StateMessage
        title="Sem capítulo disponível"
        detail="Ative uma área de estudo com alemão para liberar o modo aventura."
      />
    );
  }

  return (
    <div
      className="-mx-3 -mt-3 min-h-[calc(100dvh-3.5rem)] md:mx-0 md:mt-0 md:min-h-[72vh] md:rounded-[8px] relative overflow-hidden flex flex-col justify-end p-6 pb-28 md:p-10 md:pb-10"
      style={{ background: "linear-gradient(180deg, #0f0500 0%, #1c0c00 55%, #3d1a00 100%)" }}
    >
      <div
        className="pointer-events-none absolute inset-0"
        style={{ background: "radial-gradient(ellipse at 50% 25%, rgba(217,119,6,0.14), transparent 65%)" }}
      />
      <div className="relative z-10">
        <p className="text-[10px] font-bold uppercase tracking-widest text-amber-400">
          {chapter.level} · {chapter.language_code.toUpperCase()}
        </p>
        <h1 className="mt-2 text-4xl font-semibold leading-tight text-white md:text-5xl">{chapter.title}</h1>
        <p className="mt-3 text-lg font-medium leading-relaxed text-amber-200/75">{chapter.subtitle}</p>

        <div className="mt-8 rounded-[8px] border border-red-900/50 bg-red-950/30 p-4">
          <div className="flex items-center gap-2">
            <Skull size={15} className="text-red-400" />
            <p className="text-xs font-bold uppercase tracking-wide text-red-400">{chapter.boss_name}</p>
          </div>
          <p className="mt-2 text-sm font-medium leading-6 text-red-200/60">{chapter.boss_intro}</p>
        </div>

        <div className="mt-5 flex items-center gap-3">
          <div className="flex -space-x-1">
            {chapter.phases.slice(0, 10).map((p) => (
              <div
                key={p.id}
                className={`h-2.5 w-2.5 rounded-full ring-1 ring-amber-900 ${p.is_completed ? "bg-amber-400" : "bg-amber-950"}`}
              />
            ))}
          </div>
          <p className="text-xs font-semibold text-amber-400/70">{chapter.phases.length} fases</p>
        </div>

        <button
          type="button"
          onClick={enterChapter}
          className="mt-7 flex w-full items-center justify-center gap-2 rounded-[8px] bg-amber-500 px-6 py-4 text-base font-semibold text-white shadow-lg transition hover:bg-amber-400 active:scale-[0.98]"
        >
          <Swords size={18} />
          Iniciar Aventura
        </button>
      </div>
    </div>
  );
}
