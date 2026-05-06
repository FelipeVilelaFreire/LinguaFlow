import { CalendarCheck, Compass, Home, Library, Settings } from "lucide-react";

import type { NavItem } from "../types/navigation";

export const NAV_ITEMS: NavItem[] = [
  { route: "home", labelKey: "home", icon: Home },
  { route: "adventure", labelKey: "adventure", icon: Compass },
  { route: "today", labelKey: "today", icon: CalendarCheck },
  { route: "vocabulary", labelKey: "vocabulary", icon: Library },
  { route: "account", labelKey: "profile", icon: Settings },
];

export const ROUTE_PATHS = {
  home: "/",
  adventure: "/aventura",
  today: "/estudo-guiado",
  vocabulary: "/vocabulario",
  account: "/perfil",
  history: "/historico",
} as const;

export const ADVENTURE_CHAPTER_BASE = "/aventura/capitulo";

export const AUTH_PATHS = {
  login: "/login",
  onboarding: "/onboarding",
} as const;
