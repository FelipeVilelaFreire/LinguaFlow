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

### Modo Aventura (RPG) — Hierarquia obrigatória

```
SÉRIE  (nível CEFR — ex: A1)
  └── TEMPORADA  (5 por série — badge T1…T5)
        └── FASE  (25 por temporada — types: story | review | boss)
              └── SEÇÃO  (6 por fase)
                    1. Cotidiano      — fatia de vida, contexto do NPC
                    2. Aquecimento    — revisão do vocabulário anterior
                    3. Evento Principal — novo vocabulário via narrativa
                    4. Decodificação  — padrão gramatical revelado
                    5. Prática        — exercícios guiados
                    6. Obstáculo      — gate Metroidvania (vocabulário como chave)
```

**Regras fixas — nunca quebrar:**
- `"A1"` identifica a **SÉRIE inteira** (todas as 5 temporadas). Não é o nível de uma temporada.
- Cada temporada mostra seu badge como **T1, T2, T3, T4, T5** — não A1/A2/B1/etc.
- O contexto do arco (ex: "A1 · Il Viandante") aparece no header da série e do mapa, nunca repetido por temporada.
- Fases 1–14 = história, Fases 15/20 = revisão narrativa, Fases 21–23 = checkpoints SRS, Fase 24 = pré-boss, Fase 25 = Boss.
- Boss fecha sempre a temporada + desbloqueia recompensa que entra na Mochila.

**MVP em produção: Italiano — "Il Viandante" (A1)**
| T | Cenário | Boss |
|---|---------|------|
| T1 | Arrivo al Borgo | Il Condottiero |
| T2 | Venezia dei Mercanti | Il Leone Alato |
| T3 | La Toscana dei Medici | Il Magnifico |
| T4 | Napoli e il Vesuvio | Il Vesuvio |
| T5 | Roma Aeterna | L'Imperatore |

**Arquivos-chave do modo aventura:**
| Arquivo | Responsabilidade |
|---------|-----------------|
| `src/types/adventure.ts` | `AdventureChapter`, `AdventurePhase`, `PhaseType` |
| `src/mocks/adventureItMock.ts` | Dados mock do "Il Viandante" (substituir por API no futuro) |
| `src/theme/adventureColors.ts` | Paleta escura imersiva por idioma (`getAdventureColors`) |
| `src/screens/AdventureScreen.tsx` | Landing da série (lista as 5 temporadas) |
| `src/screens/adventure/AdventureMapScreen.tsx` | Mapa de nós da temporada (winding path, 25 nós, ~85 px entre nós) |
| `src/screens/adventure/AdventureModule.tsx` | Container 3-abas: Mapa / Mochila / Herói |

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

## Arquitetura CSS — Como escrever estilos

Regra de ouro: cada tipo de estilo tem um lugar fixo. Nunca misturar.

| O que | Onde fica | Exemplo |
|---|---|---|
| Layout, espaçamento, cores slate | Tailwind no JSX | `className="flex flex-col gap-3"` |
| CSS vars, hover com vars, animações | `globals.css` | `.auth-submit`, `.auth-input:focus` |
| Valor calculado em JS | `style={{}}` inline | `opacity: mounted ? 1 : 0` |
| **Nunca** | `<style>` dentro do componente | — |

**Por que isso importa para IA:** quando os estilos estão em um só lugar previsível, qualquer modelo consegue ler, editar e não quebrar o que já existe. Estilos espalhados entre `style={{}}`, `className` e `<style>` tornam o código imprevisível para edição automatizada.

**Aplicação prática:**
- Classe nova que usa `--area-primary`? → vai para `globals.css`
- Posição/tamanho/cor slate? → vai para `className` com Tailwind
- Delay de animação que depende de índice JS? → único caso aceitável para `style={{}}`
- Quer criar `.minha-screen-btn`? → adiciona em `globals.css`, agrupa próximo às outras classes da tela

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
