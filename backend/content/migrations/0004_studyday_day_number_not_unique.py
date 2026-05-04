from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0003_goal_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studyday",
            name="day_number",
            field=models.PositiveIntegerField(),
        ),
    ]
