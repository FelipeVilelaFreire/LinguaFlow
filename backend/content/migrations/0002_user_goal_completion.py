from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="goal",
            name="user",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name="StudyDayCompletion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("completed_at", models.DateTimeField(auto_now_add=True)),
                ("study_day", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="completions", to="content.studyday")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "ordering": ["-completed_at"],
                "unique_together": {("user", "study_day")},
            },
        ),
    ]
