import type { Metadata } from "next";
import "../src/theme/globals.css";

export const metadata: Metadata = {
  title: "Talkly",
  description: "Aprenda idiomas vivendo a historia",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
