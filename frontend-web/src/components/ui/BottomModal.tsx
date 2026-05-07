import { X } from "lucide-react";
import type { ReactNode, MouseEvent } from "react";

interface BottomModalProps {
  title: string;
  onClose: () => void;
  children: ReactNode;
  footer?: ReactNode;
}

export default function BottomModal({ title, onClose, children, footer }: BottomModalProps) {
  function stopProp(e: MouseEvent) {
    e.stopPropagation();
  }

  return (
    <div className="bottom-modal-backdrop" onClick={onClose}>
      <div className="bottom-modal-sheet" onClick={stopProp}>
        <div className="bottom-modal-handle" />

        {/* Header */}
        <div className="flex shrink-0 items-center justify-between px-6 pt-4 pb-0">
          <p className="text-lg font-bold text-slate-950">{title}</p>
          <button
            type="button"
            onClick={onClose}
            className="flex h-8 w-8 items-center justify-center rounded-full bg-slate-100 text-slate-500 transition hover:bg-slate-200"
          >
            <X size={16} />
          </button>
        </div>

        {/* Scrollable content */}
        <div className={`flex-1 overflow-y-auto px-6 pt-5 ${footer ? "pb-4" : "pb-8"}`}>
          {children}
        </div>

        {/* Sticky footer */}
        {footer && (
          <div className="shrink-0 border-t border-slate-100 px-6 pb-8 pt-4">
            {footer}
          </div>
        )}
      </div>
    </div>
  );
}
