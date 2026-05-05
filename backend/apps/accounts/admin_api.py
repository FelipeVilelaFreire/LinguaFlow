from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.goals.models import Goal
from apps.learning.models import Language, Lesson, Phrase, Scenario, StudyDay
from apps.progress.models import Favorite, StudyDayCompletion, UserProgress


User = get_user_model()


class AdminDashboardViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=["get"])
    def summary(self, request):
        return Response(
            {
                "users": User.objects.count(),
                "staff_users": User.objects.filter(is_staff=True).count(),
                "active_goals": Goal.objects.filter(is_active=True).count(),
                "goals": Goal.objects.count(),
                "languages": Language.objects.count(),
                "scenarios": Scenario.objects.count(),
                "lessons": Lesson.objects.count(),
                "study_days": StudyDay.objects.count(),
                "phrases": Phrase.objects.count(),
                "completions": StudyDayCompletion.objects.count(),
                "favorites": Favorite.objects.count(),
                "progress_entries": UserProgress.objects.count(),
            }
        )

    @action(detail=False, methods=["get"])
    def users(self, request):
        users = User.objects.order_by("-date_joined")[:100]
        return Response(
            [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser,
                    "is_active": user.is_active,
                    "date_joined": user.date_joined,
                    "goal_count": Goal.objects.filter(user=user).count(),
                    "completion_count": StudyDayCompletion.objects.filter(user=user).count(),
                }
                for user in users
            ]
        )

    @action(detail=False, methods=["get"])
    def goals(self, request):
        goals = Goal.objects.select_related("user", "source_language", "target_language").order_by("-is_active", "-id")[:150]
        return Response(
            [
                {
                    "id": goal.id,
                    "user": goal.user.username if goal.user else None,
                    "source_language": goal.source_language.code,
                    "target_language": goal.target_language.code,
                    "current_level": goal.current_level,
                    "target_level": goal.target_level,
                    "duration_days": goal.duration_days,
                    "session_minutes": goal.session_minutes,
                    "study_weekdays": goal.study_weekdays,
                    "is_active": goal.is_active,
                    "learned_phrases": goal.learned_phrases,
                    "total_phrases": goal.total_phrases,
                    "completed_lessons": goal.completed_lessons,
                    "streak_days": goal.streak_days,
                }
                for goal in goals
            ]
        )

    @action(detail=False, methods=["get"])
    def content(self, request):
        languages = Language.objects.order_by("code")
        scenarios = Scenario.objects.order_by("slug")
        phrase_counts = {
            f"{item['source_language__code']}->{item['target_language__code']} {item['difficulty']}": item["count"]
            for item in Phrase.objects.values("source_language__code", "target_language__code", "difficulty").annotate(count=Count("id"))
        }
        return Response(
            {
                "languages": [{"id": item.id, "code": item.code, "name": item.name} for item in languages],
                "scenarios": [
                    {
                        "id": item.id,
                        "slug": item.slug,
                        "title": item.title,
                        "phrase_count": Phrase.objects.filter(scenario=item).count(),
                        "lesson_count": Lesson.objects.filter(scenario=item).count(),
                    }
                    for item in scenarios
                ],
                "phrase_counts": phrase_counts,
                "lesson_count": Lesson.objects.count(),
                "study_day_count": StudyDay.objects.count(),
            }
        )
