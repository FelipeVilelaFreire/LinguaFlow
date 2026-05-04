import { CheckCircle2, ChevronRight, Flame, LogOut, X } from "lucide-react";
import type { ReactNode } from "react";
import { useState } from "react";

import { useStrings } from "../../contexts/StringsContext";
import type { User } from "../../services/authService";
import { getStudyAreaTheme, getStudyAreaThemeStyle } from "../../theme/studyAreaTheme";
import type { Goal } from "../../types/content";
import type { AppRoute, NavItem } from "../../types/navigation";

interface AppLayoutProps {
  activeRoute: AppRoute;
  children: ReactNode;
  navItems: NavItem[];
  user: User;
  activeGoal: Goal;
  goals: Goal[];
  switchingAreaLabel: string | null;
  onLogout: () => void;
  onSwitchGoal: (goal: Goal) => void;
  onNavigate: (route: AppRoute) => void;
}

export default function AppLayout({ activeRoute, activeGoal, children, goals, navItems, switchingAreaLabel, user, onLogout, onSwitchGoal, onNavigate }: AppLayoutProps) {
  const [isAreaModalOpen, setIsAreaModalOpen] = useState(false);
  const strings = useStrings();
  const activeTheme = getStudyAreaTheme(activeGoal);
  const activeArea = activeTheme.label;

  return (
    <div className="min-h-screen text-slate-950 transition-colors duration-500" style={{ ...getStudyAreaThemeStyle(activeTheme), background: "var(--area-page)" }}>
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
          <button type="button" onClick={() => setIsAreaModalOpen(true)} className="w-full rounded-[8px] p-3 text-left ring-1 transition hover:brightness-[0.98]" style={{ background: "var(--area-primary-soft)", borderColor: "var(--area-primary-soft)" }}>
            <p className="text-xs font-semibold uppercase" style={{ color: "var(--area-primary-dark)" }}>{strings.layout.activeArea}</p>
            <p className="mt-1 truncate font-semibold text-slate-950">{activeArea}</p>
            <p className="mt-1 text-xs font-medium text-slate-500">{activeGoal.progress_percent}% {strings.layout.completed}</p>
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

      <main className="min-h-screen px-4 py-4 md:ml-72 md:px-8 md:py-8">
        <div key={activeRoute} className="mx-auto max-w-6xl animate-[fadeIn_220ms_ease-out]">{children}</div>
      </main>

      <nav className="fixed inset-x-0 bottom-0 z-20 grid grid-cols-6 border-t border-slate-200 bg-white md:hidden">
        {navItems.map((item) => (
          <button
            key={item.route}
            type="button"
            onClick={() => onNavigate(item.route)}
            className={`flex h-16 min-w-0 flex-col items-center justify-center gap-1 text-[10px] font-semibold ${
              activeRoute === item.route ? "text-emerald-700" : "text-slate-500"
            }`}
          >
            <item.icon size={18} />
            <span className="max-w-full truncate px-1">{strings.nav[item.labelKey]}</span>
          </button>
        ))}
      </nav>

      {isAreaModalOpen ? (
        <div className="fixed inset-0 z-40 grid place-items-center bg-slate-950/40 px-4 backdrop-blur-sm">
          <section className="w-full max-w-lg animate-[fadeIn_180ms_ease-out] rounded-[8px] bg-white p-5 shadow-xl ring-1 ring-slate-200">
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
              {goals.map((goal) => {
                const theme = getStudyAreaTheme(goal);
                return (
                  <button
                    key={goal.id}
                    type="button"
                    onClick={() => {
                      setIsAreaModalOpen(false);
                      onSwitchGoal(goal);
                    }}
                    className={`rounded-[8px] p-4 text-left ring-1 transition ${goal.is_active ? "" : "bg-white ring-slate-200 hover:bg-slate-50"}`}
                    style={goal.is_active ? { background: theme.primarySoft, boxShadow: `inset 0 0 0 1px ${theme.primary}` } : undefined}
                  >
                    <div className="flex items-start justify-between gap-4">
                      <div>
                        <p className="font-semibold">{theme.label}</p>
                        <p className="mt-0.5 text-sm font-medium" style={{ color: theme.primaryDark }}>{theme.name}</p>
                        <p className="mt-1 text-sm font-medium text-slate-500">{goal.progress_percent}% {strings.layout.completed}</p>
                      </div>
                      {goal.is_active ? <CheckCircle2 style={{ color: theme.primary }} size={20} /> : null}
                    </div>
                  </button>
                );
              })}
            </div>

            <button type="button" onClick={() => { setIsAreaModalOpen(false); onNavigate("account"); }} className="mt-4 h-11 w-full rounded-[8px] px-4 font-semibold text-white transition hover:brightness-95" style={{ background: "var(--area-primary)" }}>
              {strings.actions.manageInProfile}
            </button>
          </section>
        </div>
      ) : null}

      {switchingAreaLabel ? (
        <div className="fixed inset-0 z-50 grid place-items-center overflow-hidden text-white" style={{ background: "linear-gradient(135deg, var(--area-primary-dark), var(--area-primary))" }}>
          <div className="absolute inset-y-0 left-0 w-full animate-[areaSweep_900ms_ease-in-out] bg-white/10" />
          <div className="absolute h-72 w-72 rounded-full blur-3xl animate-[areaPulse_900ms_ease-in-out]" style={{ background: "var(--area-accent)" }} />
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
