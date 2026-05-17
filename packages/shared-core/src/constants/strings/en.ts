import type { Strings } from "./types";

export const EN: Strings = {
  app: {
    name: "Talkly",
    subtitle: "Learn languages by living the story",
    loading: "Loading Talkly...",
  },
  actions: {
    back: "Back",
    continue: "Continue",
    start: "Start",
    finish: "Finish",
    retry: "Try again",
    close: "Close",
    save: "Save",
    cancel: "Cancel",
  },
  nav: {
    home: "Home",
    adventure: "Adventure",
    study: "Study",
    vocabulary: "Vocabulary",
    profile: "Profile",
  },
  home: {
    title: "Today",
    headline: "Continue where you left off.",
    adventureCta: "Continue adventure",
    studyCta: "Study now",
  },
  adventure: {
    title: "Adventure",
    mapTitle: "Map",
    loading: "Loading adventure...",
    empty: "No adventure available.",
    phaseLabel: (n) => `Phase ${n}`,
    sectionProgress: (done, total) => `${done}/${total} sections`,
    backToMap: "Back to map",
  },
  errors: {
    generic: "Could not complete the action.",
  },
};
