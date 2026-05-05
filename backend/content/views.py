from apps.accounts.views import AuthViewSet
from apps.goals.views import GoalViewSet
from apps.learning.views import PhraseViewSet, ScenarioViewSet, StudyDayViewSet
from apps.progress.views import FavoriteViewSet, ProgressViewSet

__all__ = [
    "AuthViewSet",
    "FavoriteViewSet",
    "GoalViewSet",
    "PhraseViewSet",
    "ProgressViewSet",
    "ScenarioViewSet",
    "StudyDayViewSet",
]
