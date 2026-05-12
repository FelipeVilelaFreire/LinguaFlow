import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learning", "0002_language_is_ready"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudyModule",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("lang_code", models.CharField(max_length=2)),
                ("title", models.CharField(max_length=120)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"db_table": "content_study_module", "ordering": ["order"]},
        ),
        migrations.AddField(
            model_name="scenario",
            name="module",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="scenarios",
                to="learning.studymodule",
            ),
        ),
        migrations.AddField(
            model_name="scenario",
            name="adventure_phase",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="scenario",
            name="order",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
