import { createContext, useContext } from "react";
import type { ReactNode } from "react";

import { STRINGS, STRINGS_BY_LOCALE, type AppLocale, type AppStrings } from "../constants/strings";

const StringsContext = createContext<{ strings: AppStrings; locale: AppLocale }>({ strings: STRINGS, locale: "pt" });

interface StringsProviderProps {
  children: ReactNode;
  locale: AppLocale;
}

export function StringsProvider({ children, locale }: StringsProviderProps) {
  return <StringsContext.Provider value={{ strings: STRINGS_BY_LOCALE[locale], locale }}>{children}</StringsContext.Provider>;
}

export function useStrings() {
  return useContext(StringsContext).strings;
}

export function useLocale() {
  return useContext(StringsContext).locale;
}
