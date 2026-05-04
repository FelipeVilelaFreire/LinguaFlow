from django.conf import settings
from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"


class Scenario(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

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
        unique_together = ("source_language", "target_language", "source_text", "target_text")

    def __str__(self) -> str:
        return self.target_text


class Lesson(models.Model):
    title = models.CharField(max_length=140)
    day_number = models.PositiveIntegerField(default=1)
    scenario = models.ForeignKey(Scenario, related_name="lessons", on_delete=models.PROTECT)
    phrases = models.ManyToManyField(Phrase, related_name="lessons")
    video_title = models.CharField(max_length=140, blank=True)
    video_url = models.URLField(blank=True)
    video_duration = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ["day_number", "id"]

    def __str__(self) -> str:
        return self.title


class StudyDay(models.Model):
    day_number = models.PositiveIntegerField()
    lesson = models.ForeignKey(Lesson, related_name="study_days", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["day_number"]

    def __str__(self) -> str:
        return f"Day {self.day_number}: {self.lesson.title}"


class StudyDayCompletion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    study_day = models.ForeignKey(StudyDay, related_name="completions", on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "study_day")
        ordering = ["-completed_at"]


class UserProgress(models.Model):
    STATUS_NEW = "new"
    STATUS_LEARNING = "learning"
    STATUS_MASTERED = "mastered"
    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_LEARNING, "Learning"),
        (STATUS_MASTERED, "Mastered"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    phrase = models.ForeignKey(Phrase, related_name="progress_entries", on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_NEW)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "phrase")


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    phrase = models.ForeignKey(Phrase, related_name="favorite_entries", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "phrase")


class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    source_language = models.ForeignKey(Language, related_name="source_goals", on_delete=models.PROTECT)
    target_language = models.ForeignKey(Language, related_name="target_goals", on_delete=models.PROTECT)
    target_level = models.CharField(max_length=8, default="A1")
    duration_days = models.PositiveIntegerField(default=90)
    start_date = models.DateField(auto_now_add=True)
    total_phrases = models.PositiveIntegerField(default=300)
    learned_phrases = models.PositiveIntegerField(default=0)
    completed_lessons = models.PositiveIntegerField(default=0)
    streak_days = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.target_language.code} {self.target_level}"
