# Estrutura Recomendada Do Estudo

O Estudo nao deve ser apenas uma lista de modulos com frases. Ele precisa ter uma hierarquia propria, equivalente em profundidade a Aventura, mas sem narrativa, itens, boss ou HP.

## Hierarquia

```txt
StudyCourse
  -> StudyUnit
      -> StudyLesson
          -> StudySection
              -> StudyStep
```

Comparacao com Aventura:

| Aventura | Estudo |
| --- | --- |
| Capitulo / temporada | Curso / unidade |
| Fase | Licao |
| Secao da fase | Secao pedagogica |
| Step narrativo/exercicio | Step de aprendizado |
| Boss | Checkpoint de revisao |

## Exemplo De Uma Licao

```txt
Licao: Saudacoes basicas

Secao 1 - Explicacao
  Step: objetivo da licao
  Step: regra gramatical curta
  Step: exemplos principais

Secao 2 - Compreensao
  Step: frase alvo
  Step: traducao
  Step: padrao da frase

Secao 3 - Pratica
  Step: multipla escolha
  Step: completar lacuna
  Step: ordenar palavras
  Step: escrever

Secao 4 - Revisao
  Step: frases antigas
  Step: erro recorrente
  Step: mini checkpoint
```

## Regra De Produto

O Estudo deve compartilhar o mesmo conteudo e o mesmo progresso pedagogico da Aventura, mas precisa ter uma experiencia propria:

- mais clara;
- mais didatica;
- mais previsivel;
- menos emocional;
- sem dependencia de narrativa.

## Implementacao Em Fases

### Fase 1 - Frontend

Usar os dados atuais:

- `StudyModule` como unidade;
- `Scenario` como licao;
- frases como conteudo da licao;
- steps calculados no frontend: explicacao, entender, praticar, revisar.

### Fase 2 - Backend

Criar dados reais:

```txt
StudySection
- lesson
- kind: explain | understand | practice | review | checkpoint
- title
- order

StudyStep
- section
- kind: intro | explanation | phrase | multiple_choice | fill_blank | write | word_order | review
- prompt
- answer
- phrase nullable
- order
```

### Fase 3 - Progresso

Separar o progresso visual do Estudo:

```txt
StudySectionProgress
- user
- section
- completed_steps
- completed_at
```

O progresso pedagogico continua unificado com a Aventura, mas o progresso de interface do Estudo pode saber exatamente qual secao/step o usuario concluiu.
