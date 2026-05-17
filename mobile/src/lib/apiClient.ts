import type { ApiClient, ApiRequestOptions } from "@linguaflow/shared-core";
import { asyncStorageAdapter } from "./storageAdapter";

const API_URL = process.env.EXPO_PUBLIC_API_URL ?? "http://localhost:8001/api";
const ACCESS_TOKEN_KEY = "fluenci_access_token";
const REFRESH_TOKEN_KEY = "fluenci_refresh_token";

async function refreshAccessToken() {
  const refresh = await asyncStorageAdapter.getItem(REFRESH_TOKEN_KEY);
  if (!refresh) return false;

  const response = await fetch(`${API_URL}/auth/refresh/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh }),
  });

  if (!response.ok) {
    await asyncStorageAdapter.multiRemove([ACCESS_TOKEN_KEY, REFRESH_TOKEN_KEY]);
    return false;
  }

  const data = (await response.json()) as { access: string };
  await asyncStorageAdapter.setItem(ACCESS_TOKEN_KEY, data.access);
  return true;
}

async function requestWithAuth<T>(path: string, options: ApiRequestOptions | undefined, allowRefresh: boolean): Promise<T> {
  const token = await asyncStorageAdapter.getItem(ACCESS_TOKEN_KEY);
  const response = await fetch(`${API_URL}${path}`, {
    method: options?.method,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options?.headers,
    },
    body: options?.body,
  });

  if (response.status === 401 && allowRefresh && await refreshAccessToken()) {
    return requestWithAuth<T>(path, options, false);
  }

  if (!response.ok) {
    throw new Error(`API error ${response.status}`);
  }

  if (response.status === 204) return undefined as T;
  return response.json() as Promise<T>;
}

export const apiClient: ApiClient = {
  request(path, options) {
    return requestWithAuth(path, options, true);
  },
};
