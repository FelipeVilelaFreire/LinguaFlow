export interface StorageAdapter {
  getItem(key: string): Promise<string | null>;
  setItem(key: string, value: string): Promise<void>;
  removeItem(key: string): Promise<void>;
  multiRemove(keys: string[]): Promise<void>;
}

let adapter: StorageAdapter | null = null;

export function setStorageAdapter(nextAdapter: StorageAdapter) {
  adapter = nextAdapter;
}

export function storage() {
  if (!adapter) {
    throw new Error("Shared-core storage adapter not set. Call setStorageAdapter() at app boot.");
  }
  return adapter;
}
