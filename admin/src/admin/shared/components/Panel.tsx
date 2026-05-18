import type { ReactNode } from "react";

export function Panel({
  children,
  eyebrow,
  title,
}: {
  children: ReactNode;
  eyebrow: string;
  title: string;
}) {
  return (
    <section className="admin-panel">
      <p>{eyebrow}</p>
      <h3>{title}</h3>
      <div>{children}</div>
    </section>
  );
}
