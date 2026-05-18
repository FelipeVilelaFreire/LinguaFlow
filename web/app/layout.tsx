import type { Metadata } from "next";
import "../src/styles/globals.css";
import { AppBoot } from "@/src/components/layout";

export const metadata: Metadata = {
  title: "Talkly",
  description: "Aprenda idiomas vivendo a historia",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>
        <AppBoot>{children}</AppBoot>
      </body>
    </html>
  );
}

