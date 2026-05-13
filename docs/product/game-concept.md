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

### Atributos do Personagem

```
[Nome do jogador]
──────────────────────────────────
❤️  HP (Lebenspunkte)   ████████░░  80/100
⚡  Stamina             ██████░░░░  60/100
✨  Runa                ████░░░░░░  40/100
──────────────────────────────────
Fome:  ██░░░░  (precisa comer)
Sede:  ████░░  (ok por enquanto)
```

- **HP** — cai quando você erra no boss. Recupera com comida.
- **Stamina** — cai ao longo das fases. Recupera com água e descanso.
- **Runa** — combustível dos poderes. Recupera dominando palavras novas.

---

### Sistema de Domínio — Quanto Você Sabe, Tanto Você Pode

A palavra não tem poder fixo. O poder **cresce conforme você a encontra e acerta em mais contextos**.

```
Nível 1 — Vista (apareceu na narrativa):
  Feuer  🔥        5 dano

Nível 2 — Praticada (exercícios da fase concluídos):
  Feuer  🔥🔥      12 dano

Nível 3 — Consolidada (revisada corretamente em fases posteriores):
  Feuer  🔥🔥🔥    20 dano  ← domínio máximo
```

**Por que funciona:** o jogador quer acertar os exercícios de verdade — errar não é neutro, enfraquece os poderes. E quer voltar para revisar — cada acerto em fase posterior fortalece o poder.

A consolidação acontece naturalmente pelo ritmo do jogo: a palavra aparece na narrativa nova, na seção de revisão, na conversa com NPCs recorrentes. Cada acerto = mais força.

---

### Inventário Vivo — Itens Invocados pelo Conhecimento

Você não recebe itens como recompensa. **Você os invoca ao dominar o nome.** Não sabe a palavra? O item não existe para você.

#### Comida (recupera HP, mata fome/sede)
| Palavra | Item | Efeito |
|---------|------|--------|
| Apfel | 🍎 Maçã | +10 HP, -fome |
| Brot | 🍞 Pão | +15 HP, -fome longa |
| Milch | 🥛 Leite | +10 HP, -sede |
| Wasser | 💧 Água | +stamina, -sede |
| Fleisch | 🥩 Carne | +25 HP, -fome longa |
| Ei | 🥚 Ovo | +10 HP |
| Käse | 🧀 Queijo | +10 HP, -fome |

#### Armas e Proteção
| Palavra | Item | Efeito no boss |
|---------|------|----------------|
| Messer | 🔪 Faca | +5 dano |
| Schwert | ⚔️ Espada | +15 dano |
| Schild | 🛡️ Escudo | -10 dano recebido |

#### Poderes Elementais (Runensprache)
| Palavra | Poder | Efeito (nível máximo) |
|---------|-------|----------------------|
| Feuer | 🔥 Fogo | 20 dano no boss |
| Wasser | 🌊 Água | Escudo líquido — bloqueia próximo ataque |
| Stein | 🪨 Pedra | Barreira — reduz todo dano pela metade |
| Licht | 💡 Luz | Revela fraqueza do boss |
| Dunkel | 🌑 Escuridão | Atordoa boss por 1 turno |
| Wind | 💨 Vento | Você ataca primeiro neste turno |

---

### Alimentação como Vocabulário Passivo

Entre fases, o personagem tem fome e sede. O inventário abre com os itens em alemão. Você escolhe o que consumir.

Sem exercício. Sem pressão. Em 2 semanas você memoriza `Milch`, `Apfel`, `Brot`, `Wasser` porque a sobrevivência do personagem depende disso todos os dias.

---

### Poderes por Categoria Gramatical

O tipo de palavra define o tipo de poder:

| Categoria | Exemplos | Poder |
|-----------|----------|-------|
| Substantivos de natureza | `Feuer`, `Wasser`, `Stein`, `Wind` | Magias elementais |
| Verbos de ação | `laufen`, `kämpfen`, `springen` | Habilidades físicas |
| Adjetivos | `stark`, `schnell`, `groß` | Buffs de atributo |
| Verbos sociais | `sprechen`, `helfen`, `fragen` | Habilidades diplomáticas |
| Tempo e números | `jetzt`, `morgen`, `immer` | Poderes de previsão |

---

### Verbos como Habilidades — O Sistema de Ações

Aprender um verbo não é só vocabulário. É desbloquear uma ação real no mundo do jogo.

| Verbo (DE) | Tradução | Habilidade desbloqueada |
|-----------|----------|------------------------|
| jagen | caçar | 🏹 Arco → pode caçar animais para comida |
| schwimmen | nadar | 🏊 Acesso a áreas aquáticas |
| klettern | escalar | 🧗 Acesso a áreas elevadas |
| schlafen | dormir | 🛏️ Recupera HP completo na estalagem |
| kochen | cozinhar | 🍳 Transforma comida crua em refeição melhor |
| kämpfen | lutar | ⚔️ Habilidades de combate avançadas |
| laufen | correr | 💨 Fuga de situações de perigo |
| sprechen | falar | 💬 Novas opções de diálogo com NPCs |
| fragen | perguntar | ❓ Extrai informações extras de NPCs |
| helfen | ajudar | 🤝 Soluções diplomáticas em vez de combate |
| suchen | procurar | 🔍 Encontra itens escondidos nas cenas |

**Conjugação como nível de poder:**
Não basta saber o infinitivo. Cada forma conjugada domina aumenta a habilidade:

```
jagen (infinitivo):         habilidade desbloqueada — nível básico
ich jage (presente):        uso atual, situações do dia a dia
ich jagte (passado):        referência ao que já fez — +confiança de NPCs
ich werde jagen (futuro):   planejamento — opções estratégicas no mapa
todas as formas:            domínio total → habilidade no nível máximo
```

---

### Batalha com Boss

O boss ataca. Você responde corretamente para defender ou atacar.

- **Acertou** → causa dano (baseado no nível de domínio da palavra)
- **Errou** → perde HP
- **Usou poder** → efeito proporcional ao domínio (nível 1/2/3)
- **Usou habilidade de verbo** → ação especial disponível se dominou o verbo
- Não dá pra furar na sorte — o boss testa especificamente as palavras que você viu
- Perde: refaz as frases que errou → tenta de novo

---

### Kids Module (Futuro)

Se o app escalar, criar módulo separado com:
- História mais leve, personagens coloridos, sem temas de vingança/morte
- Mesmo sistema de vocabulário e Runensprache — simplificado visualmente
- Público: 8-12 anos, com pais como decisores de compra
- Visual completamente diferente — não misturar com o módulo principal

---

## Mundos e Narrativa por Série

### Princípio narrativo
Cada série tem uma história própria que **faz sentido com o nível linguístico do personagem**.
No A1 você não sabe nada — faz sentido ser recém chegado ou amnésico.
No B2 você já é fluente o suficiente para ser espião.
A história justifica o vocabulário. O vocabulário avança a história.

---

### A1 — Vila Medieval: O Forasteiro
**Visual:** tons quentes, âmbar, épico simples
**Personagem:** você acorda sem memória num vilarejo germânico. Ninguém te conhece. Ninguém fala sua língua.
**Por que funciona:** amnésia = zero vocabulário faz sentido total. Cada palavra aprendida reconstrói sua identidade.
**Vocabulário natural:** comida, abrigo, direções, números, saudações, objetos do dia a dia.
**Boss final:** o líder do vilarejo te testa antes de aceitar você como um dos seus.
**Recompensa:** A Espada das Runas → carrega para o A2.

---

### A2 — Bundesliga: O Reforço
**Visual:** verde gramado, amarelo, atmosfera de estádio e cidade moderna
**Personagem:** um clube brasileiro te contrata como novo jogador. Você voa para a Alemanha imediatamente. Você sabe o básico — mas precisa se virar sozinho.
**Por que funciona:** sabe as palavras básicas mas enfrenta a vida real — apartamento, supermercado, treinos, vestiário, coletiva de imprensa, cidade nova.
**Vocabulário natural:** rotina, trabalho, cidade, transporte, alimentação, cotidiano, relacionamentos simples.
**Boss final:** a coletiva de imprensa decisiva — jornalistas te pressionam, cada palavra errada vira manchete.
**Recompensa:** A Chuteira de Ouro → carrega para o B1.

---

### B1 — Universidade de Berlim: O Intercambista
**Visual:** roxo e cinza, arquitetura clássica, outono berlinense
**Personagem:** você conseguiu uma vaga de intercâmbio. Aulas, professores, projetos em grupo, burocracia alemã, amizades, cultura, vida de república.
**Por que funciona:** consegue se comunicar mas precisa argumentar, opinar, debater, explicar ideias complexas.
**Vocabulário natural:** academia, política, cultura, opiniões, discussões, burocracia, amizades profundas.
**Boss final:** apresentação final de TCC para uma banca exigente — sem rascunho, ao vivo.
**Recompensa:** O Diploma de Berlim → carrega para o B2.

---

### B2 — Berlim 1961: O Espião
**Visual:** cinza e vermelho escuro, Guerra Fria, sombrio e tenso
**Personagem:** você é enviado como agente disfarçado em Berlim Oriental. O Muro acabou de ser construído. Uma palavra errada te expõe.
**Por que funciona:** fluência quase nativa exigida — sotaque, nuances, vocabulário político, gírias, pressão social real.
**Vocabulário natural:** política, ideologia, persuasão, negociação, vocabulário técnico, linguagem formal e informal.
**Boss final:** interrogatório pela Stasi — eles sabem que você não é quem diz ser. Prove o contrário.
**Recompensa:** O Dossiê Secreto → carrega para o C1.

---

### C1 — Ruínas Antigas: O Tradutor
**Visual:** preto e dourado, misterioso, ruínas iluminadas por tochas
**Personagem:** um arqueólogo descobre manuscritos germânicos medievais. Você é o único chamado para traduzir. O conteúdo muda a história da língua alemã.
**Por que funciona:** domínio total — linguagem formal, expressões arcaicas, nuances históricas, registro culto.
**Vocabulário natural:** linguagem formal, história, filosofia, expressões idiomáticas avançadas, registros variados.
**Boss final:** apresentação pública da descoberta para a academia — qualquer erro de tradução destrói sua credibilidade.
**Recompensa:** O Grimório Original — você virou mestre.

---

### Tabela resumo

| Série | História | Visual | Nível linguístico exigido |
|-------|----------|--------|--------------------------|
| A1 | Forasteiro na Vila Medieval | Âmbar, épico | Zero — tudo começa aqui |
| A2 | Reforço na Bundesliga | Verde, moderno | Básico — cotidiano real |
| B1 | Intercambista em Berlim | Roxo, clássico | Intermediário — opinar e argumentar |
| B2 | Espião na Guerra Fria | Cinza escuro, tenso | Avançado — fluência sob pressão |
| C1 | Tradutor das Ruínas | Preto e dourado | Domínio — linguagem formal e arcaica |

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
