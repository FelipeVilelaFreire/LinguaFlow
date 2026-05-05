from datetime import timedelta

from django.utils import timezone
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.learning.models import Phrase

from .models import Favorite, UserProgress
from .serializers import FavoriteSerializer, ProgressSerializer


class FavoriteViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        queryset = Favorite.objects.select_related("phrase", "phrase__source_language", "phrase__target_language", "phrase__scenario").order_by("-created_at")
        if self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        return queryset.filter(user__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user if self.request.user.is_authenticated else None)

    def create(self, request, *args, **kwargs):
        phrase_id = request.data.get("phrase_id")
        if not phrase_id:
            return Response({"detail": "phrase_id is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            phrase = Phrase.objects.get(id=phrase_id)
        except Phrase.DoesNotExist:
            return Response({"detail": "Phrase not found."}, status=status.HTTP_404_NOT_FOUND)

        favorite, created = Favorite.objects.get_or_create(
            user=request.user if request.user.is_authenticated else None,
            phrase=phrase,
        )
        serializer = self.get_serializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def mark(self, request):
        phrase_id = request.data.get("phrase_id")
        is_correct = bool(request.data.get("correct"))
        answer = str(request.data.get("answer", ""))[:255]
        if not phrase_id:
            return Response({"detail": "phrase_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            phrase = Phrase.objects.get(id=phrase_id)
        except Phrase.DoesNotExist:
            return Response({"detail": "Phrase not found."}, status=status.HTTP_404_NOT_FOUND)
        progress, _ = UserProgress.objects.get_or_create(
            user=request.user if request.user.is_authenticated else None,
            phrase=phrase,
        )

        if is_correct:
            progress.correct_count += 1
            progress.interval_days = next_interval(progress.interval_days, progress.correct_count)
            progress.status = UserProgress.STATUS_MASTERED if progress.correct_count >= 4 else UserProgress.STATUS_LEARNING
        else:
            progress.incorrect_count += 1
            progress.interval_days = 1
            progress.status = UserProgress.STATUS_LEARNING

        progress.last_answer = answer
        progress.review_due = timezone.localdate() + timedelta(days=progress.interval_days)
        progress.save(update_fields=["correct_count", "incorrect_count", "interval_days", "status", "last_answer", "review_due", "updated_at"])
        return Response(self.get_serializer(progress).data)


def next_interval(current_interval: int, correct_count: int) -> int:
    if correct_count <= 1:
        return 1
    if correct_count == 2:
        return 3
    if correct_count == 3:
        return 7
    return min(30, max(14, current_interval * 2))


class ProgressViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = ProgressSerializer

    def get_queryset(self):
        queryset = UserProgress.objects.select_related("phrase", "phrase__source_language", "phrase__target_language", "phrase__scenario").order_by("-updated_at")
        if self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        return queryset.filter(user__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user if self.request.user.is_authenticated else None)
