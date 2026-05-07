# Talkly — Frontend Web (Claude Code: escopo exclusivo)

## Regra crítica — nunca hardcodar strings de UI

**Todo texto visível ao usuário deve vir de `src/constants/strings.ts` via `useStrings()`.**

Isso é especialmente obrigatório porque o Talkly é um **app de idiomas** — hardcodar "Italiano", "Começar", "Fase 1" é uma contradição direta com o produto.

```ts
// ❌ NUNCA
<button>Começar</button>
subtitle: `Fase ${n} · Italiano`
const LANG_NAME = { IT: "Italiano" }  // mapa local de idiomas também é proibido

// ✅ SEMPRE
const s = useStrings();
<button>{s.adventure.phaseStart}</button>
subtitle: `${s.adventure.phaseLabel(n)} · ${s.languages[langCode]}`
```

- Adicionar em **PT_STRINGS e EN_STRINGS** antes de usar
- `strings.languages` tem todos os idiomas suportados: DE, ES, EN, IT, FR, JA, PT
- Hook: `useStrings()` de `src/contexts/StringsContext.tsx`

> **Esta instância do Claude Code trabalha SOMENTE no diretório `frontend-web/`.**
> Não sugerir, criar ou editar arquivos fora desta pasta. Backend (Django/DRF) é responsabilidade de outra instância.

---

## Stack

- React 18 + Vite + TypeScript (strict)
- Tailwind CSS — layout, espaçamento, cores slate
- Lucide React — ícones (nunca usar outra lib de ícone)
- CSS custom properties — theming (não Tailwind config)
- Sem bibliotecas de UI externas (sem shadcn, sem MUI, sem Radix)

---

## Mobile First — regras obrigatórias

- Alvos de toque mínimo: `h-12`
- Sem interações hover-only
- Layout coluna única no mobile; grid apenas em `md:` e acima
- Modais complexos → bottom sheets ou telas dedicadas
- Full-screen views quebram o padding do `<main>` com `-mx-3 -mt-3 min-h-[calc(100dvh-3.5rem)]`
  - **Exceção:** telas que renderizam fora do AppLayout usam `h-dvh` sem margens negativas

---

## Navegação — 5 abas

| Rota | Aba |
|------|-----|
| `/` | Home |
| `/aventura` | Aventura |
| `/estudo-guiado` | Estudo |
| `/vocabulario` | Vocabulário |
| `/perfil` | Perfil |

**Telas full-screen (sem AppLayout, sem navbar teal):**
- `/aventura` → `AdventureScreen` (landing das séries)
- `/aventura/mapa` → `AdventureModule` tab=map
- `/aventura/mochila` → `AdventureModule` tab=mochila
- `/aventura/heroi` → `AdventureModule` tab=heroi
- `/aventura/capitulo/:id` → `AdventureChapterScreen`
- `/historico` → `HistoryScreen`
- `/perfil/editar` → `EditProfileScreen`

---

## Modo Aventura — hierarquia

```
SÉRIE  (nível CEFR — ex: A1)
  └── TEMPORADA  (5 por série — badge T1…T5)
        └── FASE  (25 por temporada — types: story | review | boss)
              └── SEÇÃO  (6 por fase)
                    1. Cotidiano
                    2. Aquecimento
                    3. Evento Principal
                    4. Decodificação
                    5. Prática
                    6. Obstáculo (gate Metroidvania)
```

**Regras fixas:**
- `"A1"` = SÉRIE inteira (5 temporadas). Não é nível de temporada.
- Badges por temporada: **T1, T2, T3, T4, T5** — nunca A1/A2/B1.
- Fases 1–14 = história, 15/20 = revisão, 21–23 = checkpoints SRS, 24 = pré-boss, 25 = boss.

**MVP: Italiano "Il Viandante" (A1)**
| T | Cenário | Boss |
|---|---------|------|
| T1 | Arrivo al Borgo | Il Condottiero |
| T2 | Venezia dei Mercanti | Il Leone Alato |
| T3 | La Toscana dei Medici | Il Magnifico |
| T4 | Napoli e il Vesuvio | Il Vesuvio |
| T5 | Roma Aeterna | L'Imperatore |

---

## Tema dual do modo aventura (dark / light)

`themeMode: "dark" | "light"` vive no `AdventureModule` e é passado para filhos como prop.

```ts
// Uso correto:
import { getAdventureColors } from "../theme/adventureColors";
import type { AdventureThemeMode } from "../theme/adventureColors";

const c = getAdventureColors(langCode, themeMode); // themeMode padrão "dark"
```

**Tokens neutros (NUNCA usar rgba hardcoded nos componentes de aventura):**

| Token | Dark | Light |
|-------|------|-------|
| `c.surface` | rgba(255,255,255,0.08) | rgba(0,0,0,0.04) |
| `c.surfaceMid` | rgba(0,0,0,0.35) | rgba(0,0,0,0.06) |
| `c.textOnBg` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) |
| `c.textFaint` | rgba(255,255,255,0.18) | rgba(0,0,0,0.28) |
| `c.borderFaint` | rgba(255,255,255,0.06) | rgba(0,0,0,0.08) |

**Regra crítica de cor de texto — NUNCA usar `parchmentText` ou `parchmentSubtext` diretamente no fundo da tela:**

`parchmentText` é near-black (ex: `#1c1412`) — serve apenas como texto *em cima de* um painel claro (parchment). Usar no fundo escuro do modo aventura = texto invisível.

| Onde usar | Token correto |
|-----------|---------------|
| Título principal sobre fundo da tela | `c.parchment` — adapta automaticamente (cream no dark, tom cultural escuro no light) |
| Texto secundário / NPC / subtítulo | `c.textOnBg` — rgba adaptável por modo |
| Texto mudo / locked / hint | `c.textFaint` — rgba adaptável por modo |
| Texto em cima de painel parchment claro | `c.parchmentText` — único caso válido |

```tsx
// ❌ NUNCA — parchmentText é near-black, invisível no dark
<p style={{ color: c.parchmentText }}>Título</p>

// ✅ SEMPRE para texto sobre o fundo da tela
<p style={{ color: c.parchment }}>Título</p>          // principal
<p style={{ color: c.textOnBg }}>Subtítulo</p>        // secundário
<p style={{ color: c.textFaint }}>Hint / locked</p>   // mudo
```

**`themeMode` deve ser passado para TODAS as telas filhas do `AdventureModule`:**

```tsx
// ✅ Correto — todas recebem themeMode
<AdventureMapScreen     langCode={langCode} themeMode={themeMode} ... />
<AdventureMochilaScreen langCode={langCode} themeMode={themeMode} />
<AdventureHeroScreen    langCode={langCode} themeMode={themeMode} />

// ❌ Nunca — sem themeMode → sempre dark, cores erradas no light mode
<AdventureMochilaScreen langCode={langCode} />
```

**Header e nav são responsabilidade do `AdventureModule`, não das telas filhas:**

O `AdventureModule` renderiza header + nav compartilhados. As telas filhas (Map, Mochila, Herói) renderizam apenas o conteúdo scrollável — sem header próprio.

```
AdventureModule
  ├── <header>  ← compartilhado (back, flag, tema toggle, progresso)
  ├── <div flex-1 overflow-y-auto>  ← conteúdo da aba ativa
  │     AdventureMapScreen | AdventureMochilaScreen | AdventureHeroScreen
  └── <nav>  ← bottom tabs compartilhada
```

**Roadmap:** adicionar `time_of_day: "dawn"|"day"|"dusk"|"night"` em `AdventurePhase` (backend) e derivar `themeMode` automaticamente. Por enquanto o toggle é manual (botão sol/lua no header do mapa).

---

## Arquivos-chave do modo aventura

| Arquivo | Responsabilidade |
|---------|-----------------|
| `src/types/adventure.ts` | `AdventureChapter`, `AdventurePhase`, `PhaseType` |
| `src/mocks/adventureItMock.ts` | Mock "Il Viandante" — T1 completo, T2 completo, T3-T5 skeleton |
| `src/theme/adventureColors.ts` | Paletas dark+light por idioma (IT/DE/EN/ES/FR/JA) |
| `src/screens/AdventureScreen.tsx` | Landing da série (full-screen, sem AppLayout) |
| `src/screens/adventure/AdventureModule.tsx` | Container 3-abas: Mapa/Mochila/Herói (gerencia themeMode) |
| `src/screens/adventure/AdventureMapScreen.tsx` | Mapa de nós winding path (25 nós, ~85px entre nós) |

---

## Design System

### Princípio: uma linha muda tudo
Tema via `src/theme/colors.ts` → `getStudyAreaThemeStyle()` → CSS vars no `<main>` → todos os componentes via `var(--area-primary)` etc.

**Nunca usar classes Tailwind de cor hardcoded** em componentes temáticos (`bg-emerald-600`, `text-teal-700`). Usar CSS vars ou classes utilitárias.

### Tokens CSS custom properties
| Variável | Uso |
|----------|-----|
| `--area-primary` | Botões principais, badges, ícones destaque |
| `--area-primary-dark` | Hover, estados ativos |
| `--area-primary-soft` | Background suave de badges |
| `--area-accent` | Destaque secundário (XP, streak) |
| `--area-page` | Background de tela |
| `--area-text-on-primary` | Texto sobre `--area-primary` |

### Paleta base (sempre igual)
| Contexto | Valor |
|----------|-------|
| Background | `bg-slate-50` / `var(--area-page)` |
| Cards | `bg-white` |
| Border cards | `ring-1 ring-slate-200` |
| Texto principal | `text-slate-950` |
| Texto secundário | `text-slate-500` |
| Border-radius | `rounded-[8px]` |

### Classes utilitárias (`globals.css`)
```
.area-text-primary    → color: var(--area-primary)
.area-bg-soft         → bg: var(--area-primary-soft), color: var(--area-primary)
.area-btn             → bg: var(--area-primary), color: var(--area-text-on-primary)
.area-btn:hover       → bg: var(--area-primary-dark)
.area-input:focus     → border: var(--area-primary) + ring suave
```

---

## Arquitetura CSS — onde cada estilo vai

| O que | Onde | Exemplo |
|---|---|---|
| Layout, espaçamento, cores slate | Tailwind `className` | `"flex flex-col gap-3"` |
| CSS vars, hover com vars, animações | `globals.css` | `.area-btn`, `@keyframes` |
| Valor calculado em JS | `style={{}}` inline | `opacity: mounted ? 1 : 0` |
| **Nunca** | `<style>` dentro do componente | — |

---

## Animações (todas em `globals.css`)

| Nome | Uso |
|------|-----|
| `adventureBounce` | Nó atual no mapa — container do nó (inclui `translate(-50%,-50%)`) |
| `sheetSlideUp` | Bottom sheet entrando |
| `narrativeFadeIn` | Texto narrativo |
| `fadeIn` | Entrada suave geral |
| `studyCardIn` | Cards de exercício |
| `successPop` | Feedback positivo |
| `shake` | Resposta errada |
| `confettiFall` | Celebração |

---

## Componentes — regras de código

- Sem comentários exceto WHY não-óbvio
- Sem error handling para cenários impossíveis
- Sem features além do que a tarefa pede
- Sem abstrações prematuras
- Sem `<style>` dentro de componentes
- Sempre `type="button"` em `<button>` fora de forms
- Ícones: só Lucide React
- Preferir `Edit` sobre `Write` ao modificar arquivos existentes

---

## Contexto do projeto

- App: **Talkly** — aprender idiomas vivendo histórias
- Modo Estudo: flashcards guiados por tema (UI clara, tema teal)
- Modo Aventura: RPG imersivo por idioma (UI dark/RPG, cores por cultura)
- Backend: Django + DRF + JWT (em `../backend/`) — **não tocar nesta instância**
- Mock data em `src/mocks/` substitui API enquanto backend não está conectado
