import { BookOpen, CalendarCheck, History, Home, Library, Settings } from "lucide-react";

import type { NavItem } from "../types/navigation";

export const NAV_ITEMS: NavItem[] = [
  { route: "home", labelKey: "home", icon: Home },
  { route: "today", labelKey: "today", icon: CalendarCheck },
  { route: "history", labelKey: "history", icon: History },
  { route: "scenarios", labelKey: "scenarios", icon: BookOpen },
  { route: "vocabulary", labelKey: "vocabulary", icon: Library },
  { route: "account", labelKey: "profile", icon: Settings },
];

export const ROUTE_PATHS = {
  home: "/",
  today: "/estudo-guiado",
  history: "/historico",
  scenarios: "/cenarios",
  vocabulary: "/vocabulario",
  account: "/perfil",
} as const;

export const AUTH_PATHS = {
  login: "/login",
  onboarding: "/onboarding",
} as const;
