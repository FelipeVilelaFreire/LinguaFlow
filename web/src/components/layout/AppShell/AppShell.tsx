"use client";

import {
  STRINGS,
  authService,
  contentService,
  getStudyAreaTheme,
  getStudyAreaThemeVars,
  ROUTES,
} from "@linguaflow/shared-core";
import type { Goal, User } from "@linguaflow/shared-core";
import { BookMarked, BookOpen, ChevronDown, ChevronRight, CircleUser, Flame, LayoutDashboard, LogOut, Swords } from "lucide-react";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import type { CSSProperties, ReactNode } from "react";
import { useEffect, useMemo, useState } from "react";
import { LangFlag } from "@/src/components/shared";
import styles from "./AppShell.module.css";

const NAV_ITEMS = [
  { href: ROUTES.home, label: STRINGS.nav.home, icon: LayoutDashboard },
  { href: ROUTES.adventure, label: STRINGS.nav.adventure, icon: Swords },
  { href: ROUTES.study, label: STRINGS.nav.study, icon: BookOpen },
  { href: ROUTES.vocabulary, label: STRINGS.nav.vocabulary, icon: BookMarked },
  { href: ROUTES.account, label: STRINGS.nav.profile, icon: CircleUser },
];

const PUBLIC_PATHS = new Set<string>([ROUTES.login, ROUTES.onboarding]);

export function AppShell({ children }: { children: ReactNode }) {
  const pathname = usePathname();
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [goal, setGoal] = useState<Goal | null>(null);
  const [loading, setLoading] = useState(true);

  const isPublic = PUBLIC_PATHS.has(pathname);
  const isImmersive = pathname.startsWith("/aventura/capitulo");

  useEffect(() => {
    if (isPublic || isImmersive) {
      setLoading(false);
      return;
    }

    let cancelled = false;
    async function loadShell() {
      setLoading(true);
      try {
        const [nextUser, nextGoal] = await Promise.all([
          authService.me(),
          contentService.getCurrentGoal().catch(() => null),
        ]);
        if (!cancelled) {
          setUser(nextUser);
          setGoal(nextGoal);
        }
      } catch {
        if (!cancelled) {
          setUser(null);
          setGoal(null);
        }
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    loadShell();
    return () => {
      cancelled = true;
    };
  }, [isImmersive, isPublic, pathname]);

  const theme = useMemo(() => getStudyAreaTheme(goal), [goal]);
  const themeVars = getStudyAreaThemeVars(theme) as CSSProperties;
  const currentLevel = goal?.current_level && goal.current_level !== "NONE" ? goal.current_level : null;

  if (isPublic || isImmersive) return <>{children}</>;

  function logout() {
    authService.logout();
    router.replace(ROUTES.login);
  }

  return (
    <div className={styles.shell} style={themeVars}>
      <header className={styles.mobileHeader}>
        <button className={styles.mobileBrand} type="button">
          <span className={styles.mobileIcon}><Flame size={16} /></span>
          <span className={styles.mobileText}>
          <img alt={STRINGS.app.name} className={styles.logo} src="/lang-plus.svg" />
          <span>{goal ? theme.label : STRINGS.app.subtitle}</span>
          </span>
          {currentLevel ? <small>{currentLevel}</small> : null}
          <ChevronDown size={14} />
        </button>
      </header>

      <aside className={styles.sidebar}>
        <div className={styles.sidebarTop}>
          <img alt={STRINGS.app.name} className={styles.sidebarLogo} src="/lang-plus.svg" />
          <p>{STRINGS.app.subtitle}</p>
        </div>

        <nav className={styles.sidebarNav}>
          {NAV_ITEMS.map((item) => {
            const active = item.href === ROUTES.home ? pathname === item.href : pathname.startsWith(item.href);
            return (
              <Link className={active ? styles.activeNavItem : styles.navItem} href={item.href} key={item.href}>
                <span className={styles.navLabel}><item.icon size={16} />{item.label}</span>
                {active ? <ChevronRight className={styles.chevron} size={14} /> : null}
              </Link>
            );
          })}
        </nav>

        <div className={styles.sidebarFooter}>
          <Link className={styles.areaButton} href={ROUTES.account}>
            {goal?.target_language?.code ? <LangFlag code={goal.target_language.code} size="sm" /> : <span className={styles.areaDot} />}
            <span>
              <strong>{goal ? theme.label : STRINGS.home.headline}</strong>
              <small>{goal ? `${goal.progress_percent}%${currentLevel ? ` · ${currentLevel}` : ""}` : STRINGS.app.subtitle}</small>
            </span>
          </Link>

          <div className={styles.userRow}>
            <span className={styles.avatar}>{user?.username?.charAt(0).toUpperCase() ?? "?"}</span>
            <span className={styles.username}>{user?.username ?? (loading ? STRINGS.app.loading : STRINGS.nav.profile)}</span>
            <button aria-label={STRINGS.admin.app.logout} className={styles.logoutButton} onClick={logout} type="button">
              <LogOut size={13} />
            </button>
          </div>
        </div>
      </aside>

      <main className={styles.main}>
        <div className={styles.content}>{children}</div>
      </main>

      <nav className={styles.bottomNav}>
        {NAV_ITEMS.map((item) => {
          const active = item.href === ROUTES.home ? pathname === item.href : pathname.startsWith(item.href);
          return (
            <Link className={active ? styles.activeBottomItem : styles.bottomItem} href={item.href} key={item.href}>
              <span><item.icon size={18} /></span>
              <small>{item.label}</small>
            </Link>
          );
        })}
      </nav>
    </div>
  );
}

