import type { Strings } from "./types";

export const DE_DE: Strings = {
  app: {
    name: "Talkly",
    subtitle: "Sprachen lernen, indem du die Geschichte erlebst",
    loading: "Talkly wird geladen...",
  },
  actions: {
    back: "Zurueck",
    continue: "Weiter",
    start: "Starten",
    finish: "Abschliessen",
    retry: "Erneut versuchen",
    close: "Schliessen",
    save: "Speichern",
    cancel: "Abbrechen",
  },
  nav: {
    home: "Start",
    adventure: "Abenteuer",
    study: "Lernen",
    vocabulary: "Vokabeln",
    profile: "Profil",
  },
  home: {
    title: "Heute",
    headline: "Mach dort weiter, wo du aufgehoert hast.",
    adventureCta: "Abenteuer fortsetzen",
    studyCta: "Jetzt lernen",
  },
  adventure: {
    title: "Abenteuer",
    mapTitle: "Karte",
    loading: "Abenteuer wird geladen...",
    empty: "Kein Abenteuer verfuegbar.",
    phaseLabel: (n) => `Phase ${n}`,
    sectionProgress: (done, total) => `${done}/${total} Abschnitte`,
    backToMap: "Zur Karte",
  },
  errors: {
    generic: "Die Aktion konnte nicht abgeschlossen werden.",
  },
};
