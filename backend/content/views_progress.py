from rest_framework import mixins, viewsets

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


class ProgressViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = ProgressSerializer

    def get_queryset(self):
        queryset = UserProgress.objects.select_related("phrase", "phrase__source_language", "phrase__target_language", "phrase__scenario").order_by("-updated_at")
        if self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        return queryset.filter(user__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user if self.request.user.is_authenticated else None)
