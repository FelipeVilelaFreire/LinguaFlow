const LANG_TO_ISO: Record<string, string> = {
  DE: "de",
  ES: "es",
  EN: "us",
  PT: "br",
  FR: "fr",
  IT: "it",
  ZH: "cn",
  JA: "jp",
  RU: "ru",
  NL: "nl",
  PL: "pl",
  SV: "se",
  KO: "kr",
  AR: "sa",
};

type FlagSize = "xs" | "sm" | "md" | "lg" | "xl";

const SIZE_MAP: Record<FlagSize, { w: number; h: number; cdn: number; radius: string }> = {
  xs: { w: 18, h: 12, cdn: 40,  radius: "rounded" },
  sm: { w: 26, h: 17, cdn: 40,  radius: "rounded" },
  md: { w: 34, h: 23, cdn: 40,  radius: "rounded-md" },
  lg: { w: 46, h: 31, cdn: 80,  radius: "rounded-lg" },
  xl: { w: 58, h: 39, cdn: 80,  radius: "rounded-lg" },
};

interface LangFlagProps {
  code: string;
  size?: FlagSize;
  className?: string;
}

export default function LangFlag({ code, size = "md", className = "" }: LangFlagProps) {
  const iso = LANG_TO_ISO[code.toUpperCase()] ?? code.toLowerCase().slice(0, 2);
  const { w, h, cdn, radius } = SIZE_MAP[size];

  return (
    <img
      src={`https://flagcdn.com/w${cdn}/${iso}.png`}
      srcSet={`https://flagcdn.com/w${cdn * 2}/${iso}.png 2x`}
      alt={`${code} flag`}
      width={w}
      height={h}
      className={`object-cover shadow-sm ring-1 ring-black/[0.08] ${radius} ${className}`}
      onError={(e) => { (e.currentTarget as HTMLImageElement).style.display = "none"; }}
    />
  );
}
