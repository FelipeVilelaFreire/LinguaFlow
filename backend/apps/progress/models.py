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


# ─── Word mastery tiers ───────────────────────────────────────────────────────
# Cross-mode: tier de uma palavra é o mesmo no Modo Aventura e no Modo Estudo.
# word_id format: {lang_code}_{word_base}  e.g. "it_ciao", "es_hola"

class WordMastery(models.Model):
    TIER_BRONZE    = "bronze"
    TIER_PRATA     = "prata"
    TIER_OURO      = "ouro"
    TIER_DIAMANTE  = "diamante"
    TIER_ESMERALDA = "esmeralda"
    TIER_CHOICES   = [
        (TIER_BRONZE,    "Bronze"),
        (TIER_PRATA,     "Prata"),
        (TIER_OURO,      "Ouro"),
        (TIER_DIAMANTE,  "Diamante"),
        (TIER_ESMERALDA, "Esmeralda"),
    ]
    TIER_ORDER = [TIER_BRONZE, TIER_PRATA, TIER_OURO, TIER_DIAMANTE, TIER_ESMERALDA]

    # Acertos consecutivos necessários para subir de tier
    STREAK_TO_ADVANCE = {
        TIER_BRONZE:    3,
        TIER_PRATA:     5,
        TIER_OURO:      5,
        TIER_DIAMANTE:  5,
        TIER_ESMERALDA: None,  # maestria confirmada
    }

    user         = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="word_mastery", on_delete=models.CASCADE)
    word_id      = models.CharField(max_length=80)
    target       = models.CharField(max_length=120, blank=True)
    native       = models.CharField(max_length=120, blank=True)
    lang_code    = models.CharField(max_length=5, blank=True)
    tier         = models.CharField(max_length=12, choices=TIER_CHOICES, default=TIER_BRONZE)
    streak       = models.PositiveSmallIntegerField(default=0)
    last_seen_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "word_id")
        ordering = ["-last_seen_at"]

    def __str__(self):
        return f"{self.user} — {self.word_id} ({self.tier}, streak={self.streak})"

    def record_answer(self, correct: bool) -> bool:
        """Update streak/tier. Returns True if tier was promoted."""
        from django.utils import timezone

        self.last_seen_at = timezone.now()

        if not correct:
            self.streak = 0
            self.save(update_fields=["streak", "last_seen_at"])
            return False

        self.streak += 1
        threshold = self.STREAK_TO_ADVANCE.get(self.tier)
        promoted = False

        if threshold and self.streak >= threshold:
            idx = self.TIER_ORDER.index(self.tier)
            if idx < len(self.TIER_ORDER) - 1:
                self.tier = self.TIER_ORDER[idx + 1]
                self.streak = 0
                promoted = True

        self.save(update_fields=["tier", "streak", "last_seen_at"])
        return promoted


# ─── Adventure flags — personalization signals ────────────────────────────────
# Each flag is a small fact about what the player did. Used to vary NPC dialogue
# and content step visibility in later phases. Examples:
#   phase_3_perfect             → score >= 95 on phase 3 of any chapter
#   phase_5_completed           → just completion (any score)
#   met_don_miguel              → first time NPC was talked to
#   has_sombrero_viejo          → item earned/owned
#
# Read by the sections endpoint to filter steps tagged with `if_flag` /
# `if_not_flag`. Written automatically by phase completion, character meet,
# and item earn endpoints.

class UserAdventureFlag(models.Model):
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="adventure_flags", on_delete=models.CASCADE)
    flag_key = models.CharField(max_length=80)
    value    = models.CharField(max_length=120, blank=True)
    set_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "flag_key")
        ordering = ["-set_at"]

    def __str__(self):
        return f"{self.user} — {self.flag_key}"


class DailyStreak(models.Model):
    user             = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="daily_streak")
    current_streak   = models.PositiveIntegerField(default=0)
    longest_streak   = models.PositiveIntegerField(default=0)
    last_active_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "progress_dailystreak"

    def record_activity(self) -> dict:
        from django.utils import timezone
        today   = timezone.localdate()
        updated = False

        if self.last_active_date is None:
            self.current_streak = 1
            updated = True
        elif self.last_active_date == today:
            pass  # already counted today
        elif (today - self.last_active_date).days == 1:
            self.current_streak += 1
            updated = True
        else:
            self.current_streak = 1  # streak broken
            updated = True

        if updated:
            self.last_active_date = today
            if self.current_streak > self.longest_streak:
                self.longest_streak = self.current_streak
            self.save()

        return {
            "current":       self.current_streak,
            "longest":       self.longest_streak,
            "updated_today": updated,
        }
