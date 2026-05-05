import calendar
from collections import defaultdict
from datetime import date

from django.utils import timezone
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Goal, Language, Phrase, StudyDayCompletion
from .serializers import GoalSerializer, OnboardingSerializer


class GoalViewSet(mixins.DestroyModelMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = GoalSerializer
    queryset = Goal.objects.select_related("source_language", "target_language", "user").order_by("-id")

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        return queryset.filter(user__isnull=True)

    @action(detail=False, methods=["get"])
    def current(self, request):
        goal = self.get_queryset().filter(is_active=True).first() or self.get_queryset().first()
        if not goal:
            return Response({"detail": "No goal found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(self.get_serializer(goal).data)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def history(self, request):
        today = timezone.localdate()
        try:
            year = int(request.query_params.get("year", today.year))
            month = int(request.query_params.get("month", today.month))
            if month < 1 or month > 12:
                raise ValueError
        except ValueError:
            return Response({"detail": "Invalid month or year."}, status=status.HTTP_400_BAD_REQUEST)

        _, last_day = calendar.monthrange(year, month)
        start_date = date(year, month, 1)
        end_date = date(year, month, last_day)
        goals = list(self.get_queryset().order_by("-is_active", "-id"))
        completions = (
            StudyDayCompletion.objects.filter(user=request.user, completed_at__date__gte=start_date, completed_at__date__lte=end_date)
            .select_related("goal", "study_day", "study_day__lesson")
            .order_by("completed_at")
        )
        completions_by_goal_and_day = defaultdict(list)
        for completion in completions:
            if not completion.goal_id:
                continue
            completed_day = timezone.localtime(completion.completed_at).date().isoformat()
            completions_by_goal_and_day[(completion.goal_id, completed_day)].append(
                {
                    "id": completion.id,
                    "lesson_title": completion.study_day.lesson.title,
                    "study_day": completion.study_day.day_number,
                    "completed_at": completion.completed_at,
                }
            )

        goal_payload = []
        for goal in goals:
            days = []
            for day_number in range(1, last_day + 1):
                current = date(year, month, day_number)
                day_key = current.isoformat()
                day_completions = completions_by_goal_and_day[(goal.id, day_key)]
                days.append(
                    {
                        "date": day_key,
                        "planned": current.weekday() in (goal.study_weekdays or []),
                        "completed": len(day_completions) > 0,
                        "completion_count": len(day_completions),
                        "lessons": day_completions,
                    }
                )
            goal_payload.append({"goal": self.get_serializer(goal).data, "days": days})

        return Response({"year": year, "month": month, "goals": goal_payload})

    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def onboarding(self, request):
        serializer = OnboardingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        source = Language.objects.get(code=data["source_language"].upper())
        target = Language.objects.get(code=data["target_language"].upper())
        total_phrases = Phrase.objects.filter(source_language=source, target_language=target, difficulty=data["target_level"]).count() or 300
        Goal.objects.filter(user=request.user).update(is_active=False)
        goal = Goal.objects.create(
            user=request.user,
            source_language=source,
            target_language=target,
            target_level=data["target_level"],
            duration_days=data["duration_days"],
            start_date=timezone.localdate(),
            total_phrases=total_phrases,
            study_weekdays=data["study_weekdays"],
            session_minutes=data["session_minutes"],
            is_active=True,
        )
        return Response(self.get_serializer(goal).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def activate(self, request, pk=None):
        goal = self.get_object()
        Goal.objects.filter(user=request.user).update(is_active=False)
        goal.is_active = True
        goal.save(update_fields=["is_active"])
        return Response(self.get_serializer(goal).data)

    def destroy(self, request, *args, **kwargs):
        goal = self.get_object()
        was_active = goal.is_active
        goal.delete()
        next_goal = None
        if was_active:
            next_goal = self.get_queryset().first()
            if next_goal:
                next_goal.is_active = True
                next_goal.save(update_fields=["is_active"])
        return Response({"current_goal": self.get_serializer(next_goal).data if next_goal else None})
