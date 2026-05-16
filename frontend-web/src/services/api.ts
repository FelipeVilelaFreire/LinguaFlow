const API_URL = import.meta.env.VITE_API_URL ?? "http://localhost:8001/api";
const ACCESS_TOKEN_KEY = "fluenci_access_token";
const REFRESH_TOKEN_KEY = "fluenci_refresh_token";

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
    throw new Error(await getApiErrorMessage(response));
  }

  if (response.status === 204) {
    return undefined as T;
  }

  return response.json() as Promise<T>;
}

async function getApiErrorMessage(response: Response) {
  try {
    const data = await response.json();
    if (typeof data.detail === "string") return data.detail;
    if (Array.isArray(data.non_field_errors) && data.non_field_errors.length) return String(data.non_field_errors[0]);
    const firstError = Object.entries(data).find(([, value]) => Array.isArray(value) && value.length);
    if (firstError) return `${firstError[0]}: ${String((firstError[1] as unknown[])[0])}`;
  } catch {
    // Keep the status fallback below when the response is not JSON.
  }
  return `API error ${response.status}`;
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
