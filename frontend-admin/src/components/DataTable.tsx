import type { ReactNode } from "react";

export default function DataTable({
  columns,
  children,
  title,
  description,
  empty = false,
}: {
  columns: string[];
  children: ReactNode;
  title?: string;
  description?: string;
  empty?: boolean;
}) {
  return (
    <div className="overflow-hidden rounded-[8px] border border-line bg-white shadow-sm">
      {(title || description) && (
        <div className="border-b border-line px-4 py-4">
          {title ? <h3 className="text-lg font-bold">{title}</h3> : null}
          {description ? <p className="mt-1 text-sm font-medium text-slate-500">{description}</p> : null}
        </div>
      )}
      <div className="overflow-x-auto">
        <table className="w-full min-w-[760px] border-collapse text-left text-sm">
          <thead className="bg-slate-50 text-xs font-semibold uppercase text-slate-500">
            <tr>
              {columns.map((column) => (
                <th key={column} className="px-4 py-3">{column}</th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-line">
            {empty ? (
              <tr>
                <td className="px-4 py-8 text-center font-semibold text-slate-500" colSpan={columns.length}>
                  Nenhum registro encontrado.
                </td>
              </tr>
            ) : children}
          </tbody>
        </table>
      </div>
    </div>
  );
}
