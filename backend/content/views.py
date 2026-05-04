from django.db.models import Count
from django.utils import timezone
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Favorite, Goal, Language, Phrase, Scenario, StudyDay, StudyDayCompletion, UserProgress
from .serializers import (
    FavoriteSerializer,
    GoalSerializer,
    LoginSerializer,
    OnboardingSerializer,
    PhraseSerializer,
    ProgressSerializer,
    RegisterSerializer,
    ScenarioSerializer,
    StudyDaySerializer,
    UserSerializer,
)


def auth_payload(user):
    refresh = RefreshToken.for_user(user)
    return {"access": str(refresh.access_token), "refresh": str(refresh), "user": UserSerializer(user).data}


class AuthViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=["post"], permission_classes=[])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(auth_payload(user), status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"], permission_classes=[])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(auth_payload(serializer.validated_data["user"]))

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        return Response(UserSerializer(request.user).data)

    @action(detail=False, methods=["post"], permission_classes=[])
    def refresh(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            refresh = RefreshToken(refresh_token)
        except Exception:
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"access": str(refresh.access_token)})


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
    queryset = Scenario.objects.annotate(phrase_count=Count("phrases")).order_by("title")


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
            return Response({"detail": "No active study day found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(self.get_serializer(study_day).data)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def complete(self, request, pk=None):
        study_day = self.get_object()
        completion, created = StudyDayCompletion.objects.get_or_create(user=request.user, study_day=study_day)
        goal = Goal.objects.filter(user=request.user, is_active=True).first()
        if goal and created:
            phrase_count = study_day.lesson.phrases.count()
            goal.learned_phrases = min(goal.total_phrases, goal.learned_phrases + phrase_count)
            goal.completed_lessons += 1
            goal.streak_days += 1
            goal.save(update_fields=["learned_phrases", "completed_lessons", "streak_days"])
        return Response({"completed": True, "created": created, "completed_at": completion.completed_at})


class FavoriteViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        queryset = Favorite.objects.select_related("phrase", "phrase__source_language", "phrase__target_language", "phrase__scenario").order_by("-created_at")
        if self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        return queryset.filter(user__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user if self.request.user.is_authenticated else None)


class ProgressViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = ProgressSerializer

    def get_queryset(self):
        queryset = UserProgress.objects.select_related("phrase", "phrase__source_language", "phrase__target_language", "phrase__scenario").order_by("-updated_at")
        if self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        return queryset.filter(user__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user if self.request.user.is_authenticated else None)


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
