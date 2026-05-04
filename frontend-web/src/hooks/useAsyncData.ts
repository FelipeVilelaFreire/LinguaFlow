import { useEffect, useState } from "react";

export interface AsyncData<T> {
  data: T | null;
  error: string | null;
  loading: boolean;
  reload: () => void;
}

export function useAsyncData<T>(loader: () => Promise<T>, deps: unknown[] = []): AsyncData<T> {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [version, setVersion] = useState(0);

  useEffect(() => {
    let active = true;
    setLoading(true);
    setError(null);

    loader()
      .then((value) => {
        if (active) setData(value);
      })
      .catch((err: Error) => {
        if (active) setError(err.message);
      })
      .finally(() => {
        if (active) setLoading(false);
      });

    return () => {
      active = false;
    };
  }, [version, ...deps]);

  return { data, error, loading, reload: () => setVersion((current) => current + 1) };
}
