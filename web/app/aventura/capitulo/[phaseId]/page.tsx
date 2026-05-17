import { AdventureChapterRunnerScreen } from "@/src/screens/AdventureChapterRunnerScreen";

export default async function Page({ params }: { params: Promise<{ phaseId: string }> }) {
  const { phaseId } = await params;
  return <AdventureChapterRunnerScreen phaseId={Number(phaseId)} />;
}
