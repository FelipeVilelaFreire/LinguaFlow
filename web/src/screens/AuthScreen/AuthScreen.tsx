"use client";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRight, faCheckCircle, faEye, faEyeSlash } from "@fortawesome/free-solid-svg-icons";
import { ROUTES, STRINGS, authService, contentService } from "@linguaflow/shared-core";
import type { Strings } from "@linguaflow/shared-core";
import { useRouter } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import styles from "./AuthScreen.module.css";

type AuthMode = "login" | "register";

export function AuthScreen() {
  const router = useRouter();
  const [mode, setMode] = useState<AuthMode>("login");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [mounted, setMounted] = useState(false);
  const [shaking, setShaking] = useState(false);
  const firstInputRef = useRef<HTMLInputElement>(null);

  const passwordRules = getPasswordRules(password, STRINGS);
  const isPasswordValid = passwordRules.every((rule) => rule.valid);
  const passwordsMatch = password === confirmPassword;

  useEffect(() => {
    const timeout = window.setTimeout(() => setMounted(true), 40);
    return () => window.clearTimeout(timeout);
  }, []);

  function switchMode(next: AuthMode) {
    setMode(next);
    setError("");
    setPassword("");
    setConfirmPassword("");
    window.setTimeout(() => firstInputRef.current?.focus(), 120);
  }

  function triggerShake() {
    setShaking(true);
    window.setTimeout(() => setShaking(false), 400);
  }

  async function submit() {
    if (mode === "register") {
      if (!username.trim()) return fail(STRINGS.auth.usernameRequiredRegister);
      if (!email.trim()) return fail(STRINGS.auth.emailRequired);
      if (!isPasswordValid) return fail(STRINGS.auth.passwordRulesIncomplete);
      if (!passwordsMatch) return fail(STRINGS.auth.passwordsDoNotMatch);
    } else {
      if (!username.trim()) return fail(STRINGS.auth.usernameRequiredLogin);
      if (!password) return fail(STRINGS.auth.passwordRequired);
    }

    setLoading(true);
    setError("");
    try {
      if (mode === "login") await authService.login(username, password);
      else await authService.register(username, email, password);

      try {
        await contentService.getCurrentGoal();
        router.replace(ROUTES.home);
      } catch {
        router.replace(ROUTES.onboarding);
      }
    } catch (err) {
      fail(getAuthErrorMessage(err, mode, STRINGS));
    } finally {
      setLoading(false);
    }
  }

  function fail(message: string) {
    setError(message);
    triggerShake();
  }

  return (
    <main className={styles.page}>
      <div aria-hidden className={styles.glow} />

      <section className={styles.shell}>
        <header className={`${styles.header} ${mounted ? styles.visible : ""}`}>
          <div className={styles.logoMark}>
            <img src="/lang-plus.svg" alt="Talkly" />
          </div>
          <p>Aprenda idiomas vivendo a historia</p>
        </header>

        <div className={`${styles.card} ${mounted ? styles.visible : ""}`}>
          <div className={styles.tabs}>
            <button className={mode === "login" ? styles.activeTab : ""} onClick={() => switchMode("login")} type="button">
              {STRINGS.auth.loginTab}
            </button>
            <button className={mode === "register" ? styles.activeTab : ""} onClick={() => switchMode("register")} type="button">
              {STRINGS.auth.registerTab}
            </button>
          </div>

          <div className={`${styles.fields} ${shaking ? styles.shake : ""}`}>
            <Field label={STRINGS.auth.usernameLabel} htmlFor="username">
              <input
                ref={firstInputRef}
                id="username"
                value={username}
                onChange={(event) => setUsername(event.target.value)}
                onKeyDown={(event) => event.key === "Enter" && submit()}
                placeholder="seu_usuario"
                autoComplete="username"
                className={styles.input}
              />
            </Field>

            {mode === "register" && (
              <Field label={STRINGS.auth.emailLabel} htmlFor="email">
                <input
                  id="email"
                  value={email}
                  onChange={(event) => setEmail(event.target.value)}
                  onKeyDown={(event) => event.key === "Enter" && submit()}
                  placeholder="seu@email.com"
                  type="email"
                  autoComplete="email"
                  className={styles.input}
                />
              </Field>
            )}

            <Field label={STRINGS.auth.passwordLabel} htmlFor="password">
              <PasswordInput
                id="password"
                value={password}
                onChange={setPassword}
                onEnter={submit}
                show={showPassword}
                onToggleShow={() => setShowPassword((value) => !value)}
                autoComplete={mode === "login" ? "current-password" : "new-password"}
              />
            </Field>

            {mode === "register" && (
              <Field label={STRINGS.auth.confirmPasswordLabel} htmlFor="confirm">
                <PasswordInput
                  id="confirm"
                  value={confirmPassword}
                  onChange={setConfirmPassword}
                  onEnter={submit}
                  show={showConfirm}
                  onToggleShow={() => setShowConfirm((value) => !value)}
                  autoComplete="new-password"
                  hasError={confirmPassword.length > 0 && !passwordsMatch}
                />
              </Field>
            )}
          </div>

          {mode === "login" && (
            <div className={styles.forgot}>
              <a href="#">{STRINGS.auth.forgotPassword}</a>
            </div>
          )}

          {mode === "register" && password.length > 0 && (
            <div className={styles.rules}>
              {passwordRules.map((rule) => (
                <div key={rule.label} className={rule.valid ? styles.validRule : ""}>
                  <FontAwesomeIcon icon={faCheckCircle} />
                  {rule.label}
                </div>
              ))}
            </div>
          )}

          {error && <div className={styles.error}>{error}</div>}

          <button className={styles.submit} disabled={loading} onClick={submit} type="button">
            {loading ? <LoadingDots /> : (
              <>
                {mode === "login" ? STRINGS.auth.loginTab : STRINGS.auth.registerTab}
                <FontAwesomeIcon icon={faArrowRight} />
              </>
            )}
          </button>

          <div className={styles.divider}>
            <span />
            <small>{STRINGS.auth.orContinueWith}</small>
            <span />
          </div>

          <button className={styles.google} type="button">
            <GoogleIcon />
            {STRINGS.auth.continueWithGoogle}
          </button>

          <p className={styles.switchMode}>
            {mode === "login" ? STRINGS.auth.noAccountPrompt : STRINGS.auth.hasAccountPrompt}
            <button type="button" onClick={() => switchMode(mode === "login" ? "register" : "login")}>
              {mode === "login" ? STRINGS.auth.registerTab : STRINGS.auth.loginTab}
            </button>
          </p>
        </div>
      </section>
    </main>
  );
}

function Field({ label, htmlFor, children }: { label: string; htmlFor: string; children: React.ReactNode }) {
  return (
    <div className={styles.field}>
      <label htmlFor={htmlFor}>{label}</label>
      {children}
    </div>
  );
}

function PasswordInput({
  id,
  value,
  onChange,
  onEnter,
  show,
  onToggleShow,
  autoComplete,
  hasError,
}: {
  id: string;
  value: string;
  onChange: (value: string) => void;
  onEnter: () => void;
  show: boolean;
  onToggleShow: () => void;
  autoComplete: string;
  hasError?: boolean;
}) {
  return (
    <div className={styles.passwordField}>
      <input
        id={id}
        value={value}
        onChange={(event) => onChange(event.target.value)}
        onKeyDown={(event) => event.key === "Enter" && onEnter()}
        placeholder="........"
        type={show ? "text" : "password"}
        autoComplete={autoComplete}
        className={`${styles.input} ${hasError ? styles.inputError : ""}`}
      />
      <button type="button" onClick={onToggleShow} tabIndex={-1}>
        <FontAwesomeIcon icon={show ? faEyeSlash : faEye} />
      </button>
    </div>
  );
}

function LoadingDots() {
  return (
    <span className={styles.loadingDots}>
      {[0, 1, 2].map((item) => <span key={item} />)}
    </span>
  );
}

function GoogleIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden>
      <path d="M17.64 9.2c0-.63-.05-1.25-.16-1.83H9v3.47h4.84a4.14 4.14 0 0 1-1.8 2.72v2.26h2.92c1.7-1.57 2.68-3.87 2.68-6.62Z" fill="#4285F4" />
      <path d="M9 18c2.43 0 4.47-.8 5.96-2.18l-2.91-2.26c-.8.54-1.84.86-3.05.86a5.38 5.38 0 0 1-5.04-3.71H.96v2.33A9 9 0 0 0 9 18Z" fill="#34A853" />
      <path d="M3.96 10.71A5.4 5.4 0 0 1 3.68 9c0-.59.1-1.17.28-1.71V4.96H.96A9 9 0 0 0 0 9c0 1.45.35 2.83.96 4.04l3-2.33Z" fill="#FBBC05" />
      <path d="M9 3.58c1.32 0 2.5.45 3.44 1.35l2.58-2.59A8.65 8.65 0 0 0 9 0 9 9 0 0 0 .96 4.96l3 2.33A5.38 5.38 0 0 1 9 3.58Z" fill="#EA4335" />
    </svg>
  );
}

function getAuthErrorMessage(error: unknown, mode: AuthMode, strings: Strings) {
  const message = error instanceof Error ? error.message : "";
  if (message.includes("Username already exists")) return strings.auth.errorUsernameExists;
  if (message.includes("Invalid username or password")) return strings.auth.errorInvalidCredentials;
  if (message.includes("uppercase")) return strings.auth.errorPasswordUppercase;
  if (message.includes("lowercase")) return strings.auth.errorPasswordLowercase;
  if (message.includes("number")) return strings.auth.errorPasswordNumber;
  if (message.includes("password:")) return strings.auth.errorPasswordLength;
  if (message.includes("email:")) return strings.auth.errorEmailInvalid;
  if (message.includes("Failed to fetch")) return strings.auth.errorBackendUnavailable;
  return mode === "login" ? strings.auth.errorLoginFallback : strings.auth.errorRegisterFallback;
}

function getPasswordRules(password: string, strings: Strings) {
  return [
    { label: strings.auth.passwordRuleLength, valid: password.length >= 6 },
    { label: strings.auth.passwordRuleUppercase, valid: /[A-Z]/.test(password) },
    { label: strings.auth.passwordRuleLowercase, valid: /[a-z]/.test(password) },
    { label: strings.auth.passwordRuleNumber, valid: /\d/.test(password) },
  ];
}
