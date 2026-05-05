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
            name="Goal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("target_level", models.CharField(default="A1", max_length=8)),
                ("duration_days", models.PositiveIntegerField(default=90)),
                ("start_date", models.DateField(auto_now_add=True)),
                ("total_phrases", models.PositiveIntegerField(default=300)),
                ("learned_phrases", models.PositiveIntegerField(default=0)),
                ("completed_lessons", models.PositiveIntegerField(default=0)),
                ("streak_days", models.PositiveIntegerField(default=0)),
                ("study_weekdays", models.JSONField(default=list)),
                ("session_minutes", models.PositiveIntegerField(default=30)),
                ("is_active", models.BooleanField(default=True)),
                ("source_language", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="source_goals", to="learning.language")),
                ("target_language", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="target_goals", to="learning.language")),
                ("user", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "content_goal"},
        ),
    ]
