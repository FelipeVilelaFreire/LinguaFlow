from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("progress", "0002_ensure_legacy_completion_goal_column"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprogress",
            name="correct_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="userprogress",
            name="incorrect_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="userprogress",
            name="interval_days",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="userprogress",
            name="review_due",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="userprogress",
            name="last_answer",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
