import type { LucideIcon } from "lucide-react";
import type { AppStrings } from "../constants/strings";

export type AppRoute =
  | "home"
  | "adventure"
  | "adventure-map"
  | "adventure-mochila"
  | "adventure-palavras"
  | "adventure-heroi"
  | "adventure-personagens"
  | "adventure-chapter"
  | "today"
  | "vocabulary"
  | "account"
  | "history"
  | "editprofile";

export interface NavItem {
  route: AppRoute;
  labelKey: keyof AppStrings["nav"];
  icon: LucideIcon;
}
