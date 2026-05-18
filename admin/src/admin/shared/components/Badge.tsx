import type { ReactNode } from "react";

export function Badge({ children, tone = "neutral" }: { children: ReactNode; tone?: "neutral" | "good" | "warn" }) {
  return <span className={`admin-badge admin-badge-${tone}`}>{children}</span>;
}
