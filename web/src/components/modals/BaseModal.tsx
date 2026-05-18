"use client";

import type { ReactNode } from "react";
import styles from "./BaseModal.module.css";

export function BaseModal({
  children,
  closeLabel,
  onClose,
  panelClassName,
}: {
  children: ReactNode;
  closeLabel: string;
  onClose: () => void;
  panelClassName?: string;
}) {
  return (
    <div className={styles.backdrop} role="presentation" onClick={onClose}>
      <section
        aria-modal="true"
        className={[styles.panel, panelClassName].filter(Boolean).join(" ")}
        role="dialog"
        onClick={(event) => event.stopPropagation()}
      >
        <button className={styles.closeButton} type="button" onClick={onClose} aria-label={closeLabel}>
          ×
        </button>
        {children}
      </section>
    </div>
  );
}
