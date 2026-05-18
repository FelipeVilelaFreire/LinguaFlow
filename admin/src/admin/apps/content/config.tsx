import { STRINGS } from "@linguaflow/shared-core";
import type { AdminAppConfig } from "../../shared/types";

type ContentRecord = { id: number; slug: string; title: string; phrase_count: number; lesson_count: number };

export const contentConfig: AdminAppConfig<ContentRecord> = {
  key: "content",
  group: "content",
  icon: "CT",
  title: STRINGS.admin.apps.content.title,
  description: STRINGS.admin.apps.content.description,
  searchPlaceholder: "Buscar cenario ou slug",
  getRecords: (data) => data.content?.scenarios ?? [],
  columns: [
    { key: "title", label: STRINGS.admin.shared.fields.title, value: (row) => row.title },
    { key: "slug", label: "Slug", value: (row) => row.slug },
    { key: "phrases", label: "Frases", value: (row) => row.phrase_count },
    { key: "lessons", label: "Aulas", value: (row) => row.lesson_count },
  ],
  getMetrics: (data) => [
    { label: "Idiomas", value: data.summary?.languages ?? 0 },
    { label: "Cenarios", value: data.summary?.scenarios ?? 0 },
    { label: "Frases", value: data.summary?.phrases ?? 0 },
  ],
};
