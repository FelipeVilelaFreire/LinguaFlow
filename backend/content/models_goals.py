from django.conf import settings
from django.db import models

from .models_learning import Language


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
    study_weekdays = models.JSONField(default=list)
    session_minutes = models.PositiveIntegerField(default=30)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.target_language.code} {self.target_level}"
