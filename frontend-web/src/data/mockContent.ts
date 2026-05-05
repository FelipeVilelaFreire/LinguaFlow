import type { Favorite, Goal, Phrase, Scenario, StudyDay } from "../types/content";

const pt = { id: 1, code: "PT", name: "Português" };
const de = { id: 2, code: "DE", name: "Alemão" };

export const mockScenarios: Scenario[] = [
  { id: 1, slug: "restaurant", title: "Restaurante", description: "Pedir comida, pagar e resolver situações simples.", phrase_count: 6 },
  { id: 2, slug: "market", title: "Mercado", description: "Comprar itens, perguntar preços e quantidades.", phrase_count: 6 },
  { id: 3, slug: "transport", title: "Transporte", description: "Usar trem, ônibus, táxi e pedir direções.", phrase_count: 6 },
  { id: 4, slug: "university", title: "Universidade", description: "Conversas rápidas sobre aula, estudo e rotina.", phrase_count: 6 },
  { id: 5, slug: "housing", title: "Moradia", description: "Aluguel, manutenção e vida em casa.", phrase_count: 6 },
];

export const mockPhrases: Phrase[] = [
  phrase(1, "restaurant", "Eu gostaria de uma água.", "Ich hätte gern ein Wasser."),
  phrase(2, "restaurant", "A conta, por favor.", "Die Rechnung, bitte."),
  phrase(3, "restaurant", "Tem uma mesa livre?", "Haben Sie einen freien Tisch?"),
  phrase(4, "market", "Quanto custa isso?", "Wie viel kostet das?"),
  phrase(5, "market", "Eu pago com cartão.", "Ich zahle mit Karte."),
  phrase(6, "transport", "Onde fica a estação?", "Wo ist der Bahnhof?"),
  phrase(7, "transport", "Eu preciso de um bilhete.", "Ich brauche eine Fahrkarte."),
  phrase(8, "university", "Você pode me ajudar?", "Kannst du mir helfen?"),
  phrase(9, "housing", "Eu procuro um apartamento.", "Ich suche eine Wohnung."),
];

export const mockGoal: Goal = {
  id: 1,
  current_level: "NONE",
  target_level: "A1",
  duration_days: 90,
  total_phrases: 300,
  learned_phrases: 18,
  completed_lessons: 3,
  streak_days: 4,
  study_weekdays: [0, 1, 2, 3, 4, 5, 6],
  session_minutes: 60,
  is_study_day_today: true,
  next_study_date: new Date().toISOString().slice(0, 10),
  is_active: true,
  progress_percent: 6,
};

export const mockToday: StudyDay = {
  id: 1,
  day_number: 7,
  is_active: true,
  completed: false,
  practice_items: [],
  lesson: {
    id: 1,
    title: "Restaurant Basics",
    day_number: 7,
    scenario: mockScenarios[0],
    phrases: mockPhrases.filter((item) => item.category === "Restaurante"),
    video_title: "A1 German: Restaurante",
    video_url: "https://www.youtube.com/results?search_query=german+a1+restaurant+phrases",
    video_duration: "~10 min",
  },
};

export function getMockFavorites(): Favorite[] {
  const ids = readFavoriteIds();
  return ids
    .map((id) => mockPhrases.find((phraseItem) => phraseItem.id === id))
    .filter((phraseItem): phraseItem is Phrase => Boolean(phraseItem))
    .map((phraseItem) => ({
      id: phraseItem.id,
      phrase: phraseItem,
      created_at: new Date().toISOString(),
    }));
}

export function addMockFavorite(phraseId: number): Favorite {
  const ids = readFavoriteIds();
  if (!ids.includes(phraseId)) {
    writeFavoriteIds([...ids, phraseId]);
  }
  const phraseItem = mockPhrases.find((item) => item.id === phraseId) ?? mockPhrases[0];
  return { id: phraseItem.id, phrase: phraseItem, created_at: new Date().toISOString() };
}

export function removeMockFavorite(favoriteId: number): void {
  writeFavoriteIds(readFavoriteIds().filter((id) => id !== favoriteId));
}

function phrase(id: number, scenarioSlug: string, sourceText: string, targetText: string): Phrase {
  const scenario = mockScenarios.find((item) => item.slug === scenarioSlug) ?? mockScenarios[0];
  return {
    id,
    source_language: pt,
    target_language: de,
    source_text: sourceText,
    target_text: targetText,
    category: scenario.title,
    scenario: scenario.id,
    scenario_title: scenario.title,
    difficulty: "A1",
  };
}

function readFavoriteIds(): number[] {
  if (typeof window === "undefined") return [];
  const rawValue = window.localStorage.getItem("linguaflow:favorites");
  if (!rawValue) return [];
  try {
    return JSON.parse(rawValue) as number[];
  } catch {
    return [];
  }
}

function writeFavoriteIds(ids: number[]): void {
  if (typeof window === "undefined") return;
  window.localStorage.setItem("linguaflow:favorites", JSON.stringify(ids));
}
