import type { ReactNode } from "react";

export default function DataTable({ columns, children }: { columns: string[]; children: ReactNode }) {
  return (
    <div className="overflow-hidden rounded-[8px] bg-white shadow-soft ring-1 ring-line">
      <div className="overflow-x-auto">
        <table className="w-full min-w-[760px] border-collapse text-left text-sm">
          <thead className="bg-slate-50 text-xs font-semibold uppercase text-slate-500">
            <tr>
              {columns.map((column) => (
                <th key={column} className="px-4 py-3">{column}</th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-line">{children}</tbody>
        </table>
      </div>
    </div>
  );
}
