from django.db import migrations, models
import django.db.models.deletion


def assign_existing_completions(apps, schema_editor):
    Goal = apps.get_model("content", "Goal")
    StudyDayCompletion = apps.get_model("content", "StudyDayCompletion")
    for completion in StudyDayCompletion.objects.filter(goal__isnull=True).select_related("user"):
        goal = Goal.objects.filter(user=completion.user, is_active=True).first() or Goal.objects.filter(user=completion.user).order_by("-id").first()
        if goal:
            completion.goal = goal
            completion.save(update_fields=["goal"])


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0005_goal_study_routine"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="studydaycompletion",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="studydaycompletion",
            name="goal",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="completions", to="content.goal"),
        ),
        migrations.RunPython(assign_existing_completions, migrations.RunPython.noop),
        migrations.AlterUniqueTogether(
            name="studydaycompletion",
            unique_together={("user", "study_day", "goal")},
        ),
    ]
