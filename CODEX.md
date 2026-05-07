# Talkly - Regras de Implementacao

Este arquivo define as regras que devem guiar novas alteracoes no projeto.

## Objetivo do Produto

Talkly e uma plataforma de aprendizado de idiomas via narrativa RPG e estudo guiado diario.

Cada usuario pode ter varias areas de estudo, por exemplo:

- PT -> IT A1
- PT -> DE A1
- PT -> ES A1

Cada area deve manter progresso, streak, meta e conteudo separados.

## Modo Aventura — Hierarquia de Conteudo

Esta hierarquia e a espinha dorsal do produto. Nunca confundir os niveis.

```
SERIE   = nivel CEFR completo (ex: A1 Italiano)
           ↳ 5 TEMPORADAS por serie
                ↳ 25 FASES por temporada (badges T1…T5, nao A1/A2/B1…)
                     ↳ 6 SECOES por fase
```

As 6 secoes de cada fase (em ordem):
1. Cotidiano      — contexto do dia, apresenta o NPC
2. Aquecimento    — revisao do vocabulario anterior (SRS)
3. Evento Principal — historia avanca, vocabulario novo introduzido
4. Decodificacao  — padrao gramatical revelado em contexto
5. Pratica        — exercicios guiados com o novo vocabulario
6. Obstaculo      — gate Metroidvania: requer dominar palavras-chave para passar

Tipos de fase (campo `phase_type` em `AdventurePhase`):
- `"story"`  — fases normais (1–14, 16–19, 24)
- `"review"` — checkpoints SRS (15, 20, 21, 22, 23) — icone livro, cor dourada
- `"boss"`   — sempre a Fase 25, fecha a temporada

Regras que nunca devem ser quebradas:
- `"A1"` identifica a SERIE inteira, nao uma temporada individual.
- Badges de temporada sao T1, T2, T3, T4, T5 — nunca A1/A2/B1/B2/C1.
- O label "A1" aparece apenas no header da serie e no header do mapa.
- Boss e sempre a ultima fase (Fase 25) e desbloqueia um item para a Mochila.
- Cada fase tem exatamente `section_count: 6`.

MVP ativo: Italiano — "Il Viandante" (Serie A1)
- T1 Arrivo al Borgo → T2 Venezia → T3 Toscana → T4 Napoli → T5 Roma Aeterna
- Mock em: `frontend-web/src/mocks/adventureItMock.ts`

## Stack

Backend:

- Django
- Django REST Framework
- JWT com SimpleJWT
- SQLite em desenvolvimento

Frontend:

- React
- Vite
- TypeScript
- Tailwind CSS
- lucide-react para icones

## Estrutura

Manter separacao clara:

- `backend/`: API Django organizada por apps de dominio.
- `frontend-web/`: app React, telas, componentes, hooks, services, types e tema.
- `docs/`: especificacoes e notas de produto.

Estrutura atual do backend:

- `backend/apps/accounts/`: autenticacao, cadastro, login, usuario atual e refresh de token.
- `backend/apps/learning/`: idiomas, cenarios, frases, licoes, study days, seeds e conteudo de estudo.
- `backend/apps/goals/`: areas de estudo, onboarding, rotina, area ativa e historico mensal.
- `backend/apps/progress/`: favoritos, progresso por frase e conclusoes de estudo.
- `backend/content/`: pacote legado/compatibilidade e seeds antigos. Nao deve receber codigo novo de produto.
- `backend/linguaflow/`: configuracao global, settings e roteamento principal.

Regra importante:

- Codigo novo deve importar dos apps reais: `apps.learning`, `apps.goals`, `apps.progress`, `apps.accounts`.
- Imports via `content.*` devem ser usados apenas por compatibilidade ou seed legado.
- A documentacao detalhada da arquitetura fica em `backend/ARCHITECTURE.md`.

## Arquitetura Frontend

Seguir esta separacao:

- `screens/`: telas principais e composicao de pagina.
- `components/`: UI reutilizavel e componentes de aprendizado.
- `hooks/`: estado, regras de tela e orquestracao.
- `services/`: comunicacao HTTP com backend.
- `types/`: contratos TypeScript de dominio.
- `theme/`: tokens e temas visuais.
- `constants/`: rotas, textos e configuracoes fixas.

Regras:

- Nao fazer `fetch` direto em componente.
- Toda API deve passar por `services/`.
- Tipos de dominio devem ficar em `types/`.
- Logica complexa deve ir para hook ou service, nao ficar espalhada em JSX.
- Usar icones do `lucide-react`.

## Rotas Frontend

Rotas atuais:

- `/login`
- `/onboarding`
- `/`
- `/estudo-guiado`
- `/historico`
- `/cenarios`
- `/vocabulario`
- `/perfil`

O app e SPA, mas a URL deve representar a tela atual.

## Autenticacao

Usar JWT.

Fluxo:

- Login/cadastro retornam `access` e `refresh`.
- Frontend envia `Authorization: Bearer <access>`.
- Se o `access` expirar, tentar renovar com `refresh`.
- Logout deve limpar tokens do `localStorage`.

Endpoints principais:

- `POST /api/auth/register/`
- `POST /api/auth/login/`
- `POST /api/auth/refresh/`
- `GET /api/auth/me/`

## Areas de Estudo

`Goal` representa uma area de estudo do usuario.

Regras:

- Um usuario pode ter varias areas.
- Apenas uma area deve estar ativa por vez.
- Home, Estudo Guiado, progresso e streak devem usar a area ativa.
- Trocar de area deve passar pelo modal de area ativa ou pelo Perfil.
- Criar e excluir areas deve ficar no Perfil.
- A troca de area deve ter transicao visual full-screen.
- `Goal` tambem guarda rotina de estudo: `study_weekdays` e `session_minutes`.
- Se `study_weekdays` estiver vazio, a area esta em modo de estudo avulso.

## Rotina e Estudo Avulso

O onboarding deve permitir dois modos:

- Criar rotina: usuario escolhe dias da semana e duracao da sessao.
- Estudar avulso: usuario nao define agenda fixa por enquanto.

Regras:

- Rotina deve vir do backend, nao ficar apenas como estado visual do frontend.
- Home deve mostrar se hoje e dia de estudo ou qual e a proxima sessao.
- Se for estudo avulso, Home deve mostrar que nao existe agenda fixa.
- Historico deve separar conclusoes por area de estudo.
- Conclusoes devem registrar a area ativa no momento do estudo.

## Tema por Area

As cores do sistema devem vir da area ativa.

Arquivos principais:

- `frontend-web/src/theme/colors.ts`
- `frontend-web/src/theme/studyAreaTheme.ts`

Usar CSS variables:

- `--area-primary`
- `--area-primary-dark`
- `--area-primary-soft`
- `--area-accent`
- `--area-accent-soft`
- `--area-page`
- `--area-text-on-primary`

Nao espalhar cores fixas quando o elemento representa a area ativa.

As paletas por idioma devem ficar centralizadas em `theme/colors.ts`.
Componentes nao devem decidir manualmente que DE e amarelo/preto/vermelho,
ES e vermelho/amarelo, ou EN e azul/vermelho. Eles devem consumir tokens.

Direcao atual das paletas:

- Alemao (`DE`): preto/slate como primario, vermelho como destaque, amarelo suave como apoio.
- Espanhol (`ES`): vermelho como primario, amarelo como apoio.
- Ingles (`EN`): azul como primario, vermelho como destaque.

Se uma nova lingua for adicionada, criar primeiro os tokens em `theme/colors.ts`
e depois deixar `studyAreaTheme.ts` resolver o tema pela area ativa.

Exemplos:

- botoes principais: `var(--area-primary)`
- progress bar: `var(--area-primary)`
- destaque suave: `var(--area-primary-soft)`
- fundo geral: `var(--area-page)`

## Arquitetura CSS — Como escrever estilos

Regra de ouro: cada tipo de estilo tem um lugar fixo. Nunca misturar.

| O que | Onde fica | Exemplo |
|---|---|---|
| Layout, espacamento, cores slate | Tailwind no JSX | `className="flex flex-col gap-3"` |
| CSS vars, hover com vars, animacoes | `globals.css` | `.auth-submit`, `.auth-input:focus` |
| Valor calculado em JS | `style={{}}` inline | `opacity: mounted ? 1 : 0` |
| **Nunca** | `<style>` dentro do componente | — |

Por que isso importa para IA: quando os estilos estao em um so lugar previsivel, qualquer modelo consegue ler, editar e nao quebrar o que ja existe. Estilos espalhados entre `style={{}}`, `className` e `<style>` tornam o codigo imprevisivel para edicao automatizada.

Aplicacao pratica:
- Classe nova que usa `--area-primary`? Vai para `globals.css`.
- Posicao/tamanho/cor slate? Vai para `className` com Tailwind.
- Delay de animacao que depende de indice JS? Unico caso aceitavel para `style={{}}`.
- Quer criar `.minha-screen-btn`? Adiciona em `globals.css`, agrupa proximo as outras classes da tela.

## Design e UX

Direcao visual:

- limpo
- moderno
- simples
- mais produto do que jogo
- transicoes suaves
- cards com `8px` de radius
- evitar bordas pretas grossas e sombras cartoon

Evitar:

- visual gamificado demais
- paleta muito gritante
- excesso de `font-black`
- `shadow-[...]` agressivo
- muitas cores competindo na mesma tela

Preferir:

- `shadow-sm`
- `ring-1 ring-slate-200`
- espacos claros
- tipografia `font-medium` ou `font-semibold`
- foco visual no conteudo de estudo

## Backend

O backend esta organizado em apps reais.

### `apps.accounts`

Responsavel por:

- cadastro
- login
- usuario atual
- refresh de token

Classes principais:

- `RegisterSerializer`
- `LoginSerializer`
- `UserSerializer`
- `AuthViewSet`

### `apps.learning`

Responsavel pelo conteudo estudavel.

Modelos:

- `Language`
- `Scenario`
- `Phrase`
- `Lesson`
- `StudyDay`

ViewSets:

- `PhraseViewSet`
- `ScenarioViewSet`
- `StudyDayViewSet`

### `apps.goals`

Responsavel por areas, planejamento e historico agregado.

Modelo:

- `Goal`

ViewSet:

- `GoalViewSet`

Endpoints importantes:

- `GET /api/goals/`
- `GET /api/goals/current/`
- `POST /api/goals/onboarding/`
- `POST /api/goals/{id}/activate/`
- `GET /api/goals/history/?year=YYYY&month=M`

### `apps.progress`

Responsavel por atividade do usuario.

Modelos:

- `StudyDayCompletion`
- `UserProgress`
- `Favorite`

ViewSets:

- `FavoriteViewSet`
- `ProgressViewSet`

Regras:

- Dados de usuario devem ser filtrados pelo usuario autenticado.
- `Goal.current` deve retornar a area ativa.
- `StudyDay.today` deve considerar a area ativa.
- Favoritos e progresso devem pertencer ao usuario.
- `StudyDayCompletion` deve gravar `goal` para permitir historico separado por area.
- Nao criar codigo novo de dominio em `content/`; usar `apps/*`.
- Os models novos preservam tabelas antigas via `db_table`, por exemplo `content_goal`.

## Seeds

Comando:

```bash
python manage.py seed_content
```

O seed deve:

- criar idiomas suportados
- criar cenarios
- criar frases
- criar licoes
- criar study days

Pares com seed principal:

- `PT -> DE` nos niveis `A1`, `A2`, `B1`
- `PT -> ES` nos niveis `A1`, `A2`, `B1`
- `EN -> DE` nos niveis `A1`, `A2`, `B1`

Novos pares devem ganhar seeds proprios antes de aparecerem como disponiveis na UI.

O comando `seed_content` e exposto por `apps.learning`, mas ainda pode consumir
helpers em `content/seeds/` ate esses seeds serem migrados para a estrutura nova.

## Comandos Locais

Backend:

```powershell
cd backend
pip install -r requirements.txt
python manage.py migrate --fake-initial
python manage.py seed_content
python manage.py runserver
```

Usar `--fake-initial` quando o banco local ja tiver tabelas antigas `content_*`.
Para banco completamente novo, `python manage.py migrate` e suficiente.

Validacao backend:

```powershell
python manage.py check
python manage.py makemigrations --check
```

Frontend:

```powershell
cd frontend-web
npm install
npm run dev
```

Validacao frontend:

```powershell
npm run build
```

## Cuidados

- Antes de mudar arquitetura, verificar os arquivos existentes.
- Nao misturar backend e frontend.
- Nao remover mudancas existentes sem necessidade.
- Nao quebrar as rotas reais.
- Nao voltar para auth por token simples; manter JWT.
- Nao hardcodar cor de area quando existe token de tema.
- Se criar nova feature, manter a experiencia coerente com areas de estudo.
- Nao reintroduzir fallback mockado no frontend para dados que devem vir da API.
- Nao criar novas tabelas com nomes diferentes sem pensar na migracao dos dados existentes.
- Se mexer em models dos apps novos, criar migrations nos apps corretos.
- Se mexer em rotas de API, manter compatibilidade com o frontend ou atualizar `services/`.
