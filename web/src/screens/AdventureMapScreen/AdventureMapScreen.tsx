"use client";

import { getAdventureColors, getAdventureThemeVars, ROUTES, STRINGS } from "@linguaflow/shared-core";
import type { ApiAdventureChapter, ApiAdventurePhase } from "@linguaflow/shared-core";
import { useAdventureChapters } from "@linguaflow/shared-core/hooks/adventure";
import { BookOpen, CheckCircle2, Lock, Skull, Star } from "lucide-react";
import Link from "next/link";
import type { CSSProperties } from "react";
import { useMemo, useState } from "react";
import { LangFlag } from "@/src/components/shared";
import { AdventurePhaseModal } from "@/src/components/modals";
import styles from "./AdventureMapScreen.module.css";

const WINDING: Array<{ x: number; y: number }> = [
  { x: 50, y: 70 }, { x: 65, y: 155 }, { x: 78, y: 240 }, { x: 82, y: 325 }, { x: 72, y: 408 },
  { x: 55, y: 493 }, { x: 38, y: 578 }, { x: 24, y: 663 }, { x: 18, y: 748 }, { x: 22, y: 833 },
  { x: 34, y: 918 }, { x: 48, y: 1003 }, { x: 62, y: 1088 }, { x: 76, y: 1173 }, { x: 80, y: 1258 },
  { x: 70, y: 1340 }, { x: 55, y: 1420 }, { x: 40, y: 1500 }, { x: 26, y: 1580 }, { x: 20, y: 1660 },
  { x: 28, y: 1740 }, { x: 40, y: 1820 }, { x: 50, y: 1900 }, { x: 50, y: 1980 }, { x: 50, y: 2050 },
];

const PATH_D =
  "M50,70 " +
  "C50,112 65,112 65,155 C65,197 78,197 78,240 C78,282 82,282 82,325 C82,366 72,366 72,408 " +
  "C72,450 55,450 55,493 C55,535 38,535 38,578 C38,620 24,620 24,663 C24,705 18,705 18,748 " +
  "C18,790 22,790 22,833 C22,875 34,875 34,918 C34,960 48,960 48,1003 C48,1045 62,1045 62,1088 " +
  "C62,1130 76,1130 76,1173 C76,1215 80,1215 80,1258 C80,1299 70,1299 70,1340 " +
  "C70,1380 55,1380 55,1420 C55,1460 40,1460 40,1500 C40,1540 26,1540 26,1580 C26,1620 20,1620 20,1660 " +
  "C20,1700 28,1700 28,1740 C28,1780 40,1780 40,1820 C40,1860 50,1860 50,1900 " +
  "C50,1940 50,1940 50,1980 C50,2015 50,2015 50,2050";

const SEASON_HEIGHT = 2120;

const TABS = [
  { href: ROUTES.adventure, label: STRINGS.adventure.title },
  { href: ROUTES.adventureMap, label: STRINGS.adventure.mapTitle, active: true },
  { href: ROUTES.adventureMochila, label: STRINGS.adventure.inventory },
  { href: ROUTES.adventureBaus, label: STRINGS.adventure.chests },
  { href: ROUTES.adventurePalavras, label: STRINGS.adventure.words },
  { href: ROUTES.adventureHeroi, label: STRINGS.adventure.hero },
  { href: ROUTES.adventurePersonagens, label: STRINGS.adventure.characters },
];

export function AdventureMapScreen() {
  const langCode = "ES";
  const { chapters, isLoading, error } = useAdventureChapters(langCode);
  const colors = getAdventureColors(langCode, "dark");
  const themeStyle = getAdventureThemeVars(colors) as CSSProperties;
  const [selectedPhase, setSelectedPhase] = useState<{ chapter: ApiAdventureChapter; phase: ApiAdventurePhase } | null>(null);

  if (isLoading) return <State message={STRINGS.adventure.loading} style={themeStyle} />;
  if (error) return <State message={error} style={themeStyle} />;
  if (chapters.length === 0) return <State message={STRINGS.adventure.empty} style={themeStyle} />;

  return (
    <main className={styles.page} style={themeStyle}>
      <AdventureTabs langCode={langCode} />
      <section className={styles.mapShell}>
        {chapters.map((chapter, index) => (
          <SeasonMap
            chapter={chapter}
            colors={colors}
            isUnlocked={index === 0 || chapters[index - 1].phases.every((phase) => phase.is_completed)}
            key={chapter.id}
            onSelectPhase={(phase) => setSelectedPhase({ chapter, phase })}
          />
        ))}
      </section>
      {selectedPhase ? (
        <AdventurePhaseModal
          chapter={selectedPhase.chapter}
          phase={selectedPhase.phase}
          onClose={() => setSelectedPhase(null)}
        />
      ) : null}
    </main>
  );
}

function AdventureTabs({ langCode }: { langCode: string }) {
  return (
    <nav className={styles.tabs} aria-label={STRINGS.adventure.title}>
      {TABS.map((tab) => tab.active ? (
        <span className={styles.activeTab} key={tab.href}>
          <LangFlag code={langCode} size="xs" />
          {tab.label}
        </span>
      ) : (
        <Link href={tab.href} key={tab.href}>{tab.label}</Link>
      ))}
    </nav>
  );
}

function SeasonMap({
  chapter,
  colors,
  isUnlocked,
  onSelectPhase,
}: {
  chapter: ApiAdventureChapter;
  colors: ReturnType<typeof getAdventureColors>;
  isUnlocked: boolean;
  onSelectPhase: (phase: ApiAdventurePhase) => void;
}) {
  const currentPhase = chapter.progress?.current_phase ?? 1;
  const completed = chapter.phases.filter((phase) => phase.is_completed).length;

  return (
    <section className={styles.season}>
      <header className={styles.seasonHeader}>
        <div>
          <span className={styles.levelBadge}>{chapter.level}</span>
          {chapter.subtitle ? <small>{chapter.subtitle}</small> : null}
        </div>
        <h1>{chapter.title}</h1>
        <p>{isUnlocked ? STRINGS.adventure.phasesCompleted(completed, chapter.phases.length) : STRINGS.adventure.lockedLabel}</p>
      </header>

      <div className={styles.winding} style={{ height: SEASON_HEIGHT }}>
        <svg className={styles.path} height={SEASON_HEIGHT} preserveAspectRatio="none" viewBox={`0 0 100 ${SEASON_HEIGHT}`} width="100%">
          <path d={PATH_D} fill="none" opacity="0.24" stroke={colors.pathColor} strokeWidth="3.2" />
          <path d={PATH_D} fill="none" opacity="0.5" stroke={colors.pathColor} strokeWidth="2" />
          <path d={PATH_D} fill="none" opacity="0.35" stroke={colors.goldAccent} strokeDasharray="5,8" strokeWidth="0.7" />
        </svg>

        {chapter.phases.map((phase, index) => {
          const position = WINDING[index] ?? { x: 50, y: 70 + index * 82 };
          const status = getPhaseStatus(phase, currentPhase, isUnlocked);
          return (
            <PhaseNode
              chapter={chapter}
              colors={colors}
              key={phase.id}
              phase={phase}
              position={position}
              status={status}
              onSelect={() => onSelectPhase(phase)}
            />
          );
        })}
      </div>
    </section>
  );
}

function PhaseNode({
  chapter,
  colors,
  phase,
  position,
  status,
  onSelect,
}: {
  chapter: ApiAdventureChapter;
  colors: ReturnType<typeof getAdventureColors>;
  phase: ApiAdventurePhase;
  position: { x: number; y: number };
  status: "completed" | "current" | "locked";
  onSelect: () => void;
}) {
  const isBoss = phase.is_boss;
  const isReview = phase.phase_type === "review";
  const isCurrent = status === "current";
  const size = isBoss ? 64 : 54;
  const sectionTotal = 6;
  const completedSections = phase.completed_sections ?? 0;
  const style = {
    "--node-x": `${position.x}%`,
    "--node-y": `${position.y}px`,
    "--node-size": `${size}px`,
  } as CSSProperties;

  const inner = (
    <>
      {isCurrent ? <ProgressRing completed={completedSections} size={size + 20} total={sectionTotal} /> : null}
      <span className={getNodeClass(status, isBoss, isReview)}>
        {status === "completed" ? <CheckCircle2 size={isBoss ? 24 : 20} /> : null}
        {status === "locked" ? <Lock size={isBoss ? 22 : 17} /> : null}
        {status === "current" && isBoss ? <Skull size={22} /> : null}
        {status === "current" && isReview ? <BookOpen size={17} /> : null}
        {status === "current" && !isBoss && !isReview ? (
          <strong>
            <small>{STRINGS.adventure.dayShort}</small>
            {phase.number}
          </strong>
        ) : null}
      </span>
      <span className={styles.phaseLabel}>
        <strong>{phase.title}</strong>
        <small>{getStatusLabel(status, phase)}</small>
      </span>
      {status === "completed" && !isBoss ? <Stars score={phase.score ?? 0} total={phase.phrase_count || 1} color={colors.goldAccent} /> : null}
    </>
  );

  if (status === "locked") {
    return <div className={styles.phaseNodeWrap} style={style}>{inner}</div>;
  }

  return (
    <button className={styles.phaseNodeWrap} onClick={onSelect} style={style} type="button">
      {inner}
    </button>
  );
}

function ProgressRing({ completed, total, size }: { completed: number; total: number; size: number }) {
  const radius = size / 2 - 4;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference * (1 - Math.min(1, completed / Math.max(total, 1)));

  return (
    <svg className={styles.progressRing} height={size} viewBox={`0 0 ${size} ${size}`} width={size}>
      <circle cx={size / 2} cy={size / 2} fill="none" r={radius} />
      <circle cx={size / 2} cy={size / 2} fill="none" r={radius} strokeDasharray={circumference} strokeDashoffset={offset} />
    </svg>
  );
}

function Stars({ score, total, color }: { score: number; total: number; color: string }) {
  const count = Math.max(1, Math.ceil((score / Math.max(total, 1)) * 3));
  return (
    <span className={styles.stars}>
      {[1, 2, 3].map((item) => <Star fill={item <= count ? color : "none"} key={item} size={8} stroke={color} />)}
    </span>
  );
}

function State({ message, style }: { message: string; style: CSSProperties }) {
  return (
    <main className={styles.page} style={style}>
      <p className={styles.state}>{message}</p>
    </main>
  );
}

function getPhaseStatus(phase: ApiAdventurePhase, currentPhase: number, chapterUnlocked: boolean) {
  if (!chapterUnlocked) return "locked";
  if (phase.is_completed) return "completed";
  if (phase.number === currentPhase) return "current";
  return "locked";
}

function getNodeClass(status: "completed" | "current" | "locked", isBoss: boolean, isReview: boolean) {
  return [
    styles.phaseNode,
    status === "completed" ? styles.completedNode : "",
    status === "locked" ? styles.lockedNode : "",
    status === "current" ? styles.currentNode : "",
    isBoss ? styles.bossNode : "",
    isReview ? styles.reviewNode : "",
  ].filter(Boolean).join(" ");
}

function getStatusLabel(status: "completed" | "current" | "locked", phase: ApiAdventurePhase) {
  if (status === "completed") return STRINGS.adventure.completedLabel;
  if (status === "locked") return STRINGS.adventure.lockedLabel;
  if (phase.is_boss) return STRINGS.adventure.phaseStartBoss;
  if (phase.phase_type === "review") return STRINGS.adventure.phaseStartReview;
  return STRINGS.adventure.sectionLabel((phase.completed_sections ?? 0) + 1, 6);
}


