import type {
  AdminAdventure,
  AdminContent,
  AdminGoal,
  AdminLearningDetail,
  AdminProgressDetail,
  AdminSummary,
  AdminUser,
} from "../../../types/admin";
import { STRINGS } from "@linguaflow/shared-core";
import { API_ENDPOINTS } from "../../ini/config/endpoints";

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
    const message = response.status === 403 ? STRINGS.admin.auth.forbidden : STRINGS.admin.auth.loadError;
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
    const payload = await request<AuthResponse>(API_ENDPOINTS.auth.login, {
      body: JSON.stringify({ username, password }),
      method: "POST",
    });
    window.localStorage.setItem(TOKEN_KEY, payload.access);
    window.localStorage.setItem(REFRESH_KEY, payload.refresh);
    return payload.user;
  },
  logout() {
    window.localStorage.removeItem(TOKEN_KEY);
    window.localStorage.removeItem(REFRESH_KEY);
  },
  adventure: () => request<AdminAdventure>(API_ENDPOINTS.adminDashboard.adventure),
  content: () => request<AdminContent>(API_ENDPOINTS.adminDashboard.content),
  goals: () => request<AdminGoal[]>(API_ENDPOINTS.adminDashboard.goals),
  learningDetail: () => request<AdminLearningDetail>(API_ENDPOINTS.adminDashboard.learningDetail),
  progressDetail: () => request<AdminProgressDetail>(API_ENDPOINTS.adminDashboard.progress),
  summary: () => request<AdminSummary>(API_ENDPOINTS.adminDashboard.summary),
  users: () => request<AdminUser[]>(API_ENDPOINTS.adminDashboard.users),
};
