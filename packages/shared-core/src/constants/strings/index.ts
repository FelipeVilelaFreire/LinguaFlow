import { DE_DE } from "./de-DE";
import { EN } from "./en";
import { PT_BR } from "./pt-BR";
import type { Locale } from "./types";

let currentLocale: Locale = "pt-BR";

export function setLocale(locale: Locale) {
  currentLocale = locale;
}

export function getStrings() {
  if (currentLocale === "en") return EN;
  if (currentLocale === "de-DE") return DE_DE;
  return PT_BR;
}

export const STRINGS = new Proxy(PT_BR, {
  get(_target, prop: keyof typeof PT_BR) {
    return getStrings()[prop];
  },
});

export type { Locale, Strings } from "./types";
