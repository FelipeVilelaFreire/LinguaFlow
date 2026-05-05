from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("goals", "0001_initial"),
        ("learning", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Favorite",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("phrase", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="favorite_entries", to="learning.phrase")),
                ("user", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "content_favorite", "unique_together": {("user", "phrase")}},
        ),
        migrations.CreateModel(
            name="StudyDayCompletion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("completed_at", models.DateTimeField(auto_now_add=True)),
                ("goal", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="completions", to="goals.goal")),
                ("study_day", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="completions", to="learning.studyday")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "content_studydaycompletion", "ordering": ["-completed_at"], "unique_together": {("user", "study_day", "goal")}},
        ),
        migrations.CreateModel(
            name="UserProgress",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(choices=[("new", "New"), ("learning", "Learning"), ("mastered", "Mastered")], default="new", max_length=16)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("phrase", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="progress_entries", to="learning.phrase")),
                ("user", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "content_userprogress", "unique_together": {("user", "phrase")}},
        ),
    ]
