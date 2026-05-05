import { CheckCircle2, ChevronRight, Flame, Languages, LogOut, Trash2, X } from "lucide-react";
import type { ReactNode } from "react";
import { useState } from "react";

import { useStrings } from "../../contexts/StringsContext";
import WarningModal from "../ui/WarningModal";
import type { AppLocale } from "../../constants/strings";
import type { User } from "../../services/authService";
import { getStudyAreaTheme, getStudyAreaThemeStyle } from "../../theme/studyAreaTheme";
import type { Goal } from "../../types/content";
import type { AppRoute, NavItem } from "../../types/navigation";

interface AppLayoutProps {
  activeRoute: AppRoute;
  children: ReactNode;
  navItems: NavItem[];
  user: User;
  activeGoal: Goal | null;
  goals: Goal[];
  switchingAreaLabel: string | null;
  uiLocale: AppLocale;
  onLocaleChange: (locale: AppLocale) => void;
  onDeleteGoal: (goal: Goal) => void;
  onLogout: () => void;
  onSwitchGoal: (goal: Goal) => void;
  onNavigate: (route: AppRoute) => void;
}

export default function AppLayout({ activeRoute, activeGoal, children, goals, navItems, switchingAreaLabel, uiLocale, user, onDeleteGoal, onLocaleChange, onLogout, onSwitchGoal, onNavigate }: AppLayoutProps) {
  const [isAreaModalOpen, setIsAreaModalOpen] = useState(false);
  const [goalToDelete, setGoalToDelete] = useState<Goal | null>(null);
  const strings = useStrings();
  const activeTheme = getStudyAreaTheme(activeGoal);
  const activeArea = activeGoal ? activeTheme.label : uiLocale === "pt" ? "Nenhuma area ativa" : "No active area";
  const mobileNavItems = navItems.filter((item) => ["home", "today", "history", "vocabulary", "account"].includes(item.route));

  return (
    <div className="min-h-screen text-slate-950 transition-colors duration-500" style={{ ...getStudyAreaThemeStyle(activeTheme), background: "var(--area-page)" }}>
      <header className="safe-top sticky top-0 z-30 border-b border-slate-200 bg-white/95 px-4 pb-3 backdrop-blur md:hidden">
        <div className="flex items-center justify-between gap-3">
          <button type="button" onClick={() => onNavigate("home")} className="flex min-w-0 items-center gap-3 text-left">
            <div className="grid h-10 w-10 shrink-0 place-items-center rounded-[8px] text-white shadow-sm" style={{ background: "var(--area-primary)" }}>
              <Flame size={19} />
            </div>
            <div className="min-w-0">
              <p className="text-base font-semibold leading-tight">{strings.app.name}</p>
              <p className="truncate text-xs font-bold text-slate-500">{activeArea}</p>
            </div>
          </button>
          <button type="button" onClick={() => goals.length ? setIsAreaModalOpen(true) : onNavigate("account")} className="rounded-[8px] px-3 py-2 text-xs font-bold ring-1" style={{ background: "var(--area-primary-soft)", color: "var(--area-primary-dark)", borderColor: "var(--area-primary-soft)" }}>
            {activeGoal ? `${activeGoal.progress_percent}%` : strings.actions.createArea}
          </button>
        </div>
      </header>

      <aside className="fixed inset-y-0 left-0 hidden w-72 border-r border-slate-200 bg-white px-4 py-5 md:block">
        <div className="mb-8 flex items-center gap-3">
          <div className="grid h-11 w-11 place-items-center rounded-[8px] text-white shadow-sm" style={{ background: "var(--area-primary)" }}>
            <Flame size={21} />
          </div>
          <div>
            <h1 className="text-xl font-semibold">{strings.app.name}</h1>
            <p className="mt-0.5 text-xs font-bold text-slate-500">{strings.app.subtitle}</p>
          </div>
        </div>

        <nav className="space-y-2">
          {navItems.map((item) => (
            <button
              key={item.route}
              type="button"
              onClick={() => onNavigate(item.route)}
              className={`flex h-12 w-full items-center justify-between rounded-[8px] px-3 text-left text-sm font-semibold transition ${
                activeRoute === item.route
                  ? "text-white shadow-sm"
                  : "text-slate-600 hover:bg-slate-100"
              }`}
              style={activeRoute === item.route ? { background: "var(--area-primary)" } : undefined}
            >
              <span className="flex items-center gap-3">
                <item.icon size={18} />
                {strings.nav[item.labelKey]}
              </span>
              {activeRoute === item.route ? <ChevronRight size={16} /> : null}
            </button>
          ))}
        </nav>

        <div className="absolute inset-x-4 bottom-5 space-y-3">
          <div className="rounded-[8px] border border-slate-200 bg-slate-50 p-3">
            <p className="flex items-center gap-2 text-xs font-semibold uppercase text-slate-500">
              <Languages size={14} />
              {strings.layout.interfaceLanguage}
            </p>
            <div className="mt-3 grid grid-cols-2 gap-2">
              {(["pt", "en"] as AppLocale[]).map((locale) => (
                <button
                  key={locale}
                  type="button"
                  onClick={() => onLocaleChange(locale)}
                  className={`h-10 rounded-[8px] text-sm font-semibold ring-1 transition ${
                    uiLocale === locale ? "text-white shadow-sm" : "bg-white text-slate-600 ring-slate-200 hover:bg-slate-100"
                  }`}
                  style={uiLocale === locale ? { background: "var(--area-primary)", borderColor: "var(--area-primary)" } : undefined}
                >
                  {locale === "pt" ? strings.layout.portuguese : strings.layout.english}
                </button>
              ))}
            </div>
          </div>
          <button type="button" onClick={() => goals.length ? setIsAreaModalOpen(true) : onNavigate("account")} className="w-full rounded-[8px] p-3 text-left ring-1 transition hover:brightness-[0.98]" style={{ background: "var(--area-primary-soft)", borderColor: "var(--area-primary-soft)" }}>
            <p className="text-xs font-semibold uppercase" style={{ color: "var(--area-primary-dark)" }}>{strings.layout.activeArea}</p>
            <p className="mt-1 truncate font-semibold text-slate-950">{activeArea}</p>
            <p className="mt-1 text-xs font-medium text-slate-500">{activeGoal ? `${activeGoal.progress_percent}% ${strings.layout.completed}` : uiLocale === "pt" ? "Crie uma area no perfil" : "Create an area in profile"}</p>
          </button>
          <div className="rounded-[8px] border border-slate-200 bg-slate-50 p-3">
            <p className="text-xs font-semibold uppercase text-slate-500">{strings.layout.loggedAs}</p>
            <p className="truncate font-semibold">{user.username}</p>
            <button type="button" onClick={onLogout} className="mt-3 flex w-full items-center justify-center gap-2 rounded-[8px] bg-white px-3 py-2 text-sm font-semibold text-slate-700 ring-1 ring-slate-200 transition hover:bg-slate-100">
              <LogOut size={16} />
              {strings.actions.logout}
            </button>
          </div>
        </div>
      </aside>

      <main className="min-h-screen px-3 pb-32 pt-3 md:ml-72 md:px-8 md:py-8">
        <div key={activeRoute} className="mx-auto max-w-6xl animate-[fadeIn_220ms_ease-out]">{children}</div>
      </main>

      <nav className="safe-bottom fixed inset-x-0 bottom-0 z-30 border-t border-slate-200 bg-white/95 px-2 pt-2 shadow-[0_-10px_24px_rgba(15,23,42,0.10)] backdrop-blur md:hidden">
        <div className="mx-auto grid max-w-md grid-cols-5 items-end gap-1">
        {mobileNavItems.map((item) => {
          const isActive = activeRoute === item.route;
          return (
          <button
            key={item.route}
            type="button"
            onClick={() => onNavigate(item.route)}
            className={`flex h-14 min-w-0 flex-col items-center justify-center gap-1 rounded-[8px] text-[10px] font-semibold transition ${isActive ? "" : "text-slate-500"}`}
            style={isActive ? { background: "var(--area-primary-soft)", color: "var(--area-primary-dark)" } : undefined}
          >
            <item.icon size={18} />
            <span className="max-w-full truncate px-1">{strings.nav[item.labelKey]}</span>
          </button>
          );
        })}
        </div>
      </nav>

      {isAreaModalOpen ? (
        <div className="fixed inset-0 z-40 grid place-items-end bg-slate-950/40 px-3 pb-3 backdrop-blur-sm md:place-items-center md:px-4 md:pb-0">
          <section className="max-h-[88vh] w-full max-w-lg animate-[fadeIn_180ms_ease-out] overflow-y-auto rounded-[8px] bg-white p-4 shadow-xl ring-1 ring-slate-200 md:p-5">
            <div className="flex items-start justify-between gap-4">
              <div>
                <p className="text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{strings.layout.switchArea}</p>
                <h2 className="mt-1 text-2xl font-semibold">{strings.layout.chooseActiveStudy}</h2>
              </div>
              <button type="button" onClick={() => setIsAreaModalOpen(false)} className="grid h-9 w-9 place-items-center rounded-[8px] text-slate-500 transition hover:bg-slate-100">
                <X size={18} />
              </button>
            </div>

            <div className="mt-5 grid gap-3">
              {!goals.length ? (
                <div className="rounded-[8px] border border-dashed border-slate-300 bg-slate-50 p-5 text-center">
                  <p className="font-semibold">{uiLocale === "pt" ? "Nenhuma area criada" : "No areas yet"}</p>
                  <p className="mt-1 text-sm font-medium text-slate-500">{uiLocale === "pt" ? "Va para o perfil para criar sua primeira area de estudo." : "Go to profile to create your first study area."}</p>
                </div>
              ) : null}
              {goals.map((goal) => {
                const theme = getStudyAreaTheme(goal);
                return (
                  <article
                    key={goal.id}
                    className={`rounded-[8px] p-4 text-left ring-1 transition ${goal.is_active ? "" : "bg-white ring-slate-200 hover:bg-slate-50"}`}
                    style={goal.is_active ? { background: theme.primarySoft, boxShadow: `inset 0 0 0 1px ${theme.primary}` } : undefined}
                  >
                    <div className="flex items-start justify-between gap-4">
                      <button
                        type="button"
                        onClick={() => {
                          setIsAreaModalOpen(false);
                          onSwitchGoal(goal);
                        }}
                        className="min-w-0 flex-1 text-left"
                      >
                        <p className="font-semibold">{theme.label}</p>
                        <p className="mt-0.5 text-sm font-medium" style={{ color: theme.primaryDark }}>{theme.name}</p>
                        <p className="mt-1 text-sm font-medium text-slate-500">{goal.progress_percent}% {strings.layout.completed}</p>
                      </button>
                      <div className="flex items-center gap-2">
                        {goal.is_active ? <CheckCircle2 style={{ color: theme.primary }} size={20} /> : null}
                        <button
                          type="button"
                          onClick={() => {
                            setGoalToDelete(goal);
                          }}
                          className="grid h-9 w-9 place-items-center rounded-[8px] bg-white text-red-700 ring-1 ring-red-100 transition hover:bg-red-50"
                          title={strings.actions.delete}
                        >
                          <Trash2 size={16} />
                        </button>
                      </div>
                    </div>
                  </article>
                );
              })}
            </div>

            <button type="button" onClick={() => { setIsAreaModalOpen(false); onNavigate("account"); }} className="mt-4 h-11 w-full rounded-[8px] px-4 font-semibold text-white transition hover:brightness-95" style={{ background: "var(--area-primary)" }}>
              {strings.actions.manageInProfile}
            </button>
          </section>
        </div>
      ) : null}

      {goalToDelete ? (
        <WarningModal
          title={uiLocale === "pt" ? "Excluir area?" : "Delete area?"}
          detail={`${goalToDelete.source_language?.code ?? ""} -> ${goalToDelete.target_language?.code ?? ""} ${goalToDelete.target_level}: ${
            goals.length <= 1
              ? uiLocale === "pt"
                ? "essa e sua ultima area. Depois de excluir, sua conta ficara sem area ativa."
                : "this is your last area. After deleting it, your account will have no active area."
              : uiLocale === "pt"
                ? "essa area sera removida do seu perfil."
                : "this area will be removed from your profile."
          }`}
          cancelLabel={uiLocale === "pt" ? "Cancelar" : "Cancel"}
          confirmLabel={strings.actions.delete}
          onCancel={() => setGoalToDelete(null)}
          onConfirm={() => {
            setIsAreaModalOpen(false);
            onDeleteGoal(goalToDelete);
            setGoalToDelete(null);
          }}
        />
      ) : null}

      {switchingAreaLabel ? (
        <div className="fixed inset-0 z-50 grid place-items-center overflow-hidden text-white" style={{ background: "linear-gradient(135deg, var(--area-primary-dark), var(--area-primary))" }}>
          <div className="absolute inset-y-0 left-0 w-full animate-[areaSweep_900ms_ease-in-out] bg-white/10" />
          <div className="relative animate-[areaSwitch_900ms_ease-in-out] text-center">
            <p className="text-sm font-semibold uppercase tracking-wide opacity-80">{strings.layout.enteringArea}</p>
            <h2 className="mt-3 text-5xl font-semibold">{switchingAreaLabel}</h2>
            <div className="mx-auto mt-6 h-1.5 w-56 overflow-hidden rounded-full bg-white/20">
              <div className="h-full w-full animate-[areaSweep_900ms_ease-in-out] rounded-full bg-white" />
            </div>
          </div>
        </div>
      ) : null}
    </div>
  );
}
