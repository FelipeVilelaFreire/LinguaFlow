import { Heart } from "lucide-react";
import { useState } from "react";

import StateMessage from "../../../components/ui/StateMessage";
import { useStrings } from "../../../contexts/StringsContext";
import { useAsyncData } from "../../../hooks/useAsyncData";
import { contentService } from "../../../services/contentService";

interface ScenariosScreenProps {
  hideHeader?: boolean;
}

export default function ScenariosScreen({ hideHeader }: ScenariosScreenProps = {}) {
  const s = useStrings();
  const [selectedScenario, setSelectedScenario] = useState<string | null>(null);
  const scenarios = useAsyncData(contentService.listScenarios);
  const phrases = useAsyncData(() => contentService.listPhrases(selectedScenario ?? undefined), [selectedScenario]);

  if (scenarios.loading) return <StateMessage />;
  if (scenarios.error || !scenarios.data) return <StateMessage title={s.states.empty} detail={s.states.apiHint} />;

  return (
    <div className="pb-4">

      {/* Header */}
      {!hideHeader && (
        <div className="mb-5">
          <p className="text-xs font-semibold uppercase tracking-wide area-text-primary">{s.scenarios.eyebrow}</p>
          <h1 className="mt-1 text-2xl font-bold text-slate-950">{s.scenarios.title}</h1>
          <p className="mt-1 text-sm font-medium text-slate-500">{s.scenarios.subtitle}</p>
        </div>
      )}

      {/* Scenario grid */}
      <div className="grid grid-cols-2 gap-2">
        {scenarios.data.map((scenario) => {
          const isSelected = selectedScenario === scenario.slug;
          return (
            <button
              key={scenario.slug}
              type="button"
              onClick={() => setSelectedScenario(isSelected ? null : scenario.slug)}
              className={`rounded-xl border p-4 text-left transition ${
                isSelected
                  ? "border-transparent text-white"
                  : "border-slate-200 bg-white hover:border-slate-300"
              }`}
              style={isSelected ? { background: "var(--area-primary)" } : undefined}
            >
              <h3 className={`text-sm font-bold ${isSelected ? "text-white" : "text-slate-950"}`}>
                {scenario.title}
              </h3>
              <p className={`mt-1 line-clamp-2 text-xs font-medium ${isSelected ? "text-white/80" : "text-slate-500"}`}>
                {scenario.description}
              </p>
              <p className={`mt-3 text-[11px] font-bold uppercase tracking-wide ${isSelected ? "text-white/70" : "area-text-primary"}`}>
                {s.scenarios.phrasesCount(scenario.phrase_count)}
              </p>
            </button>
          );
        })}
      </div>

      {/* Phrase list */}
      {!selectedScenario && (
        <p className="mt-6 text-center text-sm font-medium text-slate-400">{s.scenarios.selectPrompt}</p>
      )}

      {selectedScenario && (
        <div className="mt-4">
          {phrases.loading && <StateMessage />}
          {phrases.data && (
            <div className="flex flex-col gap-2">
              {phrases.data.map((phrase) => (
                <div key={phrase.id} className="card p-4">
                  <div className="flex items-start justify-between gap-3">
                    <div>
                      <p className="text-base font-bold text-slate-950">{phrase.target_text}</p>
                      <p className="mt-1 text-sm font-medium text-slate-500">{phrase.source_text}</p>
                    </div>
                    <button
                      type="button"
                      onClick={() => contentService.favoritePhrase(phrase.id)}
                      className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-red-100 bg-white text-red-400 transition hover:bg-red-50 hover:text-red-600"
                    >
                      <Heart size={15} />
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
