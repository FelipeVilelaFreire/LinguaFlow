from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0002_user_goal_completion"),
    ]

    operations = [
        migrations.AddField(
            model_name="goal",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
