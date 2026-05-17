import { useCallback } from "react";
import { createRoot } from "react-dom/client";

import ImmersiveTransitionOverlay from "../components/navigation/ImmersiveTransitionOverlay";
import type { ImmersiveTransitionOptions } from "../components/navigation/ImmersiveTransitionOverlay";

export function useImmersiveNav() {
  const navigateImmersive = useCallback((
    path: string,
    stateData: object = {},
    options?: ImmersiveTransitionOptions,
  ) => {
    const el = document.createElement("div");
    document.body.appendChild(el);

    const root = createRoot(el);
    root.render(<ImmersiveTransitionOverlay {...options} />);

    window.setTimeout(() => {
      window.history.pushState(stateData, "", path);
      window.dispatchEvent(new PopStateEvent("popstate"));
    }, 550);

    window.setTimeout(() => {
      el.style.transition = "opacity 300ms ease-out";
      el.style.opacity = "0";
      window.setTimeout(() => {
        root.unmount();
        el.remove();
      }, 300);
    }, 950);
  }, []);

  return { navigateImmersive };
}
