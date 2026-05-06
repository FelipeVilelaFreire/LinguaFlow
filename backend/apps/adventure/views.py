from django.utils import timezone
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.goals.models import Goal
from apps.learning.serializers import PhraseSerializer

from .models import AdventureChapter, AdventurePhase, AdventurePhaseCompletion, AdventureProgress
from .serializers import AdventureChapterListSerializer, AdventureChapterSerializer


class AdventureChapterViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = AdventureChapter.objects.prefetch_related("phases").select_related("language")
    lookup_field = "slug"

    def get_serializer_class(self):
        return AdventureChapterSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        language = self.request.query_params.get("language")
        if language:
            qs = qs.filter(language__code=language.upper())
        elif self.request.user.is_authenticated:
            goal = Goal.objects.filter(user=self.request.user, is_active=True).select_related("target_language").first()
            if goal:
                qs = qs.filter(language=goal.target_language)
        return qs


class AdventurePhaseViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = AdventurePhase.objects.select_related("chapter__language")
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        from .serializers import AdventurePhaseSerializer
        return AdventurePhaseSerializer

    @action(detail=True, methods=["get"])
    def phrases(self, request, pk=None):
        phase = self.get_object()
        source_code = self._get_source_code(request)
        phrases = phase.get_phrases(source_code)
        if not phrases.exists():
            return Response({"detail": "No phrases found for this phase. Run seed_content first."}, status=status.HTTP_404_NOT_FOUND)
        return Response(PhraseSerializer(phrases, many=True).data)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        phase = self.get_object()
        score = max(0, min(100, int(request.data.get("score", 0))))

        completion, created = AdventurePhaseCompletion.objects.update_or_create(
            user=request.user,
            phase=phase,
            defaults={"score": score},
        )

        progress, _ = AdventureProgress.objects.get_or_create(
            user=request.user,
            chapter=phase.chapter,
        )

        next_phase = phase.chapter.phases.filter(number__gt=phase.number).order_by("number").first()

        if next_phase and progress.current_phase <= phase.number:
            progress.current_phase = next_phase.number
            progress.save(update_fields=["current_phase"])

        if phase.is_boss:
            progress.reward_unlocked = True
            progress.completed_at = timezone.now()
            progress.save(update_fields=["reward_unlocked", "completed_at"])

        return Response({
            "score": score,
            "phase_number": phase.number,
            "is_boss": phase.is_boss,
            "reward_unlocked": progress.reward_unlocked,
            "current_phase": progress.current_phase,
            "chapter_completed": progress.completed_at is not None,
        })

    def _get_source_code(self, request):
        if request.user.is_authenticated:
            goal = Goal.objects.filter(user=request.user, is_active=True).select_related("source_language").first()
            if goal:
                return goal.source_language.code
        return request.query_params.get("source", "PT")
