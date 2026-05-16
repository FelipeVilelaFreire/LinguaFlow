import { CheckCircle2, ChevronDown, ChevronRight, Flame, Languages, LogOut, Plus, Trash2, X } from "lucide-react";
import type { ReactNode } from "react";
import { useState } from "react";

import { useStrings } from "../../contexts/StringsContext";
import AddAreaModal from "../ui/AddAreaModal";
import LangFlag from "../ui/LangFlag";
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
  fullWidth?: boolean;
  onLocaleChange: (locale: AppLocale) => void;
  onCreateGoal: (goal: Goal) => void;
  onDeleteGoal: (goal: Goal) => void;
  onLogout: () => void;
  onSwitchGoal: (goal: Goal) => void;
  onNavigate: (route: AppRoute) => void;
}

export default function AppLayout({ activeRoute, activeGoal, children, fullWidth, goals, navItems, switchingAreaLabel, uiLocale, user, onCreateGoal, onDeleteGoal, onLocaleChange, onLogout, onSwitchGoal, onNavigate }: AppLayoutProps) {
  const [isAreaModalOpen, setIsAreaModalOpen] = useState(false);
  const [showAddArea, setShowAddArea] = useState(false);
  const [goalToDelete, setGoalToDelete] = useState<Goal | null>(null);
  const strings = useStrings();
  const activeTheme = getStudyAreaTheme(activeGoal);
  const activeArea = activeGoal ? activeTheme.label : strings.home.noActiveArea;
  const mobileNavItems = navItems.filter((item) => ["home", "adventure", "today", "vocabulary", "account"].includes(item.route));

  return (
    <div className="min-h-screen text-slate-950 transition-colors duration-500" style={{ ...getStudyAreaThemeStyle(activeTheme), background: "var(--area-page)" }}>
      <header className="safe-top sticky top-0 z-30 border-b border-slate-200 bg-white/95 backdrop-blur md:hidden">
        <button
          type="button"
          onClick={() => setIsAreaModalOpen(true)}
          className="flex w-full items-center gap-3 px-4 pb-3 text-left"
        >
          <div className="grid h-8 w-8 shrink-0 place-items-center rounded-[8px] text-white shadow-sm" style={{ background: "var(--area-primary)" }}>
            <Flame size={16} />
          </div>
          <div className="min-w-0 flex-1">
            <img src="/lang-plus.svg" alt="Lang+" className="h-7 w-auto" />
            <p className="truncate text-xs font-medium text-slate-500">{activeArea}</p>
          </div>
          {activeGoal && (
            <span className="shrink-0 rounded-full px-2.5 py-0.5 text-xs font-bold" style={{ background: activeTheme.primarySoft, color: activeTheme.primaryDark }}>
              {activeGoal.current_level}
            </span>
          )}
          <ChevronDown size={14} className="shrink-0 text-slate-400" />
        </button>
      </header>

      <aside className="fixed inset-y-0 left-0 hidden w-80 flex-col border-r border-slate-200 bg-white md:flex">
        {/* Logo + nav */}
        <div className="flex-1 px-3 pb-3 pt-4">
          <div className="mb-5 px-1">
            <img src="/lang-plus.svg" alt="Lang+" className="h-10 w-auto" />
            <p className="mt-1 truncate text-[10px] font-semibold text-slate-400">{strings.app.subtitle}</p>
          </div>

          <nav className="space-y-0.5">
            {navItems.map((item) => (
              <button
                key={item.route}
                type="button"
                onClick={() => onNavigate(item.route)}
                className={`flex h-10 w-full items-center justify-between rounded-[8px] px-3 text-left text-sm font-semibold transition ${
                  activeRoute === item.route
                    ? "text-white shadow-sm"
                    : "text-slate-600 hover:bg-slate-100"
                }`}
                style={activeRoute === item.route ? { background: "var(--area-primary)" } : undefined}
              >
                <span className="flex items-center gap-2.5">
                  <item.icon size={16} />
                  {strings.nav[item.labelKey]}
                </span>
                {activeRoute === item.route ? <ChevronRight size={14} /> : null}
              </button>
            ))}
          </nav>
        </div>

        {/* Footer compacto — sem scrollbar */}
        <div className="shrink-0 space-y-1.5 border-t border-slate-100 px-3 py-3">

          {/* Idioma — chips inline */}
          <div className="flex items-center gap-1.5 px-1">
            <Languages size={11} className="shrink-0 text-slate-400" />
            <span className="flex-1 text-[10px] font-semibold uppercase text-slate-400">{strings.layout.interfaceLanguage}</span>
            <div className="flex gap-1">
              {(["pt", "en"] as AppLocale[]).map((locale) => (
                <button
                  key={locale}
                  type="button"
                  onClick={() => onLocaleChange(locale)}
                  className={`h-6 rounded-[5px] px-2 text-[11px] font-bold transition ${
                    uiLocale === locale ? "text-white shadow-sm" : "text-slate-500 hover:bg-slate-100"
                  }`}
                  style={uiLocale === locale ? { background: "var(--area-primary)" } : undefined}
                >
                  {locale.toUpperCase()}
                </button>
              ))}
            </div>
          </div>

          {/* Área ativa — linha compacta */}
          <button
            type="button"
            onClick={() => goals.length ? setIsAreaModalOpen(true) : onNavigate("account")}
            className="flex w-full items-center gap-2 rounded-[8px] px-2 py-1.5 text-left transition hover:brightness-[0.97]"
            style={{ background: "var(--area-primary-soft)" }}
          >
            <div className="h-2 w-2 shrink-0 rounded-full" style={{ background: "var(--area-primary)" }} />
            <p className="flex-1 truncate text-xs font-semibold text-slate-700">{activeArea}</p>
            {activeGoal && (
              <span className="shrink-0 rounded-full px-1.5 py-0.5 text-[10px] font-bold" style={{ color: "var(--area-primary-dark)" }}>
                {activeGoal.current_level}
              </span>
            )}
          </button>

          {/* Usuário + logout — linha única */}
          <div className="flex items-center gap-2 px-1 py-0.5">
            <div className="grid h-6 w-6 shrink-0 place-items-center rounded-full text-[11px] font-bold text-white" style={{ background: "var(--area-primary)" }}>
              {user.username.charAt(0).toUpperCase()}
            </div>
            <p className="flex-1 truncate text-sm font-semibold text-slate-700">{user.username}</p>
            <button
              type="button"
              onClick={onLogout}
              className="shrink-0 grid h-7 w-7 place-items-center rounded-[6px] text-slate-400 ring-1 ring-slate-200 transition hover:bg-red-50 hover:text-red-500 hover:ring-red-200"
              title={strings.actions.logout}
            >
              <LogOut size={13} />
            </button>
          </div>

        </div>
      </aside>

      <main className={`min-h-screen px-3 pb-32 pt-3 md:ml-80 ${fullWidth ? "md:p-0" : "md:px-8 md:py-8"}`}>
        <div key={activeRoute} className={`animate-[fadeIn_220ms_ease-out] ${fullWidth ? "h-full" : "mx-auto max-w-6xl"}`}>{children}</div>
      </main>

      <nav className="safe-bottom fixed inset-x-0 bottom-0 z-30 border-t border-slate-200 bg-white px-2 pt-2 shadow-[0_-10px_24px_rgba(15,23,42,0.12)] backdrop-blur md:hidden">
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
        <div className="fixed inset-0 z-40 grid place-items-end bg-slate-950/40 px-3 pb-3 backdrop-blur-sm md:place-items-center md:px-4 md:pb-0" onClick={() => setIsAreaModalOpen(false)}>
          <section className="flex max-h-[88vh] w-full max-w-lg flex-col overflow-hidden rounded-[16px] bg-white shadow-xl md:max-h-[70vh]" style={{ animation: "sheetSlideUp 0.32s cubic-bezier(0.16, 1, 0.3, 1)" }} onClick={(e) => e.stopPropagation()}>

            {/* Scrollable body */}
            <div className="flex-1 overflow-y-auto p-4 md:p-5">
              <div className="flex items-start justify-between gap-4">
                <div>
                  <p className="text-sm font-semibold uppercase" style={{ color: "var(--area-primary)" }}>{strings.layout.switchArea}</p>
                  <h2 className="mt-1 text-2xl font-semibold">{strings.layout.chooseActiveStudy}</h2>
                </div>
                <button type="button" onClick={() => setIsAreaModalOpen(false)} className="grid h-9 w-9 shrink-0 place-items-center rounded-[8px] text-slate-500 transition hover:bg-slate-100">
                  <X size={18} />
                </button>
              </div>

              <div className="mt-4 grid gap-2">
                {!goals.length ? (
                  <div className="rounded-[8px] border border-dashed border-slate-300 bg-slate-50 p-5 text-center">
                    <p className="font-semibold">{strings.layout.noAreasCreated}</p>
                    <p className="mt-1 text-sm font-medium text-slate-500">{strings.layout.addAreaBelow}</p>
                  </div>
                ) : null}
                {goals.map((goal) => {
                  const theme = getStudyAreaTheme(goal);
                  return (
                    <article
                      key={goal.id}
                      className={`rounded-[12px] p-3 text-left transition ${goal.is_active ? "" : "bg-slate-50 hover:bg-slate-100"}`}
                      style={goal.is_active ? { background: theme.primarySoft, boxShadow: `inset 0 0 0 1.5px ${theme.primary}` } : undefined}
                    >
                      <div className="flex items-center gap-3">
                        <button
                          type="button"
                          onClick={() => { setIsAreaModalOpen(false); onSwitchGoal(goal); }}
                          className="flex min-w-0 flex-1 items-center gap-3 text-left"
                        >
                          <LangFlag code={goal.target_language?.code ?? ""} size="md" className="shrink-0" />
                          <div className="min-w-0">
                            <div className="flex items-center gap-2">
                              <p className="font-semibold text-slate-950">{theme.label}</p>
                              <span className="rounded-full px-2 py-0.5 text-[10px] font-bold" style={{ background: theme.primarySoft, color: theme.primaryDark }}>
                                {goal.current_level}
                              </span>
                            </div>
                            <p className="mt-0.5 text-xs font-medium text-slate-500">{goal.progress_percent}% {strings.layout.completed}</p>
                          </div>
                        </button>
                        <div className="flex shrink-0 items-center gap-2">
                          {goal.is_active ? <CheckCircle2 style={{ color: theme.primary }} size={18} /> : null}
                          <button
                            type="button"
                            onClick={() => setGoalToDelete(goal)}
                            className="grid h-8 w-8 place-items-center rounded-[8px] bg-white text-red-500 ring-1 ring-red-100 transition hover:bg-red-50"
                            title={strings.actions.delete}
                          >
                            <Trash2 size={14} />
                          </button>
                        </div>
                      </div>
                    </article>
                  );
                })}
              </div>
            </div>

            {/* Sticky footer */}
            <div className="shrink-0 border-t border-slate-100 p-4">
              <button
                type="button"
                onClick={() => setShowAddArea(true)}
                className="flex h-12 w-full items-center justify-center gap-2 rounded-[10px] font-semibold text-white transition hover:brightness-95"
                style={{ background: "var(--area-primary)" }}
              >
                <Plus size={16} />
                {strings.profile.addArea}
              </button>
            </div>

          </section>
        </div>
      ) : null}

      {showAddArea && (
        <AddAreaModal
          onClose={() => setShowAddArea(false)}
          onCreated={(goal) => { onCreateGoal(goal); setShowAddArea(false); setIsAreaModalOpen(false); }}
        />
      )}

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
