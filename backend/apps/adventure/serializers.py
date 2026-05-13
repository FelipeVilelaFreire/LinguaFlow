from rest_framework import serializers

from apps.learning.serializers import PhraseSerializer
from apps.progress.models import WordMastery

from .models import (
    AdventureCharacter,
    AdventureChapter,
    AdventureItem,
    AdventurePhase,
    AdventurePhaseCompletion,
    AdventureProgress,
    AdventureSectionProgress,
    PhaseSection,
    UserCharacterMet,
    UserInventoryItem,
)


# ─── Phase ────────────────────────────────────────────────────────────────────

class AdventurePhaseSerializer(serializers.ModelSerializer):
    is_completed       = serializers.SerializerMethodField()
    score              = serializers.SerializerMethodField()
    completed_sections = serializers.SerializerMethodField()

    class Meta:
        model  = AdventurePhase
        fields = [
            "id", "number", "title", "narrative_intro", "narrative_outro",
            "key_words", "scenario_slug", "phrase_count",
            "phase_type", "is_boss",
            "is_completed", "score", "completed_sections",
        ]

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

    def get_completed_sections(self, phase):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return 0
        # A completed phase always has all 6 sections done
        if AdventurePhaseCompletion.objects.filter(user=request.user, phase=phase).exists():
            return 6
        sp = AdventureSectionProgress.objects.filter(user=request.user, phase=phase).first()
        return sp.completed_sections if sp else 0


# ─── Progress ─────────────────────────────────────────────────────────────────

class AdventureProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model  = AdventureProgress
        fields = ["current_phase", "reward_unlocked", "started_at", "completed_at"]


# ─── Chapter ──────────────────────────────────────────────────────────────────

class AdventureChapterSerializer(serializers.ModelSerializer):
    phases        = serializers.SerializerMethodField()
    progress      = serializers.SerializerMethodField()
    language_code = serializers.CharField(source="language.code", read_only=True)

    class Meta:
        model  = AdventureChapter
        fields = [
            "id", "slug", "language_code", "level", "order",
            "title", "subtitle", "background",
            "boss_name", "boss_intro",
            "reward_name", "reward_description",
            "phases", "progress",
        ]

    def get_phases(self, chapter):
        return AdventurePhaseSerializer(chapter.phases.all(), many=True, context=self.context).data

    def get_progress(self, chapter):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return None
        progress = AdventureProgress.objects.filter(user=request.user, chapter=chapter).first()
        return AdventureProgressSerializer(progress).data if progress else None


class AdventureChapterListSerializer(serializers.ModelSerializer):
    progress      = serializers.SerializerMethodField()
    language_code = serializers.CharField(source="language.code", read_only=True)
    total_phases  = serializers.IntegerField(source="phases.count", read_only=True)

    class Meta:
        model  = AdventureChapter
        fields = [
            "id", "slug", "language_code", "level", "order",
            "title", "subtitle", "background",
            "reward_name", "total_phases", "progress",
        ]

    def get_progress(self, chapter):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return None
        progress = AdventureProgress.objects.filter(user=request.user, chapter=chapter).first()
        return AdventureProgressSerializer(progress).data if progress else None


# ─── Character ────────────────────────────────────────────────────────────────

class AdventureCharacterSerializer(serializers.ModelSerializer):
    is_met = serializers.SerializerMethodField()

    class Meta:
        model  = AdventureCharacter
        fields = [
            "id", "slug", "name", "role", "emoji", "description", "quote",
            "character_type", "lang_bridge", "order", "is_met",
        ]

    def get_is_met(self, character):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return UserCharacterMet.objects.filter(user=request.user, character=character).exists()


# ─── Item / Inventory ─────────────────────────────────────────────────────────

class AdventureItemSerializer(serializers.ModelSerializer):
    source_phase_number    = serializers.IntegerField(source="source_phase.number",    read_only=True, default=None)
    source_character_name  = serializers.CharField(source="source_character.name",     read_only=True, default=None)

    class Meta:
        model  = AdventureItem
        fields = [
            "id", "slug", "emoji", "name", "lore", "rarity", "action", "order",
            "source_phase_number", "source_character_name",
        ]


class UserInventoryItemSerializer(serializers.ModelSerializer):
    item = AdventureItemSerializer(read_only=True)

    class Meta:
        model  = UserInventoryItem
        fields = ["id", "item", "earned_at", "is_used", "used_at"]


# ─── Phase sections ───────────────────────────────────────────────────────────

class PhaseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PhaseSection
        fields = ["section_number", "section_type", "content"]

    def to_representation(self, instance):
        rep = {"type": instance.section_type}
        rep.update(instance.content)
        return rep


# ─── Vocabulary (word mastery) ────────────────────────────────────────────────

class WordMasterySerializer(serializers.ModelSerializer):
    class Meta:
        model  = WordMastery
        fields = ["word_id", "target", "native", "tier"]


# ─── Section progress ─────────────────────────────────────────────────────────

class SectionProgressSerializer(serializers.ModelSerializer):
    phase_id = serializers.IntegerField(source="phase.id", read_only=True)

    class Meta:
        model  = AdventureSectionProgress
        fields = ["phase_id", "completed_sections", "updated_at"]


