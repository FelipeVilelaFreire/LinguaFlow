interface ProgressBarProps {
  value: number;
}

export default function ProgressBar({ value }: ProgressBarProps) {
  return (
    <div className="h-3 w-full overflow-hidden rounded-full bg-slate-100">
      <div className="h-full rounded-full transition-all duration-500" style={{ width: `${Math.min(100, Math.max(0, value))}%`, background: "var(--area-primary)" }} />
    </div>
  );
}
