"use client";

import { STRINGS } from "@linguaflow/shared-core";
import { useRouter } from "next/navigation";
import type { MouseEvent, ReactNode } from "react";
import { useEffect, useRef, useState } from "react";
import styles from "./AdventureTransitionLink.module.css";

export function AdventureTransitionLink({
  children,
  className,
  href,
}: {
  children: ReactNode;
  className?: string;
  href: string;
}) {
  const router = useRouter();
  const [visible, setVisible] = useState(false);
  const timers = useRef<number[]>([]);

  useEffect(() => {
    return () => {
      timers.current.forEach((timer) => window.clearTimeout(timer));
    };
  }, []);

  function navigate(event: MouseEvent<HTMLAnchorElement>) {
    event.preventDefault();
    setVisible(true);
    timers.current.push(window.setTimeout(() => router.push(href), 550));
    timers.current.push(window.setTimeout(() => setVisible(false), 980));
  }

  return (
    <>
      <a className={className} href={href} onClick={navigate}>
        {children}
      </a>
      {visible ? (
        <div className={styles.overlay} aria-live="polite">
          <div className={styles.content}>
            <div className={styles.mark} />
            <p>{STRINGS.adventure.title}</p>
            <span>{STRINGS.adventure.loading}</span>
          </div>
        </div>
      ) : null}
    </>
  );
}
