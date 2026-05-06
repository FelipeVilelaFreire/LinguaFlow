# LinguaFlow — Game Concept

## Visão Geral

O LinguaFlow não é um app de estudo — é um **RPG onde aprender o idioma É o jogo**.

O jogador não "aprende alemão". Ele é um personagem preso num mundo onde só sobrevive quem domina a língua. A língua fica invisível; o que aparece é a aventura.

---

## Estrutura de Progressão

Cada nível CEFR (A1, A2, B1...) é um **capítulo completo** com:

- Sua própria história (começo, meio e fim)
- Seu próprio visual e design (tema muda por capítulo)
- Sub-fases internas (ex: A1 tem fases 1 a 9)
- Um **boss final** derrotado com o vocabulário aprendido no capítulo
- Uma **recompensa/tesouro** que carrega para o próximo capítulo como vantagem

---

## Exemplo de Fluxo

```
A1 - Vila Medieval
├── Fase 1-3: Você acorda sem memória, aprende o básico pra se comunicar
├── Fase 4-6: Descobre que a vila está em perigo
├── Fase 7-9: Aprende vocabulário de batalha e se prepara
└── BOSS FINAL: Derrota o vilão usando as palavras que aprendeu
         ↓
    Recompensa: A Espada das Runas → carrega pro A2 como vantagem

A2 - Floresta Sombria
├── Jogador entra com a Espada das Runas do A1
├── A espada dá vantagem em certos desafios de A2
├── Nova história, novo visual, novos personagens
└── BOSS FINAL → novo item para o A3
```

---

## Mundos e Temas

| Nível | Mundo | Visual | Narrativa |
|-------|-------|--------|-----------|
| A1 | Vila Medieval | Tons quentes, épico simples | Guerreiro amnésico aprende a língua pra sobreviver |
| A2 | Floresta Sombria | Verde escuro, místico | Magia ligada às palavras, segredos da floresta |
| B1 | Reino do Castelo | Roxo e dourado, grandioso | Intrigas políticas, você vira diplomata |
| B2 | Porto Internacional | Azul oceano, vibrante | Espião/comerciante em missões secretas |
| C1 | Ruínas Antigas | Preto e ouro, misterioso | Descobre a origem do idioma, virou mestre |

---

## Por Que Funciona

- A pessoa termina A1 pra **pegar a espada**, não só pra aprender alemão
- A recompensa do capítulo anterior cria **antecipação** para o próximo
- O idioma é o **mecanismo do jogo**, não o objetivo explícito
- Cada capítulo tem design diferente — nunca enjoa visualmente
- O boss final dá **sensação de conquista real** ao completar um nível

---

## Princípios de Design

1. **A história força o vocabulário** — o jogador precisa das palavras pra avançar na narrativa
2. **Continuidade entre capítulos** — itens e consequências carregam entre fases
3. **Visual muda por capítulo** — cada mundo tem paleta, tipografia e estilo próprios
4. **Boss como culminação** — o boss testa tudo que foi aprendido no capítulo
5. **Recompensa com significado narrativo** — o item ganho tem papel na história seguinte

---

## Escopo Real de Implementação

### Princípio central
> **O objetivo é a história, não o design.**

O que faz o jogador continuar não é um mapa animado ou sprites — é querer saber o que acontece depois. O design serve a história, não o contrário.

### Nível de complexidade escolhido: Seleção de Fases
Tipo Mario Bros — simples de construir, poderoso na experiência:

- Tela com nós conectados por um caminho (cada lição = um nó)
- Nó completo = aceso / bloqueado = escuro com cadeado
- Background com atmosfera do mundo atual (vila, floresta...)
- Clica no nó, entra na missão com contexto narrativo
- Final de capítulo = desafio do chefe com visual mais dramático
- **Sem mapa interativo complexo, sem personagens animados**

### O que cria a sensação de jogo de verdade
- A narrativa de cada fase (o jogador quer saber o que vem depois)
- A progressão visível no caminho de nós
- O item/recompensa ao final do capítulo
- A mudança de atmosfera entre capítulos

### Decisões Técnicas

**Stack do Frontend**
- **React + Vite + TypeScript** — base atual, mantida
- **Tailwind CSS** — estrutura de layout e espaçamento
- **ReactBits** — efeitos visuais de atmosfera (backgrounds, transições, glow)

Tailwind cuida da estrutura, ReactBits cuida da vida visual.

### Primeiro passo técnico
Instalar o ReactBits e construir a tela de seleção de fases do A1 (Vila Medieval) com o caminho de nós e a atmosfera do mundo.
