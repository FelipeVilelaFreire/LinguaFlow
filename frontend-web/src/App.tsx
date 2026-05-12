import { useEffect, useMemo, useState } from "react";

import AppLayout from "./components/layout/AppLayout";
import { APP_NAME } from "./constants/app";
import { getLocaleFromSourceLanguage, type AppLocale } from "./constants/strings";
import { StringsProvider } from "./contexts/StringsContext";
import { adventureChapterPath, NAV_ITEMS, ROUTES } from "./constants/routes";
import AccountScreen from "./screens/AccountScreen";
import AdventureChapterScreen from "./screens/adventure/abas/mapa/components/AdventureChapterScreen";
import AdventureModule from "./screens/adventure/AdventureModule";
import type { AdventureTab } from "./screens/adventure/AdventureModule";
import EditProfileScreen from "./screens/EditProfileScreen";
import HistoryScreen from "./screens/HistoryScreen";
import AdventureScreen from "./screens/AdventureScreen";
import AuthScreen from "./screens/AuthScreen";
import HomeScreen from "./screens/HomeScreen";
import OnboardingScreen from "./screens/OnboardingScreen";
import StudyScreen from "./screens/StudyScreen";
import VocabularyScreen from "./screens/VocabularyScreen";
import { authService, type User } from "./services/authService";
import { contentService } from "./services/contentService";
import type { Goal } from "./types/content";
import type { AppRoute } from "./types/navigation";

const UI_LOCALE_KEY = "fluenci_ui_locale";

// Maps AppRoute to a browser path (adventure-chapter is dynamic so omitted)
const ROUTE_PATH: Partial<Record<AppRoute, string>> = {
  home:               ROUTES.home,
  adventure:          ROUTES.adventure,
  "adventure-map":      ROUTES.adventureMap,
  "adventure-mochila":      ROUTES.adventureMochila,
  "adventure-palavras":     ROUTES.adventurePalavras,
  "adventure-heroi":        ROUTES.adventureHeroi,
  "adventure-personagens":  ROUTES.adventurePersonagens,
  today:              ROUTES.today,
  vocabulary:         ROUTES.vocabulary,
  account:            ROUTES.account,
  history:            ROUTES.history,
  editprofile:        ROUTES.editProfile,
};

export default function App() {
  const [route, setRoute] = useState<AppRoute>(() => routeFromPath(window.location.pathname));
  const [user, setUser] = useState<User | null>(null);
  const [goal, setGoal] = useState<Goal | null>(null);
  const [goals, setGoals] = useState<Goal[]>([]);
  const [uiLocale, setUiLocale] = useState<AppLocale | null>(() => {
    const saved = window.localStorage.getItem(UI_LOCALE_KEY);
    return saved === "pt" || saved === "en" ? saved : null;
  });
  const [switchingAreaLabel, setSwitchingAreaLabel] = useState<string | null>(null);
  const [booting, setBooting] = useState(true);

  const activeLocale = uiLocale ?? getLocaleFromSourceLanguage(goal?.source_language?.code);
  const langCode = goal?.target_language?.code ?? "ES";

  useEffect(() => {
    function handlePopState() {
      setRoute(routeFromPath(window.location.pathname));
    }
    window.addEventListener("popstate", handlePopState);
    return () => window.removeEventListener("popstate", handlePopState);
  }, []);

  useEffect(() => {
    async function boot() {
      if (!authService.getToken()) { setBooting(false); return; }
      try {
        const currentUser = await authService.me();
        setUser(currentUser);
      } catch {
        authService.logout();
        setBooting(false);
        return;
      }
      try {
        const currentGoal = await contentService.getCurrentGoal();
        setGoal(currentGoal);
        setGoals(await contentService.listGoals());
      } catch {
        setGoal(null);
      } finally {
        setBooting(false);
      }
    }
    boot();
  }, []);

  useEffect(() => {
    if (booting) return;
    if (!user && window.location.pathname !== ROUTES.login) {
      replacePath(ROUTES.login);
      return;
    }
    if (user && isAuthPath(window.location.pathname)) {
      replacePath(ROUTE_PATH[route] ?? ROUTES.home);
    }
  }, [booting, user, goal, route]);

  const screen = useMemo(() => {
    if (route === "adventure") return <AdventureScreen langCode={langCode} />;
    if (route === "today") return <StudyScreen onCompleted={() => contentService.getCurrentGoal().then(setGoal)} onNavigate={navigate} />;
    if (route === "vocabulary") return <VocabularyScreen />;
    if (route === "history") return (
      <div className="md:max-w-2xl md:mx-auto">
        <HistoryScreen onBack={() => navigate("account")} />
      </div>
    );
    if (route === "editprofile" && user) return (
      <div className="md:max-w-2xl md:mx-auto">
        <EditProfileScreen
          user={user}
          uiLocale={activeLocale}
          onBack={() => navigate("account")}
          onLocaleChange={changeUiLocale}
          onLogout={logout}
        />
      </div>
    );
    if (route === "account" && user) {
      return (
        <AccountScreen
          user={user}
          goals={goals}
          onCreateGoal={handleGoalChanged}
          onUpdateGoal={handleGoalChanged}
          onDeleteGoal={deleteGoal}
          onLogout={logout}
          onSwitchGoal={switchGoal}
          onViewHistory={() => navigate("history")}
          onEditProfile={() => navigate("editprofile")}
        />
      );
    }
    return <HomeScreen hasActiveGoal={Boolean(goal)} onCreateArea={() => navigate("account")} onStartToday={() => navigate("today")} />;
  }, [route, user, goal, goals, activeLocale]);

  function navigate(nextRoute: AppRoute) {
    setRoute(nextRoute);
    const nextPath = ROUTE_PATH[nextRoute];
    if (nextPath && window.location.pathname !== nextPath) {
      window.history.pushState({}, "", nextPath);
    }
  }

  function logout() {
    authService.logout();
    setUser(null);
    setGoal(null);
    setGoals([]);
    setRoute("home");
    replacePath(ROUTES.login);
  }

  async function handleGoalChanged(nextGoal: Goal) {
    setGoal(nextGoal);
    setGoals(await contentService.listGoals());
  }

  async function switchGoal(nextGoal: Goal) {
    if (nextGoal.is_active) return;
    const label = `${nextGoal.source_language?.code ?? "PT"} -> ${nextGoal.target_language?.code ?? "??"} ${nextGoal.target_level}`;
    setSwitchingAreaLabel(label);
    await new Promise((resolve) => window.setTimeout(resolve, 520));
    const activatedGoal = await contentService.activateGoal(nextGoal.id);
    setGoal(activatedGoal);
    setGoals(await contentService.listGoals());
    await new Promise((resolve) => window.setTimeout(resolve, 260));
    setSwitchingAreaLabel(null);
    navigate("home");
  }

  async function deleteGoal(goalToDelete: Goal) {
    const result = await contentService.deleteGoal(goalToDelete.id);
    const nextGoals = await contentService.listGoals();
    setGoals(nextGoals);
    if (result.current_goal) {
      setGoal(result.current_goal);
      if (route === "account") return;
      navigate("home");
      return;
    }
    setGoal(null);
    setRoute("account");
    replacePath(ROUTES.account);
  }

  function changeUiLocale(locale: AppLocale) {
    setUiLocale(locale);
    window.localStorage.setItem(UI_LOCALE_KEY, locale);
  }

  if (booting) return (
    <div className="grid min-h-screen place-items-center bg-slate-50 font-semibold">
      Loading {APP_NAME}...
    </div>
  );

  if (!user) {
    return (
      <StringsProvider locale="pt">
        <AuthScreen onAuthenticated={async (currentUser) => {
          setUser(currentUser);
          try {
            const currentGoal = await contentService.getCurrentGoal();
            setGoal(currentGoal);
            setGoals(await contentService.listGoals());
            navigate("home");
          } catch {
            setGoal(null);
            setGoals([]);
            window.history.pushState({}, "", ROUTES.onboarding);
          }
        }} />
      </StringsProvider>
    );
  }

  if (window.location.pathname === ROUTES.onboarding) {
    return (
      <StringsProvider locale="pt">
        <OnboardingScreen onComplete={(createdGoal) => {
          setGoal(createdGoal);
          setGoals([createdGoal]);
          navigate("home");
        }} />
      </StringsProvider>
    );
  }

  // ── Full-screen adventure chapter (exercise) ──────────────────────────────
  if (route === "adventure-chapter") {
    const chapterId = parseInt(window.location.pathname.split("/").pop() ?? "0");
    return (
      <StringsProvider locale={activeLocale}>
        <AdventureChapterScreen
          chapterId={chapterId}
          onBack={() => navigate("adventure-map")}
        />
      </StringsProvider>
    );
  }

  // ── Full-screen adventure module (map / mochila / herói) ─────────────────
  if (route === "adventure-map" || route === "adventure-mochila" || route === "adventure-palavras" || route === "adventure-heroi" || route === "adventure-personagens") {
    const tabMap: Record<string, AdventureTab> = {
      "adventure-map":          "map",
      "adventure-mochila":      "mochila",
      "adventure-palavras":     "palavras",
      "adventure-heroi":        "heroi",
      "adventure-personagens":  "personagens",
    };
    return (
      <StringsProvider locale={activeLocale}>
        <AdventureModule
          langCode={langCode}
          sourceLangCode={goal?.source_language?.code ?? "PT"}
          initialTab={tabMap[route]}
          chapterPath={adventureChapterPath}
          firstName={user?.first_name ?? ""}
          onBack={() => navigate("adventure")}
          onTabChange={(tab) => {
            navigate(`adventure-${tab}` as AppRoute);
          }}
        />
      </StringsProvider>
    );
  }


  // ── Main app with bottom nav ──────────────────────────────────────────────
  return (
    <StringsProvider locale={activeLocale}>
      <AppLayout
        activeRoute={route}
        activeGoal={goal}
        goals={goals}
        switchingAreaLabel={switchingAreaLabel}
        navItems={NAV_ITEMS}
        user={user}
        uiLocale={activeLocale}
        fullWidth={route === "adventure"}
        onCreateGoal={handleGoalChanged}
        onDeleteGoal={deleteGoal}
        onLocaleChange={changeUiLocale}
        onLogout={logout}
        onSwitchGoal={switchGoal}
        onNavigate={navigate}
      >
        {screen}
      </AppLayout>
    </StringsProvider>
  );
}

function routeFromPath(pathname: string): AppRoute {
  if (pathname.startsWith(ROUTES.adventureChapterBase + "/")) return "adventure-chapter";
  if (pathname === ROUTES.adventureMap)      return "adventure-map";
  if (pathname === ROUTES.adventureMochila)     return "adventure-mochila";
  if (pathname === ROUTES.adventurePalavras)    return "adventure-palavras";
  if (pathname === ROUTES.adventureHeroi)       return "adventure-heroi";
  if (pathname === ROUTES.adventurePersonagens) return "adventure-personagens";
  const found = (Object.entries(ROUTE_PATH) as Array<[AppRoute, string]>)
    .find(([, path]) => path === pathname);
  return found?.[0] ?? "home";
}

function replacePath(path: string) {
  if (window.location.pathname !== path) {
    window.history.replaceState({}, "", path);
  }
}

function isAuthPath(pathname: string) {
  return pathname === ROUTES.login || pathname === ROUTES.onboarding;
}
