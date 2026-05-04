const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8000/api";
const ACCESS_TOKEN_KEY = "linguaflow_access_token";
const REFRESH_TOKEN_KEY = "linguaflow_refresh_token";

export function getAuthToken() {
  return localStorage.getItem(ACCESS_TOKEN_KEY);
}

function getRefreshToken() {
  return localStorage.getItem(REFRESH_TOKEN_KEY);
}

export function setAuthTokens(access: string | null, refresh?: string | null) {
  if (access) localStorage.setItem(ACCESS_TOKEN_KEY, access);
  else localStorage.removeItem(ACCESS_TOKEN_KEY);

  if (refresh) localStorage.setItem(REFRESH_TOKEN_KEY, refresh);
  else if (refresh === null) localStorage.removeItem(REFRESH_TOKEN_KEY);
}

export function clearAuthTokens() {
  localStorage.removeItem(ACCESS_TOKEN_KEY);
  localStorage.removeItem(REFRESH_TOKEN_KEY);
}

export async function apiRequest<T>(path: string, options?: RequestInit): Promise<T> {
  return requestWithAuth<T>(path, options, true);
}

async function requestWithAuth<T>(path: string, options: RequestInit | undefined, allowRefresh: boolean): Promise<T> {
  const token = getAuthToken();
  const response = await fetch(`${API_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options?.headers,
    },
    ...options,
  });

  if (response.status === 401 && allowRefresh) {
    const refreshed = await refreshAccessToken();
    if (refreshed) {
      return requestWithAuth<T>(path, options, false);
    }
  }

  if (!response.ok) {
    throw new Error(`API error ${response.status}`);
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return response.json() as Promise<T>;
}

async function refreshAccessToken() {
  const refresh = getRefreshToken();
  if (!refresh) return false;

  const response = await fetch(`${API_URL}/auth/refresh/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh }),
  });

  if (!response.ok) {
    clearAuthTokens();
    return false;
  }

  const data = (await response.json()) as { access: string };
  setAuthTokens(data.access);
  return true;
}
