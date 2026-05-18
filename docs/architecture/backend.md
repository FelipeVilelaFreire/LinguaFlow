# Backend Architecture

Arquitetura ativa do backend Django/DRF do LinguaFlow.

O backend usa apps Django reais por dominio. A regra principal e simples:
codigo de produto fica em `apps/<dominio>/`; configuracao global fica em
`config/`; dados/seeds legados ficam fora do caminho principal.

## Estrutura Atual

```txt
backend/
|-- manage.py
|-- requirements.txt
|-- db.sqlite3
|-- config/
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- apps/
|   |-- accounts/
|   |   |-- admin.py
|   |   |-- admin_api.py
|   |   |-- apps.py
|   |   |-- serializers.py
|   |   `-- views.py
|   |-- adventure/
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- serializers.py
|   |   |-- views.py
|   |   |-- management/commands/
|   |   `-- migrations/
|   |-- goals/
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- serializers.py
|   |   |-- views.py
|   |   `-- migrations/
|   |-- learning/
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- serializers.py
|   |   |-- views.py
|   |   |-- management/commands/
|   |   `-- migrations/
|   `-- progress/
|       |-- admin.py
|       |-- apps.py
|       |-- models.py
|       |-- serializers.py
|       |-- views.py
|       `-- migrations/
`-- content/
    |-- management/
    |-- migrations/
    `-- seeds/
```

## Responsabilidades

- `config/`: configuracao global do Django, DRF, CORS, JWT, banco e rotas.
- `apps/accounts/`: autenticacao, usuario atual, login, registro e dashboard admin via API.
- `apps/learning/`: idiomas, cenarios, frases, aulas, modulos e dias de estudo.
- `apps/goals/`: areas de estudo, objetivo ativo, rotina, onboarding e historico por meta.
- `apps/progress/`: progresso do usuario, favoritos, completions, streak e estado salvo.
- `apps/adventure/`: capitulos, fases, personagens, inventario, itens, vocabulario de aventura e endpoints de dev.
- `content/`: area legada para seeds/cache/migracoes antigas. Nao deve receber codigo novo de produto.
- `bats/backend/`: automacao local do backend. Fica fora de `backend/`
  porque `bats/` e a raiz unica de scripts Windows do repositorio.
- `tts_models/`: modelos Piper locais para laboratorio/dev de TTS. E gerado,
  ignorado pelo Git e nao contem Django models.
- `media/`: cache/arquivos locais gerados pelo Django, como WAVs da aventura.
  E ignorado pelo Git e pode ser recriado.

## Installed Apps

Os apps de dominio ativos ficam em `config/settings.py`:

```python
INSTALLED_APPS = [
    "apps.accounts.apps.AccountsConfig",
    "apps.learning.apps.LearningConfig",
    "apps.goals.apps.GoalsConfig",
    "apps.progress.apps.ProgressConfig",
    "apps.adventure.apps.AdventureConfig",
]
```

## Rotas

As rotas de API ficam centralizadas em `config/urls.py` com `DefaultRouter`.
Esse arquivo deve registrar ViewSets, mas a regra de negocio deve continuar
dentro do app de dominio.

Principais grupos:

```txt
/api/auth/
/api/admin-dashboard/
/api/phrases/
/api/scenarios/
/api/study/modules/
/api/study-days/
/api/goals/
/api/favorites/
/api/progress/
/api/adventure/chapters/
/api/adventure/phases/
/api/adventure/characters/
/api/adventure/items/
/api/adventure/inventory/
/api/adventure/vocabulary/
/api/adventure/dev/
```

## Regras

- Models, serializers, views, admin e migrations ficam dentro do app do dominio.
- Novo codigo de autenticacao entra em `apps/accounts/`.
- Novo codigo de estudo/conteudo entra em `apps/learning/`.
- Novo codigo de metas/areas/rotina entra em `apps/goals/`.
- Novo codigo de progresso entra em `apps/progress/`.
- Novo codigo de aventura entra em `apps/adventure/`.
- Rotas continuam centralizadas em `config/urls.py`.
- Seeds de estudo ficam em `apps/learning/management/commands/`.
- Seeds da aventura ficam em `apps/adventure/management/commands/`.
- `content/` e compatibilidade legada nao devem ser usados para codigo novo.

Import preferido:

```python
from apps.accounts.views import AuthViewSet
from apps.adventure.models import AdventureCharacter
from apps.goals.models import Goal
from apps.learning.models import Phrase
from apps.progress.models import Favorite
```

Evitar em codigo novo:

```python
from content.models import Goal
```

## Banco E Compatibilidade

Alguns models mantem nomes antigos de tabela via `db_table`, por exemplo
`content_goal`. Isso preserva bancos locais antigos enquanto o codigo fica
organizado por apps Django reais.

Migrations de compatibilidade devem ficar no app que hoje e dono do dominio.
Exemplo: ajustes de `Goal` ficam em `apps/goals/migrations/`, mesmo que a tabela
continue chamada `content_goal`.

## Seeds

O backend hoje tem seeds grandes, principalmente em `apps/adventure/management/commands/`.
Esse e o ponto que mais pode melhorar depois da separacao por apps.

Padrao recomendado:

```txt
apps/adventure/
|-- management/commands/
|   |-- seed_es.py
|   |-- seed_es_full.py
|   |-- seed_es_sections.py
|   |-- seed_es_f2_sections.py
|   |-- seed_es_f3_sections.py
|   |-- seed_es_f4_sections.py
|   |-- seed_es_f5_sections.py
|   `-- seed_voice.py
`-- seed_data/
    |-- es_characters.py
    |-- es_voice.py
    |-- es_f1_sections.py
    |-- es_f2_sections.py
    |-- es_f3_sections.py
    |-- es_f4_sections.py
    `-- es_f5_sections.py
```

Os comandos podem continuar existindo, mas deveriam ficar finos: eles chamam
funcoes/dados de `seed_data/` em vez de carregar dezenas de milhares de linhas
diretamente no command.

Automacao local para rodar migrations e seeds fica em:

```bat
bats\backend\setup.bat
bats\backend\migrations.bat
```

Nao recrie `backend\bats`; scripts Windows do projeto ficam centralizados em
`bats/`.

## Validacao

```powershell
cd backend
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py makemigrations --check
```

Para banco novo:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
```

Para banco legado com tabelas `content_*` ja existentes:

```powershell
.\.venv\Scripts\python.exe manage.py migrate --fake-initial
```
