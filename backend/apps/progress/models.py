from django.conf import settings
from django.db import models

from apps.goals.models import Goal
from apps.learning.models import Phrase, StudyDay


class StudyDayCompletion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    study_day = models.ForeignKey(StudyDay, related_name="completions", on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, related_name="completions", null=True, blank=True, on_delete=models.SET_NULL)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content_studydaycompletion"
        unique_together = ("user", "study_day", "goal")
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
    correct_count = models.PositiveIntegerField(default=0)
    incorrect_count = models.PositiveIntegerField(default=0)
    interval_days = models.PositiveIntegerField(default=1)
    review_due = models.DateField(null=True, blank=True)
    last_answer = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content_userprogress"
        unique_together = ("user", "phrase")


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    phrase = models.ForeignKey(Phrase, related_name="favorite_entries", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content_favorite"
        unique_together = ("user", "phrase")
