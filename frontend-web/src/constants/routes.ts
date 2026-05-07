import { BookMarked, BookOpen, LayoutDashboard, Swords, CircleUser } from "lucide-react";

import type { NavItem } from "../types/navigation";

export const ROUTES = {
  home: "/",
  adventure: "/aventura",
  adventureMap: "/aventura/mapa",
  adventureMochila: "/aventura/mochila",
  adventureHeroi: "/aventura/heroi",
  adventureChapterBase: "/aventura/capitulo",
  today: "/estudo-guiado",
  vocabulary: "/vocabulario",
  account: "/perfil",
  history: "/historico",
  editProfile: "/editperfil",
  login: "/login",
  onboarding: "/onboarding",
} as const;

export function adventureChapterPath(id: number): string {
  return `${ROUTES.adventureChapterBase}/${id}`;
}

export const NAV_ITEMS: NavItem[] = [
  { route: "home",       labelKey: "home",      icon: LayoutDashboard },
  { route: "adventure",  labelKey: "adventure", icon: Swords },
  { route: "today",      labelKey: "today",     icon: BookOpen },
  { route: "vocabulary", labelKey: "vocabulary",icon: BookMarked },
  { route: "account",    labelKey: "profile",   icon: CircleUser },
];
