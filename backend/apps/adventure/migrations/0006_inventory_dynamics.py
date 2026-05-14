"""
Migração 0006 — Dinâmica de itens viva.

Adiciona:
  · AdventureItem.item_tag (comida/bebida/arma/documento/moneda/remedio/comum)
  · AdventureItem.is_degraded (versão fallback de uma palavra errada cronicamente)
  · AdventureItem.degrades_to (FK self — qual item este substitui)
  · AdventurePhase.has_chest (esta fase abre baú ao concluir?)
  · AdventurePhase.chest_tier (qual tier de baú: comum/raro/epico/lendario/mitico)
  · UserItemQueue (fila embaralhada por usuário+tier, garante coleção sem repetir)

Sem dados — só estrutura. Seeds adicionam tags/tiers nos itens existentes.
"""
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adventure", "0005_adventurecharacter_description"),
    ]

    operations = [
        # ── AdventureItem — tag + degradação ─────────────────────────────────
        migrations.AddField(
            model_name="adventureitem",
            name="item_tag",
            field=models.CharField(
                max_length=20,
                blank=True,
                default="",
                help_text="comida/bebida/arma/documento/moneda/remedio/comum — usado por item_moment",
            ),
        ),
        migrations.AddField(
            model_name="adventureitem",
            name="is_degraded",
            field=models.BooleanField(
                default=False,
                help_text="Versão fallback — gerada automaticamente quando palavra erra 5x+",
            ),
        ),
        migrations.AddField(
            model_name="adventureitem",
            name="degrades_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.SET_NULL,
                related_name="degraded_versions",
                to="adventure.adventureitem",
                help_text="Item pleno que este (degradado) substitui temporariamente",
            ),
        ),

        # ── AdventurePhase — baús ────────────────────────────────────────────
        migrations.AddField(
            model_name="adventurephase",
            name="has_chest",
            field=models.BooleanField(
                default=False,
                help_text="Esta fase entrega um item de baú ao concluir (sorteado da fila do user)",
            ),
        ),
        migrations.AddField(
            model_name="adventurephase",
            name="chest_tier",
            field=models.CharField(
                max_length=10,
                blank=True,
                default="",
                choices=[
                    ("comum",    "Comum"),
                    ("raro",     "Raro"),
                    ("epico",    "Épico"),
                    ("lendario", "Lendário"),
                    ("mitico",   "Mítico"),
                ],
                help_text="Tier do baú desta fase — ignorado se has_chest=False",
            ),
        ),

        # ── UserItemQueue — fila embaralhada por usuário ─────────────────────
        migrations.CreateModel(
            name="UserItemQueue",
            fields=[
                ("id", models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name="ID",
                )),
                ("tier", models.CharField(
                    max_length=10,
                    choices=[
                        ("comum",    "Comum"),
                        ("raro",     "Raro"),
                        ("epico",    "Épico"),
                        ("lendario", "Lendário"),
                        ("mitico",   "Mítico"),
                    ],
                )),
                ("ordered_item_ids", models.JSONField(
                    default=list,
                    help_text="Lista de item IDs em ordem embaralhada (uma vez por user+tier)",
                )),
                ("next_index", models.PositiveIntegerField(
                    default=0,
                    help_text="Próximo índice da fila a entregar",
                )),
                ("chapter", models.ForeignKey(
                    on_delete=models.CASCADE,
                    related_name="user_queues",
                    to="adventure.adventurechapter",
                )),
                ("user", models.ForeignKey(
                    on_delete=models.CASCADE,
                    related_name="item_queues",
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={
                "unique_together": {("user", "chapter", "tier")},
            },
        ),
    ]
