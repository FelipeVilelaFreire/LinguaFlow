import random
from datetime import timedelta

from django.db.models import Q
from django.utils import timezone
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.goals.models import Goal
from apps.progress.models import DailyStreak, UserAdventureFlag, WordMastery
from apps.learning.serializers import PhraseSerializer

from .models import (
    AdventureCharacter,
    AdventureChapter,
    AdventureItem,
    AdventurePhase,
    AdventurePhaseCompletion,
    AdventureProgress,
    AdventureSectionProgress,
    PhaseSection,
    UserCharacterMet,
    UserInventoryItem,
)
from .serializers import (
    AdventureCharacterSerializer,
    AdventureChapterListSerializer,
    AdventureChapterSerializer,
    AdventureItemSerializer,
    PhaseSectionSerializer,
    SectionProgressSerializer,
    UserInventoryItemSerializer,
    WordMasterySerializer,
)


# ─── SRS study session ────────────────────────────────────────────────────────

_TIER_INTERVALS = {
    WordMastery.TIER_BRONZE:    timedelta(days=1),
    WordMastery.TIER_PRATA:     timedelta(days=3),
    WordMastery.TIER_OURO:      timedelta(days=7),
    WordMastery.TIER_DIAMANTE:  timedelta(days=14),
    WordMastery.TIER_ESMERALDA: timedelta(days=30),
}

_WRITE_TIERS = {WordMastery.TIER_DIAMANTE, WordMastery.TIER_ESMERALDA}


def _build_srs_exercise(word: WordMastery, pool: list) -> dict:
    if word.tier in _WRITE_TIERS:
        t    = word.target or ""
        hint = (t[0] + "·" * (len(t) - 1)) if len(t) > 1 else t
        return {
            "kind":    "write_word",
            "word_id": word.word_id,
            "tier":    word.tier,
            "target":  word.target,
            "native":  word.native,
            "prompt":  f"Como se diz '{word.native}'?",
            "answer":  word.target,
            "hint":    hint,
        }

    # Ouro → target→native recognition; Bronze/Prata → native→target production
    if word.tier == WordMastery.TIER_OURO:
        question     = f"O que significa '{word.target}'?"
        correct_text = word.native
        texts        = [d.native for d in pool if d.native and d.native != word.native]
    else:
        question     = f"Como se diz '{word.native}'?"
        correct_text = word.target
        texts        = [d.target for d in pool if d.target and d.target != word.target]

    random.shuffle(texts)
    distractors = (texts[:3] + ["—", "—", "—"])[:3]

    correct_pos = random.randint(0, 3)
    ids = ["a", "b", "c", "d"]
    options, di = [], 0
    for i, oid in enumerate(ids):
        if i == correct_pos:
            options.append({"id": oid, "text": correct_text})
        else:
            options.append({"id": oid, "text": distractors[di]})
            di += 1

    return {
        "kind":     "multiple_choice",
        "word_id":  word.word_id,
        "tier":     word.tier,
        "target":   word.target,
        "native":   word.native,
        "question": question,
        "options":  options,
        "correct":  ids[correct_pos],
    }


# ─── Flag helpers ─────────────────────────────────────────────────────────────

def _set_flag(user, key: str, value: str = "") -> None:
    UserAdventureFlag.objects.get_or_create(user=user, flag_key=key, defaults={"value": value})


def _get_user_flags(user) -> set[str]:
    """All flag keys for a user — explicit + synthetic (met_/has_) from inventory + characters met."""
    explicit = set(UserAdventureFlag.objects.filter(user=user).values_list("flag_key", flat=True))
    met = {f"met_{slug}" for slug in UserCharacterMet.objects.filter(user=user).values_list("character__slug", flat=True)}
    has = {f"has_{slug}" for slug in UserInventoryItem.objects.filter(user=user).values_list("item__slug", flat=True)}
    return explicit | met | has


def _filter_steps_by_flags(steps: list, user_flags: set[str]) -> list:
    """Drop steps whose `if_flag` is missing or whose `if_not_flag` is present."""
    out = []
    for step in steps:
        required = step.get("if_flag")
        excluded = step.get("if_not_flag")
        if required and required not in user_flags:
            continue
        if excluded and excluded in user_flags:
            continue
        out.append(step)
    return out


# ─── Chapters ─────────────────────────────────────────────────────────────────

class AdventureChapterViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset     = AdventureChapter.objects.prefetch_related("phases").select_related("language")
    lookup_field = "slug"

    def get_serializer_class(self):
        return AdventureChapterSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        language = self.request.query_params.get("language")
        if language:
            qs = qs.filter(language__code=language.upper())
        elif self.request.user.is_authenticated:
            goal = Goal.objects.filter(user=self.request.user, is_active=True).select_related("target_language").first()
            if goal:
                qs = qs.filter(language=goal.target_language)
        return qs

    @action(detail=False, methods=["get"], url_path="languages")
    def available_languages(self, request):
        """Returns one entry per language that has at least one adventure chapter."""
        chapters = (
            AdventureChapter.objects
            .filter(language__is_ready=True)
            .select_related("language")
            .order_by("language__code", "order")
        )
        seen = set()
        result = []
        for ch in chapters:
            if ch.language.code not in seen:
                seen.add(ch.language.code)
                result.append({
                    "code":             ch.language.code,
                    "chapter_title":    ch.title,
                    "chapter_subtitle": ch.subtitle,
                })
        return Response(result)


# ─── Phases ───────────────────────────────────────────────────────────────────

class AdventurePhaseViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset           = AdventurePhase.objects.select_related("chapter__language")
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        from .serializers import AdventurePhaseSerializer
        return AdventurePhaseSerializer

    @action(detail=True, methods=["get"])
    def phrases(self, request, pk=None):
        phase = self.get_object()
        source_code = self._get_source_code(request)
        phrases = phase.get_phrases(source_code)
        if not phrases.exists():
            return Response(
                {"detail": "No phrases found for this phase. Run seed_es first."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(PhraseSerializer(phrases, many=True).data)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        phase = self.get_object()
        score = max(0, min(100, int(request.data.get("score", 0))))

        AdventurePhaseCompletion.objects.update_or_create(
            user=request.user, phase=phase,
            defaults={"score": score},
        )

        progress, _ = AdventureProgress.objects.get_or_create(
            user=request.user, chapter=phase.chapter,
        )

        next_phase = phase.chapter.phases.filter(number__gt=phase.number).order_by("number").first()
        if next_phase and progress.current_phase <= phase.number:
            progress.current_phase = next_phase.number
            progress.save(update_fields=["current_phase"])

        if phase.is_boss:
            progress.reward_unlocked = True
            progress.completed_at = timezone.now()
            progress.save(update_fields=["reward_unlocked", "completed_at"])

        # Award all items bound to this phase (cotidiano gifts + boss reward).
        # Idempotent via get_or_create — re-completing the phase doesn't duplicate.
        items = list(AdventureItem.objects.filter(source_phase=phase).order_by("order"))
        earned_items = []
        for item in items:
            UserInventoryItem.objects.get_or_create(user=request.user, item=item)
            earned_items.append({
                "slug":   item.slug,
                "emoji":  item.emoji,
                "name":   item.name,
                "lore":   item.lore,
                "rarity": item.rarity,
                "action": item.action,
            })
        # Backward compat: first item also surfaces as `earned_item` (singular)
        earned_item = earned_items[0] if earned_items else None

        # Personalization flags — fire automatic signals so future content can
        # react to what the player did. has_<slug> is synthetic (derived from
        # inventory), so it doesn't need an explicit row here.
        _set_flag(request.user, f"phase_{phase.id}_completed", value=str(score))
        if score >= 95:
            _set_flag(request.user, f"phase_{phase.id}_perfect")
        if score < 60:
            _set_flag(request.user, f"phase_{phase.id}_struggled")
        if phase.chapter.phases.filter(number=1).first() == phase:
            _set_flag(request.user, f"chapter_{phase.chapter.slug}_started")

        streak_obj, _ = DailyStreak.objects.get_or_create(user=request.user)
        streak_data   = streak_obj.record_activity()

        return Response({
            "score":             score,
            "phase_number":      phase.number,
            "is_boss":           phase.is_boss,
            "reward_unlocked":   progress.reward_unlocked,
            "current_phase":     progress.current_phase,
            "chapter_completed": progress.completed_at is not None,
            "earned_item":       earned_item,
            "earned_items":      earned_items,
            "key_words":         phase.key_words,
            "streak":            streak_data,
        })

    @action(detail=True, methods=["get"], url_path="sections")
    def sections(self, request, pk=None):
        phase = self.get_object()
        qs = PhaseSection.objects.filter(phase=phase)
        if not qs.exists():
            return Response(
                {"detail": "No sections found for this phase."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Filter steps/beats/exercises by user flags. Each step may carry
        # `if_flag` or `if_not_flag` conditionals — server drops what shouldn't
        # render so the renderer stays dumb.
        user_flags = _get_user_flags(request.user)
        result = []
        for sec in qs:
            content = dict(sec.content or {})
            for key in ("steps", "exercises", "beats"):
                if key in content and isinstance(content[key], list):
                    content[key] = _filter_steps_by_flags(content[key], user_flags)
            result.append({"type": sec.section_type, **content})

        return Response(result)

    @action(detail=True, methods=["get", "post"], url_path="section-progress")
    def section_progress(self, request, pk=None):
        phase = self.get_object()

        if request.method == "GET":
            sp = AdventureSectionProgress.objects.filter(user=request.user, phase=phase).first()
            return Response({
                "phase_id":           phase.id,
                "completed_sections": sp.completed_sections if sp else 0,
            })

        count = max(0, min(6, int(request.data.get("completed_sections", 0))))
        sp, _ = AdventureSectionProgress.objects.update_or_create(
            user=request.user, phase=phase,
            defaults={"completed_sections": count},
        )
        return Response(SectionProgressSerializer(sp).data)

    def _get_source_code(self, request):
        if request.user.is_authenticated:
            goal = Goal.objects.filter(user=request.user, is_active=True).select_related("source_language").first()
            if goal:
                return goal.source_language.code
        return request.query_params.get("source", "PT")


# ─── Characters ───────────────────────────────────────────────────────────────

class AdventureCharacterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset           = AdventureCharacter.objects.select_related("chapter", "first_phase")
    serializer_class   = AdventureCharacterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        chapter_slug = self.request.query_params.get("chapter")
        if chapter_slug:
            qs = qs.filter(chapter__slug=chapter_slug)
        return qs

    @action(detail=True, methods=["post"])
    def meet(self, request, pk=None):
        character = self.get_object()
        _, created = UserCharacterMet.objects.get_or_create(user=request.user, character=character)
        return Response({"character_id": character.id, "created": created})

    @action(detail=False, methods=["post"], url_path="meet-by-name")
    def meet_by_name(self, request):
        """
        Marks a character as met using their display name + the user's active
        target language. Used by the chat renderer which only knows the NPC's
        display name (e.g. "Don Miguel"), not the database id.
        """
        name = (request.data.get("name") or "").strip()
        if not name:
            return Response({"detail": "name is required."}, status=status.HTTP_400_BAD_REQUEST)

        goal = Goal.objects.filter(user=request.user, is_active=True).select_related("target_language").first()
        if not goal:
            return Response({"detail": "No active goal."}, status=status.HTTP_404_NOT_FOUND)

        character = (
            AdventureCharacter.objects
            .filter(chapter__language=goal.target_language, name__icontains=name)
            .order_by("order").first()
        )
        if not character:
            return Response({"detail": f"Character '{name}' not found for active language."},
                            status=status.HTTP_404_NOT_FOUND)

        _, created = UserCharacterMet.objects.get_or_create(user=request.user, character=character)
        return Response({
            "character_id": character.id,
            "slug":         character.slug,
            "name":         character.name,
            "created":      created,
        })


# ─── Vocabulary ───────────────────────────────────────────────────────────────

class VocabularyViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class   = WordMasterySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = WordMastery.objects.filter(user=self.request.user)
        lang = self.request.query_params.get("lang")
        if lang:
            qs = qs.filter(lang_code=lang.lower())
        return qs

    @action(detail=False, methods=["get"], url_path="study-session")
    def study_session(self, request):
        """SRS session: returns up to 20 words due for review, as exercises."""
        goal = Goal.objects.filter(
            user=request.user, is_active=True
        ).select_related("target_language").first()
        if not goal:
            return Response({"total": 0, "due_count": 0, "exercises": []})

        lang_code = goal.target_language.code.lower()
        now       = timezone.now()

        all_words = list(WordMastery.objects.filter(user=request.user, lang_code=lang_code))
        total     = len(all_words)

        due = [
            w for w in all_words
            if w.last_seen_at is None
            or (now - w.last_seen_at) >= _TIER_INTERVALS.get(w.tier, timedelta(days=1))
        ]
        due_count = len(due)

        if not due:
            return Response({"total": total, "due_count": 0, "exercises": []})

        session_words = due[:20]
        random.shuffle(session_words)

        session_ids  = {w.word_id for w in session_words}
        distractor_pool = [w for w in all_words if w.word_id not in session_ids]

        return Response({
            "total":     total,
            "due_count": due_count,
            "exercises": [_build_srs_exercise(w, distractor_pool) for w in session_words],
        })

    @action(detail=False, methods=["post"])
    def record(self, request):
        """
        Records a single answer for a word. Creates the WordMastery on first
        sight (using target/native/lang_code from payload), then updates streak
        and tier via WordMastery.record_answer().
        """
        word_id   = request.data.get("word_id")
        correct   = bool(request.data.get("correct", False))
        target    = request.data.get("target",    "")
        native    = request.data.get("native",    "")
        lang_code = request.data.get("lang_code", "").lower()

        if not word_id:
            return Response({"detail": "word_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        mastery, created = WordMastery.objects.get_or_create(
            user=request.user, word_id=word_id,
            defaults={"target": target, "native": native, "lang_code": lang_code},
        )

        # Backfill metadata if it was empty on previous records
        updated_fields = []
        if not mastery.target    and target:    mastery.target    = target;    updated_fields.append("target")
        if not mastery.native    and native:    mastery.native    = native;    updated_fields.append("native")
        if not mastery.lang_code and lang_code: mastery.lang_code = lang_code; updated_fields.append("lang_code")
        if updated_fields and not created:
            mastery.save(update_fields=updated_fields)

        promoted = mastery.record_answer(correct)

        return Response({
            "word_id":  mastery.word_id,
            "target":   mastery.target,
            "native":   mastery.native,
            "tier":     mastery.tier,
            "streak":   mastery.streak,
            "promoted": promoted,
            "created":  created,
        })


# ─── DEV tools ────────────────────────────────────────────────────────────────

class AdventureDevViewSet(viewsets.GenericViewSet):
    """Dev-only helpers. Not gated by env flag in MVP — guard in production."""
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"], url_path="jump-to-phase")
    def jump_to_phase(self, request):
        """
        Puts the user at "Phase X, Section Y" — meaning sections 1..Y-1 of
        phase X are completed (and so are all phases 1..X-1). Wipes the rest
        and pre-unlocks the corresponding characters, items, and word mastery
        (Bronze tier) for every word_id seen in those completed sections.
        """
        chapter_slug   = request.data.get("chapter_slug")
        phase_number   = int(request.data.get("phase_number",   1) or 1)
        section_number = int(request.data.get("section_number", 1) or 1)
        section_number = max(1, min(6, section_number))

        if not chapter_slug:
            return Response({"detail": "chapter_slug is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            chapter = AdventureChapter.objects.select_related("language").get(slug=chapter_slug)
        except AdventureChapter.DoesNotExist:
            return Response({"detail": "Chapter not found."}, status=status.HTTP_404_NOT_FOUND)

        user      = request.user
        lang_code = chapter.language.code.lower()

        # 1. Wipe progress in this chapter
        AdventurePhaseCompletion.objects.filter(user=user, phase__chapter=chapter).delete()
        AdventureSectionProgress.objects.filter(user=user, phase__chapter=chapter).delete()
        UserCharacterMet.objects.filter(user=user, character__chapter=chapter).delete()
        UserInventoryItem.objects.filter(user=user, item__chapter=chapter).delete()
        WordMastery.objects.filter(user=user, lang_code=lang_code).delete()

        # Clear flags scoped to this chapter (phase_*_X / chapter_<slug>_*)
        phase_ids = list(chapter.phases.values_list("id", flat=True))
        flag_filter = Q(flag_key__startswith=f"chapter_{chapter.slug}_")
        for pid in phase_ids:
            flag_filter |= Q(flag_key__startswith=f"phase_{pid}_")
        UserAdventureFlag.objects.filter(user=user).filter(flag_filter).delete()

        # 2. Mark phases 1..N-1 fully completed
        completed_phases = list(chapter.phases.filter(number__lt=phase_number))
        AdventurePhaseCompletion.objects.bulk_create([
            AdventurePhaseCompletion(user=user, phase=ph, score=100)
            for ph in completed_phases
        ])

        # 3. Set in-progress section count for phase N (Y-1 sections done)
        target_phase = chapter.phases.filter(number=phase_number).first()
        if target_phase and section_number > 1:
            AdventureSectionProgress.objects.create(
                user=user, phase=target_phase, completed_sections=section_number - 1,
            )

        # 4. AdventureProgress.current_phase = N
        progress, _ = AdventureProgress.objects.get_or_create(user=user, chapter=chapter)
        progress.current_phase   = phase_number
        progress.reward_unlocked = False
        progress.completed_at    = None
        progress.save(update_fields=["current_phase", "reward_unlocked", "completed_at"])

        # 5. Characters — introduced before phase N, plus those of phase N
        #    if the player has already started section 2+ of phase N.
        char_filter = {"chapter": chapter}
        if section_number > 1:
            char_filter["first_phase__number__lte"] = phase_number
        else:
            char_filter["first_phase__number__lt"]  = phase_number
        met_chars = list(AdventureCharacter.objects.filter(**char_filter))
        UserCharacterMet.objects.bulk_create([
            UserCharacterMet(user=user, character=ch) for ch in met_chars
        ])

        # 6. Items from boss phases already passed
        boss_items = list(AdventureItem.objects.filter(
            chapter=chapter,
            source_phase__number__lt=phase_number,
            source_phase__phase_type=AdventurePhase.PHASE_TYPE_BOSS,
        ))
        UserInventoryItem.objects.bulk_create([
            UserInventoryItem(user=user, item=it) for it in boss_items
        ])

        # 7. Word mastery — scan PhaseSection.content of completed sections:
        #    all sections of phases 1..N-1 + sections 1..Y-1 of phase N.
        completed_sections_q = Q(phase__chapter=chapter, phase__number__lt=phase_number)
        if section_number > 1:
            completed_sections_q |= Q(
                phase__chapter=chapter,
                phase__number=phase_number,
                section_number__lt=section_number,
            )
        sections = PhaseSection.objects.filter(completed_sections_q)

        seen: dict[str, dict] = {}
        for sec in sections:
            content = sec.content or {}
            all_steps = list(content.get("steps", [])) + list(content.get("exercises", []))
            for step in all_steps:
                wid = step.get("word_id")
                if wid and wid not in seen:
                    seen[wid] = {"target": step.get("target", ""), "native": step.get("native", "")}
                if step.get("kind") == "vocab_list":
                    for item in step.get("items", []):
                        target = (item.get("target") or "").strip()
                        if not target:
                            continue
                        derived_wid = f"{lang_code}_" + target.lower().replace(" ", "_").replace("?", "").replace("¿", "").replace("¡", "").replace("!", "")
                        if derived_wid not in seen:
                            seen[derived_wid] = {"target": target, "native": item.get("native", "")}

        WordMastery.objects.bulk_create([
            WordMastery(
                user=user, word_id=wid,
                target=meta["target"], native=meta["native"],
                lang_code=lang_code, tier=WordMastery.TIER_BRONZE,
            )
            for wid, meta in seen.items()
        ])

        return Response({
            "chapter":          chapter.slug,
            "current_phase":    phase_number,
            "current_section":  section_number,
            "completed_phases": len(completed_phases),
            "met_characters":   len(met_chars),
            "words_unlocked":   len(seen),
            "items_unlocked":   len(boss_items),
        })


# ─── Inventory ────────────────────────────────────────────────────────────────

class UserInventoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class   = UserInventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserInventoryItem.objects.filter(user=self.request.user).select_related("item")

    @action(detail=True, methods=["post"])
    def use(self, request, pk=None):
        inv = self.get_object()
        if inv.is_used:
            return Response({"detail": "Item already used."}, status=status.HTTP_400_BAD_REQUEST)
        inv.is_used = True
        inv.used_at = timezone.now()
        inv.save(update_fields=["is_used", "used_at"])
        return Response(UserInventoryItemSerializer(inv).data)
