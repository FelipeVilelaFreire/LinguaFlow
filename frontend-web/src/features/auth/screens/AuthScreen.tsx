import { ArrowRight, CheckCircle2, Eye, EyeOff } from "lucide-react";
import { useEffect, useRef, useState } from "react";

import { APP_TAGLINE_PT } from "../../../constants/app";
import { useStrings } from "../../../contexts/StringsContext";
import { authService, type User } from "../../../services/authService";

interface AuthScreenProps {
  onAuthenticated: (user: User) => void;
}

export default function AuthScreen({ onAuthenticated }: AuthScreenProps) {
  const s = useStrings();
  const [mode, setMode] = useState<"login" | "register">("login");
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

  const passwordRules = getPasswordRules(password, s);
  const isPasswordValid = passwordRules.every((r) => r.valid);
  const passwordsMatch = password === confirmPassword;

  useEffect(() => {
    const t = setTimeout(() => setMounted(true), 40);
    return () => clearTimeout(t);
  }, []);

  function switchMode(next: "login" | "register") {
    setMode(next);
    setError("");
    setPassword("");
    setConfirmPassword("");
    setTimeout(() => firstInputRef.current?.focus(), 120);
  }

  function triggerShake() {
    setShaking(true);
    setTimeout(() => setShaking(false), 400);
  }

  async function submit() {
    if (mode === "register") {
      if (!username.trim()) { setError(s.auth.usernameRequiredRegister); triggerShake(); return; }
      if (!email.trim()) { setError(s.auth.emailRequired); triggerShake(); return; }
      if (!isPasswordValid) { setError(s.auth.passwordRulesIncomplete); triggerShake(); return; }
      if (!passwordsMatch) { setError(s.auth.passwordsDoNotMatch); triggerShake(); return; }
    } else {
      if (!username.trim()) { setError(s.auth.usernameRequiredLogin); triggerShake(); return; }
      if (!password) { setError(s.auth.passwordRequired); triggerShake(); return; }
    }

    setLoading(true);
    setError("");
    try {
      const user = mode === "login"
        ? await authService.login(username, password)
        : await authService.register(username, email, password);
      onAuthenticated(user);
    } catch (err) {
      setError(getAuthErrorMessage(err, mode, s));
      triggerShake();
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="flex min-h-dvh flex-col items-center justify-center bg-white px-4 py-10">

      {/* Ambient teal glow — posição fixa, definida no globals.css */}
      <div aria-hidden className="auth-glow z-0" />

      <div className="relative z-10 flex w-full max-w-[400px] flex-col items-center gap-7">

        {/* Logo */}
        <header
          className="text-center transition-[opacity,transform] duration-500"
          style={{
            opacity: mounted ? 1 : 0,
            transform: mounted ? "translateY(0)" : "translateY(-14px)",
            transitionTimingFunction: "cubic-bezier(0.16,1,0.3,1)",
          }}
        >
          <div className="auth-logo-icon mb-3.5">
            <img src="/lang-plus.svg" alt="Lang+" />
          </div>
          <p className="mt-1.5 text-sm font-medium text-slate-500">{APP_TAGLINE_PT}</p>
        </header>

        {/* Card */}
        <div
          className="w-full rounded-2xl border border-slate-200 bg-white p-7 shadow-[0_2px_4px_rgba(0,0,0,0.03),0_8px_24px_rgba(0,0,0,0.06)] transition-[opacity,transform] duration-500"
          style={{
            opacity: mounted ? 1 : 0,
            transform: mounted ? "translateY(0)" : "translateY(18px)",
            transitionTimingFunction: "cubic-bezier(0.16,1,0.3,1)",
            transitionDelay: "80ms",
          }}
        >
          {/* Tab toggle */}
          <div className="auth-tab-pill mb-6">
            <button className={`auth-tab ${mode === "login" ? "active" : ""}`} onClick={() => switchMode("login")}>
              {s.auth.loginTab}
            </button>
            <button className={`auth-tab ${mode === "register" ? "active" : ""}`} onClick={() => switchMode("register")}>
              {s.auth.registerTab}
            </button>
          </div>

          {/* Fields */}
          <div
            className="flex flex-col gap-3"
            style={{ animation: shaking ? "shake 0.38s ease" : "none" }}
          >
            <Field label={s.auth.usernameLabel} htmlFor="username">
              <input
                ref={firstInputRef}
                id="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && submit()}
                placeholder="seu_usuario"
                autoComplete="username"
                className="auth-input"
              />
            </Field>

            {mode === "register" && (
              <Field label={s.auth.emailLabel} htmlFor="email">
                <input
                  id="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  onKeyDown={(e) => e.key === "Enter" && submit()}
                  placeholder="seu@email.com"
                  type="email"
                  autoComplete="email"
                  className="auth-input"
                />
              </Field>
            )}

            <Field label={s.auth.passwordLabel} htmlFor="password">
              <PasswordInput
                id="password"
                value={password}
                onChange={setPassword}
                onEnter={submit}
                show={showPassword}
                onToggleShow={() => setShowPassword((v) => !v)}
                placeholder="••••••••"
                autoComplete={mode === "login" ? "current-password" : "new-password"}
              />
            </Field>

            {mode === "register" && (
              <Field label={s.auth.confirmPasswordLabel} htmlFor="confirm">
                <PasswordInput
                  id="confirm"
                  value={confirmPassword}
                  onChange={setConfirmPassword}
                  onEnter={submit}
                  show={showConfirm}
                  onToggleShow={() => setShowConfirm((v) => !v)}
                  placeholder="••••••••"
                  autoComplete="new-password"
                  hasError={confirmPassword.length > 0 && !passwordsMatch}
                />
              </Field>
            )}
          </div>

          {/* Esqueci a senha */}
          {mode === "login" && (
            <div className="mt-2 text-right">
              <a href="#" className="area-text-primary text-[13px] font-medium no-underline hover:underline">
                {s.auth.forgotPassword}
              </a>
            </div>
          )}

          {/* Requisitos de senha */}
          {mode === "register" && password.length > 0 && (
            <div className="auth-rules">
              {passwordRules.map((rule) => (
                <div key={rule.label} className={`auth-rule ${rule.valid ? "valid" : ""}`}>
                  <CheckCircle2
                    size={15}
                    className="shrink-0"
                    style={{ fill: rule.valid ? "var(--area-primary-soft)" : "transparent", transition: "fill 0.2s" }}
                  />
                  {rule.label}
                </div>
              ))}
            </div>
          )}

          {/* Error */}
          {error && (
            <div className="mt-3.5 rounded-[10px] border border-red-200 bg-red-50 px-3.5 py-3 text-[13.5px] font-semibold text-red-600"
              style={{ animation: "fadeIn 0.25s ease" }}>
              {error}
            </div>
          )}

          {/* Submit */}
          <button
            type="button"
            onClick={submit}
            disabled={loading}
            className="auth-submit mt-5"
          >
            {loading ? <LoadingDots /> : (
              <>
                {mode === "login" ? s.auth.loginTab : s.auth.registerTab}
                <ArrowRight size={17} strokeWidth={2.5} />
              </>
            )}
          </button>

          {/* Divisor */}
          <div className="my-5 flex items-center gap-3">
            <div className="h-px flex-1 bg-slate-200" />
            <span className="text-xs font-semibold text-slate-400">{s.auth.orContinueWith}</span>
            <div className="h-px flex-1 bg-slate-200" />
          </div>

          {/* Google */}
          <button type="button" className="auth-google" onClick={() => { /* TODO: Google OAuth */ }}>
            <GoogleIcon />
            {s.auth.continueWithGoogle}
          </button>

          {/* Switch mode */}
          <p className="mt-5 text-center text-[13.5px] font-medium text-slate-500">
            {mode === "login" ? s.auth.noAccountPrompt : s.auth.hasAccountPrompt}
            <button
              type="button"
              onClick={() => switchMode(mode === "login" ? "register" : "login")}
              className="area-text-primary border-none bg-transparent p-0 text-[13.5px] font-bold"
              style={{ cursor: "pointer" }}
            >
              {mode === "login" ? s.auth.registerTab : s.auth.loginTab}
            </button>
          </p>
        </div>
      </div>
    </main>
  );
}

function Field({ label, htmlFor, children }: { label: string; htmlFor: string; children: React.ReactNode }) {
  return (
    <div className="flex flex-col gap-1.5">
      <label htmlFor={htmlFor} className="text-[13px] font-semibold text-slate-600">
        {label}
      </label>
      {children}
    </div>
  );
}

function PasswordInput({ id, value, onChange, onEnter, show, onToggleShow, placeholder, autoComplete, hasError }: {
  id: string; value: string; onChange: (v: string) => void; onEnter: () => void;
  show: boolean; onToggleShow: () => void; placeholder: string; autoComplete: string; hasError?: boolean;
}) {
  return (
    <div className="relative">
      <input
        id={id}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && onEnter()}
        placeholder={placeholder}
        type={show ? "text" : "password"}
        autoComplete={autoComplete}
        className={`auth-input pr-11 ${hasError ? "error" : ""}`}
      />
      <button
        type="button"
        onClick={onToggleShow}
        tabIndex={-1}
        className="absolute right-3 top-1/2 flex -translate-y-1/2 items-center border-none bg-transparent p-1 text-slate-400"
        style={{ cursor: "pointer" }}
      >
        {show ? <EyeOff size={16} /> : <Eye size={16} />}
      </button>
    </div>
  );
}

function LoadingDots() {
  return (
    <span className="flex items-center gap-1.5">
      {[0, 1, 2].map((i) => (
        <span
          key={i}
          className="h-1.5 w-1.5 rounded-full bg-current opacity-70"
          style={{ animation: "loadingDot 1.2s ease-in-out infinite", animationDelay: `${i * 0.2}s` }}
        />
      ))}
    </span>
  );
}

function GoogleIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M17.64 9.20455C17.64 8.56636 17.5827 7.95272 17.4764 7.36364H9V10.845H13.8436C13.635 11.97 13.0009 12.9232 12.0477 13.5614V15.8196H14.9564C16.6582 14.2527 17.64 11.9455 17.64 9.20455Z" fill="#4285F4"/>
      <path d="M9 18C11.43 18 13.4673 17.1941 14.9564 15.8195L12.0477 13.5613C11.2418 14.1013 10.2109 14.4204 9 14.4204C6.65591 14.4204 4.67182 12.8372 3.96409 10.71H0.957275V13.0418C2.43818 15.9831 5.48182 18 9 18Z" fill="#34A853"/>
      <path d="M3.96409 10.71C3.78409 10.17 3.68182 9.59318 3.68182 9C3.68182 8.40682 3.78409 7.83 3.96409 7.29V4.95818H0.957275C0.347727 6.17318 0 7.54773 0 9C0 10.4523 0.347727 11.8268 0.957275 13.0418L3.96409 10.71Z" fill="#FBBC05"/>
      <path d="M9 3.57955C10.3214 3.57955 11.5077 4.03364 12.4405 4.92545L15.0218 2.34409C13.4632 0.891818 11.4259 0 9 0C5.48182 0 2.43818 2.01682 0.957275 4.95818L3.96409 7.29C4.67182 5.16273 6.65591 3.57955 9 3.57955Z" fill="#EA4335"/>
    </svg>
  );
}

function getAuthErrorMessage(error: unknown, mode: "login" | "register", s: ReturnType<typeof useStrings>) {
  const message = error instanceof Error ? error.message : "";
  if (message.includes("Username already exists")) return s.auth.errorUsernameExists;
  if (message.includes("Invalid username or password")) return s.auth.errorInvalidCredentials;
  if (message.includes("uppercase")) return s.auth.errorPasswordUppercase;
  if (message.includes("lowercase")) return s.auth.errorPasswordLowercase;
  if (message.includes("number")) return s.auth.errorPasswordNumber;
  if (message.includes("password:")) return s.auth.errorPasswordLength;
  if (message.includes("email:")) return s.auth.errorEmailInvalid;
  if (message.includes("Failed to fetch")) return s.auth.errorBackendUnavailable;
  return mode === "login"
    ? s.auth.errorLoginFallback
    : s.auth.errorRegisterFallback;
}

function getPasswordRules(password: string, s: ReturnType<typeof useStrings>) {
  return [
    { label: s.auth.passwordRuleLength, valid: password.length >= 6 },
    { label: s.auth.passwordRuleUppercase, valid: /[A-Z]/.test(password) },
    { label: s.auth.passwordRuleLowercase, valid: /[a-z]/.test(password) },
    { label: s.auth.passwordRuleNumber, valid: /\d/.test(password) },
  ];
}
