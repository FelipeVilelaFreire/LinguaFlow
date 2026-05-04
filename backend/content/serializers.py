from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from .models import Favorite, Goal, Language, Lesson, Phrase, Scenario, StudyDay, StudyDayCompletion, UserProgress


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name"]


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, min_length=6)

    def validate_username(self, value: str) -> str:
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs["username"], password=attrs["password"])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        attrs["user"] = user
        return attrs


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["id", "code", "name"]


class ScenarioSerializer(serializers.ModelSerializer):
    phrase_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Scenario
        fields = ["id", "slug", "title", "description", "phrase_count"]


class PhraseSerializer(serializers.ModelSerializer):
    source_language = LanguageSerializer(read_only=True)
    target_language = LanguageSerializer(read_only=True)
    source_language_id = serializers.PrimaryKeyRelatedField(source="source_language", queryset=Language.objects.all(), write_only=True)
    target_language_id = serializers.PrimaryKeyRelatedField(source="target_language", queryset=Language.objects.all(), write_only=True)
    scenario_title = serializers.CharField(source="scenario.title", read_only=True)

    class Meta:
        model = Phrase
        fields = [
            "id",
            "source_language",
            "target_language",
            "source_language_id",
            "target_language_id",
            "source_text",
            "target_text",
            "category",
            "scenario",
            "scenario_title",
            "difficulty",
        ]


class LessonSerializer(serializers.ModelSerializer):
    scenario = ScenarioSerializer(read_only=True)
    phrases = PhraseSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ["id", "title", "day_number", "scenario", "phrases", "video_title", "video_url", "video_duration"]


class StudyDaySerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)
    completed = serializers.SerializerMethodField()

    class Meta:
        model = StudyDay
        fields = ["id", "day_number", "lesson", "is_active", "completed"]

    def get_completed(self, obj: StudyDay) -> bool:
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return obj.completions.filter(user=request.user).exists()


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


class GoalSerializer(serializers.ModelSerializer):
    source_language = LanguageSerializer(read_only=True)
    target_language = LanguageSerializer(read_only=True)
    progress_percent = serializers.SerializerMethodField()

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
            "is_active",
            "progress_percent",
        ]
        read_only_fields = ["user", "learned_phrases", "completed_lessons", "streak_days", "is_active", "progress_percent"]

    def get_progress_percent(self, obj: Goal) -> int:
        if obj.total_phrases == 0:
            return 0
        return min(100, round((obj.learned_phrases / obj.total_phrases) * 100))


class OnboardingSerializer(serializers.Serializer):
    source_language = serializers.CharField(max_length=2)
    target_language = serializers.CharField(max_length=2)
    target_level = serializers.CharField(max_length=8)
    duration_days = serializers.IntegerField(min_value=7, max_value=365)


class StudyCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDayCompletion
        fields = ["id", "study_day", "completed_at"]
