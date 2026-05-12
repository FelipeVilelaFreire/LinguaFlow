// Renders any emoji as a Twemoji SVG via jsDelivr CDN.
// This guarantees identical rendering on Windows 10, old Android, and all modern platforms.

function toCdnUrl(emoji: string): string {
  const codepoints = [...emoji]
    .map(ch => ch.codePointAt(0)!)
    .filter(cp => cp !== 0xFE0F)   // strip variation selectors
    .map(cp => cp.toString(16));
  return `https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/${codepoints.join("-")}.svg`;
}

export default function Emoji({
  char,
  size = 20,
  className,
  style,
}: {
  char: string;
  size?: number;
  className?: string;
  style?: React.CSSProperties;
}) {
  if (!char) return null;
  return (
    <img
      src={toCdnUrl(char)}
      alt={char}
      width={size}
      height={size}
      draggable={false}
      className={className}
      style={{ display: "inline-block", ...style }}
    />
  );
}
