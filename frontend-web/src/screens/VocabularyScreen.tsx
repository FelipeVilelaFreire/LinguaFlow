import { Heart, Trash2 } from "lucide-react";

import StateMessage from "../components/ui/StateMessage";
import { useStrings } from "../contexts/StringsContext";
import { useAsyncData } from "../hooks/useAsyncData";
import { contentService } from "../services/contentService";

export default function VocabularyScreen() {
  const strings = useStrings();
  const favorites = useAsyncData(contentService.listFavorites);

  async function removeFavorite(id: number) {
    await contentService.removeFavorite(id);
    favorites.reload();
  }

  if (favorites.loading) return <StateMessage />;
  if (favorites.error || !favorites.data) return <StateMessage title={strings.states.empty} detail={strings.states.apiHint} />;

  return (
    <div className="pb-20 md:pb-0">
      <header className="rounded-[8px] bg-white p-6 shadow-sm ring-1 ring-slate-200">
        <p className="flex items-center gap-2 text-sm font-semibold uppercase text-rose-600">
          <Heart size={18} />
          {strings.vocabulary.eyebrow}
        </p>
        <h2 className="mt-2 text-4xl font-semibold">{strings.vocabulary.title}</h2>
        <p className="mt-2 max-w-xl font-medium text-slate-600">{strings.vocabulary.subtitle}</p>
      </header>

      <section className="mt-6 rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
        {favorites.data.length === 0 ? <StateMessage title={strings.states.empty} /> : null}
        <div className="grid gap-3">
          {favorites.data.map((favorite) => (
            <div key={favorite.id} className="flex flex-col gap-3 rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-100 md:flex-row md:items-center md:justify-between">
              <div>
                <p className="text-xl font-semibold">{favorite.phrase.target_text}</p>
                <p className="mt-1 text-sm font-bold text-slate-500">{favorite.phrase.source_text}</p>
              </div>
              <button type="button" onClick={() => removeFavorite(favorite.id)} className="inline-flex items-center justify-center gap-2 rounded-[8px] bg-white px-3 py-2 text-sm font-semibold text-slate-700 ring-1 ring-slate-200 transition hover:bg-red-50 hover:text-red-700">
                <Trash2 size={16} />
                {strings.actions.remove}
              </button>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
