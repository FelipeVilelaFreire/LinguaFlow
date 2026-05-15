# Talkly — Diretrizes para Claude Code

## Regra crítica — nunca hardcodar strings de UI

**Todo texto visível ao usuário deve vir de `src/constants/strings.ts` via `useStrings()`.**

Isso é especialmente obrigatório porque o Talkly é um **app de idiomas** — hardcodar nomes de idiomas, labels de ações ou textos de interface é uma contradição direta com o produto.

```ts
// ❌ NUNCA
<button>Começar</button>
subtitle: `Fase ${n} · Italiano`

// ✅ SEMPRE
const s = useStrings();
<button>{s.adventure.phaseStart}</button>
subtitle: `${s.adventure.phaseLabel(n)} · ${s.languages[langCode]}`
```

Arquivos de strings:
- `src/constants/strings.ts` — PT_STRINGS + EN_STRINGS, exporta `AppStrings`
- `src/contexts/StringsContext.tsx` — `useStrings()` hook

Ao adicionar qualquer texto novo, adicionar em **ambos** PT_STRINGS e EN_STRINGS antes de usar no componente.

---

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

**Meta operacional de equivalencia:** por idioma/temporada A1 T1, manter 25 fases de aventura, 6 secoes por fase, 25 StudyDays ativos, 5 modulos de estudo, 8 cenarios e 12 frases por StudyDay. O total bruto de steps da aventura nao precisa ser identico entre idiomas, mas deve ficar na mesma ordem de grandeza; diferencas grandes precisam ser justificadas por conteudo real, nao por seed inflado ou estudo raso.

### Estudo x Aventura - regra canonica de produto

Estudo e Aventura sao dois modulos separados do mesmo aprendizado. Eles nao devem ser misturados como a mesma tela, o mesmo fluxo ou o mesmo modelo de progresso, mas precisam andar alinhados em idioma, nivel, temporada, vocabulario, cenarios e peso didatico.

| Modulo | Regra de acesso | Papel |
|--------|-----------------|-------|
| Aventura | Progressiva e bloqueada. O usuario precisa passar pelas fases/secoes para avancar no mapa. | Experiencia RPG, historia, recompensa, mochila, personagens e gates de fase. |
| Estudo | Livre. O usuario pode abrir o estudo guiado, cenarios e pratica sem depender de estar na mesma fase da aventura. | Reforco didatico, pratica direta, revisao, explicacao e consolidacao do mesmo conteudo. |

**Regra de alinhamento:** cada fase da aventura deve ter uma contraparte clara no estudo. O estudo pode ser mais livre e mais explicativo, mas nao pode ser mais fraco, solto ou desalinhado. Se a aventura F3 trabalha lugares/direcoes, o estudo correspondente tambem deve trabalhar lugares/direcoes com vocabulario, frases, exercicios e explicacao em peso equivalente.

**Seeds:** ao criar ou alterar seeds de idioma, manter Aventura e Estudo com o mesmo peso de conteudo e didatica. Aventura pode distribuir conteudo em narrativa, secoes e gates; Estudo deve transformar esse mesmo nucleo em modulos, cenarios, lessons, StudyDays, frases, explicacoes, notas e pratica. Nunca criar uma aventura completa para um idioma e deixar o estudo raso, incompleto ou sem correspondencia.

**Progresso do usuario:** a Aventura controla desbloqueio por `AdventureProgress`, `AdventurePhaseCompletion` e `AdventureSectionProgress`. O Estudo controla conclusao por `StudyDayCompletion`, `Goal.completed_lessons` e revisao/SRS. O progresso e separado, mas o ritmo pedagogico precisa apontar para o mesmo caminho de aprendizado.

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
              └── SEÇÃO  (6 por fase — steps variáveis por seção, total ~50/fase)
```

### ⚠️ REGRA ABSOLUTAMENTE CRÍTICA — SÉRIE = CEFR

**SÉRIE = nível CEFR. Toda série tem exatamente 5 temporadas (T1–T5).**

As 5 temporadas de uma série **NÃO representam níveis CEFR diferentes**. Elas aprofundam o **mesmo nível CEFR** progressivamente. Quem conclui as 5 temporadas do A1 **sai no A1**.

```
SÉRIE A1  →  T1 · T2 · T3 · T4 · T5   ← todas A1, mesmo nível (~65h)
SÉRIE A2  →  T1 · T2 · T3 · T4 · T5   ← todas A2, outra história
SÉRIE B1  →  T1 · T2 · T3 · T4 · T5   ← todas B1, outra história
SÉRIE B2  →  T1 · T2 · T3 · T4 · T5   ← todas B2, outra história
SÉRIE C1  →  T1 · T2 · T3 · T4 · T5   ← todas C1, outra história
```

**Nunca quebrar:**
- Badge de temporada = sempre **T1/T2/T3/T4/T5** — jamais A1/A2/B1/B2/C1
- Slug de temporada = sempre prefixado pela série: `it-a1-*` para todas as temporadas do A1 italiano
- O label "A1" aparece no header da série — nunca repetido por temporada
- MVP: SÉRIE A1 italiano = "Il Viandante" (T1 Borgo · T2 Venezia · T3 Toscana · T4 Napoli · T5 Roma)

### Seções — modelo definitivo de produto

**Frontend é um renderer estático. Backend define o conteúdo.**
O frontend nunca muda — ele apenas renderiza o que o backend (hoje: mocks) fornece. Adicionar uma nova fase, temporada ou idioma = mudar o seed, nunca o código do componente.

**Separação obrigatória de responsabilidades:**

| Componente | Responsabilidade |
|-----------|-----------------|
| `AdventurePhaseRunner` | Gerencia o fluxo das 6 seções de uma fase + tela de conclusão. Importa dados de `src/mocks/phaseContentMock.ts` via `PHASE_SECTIONS_MAP[phaseNumber]`. Passa uma seção por vez ao renderer. |
| `AdventureChapterSections` | Renderiza **uma única seção**, step a step. Não conhece as outras seções. Recebe `section`, `sectionNumber`, `totalSections`, `phaseNumber`, `onComplete`, `onBack`. |

**Regra de conteúdo — nunca quebrar:**
- Nenhum texto de história, fala de NPC, narrativa ou vocab pode estar hardcoded no componente.
- Todo conteúdo vem de dados. O renderer é genérico — seu código não muda quando o conteúdo muda.

---

### As 6 seções — modelo definitivo de produto

Os nomes internos das seções são **arquitetura de backend — nunca visíveis ao jogador**.

**Cada step = 1 tela/atividade** (uma pergunta, um bloco narrativo, uma lista de vocab). Número de steps por seção é variável — determinado pelo conteúdo, não fixo. Mínimo 3 exercícios por seção em qualquer fase.

| # | Tipo interno (`type`) | Perfil | Exercícios | Tipo de conteúdo |
|---|---|---|---|---|
| 1 | `cotidiano` | Imersão narrativa + prática leve | 4 | Beats acumulados (scene/npc/player) → 4 exercícios de reconhecimento |
| 2 | `revisao_srs` | Revisão SRS — fase(s) anterior(es) | 12 | Exercícios dinâmicos do algoritmo SRS |
| 3 | `pratica` | Prática intensa do vocab novo | 10 | Exercícios variados usando o vocab praticado |
| 4 | `gramatica_narrativa` | NPC ensina gramática via história | 8 | Narrativa → NPC apresenta padrão → 8 exercícios |
| 5 | `reforco` | Pattern card + reforço explícito | 6 | Pattern card → NPC demonstra → 6 exercícios focados no padrão |
| 6 | `obstaculo` | Gate final — produção ativa | 10 gated | Cena → NPC desafia → 10 exercícios travados (errar trava) |
| | **Total por fase** | | **50** | |

**Fluxo pedagógico (por que essa ordem):**
- Seção 1: ouvir o vocab **em contexto** sem entender ainda — imersão intencional
- Seção 2: revisar o que veio **antes** — SRS mantém retenção de longo prazo
- Seção 3: narrativa avança + praticar o vocab **recém-aprendido** em uso
- Seções 4–5: apresentar e reforçar a **gramática** nova via personagem
- Seção 6: usar **tudo junto** sob pressão — o único gate real da fase

**Regra especial — primeira fase de cada temporada:**
A seção 2 (`revisao_srs`) não tem histórico anterior. Nesse caso ela vira aquecimento contextual (apresentação do cenário, vocabulário de sobrevivência do novo arco). O backend pode sinalizar com `is_first_of_season: true` na fase.

---

### Step types — contrato frontend/backend

**Cada step = 1 tela.** O frontend renderiza qualquer combinação válida. O backend só precisa enviar steps válidos — o renderer não muda quando o conteúdo muda.

```ts
type SectionStep =
  | { kind: "narrative";       text: string }
  | { kind: "scene";           text: string }
  | { kind: "npc_speak";       npc: string; line: string; translation?: string }
  | { kind: "player_react";    text: string }
  | { kind: "reveal";          phrase: string; meaning: string; note?: string }
  | { kind: "pattern";         parts: PatternPart[]; example: string; translation: string; note: string }
  | { kind: "vocab_list";      items: Array<{ target: string; native: string }> }
  | { kind: "multiple_choice"; question: string; options: Option[]; correct: string; explanation?: string }
  | { kind: "fill_blank";      prompt: string; answer: string }
  | { kind: "translate";       source: string; answer: string };
```

---

### Regras de comportamento — nunca quebrar

**Seção 1 — cotidiano acumulado:**
- Beats narrativos (`scene`, `narrative`, `npc_speak`, `player_react`) renderizam em modo chat acumulado.
- `scene` e `narrative` aparecem automaticamente (sem tap). Botão Continuar só em `npc_speak` e `player_react`.
- Falas do NPC **sem tradução** — imersão intencional, o player não entende ainda.
- Após os beats, os exercícios da seção aparecem um a um (step normal).

**Todas as seções com steps:**
- Um step por vez, foco total em cada tela.
- `canContinue` por tipo:
  - `fill_blank` / `translate`: só após revelar a resposta
  - `multiple_choice` em `obstaculo`: só com resposta **correta** (gated — trava até acertar)
  - `multiple_choice` em outras seções: qualquer resposta avança (mostra certo/errado + explicação)
  - Demais tipos (`narrative`, `npc_speak`, `vocab_list`, etc.): sempre liberado

**Seção 6 (`obstaculo`) é o único gate real:**
- Errar trava. O player deve acertar para passar.
- Todas as outras seções ensinam com feedback — errar não impede progressão.
- Completar o Obstáculo = fase concluída = recompensa desbloqueada (loot pool da temporada).

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

**Tema dual — dark / light:**

O modo aventura suporta dois temas por idioma. O toggle sun/moon vive em `AdventureMapScreen` como estado local (`themeMode: "dark" | "light"`).

- `getAdventureColors(langCode, mode?)` — segundo parâmetro opcional, padrão `"dark"`
- `adventureColors.ts` exporta `AdventureThemeMode = "dark" | "light"`
- Estrutura interna: `ADVENTURE_COLORS[lang].dark` e `ADVENTURE_COLORS[lang].light`
- Tokens neutros em `AdventureColorTokens` (evitar rgba hardcoded nos componentes):
  | Token | Dark | Light |
  |-------|------|-------|
  | `surface` | rgba(255,255,255,0.08) | rgba(0,0,0,0.04) |
  | `surfaceMid` | rgba(0,0,0,0.35) | rgba(0,0,0,0.06) |
  | `textOnBg` | rgba(255,255,255,0.70) | rgba(0,0,0,0.60) |
  | `textFaint` | rgba(255,255,255,0.18) | rgba(0,0,0,0.28) |
  | `borderFaint` | rgba(255,255,255,0.06) | rgba(0,0,0,0.08) |

**Roadmap planejado:** adicionar `time_of_day: "dawn" | "day" | "dusk" | "night"` em `AdventurePhase` e derivar o modo automaticamente a partir da fase — por enquanto o toggle é manual.

**Regra:** nunca usar `rgba(255,255,255,...)` ou `rgba(0,0,0,...)` hardcoded em componentes de aventura. Usar sempre os tokens acima.

**Arquivos-chave do modo aventura:**
| Arquivo | Responsabilidade |
|---------|-----------------|
| `src/types/adventure.ts` | `AdventureChapter`, `AdventurePhase`, `PhaseType` |
| `src/mocks/adventureItMock.ts` | Dados mock do "Il Viandante" (substituir por API no futuro) |
| `src/theme/adventureColors.ts` | Paleta dark+light por idioma (`getAdventureColors(lang, mode?)`) |
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
