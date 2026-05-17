export interface ApiRequestOptions {
  method?: string;
  headers?: Record<string, string>;
  body?: string;
}

export interface ApiClient {
  request<T>(path: string, options?: ApiRequestOptions): Promise<T>;
}

let client: ApiClient | null = null;

export function setApiClient(nextClient: ApiClient) {
  client = nextClient;
}

export function api() {
  if (!client) {
    throw new Error("Shared-core API client not set. Call setApiClient() at app boot.");
  }
  return client;
}
