import type { ReactNode } from "react";

export default function StatCard({ icon, label, value, detail }: { icon: ReactNode; label: string; value: number; detail?: string }) {
  return (
    <article className="rounded-[8px] border border-line bg-white p-5 shadow-sm">
      <div className="flex items-start justify-between gap-3">
        <div>
          <p className="text-sm font-semibold text-slate-500">{label}</p>
          <p className="mt-2 text-3xl font-bold tracking-tight">{value.toLocaleString("pt-BR")}</p>
        </div>
        <div className="grid h-10 w-10 place-items-center rounded-[8px] bg-teal-50 text-brand">{icon}</div>
      </div>
      {detail ? <p className="mt-4 rounded-[8px] bg-slate-50 px-3 py-2 text-xs font-semibold text-slate-500">{detail}</p> : null}
    </article>
  );
}
