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

## Estrutura do App

### Navegação (5 abas)
| Rota | Aba | Conteúdo |
|------|-----|----------|
| `/` | Home | Dashboard de progresso |
| `/aventura` | Aventura | Modo história RPG |
| `/estudo-guiado` | Estudo | Sessão do dia + Cenários |
| `/vocabulario` | Vocabulário | Flashcards e favoritos |
| `/perfil` | Perfil | Conta, metas e Histórico |

### Modo Aventura (RPG)
Cada nível CEFR é um capítulo com narrativa temática (Alemão = Germânicos):
- A1 = Vila Medieval · A2 = Floresta Sombria · B1 = Reino do Castelo
- B2 = Porto Internacional · C1 = Ruínas Antigas
- Boss final ao completar cada capítulo + item de recompensa que carrega pro próximo

## Stack
- React + Vite + TypeScript
- Tailwind CSS (estrutura e espaçamento)
- Lucide React (ícones)
- CSS custom properties para theming (não Tailwind config)

---

## Design System

### Princípio: uma linha muda tudo
O tema inteiro vem de **`src/theme/colors.ts`**. Mudar `STUDY_AREA_COLORS.DE` propaga para:
1. `getStudyAreaThemeStyle()` em `studyAreaTheme.ts`
2. CSS custom properties no `<main>` do AppLayout
3. Todos os componentes via `var(--area-primary)` etc.
4. CSS utilitários em `globals.css` (`.area-btn`, `.area-text-primary`, etc.)

**Nunca usar classes Tailwind de cor hardcoded** (ex: `bg-emerald-600`, `text-teal-700`) em componentes que devem seguir o tema. Usar sempre as CSS vars ou as classes utilitárias.

### Tokens de cor (CSS custom properties)
| Variável | Uso |
|----------|-----|
| `--area-primary` | Botões principais, ícones de destaque, badges |
| `--area-primary-dark` | Hover de botões, estados ativos |
| `--area-primary-soft` | Background suave de badges e ícones |
| `--area-accent` | Elementos de destaque secundário (ex: XP, streak) |
| `--area-accent-soft` | Background suave do accent |
| `--area-page` | Background de tela |
| `--area-text-on-primary` | Texto sobre `--area-primary` (pode ser claro ou escuro dependendo do idioma) |

### Valores atuais — Idioma Alemão (padrão/fallback)
```ts
primary: "#14b8a6"          // teal
primaryDark: "#0f766e"
primarySoft: "#f0fdfa"
accent: "#dc2626"           // vermelho
accentSoft: "#fef2f2"
page: "#f8fafc"
textOnPrimary: "#0f172a"    // escuro — teal é claro demais para texto branco
```

### Classes utilitárias de tema (definidas em globals.css)
```
.area-text-primary      → color: var(--area-primary)
.area-bg-soft           → bg: var(--area-primary-soft), color: var(--area-primary)
.area-ring-soft         → box-shadow ring usando --area-primary com 25% opacidade
.area-btn               → bg: var(--area-primary), color: var(--area-text-on-primary)
.area-btn:hover         → bg: var(--area-primary-dark)
.area-input:focus       → border: var(--area-primary) + ring suave
```

### Paleta base (sempre igual, independe do idioma)
| Contexto | Valor |
|----------|-------|
| Background de tela | `bg-slate-50` ou `var(--area-page)` |
| Cards | `bg-white` |
| Border de cards | `ring-1 ring-slate-200` |
| Texto principal | `text-slate-950` |
| Texto secundário | `text-slate-500` |
| Dividers internos | `divide-y divide-slate-100` |
| Hairline grid | `gap-px bg-slate-200` (pai) + `bg-white` (filhos) |
| Border-radius padrão | `rounded-[8px]` |
| Sombra de card | `shadow-sm` |

### Tipografia
- Font: Inter (definida no `:root` de globals.css)
- Títulos de seção: `text-sm font-semibold uppercase text-slate-500`
- Body: `text-base font-medium`
- Labels de stat: `text-xs font-semibold text-slate-500`
- Valores de stat: `text-xl font-bold`

### Botões
```
Primário:   area-btn + rounded-[8px] h-14 px-5 font-semibold shadow-sm transition
Secundário: ring-1 ring-slate-200 rounded-[8px] py-3 text-sm font-semibold hover:bg-slate-50
Destrutivo: bg-red-600 text-white hover:bg-red-700
```

### Inputs
```
area-input h-12 rounded-[8px] border border-slate-200 px-4 font-medium transition
```

### Cards
```
Simples:     bg-white rounded-[8px] shadow-sm ring-1 ring-slate-200 p-4
Com divisor: bg-white rounded-[8px] shadow-sm ring-1 ring-slate-200 divide-y divide-slate-100
Grid hairline: grid grid-cols-N gap-px bg-slate-200 overflow-hidden rounded-[8px]
               cada célula: bg-white p-4
```

---

## Animações (definidas em globals.css)
| Nome | Uso |
|------|-----|
| `fadeIn` | Entrada suave de elementos (opacity + translateY) |
| `studyCardIn` | Cards de exercício entrando |
| `stackLift` | Elemento subindo da pilha |
| `successPop` | Feedback positivo (scale pop) |
| `celebrationRise` | Tela de conclusão |
| `shake` | Erro / resposta errada |
| `adventureBounce` | Nó atual no mapa de aventura |
| `sheetSlideUp` | Bottom sheet entrando |
| `narrativeFadeIn` | Texto narrativo aparecendo |
| `confettiFall` | Partículas de celebração |
| `lessonBounce` | Ícone de lição pulsando |
| `progressGlow` | Brilho na barra de progresso |

Sempre respeitar `prefers-reduced-motion` — globals.css já tem o media query global.

---

## Arquivos chave
| Arquivo | Responsabilidade |
|---------|-----------------|
| `src/constants/app.ts` | Nome e tagline do app (fonte única) |
| `src/theme/colors.ts` | Tokens de cor por idioma (fonte única de tema) |
| `src/theme/studyAreaTheme.ts` | Converte colors → CSS vars inline style |
| `src/styles/globals.css` | Animações + classes utilitárias de tema |
| `src/components/layout/AppLayout.tsx` | Aplica o tema via `getStudyAreaThemeStyle()` |
| `.env` | `VITE_APP_NAME=Talkly` para o `<title>` do HTML |
