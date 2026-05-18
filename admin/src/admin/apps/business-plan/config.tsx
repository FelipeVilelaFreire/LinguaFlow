import { STRINGS } from "@linguaflow/shared-core";
import { Badge } from "../../shared/components/Badge";
import type { AdminAppConfig } from "../../shared/types";
import { formatCurrency } from "../../shared/utils/format";

type BusinessPlanRecord = {
  scenario: string;
  activeUsers: number;
  payingUsers: number;
  monthlyPrice: number;
  costs: number;
  risk: "alto" | "medio" | "baixo";
};

const RECORDS: BusinessPlanRecord[] = [
  { scenario: STRINGS.admin.businessPlan.pessimistic, activeUsers: 250, payingUsers: 8, monthlyPrice: 19, costs: 850, risk: "alto" },
  { scenario: STRINGS.admin.businessPlan.realistic, activeUsers: 900, payingUsers: 45, monthlyPrice: 24, costs: 1450, risk: "medio" },
  { scenario: STRINGS.admin.businessPlan.optimistic, activeUsers: 2400, payingUsers: 180, monthlyPrice: 29, costs: 3200, risk: "baixo" },
];

export const businessPlanConfig: AdminAppConfig<BusinessPlanRecord> = {
  key: "business-plan",
  group: "strategy",
  icon: "BP",
  title: STRINGS.admin.apps.businessPlan.title,
  description: STRINGS.admin.apps.businessPlan.description,
  searchPlaceholder: "Buscar cenario",
  getRecords: () => RECORDS,
  columns: [
    { key: "scenario", label: STRINGS.admin.businessPlan.scenario, value: (row) => row.scenario },
    { key: "active", label: STRINGS.admin.businessPlan.activeUsers, value: (row) => row.activeUsers },
    { key: "paying", label: STRINGS.admin.businessPlan.payingUsers, value: (row) => row.payingUsers },
    { key: "price", label: STRINGS.admin.businessPlan.monthlyPrice, value: (row) => formatCurrency(row.monthlyPrice) },
    { key: "mrr", label: STRINGS.admin.businessPlan.mrr, value: (row) => formatCurrency(row.payingUsers * row.monthlyPrice) },
    { key: "costs", label: STRINGS.admin.businessPlan.costs, value: (row) => formatCurrency(row.costs) },
    { key: "risk", label: STRINGS.admin.businessPlan.risk, value: (row) => <Badge tone={row.risk === "baixo" ? "good" : row.risk === "medio" ? "neutral" : "warn"}>{row.risk}</Badge> },
  ],
  getMetrics: () => [
    { label: STRINGS.admin.businessPlan.assumptions, value: 3, detail: "usuarios, preco, custos" },
    { label: STRINGS.admin.businessPlan.validation, value: 7, detail: "acoes em docs/BUSINESS-MODEL.md" },
    { label: STRINGS.admin.businessPlan.runway, value: "manual", detail: "proxima etapa: editar premissas no admin" },
  ],
};
