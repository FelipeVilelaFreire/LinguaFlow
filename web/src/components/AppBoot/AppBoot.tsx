"use client";

import { useEffect } from "react";
import { setApiClient, setLocale, setStorageAdapter } from "@linguaflow/shared-core";
import { apiClient } from "@/src/lib/apiClient";
import { webStorageAdapter } from "@/src/lib/storageAdapter";

export function AppBoot({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    setApiClient(apiClient);
    setStorageAdapter(webStorageAdapter);
    setLocale("pt-BR");
  }, []);

  return <>{children}</>;
}
