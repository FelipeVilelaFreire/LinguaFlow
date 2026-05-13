from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adventure", "0004_adventureitem_word_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="adventurecharacter",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
    ]
