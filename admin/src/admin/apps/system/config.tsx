import { STRINGS } from "@linguaflow/shared-core";
import { Badge } from "../../shared/components/Badge";
import type { AdminAppConfig } from "../../shared/types";

type SystemRecord = { name: string; label: string; models: string; status: string };

const RECORDS: SystemRecord[] = [
  { name: "accounts", label: "Contas", models: "Usuarios, autenticacao e admin dashboard", status: STRINGS.admin.shared.status.connected },
  { name: "goals", label: "Areas de estudo", models: "Objetivos, idioma fonte/alvo e rotina", status: STRINGS.admin.shared.status.connected },
  { name: "learning", label: "Estudo", models: "Idiomas, cenarios, frases, aulas e study days", status: STRINGS.admin.shared.status.connected },
  { name: "progress", label: "Progresso", models: "Favoritos, conclusoes, SRS e streaks", status: STRINGS.admin.shared.status.connected },
  { name: "adventure", label: "Aventura", models: "Capitulos, fases, personagens, itens e baus", status: STRINGS.admin.shared.status.connected },
];

export const systemConfig: AdminAppConfig<SystemRecord> = {
  key: "system",
  group: "system",
  icon: "SY",
  title: STRINGS.admin.apps.system.title,
  description: STRINGS.admin.apps.system.description,
  searchPlaceholder: "Buscar app Django",
  getRecords: () => RECORDS,
  columns: [
    { key: "name", label: STRINGS.admin.shared.fields.name, value: (row) => <code>{row.name}</code> },
    { key: "label", label: STRINGS.admin.shared.fields.title, value: (row) => row.label },
    { key: "models", label: STRINGS.admin.shared.fields.description, value: (row) => row.models },
    { key: "status", label: STRINGS.admin.shared.fields.status, value: (row) => <Badge tone="good">{row.status}</Badge> },
  ],
};
