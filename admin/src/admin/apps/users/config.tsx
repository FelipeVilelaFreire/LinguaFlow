import { STRINGS } from "@linguaflow/shared-core";
import { Badge } from "../../shared/components/Badge";
import type { AdminAppConfig } from "../../shared/types";
import { formatDate } from "../../shared/utils/format";
import type { AdminUser } from "../../../types/admin";

const F = STRINGS.admin.shared.fields;
const S = STRINGS.admin.shared.status;

export const usersConfig: AdminAppConfig<AdminUser> = {
  key: "users",
  group: "operation",
  icon: "US",
  title: STRINGS.admin.apps.users.title,
  description: STRINGS.admin.apps.users.description,
  searchPlaceholder: "Buscar por usuario, email ou ID",
  getRecords: (data) => data.users,
  columns: [
    { key: "id", label: F.id, value: (row) => row.id },
    { key: "username", label: F.user, value: (row) => row.username },
    { key: "email", label: F.email, value: (row) => row.email || "-" },
    { key: "access", label: "Acesso", value: (row) => <Badge tone={row.is_staff ? "good" : "neutral"}>{row.is_staff ? S.staff : S.student}</Badge> },
    { key: "status", label: F.status, value: (row) => <Badge tone={row.is_active ? "good" : "warn"}>{row.is_active ? S.active : S.inactive}</Badge> },
    { key: "goals", label: STRINGS.admin.apps.goals.title, value: (row) => row.goal_count },
    { key: "joined", label: F.created, value: (row) => formatDate(row.date_joined) },
  ],
  getMetrics: (data) => [
    { label: STRINGS.admin.apps.users.title, value: data.summary?.users ?? 0 },
    { label: S.staff, value: data.summary?.staff_users ?? 0 },
    { label: S.active, value: data.users.filter((user) => user.is_active).length },
  ],
};
