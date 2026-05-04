from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from content.views import AuthViewSet, FavoriteViewSet, GoalViewSet, PhraseViewSet, ProgressViewSet, ScenarioViewSet, StudyDayViewSet

router = DefaultRouter()
router.register("auth", AuthViewSet, basename="auth")
router.register("phrases", PhraseViewSet, basename="phrase")
router.register("favorites", FavoriteViewSet, basename="favorite")
router.register("progress", ProgressViewSet, basename="progress")
router.register("scenarios", ScenarioViewSet, basename="scenario")
router.register("study-days", StudyDayViewSet, basename="study-day")
router.register("goals", GoalViewSet, basename="goal")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
