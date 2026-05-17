import type { StorageAdapter } from "@linguaflow/shared-core";

export const webStorageAdapter: StorageAdapter = {
  async getItem(key) {
    if (typeof window === "undefined") return null;
    return window.localStorage.getItem(key);
  },
  async setItem(key, value) {
    if (typeof window !== "undefined") window.localStorage.setItem(key, value);
  },
  async removeItem(key) {
    if (typeof window !== "undefined") window.localStorage.removeItem(key);
  },
  async multiRemove(keys) {
    if (typeof window === "undefined") return;
    keys.forEach((key) => window.localStorage.removeItem(key));
  },
};
