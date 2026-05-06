import { useState } from "react";

import { useStrings } from "../contexts/StringsContext";
import ScenariosScreen from "./ScenariosScreen";
import TodayScreen from "./TodayScreen";

interface StudyScreenProps {
  onCompleted: () => void;
}

export default function StudyScreen({ onCompleted }: StudyScreenProps) {
  const s = useStrings();
  const [tab, setTab] = useState<"session" | "scenarios">("session");

  return (
    <div>
      <div className="mb-4 grid grid-cols-2 gap-1 rounded-[8px] bg-slate-100 p-1">
        <button
          type="button"
          onClick={() => setTab("session")}
          className={`h-10 rounded-[6px] text-sm font-semibold transition ${tab === "session" ? "bg-white text-slate-950 shadow-sm" : "text-slate-500 hover:text-slate-700"}`}
        >
          {s.today.tabSession}
        </button>
        <button
          type="button"
          onClick={() => setTab("scenarios")}
          className={`h-10 rounded-[6px] text-sm font-semibold transition ${tab === "scenarios" ? "bg-white text-slate-950 shadow-sm" : "text-slate-500 hover:text-slate-700"}`}
        >
          {s.today.tabScenarios}
        </button>
      </div>
      {tab === "session" ? <TodayScreen onCompleted={onCompleted} /> : <ScenariosScreen />}
    </div>
  );
}
