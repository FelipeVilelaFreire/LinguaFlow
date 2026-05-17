"use client";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft, faArrowRight, faCheck } from "@fortawesome/free-solid-svg-icons";
import { ROUTES, STRINGS, adventureService, contentService } from "@linguaflow/shared-core";
import type { AvailableLanguage } from "@linguaflow/shared-core";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import styles from "./OnboardingScreen.module.css";

const SOURCE_LANGUAGES = [
  { code: "PT", detailKey: "sourceLanguageDetailPt" as const },
];

const LEVELS = [
  { code: "A1", labelKey: "levelIniciante" as const, detailKey: "levelA1Detail" as const },
];

const WEEKDAYS = [0, 1, 2, 3, 4, 5, 6];
const SESSION_OPTIONS = [15, 30, 45, 60, 90];

export function OnboardingScreen() {
  const router = useRouter();
  const [step, setStep] = useState<1 | 2>(1);
  const [direction, setDirection] = useState<"forward" | "back">("forward");
  const [sourceLanguage, setSourceLanguage] = useState(SOURCE_LANGUAGES[0]);
  const [targetLanguage, setTargetLanguage] = useState<AvailableLanguage | null>(null);
  const [level, setLevel] = useState(LEVELS[0]);
  const [studyDays, setStudyDays] = useState([0, 2, 4]);
  const [sessionMinutes, setSessionMinutes] = useState(30);
  const [loading, setLoading] = useState(false);
  const [availableTargets, setAvailableTargets] = useState<AvailableLanguage[]>([]);
  const [loadingLanguages, setLoadingLanguages] = useState(true);

  useEffect(() => {
    adventureService.listAvailableLanguages()
      .then((languages) => {
        setAvailableTargets(languages);
        if (languages.length > 0) setTargetLanguage(languages[0]);
      })
      .finally(() => setLoadingLanguages(false));
  }, []);

  function goToStep2() {
    setDirection("forward");
    setStep(2);
  }

  function goToStep1() {
    setDirection("back");
    setStep(1);
  }

  function toggleDay(day: number) {
    setStudyDays((current) =>
      current.includes(day) ? current.filter((item) => item !== day) : [...current, day].sort((a, b) => a - b),
    );
  }

  async function finish() {
    if (studyDays.length === 0 || !targetLanguage) return;
    setLoading(true);
    try {
      await contentService.createGoal({
        source_language: sourceLanguage.code,
        target_language: targetLanguage.code,
        target_level: level.code,
        duration_days: 90,
        study_weekdays: studyDays,
        session_minutes: sessionMinutes,
      });
      router.replace(ROUTES.home);
    } finally {
      setLoading(false);
    }
  }

  const months = estimateMonths(studyDays, sessionMinutes);
  const animClass = direction === "forward" ? styles.stepForward : styles.stepBack;

  return (
    <main className={styles.page}>
      <div aria-hidden className={styles.glow} />
      <section className={styles.shell}>
        <header className={styles.header}>
          <img src="/lang-plus.svg" alt="Talkly" />
          <span>{STRINGS.onboarding.stepProgress(step, 2)}</span>
          <div className={styles.progressBar}>
            <div style={{ width: step === 1 ? "50%" : "100%" }} />
          </div>
        </header>

        <div className={`${styles.card} ${animClass}`} key={step}>
          {step === 1 ? (
            <Step1
              sourceLanguage={sourceLanguage}
              targetLanguage={targetLanguage}
              availableTargets={availableTargets}
              loadingLanguages={loadingLanguages}
              level={level}
              onSelectSource={setSourceLanguage}
              onSelectTarget={setTargetLanguage}
              onSelectLevel={setLevel}
            />
          ) : (
            <Step2
              studyDays={studyDays}
              sessionMinutes={sessionMinutes}
              months={months}
              onToggleDay={toggleDay}
              onSelectMinutes={setSessionMinutes}
            />
          )}

          <div className={styles.footer}>
            {step === 2 && (
              <button className={styles.backButton} onClick={goToStep1} type="button" aria-label={STRINGS.actions.back}>
                <FontAwesomeIcon icon={faArrowLeft} />
              </button>
            )}
            <button
              className={styles.submit}
              disabled={loading || (step === 2 && studyDays.length === 0) || (step === 1 && !targetLanguage)}
              onClick={step === 1 ? goToStep2 : finish}
              type="button"
            >
              {loading ? <LoadingDots /> : (
                <>
                  {step === 1 ? STRINGS.onboarding.next : STRINGS.onboarding.start}
                  <FontAwesomeIcon icon={faArrowRight} />
                </>
              )}
            </button>
          </div>
        </div>
      </section>
    </main>
  );
}

function Step1({
  sourceLanguage,
  targetLanguage,
  availableTargets,
  loadingLanguages,
  level,
  onSelectSource,
  onSelectTarget,
  onSelectLevel,
}: {
  sourceLanguage: typeof SOURCE_LANGUAGES[number];
  targetLanguage: AvailableLanguage | null;
  availableTargets: AvailableLanguage[];
  loadingLanguages: boolean;
  level: typeof LEVELS[number];
  onSelectSource: (language: typeof SOURCE_LANGUAGES[number]) => void;
  onSelectTarget: (language: AvailableLanguage) => void;
  onSelectLevel: (level: typeof LEVELS[number]) => void;
}) {
  return (
    <div className={styles.content}>
      <div>
        <h1>{STRINGS.onboarding.configureCourseTitle}</h1>
        <p>{STRINGS.onboarding.configureCourseSubtitle}</p>
      </div>

      <Section label={STRINGS.onboarding.youSpeak}>
        {SOURCE_LANGUAGES.map((language) => (
          <SelectCard
            key={language.code}
            code={language.code}
            title={STRINGS.languages[language.code as keyof typeof STRINGS.languages] ?? language.code}
            detail={STRINGS.onboarding[language.detailKey]}
            selected={sourceLanguage.code === language.code}
            onClick={() => onSelectSource(language)}
          />
        ))}
      </Section>

      <Section label={STRINGS.onboarding.youLearn}>
        {loadingLanguages ? (
          <div className={styles.loadingLine}>
            <LoadingDots /> {STRINGS.onboarding.loadingLanguages}
          </div>
        ) : (
          availableTargets.map((language) => (
            <SelectCard
              key={language.code}
              code={language.code}
              title={STRINGS.languages[language.code as keyof typeof STRINGS.languages] ?? language.code}
              detail={language.chapter_subtitle || language.chapter_title}
              selected={targetLanguage?.code === language.code}
              onClick={() => onSelectTarget(language)}
            />
          ))
        )}
      </Section>

      <Section label={STRINGS.onboarding.levelLabel}>
        <div className={styles.levelGrid}>
          {LEVELS.map((item) => (
            <button
              key={item.code}
              className={`${styles.pill} ${level.code === item.code ? styles.selected : ""}`}
              onClick={() => onSelectLevel(item)}
              type="button"
            >
              <strong>{item.code}</strong>
              <span>{STRINGS.onboarding[item.labelKey]}</span>
              <small>{STRINGS.onboarding[item.detailKey]}</small>
            </button>
          ))}
        </div>
      </Section>
    </div>
  );
}

function Step2({
  studyDays,
  sessionMinutes,
  months,
  onToggleDay,
  onSelectMinutes,
}: {
  studyDays: number[];
  sessionMinutes: number;
  months: number | null;
  onToggleDay: (day: number) => void;
  onSelectMinutes: (minutes: number) => void;
}) {
  return (
    <div className={styles.content}>
      <div>
        <h1>{STRINGS.onboarding.routineTitle}</h1>
        <p>{STRINGS.onboarding.routineSubtitle}</p>
      </div>

      <Section label={STRINGS.onboarding.daysLabel}>
        <div className={styles.dayGrid}>
          {WEEKDAYS.map((day) => (
            <button
              key={day}
              className={`${styles.dayPill} ${studyDays.includes(day) ? styles.selected : ""}`}
              onClick={() => onToggleDay(day)}
              type="button"
            >
              {STRINGS.weekdays.short[day]}
            </button>
          ))}
        </div>
        {studyDays.length === 0 && <p className={styles.dayError}>{STRINGS.onboarding.chooseDayError}</p>}
      </Section>

      <Section label={STRINGS.onboarding.durationLabel}>
        <div className={styles.sessionGrid}>
          {SESSION_OPTIONS.map((option) => (
            <button
              key={option}
              className={`${styles.pill} ${sessionMinutes === option ? styles.selected : ""}`}
              onClick={() => onSelectMinutes(option)}
              type="button"
            >
              {formatSessionDuration(option, "short")}
            </button>
          ))}
        </div>
      </Section>

      {months !== null && (
        <div className={styles.estimate}>
          <strong>{STRINGS.onboarding.estimateSentence(months)}</strong>
          <span>{STRINGS.onboarding.estimatePace(studyDays.length, formatSessionDuration(sessionMinutes, "long"))}</span>
        </div>
      )}
    </div>
  );
}

function SelectCard({
  code,
  title,
  detail,
  selected,
  onClick,
}: {
  code: string;
  title: string;
  detail: string;
  selected: boolean;
  onClick: () => void;
}) {
  return (
    <button className={`${styles.selectCard} ${selected ? styles.selected : ""}`} onClick={onClick} type="button">
      <LangFlag code={code} />
      <span>
        <strong>{title}</strong>
        <small>{detail}</small>
      </span>
      {selected && <FontAwesomeIcon icon={faCheck} />}
    </button>
  );
}

function Section({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div className={styles.section}>
      <p>{label}</p>
      {children}
    </div>
  );
}

function LangFlag({ code }: { code: string }) {
  const countryCode = code === "PT" ? "br" : code === "EN" ? "us" : code.toLowerCase();
  return (
    <img
      src={`https://flagcdn.com/w40/${countryCode}.png`}
      srcSet={`https://flagcdn.com/w80/${countryCode}.png 2x`}
      alt={STRINGS.onboarding.flagAlt(code)}
      width={26}
      height={17}
    />
  );
}

function LoadingDots() {
  return (
    <span className={styles.loadingDots}>
      {[0, 1, 2].map((item) => <span key={item} />)}
    </span>
  );
}

function estimateMonths(days: number[], minutes: number) {
  if (days.length === 0) return null;
  const weeks = 80 / ((days.length * minutes) / 60);
  return Math.max(1, Math.round(weeks / 4.3));
}

function formatSessionDuration(minutes: number, style: "short" | "long") {
  if (minutes === 60) return style === "long" ? STRINGS.onboarding.hourLong : STRINGS.onboarding.hourShort;
  if (minutes === 90) return STRINGS.onboarding.hourAndHalfShort;
  return STRINGS.onboarding.minutesShort(minutes);
}
