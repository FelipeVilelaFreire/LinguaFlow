# Adventure Chests, Items and Skills

> Ideia de produto para evoluir os baus, a mochila e o poder narrativo do heroi
> sem quebrar a historia principal.

## Objetivo

Transformar baus e itens em um sistema de progressao narrativa leve:

- O jogador ganha baus ao completar fases especiais.
- Baus ficam armazenados e podem ter tempo de abertura.
- O item recebido muda a jornada, mas nao trava a historia.
- Itens podem canalizar skills, como fogo, agua, cura, persuasao ou defesa.
- A forca real de uma skill depende do item, da raridade e do dominio da palavra ligada a ele.

O principio central e: **a narrativa principal nunca falha por falta de drop aleatorio**. Baus criam variacao, poder e personalizacao, nao bloqueio.

## Estado Atual

O projeto ja tem uma boa base:

- `AdventureItem` tem `rarity`, `item_tag`, `word_id`, `source_phase` e `source_character`.
- `UserInventoryItem` guarda os itens do jogador.
- `WordMastery` guarda dominio por palavra: `bronze`, `prata`, `ouro`, `diamante`, `esmeralda`.
- O heroi ja tem XP, nivel geral e atributos simples: vocabulario, gramatica e fluencia.
- O fluxo de fase ja tenta abrir bau ao concluir uma fase com `has_chest=True`.

O que falta para essa visao:

- Baus armazenados por usuario.
- Timer de abertura.
- Separacao clara entre item obrigatorio de historia e item variavel de bau.
- Conceito de skill/poder ligado a itens e palavras.
- Regras narrativas que usam tags/skills em vez de exigir item especifico.

## Tipos de Recompensa

### 1. Itens Obrigatorios da Historia

Sao itens que a narrativa principal precisa garantir.

Exemplos:

- passe da cidade
- selo do povoado
- prova contra o boss
- chave principal
- carta importante

Regras:

- Nunca dependem de bau.
- Vem de fase, boss, personagem ou escolha narrativa.
- Podem ter `source_phase` ou `source_character`.
- A historia pode assumir que o jogador tera esses itens quando forem necessarios.

### 2. Itens Variaveis de Bau

Sao itens de complemento.

Eles podem:

- aumentar poder do heroi;
- abrir variacoes de dialogo;
- melhorar resultado de uma cena;
- dar alternativa para resolver obstaculos;
- mudar o texto narrativo;
- melhorar combate, cura, social, investigacao ou sobrevivencia;
- alimentar colecao e replay.

Eles nao podem:

- bloquear a historia principal;
- ser a unica forma de derrotar um boss;
- ser obrigatorios para continuar a temporada.

## Baus Armazenados

O fluxo recomendado:

```txt
terminou fase com bau
-> backend cria um UserChest
-> bau aparece em slots de bau
-> jogador escolhe iniciar abertura
-> timer termina
-> jogador coleta
-> item e sorteado/entregue
```

Modelo sugerido:

```txt
UserChest
- user
- phase
- chapter
- chest_tier
- phase_score
- status: stored | opening | ready | claimed | discarded
- rolled_rarity nullable
- earned_item nullable
- created_at
- started_at nullable
- unlock_at nullable
- claimed_at nullable
```

Regras iniciais:

- 3 ou 4 slots de bau.
- Apenas 1 bau abrindo por vez.
- Sem infra extra no MVP.
- O backend compara `now >= unlock_at` para permitir coleta.
- O frontend mostra countdown usando `unlock_at`.

Tempos recomendados para MVP:

| Bau | Tempo |
| --- | --- |
| comum | 2 min |
| raro | 10 min |
| epico | 30 min |
| lendario | 2 h |

Esses tempos sao curtos de proposito. LinguaFlow e um app de aprendizado; o timer deve gerar retorno leve, nao frustracao.

## Slots Cheios

Nao bloquear progresso da fase se os slots estiverem cheios.

Opcoes possiveis:

- converter o bau em XP;
- converter em moeda futura;
- mostrar "slots cheios" e descartar o bau;
- permitir substituir um bau armazenado.

Recomendacao MVP: **se slots estiverem cheios, converter em XP ou recompensa pequena**. Isso evita punir o estudo.

## Item, Skill e Palavra

A regra principal:

```txt
item nao e o poder;
item canaliza uma skill;
palavra dominada aumenta o efeito.
```

Exemplos:

| Item | Item tag | Skill tag | Word |
| --- | --- | --- | --- |
| Tocha Antiga | arma | fogo | es_fuego |
| Cantil Azul | bebida | agua | es_agua |
| Pao de Milho | comida | sustento | es_pan |
| Medalha Velha | documento | persuasao | es_recuerdo |
| Ervas de Maria | remedio | cura | es_medicina |

Campos sugeridos em `AdventureItem`:

```txt
skill_tag: fogo | agua | cura | sustento | defesa | persuasao | investigacao | comercio | memoria | coragem | nenhum
power_value: numero base opcional
charges: usos opcionais, se o item for consumivel
```

Para o MVP, `skill_tag` pode ser suficiente. O poder pode ser calculado por raridade e dominio da palavra.

## Dominio da Skill

O jogador pode ter um item, mas nao dominar bem a palavra ligada a ele.

Tres estados narrativos:

```txt
nao tem item:
  segue rota normal

tem item, mas word mastery baixo:
  usa com efeito fraco ou inseguro

tem item e word mastery alto:
  usa com efeito forte e abre resultado melhor
```

Tabela sugerida:

| Word tier | Nivel narrativo | Multiplicador |
| --- | --- | --- |
| sem mastery | desconhecido | 0.5 |
| bronze | iniciante | 1.0 |
| prata | estavel | 1.25 |
| ouro | forte | 1.5 |
| diamante | avancado | 2.0 |
| esmeralda | mestre | 2.5 |

Raridade tambem entra:

| Raridade | Base |
| --- | --- |
| comum | 10 |
| raro | 20 |
| epico | 35 |
| lendario | 55 |

Formula inicial:

```txt
item_power = rarity_base * word_mastery_multiplier
```

Exemplo:

```txt
Tocha Antiga
raridade: raro = 20
word_id: es_fuego
dominio: ouro = 1.5

poder de fogo = 30
```

## Skill do Heroi

No futuro, alem do item e da palavra, pode existir nivel acumulado por skill.

Modelo possivel:

```txt
UserSkillMastery
- user
- chapter nullable
- skill_tag
- xp
- level
- last_used_at
```

Como evolui:

- usar item de fogo aumenta XP de `fogo`;
- acertar palavras ligadas a fogo aumenta XP de `fogo`;
- concluir cenas com fogo aumenta XP de `fogo`;
- bau raro/epico pode dar item que acelera uma skill.

Mas isso deve vir depois. Para o primeiro passo, usar `WordMastery` ja entrega bastante profundidade.

## Cenas Narrativas por Requisito Flexivel

A narrativa nao deve pedir "precisa da Tocha Antiga".

Ela deve pedir:

```txt
precisa de skill_tag=fogo
ou item_tag=arma
ou skill_tag=persuasao
ou soma de alternativas >= X
```

Exemplo de cena:

```txt
Obstaculo: porta selada
Requisitos possiveis:
- fogo >= 35
- agua >= 35
- documento >= 25
- investigacao >= 40
```

Resultados:

```txt
sem requisito:
  voce resolve com esforco, mas perde tempo ou recebe texto mais simples

requisito parcial:
  voce abre uma alternativa boa, mas ainda precisa de ajuda

requisito forte:
  voce resolve de forma marcante e ganha cena especial
```

## Boss com Soma de Forcas

O boss final nao deve exigir um item especifico.

Ele pode exigir uma soma de pressoes narrativas:

```txt
boss_pressure_needed = 100

fontes possiveis:
- fogo
- agua
- arma
- defesa
- cura
- persuasao
- documento
- investigacao
- palavras-chave dominadas
- aliados conhecidos
```

Exemplo:

```txt
Jogador A:
- fogo avancado: 70
- coragem: 20
- arma comum: 15
total: 105
resultado: vence com fogo como acao principal

Jogador B:
- fogo baixo: 20
- arma rara: 40
- documento forte: 30
- cura: 15
total: 105
resultado: vence combinando estrategia e recursos

Jogador C:
- sem poder elemental
- persuasao: 45
- investigacao: 35
- palavras-chave dominadas: 30
total: 110
resultado: vence por dialogo e prova
```

Isso permite que jogadores tenham jornadas diferentes sem criar fail state injusto.

## Comida, Bebida e Remedio

Esses itens seguem a mesma regra dos poderes.

Exemplo de comida:

```txt
Pao de Milho
tag: comida
skill: sustento
word: es_pan
```

Resultados:

```txt
sem item:
  voce procura outra solucao

tem item + bronze:
  recupera pouco ou ajuda de forma simples

tem item + ouro:
  recupera bem e abre fala extra

tem item + esmeralda:
  vira momento narrativo forte, talvez salva um aliado
```

Exemplo de remedio:

```txt
Ervas de Maria
tag: remedio
skill: cura
word: es_medicina
```

Pode:

- recuperar o heroi;
- evitar penalidade;
- melhorar relacao com personagem;
- salvar um NPC em uma variacao narrativa;
- fortalecer cena futura.

## Exemplo de Estrutura de Cena

Um passo de narrativa poderia ter dados assim:

```json
{
  "kind": "skill_moment",
  "title": "A porta queimada",
  "text": "A madeira esta marcada por um calor antigo.",
  "requirements": [
    { "type": "skill", "tag": "fogo", "power": 35 },
    { "type": "skill", "tag": "agua", "power": 35 },
    { "type": "item_tag", "tag": "documento", "power": 25 }
  ],
  "outcomes": {
    "none": "Voce forca a passagem com dificuldade.",
    "partial": "Seu recurso ajuda, mas voce ainda precisa improvisar.",
    "strong": "Voce entende o mecanismo e atravessa com seguranca."
  }
}
```

## Ordem de Implementacao Recomendada

### Fase 1: Base Segura dos Baus

- Criar `UserChest`.
- Trocar abertura imediata por bau armazenado.
- Garantir que bau so nasce depois de fase concluida.
- Garantir que cada fase gere no maximo um bau por usuario.
- Criar endpoints: listar, iniciar abertura, coletar.

### Fase 2: Timer e UI

- Criar tela/aba de baus.
- Mostrar slots.
- Mostrar countdown.
- Permitir iniciar abertura.
- Permitir coletar quando pronto.

### Fase 3: Skill Tag nos Itens

- Adicionar `skill_tag` em `AdventureItem`.
- Atualizar seeds com skills basicas.
- Calcular poder por raridade + dominio da palavra.
- Exibir skill/poder na mochila.

### Fase 4: Momentos Narrativos Flexiveis

- Criar `skill_moment` ou evoluir `item_moment`.
- Permitir requisitos por `item_tag` e `skill_tag`.
- Retornar outcome narrativo conforme poder calculado.

### Fase 5: Skill Mastery Propria

- Criar `UserSkillMastery`.
- Dar XP por uso de skill.
- Mostrar poderes do heroi na aba Heroi.
- Usar skill level em boss e cenas especiais.

## Decisoes de Design

- Historia obrigatoria vem de item fixo, nao de bau.
- Bau e recompensa variavel, nao chave obrigatoria.
- Item especifico nao deve ser requisito de fase futura.
- Requisito narrativo deve ser por tag, skill ou soma de poder.
- Palavra dominada melhora o efeito do item.
- Raridade melhora potencial, mas dominio linguistico deve importar mais no longo prazo.
- Timers devem ser curtos no MVP.
- Sem monetizacao, gemas ou aceleracao no inicio.

## Resumo

O sistema ideal para LinguaFlow nao e "ganhou o item certo ou perdeu".

E:

```txt
voce aprendeu palavras
-> ganhou itens
-> itens canalizam skills
-> dominio da palavra aumenta poder
-> a narrativa reconhece suas escolhas
-> o boss pode ser vencido de varios jeitos
```

Isso preserva aprendizado, narrativa e personalizacao ao mesmo tempo.
