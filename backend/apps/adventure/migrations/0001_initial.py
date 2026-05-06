from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("learning", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdventureChapter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(unique=True)),
                ("level", models.CharField(max_length=8)),
                ("order", models.PositiveIntegerField(default=1)),
                ("title", models.CharField(max_length=140)),
                ("subtitle", models.CharField(blank=True, max_length=200)),
                ("background", models.CharField(default="default", max_length=60)),
                ("boss_name", models.CharField(max_length=120)),
                ("boss_intro", models.TextField(blank=True)),
                ("reward_name", models.CharField(max_length=120)),
                ("reward_description", models.TextField(blank=True)),
                ("language", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="adventure_chapters", to="learning.language")),
            ],
            options={"ordering": ["order"]},
        ),
        migrations.CreateModel(
            name="AdventurePhase",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.PositiveIntegerField()),
                ("title", models.CharField(max_length=140)),
                ("narrative_intro", models.TextField()),
                ("narrative_outro", models.TextField()),
                ("key_words", models.JSONField(default=list)),
                ("scenario_slug", models.CharField(max_length=60)),
                ("phrase_count", models.PositiveIntegerField(default=6)),
                ("is_boss", models.BooleanField(default=False)),
                ("chapter", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="phases", to="adventure.adventurechapter")),
            ],
            options={"ordering": ["number"], "unique_together": {("chapter", "number")}},
        ),
        migrations.CreateModel(
            name="AdventureProgress",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("current_phase", models.PositiveIntegerField(default=1)),
                ("reward_unlocked", models.BooleanField(default=False)),
                ("started_at", models.DateTimeField(auto_now_add=True)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                ("chapter", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="progress_entries", to="adventure.adventurechapter")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="adventure_progress", to=settings.AUTH_USER_MODEL)),
            ],
            options={"unique_together": {("user", "chapter")}},
        ),
        migrations.CreateModel(
            name="AdventurePhaseCompletion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("score", models.PositiveIntegerField(default=0)),
                ("completed_at", models.DateTimeField(auto_now_add=True)),
                ("phase", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="completions", to="adventure.adventurephase")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="phase_completions", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-completed_at"], "unique_together": {("user", "phase")}},
        ),
    ]
