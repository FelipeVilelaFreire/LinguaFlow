from django.contrib import admin

from .models import Language, Lesson, Phrase, Scenario, StudyDay


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name")
    search_fields = ("code", "name")
    ordering = ("code",)


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ("id", "slug", "title")
    search_fields = ("slug", "title", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("slug",)


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ("id", "source_language", "target_language", "difficulty", "category", "target_text")
    list_filter = ("source_language", "target_language", "difficulty", "scenario")
    search_fields = ("source_text", "target_text", "category")
    autocomplete_fields = ("source_language", "target_language", "scenario")
    ordering = ("source_language", "target_language", "difficulty", "id")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "day_number", "scenario", "title", "video_duration")
    list_filter = ("scenario",)
    search_fields = ("title", "video_title", "video_url")
    autocomplete_fields = ("scenario", "phrases")
    ordering = ("day_number", "id")


@admin.register(StudyDay)
class StudyDayAdmin(admin.ModelAdmin):
    list_display = ("id", "day_number", "lesson", "is_active")
    list_filter = ("is_active",)
    search_fields = ("lesson__title",)
    autocomplete_fields = ("lesson",)
    ordering = ("day_number", "id")
