export function useImmersiveNav() {
  function navigateImmersive(path: string, stateData: object = {}) {
    const el = document.createElement("div");
    Object.assign(el.style, {
      position: "fixed",
      inset: "0",
      zIndex: "9999",
      background: "#0a0200",
      animation: "immersiveWipe 580ms cubic-bezier(0.76, 0, 0.24, 1) both",
      pointerEvents: "none",
    });
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
