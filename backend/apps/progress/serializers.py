from rest_framework import serializers

from apps.learning.models import Phrase
from apps.learning.serializers import PhraseSerializer

from .models import Favorite, UserProgress


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
        fields = [
            "id",
            "phrase",
            "phrase_id",
            "status",
            "correct_count",
            "incorrect_count",
            "interval_days",
            "review_due",
            "last_answer",
            "updated_at",
        ]
