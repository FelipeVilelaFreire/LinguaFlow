import { Stack } from "expo-router";
import { useEffect } from "react";
import { setApiClient, setLocale, setStorageAdapter } from "@linguaflow/shared-core";
import { apiClient } from "@/src/lib/apiClient";
import { asyncStorageAdapter } from "@/src/lib/storageAdapter";

export default function RootLayout() {
  useEffect(() => {
    setApiClient(apiClient);
    setStorageAdapter(asyncStorageAdapter);
    setLocale("pt-BR");
  }, []);

  return <Stack screenOptions={{ headerShown: false }} />;
}
