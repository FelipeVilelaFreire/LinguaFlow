# Frontend Web Architecture

Arquitetura ativa do `frontend-web`, usando React, Vite, TypeScript e Tailwind CSS.

O guia antigo baseado em Next.js foi preservado em `../archive/frontend-web-architecture-legacy.md`.

## Estrutura Atual

```txt
frontend-web/
|-- public/
|   `-- es/
|       `-- characters/
`-- src/
    |-- App.tsx
    |-- main.tsx
    |-- components/
    |-- constants/
    |-- contexts/
    |-- features/
    |   |-- account/
    |   |   `-- screens/
    |   |-- adventure/
    |   |   |-- components/
    |   |   |-- constants/
    |   |   |-- screens/
    |   |   `-- theme/
    |   |-- auth/
    |   |   `-- screens/
    |   |-- history/
    |   |   `-- screens/
    |   |-- home/
    |   |   `-- screens/
    |   `-- study/
    |       |-- components/
    |       `-- screens/
    |-- hooks/
    |-- services/
    |-- styles/
    |-- theme/
    `-- types/
```

## Responsabilidades

- `features/`: telas e UI especifica por dominio. Cada feature pode ter `screens/`, `components/`, `constants/` e `theme/` quando fizer sentido.
- `features/adventure/`: experiencia de aventura, incluindo telas, avatar/modal de personagem, constantes e tema visual local.
- `features/study/`: telas e componentes especificos do estudo guiado, vocabulario, cenario e sessao.
- `features/account/`: telas de conta e edicao de perfil.
- `features/auth/`: telas de login/cadastro e onboarding.
- `features/home/`: tela inicial do app logado.
- `features/history/`: tela de historico.
- `components/`: componentes compartilhados entre varias areas do app.
- `services/`: acesso a API, audio, armazenamento local e servicos do navegador.
- `contexts/`: estado global via React Context.
- `hooks/`: hooks reutilizaveis entre features.
- `constants/`: strings e configuracoes estaticas compartilhadas.
- `types/`: contratos TypeScript compartilhados entre telas, servicos e componentes.
- `theme/`: tokens visuais compartilhados ou temas ainda nao migrados.
- `styles/`: CSS global e utilitarios.

## Regras

- Telas e componentes especificos de uma area devem ficar dentro de `features/<area>/`.
- Codigo usado por mais de uma area deve continuar em `components/`, `hooks/`, `services/`, `types`, `constants` ou `theme`.
- `services/` e `types/` ficam globais por padrao, mesmo quando o dominio principal e uma feature especifica.
- Hooks ficam globais enquanto forem reutilizaveis ou enquanto a arquitetura nao decidir explicitamente por hooks locais da feature.
- A feature `adventure` centraliza avatar de personagens, modal de perfil, telas da aventura, constantes de personagens e cores da aventura.
- UI visivel deve usar o sistema de strings quando aplicavel.
- Tipos de API devem viver em `types/`; transformacoes podem ficar em services/helpers.
- Evitar componentes gigantes: fluxos de aventura devem ser quebrados em componentes por responsabilidade.
- Usar `lucide-react` para icones quando houver equivalente.

## Validacao

```bash
cd frontend-web
.\node_modules\.bin\tsc.cmd -b --pretty false
```

## Estrutura Alvo

```txt
src/
|-- app/
|-- shared/
`-- features/
    |-- account/
    |-- adventure/
    |-- auth/
    |-- study/
    |-- goals/
    |-- history/
    |-- home/
    `-- layout/
```

Prioridade sugerida:

- Extrair `App.tsx` e roteamento para `app/` quando o roteador crescer.
- Avaliar `features/goals/` se a gestao de metas sair de `account`.
- Depois disso, avaliar se `components/`, `constants/`, `theme` e `hooks` devem virar `shared/`.
