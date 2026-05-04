import { createContext, useContext } from "react";
import type { ReactNode } from "react";

import { STRINGS, STRINGS_BY_LOCALE, type AppLocale, type AppStrings } from "../constants/strings";

const StringsContext = createContext<AppStrings>(STRINGS);

interface StringsProviderProps {
  children: ReactNode;
  locale: AppLocale;
}

export function StringsProvider({ children, locale }: StringsProviderProps) {
  return <StringsContext.Provider value={STRINGS_BY_LOCALE[locale]}>{children}</StringsContext.Provider>;
}

export function useStrings() {
  return useContext(StringsContext);
}
