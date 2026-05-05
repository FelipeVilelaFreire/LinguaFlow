from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goals", "0002_ensure_legacy_goal_columns"),
    ]

    operations = [
        migrations.AddField(
            model_name="goal",
            name="current_level",
            field=models.CharField(default="NONE", max_length=8),
        ),
    ]
