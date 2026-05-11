from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("adventure", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # ── 1. phase_type on AdventurePhase ──────────────────────────────────
        migrations.AddField(
            model_name="adventurephase",
            name="phase_type",
            field=models.CharField(
                choices=[("story", "Story"), ("review", "Review"), ("boss", "Boss")],
                default="story",
                max_length=10,
            ),
        ),

        # ── 2. AdventureCharacter ─────────────────────────────────────────────
        migrations.CreateModel(
            name="AdventureCharacter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(max_length=80)),
                ("name", models.CharField(max_length=120)),
                ("role", models.CharField(max_length=120)),
                ("emoji", models.CharField(max_length=10)),
                ("character_type", models.CharField(
                    choices=[("main", "Main"), ("ally", "Ally"), ("boss", "Boss"), ("npc", "NPC")],
                    default="npc", max_length=10,
                )),
                ("quote", models.TextField()),
                ("lang_bridge", models.BooleanField(default=False)),
                ("order", models.PositiveIntegerField(default=1)),
                ("chapter", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="characters", to="adventure.adventurechapter")),
                ("first_phase", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="introduced_characters", to="adventure.adventurephase")),
            ],
            options={"ordering": ["order"], "unique_together": {("chapter", "slug")}},
        ),

        # ── 3. UserCharacterMet ───────────────────────────────────────────────
        migrations.CreateModel(
            name="UserCharacterMet",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("met_at", models.DateTimeField(auto_now_add=True)),
                ("character", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="met_by", to="adventure.adventurecharacter")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="characters_met", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["met_at"], "unique_together": {("user", "character")}},
        ),

        # ── 4. AdventureItem ──────────────────────────────────────────────────
        migrations.CreateModel(
            name="AdventureItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(max_length=80)),
                ("emoji", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=120)),
                ("lore", models.TextField()),
                ("rarity", models.CharField(
                    choices=[("comum", "Comum"), ("raro", "Raro"), ("epico", "Épico"), ("lendario", "Lendário")],
                    default="comum", max_length=10,
                )),
                ("action", models.CharField(
                    choices=[("examinar", "Examinar"), ("entregar", "Entregar"), ("usar", "Usar"), ("equipar", "Equipar")],
                    default="examinar", max_length=10,
                )),
                ("order", models.PositiveIntegerField(default=1)),
                ("chapter", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="items", to="adventure.adventurechapter")),
                ("source_character", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="given_items", to="adventure.adventurecharacter")),
                ("source_phase", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="reward_items", to="adventure.adventurephase")),
            ],
            options={"ordering": ["order"], "unique_together": {("chapter", "slug")}},
        ),

        # ── 5. UserInventoryItem ──────────────────────────────────────────────
        migrations.CreateModel(
            name="UserInventoryItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("earned_at", models.DateTimeField(auto_now_add=True)),
                ("is_used", models.BooleanField(default=False)),
                ("used_at", models.DateTimeField(blank=True, null=True)),
                ("item", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="owned_by", to="adventure.adventureitem")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="inventory", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["earned_at"], "unique_together": {("user", "item")}},
        ),

        # ── 6. AdventureSectionProgress ───────────────────────────────────────
        migrations.CreateModel(
            name="AdventureSectionProgress",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("completed_sections", models.PositiveSmallIntegerField(default=0)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("phase", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="section_progress", to="adventure.adventurephase")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="section_progress", to=settings.AUTH_USER_MODEL)),
            ],
            options={"unique_together": {("user", "phase")}},
        ),
    ]
