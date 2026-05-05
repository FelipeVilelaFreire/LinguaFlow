# LinguaFlow Backend Architecture

LinguaFlow now uses real Django apps grouped by product domain. The goal is to
make the backend easy to navigate as the product grows: auth code lives with
auth, learning content lives with learning, plans live with goals, and user
activity lives with progress.

## Project Tree

```text
backend/
  manage.py
  linguaflow/
    settings.py
    urls.py
    wsgi.py
  apps/
    accounts/
      apps.py
      serializers.py
      views.py
    learning/
      apps.py
      admin.py
      models.py
      serializers.py
      views.py
      management/commands/seed_content.py
      migrations/
    goals/
      apps.py
      admin.py
      models.py
      serializers.py
      views.py
      migrations/
    progress/
      apps.py
      admin.py
      models.py
      serializers.py
      views.py
      migrations/
  content/
    models.py
    serializers.py
    views.py
    seeds/
    migrations/
```

`linguaflow/` is the Django project. It owns global settings, installed apps,
router registration, CORS, DRF, and JWT configuration.

`apps/` contains the real Django apps.

`content/` remains as a compatibility package for old imports and seed data. It
is no longer the main app installed by Django.

## Installed Apps

The domain apps are registered in `linguaflow/settings.py`:

```python
INSTALLED_APPS = [
    ...
    "apps.accounts.apps.AccountsConfig",
    "apps.learning.apps.LearningConfig",
    "apps.goals.apps.GoalsConfig",
    "apps.progress.apps.ProgressConfig",
]
```

The old `content` app is intentionally not installed anymore. Its files remain
only as import compatibility and seed helpers.

## Domains

### Accounts

Path:

```text
apps/accounts/
```

Owns authentication and user identity.

Main classes:

```text
RegisterSerializer
LoginSerializer
UserSerializer
AuthViewSet
```

Endpoints:

```text
POST /api/auth/register/
POST /api/auth/login/
GET  /api/auth/me/
POST /api/auth/refresh/
```

This app does not define a custom user model yet. It uses Django's built-in User
model and exposes the auth API around it.

### Learning

Path:

```text
apps/learning/
```

Owns the study material.

Models:

```text
Language
Scenario
Phrase
Lesson
StudyDay
```

ViewSets:

```text
PhraseViewSet
ScenarioViewSet
StudyDayViewSet
```

Endpoints:

```text
GET /api/scenarios/
GET /api/phrases/
GET /api/phrases/?scenario=restaurant
GET /api/study-days/today/
POST /api/study-days/{id}/complete/
```

This app answers: "What can the user study?"

### Goals

Path:

```text
apps/goals/
```

Owns user study plans and study areas.

Model:

```text
Goal
```

Important fields:

```text
source_language
target_language
target_level
duration_days
study_weekdays
session_minutes
is_active
completed_lessons
learned_phrases
streak_days
```

ViewSet:

```text
GoalViewSet
```

Endpoints:

```text
GET    /api/goals/
GET    /api/goals/current/
POST   /api/goals/onboarding/
POST   /api/goals/{id}/activate/
DELETE /api/goals/{id}/
GET    /api/goals/history/?year=YYYY&month=M
```

This app answers: "What is the user trying to accomplish and how is the plan
configured?"

### Progress

Path:

```text
apps/progress/
```

Owns user activity and saved learning state.

Models:

```text
StudyDayCompletion
UserProgress
Favorite
```

ViewSets:

```text
FavoriteViewSet
ProgressViewSet
```

Endpoints:

```text
GET    /api/favorites/
POST   /api/favorites/
DELETE /api/favorites/{id}/
GET    /api/progress/
POST   /api/progress/
PATCH  /api/progress/{id}/
```

`StudyDayCompletion` links a completed study day to the user and the active
goal. That lets the history page show activity separately for German, Spanish,
or any other area.

## API Routing

The router is still centralized in:

```text
linguaflow/urls.py
```

Flow:

```text
HTTP request
  -> linguaflow/urls.py
  -> domain ViewSet
  -> domain Serializer
  -> domain Model
  -> JSON response
```

Example:

```text
POST /api/goals/onboarding/
  -> apps.goals.views.GoalViewSet.onboarding()
  -> apps.goals.serializers.OnboardingSerializer
  -> apps.goals.models.Goal
  -> apps.goals.serializers.GoalSerializer
```

## Database Compatibility

The code is split into new Django apps, but the models keep the old table names
with `db_table`.

Examples:

```python
class Goal(models.Model):
    ...
    class Meta:
        db_table = "content_goal"
```

This keeps existing SQLite data usable while giving the codebase a real app
structure.

Current table names remain:

```text
content_language
content_scenario
content_phrase
content_lesson
content_studyday
content_goal
content_studydaycompletion
content_userprogress
content_favorite
```

## Migration Notes

Because the database may already have the old `content_*` tables, an existing
database should apply the new initial migrations with:

```powershell
python manage.py migrate --fake-initial
```

For a fresh database, normal migrate is enough:

```powershell
python manage.py migrate
```

After the migration state is aligned, future migrations can be created and
applied normally.

Recommended validation flow after this architecture split:

```powershell
python manage.py migrate --fake-initial
python manage.py check
python manage.py runserver
```

If the database is brand new and does not contain the legacy `content_*` tables,
use the normal migration command instead:

```powershell
python manage.py migrate
python manage.py seed_content
python manage.py runserver
```

The extra legacy-safety migrations under `apps/goals/migrations/` and
`apps/progress/migrations/` make sure older local databases have the newer
columns required by the planning and history features:

```text
content_goal.study_weekdays
content_goal.session_minutes
content_studydaycompletion.goal_id
```

## Compatibility Package

The old `content/` package remains with these facades:

```text
content/models.py
content/serializers.py
content/views.py
```

They re-export classes from the new apps, so older imports continue to work:

```python
from content.models import Goal, Phrase
from content.views import GoalViewSet
```

New code should import from the real app directly:

```python
from apps.goals.models import Goal
from apps.learning.models import Phrase
from apps.progress.models import StudyDayCompletion
```

## Rules For New Backend Code

Use these boundaries:

- Login, registration, current user, and token behavior go in `apps/accounts/`.
- Languages, scenarios, phrases, lessons, and study days go in `apps/learning/`.
- Study plans, active areas, routines, onboarding, and goal reports go in
  `apps/goals/`.
- Completions, favorites, phrase progress, and activity state go in
  `apps/progress/`.
- API registration stays in `linguaflow/urls.py`.
- Seed content currently lives under `content/seeds/` and is exposed through
  `apps.learning.management.commands.seed_content`.

Import rule:

```python
# Preferred in new code
from apps.goals.models import Goal
from apps.learning.models import Phrase
from apps.progress.models import Favorite

# Compatibility only
from content.models import Goal
```

The `content.*` imports should be treated as a bridge for legacy code and seed
helpers. New production code should use the domain apps directly.

## Development Commands

Backend:

```powershell
cd C:\Users\Felipe.Freire\Documents\Documentos\Sites\LinguaFlow\LinguaFlow\backend
conda activate linguaflow
python manage.py migrate --fake-initial
python manage.py check
python manage.py runserver
```

Frontend:

```powershell
cd C:\Users\Felipe.Freire\Documents\Documentos\Sites\LinguaFlow\LinguaFlow\frontend-web
npm run dev
```

Seed content:

```powershell
python manage.py seed_content
```

Current seeded course pairs:

```text
PT -> DE: A1, A2, B1
PT -> ES: A1, A2, B1
EN -> DE: A1, A2, B1
```

Create new migrations after model changes:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Check migration drift:

```powershell
python manage.py makemigrations --check
```

## Summary

The backend is now organized as real Django apps by domain, while preserving old
database table names for safety. This gives the project a cleaner structure
without discarding existing local data.
