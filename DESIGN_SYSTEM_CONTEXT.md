# Talkly — Design System Context
Paste this entire file at the start of any AI conversation to give full design system context.

---

// CLAUDE.md — Project rules and conventions

# Talkly — Diretrizes para Claude Code

## Nome e identidade
- **App name:** `Talkly` — definido em `src/constants/app.ts` (APP_NAME)
- **Tagline PT:** `Aprenda idiomas vivendo a historia` (APP_TAGLINE_PT)
- Mudar o nome em `app.ts` já muda tudo: strings.ts, App.tsx, AuthScreen.tsx, index.html (via `VITE_APP_NAME` no `.env`)

## Mobile First
Todo desenvolvimento prioriza mobile. Desktop é aprimoramento, não base.

- Bottom nav com no máximo 5 itens
- Alvos de toque generosos (mínimo h-12), sem interações hover-only
- Layout de coluna única em mobile, grid apenas em `md:` e acima
- Modais complexos → preferir telas dedicadas ou bottom sheets
- Full-screen views quebram o padding do `<main>` com `-mx-3 -mt-3 min-h-[calc(100dvh-3.5rem)]`

## Stack
- React + Vite + TypeScript
- Tailwind CSS (estrutura e espaçamento)
- Lucide React (ícones)
- CSS custom properties para theming (não Tailwind config)

## Princípio: uma linha muda tudo
O tema inteiro vem de `src/theme/colors.ts`. Mudar `STUDY_AREA_COLORS.DE` propaga para toda a UI via CSS custom properties.

**Nunca usar classes Tailwind de cor hardcoded** (ex: `bg-emerald-600`, `text-teal-700`).
Sempre usar as CSS vars (`var(--area-primary)`) ou as classes utilitárias (`.area-btn`, `.area-text-primary`).

---

// src/theme/colors.ts — Color tokens per language

export interface StudyAreaColorTokens {
  name: string;
  primary: string;
  primaryDark: string;
  primarySoft: string;
  accent: string;
  accentSoft: string;
  page: string;
  textOnPrimary: string;
}

export const STUDY_AREA_COLORS = {
  DE: {
    name: "Alemao",
    primary: "#14b8a6",
    primaryDark: "#0f766e",
    primarySoft: "#f0fdfa",
    accent: "#dc2626",
    accentSoft: "#fef2f2",
    page: "#f8fafc",
    textOnPrimary: "#0f172a",  // dark — teal is too light for white text (contrast ~2.5:1)
  },
  ES: {
    name: "Espanhol",
    primary: "#111827",
    primaryDark: "#030712",
    primarySoft: "#f1f5f9",
    accent: "#facc15",
    accentSoft: "#fefce8",
    page: "#f8fafc",
    textOnPrimary: "#ffffff",
  },
  EN: {
    name: "Ingles",
    primary: "#1e3a8a",
    primaryDark: "#172554",
    primarySoft: "#f1f5f9",
    accent: "#dc2626",
    accentSoft: "#fef2f2",
    page: "#f8fafc",
    textOnPrimary: "#ffffff",
  },
};

// FALLBACK = DE (teal)
export const FALLBACK_STUDY_AREA_COLORS = STUDY_AREA_COLORS.DE;

---

// src/theme/studyAreaTheme.ts — How tokens become CSS vars

// getStudyAreaThemeStyle(theme) returns a CSSProperties object applied inline
// on the <main> element in AppLayout. This is what sets all --area-* vars.

export function getStudyAreaThemeStyle(theme) {
  return {
    "--area-primary": theme.primary,
    "--area-primary-dark": theme.primaryDark,
    "--area-primary-soft": theme.primarySoft,
    "--area-accent": theme.accent,
    "--area-accent-soft": theme.accentSoft,
    "--area-page": theme.page,
    "--area-text-on-primary": theme.textOnPrimary,
  };
}

---

// src/styles/globals.css — CSS vars defaults + utility classes + animations

:root {
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
  color: #111827;
  background: #f7f7f4;
  --area-primary: #14b8a6;
  --area-primary-dark: #0f766e;
  --area-primary-soft: #f0fdfa;
  --area-accent: #dc2626;
  --area-accent-soft: #fef2f2;
  --area-page: #f8fafc;
  --area-text-on-primary: #0f172a;
}

/* Theme utility classes — use these instead of hardcoded Tailwind color classes */

.area-text-primary {
  color: var(--area-primary);
}

.area-bg-soft {
  background-color: var(--area-primary-soft);
  color: var(--area-primary);
}

.area-ring-soft {
  box-shadow: 0 0 0 1px color-mix(in srgb, var(--area-primary) 25%, transparent);
}

.area-btn {
  background-color: var(--area-primary);
  color: var(--area-text-on-primary);
}
.area-btn:hover:not(:disabled) {
  background-color: var(--area-primary-dark);
}

.area-input:focus {
  outline: none;
  border-color: var(--area-primary) !important;
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--area-primary) 18%, transparent);
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  35%       { transform: translateX(-5px); }
  70%       { transform: translateX(5px); }
}
@keyframes studyCardIn {
  0%   { opacity: 0; transform: translateY(18px) scale(0.985); }
  65%  { opacity: 1; transform: translateY(-2px) scale(1.002); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes stackLift {
  0%   { transform: translateY(10px) scale(0.98); opacity: 0.45; }
  100% { transform: translateY(0) scale(1); opacity: 1; }
}
@keyframes successPop {
  0%   { transform: scale(0.96); opacity: 0; }
  60%  { transform: scale(1.02); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}
@keyframes celebrationRise {
  from { opacity: 0; transform: translateY(18px) scale(0.98); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes progressGlow {
  0%, 100% { box-shadow: 0 0 0 rgba(4,120,87,0); }
  50%       { box-shadow: 0 0 28px rgba(4,120,87,0.22); }
}
@keyframes confettiFall {
  0%   { opacity: 0; transform: translateY(-24px) rotate(0deg); }
  20%  { opacity: 1; }
  100% { opacity: 0; transform: translateY(86px) rotate(160deg); }
}
@keyframes adventureBounce {
  0%, 100% { transform: translate(-50%,-50%) translateY(0px); }
  45%       { transform: translate(-50%,-50%) translateY(-10px); }
}
@keyframes sheetSlideUp {
  from { transform: translateY(100%); opacity: 0; }
  to   { transform: translateY(0); opacity: 1; }
}
@keyframes narrativeFadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes lessonBounce {
  0%  { transform: translateY(0) scale(1); }
  38% { transform: translateY(-7px) scale(1.012); }
  100%{ transform: translateY(0) scale(1); }
}
@keyframes optionTap {
  0%   { transform: scale(0.98); }
  70%  { transform: scale(1.015); }
  100% { transform: scale(1); }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

---

// Design tokens quick reference

BASE PALETTE (always the same, language-independent):
  Screen bg:        bg-slate-50  or  var(--area-page)
  Card bg:          bg-white
  Card border:      ring-1 ring-slate-200
  Card shadow:      shadow-sm
  Card radius:      rounded-[8px]      ← always this, never rounded-lg etc
  Text primary:     text-slate-950
  Text secondary:   text-slate-500
  Row dividers:     divide-y divide-slate-100
  Grid hairlines:   gap-px bg-slate-200 (parent) + bg-white (children)

TYPOGRAPHY:
  Section label:    text-sm font-semibold uppercase text-slate-500
  Body:             text-base font-medium
  Stat value:       text-xl font-bold
  Stat label:       text-xs font-semibold text-slate-500

BUTTONS:
  Primary:    <button class="area-btn rounded-[8px] h-14 w-full font-semibold shadow-sm transition disabled:opacity-60">
  Secondary:  <button class="rounded-[8px] py-3 text-sm font-semibold ring-1 ring-slate-200 hover:bg-slate-50">
  Destructive:<button class="bg-red-600 text-white rounded-[8px] hover:bg-red-700">

INPUTS:
  <input class="area-input h-12 rounded-[8px] border border-slate-200 px-4 font-medium transition">

CARDS:
  Simple:       <div class="bg-white rounded-[8px] shadow-sm ring-1 ring-slate-200 p-4">
  With dividers:<div class="bg-white rounded-[8px] shadow-sm ring-1 ring-slate-200 divide-y divide-slate-100">
  Grid hairline:<div class="grid grid-cols-3 gap-px bg-slate-200 overflow-hidden rounded-[8px] shadow-sm">
                  <div class="bg-white p-4">...</div>

BADGES / ICON CONTAINERS:
  <div class="area-bg-soft area-ring-soft rounded-full px-4 py-2 text-sm font-semibold">
  <div class="area-bg-soft area-ring-soft rounded-[8px] h-12 w-12 grid place-items-center">

THEMED TEXT:
  <p class="area-text-primary font-semibold">

FULL-SCREEN VIEWS (break out of <main> padding):
  <div class="-mx-3 -mt-3 min-h-[calc(100dvh-3.5rem)] md:mx-0 md:mt-0 md:rounded-[8px]">
