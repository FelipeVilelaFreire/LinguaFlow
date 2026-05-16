from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.adventure.models import (
    AdventureChapter,
    AdventureCharacter,
    AdventureItem,
    AdventurePhase,
    AdventureSectionProgress,
    AdventureSkill,
    PhaseSection,
    UserChest,
    UserInventoryItem,
    UserSkillMastery,
)
from apps.goals.models import Goal
from apps.learning.models import Language, Lesson, Phrase, Scenario, StudyDay, StudyModule
from apps.progress.models import DailyStreak, Favorite, StudyDayCompletion, UserProgress, WordMastery


User = get_user_model()


class AdminDashboardViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=["get"])
    def summary(self, request):
        return Response(
            {
                "users": User.objects.count(),
                "staff_users": User.objects.filter(is_staff=True).count(),
                "active_goals": Goal.objects.filter(is_active=True).count(),
                "goals": Goal.objects.count(),
                "languages": Language.objects.count(),
                "scenarios": Scenario.objects.count(),
                "lessons": Lesson.objects.count(),
                "study_days": StudyDay.objects.count(),
                "phrases": Phrase.objects.count(),
                "completions": StudyDayCompletion.objects.count(),
                "favorites": Favorite.objects.count(),
                "progress_entries": UserProgress.objects.count(),
            }
        )

    @action(detail=False, methods=["get"])
    def users(self, request):
        users = User.objects.order_by("-date_joined")[:100]
        return Response(
            [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "is_staff": user.is_staff,
                    "is_superuser": user.is_superuser,
                    "is_active": user.is_active,
                    "date_joined": user.date_joined,
                    "goal_count": Goal.objects.filter(user=user).count(),
                    "completion_count": StudyDayCompletion.objects.filter(user=user).count(),
                }
                for user in users
            ]
        )

    @action(detail=False, methods=["get"])
    def goals(self, request):
        goals = Goal.objects.select_related("user", "source_language", "target_language").order_by("-is_active", "-id")[:150]
        return Response(
            [
                {
                    "id": goal.id,
                    "user": goal.user.username if goal.user else None,
                    "source_language": goal.source_language.code,
                    "target_language": goal.target_language.code,
                    "current_level": goal.current_level,
                    "target_level": goal.target_level,
                    "duration_days": goal.duration_days,
                    "session_minutes": goal.session_minutes,
                    "study_weekdays": goal.study_weekdays,
                    "is_active": goal.is_active,
                    "learned_phrases": goal.learned_phrases,
                    "total_phrases": goal.total_phrases,
                    "completed_lessons": goal.completed_lessons,
                    "streak_days": goal.streak_days,
                }
                for goal in goals
            ]
        )

    @action(detail=False, methods=["get"])
    def content(self, request):
        languages = Language.objects.order_by("code")
        scenarios = Scenario.objects.order_by("slug")
        phrase_counts = {
            f"{item['source_language__code']}->{item['target_language__code']} {item['difficulty']}": item["count"]
            for item in Phrase.objects.values("source_language__code", "target_language__code", "difficulty").annotate(count=Count("id"))
        }
        return Response(
            {
                "languages": [{"id": item.id, "code": item.code, "name": item.name} for item in languages],
                "scenarios": [
                    {
                        "id": item.id,
                        "slug": item.slug,
                        "title": item.title,
                        "phrase_count": Phrase.objects.filter(scenario=item).count(),
                        "lesson_count": Lesson.objects.filter(scenario=item).count(),
                    }
                    for item in scenarios
                ],
                "phrase_counts": phrase_counts,
                "lesson_count": Lesson.objects.count(),
                "study_day_count": StudyDay.objects.count(),
            }
        )

    @action(detail=False, methods=["get"], url_path="learning-detail")
    def learning_detail(self, request):
        modules = StudyModule.objects.order_by("lang_code", "order")
        lessons = Lesson.objects.select_related("scenario", "scenario__module").prefetch_related("phrases").order_by("day_number", "id")[:200]
        phrases = Phrase.objects.select_related("source_language", "target_language", "scenario").order_by("-id")[:250]
        study_days = StudyDay.objects.select_related("lesson", "lesson__scenario").order_by("day_number", "id")[:200]

        return Response(
            {
                "modules": [
                    {
                        "id": item.id,
                        "lang_code": item.lang_code,
                        "title": item.title,
                        "order": item.order,
                        "scenario_count": item.scenarios.count(),
                    }
                    for item in modules
                ],
                "lessons": [
                    {
                        "id": item.id,
                        "title": item.title,
                        "day_number": item.day_number,
                        "scenario": item.scenario.title,
                        "module": item.scenario.module.title if item.scenario.module else "",
                        "objective": item.objective,
                        "phrase_count": item.phrases.count(),
                        "has_video": bool(item.video_url),
                    }
                    for item in lessons
                ],
                "study_days": [
                    {
                        "id": item.id,
                        "day_number": item.day_number,
                        "lesson": item.lesson.title,
                        "scenario": item.lesson.scenario.title,
                        "is_active": item.is_active,
                    }
                    for item in study_days
                ],
                "phrases": [
                    {
                        "id": item.id,
                        "source_language": item.source_language.code,
                        "target_language": item.target_language.code,
                        "source_text": item.source_text,
                        "target_text": item.target_text,
                        "category": item.category,
                        "scenario": item.scenario.title if item.scenario else "",
                        "difficulty": item.difficulty,
                    }
                    for item in phrases
                ],
            }
        )

    @action(detail=False, methods=["get"])
    def adventure(self, request):
        chapters = AdventureChapter.objects.select_related("language").order_by("language__code", "order")
        phases = AdventurePhase.objects.select_related("chapter", "chapter__language").order_by("chapter__language__code", "chapter__order", "number")[:250]
        sections = PhaseSection.objects.select_related("phase", "phase__chapter").order_by("phase__chapter__order", "phase__number", "section_number")[:400]
        characters = AdventureCharacter.objects.select_related("chapter").order_by("chapter__order", "order")[:250]
        skills = AdventureSkill.objects.select_related("chapter").order_by("chapter__order", "order")[:250]
        items = AdventureItem.objects.select_related("chapter", "skill", "source_phase").order_by("chapter__order", "order")[:350]

        return Response(
            {
                "chapters": [
                    {
                        "id": item.id,
                        "language": item.language.code,
                        "level": item.level,
                        "order": item.order,
                        "title": item.title,
                        "boss_name": item.boss_name,
                        "phase_count": item.phases.count(),
                        "character_count": item.characters.count(),
                        "item_count": item.items.count(),
                    }
                    for item in chapters
                ],
                "phases": [
                    {
                        "id": item.id,
                        "chapter": item.chapter.title,
                        "language": item.chapter.language.code,
                        "number": item.number,
                        "title": item.title,
                        "scenario_slug": item.scenario_slug,
                        "phrase_count": item.phrase_count,
                        "phase_type": item.phase_type,
                        "has_chest": item.has_chest,
                        "chest_tier": item.chest_tier,
                        "section_count": item.sections.count(),
                    }
                    for item in phases
                ],
                "sections": [
                    {
                        "id": item.id,
                        "phase": item.phase.number,
                        "chapter": item.phase.chapter.title,
                        "section_number": item.section_number,
                        "section_type": item.section_type,
                        "step_count": len(item.content.get("steps", [])) if isinstance(item.content, dict) else 0,
                    }
                    for item in sections
                ],
                "characters": [
                    {
                        "id": item.id,
                        "chapter": item.chapter.title,
                        "name": item.name,
                        "role": item.role,
                        "emoji": item.emoji,
                        "character_type": item.character_type,
                        "lang_bridge": item.lang_bridge,
                        "first_phase": item.first_phase.number if item.first_phase else None,
                    }
                    for item in characters
                ],
                "skills": [
                    {
                        "id": item.id,
                        "chapter": item.chapter.title,
                        "name": item.name,
                        "category": item.category,
                        "emoji": item.emoji,
                        "base_power": item.base_power,
                        "item_count": item.items.count(),
                    }
                    for item in skills
                ],
                "items": [
                    {
                        "id": item.id,
                        "chapter": item.chapter.title,
                        "name": item.name,
                        "emoji": item.emoji,
                        "rarity": item.rarity,
                        "action": item.action,
                        "item_tag": item.item_tag,
                        "skill": item.skill.name if item.skill else "",
                        "source_phase": item.source_phase.number if item.source_phase else None,
                    }
                    for item in items
                ],
                "user_counts": {
                    "chests": UserChest.objects.count(),
                    "inventory_items": UserInventoryItem.objects.count(),
                    "skill_mastery": UserSkillMastery.objects.count(),
                    "section_progress": AdventureSectionProgress.objects.count(),
                },
            }
        )

    @action(detail=False, methods=["get"])
    def progress(self, request):
        completions = StudyDayCompletion.objects.select_related("user", "study_day", "study_day__lesson", "goal").order_by("-completed_at")[:200]
        progress_entries = UserProgress.objects.select_related("user", "phrase").order_by("-updated_at")[:250]
        favorites = Favorite.objects.select_related("user", "phrase").order_by("-created_at")[:200]
        word_mastery = WordMastery.objects.select_related("user").order_by("-last_seen_at")[:250]
        streaks = DailyStreak.objects.select_related("user").order_by("-longest_streak")[:100]

        return Response(
            {
                "completions": [
                    {
                        "id": item.id,
                        "user": item.user.username,
                        "study_day": item.study_day.day_number,
                        "lesson": item.study_day.lesson.title,
                        "goal": str(item.goal) if item.goal else "",
                        "completed_at": item.completed_at,
                    }
                    for item in completions
                ],
                "progress_entries": [
                    {
                        "id": item.id,
                        "user": item.user.username if item.user else "",
                        "phrase": item.phrase.target_text,
                        "status": item.status,
                        "correct_count": item.correct_count,
                        "incorrect_count": item.incorrect_count,
                        "review_due": item.review_due,
                        "updated_at": item.updated_at,
                    }
                    for item in progress_entries
                ],
                "favorites": [
                    {
                        "id": item.id,
                        "user": item.user.username if item.user else "",
                        "phrase": item.phrase.target_text,
                        "created_at": item.created_at,
                    }
                    for item in favorites
                ],
                "word_mastery": [
                    {
                        "id": item.id,
                        "user": item.user.username,
                        "word_id": item.word_id,
                        "target": item.target,
                        "native": item.native,
                        "lang_code": item.lang_code,
                        "tier": item.tier,
                        "streak": item.streak,
                        "error_count": item.error_count,
                        "last_seen_at": item.last_seen_at,
                    }
                    for item in word_mastery
                ],
                "streaks": [
                    {
                        "id": item.id,
                        "user": item.user.username,
                        "current_streak": item.current_streak,
                        "longest_streak": item.longest_streak,
                        "last_active_date": item.last_active_date,
                    }
                    for item in streaks
                ],
            }
        )
