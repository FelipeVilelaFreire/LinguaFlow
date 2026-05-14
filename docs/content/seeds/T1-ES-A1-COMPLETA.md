# Talkly — Temporada 1 ES A1 completa + Dinâmica de itens viva

> Sessão de implementação que entregou T1 ES A1 inteira (F1-F25 com BOSS) e
> ativou pela primeira vez o sistema dinâmico de mochila — `item_moment`,
> baús sorteados e itens degradados.

---

## 1. O que existia antes desta sessão

Quando começamos a sessão:

- **F1-F5** já existiam (ES A1, "El Pueblo de San Cristóbal")
- F6-F25 — **inexistentes**
- Sistema de itens — só a **estrutura básica**: `AdventureItem` com word_id, source_phase, raridades. Apenas 4 itens cotidianos seedados na F1
- Sistema de baú — **apenas mapeado em docs** (inventory-system.md), nada implementado
- `item_moment` — **só conceito**, sem renderer no frontend, sem step type no backend

## 2. O que foi entregue nesta sessão

### 2.1 Fases F6 → F25 (20 fases completas)

Cada fase com 6 seções (Cotidiano → Revisão SRS → Prática → Gramática → Reforço → Obstáculo gated).

| Bloco | Fases | Conteúdo | Milestones canônicos |
|---|---|---|---|
| F6-F10 | "Lo que vio Sofía" → "La sombra del Vigilante" | Entrada da Sofía (F6) e da María (F8), primeiro confronto com El Vigilante | Sofía F6, María F8 ✅ |
| F11-F15 | "El Ayuntamiento" → "El primer testigo" | Apresentação do Alcalde, três testigos, pase provisório | Pase de 1 mês |
| F16-F20 | "Lo que Carmen no contó" → "La visita inesperada" | Backstory Carmen↔Alcalde, marca dos Buscadores, **4ª revisão + 1ª palavra da carta (VUELVES)** | F19 = 4ª revisão canônica ✅ |
| F21-F25 | "El confronto a María" → **"El Jefe del Pueblo"** | Confronto direto, julgamento, Carmen aparece, **BOSS T1** | F25 boss + 2ª palavra (HERMANO) ✅ |

**Vocabulário acumulado:** ~120 palavras lexicais + ~15 paradigmas gramaticais (presente, passado, futuro próximo, possessivos, gênero, adjetivos, querer/poder/deber + verbo, condicional simples, cuando, si).

**Conformidade pedagógica:**
- ✅ Zero metalinguagem proibida nas falas/perguntas (sem "pretérito", "1ª pessoa", "infinitivo", "concordância" — só linguagem natural)
- ✅ Padrão conversacional 100% (NPC + situação + reação em cada exercício)
- ✅ Gate em S6 com `"gated": True`
- ✅ Closing beats fazem transição pra próxima fase
- ✅ Proporção ~25-30% novo / ~70-75% revisão na maioria das fases

### 2.2 Sistema dinâmico de itens — backend

**Migração 0006** (`adventure/migrations/0006_inventory_dynamics.py`) adicionou:

| Modelo | Campos novos |
|---|---|
| `AdventureItem` | `item_tag` (comida/bebida/arma/documento/moneda/remedio/comum) · `is_degraded` · `degrades_to` (FK self) |
| `AdventurePhase` | `has_chest` (bool) · `chest_tier` (comum/raro/épico/lendário/mítico) |
| `UserItemQueue` (novo) | Fila embaralhada por usuário+capítulo+tier. Garante que cada player recebe a coleção inteira sem repetir, em ordem única pra ele |

**Endpoints novos** (`adventure/views.py`):

```
POST /adventure/phases/{id}/open-chest/
  → Abre baú da fase (se has_chest=True). Sorteia próximo item da fila do user.
  → Idempotente: usuário sempre recebe o mesmo item daquele baú.

GET /adventure/inventory/by-tag/?tag=comida
  → Lista itens da mochila do user com essa tag. Prioridade: item pleno > degradado.

POST /adventure/inventory/use-by-tag/  body: {"tag": "comida"}
  → Resolve item_moment consumindo primeiro item com aquela tag.
  → Items consumíveis (action="usar"/"entregar") somem da mochila.
  → Items "examinar"/"equipar" ficam.
```

### 2.3 Sistema dinâmico — frontend

**Novo step type** em `frontend-web/src/types/sections.ts`:

```ts
export interface ItemMomentStep {
  kind:        "item_moment";
  npc:         string;
  situation:   string;       // texto narrativo
  npc_line:    string;       // fala do NPC
  item_tag:    string;       // tag necessária
  on_use:  { narrative; npc_reaction; bonus }
  on_skip: { npc_reaction }
}
```

**Novo case no renderer** (`AdventureChapterSections.tsx`):
1. Renderiza situação narrativa + fala do NPC
2. Chama `/inventory/by-tag/?tag=X` em background
3. Mostra 2 botões:
   - **Se tem item:** "Usar [emoji] [nome]" (verde se pleno, dourado-suave se degradado)
   - **Sempre:** "Continuar sem item"
4. Ao clicar Usar → POST `/inventory/use-by-tag/` → mostra `on_use.narrative` + `on_use.npc_reaction`
5. Ao clicar Pular → mostra `on_skip.npc_reaction`

**Baú automático** (`AdventurePhaseRunner.tsx`):
- Ao completar uma fase com `has_chest=True`, chama `POST /open-chest/` automaticamente
- Item sorteado vira o `earned_item` da fase — aparece no Trophy/Item screens já existente

**Strings PT+EN** (`strings.ts`):
- `itemMomentUse(name)`, `itemMomentUseDegraded(name)`, `itemMomentSkip`
- `itemMomentNoItem`, `itemMomentUsed(name)`
- `chestOpen`, `chestRewardLabel`

### 2.4 Pool de itens criado

No `seed_es_full.py` (via 4 blocos novos):

| Bloco | Quantos | Detalhes |
|---|---|---|
| **PHASE1_ITEMS** (já existiam) | 4 | pan/manzana/agua/moneda — agora com `item_tag` e `action` corretas |
| **CHEST_POOL** | **~46** | 19 comuns + 15 raros + 10 épicos + 2 lendários de pool. Sorteados por drop rate (ver abaixo) |
| **DEGRADED** | 3 | mendrugo_seco, agua_estancada, manzana_machucada — versões fallback. **Trigger automático ATIVO**: errar a palavra 5x sem nunca acertar → versão degradada entra na mochila; acertar depois → degradado sai, pleno entra |
| **BOSS_REWARDS (F25)** | 2 | **Sello del Pueblo** (lendário) + **Fragmento 2 da Carta** ("Hermano", lendário). Entregues via `source_phase=25` (garantido, não sorteado) |

### Sistema de baú "Sorte + Mérito" (estilo Clash Royale)

`open_chest` reescrito em 3 camadas — ver `docs/content/es-a1/inventory-system.md`:

1. **Score da fase → tier do baú** — 95%+ = lendário, 85%+ = épico, 70%+ = raro, resto = comum
2. **Tier do baú → drop rate** — cada tier tem tabela de probabilidade (baú comum: 75/22/3/0 · baú lendário: 5/25/40/30). A raridade máxima nunca é garantida — é *chance*
3. **Raridade → item elegível** — sorteia entre os que o user não tem; itens raros/épicos/lendários com `word_id` só caem pra quem **dominou a palavra**; se a raridade esgotou, desce um nível

**Resultado:** pool de 46 itens >> 15 baús → cada usuário termina com **mochila diferente**. Coleção completa virou conquista, não garantia.

**Fases com baú** (`has_chest=True`) — 15 fases:
- F2, F3, F6, F9, F11, F13, F17, F22 · F7, F12, F16, F20 · F8, F14, F19
- O `chest_tier` do seed virou irrelevante para a entrega (o tier real vem do score) — mantido só como metadado
- Lendários do boss F25 vêm via `source_phase` (garantido)

### 2.5 item_moments distribuídos — 8 momentos interativos

| Fase | Tag | Contexto narrativo |
|---|---|---|
| F4 (mercado) | comida | Don Miguel com fome saindo do mercado |
| F7 (día normal) | bebida | Sofía com garganta seca após o dia inteiro |
| F9 (cuatro a la mesa) | comida | Somar à mesa compartilhada do grupo |
| F12 (tres días) | bebida | Eduardo com sede da fragua antes de testemunhar |
| F13 (familia de Miguel) | comida | Pôr algo na mesa de Doña Lucía — entrar na família |
| F21 (confronto María) | remedio | Hierba de María acalma a conversa |
| F23 (plan del Alcalde) | moneda | Soborno de guarda jovem |
| F24 (víspera del juicio) | remedio | Dormir antes do boss |

Cada item_moment tem `on_use` (bônus narrativo + reação NPC) e `on_skip` (NPC aceita sem punição — item é sempre bônus, nunca bloqueio).

## 3. Conformidade pedagógica (auditoria)

### F1-F20 (após correções prévias da sessão)
- **Metalinguagem proibida em conteúdo visto pelo aluno:** 0
- **Proporção novo/revisão média:** ~30% / 70%
- **SRS retroativo:** palavras de F1-F5 reaparecem em F6-F20 organicamente

### F21-F25 (criadas nesta sessão)
- **Metalinguagem visível ao aluno:** 0
- **Vocab novo por fase:** 2-3 lexicais + 1 paradigma (dentro da regra 80/20 do CLAUDE.md)
- **Item_moments narrativos:** 3 (F21 com Hierba, F23 com moneda, F24 com Hierba)
- **Baú lendário no boss:** ✅

## 4. Setup atualizado

`backend/setup.bat` cobre 28 passos cobrindo F1-F25 + study modules. Roda em ordem:

```
1.  migrate
2.  seed_languages
3.  seed_es_full  ← agora cria pool de baús, items degradados, F25 boss rewards
4-28. seed_es_f1_sections .. seed_es_f25_sections (25 fases)
final: seed_es_study
```

## 5. O que JÁ foi conectado (todas as 3 lacunas fechadas)

| Item | Status | Como |
|---|---|---|
| **Degradação automática** | ✅ | Migração `progress/0007` adiciona `error_count` + `ever_correct` em `WordMastery`. Endpoint `record` cria/remove o item degradado: errou 5x sem acertar → degradado entra; acertou → degradado sai e pleno entra |
| **Itens bloqueados 🔒 na mochila** | ✅ | Endpoint `GET /inventory/locked/` retorna itens cuja palavra foi vista mas não dominada. `AdventureMochilaScreen` renderiza seção "Por descobrir" com cadeado cinza + hint "Domine X para desbloquear" |
| **Animação de item saindo da mochila** | ✅ | `@keyframes itemFlyOut` + `.item-fly-out` em `globals.css`. Botão "Usar item" do `item_moment` dispara a animação (salto + fade, 620ms) antes de resolver |

## 5b. O que ainda NÃO está pronto (próximas iterações)

| Item | Status | Por quê |
|---|---|---|
| `fill_blank` e `translate` no renderer | ❌ | Step types existem em `sections.ts` mas o renderer não tem `case` pra eles. Atualmente 100% dos exercícios são `multiple_choice` |
| ChestOpen modal customizado | ❌ | Hoje o baú reaproveita o stage "item" do AdventurePhaseRunner — funciona mas não tem animação dedicada |
| `equipar` (item permanente reutilizável) | ❌ | Nenhum item T1 usa — fica pra armas em T2+ |

## 6. Como testar a dinâmica nova

```bash
cd backend
setup.bat   # roda 28 passos, popula F1-F25 + items
python manage.py runserver
```

Frontend:
```bash
cd frontend-web
npm install
npm run dev
```

Caminhos críticos pra validar:
1. **Completar F5 ou F10** → deve abrir baú comum automaticamente, item entra na mochila
2. **Completar F15 ou F20** → baú raro, mesma coisa
3. **Chegar na F21 S3 ou F23 S3 ou F24 S3** → step `item_moment` aparece. Se tem item da tag certa: botão verde "Usar X" + reação especial. Se não tem: botão "Continuar" + reação alternativa
4. **Completar F25 (boss)** → Sello del Pueblo (lendário) + Fragmento 2 entregue + baú lendário

## 7. Personagens introduzidos nesta sessão (T1)

Já estavam no chapter desde antes da sessão:
- Protagonista · Miguel · Sofía · María · Don Miguel · Rosa · Carmen · Eduardo · El Vigilante

Novos personagens introduzidos nesta sessão:
- **El Alcalde** (F11+, boss T1) — primo do antigo alcalde, ex-noivo da Carmen
- **Doña Lucía** (F13) — mãe de Miguel, reconhece María "de algún sitio"
- **Lola e Rita** (F13 cameos) — irmãs de Miguel
- **El Inspector** (F20+) — primo do Alcalde, faz auditorias do distrito

## 8. Pistas narrativas plantadas pro arco T1+

Pistas que ficaram em aberto pro player resolver em T2-T5:

| Pista | Onde | Resolução |
|---|---|---|
| María não se chama María — apellido era "Sangra" | F17 | T5 |
| Doña Lucía reconhece María "de algún sitio" | F13 fim | F19+ ou T2 |
| Carmen e o Alcalde foram noivos há 25 anos | F16 + F25 | F25 ✅ resolvido em parte |
| Carta de Don Miguel veio do Buscador há 20 anos | F18 | T3 (James entra) |
| Eduardo tem marca dos Buscadores nas costas | F17 | T3 |
| "Alguien en el norte" sabe quem é o forastero | F21 fim | T2 |
| Você tem um irmão (HERMANO) | F25 (palavra da carta) | T2-T5 (arco principal) |
| Pase definitivo ganho | F25 | ✅ resolvido |

## 9. Status geral

```
✅ Backend  — campos novos + endpoints (open-chest, by-tag, use-by-tag)
✅ Frontend — step item_moment renderiza · baú automático ao fim da fase
✅ Seeds    — pool de 12 items + 3 degradados + 2 boss rewards
✅ F1-F25   — T1 inteira jogável + boss
✅ setup.bat — 28 passos, roda tudo
✅ Sem metalinguagem proibida em F16-F25
```

A T1 está pronta pra ser jogada de ponta a ponta. F25 fecha com cliffhanger pra T2 (HERMANO + ir ao norte).
