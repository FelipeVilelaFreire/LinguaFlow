"use client";

import { useEffect } from "react";
import { useState } from "react";
import { ACCESS_TOKEN_KEY, ROUTES, setApiClient, setLocale, setStorageAdapter } from "@linguaflow/shared-core";
import { usePathname, useRouter } from "next/navigation";
import { apiClient } from "@/src/lib/apiClient";
import { webStorageAdapter } from "@/src/lib/storageAdapter";
import { AppShell } from "@/src/components/layout";

export function AppBoot({ children }: { children: React.ReactNode }) {
  const [ready, setReady] = useState(false);
  const pathname = usePathname();
  const router = useRouter();

  useEffect(() => {
    setApiClient(apiClient);
    setStorageAdapter(webStorageAdapter);
    setLocale("pt-BR");
    setReady(true);
  }, []);

  useEffect(() => {
    if (!ready || typeof window === "undefined") return;
    const publicPaths = new Set<string>([ROUTES.login, ROUTES.onboarding]);
    const token = window.localStorage.getItem(ACCESS_TOKEN_KEY);
    if (!token && !publicPaths.has(pathname)) {
      router.replace(ROUTES.login);
    }
    if (token && pathname === ROUTES.login) {
      router.replace(ROUTES.home);
    }
  }, [pathname, ready, router]);

  if (!ready) return null;
  return <AppShell>{children}</AppShell>;
}

