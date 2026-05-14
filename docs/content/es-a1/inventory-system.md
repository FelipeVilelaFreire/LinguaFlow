# Talkly — Sistema de Mochila e Baús

> Documento canônico do sistema de inventário dinâmico do Modo Aventura.
> Toda decisão de backend, frontend e seed sobre itens deve respeitar este documento.

---

## Princípio Central

**A Mochila é o espelho do vocabulário do jogador.**

Cada item representa uma palavra que o jogador dominou. Acertar a palavra → item entra na Mochila. Errar → item fica bloqueado. A Mochila de cada jogador conta a versão deles da mesma história.

**Itens são sempre bônus — nunca bloqueio.** O caminho sem item é sempre completável. Ter itens torna a experiência mais rica, não mais fácil.

---

## As Duas Camadas de Itens

### Camada 1 — Itens da História (fixos)

Ganhos em momentos narrativos específicos. Todo jogador que passa pela cena recebe o item — mas só se tiver acertado a palavra associada. Definidos no seed da fase.

```
Fase 1 · Seção 1  →  Rosa dá pan_fresco       (word_id: es_pan)
Fase 3 · Seção 4  →  Miguel dá sombrero       (word_id: es_sombrero)
Fase 8 · Seção 2  →  María dá frasco_de_cura  (word_id: es_medicina)
```

### Camada 2 — Baús (random por usuário)

Aparecem em algumas fases — não em todas. Definido no seed se aquela fase tem baú (`has_chest: true`, `chest_tier: "raro"`). O item específico é sorteado da fila do usuário (ver modelo de shuffle abaixo).

---

## Raridades

| Tier | Frequência por Temporada | Quando aparece |
|------|------------------------|----------------|
| **Comum** | ~8 baús | A cada 2-3 fases — cotidiano |
| **Raro** | ~4 baús | A cada 5-6 fases — marcos de progressão |
| **Épico** | ~3 baús | Fases milestone (F5, F12, F20) |
| **Lendário** | ~2 baús | F8 (milestone narrativo) + Boss F25 |
| **Mítico** | ~1 baú | O momento mais especial da temporada |

**Total na série A1 completa (5 temporadas):**
```
Comum:    ~40 itens
Raro:     ~20 itens
Épico:    ~15 itens
Lendário: ~10 itens
Mítico:    ~5 itens  (1 por temporada — momento único)
```

**Mítico por temporada — ES A1:**

| T | Momento | Item mítico |
|---|---------|-------------|
| T1 | Boss F25 — primeiro uso consciente do dom | `la_primera_palabra` |
| T2 | Catalina descobre que tem o dom | `espejo_roto` |
| T3 | Protagonista + James derrotam o boss juntos | `piedra_del_pacto` |
| T4 | Grupo descobre que María sabia desde o início | `diario_de_maría` |
| T5 | Carta de Valentina abre completamente | `la_carta_de_valentina` |

---

## Modelo de Baú — "Sorte + Mérito" (estilo Clash Royale)

> **Mudança de filosofia (2026-05):** o modelo antigo ("todos chegam com tudo,
> só a ordem muda") foi substituído. Agora **dois jogadores terminam a
> temporada com mochilas diferentes** — a coleção completa é rara, não
> garantida. Quem joga bem ganha mais e melhor; mas a sorte decide *quais*.

O baú funciona em **3 camadas**:

### Camada 1 — Score da fase → TIER do baú (mérito)

A porcentagem de acerto na fase decide qual baú o jogador abre:

| Score da fase | Tier do baú |
|---------------|-------------|
| 95-100% | Lendário |
| 85-94%  | Épico |
| 70-84%  | Raro |
| 0-69%   | Comum |

### Camada 2 — Tier do baú → DROP RATE da raridade (sorte)

Cada tier de baú tem uma tabela de probabilidade. O baú **não garante** a
raridade máxima — dá uma *chance*. Até um baú comum pode soltar um raro.

| Baú \ Item | Comum | Raro | Épico | Lendário |
|------------|-------|------|-------|----------|
| **Comum**    | 75% | 22% | 3%  | 0%  |
| **Raro**     | 40% | 42% | 16% | 2%  |
| **Épico**    | 15% | 38% | 35% | 12% |
| **Lendário** | 5%  | 25% | 40% | 30% |

### Camada 3 — Raridade sorteada → ITEM elegível (mérito + sorte)

- O item é sorteado aleatoriamente da raridade que saiu, **entre os que o
  usuário ainda não tem** (sem repetição).
- **Itens raros/épicos/lendários com `word_id`** só entram no sorteio do
  usuário **se ele dominou aquela palavra** (`WordMastery` tier ≥ bronze).
  Comuns nunca filtram — jogador iniciante não pode ficar com mochila vazia.
- Se a raridade sorteada estiver esgotada pro usuário, **desce um nível**
  (lendário → épico → raro → comum).

### Resultado

O **pool é grande** (~46 itens na T1, contra 15 baús). Cada usuário só
sorteia uma fração. A coleção completa é conquista — não inevitabilidade.

```python
# Conceitual (backend: AdventurePhaseViewSet.open_chest)
score        = phase_completion.score
chest_tier   = score_to_tier(score)              # camada 1
rolled       = weighted_choice(DROP_RATES[chest_tier])  # camada 2
pool         = items[rolled] - owned - word_gated_locked  # camada 3
item         = random.choice(pool) or descend_rarity()
```

---

## Word → Item — A Ligação Fundamental

Cada item tem um `word_id`. O item só entra na Mochila quando o jogador acerta a palavra pela primeira vez (`tier >= bronze`).

| Estado da palavra | Estado do item |
|-------------------|---------------|
| Nunca vista | Item não aparece |
| Vista mas nunca acertada | Item aparece bloqueado 🔒 na Mochila |
| Acertada 1+ vez (Bronze) | Item disponível ✓ |
| Acertada cronicamente errada (5x+) | Item degradado desbloqueado automaticamente |

---

## Item_Moment — Uso Durante as Fases

### O step type `item_moment`

Novo tipo de step no contrato frontend/backend:

```ts
| {
    kind: "item_moment";
    npc: string;
    situation: string;        // texto narrativo da situação
    npc_line: string;         // fala do NPC pedindo/sugerindo o uso
    item_tag: string;         // tag do item necessário (não o item específico)
    on_use: {
      narrative: string;
      npc_reaction: string;
      bonus: "skip_exercise" | "extra_dialogue" | "relationship_boost" | "reduce_gated";
    };
    on_skip: {
      npc_reaction: string;   // NPC aceita e segue — sem punição
    };
  }
```

### Tags de item — matching flexível

O `item_moment` não exige um item específico. Qualquer item com a tag serve:

| Tag | Itens que ativam |
|-----|-----------------|
| `comida` | pan, manzana, tortilla, fruta_seca |
| `bebida` | agua, vino, leche |
| `arma` | navaja, espada, palo |
| `documento` | carta_sellada, mapa_rasgado, libro_cifrado |
| `moeda` | moneda_de_cobre, moneda_de_plata |
| `remedio` | frasco_de_maría, hierba_seca |

### Exemplo no seed

```python
{
    "kind": "item_moment",
    "npc": "Miguel",
    "situation": "Depois de horas caminhando, o grupo para. Miguel apoia nas joelhas.",
    "npc_line": "¿Tienes algo para comer, amigo?",
    "item_tag": "comida",
    "on_use": {
        "narrative": "Você tira o pão da mochila. Miguel parte ao meio sem perguntar.",
        "npc_reaction": "Pan fresco. No lo esperaba.",
        "bonus": "skip_exercise"
    },
    "on_skip": {
        "npc_reaction": "No importa. Seguimos."
    }
}
```

---

## Tipos de Ação por Item

| Ação | Comportamento | Exemplo |
|------|--------------|---------|
| **Usar** (consumível) | Sai da Mochila ao usar. Uso único. | Pan, Agua, Poção |
| **Equipar** (permanente) | Fica na Mochila. Usável múltiplas vezes no contexto certo. | Espada, Sombrero |
| **Entregar** (quest) | Sai ao entregar a um NPC específico. Avança subplot. | Carta selada → Valentina |
| **Examinar** (lore) | Nunca sai. Revela texto de lore ao inspecionar. | Diário de María |

---

## Sistema de Recuperação — Nunca Travar

Quando um `item_moment` ativa e o jogador não tem o item, o fluxo é:

```
item_moment "comida" aparece
        │
        ├── tem item com tag "comida"?
        │     SIM → [Usar item ✓]  →  bônus completo
        │
        └── NÃO
              │
              ├── tem item degradado com tag "comida"?
              │     SIM → [Usar versão simples 🥖]  →  bônus menor
              │
              └── NÃO
                    │
                    ├── [Tentar recuperar]  →  exercício de recuperação
                    │     Tentativa 1: múltipla escolha 4 opções
                    │     Tentativa 2: múltipla escolha com dica visual
                    │     Tentativa 3: múltipla escolha 2 opções
                    │     Acertou → item aparece + usado → bônus completo
                    │     Errou 3x → Camada NPC (abaixo)
                    │
                    └── [Continuar sem item]  →  caminho normal, sem bônus
```

### Camada NPC — fallback narrativo

Após 3 tentativas sem acertar, o NPC resolve organicamente. O jogador nunca trava:

```
Miguel revira o próprio bolso.
"No importa. Tengo algo aquí."
Ele tira um pedaço de pão velho da jaqueta.
"No es mucho. Pero sirve."
→ história continua, sem bônus, sem punição extra
```

### Item degradado — palavras com erro crônico

Se uma palavra foi errada 5+ vezes sem nunca ter sido acertada, o sistema desbloqueia automaticamente uma versão degradada do item. Funciona em `item_moments` mas com bônus menor. Some quando a palavra for finalmente dominada.

```
pan errada 5x+  →  🥖 Mendrugo Seco desbloqueado  (bônus menor)
pan tier Bronze  →  🍞 Pan Fresco desbloqueado  (Mendrugo some, Pan entra)
```

---

## Impacto no SRS — Palavras com Erro Crônico

Erros em palavras com itens associados aumentam a prioridade no algoritmo SRS:

```
word errada 1-2x  →  aparece normal na Seção 2 das próximas fases
word errada 3-4x  →  aparece no início da Seção 2, exercício mais fácil
word errada 5x+   →  aparece em múltiplas seções + item degradado desbloqueado
word acertada 3x seguidas  →  sai da lista prioritária + item pleno desbloqueado
```

---

## A Mochila — Interface

### Três estados visuais de item

```
🍞 Pan Fresco      ✓  cor viva — disponível para uso
🪙 Moneda de Cobre 🔒  cinza — viu a palavra mas ainda não acertou
                       texto: "acerte 'moneda' para desbloquear"
🥖 Mendrugo Seco   ⚠️  cor suave — versão degradada ativa
                       texto: "versão temporária até dominar 'pan'"
```

### Organização

Items organizados por fase/região onde foram encontrados. A Mochila conta a história do jogador: onde estava, o que viveu, o que carregou.

---

## Modelo de Dados — Backend

### Campos novos em `AdventureItem`

```python
word_id        = CharField  # es_pan, es_agua, etc. — liga ao vocabulário
item_tag       = CharField  # comida, bebida, arma, documento, moeda, remedio
is_degraded    = BooleanField(default=False)  # True = versão fallback
degrades_to    = FK('self', null=True)  # item pleno que substitui este
```

### Campos novos em `AdventurePhase`

```python
has_chest      = BooleanField(default=False)
chest_tier     = CharField(choices=['comum','raro','epico','lendario','mitico'], null=True)
```

### Nova tabela: `UserItemQueue`

```python
user           = FK(User)
tier           = CharField  # raro, epico, etc.
ordered_items  = JSONField  # [item_id, item_id, ...] — fila embaralhada por user_id
next_index     = IntegerField(default=0)
```

### Lógica de desbloqueio

```python
# Ao registrar resposta correta numa palavra:
def on_word_correct(user, word_id):
    item = AdventureItem.objects.filter(word_id=word_id, is_degraded=False).first()
    if item and not UserInventory.objects.filter(user=user, item=item).exists():
        UserInventory.objects.create(user=user, item=item)
        # remove item degradado se existia
        degraded = AdventureItem.objects.filter(word_id=word_id, is_degraded=True).first()
        if degraded:
            UserInventory.objects.filter(user=user, item=degraded).delete()
```

---

## Endpoints Necessários

| Método | Endpoint | Descrição |
|--------|---------|-----------|
| `POST` | `/adventure/phases/{id}/open-chest/` | Abre baú da fase — retorna próximo item da fila do usuário |
| `POST` | `/adventure/inventory/{id}/use/` | Usa item — consome se `action == "usar"` |
| `GET` | `/adventure/inventory/` | Lista Mochila do usuário com estados |
| `POST` | `/adventure/vocabulary/record/` | Já existe — dispara desbloqueio de item se acerto |
