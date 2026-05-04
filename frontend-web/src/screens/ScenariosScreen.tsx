import { Heart, MapPinned } from "lucide-react";
import { useState } from "react";

import StateMessage from "../components/ui/StateMessage";
import { useStrings } from "../contexts/StringsContext";
import { useAsyncData } from "../hooks/useAsyncData";
import { contentService } from "../services/contentService";

export default function ScenariosScreen() {
  const strings = useStrings();
  const [selectedScenario, setSelectedScenario] = useState<string | null>(null);
  const scenarios = useAsyncData(contentService.listScenarios);
  const phrases = useAsyncData(() => contentService.listPhrases(selectedScenario ?? undefined), [selectedScenario]);

  if (scenarios.loading) return <StateMessage />;
  if (scenarios.error || !scenarios.data) return <StateMessage title={strings.states.empty} detail={strings.states.apiHint} />;

  return (
    <div className="pb-20 md:pb-0">
      <header className="rounded-[8px] bg-white p-6 shadow-sm ring-1 ring-slate-200">
        <p className="flex items-center gap-2 text-sm font-semibold uppercase text-emerald-700">
          <MapPinned size={18} />
          {strings.scenarios.eyebrow}
        </p>
        <h2 className="mt-2 text-4xl font-semibold">{strings.scenarios.title}</h2>
        <p className="mt-2 max-w-xl font-medium text-slate-600">{strings.scenarios.subtitle}</p>
      </header>

      <div className="mt-6 grid gap-3 md:grid-cols-2 lg:grid-cols-3">
        {scenarios.data.map((scenario) => (
          <button key={scenario.slug} type="button" onClick={() => setSelectedScenario(scenario.slug)} className={`rounded-[8px] p-5 text-left shadow-sm ring-1 transition hover:-translate-y-0.5 ${selectedScenario === scenario.slug ? "bg-slate-950 text-white ring-slate-950" : "bg-white ring-slate-200 hover:ring-emerald-200"}`}>
            <h3 className="text-xl font-semibold">{scenario.title}</h3>
            <p className={`mt-2 text-sm font-bold ${selectedScenario === scenario.slug ? "text-slate-300" : "text-slate-700"}`}>{scenario.description}</p>
            <p className="mt-4 text-xs font-semibold uppercase">{scenario.phrase_count} frases</p>
          </button>
        ))}
      </div>

      <section className="mt-6 rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
        {phrases.loading ? <StateMessage /> : null}
        <div className="grid gap-3 md:grid-cols-2">
          {phrases.data?.map((phrase) => (
            <div key={phrase.id} className="rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-100 transition hover:ring-slate-200">
              <div className="flex justify-between gap-3">
                <div>
                  <p className="text-lg font-semibold">{phrase.target_text}</p>
                  <p className="mt-1 text-sm font-bold text-slate-500">{phrase.source_text}</p>
                </div>
                <button type="button" onClick={() => contentService.favoritePhrase(phrase.id)} className="grid h-9 w-9 shrink-0 place-items-center rounded-[8px] bg-rose-50 text-rose-600 ring-1 ring-rose-100">
                  <Heart size={16} />
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
