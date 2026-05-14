"""
Migração 0007 — Rastreamento de erro em WordMastery.

Adiciona:
  · error_count  — total acumulado de erros nesta palavra (não streak)
  · ever_correct — True assim que a palavra é acertada pela primeira vez

Usado pela degradação automática de itens: palavra errada 5x+ SEM nunca
ter sido acertada → libera versão degradada do item ligado a ela.
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("progress", "0006_useradventureflag"),
    ]

    operations = [
        migrations.AddField(
            model_name="wordmastery",
            name="error_count",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Total acumulado de erros nesta palavra (não reinicia como o streak)",
            ),
        ),
        migrations.AddField(
            model_name="wordmastery",
            name="ever_correct",
            field=models.BooleanField(
                default=False,
                help_text="True após o primeiro acerto — usado pela degradação de itens",
            ),
        ),
    ]
