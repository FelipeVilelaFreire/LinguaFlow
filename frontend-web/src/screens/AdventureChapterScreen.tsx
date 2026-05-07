import { getAdventureColors } from "../theme/adventureColors";
import AdventurePhaseRunner from "./adventure/AdventurePhaseRunner";

const PROGRESS_KEY = "talkly_it_progress";

interface AdventureChapterScreenProps {
  chapterId: number;
  onBack: () => void;
}

export default function AdventureChapterScreen({ onBack }: AdventureChapterScreenProps) {
  const phaseNumber     = (window.history.state?.phaseNumber     as number | undefined) ?? 1;
  const langCode        = (window.history.state?.langCode        as string | undefined) ?? "IT";
  const chapterId       = (window.history.state?.chapterId       as number | undefined) ?? 1;
  const startSectionIdx = (window.history.state?.startSectionIdx as number | undefined) ?? 0;
  const c               = getAdventureColors(langCode, "dark");
  const bg              = `linear-gradient(180deg, ${c.bgFrom} 0%, ${c.bgMid} 55%, ${c.bgTo} 100%)`;

  function handleSectionComplete(newCount: number) {
    const saved = JSON.parse(localStorage.getItem(PROGRESS_KEY) ?? "{}") as Record<string, number>;
    saved[String(chapterId)] = newCount;
    localStorage.setItem(PROGRESS_KEY, JSON.stringify(saved));
    window.dispatchEvent(new CustomEvent("talkly:section_complete", { detail: { phaseId: chapterId, newCount } }));
  }

  return (
    <div className="h-dvh" style={{ background: bg }}>
      <AdventurePhaseRunner
        phaseNumber={phaseNumber}
        langCode={langCode}
        startSectionIdx={startSectionIdx}
        onSectionComplete={handleSectionComplete}
        onBack={onBack}
      />
    </div>
  );
}
