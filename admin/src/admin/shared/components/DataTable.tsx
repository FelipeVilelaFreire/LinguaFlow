import type { AdminColumn } from "../types";

export function DataTable<T>({
  columns,
  emptyLabel,
  records,
}: {
  columns: AdminColumn<T>[];
  emptyLabel: string;
  records: T[];
}) {
  if (records.length === 0) {
    return <div className="admin-empty">{emptyLabel}</div>;
  }

  return (
    <div className="admin-table-wrap">
      <table className="admin-table">
        <thead>
          <tr>
            {columns.map((column) => (
              <th key={column.key}>{column.label}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {records.map((record, index) => (
            <tr key={index}>
              {columns.map((column) => (
                <td key={column.key}>{column.value(record)}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
