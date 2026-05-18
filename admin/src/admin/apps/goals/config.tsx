import { STRINGS } from "@linguaflow/shared-core";
import { Badge } from "../../shared/components/Badge";
import type { AdminAppConfig } from "../../shared/types";
import { formatWeekdays } from "../../shared/utils/format";
import type { AdminGoal } from "../../../types/admin";

const F = STRINGS.admin.shared.fields;
const S = STRINGS.admin.shared.status;

export const goalsConfig: AdminAppConfig<AdminGoal> = {
  key: "goals",
  group: "operation",
  icon: "AR",
  title: STRINGS.admin.apps.goals.title,
  description: STRINGS.admin.apps.goals.description,
  searchPlaceholder: "Buscar por usuario, idioma ou nivel",
  getRecords: (data) => data.goals,
  columns: [
    { key: "id", label: F.id, value: (row) => row.id },
    { key: "user", label: F.user, value: (row) => row.user ?? "-" },
    { key: "course", label: "Curso", value: (row) => `${row.source_language} -> ${row.target_language}` },
    { key: "level", label: F.level, value: (row) => `${row.current_level} -> ${row.target_level}` },
    { key: "routine", label: "Rotina", value: (row) => `${formatWeekdays(row.study_weekdays)} / ${row.session_minutes} min` },
    { key: "progress", label: "Progresso", value: (row) => `${row.learned_phrases}/${row.total_phrases}` },
    { key: "status", label: F.status, value: (row) => <Badge tone={row.is_active ? "good" : "warn"}>{row.is_active ? S.active : S.inactive}</Badge> },
  ],
  getMetrics: (data) => [
    { label: "Areas ativas", value: data.summary?.active_goals ?? 0 },
    { label: "Areas totais", value: data.summary?.goals ?? 0 },
    { label: "Streak medio", value: Math.round(data.goals.reduce((sum, goal) => sum + goal.streak_days, 0) / Math.max(data.goals.length, 1)) },
  ],
};
