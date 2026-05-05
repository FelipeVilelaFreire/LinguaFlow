from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.goals.models import Goal
from apps.progress.models import StudyDayCompletion

from .models import Phrase, Scenario, StudyDay
from .serializers import PhraseSerializer, ScenarioSerializer, StudyDaySerializer


class PhraseViewSet(viewsets.ModelViewSet):
    serializer_class = PhraseSerializer

    def get_queryset(self):
        queryset = Phrase.objects.select_related("source_language", "target_language", "scenario").order_by("id")
        category = self.request.query_params.get("category")
        scenario = self.request.query_params.get("scenario")
        if category:
            queryset = queryset.filter(category__iexact=category)
        if scenario:
            queryset = queryset.filter(scenario__slug=scenario)
        return queryset


class ScenarioViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ScenarioSerializer

    def get_queryset(self):
        return Scenario.objects.annotate(phrase_count=Count("phrases")).order_by("title")


class StudyDayViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StudyDaySerializer
    queryset = StudyDay.objects.select_related("lesson", "lesson__scenario").prefetch_related(
        "lesson__phrases",
        "lesson__phrases__source_language",
        "lesson__phrases__target_language",
    )

    @action(detail=False, methods=["get"])
    def today(self, request):
        goal = Goal.objects.filter(user=request.user, is_active=True).first() if request.user.is_authenticated else None
        day_number = (goal.completed_lessons + 1) if goal else 1
        queryset = self.get_queryset()
        if goal:
            queryset = queryset.filter(
                lesson__phrases__source_language=goal.source_language,
                lesson__phrases__target_language=goal.target_language,
                lesson__phrases__difficulty=goal.target_level,
            ).distinct()
        study_day = queryset.filter(day_number=day_number).first() or queryset.filter(is_active=True).first()
        if not study_day:
            return Response({"detail": "No active study day found."}, status=404)
        return Response(self.get_serializer(study_day).data)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def complete(self, request, pk=None):
        study_day = self.get_object()
        goal = Goal.objects.filter(user=request.user, is_active=True).first()
        completion, created = StudyDayCompletion.objects.get_or_create(user=request.user, study_day=study_day, goal=goal)
        if goal and created:
            phrase_count = study_day.lesson.phrases.count()
            goal.learned_phrases = min(goal.total_phrases, goal.learned_phrases + phrase_count)
            goal.completed_lessons += 1
            goal.streak_days += 1
            goal.save(update_fields=["learned_phrases", "completed_lessons", "streak_days"])
        return Response({"completed": True, "created": created, "completed_at": completion.completed_at})
