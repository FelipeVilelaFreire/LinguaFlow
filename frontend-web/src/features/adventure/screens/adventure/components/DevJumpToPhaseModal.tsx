import { useState } from "react";

import BottomModal from "../../../../../components/ui/BottomModal";
import { useStrings } from "../../../../../contexts/StringsContext";

interface DevJumpToPhaseModalProps {
  chapterSlug:   string;
  phasesCount:   number;
  onClose:       () => void;
  onConfirm:     (phaseNumber: number, sectionNumber: number) => Promise<void>;
}

const SECTIONS_PER_PHASE = 6;

export default function DevJumpToPhaseModal({
  chapterSlug: _chapterSlug,
  phasesCount,
  onClose,
  onConfirm,
}: DevJumpToPhaseModalProps) {
  const s = useStrings();
  const [selectedPhase,   setSelectedPhase]   = useState<number | null>(null);
  const [selectedSection, setSelectedSection] = useState<number>(1);
  const [submitting,      setSubmitting]      = useState(false);

  const phases   = Array.from({ length: Math.max(1, phasesCount) },   (_, i) => i + 1);
  const sections = Array.from({ length: SECTIONS_PER_PHASE },         (_, i) => i + 1);

  async function handleConfirm() {
    if (selectedPhase === null || submitting) return;
    setSubmitting(true);
    try {
      await onConfirm(selectedPhase, selectedSection);
      onClose();
    } finally {
      setSubmitting(false);
    }
  }

  const ctaLabel = submitting
    ? s.adventure.devJumping
    : selectedPhase === null
      ? s.adventure.devJumpPickPhase
      : s.adventure.devJumpConfirm(selectedPhase, selectedSection);

  return (
    <BottomModal
      title={s.adventure.devJumpTitle}
      onClose={onClose}
      footer={
        <button
          type="button"
          onClick={handleConfirm}
          disabled={selectedPhase === null || submitting}
          className="w-full rounded-xl py-3.5 text-base font-bold transition active:scale-[0.97] disabled:cursor-not-allowed disabled:opacity-40"
          style={{ background: "#0f172a", color: "white" }}
        >
          {ctaLabel}
        </button>
      }
    >
      <p className="mb-5 text-sm leading-relaxed text-slate-500">
        {s.adventure.devJumpHint}
      </p>

      <p className="mb-2 text-xs font-bold uppercase tracking-wider text-slate-500">
        {s.adventure.devJumpPhaseLabel}
      </p>
      <div className="mb-6 grid grid-cols-5 gap-2">
        {phases.map(n => {
          const isSelected = selectedPhase === n;
          return (
            <button
              key={n}
              type="button"
              onClick={() => { setSelectedPhase(n); setSelectedSection(1); }}
              className="flex h-12 items-center justify-center rounded-lg text-sm font-bold transition active:scale-[0.95]"
              style={{
                background: isSelected ? "#0f172a"  : "#f1f5f9",
                color:      isSelected ? "white"    : "#0f172a",
                border:     isSelected ? "1px solid #0f172a" : "1px solid #e2e8f0",
              }}
            >
              {n}
            </button>
          );
        })}
      </div>

      <p className="mb-2 text-xs font-bold uppercase tracking-wider text-slate-500">
        {s.adventure.devJumpSectionLabel}
      </p>
      <div className="grid grid-cols-6 gap-2">
        {sections.map(n => {
          const isSelected = selectedSection === n;
          const disabled   = selectedPhase === null;
          return (
            <button
              key={n}
              type="button"
              onClick={() => !disabled && setSelectedSection(n)}
              disabled={disabled}
              className="flex h-12 items-center justify-center rounded-lg text-sm font-bold transition active:scale-[0.95] disabled:cursor-not-allowed disabled:opacity-40"
              style={{
                background: isSelected ? "#0f172a"  : "#f1f5f9",
                color:      isSelected ? "white"    : "#0f172a",
                border:     isSelected ? "1px solid #0f172a" : "1px solid #e2e8f0",
              }}
            >
              {n}
            </button>
          );
        })}
      </div>
    </BottomModal>
  );
}
