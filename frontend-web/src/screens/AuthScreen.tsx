import { ArrowRight, Languages, Sparkles } from "lucide-react";
import { useState } from "react";

import { authService, type User } from "../services/authService";

interface AuthScreenProps {
  onAuthenticated: (user: User) => void;
}

export default function AuthScreen({ onAuthenticated }: AuthScreenProps) {
  const [mode, setMode] = useState<"login" | "register">("register");
  const [username, setUsername] = useState("felipe");
  const [email, setEmail] = useState("felipe@linguaflow.dev");
  const [password, setPassword] = useState("linguaflow");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function submit() {
    setLoading(true);
    setError("");
    try {
      const user = mode === "login" ? await authService.login(username, password) : await authService.register(username, email, password);
      onAuthenticated(user);
    } catch {
      setError("Nao foi possivel entrar. Confira os dados ou tente outro usuario.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen overflow-hidden bg-slate-50 text-slate-950">
      <div className="mx-auto grid min-h-screen max-w-6xl items-center gap-8 px-5 py-8 lg:grid-cols-[1.05fr_0.95fr]">
        <section className="relative">
          <div className="inline-flex items-center gap-2 rounded-full bg-emerald-50 px-4 py-2 text-sm font-semibold text-emerald-700 ring-1 ring-emerald-100">
            <Sparkles size={18} />
            Daily language flow
          </div>
          <h1 className="mt-6 max-w-2xl text-5xl font-semibold leading-tight tracking-normal md:text-7xl">
            LinguaFlow
          </h1>
          <p className="mt-5 max-w-xl text-xl font-medium text-slate-600">
            Um app de estudo diario com metas, licoes curtas, cenarios reais e progresso por usuario.
          </p>
          <div className="mt-8 grid max-w-xl gap-3 sm:grid-cols-3">
            {["PT -> DE", "30 dias", "180 frases"].map((item) => (
              <div key={item} className="rounded-[8px] bg-white p-4 font-semibold shadow-sm ring-1 ring-slate-200">
                {item}
              </div>
            ))}
          </div>
        </section>

        <section className="rounded-[8px] bg-white p-5 shadow-sm ring-1 ring-slate-200 md:p-7">
          <div className="mb-6 flex items-center justify-between">
            <div>
              <p className="text-sm font-semibold uppercase text-emerald-700">{mode === "login" ? "Entrar" : "Criar conta"}</p>
              <h2 className="text-2xl font-semibold">Comece seu curso</h2>
            </div>
            <div className="grid h-12 w-12 place-items-center rounded-[8px] bg-emerald-50 text-emerald-700 ring-1 ring-emerald-100">
              <Languages />
            </div>
          </div>

          <div className="grid gap-3">
            <input className="h-12 rounded-[8px] border border-slate-200 px-4 font-medium outline-none transition focus:border-emerald-500 focus:ring-4 focus:ring-emerald-100" value={username} onChange={(event) => setUsername(event.target.value)} placeholder="usuario" />
            {mode === "register" ? (
              <input className="h-12 rounded-[8px] border border-slate-200 px-4 font-medium outline-none transition focus:border-emerald-500 focus:ring-4 focus:ring-emerald-100" value={email} onChange={(event) => setEmail(event.target.value)} placeholder="email" />
            ) : null}
            <input className="h-12 rounded-[8px] border border-slate-200 px-4 font-medium outline-none transition focus:border-emerald-500 focus:ring-4 focus:ring-emerald-100" value={password} onChange={(event) => setPassword(event.target.value)} placeholder="senha" type="password" />
          </div>

          {error ? <p className="mt-4 rounded-[8px] bg-red-100 p-3 text-sm font-bold text-red-700">{error}</p> : null}

          <button type="button" onClick={submit} disabled={loading} className="mt-5 flex h-14 w-full items-center justify-center gap-2 rounded-[8px] bg-emerald-600 px-5 py-4 font-semibold text-white shadow-sm transition hover:bg-emerald-700 disabled:opacity-60">
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
