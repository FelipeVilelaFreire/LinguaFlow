from django.contrib import admin

from .models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "source_language",
        "target_language",
        "current_level",
        "target_level",
        "duration_days",
        "session_minutes",
        "is_active",
        "progress_percent",
    )
    list_filter = ("is_active", "source_language", "target_language", "current_level", "target_level")
    search_fields = ("user__username", "user__email", "source_language__code", "target_language__code")
    autocomplete_fields = ("user", "source_language", "target_language")
    ordering = ("-is_active", "-id")

    @admin.display(description="Progress")
    def progress_percent(self, obj: Goal) -> str:
        if not obj.total_phrases:
            return "0%"
        return f"{min(100, round((obj.learned_phrases / obj.total_phrases) * 100))}%"
