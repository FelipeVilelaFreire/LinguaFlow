import type { PT_BR } from "./pt-BR";

type WidenStrings<T> = {
  [K in keyof T]: T[K] extends (...args: infer A) => string
    ? (...args: A) => string
    : T[K] extends string
      ? string
      : T[K] extends Record<string, unknown>
        ? WidenStrings<T[K]>
        : T[K];
};

export type Strings = WidenStrings<typeof PT_BR>;
export type Locale = "pt-BR" | "en" | "de-DE";
