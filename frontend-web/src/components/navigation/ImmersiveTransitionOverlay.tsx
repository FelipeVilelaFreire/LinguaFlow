import type { CSSProperties } from "react";

export interface ImmersiveTransitionOptions {
  title?: string;
  subtitle?: string;
  langCode?: string;
}

const LANG_ISO: Record<string, string> = {
  IT: "it",
  DE: "de",
  EN: "us",
  ES: "es",
  FR: "fr",
  JA: "jp",
  PT: "br",
  ZH: "cn",
};

const overlayStyle: CSSProperties = {
  position: "fixed",
  inset: 0,
  zIndex: 9999,
  background: "linear-gradient(180deg, #120600 0%, #1e0d00 55%, #2d1200 100%)",
  animation: "immersiveWipe 820ms cubic-bezier(0.76, 0, 0.24, 1) both",
  pointerEvents: "none",
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  justifyContent: "center",
  gap: 0,
};

const contentStyle: CSSProperties = {
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  gap: 16,
  textAlign: "center",
  padding: "0 32px",
  opacity: 0,
  animation: "immersiveReveal 400ms 360ms ease-out both",
};

const flagStyle: CSSProperties = {
  width: 56,
  height: "auto",
  borderRadius: 6,
  boxShadow: "0 4px 20px rgba(0,0,0,0.6), 0 0 0 1px rgba(255,255,255,0.12)",
  objectFit: "cover",
};

export default function ImmersiveTransitionOverlay({ title, subtitle, langCode }: ImmersiveTransitionOptions) {
  const iso = langCode ? (LANG_ISO[langCode.toUpperCase()] ?? langCode.toLowerCase().slice(0, 2)) : null;

  return (
    <div style={overlayStyle}>
      <div style={contentStyle}>
        {iso ? (
          <img
            src={`https://flagcdn.com/w80/${iso}.png`}
            srcSet={`https://flagcdn.com/w160/${iso}.png 2x`}
            alt={langCode ?? ""}
            style={flagStyle}
          />
        ) : null}

        <div style={{ width: 32, height: 1, background: "rgba(217,119,6,0.4)", margin: "0 auto" }} />

        {title ? (
          <p
            style={{
              color: "#faf3e0",
              fontSize: "1.25rem",
              fontWeight: 700,
              letterSpacing: "0.04em",
              fontFamily: "inherit",
              margin: 0,
              lineHeight: 1.2,
            }}
          >
            {title}
          </p>
        ) : null}

        {subtitle ? (
          <p
            style={{
              color: "rgba(245,158,11,0.5)",
              fontSize: "0.6875rem",
              fontWeight: 600,
              letterSpacing: "0.14em",
              textTransform: "uppercase",
              fontFamily: "inherit",
              margin: 0,
            }}
          >
            {subtitle}
          </p>
        ) : null}
      </div>
    </div>
  );
}
