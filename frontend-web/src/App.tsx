import { useEffect, useMemo, useState } from "react";

import AppLayout from "./components/layout/AppLayout";
import { APP_NAME } from "./constants/app";
import { getLocaleFromSourceLanguage, type AppLocale } from "./constants/strings";
import { StringsProvider } from "./contexts/StringsContext";
import { ADVENTURE_CHAPTER_BASE, AUTH_PATHS, NAV_ITEMS, ROUTE_PATHS } from "./constants/routes";
import AccountScreen from "./screens/AccountScreen";
import AdventureChapterScreen from "./screens/AdventureChapterScreen";
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

const UI_LOCALE_KEY = "talkly_ui_locale";

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

  useEffect(() => {
    function handlePopState() {
      setRoute(routeFromPath(window.location.pathname));
    }
    window.addEventListener("popstate", handlePopState);
    return () => window.removeEventListener("popstate", handlePopState);
  }, []);

  useEffect(() => {
    async function boot() {
      if (!authService.getToken()) {
        setBooting(false);
        return;
      }
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
    if (!user && window.location.pathname !== AUTH_PATHS.login) {
      replacePath(AUTH_PATHS.login);
      return;
    }
    if (user && isAuthPath(window.location.pathname)) {
      replacePath(ROUTE_PATHS[route as keyof typeof ROUTE_PATHS] ?? ROUTE_PATHS.home);
    }
  }, [booting, user, goal, route]);

  const screen = useMemo(() => {
    if (route === "adventure") return <AdventureScreen />;
    if (route === "today") return <StudyScreen onCompleted={() => contentService.getCurrentGoal().then(setGoal)} />;
    if (route === "vocabulary") return <VocabularyScreen />;
    if (route === "history") {
      return <HistoryScreen onBack={() => navigate("account")} />;
    }
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
        />
      );
    }
    return <HomeScreen hasActiveGoal={Boolean(goal)} onCreateArea={() => navigate("account")} onStartToday={() => navigate("today")} />;
  }, [route, user, goal, goals]);

  function navigate(nextRoute: AppRoute) {
    setRoute(nextRoute);
    const nextPath = ROUTE_PATHS[nextRoute as keyof typeof ROUTE_PATHS];
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
    replacePath(AUTH_PATHS.login);
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
    replacePath(ROUTE_PATHS.account);
  }

  function changeUiLocale(locale: AppLocale) {
    setUiLocale(locale);
    window.localStorage.setItem(UI_LOCALE_KEY, locale);
  }

  if (booting) return <div className="grid min-h-screen place-items-center bg-slate-50 font-semibold">Loading {APP_NAME}...</div>;
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
            window.history.pushState({}, "", AUTH_PATHS.onboarding);
          }
        }} />
      </StringsProvider>
    );
  }
  if (window.location.pathname === AUTH_PATHS.onboarding) {
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

  const activeLocale = uiLocale ?? getLocaleFromSourceLanguage(goal?.source_language?.code);

  if (route === "adventure-chapter") {
    const chapterId = parseInt(window.location.pathname.split("/").pop() ?? "0");
    return (
      <StringsProvider locale={activeLocale}>
        <AdventureChapterScreen chapterId={chapterId} onBack={() => navigate("adventure")} />
      </StringsProvider>
    );
  }

  return (
    <StringsProvider locale={activeLocale}>
      <AppLayout activeRoute={route} activeGoal={goal} goals={goals} switchingAreaLabel={switchingAreaLabel} navItems={NAV_ITEMS} user={user} uiLocale={activeLocale} onDeleteGoal={deleteGoal} onLocaleChange={changeUiLocale} onLogout={logout} onSwitchGoal={switchGoal} onNavigate={navigate}>
        {screen}
      </AppLayout>
    </StringsProvider>
  );
}

function routeFromPath(pathname: string): AppRoute {
  if (pathname.startsWith(ADVENTURE_CHAPTER_BASE + "/")) return "adventure-chapter";
  const found = (Object.entries(ROUTE_PATHS) as Array<[AppRoute, string]>).find(([, path]) => path === pathname);
  return found?.[0] ?? "home";
}

function replacePath(path: string) {
  if (window.location.pathname !== path) {
    window.history.replaceState({}, "", path);
  }
}

function isAuthPath(pathname: string) {
  return pathname === AUTH_PATHS.login || pathname === AUTH_PATHS.onboarding;
}
