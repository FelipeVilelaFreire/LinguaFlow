from rest_framework import serializers

from apps.learning.serializers import PhraseSerializer

from .models import AdventureChapter, AdventurePhase, AdventurePhaseCompletion, AdventureProgress


class AdventurePhaseSerializer(serializers.ModelSerializer):
    is_completed = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()

    class Meta:
        model = AdventurePhase
        fields = ["id", "number", "title", "narrative_intro", "narrative_outro", "key_words", "scenario_slug", "phrase_count", "is_boss", "is_completed", "score"]

    def get_is_completed(self, phase):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return AdventurePhaseCompletion.objects.filter(user=request.user, phase=phase).exists()

    def get_score(self, phase):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return None
        completion = AdventurePhaseCompletion.objects.filter(user=request.user, phase=phase).first()
        return completion.score if completion else None


class AdventureProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdventureProgress
        fields = ["current_phase", "reward_unlocked", "started_at", "completed_at"]


class AdventureChapterSerializer(serializers.ModelSerializer):
    phases = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    language_code = serializers.CharField(source="language.code", read_only=True)

    class Meta:
        model = AdventureChapter
        fields = ["id", "slug", "language_code", "level", "order", "title", "subtitle", "background", "boss_name", "boss_intro", "reward_name", "reward_description", "phases", "progress"]

    def get_phases(self, chapter):
        return AdventurePhaseSerializer(chapter.phases.all(), many=True, context=self.context).data

    def get_progress(self, chapter):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return None
        progress = AdventureProgress.objects.filter(user=request.user, chapter=chapter).first()
        return AdventureProgressSerializer(progress).data if progress else None


class AdventureChapterListSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()
    language_code = serializers.CharField(source="language.code", read_only=True)
    total_phases = serializers.IntegerField(source="phases.count", read_only=True)

    class Meta:
        model = AdventureChapter
        fields = ["id", "slug", "language_code", "level", "order", "title", "subtitle", "background", "reward_name", "total_phases", "progress"]

    def get_progress(self, chapter):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return None
        progress = AdventureProgress.objects.filter(user=request.user, chapter=chapter).first()
        return AdventureProgressSerializer(progress).data if progress else None
