"use client";

import type { ApiClient, ApiRequestOptions } from "@linguaflow/shared-core";

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8001/api";
const ACCESS_TOKEN_KEY = "fluenci_access_token";
const REFRESH_TOKEN_KEY = "fluenci_refresh_token";

function getAccessToken() {
  if (typeof window === "undefined") return null;
  return window.localStorage.getItem(ACCESS_TOKEN_KEY);
}

function getRefreshToken() {
  if (typeof window === "undefined") return null;
  return window.localStorage.getItem(REFRESH_TOKEN_KEY);
}

function setAccessToken(access: string) {
  window.localStorage.setItem(ACCESS_TOKEN_KEY, access);
}

function clearTokens() {
  window.localStorage.removeItem(ACCESS_TOKEN_KEY);
  window.localStorage.removeItem(REFRESH_TOKEN_KEY);
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
    clearTokens();
    return false;
  }

  const data = (await response.json()) as { access: string };
  setAccessToken(data.access);
  return true;
}

async function requestWithAuth<T>(path: string, options: ApiRequestOptions | undefined, allowRefresh: boolean): Promise<T> {
  const token = getAccessToken();
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
