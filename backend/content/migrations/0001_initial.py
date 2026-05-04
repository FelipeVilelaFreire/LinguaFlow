from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("code", models.CharField(max_length=2, unique=True)), ("name", models.CharField(max_length=80))],
        ),
        migrations.CreateModel(
            name="Scenario",
            fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("slug", models.SlugField(unique=True)), ("title", models.CharField(max_length=120)), ("description", models.TextField(blank=True))],
        ),
        migrations.CreateModel(
            name="Goal",
            fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("target_level", models.CharField(default="A1", max_length=8)), ("duration_days", models.PositiveIntegerField(default=90)), ("start_date", models.DateField(auto_now_add=True)), ("total_phrases", models.PositiveIntegerField(default=300)), ("learned_phrases", models.PositiveIntegerField(default=0)), ("completed_lessons", models.PositiveIntegerField(default=0)), ("streak_days", models.PositiveIntegerField(default=0)), ("source_language", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="source_goals", to="content.language")), ("target_language", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="target_goals", to="content.language"))],
        ),
        migrations.CreateModel(
            name="Phrase",
            fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("source_text", models.CharField(max_length=255)), ("target_text", models.CharField(max_length=255)), ("category", models.CharField(blank=True, max_length=80)), ("difficulty", models.CharField(default="A1", max_length=8)), ("created_at", models.DateTimeField(auto_now_add=True)), ("scenario", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="phrases", to="content.scenario")), ("source_language", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="source_phrases", to="content.language")), ("target_language", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="target_phrases", to="content.language"))],
            options={"unique_together": {("source_language", "target_language", "source_text", "target_text")}},
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("title", models.CharField(max_length=140)), ("day_number", models.PositiveIntegerField(default=1)), ("video_title", models.CharField(blank=True, max_length=140)), ("video_url", models.URLField(blank=True)), ("video_duration", models.CharField(blank=True, max_length=30)), ("phrases", models.ManyToManyField(related_name="lessons", to="content.phrase")), ("scenario", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="lessons", to="content.scenario"))],
            options={"ordering": ["day_number", "id"]},
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("created_at", models.DateTimeField(auto_now_add=True)), ("phrase", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="favorite_entries", to="content.phrase")), ("user", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL))],
            options={"unique_together": {("user", "phrase")}},
        ),
        migrations.CreateModel(
            name="StudyDay",
            fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("day_number", models.PositiveIntegerField(unique=True)), ("is_active", models.BooleanField(default=True)), ("lesson", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="study_days", to="content.lesson"))],
            options={"ordering": ["day_number"]},
        ),
        migrations.CreateModel(
            name="UserProgress",
            fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("status", models.CharField(choices=[("new", "New"), ("learning", "Learning"), ("mastered", "Mastered")], default="new", max_length=16)), ("updated_at", models.DateTimeField(auto_now=True)), ("phrase", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="progress_entries", to="content.phrase")), ("user", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL))],
            options={"unique_together": {("user", "phrase")}},
        ),
    ]
