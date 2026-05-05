from django.contrib import admin

from .models import Favorite, StudyDayCompletion, UserProgress


@admin.register(StudyDayCompletion)
class StudyDayCompletionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "goal", "study_day", "completed_at")
    list_filter = ("completed_at", "goal")
    search_fields = ("user__username", "user__email", "study_day__lesson__title")
    autocomplete_fields = ("user", "goal", "study_day")
    ordering = ("-completed_at",)


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "phrase", "status", "updated_at")
    list_filter = ("status", "updated_at")
    search_fields = ("user__username", "user__email", "phrase__source_text", "phrase__target_text")
    autocomplete_fields = ("user", "phrase")
    ordering = ("-updated_at",)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "phrase", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "user__email", "phrase__source_text", "phrase__target_text")
    autocomplete_fields = ("user", "phrase")
    ordering = ("-created_at",)
