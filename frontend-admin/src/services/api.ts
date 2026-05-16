import type { AdminAdventure, AdminContent, AdminGoal, AdminLearningDetail, AdminProgressDetail, AdminSummary, AdminUser } from "../types/admin";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:8001/api";
const TOKEN_KEY = "linguaflow_admin_access";
const REFRESH_KEY = "linguaflow_admin_refresh";

interface AuthResponse {
  access: string;
  refresh: string;
  user: {
    id: number;
    username: string;
    email: string;
    first_name: string;
  };
}

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const token = window.localStorage.getItem(TOKEN_KEY);
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
  });

  if (!response.ok) {
    const message = response.status === 403 ? "Usuario sem permissao de admin." : "Nao foi possivel carregar os dados.";
    throw new Error(message);
  }

  if (response.status === 204) return undefined as T;
  return response.json() as Promise<T>;
}

export const adminApi = {
  isAuthenticated() {
    return Boolean(window.localStorage.getItem(TOKEN_KEY));
  },
  async login(username: string, password: string) {
    const payload = await request<AuthResponse>("/auth/login/", {
      method: "POST",
      body: JSON.stringify({ username, password }),
    });
    window.localStorage.setItem(TOKEN_KEY, payload.access);
    window.localStorage.setItem(REFRESH_KEY, payload.refresh);
    return payload.user;
  },
  logout() {
    window.localStorage.removeItem(TOKEN_KEY);
    window.localStorage.removeItem(REFRESH_KEY);
  },
  summary: () => request<AdminSummary>("/admin-dashboard/summary/"),
  users: () => request<AdminUser[]>("/admin-dashboard/users/"),
  goals: () => request<AdminGoal[]>("/admin-dashboard/goals/"),
  content: () => request<AdminContent>("/admin-dashboard/content/"),
  learningDetail: () => request<AdminLearningDetail>("/admin-dashboard/learning-detail/"),
  adventure: () => request<AdminAdventure>("/admin-dashboard/adventure/"),
  progressDetail: () => request<AdminProgressDetail>("/admin-dashboard/progress/"),
};
