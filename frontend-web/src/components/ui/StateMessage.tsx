import { useStrings } from "../../contexts/StringsContext";

interface StateMessageProps {
  title?: string;
  detail?: string;
}

export default function StateMessage({ title, detail }: StateMessageProps) {
  const strings = useStrings();
  const displayTitle = title ?? strings.states.loading;

  return (
    <div className="rounded-[8px] border border-dashed border-slate-300 bg-white p-6 text-center">
      <p className="font-semibold">{displayTitle}</p>
      {detail ? <p className="mt-2 text-sm font-medium text-slate-500">{detail}</p> : null}
    </div>
  );
}
