import { ROUTES, STRINGS } from "@linguaflow/shared-core";
import Link from "next/link";
import styles from "./HomeScreen.module.css";

export function HomeScreen() {
  return (
    <main className={styles.page}>
      <section className={styles.hero}>
        <p className={styles.eyebrow}>{STRINGS.home.title}</p>
        <h1 className={styles.title}>{STRINGS.home.headline}</h1>
        <div className={styles.actions}>
          <Link className={styles.primaryAction} href={ROUTES.adventureMap}>
            {STRINGS.home.adventureCta}
          </Link>
          <Link className={styles.secondaryAction} href={ROUTES.study}>
            {STRINGS.home.studyCta}
          </Link>
        </div>
      </section>
    </main>
  );
}
