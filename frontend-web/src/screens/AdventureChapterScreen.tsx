import { getAdventureColors } from "../theme/adventureColors";
import AdventureChapterSections from "./adventure/AdventureChapterSections";

interface AdventureChapterScreenProps {
  chapterId: number;
  onBack: () => void;
}

export default function AdventureChapterScreen({ onBack }: AdventureChapterScreenProps) {
  const phaseNumber = (window.history.state?.phaseNumber as number | undefined) ?? 1;
  const langCode    = (window.history.state?.langCode    as string | undefined) ?? "IT";
  const c           = getAdventureColors(langCode, "dark");
  const bg          = `linear-gradient(180deg, ${c.bgFrom} 0%, ${c.bgMid} 55%, ${c.bgTo} 100%)`;

  return (
    <div className="h-dvh" style={{ background: bg }}>
      <AdventureChapterSections phaseNumber={phaseNumber} langCode={langCode} onBack={onBack} />
    </div>
  );
}
