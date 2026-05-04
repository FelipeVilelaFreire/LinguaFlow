import { ExternalLink } from "lucide-react";

import { useStrings } from "../../contexts/StringsContext";

interface VideoCardProps {
  duration: string;
  title: string;
  url: string;
}

export default function VideoCard({ duration, title, url }: VideoCardProps) {
  const strings = useStrings();

  return (
    <section className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200">
      <p className="text-sm font-semibold uppercase text-slate-500">{strings.today.video}</p>
      <h3 className="mt-2 text-2xl font-semibold">{title}</h3>
      <p className="mt-1 text-sm font-medium text-slate-600">{duration}</p>
      <a href={url} target="_blank" rel="noreferrer" className="mt-5 inline-flex items-center gap-2 rounded-[8px] bg-slate-950 px-4 py-3 text-sm font-semibold text-white transition hover:bg-slate-800">
        {strings.actions.openVideo}
        <ExternalLink size={16} />
      </a>
    </section>
  );
}
