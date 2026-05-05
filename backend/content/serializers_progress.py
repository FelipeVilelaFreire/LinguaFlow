from rest_framework import serializers

from .models import Favorite, Phrase, UserProgress
from .serializers_learning import PhraseSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    phrase = PhraseSerializer(read_only=True)
    phrase_id = serializers.PrimaryKeyRelatedField(source="phrase", queryset=Phrase.objects.all(), write_only=True)

    class Meta:
        model = Favorite
        fields = ["id", "phrase", "phrase_id", "created_at"]


class ProgressSerializer(serializers.ModelSerializer):
    phrase = PhraseSerializer(read_only=True)
    phrase_id = serializers.PrimaryKeyRelatedField(source="phrase", queryset=Phrase.objects.all(), write_only=True)

    class Meta:
        model = UserProgress
        fields = ["id", "phrase", "phrase_id", "status", "updated_at"]
