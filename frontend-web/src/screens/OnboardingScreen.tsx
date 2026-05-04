import { ArrowRight, Check, Flag } from "lucide-react";
import { useState } from "react";

import { contentService } from "../services/contentService";
import { useStrings } from "../contexts/StringsContext";
import type { Goal } from "../types/content";

interface OnboardingScreenProps {
  onComplete: (goal: Goal) => void;
}

export default function OnboardingScreen({ onComplete }: OnboardingScreenProps) {
  const strings = useStrings();
  const [duration, setDuration] = useState(30);
  const [loading, setLoading] = useState(false);

  async function start() {
    setLoading(true);
    const goal = await contentService.createGoal({
      source_language: "PT",
      target_language: "DE",
      target_level: "A1",
      duration_days: duration,
    });
    onComplete(goal);
  }

  return (
    <main className="min-h-screen bg-slate-50 px-5 py-8 text-slate-950">
      <section className="mx-auto max-w-4xl">
        <div className="rounded-[8px] bg-white p-6 shadow-sm ring-1 ring-slate-200">
          <div className="flex items-center gap-4">
            <div className="grid h-14 w-14 place-items-center rounded-[8px] bg-emerald-50 text-emerald-700 ring-1 ring-emerald-100">
              <Flag />
            </div>
            <div>
              <p className="text-sm font-semibold uppercase text-emerald-700">{strings.onboarding.eyebrow}</p>
              <h1 className="text-3xl font-semibold">{strings.onboarding.title}</h1>
            </div>
          </div>

          <div className="mt-8 grid gap-4 md:grid-cols-3">
            <Choice title={strings.onboarding.source} value="Portugues" detail="Voce entende a explicacao em PT" />
            <Choice title={strings.onboarding.target} value="Alemao A1" detail="Frases reais para rotina" />
            <Choice title={strings.onboarding.session} value="10-15 min" detail="Estudo guiado diario" />
          </div>

          <div className="mt-8 rounded-[8px] bg-slate-50 p-5 ring-1 ring-slate-200">
            <label className="text-sm font-semibold uppercase text-slate-500">{strings.onboarding.duration}</label>
            <div className="mt-4 flex flex-wrap gap-3">
              {[30, 60, 90].map((item) => (
                <button key={item} type="button" onClick={() => setDuration(item)} className={`rounded-[8px] px-5 py-3 font-semibold ring-1 transition ${duration === item ? "bg-emerald-600 text-white ring-emerald-600" : "bg-white ring-slate-200 hover:bg-slate-50"}`}>
                  {item} dias
                </button>
              ))}
            </div>
          </div>

          <button type="button" onClick={start} disabled={loading} className="mt-7 flex h-14 w-full items-center justify-center gap-2 rounded-[8px] bg-emerald-600 font-semibold text-white shadow-sm transition hover:bg-emerald-700">
            {loading ? strings.actions.creating : strings.onboarding.start}
            <ArrowRight size={18} />
          </button>
        </div>
      </section>
    </main>
  );
}

function Choice({ title, value, detail }: { title: string; value: string; detail: string }) {
  return (
    <div className="rounded-[8px] bg-white p-4 ring-1 ring-slate-200">
      <Check className="text-emerald-500" />
      <p className="mt-4 text-sm font-semibold uppercase text-slate-500">{title}</p>
      <p className="text-xl font-semibold">{value}</p>
      <p className="mt-1 text-sm font-medium text-slate-500">{detail}</p>
    </div>
  );
}
