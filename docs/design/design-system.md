# Design System

Documento ativo para decisoes visuais do LinguaFlow/Talkly. O dump antigo de prompt foi preservado em `../archive/design-system-context-legacy.md`.

## Principios

- Mobile first: desktop melhora a experiencia, mas nao define a base.
- Interfaces de estudo devem ser claras, rapidas e com pouca escolha.
- Interfaces operacionais/admin devem ser densas, previsiveis e sem visual de landing page.
- Texto visivel de UI deve vir do sistema de strings do frontend.
- Evitar cores hardcoded em componentes quando houver tokens de tema.

## Tokens

O tema do app web vem de `frontend-web/src/theme/`:

- `colors.ts`: tokens por area/idioma.
- `studyAreaTheme.ts`: converte tokens em CSS variables.
- `adventureColors.ts`: paletas especificas do modo aventura.

Preferir CSS variables e helpers existentes:

- `--area-primary`
- `--area-primary-dark`
- `--area-primary-soft`
- `--area-accent`
- `--area-page`
- `.area-btn`
- `.area-text-primary`
- `.area-bg-soft`

## Componentes

- Botoes de acao devem ter estado de loading/disabled quando executam trabalho.
- Modais simples podem ser centralizados; fluxos complexos em mobile devem virar tela dedicada ou bottom sheet.
- Cards devem representar itens reais e repetidos, nao envolver secoes inteiras da pagina.
- Icones devem vir de `lucide-react` quando existir equivalente.

## Movimento

Animacoes devem reforcar feedback, nao decorar:

- acerto: pop curto;
- erro: shake curto;
- entrada de etapa: fade/slide leve;
- progresso: transicao suave.

Respeitar `prefers-reduced-motion`.

## Arquivos Relacionados

- [Frontend Web Architecture](../architecture/frontend-web.md)
- [ES Character Image Prompts](characters-es-image-prompts.md)
- [Legacy Design System Context](../archive/design-system-context-legacy.md)
