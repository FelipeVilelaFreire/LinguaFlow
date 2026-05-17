import { AdventureChapterRunnerScreen } from "@/src/screens/AdventureChapterRunnerScreen";
import { useLocalSearchParams } from "expo-router";

export default function Page() {
  const params = useLocalSearchParams<{ phaseId: string }>();
  return <AdventureChapterRunnerScreen phaseId={Number(params.phaseId)} />;
}
