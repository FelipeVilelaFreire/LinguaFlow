from rest_framework import serializers

from .models import Language, Lesson, Phrase, Scenario, StudyDay


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
