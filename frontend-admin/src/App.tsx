import { BookOpen, Database, GraduationCap, LayoutDashboard, LogOut, RefreshCw, Shield, Users } from "lucide-react";
import type { FormEvent, ReactNode } from "react";
import { useEffect, useMemo, useState } from "react";

import DataTable from "./components/DataTable";
import StatCard from "./components/StatCard";
import { adminApi } from "./services/api";
import type { AdminContent, AdminGoal, AdminSummary, AdminUser } from "./types/admin";

type AdminTab = "dashboard" | "users" | "goals" | "content";

export default function App() {
  const [authenticated, setAuthenticated] = useState(adminApi.isAuthenticated());
  const [tab, setTab] = useState<AdminTab>("dashboard");
  const [summary, setSummary] = useState<AdminSummary | null>(null);
  const [users, setUsers] = useState<AdminUser[]>([]);
  const [goals, setGoals] = useState<AdminGoal[]>([]);
  const [content, setContent] = useState<AdminContent | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (authenticated) void loadAll();
  }, [authenticated]);

  async function loadAll() {
    setLoading(true);
    setError(null);
    try {
      const [nextSummary, nextUsers, nextGoals, nextContent] = await Promise.all([
        adminApi.summary(),
        adminApi.users(),
        adminApi.goals(),
        adminApi.content(),
      ]);
      setSummary(nextSummary);
      setUsers(nextUsers);
      setGoals(nextGoals);
      setContent(nextContent);
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

  if (!authenticated) return <LoginScreen onAuthenticated={() => setAuthenticated(true)} />;

  return (
    <div className="min-h-screen bg-paper text-slate-950">
      <aside className="fixed inset-y-0 left-0 hidden w-72 border-r border-line bg-white px-4 py-5 md:block">
        <div className="flex items-center gap-3">
          <div className="grid h-11 w-11 place-items-center rounded-[8px] bg-brand text-white">
            <Shield size={21} />
          </div>
          <div>
            <h1 className="text-xl font-semibold">LinguaFlow Admin</h1>
            <p className="text-xs font-bold uppercase text-slate-500">Backoffice</p>
          </div>
        </div>

        <nav className="mt-8 space-y-2">
          <NavButton active={tab === "dashboard"} icon={<LayoutDashboard size={18} />} label="Dashboard" onClick={() => setTab("dashboard")} />
          <NavButton active={tab === "users"} icon={<Users size={18} />} label="Usuarios" onClick={() => setTab("users")} />
          <NavButton active={tab === "goals"} icon={<GraduationCap size={18} />} label="Areas" onClick={() => setTab("goals")} />
          <NavButton active={tab === "content"} icon={<BookOpen size={18} />} label="Conteudo" onClick={() => setTab("content")} />
        </nav>

        <div className="absolute inset-x-4 bottom-5 space-y-2">
          <button type="button" onClick={loadAll} className="flex h-11 w-full items-center justify-center gap-2 rounded-[8px] bg-slate-50 font-semibold text-slate-700 ring-1 ring-line transition hover:bg-slate-100">
            <RefreshCw size={16} />
            Atualizar
          </button>
          <button type="button" onClick={logout} className="flex h-11 w-full items-center justify-center gap-2 rounded-[8px] bg-slate-950 font-semibold text-white transition hover:bg-slate-800">
            <LogOut size={16} />
            Sair
          </button>
        </div>
      </aside>

      <main className="min-h-screen px-4 py-5 md:ml-72 md:px-8">
        <div className="mx-auto max-w-7xl">
          <header className="flex flex-col gap-3 rounded-[8px] bg-white p-5 shadow-soft ring-1 ring-line md:flex-row md:items-center md:justify-between">
            <div>
              <p className="text-sm font-semibold uppercase text-brand">Painel administrativo</p>
              <h2 className="mt-1 text-3xl font-semibold">{getTabTitle(tab)}</h2>
            </div>
            <div className="flex gap-2 md:hidden">
              {(["dashboard", "users", "goals", "content"] as AdminTab[]).map((item) => (
                <button key={item} type="button" onClick={() => setTab(item)} className={`h-10 rounded-[8px] px-3 text-sm font-semibold ring-1 ${tab === item ? "bg-brand text-white ring-brand" : "bg-white text-slate-600 ring-line"}`}>
                  {getTabTitle(item)}
                </button>
              ))}
            </div>
          </header>

          {error ? <div className="mt-4 rounded-[8px] bg-red-50 p-4 font-semibold text-red-700 ring-1 ring-red-100">{error}</div> : null}
          {loading ? <div className="mt-4 rounded-[8px] bg-white p-4 font-semibold text-slate-500 ring-1 ring-line">Carregando dados...</div> : null}

          <section className="mt-5">
            {tab === "dashboard" ? <Dashboard summary={summary} /> : null}
            {tab === "users" ? <UsersTable users={users} /> : null}
            {tab === "goals" ? <GoalsTable goals={goals} /> : null}
            {tab === "content" ? <ContentPanel content={content} /> : null}
          </section>
        </div>
      </main>
    </div>
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
      <form onSubmit={submit} className="w-full max-w-md rounded-[8px] bg-white p-6 shadow-soft ring-1 ring-line">
        <div className="grid h-12 w-12 place-items-center rounded-[8px] bg-brand text-white">
          <Shield />
        </div>
        <h1 className="mt-4 text-3xl font-semibold">LinguaFlow Admin</h1>
        <p className="mt-2 font-medium text-slate-500">Entre com um usuario staff ou superuser.</p>

        <label className="mt-6 block">
          <span className="text-sm font-semibold text-slate-600">Usuario</span>
          <input value={username} onChange={(event) => setUsername(event.target.value)} className="mt-2 h-12 w-full rounded-[8px] border border-line px-4 outline-none transition focus:border-brand" />
        </label>
        <label className="mt-4 block">
          <span className="text-sm font-semibold text-slate-600">Senha</span>
          <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} className="mt-2 h-12 w-full rounded-[8px] border border-line px-4 outline-none transition focus:border-brand" />
        </label>
        {error ? <p className="mt-4 rounded-[8px] bg-red-50 p-3 text-sm font-semibold text-red-700">{error}</p> : null}
        <button disabled={loading} className="mt-6 h-12 w-full rounded-[8px] bg-brand font-semibold text-white transition hover:brightness-95 disabled:opacity-60">
          {loading ? "Entrando..." : "Entrar"}
        </button>
      </form>
    </main>
  );
}

function Dashboard({ summary }: { summary: AdminSummary | null }) {
  if (!summary) return <EmptyState />;
  return (
    <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
      <StatCard icon={<Users size={20} />} label="Usuarios" value={summary.users} />
      <StatCard icon={<GraduationCap size={20} />} label="Areas ativas" value={summary.active_goals} />
      <StatCard icon={<BookOpen size={20} />} label="Frases" value={summary.phrases} />
      <StatCard icon={<Database size={20} />} label="Conclusoes" value={summary.completions} />
      <StatCard icon={<Shield size={20} />} label="Staff" value={summary.staff_users} />
      <StatCard icon={<GraduationCap size={20} />} label="Areas totais" value={summary.goals} />
      <StatCard icon={<BookOpen size={20} />} label="Aulas" value={summary.lessons} />
      <StatCard icon={<Database size={20} />} label="Favoritos" value={summary.favorites} />
    </div>
  );
}

function UsersTable({ users }: { users: AdminUser[] }) {
  return (
    <DataTable columns={["ID", "Usuario", "Email", "Staff", "Ativo", "Areas", "Conclusoes"]}>
      {users.map((user) => (
        <tr key={user.id}>
          <td className="px-4 py-3 font-semibold">{user.id}</td>
          <td className="px-4 py-3">{user.username}</td>
          <td className="px-4 py-3 text-slate-500">{user.email || "-"}</td>
          <td className="px-4 py-3">{user.is_staff ? "Sim" : "Nao"}</td>
          <td className="px-4 py-3">{user.is_active ? "Sim" : "Nao"}</td>
          <td className="px-4 py-3">{user.goal_count}</td>
          <td className="px-4 py-3">{user.completion_count}</td>
        </tr>
      ))}
    </DataTable>
  );
}

function GoalsTable({ goals }: { goals: AdminGoal[] }) {
  return (
    <DataTable columns={["ID", "Usuario", "Curso", "Atual", "Meta", "Rotina", "Progresso", "Streak"]}>
      {goals.map((goal) => (
        <tr key={goal.id}>
          <td className="px-4 py-3 font-semibold">{goal.id}</td>
          <td className="px-4 py-3">{goal.user ?? "-"}</td>
          <td className="px-4 py-3">{goal.source_language} -&gt; {goal.target_language}</td>
          <td className="px-4 py-3">{goal.current_level}</td>
          <td className="px-4 py-3">{goal.target_level}</td>
          <td className="px-4 py-3">{formatWeekdays(goal.study_weekdays)} / {goal.session_minutes} min</td>
          <td className="px-4 py-3">{goal.learned_phrases} / {goal.total_phrases}</td>
          <td className="px-4 py-3">{goal.streak_days}</td>
        </tr>
      ))}
    </DataTable>
  );
}

function ContentPanel({ content }: { content: AdminContent | null }) {
  const phraseCounts = useMemo(() => Object.entries(content?.phrase_counts ?? {}), [content]);
  if (!content) return <EmptyState />;

  return (
    <div className="grid gap-5 xl:grid-cols-[1fr_0.85fr]">
      <DataTable columns={["Cenario", "Slug", "Frases", "Aulas"]}>
        {content.scenarios.map((scenario) => (
          <tr key={scenario.id}>
            <td className="px-4 py-3 font-semibold">{scenario.title}</td>
            <td className="px-4 py-3 text-slate-500">{scenario.slug}</td>
            <td className="px-4 py-3">{scenario.phrase_count}</td>
            <td className="px-4 py-3">{scenario.lesson_count}</td>
          </tr>
        ))}
      </DataTable>
      <div className="space-y-4">
        <div className="rounded-[8px] bg-white p-5 shadow-soft ring-1 ring-line">
          <p className="text-sm font-semibold uppercase text-slate-500">Idiomas</p>
          <div className="mt-3 flex flex-wrap gap-2">
            {content.languages.map((language) => (
              <span key={language.id} className="rounded-[8px] bg-slate-50 px-3 py-2 text-sm font-semibold ring-1 ring-line">{language.code} - {language.name}</span>
            ))}
          </div>
        </div>
        <div className="rounded-[8px] bg-white p-5 shadow-soft ring-1 ring-line">
          <p className="text-sm font-semibold uppercase text-slate-500">Frases por curso</p>
          <div className="mt-3 grid gap-2">
            {phraseCounts.map(([label, count]) => (
              <div key={label} className="flex items-center justify-between rounded-[8px] bg-slate-50 px-3 py-2 ring-1 ring-line">
                <span className="font-semibold">{label}</span>
                <span className="text-slate-500">{count}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function NavButton({ active, icon, label, onClick }: { active: boolean; icon: ReactNode; label: string; onClick: () => void }) {
  return (
    <button type="button" onClick={onClick} className={`flex h-12 w-full items-center gap-3 rounded-[8px] px-3 text-left text-sm font-semibold transition ${active ? "bg-brand text-white" : "text-slate-600 hover:bg-slate-50"}`}>
      {icon}
      {label}
    </button>
  );
}

function EmptyState() {
  return <div className="rounded-[8px] bg-white p-5 font-semibold text-slate-500 ring-1 ring-line">Sem dados carregados.</div>;
}

function getTabTitle(tab: AdminTab) {
  return {
    dashboard: "Dashboard",
    users: "Usuarios",
    goals: "Areas",
    content: "Conteudo",
  }[tab];
}

function formatWeekdays(days: number[]) {
  if (!days.length) return "Avulso";
  if (days.length === 7) return "Todo dia";
  const labels = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"];
  return days.map((day) => labels[day]).filter(Boolean).join(", ");
}
