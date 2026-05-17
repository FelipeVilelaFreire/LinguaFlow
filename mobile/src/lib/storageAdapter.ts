import AsyncStorage from "@react-native-async-storage/async-storage";
import type { StorageAdapter } from "@linguaflow/shared-core";

export const asyncStorageAdapter: StorageAdapter = {
  getItem: AsyncStorage.getItem,
  setItem: AsyncStorage.setItem,
  removeItem: AsyncStorage.removeItem,
  multiRemove: AsyncStorage.multiRemove,
};
