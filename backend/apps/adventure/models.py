from django.conf import settings
from django.db import models

from apps.learning.models import Language, Phrase


class AdventureChapter(models.Model):
    slug = models.SlugField(unique=True)
    language = models.ForeignKey(Language, related_name="adventure_chapters", on_delete=models.PROTECT)
    level = models.CharField(max_length=8)
    order = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=140)
    subtitle = models.CharField(max_length=200, blank=True)
    background = models.CharField(max_length=60, default="default")
    boss_name = models.CharField(max_length=120)
    boss_intro = models.TextField(blank=True)
    reward_name = models.CharField(max_length=120)
    reward_description = models.TextField(blank=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.language.code} {self.level} — {self.title}"


class AdventurePhase(models.Model):
    chapter = models.ForeignKey(AdventureChapter, related_name="phases", on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=140)
    narrative_intro = models.TextField()
    narrative_outro = models.TextField()
    key_words = models.JSONField(default=list)
    scenario_slug = models.CharField(max_length=60)
    phrase_count = models.PositiveIntegerField(default=6)
    is_boss = models.BooleanField(default=False)

    class Meta:
        ordering = ["number"]
        unique_together = ("chapter", "number")

    def __str__(self):
        label = "BOSS" if self.is_boss else f"Fase {self.number}"
        return f"{self.chapter} — {label}: {self.title}"

    def get_phrases(self, source_language_code: str):
        return (
            Phrase.objects.filter(
                target_language=self.chapter.language,
                source_language__code=source_language_code.upper(),
                scenario__slug=self.scenario_slug,
                difficulty=self.chapter.level,
            )
            .select_related("scenario", "source_language", "target_language")
            .order_by("id")[: self.phrase_count]
        )


class AdventureProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="adventure_progress", on_delete=models.CASCADE)
    chapter = models.ForeignKey(AdventureChapter, related_name="progress_entries", on_delete=models.CASCADE)
    current_phase = models.PositiveIntegerField(default=1)
    reward_unlocked = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "chapter")

    def __str__(self):
        return f"{self.user} — {self.chapter} (fase {self.current_phase})"


class AdventurePhaseCompletion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="phase_completions", on_delete=models.CASCADE)
    phase = models.ForeignKey(AdventurePhase, related_name="completions", on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "phase")
        ordering = ["-completed_at"]

    def __str__(self):
        return f"{self.user} — {self.phase} ({self.score}%)"
