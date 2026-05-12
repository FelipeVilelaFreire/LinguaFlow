from django.utils import timezone
from rest_framework import serializers

from apps.progress.models import UserProgress

from .models import Language, Lesson, Phrase, Scenario, StudyDay, StudyModule


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ["id", "code", "name"]


class ScenarioSerializer(serializers.ModelSerializer):
    phrase_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Scenario
        fields = ["id", "slug", "title", "description", "phrase_count"]


class StudyLessonSerializer(serializers.ModelSerializer):
    phrase_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Scenario
        fields = ["id", "slug", "title", "description", "adventure_phase", "order", "phrase_count"]


class StudyModuleSerializer(serializers.ModelSerializer):
    lessons = StudyLessonSerializer(many=True, read_only=True, source="scenarios")

    class Meta:
        model = StudyModule
        fields = ["id", "title", "lang_code", "order", "lessons"]


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
    practice_items = serializers.SerializerMethodField()

    class Meta:
        model = StudyDay
        fields = ["id", "day_number", "lesson", "is_active", "completed", "practice_items"]

    def get_completed(self, obj: StudyDay) -> bool:
        request = self.context.get("request")
        if not request or not request.user.is_authenticated:
            return False
        return obj.completions.filter(user=request.user).exists()

    def get_practice_items(self, obj: StudyDay) -> list[dict]:
        current_phrases = list(obj.lesson.phrases.all()[:12])
        items = [self._intro_item(obj, current_phrases)]
        for index, phrase in enumerate(current_phrases):
            items.append(self._practice_item("new", phrase, index, "Understand the target phrase."))
            if index < 6:
                items.append(self._practice_item("multiple_choice", phrase, index, "Choose the correct translation."))
            if index < 8:
                items.append(self._practice_item("fill_blank", phrase, index, "Complete the missing word."))
            items.append(self._practice_item("reverse", phrase, index, "Translate from your base language."))
            if index < 6:
                items.append(self._practice_item("word_order", phrase, index, "Put the words in the right order."))
                items.append(self._practice_item("dictation", phrase, index, "Type the target sentence from memory."))

        review_phrases = self._review_phrases(obj)
        for index, phrase in enumerate(review_phrases):
            items.append(self._practice_item("review", phrase, index, "Spaced review from an earlier lesson."))
        return items

    def _intro_item(self, obj: StudyDay, phrases: list[Phrase]) -> dict:
        preview = phrases[:5]
        return {
            "id": f"intro-{obj.id}",
            "type": "intro",
            "prompt": obj.lesson.title,
            "answer": "",
            "helper": f"Preview the {obj.lesson.scenario.title} lesson before practicing.",
            "options": [],
            "word_bank": [],
            "preview_phrases": [
                {
                    "source_text": phrase.source_text,
                    "target_text": phrase.target_text,
                    "source_code": phrase.source_language.code,
                    "target_code": phrase.target_language.code,
                }
                for phrase in preview
            ],
            "phrase": PhraseSerializer(preview[0]).data if preview else None,
        }

    def _review_phrases(self, obj: StudyDay):
        request = self.context.get("request")
        if not request or not request.user.is_authenticated or obj.day_number <= 1:
            return []
        due_phrase_ids = list(
            UserProgress.objects.filter(user=request.user, review_due__lte=timezone.localdate())
            .exclude(status=UserProgress.STATUS_MASTERED)
            .values_list("phrase_id", flat=True)[:12]
        )
        due_queryset = Phrase.objects.filter(id__in=due_phrase_ids)
        current_phrase = obj.lesson.phrases.first()
        if current_phrase:
            due_queryset = due_queryset.filter(
                source_language=current_phrase.source_language,
                target_language=current_phrase.target_language,
                difficulty=current_phrase.difficulty,
            )
        due_phrases = list(due_queryset.select_related("source_language", "target_language", "scenario"))
        if len(due_phrases) >= 12:
            return due_phrases[:12]

        review_day_numbers = [obj.day_number - offset for offset in (1, 3, 7, 14) if obj.day_number - offset > 0]
        if not review_day_numbers:
            return due_phrases
        queryset = Phrase.objects.filter(lessons__study_days__day_number__in=review_day_numbers)
        if current_phrase:
            queryset = queryset.filter(
                source_language=current_phrase.source_language,
                target_language=current_phrase.target_language,
                difficulty=current_phrase.difficulty,
            )
        scheduled_phrases = list(queryset.exclude(id__in=[phrase.id for phrase in due_phrases]).select_related("source_language", "target_language", "scenario").distinct().order_by("id")[: 12 - len(due_phrases)])
        return due_phrases + scheduled_phrases

    def _practice_item(self, item_type: str, phrase: Phrase, index: int, helper: str) -> dict:
        prompts = {
            "new": phrase.target_text,
            "multiple_choice": phrase.target_text,
            "fill_blank": self._blank_prompt(phrase.target_text),
            "reverse": phrase.source_text,
            "dictation": phrase.source_text,
            "word_order": phrase.source_text,
            "review": phrase.target_text,
        }
        answers = {
            "new": phrase.source_text,
            "multiple_choice": phrase.source_text,
            "fill_blank": self._blank_answer(phrase.target_text),
            "reverse": phrase.target_text,
            "dictation": phrase.target_text,
            "word_order": phrase.target_text,
            "review": phrase.source_text,
        }
        return {
            "id": f"{item_type}-{phrase.id}-{index}",
            "type": item_type,
            "prompt": prompts[item_type],
            "answer": answers[item_type],
            "helper": helper,
            "options": self._options(item_type, phrase),
            "word_bank": self._word_bank(item_type, phrase),
            "phrase": PhraseSerializer(phrase).data,
        }

    def _options(self, item_type: str, phrase: Phrase) -> list[str]:
        if item_type != "multiple_choice":
            return []
        distractors = list(
            Phrase.objects.filter(
                source_language=phrase.source_language,
                target_language=phrase.target_language,
                difficulty=phrase.difficulty,
            )
            .exclude(id=phrase.id)
            .order_by("id")
            .values_list("source_text", flat=True)[:3]
        )
        return sorted([phrase.source_text, *distractors])

    def _word_bank(self, item_type: str, phrase: Phrase) -> list[str]:
        if item_type != "word_order":
            return []
        return sorted([word.strip(".,!?") for word in phrase.target_text.split() if word.strip(".,!?")], key=str.lower)

    def _blank_prompt(self, text: str) -> str:
        words = text.split()
        if len(words) < 2:
            return text
        index = min(len(words) - 1, max(1, len(words) // 2))
        words[index] = "____"
        return " ".join(words)

    def _blank_answer(self, text: str) -> str:
        words = text.split()
        if len(words) < 2:
            return text
        index = min(len(words) - 1, max(1, len(words) // 2))
        return words[index].strip(".,!?")
