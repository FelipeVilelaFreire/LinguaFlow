# Briefing — Melhorias no Seed ES A1 (Fase 1)

> Este documento é um briefing para um novo agente Claude trabalhar nas melhorias
> do seed de conteúdo da Fase 1 Espanhol A1 do Talkly.
> Leia todos os documentos listados antes de tocar em qualquer arquivo.

---

## 1. Leia primeiro — documentos canônicos

Estes arquivos são a fonte de verdade. Qualquer decisão narrativa ou pedagógica
deve ser consistente com eles:

| Arquivo | O que contém |
|---------|-------------|
| `CLAUDE.md` | Regras do projeto, arquitetura, padrões obrigatórios |
| `docs/content/es-a1/story.md` | Bíblia narrativa — lore, arco das 5 temporadas, personagens universais |
| `docs/content/es-a1/characters.md` | Perfis completos de todos os personagens — **leia com atenção o Miguel** |
| `docs/content/es-a1/inventory-system.md` | Sistema de Mochila, itens, word→item |

---

## 2. Contexto da sessão anterior — o que foi decidido

### Miguel foi atualizado (docs/content/es-a1/characters.md já reflete isso)

O personagem Don Miguel el Campesino teve seu perfil alterado nesta sessão:

- **Idade:** 29 → **20 anos** (mesma idade do protagonista)
- **Papel:** deixou de ser "campesino experiente que guia" e virou **melhor amigo**
- **Personalidade nova:** irreverente, fala antes de pensar, conecta rápido, leal sem cerimônia
- **A amizade nasce na F1 e dura 5 temporadas** — não se conheciam antes (protagonista não tem memória)
- **Voz nas falas:** português quebrado + exclamações em espanhol, energia de jovem de 20 anos, não de tutor

O seed ainda usa a voz antiga (Miguel sábio/guia). **Precisa ser reescrito.**

---

## 3. Regra crítica da F1 — distribuição de exercícios diferente

A Fase 1 de cada temporada tem um ritmo diferente das fases normais.
**Máximo ~25 exercícios, concentrados nas seções finais:**

| Seção | Exercícios | Caráter |
|-------|-----------|---------|
| S1 · cotidiano | ~2 | Quase só narrativa — o jogador observa |
| S2 · aquecimento | ~3 | Sem SRS → apresentação de cenário e vocab de sobrevivência |
| S3 · pratica | ~5 | Prática leve — metade do volume normal |
| S4 · gramatica_narrativa | ~5 | Encontro com NPC novo + explicação das palavras |
| S5 · reforco | ~5 | Convivência — vocab em uso natural |
| S6 · obstaculo | ~5 | Gate final gated — mais curto que fases normais |
| **Total** | **~25** | Fases normais têm 33–40 |

O seed atual **não respeita essa distribuição** — tem exercícios demais nas seções
iniciais e narrativa de menos. O objetivo desta reescrita é corrigir isso.

---

## 4. Os 5 tópicos de melhoria do seed

### Tópico 4 + 6 — Reescrever a voz do Miguel e a barreira de idioma (PRIORIDADE)

**Problema:** Miguel fala espanhol mas o jogador "entende" tudo desde o início. A
imersão intencional da Seção 1 — onde o jogador genuinamente não entende nada —
está fraca. Além disso, a voz do Miguel reflete o perfil antigo (29 anos, sábio).

**O que fazer:**
- Reescrever os primeiros beats da S1 com Miguel falando espanhol sem tradução
- A virada narrativa: ele tenta espanhol → não funciona → lembra que o avô falava
  diferente → muda para português quebrado. Isso é o momento de conexão.
- Falas e `npc_reaction` do Miguel devem refletir o novo perfil: curtas, diretas,
  com energia de 20 anos. Menos "Don Miguel clareia a garganta e explica...",
  mais "Miguel ri. — É assim, ó."
- Manter o português quebrado: exclamações em espanhol ("¡Exacto!", "¡Bien!") +
  explicações truncadas em PT

**Exemplo do contraste:**
```
// ❌ Voz antiga
npc_reaction: "Correto. 'Buenos días' é a saudação da manhã em espanhol."

// ✅ Voz nova
npc_reaction: "¡Eso! Buenos días — é de manhã, fala isso."
```

---

### Tópico 5 — Palavras testadas sem apresentação prévia

**Problema:** o seed pergunta exercícios com "gracias", "buenas tardes", "forastero"
sem nunca ter mostrado o significado antes. O jogador não tem como saber.

**Regra obrigatória do CLAUDE.md (padrão conversacional):**
Todo exercício é um turno de diálogo. O NPC sempre introduz a situação antes.
Padrão:
```
npc_speak → NPC fala dentro de uma situação real (com tradução)
multiple_choice → jogador responde, NPC reage
```

**O que fazer:**
- Para cada palavra nova testada num `multiple_choice`, garantir que existe um
  `npc_speak` ou `reveal` anterior mostrando o significado em contexto
- Não precisa ser uma aula — pode ser Miguel usando a palavra numa situação
  onde o significado fica óbvio pelo contexto + tradução no campo `translation`

**Exemplo:**
```python
# Antes de testar "gracias":
{ "kind": "npc_speak", "npc": "Miguel",
  "line": "Rosa te deu pão de graça. Fala 'gracias' pra ela.",
  "translation": "gracias = obrigado" },
{ "kind": "multiple_choice", "npc": "Miguel",
  "question": "Rosa acabou de te dar o pão. Você diz:",
  "options": [...], "correct": "a", "word_id": "es_gracias",
  "npc_reaction": "¡Eso! Básico. Ela vai gostar." }
```

---

### Tópico 2 — Badge "Novo personagem" não aparece

**Problema:** o frontend tem toda a lógica pronta — quando um `npc_speak` step tem
`"is_new_npc": true`, aparece o badge "✦ Novo personagem" sobre a fala.
Mas o seed não passa esse campo em nenhum step — então nunca aparece.

**O que fazer:**
- Adicionar `"is_new_npc": True` no primeiro `npc_speak` de cada NPC que aparece
  pela primeira vez na fase
- Na F1: Miguel (S1), Rosa la Panadera (S2)
- Verificar se o serializer do backend já passa `is_new_npc` — se não passar,
  precisa adicionar

**Arquivos relevantes:**
- `backend/apps/adventure/management/commands/seed_es_sections.py` — seed da F1
- `backend/apps/adventure/serializers.py` — verificar se `is_new_npc` é serializado

---

### Tópico 3 — Badge "+1 palavra" não aparece

**Problema:** o frontend dispara o badge `+1` quando:
1. A seção tem um step `vocab_list`
2. O exercício tem `word_id`
3. O `word_id` ainda não foi acertado antes

A Seção 1 não tem `vocab_list` — então o badge nunca dispara em nenhuma seção.

**O que fazer:**
- Adicionar um step `vocab_list` na S1, após os beats narrativos iniciais e antes
  dos exercícios. Ele lista as palavras que acabaram de aparecer na narrativa.
- Formato:
```python
{ "kind": "vocab_list",
  "items": [
    { "target": "hola",        "native": "olá" },
    { "target": "forastero",   "native": "estrangeiro" },
    { "target": "me llamo",    "native": "meu nome é" },
    { "target": "buenos días", "native": "bom dia" },
  ]
}
```
- Verificar se as S2–S6 também precisam de `vocab_list` para as palavras que
  introduzem

---

## 4. Arquivos do seed para modificar

```
backend/
  apps/
    adventure/
      management/
        commands/
          seed_es_sections.py      ← F1 (6 seções) — PRINCIPAL
          seed_es_f2_sections.py   ← F2
          seed_es_f3_sections.py   ← F3
          seed_es_f4_sections.py   ← F4
          seed_es_f5_sections.py   ← F5
          seed_es_full.py          ← fases (metadados, não conteúdo)
      serializers.py               ← verificar is_new_npc
      views.py                     ← endpoints de adventure
```

O foco desta sessão é o `seed_es_sections.py` (Fase 1).

---

## 5. Estrutura de uma seção no seed — referência rápida

Cada seção segue este padrão no seed:

```python
{
    "type": "cotidiano",          # ou revisao_srs, pratica, etc.
    "characters": ["Miguel"],
    "context": { "before": "...", "now": "..." },
    "steps": [
        # Beats narrativos
        { "kind": "scene",      "text": "..." },
        { "kind": "npc_speak",  "npc": "Miguel", "line": "...", "translation": "...",
          "is_new_npc": True },  # ← só no primeiro npc_speak do NPC na fase
        { "kind": "player_react", "text": "..." },

        # vocab_list (deve existir antes dos exercícios)
        { "kind": "vocab_list", "items": [{ "target": "...", "native": "..." }] },

        # Exercícios — sempre com NPC
        { "kind": "multiple_choice",
          "npc": "Miguel",
          "question": "...",       # descreve situação, não pede definição
          "options": [{ "id": "a", "text": "..." }, ...],
          "correct": "a",
          "word_id": "es_hola",    # obrigatório para palavras de vocab
          "npc_reaction": "¡Eso!" # curto, na voz do personagem
        },
    ]
}
```

**Step types disponíveis:**
`narrative | scene | npc_speak | player_react | reveal | pattern | vocab_list |
multiple_choice | fill_blank | translate`

---

## 6. Regras críticas do CLAUDE.md que se aplicam ao seed

1. **Todo exercício é um turno de diálogo** — nunca `multiple_choice` solto sem NPC
2. **`question` descreve situação** ("Você encontra Miguel. Você diz:"), não pede
   definição ("Como se diz olá?")
3. **`npc_reaction` curto e na voz do personagem** ("¡Bien!", "Eso.", "Sigue.")
4. **Miguel fala português quebrado** — exclamações ES + explicações PT truncadas
5. **Rosa e outros NPCs falam só espanhol** — imersão, player aprende pelo contexto
6. **Seção 1** — beats narrativos aparecem sem tradução nas falas do NPC (imersão
   intencional). Tradução só no campo `translation` do `npc_speak`
7. **`word_id` obrigatório** em exercícios que testam vocabulário específico
   Formato: `es_{palavra}` ex: `es_hola`, `es_buenos_dias`, `es_gracias`

---

## 7. Como rodar o seed depois de editar

```bat
cd C:\Users\Felipe.Freire\Documents\Documentos\Sites\LinguaFlow\LinguaFlow\backend
conda activate linguaflow
python manage.py seed_es_sections
```

Para rodar tudo do zero (migrate + todos os seeds):
```bat
setup.bat
```

---

## 8. O que NÃO fazer

- Não mudar a estrutura do `AdventureChapterSections.tsx` ou outros componentes
  frontend — o renderer é genérico e não deve mudar quando o conteúdo muda
- Não criar novos step types — usar apenas os que já existem (listados acima)
- Não hardcodar texto de UI nos seeds — o seed é conteúdo narrativo, não strings
  de interface
- Não alterar `docs/content/es-a1/story.md` ou `docs/content/es-a1/characters.md` sem consultar o usuário —
  esses documentos são a fonte de verdade e mudanças têm impacto em cascata

---

*Gerado na sessão de 12/05/2026. Miguel atualizado para 20 anos nesta sessão.*
