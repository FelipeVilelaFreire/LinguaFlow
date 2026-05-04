import { useEffect, useMemo, useState } from "react";

import AppLayout from "./components/layout/AppLayout";
import { getLocaleFromSourceLanguage } from "./constants/strings";
import { StringsProvider } from "./contexts/StringsContext";
import { AUTH_PATHS, NAV_ITEMS, ROUTE_PATHS } from "./constants/routes";
import AccountScreen from "./screens/AccountScreen";
import AuthScreen from "./screens/AuthScreen";
import HomeScreen from "./screens/HomeScreen";
import OnboardingScreen from "./screens/OnboardingScreen";
import ScenariosScreen from "./screens/ScenariosScreen";
import TodayScreen from "./screens/TodayScreen";
import VocabularyScreen from "./screens/VocabularyScreen";
import { authService, type User } from "./services/authService";
import { contentService } from "./services/contentService";
import type { Goal } from "./types/content";
import type { AppRoute } from "./types/navigation";

export default function App() {
  const [route, setRoute] = useState<AppRoute>(() => routeFromPath(window.location.pathname));
  const [user, setUser] = useState<User | null>(null);
  const [goal, setGoal] = useState<Goal | null>(null);
  const [goals, setGoals] = useState<Goal[]>([]);
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
    if (user && !goal && window.location.pathname !== AUTH_PATHS.onboarding) {
      replacePath(AUTH_PATHS.onboarding);
      return;
    }
    if (user && goal && isAuthPath(window.location.pathname)) {
      replacePath(ROUTE_PATHS[route]);
    }
  }, [booting, user, goal, route]);

  const screen = useMemo(() => {
    if (route === "today") return <TodayScreen onCompleted={() => contentService.getCurrentGoal().then(setGoal)} />;
    if (route === "scenarios") return <ScenariosScreen />;
    if (route === "vocabulary") return <VocabularyScreen />;
    if (route === "account" && user) {
      return (
        <AccountScreen
          user={user}
          goals={goals.length ? goals : ([goal].filter(Boolean) as Goal[])}
          onCreateGoal={handleGoalChanged}
          onDeleteGoal={deleteGoal}
          onLogout={logout}
          onSwitchGoal={switchGoal}
        />
      );
    }
    return <HomeScreen onStartToday={() => navigate("today")} />;
  }, [route, user]);

  function navigate(nextRoute: AppRoute) {
    setRoute(nextRoute);
    const nextPath = ROUTE_PATHS[nextRoute];
    if (window.location.pathname !== nextPath) {
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
      return;
    }
    setGoal(null);
    replacePath(AUTH_PATHS.onboarding);
  }

  if (booting) return <div className="grid min-h-screen place-items-center bg-slate-50 font-semibold">Loading LinguaFlow...</div>;
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
            replacePath(AUTH_PATHS.onboarding);
          }
        }} />
      </StringsProvider>
    );
  }
  if (!goal) {
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

  return (
    <StringsProvider locale={getLocaleFromSourceLanguage(goal.source_language?.code)}>
      <AppLayout activeRoute={route} activeGoal={goal} goals={goals.length ? goals : [goal]} switchingAreaLabel={switchingAreaLabel} navItems={NAV_ITEMS} user={user} onLogout={logout} onSwitchGoal={switchGoal} onNavigate={navigate}>
        {screen}
      </AppLayout>
    </StringsProvider>
  );
}

function routeFromPath(pathname: string): AppRoute {
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
