import type { ReactNode } from "react";
import type {
  AdminAdventure,
  AdminContent,
  AdminGoal,
  AdminLearningDetail,
  AdminProgressDetail,
  AdminSummary,
  AdminUser,
} from "../../types/admin";

export type AdminAppKey =
  | "dashboard"
  | "users"
  | "goals"
  | "content"
  | "learning"
  | "adventure"
  | "progress"
  | "business-plan"
  | "system";

export type AdminGroup = "operation" | "content" | "strategy" | "system";

export interface AdminDataset {
  summary: AdminSummary | null;
  users: AdminUser[];
  goals: AdminGoal[];
  content: AdminContent | null;
  learning: AdminLearningDetail | null;
  adventure: AdminAdventure | null;
  progress: AdminProgressDetail | null;
}

export interface AdminColumn<T> {
  key: string;
  label: string;
  value: (row: T) => ReactNode;
}

export interface AdminCardMetric {
  label: string;
  value: ReactNode;
  detail?: string;
}

export interface AdminAppConfig<T = unknown> {
  key: AdminAppKey;
  group: AdminGroup;
  icon: string;
  title: string;
  description: string;
  searchPlaceholder: string;
  getRecords: (data: AdminDataset) => T[];
  columns: AdminColumn<T>[];
  getMetrics?: (data: AdminDataset) => AdminCardMetric[];
  renderAside?: (data: AdminDataset) => ReactNode;
}
