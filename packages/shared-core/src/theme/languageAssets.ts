export type FlagSize = "xs" | "sm" | "md" | "lg" | "xl";

export const LANG_TO_FLAG_ISO: Record<string, string> = {
  AR: "sa",
  DE: "de",
  EN: "us",
  ES: "es",
  FR: "fr",
  IT: "it",
  JA: "jp",
  KO: "kr",
  NL: "nl",
  PL: "pl",
  PT: "br",
  RU: "ru",
  SV: "se",
  ZH: "cn",
};

export const FLAG_SIZE_MAP: Record<FlagSize, { width: number; height: number; cdn: number; radius: number }> = {
  xs: { width: 18, height: 12, cdn: 40, radius: 4 },
  sm: { width: 26, height: 17, cdn: 40, radius: 4 },
  md: { width: 34, height: 23, cdn: 40, radius: 8 },
  lg: { width: 46, height: 31, cdn: 80, radius: 12 },
  xl: { width: 58, height: 39, cdn: 80, radius: 12 },
};

export function getFlagIso(code: string): string {
  return LANG_TO_FLAG_ISO[code.toUpperCase()] ?? code.toLowerCase().slice(0, 2);
}

export function getFlagImage(code: string, size: FlagSize = "md") {
  const iso = getFlagIso(code);
  const dimensions = FLAG_SIZE_MAP[size];

  return {
    ...dimensions,
    iso,
    src: `https://flagcdn.com/w${dimensions.cdn}/${iso}.png`,
    srcSet: `https://flagcdn.com/w${dimensions.cdn * 2}/${iso}.png 2x`,
  };
}

export const CHARACTER_IMAGE_ALIASES: Record<string, string[]> = {
  rosa_panadera: ["rosa"],
};

export function getCharacterImageCandidates({
  langCode = "es",
  slug,
}: {
  langCode?: string;
  slug?: string | null;
}): string[] {
  if (!slug) return [];
  const lang = langCode.toLowerCase();
  const slugs = [slug, ...(CHARACTER_IMAGE_ALIASES[slug] ?? [])];
  return slugs.flatMap((imageSlug) => [
    `/${lang}/characters/${imageSlug}.png`,
    `/${lang}/characters/${imageSlug}.jpg`,
  ]);
}
