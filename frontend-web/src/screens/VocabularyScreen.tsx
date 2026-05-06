import { BookMarked, Trash2 } from "lucide-react";
import { useState } from "react";

import { useStrings } from "../contexts/StringsContext";
import { useAsyncData } from "../hooks/useAsyncData";
import { contentService } from "../services/contentService";

export default function VocabularyScreen() {
  const s = useStrings();
  const favorites = useAsyncData(contentService.listFavorites);
  const [filter, setFilter] = useState<string | null>(null);

  async function removeFavorite(id: number) {
    await contentService.removeFavorite(id);
    favorites.reload();
  }

  if (favorites.loading) {
    return (
      <div className="flex flex-col gap-3 pb-4">
        <HeaderSkeleton />
        {[1, 2, 3].map((i) => <CardSkeleton key={i} />)}
      </div>
    );
  }

  const data = favorites.data ?? [];
  const scenarios = Array.from(new Set(data.map((f) => f.phrase.scenario_title).filter(Boolean)));
  const filtered = filter ? data.filter((f) => f.phrase.scenario_title === filter) : data;

  return (
    <div className="pb-4">

      {/* Header */}
      <div className="mb-5">
        <p className="text-xs font-semibold uppercase tracking-wide area-text-primary">{s.vocabulary.eyebrow}</p>
        <h1 className="mt-1 text-2xl font-bold text-slate-950">{s.vocabulary.title}</h1>
        <p className="mt-1 text-sm font-medium text-slate-500">{s.vocabulary.subtitle}</p>
      </div>

      {/* Filter chips */}
      {scenarios.length > 0 && (
        <div className="mb-4 flex gap-2 overflow-x-auto pb-0.5" style={{ scrollbarWidth: "none" }}>
          <button
            type="button"
            onClick={() => setFilter(null)}
            className={`onb-pill shrink-0 ${filter === null ? "selected" : ""}`}
          >
            {s.vocabulary.filterAll}
            <span className="ml-1.5 rounded-full bg-current/10 px-1.5 py-px text-[10px] font-bold tabular-nums">
              {data.length}
            </span>
          </button>
          {scenarios.map((sc) => (
            <button
              key={sc}
              type="button"
              onClick={() => setFilter(filter === sc ? null : sc)}
              className={`onb-pill shrink-0 ${filter === sc ? "selected" : ""}`}
            >
              {sc}
            </button>
          ))}
        </div>
      )}

      {/* Empty state — sem nenhuma frase */}
      {data.length === 0 && (
        <div className="flex flex-col items-center gap-3 rounded-xl border border-dashed border-slate-200 bg-white px-6 py-14 text-center">
          <div className="flex h-12 w-12 items-center justify-center rounded-full area-bg-soft">
            <BookMarked size={22} className="area-text-primary" />
          </div>
          <div>
            <p className="font-bold text-slate-950">{s.vocabulary.emptyTitle}</p>
            <p className="mt-1 text-sm font-medium text-slate-500">{s.vocabulary.emptyDetail}</p>
          </div>
        </div>
      )}

      {/* Empty state — filtro sem resultado */}
      {data.length > 0 && filtered.length === 0 && (
        <p className="py-8 text-center text-sm font-medium text-slate-400">{s.vocabulary.filterEmpty}</p>
      )}

      {/* Lista de frases */}
      {filtered.length > 0 && (
        <div className="flex flex-col gap-2">
          {filtered.map((fav) => (
            <div key={fav.id} className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
              <p className="text-base font-bold text-slate-950">{fav.phrase.target_text}</p>
              <p className="mt-1 text-sm font-medium text-slate-500">{fav.phrase.source_text}</p>
              <div className="mt-3 flex items-center justify-between">
                {fav.phrase.scenario_title ? (
                  <span className="area-bg-soft rounded-full px-2.5 py-0.5 text-[11px] font-semibold">
                    {fav.phrase.scenario_title}
                  </span>
                ) : (
                  <span />
                )}
                <button
                  type="button"
                  onClick={() => removeFavorite(fav.id)}
                  className="flex h-8 w-8 items-center justify-center rounded-lg border border-red-100 bg-white text-red-400 transition hover:bg-red-50 hover:text-red-600"
                >
                  <Trash2 size={14} />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function HeaderSkeleton() {
  return (
    <div className="mb-5 flex flex-col gap-2">
      <div className="h-3 w-24 animate-pulse rounded-full bg-slate-100" />
      <div className="h-7 w-40 animate-pulse rounded-lg bg-slate-100" />
      <div className="h-4 w-56 animate-pulse rounded-full bg-slate-100" />
    </div>
  );
}

function CardSkeleton() {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
      <div className="h-5 w-3/4 animate-pulse rounded-lg bg-slate-100" />
      <div className="mt-2 h-4 w-1/2 animate-pulse rounded-full bg-slate-100" />
      <div className="mt-4 flex justify-between">
        <div className="h-5 w-20 animate-pulse rounded-full bg-slate-100" />
        <div className="h-8 w-8 animate-pulse rounded-lg bg-slate-100" />
      </div>
    </div>
  );
}
