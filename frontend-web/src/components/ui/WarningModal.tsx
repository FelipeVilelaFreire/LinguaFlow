import BottomModal from "./BottomModal";

interface WarningModalProps {
  title: string;
  detail: string;
  cancelLabel: string;
  confirmLabel: string;
  loading?: boolean;
  onCancel: () => void;
  onConfirm: () => void;
}

export default function WarningModal({
  title,
  detail,
  cancelLabel,
  confirmLabel,
  loading = false,
  onCancel,
  onConfirm,
}: WarningModalProps) {
  return (
    <BottomModal title={title} onClose={onCancel}>
      <p className="text-sm font-medium text-slate-500">{detail}</p>

      <div className="mt-6 flex gap-3">
        <button
          type="button"
          onClick={onCancel}
          disabled={loading}
          className="flex-1 rounded-xl border border-slate-200 py-3 text-sm font-semibold text-slate-700 transition hover:bg-slate-50 disabled:opacity-60"
        >
          {cancelLabel}
        </button>
        <button
          type="button"
          onClick={onConfirm}
          disabled={loading}
          className="flex-1 rounded-xl bg-red-600 py-3 text-sm font-semibold text-white transition hover:bg-red-700 disabled:opacity-60"
        >
          {loading ? "..." : confirmLabel}
        </button>
      </div>
    </BottomModal>
  );
}
