from django.db import models


class StudyModule(models.Model):
    lang_code = models.CharField(max_length=2)
    title     = models.CharField(max_length=120)
    order     = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "content_study_module"
        ordering = ["order"]

    def __str__(self) -> str:
        return f"{self.lang_code} · {self.title}"


class Language(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=80)
    is_ready = models.BooleanField(default=False)

    class Meta:
        db_table = "content_language"

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"


class Scenario(models.Model):
    slug            = models.SlugField(unique=True)
    title           = models.CharField(max_length=120)
    description     = models.TextField(blank=True)
    module          = models.ForeignKey(StudyModule, related_name="scenarios", null=True, blank=True, on_delete=models.SET_NULL)
    adventure_phase = models.PositiveIntegerField(null=True, blank=True)
    order           = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "content_scenario"
        ordering = ["order", "id"]

    def __str__(self) -> str:
        return self.title


class Phrase(models.Model):
    source_language = models.ForeignKey(Language, related_name="source_phrases", on_delete=models.PROTECT)
    target_language = models.ForeignKey(Language, related_name="target_phrases", on_delete=models.PROTECT)
    source_text = models.CharField(max_length=255)
    target_text = models.CharField(max_length=255)
    category = models.CharField(max_length=80, blank=True)
    scenario = models.ForeignKey(Scenario, related_name="phrases", null=True, blank=True, on_delete=models.SET_NULL)
    difficulty = models.CharField(max_length=8, default="A1")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content_phrase"
        unique_together = ("source_language", "target_language", "source_text", "target_text")

    def __str__(self) -> str:
        return self.target_text


class Lesson(models.Model):
    title = models.CharField(max_length=140)
    day_number = models.PositiveIntegerField(default=1)
    scenario = models.ForeignKey(Scenario, related_name="lessons", on_delete=models.PROTECT)
    phrases = models.ManyToManyField(Phrase, related_name="lessons", db_table="content_lesson_phrases")
    video_title = models.CharField(max_length=140, blank=True)
    video_url = models.URLField(blank=True)
    video_duration = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = "content_lesson"
        ordering = ["day_number", "id"]

    def __str__(self) -> str:
        return self.title


class StudyDay(models.Model):
    day_number = models.PositiveIntegerField()
    lesson = models.ForeignKey(Lesson, related_name="study_days", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "content_studyday"
        ordering = ["day_number"]

    def __str__(self) -> str:
        return f"Day {self.day_number}: {self.lesson.title}"
