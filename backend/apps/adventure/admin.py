from django.contrib import admin

from .models import (
    AdventureCharacter,
    AdventureChapter,
    AdventureItem,
    AdventurePhase,
    AdventurePhaseCompletion,
    AdventureProgress,
    AdventureSectionProgress,
    AdventureSkill,
    PhaseSection,
    UserCharacterMet,
    UserChest,
    UserInventoryItem,
    UserSkillMastery,
)


class PhaseSectionInline(admin.TabularInline):
    model  = PhaseSection
    extra  = 0
    fields = ["section_number", "section_type", "content"]


class AdventurePhaseInline(admin.TabularInline):
    model  = AdventurePhase
    extra  = 0
    fields = ["number", "title", "phase_type", "scenario_slug", "phrase_count", "is_boss"]


class AdventureCharacterInline(admin.TabularInline):
    model  = AdventureCharacter
    extra  = 0
    fields = ["slug", "name", "role", "emoji", "character_type", "description", "lang_bridge", "first_phase", "order"]


class AdventureItemInline(admin.TabularInline):
    model  = AdventureItem
    extra  = 0
    fields = ["slug", "name", "emoji", "rarity", "action", "item_tag", "skill", "source_phase", "source_character", "order"]


@admin.register(AdventureChapter)
class AdventureChapterAdmin(admin.ModelAdmin):
    list_display = ["slug", "language", "level", "title", "order"]
    list_filter  = ["language", "level"]
    inlines      = [AdventurePhaseInline, AdventureCharacterInline, AdventureItemInline]


@admin.register(AdventurePhase)
class AdventurePhaseAdmin(admin.ModelAdmin):
    list_display = ["chapter", "number", "title", "phase_type", "scenario_slug"]
    list_filter  = ["chapter", "phase_type"]
    inlines      = [PhaseSectionInline]


@admin.register(PhaseSection)
class PhaseSectionAdmin(admin.ModelAdmin):
    list_display = ["phase", "section_number", "section_type"]
    list_filter  = ["section_type", "phase__chapter"]


@admin.register(AdventureCharacter)
class AdventureCharacterAdmin(admin.ModelAdmin):
    list_display  = ["name", "role", "character_type", "chapter", "lang_bridge", "order"]
    list_filter   = ["chapter", "character_type", "lang_bridge"]
    fields = ["chapter", "slug", "name", "role", "emoji", "character_type", "description", "quote", "lang_bridge", "first_phase", "order"]


@admin.register(AdventureItem)
class AdventureItemAdmin(admin.ModelAdmin):
    list_display = ["name", "chapter", "rarity", "action", "item_tag", "skill", "source_phase", "source_character", "order"]
    list_filter  = ["chapter", "rarity", "item_tag", "skill"]


@admin.register(AdventureSkill)
class AdventureSkillAdmin(admin.ModelAdmin):
    list_display = ["name", "chapter", "slug", "category", "base_power", "order"]
    list_filter = ["chapter", "category"]


@admin.register(UserSkillMastery)
class UserSkillMasteryAdmin(admin.ModelAdmin):
    list_display = ["user", "skill", "level", "xp", "uses_count", "last_used_at"]
    list_filter = ["skill__chapter", "skill"]


@admin.register(UserChest)
class UserChestAdmin(admin.ModelAdmin):
    list_display = ["user", "chapter", "phase", "chest_tier", "status", "unlock_at", "earned_item"]
    list_filter = ["chapter", "chest_tier", "status"]


@admin.register(AdventureProgress)
class AdventureProgressAdmin(admin.ModelAdmin):
    list_display = ["user", "chapter", "current_phase", "reward_unlocked", "completed_at"]
    list_filter  = ["chapter", "reward_unlocked"]


@admin.register(AdventurePhaseCompletion)
class AdventurePhaseCompletionAdmin(admin.ModelAdmin):
    list_display = ["user", "phase", "score", "completed_at"]


@admin.register(AdventureSectionProgress)
class AdventureSectionProgressAdmin(admin.ModelAdmin):
    list_display = ["user", "phase", "completed_sections", "updated_at"]


@admin.register(UserCharacterMet)
class UserCharacterMetAdmin(admin.ModelAdmin):
    list_display = ["user", "character", "met_at"]
    list_filter  = ["character__chapter"]


@admin.register(UserInventoryItem)
class UserInventoryItemAdmin(admin.ModelAdmin):
    list_display = ["user", "item", "earned_at", "is_used"]
    list_filter  = ["item__chapter", "is_used"]
