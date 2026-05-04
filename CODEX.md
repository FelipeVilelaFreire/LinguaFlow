# LinguaFlow - Regras de Implementacao

Este arquivo define as regras que devem guiar novas alteracoes no projeto.

## Objetivo do Produto

LinguaFlow e uma plataforma de estudo diario de idiomas baseada em areas de estudo.

Cada usuario pode ter varias areas, por exemplo:

- PT -> DE A1
- PT -> ES A1
- PT -> EN A1

Cada area deve manter progresso, streak, meta e conteudo separados.

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

- `backend/`: API, modelos, serializers, views, seeds e comandos Django.
- `frontend-web/`: app React, telas, componentes, hooks, services, types e tema.
- `docs/`: especificacoes e notas de produto.

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

Modelos principais:

- `Language`
- `Scenario`
- `Phrase`
- `Lesson`
- `StudyDay`
- `StudyDayCompletion`
- `Goal`
- `UserProgress`
- `Favorite`

Regras:

- Dados de usuario devem ser filtrados pelo usuario autenticado.
- `Goal.current` deve retornar a area ativa.
- `StudyDay.today` deve considerar a area ativa.
- Favoritos e progresso devem pertencer ao usuario.

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

Por enquanto o conteudo mais completo esta em PT -> DE.
Novos pares, como PT -> ES, devem ganhar seeds proprios.

## Comandos Locais

Backend:

```powershell
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_content
python manage.py runserver
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
