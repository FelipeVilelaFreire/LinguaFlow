import { STRINGS } from "@linguaflow/shared-core";
import { Badge } from "../../shared/components/Badge";
import type { AdminAppConfig } from "../../shared/types";
import { formatDate } from "../../shared/utils/format";

type ProgressRecord = {
  id: number;
  user: string;
  phrase: string;
  status: string;
  correct_count: number;
  incorrect_count: number;
  review_due: string | null;
};

export const progressConfig: AdminAppConfig<ProgressRecord> = {
  key: "progress",
  group: "operation",
  icon: "PR",
  title: STRINGS.admin.apps.progress.title,
  description: STRINGS.admin.apps.progress.description,
  searchPlaceholder: "Buscar usuario, frase ou status",
  getRecords: (data) => data.progress?.progress_entries ?? [],
  columns: [
    { key: "user", label: STRINGS.admin.shared.fields.user, value: (row) => row.user || "-" },
    { key: "phrase", label: "Frase", value: (row) => row.phrase },
    { key: "status", label: STRINGS.admin.shared.fields.status, value: (row) => <Badge>{row.status}</Badge> },
    { key: "correct", label: "Acertos", value: (row) => row.correct_count },
    { key: "wrong", label: "Erros", value: (row) => row.incorrect_count },
    { key: "review", label: "Revisao", value: (row) => formatDate(row.review_due) },
  ],
  getMetrics: (data) => [
    { label: "Conclusoes", value: data.progress?.completions.length ?? 0 },
    { label: "SRS", value: data.progress?.progress_entries.length ?? 0 },
    { label: "Maestria", value: data.progress?.word_mastery.length ?? 0 },
    { label: "Streaks", value: data.progress?.streaks.length ?? 0 },
  ],
};
