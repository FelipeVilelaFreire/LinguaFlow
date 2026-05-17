import { ROUTES, STRINGS } from "@linguaflow/shared-core";
import Link from "next/link";
import styles from "./AdventureScreen.module.css";

export function AdventureScreen() {
  return (
    <main className={styles.page}>
      <section className={styles.panel}>
        <p className={styles.eyebrow}>{STRINGS.adventure.title}</p>
        <h1 className={styles.title}>{STRINGS.adventure.mapTitle}</h1>
        <Link className={styles.action} href={ROUTES.adventureMap}>
          {STRINGS.actions.start}
        </Link>
      </section>
    </main>
  );
}
