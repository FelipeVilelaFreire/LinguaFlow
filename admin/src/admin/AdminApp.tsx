import { STRINGS } from "@linguaflow/shared-core";
import type { FormEvent } from "react";
import { useEffect, useMemo, useState } from "react";
import { ADMIN_APPS } from "./apps";
import { DataTable } from "./shared/components/DataTable";
import { MetricCard } from "./shared/components/MetricCard";
import { adminApi } from "./shared/services/api";
import type { AdminAppConfig, AdminAppKey, AdminDataset, AdminGroup } from "./shared/types";

const EMPTY_DATASET: AdminDataset = {
  adventure: null,
  content: null,
  goals: [],
  learning: null,
  progress: null,
  summary: null,
  users: [],
};

const GROUP_ORDER: AdminGroup[] = ["operation", "content", "strategy", "system"];

export function AdminApp() {
  const [authenticated, setAuthenticated] = useState(adminApi.isAuthenticated());
  const [activeKey, setActiveKey] = useState<AdminAppKey>("dashboard");
  const [data, setData] = useState<AdminDataset>(EMPTY_DATASET);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [query, setQuery] = useState("");

  const activeApp = ADMIN_APPS.find((app) => app.key === activeKey) ?? ADMIN_APPS[0];

  useEffect(() => {
    if (authenticated) void loadAll();
  }, [authenticated]);

  async function loadAll() {
    setLoading(true);
    setError(null);
    try {
      const [summary, users, goals, content, learning, adventure, progress] = await Promise.all([
        adminApi.summary(),
        adminApi.users(),
        adminApi.goals(),
        adminApi.content(),
        adminApi.learningDetail(),
        adminApi.adventure(),
        adminApi.progressDetail(),
      ]);
      setData({ adventure, content, goals, learning, progress, summary, users });
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : STRINGS.admin.auth.error);
    } finally {
      setLoading(false);
    }
  }

  function logout() {
    adminApi.logout();
    setAuthenticated(false);
    setData(EMPTY_DATASET);
  }

  if (!authenticated) {
    return <LoginScreen onAuthenticated={() => setAuthenticated(true)} />;
  }

  return (
    <div className="admin-shell">
      <aside className="admin-sidebar">
        <Brand />
        <nav className="admin-nav">
          {GROUP_ORDER.map((group) => (
            <div className="admin-nav-group" key={group}>
              <p>{getGroupLabel(group)}</p>
              {ADMIN_APPS.filter((app) => app.group === group).map((app) => (
                <button
                  className={app.key === activeKey ? "active" : ""}
                  key={app.key}
                  type="button"
                  onClick={() => {
                    setActiveKey(app.key);
                    setQuery("");
                  }}
                >
                  <span>{app.icon}</span>
                  <strong>{app.title}</strong>
                  <small>{app.description}</small>
                </button>
              ))}
            </div>
          ))}
        </nav>
        <div className="admin-api-card">
          <strong>{STRINGS.admin.app.apiStatus}</strong>
          <span>{STRINGS.admin.app.apiStatusDetail}</span>
        </div>
      </aside>

      <main className="admin-main">
        <header className="admin-topbar">
          <div>
            <p>{STRINGS.admin.app.panel}</p>
            <h1>{activeApp.title}</h1>
            <span>{activeApp.description}</span>
          </div>
          <div className="admin-topbar-actions">
            <button type="button" onClick={loadAll}>{loading ? "..." : STRINGS.admin.app.refresh}</button>
            <button type="button" onClick={logout}>{STRINGS.admin.app.logout}</button>
          </div>
        </header>

        <section className="admin-content">
          {error ? <div className="admin-error">{error}</div> : null}
          <AdminAppPage app={activeApp} data={data} query={query} onQueryChange={setQuery} />
        </section>
      </main>
    </div>
  );
}

function AdminAppPage<T>({
  app,
  data,
  onQueryChange,
  query,
}: {
  app: AdminAppConfig<T>;
  data: AdminDataset;
  onQueryChange: (value: string) => void;
  query: string;
}) {
  const records = useMemo(() => {
    const nextRecords = app.getRecords(data);
    const normalized = query.trim().toLowerCase();
    if (!normalized) return nextRecords;
    return nextRecords.filter((record) => JSON.stringify(record).toLowerCase().includes(normalized));
  }, [app, data, query]);
  const metrics = app.getMetrics?.(data) ?? [];

  return (
    <div className="admin-page-grid">
      <div className="admin-page-main">
        {metrics.length ? (
          <section className="admin-metrics">
            {metrics.map((metric) => (
              <MetricCard key={metric.label} {...metric} />
            ))}
          </section>
        ) : null}

        <div className="admin-toolbar">
          <input
            aria-label={STRINGS.admin.app.search}
            placeholder={app.searchPlaceholder}
            value={query}
            onChange={(event) => onQueryChange(event.target.value)}
          />
          <strong>{records.length}</strong>
        </div>

        <DataTable columns={app.columns} emptyLabel={STRINGS.admin.app.empty} records={records} />
      </div>
      {app.renderAside ? <aside className="admin-page-aside">{app.renderAside(data)}</aside> : null}
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
      setError(currentError instanceof Error ? currentError.message : STRINGS.admin.auth.error);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="admin-login">
      <form onSubmit={submit}>
        <Brand />
        <p>{STRINGS.admin.auth.description}</p>
        <label>
          <span>{STRINGS.admin.auth.username}</span>
          <input value={username} onChange={(event) => setUsername(event.target.value)} autoComplete="username" />
        </label>
        <label>
          <span>{STRINGS.admin.auth.password}</span>
          <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} autoComplete="current-password" />
        </label>
        {error ? <div className="admin-error">{error}</div> : null}
        <button disabled={loading} type="submit">{loading ? STRINGS.admin.auth.submitting : STRINGS.admin.auth.submit}</button>
      </form>
    </main>
  );
}

function Brand() {
  return (
    <div className="admin-brand">
      <div>LF</div>
      <span>
        <strong>{STRINGS.admin.app.title}</strong>
        <small>{STRINGS.admin.app.subtitle}</small>
      </span>
    </div>
  );
}

function getGroupLabel(group: AdminGroup) {
  return STRINGS.admin.groups[group];
}
