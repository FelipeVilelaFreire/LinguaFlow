import type { LucideIcon } from "lucide-react";
import type { AppStrings } from "../constants/strings";

export type AppRoute = "home" | "today" | "history" | "scenarios" | "vocabulary" | "account";

export interface NavItem {
  route: AppRoute;
  labelKey: keyof AppStrings["nav"];
  icon: LucideIcon;
}
