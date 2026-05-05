import { AlertTriangle, X } from "lucide-react";
import type { MouseEvent } from "react";

interface WarningModalProps {
  cancelLabel: string;
  confirmLabel: string;
  detail: string;
  loading?: boolean;
  title: string;
  onCancel: () => void;
  onConfirm: () => void;
}

export default function WarningModal({ cancelLabel, confirmLabel, detail, loading = false, title, onCancel, onConfirm }: WarningModalProps) {
  function handleCancel(event: MouseEvent<HTMLButtonElement>) {
    event.preventDefault();
    event.stopPropagation();
    onCancel();
  }

  function handleConfirm(event: MouseEvent<HTMLButtonElement>) {
    event.preventDefault();
    event.stopPropagation();
    onConfirm();
  }

  return (
    <div className="fixed inset-0 z-50 grid place-items-center bg-slate-950/40 px-4 backdrop-blur-sm" onClick={(event) => event.stopPropagation()}>
      <section className="w-full max-w-md rounded-[8px] bg-white p-5 shadow-xl ring-1 ring-slate-200" onClick={(event) => event.stopPropagation()}>
        <div className="flex items-start justify-between gap-4">
          <div className="grid h-12 w-12 shrink-0 place-items-center rounded-[8px] bg-red-50 text-red-700 ring-1 ring-red-100">
            <AlertTriangle size={22} />
          </div>
          <button type="button" onClick={handleCancel} className="grid h-9 w-9 place-items-center rounded-[8px] text-slate-500 transition hover:bg-slate-100">
            <X size={18} />
          </button>
        </div>
        <h2 className="mt-4 text-2xl font-semibold text-slate-950">{title}</h2>
        <p className="mt-2 font-medium leading-6 text-slate-600">{detail}</p>
        <div className="mt-6 grid gap-3 sm:grid-cols-2">
          <button type="button" onClick={handleCancel} disabled={loading} className="h-11 rounded-[8px] bg-white px-4 font-semibold text-slate-700 ring-1 ring-slate-200 transition hover:bg-slate-50 disabled:opacity-60">
            {cancelLabel}
          </button>
          <button type="button" onClick={handleConfirm} disabled={loading} className="h-11 rounded-[8px] bg-red-600 px-4 font-semibold text-white transition hover:bg-red-700 disabled:opacity-60">
            {loading ? "..." : confirmLabel}
          </button>
        </div>
      </section>
    </div>
  );
}
