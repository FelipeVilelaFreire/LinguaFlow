interface ImmersiveOptions {
  title?: string;
  subtitle?: string;
}

export function useImmersiveNav() {
  function navigateImmersive(path: string, stateData: object = {}, options?: ImmersiveOptions) {
    const el = document.createElement("div");
    Object.assign(el.style, {
      position: "fixed",
      inset: "0",
      zIndex: "9999",
      background: "#0a0200",
      animation: "immersiveWipe 580ms cubic-bezier(0.76, 0, 0.24, 1) both",
      pointerEvents: "none",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
    });

    if (options?.title) {
      const wrap = document.createElement("div");
      wrap.style.cssText =
        "text-align:center;opacity:0;animation:immersiveReveal 300ms 230ms ease-out both;padding:0 24px;";

      const icon = document.createElement("p");
      icon.textContent = "⚔";
      icon.style.cssText =
        "font-size:1.75rem;color:#f59e0b;margin:0 0 12px;line-height:1;";
      wrap.appendChild(icon);

      const title = document.createElement("p");
      title.textContent = options.title;
      title.style.cssText =
        "color:#fbbf24;font-size:1.125rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;font-family:inherit;margin:0;line-height:1.3;";
      wrap.appendChild(title);

      if (options.subtitle) {
        const sub = document.createElement("p");
        sub.textContent = options.subtitle;
        sub.style.cssText =
          "color:rgba(251,191,36,0.45);font-size:0.6875rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;font-family:inherit;margin:8px 0 0;";
        wrap.appendChild(sub);
      }

      el.appendChild(wrap);
    }

    document.body.appendChild(el);

    setTimeout(() => {
      window.history.pushState(stateData, "", path);
      window.dispatchEvent(new PopStateEvent("popstate"));
    }, 400);

    setTimeout(() => {
      el.style.transition = "opacity 220ms ease-out";
      el.style.opacity = "0";
      setTimeout(() => el.remove(), 220);
    }, 600);
  }

  return { navigateImmersive };
}
