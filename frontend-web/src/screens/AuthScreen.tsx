import { ArrowRight, CheckCircle2, Languages, Sparkles } from "lucide-react";
import { useState } from "react";

import { APP_NAME, APP_TAGLINE_PT } from "../constants/app";
import { authService, type User } from "../services/authService";

interface AuthScreenProps {
  onAuthenticated: (user: User) => void;
}

export default function AuthScreen({ onAuthenticated }: AuthScreenProps) {
  const [mode, setMode] = useState<"login" | "register">("register");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const passwordRules = getPasswordRules(password);
  const isRegisterPasswordValid = passwordRules.every((rule) => rule.valid);

  async function submit() {
    if (!username.trim()) {
      setError("Informe um usuario.");
      return;
    }
    if (mode === "register" && !email.trim()) {
      setError("Informe um email.");
      return;
    }
    if (mode === "register" && !isRegisterPasswordValid) {
      setError("Complete os requisitos da senha antes de continuar.");
      return;
    }
    if (mode === "login" && !password) {
      setError("Informe sua senha.");
      return;
    }

    setLoading(true);
    setError("");
    try {
      const user = mode === "login" ? await authService.login(username, password) : await authService.register(username, email, password);
      onAuthenticated(user);
    } catch (requestError) {
      setError(getAuthErrorMessage(requestError, mode));
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen overflow-hidden bg-slate-50 text-slate-950">
      <div className="mx-auto grid min-h-screen max-w-6xl items-center gap-5 px-3 py-4 md:px-5 md:py-8 lg:grid-cols-[1.05fr_0.95fr]">
        <section className="relative">
          <div className="area-bg-soft area-ring-soft inline-flex items-center gap-2 rounded-full px-4 py-2 text-sm font-semibold">
            <Sparkles size={18} />
            {APP_TAGLINE_PT}
          </div>
          <h1 className="mt-5 max-w-2xl text-4xl font-semibold leading-tight tracking-normal md:mt-6 md:text-7xl">
            {APP_NAME}
          </h1>
          <p className="mt-4 max-w-xl text-base font-medium leading-7 text-slate-600 md:mt-5 md:text-xl">
            Aprenda idiomas com missoes, historia e pratica diaria. Do A1 ao B2, fase por fase.
          </p>
          <div className="mt-6 grid max-w-xl gap-3 sm:grid-cols-3 md:mt-8">
            {[
              { title: "Licoes curtas", detail: "Pratica diaria guiada" },
              { title: "Cenarios reais", detail: "Restaurante, mercado e rotina" },
              { title: "Progresso salvo", detail: "Conta, meta e favoritos" },
            ].map((item) => (
              <div key={item.title} className="rounded-[8px] bg-white p-4 shadow-sm ring-1 ring-slate-200">
                <p className="font-semibold">{item.title}</p>
                <p className="mt-1 text-sm font-medium text-slate-500">{item.detail}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="rounded-[8px] bg-white p-4 shadow-sm ring-1 ring-slate-200 md:p-7">
          <div className="mb-6 flex items-center justify-between">
            <div>
              <p className="area-text-primary text-sm font-semibold uppercase">{mode === "login" ? "Entrar" : "Criar conta"}</p>
              <h2 className="text-2xl font-semibold">Comece seu curso</h2>
            </div>
            <div className="area-bg-soft area-ring-soft grid h-12 w-12 place-items-center rounded-[8px]">
              <Languages />
            </div>
          </div>

          <div className="grid gap-3">
            <input className="area-input h-12 rounded-[8px] border border-slate-200 px-4 font-medium transition" value={username} onChange={(event) => setUsername(event.target.value)} placeholder="usuario" autoComplete="username" />
            {mode === "register" ? (
              <input className="area-input h-12 rounded-[8px] border border-slate-200 px-4 font-medium transition" value={email} onChange={(event) => setEmail(event.target.value)} placeholder="email" autoComplete="email" />
            ) : null}
            <input className="area-input h-12 rounded-[8px] border border-slate-200 px-4 font-medium transition" value={password} onChange={(event) => setPassword(event.target.value)} placeholder="senha" type="password" autoComplete={mode === "login" ? "current-password" : "new-password"} />
          </div>

          {mode === "register" ? (
            <div className="mt-4 rounded-[8px] bg-slate-50 p-4 ring-1 ring-slate-200">
              <p className="text-sm font-semibold uppercase text-slate-500">Senha segura</p>
              <div className="mt-3 grid gap-2">
                {passwordRules.map((rule) => (
                  <div key={rule.label} className={`flex items-center gap-2 text-sm font-semibold transition ${rule.valid ? "area-text-primary" : "text-slate-500"}`}>
                    <CheckCircle2 size={17} style={rule.valid ? { fill: "var(--area-primary-soft)" } : undefined} />
                    {rule.label}
                  </div>
                ))}
              </div>
            </div>
          ) : null}

          {error ? <p className="mt-4 rounded-[8px] bg-red-100 p-3 text-sm font-bold text-red-700">{error}</p> : null}

          <button type="button" onClick={submit} disabled={loading} className="area-btn mt-5 flex h-14 w-full items-center justify-center gap-2 rounded-[8px] px-5 py-4 font-semibold shadow-sm transition disabled:opacity-60">
            {loading ? "Carregando..." : mode === "login" ? "Entrar" : "Criar e continuar"}
            <ArrowRight size={18} />
          </button>

          <button type="button" onClick={() => setMode(mode === "login" ? "register" : "login")} className="mt-4 w-full rounded-[8px] py-3 text-sm font-semibold ring-1 ring-slate-200 transition hover:bg-slate-50">
            {mode === "login" ? "Nao tenho conta" : "Ja tenho conta"}
          </button>
        </section>
      </div>
    </main>
  );
}

function getAuthErrorMessage(error: unknown, mode: "login" | "register") {
  const message = error instanceof Error ? error.message : "";
  if (message.includes("Username already exists")) return "Esse usuario ja existe. Tente entrar ou escolha outro nome.";
  if (message.includes("Invalid username or password")) return "Usuario ou senha incorretos.";
  if (message.includes("uppercase")) return "A senha precisa ter uma letra maiuscula.";
  if (message.includes("lowercase")) return "A senha precisa ter uma letra minuscula.";
  if (message.includes("number")) return "A senha precisa ter um numero.";
  if (message.includes("password:")) return "A senha precisa ter pelo menos 6 caracteres.";
  if (message.includes("email:")) return "Informe um email valido.";
  if (message.includes("Failed to fetch")) return "Nao consegui conectar no backend. Confirme se o Django esta rodando na porta 8000.";
  return mode === "login"
    ? "Nao foi possivel entrar. Confira usuario e senha."
    : "Nao foi possivel criar a conta. Confira os dados e tente novamente.";
}

function getPasswordRules(password: string) {
  return [
    { label: "Pelo menos 6 caracteres", valid: password.length >= 6 },
    { label: "Uma letra maiuscula", valid: /[A-Z]/.test(password) },
    { label: "Uma letra minuscula", valid: /[a-z]/.test(password) },
    { label: "Um numero", valid: /\d/.test(password) },
  ];
}
