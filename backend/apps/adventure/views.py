import random
from datetime import timedelta

from django.db.models import Avg, Q, Sum
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
    AdventureSkill,
    PhaseSection,
    UserCharacterMet,
    UserChest,
    UserInventoryItem,
    UserItemQueue,
    UserSkillMastery,
)
from .serializers import (
    AdventureCharacterSerializer,
    AdventureChapterListSerializer,
    AdventureChapterSerializer,
    AdventureItemSerializer,
    AdventureSkillSerializer,
    PhaseSectionSerializer,
    SectionProgressSerializer,
    UserChestSerializer,
    UserInventoryItemSerializer,
    UserSkillMasterySerializer,
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


_SKILL_XP_BY_WORD_TIER = {
    WordMastery.TIER_BRONZE:    5,
    WordMastery.TIER_PRATA:     10,
    WordMastery.TIER_OURO:      18,
    WordMastery.TIER_DIAMANTE:  28,
    WordMastery.TIER_ESMERALDA: 45,
}

_CHEST_UNLOCK_MINUTES = {
    "comum": 2,
    "raro": 10,
    "epico": 30,
    "lendario": 120,
    "mitico": 240,
}


def _award_skill_xp(user, item: AdventureItem, *, used: bool = False, bonus: int = 0):
    if not item.skill_id:
        return None
    mastery, _ = UserSkillMastery.objects.get_or_create(user=user, skill=item.skill)
    word_tier = None
    if item.word_id:
        word = WordMastery.objects.filter(user=user, word_id=item.word_id).first()
        word_tier = word.tier if word else None
    amount = item.skill.base_power + bonus + _SKILL_XP_BY_WORD_TIER.get(word_tier, 0)
    mastery.add_xp(amount, used=used)
    return mastery


def _score_to_chest_tier(score: int) -> str:
    if score >= 95:
        return "lendario"
    if score >= 85:
        return "epico"
    if score >= 70:
        return "raro"
    return "comum"


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

    @action(detail=False, methods=["get"], url_path="hero-stats", permission_classes=[IsAuthenticated])
    def hero_stats(self, request):
        phases_qs         = AdventurePhaseCompletion.objects.filter(user=request.user)
        phases_completed  = phases_qs.count()
        avg_score         = phases_qs.aggregate(avg=Avg("score"))["avg"] or 0

        section_total = (
            AdventureSectionProgress.objects
            .filter(user=request.user)
            .aggregate(total=Sum("completed_sections"))["total"] or 0
        )

        streak_obj     = DailyStreak.objects.filter(user=request.user).first()
        current_streak = streak_obj.current_streak if streak_obj else 0
        longest_streak = streak_obj.longest_streak if streak_obj else 0

        words_qs   = WordMastery.objects.filter(user=request.user)
        total_words = words_qs.count()
        words_by_tier = {
            "bronze":    words_qs.filter(tier=WordMastery.TIER_BRONZE).count(),
            "prata":     words_qs.filter(tier=WordMastery.TIER_PRATA).count(),
            "ouro":      words_qs.filter(tier=WordMastery.TIER_OURO).count(),
            "diamante":  words_qs.filter(tier=WordMastery.TIER_DIAMANTE).count(),
            "esmeralda": words_qs.filter(tier=WordMastery.TIER_ESMERALDA).count(),
        }

        xp = (
            phases_completed * 50
            + section_total  * 10
            + current_streak * 15
            + words_by_tier["bronze"]    * 5
            + words_by_tier["prata"]     * 15
            + words_by_tier["ouro"]      * 30
            + words_by_tier["diamante"]  * 50
            + words_by_tier["esmeralda"] * 100
        )

        LEVEL_THRESHOLDS = [0, 1000, 2500, 5000, 10000, 20000, 50000]
        level = 1
        for i, threshold in enumerate(LEVEL_THRESHOLDS):
            if xp >= threshold:
                level = i + 1
            else:
                break
        xp_current_level = LEVEL_THRESHOLDS[level - 1]
        xp_next_level    = LEVEL_THRESHOLDS[level] if level < len(LEVEL_THRESHOLDS) else None

        prata_plus = (
            words_by_tier["prata"] + words_by_tier["ouro"]
            + words_by_tier["diamante"] + words_by_tier["esmeralda"]
        )
        ouro_plus = (
            words_by_tier["ouro"] + words_by_tier["diamante"] + words_by_tier["esmeralda"]
        )
        attributes = {
            "vocabulario": int(prata_plus / total_words * 100) if total_words else 0,
            "gramatica":   int(min(avg_score, 100)),
            "fluencia":    int(ouro_plus  / total_words * 100) if total_words else 0,
        }

        achievements = []
        if phases_completed >= 1:
            achievements.append({"key": "first_step", "emoji": "⚔️", "label": "Primeiro Passo", "desc": "Completou a primeira fase"})
        if phases_completed >= 10:
            achievements.append({"key": "warrior", "emoji": "🗡️", "label": "Guerreiro", "desc": "Completou 10 fases"})
        if current_streak >= 7:
            achievements.append({"key": "on_fire", "emoji": "🔥", "label": "Em Chamas", "desc": "7 dias seguidos de estudo"})
        if total_words >= 100:
            achievements.append({"key": "wordsmith", "emoji": "📚", "label": "100 Palavras", "desc": "Aprendeu 100 palavras"})
        if phases_completed >= 25:
            achievements.append({"key": "t1_survivor", "emoji": "👑", "label": "Sobrevivente T1", "desc": "Concluiu a Temporada 1"})

        return Response({
            "phases_completed":  phases_completed,
            "xp":                xp,
            "level":             level,
            "xp_current_level":  xp_current_level,
            "xp_next_level":     xp_next_level,
            "current_streak":    current_streak,
            "longest_streak":    longest_streak,
            "total_words":       total_words,
            "words_by_tier":     words_by_tier,
            "attributes":        attributes,
            "skills":            UserSkillMasterySerializer(
                UserSkillMastery.objects.filter(user=request.user).select_related("skill", "skill__chapter"),
                many=True,
            ).data,
            "achievements":      achievements,
        })


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
            _award_skill_xp(request.user, item, bonus=10)
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

        earned_chest = None
        if phase.has_chest:
            earned_chest, _ = UserChest.objects.get_or_create(
                user=request.user,
                phase=phase,
                defaults={
                    "chapter": phase.chapter,
                    "chest_tier": _score_to_chest_tier(score),
                    "phase_score": score,
                },
            )

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
            "earned_chest":      UserChestSerializer(earned_chest).data if earned_chest else None,
            "key_words":         phase.key_words,
            "streak":            streak_data,
        })

    # ── Sistema de baú estilo Clash Royale ──────────────────────────────────
    # 1. Score da fase → TIER do baú (jogar bem = baú melhor)
    # 2. Tier do baú → DROP RATE: sorteia a raridade do item (nunca garantido)
    # 3. Raridade sorteada → item elegível: word-linked raros/épicos só caem
    #    pra quem dominou a palavra (WordMastery). Comuns caem pra todos.
    # 4. Sem repetição: se o user já tem todos daquela raridade, desce um nível.
    #    Pool grande >> nº de baús → cada usuário termina com mochila diferente.

    _SCORE_TO_CHEST_TIER = [
        (95, "lendario"),
        (85, "epico"),
        (70, "raro"),
        (0,  "comum"),
    ]

    _CHEST_DROP_RATES = {
        # tier do baú : { raridade do item : peso }
        "comum":    {"comum": 75, "raro": 22, "epico": 3,  "lendario": 0},
        "raro":     {"comum": 40, "raro": 42, "epico": 16, "lendario": 2},
        "epico":    {"comum": 15, "raro": 38, "epico": 35, "lendario": 12},
        "lendario": {"comum": 5,  "raro": 25, "epico": 40, "lendario": 30},
    }

    _RARITY_DESCENDING = ["lendario", "epico", "raro", "comum"]

    # Raridades cujos itens word-linked só caem se o user dominou a palavra.
    # Comuns nunca filtram (jogador iniciante não pode ficar com mochila vazia).
    _WORD_GATED_RARITIES = {"raro", "epico", "lendario"}

    @action(detail=True, methods=["post"], url_path="open-chest")
    def open_chest(self, request, pk=None):
        """
        Abre baú da fase (se has_chest=True). Estilo Clash Royale:
        score da fase decide o tier do baú · tier sorteia a raridade do
        item por drop rate · raridade entrega item elegível que o user
        ainda não tem. Dois usuários terminam com mochilas diferentes.
        """
        phase = self.get_object()
        if not phase.has_chest:
            return Response(
                {"detail": "Esta fase não tem baú."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        completion = AdventurePhaseCompletion.objects.filter(user=request.user, phase=phase).first()
        if not completion:
            return Response({"detail": "Conclua a fase antes de ganhar o bau."}, status=status.HTTP_400_BAD_REQUEST)
        chest, _ = UserChest.objects.get_or_create(
            user=request.user,
            phase=phase,
            defaults={
                "chapter": phase.chapter,
                "chest_tier": _score_to_chest_tier(completion.score),
                "phase_score": completion.score,
            },
        )
        return Response({
            "from_chest": True,
            "chest_tier": chest.chest_tier,
            "rolled_rarity": None,
            "phase_score": chest.phase_score,
            "earned_item": None,
            "stored_chest": UserChestSerializer(chest).data,
        })

        chapter = phase.chapter

        # ── 1. Score da fase → tier do baú ───────────────────────────────────
        completion = AdventurePhaseCompletion.objects.filter(
            user=request.user, phase=phase,
        ).first()
        score = completion.score if completion else 0
        chest_tier = next(t for floor, t in self._SCORE_TO_CHEST_TIER if score >= floor)

        # ── 2. Tier do baú → sorteia raridade do item por drop rate ──────────
        rates = self._CHEST_DROP_RATES[chest_tier]
        rarities = list(rates.keys())
        weights  = list(rates.values())
        rolled_rarity = random.choices(rarities, weights=weights, k=1)[0]

        # ── 3. Mastery do usuário — quais word_ids ele domina ────────────────
        mastered_word_ids = set(
            WordMastery.objects.filter(user=request.user)
            .values_list("word_id", flat=True)
        )

        # ── 4. Itens que o user já tem (não repetir) ─────────────────────────
        owned_item_ids = set(
            UserInventoryItem.objects.filter(user=request.user)
            .values_list("item_id", flat=True)
        )

        def eligible_items(rarity):
            qs = AdventureItem.objects.filter(
                chapter=chapter, rarity=rarity, is_degraded=False,
                source_phase__isnull=True,
            ).exclude(id__in=owned_item_ids)
            items = []
            for it in qs:
                # word-linked raros/épicos/lendários: só se dominou a palavra
                if (rarity in self._WORD_GATED_RARITIES
                        and it.word_id
                        and it.word_id not in mastered_word_ids):
                    continue
                items.append(it)
            return items

        # ── 5. Desce de raridade se a sorteada estiver esgotada ──────────────
        item = None
        start_idx = self._RARITY_DESCENDING.index(rolled_rarity)
        for rarity in self._RARITY_DESCENDING[start_idx:]:
            candidates = eligible_items(rarity)
            if candidates:
                item = random.choice(candidates)
                rolled_rarity = rarity
                break

        if item is None:
            # User já tem tudo elegível — sem item, mas não é erro de fluxo
            return Response({
                "from_chest":  True,
                "chest_tier":  chest_tier,
                "rolled_rarity": None,
                "earned_item": None,
                "detail": "Coleção desta raridade completa.",
            })

        UserInventoryItem.objects.get_or_create(user=request.user, item=item)

        return Response({
            "from_chest":    True,
            "chest_tier":    chest_tier,    # tier do baú (do score)
            "rolled_rarity": rolled_rarity, # raridade que saiu no sorteio
            "phase_score":   score,
            "earned_item":   AdventureItemSerializer(item).data,
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

        characters = AdventureCharacter.objects.filter(chapter__language=goal.target_language)
        character = (
            characters.filter(name__iexact=name).order_by("order").first()
            or characters.filter(name__istartswith=f"{name} ").order_by("order").first()
            or characters.filter(name__icontains=name).order_by("order").first()
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

        # Award item tied to this word_id on first correct answer
        earned_item_data = None
        degraded_item_data = None
        if correct:
            # Acerto: entrega o item pleno (não-degradado) ligado à palavra.
            item = AdventureItem.objects.filter(word_id=word_id, is_degraded=False).first()
            if item:
                inv, item_created = UserInventoryItem.objects.get_or_create(
                    user=request.user, item=item
                )
                _award_skill_xp(request.user, item, bonus=5)
                if item_created:
                    earned_item_data = {
                        "slug":   item.slug,
                        "emoji":  item.emoji,
                        "name":   item.name,
                        "lore":   item.lore,
                        "rarity": item.rarity,
                        "action": item.action,
                    }
            # Palavra finalmente dominada → remove a versão degradada da mochila.
            degraded = AdventureItem.objects.filter(word_id=word_id, is_degraded=True).first()
            if degraded:
                UserInventoryItem.objects.filter(
                    user=request.user, item=degraded
                ).delete()
        else:
            # Erro: se passou do limite e nunca acertou, libera versão degradada.
            if mastery.should_degrade:
                degraded = AdventureItem.objects.filter(word_id=word_id, is_degraded=True).first()
                if degraded:
                    _, deg_created = UserInventoryItem.objects.get_or_create(
                        user=request.user, item=degraded
                    )
                    if deg_created:
                        degraded_item_data = {
                            "slug":   degraded.slug,
                            "emoji":  degraded.emoji,
                            "name":   degraded.name,
                            "lore":   degraded.lore,
                            "rarity": degraded.rarity,
                            "action": degraded.action,
                            "is_degraded": True,
                        }

        return Response({
            "word_id":      mastery.word_id,
            "target":       mastery.target,
            "native":       mastery.native,
            "tier":         mastery.tier,
            "streak":       mastery.streak,
            "error_count":  mastery.error_count,
            "promoted":     promoted,
            "created":      created,
            "earned_item":  earned_item_data,
            "degraded_item": degraded_item_data,
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


# ─── Item catalog ─────────────────────────────────────────────────────────────

class AdventureItemViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Public catalog of all items for a chapter (?chapter=slug). No auth required for listing."""
    serializer_class   = AdventureItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = AdventureItem.objects.select_related("chapter", "skill")
        chapter_slug = self.request.query_params.get("chapter")
        if chapter_slug:
            qs = qs.filter(chapter__slug=chapter_slug)
        return qs.order_by("order")


# ─── Inventory ────────────────────────────────────────────────────────────────

class AdventureSkillViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = AdventureSkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = AdventureSkill.objects.select_related("chapter")
        chapter_slug = self.request.query_params.get("chapter")
        if chapter_slug:
            qs = qs.filter(chapter__slug=chapter_slug)
        return qs.order_by("chapter__order", "order")

    @action(detail=False, methods=["get"], url_path="mastery")
    def mastery(self, request):
        qs = UserSkillMastery.objects.filter(user=request.user).select_related("skill", "skill__chapter")
        return Response(UserSkillMasterySerializer(qs, many=True).data)


class UserChestViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserChestSerializer
    permission_classes = [IsAuthenticated]

    _CHEST_DROP_RATES = AdventurePhaseViewSet._CHEST_DROP_RATES
    _RARITY_DESCENDING = AdventurePhaseViewSet._RARITY_DESCENDING
    _WORD_GATED_RARITIES = AdventurePhaseViewSet._WORD_GATED_RARITIES

    def get_queryset(self):
        return (
            UserChest.objects
            .filter(user=self.request.user)
            .select_related("phase", "chapter", "earned_item", "earned_item__skill")
        )

    @action(detail=True, methods=["post"], url_path="start")
    def start(self, request, pk=None):
        chest = self.get_object()
        if chest.status != UserChest.STATUS_STORED:
            return Response({"detail": "Este bau nao esta armazenado."}, status=status.HTTP_400_BAD_REQUEST)
        if UserChest.objects.filter(user=request.user, status=UserChest.STATUS_OPENING).exclude(pk=chest.pk).exists():
            return Response({"detail": "Ja existe um bau abrindo."}, status=status.HTTP_400_BAD_REQUEST)
        minutes = _CHEST_UNLOCK_MINUTES.get(chest.chest_tier, 2)
        chest.status = UserChest.STATUS_OPENING
        chest.started_at = timezone.now()
        chest.unlock_at = chest.started_at + timedelta(minutes=minutes)
        chest.save(update_fields=["status", "started_at", "unlock_at"])
        return Response(UserChestSerializer(chest).data)

    @action(detail=True, methods=["post"], url_path="claim")
    def claim(self, request, pk=None):
        chest = self.get_object()
        if not chest.is_ready:
            return Response({"detail": "Este bau ainda nao esta pronto."}, status=status.HTTP_400_BAD_REQUEST)
        if not chest.earned_item_id:
            item, rolled_rarity = self._roll_item(request.user, chest)
            if item:
                UserInventoryItem.objects.get_or_create(user=request.user, item=item)
                _award_skill_xp(request.user, item, bonus=20)
                chest.earned_item = item
                chest.rolled_rarity = rolled_rarity
        chest.status = UserChest.STATUS_CLAIMED
        chest.claimed_at = timezone.now()
        chest.save(update_fields=["earned_item", "rolled_rarity", "status", "claimed_at"])
        return Response(UserChestSerializer(chest).data)

    def _roll_item(self, user, chest):
        rates = self._CHEST_DROP_RATES.get(chest.chest_tier, self._CHEST_DROP_RATES["comum"])
        rolled_rarity = random.choices(list(rates.keys()), weights=list(rates.values()), k=1)[0]
        mastered_word_ids = set(WordMastery.objects.filter(user=user).values_list("word_id", flat=True))
        owned_item_ids = set(UserInventoryItem.objects.filter(user=user).values_list("item_id", flat=True))

        def eligible_items(rarity):
            qs = AdventureItem.objects.filter(
                chapter=chest.chapter,
                rarity=rarity,
                is_degraded=False,
                source_phase__isnull=True,
            ).exclude(id__in=owned_item_ids).select_related("skill")
            items = []
            for item in qs:
                if rarity in self._WORD_GATED_RARITIES and item.word_id and item.word_id not in mastered_word_ids:
                    continue
                items.append(item)
            return items

        start_idx = self._RARITY_DESCENDING.index(rolled_rarity)
        for rarity in self._RARITY_DESCENDING[start_idx:]:
            candidates = eligible_items(rarity)
            if candidates:
                return random.choice(candidates), rarity
        return None, ""


class UserInventoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class   = UserInventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserInventoryItem.objects.filter(user=self.request.user).select_related("item", "item__skill")

    @action(detail=True, methods=["post"])
    def use(self, request, pk=None):
        inv = self.get_object()
        if inv.is_used:
            return Response({"detail": "Item already used."}, status=status.HTTP_400_BAD_REQUEST)
        inv.is_used = True
        inv.used_at = timezone.now()
        inv.save(update_fields=["is_used", "used_at"])
        _award_skill_xp(request.user, inv.item, used=True, bonus=12)
        return Response(UserInventoryItemSerializer(inv).data)

    @action(detail=False, methods=["get"], url_path="locked")
    def locked(self, request):
        """
        Itens "vistos mas ainda não conquistados" — a palavra ligada ao item
        já apareceu pro usuário (existe WordMastery) mas ele não tem o item.
        A Mochila mostra estes em cinza com cadeado: 'acerte X para desbloquear'.

        Query opcional: ?chapter=es-a1-t1
        """
        chapter_slug = request.query_params.get("chapter")

        seen_word_ids = set(
            WordMastery.objects.filter(user=request.user)
            .values_list("word_id", flat=True)
        )
        owned_item_ids = set(
            UserInventoryItem.objects.filter(user=request.user)
            .values_list("item_id", flat=True)
        )

        qs = AdventureItem.objects.filter(word_id__in=seen_word_ids, is_degraded=False)
        if chapter_slug:
            qs = qs.filter(chapter__slug=chapter_slug)
        qs = qs.exclude(id__in=owned_item_ids).order_by("rarity", "order")

        return Response({
            "locked": [
                {
                    **AdventureItemSerializer(it).data,
                    "unlock_hint_word_id": it.word_id,
                }
                for it in qs
            ],
        })

    @action(detail=False, methods=["get"], url_path="by-tag")
    def by_tag(self, request):
        """
        Lista itens da mochila do usuário com uma tag específica.
        Usado pelo frontend ANTES de renderizar item_moment, pra saber se
        o player tem algo daquela categoria. Prioridade: item pleno > degradado.

        Query: ?tag=comida
        """
        tag = request.query_params.get("tag", "").strip()
        if not tag:
            return Response({"items": []})

        qs = UserInventoryItem.objects.filter(
            user=request.user, is_used=False, item__item_tag=tag,
        ).select_related("item").order_by("item__is_degraded", "item__order")

        return Response({
            "tag":   tag,
            "items": UserInventoryItemSerializer(qs, many=True).data,
        })

    @action(detail=False, methods=["post"], url_path="use-by-tag")
    def use_by_tag(self, request):
        """
        Resolve um item_moment consumindo o primeiro item da mochila com
        a tag pedida. Prioriza item pleno sobre degradado. Marca como usado.

        Body: {"tag": "comida"}
        """
        tag = request.data.get("tag", "").strip()
        if not tag:
            return Response({"detail": "tag required"}, status=status.HTTP_400_BAD_REQUEST)

        inv = (
            UserInventoryItem.objects
            .filter(user=request.user, is_used=False, item__item_tag=tag)
            .select_related("item")
            .order_by("item__is_degraded", "item__order")
            .first()
        )
        if not inv:
            return Response(
                {"detail": f"Nenhum item com tag '{tag}' na mochila."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Apenas items consumíveis somem da mochila ao usar.
        is_consumable = inv.item.action in (AdventureItem.ACTION_USAR, AdventureItem.ACTION_ENTREGAR)
        if is_consumable:
            inv.is_used = True
            inv.used_at = timezone.now()
            inv.save(update_fields=["is_used", "used_at"])
            _award_skill_xp(request.user, inv.item, used=True, bonus=12)

        return Response({
            "used_item":    AdventureItemSerializer(inv.item).data,
            "is_degraded":  inv.item.is_degraded,
            "consumed":     is_consumable,
        })
