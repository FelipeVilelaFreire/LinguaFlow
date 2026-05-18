import { STRINGS } from "@linguaflow/shared-core";
import type { AdminAppConfig } from "../../shared/types";

type DashboardRecord = { label: string; value: number; detail: string };

export const dashboardConfig: AdminAppConfig<DashboardRecord> = {
  key: "dashboard",
  group: "operation",
  icon: "DB",
  title: STRINGS.admin.apps.dashboard.title,
  description: STRINGS.admin.apps.dashboard.description,
  searchPlaceholder: STRINGS.admin.app.search,
  getRecords: (data) => [
    { label: STRINGS.admin.apps.users.title, value: data.summary?.users ?? 0, detail: `${data.summary?.staff_users ?? 0} staff` },
    { label: STRINGS.admin.apps.goals.title, value: data.summary?.active_goals ?? 0, detail: `${data.summary?.goals ?? 0} totais` },
    { label: "Frases", value: data.summary?.phrases ?? 0, detail: `${data.summary?.lessons ?? 0} aulas` },
    { label: "Conclusoes", value: data.summary?.completions ?? 0, detail: `${data.summary?.progress_entries ?? 0} SRS` },
  ],
  columns: [
    { key: "label", label: STRINGS.admin.shared.fields.title, value: (row) => row.label },
    { key: "value", label: STRINGS.admin.shared.fields.total, value: (row) => row.value },
    { key: "detail", label: STRINGS.admin.shared.fields.description, value: (row) => row.detail },
  ],
  getMetrics: (data) => [
    { label: STRINGS.admin.apps.users.title, value: data.summary?.users ?? 0 },
    { label: STRINGS.admin.apps.content.title, value: data.summary?.phrases ?? 0, detail: "frases" },
    { label: STRINGS.admin.apps.adventure.title, value: data.adventure?.phases.length ?? 0, detail: "fases" },
    { label: STRINGS.admin.apps.progress.title, value: data.summary?.completions ?? 0, detail: "conclusoes" },
  ],
};
