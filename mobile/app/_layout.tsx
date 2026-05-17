import { Stack, router, usePathname } from "expo-router";
import { useEffect } from "react";
import { ACCESS_TOKEN_KEY, setApiClient, setLocale, setStorageAdapter } from "@linguaflow/shared-core";
import { apiClient } from "@/src/lib/apiClient";
import { asyncStorageAdapter } from "@/src/lib/storageAdapter";

setApiClient(apiClient);
setStorageAdapter(asyncStorageAdapter);
setLocale("pt-BR");

export default function RootLayout() {
  const pathname = usePathname();

  useEffect(() => {
    setApiClient(apiClient);
    setStorageAdapter(asyncStorageAdapter);
    setLocale("pt-BR");
  }, []);

  useEffect(() => {
    let cancelled = false;
    asyncStorageAdapter.getItem(ACCESS_TOKEN_KEY).then((token) => {
      if (cancelled) return;
      const isPublic = pathname === "/login" || pathname === "/onboarding";
      if (!token && !isPublic) router.replace("/login");
      if (token && pathname === "/login") router.replace("/(tabs)/home");
    });
    return () => {
      cancelled = true;
    };
  }, [pathname]);

  return <Stack screenOptions={{ headerShown: false }} />;
}
