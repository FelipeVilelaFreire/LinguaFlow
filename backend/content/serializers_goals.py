from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers

from .models import Goal, StudyDayCompletion
from .serializers_learning import LanguageSerializer


class GoalSerializer(serializers.ModelSerializer):
    source_language = LanguageSerializer(read_only=True)
    target_language = LanguageSerializer(read_only=True)
    progress_percent = serializers.SerializerMethodField()
    is_study_day_today = serializers.SerializerMethodField()
    next_study_date = serializers.SerializerMethodField()

    class Meta:
        model = Goal
        fields = [
            "id",
            "user",
            "source_language",
            "target_language",
            "target_level",
            "duration_days",
            "start_date",
            "total_phrases",
            "learned_phrases",
            "completed_lessons",
            "streak_days",
            "study_weekdays",
            "session_minutes",
            "is_study_day_today",
            "next_study_date",
            "is_active",
            "progress_percent",
        ]
        read_only_fields = ["user", "learned_phrases", "completed_lessons", "streak_days", "is_active", "progress_percent"]

    def get_progress_percent(self, obj: Goal) -> int:
        if obj.total_phrases == 0:
            return 0
        return min(100, round((obj.learned_phrases / obj.total_phrases) * 100))

    def get_is_study_day_today(self, obj: Goal) -> bool:
        return timezone.localdate().weekday() in obj.study_weekdays

    def get_next_study_date(self, obj: Goal):
        today = timezone.localdate()
        weekdays = obj.study_weekdays or []
        if not weekdays:
            return None
        for offset in range(0, 8):
            candidate = today + timedelta(days=offset)
            if candidate.weekday() in weekdays:
                return candidate.isoformat()
        return None


class OnboardingSerializer(serializers.Serializer):
    source_language = serializers.CharField(max_length=2)
    target_language = serializers.CharField(max_length=2)
    target_level = serializers.CharField(max_length=8)
    duration_days = serializers.IntegerField(min_value=7, max_value=365)
    study_weekdays = serializers.ListField(child=serializers.IntegerField(min_value=0, max_value=6), allow_empty=True)
    session_minutes = serializers.IntegerField(min_value=10, max_value=180)

    def validate_study_weekdays(self, value):
        return sorted(set(value))


class StudyCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDayCompletion
        fields = ["id", "study_day", "completed_at"]
