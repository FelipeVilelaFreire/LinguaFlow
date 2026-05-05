import type { ReactNode } from "react";

export default function StatCard({ icon, label, value }: { icon: ReactNode; label: string; value: number }) {
  return (
    <article className="rounded-[8px] bg-white p-5 shadow-soft ring-1 ring-line">
      <div className="grid h-10 w-10 place-items-center rounded-[8px] bg-teal-50 text-brand">{icon}</div>
      <p className="mt-4 text-3xl font-semibold">{value.toLocaleString("pt-BR")}</p>
      <p className="mt-1 text-sm font-semibold text-slate-500">{label}</p>
    </article>
  );
}
