# Study Seed ES A1 - Estado Atual

Este documento explica como o seed de estudo se encaixa com a aventura ES A1 T1.

## Contexto

Talkly tem dois caminhos de aprendizado paralelos:

```text
AVENTURA -> fases narrativas + vocabulário em contexto RPG
ESTUDO   -> sessão do dia + cenários + prática estruturada
```

Os dois caminhos compartilham progresso por palavra via `WordMastery`/progresso de estudo. O usuário pode jogar só aventura, estudar só pelo modo Estudo, ou usar os dois juntos.

## Estado Atual

O seed de estudo ES A1 já existe:

```text
backend/apps/learning/management/commands/seed_es_study.py
```

Esse comando cria:

- 5 módulos de estudo
- 8 cenários temáticos
- 120 frases ES A1
- 25 `StudyDay` canônicos alinhados às fases ES A1 T1
- 25 explicações curtas com objetivo e notas de exercício

O setup de seeds do backend chama esse seed:

```text
bats/backend/setup.bat
```

Importante: seed de estudo pertence ao app `learning/`, não ao app `adventure/`.

## Cenários ES A1

O seed atual cobre estes cenários:

| Cenário | Slug | Fases relacionadas |
|---|---|---|
| Social | `es-social` | F1, F7, F13 |
| Comida e bebida | `es-comida` | F2, F9 |
| Lugares | `es-lugares` | F3 |
| Mercado e números | `es-mercado` | F4 |
| Salud | `es-salud` | F8 |
| Trabajo | `es-trabalho` | apoio temático do pueblo |
| Historia | `es-historia` | F6, F12, F14, F16-F19, F21-F22 |
| Desafío | `es-desafio` | F5, F10-F11, F15, F20, F23-F25 |

Esses slugs são os mesmos usados pela aventura em:

```text
backend/apps/adventure/seeds/es/chapter.py
```

O comando remove os slugs e módulos legados do seed antigo (`es-saudacoes`, `es-natureza`, `es-emocoes`, `es-pessoas`, `es-tempo`; `O Mundo Natural`, `Dentro de Você`, `Pessoas e Tempo`, `Pueblo e Mercado`, `Mistério e Decisão`) para manter o banco alinhado ao cânone atual.

## Módulos ES A1

| Módulo | Conteúdo |
|---|---|
| Primeiros Passos | `es-social`, `es-comida` |
| Orientação e Mercado | `es-lugares`, `es-mercado` |
| Cuidado e Ofícios | `es-salud`, `es-trabalho` |
| Memória e Segredos | `es-historia` |
| Julgamento e Desafio | `es-desafio` |

Cada cenário tem 15 frases, com:

- `source_language`: PT
- `target_language`: ES
- `source_text`: português
- `target_text`: espanhol
- `difficulty`: A1
- `scenario`: cenário temático

## StudyDays

O comando `seed_es_study` cria 25 dias canônicos:

```text
ES A1 T1 Dia 01: <titulo da fase 1>
...
ES A1 T1 Dia 25: <titulo da fase 25>
```

Cada dia usa o `scenario_slug` da fase ES correspondente em:

```text
backend/apps/adventure/seeds/es/chapter.py
```

O objetivo é que Estudo acompanhe a trilha da Aventura sem depender dela para funcionar.

Cada `Lesson` diária também recebe:

- `objective`: o objetivo pedagógico daquele dia.
- `explanation`: explicação curta conectando a fase da aventura à prática.
- `exercise_notes`: instruções rápidas para guiar escrita, escolha, lacuna, ordem de palavras e revisão.

## Ordem De Execução

Via Django:

```bash
python manage.py seed_languages
python manage.py seed_es
python manage.py seed_es_sections --reset
python manage.py seed_es_study
```

Via bat:

```bat
bats\backend\setup.bat
```

## Status

- [x] Aventura ES A1 T1 criada de F1 a F25.
- [x] Modo Estudo conectado à API.
- [x] `seed_es_study.py` cria módulos, cenários, frases, explicações e StudyDays para ES A1.
- [x] `StudyDayViewSet.today` filtra pelo idioma da meta ativa.
- [x] `bats\backend\setup.bat` chama `seed_es_study`.
- [x] `bats\backend\setup.bat` chama `seed_it_study` e `seed_de_study`.
- [ ] Validar localmente o fluxo completo com banco populado.
- [x] `seed_it_study.py` e `seed_de_study.py` criam estudo canonico para IT e DE.

## Próximo Passo Recomendado

Hoje só existe seed de estudo completo para ES. Como agora também temos aventura IT e DE, o próximo trabalho natural é criar study seeds equivalentes:

```text
backend/apps/learning/management/commands/seed_it_study.py
backend/apps/learning/management/commands/seed_de_study.py
```

Para manter o padrão organizado, prefira extrair os dados e a lógica para:

```text
backend/apps/learning/seeds/
  __init__.py
  study_runner.py
  es.py
  it.py
  de.py
```

Depois os comandos ficariam finos, igual aos comandos de aventura.

## Regra De Qualidade

O estudo deve ser um superconjunto útil do vocabulário da aventura, não uma cópia exata.

Exemplo: se a aventura F1 introduz `hola`, `buenos días`, `me llamo`, o estudo `es-social` também pode incluir `mucho gusto`, `siéntate`, `hasta luego`, família e convívio básico do pueblo.

Para IT/DE, seguir a mesma ideia:

- `pt -> it`: suporte em português, frases em italiano.
- `en -> de`: suporte em inglês, frases em alemão.
