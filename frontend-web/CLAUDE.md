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

### ⚠️ REGRA ABSOLUTAMENTE CRÍTICA — SÉRIE = CEFR

**SÉRIE = nível CEFR. Toda série tem exatamente 5 temporadas (T1–T5).**

As 5 temporadas de uma série **NÃO representam níveis CEFR diferentes**. Elas aprofundam o **mesmo nível CEFR** progressivamente. Quem conclui as 5 temporadas do A1 **sai no A1**.

```
SÉRIE A1  →  T1 · T2 · T3 · T4 · T5   ← todas A1, mesmo nível (~65h)
SÉRIE A2  →  T1 · T2 · T3 · T4 · T5   ← todas A2, outra história
SÉRIE B1  →  T1 · T2 · T3 · T4 · T5   ← todas B1, outra história
```

- Badge de temporada = sempre **T1/T2/T3/T4/T5** — jamais A1/A2/B1/B2/C1
- Slug de temporada = sempre prefixado pela série: `it-a1-*` para TODAS as 5 temporadas do A1 italiano
- O label CEFR ("A1") aparece no header da série — nunca por temporada

---

```
SÉRIE  (nível CEFR — ex: A1)
  └── TEMPORADA  (5 por série — badge T1…T5)
        └── FASE  (25 por temporada — types: story | review | boss)
              └── SEÇÃO  (6 por fase — cada seção = 1 visita ao mapa)
                    1. narrativa          →  5 exercícios
                    2. revisao_srs        → 12 exercícios
                    3. gramatica_narrativa →  8 exercícios
                    4. pratica_aplicada   → 10 exercícios
                    5. reforco            →  6 exercícios
                    6. obstaculo          → 10 exercícios gated
                    Total: 51 exercícios por fase
```

**Regras fixas:**
- `"A1"` = SÉRIE inteira (5 temporadas). Não é nível de temporada.
- Badges por temporada: **T1, T2, T3, T4, T5** — nunca A1/A2/B1.
- Fases 1–14 = história, 15/20 = revisão, 21–23 = checkpoints SRS, 24 = pré-boss, 25 = boss.
- Cada seção = 1 visita ao mapa. Completar → voltar ao mapa → anel SVG preenche 1/6.
- Número de steps por seção é variável (determinado pelo conteúdo). Cada step = 1 tela.
- Seção 2 da primeira fase de cada temporada: sem histórico SRS → aquecimento contextual.

**O chat conversacional é o fio condutor de todas as 6 seções — regra inviolável:**

O NPC está sempre presente, sempre falando dentro da história. Não existem "exercícios soltos" — cada pergunta é o NPC conduzindo uma situação real. A diferença entre as seções é só o balanço entre beats narrativos e exercícios, nunca a ausência do personagem.

| Seção | Propósito | Balanço |
|-------|-----------|---------|
| **1 · narrativa** | Imersão — vocab novo aparece sem explicação | Muitos beats, poucos exercícios. Na Fase 1 de cada temporada: pura introdução |
| **2 · revisao_srs** | Narrativa avança + pratica vocab da **fase anterior** (SRS disfarçado de conversa) | Menos beats, mais exercícios — NPC conduz cada um |
| **3 · gramatica_narrativa** | NPC ensina o conteúdo novo **explicitamente** dentro da história | Beats explicativos intercalados com exercícios |
| **4 · pratica_aplicada** | Prática intensa — poucos beats, NPC presente em cada exercício | Quase sem beats, exercícios são a conversa |
| **5 · reforco** | História usa o que foi ensinado na Seção 3 — mais orgânico, menos "aula" | Beats + exercícios, o vocab novo vive na narrativa |
| **6 · obstaculo** | Fechamento do arco da fase — narrativa forte + gate | Beats de conclusão + exercícios mistos (novo > revisão) |

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
| `c.textFaint` | rgba(255,255,255,0.52) | rgba(0,0,0,0.50) |
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

## Seções — arquitetura e regras críticas

**Separação obrigatória de responsabilidades:**

| Componente | Responsabilidade |
|-----------|-----------------|
| `AdventurePhaseRunner` | Gerencia o fluxo das 6 seções de uma fase + tela de fase completa. **Contém os dados de conteúdo** (mock ou futuro: API). Passa uma seção por vez para o renderer. |
| `AdventureChapterSections` | Renderiza **uma única seção** com seus steps internos. **Não sabe nada sobre as outras seções.** Recebe `section`, `sectionNumber`, `totalSections`, `phaseNumber`, `onComplete`, `onBack`. |

**Regra de conteúdo — nunca quebrar:**
- Nenhum texto de história, fala de NPC, narrativa ou vocab pode estar hardcoded no código do componente.
- Todo conteúdo vem de dados: hoje `PHASE_1_SECTIONS` em `AdventurePhaseRunner`, futuramente da API.
- `AdventureChapterSections` é um renderer genérico — seu código não muda quando o conteúdo muda.

**Comportamento do botão Continuar:**
- Seção 1 (`narrativa`): beats `scene`/`narrative` aparecem automaticamente. Botão só em `npc_speak`/`player_react`. Após os beats, exercícios aparecem um a um (step normal).
- Todas as seções com steps: um step por vez. `canContinue` por tipo:
  - `fill_blank` / `translate`: só após revelar
  - `multiple_choice` em `obstaculo`: só resposta correta (gated — trava)
  - `multiple_choice` em outras seções: qualquer resposta avança (mostra feedback)
  - Demais (`narrative`, `npc_speak`, `pattern`, etc.): sempre liberado
- Número de steps por seção é variável — não fixo.
- Errar fora do `obstaculo` não bloqueia — os erros são acumulados e voltam na próxima revisão SRS.

**Seção Cotidiano — regras específicas:**
- É uma história guiada beat a beat: cena → narrativa → diálogos → reações do jogador.
- Beats `scene` e `narrative` do início aparecem automaticamente (sem Continue button) — são contexto, não diálogo.
- O Continue button só aparece em beats `npc` e `player` (e no último beat).
- Falas do NPC aparecem **sem tradução** — o jogador não entende o idioma, e isso é intencional.
- Bolhas do NPC: avatar + balão à esquerda. Reações do jogador: balão à direita com avatar "Eu".
- A história do Cotidiano sempre deve ser contextualmente coerente (ex: Fase 1 começa dentro do vilarejo, logo após entrar pelo portão da cinemática de abertura).

**`AdventureChapterScreen` (mobile) e `AdventureModule` (desktop) ambos usam `AdventurePhaseRunner`:**
- Mobile: `navigateImmersive` → `/aventura/capitulo/:id` → `AdventureChapterScreen` → `AdventurePhaseRunner`
- Desktop: `setChapterView` inline → `AdventurePhaseRunner` no `AdventureModule`

---

## Sistema de Maestria de Palavras

Cada palavra do vocabulário tem um **tier de maestria** por usuário. O tier determina o tipo de exercício — mais difícil conforme o player avança.

### Tiers

| Tier | Exercício | Como subir |
|------|-----------|-----------|
| 🟤 Bronze | Múltipla escolha — 4 opções | 3 acertos corretos |
| ⚪ Prata | Múltipla escolha — distratores difíceis | 5 acertos corretos |
| 🟡 Ouro | Múltipla escolha — sem contexto extra na pergunta | 5 acertos corretos |
| 💎 Diamante | `write_word` — escrever a palavra do zero | 5 vezes seguidas |
| 💚 Esmeralda | Maestria confirmada — exercício Diamante permanente | — |

Errar **não baixa** o tier — reinicia apenas o streak de acertos do tier atual.

### Como o tier flui durante as seções

- **Seção 1 (`narrativa`):** exercícios de compreensão contextual — sem tier, pois o player ainda não conhece as palavras
- **Seção 2 (`revisao_srs`):** principal responsável por surfaçar palavras no tier atual de cada usuário
- **Seções 3–5:** palavras revisitadas — ao acertar, o streak do tier avança
- **Seção 6 (`obstaculo`):** exige Ouro+ — quem ainda está em Bronze/Prata recebe múltipla escolha difícil

### Contrato frontend / backend

O backend injeta `word_id` e `tier` em cada exercício que testa uma palavra específica. O renderer usa `tier` para decidir o tipo de UI:

```ts
// Exercício de vocabulário (tem word_id + tier):
{ kind: "multiple_choice", word_id: "it_ciao", tier: "bronze", ... }
{ kind: "write_word",       word_id: "it_ciao", tier: "diamante", ... }

// Exercício de gramática ou dedução contextual (sem word_id):
{ kind: "multiple_choice", question: "O que 'mi' indica nessa frase?", ... }
```

### Padrão de `word_id`

`{lang_code}_{palavra_base}` — tudo minúsculo, sem espaços:

| Palavra | word_id |
|---------|---------|
| ciao | `it_ciao` |
| buongiorno | `it_buongiorno` |
| come stai? | `it_come_stai` |
| bene | `it_bene` |
| grazie | `it_grazie` |
| forestiero | `it_forestiero` |
| contadino | `it_contadino` |
| mi chiamo | `it_mi_chiamo` |
| amico | `it_amico` |
| piacere | `it_piacere` |
| benvenuto | `it_benvenuto` |

### No mock

- Todas as palavras da Fase 1 começam em `tier: "bronze"` — primeira exposição
- Exercícios de gramática e dedução contextual não levam `word_id`
- Backend (futuro): tabela `word_mastery` — `user_id | word_id | tier | streak | last_seen_at`

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

## Diretrizes de conteúdo narrativo (mocks / aventura)

O Talkly é mais série do que livro. Cada beat ou step precisa ganhar seu lugar — se a informação já está no diálogo, no emoji da cena ou no contexto do exercício, o narrador não repete.

### Ciclo base — completo por si só

```
scene (emoji + lugar + horário)  →  NPC fala  →  player reage  →  exercício reforça
```

Narrativas de contexto são reserva, não regra. Máximo de 1–2 por seção, apenas quando o diálogo sozinho não fecha o ambiente.

### O que cortar sempre

| Tipo | Exemplo ruim | Por quê cortar |
|------|-------------|----------------|
| Narrativa que antecipa o NPC | "Ele claramente quer saber o que aconteceu." → NPC: "¿Cómo te fue?" | O NPC já diz |
| Narrativa que traduz o gesto | "Campesino. A palavra e o gesto se fundem." | O gesto + exercício já ensinam |
| Narrativa que resume o que aconteceu | "E assim você aprendeu cinco palavras." | O vocab_list já mostra |
| Editorial que descreve emoção óbvia | "Ela sorri com um olhar de quem vai ensinar algo." | O leitor vê pelo diálogo |
| Fechamento de cena literário | "Você se senta. Não sabe muita coisa. Mas sabe que prometeu." | O NPC fecha a cena |

### Sistema de língua por personagem — regra crítica de conteúdo

Cada NPC tem uma relação diferente com a língua do player. Isso define como suas falas e `npc_reaction` devem ser escritas.

**Espanhol (ES) — Aventura A1:**

| Personagem | Língua com o player | Como escrever falas/reações |
|-----------|--------------------|-----------------------------|
| **Don Miguel el Campesino** | Entende português, fala pouco — guia/ponte | `npc_reaction` em **português quebrado**: exclamações em espanhol ("¡Bien!", "¡Exacto!") + explicação em PT ("quem vem de fora. Como você.") |
| **Rosa la Panadera** | Só espanhol — paciente, simples | `npc_reaction` em **espanhol** — o player aprende pelo contexto |
| **Señora Carmen** | Só espanhol — culta, direta | `npc_reaction` em **espanhol** |
| **El Vigilante del Mercado** | Só espanhol — seco, formal | `npc_reaction` em **espanhol** |

**Por quê isso importa:**
Se o idioma fosse russo e todas as reações fossem em russo, o player não entenderia nada. Miguel é o único que tenta falar a língua do player — e é essa limitação que o torna humano e interessante. Os outros NPCs são imersivos justamente porque o player tem que se virar.

**Regra para novos NPCs:**
Ao criar um NPC, definir explicitamente: fala só na língua-alvo, ou tem algum vínculo com a língua nativa do player? Documentar no comentário da seção do mock.

### Player react — curto e concreto

`player_react` e `player` beats: máximo 2 linhas. Descrevem ação ou sensação física — não interpretam emoção.

```
// ❌
"Você para, surpreso. Ele acabou de falar na sua língua — com sotaque pesado, mas na sua língua. Você o olha com um misto de alívio e estranheza."

// ✅
"Você para. Ele está falando na sua língua.\n\n— Com sotaque pesado. Mas na sua língua."
```

### Narrativa de abertura de seção

1 linha de ação/ambiente, não mais.

```
// ❌  "Miguel se levanta e faz um gesto largo — vamos andar. Ele vai na sua frente, apresentando o pueblo um passo de cada vez. Desta vez, é você que tem que usar as palavras."
// ✅  "Miguel faz um gesto — vamos andar."
```

---

## Contexto do projeto

- App: **Talkly** — aprender idiomas vivendo histórias
- Modo Estudo: flashcards guiados por tema (UI clara, tema teal)
- Modo Aventura: RPG imersivo por idioma (UI dark/RPG, cores por cultura)
- Backend: Django + DRF + JWT (em `../backend/`) — **não tocar nesta instância**
- Mock data em `src/mocks/` substitui API enquanto backend não está conectado
