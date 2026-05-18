import { STRINGS } from "@linguaflow/shared-core";
import { Badge } from "../../shared/components/Badge";
import type { AdminAppConfig } from "../../shared/types";

type LessonRecord = {
  id: number;
  title: string;
  day_number: number;
  scenario: string;
  module: string;
  objective: string;
  phrase_count: number;
  has_video: boolean;
};

export const learningConfig: AdminAppConfig<LessonRecord> = {
  key: "learning",
  group: "content",
  icon: "ST",
  title: STRINGS.admin.apps.learning.title,
  description: STRINGS.admin.apps.learning.description,
  searchPlaceholder: "Buscar aula, modulo ou cenario",
  getRecords: (data) => data.learning?.lessons ?? [],
  columns: [
    { key: "day", label: "Dia", value: (row) => row.day_number },
    { key: "title", label: STRINGS.admin.shared.fields.title, value: (row) => row.title },
    { key: "module", label: "Modulo", value: (row) => row.module || "-" },
    { key: "scenario", label: "Cenario", value: (row) => row.scenario },
    { key: "phrases", label: "Frases", value: (row) => row.phrase_count },
    { key: "video", label: "Video", value: (row) => <Badge tone={row.has_video ? "good" : "neutral"}>{row.has_video ? STRINGS.admin.shared.status.yes : STRINGS.admin.shared.status.no}</Badge> },
  ],
  getMetrics: (data) => [
    { label: "Modulos", value: data.learning?.modules.length ?? 0 },
    { label: "Aulas", value: data.summary?.lessons ?? 0 },
    { label: "Study days", value: data.summary?.study_days ?? 0 },
  ],
};
