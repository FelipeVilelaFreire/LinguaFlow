import { apiRequest, clearAuthTokens, getAuthToken, setAuthTokens } from "./api";

export interface User {
  id: number;
  username: string;
  email: string;
  first_name: string;
}

export interface AuthResponse {
  access: string;
  refresh: string;
  user: User;
}

export const authService = {
  getToken: getAuthToken,
  logout: clearAuthTokens,
  async login(username: string, password: string) {
    const response = await apiRequest<AuthResponse>("/auth/login/", {
      method: "POST",
      body: JSON.stringify({ username, password }),
    });
    setAuthTokens(response.access, response.refresh);
    return response.user;
  },
  async register(username: string, email: string, password: string) {
    const response = await apiRequest<AuthResponse>("/auth/register/", {
      method: "POST",
      body: JSON.stringify({ username, email, password }),
    });
    setAuthTokens(response.access, response.refresh);
    return response.user;
  },
  me: () => apiRequest<User>("/auth/me/"),
};
