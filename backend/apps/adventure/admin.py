from django.contrib import admin

from .models import AdventureChapter, AdventurePhase, AdventurePhaseCompletion, AdventureProgress


class AdventurePhaseInline(admin.TabularInline):
    model = AdventurePhase
    extra = 0
    fields = ["number", "title", "scenario_slug", "phrase_count", "is_boss"]


@admin.register(AdventureChapter)
class AdventureChapterAdmin(admin.ModelAdmin):
    list_display = ["slug", "language", "level", "title", "order"]
    list_filter = ["language", "level"]
    inlines = [AdventurePhaseInline]


@admin.register(AdventurePhase)
class AdventurePhaseAdmin(admin.ModelAdmin):
    list_display = ["chapter", "number", "title", "scenario_slug", "is_boss"]
    list_filter = ["chapter", "is_boss"]


@admin.register(AdventureProgress)
class AdventureProgressAdmin(admin.ModelAdmin):
    list_display = ["user", "chapter", "current_phase", "reward_unlocked", "completed_at"]
    list_filter = ["chapter", "reward_unlocked"]


@admin.register(AdventurePhaseCompletion)
class AdventurePhaseCompletionAdmin(admin.ModelAdmin):
    list_display = ["user", "phase", "score", "completed_at"]
