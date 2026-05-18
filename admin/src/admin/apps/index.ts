import { adventureConfig } from "./adventure/config";
import { businessPlanConfig } from "./business-plan/config";
import { contentConfig } from "./content/config";
import { dashboardConfig } from "./dashboard/config";
import { goalsConfig } from "./goals/config";
import { learningConfig } from "./learning/config";
import { progressConfig } from "./progress/config";
import { systemConfig } from "./system/config";
import { usersConfig } from "./users/config";
import type { AdminAppConfig } from "../shared/types";

export const ADMIN_APPS: AdminAppConfig<any>[] = [
  dashboardConfig,
  usersConfig,
  goalsConfig,
  contentConfig,
  learningConfig,
  adventureConfig,
  progressConfig,
  businessPlanConfig,
  systemConfig,
] as const;
