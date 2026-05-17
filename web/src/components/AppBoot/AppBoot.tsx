"use client";

import { useEffect } from "react";
import { useState } from "react";
import { setApiClient, setLocale, setStorageAdapter } from "@linguaflow/shared-core";
import { apiClient } from "@/src/lib/apiClient";
import { webStorageAdapter } from "@/src/lib/storageAdapter";

export function AppBoot({ children }: { children: React.ReactNode }) {
  const [ready, setReady] = useState(false);

  useEffect(() => {
    setApiClient(apiClient);
    setStorageAdapter(webStorageAdapter);
    setLocale("pt-BR");
    setReady(true);
  }, []);

  if (!ready) return null;
  return <>{children}</>;
}
