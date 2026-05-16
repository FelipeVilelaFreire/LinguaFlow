import {
  Activity,
  BookOpen,
  Boxes,
  CheckCircle2,
  ChevronRight,
  Clock3,
  Database,
  GraduationCap,
  LayoutDashboard,
  LibraryBig,
  LogOut,
  RefreshCw,
  Search,
  Shield,
  Sparkles,
  Users,
} from "lucide-react";
import type { FormEvent, ReactNode } from "react";
import { useEffect, useMemo, useState } from "react";

import DataTable from "./components/DataTable";
import StatCard from "./components/StatCard";
import { adminApi } from "./services/api";
import type { AdminAdventure, AdminContent, AdminGoal, AdminLearningDetail, AdminProgressDetail, AdminSummary, AdminUser } from "./types/admin";

type AdminTab = "dashboard" | "users" | "goals" | "content" | "learning" | "adventure" | "progress" | "system";

const NAV_GROUPS: Array<{
  label: string;
  items: Array<{ tab: AdminTab; label: string; description: string; icon: ReactNode }>;
}> = [
  {
    label: "Operacao",
    items: [
      { tab: "dashboard", label: "Dashboard", description: "Visao geral", icon: <LayoutDashboard size={18} /> },
      { tab: "users", label: "Usuarios", description: "Contas e acesso", icon: <Users size={18} /> },
      { tab: "goals", label: "Areas", description: "Cursos ativos", icon: <GraduationCap size={18} /> },
    ],
  },
  {
    label: "Conteudo",
    items: [
      { tab: "content", label: "Catalogo", description: "Idiomas, cenarios e frases", icon: <BookOpen size={18} /> },
      { tab: "learning", label: "Estudo", description: "Modulos, aulas e study days", icon: <LibraryBig size={18} /> },
      { tab: "adventure", label: "Aventura", description: "Capitulos, fases e secoes", icon: <Sparkles size={18} /> },
      { tab: "progress", label: "Progresso", description: "Conclusoes e maestria", icon: <Activity size={18} /> },
      { tab: "system", label: "Apps Django", description: "Mapa dos dominios", icon: <Boxes size={18} /> },
    ],
  },
];

const DJANGO_APPS = [
  { name: "accounts", label: "Contas", models: "Usuarios, autenticacao e admin dashboard", status: "Conectado" },
  { name: "goals", label: "Areas de estudo", models: "Objetivos, idioma fonte/alvo e rotina", status: "Conectado" },
  { name: "learning", label: "Estudo", models: "Idiomas, cenarios, frases, aulas e study days", status: "Conectado" },
  { name: "progress", label: "Progresso", models: "Favoritos, conclusoes e entradas de progresso", status: "Resumo" },
  { name: "adventure", label: "Aventura", models: "Capitulos, fases, itens, baus e vocabulario", status: "Planejado" },
];

export default function App() {
  const [authenticated, setAuthenticated] = useState(adminApi.isAuthenticated());
  const [tab, setTab] = useState<AdminTab>("dashboard");
  const [summary, setSummary] = useState<AdminSummary | null>(null);
  const [users, setUsers] = useState<AdminUser[]>([]);
  const [goals, setGoals] = useState<AdminGoal[]>([]);
  const [content, setContent] = useState<AdminContent | null>(null);
  const [learning, setLearning] = useState<AdminLearningDetail | null>(null);
  const [adventure, setAdventure] = useState<AdminAdventure | null>(null);
  const [progress, setProgress] = useState<AdminProgressDetail | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [query, setQuery] = useState("");

  useEffect(() => {
    if (authenticated) void loadAll();
  }, [authenticated]);

  async function loadAll() {
    setLoading(true);
    setError(null);
    try {
      const [nextSummary, nextUsers, nextGoals, nextContent, nextLearning, nextAdventure, nextProgress] = await Promise.all([
        adminApi.summary(),
        adminApi.users(),
        adminApi.goals(),
        adminApi.content(),
        adminApi.learningDetail(),
        adminApi.adventure(),
        adminApi.progressDetail(),
      ]);
      setSummary(nextSummary);
      setUsers(nextUsers);
      setGoals(nextGoals);
      setContent(nextContent);
      setLearning(nextLearning);
      setAdventure(nextAdventure);
      setProgress(nextProgress);
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : "Erro inesperado.");
    } finally {
      setLoading(false);
    }
  }

  function logout() {
    adminApi.logout();
    setAuthenticated(false);
  }

  const filteredUsers = useMemo(() => {
    const normalized = query.trim().toLowerCase();
    if (!normalized) return users;
    return users.filter((user) =>
      [user.username, user.email, String(user.id)].some((value) => value.toLowerCase().includes(normalized)),
    );
  }, [query, users]);

  const filteredGoals = useMemo(() => {
    const normalized = query.trim().toLowerCase();
    if (!normalized) return goals;
    return goals.filter((goal) =>
      [goal.user ?? "", goal.source_language, goal.target_language, goal.current_level, goal.target_level]
        .some((value) => value.toLowerCase().includes(normalized)),
    );
  }, [goals, query]);

  if (!authenticated) return <LoginScreen onAuthenticated={() => setAuthenticated(true)} />;

  return (
    <div className="min-h-screen bg-paper text-slate-950">
      <aside className="fixed inset-y-0 left-0 hidden w-[292px] border-r border-line bg-white px-4 py-5 lg:block">
        <BrandBlock />

        <nav className="mt-8 space-y-7">
          {NAV_GROUPS.map((group) => (
            <div key={group.label}>
              <p className="px-3 text-[11px] font-bold uppercase tracking-[0.14em] text-slate-400">{group.label}</p>
              <div className="mt-2 space-y-1">
                {group.items.map((item) => (
                  <NavButton
                    key={item.tab}
                    active={tab === item.tab}
                    icon={item.icon}
                    label={item.label}
                    description={item.description}
                    onClick={() => {
                      setTab(item.tab);
                      setQuery("");
                    }}
                  />
                ))}
              </div>
            </div>
          ))}
        </nav>

        <div className="absolute inset-x-4 bottom-5 rounded-[8px] border border-line bg-slate-50 p-3">
          <div className="flex items-center gap-2 text-sm font-semibold text-slate-700">
            <span className="grid h-8 w-8 place-items-center rounded-[8px] bg-emerald-50 text-emerald-700">
              <CheckCircle2 size={16} />
            </span>
            Django API
          </div>
          <p className="mt-2 text-xs font-medium leading-5 text-slate-500">Usando os endpoints admin existentes em `/api/admin-dashboard/*`.</p>
        </div>
      </aside>

      <main className="min-h-screen lg:ml-[292px]">
        <TopBar tab={tab} loading={loading} onRefresh={loadAll} onLogout={logout} />

        <div className="mx-auto max-w-[1500px] px-4 py-5 sm:px-6 lg:px-8">
          <MobileNav activeTab={tab} onChange={setTab} />

          {error ? (
            <div className="mb-5 rounded-[8px] border border-red-100 bg-red-50 px-4 py-3 text-sm font-semibold text-red-700">{error}</div>
          ) : null}

          {(tab === "users" || tab === "goals" || tab === "content" || tab === "learning" || tab === "adventure" || tab === "progress") && (
            <div className="mb-5 flex flex-col gap-3 rounded-[8px] border border-line bg-white p-3 shadow-sm sm:flex-row sm:items-center sm:justify-between">
              <div className="relative min-w-0 flex-1">
                <Search className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" size={17} />
                <input
                  value={query}
                  onChange={(event) => setQuery(event.target.value)}
                  placeholder={getSearchPlaceholder(tab)}
                  className="h-11 w-full rounded-[8px] border border-line bg-slate-50 pl-10 pr-3 text-sm font-medium outline-none transition focus:border-brand focus:bg-white"
                />
              </div>
              <span className="rounded-[8px] bg-slate-50 px-3 py-2 text-sm font-semibold text-slate-500 ring-1 ring-line">
                {getResultCount(tab, filteredUsers.length, filteredGoals.length, content, learning, adventure, progress)}
              </span>
            </div>
          )}

          {tab === "dashboard" ? <Dashboard summary={summary} users={users} goals={goals} content={content} loading={loading} /> : null}
          {tab === "users" ? <UsersTable users={filteredUsers} /> : null}
          {tab === "goals" ? <GoalsTable goals={filteredGoals} /> : null}
          {tab === "content" ? <ContentPanel content={content} query={query} /> : null}
          {tab === "learning" ? <LearningPanel learning={learning} query={query} /> : null}
          {tab === "adventure" ? <AdventurePanel adventure={adventure} query={query} /> : null}
          {tab === "progress" ? <ProgressPanel progress={progress} query={query} /> : null}
          {tab === "system" ? <SystemPanel summary={summary} /> : null}
        </div>
      </main>
    </div>
  );
}

function BrandBlock() {
  return (
    <div className="flex items-center gap-3">
      <img src="/lang-plus.svg" alt="Lang+" className="admin-brand-logo" />
      <div className="min-w-0">
        <h1 className="text-lg font-bold tracking-tight">Admin</h1>
        <p className="text-xs font-bold uppercase tracking-[0.14em] text-slate-400">Backoffice</p>
      </div>
    </div>
  );
}

function TopBar({ tab, loading, onRefresh, onLogout }: { tab: AdminTab; loading: boolean; onRefresh: () => void; onLogout: () => void }) {
  return (
    <header className="sticky top-0 z-20 border-b border-line bg-white/95 backdrop-blur">
      <div className="mx-auto flex max-w-[1500px] items-center justify-between gap-4 px-4 py-4 sm:px-6 lg:px-8">
        <div className="min-w-0">
          <p className="flex items-center gap-2 text-xs font-bold uppercase tracking-[0.14em] text-brand">
            Painel administrativo
            <ChevronRight size={14} />
            {getTabTitle(tab)}
          </p>
          <h2 className="mt-1 truncate text-2xl font-bold tracking-tight sm:text-3xl">{getTabTitle(tab)}</h2>
        </div>
        <div className="flex shrink-0 items-center gap-2">
          <button type="button" onClick={onRefresh} className="admin-icon-button" aria-label="Atualizar dados">
            <RefreshCw size={17} className={loading ? "animate-spin" : ""} />
          </button>
          <button type="button" onClick={onLogout} className="admin-icon-button" aria-label="Sair">
            <LogOut size={17} />
          </button>
        </div>
      </div>
    </header>
  );
}

function LoginScreen({ onAuthenticated }: { onAuthenticated: () => void }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function submit(event: FormEvent) {
    event.preventDefault();
    setLoading(true);
    setError(null);
    try {
      await adminApi.login(username, password);
      onAuthenticated();
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : "Nao foi possivel entrar.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="grid min-h-screen place-items-center bg-paper px-4">
      <form onSubmit={submit} className="w-full max-w-md rounded-[8px] border border-line bg-white p-6 shadow-soft">
        <BrandBlock />
        <p className="mt-5 text-sm font-medium leading-6 text-slate-500">Entre com um usuario staff ou superuser para gerenciar conteudo, usuarios e areas.</p>

        <label className="mt-6 block">
          <span className="text-sm font-semibold text-slate-600">Usuario</span>
          <input value={username} onChange={(event) => setUsername(event.target.value)} className="admin-input mt-2" autoComplete="username" />
        </label>
        <label className="mt-4 block">
          <span className="text-sm font-semibold text-slate-600">Senha</span>
          <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} className="admin-input mt-2" autoComplete="current-password" />
        </label>
        {error ? <p className="mt-4 rounded-[8px] bg-red-50 p-3 text-sm font-semibold text-red-700">{error}</p> : null}
        <button disabled={loading} className="mt-6 h-12 w-full rounded-[8px] bg-brand font-semibold text-white transition hover:brightness-95 disabled:opacity-60">
          {loading ? "Entrando..." : "Entrar"}
        </button>
      </form>
    </main>
  );
}

function Dashboard({ summary, users, goals, content, loading }: { summary: AdminSummary | null; users: AdminUser[]; goals: AdminGoal[]; content: AdminContent | null; loading: boolean }) {
  if (!summary) return <EmptyState loading={loading} />;
  const completionRate = summary.phrases ? Math.round((summary.completions / summary.phrases) * 100) : 0;
  const activeUsers = users.filter((user) => user.is_active).length;
  const activeGoals = goals.filter((goal) => goal.is_active).length;

  return (
    <div className="space-y-5">
      <section className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        <StatCard icon={<Users size={20} />} label="Usuarios" value={summary.users} detail={`${activeUsers} ativos`} />
        <StatCard icon={<GraduationCap size={20} />} label="Areas ativas" value={summary.active_goals} detail={`${activeGoals} em andamento`} />
        <StatCard icon={<BookOpen size={20} />} label="Frases" value={summary.phrases} detail={`${summary.lessons} aulas`} />
        <StatCard icon={<Database size={20} />} label="Conclusoes" value={summary.completions} detail={`${completionRate}% vs frases`} />
      </section>

      <section className="grid gap-5 xl:grid-cols-[1.1fr_0.9fr]">
        <div className="rounded-[8px] border border-line bg-white p-5 shadow-sm">
          <div className="flex items-center justify-between gap-3">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.14em] text-slate-400">Saude do produto</p>
              <h3 className="mt-1 text-lg font-bold">Resumo operacional</h3>
            </div>
            <Activity className="text-brand" size={22} />
          </div>
          <div className="mt-5 grid gap-3 sm:grid-cols-2">
            <HealthRow label="Staff" value={summary.staff_users} total={summary.users} />
            <HealthRow label="Study days" value={summary.study_days} total={Math.max(summary.lessons, 1)} />
            <HealthRow label="Favoritos" value={summary.favorites} total={Math.max(summary.phrases, 1)} />
            <HealthRow label="Progresso" value={summary.progress_entries} total={Math.max(summary.completions, 1)} />
          </div>
        </div>

        <div className="rounded-[8px] border border-line bg-white p-5 shadow-sm">
          <p className="text-xs font-bold uppercase tracking-[0.14em] text-slate-400">Conteudo</p>
          <h3 className="mt-1 text-lg font-bold">Inventario publicado</h3>
          <div className="mt-5 grid gap-3">
            <InventoryRow icon={<LibraryBig size={17} />} label="Idiomas" value={summary.languages} />
            <InventoryRow icon={<Sparkles size={17} />} label="Cenarios" value={summary.scenarios} />
            <InventoryRow icon={<Clock3 size={17} />} label="Study days" value={content?.study_day_count ?? summary.study_days} />
          </div>
        </div>
      </section>
    </div>
  );
}

function UsersTable({ users }: { users: AdminUser[] }) {
  return (
    <DataTable title="Usuarios" description="Contas cadastradas no Django" columns={["ID", "Usuario", "Email", "Acesso", "Status", "Areas", "Conclusoes", "Entrada"]} empty={users.length === 0}>
      {users.map((user) => (
        <tr key={user.id} className="transition hover:bg-slate-50/80">
          <td className="px-4 py-3 font-semibold">{user.id}</td>
          <td className="px-4 py-3">
            <div className="font-semibold">{user.username}</div>
            {user.is_superuser ? <span className="admin-badge admin-badge-strong mt-1">Superuser</span> : null}
          </td>
          <td className="px-4 py-3 text-slate-500">{user.email || "-"}</td>
          <td className="px-4 py-3"><StatusBadge active={user.is_staff} activeLabel="Staff" inactiveLabel="Aluno" /></td>
          <td className="px-4 py-3"><StatusBadge active={user.is_active} activeLabel="Ativo" inactiveLabel="Inativo" /></td>
          <td className="px-4 py-3">{user.goal_count}</td>
          <td className="px-4 py-3">{user.completion_count}</td>
          <td className="px-4 py-3 text-slate-500">{formatDate(user.date_joined)}</td>
        </tr>
      ))}
    </DataTable>
  );
}

function GoalsTable({ goals }: { goals: AdminGoal[] }) {
  return (
    <DataTable title="Areas de estudo" description="Cursos criados pelos usuarios" columns={["ID", "Usuario", "Curso", "Nivel", "Rotina", "Progresso", "Streak", "Status"]} empty={goals.length === 0}>
      {goals.map((goal) => (
        <tr key={goal.id} className="transition hover:bg-slate-50/80">
          <td className="px-4 py-3 font-semibold">{goal.id}</td>
          <td className="px-4 py-3">{goal.user ?? "-"}</td>
          <td className="px-4 py-3">
            <div className="font-semibold">{goal.source_language} -&gt; {goal.target_language}</div>
            <span className="text-xs font-medium text-slate-500">{goal.duration_days} dias planejados</span>
          </td>
          <td className="px-4 py-3">{goal.current_level} -&gt; {goal.target_level}</td>
          <td className="px-4 py-3">{formatWeekdays(goal.study_weekdays)} / {goal.session_minutes} min</td>
          <td className="px-4 py-3">
            <ProgressCell current={goal.learned_phrases} total={goal.total_phrases} />
          </td>
          <td className="px-4 py-3">{goal.streak_days}</td>
          <td className="px-4 py-3"><StatusBadge active={goal.is_active} activeLabel="Ativa" inactiveLabel="Pausada" /></td>
        </tr>
      ))}
    </DataTable>
  );
}

function ContentPanel({ content, query }: { content: AdminContent | null; query: string }) {
  const normalized = query.trim().toLowerCase();
  const phraseCounts = useMemo(() => Object.entries(content?.phrase_counts ?? {}), [content]);
  const scenarios = useMemo(() => {
    if (!content) return [];
    if (!normalized) return content.scenarios;
    return content.scenarios.filter((scenario) =>
      [scenario.title, scenario.slug].some((value) => value.toLowerCase().includes(normalized)),
    );
  }, [content, normalized]);

  if (!content) return <EmptyState />;

  return (
    <div className="grid gap-5 xl:grid-cols-[1fr_360px]">
      <DataTable title="Cenarios" description="Conteudo de estudo agrupado por contexto" columns={["Cenario", "Slug", "Frases", "Aulas"]} empty={scenarios.length === 0}>
        {scenarios.map((scenario) => (
          <tr key={scenario.id} className="transition hover:bg-slate-50/80">
            <td className="px-4 py-3 font-semibold">{scenario.title}</td>
            <td className="px-4 py-3 text-slate-500">{scenario.slug}</td>
            <td className="px-4 py-3">{scenario.phrase_count}</td>
            <td className="px-4 py-3">{scenario.lesson_count}</td>
          </tr>
        ))}
      </DataTable>

      <aside className="space-y-4">
        <Panel title="Idiomas" eyebrow="Catalogo">
          <div className="flex flex-wrap gap-2">
            {content.languages.map((language) => (
              <span key={language.id} className="rounded-[8px] bg-slate-50 px-3 py-2 text-sm font-semibold ring-1 ring-line">
                {language.code} - {language.name}
              </span>
            ))}
          </div>
        </Panel>

        <Panel title="Frases por curso" eyebrow={`${content.lesson_count} aulas / ${content.study_day_count} study days`}>
          <div className="grid gap-2">
            {phraseCounts.map(([label, count]) => (
              <div key={label} className="flex items-center justify-between rounded-[8px] bg-slate-50 px-3 py-2 ring-1 ring-line">
                <span className="font-semibold">{label}</span>
                <span className="text-slate-500">{count}</span>
              </div>
            ))}
          </div>
        </Panel>
      </aside>
    </div>
  );
}

function LearningPanel({ learning, query }: { learning: AdminLearningDetail | null; query: string }) {
  const normalized = query.trim().toLowerCase();
  const lessons = useMemo(() => {
    if (!learning) return [];
    if (!normalized) return learning.lessons;
    return learning.lessons.filter((item) =>
      [item.title, item.scenario, item.module, item.objective].some((value) => value.toLowerCase().includes(normalized)),
    );
  }, [learning, normalized]);
  const phrases = useMemo(() => {
    if (!learning) return [];
    if (!normalized) return learning.phrases.slice(0, 80);
    return learning.phrases.filter((item) =>
      [item.source_text, item.target_text, item.category, item.scenario].some((value) => value.toLowerCase().includes(normalized)),
    ).slice(0, 80);
  }, [learning, normalized]);

  if (!learning) return <EmptyState />;

  return (
    <div className="space-y-5">
      <section className="grid gap-4 md:grid-cols-3">
        <StatCard icon={<LibraryBig size={20} />} label="Modulos" value={learning.modules.length} detail="Agrupam cenarios" />
        <StatCard icon={<BookOpen size={20} />} label="Aulas" value={learning.lessons.length} detail={`${learning.study_days.length} study days`} />
        <StatCard icon={<Database size={20} />} label="Frases recentes" value={learning.phrases.length} detail="Ultimas 250" />
      </section>

      <div className="grid gap-5 xl:grid-cols-[1fr_420px]">
        <DataTable title="Aulas" description="Lessons usadas no modo Estudo" columns={["Dia", "Aula", "Modulo", "Cenario", "Frases", "Video"]} empty={lessons.length === 0}>
          {lessons.map((lesson) => (
            <tr key={lesson.id} className="transition hover:bg-slate-50/80">
              <td className="px-4 py-3 font-semibold">{lesson.day_number}</td>
              <td className="px-4 py-3">
                <div className="font-semibold">{lesson.title}</div>
                <span className="text-xs font-medium text-slate-500">{lesson.objective || "-"}</span>
              </td>
              <td className="px-4 py-3">{lesson.module || "-"}</td>
              <td className="px-4 py-3">{lesson.scenario}</td>
              <td className="px-4 py-3">{lesson.phrase_count}</td>
              <td className="px-4 py-3"><StatusBadge active={lesson.has_video} activeLabel="Sim" inactiveLabel="Nao" /></td>
            </tr>
          ))}
        </DataTable>

        <div className="space-y-4">
          <Panel title="Modulos" eyebrow="Estrutura">
            <div className="grid gap-2">
              {learning.modules.map((module) => (
                <div key={module.id} className="rounded-[8px] bg-slate-50 px-3 py-2 ring-1 ring-line">
                  <p className="font-semibold">{module.lang_code} - {module.title}</p>
                  <p className="text-xs font-medium text-slate-500">{module.scenario_count} cenarios / ordem {module.order}</p>
                </div>
              ))}
            </div>
          </Panel>

          <Panel title="Study days" eyebrow="Calendario">
            <div className="max-h-[320px] space-y-2 overflow-auto pr-1">
              {learning.study_days.slice(0, 80).map((day) => (
                <div key={day.id} className="flex items-center justify-between gap-2 rounded-[8px] bg-slate-50 px-3 py-2 ring-1 ring-line">
                  <span className="text-sm font-semibold">Dia {day.day_number}: {day.lesson}</span>
                  <StatusBadge active={day.is_active} activeLabel="Ativo" inactiveLabel="Off" />
                </div>
              ))}
            </div>
          </Panel>
        </div>
      </div>

      <DataTable title="Frases" description="Amostra das frases do catalogo" columns={["ID", "Par", "Origem", "Destino", "Cenario", "Nivel"]} empty={phrases.length === 0}>
        {phrases.map((phrase) => (
          <tr key={phrase.id} className="transition hover:bg-slate-50/80">
            <td className="px-4 py-3 font-semibold">{phrase.id}</td>
            <td className="px-4 py-3">{phrase.source_language} -&gt; {phrase.target_language}</td>
            <td className="px-4 py-3">{phrase.source_text}</td>
            <td className="px-4 py-3 font-semibold">{phrase.target_text}</td>
            <td className="px-4 py-3 text-slate-500">{phrase.scenario || "-"}</td>
            <td className="px-4 py-3">{phrase.difficulty}</td>
          </tr>
        ))}
      </DataTable>
    </div>
  );
}

function AdventurePanel({ adventure, query }: { adventure: AdminAdventure | null; query: string }) {
  const normalized = query.trim().toLowerCase();
  const phases = useMemo(() => {
    if (!adventure) return [];
    if (!normalized) return adventure.phases;
    return adventure.phases.filter((item) =>
      [item.title, item.chapter, item.scenario_slug, item.phase_type].some((value) => value.toLowerCase().includes(normalized)),
    );
  }, [adventure, normalized]);
  const sections = useMemo(() => {
    if (!adventure) return [];
    if (!normalized) return adventure.sections.slice(0, 120);
    return adventure.sections.filter((item) =>
      [item.chapter, item.section_type, String(item.phase)].some((value) => value.toLowerCase().includes(normalized)),
    ).slice(0, 120);
  }, [adventure, normalized]);

  if (!adventure) return <EmptyState />;

  return (
    <div className="space-y-5">
      <section className="grid gap-4 md:grid-cols-4">
        <StatCard icon={<BookOpen size={20} />} label="Capitulos" value={adventure.chapters.length} detail="Temporadas/idiomas" />
        <StatCard icon={<Sparkles size={20} />} label="Fases" value={adventure.phases.length} detail={`${adventure.sections.length} secoes`} />
        <StatCard icon={<Users size={20} />} label="Personagens" value={adventure.characters.length} detail={`${adventure.skills.length} skills`} />
        <StatCard icon={<Boxes size={20} />} label="Itens" value={adventure.items.length} detail={`${adventure.user_counts.chests} baus de usuario`} />
      </section>

      <div className="grid gap-5 xl:grid-cols-[1fr_420px]">
        <DataTable title="Fases" description="Fases da aventura por capitulo" columns={["#", "Titulo", "Capitulo", "Tipo", "Cenario", "Secoes", "Bau"]} empty={phases.length === 0}>
          {phases.map((phase) => (
            <tr key={phase.id} className="transition hover:bg-slate-50/80">
              <td className="px-4 py-3 font-semibold">{phase.number}</td>
              <td className="px-4 py-3 font-semibold">{phase.title}</td>
              <td className="px-4 py-3">{phase.language} / {phase.chapter}</td>
              <td className="px-4 py-3"><span className="admin-badge">{phase.phase_type}</span></td>
              <td className="px-4 py-3 text-slate-500">{phase.scenario_slug}</td>
              <td className="px-4 py-3">{phase.section_count}</td>
              <td className="px-4 py-3"><StatusBadge active={phase.has_chest} activeLabel={phase.chest_tier || "Sim"} inactiveLabel="Nao" /></td>
            </tr>
          ))}
        </DataTable>

        <div className="space-y-4">
          <Panel title="Capitulos" eyebrow="Temporadas">
            <div className="grid gap-2">
              {adventure.chapters.map((chapter) => (
                <div key={chapter.id} className="rounded-[8px] bg-slate-50 px-3 py-2 ring-1 ring-line">
                  <p className="font-semibold">{chapter.language} {chapter.level} - {chapter.title}</p>
                  <p className="text-xs font-medium text-slate-500">{chapter.phase_count} fases / boss {chapter.boss_name}</p>
                </div>
              ))}
            </div>
          </Panel>

          <Panel title="Personagens e itens" eyebrow="Narrativa">
            <div className="grid gap-2">
              {adventure.characters.slice(0, 8).map((character) => (
                <div key={character.id} className="flex items-center justify-between rounded-[8px] bg-slate-50 px-3 py-2 ring-1 ring-line">
                  <span className="font-semibold">{character.emoji} {character.name}</span>
                  <span className="text-xs font-bold text-slate-500">{character.character_type}</span>
                </div>
              ))}
            </div>
          </Panel>
        </div>
      </div>

      <DataTable title="Secoes" description="As 6 telas/blocos de cada fase" columns={["Capitulo", "Fase", "Secao", "Tipo", "Steps"]} empty={sections.length === 0}>
        {sections.map((section) => (
          <tr key={section.id} className="transition hover:bg-slate-50/80">
            <td className="px-4 py-3">{section.chapter}</td>
            <td className="px-4 py-3 font-semibold">{section.phase}</td>
            <td className="px-4 py-3">{section.section_number}</td>
            <td className="px-4 py-3"><span className="admin-badge">{section.section_type}</span></td>
            <td className="px-4 py-3">{section.step_count}</td>
          </tr>
        ))}
      </DataTable>
    </div>
  );
}

function ProgressPanel({ progress, query }: { progress: AdminProgressDetail | null; query: string }) {
  const normalized = query.trim().toLowerCase();
  const entries = useMemo(() => {
    if (!progress) return [];
    if (!normalized) return progress.progress_entries;
    return progress.progress_entries.filter((item) =>
      [item.user, item.phrase, item.status].some((value) => value.toLowerCase().includes(normalized)),
    );
  }, [progress, normalized]);

  if (!progress) return <EmptyState />;

  return (
    <div className="space-y-5">
      <section className="grid gap-4 md:grid-cols-4">
        <StatCard icon={<CheckCircle2 size={20} />} label="Conclusoes" value={progress.completions.length} detail="Ultimas 200" />
        <StatCard icon={<Activity size={20} />} label="SRS" value={progress.progress_entries.length} detail="Ultimas 250" />
        <StatCard icon={<Sparkles size={20} />} label="Maestria" value={progress.word_mastery.length} detail="Palavras rastreadas" />
        <StatCard icon={<Clock3 size={20} />} label="Streaks" value={progress.streaks.length} detail="Usuarios com streak" />
      </section>

      <div className="grid gap-5 xl:grid-cols-[1fr_420px]">
        <DataTable title="Progresso SRS" description="Estado das frases por usuario" columns={["Usuario", "Frase", "Status", "Acertos", "Erros", "Revisao"]} empty={entries.length === 0}>
          {entries.map((item) => (
            <tr key={item.id} className="transition hover:bg-slate-50/80">
              <td className="px-4 py-3 font-semibold">{item.user || "-"}</td>
              <td className="px-4 py-3">{item.phrase}</td>
              <td className="px-4 py-3"><span className="admin-badge">{item.status}</span></td>
              <td className="px-4 py-3">{item.correct_count}</td>
              <td className="px-4 py-3">{item.incorrect_count}</td>
              <td className="px-4 py-3 text-slate-500">{item.review_due || "-"}</td>
            </tr>
          ))}
        </DataTable>

        <div className="space-y-4">
          <Panel title="Streaks" eyebrow="Engajamento">
            <div className="grid gap-2">
              {progress.streaks.slice(0, 12).map((streak) => (
                <div key={streak.id} className="flex items-center justify-between rounded-[8px] bg-slate-50 px-3 py-2 ring-1 ring-line">
                  <span className="font-semibold">{streak.user}</span>
                  <span className="text-sm font-bold text-brand">{streak.current_streak}/{streak.longest_streak}</span>
                </div>
              ))}
            </div>
          </Panel>

          <Panel title="Maestria" eyebrow="Palavras">
            <div className="max-h-[320px] space-y-2 overflow-auto pr-1">
              {progress.word_mastery.slice(0, 20).map((word) => (
                <div key={word.id} className="rounded-[8px] bg-slate-50 px-3 py-2 ring-1 ring-line">
                  <p className="font-semibold">{word.target || word.word_id}</p>
                  <p className="text-xs font-medium text-slate-500">{word.user} / {word.tier} / streak {word.streak}</p>
                </div>
              ))}
            </div>
          </Panel>
        </div>
      </div>
    </div>
  );
}

function SystemPanel({ summary }: { summary: AdminSummary | null }) {
  return (
    <div className="grid gap-5 xl:grid-cols-[1fr_360px]">
      <Panel title="Apps Django" eyebrow="Mapa dos dominios">
        <div className="grid gap-3">
          {DJANGO_APPS.map((app) => (
            <div key={app.name} className="rounded-[8px] border border-line bg-white p-4">
              <div className="flex items-start justify-between gap-3">
                <div>
                  <p className="font-bold">{app.label}</p>
                  <p className="mt-1 text-sm font-medium text-slate-500">{app.models}</p>
                  <code className="mt-2 inline-block rounded bg-slate-50 px-2 py-1 text-xs font-semibold text-slate-500">apps/{app.name}</code>
                </div>
                <span className="admin-badge">{app.status}</span>
              </div>
            </div>
          ))}
        </div>
      </Panel>

      <Panel title="Endpoints ativos" eyebrow="Admin API">
        <Endpoint path="/api/admin-dashboard/summary/" value={summary?.users ?? 0} label="usuarios no resumo" />
        <Endpoint path="/api/admin-dashboard/users/" value={summary?.staff_users ?? 0} label="staff users" />
        <Endpoint path="/api/admin-dashboard/goals/" value={summary?.goals ?? 0} label="areas totais" />
        <Endpoint path="/api/admin-dashboard/content/" value={summary?.phrases ?? 0} label="frases catalogadas" />
      </Panel>
    </div>
  );
}

function NavButton({ active, icon, label, description, onClick }: { active: boolean; icon: ReactNode; label: string; description: string; onClick: () => void }) {
  return (
    <button type="button" onClick={onClick} className={`flex w-full items-center gap-3 rounded-[8px] px-3 py-3 text-left transition ${active ? "bg-brand text-white shadow-sm" : "text-slate-600 hover:bg-slate-50"}`}>
      <span className={`grid h-9 w-9 place-items-center rounded-[8px] ${active ? "bg-white/15" : "bg-slate-50 text-brand"}`}>{icon}</span>
      <span className="min-w-0">
        <span className="block text-sm font-bold">{label}</span>
        <span className={`block truncate text-xs font-medium ${active ? "text-white/75" : "text-slate-400"}`}>{description}</span>
      </span>
    </button>
  );
}

function MobileNav({ activeTab, onChange }: { activeTab: AdminTab; onChange: (tab: AdminTab) => void }) {
  const items = NAV_GROUPS.flatMap((group) => group.items);
  return (
    <div className="mb-5 grid grid-cols-2 gap-2 lg:hidden sm:grid-cols-5">
      {items.map((item) => (
        <button key={item.tab} type="button" onClick={() => onChange(item.tab)} className={`h-11 rounded-[8px] px-3 text-sm font-bold ring-1 ${activeTab === item.tab ? "bg-brand text-white ring-brand" : "bg-white text-slate-600 ring-line"}`}>
          {item.label}
        </button>
      ))}
    </div>
  );
}

function Panel({ title, eyebrow, children }: { title: string; eyebrow: string; children: ReactNode }) {
  return (
    <section className="rounded-[8px] border border-line bg-white p-5 shadow-sm">
      <p className="text-xs font-bold uppercase tracking-[0.14em] text-slate-400">{eyebrow}</p>
      <h3 className="mt-1 text-lg font-bold">{title}</h3>
      <div className="mt-4">{children}</div>
    </section>
  );
}

function HealthRow({ label, value, total }: { label: string; value: number; total: number }) {
  const percent = Math.min(100, Math.round((value / Math.max(total, 1)) * 100));
  return (
    <div className="rounded-[8px] bg-slate-50 p-3 ring-1 ring-line">
      <div className="flex items-center justify-between text-sm font-semibold">
        <span>{label}</span>
        <span className="text-slate-500">{value.toLocaleString("pt-BR")}</span>
      </div>
      <div className="mt-3 h-2 rounded-full bg-white">
        <div className="h-2 rounded-full bg-brand" style={{ width: `${percent}%` }} />
      </div>
    </div>
  );
}

function InventoryRow({ icon, label, value }: { icon: ReactNode; label: string; value: number }) {
  return (
    <div className="flex items-center justify-between rounded-[8px] bg-slate-50 px-3 py-3 ring-1 ring-line">
      <span className="flex items-center gap-2 font-semibold text-slate-700">{icon}{label}</span>
      <span className="text-lg font-bold">{value.toLocaleString("pt-BR")}</span>
    </div>
  );
}

function StatusBadge({ active, activeLabel, inactiveLabel }: { active: boolean; activeLabel: string; inactiveLabel: string }) {
  return <span className={`admin-badge ${active ? "admin-badge-active" : ""}`}>{active ? activeLabel : inactiveLabel}</span>;
}

function ProgressCell({ current, total }: { current: number; total: number }) {
  const percent = total ? Math.round((current / total) * 100) : 0;
  return (
    <div className="min-w-[140px]">
      <div className="flex justify-between text-xs font-semibold text-slate-500">
        <span>{current} / {total}</span>
        <span>{percent}%</span>
      </div>
      <div className="mt-2 h-2 rounded-full bg-slate-100">
        <div className="h-2 rounded-full bg-brand" style={{ width: `${Math.min(percent, 100)}%` }} />
      </div>
    </div>
  );
}

function Endpoint({ path, value, label }: { path: string; value: number; label: string }) {
  return (
    <div className="mb-3 rounded-[8px] bg-slate-50 p-3 ring-1 ring-line">
      <code className="text-xs font-semibold text-slate-500">{path}</code>
      <p className="mt-2 text-sm font-semibold">{value.toLocaleString("pt-BR")} {label}</p>
    </div>
  );
}

function EmptyState({ loading = false }: { loading?: boolean }) {
  return (
    <div className="rounded-[8px] border border-line bg-white p-6 font-semibold text-slate-500 shadow-sm">
      {loading ? "Carregando dados..." : "Sem dados carregados."}
    </div>
  );
}

function getTabTitle(tab: AdminTab) {
  return {
    dashboard: "Dashboard",
    users: "Usuarios",
    goals: "Areas",
    content: "Catalogo",
    learning: "Estudo",
    adventure: "Aventura",
    progress: "Progresso",
    system: "Apps Django",
  }[tab];
}

function getSearchPlaceholder(tab: AdminTab) {
  return {
    dashboard: "Buscar",
    users: "Buscar por usuario, email ou ID",
    goals: "Buscar por usuario, idioma ou nivel",
    content: "Buscar cenario ou slug",
    learning: "Buscar aula, modulo, frase ou cenario",
    adventure: "Buscar fase, secao, capitulo ou personagem",
    progress: "Buscar usuario, frase ou status",
    system: "Buscar app",
  }[tab];
}

function getResultCount(
  tab: AdminTab,
  userCount: number,
  goalCount: number,
  content: AdminContent | null,
  learning: AdminLearningDetail | null,
  adventure: AdminAdventure | null,
  progress: AdminProgressDetail | null,
) {
  if (tab === "users") return `${userCount} usuarios`;
  if (tab === "goals") return `${goalCount} areas`;
  if (tab === "content") return `${content?.scenarios.length ?? 0} cenarios`;
  if (tab === "learning") return `${learning?.lessons.length ?? 0} aulas`;
  if (tab === "adventure") return `${adventure?.phases.length ?? 0} fases`;
  if (tab === "progress") return `${progress?.progress_entries.length ?? 0} registros`;
  return "";
}

function formatWeekdays(days: number[]) {
  if (!days.length) return "Avulso";
  if (days.length === 7) return "Todo dia";
  const labels = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"];
  return days.map((day) => labels[day]).filter(Boolean).join(", ");
}

function formatDate(value: string) {
  if (!value) return "-";
  return new Intl.DateTimeFormat("pt-BR", { day: "2-digit", month: "2-digit", year: "2-digit" }).format(new Date(value));
}
