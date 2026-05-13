# Talkly — Diretrizes para Claude Code

## Documentos canônicos — ler antes de qualquer trabalho narrativo

Estes dois arquivos são a fonte de verdade da série A1. Qualquer decisão sobre personagens, história, poderes, idades ou arco narrativo deve ser consultada e respeitada aqui:

| Arquivo | Conteúdo |
|---------|---------|
| `STORY_A1.md` | Bíblia narrativa completa — lore, poderes, arco das 5 temporadas, regras universais |
| `CHARACTERS_A1.md` | Perfis completos de todos os personagens — idades, especialidades, relações, arco individual |
| `INVENTORY_SYSTEM.md` | Sistema de Mochila e Baús — itens, raridades, word→item, item_moments, recuperação |

**Regras derivadas desses documentos que nunca podem ser quebradas:**
- Todo item tem um `word_id` — itens são palavras, nunca recompensas genéricas
- Itens são bônus, nunca bloqueio — o caminho sem item é sempre completável
- O step type `item_moment` é o único lugar onde itens são usados durante fases
- Palavras com erro crônico (5x+) desbloqueiam item degradado automaticamente — nunca travar o jogador
- O protagonista tem o dom naturalmente — não precisa de linhagem nobre
- O irmão mais velho ensinou as técnicas ao protagonista (não "transferiu o dom")
- María quer realizar o ritual dentro de uma janela de **3 meses** — a série inteira é esse prazo
- Catalina também é Portadora e também perdeu a memória — alvo constante de todos os antagonistas
- O grupo tem **6 companheiros**: Miguel · Sofía · María · Catalina · Rodrigo · James
- James (El Otro Forasteiro) é quem explica La Palabra Viva ao grupo — entra na T3
- María matou o irmão mais velho. O irmão mais velho está morto antes do início da história.

---

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

| # | Tipo interno (`type`) | Perfil | Exercícios (alvo) | Tipo de conteúdo |
|---|---|---|---|---|
| 1 | `cotidiano` | Imersão narrativa + prática leve | ~4 | Beats acumulados (scene/npc/player) → exercícios de reconhecimento contextual |
| 2 | `revisao_srs` | Revisão SRS — fase(s) anterior(es) | ~5-6 | NPC conduz situações, cada exercício é uma pergunta dele |
| 3 | `pratica` | Prática intensa — concentração de esforço | ~8-12 | Exercícios variados, NPC firing rapid-fire |
| 4 | `gramatica_narrativa` | NPC intro/encontro via história | ~3-4 | Narrativa-heavy, exercícios servem o encontro com o NPC |
| 5 | `reforco` | Convivência com NPC — vocab em uso orgânico | ~3-4 | Mais narrativa, NPC usa o vocab novo no contexto |
| 6 | `obstaculo` | Gate final — produção ativa | ~8-10 gated | Cena → NPC desafia → exercícios travados (errar trava) |
| | **Total por fase** | | **~33-40** | Concentrado em S3 e S6 — narrativa não fragmentada |

**Fluxo pedagógico (por que essa ordem):**
- Seção 1: ouvir o vocab **em contexto** sem entender ainda — imersão intencional
- Seção 2: revisar o que veio **antes** — SRS mantém retenção de longo prazo
- Seção 3: narrativa avança + praticar o vocab **recém-aprendido** em uso
- Seções 4–5: apresentar e reforçar a **gramática** nova via personagem
- Seção 6: usar **tudo junto** sob pressão — o único gate real da fase

---

### ⚠️ Padrão conversacional obrigatório — todo exercício é um turno de diálogo

**Regra inviolável: o NPC é o fio condutor de TODAS as seções, do começo ao fim.**

Não existe "exercício solto". Toda pergunta acontece dentro de uma situação real conduzida pelo NPC. O jogador nunca vê uma `multiple_choice` flutuando sem contexto narrativo.

**Padrão de cada exercício:**

```
npc_speak     → NPC fala dentro de uma situação real (com tradução)
multiple_choice (com `npc` + `npc_reaction`) → o jogador responde,
                NPC reage ao acerto
```

OU equivalente: a própria `multiple_choice` carrega o NPC via campos `npc` + `npc_reaction`, dispensando o `npc_speak` separado.

**O que NUNCA fazer:**

```
// ❌ NUNCA — exercício sterilizado
{ kind: "multiple_choice", question: "Como se diz 'olá' em espanhol?",
  options: [...], correct: "a" }

// ❌ NUNCA — narrative + lista de exercícios sem NPC
{ kind: "narrative", text: "Vamos praticar saudações." }
{ kind: "multiple_choice", question: "Qual é 'bom dia'?", ... }
```

**O que SEMPRE fazer:**

```
// ✅ Padrão A — npc_speak antes do exercício
{ kind: "npc_speak",
  npc: "Don Miguel",
  line: "Es la mañana. ¿Cómo saludas?",
  translation: "É de manhã. Como você cumprimenta?" }
{ kind: "multiple_choice",
  npc: "Don Miguel",
  question: "O sol acabou de subir. Você diz:",
  options: [...], correct: "a",
  word_id: "es_buenos_dias",
  npc_reaction: "Bueno. 'Buenos días' até o meio-dia." }

// ✅ Padrão B — multiple_choice carrega o NPC sozinho
{ kind: "multiple_choice",
  npc: "Don Miguel",
  question: "'Te dieron un pan. ¿Qué dices?'",
  options: [Gracias, Hola, Bien, Adiós],
  correct: "a", word_id: "es_gracias",
  npc_reaction: "Eso. Básico." }
```

**Por seção, o balanço entre beats narrativos e exercícios muda — mas o NPC nunca some.**

| Seção | Balanço |
|-------|---------|
| 1 · narrativa            | Muitos beats, poucos exercícios. Vocab aparece sem explicação |
| 2 · revisao_srs          | NPC passeia/conduz situações, cada exercício é uma pergunta dele |
| 3 · gramatica_narrativa  | NPC ensina explicitamente, intercalando beats com exercícios |
| 4 · pratica_aplicada     | Quase sem beats, NPC firing rapid-fire em cada exercício |
| 5 · reforco              | NPC demonstra o padrão completo em conversa real |
| 6 · obstaculo            | NPC vira examinador — cada exercício é um desafio dele (gated) |

**Diretriz de redação narrativa:**

- Falas do NPC em `npc_speak` curtas, com tradução
- `question` dentro de `multiple_choice` descreve a **situação**, não pede definição: "Você encontra um vizinho. Você diz:" ≠ "Como se diz olá?"
- `question` **evoca** o estado interno do jogador via sensação física/ambiente — **não declara**:
  - ❌ "Você está cansado. Don Miguel pergunta '¿Cómo estás?'"
  - ✅ "Seus pés doem, suas pálpebras pesam. Don Miguel: '¿Cómo estás?'"
  - Detalhes sensoriais (corpo, clima, objetos) > rótulo emocional ("você está triste")
- `npc_reaction` curto, na voz do personagem ("Eso.", "Bien hecho.", "Sigue.")
- Player react curto e concreto (ação física, não interpretação emocional)

---

### Phase Template — contrato narrativo de toda fase

**Toda fase é um pequeno dia/jornada com 3 atos mapeados nas 6 seções.**
Fase 1 ES ("O Despertar no Campo") é a **referência canônica** — qualquer fase nova segue esse molde.

**Estrutura em 3 atos:**

| Ato | Seções | Função |
|-----|--------|--------|
| **1. Set up** | Seção 1 (narrativa) + Seção 2 (narrativa + passeio) | Ancora lugar/hora, apresenta vocab novo sem traduzir, abre o mundo com cameo |
| **2. Intensivo + Encontro** | Seção 3 (exercícios fortes) + Seção 4 (narrativa, intro novo NPC) + Seção 5 (narrativa, convivência com novo NPC) | Prática concentrada da Seção 3, depois 2 seções narrativas pra introduzir e desenvolver um personagem novo |
| **3. Resolution** | Seção 6 (obstáculo + closing) | Gate final + closing beat narrativo que faz transição pra próxima fase |

**Distribuição de exercícios por seção (alvo):**

| Seção | Exercícios | Estilo |
|-------|-----------|--------|
| 1 (narrativa) | 4 | recognition contextual após beats |
| 2 (narrativa + passeio) | ~6 | encadeados com cameo do NPC novo |
| 3 (intensivo) | ~12-15 | concentração de prática — onde mora o "esforço" da fase |
| 4 (intro novo NPC) | 2-3 | narrativa-heavy, exercícios servem o encontro |
| 5 (convivência) | 2-3 | mais narrativa, NPC ensina algo sobre o mundo |
| 6 (obstáculo) | 10 gated | teste final + closing pra posada/transição |

Total ~40 exercícios por fase. Antes era ~50 distribuído, mas concentrar em 3 e 6 dá ritmo melhor (narrativa não fica fragmentada em mini-quizzes).

**Regra 80/20 — vocab novo vs revisão (Fase 2 em diante):**

- **20% palavras novas:** 2-3 palavras por fase, máximo. Introduzidas na Seção 1 e Seção 4 (encontro com NPC novo)
- **80% revisão:** o resto do conteúdo (Seções 2, 3, 5, 6) revisita vocab das fases anteriores em contextos novos
- Exceção: **Fase 1** introduz toda a base (~12 palavras) — é o único caso de "100% novo"

**Regras transversais — toda fase precisa ter:**

| Dimensão | Regra |
|----------|-------|
| **NPCs** | 1 NPC principal (recorrente) + ≥1 NPC cameo **nomeado** novo. NPCs de fases anteriores podem reaparecer |
| **Lugares** | ≥2 locais distintos. Seção 3 = lugar íntimo/parado. Seção 6 = lugar de limiar (porta, plaza, posada) |
| **Transição** | Toda fase termina num beat de descanso/transição. A fase seguinte abre nesse mesmo lugar (continuidade) |
| **Itens** | 2-4 itens cotidianos (`comum`), cada um amarrado a um beat. Raros/épicos só em marcos (fase 5, 10, 15, 20). Lendário só na fase 25 (boss) |
| **Vocab** | **Fase 1:** ~12 palavras novas (única exceção — base do jogo). **Fases 2+:** máximo 2-3 palavras novas (80% revisão, 20% novo). 1-3 estruturas gramaticais ensinadas na Seção 3 |
| **Arco emocional** | A fase tem um sentimento de chegada → partida. Ex: Fase 1 = "perdido → seguro" (posada como resolução) |
| **Grupo** | Os 6 companheiros (Miguel · Sofía · María · Catalina · Rodrigo · James) entram progressivamente. Verificar em `CHARACTERS_A1.md` em que fase cada um entra antes de escrever cenas de grupo |
| **Meta-história** | Verificar em `STORY_A1.md` se essa fase tem um evento do arco global (dom manifesta F6, María chega F8, janela de 3 meses começa F1, etc.) |

**Milestones do arco global por fase — nunca ignorar:**

| Fase | Evento obrigatório |
|------|--------------------|
| F1 | Protagonista chega ao pueblo. Janela de 3 meses começa. |
| F2 | Miguel entra no grupo. |
| F6 | Sofía entra no grupo. Primeiro sinal do dom — uma palavra funciona sem querer. |
| F8 | María entra no grupo. Ao tocar o protagonista, reconhece quem ele é. |
| F14 | María no cenário, observando. 3ª fase de revisão. |
| F19 | 4ª fase de revisão. Primera palavra da carta torna-se legível. |
| F25 | Boss. Dom usado com consciência pela 1ª vez. Carta: fragmento 1 revelado. |
| T2·F3 | Catalina entra no grupo. |
| T2·F6 | Rodrigo entra no grupo. |
| T3·F2 | James entra no grupo. Explica o dom ao grupo pela 1ª vez. |

**Checklist obrigatório antes de escrever conteúdo de uma fase nova:**

1. **Meta-história:** essa fase tem algum milestone do arco global? (ver tabela acima e `STORY_A1.md`)
2. **Narrativo:** que momento da história essa fase é?
3. **Pedagógico:** que vocab + gramática novos entram? (máximo 2-3 novas se não for F1)
4. **Emocional:** como o jogador começa e termina a fase?
5. **NPCs:** quem do grupo está presente? + quem é o cameo novo?
6. **Lugares:** quais 2-3 lugares aparecem?
7. **Itens:** que 2-4 itens cotidianos amarram aos beats?
8. **Transição:** como termina e onde a próxima fase começa?

Se algum dos 8 ficar em branco, a fase ainda não está pronta pra virar seed.

**Fase 1 ES — referência canônica:**

- Meta-história: F1 = chegada ao pueblo, início da janela de 3 meses. Dom adormecido, protagonista sem memória.
- Narrativo: chegada ao pueblo de San Cristóbal. Miguel ainda é NPC de vocabulário — entra no grupo na F2.
- Pedagógico: hola, buenos días, buenas tardes, gracias, de nada, ¿cómo te llamas?, me llamo, ¿cómo estás?, bien/mal, forastero, campesino (~12 palavras — única fase com 100% conteúdo novo)
- Emocional: perdido (chegada) → seguro (posada)
- NPCs: Miguel el Campesino (principal — guia, fala português quebrado) + Rosa la Panadera (cameo na Seção 2)
- Lugares: portão/parede de adobe → ruas do pueblo → casa de Rosa → plaza/posada
- Itens: pan_fresco, manzana_del_campo, agua_del_pozo, moneda_de_cobre
- Transição: termina caminhando com Miguel até la posada; próxima fase abre nesse mesmo lugar. F2 = Miguel entra no grupo.

**Regra especial — primeira fase de cada temporada (F1):**

A Fase 1 de cada temporada é fundamentalmente diferente das demais — é a fase de chegada, sem histórico e sem revisão. O ritmo é mais narrativo e menos denso em exercícios.

**Distribuição de exercícios na F1 (máximo ~25, concentrados nas seções finais):**

| Seção | Exercícios | Caráter |
|-------|-----------|---------|
| S1 · cotidiano | ~2 | Quase só narrativa — o jogador observa, não é testado ainda |
| S2 · aquecimento | ~3 | Sem SRS (sem histórico) → apresentação do cenário e vocab de sobrevivência |
| S3 · pratica | ~5 | Prática leve — metade do volume normal |
| S4 · gramatica_narrativa | ~5 | Encontro com NPC novo + explicação das palavras |
| S5 · reforco | ~5 | Convivência — vocab em uso natural |
| S6 · obstaculo | ~5 | Gate final gated — mais curto que fases normais |
| **Total** | **~25** | Fases normais têm 33–40 — F1 é mais leve intencionalmente |

**Por que menos exercícios na F1:**
- O jogador acabou de chegar — ainda está se orientando no mundo
- Não há vocab anterior para revisar (S2 vira aquecimento, não SRS)
- A narrativa e a ambientação precisam de espaço para respirar
- A pressão pedagógica aumenta progressivamente a partir da F2

**S2 na F1 = aquecimento contextual, não revisão:**
Sem histórico anterior, a S2 apresenta o cenário, os personagens e as primeiras palavras de sobrevivência de forma narrativa. O backend sinaliza com `is_first_of_season: true` na fase.

**Esta regra se aplica à F1 de toda temporada** (T1·F1, T2·F1, T3·F1, etc.), não só ao ES A1.

---

### Step types — contrato frontend/backend

**Cada step = 1 tela.** O frontend renderiza qualquer combinação válida. O backend só precisa enviar steps válidos — o renderer não muda quando o conteúdo muda.

```ts
type SectionStep =
  | { kind: "narrative";       text: string }
  | { kind: "scene";           text: string }
  | { kind: "npc_speak";       npc: string; line: string; translation?: string; pace?: "slow" | "normal" | "urgent" }
  | { kind: "player_react";    text: string }
  | { kind: "reveal";          phrase: string; meaning: string; note?: string }
  | { kind: "pattern";         parts: PatternPart[]; example: string; translation: string; note: string }
  | { kind: "vocab_list";      items: Array<{ target: string; native: string }> }
  | { kind: "multiple_choice"; question: string; options: Option[]; correct: string; explanation?: string }
  | { kind: "fill_blank";      prompt: string; answer: string }
  | { kind: "translate";       source: string; answer: string };
```

**Campo `pace` — ritmo de fala dos NPCs:**

Controla a velocidade de leitura do TTS para cada fala de NPC. O campo é opcional — omitir = `"normal"`.

| Valor | Multiplicador | Quando usar |
|-------|--------------|-------------|
| `"slow"` | ×0.72 | Personagens graves/sábios, sussurros, momentos de peso emocional (Ernesto, El Vigilante, Don Miguel em momentos sérios) |
| `"normal"` | ×1.0 | Conversas do dia a dia, instruções pedagógicas |
| `"urgent"` | ×1.35 | Exclamações, chamados à distância, situações de perigo, prática rápida ("Vamos rápido!") |

A velocidade final do TTS combina 3 fatores: `(pitch_base * speedMultiplier * paceMult)`.
- `speedMultiplier`: preferência do usuário (1× / 1.5× / 2×), padrão **1.5×**
- `paceMult`: o multiplicador de `pace` acima

O campo `pace` também existe em `NarrativaBeat` (`kind: "npc"`) na Seção 1 (narrativa acumulada).

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

**Gate de 50% por seção — regra obrigatória:**

Cada seção precisa de ≥ 50% de acertos nos exercícios para desbloquear a próxima.

```
S1 completa → score ≥ 50%  →  avança para S2
             score < 50%  →  tela de resultado + retry embaralhado

S2 → S3 → S4 → S5: mesma lógica
S6 (obstáculo): já é 100% gated por exercício — sem gate adicional
```

**Tela de retry (Opção B):**
- Mostra score: "Você acertou 2 de 5. Precisa de 3 para avançar."
- Lista cada exercício com ✓ ou ✗ e a resposta correta
- Botão [Tentar de novo] → mesmos exercícios em ordem embaralhada
- Sem limite de tentativas

**O que conta para o score:** apenas steps do tipo exercício (`multiple_choice`, `fill_blank`, `translate`). Beats narrativos (`scene`, `narrative`, `npc_speak`, `player_react`) não contam.

**Itens não são afetados pelo score** — itens são recompensa de vocabulário, não de performance.

**Seção 6 (`obstaculo`) é 100% gated por exercício:**
- Errar trava. O player deve acertar para passar.
- A S6 já garante domínio do conteúdo crítico — o gate de 50% é desnecessário aqui.
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
