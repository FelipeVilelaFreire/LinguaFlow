from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.accounts.admin_api import AdminDashboardViewSet
from apps.accounts.views import AuthViewSet
from apps.adventure.views import AdventureChapterViewSet, AdventurePhaseViewSet
from apps.goals.views import GoalViewSet
from apps.learning.views import PhraseViewSet, ScenarioViewSet, StudyDayViewSet
from apps.progress.views import FavoriteViewSet, ProgressViewSet

router = DefaultRouter()
router.register("auth", AuthViewSet, basename="auth")
router.register("admin-dashboard", AdminDashboardViewSet, basename="admin-dashboard")
router.register("phrases", PhraseViewSet, basename="phrase")
router.register("favorites", FavoriteViewSet, basename="favorite")
router.register("progress", ProgressViewSet, basename="progress")
router.register("scenarios", ScenarioViewSet, basename="scenario")
router.register("study-days", StudyDayViewSet, basename="study-day")
router.register("goals", GoalViewSet, basename="goal")
router.register("adventure/chapters", AdventureChapterViewSet, basename="adventure-chapter")
router.register("adventure/phases", AdventurePhaseViewSet, basename="adventure-phase")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
