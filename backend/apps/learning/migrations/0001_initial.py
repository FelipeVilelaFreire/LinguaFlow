from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.CharField(max_length=2, unique=True)),
                ("name", models.CharField(max_length=80)),
            ],
            options={"db_table": "content_language"},
        ),
        migrations.CreateModel(
            name="Scenario",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(unique=True)),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
            ],
            options={"db_table": "content_scenario"},
        ),
        migrations.CreateModel(
            name="Phrase",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("source_text", models.CharField(max_length=255)),
                ("target_text", models.CharField(max_length=255)),
                ("category", models.CharField(blank=True, max_length=80)),
                ("difficulty", models.CharField(default="A1", max_length=8)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("scenario", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="phrases", to="learning.scenario")),
                ("source_language", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="source_phrases", to="learning.language")),
                ("target_language", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="target_phrases", to="learning.language")),
            ],
            options={"db_table": "content_phrase", "unique_together": {("source_language", "target_language", "source_text", "target_text")}},
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=140)),
                ("day_number", models.PositiveIntegerField(default=1)),
                ("video_title", models.CharField(blank=True, max_length=140)),
                ("video_url", models.URLField(blank=True)),
                ("video_duration", models.CharField(blank=True, max_length=30)),
                ("phrases", models.ManyToManyField(db_table="content_lesson_phrases", related_name="lessons", to="learning.phrase")),
                ("scenario", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="lessons", to="learning.scenario")),
            ],
            options={"db_table": "content_lesson", "ordering": ["day_number", "id"]},
        ),
        migrations.CreateModel(
            name="StudyDay",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("day_number", models.PositiveIntegerField()),
                ("is_active", models.BooleanField(default=True)),
                ("lesson", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="study_days", to="learning.lesson")),
            ],
            options={"db_table": "content_studyday", "ordering": ["day_number"]},
        ),
    ]
