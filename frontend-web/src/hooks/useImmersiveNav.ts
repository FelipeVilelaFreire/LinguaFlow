const LANG_ISO: Record<string, string> = {
  IT: "it", DE: "de", EN: "us", ES: "es",
  FR: "fr", JA: "jp", PT: "br", ZH: "cn",
};

interface ImmersiveOptions {
  title?:    string;
  subtitle?: string;
  langCode?: string;
}

export function useImmersiveNav() {
  function navigateImmersive(path: string, stateData: object = {}, options?: ImmersiveOptions) {
    const el = document.createElement("div");
    Object.assign(el.style, {
      position:       "fixed",
      inset:          "0",
      zIndex:         "9999",
      background:     "linear-gradient(180deg, #120600 0%, #1e0d00 55%, #2d1200 100%)",
      animation:      "immersiveWipe 820ms cubic-bezier(0.76, 0, 0.24, 1) both",
      pointerEvents:  "none",
      display:        "flex",
      flexDirection:  "column",
      alignItems:     "center",
      justifyContent: "center",
      gap:            "0",
    });

    // Content wrapper — fades in after the wipe starts
    const wrap = document.createElement("div");
    wrap.style.cssText =
      "display:flex;flex-direction:column;align-items:center;gap:16px;" +
      "text-align:center;padding:0 32px;" +
      "opacity:0;animation:immersiveReveal 400ms 360ms ease-out both;";

    // Flag
    const iso = options?.langCode ? (LANG_ISO[options.langCode.toUpperCase()] ?? options.langCode.toLowerCase().slice(0, 2)) : null;
    if (iso) {
      const flag = document.createElement("img");
      flag.src    = `https://flagcdn.com/w80/${iso}.png`;
      flag.srcset = `https://flagcdn.com/w160/${iso}.png 2x`;
      flag.alt    = options?.langCode ?? "";
      flag.style.cssText =
        "width:56px;height:auto;border-radius:6px;" +
        "box-shadow:0 4px 20px rgba(0,0,0,0.6),0 0 0 1px rgba(255,255,255,0.12);" +
        "object-fit:cover;";
      wrap.appendChild(flag);
    }

    // Divider line
    const line = document.createElement("div");
    line.style.cssText =
      "width:32px;height:1px;background:rgba(217,119,6,0.4);margin:0 auto;";
    wrap.appendChild(line);

    // Title
    if (options?.title) {
      const title = document.createElement("p");
      title.textContent = options.title;
      title.style.cssText =
        "color:#faf3e0;font-size:1.25rem;font-weight:700;" +
        "letter-spacing:0.04em;font-family:inherit;margin:0;line-height:1.2;";
      wrap.appendChild(title);
    }

    // Subtitle
    if (options?.subtitle) {
      const sub = document.createElement("p");
      sub.textContent = options.subtitle;
      sub.style.cssText =
        "color:rgba(245,158,11,0.5);font-size:0.6875rem;font-weight:600;" +
        "letter-spacing:0.14em;text-transform:uppercase;font-family:inherit;margin:0;";
      wrap.appendChild(sub);
    }

    el.appendChild(wrap);
    document.body.appendChild(el);

    // Navigate mid-transition
    setTimeout(() => {
      window.history.pushState(stateData, "", path);
      window.dispatchEvent(new PopStateEvent("popstate"));
    }, 550);

    // Fade out overlay
    setTimeout(() => {
      el.style.transition = "opacity 300ms ease-out";
      el.style.opacity    = "0";
      setTimeout(() => el.remove(), 300);
    }, 950);
  }

  return { navigateImmersive };
}
