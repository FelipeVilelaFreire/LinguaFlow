from django.db import migrations, models


def set_default_routine(apps, schema_editor):
    Goal = apps.get_model("content", "Goal")
    Goal.objects.filter(study_weekdays=[]).update(study_weekdays=[0, 1, 2, 3, 4, 5, 6], session_minutes=60)


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0004_studyday_day_number_not_unique"),
    ]

    operations = [
        migrations.AddField(
            model_name="goal",
            name="session_minutes",
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AddField(
            model_name="goal",
            name="study_weekdays",
            field=models.JSONField(default=list),
        ),
        migrations.RunPython(set_default_routine, migrations.RunPython.noop),
    ]
