import { ROUTES, STRINGS } from "@linguaflow/shared-core";
import { BookOpen, Boxes, Gem, Map, Shield, Sparkles } from "lucide-react";
import Link from "next/link";
import { AdventureTransitionLink } from "@/src/components/features/adventure";
import styles from "./AdventureScreen.module.css";

const SHORTCUTS = [
  { href: ROUTES.adventureMap, label: STRINGS.adventure.mapTitle, icon: Map },
  { href: ROUTES.adventureMochila, label: STRINGS.adventure.inventory, icon: Boxes },
  { href: ROUTES.adventureBaus, label: STRINGS.adventure.chests, icon: Gem },
  { href: ROUTES.adventurePalavras, label: STRINGS.adventure.words, icon: BookOpen },
  { href: ROUTES.adventureHeroi, label: STRINGS.adventure.hero, icon: Shield },
  { href: ROUTES.adventurePersonagens, label: STRINGS.adventure.characters, icon: Sparkles },
];

export function AdventureScreen() {
  return (
    <main className={styles.page}>
      <section className={styles.hero}>
        <p className={styles.eyebrow}>{STRINGS.adventure.title}</p>
        <h1>{STRINGS.adventure.hubTitle}</h1>
        <span>{STRINGS.adventure.hubSubtitle}</span>
        <AdventureTransitionLink className={styles.primaryAction} href={ROUTES.adventureMap}>
          <Map size={18} />
          {STRINGS.adventure.openMap}
        </AdventureTransitionLink>
      </section>

      <section className={styles.shortcuts} aria-label={STRINGS.adventure.collectionTitle}>
        {SHORTCUTS.map((item) => (
          <Link className={styles.shortcut} href={item.href} key={item.href}>
            <item.icon size={18} />
            <span>{item.label}</span>
          </Link>
        ))}
      </section>
    </main>
  );
}

