import { api } from "../lib/apiClient";
import { storage } from "../lib/storage";
import type { AuthResponse, User } from "../types/auth";

export const ACCESS_TOKEN_KEY = "fluenci_access_token";
export const REFRESH_TOKEN_KEY = "fluenci_refresh_token";

export const authService = {
  getToken: () => storage().getItem(ACCESS_TOKEN_KEY),

  async setTokens(access: string | null, refresh?: string | null) {
    if (access) await storage().setItem(ACCESS_TOKEN_KEY, access);
    else await storage().removeItem(ACCESS_TOKEN_KEY);

    if (refresh) await storage().setItem(REFRESH_TOKEN_KEY, refresh);
    else if (refresh === null) await storage().removeItem(REFRESH_TOKEN_KEY);
  },

  async logout() {
    await storage().multiRemove([ACCESS_TOKEN_KEY, REFRESH_TOKEN_KEY]);
  },

  async login(username: string, password: string) {
    const response = await api().request<AuthResponse>("/auth/login/", {
      method: "POST",
      body: JSON.stringify({ username, password }),
    });
    await this.setTokens(response.access, response.refresh);
    return response.user;
  },

  async register(username: string, email: string, password: string) {
    const response = await api().request<AuthResponse>("/auth/register/", {
      method: "POST",
      body: JSON.stringify({ username, email, password }),
    });
    await this.setTokens(response.access, response.refresh);
    return response.user;
  },

  me: () => api().request<User>("/auth/me/"),
};
