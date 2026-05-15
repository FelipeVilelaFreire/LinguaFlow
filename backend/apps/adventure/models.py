from django.conf import settings
from django.db import models
from django.utils import timezone

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


class PhaseSection(models.Model):
    TYPE_NARRATIVA          = "narrativa"
    TYPE_REVISAO_SRS        = "revisao_srs"
    TYPE_PRATICA_APLICADA   = "pratica_aplicada"
    TYPE_GRAMATICA_NARRATIVA = "gramatica_narrativa"
    TYPE_REFORCO            = "reforco"
    TYPE_OBSTACULO          = "obstaculo"
    TYPE_CHOICES = [
        (TYPE_NARRATIVA,           "Narrativa"),
        (TYPE_REVISAO_SRS,         "Revisão SRS"),
        (TYPE_PRATICA_APLICADA,    "Prática Aplicada"),
        (TYPE_GRAMATICA_NARRATIVA, "Gramática Narrativa"),
        (TYPE_REFORCO,             "Reforço"),
        (TYPE_OBSTACULO,           "Obstáculo"),
    ]

    phase          = models.ForeignKey("AdventurePhase", related_name="sections", on_delete=models.CASCADE)
    section_number = models.PositiveSmallIntegerField()
    section_type   = models.CharField(max_length=25, choices=TYPE_CHOICES)
    content        = models.JSONField()

    class Meta:
        ordering = ["section_number"]
        unique_together = ("phase", "section_number")

    def __str__(self):
        return f"{self.phase} — Seção {self.section_number} ({self.section_type})"


class AdventurePhase(models.Model):
    PHASE_TYPE_STORY  = "story"
    PHASE_TYPE_REVIEW = "review"
    PHASE_TYPE_BOSS   = "boss"
    PHASE_TYPE_CHOICES = [
        (PHASE_TYPE_STORY,  "Story"),
        (PHASE_TYPE_REVIEW, "Review"),
        (PHASE_TYPE_BOSS,   "Boss"),
    ]

    CHEST_TIER_COMUM    = "comum"
    CHEST_TIER_RARO     = "raro"
    CHEST_TIER_EPICO    = "epico"
    CHEST_TIER_LENDARIO = "lendario"
    CHEST_TIER_MITICO   = "mitico"
    CHEST_TIER_CHOICES = [
        (CHEST_TIER_COMUM,    "Comum"),
        (CHEST_TIER_RARO,     "Raro"),
        (CHEST_TIER_EPICO,    "Épico"),
        (CHEST_TIER_LENDARIO, "Lendário"),
        (CHEST_TIER_MITICO,   "Mítico"),
    ]

    chapter = models.ForeignKey(AdventureChapter, related_name="phases", on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=140)
    narrative_intro = models.TextField()
    narrative_outro = models.TextField()
    key_words = models.JSONField(default=list)
    scenario_slug = models.CharField(max_length=60)
    phrase_count = models.PositiveIntegerField(default=6)
    phase_type = models.CharField(max_length=10, choices=PHASE_TYPE_CHOICES, default=PHASE_TYPE_STORY)
    is_boss = models.BooleanField(default=False)
    has_chest = models.BooleanField(default=False)
    chest_tier = models.CharField(max_length=10, choices=CHEST_TIER_CHOICES, blank=True, default="")

    class Meta:
        ordering = ["number"]
        unique_together = ("chapter", "number")

    def __str__(self):
        label = "BOSS" if self.is_boss else f"Fase {self.number}"
        return f"{self.chapter} — {label}: {self.title}"

    def save(self, *args, **kwargs):
        self.is_boss = self.phase_type == self.PHASE_TYPE_BOSS
        super().save(*args, **kwargs)

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


# ─── Characters ───────────────────────────────────────────────────────────────

class AdventureCharacter(models.Model):
    """
    Any person the player encounters in the adventure.
    character_type defines their role — never use separate classes per type.
    """
    TYPE_MAIN    = "main"     # protagonistas da história principal
    TYPE_ALLY    = "ally"     # aliados/guias (podem falar a língua do player)
    TYPE_BOSS    = "boss"     # antagonista final de cada temporada
    TYPE_NPC     = "npc"      # personagens de suporte (lojista, guarda, etc.)
    TYPE_CHOICES = [
        (TYPE_MAIN, "Main"),
        (TYPE_ALLY, "Ally"),
        (TYPE_BOSS, "Boss"),
        (TYPE_NPC,  "NPC"),
    ]

    chapter        = models.ForeignKey(AdventureChapter, related_name="characters", on_delete=models.CASCADE)
    slug           = models.SlugField(max_length=80)
    name           = models.CharField(max_length=120)
    role           = models.CharField(max_length=120)   # occupation/title in target language, e.g. "Campesino"
    emoji          = models.CharField(max_length=10)
    character_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=TYPE_NPC)
    description    = models.TextField(blank=True, default="")
    quote          = models.TextField()                 # memorable quote
    lang_bridge    = models.BooleanField(default=False) # speaks the player's native language
    first_phase    = models.ForeignKey(
        AdventurePhase, related_name="introduced_characters",
        on_delete=models.SET_NULL, null=True, blank=True,
    )
    order          = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        unique_together = ("chapter", "slug")

    def __str__(self):
        return f"{self.chapter} — {self.name} ({self.get_character_type_display()})"


class UserCharacterMet(models.Model):
    user      = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="characters_met", on_delete=models.CASCADE)
    character = models.ForeignKey(AdventureCharacter, related_name="met_by", on_delete=models.CASCADE)
    met_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "character")
        ordering = ["met_at"]

    def __str__(self):
        return f"{self.user} met {self.character.name}"


# ─── Items / Inventory ────────────────────────────────────────────────────────

class AdventureSkill(models.Model):
    CATEGORY_COMBATE       = "combate"
    CATEGORY_SOBREVIVENCIA = "sobrevivencia"
    CATEGORY_SOCIAL        = "social"
    CATEGORY_INVESTIGACAO  = "investigacao"
    CATEGORY_SUPORTE       = "suporte"
    CATEGORY_CHOICES = [
        (CATEGORY_COMBATE,       "Combate"),
        (CATEGORY_SOBREVIVENCIA, "Sobrevivencia"),
        (CATEGORY_SOCIAL,        "Social"),
        (CATEGORY_INVESTIGACAO,  "Investigacao"),
        (CATEGORY_SUPORTE,       "Suporte"),
    ]

    chapter     = models.ForeignKey(AdventureChapter, related_name="skills", on_delete=models.CASCADE)
    slug        = models.SlugField(max_length=80)
    name        = models.CharField(max_length=120)
    description = models.TextField(blank=True, default="")
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CATEGORY_SUPORTE)
    emoji       = models.CharField(max_length=10, blank=True, default="")
    base_power  = models.PositiveSmallIntegerField(default=10)
    order       = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        unique_together = ("chapter", "slug")

    def __str__(self):
        return f"{self.chapter} - {self.name}"


class AdventureItem(models.Model):
    RARITY_COMUM    = "comum"
    RARITY_RARO     = "raro"
    RARITY_EPICO    = "epico"
    RARITY_LENDARIO = "lendario"
    RARITY_CHOICES  = [
        (RARITY_COMUM,    "Comum"),
        (RARITY_RARO,     "Raro"),
        (RARITY_EPICO,    "Épico"),
        (RARITY_LENDARIO, "Lendário"),
    ]

    ACTION_EXAMINAR = "examinar"
    ACTION_ENTREGAR = "entregar"
    ACTION_USAR     = "usar"
    ACTION_EQUIPAR  = "equipar"
    ACTION_CHOICES  = [
        (ACTION_EXAMINAR, "Examinar"),
        (ACTION_ENTREGAR, "Entregar"),
        (ACTION_USAR,     "Usar"),
        (ACTION_EQUIPAR,  "Equipar"),
    ]

    # Tags para item_moment — qualquer item com a tag matching pode ser usado
    TAG_COMIDA    = "comida"
    TAG_BEBIDA    = "bebida"
    TAG_ARMA      = "arma"
    TAG_DOCUMENTO = "documento"
    TAG_MONEDA    = "moneda"
    TAG_REMEDIO   = "remedio"
    TAG_COMUM     = "comum"

    chapter      = models.ForeignKey(AdventureChapter, related_name="items", on_delete=models.CASCADE)
    slug         = models.SlugField(max_length=80)
    emoji        = models.CharField(max_length=10)
    name         = models.CharField(max_length=120)
    lore         = models.TextField()
    rarity       = models.CharField(max_length=10, choices=RARITY_CHOICES, default=RARITY_COMUM)
    action       = models.CharField(max_length=10, choices=ACTION_CHOICES, default=ACTION_EXAMINAR)
    word_id      = models.CharField(max_length=60, blank=True, default="")
    item_tag     = models.CharField(max_length=20, blank=True, default="")
    skill        = models.ForeignKey(AdventureSkill, related_name="items", on_delete=models.SET_NULL, null=True, blank=True)
    is_degraded  = models.BooleanField(default=False)
    degrades_to  = models.ForeignKey(
        "self", related_name="degraded_versions",
        on_delete=models.SET_NULL, null=True, blank=True,
    )
    source_phase = models.ForeignKey(
        AdventurePhase, related_name="reward_items",
        on_delete=models.SET_NULL, null=True, blank=True,
    )
    source_character = models.ForeignKey(
        AdventureCharacter, related_name="given_items",
        on_delete=models.SET_NULL, null=True, blank=True,
    )
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        unique_together = ("chapter", "slug")

    def __str__(self):
        return f"{self.chapter} — {self.name} ({self.rarity})"


class UserInventoryItem(models.Model):
    user      = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="inventory", on_delete=models.CASCADE)
    item      = models.ForeignKey(AdventureItem, related_name="owned_by", on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    is_used   = models.BooleanField(default=False)
    used_at   = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "item")
        ordering = ["earned_at"]

    def __str__(self):
        return f"{self.user} — {self.item.name}"


# ─── Section-level progress ───────────────────────────────────────────────────

class UserSkillMastery(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="skill_mastery", on_delete=models.CASCADE)
    skill        = models.ForeignKey(AdventureSkill, related_name="mastery_entries", on_delete=models.CASCADE)
    xp           = models.PositiveIntegerField(default=0)
    level        = models.PositiveSmallIntegerField(default=1)
    uses_count   = models.PositiveIntegerField(default=0)
    last_used_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "skill")
        ordering = ["skill__order"]

    def __str__(self):
        return f"{self.user} - {self.skill.slug} lv {self.level}"

    @staticmethod
    def level_for_xp(xp: int) -> int:
        if xp >= 1000:
            return 5
        if xp >= 500:
            return 4
        if xp >= 220:
            return 3
        if xp >= 80:
            return 2
        return 1

    def add_xp(self, amount: int, used: bool = False):
        self.xp += max(0, amount)
        self.level = self.level_for_xp(self.xp)
        if used:
            self.uses_count += 1
            self.last_used_at = timezone.now()
        self.save(update_fields=["xp", "level", "uses_count", "last_used_at"])


class UserChest(models.Model):
    STATUS_STORED    = "stored"
    STATUS_OPENING   = "opening"
    STATUS_READY     = "ready"
    STATUS_CLAIMED   = "claimed"
    STATUS_DISCARDED = "discarded"
    STATUS_CHOICES = [
        (STATUS_STORED,    "Stored"),
        (STATUS_OPENING,   "Opening"),
        (STATUS_READY,     "Ready"),
        (STATUS_CLAIMED,   "Claimed"),
        (STATUS_DISCARDED, "Discarded"),
    ]

    user          = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="adventure_chests", on_delete=models.CASCADE)
    phase         = models.ForeignKey(AdventurePhase, related_name="user_chests", on_delete=models.CASCADE)
    chapter       = models.ForeignKey(AdventureChapter, related_name="user_chests", on_delete=models.CASCADE)
    chest_tier    = models.CharField(max_length=10, choices=AdventurePhase.CHEST_TIER_CHOICES)
    phase_score   = models.PositiveIntegerField(default=0)
    status        = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_STORED)
    rolled_rarity = models.CharField(max_length=10, choices=AdventureItem.RARITY_CHOICES, blank=True, default="")
    earned_item   = models.ForeignKey(AdventureItem, related_name="chest_drops", on_delete=models.SET_NULL, null=True, blank=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    started_at    = models.DateTimeField(null=True, blank=True)
    unlock_at     = models.DateTimeField(null=True, blank=True)
    claimed_at    = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "phase")
        ordering = ["status", "unlock_at", "created_at"]

    @property
    def is_ready(self):
        return self.status == self.STATUS_READY or (
            self.status == self.STATUS_OPENING and self.unlock_at is not None and self.unlock_at <= timezone.now()
        )


class AdventureSectionProgress(models.Model):
    user               = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="section_progress", on_delete=models.CASCADE)
    phase              = models.ForeignKey(AdventurePhase, related_name="section_progress", on_delete=models.CASCADE)
    completed_sections = models.PositiveSmallIntegerField(default=0)  # 0–6
    updated_at         = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "phase")

    def __str__(self):
        return f"{self.user} — phase {self.phase_id}: {self.completed_sections}/6"


# ─── User progress (existing) ─────────────────────────────────────────────────

class AdventureProgress(models.Model):
    user           = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="adventure_progress", on_delete=models.CASCADE)
    chapter        = models.ForeignKey(AdventureChapter, related_name="progress_entries", on_delete=models.CASCADE)
    current_phase  = models.PositiveIntegerField(default=1)
    reward_unlocked = models.BooleanField(default=False)
    started_at     = models.DateTimeField(auto_now_add=True)
    completed_at   = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "chapter")

    def __str__(self):
        return f"{self.user} — {self.chapter} (fase {self.current_phase})"


class AdventurePhaseCompletion(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="phase_completions", on_delete=models.CASCADE)
    phase        = models.ForeignKey(AdventurePhase, related_name="completions", on_delete=models.CASCADE)
    score        = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "phase")
        ordering = ["-completed_at"]

    def __str__(self):
        return f"{self.user} — {self.phase} ({self.score}%)"


# ─── Item Queue (shuffle por usuário) ─────────────────────────────────────────

class UserItemQueue(models.Model):
    """
    Cada usuário tem uma fila embaralhada por tier de baú em cada capítulo.
    No início da temporada, embaralha pool de items[tier] e guarda a ordem.
    A cada baú aberto, entrega item[next_index] e incrementa.
    No fim da temporada, todo jogador tem a coleção completa — mas viveu
    em ordem diferente.
    """
    TIER_CHOICES = AdventurePhase.CHEST_TIER_CHOICES

    user             = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="item_queues", on_delete=models.CASCADE)
    chapter          = models.ForeignKey(AdventureChapter, related_name="user_queues", on_delete=models.CASCADE)
    tier             = models.CharField(max_length=10, choices=TIER_CHOICES)
    ordered_item_ids = models.JSONField(default=list)
    next_index       = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("user", "chapter", "tier")

    def __str__(self):
        return f"{self.user} — {self.chapter.slug} — {self.tier} ({self.next_index}/{len(self.ordered_item_ids)})"

    def pop_next(self):
        """Returns the next item_id to deliver, or None if queue exhausted."""
        if self.next_index >= len(self.ordered_item_ids):
            return None
        item_id = self.ordered_item_ids[self.next_index]
        self.next_index += 1
        self.save(update_fields=["next_index"])
        return item_id
