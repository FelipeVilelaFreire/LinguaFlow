# Talkly — Game Concept

## Visão Central

O Talkly não é um app de estudo — é um **RPG completo onde o vocabulário É o mecanismo do jogo**.

O jogador não "aprende alemão". Ele é um personagem num mundo onde só sobrevive quem domina a língua. A língua fica invisível; o que aparece é a aventura.

> **Princípio:** Você só tem poder sobre algo se souber o nome em alemão. O jogo não te dá a palavra — ele te força a aprender para sobreviver.

---

## Estrutura de Progressão: Série → Temporada → Episódio

Cada nível CEFR é uma **série completa** com história própria — começo, meio e fim. Não é um "capítulo curto": é uma jornada de meses, como o Duolingo real.

```
Série A1 — Vila Medieval (~50 episódios, ~50 horas de conteúdo)
  ├── Temporada 1 — Chegada ao Vilarejo         (10 episódios)
  ├── Temporada 2 — A Guilda dos Mercadores      (10 episódios)
  ├── Temporada 3 — A Floresta das Runas         (10 episódios)
  ├── Temporada 4 — A Fortaleza do Norte         (10 episódios)
  └── Temporada 5 — O Boss Final                 (10 episódios + boss)
           ↓
      Recompensa: A Espada das Runas → carrega para A2

Série A2 — Floresta Sombria (~50 episódios)
  ├── Entra com a Espada do A1 como vantagem
  ├── Nova história, novos personagens, novo visual
  └── Boss Final → novo item para A3
```

**Volume por episódio:** ~30–40 frases, ~1 hora de conteúdo real.
**Volume por série:** ~1.500–2.000 frases por nível CEFR.
**Ritmo esperado:** 1 episódio/dia = 50 dias no A1. O jogador naturalmente fica meses em cada série.

---

## O Vocabulário Como Mecânica de Jogo

### Inventário vivo
Quando você aprende uma palavra, o objeto aparece no seu inventário.

- Aprende `Apfel` → maçã aparece no inventário → pode comer para recuperar HP
- Aprende `Wasser` → água disponível → recupera energia entre batalhas
- Aprende `Brot` → pão → sustento mais longo
- Aprende `Schwert` → espada desbloqueada como arma
- Aprende `Schild` → escudo defensivo disponível

Você não recebe o item como recompensa — você **o invoca ao dominar o nome**. Não sabe a palavra? O item não existe para você.

### Alimentação como vocabulário passivo
Entre batalhas, o personagem tem fome e sede. Você escolhe o que consumir do inventário — os itens estão em alemão. Sem exercício formal, você memoriza `Milch`, `Fleisch`, `Käse`, `Wein` naturalmente, porque a sobrevivência do personagem depende disso.

### Sistema de Poderes por Categoria Gramatical
O tipo de palavra que você aprende define o tipo de poder:

| Categoria | Exemplos | Poder desbloqueado |
|-----------|----------|--------------------|
| Verbos de ação | `laufen`, `kämpfen`, `springen` | Habilidades físicas e movimentos |
| Substantivos de natureza | `Feuer`, `Wasser`, `Stein`, `Wind` | Magias elementais |
| Cores e adjetivos | `stark`, `schnell`, `groß` | Buffs e melhorias de atributos |
| Verbos sociais | `sprechen`, `helfen`, `fragen` | Habilidades diplomáticas e de persuasão |
| Números e tempo | `jetzt`, `morgen`, `immer` | Poderes de previsão e tempo |

### Batalha com Boss
O boss ataca. Você precisa responder corretamente para defender ou atacar.
- Acertou → causa dano, avança
- Errou → perde HP
- O nível de dificuldade do boss reflete o quanto você consolidou o vocabulário da temporada
- Não dá para "furar" o boss na sorte — ele testa especificamente as palavras que você viu

---

## Mundos e Narrativa por Série

| Série | Mundo | Visual | Arco Narrativo |
|-------|-------|--------|----------------|
| A1 | Vila Medieval | Tons quentes, âmbar, épico simples | Guerreiro amnésico aprende a língua pra sobreviver. Descobre sua origem. |
| A2 | Floresta Sombria | Verde escuro, místico, névoa | Magia ligada às palavras. Criaturas que só entendem alemão puro. |
| B1 | Reino do Castelo | Roxo e dourado, grandioso | Intrigas políticas. Você vira diplomata — palavras erradas têm consequências. |
| B2 | Porto Internacional | Azul oceano, vibrante, cosmopolita | Espião/comerciante em missões. Dialetos e gírias entram em cena. |
| C1 | Ruínas Antigas | Preto e ouro, misterioso | Descobre a origem do idioma. Você virou mestre — ensina outros personagens. |

---

## Por Que Funciona Melhor Que o Duolingo

| Duolingo | Talkly |
|----------|--------|
| Você aprende uma palavra pra ganhar XP | Você aprende uma palavra pra invocar um item que te salva |
| A motivação é a streak (não perder) | A motivação é saber o que acontece na história |
| Palavras são exercícios isolados | Palavras são poderes reais no mundo do jogo |
| Você pode chutar e avançar | Boss não deixa passar sem dominar de verdade |
| Visual não muda muito | Cada série tem visual completamente diferente |

---

## Recompensas Entre Séries

A recompensa do boss final de cada série **tem papel narrativo na próxima**:

- A1 → **Espada das Runas** → em A2, corta as trevas da floresta
- A2 → **Grimório da Floresta** → em B1, permite ler documentos secretos do reino
- B1 → **Selo Real** → em B2, abre portas em portos e alfândegas
- B2 → **Mapa Estelar** → em C1, guia pelas ruínas antigas

O jogador termina A1 pra **pegar a espada e ver o que ela faz em A2**, não só pra "subir de nível".

---

## Implementação Técnica Futura

### Novo modelo de dados necessário
```
AdventureChapter (Série/Level CEFR)
  └── AdventureSeason (Temporada)
        └── AdventurePhase (Episódio, ~1h)
              └── Phrase (frase/exercício)
```

### Sistema de inventário (futuro)
- `PlayerInventory` → itens desbloqueados por palavra aprendida
- `ItemEffect` → tipo de efeito (cura, dano, buff, cosmético)
- `VocabularyLink` → palavra que invoca o item

### Sistema de atributos do personagem (futuro)
- HP (Lebenspunkte) — recuperado com comida/descanso
- Stamina — gasta em batalhas, recuperada com água
- Power — cresce com verbos de ação dominados
- Wisdom — cresce com substantivos abstratos

---

## Princípios de Design Imutáveis

1. **Vocabulário = poder** — saber a palavra te dá controle sobre o objeto/ação no jogo
2. **Não dá pra passar sem aprender** — boss testa de verdade, sem sorte
3. **A história força o vocabulário** — o jogador precisa das palavras pra avançar na narrativa
4. **Continuidade entre séries** — itens e consequências carregam entre níveis
5. **Volume real** — 50 episódios/série, 1h cada, é um jogo completo por nível CEFR
6. **Visual muda por série** — cada mundo tem paleta, tipografia e atmosfera próprias
7. **Imersão total** — o idioma é invisível; o que aparece é aventura
